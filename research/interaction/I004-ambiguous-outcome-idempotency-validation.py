import json, socket, threading, urllib.request, urllib.error, http.client
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

class State:
    def __init__(self): self.lock=threading.Lock(); self.reset()
    def reset(self):
        with getattr(self,'lock',threading.Lock()):
            self.record={'id':'r1','title':'Flight 101','notes':'Routine','version':1}; self.transfers=[]; self.op_ledger={}
    def etag(self): return f'"r1-v{self.record["version"]}"'
S=State()

class H(BaseHTTPRequestHandler):
    protocol_version='HTTP/1.1'
    def log_message(self,*a): pass
    def body(self):
        n=int(self.headers.get('Content-Length','0')); return json.loads(self.rfile.read(n) or b'{}')
    def sendj(self,status,body,headers=None):
        raw=json.dumps(body,separators=(',',':')).encode(); self.send_response(status); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(raw)))
        for k,v in (headers or {}).items(): self.send_header(k,v)
        self.end_headers(); self.wfile.write(raw)
    def drop(self):
        try: self.connection.shutdown(socket.SHUT_RDWR)
        except OSError: pass
        self.connection.close(); self.close_connection=True
    def do_GET(self):
        p=urlparse(self.path).path
        with S.lock:
            if p=='/record': return self.sendj(200,S.record,{'ETag':S.etag()})
            if p=='/transfers': return self.sendj(200,{'count':len(S.transfers),'items':S.transfers})
        return self.sendj(404,{'error':'not_found'})
    def do_PUT(self):
        p=urlparse(self.path).path; inc=self.body(); smart=p=='/record-smart'; im=self.headers.get('If-Match'); drop=self.headers.get('X-Drop-After-Apply')=='1'
        with S.lock:
            desired={'title':inc.get('title',S.record['title']),'notes':inc.get('notes',S.record['notes'])}
            if im!=S.etag():
                same=S.record['title']==desired['title'] and S.record['notes']==desired['notes']
                if smart and same: return self.sendj(200,S.record,{'ETag':S.etag(),'X-Outcome':'already-applied'})
                return self.sendj(412,{'error':'precondition_failed'},{'ETag':S.etag()})
            S.record={'id':'r1','title':desired['title'],'notes':desired['notes'],'version':S.record['version']+1}; result=dict(S.record); et=S.etag()
        if drop: return self.drop()
        return self.sendj(200,result,{'ETag':et,'X-Outcome':'applied'})
    def do_POST(self):
        if urlparse(self.path).path!='/transfers': return self.sendj(404,{'error':'not_found'})
        inc=self.body(); op=self.headers.get('X-Operation-Id'); drop=self.headers.get('X-Drop-After-Apply')=='1'; fingerprint=json.dumps({'amount':inc.get('amount'),'currency':inc.get('currency')},sort_keys=True,separators=(',',':'))
        with S.lock:
            if op and op in S.op_ledger:
                prior=S.op_ledger[op]
                if prior['fingerprint']!=fingerprint: return self.sendj(409,{'error':'operation_id_reused_with_different_payload'})
                result=prior['result']; replay=True
            else:
                result={'transferId':f't{len(S.transfers)+1}','amount':inc.get('amount'),'currency':inc.get('currency')}; S.transfers.append(result); replay=False
                if op: S.op_ledger[op]={'fingerprint':fingerprint,'result':result}
        if drop and not replay: return self.drop()
        return self.sendj(200,result,{'X-Outcome':'replayed' if replay else 'applied'})

def req(method,url,body=None,headers=None):
    data=None if body is None else json.dumps(body).encode(); h={'Accept':'application/json',**(headers or {})}
    if body is not None: h['Content-Type']='application/json'
    try:
        r=urllib.request.urlopen(urllib.request.Request(url,data=data,headers=h,method=method),timeout=3); raw=r.read(); return {'kind':'response','status':r.status,'body':json.loads(raw) if raw else None,'etag':r.headers.get('ETag'),'outcome':r.headers.get('X-Outcome')}
    except urllib.error.HTTPError as e:
        raw=e.read(); return {'kind':'response','status':e.code,'body':json.loads(raw) if raw else None,'etag':e.headers.get('ETag'),'outcome':e.headers.get('X-Outcome')}
    except (urllib.error.URLError,http.client.RemoteDisconnected,ConnectionResetError,BrokenPipeError) as e:
        return {'kind':'outcome_unknown','error':type(e).__name__+': '+str(e)}

