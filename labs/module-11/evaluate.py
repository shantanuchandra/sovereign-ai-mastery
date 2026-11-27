"""Synthetic exact-match scoring and declared-policy checks, not production assurance."""
import hashlib,json,unicodedata
from pathlib import Path

def normalize(text):
    return ' '.join(unicodedata.normalize('NFKC',text).casefold().split())

def score_rows(rows):
    if not isinstance(rows,list) or len(rows)>1000:raise ValueError('rows must be a bounded list')
    groups={};ids=set()
    for r in rows:
        if not isinstance(r,dict) or not isinstance(r.get('id'),str) or not r['id'].strip() or r['id'] in ids:raise ValueError('unique nonempty id required')
        ids.add(r['id']);lang=r.get('language')
        if lang not in ('en','ar'):raise ValueError('language must be en or ar')
        if any(not isinstance(r.get(k),str) for k in ('expected','output')) or not normalize(r['expected']):raise ValueError('expected and output text required')
        g=groups.setdefault(lang,dict(passed=0,total=0));g['total']+=1
        g['passed']+=normalize(r['output'])==normalize(r['expected'])
    return {k:dict(v,rate=v['passed']/v['total']) for k,v in groups.items()}

def decide(candidate):
    """Fixed fictional BANK-A air-gap policy, 100% exact match per language."""
    blocked=[];gaps=[]
    site=candidate.get('site')
    if not isinstance(site,str) or not site.strip() or site=='UNKNOWN':gaps.append('physical site unknown')
    elif site!='BANK-A':blocked.append('outside BANK-A')
    for key,forbidden in [('network',True),('remote_operator',True),('license_review',False)]:
        value=candidate.get(key)
        if type(value) is not bool:gaps.append(key+' missing or not boolean')
        elif value==forbidden:blocked.append(key+' conflicts with declared rule')
    if candidate.get('provenance') is not True:gaps.append('provenance review missing')
    if not isinstance(candidate.get('build'),str) or not candidate['build'].strip() or candidate['build']!=candidate.get('evaluated_build'):gaps.append('evaluated build does not match candidate')
    try:groups=score_rows(candidate.get('rows',[]))
    except ValueError as e:groups={};gaps.append(str(e))
    for language in ('en','ar'):
        if language not in groups:gaps.append(language+' denominator missing')
        elif groups[language]['passed']!=groups[language]['total']:blocked.append(language+' exact-match criterion not met')
    return dict(status='BLOCKED' if blocked else 'UNVERIFIED' if gaps else 'REVIEW_REQUIRED',blocked=blocked,gaps=gaps,groups=groups,scope='Declared educational fixture; not observed physical or legal assurance')

def verify_manifest(root,manifest):
    root=Path(root).resolve();files=manifest.get('files')
    if not isinstance(files,dict) or not files:raise ValueError('nonempty manifest required')
    for name,digest in files.items():
        if not isinstance(name,str) or Path(name).is_absolute() or '..' in Path(name).parts:raise ValueError('unsafe manifest path')
        path=(root/name).resolve()
        if not path.is_relative_to(root) or not path.is_file():raise ValueError('missing or escaped artifact: '+name)
        if not isinstance(digest,str) or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:raise ValueError('digest mismatch: '+name)
    return True

if __name__=='__main__':
    import sys
    print(json.dumps(decide(json.loads(Path(sys.argv[1]).read_text())),ensure_ascii=False,indent=2))
