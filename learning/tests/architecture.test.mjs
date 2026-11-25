import test from 'node:test';
import assert from 'node:assert/strict';
import {PRESETS,createBlueprint,createChallenges,evaluateChallenge,exportJournal} from '../studio-engine.mjs';
test('blocked architecture reasoning links to Module 07 and retains its lesson in exports',()=>{
 const input={...PRESETS.onsite,capacity:'laptop'};
 const b=createBlueprint(input);assert.equal(b.status,'BLOCKED');
 const qs=createChallenges(input),q=qs.find(q=>q.id==='operations');
 const r=evaluateChallenge(q,0);assert.equal(r.ok,false);
 assert.match(r.lesson.url,/07-end-to-end/);
 assert.ok(b.lessons.some(l=>l.url===r.lesson.url));
 assert.match(exportJournal(b,qs,{operations:0}),/07-end-to-end/);
});
