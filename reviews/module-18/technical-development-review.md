# Module 18 technical, source and security development review

28 November 2026. Same-author AI-assisted self-review by the module author, Codex/GPT-6 agent; exact runtime model revision is not exposed. This is not an independent audit or different-model review. Independent review NOT COMPLETED. Module 04 remains HOLD. No production, physical-site or legal assurance is inferred.

## Scope and decisions inspected

Inspected the chapter, standard-library lab, adverse tests, retained observation, exit plan, separate solution key, diagram and public social derivative. The 14-section chapter covers the seven TOC topics. It distinguishes recovery objectives from observations, backup creation from restore, historical content from current retirement/authorization, format equality from model quality, count equality from field/tenant equality, declaration from physical evidence and current revocation from historic approval.

Hard premises/operator/connectivity/media conditions cover 17 protected artifact categories including OCR, speech, support, activation, updates, backup and failover. Known conflicts dominate unrelated missing evidence. Favorable declarations remain DECLARED_ONLY, never a verified physical air gap. The fixture has no network enforcement, authentic caller identity, trusted host isolation or actual service. Unknown fields cannot silently earn physical assurance.

`capture()` and `recover()` perform real file operations inside a fresh temporary directory in the demonstration. The live file is deleted before restoration. Backup bytes are checked against a process-memory digest; schema and unique IDs are checked; current retirement excludes d2 before file exposure. The restored digest is retained. Local staging and replacement are not crash durability or a distributed transaction. `migrate()` rechecks current retirement before parameterized SQLite insertion and verifies every returned record. This closes an initially identified window where a retirement change after restoration could otherwise migrate obsolete content. `substitute()` rechecks retirement and model revocation but is a deterministic filter, not a language model.

## Actual verification

Commands run from the repository root:

```bash
python3 labs/module-18/resilience.py
python3 -m unittest discover -s labs/module-18 -p 'test_*.py' -v
```

Actual final result: 20 tests passed, with additional subtests for all 17 external artifact paths. The retained `observed-resilience-run.json` shows live-file deletion before restore, d1/d3 restored, d2 excluded, two exact migrated records, tenant-a substitute returning d1, declared external failover BLOCKED and revoked model BLOCKED. No timing result, production RTO/RPO or model evaluation is manufactured.

Tests include integrity failure leaving live bytes unchanged, missing backup, incompatible schema even when its checksum matches, duplicate IDs, changed retirement before migration, incomplete declarations, remote/connected/media conflicts and current revocation. Peer review also identified revocation precedence under missing boundary declarations, unhashable malformed model references and bool/float schema coercion. Those now have regression tests: known boundary/revocation conflicts remain BLOCKED, malformed model references return UNVERIFIED, and the schema must be exact integer 1. These are synthetic process/file properties. No fault injection into actual cloud, physical facility, database service or key-management system occurred.

## Source check

Retrieved official primary sources on 2026-11-28 and located each short ledger extract in original text: NIST SP 800-34 Rev. 1 (May 2010), Appendix G p. G-2, Recovery Point Objective; NIST SP 800-53 Rev. 5 (September 2020, includes December 2020 updates), CP-10 p. 128; PostgreSQL 18 pg_dump, Description and Warning. The exact NIST text and PostgreSQL apostrophe/wording match the ledger. Each original source contributes fewer than 25 quoted words in the chapter. Source publication/version is kept separate from check date. PostgreSQL 18 is pinned, not claimed as latest; no PostgreSQL software is tested. NIST control text does not supply GCC legal applicability or certification.

## Risks and remaining work

The current retirement/revocation registry, expected digest and boundary declarations are editable process memory. An attacker controlling them can defeat these checks. No signature, authenticated provenance, append-only audit, encrypted backup, durable authorization, secure deletion or license verification is implemented. `Exercise` owns fixed filenames and should only receive a disposable directory, as the guide now states. Parameterized SQL avoids interpreting record text as SQL, but this is not a general untrusted-file ingestion service.

Actual model/domain/Arabic quality, rights/contracts, trustworthy evidence custody, real recovery capacity, independent security testing, physical air-gap and production RTO/RPO review remain NOT COMPLETED. Shared site build, final publication routes and deployed interaction belong to the coordinator. No shared build, commit, push or publication was performed by this author.

## Independent review prompt

Review all Module 18 assets as an independent reviewer. Try to revive a retired record during restore, migration and substitution; try a revoked model and a known external path combined with missing fields. Challenge digest trust, schema compatibility, migration equality, shared failure dependencies and evidence freshness. Identify any sentence overstating production RTO/RPO, physical isolation, legal applicability or independence. Run the lab/adverse tests and record exact environment, findings, reviewer identity/model/version/date and observed output. Preserve Module 04 HOLD and open production/manual gaps. Independent output is not present in this file.
