"""Bounded experiment contracts and consistency checks; no model dependency."""
import hashlib
import json
import math
import statistics
import unicodedata
from pathlib import Path

MODEL = 'HuggingFaceTB/SmolLM2-135M-Instruct'
REVISION = '12fd25f77366fa6b3b4b768ec3050bf629380bac'
FILES = ['README.md','config.json','generation_config.json','merges.txt','model.safetensors','special_tokens_map.json','tokenizer.json','tokenizer_config.json','vocab.json']
PROFILES = (1, 2)
REPEATS = 3
MAX_NEW_TOKENS = 24


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def normalized(text):
    return ' '.join(unicodedata.normalize('NFKC', text).casefold().split())


def verify_manifest(root, manifest):
    root = Path(root).resolve()
    if manifest.get('model') != MODEL or manifest.get('revision') != REVISION:
        raise ValueError('unexpected model or revision')
    files = manifest.get('files')
    if not isinstance(files, dict) or set(files) != set(FILES):
        raise ValueError('unexpected artifact inventory')
    for name, expected in files.items():
        path = (root / name).resolve()
        if not path.is_relative_to(root) or not path.is_file() or digest(path) != expected:
            raise ValueError('missing, escaped or changed artifact: ' + name)
    return files


def summarize(rows):
    if not isinstance(rows, list) or not rows or len(rows) > 200:
        raise ValueError('bounded nonempty measurement list required')
    seen = set(); groups = {}
    for row in rows:
        if row.get('threads') not in PROFILES or type(row.get('threads')) is not int:
            raise ValueError('unexpected profile')
        if type(row.get('repeat')) is not int or row['repeat'] not in range(REPEATS):
            raise ValueError('unexpected repeat')
        key = (row['threads'], row.get('id'), row['repeat'])
        if key in seen: raise ValueError('duplicate measurement')
        seen.add(key)
        if row.get('language') not in ('en', 'ar'): raise ValueError('unsupported language')
        if any(not isinstance(row.get(k), str) for k in ('id','expected','output')) or not row['id'] or not normalized(row['expected']):
            raise ValueError('case identity and text required')
        if type(row.get('seconds')) not in (int,float) or not math.isfinite(row['seconds']) or row['seconds'] <= 0:
            raise ValueError('finite positive duration required')
        for k in ('input_tokens','generated_tokens'):
            if type(row.get(k)) is not int or row[k] <= 0: raise ValueError('positive token count required')
        if row['generated_tokens'] > MAX_NEW_TOKENS: raise ValueError('generation bound exceeded')
        g = groups.setdefault(str(row['threads']), {'times': [], 'tokens': 0, 'slices': {}})
        g['times'].append(row['seconds']); g['tokens'] += row['generated_tokens']
        s = g['slices'].setdefault(row['language'], {'passed_measurements':0, 'measurements':0, 'case_ids':set()})
        s['measurements'] += 1; s['case_ids'].add(row['id'])
        s['passed_measurements'] += normalized(row['output']) == normalized(row['expected'])
    result = {}
    for profile, group in groups.items():
        result[profile] = {'median_generation_seconds': statistics.median(group['times']), 'total_generation_seconds': sum(group['times']), 'generated_tokens':group['tokens'], 'aggregate_generated_tokens_per_second':group['tokens']/sum(group['times']), 'measurements':len(group['times']), 'slices':{k:dict(unique_cases=len(v['case_ids']), passed_measurements=v['passed_measurements'], measurements=v['measurements']) for k,v in group['slices'].items()}}
    return result


def decide(candidate):
    """Fictional BANK-A gates; favourable declarations still require human review."""
    blocked=[]; gaps=[]
    for key, required in [('site','BANK-A'),('network',False),('remote_operator',False)]:
        val=candidate.get(key)
        if val is None or (key != 'site' and type(val) is not bool): gaps.append(key+' missing')
        elif val != required: blocked.append(key+' conflicts with boundary')
    for key in ('rights_review','dataset_review','quality_review','rollback_test'):
        if candidate.get(key) is not True: gaps.append(key+' missing')
    try: summary=summarize(candidate.get('rows'))
    except (ValueError,TypeError,KeyError) as e: summary={};gaps.append('invalid measurements: '+str(e))
    for profile in map(str,PROFILES):
        if profile not in summary: gaps.append('profile '+profile+' missing');continue
        for lang in ('en','ar'):
            s=summary[profile]['slices'].get(lang)
            if not s: gaps.append(profile+' '+lang+' denominator missing')
            elif s['passed_measurements'] != s['measurements']: blocked.append(profile+' '+lang+' literal criterion failed')
    return {'status':'BLOCKED' if blocked else 'UNVERIFIED' if gaps else 'REVIEW_REQUIRED','blocked':blocked,'gaps':gaps,'summary':summary,'scope':'Course-authored declarations; no production approval'}


def validate_record(record, cases):
    """Detect inconsistent evidence, not forgery or real facility controls."""
    if record.get('schema') != 'module13-inference-v1': raise ValueError('schema')
    if record.get('model') != MODEL or record.get('revision') != REVISION: raise ValueError('model identity')
    hashes=record.get('artifact_hashes',{})
    if set(hashes)!=set(FILES) or any(not isinstance(x,str) or len(x)!=64 or any(c not in '0123456789abcdef' for c in x) for x in hashes.values()): raise ValueError('artifact hashes')
    expected_settings={'device':'cpu','dtype':'float32','do_sample':False,'max_new_tokens':MAX_NEW_TOKENS,'use_cache':True,'repeats':REPEATS,'warmups_per_profile':1,'profile_order':[1,2]}
    if record.get('settings') != expected_settings: raise ValueError('settings')
    if not record.get('started_utc') or not record.get('platform') or not record.get('python') or str(record.get('torch','')).split('+',1)[0]!='2.9.1' or record.get('transformers')!='4.57.3': raise ValueError('runtime/provenance')
    from datetime import datetime
    dt=datetime.fromisoformat(record['started_utc'])
    if dt.utcoffset() is None: raise ValueError('timezone required')
    loads=record.get('load_seconds',{})
    if set(loads)!={'1','2'} or any(type(x) not in (int,float) or not math.isfinite(x) or x<=0 for x in loads.values()): raise ValueError('load timings')
    if record.get('cases_sha256') != digest(Path(__file__).with_name('cases.json')): raise ValueError('case hash')
    mapping={c['id']:c for c in cases}
    rows=record.get('rows')
    if not isinstance(rows,list) or len(rows)!=len(cases)*len(PROFILES)*REPEATS: raise ValueError('complete case/profile/repeat matrix required')
    summary=summarize(rows)
    for row in rows:
        c=mapping.get(row['id'])
        if c is None or any(row.get(k)!=c[k] for k in ('prompt','language','expected')): raise ValueError('case changed')
    if record.get('summary') != summary: raise ValueError('summary inconsistent with raw observations')
    if record.get('status') != 'REVIEW_REQUIRED': raise ValueError('experiment cannot claim approval')
    if record.get('network_guard') != 'Python connect/create_connection/getaddrinfo denied; not OS isolation': raise ValueError('network scope')
    return summary


if __name__ == '__main__':
    import sys
    record=json.loads(Path(sys.argv[1]).read_text())
    cases=json.loads(Path(__file__).with_name('cases.json').read_text())
    print(json.dumps(validate_record(record,cases),ensure_ascii=False,indent=2))
