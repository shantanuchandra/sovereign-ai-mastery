/**
 * Sovereignty Learning Studio: transparent, deterministic, educational rules.
 * No external models, telemetry, vendor verification or legal determinations.
 * These outputs are architecture hypotheses, not certifications.
 */

export const VERSION = '1.1.0';
/** All option values are stable IDs: old saved v1 selections still normalize correctly. */
export const LABELS = Object.freeze({
  workload: {
    knowledge:'Employee knowledge and policy assistant', customer:'Customer support assistant', regulated:'Regulated document review',
    healthcare:'Clinical notes and medical record assistant', imaging:'Medical imaging and diagnostics research',
    banking:'Banking KYC and AML review', fraud:'Fraud monitoring and investigation',
    government:'Government citizen service assistant', defense:'Defense and national-security analysis',
    manufacturing:'Factory predictive maintenance', industrial:'Industrial control / OT knowledge assistant',
    telecom:'Telecom network operations copilot', legal:'Confidential legal and contract analysis',
    hr:'HR and payroll assistant', developer:'Internal code and software engineering assistant',
    research:'Research and intellectual-property discovery', language:'Arabic and multilingual language assistant',
    media:'Public content drafting and classification', edge:'Retail, branch or edge-device inference',
    platform:'Enterprise multi-tenant AI platform'
  },
  data: {
    public:'Public and openly licensed information', synthetic:'Synthetic test data only',
    internal:'Internal business documents', confidential:'Confidential business / financial files',
    personal:'Personal information', sensitive:'Sensitive or regulated information',
    health:'Patient or protected health information', payments:'Financial transactions and payment records',
    secrets:'Trade secrets / restricted intellectual property', classified:'Classified or national-security information',
    mixed:'Mixed classes; highest restriction governs'
  },
  location: {
    airgap:'Single premises, physically air-gapped (no network)',
    premises:'Single premises only; no data or derivatives may leave',
    approved_sites:'Only specified enterprise premises / campuses',
    country:'Selected country only', region:'Specific provider / cloud region only',
    zone:'Approved geographic zone (multiple regions)', approved:'Named permitted countries or processing locations',
    flexible:'No strict processing geography'
  },
  connectivity: {
    disconnected:'Air-gapped: no inbound or outbound network',
    isolated:'Local network only; no external egress',
    allowlist:'Restricted outbound with explicit no-data-egress controls',
    private_links:'Private connectivity to explicitly approved destinations',
    internet:'General internet access including external service endpoints',
    flexible:'No special network isolation requirement'
  },
  operator: {
    enterprise:'Enterprise employees administer all layers',
    onsite_partner:'Approved contractor, physically on-site under enterprise control',
    dedicated:'Dedicated outsourced team with supervised remote access',
    local:'Approved managed-service operators (location varies)',
    shared:'Shared enterprise/provider administration',
    provider:'Provider administration permitted by contract'
  },
  portability: {
    owned:'Model artifacts, serving and data must be enterprise-portable',
    essential:'Mandatory provider exit; rehearsed migration',
    strong:'Strong preference for replaceable models and interfaces',
    useful:'Important but negotiable',
    low:'Low priority for current pilot',
    lockin:'Proprietary dependency explicitly accepted, with review'
  },
  capacity: {
    laptop:'Laptop / local learning prototype only',
    onsite_cpu:'On-prem CPU / small edge appliance with limited capacity',
    onsite_gpu:'On-prem production GPU servers inside the premises',
    private_dc:'Enterprise-run data center, site not yet verified',
    gpu:'Enterprise-operated production compute, site not yet verified',
    colo:'Enterprise-controlled colocation (outside own premises)',
    managed:'Approved managed AI platform',
    hybrid:'Hybrid enterprise + managed compute',
    public_cloud:'Public cloud compute / APIs only'
  },
  evidence: {
    none:'No mapped evidence', assertions:'Vendor or project claims only', design:'Architecture and contracts only',
    contracts:'Executed contracts, runtime not assessed', configuration:'Configurations and diagrams inspected',
    logs:'Runtime logs captured, no completed acceptance review',
    tested:'Test records exist but are not reviewed',
    independent:'Independent review record exists; scope not validated here',
    adverse:'A test reportedly violated a requirement'
  },
  jurisdiction: {
    uae:'UAE federal / general context', difc:'UAE: DIFC entity / processing', adgm:'UAE: ADGM entity / processing',
    saudi:'Saudi Arabia', qatar:'Qatar', bahrain:'Bahrain', oman:'Oman', kuwait:'Kuwait',
    eu:'European Union', uk:'United Kingdom', us:'United States', india:'India', other:'Other / multiple / undetermined'
  },
  stage: {
    discovery:'Requirements discovery', prototype:'Exploration / technical prototype', poc:'Proof of concept',
    pilot:'Controlled pilot', beta:'Limited production beta', production:'Production rollout',
    critical:'Mission-critical deployment', migration:'Migration of an existing AI system', sunset:'Retirement and data deletion'
  }
});
export const DEFAULTS = Object.freeze({
  workload:'knowledge', data:'internal', location:'country', connectivity:'allowlist', operator:'local', portability:'essential',
  capacity:'managed', evidence:'none', jurisdiction:'uae', stage:'pilot'
});
export const PRESETS = Object.freeze({
  assistant:{...DEFAULTS},
  banking:{...DEFAULTS,workload:'banking',data:'payments',location:'country',operator:'enterprise',capacity:'laptop',stage:'production'},
  support:{...DEFAULTS,workload:'customer',data:'public',location:'zone',operator:'provider',portability:'low',connectivity:'internet',capacity:'managed',jurisdiction:'saudi',stage:'pilot'},
  onsite:{...DEFAULTS,workload:'research',data:'secrets',location:'premises',operator:'enterprise',capacity:'onsite_gpu',connectivity:'isolated',portability:'owned',stage:'production'},
  hospital:{...DEFAULTS,workload:'imaging',data:'health',location:'premises',operator:'onsite_partner',capacity:'onsite_cpu',connectivity:'allowlist',stage:'pilot'},
  factory:{...DEFAULTS,workload:'industrial',data:'secrets',location:'airgap',operator:'enterprise',capacity:'onsite_gpu',connectivity:'disconnected',stage:'critical'},
  defense:{...DEFAULTS,workload:'defense',data:'classified',location:'airgap',operator:'enterprise',capacity:'onsite_gpu',connectivity:'disconnected',stage:'prototype'},
  legal:{...DEFAULTS,workload:'legal',data:'confidential',location:'approved_sites',operator:'enterprise',capacity:'private_dc',connectivity:'private_links',stage:'pilot'},
  telecom:{...DEFAULTS,workload:'telecom',data:'internal',location:'country',operator:'shared',capacity:'hybrid',connectivity:'private_links',stage:'production'},
  retail:{...DEFAULTS,workload:'edge',data:'personal',location:'premises',operator:'enterprise',capacity:'onsite_cpu',connectivity:'isolated',stage:'pilot'},
  hr:{...DEFAULTS,workload:'hr',data:'personal',location:'region',operator:'dedicated',capacity:'managed',connectivity:'allowlist',stage:'pilot'},
  publicservice:{...DEFAULTS,workload:'government',data:'public',location:'country',operator:'local',capacity:'managed',connectivity:'allowlist',stage:'beta'},
  devtools:{...DEFAULTS,workload:'developer',data:'secrets',location:'approved_sites',operator:'enterprise',capacity:'onsite_gpu',connectivity:'isolated',stage:'poc'},
  multilingual:{...DEFAULTS,workload:'language',data:'public',location:'flexible',operator:'provider',capacity:'public_cloud',connectivity:'internet',portability:'useful',stage:'prototype'},
  platform:{...DEFAULTS,workload:'platform',data:'mixed',location:'approved',operator:'shared',capacity:'hybrid',connectivity:'private_links',portability:'essential',stage:'production'}
});
export const PRESET_LABELS = Object.freeze({
  assistant:'UAE employee knowledge assistant',banking:'Banking review with unresolved compute',support:'Saudi public information bot',
  onsite:'Strict on-premises IP research assistant',hospital:'On-site clinical imaging reviewer',
  factory:'Air-gapped factory operations',defense:'Disconnected defense analysis (fictional)',
  legal:'Legal review across approved enterprise sites',telecom:'Telecom hybrid operations',
  retail:'Store / branch edge inference',hr:'HR personal-data assistant',publicservice:'Public sector citizen service',
  devtools:'Internal code and IP copilot',multilingual:'Arabic multilingual research',platform:'Multi-tenant enterprise AI platform'
});
export function normalize(raw={}) {
  const config={};
  for(const [key,values] of Object.entries(LABELS)) config[key]=Object.hasOwn(values,raw[key])?raw[key]:DEFAULTS[key];
  return config;
}
const step=(key,label,consequence,category='constraint')=>({key,label,consequence,category});
const control=(id,dimension,claim,implementation,test,evidence='UNVERIFIED')=>({id,dimension,claim,implementation,test,evidence});
const MODS=Object.freeze({
  foundations:{label:'Module 01: bounded sovereignty claims',url:'../modules/01-sovereign-ai-fundamentals.html'},
  ontology:{label:'Sovereignty taxonomy and ontology',url:'../taxonomy/ONTOLOGY.html'},
  data:{label:'Module 08: data boundaries (syllabus)',url:'../curriculum.html#module-08'},
  infrastructure:{label:'Module 10: cloud and deployment (syllabus)',url:'../curriculum.html#module-10'},
  agents:{label:'Module 14: agents and model interfaces (syllabus)',url:'../curriculum.html#module-14'},
  security:{label:'Module 16: key custody and identity (syllabus)',url:'../curriculum.html#module-16'},
  regulation:{label:'Module 05: legal jurisdiction',url:'../modules/05-laws-regulation-jurisdiction.html'}
});
export function createBlueprint(raw={}) {
  const v=normalize(raw);
  const siteOnly=['premises','airgap','approved_sites'].includes(v.location);
  const airgap=v.location==='airgap';
  const strictCountry=['country','region','zone','approved'].includes(v.location);
  const owned=v.operator==='enterprise';
  const onsiteOperator=['enterprise','onsite_partner'].includes(v.operator);
  const onsiteCompute=['onsite_cpu','onsite_gpu'].includes(v.capacity);
  const enterpriseCompute=['onsite_cpu','onsite_gpu','private_dc','gpu','colo'].includes(v.capacity);
  const sensitive=!['public','synthetic','internal'].includes(v.data);
  const critical=['production','critical','migration','beta'].includes(v.stage);
  const conflicts=[],trace=[],gates=[];
  let id,title,why,steps,model,operations,traffic;
  if(airgap&&v.connectivity!=='disconnected'){
    conflicts.push('An air-gapped site cannot have an external or internal network mode selected.');
    gates.push('Block the proposed deployment: set connectivity to no network or remove the air-gap requirement after a formal change.');
  }
  if(siteOnly&&!onsiteCompute){
    conflicts.push(`Data must remain within selected premises, but ${LABELS.capacity[v.capacity]} is not explicitly confirmed as compute physically located there.`);
    gates.push('Block production processing of the restricted workload until physically on-site compute is provided and verified.');
  }
  if(siteOnly&&!onsiteOperator){
    conflicts.push('Premises-only processing requires enterprise administrators or physically supervised on-site contractors; remote provider access is not currently compatible.');
    gates.push('Block operational acceptance until privileged and support access is physically bounded to the approved premises.');
  }
  if(siteOnly&&(['internet','flexible'].includes(v.connectivity)||(v.location==='premises'&&v.connectivity==='private_links'))){
    conflicts.push('Unrestricted outbound connectivity is incompatible with an unqualified no-data-leaves-the-premises requirement.');
    gates.push('Block outbound data-bearing connections. Require verified deny-by-default egress and review software updates and telemetry.');
  }
  if(v.connectivity==='disconnected'&&!onsiteCompute){
    conflicts.push('No-network operation cannot rely on unspecified cloud or off-site managed inference.');
    gates.push('Require local model inference, storage, identity and audit capability before a disconnected deployment.');
  }
  if(['disconnected','isolated'].includes(v.connectivity)&&!onsiteOperator){
    conflicts.push('Disconnected or site-only networking cannot rely on remote provider administration; operators must be physically on-site.');
    gates.push('Review all administrator sessions and support procedures for offline-only access.');
  }
  if(v.connectivity==='isolated'&&!onsiteCompute){
    conflicts.push('A local-network-only architecture cannot use compute that is not explicitly verified inside the site.');
    gates.push('Provide local inference capability or revise the disconnected local-network boundary.');
  }
  if(v.operator==='onsite_partner'&&['managed','hybrid','public_cloud'].includes(v.capacity)){
    conflicts.push('Physically on-site-only operator control is not demonstrated by managed or shared cloud compute.');
    gates.push('Review provider privileged access and revise the capacity or operator assumption.');
  }
  if(owned&&!enterpriseCompute){
    conflicts.push('Enterprise-only administration conflicts with a compute option that does not establish an enterprise-operated production service.');
    gates.push('Block production until enterprise-operated capacity is available or the operator requirement is formally revised.');
  }
  if(v.evidence==='adverse'){
    conflicts.push('A reported adverse test requires triage before any launch claim can be accepted.');
    gates.push('Block launch pending RCA, corrective action and a documented passing retest covering the original acceptance criterion.');
  }
  if(conflicts.length){
    id='gated';title=siteOnly?'Gated premises-only feasibility design':'Gated prototype and architecture decision';
    why=`The selected inputs contain ${conflicts.length} hard constraint conflict(s). No managed API or off-site inference is a permissible fallback while those constraints stand. Use fictional or approved synthetic data for a local feasibility exercise, then resolve each blocker.`;
    steps=['Document the required physical, operational and connectivity boundary','Use synthetic data for a confined proof of concept only','Assign an owner and acceptance test for every blocker before real data or production'];
    model=siteOnly?'Local prototype only; NO cloud or off-prem model inference':'Prototype only until architecture conflict is resolved';
    operations='Operator and capacity assumptions unresolved; no compliant operation asserted';
    traffic=siteOnly?'Do not transmit prompts, embeddings, logs, backups or diagnostics off-site':'No deployed data flow is authorized by this design';
  } else if(airgap){
    id='airgap';title='Air-gapped on-premises AI enclave';
    why='The workload requires physically disconnected operation. A locally hosted model, local storage, on-site staff and independently tested removable-media controls form a candidate design; hardware, artifacts and operations remain unverified.';
    steps=['Prepare a signed offline model and dependency inventory','Serve inference, retrieval, logs, backups and keys entirely inside the isolated premises','Validate physical access, media ingestion, patching and restore procedures without network access'];
    model='Air-gapped local model weights with offline patch and integrity verification';
    operations='Enterprise/on-site supervised operators; no network-based remote administration';
    traffic='Zero network egress; physical removable media is a separately controlled transfer path';
    gates.push('Independent review of offline software provenance, removable-media policy and physical security is required.');
  } else if(siteOnly){
    id='onprem';title='Premises-contained AI platform with egress enforcement';
    why='The data boundary is the physical premises, not merely the selected country. Host inference and all derived artifacts locally. Verify that outbound connections, remote diagnostics, backups and human support cannot export protected data.';
    steps=['Host model serving, retrieval, embeddings, storage and keys on on-site compute','Enforce deny-by-default outbound rules with explicit exceptions and local logging','Test logs, remote support, backup targets, model updates, file exports and failover against the premises boundary'];
    model='Self-hosted local model, no off-prem inference or embeddings';
    operations=v.operator==='onsite_partner'?'Approved on-site contractors with supervised sessions; no remote privileged access':'Enterprise-only on-site administrative plane';
    traffic=['isolated','disconnected'].includes(v.connectivity)?'No external network egress or remote service endpoints':'Restricted outbound destinations with explicit no-protected-data-egress policy and testing';
    gates.push('Do not assume encrypted traffic, remote management, off-site DR or vendor telemetry satisfies a no-data-leaves-the-premises rule.');
  } else if(v.connectivity==='disconnected'){
    id='localoffline';title='Locally operated disconnected AI stack';
    why='Network disconnection excludes remote inference. With local compute this is a candidate offline architecture, but the accepted physical boundary and transfer procedures still need review.';
    steps=['Install model and dependencies from verified offline artifacts','Operate inference and evidence generation without network services','Test offline update, backups and removable-media transfer process'];
    model='Locally served model without network access'; operations='Approved local administrators';traffic='No network egress; physical access and media remain separate risks';
  } else if(onsiteCompute){
    id='onprem';title='On-site model endpoint with verified administrator boundaries';
    why='Compute is physically on premises, but this alone does not prohibit remote support, external backups or vendor access. Verify the actual boundary for this workload.';
    steps=['Run local model inference and artifact storage on the selected site','Approve operator roles, remote access and permitted destinations explicitly','Test remote support, logging, update checks, cloud fallbacks and disaster recovery'];
    model='On-site model endpoint, no implicit cloud failover';operations='Chosen administrator model, subject to privileged-access review';traffic='All external paths must match the declared geography and network rules';
  } else if(owned&&enterpriseCompute){
    id='private';title='Enterprise-operated private serving';
    why='The company controls its serving environment, but its precise site, licenses, maintenance and telemetry paths still need evidence review.';
    steps=['Deploy a private model endpoint on approved enterprise-controlled compute','Implement enterprise IAM, key custody, audit trails and egress restrictions','Test support, diagnostics, model updates and disaster recovery'];
    model='Private model endpoint with reviewed license and provenance';operations='Enterprise-owned identities, keys and service administration';traffic='Restricted network routing with destination inventory';
  } else if(strictCountry||v.operator==='local'||sensitive||v.capacity==='hybrid'){
    id='managed';title='Managed serving with explicit boundary controls';
    why='A managed service can reduce operating work, but only a specific deployment and contract can establish processing, operations and failover boundaries. No service is assumed eligible without verification.';
    steps=['Confirm eligible deployment region, SLA, access and data-flow policy','Use identity and data-minimizing policies at the application/model gateway','Verify telemetry, support, backups, failover, subprocessors and deletion'];
    model='Managed inference endpoint subject to SKU and region review'; operations='Provider/approved support roles with documented access';traffic='Route and audit only approved processing destinations';
    if(strictCountry)gates.push('Verify all inference, logging and disaster recovery paths against the selected geographic set.');
  } else if(v.portability==='essential'||v.portability==='owned'||v.location==='approved'){
    id='hybrid';title='Portable model gateway and controlled data tier';
    why='Replaceable inference services and a separate data tier help meet exit objectives, though migration and data-boundary claims remain unverified.';
    steps=['Use gateway adapters and partitioned retrieval with policy checks','Set deployment destinations and artifact/license requirements','Run an end-to-end migration and negative egress test'];
    model='Replaceable provider endpoints and tested model adapters';operations='Enterprise governance with contracted platform operations';traffic='Explicit routing and model destination audit trails';
  } else {
    id='api';title='Scoped managed API exploration';
    why='Flexible geography and permissive operating constraints can support a low-risk API experiment with approved data. Service location, retention and dependency claims still need evidence.';
    steps=['Minimize and classify prompt content before invoking the service','Record telemetry, retention, provider roles and subprocessors','Plan review/exit triggers before expanding real workloads'];
    model='Documented external inference dependency';operations='Provider administrators subject to approved terms';traffic='Recorded destinations and bounded telemetry';
  }
  if(critical&&['laptop','onsite_cpu'].includes(v.capacity))gates.push('Production performance, model suitability and failover must be tested; a laptop or CPU appliance alone does not establish an SLA.');
  if(critical&&!enterpriseCompute&&id!=='gated')gates.push('Production SLA, capacity, multitenancy and incident readiness must be validated.');
  if(sensitive)gates.push('Restricted data requires explicit owners, authorized access, retention and qualified privacy/security review.');
  if(v.workload==='imaging'&&v.capacity==='onsite_cpu')gates.push('Validate imaging model size, clinical suitability and pilot latency on the actual CPU appliance before any real-case use.');
  if(v.data==='classified'||['defense','industrial'].includes(v.workload))gates.push('High-impact or classified use requires specialist security, safety and procurement review; this tool does not authorize it.');
  if(v.workload==='platform')gates.push('Multi-tenant platforms need tenant isolation, per-workload policy, chargeback and tenant-aware audit validation.');
  if(['healthcare','imaging'].includes(v.workload))gates.push('Clinical suitability, authorization and human oversight require specialist review before patient-facing use.');
  if(v.stage==='sunset')gates.push('Document model/data disposal, backups, retention exceptions, account revocation and proof of deletion.');
  if(v.portability==='lockin')gates.push('Proprietary lock-in is an explicit, owned risk acceptance, not a sovereignty guarantee.');
  if(v.connectivity==='private_links')gates.push('Verify private links end at approved destinations and are not a path for prohibited data transfers.');
  if(v.evidence==='adverse')gates.push('Evidence status remains nonconforming until corrective action and accepted retest.');
  else if(v.evidence==='tested'||v.evidence==='independent')gates.push('Review the actual outcomes, test scope, provenance and dates; their mere existence does not prove a passing control.');
  else gates.push('No inspected passing runtime test is available. All controls remain unverified.');
  const territory=siteOnly?'No protected information, prompts, embeddings, telemetry, backups or diagnostics may leave the approved physical premises':'Declared destinations for inference, storage, processing and derivatives are enforced';
  const territorialTest=siteOnly?'Conduct isolated-network, DNS/proxy, update, failover, remote support, removable-media and backup-destination tests':'Trace prompts, logs, embeddings, support and failover destinations';
  const evidenceState=v.evidence==='adverse'?'NONCONFORMANCE_REPORTED':conflicts.length?'CONFLICT':(v.evidence==='tested'||v.evidence==='independent'?'REVIEW_REQUIRED':'UNVERIFIED');
  const controls=[
    control('TERR-01','Territorial',territory,siteOnly?'Local services; deny-by-default outbound and explicit media controls':'Destination allow-list, data-flow inventory and egress logs',territorialTest,evidenceState),
    control('OPS-01','Operational','Only permitted administrative paths may control the system',siteOnly?'On-site identities, key custody, access logging, no unapproved remote support':'Roles, key custody and privileged access review','Attempt denied privileged access and review support-path audit',evidenceState),
    control('TECH-01','Technological','Exit dependencies and model artifacts are understood',airgap?'Offline model artifact signing, SBOM, licensed weights and rebuild path':'Model/license inventory and a repeatable exit path','Replace model/serving stack in a rehearsed migration; record compatibility',evidenceState),
    control('LEGAL-01','Legal/contractual','Relevant contractual and legal boundaries receive qualified review','Counsel-reviewed scope, terms, entity and transfer map','Document the responsible entity, regulations, authorizations and exceptions','REVIEW_REQUIRED')
  ];
  const traces={
    workload:'Defines the workload, stakeholders, inference and lifecycle surfaces.',
    data:sensitive?'Requires restricted input, output, retention and access controls.':'Still requires a documented classification and data lifecycle.',
    location:siteOnly?'Hard physical boundary forbids external processing and derivative exports.':'Actual processing and storage destinations must be measured.',
    connectivity:airgap?'Must be disconnected, including diagnostics.':'Network egress and support links must match the data boundary.',
    operator:siteOnly?'Remote provider or shared administrators are not implicitly permitted.':'Privileged operations and key custody require approval.',
    portability:'Licensing and data/model migration evidence are separate from network isolation.',
    capacity:siteOnly?'Only physically verified on-site compute can satisfy this workload boundary.':'Production capabilities and facility location need confirmation.',
    evidence:'An evidence document is not an accepted test outcome.',
    jurisdiction:'This value creates counsel-review work, not a legal determination.',
    stage:critical?'Assurance, reliability and operational readiness require production validation.':'Prototype and pilot constraints are still enforceable.'
  };
  for(const [key,value] of Object.entries(v)) trace.push(step(key,`${key}: ${LABELS[key][value]}`,traces[key]));
  const lessons=[MODS.foundations,MODS.ontology];
  if(siteOnly||sensitive||strictCountry)lessons.push(MODS.data);
  if(siteOnly||owned||enterpriseCompute||v.capacity==='managed')lessons.push(MODS.infrastructure);
  if(['essential','owned','strong'].includes(v.portability))lessons.push(MODS.agents);
  lessons.push(MODS.security,MODS.regulation);
  const architectures=[
    {name:'Workload boundary',detail:LABELS.workload[v.workload],owner:'Product owner'},
    {name:'Data and retrieval',detail:siteOnly?'On-site documents, vector index, model context, logs and local backups':sensitive?'Restricted data, role-aware retrieval and derived-data governance':'Scoped data, retention and access policies',owner:'Enterprise data owner'},
    {name:'Inference and model',detail:model,owner:['onprem','airgap','localoffline','private','gated'].includes(id)?'Enterprise / physically verified':'Proposed model/service operator'},
    {name:'Operations and identity',detail:operations,owner:'Security and platform engineering'},
    {name:'Networks and evidence',detail:traffic,owner:'Network and assurance leads'}
  ];
  return {input:v,pattern:id,title,why,steps,architectures,controls,trace,gates,conflicts,lessons,
    status:conflicts.length?'BLOCKED':'PROVISIONAL',sensitivity:sensitive?'Restricted':v.data==='internal'?'Internal':'Public or synthetic',source:'Course-authored decision rules v'+VERSION};
}

