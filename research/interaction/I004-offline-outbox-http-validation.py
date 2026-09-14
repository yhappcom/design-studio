import json, os, sqlite3, threading, socket, urllib.request, urllib.error
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

class Store:
    def __init__(self):
        self.lock=threading.Lock(); self.reset()
    def reset(self):
        with getattr(self,'lock',threading.Lock()):
            self.records={'r1': {'id':'r1','title':'Flight 101','notes':'Routine','version':1}}
    def etag(self,r): return f'"{r["id"]}-v{r["version"]}"'
STORE=Store()

class H(BaseHTTPRequestHandler):
    protocol_version='HTTP/1.1'
    def log_message(self,*a): pass
    def sendj(self,status,body,headers=None):
        raw=json.dumps(body,separators=(',',':')).encode(); self.send_response(status)
        self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(raw))); self.send_header('Cache-Control','no-store')
        for k,v in (headers or {}).items(): self.send_header(k,v)
        self.end_headers(); self.wfile.write(raw)
    def readj(self):
        n=int(self.headers.get('Content-Length','0')); return json.loads(self.rfile.read(n) or b'{}')
    def do_GET(self):
        rid=urlparse(self.path).path.rsplit('/',1)[-1]
        with STORE.lock:
            r=STORE.records.get(rid)
            if not r: return self.sendj(404,{'error':'not_found'})
            return self.sendj(200,r,{'ETag':STORE.etag(r)})
    def do_PUT(self):
        rid=urlparse(self.path).path.rsplit('/',1)[-1]; inc=self.readj()
        with STORE.lock:
            cur=STORE.records.get(rid); im=self.headers.get('If-Match'); inm=self.headers.get('If-None-Match')
            if inm=='*':
                if cur: return self.sendj(412,{'error':'precondition_failed'})
                rec={'id':rid,'title':inc.get('title',''),'notes':inc.get('notes',''),'version':1}; STORE.records[rid]=rec; return self.sendj(201,rec,{'ETag':STORE.etag(rec)})
            if im and (not cur or im!=STORE.etag(cur)): return self.sendj(412,{'error':'precondition_failed'})
            if not cur: return self.sendj(404,{'error':'not_found'})
            rec={'id':rid,'title':inc.get('title',cur['title']),'notes':inc.get('notes',cur['notes']),'version':cur['version']+1}; STORE.records[rid]=rec
            return self.sendj(200,rec,{'ETag':STORE.etag(rec)})
    def do_DELETE(self):
        rid=urlparse(self.path).path.rsplit('/',1)[-1]
        with STORE.lock:
            cur=STORE.records.get(rid); im=self.headers.get('If-Match')
            if not cur: return self.sendj(404,{'error':'not_found'})
            if im and im!=STORE.etag(cur): return self.sendj(412,{'error':'precondition_failed'})
            old=STORE.records.pop(rid); return self.sendj(200,{'deleted':True,'record':old})

def request(method,url,body=None,headers=None):
    data=None if body is None else json.dumps(body).encode(); h={'Accept':'application/json',**(headers or {})}
    if body is not None: h['Content-Type']='application/json'
    req=urllib.request.Request(url,data=data,headers=h,method=method)
    try:
        with urllib.request.urlopen(req,timeout=3) as r:
            raw=r.read(); return r.status,(json.loads(raw) if raw else None),r.headers.get('ETag')
    except urllib.error.HTTPError as e:
        raw=e.read(); return e.code,(json.loads(raw) if raw else None),e.headers.get('ETag')

