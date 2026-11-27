import test from 'node:test';
import assert from 'node:assert/strict';
import {PRESETS,createBlueprint,createChallenges,createRemediation,evaluateChallenge,exportJournal} from '../studio-engine.mjs';

test('unavailable enterprise compute teaches the authored capacity lesson and exports the original miss',()=>{
 const input=PRESETS.banking,b=createBlueprint(input),qs=createChallenges(input);
 assert.equal(b.status,'BLOCKED');
 const q=qs.find(q=>q.id==='operations'),r=evaluateChallenge(q,0);
 assert.equal(r.ok,false);
 assert.equal(r.lesson.url,'../modules/09-gpus-compute-networking-platform-engineering.html');
 const follow=createRemediation(q,input);
 const journal=exportJournal(b,qs,{operations:0},'',{[follow.id]:follow.correct});
 assert.match(journal,/09-gpus-compute-networking-platform-engineering/);
 assert.match(journal,/Needs review/);
 assert.match(journal,/Follow-up result: Correct reasoning/);
});

test('capacity evidence duties never clear physical and air-gap conflicts',()=>{
 for(const input of [PRESETS.factory,{...PRESETS.onsite,capacity:'public_cloud'}]){
  const b=createBlueprint(input);
  assert.ok(b.lessons.some(l=>l.url.includes('/09-gpus-')));
  assert.ok(b.gates.some(g=>/capacity dropdown is not a benchmark/.test(g)));
  assert.match(b.flows.find(f=>f.id==='inference').test,/p95 and errors.*replica loss/);
  assert.ok(b.flows.every(f=>/physical premises/.test(f.destination)));
  if(input.location==='airgap')assert.ok(b.flows.every(f=>f.network==='NONE'));
  if(input.capacity==='public_cloud')assert.equal(b.status,'BLOCKED');
 }
});
