# Module 01 — Facilitator solutions (not published on the learner website)

1. **Territorial and operational**: privileged support access can cross the operational trust boundary and may create transfer or disclosure concerns even when storage is local. Legal scope also needs qualified review.
2. **No.** Model licenses, hosting, remote operations, hardware, maintenance, training data and supply-chain dependencies can remain. Open source is a licensing characteristic, not a sovereignty guarantee.
3. Example: **Enterprise scope; workload-specific operational and territorial controls; hybrid deployment; inference/monitoring stages.** Other classifications are acceptable if justified.
4. Example: **“Production prompts and request logs from workload HR-001 remain in listed UAE regions; no unauthorized endpoint receives them under failover/support tests.”** Name tests, logs and owner.
5. **Worked real-product answer: Microsoft Foundry Models.** This is a hypothetical UAE procurement decision using a real, documented Microsoft deployment distinction. The Microsoft Foundry Models guide states, “Global types: May be processed in any Azure region.” See [Microsoft Learn, deployment types](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/deployment-types), verified 17 Nov 2026.
   - **What an executed vendor agreement can support:** It is direct evidence of the counterparty's *contractual undertaking*, such as specific retention, deletion, subprocessor or support obligations, **only if the signed clauses actually contain those terms**. It does not, by itself, establish performance or legal compliance.
   - **What the contract cannot demonstrate:** That the selected deployment is geography-restricted, that a given request stayed inside a prescribed location, or that diagnostics and failover logs have the same boundary.
   - **Specific product lesson:** Global processing and data stored at rest can have different regional boundaries. A location requirement must be matched to the actual deployment type and documented processing locations. The official description is evidence of the product's intended options, **not proof** of a specific customer's observed request path.
   - **PM evidence request:** (1) Signed applicable terms, (2) deployment SKU and region export, (3) provider product documentation for the exact SKU, (4) network and telemetry destinations, (5) administrative and support access paths, (6) a dated test of the declared geographic acceptance criterion and its limitations. If evidence is incomplete, narrow the claim or defer release.
   - **Likely reasoning error / RCA:** The team mistakes a legal commitment for an executed technical control. Root cause is an evidence-type mismatch in the acceptance criteria. Corrective action: separate legal, architecture, configuration and runtime evidence in the claim register. The named product and documentation are real; the enterprise and contract in this exercise are fictional.

6. **Detailed worked solution and RCA:**
   - **Before any monitoring or test:** Status = `UNVERIFIED`. Nothing shows that the claim is true or false. Absence of proof is not the same as a failed control.
   - **After a controlled failover test shows an out-of-bound endpoint:** Status = `FAIL` **if** the destination is confirmed outside the approved set, the test was valid, and the criterion applied to this failover path. Preserve the event ID, timestamp, endpoint, policy version, source system and reviewer. If the destination's classification is still disputed, use `REVIEW_REQUIRED` until resolved.
   - **Example five-whys RCA (fictional):** (1) Why did logs leave? Failover forwarded telemetry to an unapproved endpoint. (2) Why? The secondary environment inherited a default exporter configuration. (3) Why was it not blocked? Destination allow-list checks were absent for the telemetry channel. (4) Why was this missed at release? Tests covered normal inference paths but not failover/monitoring. (5) Why was coverage incomplete? Sovereignty acceptance criteria were not mapped to each lifecycle and operational path.
   - **Direct cause versus systemic cause:** Direct cause = secondary telemetry endpoint configuration. Systemic cause = no owned end-to-end egress test covering failover and observability. Do not infer these are the actual causes without configuration evidence; they are hypotheses to validate.
   - **Remediation plan:** Platform owner disables the out-of-scope exporter, restricts egress via policy, audits related destinations and backups, and adds failover tests to CI/release gates. Security reviews the capture and product/legal teams assess whether disclosure and incident processes apply.
   - **Retest and closure:** After a fix is committed, the claim remains `FAIL` (or open/nonconforming) until a fresh, documented test covers normal, failover and support paths with no prohibited flows. Then the accountable reviewer may change the claim to `PASS` **for the bounded test**, with evidence ID, date and next review. It is never proof of universal sovereignty.
   - **PM decision:** Block an unqualified sovereignty claim; accept a narrowly scoped exception only through an explicit owner, approval, expiry and revalidation plan.


7. **Hard-gate versus weighted-score challenge (fictional).**
   - **Regional managed endpoint: FAIL.** It sends inference and possibly derivatives beyond the mandatory single premises. Its 4.8/5 score is irrelevant because it is not an eligible option. A same-country region does not cure this failure.
   - **On-site model: UNVERIFIED / NOT APPROVED.** Physical placement is promising but the model-quality threshold, all derivative paths, operator access, backups, local capacity, licenses and recovery must pass documented tests before restricted production.
   - **Evidence to change status:** Named site and lifecycle inventory; synthetic egress and support/failover tests; task-specific blinded quality/safety benchmark with predeclared acceptance threshold; local cold start and restore; keys/identity and supplier-access review; dated reviewer sign-off. Record actual results and remaining unknowns.
   - **Air-gap override:** All inbound and outbound network connectivity, including allowlisted support, remote licence activation and cloud failover, is prohibited. Require offline signed artifact intake, removable-media custody, malware review, local logging, restore and rollback drills. If feasible on-site capacity or rights cannot be demonstrated, state **NOT FEASIBLE UNDER CURRENT CONSTRAINTS**, not a relaxed network rule.
   - **RCA if the managed endpoint was selected:** Direct cause is off-site inference; process cause is treating the mandatory premises boundary as a weighted preference. Correct by hard-gating before option scoring and retesting the full lifecycle.

## PM memo rubric (20 points)

- Scope and control dimensions (4)
- Dependency and architecture reasoning (4)
- Falsifiable claims and evidence plan (5)
- Balanced trade-offs and decision (4)
- Explicit uncertainty and exceptions (3)

**Anti-overclaim check:** Reject memos that use an averaged score to certify full sovereignty or cite NIST/OECD as endorsing this course's custom model.