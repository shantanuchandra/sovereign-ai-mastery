import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {LABELS,PRESET_LABELS} from '../studio-engine.mjs';
const html=readFileSync(new URL('../index.html',import.meta.url),'utf8');
const ui=readFileSync(new URL('../studio-ui.mjs',import.meta.url),'utf8');
test('every dimension in the engine has a named dropdown on the page',()=>{
  for(const key of Object.keys(LABELS)){
    assert.match(html,new RegExp(`name="${key}"`),key);
    assert.match(html,new RegExp(`id="${key}"`),key);
  }
  assert.equal(Object.keys(LABELS).length,10);
});
test('presets, full library and boundary warning have UI affordances',()=>{
  for(const id of ['scenario-library','apply-scenario','boundary-warning','counter-key','counter-value'])assert.ok(html.includes(`id="${id}"`));
  assert.ok(Object.keys(PRESET_LABELS).length>=15);
  assert.match(ui,/populateDropdowns\(\)/);
  assert.match(ui,/PRESET_LABELS/);
  assert.match(html,/data-preset="onsite"/);
  assert.match(html,/data-preset="factory"/);
});