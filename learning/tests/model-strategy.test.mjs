import test from 'node:test';
import assert from 'node:assert/strict';
import {PRESETS,createBlueprint,createChallenges,evaluateChallenge,exportJournal} from '../studio-engine.mjs';
test('model selection duties and lesson survive journal export without quiz attempts',()=>{
 const b=createBlueprint(PRESETS.factory);
 assert.ok(b.lessons.some(x=>x.url.endsWith('/11-sovereign-models-model-strategy.html')));
 assert.ok(b.gates.some(x=>/tokenizer.*Arabic.*denominators/.test(x)));
 assert.match(exportJournal(b,createChallenges(PRESETS.factory),{},''),/11-sovereign-models-model-strategy/);
 assert.match(b.controls.find(x=>x.id==='TECH-01').test,/template.*denominators.*restart/);
});
test('portability misconception reaches model strategy with stable identity and correct index',()=>{
 const q=createChallenges({...PRESETS.factory,portability:'essential'}).find(x=>x.id==='portability');
 assert.equal(q.correct,0);
 const miss=evaluateChallenge(q,1);assert.equal(miss.ok,false);
 assert.equal(miss.lesson.url,'../modules/11-sovereign-models-model-strategy.html');
 assert.match(miss.action,/language-slice.*denominators/);
});
test('model advice cannot override physical air-gap conflicts',()=>{
 const b=createBlueprint({...PRESETS.factory,capacity:'public_cloud'});
 assert.equal(b.status,'BLOCKED');assert.ok(b.flows.every(f=>f.evidence==='BLOCKED'));
});
