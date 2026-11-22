import {DEFAULTS, LABELS, PRESETS, PRESET_LABELS, VERSION, normalize, createBlueprint, createChallenges, createRemediation, evaluateChallenge, compareBlueprints, exportJournal} from './studio-engine.mjs';

const STORAGE='sovereign-ai-learning-studio-v1';
const OLD='sovereign-ai-studio-v1';
const byId=id=>document.getElementById(id);
const escape=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const form=byId('assumption-form');
let answers={},remediationAnswers={},reflection='',current,questions=[],currentKey='',lastCompare;

function readSaved(){try{return JSON.parse(localStorage.getItem(STORAGE)||'null')}catch{return null}}
function safeSave(){try{localStorage.setItem(STORAGE,JSON.stringify({inputs:current.input,answers,remediationAnswers,reflection,signature:currentKey,quizVersion:VERSION}))}catch{/* Privacy settings may disable storage. */}}
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
  const boundary=byId('boundary-warning');
  const premise=['premises','airgap','approved_sites'].includes(current.input.location);
  boundary.hidden=!premise;
  if(premise){
    const phrase=current.input.location==='airgap'?'Air-gapped: no network connections and no external service endpoints.':current.input.location==='premises'?'Single-premises-only: no prompts, vector embeddings, logs, backups or diagnostics may leave the building.':'Approved-sites-only: treat every permitted facility and link as an explicit boundary.';
    boundary.textContent=phrase+' The generated design is conditional, not a certification.';
  }
  list('implementation-steps',current.steps,true);
  list('approval-gates',current.gates);
  byId('architecture-diagram').innerHTML=current.architectures.map((layer,i)=>`${i?'<div class="diagram-arrow" aria-hidden="true">↓</div>':''}<div class="diagram-node"><div class="node-title">${escape(layer.name)}</div><div class="node-detail">${escape(layer.detail)}</div><div class="node-owner">Accountable: ${escape(layer.owner)}</div></div>`).join('');
  byId('controls-table').innerHTML=current.controls.map(c=>`<tr><td><strong>${escape(c.dimension)}</strong><small>${escape(c.id)}</small></td><td>${escape(c.claim)}<small>Implementation: ${escape(c.implementation)}</small></td><td>${escape(c.test)}</td><td><code>${escape(c.evidence)}</code></td></tr>`).join('');
  byId('flow-register').innerHTML=current.flows.map(f=>`<article class="flow-card" data-flow="${f.id}"><div class="flow-heading"><h4>${escape(f.name)}</h4><code>${f.evidence}</code></div><p>${escape(f.artifacts)}</p><dl><dt>Required destination</dt><dd>${escape(f.destination)}</dd><dt>Network constraint</dt><dd>${escape({NONE:'No network connections',LOCAL_ONLY:'Local network within premises',APPROVED_DESTINATIONS:'Only explicitly permitted destinations'}[f.network])}</dd><dt>Accountable owner</dt><dd>${escape(f.owner)}</dd><dt>Acceptance test</dt><dd>${escape(f.test)}</dd></dl></article>`).join('');
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
  function appendQuestion(q,label,follow=false){
    const picked=(follow?remediationAnswers:answers)[q.id],result=evaluateChallenge(q,picked);
    const card=document.createElement('article');card.className='challenge'+(follow?' remediation':'');card.dataset.qid=q.id;
    card.innerHTML=`<div class="challenge-top">${escape(label)} / ${escape(q.dimension.toUpperCase())}</div><h3 id="question-${q.id}">${escape(q.question)}</h3>${follow?'<p class="practice-note">Try a different situation for the concept you missed. Your first answer stays in the learning record.</p>':''}<div class="answers" role="group" aria-labelledby="question-${q.id}">${q.options.map((o,j)=>`<button type="button" class="answer ${picked===j?'selected':''}" data-choice="${j}" ${result?'disabled':''}><span>${'ABC'[j]}.</span>${escape(o.text)}</button>`).join('')}</div><div class="feedback-wrap" aria-live="polite" tabindex="-1"></div>`;
    if(result){const fb=card.querySelector('.feedback-wrap');fb.innerHTML=`<div class="feedback ${result.ok?'correct':''}"><strong>${result.ok?'Reasoning supported':'Revisit the assumption'}</strong>${escape(result.feedback)}${result.ok?'':`<p><strong>Root cause to examine</strong>${escape(result.root)}</p>`}<p><strong>Next corrective test</strong>${escape(result.action)} <a href="${escape(result.lesson.url)}">Study ${escape(result.lesson.label)}</a></p></div>`;}
    region.appendChild(card);
  }
  questions.forEach((q,i)=>{
    appendQuestion(q,`QUESTION ${String(i+1).padStart(2,'0')}`);
    const first=evaluateChallenge(q,answers[q.id]);
    if(first&&!first.ok)appendQuestion(createRemediation(q,current.input),'FOLLOW-UP PRACTICE',true);
  });
  const count=Object.keys(answers).filter(id=>questions.some(q=>q.id===id)).length;
  const correct=questions.filter(q=>answers[q.id]!==undefined&&evaluateChallenge(q,answers[q.id]).ok).length;
  byId('tutor-progress').textContent=`${count} of ${questions.length} answered`;
  byId('tutor-context').textContent=count?`${correct} decisions aligned with the course reasoning, out of ${count} attempted`:'Generated from your current constraints';
  const wrong=questions.filter(q=>answers[q.id]!==undefined&&!evaluateChallenge(q,answers[q.id]).ok);
  const summary=byId('tutor-summary');
  if(!count){summary.textContent='Begin with the scenario rather than memorizing labels. Each answer shows its reasoning only after you choose.';return;}
  if(wrong.length){
    const resolved=wrong.filter(q=>{const follow=createRemediation(q,current.input);return evaluateChallenge(follow,remediationAnswers[follow.id])?.ok}).length;
    summary.innerHTML=`<strong>First-attempt revision topics:</strong> ${escape(wrong.map(q=>q.dimension).join(', '))}. ${resolved} of ${wrong.length} follow-up decisions now align with the rationale. Your first attempts are retained. Read the feedback and identify one concrete validation action. This is practice feedback, not a proficiency certification.`;
  }
  else if(count===questions.length){summary.textContent='All four decisions align with the course rationale. Now defend a counterfactual change in writing. Correct multiple-choice answers alone do not establish mastery.';}
  else summary.textContent='Good. Continue to the remaining questions, then explain the architectural choice in your own words.';
}
function build(){
  current=createBlueprint(getInputs());
  const sig=signature(current.input);
  if(sig!==currentKey){answers={};remediationAnswers={};currentKey=sig;}
  questions=createChallenges(current.input);
  renderArchitecture();updateCounterOptions();renderComparison();renderChallenges();safeSave();
  document.querySelectorAll('[data-preset]').forEach(b=>b.classList.toggle('selected',signature(PRESETS[b.dataset.preset])===sig));
}
// Dropdowns are populated from the same taxonomy as the decision engine.
// This avoids stale HTML options when the vocabulary expands.
function populateDropdowns(){
  for(const [key,values] of Object.entries(LABELS)){
    const el=form.elements.namedItem(key);
    if(!el)throw new Error(`Missing dropdown for ${key}`);
    el.replaceChildren();
    for(const [value,label] of Object.entries(values)){
      const option=document.createElement('option');option.value=value;option.textContent=label;el.append(option);
    }
  }
  const counter=byId('counter-key');counter.replaceChildren();
  const titles={workload:'Workload / use case',data:'Data classification',location:'Physical and geographic boundary',connectivity:'Network and egress',operator:'Operating authority',portability:'Technology portability',capacity:'Infrastructure and compute',evidence:'Available evidence',jurisdiction:'Jurisdiction',stage:'Release stage'};
  for(const key of Object.keys(LABELS)){const option=document.createElement('option');option.value=key;option.textContent=titles[key];counter.append(option);}
  counter.value='location';
  const library=byId('scenario-library');library.replaceChildren();
  for(const [key,label] of Object.entries(PRESET_LABELS)){
    const option=document.createElement('option');option.value=key;option.textContent=label;library.append(option);
  }
  library.value='onsite';
}
populateDropdowns();
const saved=readSaved();
let inputs=saved?.inputs;
if(!inputs){try{inputs=JSON.parse(localStorage.getItem(OLD)||'null')}catch{inputs=null}}
applyInputs(inputs||DEFAULTS);
current=createBlueprint(getInputs());currentKey=signature(current.input);
if(saved?.quizVersion===VERSION&&saved?.signature===currentKey&&saved.answers&&typeof saved.answers==='object'){
  const proposed=createChallenges(current.input);
  for(const q of proposed){
    const first=evaluateChallenge(q,saved.answers[q.id]);
    if(!first)continue;
    answers[q.id]=saved.answers[q.id];
    if(!first.ok){const follow=createRemediation(q,current.input),picked=saved.remediationAnswers?.[follow.id];if(evaluateChallenge(follow,picked))remediationAnswers[follow.id]=picked;}
  }
}
reflection=typeof saved?.reflection==='string'?saved.reflection.slice(0,2400):'';
byId('reflection').value=reflection;
build();

