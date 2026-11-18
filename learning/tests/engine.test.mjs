import test from 'node:test';
import assert from 'node:assert/strict';
import {DEFAULTS,PRESETS,LABELS,normalize,createBlueprint,createChallenges,evaluateChallenge,compareBlueprints,exportJournal} from '../studio-engine.mjs';

test('normalizes unsupported inputs safely',()=>{
  const n=normalize({location:'unknown',stage:'not-a-stage',data:'sensitive'});
  assert.equal(n.location,DEFAULTS.location);assert.equal(n.stage,DEFAULTS.stage);assert.equal(n.data,'sensitive');
});
test('enterprise-only administration without operating compute blocks production',()=>{
  for(const capacity of ['laptop','managed']){
    const b=createBlueprint({...PRESETS.banking,capacity});
    assert.equal(b.pattern,'gated');assert.equal(b.status,'BLOCKED');
    assert.equal(b.controls.find(x=>x.dimension==='Operational').evidence,'CONFLICT');
    assert.ok(b.gates.some(g=>g.includes('Block production')));
  }
});
test('private inference does not imply certification',()=>{
  const b=createBlueprint({...PRESETS.banking,capacity:'gpu'});
  assert.equal(b.pattern,'private');assert.equal(b.status,'PROVISIONAL');
  assert.ok(b.controls.every(x=>x.evidence!=='PASS'));
});
test('managed service only provisional for country-only processing',()=>{
  const b=createBlueprint(PRESETS.assistant);assert.equal(b.pattern,'managed');
  assert.ok(b.gates.some(x=>x.includes('inference, logging')));
});
test('flexible public content can use limited API pilot',()=>{
  const b=createBlueprint({location:'flexible',operator:'provider',data:'public',portability:'low',stage:'pilot'});
  assert.equal(b.pattern,'api');assert.equal(b.status,'PROVISIONAL');
});
test('test record never becomes a passing compliance claim',()=>{
  const b=createBlueprint({...DEFAULTS,evidence:'tested'});
  assert.ok(b.controls.some(x=>x.evidence==='REVIEW_REQUIRED'));
  assert.ok(b.controls.every(x=>x.evidence!=='PASS'));
});
test('all input dimensions appear in trace and ontology controls',()=>{
  const b=createBlueprint(DEFAULTS);
  assert.equal(b.controls.length,4);
  assert.equal(b.trace.length,7);
  for(const key of ['territorial','operational','technological','legal'])assert.ok(b.trace.some(x=>x.key===key));
});
test('challenge set adapts to blockers and portability',()=>{
  const blocked=createChallenges(PRESETS.banking);
  const basic=createChallenges(PRESETS.support);
  assert.equal(blocked.length,4);assert.equal(basic.length,4);
  assert.match(blocked[1].question,/no production compute/);
  assert.match(basic[1].question,/provider hosts/);
  assert.notEqual(blocked[2].question,basic[2].question);
  for(const q of [...blocked,...basic]){
    assert.equal(q.options.length,3);
    assert.ok(q.correct>=0&&q.correct<q.options.length);
    assert.ok(evaluateChallenge(q,q.correct).ok);
    assert.ok(evaluateChallenge(q,(q.correct+1)%3).root);
  }
});
test('counterfactual shows exact changed constraint and architecture',()=>{
  const cmp=compareBlueprints(PRESETS.banking,{...PRESETS.banking,operator:'local'});
  assert.deepEqual(cmp.changed,['operator']);assert.equal(cmp.previous.pattern,'gated');
  assert.equal(cmp.current.pattern,'managed');assert.ok(cmp.patternChanged);
});
test('journal includes evidence caveat and answer rationales',()=>{
  const b=createBlueprint(PRESETS.assistant),qs=createChallenges(PRESETS.assistant);
  const out=exportJournal(b,qs,{[qs[0].id]:0},'I will test telemetry');
  assert.match(out,/learning journal/);assert.match(out,/Needs review/);assert.match(out,/Root cause/);
  assert.match(out,/not a legal opinion/);assert.match(out,/I will test telemetry/);
});
test('cross-product invariant: no declared sovereignty pass',()=>{
  for(const loc of Object.keys(LABELS.location))for(const op of Object.keys(LABELS.operator))for(const capacity of Object.keys(LABELS.capacity))for(const ev of Object.keys(LABELS.evidence)){
    const b=createBlueprint({location:loc,operator:op,capacity,evidence:ev});
    assert.ok(b.controls.every(c=>!['PASS','COMPLIANT','CERTIFIED'].includes(c.evidence)));
    assert.ok(b.architectures.length>=4);
  }
});