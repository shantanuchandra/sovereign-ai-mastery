const scenarios = {
  best: {
    name: 'Best case', launch: 'Days 42–50',
    trigger: 'Customer access, source approval and named approvers are in place by day 14. One integrated request passes by day 28.',
    action: 'Pass Recovery and Security before core launch. Enable sharing and reuse after their own access tests pass. Consider one partner-backed P2 validation if P0 and P1 are on track.',
    outcome: 'Customer acceptance and enough live evidence to judge repeat use, verified savings and independent peer reuse. Test one adjacent use only if those signals support it.',
  },
  average: {
    name: 'Average case', launch: 'Days 57–70',
    trigger: 'The customer is committed. Identity, integration or the security review needs another iteration.',
    action: 'Keep the release to one team, one read-only workflow, one source and one approved route. Enable P1 for the same cohort after core and sharing controls pass. Defer P2.',
    outcome: 'A controlled deployment and an impact readout covering the available work cycles. If launch is near day 70, some cohorts may need a follow-up observation window.',
  },
  worst: {
    name: 'Worst case', launch: 'Launch held',
    trigger: 'A required approval, source access, a customer environment or a mandatory control remains open.',
    action: 'Use capacity for P0 fixes and staging rehearsals. Keep live launch on hold until all mandatory gates pass for the agreed scope. Defer P1 and P2.',
    outcome: 'A tested release candidate and a named owner and date for the remaining dependency. The deployment objective remains open until customer acceptance and live evidence are available.',
  },
};

