# Which copies survive when enterprise data is retired?

A fictional factory assistant retires a manual. The live record disappears, but an older snapshot still contains its chunks and word-count vectors. What happens after recovery?

SQLite documents its Backup API as creating a snapshot.[^backup] In the hypothetical course application, we keep a separate retirement ledger and reapply it after restoring the snapshot. That is application policy, not an automatic retention feature.

Three questions for a data-control review:

- Do tenant and expiry checks run before ranking or returning excerpts?
- Which derivatives and recovery copies follow the source retirement decision?
- What remains unproved about unknown copies, authentication and physical erasure?

Module 08 includes a synthetic, CPU-only pipeline, 19 tests and a reusable data-control specification. Its vectors are lexical word counts; they do not anonymize the text. All examples are fictional. Educational draft; independent assessment and manual accessibility review pending.

[Read the lesson](../../chapters/08-data-sovereignty-engineering.md) and explore the [eight-question HTML deck](CAROUSEL.html).

[^backup]: SQLite project, *SQLite Backup API*, section 1, https://www.sqlite.org/backup.html. Verified: 2026-11-27. The course application is hypothetical; no customer incident or production erasure claim is asserted.
