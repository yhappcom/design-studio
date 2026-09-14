import hashlib, http.client, json, socket, threading, time, uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

S={"effects":[],"keys":{},"processing":set(),"drop_next":False,"slow_next":False}
LOCK=threading.Lock()

def enc(x): return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def fp(b): return hashlib.sha256(b).hexdigest()

class Handler(BaseHTTPRequestHandler):
    protocol_version="HTTP/1.1"
    def log_message(self,*a): pass
    def reply(self,status,obj,extra=None):
        b=enc(obj); self.send_response(status); self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(b)))
        for k,v in (extra or {}).items(): self.send_header(k,v)
        self.end_headers(); self.wfile.write(b)
    def do_POST(self):
        if self.path!="/effects": self.reply(404,{"error":"not_found"}); return
        n=int(self.headers.get("Content-Length","0")); body=self.rfile.read(n)
        key=self.headers.get("Idempotency-Key"); f=fp(body); payload=json.loads(body)
        if key:
            with LOCK:
                if key in S["processing"]:
                    self.reply(409,{"error":"outstanding"}); return
                if key in S["keys"]:
                    old=S["keys"][key]
                    if old["fingerprint"]!=f:
                        self.reply(422,{"error":"key_reused_different_payload"}); return
                    self.reply(old["status"],old["result"],{"Idempotency-Replayed":"true"}); return
                S["processing"].add(key)
        if S["slow_next"]:
            S["slow_next"]=False; time.sleep(0.35)
        with LOCK:
            effect={"effect_id":f"e{len(S['effects'])+1}","amount":payload["amount"]}
            S["effects"].append(effect)
            if key:
                S["keys"][key]={"fingerprint":f,"status":201,"result":effect}
                S["processing"].discard(key)
        if S["drop_next"]:
            S["drop_next"]=False; self.close_connection=True
            try:self.connection.shutdown(socket.SHUT_RDWR)
            except OSError:pass
            self.connection.close(); return
        self.reply(201,effect)

def request(port,payload,key=None,timeout=2):
    c=http.client.HTTPConnection("127.0.0.1",port,timeout=timeout); body=enc(payload)
    h={"Content-Type":"application/json","Content-Length":str(len(body))}
    if key:h["Idempotency-Key"]=key
    try:
        c.request("POST","/effects",body,h); r=c.getresponse(); raw=r.read()
        return {"status":r.status,"body":json.loads(raw),"replayed":r.getheader("Idempotency-Replayed")}
    except Exception as e:return {"transport_error":type(e).__name__}
    finally:c.close()

def reset():
    with LOCK:S["effects"].clear();S["keys"].clear();S["processing"].clear()
    S["drop_next"]=False;S["slow_next"]=False

srv=ThreadingHTTPServer(("127.0.0.1",0),Handler); port=srv.server_port
threading.Thread(target=srv.serve_forever,daemon=True).start()
checks=[]; data={}
def ck(name,cond): checks.append({"name":name,"pass":bool(cond)})

reset(); S["drop_next"]=True
a1=request(port,{"amount":100}); a2=request(port,{"amount":100})
data["naive_unknown_retry"]={"first":a1,"retry":a2,"effects":list(S["effects"])}
ck("A1 first response is transport-unknown", "transport_error" in a1)
ck("A2 first request nevertheless committed", len(S["effects"])>=1)
ck("A3 naive retry creates duplicate side effect", len(S["effects"])==2)
ck("A4 duplicate has distinct identities", len({x["effect_id"] for x in S["effects"]})==2)

reset(); key="intent-"+uuid.uuid4().hex; S["drop_next"]=True
b1=request(port,{"amount":100},key); b2=request(port,{"amount":100},key)
data["stable_key_retry"]={"key":key,"first":b1,"retry":b2,"effects":list(S["effects"])}
ck("B1 keyed first response is transport-unknown", "transport_error" in b1)
ck("B2 only one effect exists after same-key retry", len(S["effects"])==1)
ck("B3 retry returns original effect identity", b2.get("body",{}).get("effect_id")=="e1")
ck("B4 replay is explicitly detectable in harness", b2.get("replayed")=="true")

reset(); k1="intent-"+uuid.uuid4().hex; k2="intent-"+uuid.uuid4().hex; S["drop_next"]=True
c1=request(port,{"amount":100},k1); c2=request(port,{"amount":100},k2)
data["fresh_key_retry_bug"]={"first_key":k1,"retry_key":k2,"first":c1,"retry":c2,"effects":list(S["effects"])}
ck("C1 first result unknown", "transport_error" in c1)
ck("C2 fresh retry key duplicates original intent", len(S["effects"])==2)

reset(); k="intent-"+uuid.uuid4().hex
d1=request(port,{"amount":100},k); d2=request(port,{"amount":200},k)
data["payload_mismatch"]={"first":d1,"reuse":d2,"effects":list(S["effects"])}
ck("D1 first keyed request committed", d1.get("status")==201 and len(S["effects"])==1)
ck("D2 same key different payload rejected", d2.get("status")==422)
ck("D3 rejected reuse creates no second effect", len(S["effects"])==1)

reset(); k="intent-"+uuid.uuid4().hex; S["slow_next"]=True
holder={}
t=threading.Thread(target=lambda: holder.setdefault("first",request(port,{"amount":300},k)),daemon=True); t.start()
deadline=time.time()+1
while k not in S["processing"] and time.time()<deadline: time.sleep(.005)
e2=request(port,{"amount":300},k); t.join(); e3=request(port,{"amount":300},k)
data["concurrent_duplicate"]={"first":holder.get("first"),"concurrent":e2,"after_complete":e3,"effects":list(S["effects"])}
ck("E1 concurrent same-key request is not processed twice", e2.get("status")==409)
ck("E2 original eventually commits once", holder.get("first",{}).get("status")==201 and len(S["effects"])==1)
ck("E3 later retry replays completed result", e3.get("status")==201 and e3.get("replayed")=="true")
ck("E4 later replay keeps original identity", e3.get("body",{}).get("effect_id")=="e1")

ck("F1 ambiguous transport result maps to outcome_unknown, not safe failure", "transport_error" in b1 and len(data["stable_key_retry"]["effects"])==1)

summary={"environment":{"protocol":"HTTP/1.1","server":"Python ThreadingHTTPServer","client":"http.client"},
         "assertions":{"passed":sum(x["pass"] for x in checks),"total":len(checks),"details":checks},
         "scenarios":data,
         "notes":["Idempotency-Key draft-07 is expired work-in-progress, not an RFC.","Harness uses its key/fingerprint/replay/conflict pattern as bounded practice, not a standards-conformance claim."]}
print(json.dumps(summary,indent=2))
open("I005-ambiguous-outcome-idempotency-results.json","w").write(json.dumps(summary,indent=2))
srv.shutdown()