const features = [
  {
    id: 'continuity', priority: 'P0', name: 'Pilot navigation and state recovery',
    actions: ['Confirm which return paths prevent completion of the pilot checklist.', 'Fix and test those paths for the originating conversation and permitted working state.'],
    measure: 'A · All agreed navigation cases pass. Users resume the real task without reconstructing context.',
    why: 'A broken return path interrupts the very workflow users need to repeat.',
    days: [[1,14],[1,14],[1,14]],
  },
  {
    id: 'answers', priority: 'P0', name: 'Jean · Verifiable answers',
    actions: ['Prototype a cited answer or checklist on one real task.', 'Add coverage for missing evidence, contradictory records and mismatched totals.'],
    measure: 'A, I, G · Customer case acceptance, material corrections, time to a verified result and citation support.',
    why: 'Users need to check the work quickly enough for the assisted path to save time.',
    days: [[8,35],[8,49],[8,56]],
  },
  {
    id: 'connector', priority: 'P0', name: 'Connectors + Dotti · Fresh evidence',
    actions: ['Connect one approved source and test two permission roles.', 'Verify refresh, deletion and revocation. Measure API and ingestion cost before changing cadence.'],
    measure: 'I, G, R · Source updates meet the agreed freshness window. All mandatory access cases pass. A second operator reproduces setup.',
    why: 'A convincing answer can still be wrong when documents change or a user loses access.',
    days: [[8,35],[8,49],[8,63]],
  },
  {
    id: 'routing', priority: 'P0', name: 'Simon · Approved route and recovery',
    actions: ['Record model, version and routing reason for one approved route.', 'Before launch, have Customer IT time an approved rollback and verify workflow and security controls after restore.'],
    measure: 'S, R · All mandatory route cases pass. Customer IT restores the last approved release within 30 minutes and reruns workflow and security checks.',
    why: 'The customer must be able to verify where inference ran and recover from a bad update.',
    days: [[15,42],[15,56],[15,70]],
  },
  {
    id: 'gateway', priority: 'P0', name: 'Gateway · Policy enforcement and audit',
    actions: ['Map mandatory allow, deny, revocation and outage cases to customer policy and expected audit evidence.', 'Run the suite against the release candidate and have Customer Security reconstruct sampled decisions and sign off.'],
    measure: 'S · Every mandatory RBAC, routing, policy and outage test passes. Zero unauthorised disclosures in the acceptance suite and Security approves the audit evidence.',
    why: 'Customer approval depends on evidence that policy applies to the workflow and to shared results.',
    days: [[8,42],[8,56],[8,70]],
  },
  {
    id: 'synthia', priority: 'P0', name: 'Synthia · Held-out release evaluation',
    actions: ['Version synthetic regression cases for stale sources, conflicting evidence and permission changes.', 'Pair them with customer acceptance cases and verify the suite detects selected known failures.'],
    measure: 'G, S · Known regressions are detected. Customer acceptance tests are scored against the exact candidate and can be rerun.',
    why: 'Synthetic coverage helps catch regressions. Customer cases prove fidelity to the actual workflow.',
    days: [[8,42],[8,56],[8,77]],
  },
  {
    id: 'launch', priority: 'P0', name: 'Controlled launch and live observation',
    actions: ['Obtain sponsor, IT and Security approval after the mandatory recovery and security gates pass in the target environment.', 'Enable named users and review completed work cycles with the sponsor.'],
    measure: 'A, I, S · Customer-approved live use, repeat adoption with verified savings and a recorded observation window.',
    why: 'A staged release proves readiness. Live work cycles show whether the customer changes how they work.',
    days: [[42,90],[57,90],null],
  },
  {
    id: 'impact', priority: 'P0', name: 'Impact assessment and deployment playbook',
    actions: ['Freeze the measurement method and manual baseline by day 28.', 'After launch, measure paired manual and assisted cases. Ask a second operator to repeat setup and recovery.', 'Share exact minutes and AED saved, the matched case count and dates, rework and deployment effort for the Day 90 decision.'],
    measure: 'A, I, R, S · Signed savings and rework readout, timed recovery, Security evidence and second-operator results.',
    why: 'The day-90 decision needs proof of customer value and a credible way to deliver it again.',
    days: [[1,90],[1,90],[1,90]],
  },
  {
    id: 'sharing', priority: 'P1', name: 'Share a verified result',
    actions: ['Prototype an in-tenant link for Colleague A and Colleague B.', 'Activate after approval of the core release and passing share, open and revocation tests. Measure share-to-open conversion.'],
    measure: 'P, S · Report share-to-open and open-to-first-run conversion. All recipient and revocation tests pass.',
    why: 'A colleague can discover JEAN in the context of useful work and verify value for themselves.',
    days: [[29,70],[43,84],null],
  },
  {
    id: 'reuse', priority: 'P1', name: 'Reuse the workflow',
    actions: ['Give the recipient a way to start a fresh run with their own permissions and inputs.', 'Compare a simple reuse action with a scoped Mate if a real handoff gap emerges.'],
    measure: 'P, I, S · Independent verified runs and subsequent repeat use with savings. Permission checks pass for reused tasks.',
    why: 'The second user needs a clear route from reading a useful result to producing one.',
    days: [[43,77],[57,90],null],
  },
  {
    id: 'authoring', priority: 'P2', name: 'Validate one Gateway rule template',
    actions: ['Reserve a best-case validation window. Use it only if a named partner confirms that rule authoring slows the pilot and P0 and P1 are on track.', 'Test a paper or interactive prototype for one proven rule.'],
    measure: 'S, R · Compare setup time and policy errors with the current authoring method before funding implementation.',
    why: 'A repeatable template could reduce delivery effort after the first rule has been proven.',
    days: [[71,84],null,null],
  },
  {
    id: 'dashboard', priority: 'P2', name: 'Evidence view for the pilot sponsor',
    actions: ['Consider this as an alternative to the rule-template validation if the customer identifies a more important evidence-retrieval blocker.'],
    measure: 'S · Compare time to find the relevant evidence and accuracy of the reviewer’s interpretation.',
    why: 'A narrow evidence view has a testable job for an existing customer.',
    days: [null,null,null],
  },
  {
    id: 'next-connector', priority: 'P2', name: 'Validate one additional connector',
    actions: ['Review as an alternative P2 validation if a named design partner can show that an additional source is needed for the next workflow.'],
    measure: 'I, R · Document the recurring use case, source permissions and expected integration effort before staffing a build.',
    why: 'Connector demand is worth validating once the existing source works for the pilot.',
    days: [null,null,null],
  },
  {
    id: 'discovery', priority: 'P3', name: 'Advanced triage, graph exploration and Sovereignty Score',
    actions: ['Keep these in the research backlog. Revisit after Day 90 when a named sponsor can describe a workflow and a measurable problem.'],
    measure: 'Research · A named user, recurring problem and testable outcome earn a discovery slot.',
    why: 'The pilot can complete its checklist and acceptance review with existing tools and linked evidence.',
    days: [null,null,null],
  },
  {
    id: 'twin', priority: 'P3', name: 'Project Twin · War-gaming research',
    actions: ['Revisit after Day 90 if a customer sponsors one concrete simulation or planning use case.'],
    measure: 'Research · A validated use case and an evaluation plan for held-out scenarios.',
    why: 'Both simulation modes need a customer-backed problem before they earn capacity.',
    days: [null,null,null],
  },
];

