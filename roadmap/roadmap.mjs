const scenarios = {
  best: {
    name: 'Best case', launch: 'Days 42–50',
    trigger: 'Customer access, source approval and named approvers are in place by day 14. One integrated request passes by day 28.',
    action: 'Launch the core workflow once the gates pass. Use the longer observation window to measure the sharing and reuse loop and rehearse setup with a second operator.',
    outcome: 'Customer acceptance and enough live evidence to judge repeat use, verified savings and independent peer reuse. Test one adjacent use only if those signals support it.',
  },
  average: {
    name: 'Average case', launch: 'Days 57–70',
    trigger: 'The customer is committed. Identity, integration or the security review needs another iteration.',
    action: 'Keep the release to one team, one read-only workflow, one source and one approved route. Pilot permission-checked sharing and reuse with the same cohort after the core gates pass.',
    outcome: 'A controlled deployment and an impact readout covering the available work cycles. If launch is near day 70, some cohorts may need a follow-up observation window.',
  },
  worst: {
    name: 'Worst case', launch: 'Launch held',
    trigger: 'A required approval, source access, a customer environment or a mandatory control remains open.',
    action: 'Agree a smaller workflow or user group with the sponsor if it still has value. Keep the mandatory gates. Rehearse on approved staging data and defer the live growth experiments.',
    outcome: 'A tested release candidate and a named owner and date for the remaining dependency. The deployment objective remains open until customer acceptance and live evidence are available.',
  },
};

