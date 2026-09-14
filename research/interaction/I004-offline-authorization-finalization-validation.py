import json,sqlite3,threading,tempfile,shutil
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib import request,error

class State:
    def __init__(self):
        self.records={"r1":{"version":1,"title":"Flight 101","notes":"Routine","status":"draft","finalized":False}}
        self.can_edit={"A":True,"B":True}
        self.amendments={}
        self.next_amend=1
        self.patch_count=0
S=State()
def reset():
    global S; S=State()
def etag(rid): return f'"{rid}-v{S.records[rid]["version"]}"'
def pub(rid): return {k:v for k,v in S.records[rid].items() if k!="version"}
class H(BaseHTTPRequestHandler):
    protocol_version="HTTP/1.1"
    def log_message(self,*a): pass
    def body(self):
        n=int(self.headers.get("Content-Length","0")); return json.loads(self.rfile.read(n) or b"{}")
    def j(self,status,obj,heads=None):
        b=json.dumps(obj).encode(); self.send_response(status); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(b)))
        for k,v in (heads or {}).items(): self.send_header(k,v)
        self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if self.path.startswith("/records/"):
            rid=self.path.rsplit("/",1)[-1]
            return self.j(404,{"error":"not_found"}) if rid not in S.records else self.j(200,pub(rid),{"ETag":etag(rid)})
        return self.j(404,{"error":"not_found"})
    def do_PATCH(self):
        if not self.path.startswith("/records/"): return self.j(404,{"error":"not_found"})
        rid=self.path.rsplit("/",1)[-1]; actor=self.headers.get("X-Actor"); body=self.body()
        if rid not in S.records: return self.j(404,{"error":"not_found"})
        if not S.can_edit.get(actor,False): return self.j(403,{"error":"forbidden","reason":"permission_revoked"})
        if S.records[rid]["finalized"]: return self.j(409,{"error":"conflict","reason":"record_finalized","recovery":"create_amendment"})
        if self.headers.get("If-Match")!=etag(rid): return self.j(412,{"error":"precondition_failed","current":pub(rid)},{"ETag":etag(rid)})
        for k,v in body.items():
            if k not in ("finalized","version"): S.records[rid][k]=v
        S.records[rid]["version"]+=1; S.patch_count+=1
        return self.j(200,pub(rid),{"ETag":etag(rid)})
    def do_POST(self):
        if self.path!="/amendments": return self.j(404,{"error":"not_found"})
        actor=self.headers.get("X-Actor"); body=self.body()
        if actor not in ("A","B"): return self.j(403,{"error":"forbidden"})
        parent=body.get("parent_id")
        if parent not in S.records or not S.records[parent]["finalized"]: return self.j(409,{"error":"parent_not_finalized"})
        aid=f"a{S.next_amend}"; S.next_amend+=1
        S.amendments[aid]={"id":aid,"parent_id":parent,"actor":actor,"notes":body.get("notes","")}
        return self.j(201,S.amendments[aid])

def http(method,url,obj=None,actor="A",headers=None):
    data=None if obj is None else json.dumps(obj).encode()
    h={"Content-Type":"application/json","X-Actor":actor,**(headers or {})}
    q=request.Request(url,data=data,method=method,headers=h)
    try:
        with request.urlopen(q,timeout=2) as r: return r.status,json.loads(r.read()),r.headers.get("ETag")
    except error.HTTPError as e: return e.code,json.loads(e.read()),e.headers.get("ETag")

class Outbox:
    def __init__(self,path):
        self.db=sqlite3.connect(path)
        self.db.execute("create table if not exists q(op text primary key,rid text,actor text,base text,payload text,status text)")
        self.db.commit()
    def put(self,op,rid,actor,base,payload):
        self.db.execute("insert into q values(?,?,?,?,?,'queued')",(op,rid,actor,base,json.dumps(payload))); self.db.commit()
    def get(self,op):
        r=self.db.execute("select * from q where op=?",(op,)).fetchone()
        return {"op":r[0],"rid":r[1],"actor":r[2],"base":r[3],"payload":json.loads(r[4]),"status":r[5]}
    def status(self,op,s): self.db.execute("update q set status=? where op=?",(s,op)); self.db.commit()

