# LinkedIn post draft

What would your AI assistant restore after an outage: the last backup, or the last state it is still authorized to serve?

An old backup can contain retired documents, revoked model references and obsolete permissions. Restoring those bytes can recreate a control failure even when the integrity check succeeds.

Module 18's synthetic exercise deletes a real local file, restores eligible records, migrates JSON into SQLite and checks tenant filtering with a deterministic substitute. It preserves the current retirement of d2 and denies a declared external failover path. It runs locally with Python's standard library.

The result is narrow evidence. It does not measure production RTO/RPO, prove physical isolation, evaluate a language model or supply an independent audit. PostgreSQL's documented warning about code execution during dump restoration is a useful reminder to review the trust of the recovery source itself.

Which dependencies would your exit plan need to recover: data, permissions, model/runtime, keys, activation, support or all of them? Who owns the next dated retest?

Educational draft, not legal advice or production approval. BANK-A is fictional; Module 04 remains HOLD. Independent/manual review pending. Sources checked 28 November 2026: NIST SP 800-34 Rev. 1, NIST SP 800-53 Rev. 5 CP-10 and PostgreSQL 18 pg_dump. Full source ledger and actual bounded observation accompany the lesson. Review public links and export the untagged PDF before posting; HTML is preferred.

#SovereignAI #AIProductManagement #Resilience #VendorExit
