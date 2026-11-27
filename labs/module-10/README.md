# Module 10 deployment comparison lab

**Educational draft.** Compare three fictional diagrams/inventories and replay supplied recovery events. This is a declaration checker and deterministic simulation, not cloud deployment, provider discovery, firewall enforcement or a real restoration test.

## Environment and commands

Python 3.11+ standard library, including the Apple Silicon/16 GB baseline. No downloads after obtaining these files; no Docker, credentials, accounts, Terraform installation or paid resources. From the repository root:

```bash
python3 labs/module-10/compare.py
python3 -m unittest discover -s labs/module-10 -p 'test_*.py' -v
```

The program reads `deployments.json` and writes JSON to standard output. It opens no service, makes no network request and creates no infrastructure. An optional first argument selects another local fixture file. No cleanup is needed beyond any output files you choose to save. Do not use real secrets, infrastructure state or bank/customer information.

## Compare diagram and declarations

Read the [chapter diagram](../../diagrams/module-10-deployment.svg) alongside the three fixture inventories. The default policy requires BANK-A in AE, enterprise/on-site-partner operators, host-loss recovery within 10 minutes and recovery-point age within 2 minutes. Connected operation is permitted only where separately declared; the default local routes have no network path. All fifteen entries are treated as protected: Module 07's fourteen lifecycle purposes plus `iac_state`.

1. Local-private keeps each route at BANK-A with enterprise operators.
2. Fictional managed domestic service places routes at DC-B with provider-remote operators.
3. Hybrid keeps inference local but moves support, telemetry, backups, failover and IaC state to DC-B/provider operation.

Expected default result: local-private REVIEW_REQUIRED; managed and hybrid BLOCKED; only local-private ranked. Their invented scores are 70/95/90 and monthly costs 12,000/8,000/10,000 AED. Scores rank declared fit, not sovereignty or compliance. No supplier capability, quote or tariff is claimed.

The event sequence is checkpoint minute 8, failure 10, restoration 14. It yields a **simulated** 4-minute recovery window and 2-minute recovery-point age. The program subtracts supplied minutes. It restores no data and tests no actual failover, transaction consistency, identity dependency or retired-copy control. The named domains are declarations, not verified independent infrastructure.

## Controlled experiments

Copy the fixture to a learner-owned file and record one mutation per run. Preserve the original.

| Mutation | Learning result |
|---|---|
| Move an individual protected route off-site | Known conflict remains BLOCKED |
| Give that route an unknown/duplicate purpose | Gap is added; known conflict remains |
| Remove a route or mark inventory incomplete | UNVERIFIED if no known conflict exists |
| Change policy to country-only | Site restriction can relax; country/operator/network/recovery gates still apply |
| Set `airgap: true` and any route `network: true` | BLOCKED, including support, activation or state |
| Require site-loss recovery while restoring at BANK-A | BLOCKED; a same-site target shares the lost site |
| Move recovery off-site under premises-only rule | Still BLOCKED for placement |
| Use country-only plus authorized second-site recovery | May reach REVIEW_REQUIRED; not operational approval |
| Tighten RTO to 3 or RPO to 1 minute | Separate recovery objective failure |
| Set evidence to assumed or mismatch observed build | UNVERIFIED and excluded from ranking |

Schema errors raise ValueError: malformed numbers/booleans/enums, missing required object fields, unbounded lists or invalid event order/cardinality. Unknown route/operator classifications create gaps rather than silently assigning them. `UNKNOWN` destinations create gaps, while a separately known country/site conflict still blocks. Input labels never authenticate their evidence.

Checkpoint, failure and restoration destinations must agree with the corresponding backup, inference and failover declarations; disagreement creates an evidence gap. Unknown failure domains remain unverified. A remote-administration label conflicts with premises-only or physical-air-gap operation even if mistakenly included in the policy's operator list. Thirty tests include these adverse cases.

## Submission and limits

Allow 60–90 minutes. Submit original and mutated JSON outputs, the diagram-to-route comparison, a simulation calculation, an infeasible site-loss case and the separate [scorecard/ADR](ADR.md). Explain which original requirement would need authorized change. Do not edit a fixture and report that a firewall, administrator or backup destination was actually changed.

The module's tests exercise deterministic decision rules and malformed/adverse inputs. Real cloud services, physical site, access, egress, legal applicability, recovery, model performance and cloud licences are unverified. Reuse Module 08's identity/retention contract and Module 09's capacity evidence when planning real acceptance tests.