class OfflineClient:
    def __init__(self,dbpath,base_url):
        self.dbpath=dbpath; self.base_url=base_url.rstrip('/'); self.online=True; self.db=sqlite3.connect(dbpath)
        self.db.execute('create table if not exists snapshots(record_id text primary key, etag text, record_json text not null)')
        self.db.execute('create table if not exists drafts(record_id text primary key, record_json text not null)')
        self.db.execute('create table if not exists outbox(op_id text primary key, record_id text not null, base_etag text not null, base_json text not null, patch_json text not null, local_json text not null, status text not null)')
        self.db.commit()
    def close(self): self.db.close()
    def get(self,rid='r1'):
        st,body,etag=request('GET',f'{self.base_url}/records/{rid}')
        if st==200:
            self.db.execute('insert or replace into snapshots values(?,?,?)',(rid,etag,json.dumps(body))); self.db.commit()
        return {'status':st,'record':body if st==200 else None,'etag':etag}
    def queue_patch(self,rid,patch):
        etag,basej=self.db.execute('select etag,record_json from snapshots where record_id=?',(rid,)).fetchone(); base=json.loads(basej); local={**base,**patch}; op='op-'+rid
        self.db.execute('insert or replace into drafts values(?,?)',(rid,json.dumps(local)))
        self.db.execute('insert or replace into outbox values(?,?,?,?,?,?,?)',(op,rid,etag,json.dumps(base),json.dumps(patch),json.dumps(local),'queued')); self.db.commit()
    def outbox(self):
        rows=self.db.execute('select op_id,record_id,base_etag,base_json,patch_json,local_json,status from outbox').fetchall()
        return [dict(op_id=a,record_id=b,base_etag=c,base=json.loads(d),patch=json.loads(e),local=json.loads(f),status=g) for a,b,c,d,e,f,g in rows]
    def draft(self,rid='r1'):
        r=self.db.execute('select record_json from drafts where record_id=?',(rid,)).fetchone(); return json.loads(r[0]) if r else None
    def _set_status(self,op,status): self.db.execute('update outbox set status=? where op_id=?',(status,op['op_id'])); self.db.commit()
    def _clear(self,op): self.db.execute('delete from outbox where op_id=?',(op['op_id'],)); self.db.execute('delete from drafts where record_id=?',(op['record_id'],)); self.db.commit()
    def flush_one(self):
        ops=self.outbox()
        if not ops: return {'kind':'empty'}
        op=ops[0]
        if not self.online: self._set_status(op,'network_pending'); return {'kind':'network_pending'}
        st,body,etag=request('PUT',f'{self.base_url}/records/{op["record_id"]}',op['local'],{'If-Match':op['base_etag']})
        if st==200: self._clear(op); return {'kind':'saved','saved':body,'etag':etag}
        if st!=412: self._set_status(op,'error'); return {'kind':'error','status':st}
        gst,current,current_etag=request('GET',f'{self.base_url}/records/{op["record_id"]}')
        if gst==404: self._set_status(op,'conflict_deleted'); return {'kind':'deleted_conflict','local':op['local'],'base':op['base']}
        local_fields=set(op['patch']); remote_fields={k for k,v in current.items() if k!='version' and op['base'].get(k)!=v}; overlap=sorted(local_fields & remote_fields)
        if overlap: self._set_status(op,'conflict_same_field'); return {'kind':'same_field_conflict','overlap':overlap,'local':op['local'],'current':current,'base':op['base']}
        merged={**current,**op['patch']}; st2,b2,e2=request('PUT',f'{self.base_url}/records/{op["record_id"]}',merged,{'If-Match':current_etag})
        if st2==200: self._clear(op); return {'kind':'auto_merged','saved':b2,'etag':e2,'remote_fields':sorted(remote_fields),'local_fields':sorted(local_fields)}
        self._set_status(op,'rebase_failed'); return {'kind':'rebase_failed','status':st2}
    def keep_as_new(self,newid):
        op=self.outbox()[0]; rec={**op['local'],'id':newid}; rec.pop('version',None)
        st,b,e=request('PUT',f'{self.base_url}/records/{newid}',rec,{'If-None-Match':'*'})
        if st==201: self._clear(op); return {'kind':'created_new','record':b,'etag':e}
        return {'kind':'create_failed','status':st}

def free_port():
    s=socket.socket(); s.bind(('127.0.0.1',0)); p=s.getsockname()[1]; s.close(); return p
checks=[]
def ck(name,cond): checks.append({'name':name,'pass':bool(cond)})
def rm(p):
    try: os.remove(p)
    except FileNotFoundError: pass

