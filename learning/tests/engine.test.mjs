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
  assert.equal(b.trace.length,Object.keys(LABELS).length);
  for(const key of ['location','operator','portability','jurisdiction','connectivity'])assert.ok(b.trace.some(x=>x.key===key));
});
test('challenge set adapts to blockers and portability',()=>{
  const blocked=createChallenges(PRESETS.banking);
  const basic=createChallenges(PRESETS.support);
  assert.equal(blocked.length,7);assert.equal(basic.length,7);
  assert.match(blocked[1].question,/enterprise compute is unavailable/);
  assert.match(basic[1].question,/platform hosts/);
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


test('broad taxonomy supports all presets with valid dropdown values',()=>{
  assert.ok(Object.keys(LABELS.workload).length>=18);
  for(const p of Object.values(PRESETS))for(const [key,value] of Object.entries(p))assert.ok(Object.hasOwn(LABELS[key],value),`${key}:${value}`);
  assert.ok(Object.keys(LABELS.location).length>=8);
});
test('premises only and adequate onsite controls never select a cloud endpoint',()=>{
  const b=createBlueprint(PRESETS.onsite);
  assert.equal(b.pattern,'onprem');assert.equal(b.status,'PROVISIONAL');
  assert.match(b.architectures[2].detail,/no off-prem/);
  assert.match(b.controls[0].claim,/telemetry, backups or diagnostics/);
  assert.ok(createChallenges(PRESETS.onsite)[0].question.includes('premises'));
});
test('on-premises rule blocks remote cloud compute even with vendor promises',()=>{
  for(const capacity of ['managed','public_cloud','colo','gpu','private_dc','hybrid','laptop']){
    const b=createBlueprint({...PRESETS.onsite,capacity});
    assert.equal(b.pattern,'gated',capacity);assert.equal(b.status,'BLOCKED');
    assert.doesNotMatch(b.architectures[2].detail,/managed inference endpoint/i);
    assert.ok(b.conflicts.some(x=>x.includes('physically located')));
  }
});
test('premises restriction disallows unsupported external links and remote administration',()=>{
  for(const connectivity of ['internet','flexible','private_links'])assert.equal(createBlueprint({...PRESETS.onsite,connectivity}).status,'BLOCKED');
  for(const operator of ['local','provider','shared','dedicated'])assert.equal(createBlueprint({...PRESETS.onsite,operator}).status,'BLOCKED');
});
test('air gap only permits disconnected networking and onsite compute',()=>{
  const a=createBlueprint(PRESETS.factory);
  assert.equal(a.pattern,'airgap');assert.equal(a.status,'PROVISIONAL');
  for(const connectivity of Object.keys(LABELS.connectivity)){
    const b=createBlueprint({...PRESETS.factory,connectivity});
    assert.equal(b.status,connectivity==='disconnected'?'PROVISIONAL':'BLOCKED');
  }
});
test('reported failing evidence blocks release until RCA and retest',()=>{
  const b=createBlueprint({...PRESETS.onsite,evidence:'adverse'});
  assert.equal(b.status,'BLOCKED');assert.match(b.gates.join(' '),/RCA/);
  assert.ok(b.controls.every(x=>x.evidence!=='PASS'));
});
test('every processing boundary and operating capability pair is fail closed when premises-only',()=>{
  for(const location of ['premises','airgap'])for(const capacity of Object.keys(LABELS.capacity))for(const operator of Object.keys(LABELS.operator)){
    const b=createBlueprint({...PRESETS.onsite,location,capacity,operator,connectivity:location==='airgap'?'disconnected':'isolated'});
    if(b.status==='PROVISIONAL'){
      assert.ok(['onsite_cpu','onsite_gpu'].includes(capacity));assert.ok(['enterprise','onsite_partner'].includes(operator));
      assert.ok(['onprem','airgap'].includes(b.pattern));
    }else assert.equal(b.pattern,'gated');
  }
});
test('local-only network rejects remote compute and remote administration',()=>{
  for(const capacity of ['managed','hybrid','public_cloud','colo'])assert.equal(createBlueprint({...PRESETS.assistant,location:'country',connectivity:'isolated',capacity}).status,'BLOCKED');
  for(const operator of ['provider','shared','local','dedicated'])assert.equal(createBlueprint({...PRESETS.factory,operator}).status,'BLOCKED');
});
test('on-premises learning journal records hard boundary and precise test',()=>{
  const b=createBlueprint(PRESETS.onsite);
  const md=exportJournal(b,createChallenges(b.input),{},'I must test backup and telemetry paths.');
  assert.match(md,/Single premises only/);
  assert.match(md,/removable-media/);
  assert.match(md,/on-prem/i);
});

test('Module 02 A-03: all selectable Studio paths reject air-gap network and remote operators',()=>{
  for(const connectivity of Object.keys(LABELS.connectivity)){
    for(const operator of Object.keys(LABELS.operator)){
      const b=createBlueprint({...PRESETS.factory,connectivity,operator});
      const eligible=connectivity==='disconnected'&&['enterprise','onsite_partner'].includes(operator);
      assert.equal(b.status,eligible?'PROVISIONAL':'BLOCKED',JSON.stringify({connectivity,operator}));
      if(!eligible){
        assert.equal(b.pattern,'gated',JSON.stringify({connectivity,operator}));
        assert.ok(b.controls.every(c=>c.evidence!=='PASS'));
      }
    }
  }
});
test('Module 02 A-03: premises-only hard gate cannot be cleared by evidence label or release stage',()=>{
  for(const evidence of Object.keys(LABELS.evidence)){
    for(const stage of Object.keys(LABELS.stage)){
      for(const capacity of ['managed','hybrid','public_cloud','colo']){
        const b=createBlueprint({...PRESETS.onsite,evidence,stage,capacity});
        assert.equal(b.status,'BLOCKED',JSON.stringify({evidence,stage,capacity}));
        assert.equal(b.pattern,'gated');
        assert.ok(b.controls.every(c=>c.evidence!=='PASS'));
      }
    }
  }
});
test('Module 02 A-03: local premises with external network options remains blocked',()=>{
  for(const connectivity of ['internet','flexible','private_links']){
    for(const evidence of Object.keys(LABELS.evidence)){
      const b=createBlueprint({...PRESETS.onsite,connectivity,evidence});
      assert.equal(b.status,'BLOCKED',JSON.stringify({connectivity,evidence}));
      assert.equal(b.pattern,'gated');
    }
  }
});
