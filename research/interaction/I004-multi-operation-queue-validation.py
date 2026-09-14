import json,sqlite3,threading,tempfile,shutil
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib import request,error

R={"r1":{"version":1,"title":"Flight 101","notes":"Routine","landings":0,"events":[],"status":"draft"},
   "r2":{"version":1,"title":"Independent","notes":"Base","landings":0,"events":[],"status":"draft"}}
NEXT=3
def reset():
    global R,NEXT
    R={"r1":{"version":1,"title":"Flight 101","notes":"Routine","landings":0,"events":[],"status":"draft"},
       "r2":{"version":1,"title":"Independent","notes":"Base","landings":0,"events":[],"status":"draft"}}
    NEXT=3
def etag(rid): return None if rid not in R else f'"{rid}-v{R[rid]["version"]}"'
def pub(rid): return None if rid not in R else {k:v for k,v in R[rid].items() if k!="version"}
def apply(rec,ops):
    x={k:(list(v) if isinstance(v,list) else v) for k,v in rec.items()}
    for o in ops:
        if o["kind"]=="replace": x[o["field"]]=o["value"]
        elif o["kind"]=="inc": x[o["field"]]=x.get(o["field"],0)+o["delta"]
        elif o["kind"]=="append": x[o["field"]]=list(x.get(o["field"],[]))+[o["value"]]
    return x
class H(BaseHTTPRequestHandler):
    protocol_version="HTTP/1.1"
    def log_message(self,*a): pass
    def j(self,s,o,h=None):
        b=json.dumps(o).encode(); self.send_response(s); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(b)))
        for k,v in (h or {}).items(): self.send_header(k,v)
        self.end_headers(); self.wfile.write(b)
    def body(self): return json.loads(self.rfile.read(int(self.headers.get("Content-Length","0"))) or b"{}")
    def do_GET(self):
        rid=self.path.rsplit("/",1)[-1]
        self.j(404,{"error":"not_found"}) if rid not in R else self.j(200,pub(rid),{"ETag":etag(rid)})
    def do_PATCH(self):
        rid=self.path.rsplit("/",1)[-1]; b=self.body()
        if rid not in R: return self.j(404,{"error":"not_found"})
        if self.headers.get("If-Match")!=etag(rid): return self.j(412,{"error":"precondition_failed","current":pub(rid)},{"ETag":etag(rid)})
        x=apply(R[rid],b["ops"]); x["version"]=R[rid]["version"]+1; R[rid]=x; self.j(200,pub(rid),{"ETag":etag(rid)})
    def do_POST(self):
        global NEXT
        if self.path!="/records": return self.j(404,{"error":"not_found"})
        b=self.body(); rid=f"r{NEXT}"; NEXT+=1
        R[rid]={"version":1,**b}; [R[rid].setdefault(k,v) for k,v in {"notes":"","landings":0,"events":[],"status":"draft"}.items()]
        self.j(201,{"id":rid,**pub(rid)},{"ETag":etag(rid)})
def http(m,u,o=None,h=None):
    q=request.Request(u,data=None if o is None else json.dumps(o).encode(),method=m,headers={"Content-Type":"application/json",**(h or {})})
    try:
        with request.urlopen(q,timeout=2) as r: return r.status,json.loads(r.read()),r.headers.get("ETag")
    except error.HTTPError as e: return e.code,json.loads(e.read()),e.headers.get("ETag")
class Q:
    def __init__(self,p):
        self.d=sqlite3.connect(p); self.d.execute("create table if not exists q(seq integer primary key autoincrement,op text unique,rid text,base text,ops text,dep text,status text,temp text)"); self.d.execute("create table if not exists map(temp text primary key,server text)"); self.d.commit()
    def add(self,op,rid,base,ops,dep=None,temp=None): self.d.execute("insert into q(op,rid,base,ops,dep,status,temp) values(?,?,?,?,?,'queued',?)",(op,rid,base,json.dumps(ops),dep,temp)); self.d.commit()
    def rows(self):
        return [{"seq":r[0],"op":r[1],"rid":r[2],"base":r[3],"ops":json.loads(r[4]),"dep":r[5],"status":r[6],"temp":r[7]} for r in self.d.execute("select * from q order by seq")]
    def st(self,op,s): self.d.execute("update q set status=? where op=?",(s,op)); self.d.commit()
    def target(self,op,rid,base): self.d.execute("update q set rid=?,base=? where op=?",(rid,base,op)); self.d.commit()
    def map(self,t,s): self.d.execute("insert or replace into map values(?,?)",(t,s)); self.d.commit()
    def mapped(self,t): return self.d.execute("select server from map where temp=?",(t,)).fetchone()[0]
