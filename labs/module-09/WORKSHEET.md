# Module 09 compute-sizing decision worksheet

Course-authored PM template, 27 November 2026. Use fictional or approved public inputs; no legal opinion or production approval.

## 1. Workload and accountable decision

Name workload/purpose, accountable PM, platform/recovery/security owners, candidate model/runtime/build, allowed use and review date. Separate training, fine-tuning, batch and online profiles. State the exact premises, country and connectivity rule. Link Module 07 components/routes and Module 08 artifact/retention rules.

## 2. Profile and memory budget

| Input | Value and unit | Assumed / observed / supplier-claimed | Source, build and date |
|---|---|---|---|
| Parameters / stored precision | Fill | Fill | Fill |
| Layers / KV heads / head dimension | Fill | Fill | Fill |
| Context / concurrent sequences / cache precision | Fill | Fill | Fill |
| Runtime / buffers / OS / VM / other services | Fill | Fill | Fill |
| Available per-device and per-host budget | Fill | Fill | Fill |
| Added margin and packing assumptions | Fill | Fill | Fill |

Show the arithmetic and its omitted allocations. Explain whether one replica spans devices or replicas share a host. Do not add device capacities without an operable placement/sharding plan. Retain actual peak-memory and restart evidence as separate observations.

## 3. Service and failure acceptance

Record workload mix, load generation method, duration, warm/cold cases, successful throughput, full error denominator, latency population/percentile, admission behavior and accepted thresholds. Name every replica, shared dependency and failure domain. Calculate active/spare capacity, then define a replica-loss and recovery rehearsal. An idle spare on the same failed host is not independent recovery.

## 4. Boundaries, operations and costs

Inventory all fourteen architecture lifecycle IDs. Include preprocessing, prompts, vectors, diagnostics, telemetry, support, activation, updates, backups and failover. Define resource requests/limits separately from identity-derived access and tenant isolation. Record denied-path tests and remaining placement/egress evidence.

Use dated hardware, software/model rights, facility, power, cooling, network, support and exit inputs for real decisions. Mark invented values. Keep average versus peak power and accounting periods explicit; divide costs by successful useful work at accepted quality, not attempted requests alone.

## 5. Recommendation and scoring

Compare admissible on-site options and a manual fallback. Keep prohibited alternatives blocked until an authorized requirement change. Record recommendation, rejected options, missing evidence, owners, dated retest and review trigger.

Illustrative 20-point rubric: profile/memory assumptions (5), load/error/failure evidence plan (5), physical and operational controls (4), cost sensitivity with provenance (3), bounded recommendation and ownership (3). Require 12/20 for course progress, plus remediation of hard-boundary overrides and unsupported performance/assurance claims regardless of score. This is not a qualification or certification.
