#!/usr/bin/env python3
"""Course-authored governance triage. Reads synthetic declarations, never certifies them."""
import argparse
from datetime import date
import json
import math
from pathlib import Path

LIFECYCLE=('inference','training','embeddings','speech_ocr','diagnostics','telemetry','backup','support_activation','failover','updates')
CONTROLS=('boundary','quality','oversight','recovery')

def text(value):
    return isinstance(value,str) and bool(value.strip())

def number(value):
    return type(value) is int or (type(value) is float and math.isfinite(value))

def evaluate(record):
    """Known conflicts outrank missing evidence. Strongest output is REVIEW_REQUIRED."""
    blockers=[];gaps=[];rates={};aggregate=None
    if not isinstance(record,dict):record={};gaps.append('record')
    for k in ('id','build_id','site','country','intended_use'):
        if not text(record.get(k)):gaps.append(k)
    boundary=record.get('boundary')
    if boundary not in ('country','premises','airgap'):gaps.append('boundary')
    uses=record.get('allowed_uses')
    if not isinstance(uses,list) or not uses or not all(text(u) for u in uses):gaps.append('allowed_uses')
    elif text(record.get('intended_use')) and record['intended_use'] not in uses:blockers.append('intended_use')
    roles=record.get('roles')
    roles=roles if isinstance(roles,dict) else {}
    people=[]
    for role in ('responsible','validator','accountable'):
        person=roles.get(role)
        if not text(person):gaps.append('role:'+role)
        else:people.append(person.strip().casefold())
    if len(people)!=len(set(people)):gaps.append('role_separation')
    incident=record.get('incident_open')
    if type(incident) is not bool:gaps.append('incident_open')
    elif incident:blockers.append('open_incident')
    flows=record.get('flows');seen=set()
    if not isinstance(flows,list):flows=[];gaps.append('flows')
    for flow in flows:
        if not isinstance(flow,dict):gaps.append('flow_record');continue
        kind=flow.get('kind')
        if not isinstance(kind,str) or kind not in LIFECYCLE:
            gaps.append('flow_kind')
            kind=kind if text(kind) else 'unknown'
        else:
            if kind in seen:gaps.append('duplicate_flow:'+kind)
            seen.add(kind)
        for k in ('country','site'):
            if not text(flow.get(k)):gaps.append(k+':'+kind)
        if type(flow.get('network')) is not bool:gaps.append('network:'+kind)
        if boundary in ('country','premises','airgap') and text(flow.get('country')) and text(record.get('country')) and flow['country']!=record['country']:
            blockers.append('country:'+kind)
        if boundary in ('premises','airgap') and text(flow.get('site')) and text(record.get('site')) and flow['site']!=record['site']:
            blockers.append('site:'+kind)
        if boundary=='airgap' and flow.get('network') is True:blockers.append('network:'+kind)
    gaps.extend('missing_flow:'+kind for kind in LIFECYCLE if kind not in seen)
    criteria=record.get('criteria');criteria=criteria if isinstance(criteria,dict) else {}
    valid_criteria=True
    for k in ('error_limit','disparity_limit'):
        v=criteria.get(k)
        if not number(v) or not 0<=v<=1:gaps.append('criteria:'+k);valid_criteria=False
    minimum=criteria.get('min_group_size')
    if type(minimum) is not int or minimum<1:gaps.append('criteria:min_group_size');valid_criteria=False
    groups=record.get('groups');seen=set();total_n=total_errors=0;complete_counts=True
    if not isinstance(groups,list) or not groups:groups=[];gaps.append('groups')
    for group in groups:
        if not isinstance(group,dict):gaps.append('group_record');complete_counts=False;continue
        name=group.get('id')
        if not text(name):gaps.append('group_id');complete_counts=False;continue
        if name in seen:gaps.append('duplicate_group:'+name);complete_counts=False
        seen.add(name)
        n,e=group.get('n'),group.get('errors')
        if type(n) is not int or type(e) is not int or n<0 or not 0<=e<=n:
            gaps.append('counts:'+name);complete_counts=False;continue
        total_n+=n;total_errors+=e
        if n==0:gaps.append('sample:'+name);continue
        rate=e/n;rates[name]=rate
        if valid_criteria:
            if n<minimum:gaps.append('sample:'+name)
            if rate>criteria['error_limit']:blockers.append('group_error:'+name)
    if total_n and complete_counts:aggregate=total_errors/total_n
    if valid_criteria and len(rates)>1 and max(rates.values())-min(rates.values())>criteria['disparity_limit']:
        blockers.append('group_disparity')
    controls=record.get('controls');seen=set()
    if not isinstance(controls,list):controls=[];gaps.append('controls')
    for control in controls:
        if not isinstance(control,dict):gaps.append('control_record');continue
        cid=control.get('id')
        if not isinstance(cid,str) or cid not in CONTROLS:gaps.append('control_id');continue
        if cid in seen:gaps.append('duplicate_control:'+cid)
        seen.add(cid)
        outcome=control.get('outcome')
        if outcome=='fail':blockers.append('control_failure:'+cid)
        elif outcome!='pass':gaps.append('control_outcome:'+cid)
        if not text(control.get('build_id')) or control['build_id']!=record.get('build_id'):gaps.append('build:'+cid)
        for k in ('test_id','reviewer','evidence'):
            if not text(control.get(k)):gaps.append(k+':'+cid)
        try:
            tested=date.fromisoformat(control.get('date',''))
            reviewed=date.fromisoformat(record.get('review_date',''))
            if tested>reviewed or (reviewed-tested).days>30:raise ValueError('outside course evidence window')
        except (ValueError,TypeError):gaps.append('date:'+cid)
        if text(control.get('reviewer')) and text(roles.get('validator')) and control['reviewer'].strip().casefold()!=roles['validator'].strip().casefold():gaps.append('validator:'+cid)
    gaps.extend('missing_control:'+cid for cid in CONTROLS if cid not in seen)
    return {'id':record.get('id'),'status':'BLOCKED' if blockers else 'UNVERIFIED' if gaps else 'REVIEW_REQUIRED',
            'blockers':sorted(set(blockers)),'gaps':sorted(set(gaps)),
            'group_errors':rates,'aggregate_error':aggregate,
            'limits':'Synthetic declarations only; not production assurance, legal compliance or fairness certification.'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('cases',type=Path)
    args=parser.parse_args()
    records=json.loads(args.cases.read_text())
    if not isinstance(records,list):parser.error('cases must be a JSON array')
    print(json.dumps([evaluate(r) for r in records],indent=2,allow_nan=False))

if __name__=='__main__':main()
