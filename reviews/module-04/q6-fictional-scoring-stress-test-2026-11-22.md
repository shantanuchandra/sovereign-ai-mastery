# Module 04 Q6 rubric stress test: two fictional submissions

**Date:** 2026-11-22. **Author/rater:** GPT-6, single-model self-calibration exercise, NOT independent assessment calibration. **Source:** Module 04 Q6 prompt and separate facilitator key at `assessments/solutions/04-uae-gcc-global-sovereign-ai-ecosystems-solutions.md`. These are invented learner responses, not real student submissions. Keep this file in `reviews/`, not the public learner chapter or social assets.

## Test A: strong evidence-led response (fictional)

> “PLANT-47 starts REVIEW REQUIRED and becomes BLOCKED after an attempted remote ASR call; gateway logs show denial, not successful exfiltration. OT-47 stays UNVERIFIED until on-site inspection. Direct cause is an enabled ASR fallback; systemic cause is a text-only sign-off and unowned dependencies. Disable voice, preserve sanitized trace/config hashes and allow a manual workflow only. Security and plant operations must inspect model, ASR, retrieval, telemetry, backups, support, licence and physical paths. Schedule a future normal/timeout/restart/update/restore/licence-expiry/denied-egress test, with owners and expected/actual evidence IDs. CISO, plant owner, legal/procurement, Arabic evaluator and PM sign the release board. Reopen only after evidence is reviewed.”

| Q6 criterion | Max | Awarded | Reason |
|---|---:|---:|---|
| State transitions | 3 | 3 | Both workloads retain correct non-approved states |
| Observation vs disclosure | 2 | 2 | Attempt and denial distinguished from exfiltration |
| Direct and systemic RCA | 3 | 3 | Adapter misconfiguration and governance failure named |
| Containment and alternative | 2 | 2 | Voice disabled, sanitized evidence and manual fallback |
| Controls and owners | 3 | 2 | Lists boundaries but does not individually assign each owner |
| Retest and dated plan | 3 | 2 | Future scheduling mentioned but no explicit date-to-be-scheduled field |
| Closure and residual risk | 2 | 1 | Authorities named but residual risk/rollback trigger implicit |
| **Total** | **18** | **15** | **No hard veto violated; strong but incomplete** |

## Test B: persuasive but unsafe response (fictional)

> “The 100% local model metric and successful gateway block show sovereignty. Approve PLANT-47 with a cloud ASR fallback in the UAE because it remains in-country. Approve OT-47 using a temporary vendor support tunnel for licence renewal. The vendor benchmark demonstrates Arabic accuracy. The team can investigate backups later.”

| Q6 criterion | Max | Awarded | Reason |
|---|---:|---:|---|
| State transitions | 3 | 0 | Converts unknown and adverse evidence into approval |
| Observation vs disclosure | 2 | 1 | Notes denial but treats it as application correctness |
| Direct and systemic RCA | 3 | 0 | Neither cause investigated |
| Containment and alternative | 2 | 0 | Leaves prohibited voice path active |
| Controls and owners | 3 | 0 | No owner or full dependency inventory |
| Retest and dated plan | 3 | 0 | No falsifiable retest |
| Closure and residual risk | 2 | 0 | No valid authority or risk statement |
| **Total** | **18** | **1** | **HARD VETO: off-premises ASR and connected OT tunnel; release-blocking regardless of points** |

## Scoring ambiguities exposed

1. The rubric's “dated plan” criterion must accept an explicit **date to be scheduled** and reject invented completed tests; do not demand a fabricated calendar date.
2. An answer that lists all components but omits control ownership should not receive full controls/owners credit.
3. A firewall denial can earn limited observation credit but never locality approval; distinguish attempted and delivered data.
4. Record **numeric score** and **hard-veto release disposition** in separate fields. An unsafe answer is BLOCKED even if other rubric points are earned.
5. A real inter-rater calibration needs two genuinely separate assessors, identical anonymized submissions, blinded scoring, disagreement analysis and an adjudicated rubric. This single GPT-6 exercise does not satisfy E04-03.

**Checks performed:** Manual comparison of both invented answers to the existing Q6 18-point rubric; arithmetic checked (15/18 and 1/18). No learner study, independent rater, browser, Python or assistive-technology test performed. **Gate:** E04-03 remains OPEN; Module 04 remains HOLD.