def free_port():
    s=socket.socket(); s.bind(('127.0.0.1',0)); p=s.getsockname()[1]; s.close(); return p
checks=[]
def ck(name,cond): checks.append({'name':name,'pass':bool(cond)})

def run():
    port=free_port(); srv=ThreadingHTTPServer(('127.0.0.1',port),H); threading.Thread(target=srv.serve_forever,daemon=True).start(); b=f'http://127.0.0.1:{port}'
    try:
        S.reset(); base=req('GET',b+'/record'); desired={**base['body'],'notes':'Weather diversion'}; first=req('PUT',b+'/record-strict',desired,{'If-Match':base['etag'],'X-Drop-After-Apply':'1'}); ck('S1 lost response becomes outcome unknown, not known failure',first['kind']=='outcome_unknown'); after=req('GET',b+'/record'); ck('S1 server actually applied first PUT once',after['body']['notes']=='Weather diversion' and after['body']['version']==2); retry=req('PUT',b+'/record-strict',desired,{'If-Match':base['etag']}); ck('S1 naive stale retry returns 412',retry['status']==412); ck('S1 strict 412 alone cannot distinguish own prior success from external conflict',retry['status']==412 and after['body']['notes']==desired['notes'])
        S.reset(); base=req('GET',b+'/record'); desired={**base['body'],'notes':'Weather diversion'}; first=req('PUT',b+'/record-smart',desired,{'If-Match':base['etag'],'X-Drop-After-Apply':'1'}); after1=req('GET',b+'/record'); retry=req('PUT',b+'/record-smart',desired,{'If-Match':base['etag']}); after2=req('GET',b+'/record'); ck('S2 smart first response is outcome unknown',first['kind']=='outcome_unknown'); ck('S2 retry confirms already-applied outcome',retry['status']==200 and retry['outcome']=='already-applied' and retry['body']['version']==2); ck('S2 confirmation does not create duplicate PUT effect/version',after1['body']['version']==2 and after2['body']['version']==2)
        S.reset(); payload={'amount':100,'currency':'USD'}; first=req('POST',b+'/transfers',payload,{'X-Drop-After-Apply':'1'}); mid=req('GET',b+'/transfers'); retry=req('POST',b+'/transfers',payload); final=req('GET',b+'/transfers'); ck('S3 POST response loss is outcome unknown',first['kind']=='outcome_unknown'); ck('S3 first POST side effect actually happened',mid['body']['count']==1); ck('S3 blind POST retry duplicates side effect',final['body']['count']==2 and retry['body']['transferId']=='t2')
        S.reset(); op='transfer-op-123'; first=req('POST',b+'/transfers',payload,{'X-Operation-Id':op,'X-Drop-After-Apply':'1'}); mid=req('GET',b+'/transfers'); retry=req('POST',b+'/transfers',payload,{'X-Operation-Id':op}); final=req('GET',b+'/transfers'); ck('S4 keyed POST first response remains outcome unknown',first['kind']=='outcome_unknown'); ck('S4 keyed POST first effect occurred exactly once',mid['body']['count']==1); ck('S4 same operation identity replays original result',retry['status']==200 and retry['outcome']=='replayed' and retry['body']['transferId']=='t1'); ck('S4 keyed retry does not duplicate side effect',final['body']['count']==1); bad=req('POST',b+'/transfers',{'amount':200,'currency':'USD'},{'X-Operation-Id':op}); ck('S4 operation identity reuse with different payload is rejected',bad['status']==409)
    finally: srv.shutdown(); srv.server_close()
    return {'summary':{'passed':sum(x['pass'] for x in checks),'total':len(checks),'all_pass':all(x['pass'] for x in checks)},'assertions':checks}

if __name__=='__main__': print(json.dumps(run(),indent=2))
