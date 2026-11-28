# Module 18 synthetic restore and exit exercise

Educational draft, 28 November 2026. Standard-library Python 3.11+, local synthetic data only. No production RTO/RPO, real model, physical isolation, compliance or independent audit is demonstrated. Module 04 remains HOLD.

## Run and inspect

From the repository root:

```bash
python3 labs/module-18/resilience.py
python3 -m unittest discover -s labs/module-18 -p 'test_*.py' -v
```

Allow 60–90 minutes to inspect implementation and adverse tests, plus the distinct PM artifact. No cloud, accounts, GPU, Docker, secrets, downloads or paid resources are required. Running the first command regenerates [observed-resilience-run.json](observed-resilience-run.json). It contains actual deterministic results, not an expected-output mock. Temporary exercise files are removed on completion.

## What happens

`capture()` writes a real local live file and backup containing three invented records. The process retains its expected SHA-256 in memory. The demonstration then adds d2 to the current retirement set and deletes the live file. `recover()` checks complete declared premises/operator/air-gap/media conditions, current model revocation, backup presence, integrity and schema. It excludes currently retired records before replacing the live file through a staging file. This is a real local restoration of eligible bytes, not a remote recovery or a distributed transaction.

`migrate()` imports the remaining records using parameterized inserts into a real temporary SQLite file. It compares every field and tenant identifier after reading the destination. There are two eligible records, d1 for tenant a and d3 for tenant b. `substitute()` is a deterministic list filter, returns only d1 for tenant a, and rechecks current retirement/model revocation. It is not an LLM or quality evaluation.

The fixed exercise directory owns `live.json`, `backup.json`, `restore.stage` and `migration.sqlite`. The demonstration always uses a newly created temporary directory. Do not point `Exercise` at a directory containing files you want to preserve: capture and migration replace those fixed exercise filenames. The implementation is educational code, not a hardened untrusted-input file service.

## Adverse checks

The 20 tests cover actual restore, current retirement, each protected artifact routed externally, missing paths, conflict dominance, operator/connectivity/media conflicts, unknown declarations, tampered bytes, missing backup, incompatible schema despite matching checksum, duplicate IDs, revoked models despite missing boundary evidence, malformed model references without exceptions, exact integer schema checks, exact migration equality, retirement changes before migration, tenant filtering and retained-observation behavior. Parameterized subtests inspect all 17 artifact categories.

Acceptance requires that an integrity failure does not replace the existing live file, a known external path is BLOCKED even with unrelated missing fields, missing declarations are UNVERIFIED, and favorable declarations remain DECLARED_ONLY. These are tested fixture properties. A BLOCKED result does not prove an actual external transfer occurred; it identifies a declared conflict.

## Limits and extensions

The expected digest and current retirement/revocation registries are editable process memory. Hash equality is not authentication, immutable logging, license verification or trusted provenance. The fixture does not encrypt files, protect keys, implement caller identity, enforce host networking, recover from power loss, retain a durable journal or prove a physical air gap. Atomic local replacement alone is not crash durability. Migration checks format equality, not embeddings, language quality, complete database state or service capacity. No elapsed-time statistic or business RTO/RPO is asserted.

A useful extension is a separately reviewed durable retirement registry and crash-recovery journal with trusted operator identity. Keep original failed observations visible. Complete [EXIT_PLAN.md](EXIT_PLAN.md), assign production/physical/rights/domain review gaps and return to the [chapter](../../chapters/18-resilience-audit-vendor-exit.md).
