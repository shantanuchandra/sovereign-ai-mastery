import test from 'node:test';
import assert from 'node:assert/strict';
import {VERSION,PRESETS,createBlueprint,createChallenges,createRemediation,evaluateChallenge,exportJournal} from '../studio-engine.mjs';

test('new practice appends to the four stable decisions without invalidating saved answers',()=>{
  const qs=createChallenges(PRESETS.factory);
  assert.deepEqual(qs.map(q=>q.id),['location','operations','portability','evidence','rag-permissions','optimization-evidence','agent-approval']);
  assert.deepEqual(qs.slice(0,4).map(q=>q.correct),[1,2,0,1]);
  assert.equal(VERSION,'1.2.0');
});
test('retrieval practice checks revocation before ranking and context assembly',()=>{
  const q=createChallenges(PRESETS.factory).find(q=>q.id==='rag-permissions');
  const miss=evaluateChallenge(q,0);
  assert.equal(miss.ok,false);assert.match(miss.action,/revocation.*cache.*context/i);
  assert.match(miss.lesson.url,/12-sovereign-rag-systems/);
  const follow=createRemediation(q,PRESETS.factory);
  assert.match(follow.question,/cache/i);
  assert.equal(evaluateChallenge(follow,follow.correct).ok,true);
});
test('optimization practice keeps errors, quality and latency populations separate',()=>{
  const q=createChallenges(PRESETS.support).find(q=>q.id==='optimization-evidence');
  assert.match(q.question,/Arabic/);
  assert.match(q.options[q.correct].text,/errors.*quality/i);
  assert.match(evaluateChallenge(q,0).lesson.url,/13-fine-tuning-optimization-evaluation/);
});
test('agent practice binds approval to action and rejects substituted arguments',()=>{
  const q=createChallenges(PRESETS.factory).find(q=>q.id==='agent-approval');
  assert.match(q.options[q.correct].text,/tenant.*arguments.*expiry/);
  const follow=createRemediation(q,PRESETS.factory);
  assert.match(follow.question,/replay/i);
  assert.match(evaluateChallenge(q,0).lesson.url,/14-agents-apis-enterprise-integrations/);
});
test('all three published lessons, gates and practice survive journal export',()=>{
  const b=createBlueprint(PRESETS.factory),qs=createChallenges(PRESETS.factory);
  for(const n of ['12','13','14'])assert.ok(b.lessons.some(l=>l.url.includes('/'+n+'-')));
  assert.ok(b.gates.some(g=>/revocation.*ranking.*context/.test(g)));
  assert.ok(b.gates.some(g=>/optimization.*errors.*Arabic/.test(g)));
  assert.ok(b.gates.some(g=>/approval.*arguments.*expiry.*replay/.test(g)));
  const md=exportJournal(b,qs,{'rag-permissions':0,'optimization-evidence':0,'agent-approval':0},'',{});
  for(const n of ['12','13','14'])assert.match(md,new RegExp('/'+n+'-'));
  assert.equal((md.match(/Follow-up result: Not attempted/g)||[]).length,3);
});
test('passing every practice answer cannot clear a physical conflict',()=>{
  const inputs={...PRESETS.factory,capacity:'public_cloud'},b=createBlueprint(inputs),qs=createChallenges(inputs);
  for(const q of qs)assert.equal(evaluateChallenge(q,q.correct).ok,true);
  assert.equal(b.status,'BLOCKED');assert.ok(b.flows.every(f=>f.evidence==='BLOCKED'));
});
