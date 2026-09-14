from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from threading import Thread, Lock
import json
from pathlib import Path

class Store:
    def __init__(self):
        self.lock=Lock(); self.reset()
    def reset(self):
        with getattr(self,'lock',Lock()):
            self.records={'r1':{'id':'r1','title':'Flight 101','notes':'Routine','version':1}}
    def etag(self, rec): return f'"{rec["id"]}-v{rec["version"]}"'
store=Store()

class H(BaseHTTPRequestHandler):
    server_version='I004Lab/1.0'
    protocol_version='HTTP/1.1'
    def log_message(self,*args): pass
    def body(self):
        n=int(self.headers.get('Content-Length','0')); raw=self.rfile.read(n) if n else b''
        return json.loads(raw.decode()) if raw else None
    def sendj(self,status,obj=None,headers=None):
        data=b'' if obj is None else json.dumps(obj,ensure_ascii=False,separators=(',',':')).encode()
        self.send_response(status)
        for k,v in (headers or {}).items(): self.send_header(k,v)
        if data:self.send_header('Content-Type','application/json; charset=utf-8')
        self.send_header('Content-Length',str(len(data))); self.send_header('Connection','close'); self.end_headers()
        if data:self.wfile.write(data)
    def rec_id(self):
        p=self.path.split('?')[0].strip('/').split('/')
        return p[1] if len(p)==2 and p[0]=='records' else None
    def do_GET(self):
        rid=self.rec_id()
        if rid is None:return self.sendj(404,{'error':'not_found'})
        with store.lock:
            rec=store.records.get(rid)
            if not rec:return self.sendj(404,{'error':'not_found'})
            self.sendj(200,rec,{'ETag':store.etag(rec),'Cache-Control':'no-store'})
    def do_PUT(self):
        rid=self.rec_id(); payload=self.body() or {}
        if rid is None:return self.sendj(404,{'error':'not_found'})
        with store.lock:
            rec=store.records.get(rid); if_match=self.headers.get('If-Match'); if_none=self.headers.get('If-None-Match')
            if if_none=='*':
                if rec is not None:return self.sendj(412,{'error':'precondition_failed','reason':'already_exists'},{'ETag':store.etag(rec)})
                new={'id':rid,'title':payload.get('title',''),'notes':payload.get('notes',''),'version':1}; store.records[rid]=new
                return self.sendj(201,new,{'ETag':store.etag(new),'Location':f'/records/{rid}'})
            if rec is None:
                if if_match is not None:return self.sendj(412,{'error':'precondition_failed','reason':'missing_current'})
                return self.sendj(404,{'error':'not_found'})
            current=store.etag(rec)
            if if_match is not None and if_match!=current:
                return self.sendj(412,{'error':'precondition_failed','current':rec.copy()},{'ETag':current})
            new={'id':rid,'title':payload.get('title',rec['title']),'notes':payload.get('notes',rec['notes']),'version':rec['version']+1}; store.records[rid]=new
            return self.sendj(200,new,{'ETag':store.etag(new)})
    def do_DELETE(self):
        rid=self.rec_id()
        if rid is None:return self.sendj(404,{'error':'not_found'})
        with store.lock:
            rec=store.records.get(rid)
            if rec is None:return self.sendj(404,{'error':'not_found'})
            current=store.etag(rec); if_match=self.headers.get('If-Match')
            if if_match is not None and if_match!=current:
                return self.sendj(412,{'error':'precondition_failed','current':rec.copy()},{'ETag':current})
            del store.records[rid]; self.sendj(204)

class Client:
    def __init__(self,base): self.base=base
    def req(self,method,path,body=None,headers=None):
        data=None if body is None else json.dumps(body).encode(); h={'Accept':'application/json'}; h.update(headers or {})
        if data:h['Content-Type']='application/json'
        q=Request(self.base+path,data=data,headers=h,method=method)
        try:
            with urlopen(q,timeout=2) as r:
                raw=r.read(); return {'status':r.status,'headers':dict(r.headers.items()),'body':json.loads(raw) if raw else None}
        except HTTPError as e:
            raw=e.read(); return {'status':e.code,'headers':dict(e.headers.items()),'body':json.loads(raw) if raw else None}

assertions=[]; scenarios={}
def ck(name,cond,obs=None): assertions.append({'name':name,'pass':bool(cond),'observed':obs})
def hdr(resp,name): return next((v for k,v in resp['headers'].items() if k.lower()==name.lower()),None)

