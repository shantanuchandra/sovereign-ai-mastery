/** Self-reported learner progress; no network, approval or mastery inference. */
const KEY = 'sovereign-study-plan-v1';
const checks = [...document.querySelectorAll('input[data-hour]')];
const ids = new Set(checks.map(c => c.dataset.hour));
const status = document.getElementById('plan-status');
const counter = document.getElementById('plan-progress');
let done = new Set();
try {
  const saved = JSON.parse(localStorage.getItem(KEY) || '[]');
  if (Array.isArray(saved)) done = new Set(saved.filter(x => ids.has(x)));
} catch { status.textContent = 'Saved progress is unavailable. You can still study and export this session.'; }
function update() {
  counter.textContent = `${done.size} of ${checks.length} study hours marked complete`;
  for (const c of checks) c.checked = done.has(c.dataset.hour);
}
for (const c of checks) c.addEventListener('change', () => {
  c.checked ? done.add(c.dataset.hour) : done.delete(c.dataset.hour);
  try { localStorage.setItem(KEY, JSON.stringify([...done])); }
  catch { status.textContent = 'Progress could not be saved. Export your record before closing this page.'; }
  update();
});
const filter = document.getElementById('plan-module');
function select(value) {
  filter.value = value;
  for (const section of document.querySelectorAll('[data-module]')) {
    section.hidden = value !== 'all' && section.dataset.module !== value;
  }
}
filter.addEventListener('change', () => {
  select(filter.value);
  history.replaceState(null, '', filter.value === 'all' ? '#study-plan' : `#module-${filter.value}`);
});
function fromHash() {
  const match = /^#module-(\d{2})$/.exec(location.hash);
  select(match && document.querySelector(`[data-module="${match[1]}"]`) ? match[1] : 'all');
}
window.addEventListener('hashchange', fromHash);
fromHash();
document.getElementById('export-plan').addEventListener('click', () => {
  const lines = ['# Sovereign AI Mastery — study record', '',
    'Self-reported progress only. No competency certification or publication approval.', '',
    `Completed: ${done.size} / ${checks.length} study hours`, ''];
  for (const section of document.querySelectorAll('[data-module]')) {
    lines.push(`## ${section.querySelector('h2').textContent}`, '');
    for (const c of section.querySelectorAll('input[data-hour]')) {
      lines.push(`- [${done.has(c.dataset.hour) ? 'x' : ' '}] ${c.closest('li').querySelector('label').textContent.trim()}`);
    }
    lines.push('');
  }
  const url = URL.createObjectURL(new Blob([lines.join('\n')], {type:'text/markdown'}));
  const link = document.createElement('a'); link.href=url; link.download='sovereign-ai-study-record.md';
  document.body.appendChild(link); link.click(); link.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000);
});
update();
