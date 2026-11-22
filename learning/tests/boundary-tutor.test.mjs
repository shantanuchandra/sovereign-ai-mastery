import test from 'node:test';
import assert from 'node:assert/strict';
import * as engine from '../studio-engine.mjs';

test('premises flows cover hidden lifecycle paths and retain a physical destination',()=>{
  const b=engine.createBlueprint(engine.PRESETS.onsite);
  assert.ok(Array.isArray(b.flows),'blueprint must include a data-flow register');
  for(const id of ['ingestion','retrieval','inference','outputs','telemetry','backup','support','updates','licensing']){
    const flow=b.flows.find(f=>f.id===id);
    assert.ok(flow,id);
    assert.match(flow.destination,/premises/i,id);
    assert.ok(flow.owner&&flow.test&&flow.artifacts,id);
    assert.equal(flow.evidence,'UNVERIFIED');
  }
});

test('every air-gap flow forbids network use, including activation and support',()=>{
  const b=engine.createBlueprint(engine.PRESETS.factory);
  assert.ok(Array.isArray(b.flows),'air-gap design needs explicit flows');
  for(const flow of b.flows){
    assert.equal(flow.network,'NONE',flow.id);
    assert.doesNotMatch(flow.destination,/cloud|remote portal/i);
  }
  assert.match(b.flows.find(f=>f.id==='licensing').test,/offline.*restart|restart.*offline/i);
  assert.match(b.flows.find(f=>f.id==='updates').test,/media/i);
});

test('incompatible and adverse designs cannot export permissive flow records',()=>{
  for(const changes of [{capacity:'public_cloud'},{connectivity:'internet'},{evidence:'adverse'}]){
    const b=engine.createBlueprint({...engine.PRESETS.onsite,...changes});
    assert.equal(b.status,'BLOCKED');
    assert.ok(Array.isArray(b.flows),'blocked designs still expose required paths');
    assert.ok(b.flows.every(f=>f.evidence==='BLOCKED'));
  }
});

test('new scenarios use valid taxonomy values and expose speech and OCR dependencies',()=>{
  for(const id of ['insurance','procurement','education','energy','geospatial','speech']){
    assert.ok(engine.LABELS.workload[id],id);
    assert.ok(engine.PRESETS[id],id);
    assert.ok(engine.PRESET_LABELS[id],id);
    assert.deepEqual(engine.normalize(engine.PRESETS[id]),engine.PRESETS[id]);
  }
  const voice=engine.createBlueprint(engine.PRESETS.speech);
  assert.ok(voice.flows.some(f=>f.id==='speech'&&/audio|transcript/i.test(f.artifacts)));
  const insurance=engine.createBlueprint(engine.PRESETS.insurance);
  assert.ok(insurance.flows.some(f=>f.id==='ocr'&&/OCR/.test(f.name)));
});

test('each missed concept produces a new question with an actionable rationale',()=>{
  assert.equal(typeof engine.createRemediation,'function');
  for(const inputs of [engine.PRESETS.onsite,engine.PRESETS.factory,engine.PRESETS.support]){
    for(const q of engine.createChallenges(inputs)){
      const follow=engine.createRemediation(q,inputs);
      assert.equal(follow.id,`remediation-${q.id}`);
      assert.notEqual(follow.question,q.question);
      assert.equal(follow.options.length,3);
      assert.equal(engine.evaluateChallenge(follow,follow.correct).ok,true);
      assert.ok(engine.evaluateChallenge(follow,(follow.correct+1)%3).action);
    }
  }
  assert.equal(engine.createRemediation({id:'unknown'},{}),null);
  assert.equal(engine.createRemediation({id:'__proto__'},{}),null);
});

test('journal keeps the first misconception after a correct follow-up and exports flows',()=>{
  const b=engine.createBlueprint(engine.PRESETS.factory),qs=engine.createChallenges(b.input);
  assert.equal(typeof engine.createRemediation,'function');
  const q=qs[0],follow=engine.createRemediation(q,b.input);
  const md=engine.exportJournal(b,qs,{[q.id]:(q.correct+1)%3},'Test local activation',{[follow.id]:follow.correct});
  assert.match(md,/Data-flow register/);
  assert.match(md,/licensing/i);
  assert.match(md,/Needs review/);
  assert.match(md,/Follow-up result: Correct reasoning/);
  assert.match(md,/first attempt/i);
  assert.doesNotThrow(()=>engine.exportJournal(b,qs,{location:999},'',{'remediation-location':999}));
});
