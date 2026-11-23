# Module 05 facilitator solutions and scoring rubric

> **DRAFT only; separate from learner chapter and public site.** The case facts and answers are invented teaching material. Do not construe any outcome as a legal opinion, evidence of a real supplier, physical isolation or compliance. Version: 2026-11-23. Reviewer status: GPT-6 author self-check only; independent legal/assessment calibrator **NOT COMPLETED**.

## Assessment contract

Total **40 points**: Q1–Q4 four points each, Q5 six points, Q6 eighteen points. Knowledge scoring is subordinate to the **safety veto**: a learner proposing an unreviewed offshore transfer, prohibited support tunnel, online licence check or cloud fallback for the named-site or air-gapped cases **fails the release recommendation irrespective of total score**. Record *numeric score* and *release-eligibility decision* separately.

## Q1 | Federal-regime triage (4 points)

**Worked answer:** Start with (1) specific contracting legal entity/establishment; (2) activity/purpose and controller/processor roles; (3) categories and origin/nexus of personal or derived data; (4) individuals/data-subject geography and access/processor locations; (5) sector exceptions, governing contracts, exact law/version and counsel-approved scope. A UAE storage region covers only a portion of processing location. Support access, handling of a health record or a DIFC entity may change the applicable analysis. Do not assert the law's exact obligations without current authoritative text and counsel.

**Rubric:** 1 entity/role; 1 activity/data/subject; 1 sector and instrument/version/counsel; 1 operational/transfer destination caveat. A list of five technical controls without legal scope earns at most 1/4.

## Q2 | DIFC versus ADGM (4 points)

**Worked answer:** DIFC references Law 5/2020, current amendments and Commissioner tools, including the Articles 26–27 transfer review topic. ADGM references the Data Protection Regulations 2021 and Office of Data Protection SCC addendum guidance (paragraphs 1.2–1.3 cite Part V and Article 42(3)(c)); the controlling consolidated regulation and specific transfer mechanism remain for counsel to verify. Neither source certifies a supplier configuration. Technical tests: (a) attempt unauthorized offshore diagnostic log view and require denial with an audit record; (b) cold restart, backup restore and licence-failure traces to find hidden remote egress; inspect both data and control planes. Legal counsel separately maps roles, instruments and safeguards.

**Rubric:** 1 DIFC source and scope; 1 ADGM source and scope; 1 effective negative access test; 1 separate recovery/egress and legal-versus-technical distinction. A generic statement that either free-zone law "always permits transfer" is unsafe.

## Q3 | Saudi law and transfer regulation (4 points)

**Worked answer:** SDAIA's PDPL Article 29 addresses transfers/disclosures outside KSA subject to stated conditions. The *distinct* transfer regulation lays out additional structures, including specific exemptions and risk-assessment provisions; the governing versions, purposes and data flows need counsel. “Every AI input must remain inside Saudi Arabia under the PDPL” is not a conclusion supported by citing Article 29 alone. Neither a data residency checkbox nor a cloud vendor's plan proves compliance.

**Rubric:** 1 distinguish PDPL and transfer regulation; 1 articulate conditional applicability; 1 reject the blanket localization inference; 1 name an owner and evidence to collect (transfer record, support paths, counsel review). Do not score invented decree dates or legal exceptions as evidence.

## Q4 | Legal-control-evidence row (4 points)

**Example row (synthetic):** GC-02; GulfCare DIFC; support diagnostics for synthetic employee IDs; legal candidate DIFC Law 5/2020 Articles 26–27; counsel state NEEDS_COUNSEL; destination/offshore viewer UNKNOWN; owner CISO, privacy and legal separate; CTRL-GC02-SUPPORT; TEST-GC02-DENY; expected unapproved viewer denial, event and exact timestamp; decision HOLD. The PM may use a negative-path access test to establish part of the technical path, but cannot turn it into transfer authorization.

**Rubric:** 1 activity/entity/source pinpoint; 1 counsel state and accountable reviewer; 1 concrete deny test and evidence; 1 justified HOLD pending unresolved routes. Passing a schema validator alone is not 4/4.

## Q5 | Real regulator tool case (6 points)

