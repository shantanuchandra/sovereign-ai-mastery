# Architecture & Learning Studio (v1.2)

> A browser-only **adaptive learning exercise** for the Sovereign AI Mastery field guide. It is not an AI model, a compliance tool, legal advice, procurement clearance or a sovereignty certification.

## What it does

1. **Ten questions** define a bounded AI workload, its data class, processing geography, operational authority, portability, compute capacity, available evidence, jurisdiction and delivery stage.
2. A **deterministic decision engine** returns one of several provisional architecture patterns. Its reasoning trace connects every input to an implementation consequence.
3. A generated **layered architecture**, four-dimension control table, lifecycle data-flow register, evidence status, test plan and hard gates explain how to assess the proposal.
4. **Change one constraint** compares the original and proposed architecture without overwriting inputs until the learner explicitly applies the change.
5. **Four adaptive case questions** change with the configuration. Each answer has a rationale. A missed answer unlocks a different follow-up situation for that concept, with a corrective test and course reading. First attempts remain separate from follow-up results; practice never clears architecture gates.
6. **Export Markdown and JSON** records assumptions, the architecture, lifecycle flows, first decisions, follow-up decisions, an optional reflection and unresolved evidence. The user may review and commit these files to the public GitHub repository.

## Rules and their limits

The engine is **rule-based**, not LLM-backed. It does not inspect actual deployments, execute cloud APIs, estimate production costs, evaluate model quality or verify laws. Inputs and quiz state stay in local browser storage; no questionnaire data is posted automatically. Export is initiated by the learner.

The course ontology in [`taxonomy/ontology.yaml`](../taxonomy/ontology.yaml) defines relevant classes and relationships. The Studio's dimensions and evidence states are a course-authored product design synthesis and **not an official framework**. The linked NIST AI RMF 1.0 is background on AI risk governance, not an endorsement of the Studio's sovereignty typology.

## Workload library and physical data boundaries

The Studio offers 26 workload categories and 21 fictional use-case presets. They span financial services, health, government, defense, manufacturing, telecom, HR, legal, research/IP, multilingual applications, retail/edge, enterprise AI platforms, insurance, procurement, education, energy, geospatial analysis and speech. A preset is a starting configuration, not a claim that the industry automatically requires a particular deployment.

The ten questions cover workload, data class, where data and derivatives may exist, network connectivity, administrator authority, portability, infrastructure capacity, evidence available, jurisdiction and release stage. The page dropdowns are populated from `LABELS`, so the browser and decision engine share one taxonomy. Existing version 1 saved selections remain valid; new connectivity defaults to restricted, allow-listed outbound connectivity.

**Premises-only means an actual physical site, not simply an in-country region.** It includes prompts, source documents, embeddings, model context, telemetry, audit logs, diagnostics, backups, support exports and derived copies. This is a *requirement*, not a proven property of any platform.

- `premises`: One physical site. Inference and all restricted derivatives remain on-site; require on-site capacity, on-site operations and a no-data-egress test. A cloud or colocated compute selection is blocked. Unrestricted internet and off-site private links are blocked.
- `airgap`: No network connection. The tool blocks any other connectivity choice and requires explicit local compute and on-site operators. Physical media, offline updates and local backup paths still need evidence.
- `approved_sites`: A defined set of enterprise facilities. Private inter-site links are conditional, not automatically safe; destination inventories and tests are required.
- Country, provider region, approved geographic zone, whitelisted processing locations and flexible geography are weaker or different boundary definitions; none implies physical-premises control.

If inputs are contradictory, output is `BLOCKED` with named gates. It does not silently recommend a managed model API. An `ONPREM` or `AIRGAP` proposal is always `PROVISIONAL` until independent control tests are accepted.

## Lifecycle register and targeted practice

Every blueprint includes nine required review paths: ingestion, retrieval/embeddings, inference, outputs, telemetry/evaluation, backup/recovery, support, updates and licensing. Relevant workload selections add speech/ASR/TTS, document OCR or sensor/imagery preprocessing. These are suggested surfaces to investigate, not an exhaustive discovered inventory. Each record has artifacts, a required destination, network constraint, accountable owner, acceptance test and `UNVERIFIED` or `BLOCKED` status.

Disconnected designs explicitly require offline activation, cold restart, restore, local identity and controlled update media. A model that works offline but requires online renewal still has an unresolved dependency. The register never infers that a real product meets these requirements.

Saved selections and reflections remain compatible with earlier versions. Quiz answers are restored only when the rules version and all ten selections match, and answer indexes are validated. Upgrading from v1.1 restarts practice while retaining assumptions and the reflection. Storage failures leave the Studio usable, including local exports. Changing a constraint or restarting practice clears both first and follow-up answers.

## Decision patterns

| Condition (priority order) | Provisional pattern | Required caution |
|---|---|---|
| Hard premises, compute, operator, connectivity conflict or reported adverse test | Gated feasibility design | No real restricted data until blockers, RCA and retest are resolved |
| Disconnected premises plus suitable on-site operator and compute | Air-gapped on-premises enclave | Verify physical and removable-media controls |
| Premises-only with on-site compute and approved on-site operators | Premises-contained local platform | Check no-data-egress across support, logs, backups, updates and failover |
| Disconnected network with local capacity (other locations) | Offline local serving | Network is absent, but media/access risks remain |
| Enterprise-operated production compute | Enterprise private serving | Facility, artifacts and telemetry still require validation |
| Specific location, sensitive processing or contracted operations | Managed serving with evidence gates | Exact service SKU and access boundaries must be checked |
| Flexible environments and high portability | Portable model gateway | Replaceability needs measured migration |
| Flexible public or approved data pilot | Managed API exploration | Not suitable for premises-confined data |

All patterns are educational hypotheses. They cannot certify a provider, declare a jurisdiction legally compliant or guarantee deployment suitability.

## Run locally

```sh
python3 -m http.server 8000
# Open http://localhost:8000/learning/
```

Requires no packages for the browser experience and no API key. The default desktop layout uses the field-guide palette with responsive mobile behavior.

## Test

```sh
node --test learning/tests/*.test.mjs
node --check learning/studio-ui.mjs
node --check learning/studio-engine.mjs
python3 scripts/build_site.py
python3 learning/tests/test_rendered_studio.py
```

Build dependencies are Beautiful Soup 4 and Mistune 3. The browser tests additionally require Playwright and its Chromium browser (`python3 -m playwright install chromium`). The production browser experience still requires no packages or API key.

The tests cover normalizing historical inputs, all 21 scenario presets and dropdown contents, incompatible premises and air-gap requirements, lifecycle flows, adaptive follow-ups, architecture comparisons, both actual downloads, saved-state migration, unavailable storage, keyboard answers and layout at 1440/1280/390/320px. The browser suite blocks and reports external requests. The Studio pull-request workflow and Pages workflow run these checks. They do not replace cross-browser or manual assistive-technology review, actual infrastructure testing or independent legal applicability review.

## Security and publication

- Do not input customer information, confidential architecture, personal identifiers, credentials or real access-control records.
- Local storage contains only chosen values and brief learning reflections, and can be cleared via browser settings. This is not a secure vault.
- The repository is public. Exported Markdown and JSON should be reviewed and redacted before committing.
- There is no hidden use of cloud inference or an external LLM. The tutor is a transparent scenario engine, not a conversational model.

## Product extension path

After actual learning feedback and module coverage improve, consider an opt-in server-based tutor backed by a constrained knowledge base, source retrieval, and per-answer citations. A real model should disclose its version, retrieval scope, uncertainties, operational costs, and data-processing boundaries. Do not add a secret model key to client-side code.