function choice(text,why){return {text,why};}
export function createChallenges(raw={}) {
  const v=normalize(raw);const qs=[];
  const siteOnly=['premises','airgap','approved_sites'].includes(v.location);
  const onsite=['onsite_cpu','onsite_gpu'].includes(v.capacity);
  const siteConflict=siteOnly&&(!onsite||!['enterprise','onsite_partner'].includes(v.operator)||['internet','flexible'].includes(v.connectivity)||(v.location==='premises'&&v.connectivity==='private_links')||(v.location==='airgap'&&v.connectivity!=='disconnected'));
  if(siteOnly){
    qs.push({id:'location',dimension:'Territorial',question:'All enterprise data and derived artifacts must remain physically on the premises. A vendor asks to upload model diagnostics to its external support portal. What should you do?',options:[choice('Permit it because diagnostics are not the original documents.','Diagnostics can contain prompts, metadata, traces or derived data and require classification.'),choice('Keep diagnostics local, block the export path, and require an approved evidence-backed exception if the policy changes.','Correct. The boundary applies to derivatives and support workflows, not just the original files.'),choice('Permit it if encryption is enabled.','Encryption does not make off-premises transfer compatible with a strict location prohibition.')],correct:1,root:'Treating observability and support artifacts as outside the data boundary.',action:'Run a no-data-egress test on telemetry, updates, backup, export and remote-support paths.',lesson:MODS.data});
  } else if(['country','region','zone','approved'].includes(v.location)) {
    qs.push({id:'location',dimension:'Territorial',question:'A provider promises storage inside your approved region but does not specify inference-log destinations. What is proven?',options:[choice('The service is entirely sovereign.','Storage is only one path.'),choice('Only the bounded storage claim; logs, model calls, support and backup paths require independent review.','Correct. Do not extrapolate a narrow product commitment.'),choice('Encryption means processing location no longer matters.','Cryptography does not remove location constraints.')],correct:1,root:'Overgeneralizing a narrow data residency statement.',action:'Trace each runtime path and compare destinations with approved locations.',lesson:MODS.data});
  } else {
    qs.push({id:'location',dimension:'Territorial',question:'Processing geography is flexible. Is a destination inventory still necessary?',options:[choice('No, geographic flexibility removes data-flow obligations.','Flexible does not mean unknown.'),choice('Yes, record what flows where, which data is included and why it is allowed.','Correct. Visibility is a prerequisite for risk decisions.'),choice('No, an open-weight model cannot transmit information.','Serving infrastructure and telemetry can still move data.')],correct:1,root:'Treating unconstrained geography as an absence of governance.',action:'Record actual processing and logging destinations.',lesson:MODS.data});
  }
  if(siteConflict){
    qs.push({id:'operations',dimension:'Operational',question:'The premises-only requirement conflicts with the selected compute, access or connectivity option. What should the PM approve?',options:[choice('Launch using a remote cloud model and note the exception after release.','An unapproved external model violates the stated hard boundary.'),choice('Block real-data deployment. Keep only a synthetic local prototype while capacity, access and egress requirements are corrected.','Correct. Hard conflicts must be resolved or formally changed before processing real data.'),choice('Rename the system sovereign and rely on contractual marketing language.','A label and an unverified contract do not change an incompatible network path.')],correct:1,root:'Treating a hard data boundary as a preference that can be traded away silently.',action:'Assign owners to the conflicting input choices, procure on-site compute, and run egress and privileged-access tests.',lesson:MODS.infrastructure});
  } else if(v.operator==='enterprise'&&!['onsite_cpu','onsite_gpu','private_dc','gpu','colo'].includes(v.capacity)){
    qs.push({id:'operations',dimension:'Operational',question:'Enterprise-only operators are required but enterprise compute is unavailable. What decision is defensible?',options:[choice('Launch a provider-run platform and mark the requirement satisfied.','Provider-administered hosting does not automatically meet enterprise-only control.'),choice('Gate the prototype; acquire capacity or formally revise operating requirements.','Correct. Resolve the impossible operating assumption.'),choice('Disable administrative logging.','Removing evidence does not create capacity.')],correct:1,root:'Choosing an architecture before resolving operating authority.',action:'Document a blocking decision with owner and acceptance criterion.',lesson:MODS.infrastructure});
  } else {
    qs.push({id:'operations',dimension:'Operational',question:'A platform hosts the model in an approved location. What demonstrates operational control?',options:[choice('The marketing term sovereign.','Marketing wording is not access evidence.'),choice('A photograph of the data center.','Location does not establish who can administer it.'),choice('Privileged identities, actual support paths, key custody and tested access policies.','Correct. Operational authority requires enforceable and inspectable controls.')],correct:2,root:'Substituting a location assertion for operational access evidence.',action:'Review privileged roles and execute a negative authorization test.',lesson:MODS.security});
  }
  if(['essential','owned','strong'].includes(v.portability)){
    qs.push({id:'portability',dimension:'Technological',question:'Your local platform uses portable model files. Does that alone guarantee a vendor exit?',options:[choice('No. Rehearse a rebuild and migration using the actual license, runtime, integrations and dependencies.','Correct. A weight file is one input to a complete migration.'),choice('Yes. Model weight format guarantees every application will behave identically.','Serving, tokenizers, guardrails, tooling and performance can differ.'),choice('Yes, because on-premises deployments have no supply-chain dependencies.','Local hardware, packages and vendor support remain dependencies.')],correct:0,root:'Mistaking one portable artifact for an operable exit plan.',action:'Run an offline or authorized migration rehearsal with timing, quality and licensing checks.',lesson:MODS.agents});
  } else {
    qs.push({id:'portability',dimension:'Technological',question:'Provider exit is a lower-priority requirement. What should still be recorded?',options:[choice('Nothing; this removes all dependency risk.','A deferred risk is still an owned decision.'),choice('The accepted dependency, estimated exit effort, owner and review trigger.','Correct. Transparent trade-offs support future decisions.'),choice('A guarantee that exit will always be easy.','An untested guarantee is not meaningful evidence.')],correct:1,root:'Treating a prioritized-down risk as nonexistent.',action:'Record the dependency and review trigger in the decision log.',lesson:MODS.ontology});
  }
  const stem=v.evidence==='adverse'?'A controlled test reportedly found a boundary violation.':v.evidence==='none'?'No runtime test has been recorded.':['tested','independent','logs','configuration'].includes(v.evidence)?'Records exist, but the acceptance result has not been validated.':'Only policy, vendor or design documents are available.';
  qs.push({id:'evidence',dimension:'Evidence',question:`${stem} What claim state should you use?`,options:[choice('PASS because some documentation exists.','Documentation alone does not establish an accepted passing result.'),choice(v.evidence==='adverse'?'Reported nonconformance: stop release and investigate, remediate and retest.':['tested','independent'].includes(v.evidence)?'REVIEW_REQUIRED until evidence outcomes and scope are accepted.':'UNVERIFIED until valid evidence supports the claim.','Correct. Status depends on reviewed evidence and adverse observations.'),choice('CERTIFIED because the tool generated an architecture.','The questionnaire cannot issue certifications.')],correct:1,root:'Conflating evidence presence with a passing control outcome.',action:v.evidence==='adverse'?'Record the adverse path, root cause, owner, containment and dated retest.':'Define a repeatable test, criteria and reviewer.',lesson:MODS.foundations});
  return qs;
}