const scenarioOrder = Object.keys(scenarios);
const periodEnds = [14, 28, 42, 56, 70, 84, 90];
const state = { scenario: 'average', filter: 'all' };
const byId = (id) => document.getElementById(id);
const priorityClass = (priority) => priority.toLowerCase();

const measureLinks = {
  A: ['adoption-measure', 'Adoption'],
  I: ['impact-measure', 'Impact'],
  G: ['governance-measure', 'Governance and quality'],
  R: ['repeatability-measure', 'Repeatability'],
  S: ['recovery-security-measure', 'Recovery and Security'],
  P: ['peer-growth-measure', 'Peer-led growth'],
};

function renderMeasure(measure) {
  const [codes, description] = measure.split(' · ');
  const links = codes.split(', ').map((code) => {
    const target = measureLinks[code];
    return target ? `<a href="#${target[0]}">${target[1]}</a>` : code;
  });
  return `<p class="measure-links">${links.join(' / ')}</p><p>${description}</p>`;
}

function renderFeatures() {
  byId('features').innerHTML = features.map((feature) => `
    <tr id="feature-${feature.id}">
      <th scope="row" data-label="Feature"><span class="tag ${priorityClass(feature.priority)}">${feature.priority}</span> ${feature.name}</th>
      <td data-label="Actions"><ul>${feature.actions.map((action) => `<li>${action}</li>`).join('')}</ul></td>
      <td data-label="Success measure">${renderMeasure(feature.measure)}</td>
      <td data-label="Why this is a priority">${feature.why}</td>
    </tr>`).join('');
}

