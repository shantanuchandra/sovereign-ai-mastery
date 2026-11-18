import {DEFAULTS, LABELS, PRESETS, VERSION, normalize, createBlueprint, createChallenges, evaluateChallenge, compareBlueprints, exportJournal} from './studio-engine.mjs';

const STORAGE='sovereign-ai-learning-studio-v1';
const OLD='sovereign-ai-studio-v1';
const byId=id=>document.getElementById(id);
const escape=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;','"':'&quot;'}[c]));
const form=byId('assumption-form');
let answers={},reflection='',current,questions=[],currentKey='',lastCompare;

function readSaved(){try{return JSON.parse(localStorage.getItem(STORAGE)||'null')}catch{return null}}
function safeSave(){try{localStorage.setItem(STORAGE,JSON.stringify({inputs:current.input,answers,reflection,signature:currentKey}))}catch{/* Privacy settings may disable storage. */}}
function applyInputs(values){const v=normalize(values);for(const [key,value] of Object.entries(v))if(form.elements.namedItem(key))form.elements.namedItem(key).value=value;return v}
function getInputs(){return normalize(Object.fromEntries(new FormData(form).entries()))}
function signature(v){return Object.entries(v).map(([k,val])=>`${k}:${val}`).join('|')}
function list(id,arr,ordered=false){const el=byId(id);el.replaceChildren();arr.forEach(s=>{const child=document.createElement('li');child.textContent=s;el.appendChild(child)})}
function renderArchitecture(){
  byId('solution-title').textContent=current.title;
  byId('solution-why').textContent=current.why;
  byId('solution-status').textContent=current.status;
  byId('solution-status').classList.toggle('blocked',current.status==='BLOCKED');
  byId('margin-pattern').textContent=current.title;
  byId('margin-gate').textContent=current.gates[0]||'All major claims still require actual tests and reviewer acceptance.';
  list('implementation-steps',current.steps,true);
  list('approval-gates',current.gates);
  byId('architecture-diagram').innerHTML=current.architectures.map((layer,i)=>`${i?'<div class="diagram-arrow" aria-hidden="true">↓</div>':''}<div class="diagram-node"><div class="node-title">${escape(layer.name)}</div><div class="node-detail">${escape(layer.detail)}</div><div class="node-owner">Accountable: ${escape(layer.owner)}</div></div>`).join('');
  byId('controls-table').innerHTML=current.controls.map(c=>`<tr><td><strong>${escape(c.dimension)}</strong><small>${escape(c.id)}</small></td><td>${escape(c.claim)}<small>Implementation: ${escape(c.implementation)}</small></td><td>${escape(c.test)}</td><td><code>${escape(c.evidence)}</code></td></tr>`).join('');
  byId('reasoning-trace').innerHTML=current.trace.map(t=>`<li><strong>${escape(t.label)}.</strong> ${escape(t.consequence)}</li>`).join('');
  byId('lesson-links').innerHTML=current.lessons.map(l=>`<a href="${escape(l.url)}">${escape(l.label)} ↗</a>`).join('');
}
function updateCounterOptions(){
  const key=byId('counter-key').value,v=current.input;
  const select=byId('counter-value'),old=select.value;
  select.replaceChildren();
  for(const [value,label] of Object.entries(LABELS[key])){
    const option=document.createElement('option');option.value=value;option.textContent=label+(value===v[key]?' (current)':'');select.appendChild(option);
  }
  if(old&&old in LABELS[key]&&old!==v[key])select.value=old;
  else select.value=Object.keys(LABELS[key]).find(x=>x!==v[key])||v[key];
}
function renderComparison(){
  const key=byId('counter-key').value;
  const v={...current.input,[key]:byId('counter-value').value};
  lastCompare=compareBlueprints(current.input,v);
  byId('compare-original').textContent=lastCompare.previous.title;
  byId('compare-next').textContent=lastCompare.current.title;
  byId('compare-original-why').textContent=lastCompare.previous.why;
  byId('compare-next-why').textContent=lastCompare.current.why;
  const changed=lastCompare.changed.map(k=>LABELS[k][current.input[k]]+' → '+LABELS[k][v[k]]);
  const summary=!changed.length?'No constraint changed. Choose another value to compare.':lastCompare.patternChanged?'The pattern changed. Identify which input removed or introduced a hard constraint.':'The pattern remained the same, but assurance gates, control duties or risk exposure can still change.';
  byId('counter-explanation').textContent=(changed.length?'Changed: '+changed.join('; ')+'. ':'')+summary+(lastCompare.gatesAdded.length?' New gate: '+lastCompare.gatesAdded.join('; '):'');
  byId('apply-counter').disabled=!changed.length;
}
function renderChallenges(){
  const region=byId('challenge-list');region.replaceChildren();
  questions.forEach((q,i)=>{
    const picked=answers[q.id];const has=picked!==undefined;
    const card=document.createElement('article');card.className='challenge';card.dataset.qid=q.id;
    card.innerHTML=`<div class="challenge-top">QUESTION ${String(i+1).padStart(2,'0')} / ${escape(q.dimension.toUpperCase())}</div><h3>${escape(q.question)}</h3><div class="answers" role="group" aria-label="Answers for question ${i+1}">${q.options.map((o,j)=>`<button type="button" class="answer ${picked===j?'selected':''}" data-choice="${j}" ${has?'disabled':''}><span>${'ABC'[j]}.</span>${escape(o.text)}</button>`).join('')}</div><div class="feedback-wrap" aria-live="polite"></div>`;
    if(has){const e=evaluateChallenge(q,picked);const fb=card.querySelector('.feedback-wrap');fb.innerHTML=`<div class="feedback ${e.ok?'correct':''}"><strong>${e.ok?'Reasoning supported':'Revisit the assumption'}</strong>${escape(e.feedback)}<div style="margin-top:8px"><strong>Root cause to examine</strong>${escape(e.root)}</div><div style="margin-top:8px"><strong>Next corrective test</strong>${escape(e.action)} <a href="${escape(e.lesson.url)}">Study ${escape(e.lesson.label)}</a></div></div>`;}
    region.appendChild(card);
  });
  const count=Object.keys(answers).filter(id=>questions.some(q=>q.id===id)).length;
  const correct=questions.filter(q=>answers[q.id]!==undefined&&evaluateChallenge(q,answers[q.id]).ok).length;
  byId('tutor-progress').textContent=`${count} of ${questions.length} answered`;
  byId('tutor-context').textContent=count?`${correct} decisions aligned with the course reasoning, out of ${count} attempted`:'Generated from your current constraints';
  const wrong=questions.filter(q=>answers[q.id]!==undefined&&!evaluateChallenge(q,answers[q.id]).ok);
  const summary=byId('tutor-summary');
  if(!count){summary.textContent='Begin with the scenario rather than memorizing labels. Each answer shows its reasoning only after you choose.';return;}
  if(wrong.length){summary.innerHTML=`<strong>Focus for revision:</strong> ${escape(wrong.map(q=>q.dimension).join(', '))}. Read the feedback and identify one concrete validation action. This is practice feedback, not a proficiency certification.`;}
  else if(count===questions.length){summary.textContent='All four decisions align with the course rationale. Now defend a counterfactual change in writing. Correct multiple-choice answers alone do not establish mastery.';}
  else summary.textContent='Good. Continue to the remaining questions, then explain the architectural choice in your own words.';
}
function build(){
  current=createBlueprint(getInputs());
  const sig=signature(current.input);
  if(sig!==currentKey){answers={};currentKey=sig;}
  questions=createChallenges(current.input);
  renderArchitecture();updateCounterOptions();renderComparison();renderChallenges();safeSave();
  document.querySelectorAll('[data-preset]').forEach(b=>b.classList.toggle('selected',signature(PRESETS[b.dataset.preset])===sig));
}
const saved=readSaved();
let inputs=saved?.inputs;
if(!inputs){try{inputs=JSON.parse(localStorage.getItem(OLD)||'null')}catch{inputs=null}}
applyInputs(inputs||DEFAULTS);
current=createBlueprint(getInputs());currentKey=signature(current.input);
if(saved?.signature===currentKey&&saved.answers&&typeof saved.answers==='object'){
  const proposed=createChallenges(current.input);
  for(const q of proposed)if(Number.isInteger(saved.answers[q.id])&&saved.answers[q.id]>=0&&saved.answers[q.id]<q.options.length)answers[q.id]=saved.answers[q.id];
}
reflection=typeof saved?.reflection==='string'?saved.reflection.slice(0,2400):'';
byId('reflection').value=reflection;
build();

