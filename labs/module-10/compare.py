#!/usr/bin/env python3
"""Declaration checks and a deterministic recovery timeline, never cloud discovery."""
import json
from pathlib import Path
import sys

ROUTES=('ingestion','training','embeddings','speech_ocr','inference','outputs',
        'diagnostics','telemetry','backup','support','activation','updates',
        'failover','retirement','iac_state')
OPERATORS=('enterprise','onsite_partner','provider_remote')

def text(value,name):
    if not isinstance(value,str) or not value.strip() or len(value)>200:
        raise ValueError(name+' must be a nonempty string of at most 200 characters')
    return value

def number(value,name,maximum=1_000_000_000):
    if type(value) not in (int,float) or not 0<=value<=maximum:
        raise ValueError(name+' must be finite and within the declared nonnegative range')
    return value

def flag(value,name):
    if type(value) is not bool:raise ValueError(name+' must be boolean')
    return value

def place(item):
    if not isinstance(item,dict):raise ValueError('location entry must be an object')
    return text(item.get('site'),'site'),text(item.get('country'),'country')

def simulate(events):
    if not isinstance(events,list) or len(events)!=3:
        raise ValueError('exactly checkpoint, failure and restore events required')
    times=[]
    for item,kind in zip(events,('checkpoint','failure','restore')):
        if not isinstance(item,dict) or item.get('kind')!=kind:raise ValueError('invalid event order or kind')
        place(item);times.append(number(item.get('at'),'event minute',1_000_000))
    if times!=sorted(times):raise ValueError('event times must be nondecreasing')
    return {'rto_minutes':times[2]-times[1],'rpo_minutes':times[1]-times[0],
            'evidence':'deterministic simulation of supplied minutes, not a measured recovery'}

def assess(policy,candidate):
    if not isinstance(policy,dict) or not isinstance(candidate,dict):raise ValueError('objects required')
    if policy.get('scope') not in ('premises','country'):raise ValueError('scope must be premises or country')
    if policy.get('failure_scope') not in ('host','site'):raise ValueError('failure scope must be host or site')
    if 'UNKNOWN' in place(policy):raise ValueError('policy must name its actual declared site and country')
    flag(policy.get('airgap'),'airgap')
    allowed=policy.get('allowed_operators')
    if not isinstance(allowed,list) or not allowed or any(x not in OPERATORS for x in allowed):
        raise ValueError('explicit recognized allowed operators required')
    for key in ('rto_minutes','rpo_minutes'):number(policy.get(key),key,1_000_000)
    ident=text(candidate.get('id'),'id');text(candidate.get('pattern'),'pattern')
    text(candidate.get('build'),'build');text(candidate.get('observed_build'),'observed_build')
    score=number(candidate.get('fit_score'),'fit_score',100)
    cost=number(candidate.get('monthly_cost_aed'),'monthly_cost_aed')
    flag(candidate.get('dependency_inventory_complete'),'dependency_inventory_complete')
    if candidate.get('evidence_kind') not in ('assumed','simulation','deployment_test'):
        raise ValueError('unsupported evidence kind')
    routes=candidate.get('routes')
    if not isinstance(routes,list) or len(routes)>200:raise ValueError('bounded routes list required')
    conflicts=[];gaps=[];seen=set()
    def check_location(item,label):
        site,country=place(item)
        if country=='UNKNOWN':gaps.append(label+': country unknown')
        elif country!=policy['country']:conflicts.append(label+': outside allowed country')
        if site=='UNKNOWN':gaps.append(label+': site unknown')
        elif policy['scope']=='premises' and site!=policy['site']:
            conflicts.append(label+': outside physical premises')
    for route in routes:
        purpose=text(route.get('purpose'),'purpose') if isinstance(route,dict) else ''
        check_location(route,purpose)
        network=flag(route.get('network'),'network')
        if policy['airgap'] and network:conflicts.append(purpose+': network path conflicts with air gap')
        operator=text(route.get('operator'),'operator')
        if operator not in OPERATORS:gaps.append(purpose+': operator unknown')
        elif operator not in allowed:conflicts.append(purpose+': unapproved operator')
        if operator=='provider_remote' and (policy['scope']=='premises' or policy['airgap']):
            conflicts.append(purpose+': remote administration conflicts with physical boundary')
        if purpose not in ROUTES:gaps.append(purpose+': unknown purpose')
        if purpose in seen:gaps.append(purpose+': duplicate purpose')
        seen.add(purpose)
    gaps.extend(x+': missing route' for x in ROUTES if x not in seen)
    recovery=candidate.get('recovery')
    if not isinstance(recovery,dict):raise ValueError('recovery object required')
    result=simulate(recovery.get('events'))
    for event in recovery['events']:check_location(event,'recovery '+event['kind'])
    for purpose,event in zip(('backup','inference','failover'),recovery['events']):
        declared=[r for r in routes if r['purpose']==purpose]
        if len(declared)==1 and place(declared[0])!=place(event):
            gaps.append(purpose+': route and recovery event locations disagree')
    failed=text(recovery.get('failed_domain'),'failed_domain')
    target=text(recovery.get('target_domain'),'target_domain')
    if 'UNKNOWN' in (failed,target):gaps.append('failure domain unknown')
    if failed==target and failed!='UNKNOWN':conflicts.append('recovery shares declared failed domain')
    if policy['failure_scope']=='site' and recovery['events'][1]['site']==recovery['events'][2]['site']:
        conflicts.append('site-loss recovery remains at failed site')
    for key in ('rto_minutes','rpo_minutes'):
        if result[key]>policy[key]:conflicts.append(key+': simulated result exceeds objective')
    if not candidate['dependency_inventory_complete']:gaps.append('dependency inventory incomplete')
    if candidate['evidence_kind']=='assumed':gaps.append('recovery and controls remain assumed')
    if candidate['observed_build']!=candidate['build']:gaps.append('evidence refers to a different build')
    status='BLOCKED' if conflicts else 'UNVERIFIED' if gaps else 'REVIEW_REQUIRED'
    return {'id':ident,'status':status,'conflicts':conflicts,'gaps':gaps,'recovery':result,
            'fit_score':score,'monthly_cost_aed':cost,
            'limit':'Supplied declarations and simulation do not authenticate controls, geography, identities or legal compliance.'}

def compare(policy,candidates):
    if not isinstance(candidates,list) or not 1<=len(candidates)<=30:raise ValueError('1 to 30 candidates required')
    results=[assess(policy,c) for c in candidates]
    if len({r['id'] for r in results})!=len(results):raise ValueError('duplicate candidate IDs')
    ranked=sorted((r for r in results if r['status']=='REVIEW_REQUIRED'),key=lambda r:(-r['fit_score'],r['monthly_cost_aed'],r['id']))
    return {'candidates':results,'ranked_candidates':[r['id'] for r in ranked],
            'notice':'Fictional preferences rank only nonblocked complete declarations; no deployment is approved.'}

def main():
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('deployments.json')
    fixture=json.loads(path.read_text())
    print(json.dumps(compare(fixture['policy'],fixture['candidates']),indent=2))

if __name__=='__main__':main()
