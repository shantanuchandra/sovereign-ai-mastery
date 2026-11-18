/**
 * Sovereignty Learning Studio: transparent, deterministic, educational rules.
 * No external models, telemetry, vendor verification or legal determinations.
 * These outputs are architecture hypotheses, not certifications.
 */

export const VERSION = '1.0.0';
export const LABELS = Object.freeze({
  workload: {knowledge:'Internal knowledge assistant',customer:'Customer-facing assistant',regulated:'Regulated document analysis'},
  data: {public:'Public material only',internal:'Internal business documents',sensitive:'Sensitive or regulated information'},
  location: {country:'Selected country only',zone:'Approved geographic zone',flexible:'No strict processing geography'},
  operator: {enterprise:'Enterprise-authorized administrators only',local:'Approved managed-service operators',provider:'Provider administration permitted by contract'},
  portability: {essential:'Mandatory; exit rehearsals required',useful:'Important but negotiable',low:'Low priority for this pilot'},
  capacity: {laptop:'Laptop / prototype only',managed:'Approved managed platform available',gpu:'Enterprise-operated production compute'},
  evidence: {none:'No mapped evidence',design:'Architecture and contracts only',tested:'Test records exist but are not reviewed'},
  jurisdiction: {uae:'UAE',saudi:'Saudi Arabia',eu:'European Union',other:'Other or undecided'},
  stage: {prototype:'Exploration',pilot:'Controlled pilot',production:'Production rollout'}
});
export const DEFAULTS = Object.freeze({
  workload:'knowledge', data:'internal', location:'country', operator:'local', portability:'essential',
  capacity:'managed', evidence:'none', jurisdiction:'uae', stage:'pilot'
});
export const PRESETS = Object.freeze({
  assistant: {...DEFAULTS},
  banking:{...DEFAULTS,workload:'regulated',data:'sensitive',location:'country',operator:'enterprise',capacity:'laptop',stage:'production'},
  support:{...DEFAULTS,workload:'customer',data:'public',location:'zone',operator:'provider',portability:'low',capacity:'managed',jurisdiction:'saudi',stage:'pilot'},
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
  const v=normalize(raw);const strict=v.location==='country';const owned=v.operator==='enterprise';
  const managedOperator=v.operator==='local';const prodGPU=v.capacity==='gpu';
  const sensitive=v.data==='sensitive';const critical=v.stage==='production';
  const conflicts=[];const trace=[];const gates=[];
  let id,title,why,steps,model,operations,traffic;
  if(owned&&!prodGPU){
    id='gated';title='Gated local prototype and infrastructure decision';
    why='Enterprise-only administration is a hard constraint, but production compute is not available. No managed offering is assumed to satisfy it. Prototype safely and resolve the operating model first.';
    steps=['Prototype with synthetic material on local hardware','Procure enterprise-operated capacity or formally revise the operator boundary','Do not process sensitive data in a production service until the conflict is resolved'];
    model='Local small-model inference for learning; production model undecided';operations='Enterprise operators only; no provider access assumed';traffic='Prototype-only egress deny rules, then production path testing';
    conflicts.push('Operator constraint and infrastructure capability do not currently support a production design.');
    gates.push('Block production approval pending capacity or an explicitly changed operator requirement.');
  }else if(owned&&prodGPU){
    id='private';title='Enterprise-operated private serving';
    why='Enterprise-operated compute can support direct administrative control. That does not establish complete sovereignty until model artifacts, remote maintenance, telemetry and failover are traced.';
    steps=['Deploy private serving on approved enterprise infrastructure','Implement enterprise IAM, key custody, restricted egress and audit logging','Test normal, support, diagnostic and disaster-recovery paths'];
    model='Private model endpoint with reviewed model license and provenance';operations='Enterprise-run control plane, identities and key custody';traffic='Private application-to-model route with explicit egress allow-list';
  }else if(strict || managedOperator || sensitive){
    id='managed';title='Controlled managed serving with evidence gates';
    why='A managed platform may reduce operating burden. Geography, privileged access, subcontractors, logs and failover must be verified for the exact deployment and contract.';
    steps=['Verify an available deployment option meets geographic and access needs','Isolate enterprise data and make model requests through a governed gateway','Require independent checks of support paths, telemetry and contractual terms'];
    model='Scoped managed model endpoint, subject to exact region/SKU review';operations=managedOperator?'Approved managed administrators plus enterprise access review':'Provider-administered under explicit contractual controls';traffic='Location-aware routing and logging controls; actual endpoints unverified';
    if(strict)gates.push('Verify that inference, logging and disaster recovery stay in the selected country.');
  }else if(v.portability==='essential' || v.location==='zone'){
    id='hybrid';title='Portable hybrid gateway architecture';
    why='A replaceable model gateway and bounded data tier fit a flexible operating environment with portability or region constraints.';
    steps=['Keep document retrieval and policy enforcement behind a controlled gateway','Use replaceable inference adapters and explicit data-boundary rules','Rehearse export, provider substitution and policy validation'];
    model='Provider models behind swappable inference adapters';operations='Provider operations permitted only within approved policies';traffic='Gateway records routing destinations and data classification';
  }else{
    id='api';title='Documented managed API experiment';
    why='Flexible processing and lower portability requirements support a small pilot with public or approved internal data. Vendor dependence and routing remain explicit.';
    steps=['Start with minimum-privilege inference and minimized prompts','Document destinations, retention and subprocessors','Set an exit decision before increasing scope'];
    model='Managed API model with explicit provider dependency';operations='Provider administration governed by signed terms';traffic='Minimal data flows, audit log redaction and basic egress observations';
  }
  if(critical&&!prodGPU&&id!=='gated')gates.push('Production-grade SLA, capacity, tenancy, and incident readiness must be validated; this questionnaire cannot verify them.');
  if(sensitive)gates.push('Sensitive data requires classification, authorized access, retention and human legal/security review before real use.');
  if(v.evidence!=='tested')gates.push('No inspected, passing runtime test is available. Treat all proposed controls as unverified.');
  if(v.evidence==='tested')gates.push('A test record exists, but its result and scope have not been inspected. A human reviewer must accept or reject it.');
  trace.push(step('scope',`Workload: ${LABELS.workload[v.workload]}`,'Sets the system and data boundary.'));
  trace.push(step('territorial',`Processing geography: ${LABELS.location[v.location]}`,strict?'Requires tracing request, log, support and failover locations.':'Still requires documenting actual routing.'));
  trace.push(step('operational',`Administrators: ${LABELS.operator[v.operator]}`,owned?'Constrains the permissible operating model and privileged identities.':'Requires explicit support access approval and contractual controls.'));
  trace.push(step('technological',`Exit requirement: ${LABELS.portability[v.portability]}`,v.portability==='essential'?'Requires an observed migration rehearsal, not just an open API.':'Record acceptable dependencies and a review trigger.'));
  trace.push(step('capacity',`Compute: ${LABELS.capacity[v.capacity]}`,id==='gated'?'Creates a blocker to production under enterprise-only administration.':'Makes the architecture a candidate, not a deployed system.'));
  trace.push(step('evidence',`Evidence: ${LABELS.evidence[v.evidence]}`,'Never infer success or compliance merely from document availability.'));
  trace.push(step('legal',`Jurisdiction: ${LABELS.jurisdiction[v.jurisdiction]}`,'Legal applicability is a qualified review task, not a browser calculation.'));
  const states=(key)=>conflicts.length&&key==='operational'?'CONFLICT':v.evidence==='tested'?'REVIEW_REQUIRED':'UNVERIFIED';
  const controls=[
    control('TERR-01','Territorial','Declared processing boundary covers requests and derived data','Region and egress policies plus logged destination inventory','Observe inference, embedding, logs, backups, support and failover paths',states('territorial')),
    control('OPS-01','Operational','Only authorized administrators may operate the service','Identity roles, privileged access review, key-custody boundaries','Review access grants; attempt an unauthorized admin action in a controlled test',states('operational')),
    control('TECH-01','Technological','Migration is feasible within accepted exit limits','Document weights/licensing and model gateway adapters','Export data and replace an endpoint; record compatibility and time',states('technological')),
    control('LEGAL-01','Legal/contractual','Applicable obligations and provider terms are understood','Counsel-reviewed applicability matrix and signed relevant clauses','Review actual entities, activities, terms, subprocessors and transfer paths','REVIEW_REQUIRED')
  ];
  if(v.portability!=='essential')controls[2].claim='Critical dependencies and acceptable exit limits are documented';
  const lessons=[MODS.foundations,MODS.ontology];
  if(strict||sensitive)lessons.push(MODS.data);
  if(owned||prodGPU||managedOperator)lessons.push(MODS.infrastructure);
  if(v.portability==='essential')lessons.push(MODS.agents);
  lessons.push(MODS.security,MODS.regulation);
  const architectures=[
    {name:'Workload and users',detail:LABELS.workload[v.workload],owner:'Enterprise product owner'},
    {name:'Data and retrieval',detail:sensitive?'Restricted documents, classified embeddings and audit trails':'Scoped data sources, retention and retrieval permissions',owner:'Enterprise data owners'},
    {name:'Model serving',detail:model,owner:id==='private'||id==='gated'?'Enterprise / proposed':'Provider or approved operator / proposed'},
    {name:'Operations and identity',detail:operations,owner:'Security and platform engineering'},
    {name:'Trust and evidence',detail:traffic,owner:'Architecture review and assurance'}
  ];
  return {input:v,pattern:id,title,why,steps,architectures,controls,trace,gates,conflicts,lessons,status:conflicts.length?'BLOCKED':'PROVISIONAL',sensitivity:sensitive?'Restricted':v.data==='internal'?'Internal':'Public',source:'Course-authored decision rules v'+VERSION};
}

function choice(text,why){return {text,why};}
export function createChallenges(raw={}) {
  const v=normalize(raw);
  const qs=[];
  if(v.location==='country'){
    qs.push({id:'location',dimension:'Territorial',question:'A vendor confirms that files stay in your country, but says nothing about inference logs. What can you conclude?',options:[choice('The service is fully sovereign.','File storage is only one data path.'),choice('The storage claim is narrow; verify inference, telemetry, backups and failover.','Correct. Verify all declared data paths against the location criterion.'),choice('Contract language alone proves all traffic routes.','A signed promise and a measured runtime path are different evidence.')],correct:1,root:'Confusing stored-data location with the full processing boundary.',action:'Draw the data flow for one prompt, including telemetry and support.',lesson:MODS.data});
  }else{
    qs.push({id:'location',dimension:'Territorial',question:'Geography is flexible. Does that eliminate territorial analysis?',options:[choice('Yes. No data flow map is necessary.','Flexible is not the same as unknown.'),choice('No. Record actual destinations and identify which data may travel.','Correct. A flexible boundary still needs a documented decision and visibility.'),choice('Yes, if the model is open-weight.','Model licensing does not describe network destinations.')],correct:1,root:'Treating the absence of a location restriction as the absence of data governance.',action:'Record permitted processing destinations and exclusions.',lesson:MODS.data});
  }
  if(v.operator==='enterprise'&&v.capacity!=='gpu'){
    qs.push({id:'operations',dimension:'Operational',question:'You require enterprise-only administrators, but have no production compute. Which decision is defensible?',options:[choice('Launch on a provider-run platform and call the requirement satisfied.','The provider operating model may violate the non-negotiable constraint.'),choice('Keep the prototype gated; acquire capacity or formally revise the constraint.','Correct. A conflict must not be hidden behind a deployment label.'),choice('Remove administrative logging to reduce workload.','This weakens evidence and does not create capacity.')],correct:1,root:'Architecture selected before resolving an incompatible operating assumption.',action:'Create a decision record with the blocking constraint and change owner.',lesson:MODS.infrastructure});
  }else{
    qs.push({id:'operations',dimension:'Operational',question:'A provider hosts your model in an approved geography. What evidence is most relevant to operational control?',options:[choice('The provider sales brochure says sovereign.','Marketing wording is not a privileged-access review.'),choice('A map displaying the data center.','Location does not specify who can administer the service.'),choice('Named support identities, privileged roles, key custody, and access tests.','Correct. Administrative authority must be traced and tested.')],correct:2,root:'Substituting a location assertion for evidence of operational authority.',action:'Request the support access matrix and run a negative privilege test.',lesson:MODS.security});
  }
  if(v.portability==='essential'){
    qs.push({id:'portability',dimension:'Technological',question:'Your architecture uses an open API. Does that prove a viable vendor exit?',options:[choice('No. Test data export, model substitution, behavior, licensing and migration time.','Correct. An API convention is only one part of portability.'),choice('Yes. All open APIs are behaviorally equivalent.','Models, prompts, tools, policies and weights can differ significantly.'),choice('Yes, if inference stays in-country.','Territorial and technological controls are independent.')],correct:0,root:'Confusing a standardized interface with demonstrated substitutability.',action:'Perform a time-boxed migration rehearsal and record residual dependencies.',lesson:MODS.agents});
  }else{
    qs.push({id:'portability',dimension:'Technological',question:'Exit planning is a lower priority for this pilot. What should still be captured?',options:[choice('Nothing; portability no longer matters.','The dependency and reason for tolerating it still matter.'),choice('Document the dependency, accepted exit cost, owner and review trigger.','Correct. Low priority is not zero accountability.'),choice('Promise migration will be effortless.','A promise without a rehearsal is not an observed result.')],correct:1,root:'Treating prioritized-down risk as nonexistent risk.',action:'Add a vendor dependency and exception entry to the decision log.',lesson:MODS.ontology});
  }
  const stem=v.evidence==='none'?'No one has recorded a runtime sovereignty test.':v.evidence==='design'?'The team has an architecture diagram and a signed contract, but no runtime test.':'Someone uploaded a test report, but the observations and scope have not been reviewed.';
  qs.push({id:'evidence',dimension:'Evidence',question:`${stem} What is the correct claim status?`,options:[choice('PASS; documentation is enough.','A document or unreviewed report does not establish a passing observed control.'),choice(v.evidence==='tested'?'REVIEW_REQUIRED until someone validates the report.':'UNVERIFIED until an applicable test produces reviewable evidence.','Correct. Match the evidence status to what was actually observed.'),choice('FAIL; all missing evidence proves the control is broken.','Failure requires a defined, valid adverse observation.')],correct:1,root:'Conflating absence of proof with success or observed failure.',action:'Define a falsifiable acceptance test, owner, evidence ID and review date.',lesson:MODS.foundations});
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