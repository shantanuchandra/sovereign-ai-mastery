import test from 'node:test';
import assert from 'node:assert/strict';
import {VERSION,PRESETS,createBlueprint,createChallenges,exportJournal} from '../studio-engine.mjs';

test('security, custody and operations lessons reach every generated blueprint and journal',()=>{
  for(const input of Object.values(PRESETS)){
    const b=createBlueprint(input),questions=createChallenges(input);
    const journal=exportJournal(b,questions,{},'',{});
    for(const n of ['15','16','17']){
      assert.ok(b.lessons.some(l=>l.url.includes('/'+n+'-')));
      assert.match(journal,new RegExp('/'+n+'-'));
    }
    assert.ok(b.gates.some(g=>/indirect prompt injection.*outside the model.*provenance/.test(g)));
    assert.ok(b.gates.some(g=>/decrypt.*administration.*revocation.*rotation.*attestation/.test(g)));
    assert.ok(b.gates.some(g=>/rollback.*exact model.*attempted.*SLO.*redacted traces/.test(g)));
  }
});

test('new guidance preserves identities, saved-answer version and seven original practice decisions',()=>{
  assert.equal(VERSION,'1.2.0');
  assert.deepEqual(createChallenges(PRESETS.factory).slice(0,7).map(q=>[q.id,q.correct]),[
    ['location',1],['operations',2],['portability',0],['evidence',1],
    ['rag-permissions',1],['optimization-evidence',2],['agent-approval',1]
  ]);
});

test('security guidance cannot grant a pass to prohibited external infrastructure',()=>{
  for(const preset of [PRESETS.factory,PRESETS.onsite]){
    const b=createBlueprint({...preset,capacity:'public_cloud',evidence:'independent'});
    assert.equal(b.status,'BLOCKED');
    assert.ok(b.flows.every(f=>f.evidence==='BLOCKED'));
    assert.ok(b.controls.every(c=>c.evidence!=='PASS'));
    assert.ok(b.gates.some(g=>/Encryption and attestation do not establish physical residency/.test(g)));
  }
});
