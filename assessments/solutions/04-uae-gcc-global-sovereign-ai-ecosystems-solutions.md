# Module 04 | Facilitator solutions and decision-assessment rubric

> **Facilitator-only.** This public GitHub source is deliberately excluded from the learner-facing website. All enterprise workloads, scores, incident details and test IDs below are **fictional or synthetic**. The named TII product announcement is real, but no supplier or real-world air-gap capability is certified here. This rubric is a GPT-6 authored teaching aid, not an independently calibrated assessment.

**Learner assessment:** [Module 04 Q1–Q6](../../chapters/04-uae-gcc-global-sovereign-ai-ecosystems.md)  
**Lab:** [Synthetic GCC evidence-map lab](../../labs/module-04/README.md)  
**Ontology:** [Course-authored ontology](../../taxonomy/ONTOLOGY.md)  
**Scoring:** Q1–Q4 = 4 points each; Q5 = 6; Q6 = 18; **total 40**. PM board pack = separate 20 points. Any recommendation that permits forbidden off-premises PLANT-47 processing or any network path for OT-47 must be marked **release-blocking** irrespective of numerical score.

## Q1. Strategy is not a deployment certificate (4 points)

**Worked reasoning:** UAE national strategy is a policy direction, not a signed approval of an enterprise's specific supplier, system or restricted data flow. The buyer must identify the exact workload, processing and derived data, contract and jurisdiction, and the accountable authority. A “sovereign” label is an unverified supplier claim until backed by site inventory, privileged access, subprocessors, support/backup routing, tests and binding contractual controls. A non-AI FAQ search or manually curated knowledge base is a legitimate baseline.

**Award one point each:** policy versus approval; workload-specific control authority; supplier claim versus verified evidence; concrete evidence and non-AI alternative. No points for claiming a national plan automatically waives a sector-specific rule.

## Q2. Four-jurisdiction evidence map (4 points)

| Market | Evidence issuer and limited scope | Missing decision evidence and owner |
|---|---|---|
| UAE | UAE National AI Strategy 2031: national direction, not vendor certification | Enterprise data classification, regulator/legal applicability, processor contracts; local counsel and privacy |
| Saudi Arabia | SDAIA strategy and published PDPL/transfer materials: issuer policy and law sources with applicability to be reviewed | Actual controller/processor, transfer circumstances and sector requirements; Saudi counsel/privacy |
| Qatar | HBKU/QCRI national AI strategy material: research/policy framing | Buyer-specific data rights, hosting and sector conditions; Qatar legal and enterprise security |
| Bahrain | Government General AI Policy: government-entity scope must be read carefully | Whether any private-sector obligations separately apply; Bahrain counsel and procurement |

**Award:** 1 for four genuinely distinct issuers/scopes; 1 for avoiding a fictitious GCC passport; 1 for buyer-specific unknowns; 1 for named reviewers. Do not infer uniform cross-border approval from membership in a regional organization. Sources and issuer dates must be supplied from the chapter evidence ledger, not invented.

## Q3. Eligibility-first architecture (4 points)

| Fictional workload | Connected managed inference | On-site local inference | Physically disconnected package |
|---|---|---|---|
| Public FAQ | Conditionally eligible after content, rights, retention and supplier checks | Eligible if justified by cost and operations | Usually unnecessary; capacity and maintenance burden |
| FACTORY-A confidential design | **Blocked** if any processing, derivatives, support, logs or backups leave named premises | **Unverified** until all component paths, local rights and recovery tested | Potentially eligible but still needs rights, operations and capacity evidence |
| OT-47 no-network terminal | **Blocked** | **Blocked if any network path exists**, even to a private gateway | **Unverified** pending physical inspection, offline licensing, restart and recovery |

**Award:** 1 for three-workload differentiation; 1 for named-site versus country distinction; 1 for no-network OT hard gate; 1 for dependencies plus a falsifiable retest. A score cannot override an explicit prohibited path.

## Q4. Arabic evaluation is multi-component (4 points)

**Illustrative six slices, not measured performance:** (1) MSA retrieval with citations, (2) Emirati dialect intent, (3) Arabic-English mixed utterance, (4) invented asset ID and numeral exact-match, (5) local speech transcription under noise/timeout, (6) clean restart/ASR outage with no cloud fallback. Every row should record synthetic input ID, expected intent/entity, native reviewer, severity, model/version, destination trace and evidence state. Include OCR and embeddings if present; if absent, mark NOT USED rather than inventing verification. A text model's vendor-reported benchmark cannot establish voice, transcription, OCR, logging, backup or support locality.

**Award:** 1 for six balanced slices; 1 for critical entity/native-speaker criteria; 1 for all-component destinations and denial tests; 1 for unknown-versus-tested distinction.

## Q5. TII product announcement, fictional industrial buyer (6 points)

