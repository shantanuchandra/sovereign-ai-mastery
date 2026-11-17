#!/usr/bin/env python3
"""Validate claim structure, not real-world sovereignty or regulatory compliance."""
import json, sys
from pathlib import Path
REQUIRED = ('id','workload','scope','dimension','owner','criterion','control','test','evidence')
DIMENSIONS = {'territorial','operational','technological','legal_contractual'}
SCOPES = {'national','sectoral','enterprise','workload'}

def assess(claim):
    missing=[field for field in REQUIRED if not claim.get(field)]
    if missing: return {'id':claim.get('id','<missing>'),'status':'INVALID','reason':'Missing: '+', '.join(missing)}
    if claim['scope'] not in SCOPES or claim['dimension'] not in DIMENSIONS:
        return {'id':claim['id'],'status':'INVALID','reason':'Unrecognized scope or dimension'}
    e=claim['evidence']
    if not isinstance(e,dict):return {'id':claim['id'],'status':'INVALID','reason':'Evidence must be an object'}
    if e.get('status') != 'tested' or not e.get('source') or not e.get('observed_at'):
        return {'id':claim['id'],'status':'UNVERIFIED','reason':'Dated test evidence not supplied'}
    # A reported test does not independently establish that the control passes.
    return {'id':claim['id'],'status':'REVIEW_REQUIRED','reason':'Test record present; verify outcome and authenticity separately'}

def main(path):
    obj=json.loads(Path(path).read_text())
    if not isinstance(obj.get('claims'),list):raise ValueError('claims must be an array')
    report={'results':[assess(c) for c in obj['claims']]}
    print(json.dumps(report,indent=2));return int(any(x['status']=='INVALID' for x in report['results']))
if __name__=='__main__':sys.exit(main(sys.argv[1] if len(sys.argv)>1 else str(Path(__file__).with_name('claims.json'))))