# Module 08 facilitator solutions and scoring rubric

Author-generated educational draft, 27 November 2026. Keep excluded from the public reader build. Independent assessment NOT COMPLETED; source-repository visibility is not confidentiality.

## Q1. Derivatives and provenance (5 points)

Queries/excerpts can contain restricted content; vectors, hashes and metadata can reveal words, linkage or operational context (2). The lab's word-count keys directly show why its vectors are not anonymous (1). Source hashes link canonical content but do not authenticate the publisher or establish processing authority (2).

## Q2. Tenant filtering (5 points)

SQL restricts the supplied tenant before scoring/excerpt selection (2). The caller can supply a tenant string, so the library itself does not authenticate or authorize a user (1). A production gateway must derive scope from verified identity and enforce it for ingestion, retrieval, deletion, snapshot and restore, with privileged-access review (2). Do not award full tenant-isolation assurance from this test.

## Q3. Retention (5 points)

The fixture expiry is exclusive: no eligible result on 2026-12-01 (2). Live purge, child chunk/vector removal, known backups, current tombstones during restore and unknown copies need separate observations (2). A trusted service clock and qualified review of actual retention/hold rules remain necessary (1). No statutory period is prescribed by the course fixture.

## Q4. Preprocessing boundary (5 points)

Off-site OCR conflicts with unchanged factory-only handling of protected artifacts/derivatives (2). Hold the proposal or arrange a separately authorized policy change; do not silently substitute country residency (1). Inspect on-site parser runtime, temporary files, diagnostics, update/activation, failure/fallback and recovery paths, and test Arabic task quality (2). Local final inference alone is insufficient.

## Q5. Actual product behavior, hypothetical application (5 points)

SQLite's documented backup operation creates a snapshot of source state (1). A pre-retirement snapshot can therefore contain content absent from later live tables (1). The course application preserves a separate tombstone ledger, filters retrieval against it and reapplies retirement after restore; this is application behavior tested locally, not SQLite's automatic retention policy (2). Physical remnants, external copies, storage snapshots and comprehensive secure erasure remain unproved (1).

Source: SQLite project, *SQLite Backup API*, §1, https://www.sqlite.org/backup.html. Inspected 2026-11-27. The course scenario is not a reported SQLite customer incident or defect claim.

## Q6. Root-cause analysis and bounded closure (15 points)

1. **Observation/state (3):** Begin UNVERIFIED for undocumented vector/backup behavior. Observed retrieval of expired content after restore is a failed acceptance criterion and blocks release. Preserve the query, build, fixture clock, lineage and restore sequence without leaking real content.
2. **Direct cause (2):** Investigate eligibility filtering against expiry and tombstones, restoration of old rows, and ledger replay before serving. Do not infer that a hidden UI excerpt repairs access to the record through other paths.
3. **Systemic cause (2):** A source-only deletion contract, missing derivative/replica inventory and incomplete restore testing allowed the proposal to escape review. Treat these as course-case hypotheses requiring evidence, not findings about a real organization.
4. **Containment/owners (2):** Accountable release authority keeps retrieval stopped or in approved synthetic use. Data steward owns lifecycle policy; platform/recovery owner repairs restore behavior; security owns identity-derived tenant enforcement. Use the approved manual fallback.
5. **Repair/retest (3):** Preserve the retirement ledger independently, filter eligibility before scoring, remove live derivatives and disposition known copies. Plan a dated retest, for example 2026-11-30, of expiry boundary, wrong tenant, source/chunk/vector rows, reopen, old-snapshot restore, missing ledger, known-copy retirement and relevant infrastructure paths. A plan is not completed evidence.
6. **Closure (3):** Repeated adverse results remain blocked. Corrected behavior with missing evidence remains UNVERIFIED. Favorable bounded synthetic tests support REVIEW_REQUIRED, not authentication, anonymity, secure erasure or legal compliance. Record residual risks, scope, owner and review trigger. Renaming a vector or hiding an excerpt changes no underlying eligibility rule.

**Total 40 points.** Illustrative course knowledge threshold 24/40. Invented evidence, a hard-boundary override or unsupported anonymity/erasure claim requires remediation regardless of score. This is not an external qualification.

## Lab and PM rubric

Run all 19 tests and the temporary-directory demo. Observe one tenant-A result before retirement, UNVERIFIED while a registered snapshot exists, and zero after restore with tombstones reapplied. Check tenant B remains eligible under its supplied scope. Removing a registered file is bounded known-copy disposition; no global deletion claim follows.

The separate data-control specification has a 20-point rubric: classification/ownership 4, lineage/scope 4, retention/deletion/restore 6, physical/network boundaries 4, bounded decision/trigger 2. Require 12/20 plus remediation of hard-gate or assurance overclaims. The logging scenario needs a justified purpose, minimization, identity/access, retention/hold review and an accountable approval, not an automatic indefinite-retention feature.