**Real source anchor:** Technology Innovation Institute, [official Falcon-Emirati, speech and visual-text announcement](https://www.tii.ae/news/tii-launches-falcon-emirati-alongside-new-arabic-ai-models-speech-and-visual-text), dated **6 October 2026**; issuer source referenced and inspected in Module 04 §4.7 on **22 November 2026**. This is a product announcement, **not** evidence of an approved FACTORY-A deployment or independent reproduction of performance claims.

**Worked recommendation:** **Do not approve production deployment yet.** Investigate conditionally only if procurement can establish rights for offline local execution, pinned model/artifact integrity, language task suitability, component inventory, and absence of any external ASR/OCR/translation/retrieval/telemetry/logging/support/backup/licensing path. A CISO and FACTORY-A data owner must accept the named-site evidence; procurement/legal must verify rights and contracts; native-language reviewer must verify domain quality. Negative tests: force ASR timeout and verify **no remote fallback attempt**; run clean offline restart/licence-expiry and confirm no network activation or unsafe silent failure. Test a recovery/backup restore without offsite derivatives. If any required external path is unavoidable, mark **BLOCKED** or **NOT FEASIBLE UNDER CURRENT CONSTRAINTS**, not “conditionally approved.” A signed architecture and independent-in-purpose network trace showing all required processing inside FACTORY-A could support later re-review, but never proves physical isolation for OT-47 by itself.

**Six-point rubric:** 1 named product/issuer and exact claim boundary; 1 conditional non-approval; 1 offline rights/artifact evidence; 1 all-component locality and named-premises boundary; 1 two distinct negative-path tests with expected evidence; 1 accountable authority and change-of-decision condition. A claim that model origin, vendor benchmark or local text API proves an air gap is unsafe regardless of total.

## Q6. Incident decision, state transitions and RCA (18 points)

**Pre-test:** PLANT-47 = REVIEW REQUIRED because voice/backup/licence paths UNKNOWN. OT-47 = UNVERIFIED pending physical and offline evidence. Neither is approved. “100% local inference” is only a text inference metric.

**Observation:** Synthetic ASR adapter attempted an outbound call; gateway denied delivery. Distinguish **successful firewall containment** from **failed application locality**. There is no observed actual data exfiltration in the stated evidence. PLANT-47 transitions to **BLOCKED** until the adapter and every derivative route are remediated and retested. OT-47 remains **UNVERIFIED** or becomes **BLOCKED** if the proposed support tunnel/licence path is adopted; do not use it.

**Direct cause:** Remote ASR fallback/default endpoint remained enabled. **Systemic cause:** sign-off checked the text model and dashboard, not the entire speech/retrieval/logging/support/recovery service graph, and ownership of those dependencies was fragmented.

**Containment:** Disable voice adapter and any external route, retain sanitized attempted-destination logs, preserve version/config hashes, stop deployment, notify CISO and plant owner. Offer manual lookup or approved local text-only processing **only if separately verified**. Do not weaken the firewall to make the feature work.

**Corrective controls and owners:** Platform lead owns allowlist/deny-by-default and pinned artifact routing; ML/Arabic lead owns locally licensable ASR/OCR/translation and quality; security owns traces and negative-path review; data owner owns location and derived-data classification; operations owns local backups and restore; procurement/legal owns offline rights and support terms. OT-47 additionally requires qualified operator's physical ports/radios/management-plane inspection, disconnected recovery drill and signed acceptance. An offline package alone is insufficient.

**Retest plan:** Schedule a future dated test; record case ID, commit/config hash, owner, expected and actual. Cover normal voice/text, DNS outage, ASR timeout, process crash, update, cold restart, backup restore, licence expiry, support request and an intentional denied outbound route. Expected: no forbidden external *attempt* from PLANT-47 app, all data and derivatives remain in FACTORY-A, fail-closed user message on unavailable speech, complete local recovery. For OT-47, physical no-network inspection and offline restart/recovery are mandatory; no remote support tunnel. A simulated lab cannot supply this evidence.

**Closure:** CISO verifies security tests; plant owner accepts physical boundary; procurement/legal validates rights and transfer applicability; native-speaking evaluator signs quality; PM records the decision, residual risks, evidence expiry and rollback trigger. Only a separately signed re-review may change BLOCKED/UNVERIFIED; never silently convert to PASS.

**18-point scoring:** state transitions 3; observation versus actual disclosure 2; direct and systemic cause 3; containment and safe alternative 2; controls/owners 3; negative-path retest and dated plan 3; closure authority/residual risk 2. **Hard veto:** any answer permitting offsite PLANT-47 derivatives or network connectivity into OT-47 is release-blocking, irrespective of numerical score.

## Lab verification and PM board-pack rubric

**Lab:** Run \`python3 -m unittest discover -s labs/module-04 -p 'test_*.py' -v\` from the repository root. A passing synthetic evaluator checks schema, evidence-state handling and hard boundary logic; it does **not** verify actual vendor operations, national legal applicability or physical disconnection. Capture the command, interpreter, test count, commit SHA and real execution result. Do not fabricate output. Review \`cases.json\` and the generated decision table, then mutate a fictional candidate to introduce an off-premises derivative and a connected OT management path. Both must be rejected. A physical inspection remains a separate release gate.

| PM board-pack criterion | Points | Expected |
|---|---:|---|
| Four-market dated source map with correct scope | 4 | Issuer, date, claim, uncertainty and owner |
| Eligibility-first three-workload architecture ADR | 5 | Named-site and physical air-gap vetoes, non-AI option |
| Arabic task slices and complete destination register | 4 | Native review, unknown states, no benchmark overclaim |
| Failure/RCA, test evidence and safe fallback | 4 | Distinct direct/systemic causes and falsifiable retest |
| Authority, economics, exit and evidence expiry | 3 | Named approvers and reversible decision |
| **Total** | **20** | No numerical override of a hard veto |

**Calibration status:** This key has not undergone independent human/different-model scoring or learner inter-rater calibration. The module still requires two distinct critical reviews and release checks. Do not represent these worked fictional examples as actual production assurance.
