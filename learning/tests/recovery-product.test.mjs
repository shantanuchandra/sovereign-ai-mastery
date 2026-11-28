import test from 'node:test';
import assert from 'node:assert/strict';
import {VERSION,PRESETS,createBlueprint,createChallenges,createRemediation,evaluateChallenge,exportJournal} from '../studio-engine.mjs';

const additions=['recovery-evidence','discovery-evidence','acceptance-trace'];
test('three new decisions append while seven saved first attempts keep their identity and answer meaning',()=>{
  const qs=createChallenges(PRESETS.factory);
  assert.equal(VERSION,'1.2.0');
  assert.deepEqual(qs.map(q=>q.id),['location','operations','portability','evidence','rag-permissions','optimization-evidence','agent-approval',...additions]);
  assert.deepEqual(qs.slice(0,7).map(q=>q.correct),[1,2,0,1,1,2,1]);
  assert.deepEqual(qs.slice(7).map(q=>q.correct),[2,1,0]);
});
test('new missed concepts provide a distinct transfer question, actionable feedback and the right lesson',()=>{
  const qs=createChallenges(PRESETS.onsite);
  for(const [i,id] of additions.entries()){
    const q=qs.find(q=>q.id===id),miss=evaluateChallenge(q,(q.correct+1)%3),follow=createRemediation(q,PRESETS.onsite);
    assert.equal(miss.ok,false);assert.ok(miss.root&&miss.action);
    assert.match(miss.lesson.url,new RegExp('/'+(18+i)+'-'));
    assert.notEqual(follow.question,q.question);
    assert.equal(follow.id,'remediation-'+id);
    assert.equal(evaluateChallenge(follow,follow.correct).ok,true);
  }
});
test('recovery, discovery and requirements reasoning retains bounded evidence distinctions',()=>{
  const qs=createChallenges(PRESETS.factory);
  assert.match(qs.find(q=>q.id===additions[0]).options[2].text,/current retirement.*indexes and caches/);
  assert.match(qs.find(q=>q.id===additions[1]).options[1].text,/hypothesis.*block.*buyer value/);
  assert.match(qs.find(q=>q.id===additions[2]).options[0].text,/exact build.*negative test/);
});
test('new lessons, original misses and follow-up outcomes remain in the actual journal format',()=>{
  const b=createBlueprint(PRESETS.factory),qs=createChallenges(PRESETS.factory),answers={},followups={};
  for(const id of additions){const q=qs.find(q=>q.id===id);answers[id]=(q.correct+1)%3;const f=createRemediation(q,b.input);followups[f.id]=f.correct;}
  const journal=exportJournal(b,qs,answers,'Evidence remains scoped.',followups);
  for(const n of [18,19,20])assert.match(journal,new RegExp('/'+n+'-'));
  assert.equal((journal.match(/- Result: Needs review/g)||[]).length,3);
  assert.equal((journal.match(/Follow-up result: Correct reasoning/g)||[]).length,3);
});
test('value scores and correct practice cannot lift a known physical conflict',()=>{
  for(const input of Object.values(PRESETS)){
    const b=createBlueprint({...input,location:'airgap',connectivity:'internet',capacity:'public_cloud'});
    assert.equal(b.status,'BLOCKED');
    assert.ok(b.flows.every(f=>f.evidence==='BLOCKED'));
    for(const q of createChallenges(b.input))assert.equal(evaluateChallenge(q,q.correct).ok,true);
    for(const n of [18,19,20])assert.ok(b.lessons.some(l=>l.url.includes('/'+n+'-')));
  }
});