def run():
    A=[]; scenarios={}
    def ck(name,cond,detail=None):
        A.append({"name":name,"pass":bool(cond),"detail":detail})
        if not cond: raise AssertionError(name)
    srv=ThreadingHTTPServer(("127.0.0.1",0),H); threading.Thread(target=srv.serve_forever,daemon=True).start()
    base=f"http://127.0.0.1:{srv.server_address[1]}"; td=tempfile.mkdtemp()
    try:
        reset(); q=Outbox(td+"/p.sqlite"); _,_,e=http("GET",base+"/records/r1",actor="A"); q.put("p1","r1","A",e,{"notes":"Offline note"})
        S.can_edit["A"]=False
        row=q.get("p1"); s,b,_=http("PATCH",base+"/records/r1",row["payload"],actor=row["actor"],headers={"If-Match":row["base"]})
        ck("revoked_permission_returns_403",s==403,(s,b)); ck("403_reason_explicit",b.get("reason")=="permission_revoked",b); q.status("p1","blocked_permission")
        _,cur,ecur=http("GET",base+"/records/r1",actor="A")
        ck("permission_failure_does_not_mutate",cur["notes"]=="Routine" and ecur==e,cur)
        ck("blocked_intent_preserved",q.get("p1")["payload"]["notes"]=="Offline note" and q.get("p1")["status"]=="blocked_permission",q.get("p1"))
        scenarios["permission_revoked"]={"status":s,"queue":q.get("p1"),"current":cur}

        reset(); q=Outbox(td+"/f.sqlite"); _,_,e=http("GET",base+"/records/r1",actor="A"); q.put("f1","r1","A",e,{"notes":"Late correction"})
        S.records["r1"]["finalized"]=True; S.records["r1"]["status"]="finalized"; S.records["r1"]["version"]+=1
        row=q.get("f1"); s,b,_=http("PATCH",base+"/records/r1",row["payload"],actor="A",headers={"If-Match":row["base"]})
        ck("finalized_returns_409_before_stale_412",s==409,(s,b)); ck("finalized_reason_explicit",b.get("reason")=="record_finalized",b); q.status("f1","blocked_finalized")
        _,cur,_=http("GET",base+"/records/r1",actor="A"); ck("finalized_original_unchanged",cur["notes"]=="Routine" and cur["status"]=="finalized",cur)
        sa,ba,_=http("POST",base+"/amendments",{"parent_id":"r1","notes":row["payload"]["notes"]},actor="A")
        ck("compensating_amendment_created",sa==201 and ba["parent_id"]=="r1" and ba["notes"]=="Late correction",(sa,ba)); q.status("f1","recovered_as_amendment")
        ck("original_remains_finalized_after_amendment",S.records["r1"]["finalized"] and S.records["r1"]["notes"]=="Routine",S.records["r1"])
        scenarios["finalized"]={"patch_status":s,"amendment":ba,"queue_status":q.get("f1")["status"]}

        reset(); q=Outbox(td+"/restore.sqlite"); _,_,e=http("GET",base+"/records/r1",actor="A"); q.put("r1op","r1","A",e,{"notes":"Offline A"})
        S.can_edit["A"]=False
        row=q.get("r1op"); s,_,_=http("PATCH",base+"/records/r1",row["payload"],actor="A",headers={"If-Match":row["base"]}); ck("initial_permission_block",s==403,s)
        S.can_edit["A"]=True
        _,_,be=http("GET",base+"/records/r1",actor="B"); sb,bb,_=http("PATCH",base+"/records/r1",{"title":"Remote B"},actor="B",headers={"If-Match":be}); ck("remote_change_after_block_commits",sb==200,(sb,bb))
        s412,b412,_=http("PATCH",base+"/records/r1",row["payload"],actor="A",headers={"If-Match":row["base"]}); ck("restored_permission_still_requires_stale_detection",s412==412,(s412,b412))
        _,_,current_e=http("GET",base+"/records/r1",actor="A")
        sr,br,_=http("PATCH",base+"/records/r1",{"notes":"Offline A"},actor="A",headers={"If-Match":current_e})
        ck("revalidated_disjoint_rebase_succeeds",sr==200,(sr,br)); ck("remote_and_local_preserved_after_reauth",br["title"]=="Remote B" and br["notes"]=="Offline A",br)
        scenarios["permission_restored"]={"stale_status":s412,"final":br}

        reset(); q=Outbox(td+"/acct.sqlite"); _,_,e=http("GET",base+"/records/r1",actor="A"); q.put("a1","r1","A",e,{"notes":"A private draft"})
        row=q.get("a1"); sn,bn,_=http("PATCH",base+"/records/r1",row["payload"],actor="B",headers={"If-Match":row["base"]})
        ck("naive_account_switch_can_apply_wrong_actor_intent",sn==200 and bn["notes"]=="A private draft",(sn,bn))
        reset(); q2=Outbox(td+"/acct2.sqlite"); _,_,e2=http("GET",base+"/records/r1",actor="A"); q2.put("a2","r1","A",e2,{"notes":"A private draft"})
        active_actor="B"; r=q2.get("a2")
        if r["actor"]!=active_actor: q2.status("a2","blocked_account_mismatch")
        ck("actor_mismatch_blocks_before_send",q2.get("a2")["status"]=="blocked_account_mismatch",q2.get("a2"))
        _,cur,_=http("GET",base+"/records/r1",actor="B"); ck("blocked_account_mismatch_leaves_server_unchanged",cur["notes"]=="Routine",cur)
        ck("queued_actor_identity_preserved",q2.get("a2")["actor"]=="A",q2.get("a2"))
        scenarios["account_switch"]={"naive_applied_as_B":bn,"revised_status":q2.get("a2")["status"],"server_after_revised":cur}

        return {"passed":sum(x["pass"] for x in A),"total":len(A),"all_pass":all(x["pass"] for x in A),"assertions":A,"scenarios":scenarios}
    finally:
        srv.shutdown(); srv.server_close(); shutil.rmtree(td,ignore_errors=True)

if __name__=="__main__": print(json.dumps(run(),indent=2,ensure_ascii=False))
