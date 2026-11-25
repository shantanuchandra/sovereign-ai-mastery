#!/usr/bin/env python3
"""Validate fictional evidence records; never determine legal applicability."""
import json
from pathlib import Path
import sys

FLOW_KINDS = frozenset(('source', 'preprocess', 'inference', 'retrieval', 'output',
                        'telemetry', 'backup', 'support', 'activation_update'))
REVIEWS = ('legal_review', 'transfer_review', 'contract_review', 'licence_review')
UNKNOWN = {'', 'UNKNOWN', 'UNVERIFIED'}


def text(obj, key):
    value = obj.get(key)
    if not isinstance(value, str):
        raise ValueError('Expected text field: ' + key)
    return value.strip()


def record_complete(record, fields):
    return isinstance(record, dict) and all(
        isinstance(record.get(f), str) and record[f].strip() not in UNKNOWN
        for f in fields)


def evaluate_case(case):
    if not isinstance(case, dict):
        raise ValueError('Each workload must be an object')
    ident = text(case, 'id')
    if not ident:
        raise ValueError('Workload ID must not be empty')
    boundary = text(case, 'boundary')
    if boundary not in {'country', 'premises', 'airgap'}:
        raise ValueError('Unknown boundary')
    country, site = text(case, 'country'), text(case, 'site')
    if country in UNKNOWN or (boundary != 'country' and site in UNKNOWN):
        raise ValueError('Specify the required boundary before evaluating routes')
    flows = case.get('flows')
    if not isinstance(flows, list):
        raise ValueError('Expected flows array')
    failures, gaps, seen = [], [], set()
    for field in REVIEWS:
        state = text(case, field)
        if state not in {'reviewed', 'pending', 'rejected'}:
            raise ValueError('Unknown review state: ' + field)
        if state == 'rejected':
            failures.append(field + ': recorded rejection')
        elif state == 'pending':
            gaps.append(field + ': reviewer decision missing')
    if not record_complete(case.get('review_record'), ('reviewer', 'date', 'reference')):
        gaps.append('Versioned review record missing')
    for flow in flows:
        if not isinstance(flow, dict):
            raise ValueError('Flow must be an object')
        kind = text(flow, 'kind')
        if kind not in FLOW_KINDS or kind in seen:
            raise ValueError('Unknown or duplicate lifecycle flow')
        seen.add(kind)
        flow_country, flow_site = text(flow, 'country'), text(flow, 'site')
        network = flow.get('network')
        if not isinstance(network, bool):
            raise ValueError('network must be a JSON boolean')
        if flow_country in UNKNOWN:
            gaps.append(kind + ': destination country unknown')
        elif flow_country != country:
            failures.append(kind + ': outside required country')
        if boundary in {'premises', 'airgap'}:
            if flow_site in UNKNOWN:
                gaps.append(kind + ': physical site unknown')
            elif flow_site != site:
                failures.append(kind + ': outside named physical premises')
        if boundary == 'airgap' and network:
            failures.append(kind + ': network violates physical air gap')
        observation = flow.get('observation')
        if not isinstance(observation, dict):
            gaps.append(kind + ': observation missing')
            continue
        outcome = text(observation, 'outcome')
        if outcome not in {'pass', 'fail', 'missing'}:
            raise ValueError('Unknown observation outcome')
        if outcome == 'fail':
            failures.append(kind + ': adverse test reported')
        elif outcome == 'missing' or not record_complete(
                observation, ('test_id', 'reviewer', 'date', 'evidence')):
            gaps.append(kind + ': observed test provenance incomplete')
    gaps.extend('Missing lifecycle path: ' + kind for kind in sorted(FLOW_KINDS - seen))
    disposition = 'BLOCKED' if failures else ('UNVERIFIED' if gaps else 'REVIEW_REQUIRED')
    return {'id': ident, 'disposition': disposition, 'hard_failures': failures,
            'evidence_gaps': gaps, 'fictional_simulation': True,
            'notice': 'Recorded assertions only; no legal, physical or vendor assurance.'}


def evaluate_portfolio(data):
    if not isinstance(data, dict) or not isinstance(data.get('workloads'), list) or not data['workloads']:
        raise ValueError('Expected nonempty workloads array')
    results = [evaluate_case(case) for case in data['workloads']]
    if len({r['id'] for r in results}) != len(results):
        raise ValueError('Duplicate workload ID')
    return {'notice': 'FICTIONAL EDUCATIONAL SIMULATION; NO COMPLIANCE APPROVAL.', 'results': results}


def main():
    try:
        path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name('cases.json')
        print(json.dumps(evaluate_portfolio(json.loads(path.read_text())), indent=2))
    except (OSError, ValueError) as error:
        print(json.dumps({'error': str(error)}), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
