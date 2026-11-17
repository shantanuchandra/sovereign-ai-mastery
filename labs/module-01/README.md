# Module 01 lab — can the sovereignty claim be tested?

**Goal:** Create and validate structured claims. This is a **schema exercise**, not an actual sovereignty or legal audit.

1. Open [`claims.json`](claims.json). Add a third claim for **technological** independence that includes model portability.
2. Run `python3 validate.py claims.json` from this directory.
3. Run `python3 -m unittest discover -v` to execute structural checks.
4. Edit the evidence object to simulate a dated test. Observe that the result becomes `REVIEW_REQUIRED`, **not** `COMPLIANT`.
5. Write three additional tests you would need to gather authentic evidence from a real architecture.

**Expected states:** `INVALID` means the claim schema is incomplete, `UNVERIFIED` means adequate dated test evidence has not been supplied, and `REVIEW_REQUIRED` means a claimed test record must be independently reviewed. No software-only result here proves sovereignty.

**Safety:** Use fictional data. This repository is public. Never commit credentials, real internal access logs, customer data or sensitive notes.