def run():
    A=[]
    def ck(n,c,d=None): A.append({"name":n,"pass":bool(c),"detail":d}); assert c,n
    srv=ThreadingHTTPServer(("127.0.0.1",0),H); threading.Thread(target=srv.serve_forever,daemon=True).start(); b=f"http://127.0.0.1:{srv.server_address[1]}"; td=tempfile.mkdtemp()
    try:
        reset(); _,_,e=http("GET",b+"/records/r1"); ops=[{"kind":"append","field":"events","value":"departed"},{"kind":"append","field":"events","value":"arrived"}]; s,x,_=http("PATCH",b+"/records/r1",{"ops":ops},{"If-Match":e}); ck("ordered_patch_200",s==200,s); ck("ordered_events_preserved",x["events"]==["departed","arrived"],x["events"])
        reset(); _,_,e=http("GET",b+"/records/r1"); s,y,_=http("PATCH",b+"/records/r1",{"ops":list(reversed(ops))},{"If-Match":e}); ck("reversed_patch_200",s==200,s); ck("reorder_changes_semantics",y["events"]==["arrived","departed"],y["events"])
        reset(); _,_,e=http("GET",b+"/records/r1"); reps=[{"kind":"replace","field":"title","value":"Flight 101A"},{"kind":"replace","field":"title","value":"Flight 101B"}]; _,a,_=http("PATCH",b+"/records/r1",{"ops":reps},{"If-Match":e}); reset(); _,_,e=http("GET",b+"/records/r1"); _,c,_=http("PATCH",b+"/records/r1",{"ops":[reps[-1]]},{"If-Match":e}); ck("replace_compaction_same_final",a["title"]==c["title"]=="Flight 101B")
        inc=[{"kind":"inc","field":"landings","delta":1}]*2; reset(); _,_,e=http("GET",b+"/records/r1"); _,sq,_=http("PATCH",b+"/records/r1",{"ops":inc},{"If-Match":e}); reset(); _,_,e=http("GET",b+"/records/r1"); _,nv,_=http("PATCH",b+"/records/r1",{"ops":[inc[-1]]},{"If-Match":e}); reset(); _,_,e=http("GET",b+"/records/r1"); _,sm,_=http("PATCH",b+"/records/r1",{"ops":[{"kind":"inc","field":"landings","delta":2}]},{"If-Match":e}); ck("naive_path_dedupe_loses_increment",sq["landings"]==2 and nv["landings"]==1); ck("semantic_increment_compaction_preserves_intent",sm["landings"]==2)
        reset(); q=Q(td+"/q.sqlite"); _,_,e1=http("GET",b+"/records/r1"); _,_,e2=http("GET",b+"/records/r2"); q.add("q1","r1",e1,[{"kind":"replace","field":"notes","value":"Weather diversion"}]); q.add("q2","r1",None,[{"kind":"replace","field":"title","value":"Flight 101B"}],"q1"); q.add("q3","r2",e2,[{"kind":"replace","field":"notes","value":"Independent queued"}]); q.add("q4","r1",None,[{"kind":"replace","field":"status","value":"ready"}],"q2")
        r=q.rows()[0]; s,_,ne=http("PATCH",b+"/records/r1",{"ops":r["ops"]},{"If-Match":r["base"]}); ck("q1_commits",s==200,s); q.st("q1","confirmed"); q.target("q2","r1",ne); sr,_,_=http("PATCH",b+"/records/r1",{"ops":[{"kind":"replace","field":"title","value":"Remote title"}]},{"If-Match":ne}); ck("remote_race_commits",sr==200,sr); r=[z for z in q.rows() if z["op"]=="q2"][0]; s,_,_=http("PATCH",b+"/records/r1",{"ops":r["ops"]},{"If-Match":r["base"]}); ck("q2_detects_412",s==412,s); q.st("q2","conflict_same_field"); q.st("q4","blocked_dependency"); r=[z for z in q.rows() if z["op"]=="q3"][0]; s,_,_=http("PATCH",b+"/records/r2",{"ops":r["ops"]},{"If-Match":r["base"]}); ck("independent_q3_continues",s==200,s); q.st("q3","confirmed"); st={z["op"]:z["status"] for z in q.rows()}; ck("dependent_descendant_blocked",st["q4"]=="blocked_dependency",st); ck("conflict_does_not_freeze_whole_queue",st["q3"]=="confirmed",st); _,r1,_=http("GET",b+"/records/r1"); _,r2,_=http("GET",b+"/records/r2"); ck("conflicting_title_not_overwritten",r1["title"]=="Remote title",r1); ck("independent_record_updated",r2["notes"]=="Independent queued",r2)
        reset(); s,_,_=http("PATCH",b+"/records/temp-1",{"ops":[{"kind":"replace","field":"notes","value":"Added offline"}]},{"If-Match":'"temp-1-v0"'}); ck("edit_before_create_fails",s==404,s); q2=Q(td+"/q2.sqlite"); q2.add("c1","temp-1",None,[],temp="temp-1"); q2.add("c2","temp-1",None,[{"kind":"replace","field":"notes","value":"Added offline"}],"c1"); s,x,e=http("POST",b+"/records",{"title":"Offline created","notes":""}); ck("create_returns_server_identity",s==201 and x["id"].startswith("r"),x); rid=x["id"]; q2.map("temp-1",rid); q2.st("c1","confirmed"); q2.target("c2",rid,e); r=[z for z in q2.rows() if z["op"]=="c2"][0]; s,_,_=http("PATCH",b+"/records/"+rid,{"ops":r["ops"]},{"If-Match":r["base"]}); ck("dependent_edit_after_mapping_succeeds",s==200,s); q2.st("c2","confirmed"); _,f,_=http("GET",b+"/records/"+rid); ck("created_record_contains_dependent_edit",f["title"]=="Offline created" and f["notes"]=="Added offline",f); ck("temp_identity_mapping_persisted",q2.mapped("temp-1")==rid,rid)
        return {"passed":sum(x["pass"] for x in A),"total":len(A),"all_pass":all(x["pass"] for x in A),"assertions":A}
    finally: srv.shutdown(); srv.server_close(); shutil.rmtree(td,ignore_errors=True)
if __name__=="__main__": print(json.dumps(run(),indent=2))
