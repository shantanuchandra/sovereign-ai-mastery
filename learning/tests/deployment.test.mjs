import test from 'node:test';
import assert from 'node:assert/strict';
import {PRESETS,createBlueprint,createChallenges,evaluateChallenge,exportJournal} from '../studio-engine.mjs';

test('deployment lesson and recovery evidence duties are retained in generated and exported plans',()=>{
 const b=createBlueprint(PRESETS.factory),qs=createChallenges(PRESETS.factory);
 assert.ok(b.lessons.some(x=>x.url.endsWith('/10-sovereign-cloud-deployment-patterns.html')));
 assert.ok(b.gates.some(x=>/RTO.*RPO.*IaC state/.test(x)));
 const md=exportJournal(b,qs,{},'');
 assert.match(md,/10-sovereign-cloud-deployment-patterns/);
 assert.match(b.flows.find(x=>x.id==='backup').test,/recovery point.*restoration/);
});

test('country changes never clear unchanged physical air-gap and operator conflicts',()=>{
 const input={...PRESETS.factory,capacity:'public_cloud'},b=createBlueprint(input);
 assert.equal(b.status,'BLOCKED');
 assert.ok(b.flows.every(f=>f.evidence==='BLOCKED'));
 const q=createChallenges(input).find(q=>q.id==='operations');
 assert.equal(q.correct,1);
 assert.equal(evaluateChallenge(q,0).ok,false);
});

test('operating-control misconception reaches the authored deployment lesson without changing answer identity',()=>{
 const q=createChallenges(PRESETS.onsite).find(q=>q.id==='operations');
 assert.equal(q.correct,2);
 const result=evaluateChallenge(q,0);
 assert.equal(result.ok,false);
 assert.equal(result.lesson.url,'../modules/10-sovereign-cloud-deployment-patterns.html');
});