form.addEventListener('change',build);
document.querySelectorAll('[data-preset]').forEach(b=>b.addEventListener('click',()=>{applyInputs(PRESETS[b.dataset.preset]);build();}));
byId('clear-all').addEventListener('click',()=>{applyInputs(DEFAULTS);answers={};build();});
byId('counter-key').addEventListener('change',()=>{updateCounterOptions();renderComparison();});
byId('counter-value').addEventListener('change',renderComparison);
byId('apply-counter').addEventListener('click',()=>{const key=byId('counter-key').value;form.elements.namedItem(key).value=byId('counter-value').value;build();byId('architecture').scrollIntoView({block:'start',behavior:'smooth'});});
byId('challenge-list').addEventListener('click',e=>{
  const b=e.target.closest('button[data-choice]');if(!b)return;
  const card=b.closest('[data-qid]');const q=questions.find(x=>x.id===card?.dataset.qid);if(!q||answers[q.id]!==undefined)return;
  answers[q.id]=Number(b.dataset.choice);renderChallenges();safeSave();
});
byId('restart-challenges').addEventListener('click',()=>{answers={};renderChallenges();safeSave();});
byId('reflection').addEventListener('input',e=>{reflection=e.target.value;safeSave();});
const download=(content,name,mime)=>{
  const blob=new Blob([content],{type:mime});const url=URL.createObjectURL(blob);const link=document.createElement('a');link.href=url;link.download=name;document.body.append(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(url),3000);
};
byId('download-md').addEventListener('click',()=>download(exportJournal(current,questions,answers,reflection),'sovereignty-learning-journal.md','text/markdown;charset=utf-8'));
byId('download-json').addEventListener('click',()=>download(JSON.stringify({version:VERSION,notice:'Course-authored provisional architecture. Not verified compliance.',blueprint:current,review:{challenges:questions.map(q=>({question:q.question,selectedIndex:answers[q.id]??null,feedback:answers[q.id]===undefined?null:evaluateChallenge(q,answers[q.id])})),reflection}},null,2),'sovereignty-architecture.json','application/json'));
byId('toc-toggle').addEventListener('click',()=>{const rail=document.querySelector('.rail');const opened=rail.classList.toggle('show');byId('toc-toggle').setAttribute('aria-expanded',String(opened));});
document.querySelectorAll('.rail-nav a').forEach(a=>a.addEventListener('click',()=>{document.querySelector('.rail').classList.remove('show');byId('toc-toggle').setAttribute('aria-expanded','false');}));