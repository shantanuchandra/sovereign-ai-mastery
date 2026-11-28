"""Bounded synthetic release controller. No service, identity provider or cloud is used."""
import copy
import hashlib
import json
import math
from pathlib import Path

ARTIFACTS = ('prompts', 'responses', 'ocr', 'speech', 'documents', 'embeddings', 'model_weights', 'registry', 'logs', 'traces', 'metrics', 'backups', 'support', 'activation', 'updates', 'failover', 'removable_media')
GATES = ('quality', 'security', 'identity', 'recovery')

def manifest(version='v1'):
    return {'version': version, 'model_sha256': hashlib.sha256(version.encode()).hexdigest(), 'runtime_build':'python-fixture-v1', 'prompt_version':'p1', 'retrieval_version':'r1', 'policy_version':'b1', 'telemetry_schema':'allowlist-v1', 'gates':{g:'PASS' for g in GATES}, 'artifacts':{a:'ON_PREMISES' for a in ARTIFACTS}, 'operator':'ON_SITE', 'connectivity':'OFFLINE', 'media_review':'PASS'}

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def boundary(value):
    if not isinstance(value,dict): return 'UNVERIFIED'
    assets=value.get('artifacts',{})
    if value.get('operator') not in ('ON_SITE',None,'UNKNOWN') or value.get('connectivity') not in ('OFFLINE',None,'UNKNOWN') or value.get('media_review') == 'FAIL': return 'BLOCKED'
    if not isinstance(assets,dict): return 'UNVERIFIED'
    if any(v not in ('ON_PREMISES',None,'UNKNOWN') for v in assets.values()) or value.get('operator') not in ('ON_SITE',None,'UNKNOWN') or value.get('connectivity') not in ('OFFLINE',None,'UNKNOWN') or value.get('media_review') == 'FAIL': return 'BLOCKED'
    if set(assets)!=set(ARTIFACTS) or any(v!='ON_PREMISES' for v in assets.values()) or value.get('operator')!='ON_SITE' or value.get('connectivity')!='OFFLINE' or value.get('media_review')!='PASS': return 'UNVERIFIED'
    return 'DECLARED_ONLY'

