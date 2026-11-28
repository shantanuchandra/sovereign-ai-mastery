# Module 18 carousel text equivalent

Educational draft, 28 November 2026. Eight question-led 4:5 slides. Read alongside CAROUSEL.html; no independent/manual or production assurance is claimed. Module 04 remains HOLD.

## 1. What must recovery preserve?

Recover usable, currently authorized state. A backup can contain obsolete documents and permissions that must not return to active serving.

**Decision:** Apply current retirement and revocation decisions before exposure.

Source/scope: Course restore design; fictional BANK-A.

## 2. Which clock are you measuring?

RTO targets a recovery interval. RPO identifies a recoverable point in time. A tiny local copy excludes most service dependencies.

**Decision:** Declare the business scope and clock boundaries.

Source/scope: NIST SP 800-34 Rev. 1; checked 28 Nov 2026.

## 3. Where does emergency failover go?

BANK-A has an unchanged physical-premises rule. External backups, support, activation or failover can conflict even during an outage.

**Decision:** Keep hard eligibility gates ahead of speed or scores.

Source/scope: Course premises and air-gap scenario; no legal finding.

## 4. Can an old backup revive retired content?

The lab captures d2, then retires it before restoration. Current decisions exclude d2 from the restored live file and tenant results.

**Decision:** Historical validity does not freeze authorization.

Source/scope: Actual synthetic file exercise; no durable retirement service.

## 5. Does an export prove portability?

The fixture migrates two eligible records from JSON into SQLite and compares every field and tenant. Equal counts alone would miss errors.

**Decision:** Retest permissions and behavior after migration.

Source/scope: Actual synthetic migration; no real LLM quality measured.

## 6. Do you trust what restoration executes?

PostgreSQL 18 warns that restoring a dump can execute code chosen by source superusers. Review trust and compatibility before using that mechanism.

**Decision:** A checksum supplies equality, not trusted provenance.

Source/scope: PostgreSQL 18 pg_dump warning; checked 28 Nov 2026.

## 7. Are two vendors independent recovery paths?

Different logos may share identity, facilities, networks, models or support. Trace common dependencies before assuming concentration risk fell.

**Decision:** Test the failure source that matters to the workload.

Source/scope: Course dependency analysis; no provider assurance.

## 8. Which finding remains open after the drill?

The lab restores a real local file, migrates synthetic rows and denies declared conflicts. Production RTO/RPO and physical evidence remain open.

**Decision:** Assign owners, evidence expiry and dated retests.

Source/scope: Educational draft; independent/manual review pending.

Sources: NIST SP 800-34 Rev. 1 Appendix G and section 3; NIST SP 800-53 Rev. 5 CP-10; PostgreSQL 18 pg_dump Description and Warning. Full original URLs, short exact extracts and verification date are retained in the chapter. HTML is preferred. export_pdf.py produces an untagged eight-page 8×10-inch PDF after publication preparation. test_rendered_carousel.py uses temporary output and does not build the shared website.
