# Module 04 | Synthetic assessment scoring stress test (not independent calibration)

**Date:** 22 November 2026. **Author/reviewer:** GPT-6, same-model self-check. **Evidence class:** constructed examples and rubric interpretation only. **Release status:** HOLD. **Not:** a second human rater, different-model review, learner study, accessibility inspection, or measured inter-rater reliability.

## Purpose and constraints

The existing [learner Q1–Q6](../../chapters/04-uae-gcc-global-sovereign-ai-ecosystems.md) and [facilitator key](../../assessments/solutions/04-uae-gcc-global-sovereign-ai-ecosystems-solutions.md) define 40 points, with Q6 worth 18. This record tests whether two *fictional* contrasting responses can be scored transparently without letting high arithmetic marks override the FACTORY-A named-premises or OT-47 physical air-gap hard veto. No real student submitted either response. No code or browser tests were executed to create this record.

## Two synthetic Q6 submissions

**Submission A: articulate but unsafe (fictional).** “PLANT-47 was REVIEW REQUIRED. The gateway blocked the external ASR request, so there was no observed exfiltration. Root cause: remote speech fallback left enabled and sign-off inspected only local text inference. Disable the fallback, preserve gateway traces, and assign platform/security owners. Run tests on speech timeout, restart, update, recovery, and licence expiry. CISO and plant owner sign off. Because the firewall blocked the call, release the voice workflow provisionally. For OT-47, open a time-limited vendor support tunnel and permit cloud licence renewal.”

**Submission B: safety-preserving but incomplete (fictional).** “The attempted outbound ASR call means PLANT-47 is BLOCKED, even though the gateway denied delivery. The application still tried a forbidden path. Keep OT-47 UNVERIFIED, reject any network tunnel, and use manual lookup until a local voice package, backup and licence path can be evidenced. The direct cause is remote ASR fallback; systemic cause is approval of only the text model. CISO, plant owner, procurement/legal and Arabic evaluator should review the next test. I have not specified the evidence IDs, expected results, scheduled date or full owner-by-control register.”

## Explicit Q6 scoring under the existing key

| Rubric component | Max | A | B | Scoring rationale |
|---|---:|---:|---:|---|
| Correct state transitions | 3 | 1 | 3 | A retains original state but authorizes release despite adverse evidence; B blocks PLANT-47 and preserves OT-47 uncertainty |
| Attempt vs actual disclosure | 2 | 2 | 2 | Both distinguish denied attempt from proven delivery |
| Direct and systemic RCA | 3 | 3 | 3 | Both identify ASR fallback and text-only review |
| Containment and safe alternative | 2 | 1 | 2 | A disables fallback but permits unsafe release; B retains manual fallback |
| Corrective controls and owners | 3 | 1 | 1 | Neither maps every data/telemetry/backup/support/licence control to owner |
| Negative tests and dated plan | 3 | 1 | 0 | A names cases but lacks expected/actual IDs and scheduled date; B lacks test protocol |
| Closure authority and residual risk | 2 | 1 | 1 | Both name some approvers; neither gives complete residual-risk/reopen record |
| **Arithmetic total** | **18** | **10** | **11** | Illustrative same-model scores, not calibrated measurements |

**Mandatory separate disposition:** A = **RELEASE-BLOCKING** despite 10/18 because it expressly permits a prohibited OT-47 tunnel/cloud licence and approves a still-failing PLANT-47 application path. B = **NOT RELEASE-READY** despite preserving hard gates: incomplete test evidence, date and ownership cannot be interpreted as a pass. Neither answer earns a production approval. A higher score in another question cannot offset the veto.

## Ambiguities revealed and proposed assessor instructions

1. **Veto versus points:** retain the numeric mark for instructional feedback, but record a distinct `release_eligibility = BLOCKED` field. Do not convert veto to zero automatically; this separates knowledge gaps from unsafe authorization. Facilitator should flag the exact prohibited statement and boundary.
2. **Gateway containment:** award observation credit for saying *delivery was not evidenced*; do not award application-control credit for a denied request. An attempted forbidden call is an adverse test for the application even when the network gate behaves correctly.
3. **Unknown vs failed:** OT-47 remains UNVERIFIED if no physical test was performed, but a proposed tunnel is an inadmissible design; if actually configured it becomes BLOCKED. Assessors should distinguish proposal from observation.
4. **Dated plan:** award full retest credit only with a *future scheduled or explicitly to-be-scheduled date*, test IDs, expected/actual evidence fields, owner and negative paths. Never demand invented completed test dates.
5. **Control inventory:** require distinct locations and owners for ASR, OCR if used, embeddings, prompts, logs, telemetry, backup, licence, remote support, recovery and removable media; `NOT USED` is valid if justified.
6. **Arabic quality:** native-speaker evaluation is necessary for the language acceptance argument but never substitutes for network/physical assurance.

## Follow-up independent calibration protocol (NOT EXECUTED)

Provide both anonymized fictional responses, learner questions and facilitator rubric to **two actual independent raters** (human or separately identified model instances with provenance), blind to the illustrative scores above. Ask each to score all seven Q6 components, quote the exact evidence for every point and independently apply the hard veto. Capture rater identity/type, date, model/version if applicable, scoring sheet and disagreements. Compare per-component absolute differences; resolve any difference of 2 or more points and *every* disagreement about a hard veto before finalizing the rubric. A consensus note should state whether the disagreement required rubric edits. A single GPT-6 pass cannot satisfy this requirement.

## Release disposition

This is an authored **self-stress-test**, not completion of E04-03. The separate editorial/accessibility/assessment review remains HOLD. E04-02 still requires manual zoom, keyboard/screen-reader and PDF reading-order inspection; T04-03 still has three source records unresolved. No physical inspection or legal certification is implied. Next action: secure independent scoring evidence, then reconcile review gates; Module 05 §5.1 remains blocked.
