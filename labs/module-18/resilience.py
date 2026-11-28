"""Synthetic local recovery exercise, not production or physical-boundary assurance."""
import copy
import hashlib
import json
import sqlite3
import tempfile
from pathlib import Path

ARTIFACTS = ('prompts','responses','ocr','speech','documents','embeddings','model_weights','registry','logs','traces','metrics','backups','support','activation','updates','failover','removable_media')

def declaration():
    return {'artifacts':dict.fromkeys(ARTIFACTS,'ON_PREMISES'),'operator':'ON_SITE','connectivity':'OFFLINE','media_review':'PASS'}

def boundary(value):
    if not isinstance(value,dict): return 'UNVERIFIED'
    assets=value.get('artifacts')
    # Known conflicts dominate unrelated omissions.
    if value.get('operator') not in (None,'UNKNOWN','ON_SITE') or value.get('connectivity') not in (None,'UNKNOWN','OFFLINE') or value.get('media_review')=='FAIL': return 'BLOCKED'
    if isinstance(assets,dict) and any(v not in (None,'UNKNOWN','ON_PREMISES') for v in assets.values()): return 'BLOCKED'
    if not isinstance(assets,dict) or set(assets)!=set(ARTIFACTS) or any(v!='ON_PREMISES' for v in assets.values()) or value.get('operator')!='ON_SITE' or value.get('connectivity')!='OFFLINE' or value.get('media_review')!='PASS': return 'UNVERIFIED'
    return 'DECLARED_ONLY'

def encode(value): return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def digest(data): return hashlib.sha256(data).hexdigest()

def fixture():
    return {'schema':1,'records':[{'id':'d1','tenant':'a','text':'synthetic eligible policy'},{'id':'d2','tenant':'a','text':'synthetic retired policy'},{'id':'d3','tenant':'b','text':'synthetic other tenant'}]}

def validate(snapshot):
    if not isinstance(snapshot,dict) or set(snapshot)!={'schema','records'} or type(snapshot['schema']) is not int or snapshot['schema']!=1 or not isinstance(snapshot['records'],list): raise ValueError('schema')
    ids=set()
    for r in snapshot['records']:
        if not isinstance(r,dict) or set(r)!={'id','tenant','text'} or any(not isinstance(v,str) or not v for v in r.values()) or r['id'] in ids: raise ValueError('record')
        ids.add(r['id'])
    return snapshot

class Exercise:
    def __init__(self,root):
        self.root=Path(root); self.root.mkdir(parents=True,exist_ok=True)
        self.live=self.root/'live.json'; self.backup=self.root/'backup.json'
        self.retired=set(); self.revoked_models=set(); self.expected=None
    def capture(self,snapshot):
        data=encode(validate(copy.deepcopy(snapshot)))
        self.live.write_bytes(data); self.backup.write_bytes(data); self.expected=digest(data)
        return self.expected
    def recover(self,decl,model='substitute-v1'):
        state=boundary(decl)
        if state=='BLOCKED': return {'decision':state}
        if not isinstance(model,str) or not model: return {'decision':'UNVERIFIED','reason':'INVALID_MODEL'}
        if model in self.revoked_models: return {'decision':'BLOCKED','reason':'MODEL_REVOKED'}
        if state!='DECLARED_ONLY': return {'decision':state}
        if self.expected is None or not self.backup.is_file(): return {'decision':'UNVERIFIED','reason':'MISSING_BACKUP'}
        data=self.backup.read_bytes()
        if digest(data)!=self.expected: return {'decision':'BLOCKED','reason':'INTEGRITY_MISMATCH'}
        try: snapshot=validate(json.loads(data))
        except (ValueError,TypeError,UnicodeError): return {'decision':'BLOCKED','reason':'SCHEMA'}
        # Trusted current decisions are outside the old snapshot, applied before exposure.
        active=[r for r in snapshot['records'] if r['id'] not in self.retired]
        stage=self.root/'restore.stage'
        stage.write_bytes(encode({'schema':1,'records':active}))
        stage.replace(self.live)  # Real local atomic name replacement, not distributed durability.
        return {'decision':'RESTORED_SYNTHETIC','restored_ids':[r['id'] for r in active],'retired_excluded':sorted(self.retired),'restored_sha256':digest(self.live.read_bytes()),'boundary':'DECLARED_ONLY'}
    def migrate(self):
        snapshot=validate(json.loads(self.live.read_bytes()))
        snapshot['records']=[r for r in snapshot['records'] if r['id'] not in self.retired]
        destination=self.root/'migration.sqlite'
        if destination.exists(): destination.unlink() # Fixed filename inside supplied exercise directory.
        with sqlite3.connect(destination) as db:
            db.execute('CREATE TABLE documents(id TEXT PRIMARY KEY, tenant TEXT NOT NULL, text TEXT NOT NULL)')
            db.executemany('INSERT INTO documents VALUES(:id,:tenant,:text)',snapshot['records'])
            rows=[dict(zip(('id','tenant','text'),r)) for r in db.execute('SELECT id,tenant,text FROM documents ORDER BY id')]
        expected=sorted(snapshot['records'],key=lambda r:r['id'])
        return {'decision':'MIGRATED_SYNTHETIC' if rows==expected else 'BLOCKED','rows':len(rows),'equal_records':rows==expected}
    def substitute(self,tenant,model='substitute-v1'):
        if not isinstance(model,str) or not model: return {'decision':'UNVERIFIED','reason':'INVALID_MODEL','ids':[]}
        if model in self.revoked_models: return {'decision':'BLOCKED','ids':[]}
        rows=validate(json.loads(self.live.read_bytes()))['records']
        ids=[r['id'] for r in rows if r['tenant']==tenant and r['id'] not in self.retired]
        return {'decision':'FIXTURE_ONLY','ids':ids,'model':model}

def demo():
    with tempfile.TemporaryDirectory(prefix='module18-') as root:
        e=Exercise(root); checksum=e.capture(fixture()); e.retired.add('d2'); e.live.unlink()
        missing_before=not e.live.exists(); restored=e.recover(declaration()); migration=e.migrate()
        substitute=e.substitute('a'); external=declaration(); external['artifacts']['failover']='EXTERNAL'
        denied=e.recover(external); e.revoked_models.add('old-model'); revoked=e.recover(declaration(),'old-model')
        return {'schema':'module18-observation-v1','date':'2026-11-28','synthetic':True,'backup_sha256':checksum,'live_file_deleted_before_restore':missing_before,'restore':restored,'migration':migration,'substitution':substitute,'external_failover':denied,'revoked_model':revoked,'limitations':['No production RTO or RPO measured','No real model, workload or database service','Boundary declarations are not physical evidence','No crash-durability, encryption, IAM or independent audit','Current retirement registry is in process memory','Temporary files removed after exercise']}

if __name__=='__main__':
    observation=demo()
    Path(__file__).with_name('observed-resilience-run.json').write_text(json.dumps(observation,indent=2)+'\n')
    print(json.dumps(observation,indent=2))