const features = [
  {
    id: 'continuity', priority: 'P0', name: 'Conversation → Canvas → Conversation',
    actions: ['Reproduce the wrong-conversation return path.', 'Restore the originating conversation and permitted working state on browser Back and in-app return.'],
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
    actions: ['Record model, version and routing reason for one approved route.', 'Rehearse a controlled update and rollback. Test the agreed response to route unavailability.'],
    measure: 'G, R · All mandatory route cases pass. IT restores and verifies the workflow within the agreed recovery window.',
    why: 'The customer must be able to verify where inference ran and recover from a bad update.',
    days: [[15,42],[15,56],[15,70]],
  },
  {
    id: 'gateway', priority: 'P0', name: 'Gateway · Policy enforcement and audit',
    actions: ['Agree on a decision matrix and link material rules to their source or owner.', 'Stress-test policy interactions and let Security reconstruct decisions. Verify recipient access on open before enabling sharing.'],
    measure: 'G · All mandatory decisions match the expected outcomes, including access after revocation. Security can reconstruct sampled decisions.',
    why: 'Customer approval depends on evidence that policy applies to the workflow and to shared results.',
    days: [[8,42],[8,56],[8,70]],
  },
  {
    id: 'synthia', priority: 'P0', name: 'Synthia · Held-out release evaluation',
    actions: ['Version synthetic regression cases for stale sources, conflicting evidence and permission changes.', 'Pair them with customer acceptance cases and verify the suite detects selected known failures.'],
    measure: 'G, R · Known regressions are detected. Customer acceptance tests are scored against the exact candidate and can be rerun.',
    why: 'Synthetic coverage helps catch regressions. Customer cases prove fidelity to the actual workflow.',
    days: [[8,42],[8,56],[8,77]],
  },
  {
    id: 'sharing', priority: 'P1', name: 'Share a verified result',
    actions: ['Prototype one permission-checked in-tenant share link.', 'Measure shares, authorised opens and independent first runs. Enable only after approval of the shared access path.'],
    measure: 'A, G · Report share-to-open and open-to-first-run conversion. All recipient and revocation tests pass.',
    why: 'A colleague can discover JEAN in the context of useful work and verify value for themselves.',
    days: [[29,70],[43,84],null],
  },
  {
    id: 'reuse', priority: 'P1', name: 'Reuse the workflow',
    actions: ['Give the recipient a way to start a fresh run with their own permissions and inputs.', 'Compare a simple reuse action with a scoped Mate if a real handoff gap emerges.'],
    measure: 'A, I, G · Independent verified runs and subsequent repeat use with savings. Permission checks pass for reused tasks.',
    why: 'The second user needs a clear route from reading a useful result to producing one.',
    days: [[43,77],[57,90],null],
  },
  {
    id: 'launch', priority: 'P0', name: 'Controlled launch and live observation',
    actions: ['Obtain workflow, IT and Security acceptance in the target environment.', 'Enable named users and review completed work cycles with the sponsor.'],
    measure: 'A, I, G · Customer-approved live use, repeat adoption with verified savings and a recorded observation window.',
    why: 'A staged release proves readiness. Live work cycles show whether the customer changes how they work.',
    days: [[42,90],[57,90],null],
  },
  {
    id: 'impact', priority: 'P0', name: 'Impact assessment and deployment playbook',
    actions: ['Capture manual baseline and critical deployment steps from the first install.', 'After approval, measure real workflow cycles. Ask a second operator to repeat setup and recovery.', 'Review adoption, impact and support effort with the sponsor.'],
    measure: 'A, I, G, R · Cohort results with observation window, approval evidence and a repeatability score with operator hours.',
    why: 'The day-90 decision needs proof of customer value and a credible way to deliver it again.',
    days: [[1,90],[1,90],[1,90]],
  },
  {
    id: 'authoring', priority: 'P1', name: 'Gateway · Rule templates and preview',
    actions: ['Prototype a template for one proven customer rule. Include owner, scope and effective date.', 'Replay proposed changes against historical cases while preserving original decisions.'],
    measure: 'G, R · A reviewer configures the agreed rule and verifies the preview without engineering help.',
    why: 'A repeatable template reduces implementation effort when policy authoring is a bottleneck.',
    days: [[64,84],null,null],
  },
  {
    id: 'dashboard', priority: 'P2', name: 'Dashboard and Sovereignty Score',
    actions: ['Link pilot-relevant cards to evidence.', 'Explain score changes and keep units and time windows visible.'],
    measure: 'G · A reviewer can reconstruct a sample score change from its observations and weights.',
    why: 'A score earns confidence when users can see why it moved and which control to investigate.',
    days: [[71,90],null,null],
  },
  {
    id: 'discovery', priority: 'P2', name: 'Triage, graph exploration and connector demand',
    actions: ['Validate demand for event filters, pause and rule ownership. Measure event latency separately from index freshness.', 'Test free-form graph questions with entity confirmation and actionable blockers.', 'Check Jira or monday.com coverage against a named customer need.'],
    measure: 'A, I, R · One real job, a known point of friction and evidence that a proposed change could remove it.',
    why: 'Customer demand and observed workflow friction should determine which capability earns the next build slot.',
    days: [[71,90],null,null],
  },
  {
    id: 'twin', priority: 'P2', name: 'Project Twin · War-gaming research',
    actions: ['Test forward simulation and inverse planning in one domain.', 'Use held-out scenarios and independently check whether proposed changes satisfy constraints.'],
    measure: 'Research · Compare performance on tuned and unseen cases and record infeasible recommendations.',
    why: 'The two modes need distinct evaluation before either earns a build commitment.',
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

function renderGantt() {
  const index = scenarioOrder.indexOf(state.scenario);
  const matching = features.filter((feature) => state.filter === 'all' || feature.priority === state.filter);
  const scheduled = matching.filter((feature) => feature.days[index]);
  const deferred = matching.filter((feature) => !feature.days[index]);
  const ticks = periodEnds.map((end, i) => `<span>Day ${i ? periodEnds[i - 1] + 1 : 1}–${end}</span>`).join('');
  const rows = scheduled.map((feature) => {
    const [start, end] = feature.days[index];
    const dateLabel = `Days ${start}–${end}`;
    return `<div class="chart-row">
      <a class="chart-name" href="#feature-${feature.id}"><span class="tag ${priorityClass(feature.priority)}">${feature.priority}</span> <span>${feature.name}</span></a>
      <div class="track" style="--start:${start};--span:${end - start + 1}">
        <a class="bar ${priorityClass(feature.priority)}" href="#feature-${feature.id}" aria-label="${feature.name}, ${dateLabel}" title="${dateLabel}">
          <span>${start}–${end}</span>
        </a>
      </div></div>`;
  }).join('');
  byId('gantt').innerHTML = `<div class="chart-row chart-header"><strong>Priority and feature</strong><div class="ticks">${ticks}</div></div>${rows || '<p class="empty">No scheduled work at this priority in this scenario.</p>'}`;
  byId('deferred').hidden = deferred.length === 0;
  byId('deferred').textContent = deferred.length ? `Outside this schedule: ${deferred.map((feature) => feature.name).join(' · ')}.` : '';
}

function renderScenario() {
  const scenario = scenarios[state.scenario];
  byId('scenario-summary').innerHTML = `<div class="scenario-grid">
    <article><p class="kicker">TRIGGER</p><p>${scenario.trigger}</p></article>
    <article><p class="kicker">${scenario.launch.toUpperCase()}</p><p>${scenario.action}</p></article>
    <article><p class="kicker">DAY-90 EVIDENCE</p><p>${scenario.outcome}</p></article>
  </div>`;
  byId('chart-scenario').textContent = scenario.name;
  byId('ready-day').textContent = scenario.launch.toUpperCase();
  renderGantt();
}

byId('scenario-control').addEventListener('change', (event) => {
  state.scenario = event.target.value;
  renderScenario();
});

byId('priority-filter').addEventListener('change', (event) => {
  state.filter = event.target.value;
  renderGantt();
});

renderFeatures();
renderScenario();

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