class Controller:
    def __init__(self, quota=20):
        if type(quota) is not int or quota<1: raise ValueError('quota must be positive integer')
        self.quota=quota; self.registry={}; self.approved=set(); self.revoked=set(); self.active=None; self.previous=None
        self.used=set(); self.events=[]; self.requests=[]
        self.tenants={'tenant-a','tenant-b'} # server-owned synthetic fixture, not authentication
    def register(self,value):
        value=copy.deepcopy(value)
        required={'version','model_sha256','runtime_build','prompt_version','retrieval_version','policy_version','telemetry_schema','gates','artifacts','operator','connectivity','media_review'}
        if not isinstance(value,dict) or set(value)!=required or any(not isinstance(value[k],str) or not value[k] for k in ('version','runtime_build','prompt_version','retrieval_version','policy_version')): raise ValueError('invalid manifest')
        if not isinstance(value['model_sha256'],str) or len(value['model_sha256'])!=64 or any(c not in '0123456789abcdef' for c in value['model_sha256']): raise ValueError('invalid digest')
        key=fingerprint(value)
        if key in self.registry: return key
        self.registry[key]=value
        return key
    def eligible(self,key):
        value=self.registry.get(key)
        if value is None or fingerprint(value)!=key or key in self.revoked: return 'UNVERIFIED'
        status=boundary(value)
        if status!='DECLARED_ONLY': return status
        if value.get('telemetry_schema')!='allowlist-v1' or value.get('gates')!={g:'PASS' for g in GATES}: return 'UNVERIFIED'
        return 'DECLARED_ONLY'
    def approve(self,key):
        status=self.eligible(key)
        if status=='DECLARED_ONLY': self.approved.add(key)
        self.events.append({'kind':'approval','release':key,'decision':status})
        return status
    def deploy(self,key):
        status=self.eligible(key)
        if status!='DECLARED_ONLY' or key not in self.approved:
            self.events.append({'kind':'deploy','release':key,'decision':'DENIED','boundary':status}); return False
        self.previous,self.active=self.active,key
        self.events.append({'kind':'deploy','release':key,'decision':'ACTIVATED'}); return True
    def rollback(self):
        candidate=self.previous
        if candidate is None or candidate not in self.approved or self.eligible(candidate)!='DECLARED_ONLY':
            self.events.append({'kind':'rollback','decision':'DENIED'}); return False
        self.active,self.previous=candidate,self.active
        self.events.append({'kind':'rollback','release':candidate,'decision':'ACTIVATED'}); return True
    def request(self,tenant,request_id,ok=True,latency_ms=100,tokens=20,prompt=''):
        # prompt deliberately never enters telemetry; token numbers are declared synthetic values.
        if tenant not in self.tenants or not isinstance(request_id,str) or not request_id or type(ok) is not bool or type(latency_ms) not in (int,float) or not math.isfinite(latency_ms) or latency_ms<0 or type(tokens) is not int or tokens<0: raise ValueError('invalid synthetic request')
        identity=(tenant,request_id)
        if identity in self.used: return 'DUPLICATE'
        if self.active is None or self.eligible(self.active)!='DECLARED_ONLY' or self.active not in self.approved: return 'NO_ELIGIBLE_RELEASE'
        count=sum(r['tenant']==tenant for r in self.requests)
        if count>=self.quota:
            self.events.append({'kind':'quota','tenant':tenant,'decision':'DENIED'}); return 'QUOTA_DENIED'
        self.used.add(identity)
        row={'tenant':tenant,'release':self.active,'ok':ok,'latency_ms':latency_ms,'tokens':tokens}
        self.requests.append(row)
        self.events.append({'kind':'request',**row})
        return 'RECORDED'
    def metrics(self,tenant,target=0.95,latency_limit=200):
        if tenant not in self.tenants or type(target) not in (int,float) or not math.isfinite(target) or not 0<target<1 or type(latency_limit) not in (int,float) or not math.isfinite(latency_limit) or latency_limit<0: raise ValueError('invalid SLO')
        rows=[r for r in self.requests if r['tenant']==tenant]
        total=len(rows); good=sum(r['ok'] and r['latency_ms']<=latency_limit for r in rows)
        allowance=total*(1-target)
        return {'tenant':tenant,'eligible_requests':total,'good_requests':good,'ratio':good/total if total else None,'target':target,'latency_limit_ms':latency_limit,'budget_requests':allowance,'bad_requests':total-good,'budget_consumed':(total-good)/allowance if total else None,'tokens':sum(r['tokens'] for r in rows),'decision':'NO_DATA' if not total else ('FREEZE_AND_REVIEW' if good/total<target else 'WITHIN_SYNTHETIC_SLO')}

def demo():
    c=Controller(); first=c.register(manifest()); c.approve(first); c.deploy(first)
    second=c.register(manifest('v2')); c.approve(second); c.deploy(second)
    for i in range(10): c.request('tenant-a',str(i),ok=i!=9,latency_ms=100,prompt='SYNTHETIC SECRET NOT LOGGED')
    metrics=c.metrics('tenant-a'); rolled=c.rollback()
    external=manifest('v3'); external['artifacts']['traces']='EXTERNAL'; bad=c.register(external); c.approve(bad); denied=not c.deploy(bad)
    return {'schema':'module17-observation-v1','scenario':'synthetic single-process versioned release; no network service','boundary':'DECLARED_ONLY','requests':10,'metrics':metrics,'rollback_succeeded':rolled,'external_trace_deployment_denied':denied,'active_release':c.active,'events':c.events,'limitations':['Fixture identities are not authentication','No deployed model or actual traffic','Rollback changes a pointer; no state restore','No production SLO or physical isolation evidence']}

if __name__=='__main__': print(json.dumps(demo(),indent=2,allow_nan=False))
