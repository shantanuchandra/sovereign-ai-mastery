# Module 08 local data lifecycle lab

**Educational draft, synthetic data only.** Build and inspect an actual local SQLite ingestion/retrieval pipeline. This is a lexical toy, not a neural embedding model, access gateway, anonymization system or production erasure tool.

## Environment and execution

Python 3.11+ standard library with SQLite foreign-key/backup support; CPU only, no Docker, model download, cloud account or paid resource. Default target: Apple Silicon/16 GB. Verified with Python 3.13 on macOS. Preparation means obtaining the public code; execution uses no external request. Allow 90 minutes for execution and lifecycle mutations.

```bash
python3 labs/module-08/pipeline.py
python3 -m unittest discover -s labs/module-08 -p 'test_*.py' -v
```

The demo creates an owned directory inside a temporary folder, ingests four fictional records, retrieves a tenant-A document, snapshots the database, retires that document, restores the old snapshot and reapplies the deletion ledger. It reports `before_count: 1`, retirement `UNVERIFIED` while a registered backup exists, and `after_restore_count: 0`. It removes its registered snapshot and cleans the temporary directory. No cleanup bill or external resource remains.

The fixture clock is explicitly **2026-11-26**, not the machine's current date. Expiry on 2026-12-01 is exclusive: queries at or after that date exclude the document even before physical row deletion. A real application needs an authenticated service clock; clients must not choose their own retention time.

## What is actually implemented

`store.sqlite` contains document metadata and child chunks with term-frequency vectors. `ledger.sqlite` separately holds tombstones, a known-backup inventory and metadata-only events. Both remain protected artifacts. A content hash ties each result to the canonical source representation; it neither authenticates the publisher nor anonymizes the content.

Four formats are accepted: text, string-valued structured records, **pre-written synthetic OCR text**, and **pre-written synthetic transcripts**. No image recognition, speech recognition or real multimodal model is executed. Arabic token matching is exercised, without a claim of semantic or dialect understanding.

The caller supplies a trusted tenant ID; SQL restricts rows before scoring or returning excerpts. **The lab does not authenticate callers.** A production gateway must derive tenant scope from a verified identity and enforce authorization on all operations, including ingestion, query, retirement, backup and restore. Do not expose this library as a public API.

Vectors are token counts whose dictionary keys reveal words. Classification is inherited through the document/chunk join; changing representation is not declassification. Logical retirement writes a durable tombstone first, deletes matching live documents and cascades to child chunks/vectors. Query and restore also check the ledger. Removing the ledger while a live store exists fails closed. This is a bounded single-process teaching model, not a proven distributed crash-recovery protocol.

## Experiments and acceptance

1. Inspect the fixture and identify owner, tenant, classification, source/preprocessing site, transport and expiry.
2. Query `pump pressure` separately for `plant_a` and `plant_b`. Show that tenant-B excerpts do not appear in tenant-A results. Do not confuse a supplied scope with authenticated identity.
3. Inspect chunk IDs, source hashes and inherited classifications. Compare a lexical synonym with an exact-token query; explain why this is not semantic evaluation.
4. Change a declared site, country or preprocessing destination; the ingest must reject the conflict before any document row is written. Online transport is rejected under the default physical-air-gap scenario.
5. Observe expiry filtering, then run `expire`. Check that child chunks/vectors disappear through the foreign-key relationship.
6. Create a registered snapshot before retirement, retire the source, restore that snapshot and show that the tombstone prevents retrieval resurrection. Confirm tenant B still works.
7. Remove only the registered owned snapshot. State what is still unknown about filesystem snapshots, external copies, storage media and privileged access.

Nineteen tests cover the above behavior, malformed policy/expiry, duplicate-ingest rollback, metadata-only logging, safe snapshot names, unowned directories, symlink rejection and historical restore. Submit the output, a lineage table, one negative test and the [data-control specification](CONTROL_SPEC.md).

## Residency and deletion limits

The program checks declared source/preprocessing locations and creates its artifacts under an owned root. It cannot determine whether that root sits on a cloud-synced folder, remote mount or replicated disk. Actual geographic and physical-site evidence requires infrastructure inspection. Protect prompts/queries, source records, vectors, excerpts, audit IDs, diagnostics, backups, support copies, activation, updates and failover as required by the unchanged architecture boundary. No support or activation service is implemented here; absence from this demo does not prove absence from a deployment.

Deletion is **logical removal from live tables and known owned backup files**, never certified secure erasure. SQLite journals, free pages, filesystem snapshots, external copies and physical media are not comprehensively assessed. A `REVIEW_REQUIRED` result after known backups are removed still needs human review; it does not mean all copies are gone. Losing or bypassing the ledger can defeat the lab's restore protection; protect and independently recover it in a real design.
