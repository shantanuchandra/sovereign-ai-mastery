#!/usr/bin/env python3
"""Course-authored arithmetic on declarations, never hardware discovery or approval."""
import json
import math
from pathlib import Path
import sys

ROUTES = ('ingestion', 'training', 'embeddings', 'speech_ocr', 'inference', 'outputs',
          'diagnostics', 'telemetry', 'backup', 'support', 'activation', 'updates',
          'failover', 'retirement')

def number(data, key, low, high, integer=False):
    value = data.get(key)
    if type(value) not in (int, float) or not low <= value <= high or not math.isfinite(value):
        raise ValueError(key + ': finite number required')
    if integer and type(value) is not int:
        raise ValueError(key + ': integer required')
    if not low <= value <= high:
        raise ValueError(key + ': outside supported teaching range')
    return value

def text(data, key):
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(key + ': explicit value required')
    return value

def estimate(data):
    if not isinstance(data, dict):
        raise ValueError('configuration must be an object')
    fields = {
        'parameters_billion': (.001, 10000, False), 'weight_bits': (2, 32, True),
        'layers': (1, 10000, True), 'kv_heads': (1, 10000, True),
        'head_dim': (1, 10000, True), 'context_tokens': (1, 10000000, True),
        'concurrent_sequences': (1, 1000000, True), 'kv_bytes': (1, 8, True),
        'runtime_overhead_gib': (0, 1000000, False),
        'available_memory_gib': (.001, 10000000, False),
        'headroom_fraction': (0, .9, False), 'arrival_rps': (.001, 100000000, False),
        'profile_rps': (.001, 100000000, False),
        'target_utilization': (.01, .99, False), 'installed_replicas': (1, 1000000, True),
        'spare_replicas': (0, 1000000, True), 'p95_ms': (0, 100000000, False),
        'slo_p95_ms': (.001, 100000000, False), 'error_rate': (0, 1, False),
        'max_error_rate': (0, 1, False), 'device_kw': (0, 1000000, False),
        'hours_per_month': (0, 744, False), 'energy_price_per_kwh': (0, 1000000, False),
        'fixed_monthly_cost': (0, 1000000000000, False),
        'monthly_successful_requests': (1, 1000000000000000, True),
    }
    v = {k: number(data, k, *bounds) for k, bounds in fields.items()}
    for key in ('required_site', 'compute_site', 'required_country', 'compute_country',
                'candidate_build', 'profile_build', 'currency'):
        text(data, key)
    for key in ('physical_airgap', 'external_network_dependencies'):
        if type(data.get(key)) is not bool:
            raise ValueError(key + ': Boolean required')
    if data.get('profile_evidence') not in ('assumption', 'synthetic_test', 'deployment_test'):
        raise ValueError('profile_evidence: explicit type required')
    routes = data.get('routes')
    if not isinstance(routes, list) or any(not isinstance(r, dict) for r in routes):
        raise ValueError('routes: list of declarations required')

    blocked, gaps = [], []
    if data['compute_site'] != data['required_site'] or data['compute_country'] != data['required_country']:
        blocked.append('Compute placement conflicts with the declared premises/country requirement.')
    if data['physical_airgap'] and data['external_network_dependencies']:
        blocked.append('An external network dependency conflicts with the physical air gap.')
    seen = set()
    for route in routes:
        for key in ('id', 'site', 'country'):
            text(route, key)
        if type(route.get('network')) is not bool:
            raise ValueError('route network: Boolean required')
        if route['site'] != data['required_site'] or route['country'] != data['required_country']:
            blocked.append('Prohibited declared route destination: ' + route['id'])
        if data['physical_airgap'] and route['network']:
            blocked.append('Prohibited network use: ' + route['id'])
        if route['id'] not in ROUTES:
            gaps.append('Unclassified lifecycle route: ' + route['id'])
        if route['id'] in seen:
            gaps.append('Duplicate route needs reconciliation: ' + route['id'])
        seen.add(route['id'])
    for missing in sorted(set(ROUTES) - seen):
        gaps.append('Missing lifecycle declaration: ' + missing)

    weights = v['parameters_billion'] * 1e9 * v['weight_bits'] / 8 / 2**30
    kv = (2 * v['layers'] * v['kv_heads'] * v['head_dim'] * v['context_tokens']
          * v['kv_bytes'] * v['concurrent_sequences'] / 2**30)
    memory = (weights + kv + v['runtime_overhead_gib']) * (1 + v['headroom_fraction'])
    active = math.ceil(v['arrival_rps'] / (v['profile_rps'] * v['target_utilization']))
    required = active + v['spare_replicas']
    if memory > v['available_memory_gib']:
        blocked.append('Estimated per-replica memory exceeds the declared available memory.')
    if required > v['installed_replicas']:
        blocked.append('Installed replicas cannot meet the arithmetic load plus spare requirement.')
    if v['p95_ms'] > v['slo_p95_ms'] or v['error_rate'] > v['max_error_rate']:
        blocked.append('Declared latency/error result fails the selected acceptance criterion.')
    if data['profile_evidence'] == 'assumption':
        gaps.append('Performance profile is an assumption, not an observed result.')
    if data['profile_build'] != data['candidate_build']:
        gaps.append('Performance profile does not match the candidate build.')
    energy = v['installed_replicas'] * v['device_kw'] * v['hours_per_month'] * v['energy_price_per_kwh']
    total = v['fixed_monthly_cost'] + energy
    return {
        'state': 'BLOCKED' if blocked else 'UNVERIFIED' if gaps else 'REVIEW_REQUIRED',
        'blocked': blocked, 'gaps': gaps,
        'weights_gib': round(weights, 4), 'kv_gib': round(kv, 4),
        'memory_with_headroom_gib': round(memory, 4),
        'active_replicas': active, 'required_installed_replicas': required,
        'monthly_energy_cost': round(energy, 2), 'monthly_total_cost': round(total, 2),
        'cost_per_1000_successes': round(total / v['monthly_successful_requests'] * 1000, 4),
        'currency': data['currency'],
        'limits': 'Arithmetic on supplied declarations. No model benchmark, topology discovery, legal approval or certification. Memory formula omits implementation-specific allocations.'
    }

if __name__ == '__main__':
    path = Path(sys.argv[1]) if len(sys.argv) == 2 else Path(__file__).with_name('factory.json')
    print(json.dumps(estimate(json.loads(path.read_text())), indent=2))