srv=ThreadingHTTPServer(('127.0.0.1',0),H); port=srv.server_address[1]; t=Thread(target=srv.serve_forever,daemon=True); t.start(); c=Client(f'http://127.0.0.1:{port}')
try:
    store.reset(); A=c.req('GET','/records/r1'); B=c.req('GET','/records/r1'); et1=hdr(A,'ETag')
    a_save=c.req('PUT','/records/r1',{'title':'Flight 101A','notes':'Routine'},{'If-Match':et1})
    b_naive=c.req('PUT','/records/r1',{'title':'Flight 101','notes':'Weather diversion'}); final=c.req('GET','/records/r1')
    scenarios['naive_lost_update']={'A_get':A,'B_get':B,'A_save':a_save,'B_naive':b_naive,'final':final}
    ck('N1 initial clients observe same strong ETag',hdr(A,'ETag')==hdr(B,'ETag')=='"r1-v1"')
    ck('N2 writer A conditional update succeeds and advances ETag',a_save['status']==200 and hdr(a_save,'ETag')=='"r1-v2"')
    ck('N3 naive stale whole-record PUT succeeds without a precondition',b_naive['status']==200)
    ck('N4 naive stale PUT reproduces lost update',final['body']['title']=='Flight 101' and final['body']['notes']=='Weather diversion')

    store.reset(); baseA=c.req('GET','/records/r1'); baseB=c.req('GET','/records/r1'); e1=hdr(baseA,'ETag')
    remote=c.req('PUT','/records/r1',{'title':'Flight 101A','notes':'Routine'},{'If-Match':e1})
    stale=c.req('PUT','/records/r1',{'title':'Flight 101','notes':'Weather diversion'},{'If-Match':e1}); current=c.req('GET','/records/r1')
    merged=c.req('PUT','/records/r1',{'title':current['body']['title'],'notes':'Weather diversion'},{'If-Match':hdr(current,'ETag')}); after_merge=c.req('GET','/records/r1')
    scenarios['conditional_merge']={'baseB':baseB,'remote':remote,'stale':stale,'current_after_412':current,'merged':merged,'after_merge':after_merge}
    ck('C1 stale If-Match write is rejected with 412',stale['status']==412)
    ck('C2 412 path does not mutate authoritative remote change',current['body']['title']=='Flight 101A' and current['body']['notes']=='Routine' and hdr(current,'ETag')=='"r1-v2"')
    ck('C3 412 response returns current validator in this API contract',hdr(stale,'ETag')=='"r1-v2"')
    ck('C4 safe disjoint merge is rebased against current validator',merged['status']==200 and hdr(merged,'ETag')=='"r1-v3"')
    ck('C5 disjoint merge preserves both remote and local intentions',after_merge['body']['title']=='Flight 101A' and after_merge['body']['notes']=='Weather diversion')

    store.reset(); local=c.req('GET','/records/r1'); e1=hdr(local,'ETag'); remote=c.req('PUT','/records/r1',{'title':'Flight 101A','notes':'Routine'},{'If-Match':e1})
    stale_title=c.req('PUT','/records/r1',{'title':'Flight 101B','notes':'Routine'},{'If-Match':e1}); after_conflict=c.req('GET','/records/r1')
    local_draft={'title':'Flight 101B','notes':'Routine','base_etag':e1}; scenarios['same_field_conflict']={'remote':remote,'stale':stale_title,'authoritative':after_conflict,'preserved_local_draft':local_draft}
    ck('S1 same-field stale write is rejected before overwrite',stale_title['status']==412 and after_conflict['body']['title']=='Flight 101A')
    ck('S2 local same-field draft can remain preserved client-side',local_draft['title']=='Flight 101B' and local_draft['base_etag']=='"r1-v1"')
    ck('S3 precondition detection alone does not choose conflict winner',after_conflict['body']['version']==2 and after_conflict['body']['title']!='Flight 101B')

    store.reset(); stale_client=c.req('GET','/records/r1'); e1=hdr(stale_client,'ETag'); deleted=c.req('DELETE','/records/r1',headers={'If-Match':e1})
    edit_after_delete=c.req('PUT','/records/r1',{'title':'Flight 101','notes':'Local preserved note'},{'If-Match':e1})
    new_copy=c.req('PUT','/records/r2',{'title':'Flight 101','notes':'Local preserved note'},{'If-None-Match':'*'}); duplicate_create=c.req('PUT','/records/r2',{'title':'Other','notes':'Overwrite attempt'},{'If-None-Match':'*'})
    r1=c.req('GET','/records/r1'); r2=c.req('GET','/records/r2'); scenarios['delete_vs_edit']={'stale_client':stale_client,'deleted':deleted,'stale_edit':edit_after_delete,'new_copy':new_copy,'duplicate_create':duplicate_create,'r1':r1,'r2':r2}
    ck('D1 conditional delete succeeds for current validator',deleted['status']==204)
    ck('D2 stale edit after deletion fails precondition instead of resurrecting r1',edit_after_delete['status']==412 and r1['status']==404)
    ck('D3 preserved work can be created under new identity with If-None-Match:*',new_copy['status']==201 and r2['body']['id']=='r2' and r2['body']['notes']=='Local preserved note')
    ck('D4 If-None-Match:* blocks accidental overwrite of the new identity',duplicate_create['status']==412 and r2['body']['title']=='Flight 101')
finally:
    srv.shutdown(); srv.server_close(); t.join(timeout=2)

res={'environment':{'transport':'real local HTTP/1.1 origin server via Python http.server','port_ephemeral':True},'scenarios':scenarios,'assertions':assertions,'summary':{'passed':sum(a['pass'] for a in assertions),'total':len(assertions)}}
Path('/mnt/data/i004http/results.json').write_text(json.dumps(res,ensure_ascii=False,indent=2))
print(json.dumps(res['summary']))
for a in assertions: print(('PASS' if a['pass'] else 'FAIL'),a['name'])
