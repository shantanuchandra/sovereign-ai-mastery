import test from 'node:test';
import assert from 'node:assert/strict';
import {PRESETS,createBlueprint,createChallenges,evaluateChallenge,createRemediation,exportJournal} from '../studio-engine.mjs';

test('data feedback and retained misconception link to the authored lifecycle lesson',()=>{
 for(const input of [PRESETS.factory,PRESETS.onsite,PRESETS.support]){
  const b=createBlueprint(input),qs=createChallenges(input),q=qs.find(q=>q.id==='location');
  const missed=(q.correct+1)%q.options.length;
  const first=evaluateChallenge(q,missed),follow=createRemediation(q,input);
  assert.equal(first.ok,false);
  assert.equal(first.lesson.url,'../modules/08-data-sovereignty-engineering.html');
  assert.equal(follow.lesson.url,first.lesson.url);
  const md=exportJournal(b,qs,{location:missed},'',{[follow.id]:follow.correct});
  assert.match(md,/08-data-sovereignty-engineering/);
  assert.match(md,/Needs review/);
  assert.match(md,/Follow-up result: Correct reasoning/);
 }
});

test('data lifecycle guidance retains all physical gates in designs and portable journals',()=>{
 for(const input of [PRESETS.factory,{...PRESETS.onsite,capacity:'public_cloud'}]){
  const b=createBlueprint(input);
  const retrieval=b.flows.find(f=>f.id==='retrieval'),backup=b.flows.find(f=>f.id==='backup');
  assert.match(retrieval.test,/verified identity.*expiry before ranking/);
  assert.match(backup.test,/retirement ledger.*chunks and vectors stay excluded/);
  for(const flow of [retrieval,backup]){
   assert.match(flow.destination,/physical premises/);
   if(input.location==='airgap')assert.equal(flow.network,'NONE');
   if(b.status==='BLOCKED')assert.equal(flow.evidence,'BLOCKED');
  }
  assert.match(exportJournal(b,createChallenges(input),{}),/retirement ledger/);
 }
});
