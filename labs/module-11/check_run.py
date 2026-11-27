"""Verify observed-run integrity, never require or invent a favourable quality result."""
import json,math,sys
from datetime import datetime
from pathlib import Path
from evaluate import score_rows
from prepare import MODEL,REVISION,FILES

def check_run(run):
    datetime.fromisoformat(run['started_utc'])
    if run['torch'].split('+')[0]!='2.9.1' or run['transformers']!='4.57.3':raise ValueError('unexpected runtime')
    cases=json.loads(Path(__file__).with_name('cases.json').read_text())
    if run['model']!=MODEL or run['revision']!=REVISION:raise ValueError('wrong model build')
    if set(run['artifact_hashes'])!=set(FILES):raise ValueError('incomplete artifact inventory')
    if any(len(h)!=64 or any(c not in '0123456789abcdef' for c in h) for h in run['artifact_hashes'].values()):raise ValueError('invalid hash')
    if len(run['rows'])!=len(cases):raise ValueError('missing cases')
    for case,row in zip(cases,run['rows']):
        if any(row.get(k)!=v for k,v in case.items()):raise ValueError('case specification changed')
        if not isinstance(row.get('output'),str) or not row['output'].strip():raise ValueError('missing generated text')
        for k in ('input_tokens','generated_tokens'):
            if type(row.get(k)) is not int or row[k]<=0:raise ValueError('invalid token count')
        if row['generated_tokens']>24:raise ValueError('generation bound exceeded')
        if type(row.get('seconds')) not in (int,float) or not math.isfinite(row['seconds']) or row['seconds']<0:raise ValueError('invalid time')
    if run['exact_match']!=score_rows(run['rows']):raise ValueError('score does not match raw output')
    if run['device']!='cpu' or run['dtype']!='float32' or run['threads']!=2 or run['max_new_tokens']!=24 or run['do_sample'] is not False:raise ValueError('unexpected run settings')
    if run['status']!='REVIEW_REQUIRED':raise ValueError('experiment cannot approve deployment')
    return True
if __name__=='__main__':
    check_run(json.loads(Path(sys.argv[1]).read_text()));print('Verified actual run record: 8 cases, build/settings, raw-output scores; no quality acceptance claim')
