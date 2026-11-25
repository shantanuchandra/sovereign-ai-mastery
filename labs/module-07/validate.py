#!/usr/bin/env python3
"""Course-authored graph inspection of synthetic declarations, not infrastructure discovery."""
import argparse
import json
from pathlib import Path
import re

PLANES=('data','compute','management','control')
PATHS=('ingestion','training','embeddings','speech_ocr','inference','outputs','diagnostics','telemetry','backup','support','activation','updates','failover','retirement')
ID=re.compile(r'^[a-z][a-z0-9_]{0,63}$')

def nonempty(value):return isinstance(value,str) and bool(value.strip())

def validate(record):
    blocked=[];gaps=[];nodes={};edges=[];paths=set()
    if not isinstance(record,dict):record={};gaps.append('record')
    boundary=record.get('boundary')
    if boundary not in ('country','premises','airgap'):gaps.append('boundary')
    for key in ('site','country','build_id'):
        if not nonempty(record.get(key)):gaps.append(key)
    source_nodes=record.get('nodes')
    if not isinstance(source_nodes,list):source_nodes=[];gaps.append('nodes')
    for node in source_nodes:
        if not isinstance(node,dict):gaps.append('node_record');continue
        name=node.get('id')
        if not isinstance(name,str) or not ID.fullmatch(name):gaps.append('node_id');continue
        # Inspect every declaration before indexing, so duplicates cannot hide an adverse location.
        for key in ('site','country','owner','zone'):
            if not nonempty(node.get(key)):gaps.append(f'node:{name}:{key}')
        if node.get('plane') not in PLANES:gaps.append(f'node:{name}:plane')
        if type(node.get('protected')) is not bool:gaps.append(f'node:{name}:protected')
        # Every declared component is scoped by this course's strict site/country inventory policy.
        if boundary in ('country','premises','airgap') and nonempty(record.get('country')) and nonempty(node.get('country')) and node['country']!=record['country']:
            blocked.append('country:'+name)
        if boundary in ('premises','airgap') and nonempty(record.get('site')) and nonempty(node.get('site')) and node['site']!=record['site']:
            blocked.append('site:'+name)
        if name in nodes:gaps.append('duplicate_node:'+name)
        else:nodes[name]=node
    present={n.get('plane') for n in nodes.values() if isinstance(n.get('plane'),str)}
    for plane in PLANES:
        if plane not in present:gaps.append('missing_plane:'+plane)
    source_edges=record.get('edges')
    if not isinstance(source_edges,list):source_edges=[];gaps.append('edges')
    seen=set()
    for i,edge in enumerate(source_edges):
        if not isinstance(edge,dict):gaps.append('edge_record');continue
        label=f'edge:{i}'
        kind=edge.get('kind')
        if not isinstance(kind,str) or kind not in PATHS:gaps.append(label+':kind')
        else:paths.add(kind)
        a,b=edge.get('from'),edge.get('to')
        refs_valid=isinstance(a,str) and isinstance(b,str) and a in nodes and b in nodes
        if not refs_valid:gaps.append(label+':reference')
        else:
            pair=(a,b,kind) if isinstance(kind,str) else (a,b,'unknown')
            if pair in seen:gaps.append(label+':duplicate')
            seen.add(pair)
        for key in ('owner','test','evidence','build_id'):
            if not nonempty(edge.get(key)):gaps.append(label+':'+key)
        if edge.get('build_id')!=record.get('build_id'):gaps.append(label+':build')
        if edge.get('outcome')=='fail':blocked.append(label+':failed_test')
        elif edge.get('outcome')!='pass':gaps.append(label+':outcome')
        if edge.get('transport') not in ('network','local','media'):gaps.append(label+':transport')
        if boundary=='airgap' and edge.get('transport')=='network':blocked.append(label+':network')
        if type(edge.get('protected')) is not bool:gaps.append(label+':protected')
        if refs_valid:
            crossed=nodes[a].get('zone')!=nodes[b].get('zone')
            if crossed and edge.get('authorization')!='explicit':gaps.append(label+':authorization')
            # A derived artifact cannot be declassified merely by changing an edge's Boolean flag.
            if nodes[a].get('protected') is True and edge.get('protected') is not True:
                gaps.append(label+':protection_downgrade')
        edges.append(edge)
    for kind in PATHS:
        if kind not in paths:gaps.append('missing_path:'+kind)
    return {'status':'BLOCKED' if blocked else 'UNVERIFIED' if gaps else 'REVIEW_REQUIRED',
            'blockers':sorted(set(blocked)),'gaps':sorted(set(gaps)),
            'limits':'Declared graph only; no production assurance or compliance certification.'}

def mermaid(record):
    """Render safe identifiers only; never interpolate untrusted labels or Mermaid directives."""
    nodes=record.get('nodes',[]) if isinstance(record,dict) else []
    nodes=nodes if isinstance(nodes,list) else []
    names=sorted({n['id'] for n in nodes if isinstance(n,dict) and isinstance(n.get('id'),str) and ID.fullmatch(n['id'])})
    lines=['flowchart LR']+[f'    {n}["{n}"]' for n in names]
    edges=record.get('edges',[]) if isinstance(record,dict) else []
    for e in edges if isinstance(edges,list) else []:
        if isinstance(e,dict) and e.get('from') in names and e.get('to') in names and isinstance(e.get('kind'),str) and e['kind'] in PATHS:
            lines.append(f'    {e["from"]} -->|{e["kind"]}| {e["to"]}')
    return '\n'.join(lines)+'\n'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('graph',type=Path);parser.add_argument('--mermaid',action='store_true')
    args=parser.parse_args();record=json.loads(args.graph.read_text())
    print(mermaid(record) if args.mermaid else json.dumps(validate(record),indent=2),end='' if args.mermaid else '\n')

if __name__=='__main__':main()