**Primary real-product anchor:** DIFC Commissioner of Data Protection, [Data Protection Assessment Tools](https://www.difc.com/business/registrars-and-commissioners/commissioner-of-data-protection/tools-and-templates), with a specific tool titled *Data Export / International Transfers (Articles 26 & 27)*. Checked 2026-11-23 as regulator guidance; that tool is **not** automatic permission or an independent audit.

**Worked response:** Reject the claim that clicking through the tool authorizes any overseas support view. Identify the exporter/processor and transfer scenario, capture the actual imported/exported data and redaction mechanism, official legal provisions, current contracts and subprocessor schedule, purpose and destination, privileged-access rules, testing and counsel opinion. Permit only separately authorized synthetic-data experimentation; keep real-person or restricted-diagnostic routes HOLD, and block any path forbidden by a hard customer constraint.

**Six-point rubric:** 1 named issuer/tool/Articles 26–27; 1 limitation of self-assessment guidance; 1 distinct legal applicability and transfer mechanism review; 1 destinations/support path and privilege inventory; 1 observable negative test plus signed contract; 1 explicit interim HOLD and unblock conditions. Vendor "certified by an assessment questionnaire" receives no tool-permission point.

## Q6 | Physical-site and air-gap RCA (18 points)

**Facts:** Fictional PLANT-05 contracts require **all restricted sources and derivatives** to remain within the named FACTORY-A premises; OT-05 has **no inbound or outbound network route of any kind**. A simulated voice adapter tries remote licence activation and offshore diagnostics at cold restart; a firewall blocks the request. No actual data transfer was observed in this fiction.

**Direct cause:** Offline-incompatible licence activation and an adapter's default remote fallback were left active. The processes attempted to escape the applicable boundary despite dashboard claims of local storage. **Systemic cause:** procurement accepted a happy-path regional hosting demonstration; engineering scoped only text inference; security and operations omitted speech, licence, logging, recovery and vendor-support planes from a jointly owned dependency map. The firewall achieved containment, **but the app failed its intended fail-closed routing requirement.**

**Immediate containment:** Stop deployment, disable the adapter and remote diagnostic configuration, preserve non-sensitive attempted-destination logs and hashes, avoid changing firewall rules to permit requests, retain the separate restricted-system HOLD/BLOCKED decision, notify CISO/plant owner, offer a separately approved manual search fallback.

**Corrective actions and accountable owners:**
1. Platform architect: enumerate all inference/retrieval/ASR/OCR/telemetry/licence/update/backup paths and remove remote defaults.
2. Security/CISO: deny-by-default egress and privileged access, independent-in-purpose trace and negative tests.
3. Plant data owner: define named physical boundary for sources and derivatives; accept only witnessed in-scope routes.
4. OT operator: inspect ports, wireless/management planes and removable-media procedures; execute disconnected start/recovery witness.
5. Procurement/legal: verify enforceable offline model licences, support entitlements, vendors and processor terms.
6. Operations/ML lead: reproducible pinned offline packages, Arabic quality under failure, local backup/restore and rollback evidence.

**Retest and decision:** Fail the adapter/ASR and revoke or expire licences: system must reject safely with **no attempt** to contact remote services. Inspect full destination traces, local backups, recovery images and support channels. Use qualified physical inspection and an offline cold-start/recovery demonstration for OT-05. A single clean trace is time-bound evidence, not a blanket physical certification. Until independently accepted, PLANT-05 = **BLOCKED while forbidden remote dependency exists**, then HOLD pending full retest; OT-05 = **HOLD/NOT FEASIBLE** if no offline solution is available. If a hard constraint cannot be met, recommend a manual/non-AI system.

**18-point rubric:**
| Element | Points | What earns full credit |
|---|---:|---|
| Direct technical cause | 2 | Licence and remote adapter fallback |
| Systemic organizational/architecture cause | 2 | Whole-service dependency and review gap |
| Correctly distinguish attempted vs actual egress | 2 | Firewall containment versus application failure, no invented exfiltration |
| Safe containment | 2 | Disable offending paths, no tunnel, preserve bounded diagnostics |
| Six distinct corrective owners | 4 | At least six named responsibilities covering all major controls |
| Negative and recovery tests | 3 | Disconnected cold start, ASR/crash fallback, backup restore, physical network inspection |
| Release disposition + non-AI alternative | 3 | Physical-site/air-gap hard veto, HOLD/BLOCKED, manual fallback |
| **Total** | **18** | Safety veto still independent of points |

**Safety override:** If the learner recommends an exception support tunnel, online key/licence call, offsite failover, telemetry or an unverified regional backup for OT-05 or PLANT-05, set **release recommendation = FAIL (unsafe)** even if the prose accumulates many scoring points. An egress denial is not a pass for the application. **No point is awarded for fictional claimed legal clearance or a fabricated physical witness.**

## Facilitator assessment-calibration protocol (not executed)

Give Q5/Q6 and this key to an **independent human or demonstrably different model** blinded to this author's prior scores. Request item-level scores and rationales on two synthetic answers, one fluent but recommending forbidden external support and one safety-preserving but incomplete. Record reviewer identity/model version, date, raw output, disagreement, reconciliation and rubric edits. A second GPT-6 self-score is **not** independent. The draft module and prior Module 04 still require release evidence; this key does not authorize production or publication.

## Source and provenance boundary

This key inherits the official issuer sources and currentness caveats linked in the [Module 05 learner draft](../../chapters/05-laws-regulation-jurisdiction.md). It **does not** grant current statutory applicability or certify health/financial/critical-infrastructure claims. Use counsel, official current instruments and qualified technical/physical review for real decisions.