def run():
    port=free_port(); srv=ThreadingHTTPServer(('127.0.0.1',port),H); threading.Thread(target=srv.serve_forever,daemon=True).start(); base=f'http://127.0.0.1:{port}'
    a_db='/tmp/i004A.sqlite'; b_db='/tmp/i004B.sqlite'; out={'environment':{'client_store':'SQLite durable local outbox','transport':'real HTTP/1.1 localhost via urllib'},'assertions':checks}
    try:
        STORE.reset(); rm(a_db); A=OfflineClient(a_db,base); A.get(); A.queue_patch('r1',{'notes':'Offline draft'}); A.online=False; ck('S0 offline flush stays pending',A.flush_one()['kind']=='network_pending'); ck('S0 outbox not cleared on unavailable network',len(A.outbox())==1); A.close(); A=OfflineClient(a_db,base); ck('S0 durable queue survives client restart',len(A.outbox())==1 and A.draft()['notes']=='Offline draft'); A.close()

        STORE.reset(); rm(a_db); rm(b_db); A=OfflineClient(a_db,base); B=OfflineClient(b_db,base); a=A.get(); b=B.get(); ck('S1 clients share initial validator',a['etag']==b['etag']=='"r1-v1"'); A.online=False; A.queue_patch('r1',{'notes':'Weather diversion'}); A.close(); br=B.get(); st,bb,_=request('PUT',base+'/records/r1',{**br['record'],'title':'Flight 101A'},{'If-Match':br['etag']}); ck('S1 remote client commits title v2',st==200 and bb['version']==2); A=OfflineClient(a_db,base); ck('S1 queued edit survives restart',len(A.outbox())==1); f=A.flush_one(); ck('S1 stale reconnect safely rebases',f['kind']=='auto_merged' and f['saved']['title']=='Flight 101A' and f['saved']['notes']=='Weather diversion'); ck('S1 queue clears after merged commit',A.outbox()==[] and A.draft() is None); A.close(); B.close()

        STORE.reset(); rm(a_db); rm(b_db); A=OfflineClient(a_db,base); B=OfflineClient(b_db,base); A.get(); B.get(); A.online=False; A.queue_patch('r1',{'title':'Flight 101B'}); A.close(); br=B.get(); request('PUT',base+'/records/r1',{**br['record'],'title':'Flight 101A'},{'If-Match':br['etag']}); A=OfflineClient(a_db,base); f=A.flush_one(); ck('S2 same-field reconnect remains unresolved',f['kind']=='same_field_conflict' and f['overlap']==['title']); st,cur,_=request('GET',base+'/records/r1'); ck('S2 authoritative server stays remote v2',st==200 and cur['title']=='Flight 101A' and cur['version']==2); ck('S2 draft and conflict outbox preserved',A.draft()['title']=='Flight 101B' and A.outbox()[0]['status']=='conflict_same_field'); A.close(); B.close()

        STORE.reset(); rm(a_db); rm(b_db); A=OfflineClient(a_db,base); B=OfflineClient(b_db,base); A.get(); B.get(); A.online=False; A.queue_patch('r1',{'notes':'Keep this local note'}); A.close(); br=B.get(); ds,dbody,_=request('DELETE',base+'/records/r1',headers={'If-Match':br['etag']}); ck('S3 remote delete succeeds',ds==200 and dbody['deleted']); A=OfflineClient(a_db,base); f=A.flush_one(); ck('S3 reconnect classifies delete-vs-edit',f['kind']=='deleted_conflict'); s1,_,_=request('GET',base+'/records/r1'); ck('S3 original remains deleted',s1==404); ck('S3 conflict stays durable',A.outbox()[0]['status']=='conflict_deleted' and A.draft()['notes']=='Keep this local note'); new=A.keep_as_new('r2'); ck('S3 keep-as-new creates r2',new['kind']=='created_new' and new['record']['id']=='r2'); s1,_,_=request('GET',base+'/records/r1'); s2,r2,_=request('GET',base+'/records/r2'); ck('S3 new identity does not resurrect r1',s1==404 and s2==200 and r2['id']=='r2'); ck('S3 queue clears after new-identity commit',A.outbox()==[] and A.draft() is None); A.close(); B.close()
    finally: srv.shutdown(); srv.server_close()
    out['summary']={'passed':sum(x['pass'] for x in checks),'total':len(checks),'all_pass':all(x['pass'] for x in checks)}; return out

if __name__=='__main__': print(json.dumps(run(),indent=2))
