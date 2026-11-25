import test from 'node:test';
import assert from 'node:assert/strict';
import {PRESETS,createBlueprint,createChallenges,evaluateChallenge,createRemediation,exportJournal} from '../studio-engine.mjs';

test('missed evidence challenge teaches governance and its export retains the lesson',()=>{
  const input={...PRESETS.factory,evidence:'adverse'};
  const blueprint=createBlueprint(input);
  assert.equal(blueprint.status,'BLOCKED');
  const qs=createChallenges(input);
  const q=qs.find(q=>q.id==='evidence');
  const result=evaluateChallenge(q,0);
  assert.equal(result.ok,false);
  assert.equal(result.lesson.url,'../modules/06-governance-responsible-ai-risk.html');
  assert.equal(evaluateChallenge(q,q.correct).ok,true);
  const follow=createRemediation(q,input);
  assert.equal(follow.lesson.url,result.lesson.url);
  assert.ok(blueprint.lessons.some(l=>l.url===result.lesson.url));
  const journal=exportJournal(blueprint,qs,{evidence:0});
  assert.match(typeof journal==='string'?journal:JSON.stringify(journal),/governance/i);
});
