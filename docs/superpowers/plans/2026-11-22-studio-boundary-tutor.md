# Studio boundary and tutor increment

Goal: extend the existing static Studio with workload-specific data-flow review and targeted practice after a missed decision.

Architecture: retain the browser-only deterministic engine, ten shared dropdown taxonomies and existing storage key. Add generated flow records to each blueprint and one follow-up per missed concept. Keep first answers and follow-up answers separate; invalidate quiz answers after a rules-version change while retaining assumptions and reflections.

Constraints: no external model or new production dependency; no legal or vendor acceptance claims; premises-only includes every restricted derivative; physical air gaps permit no network; blocked inputs remain blocked in every output.

- [x] Add failing behavior tests for flow boundaries, six new workloads/scenarios, remediation and exports.
- [x] Implement engine records and targeted follow-ups; keep all prior scenario values valid.
- [x] Render the flow register and remediation, persist valid answers and export both attempts.
- [x] Verify engine tests, built-site browser interactions, mobile layout, reload and downloads; add the browser check to CI.
- [ ] Update Studio documentation and record verified results; publish a reviewable branch and pull request.

Review focus: contradictory physical boundaries; speech/OCR hidden dependencies; offline licence/update paths; stale or malformed saved answers; first-attempt history surviving successful follow-up practice.
