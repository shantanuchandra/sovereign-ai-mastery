# Module 08 data-flow and data-control specification

Course-authored template, 27 November 2026. Fictional workload; no legal opinion or production assurance.

## Decision and scope

Name the workload, intended use, accountable business owner, data steward, platform operator, privacy/security reviewers and review expiry. Reuse the Module 07 component/path IDs and Module 06 control IDs. State the exact physical site/country rule and connectivity constraint; an off-site domestic replica is still outside a factory-only boundary.

## Artifact and lineage register

| Artifact | Parent/transform | Owner and tenant | Classification | Retention/retirement evidence |
|---|---|---|---|---|
| Source record | Issuer, purpose and provenance | Fill | Fill | Start/event, expiry, holds |
| Chunk and token vector | Source ID/hash, algorithm/version | Inherit and review | Inherit unless justified change approved | Live-row removal and orphan check |
| Query and excerpt | Request/context/result | Derived identity scope | Treat as protected if content requires | Logging and output policy |
| Audit/tombstone metadata | Document and event IDs | Authorized operator | Metadata can be sensitive | Minimum retained fields and authorized duration |
| Snapshot/replica | Database/build/time | Recovery owner | Preserve parent restrictions | Inventory, restore test and disposition |

## Required controls

Define the authorized intake purpose, acceptable formats, schema checks, prohibited destinations and missing-data behavior. Record every transformation, temporary copy and export. Derive tenant authorization from identity in production; never accept an untrusted tenant string as authority. Keep logs free of raw content unless an explicitly reviewed purpose requires otherwise.

For retention, specify the clock/event, duration, legal/contractual questions, hold authority, expiry action, replicas, tombstones, ledger recovery and restore behavior. The lab does not implement legal holds or determine retention periods. A real hold/deletion conflict must go to qualified reviewers; do not overwrite the policy silently.

List negative tests for wrong tenant, off-site preprocessing, expired retrieval, derived-vector deletion, old-snapshot restoration, missing ledger and unknown backup destinations. Assign an owner, criterion, build/date, observation and retest to each. Declare remaining unverified infrastructure and copies.

## Executive decision and rubric

Compare a local controlled pipeline, a separately scoped managed alternative and a manual fallback. Apply hard gates before cost/performance preferences. Record assumptions, residual risk, source limits and change triggers.

Illustrative 20-point rubric: artifact classification/ownership (4), lineage and authorized scope (4), retention/deletion/restore evidence (6), physical and network boundaries (4), bounded decision and review trigger (2). A hard-boundary override or unsupported anonymity/erasure claim requires remediation irrespective of score. This rubric is educational, not an external certification.