const types = {
  product: ['Product engineering', '#2269ad'], platform: ['Platform engineering', '#694da6'],
  policy: ['Governance engineering', '#944777'], eval: ['AI evaluation', '#077f83'],
  test: ['Acceptance testing', '#ae641c'], pilot: ['Pilot observation', '#45824c'],
  deploy: ['Deployment', '#285699'], buffer: ['Contingency buffer', '#82704c'],
  analysis: ['Discovery and impact', '#627482']
};
const owners = {continuity:'product',answers:'product',connector:'platform',routing:'platform',gateway:'policy',synthia:'eval',sharing:'product',reuse:'product',launch:'pilot',impact:'analysis',authoring:'policy',dashboard:'product','next-connector':'analysis',discovery:'analysis',twin:'analysis'};
const holidays = new Set(['2026-12-02','2026-12-03','2027-01-01']);
const calendar = Array.from({length:90}, (_, i) => {
  const date = new Date(Date.UTC(2026,10,23+i));
  return {day:i+1, label:date.toLocaleDateString('en-GB',{day:'numeric',month:'short',timeZone:'UTC'}),
    off:[0,6].includes(date.getUTCDay()) || holidays.has(date.toISOString().slice(0,10))};
});
const timelineLink = key => '#timeline-'+key;
function renderGantt() {
  const index = scenarioOrder.indexOf(state.scenario);
  const matching = features.filter(f => state.filter === 'all' || f.priority === state.filter);
  const rows = matching.filter(f => f.days[index]).map(f => ({...f, range:f.days[index],type:owners[f.id]}));
  if (state.filter === 'all' || state.filter === 'P0') {
    const gate = [42,56,77][index];
    rows.push({id:'synthia',name:'Acceptance, security and timed recovery tests',priority:'P0',range:[gate-10,gate-4],type:'test'},
      {id:'gateway',name:'Reserved for mandatory fixes and retest',priority:'P0',range:[gate-3,gate],type:'buffer'});
    if(index<2) {
      const launch = rows.find(r=>r.id==='launch');
      const first = calendar.find(c=>!c.off && c.day>=launch.range[0]).day;
      rows.push({...launch,name:'Enable named users after approval',range:[first,first],type:'deploy'});
      launch.range=[first+1,90];
    }
  }
  const ticks=periodEnds.map((end,i)=>'<span>'+calendar[i?periodEnds[i-1]:0].label+'</span>').join('');
  byId('gantt').innerHTML='<div class="chart-row chart-header"><strong>Priority and work</strong><div class="ticks">'+ticks+'</div></div>'+rows.map(r=>{
    const [name,color]=types[r.type];
    const cells=calendar.map(c=>'<i class="'+(c.off?'off':c.day>=r.range[0] && c.day<=r.range[1]?'active':'')+'" title="'+c.label+' · '+(c.off?'Off':name)+'"></i>').join('');
    return '<div class="chart-row"><a class="chart-name" href="#feature-'+r.id+'"><span class="tag '+priorityClass(r.priority)+'">'+r.priority+'</span><span>'+r.name+'<small>'+name+'</small></span></a><div class="day-track" style="--ink:'+color+'">'+cells+'</div></div>';
  }).join('')+(rows.length?'':'<p class="empty">No work scheduled at this priority.</p>');
  const deferred=matching.filter(f=>!f.days[index]);
  byId('deferred').textContent=deferred.length?'Outside this schedule · '+deferred.map(f=>f.name).join(' · '):'';
}
byId('work-key').innerHTML=Object.values(types).map(([name,color])=>'<span><i style="background:'+color+'"></i>'+name+'</span>').join('');
byId('scenario-summary').innerHTML='<table><thead><tr><th>Scenario</th><th>Trigger</th><th>Release decision</th><th>Day-90 evidence</th></tr></thead><tbody>'+scenarioOrder.map(k=>{
  const s=scenarios[k];
  return '<tr><th scope="row"><a href="'+timelineLink(k)+'">'+s.name+' →</a></th><td>'+s.trigger+'</td><td><strong>'+s.launch+'</strong><br>'+s.action+'</td><td>'+s.outcome+'</td></tr>';
}).join('')+'</tbody></table>';
function renderScenario(){
  const s=scenarios[state.scenario];
  byId('chart-scenario').textContent=s.name;
  byId('ready-day').textContent=s.launch.toUpperCase();
  byId('schedule-links').innerHTML=scenarioOrder.map(k=>'<a href="'+timelineLink(k)+'" '+(k===state.scenario?'aria-current="true"':'')+'>'+scenarios[k].name+'</a>').join('');
  renderGantt();
}
function followLink(){
  const id=location.hash.slice(1);
  const key=scenarioOrder.find(k=>'timeline-'+k===id);
  if(key){state.scenario=key;renderScenario();byId('schedule').open=true;byId('timeline').scrollIntoView();}
  const node=byId(id);
  if (node?.matches('.workflow-access')) {
    node.open = true;
    node.scrollIntoView();
  }
}
window.addEventListener('hashchange',followLink);
document.addEventListener('click',event=>{if(event.target.closest('a')?.hash===location.hash && location.hash) followLink();});
byId('priority-filter').addEventListener('change', (event) => {
  state.filter = event.target.value;
  renderGantt();
});

renderFeatures();
renderScenario();
followLink();

const themeButton = byId('theme-toggle');
const themeLabel = byId('theme-label');
const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
const themeKey = 'metis-roadmap-theme';
let selectedTheme;

try {
  const saved = window.localStorage.getItem(themeKey);
  if (saved === 'light' || saved === 'dark') selectedTheme = saved;
} catch {
  // Theme switching still works when storage is unavailable.
}

function applyTheme() {
  const theme = selectedTheme ?? (systemTheme.matches ? 'dark' : 'light');
  const nextTheme = theme === 'dark' ? 'Light' : 'Dark';
  document.documentElement.dataset.theme = theme;
  themeLabel.textContent = nextTheme;
  themeButton.setAttribute('aria-label', `Switch to ${nextTheme.toLowerCase()} theme`);
}

themeButton.addEventListener('click', () => {
  selectedTheme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
  applyTheme();
  try {
    window.localStorage.setItem(themeKey, selectedTheme);
  } catch {
    // The selected theme still applies to this page.
  }
});

systemTheme.addEventListener('change', applyTheme);
applyTheme();
themeButton.hidden = false;