export function evaluateChallenge(question,answerIndex){const option=question.options[answerIndex];if(!option)return null;const ok=answerIndex===question.correct;return {ok,feedback:option.why,root:question.root,action:question.action,lesson:question.lesson};}
export function compareBlueprints(a,b){const x=createBlueprint(a),y=createBlueprint(b);const keys=Object.keys(LABELS).filter(k=>x.input[k]!==y.input[k]);return {previous:x,current:y,changed:keys,patternChanged:x.pattern!==y.pattern,gatesAdded:y.gates.filter(g=>!x.gates.includes(g)),gatesRemoved:x.gates.filter(g=>!y.gates.includes(g))};}
export function exportJournal(blueprint,qs,answers,reflection=''){
  const clean=s=>String(s??'').replace(/\r/g,'').replace(/[\x00-\x08\x0B-\x1F]/g,'').replace(/\|/g,'\\|');
  const lines=['# Sovereignty learning journal','','> Public-learning artifact. Never add credentials, customer data, or personal identifiers.','','## Workload assumptions',''];
  for(const [key,value] of Object.entries(blueprint.input))lines.push(`- **${key}:** ${clean(LABELS[key][value])}`);
  lines.push('','## Provisional architecture','','**Pattern:** '+clean(blueprint.title),'','**Status:** '+blueprint.status,'','**Reason:** '+clean(blueprint.why),'','### Components');
  for(const c of blueprint.architectures)lines.push(`- **${c.name}:** ${clean(c.detail)}. Owner: ${clean(c.owner)}.`);
  lines.push('','### Claims and validation');
  for(const c of blueprint.controls)lines.push(`- **${c.id} / ${c.dimension} / ${c.evidence}:** ${clean(c.claim)}. Test: ${clean(c.test)}`);
  lines.push('','### Unresolved gates');for(const g of blueprint.gates)lines.push('- '+clean(g));
  lines.push('','## Adaptive tutor review','');
  qs.forEach((q,i)=>{let a=answers[q.id];lines.push(`### ${i+1}. ${clean(q.question)}`);if(a==null){lines.push('Not attempted.','');return;}const e=evaluateChallenge(q,a);lines.push(`- Selected: ${clean(q.options[a].text)}`);lines.push(`- Result: ${e.ok?'Correct reasoning':'Needs review'}`);lines.push(`- Feedback: ${clean(e.feedback)}`);if(!e.ok)lines.push(`- Root cause: ${clean(e.root)}. Corrective action: ${clean(e.action)}`);lines.push('');});
  lines.push('## My explanation and next test','',clean(reflection).replace(/</g,'&lt;')||'_Not written_','','## Source and scope','','Course-authored ontology: https://shantanuchandra.github.io/sovereign-ai-mastery/taxonomy/ONTOLOGY.html','','This worksheet is a learning hypothesis, not a legal opinion or certified architecture.');
  return lines.join('\n')+'\n';
}