form.addEventListener('change',build);
document.querySelectorAll('[data-preset]').forEach(b=>b.addEventListener('click',()=>{applyInputs(PRESETS[b.dataset.preset]);build();}));
byId('apply-scenario').addEventListener('click',()=>{const key=byId('scenario-library').value;if(!PRESETS[key])return;applyInputs(PRESETS[key]);build();byId('assumptions').scrollIntoView({block:'start',behavior:'smooth'});});
byId('clear-all').addEventListener('click',()=>{applyInputs(DEFAULTS);answers={};remediationAnswers={};build();});
byId('counter-key').addEventListener('change',()=>{updateCounterOptions();renderComparison();});
byId('counter-value').addEventListener('change',renderComparison);
byId('apply-counter').addEventListener('click',()=>{const key=byId('counter-key').value;form.elements.namedItem(key).value=byId('counter-value').value;build();byId('architecture').scrollIntoView({block:'start',behavior:'smooth'});});
byId('challenge-list').addEventListener('click',e=>{
  const b=e.target.closest('button[data-choice]');if(!b)return;
  const card=b.closest('[data-qid]'),follow=card.classList.contains('remediation');
  const q=follow?questions.map(x=>createRemediation(x,current.input)).find(x=>x.id===card.dataset.qid):questions.find(x=>x.id===card.dataset.qid);
  const target=follow?remediationAnswers:answers;if(!q||target[q.id]!==undefined)return;
  target[q.id]=Number(b.dataset.choice);renderChallenges();safeSave();
  byId('challenge-list').querySelector(`[data-qid="${q.id}"] .feedback-wrap`).focus({preventScroll:true});
});
byId('restart-challenges').addEventListener('click',()=>{answers={};remediationAnswers={};renderChallenges();safeSave();});
byId('reflection').addEventListener('input',e=>{reflection=e.target.value;safeSave();});
const download=(content,name,mime)=>{
  const blob=new Blob([content],{type:mime});const url=URL.createObjectURL(blob);const link=document.createElement('a');link.href=url;link.download=name;document.body.append(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(url),3000);
};
byId('download-md').addEventListener('click',()=>download(exportJournal(current,questions,answers,reflection,remediationAnswers),'sovereignty-learning-journal.md','text/markdown;charset=utf-8'));
byId('download-json').addEventListener('click',()=>{
  const challenges=questions.map(q=>{
    const feedback=evaluateChallenge(q,answers[q.id]),follow=feedback&&!feedback.ok?createRemediation(q,current.input):null;
    return {question:q.question,selectedIndex:answers[q.id]??null,feedback,followUp:follow?{question:follow.question,selectedIndex:remediationAnswers[follow.id]??null,feedback:evaluateChallenge(follow,remediationAnswers[follow.id])}:null};
  });
  download(JSON.stringify({version:VERSION,notice:'Course-authored provisional architecture. Not verified compliance.',blueprint:current,review:{challenges,reflection}},null,2),'sovereignty-architecture.json','application/json');
});
function closeContents(){document.querySelector('.rail').classList.remove('show');byId('toc-toggle').setAttribute('aria-expanded','false');byId('toc-toggle').focus();}
byId('toc-toggle').addEventListener('click',()=>{const rail=document.querySelector('.rail');const opened=rail.classList.toggle('show');byId('toc-toggle').setAttribute('aria-expanded',String(opened));if(opened)byId('toc-close').focus();});
byId('toc-close').addEventListener('click',closeContents);
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&document.querySelector('.rail').classList.contains('show'))closeContents();});
document.querySelectorAll('.rail-nav a').forEach(a=>a.addEventListener('click',()=>{document.querySelector('.rail').classList.remove('show');byId('toc-toggle').setAttribute('aria-expanded','false');}));
