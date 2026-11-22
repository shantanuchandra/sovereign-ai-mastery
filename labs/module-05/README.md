# Module 05 | Legal-control-evidence mapping lab (synthetic)

**Status:** DRAFT, unpublished; Module 04 release gate is still HOLD. This lab is an engineering and product-reasoning exercise, **not legal advice, official source authentication, physical air-gap proof or compliance certification**.

## Goal and baseline

Given six **fictional** activities (UAE mainland, DIFC, ADGM, KSA, named-site factory and air-gapped archive), link a legal *candidate* to a named control, accountable owner, test ID, handling boundary and proposed decision. Unknown legal applicability must stay open; no hard physical boundary may be waived by a regional cloud claim, favourable score or firewall containment.

Requires Python 3.10+ standard library only, no model, network, cloud account, GPU, API key, Docker or real customer data. Compatible with the course's Apple M4 Pro 16 GB baseline; no hardware-specific dependencies. No paid resources; cleanup consists of deleting temporary mutated JSON copies. Do not paste real contracts or protected records into this public repository.

## Inputs

- [control_map.json](control_map.json): six synthetic cases, official-source URLs treated as references and **not** dereferenced by the script, and explicit legal status.
- [validate.py](validate.py): schema, provenance, owner and fail-closed boundary checks.
- [test_validate.py](test_validate.py): standard-library unittest cases, including negative-path mutations.
- [Chapter 05](../../chapters/05-laws-regulation-jurisdiction.md): human-readable interpretation and current source caveats.

The worksheet's URL is not evidence of legal applicability. Even an APPROVED legal-review flag is only a fictional schema value; **the code does not check a real lawyer's identity or signature**, so it cannot authorize production.

## Execute

~~~bash
python3 --version
python3 labs/module-05/validate.py labs/module-05/control_map.json
python3 -m unittest discover -s labs/module-05 -p 'test_*.py' -v
~~~

The baseline should return a JSON report marked **SYNTHETIC_SCHEMA_VALIDATED_ONLY**, with six entries, four unresolved legal-counsel states, five HOLD cases and one synthetic-only pilot. Unit tests are designed to reject fabricated approval, missing source sections, unowned controls, offsite processing/backups, licence activation and any forbidden air-gap network path. **These are expected outputs, not claimed observed local executions.** Save actual command output in the run report when tests are performed.

## Manual fault injection

1. Copy the JSON fixture to a temporary location, not over the baseline.
2. Change GC-02 decision from HOLD to APPROVED without adding verified legal review: expect validator **exit 1** with pending-counsel error.
3. Restore; set PLANT-05 backup to UAE-REGION-B: expect **exit 1** for named-premises violation.
4. Restore; add OT-05 network path PRIVATE-LINK: expect **exit 1** even if it is inside UAE.
5. Restore; switch OT-05 licence_mode to ONLINE_REQUIRED: expect **exit 1** for forbidden dependency.
6. Re-run unchanged baseline and record the accepted synthetic-schema-only result.

**Evidence sheet:** commit SHA, tester, timestamp, Python version, case and mutation, command, expected and actual exit code/message, corrected artifact path, residual gap, review owner. A blocked gateway request establishes containment only, not app conformance.

## Design limits

The tests cannot validate external URLs, determine controller/processor roles, read statutes in their authoritative language, decide current amendments, prove whether logs contain personal data, verify signed contracts, inspect physical network interfaces or certify actual premises. A **manually observed** support/access/backup trace and a **qualified legal applicability decision** are separate release gates.

**Next work:** add a reference source-version tracker, run tests via an isolated draft CI workflow, have a truly independent reviewer challenge the Q6 scoring rubric and conduct rendered accessibility tests before module promotion.
