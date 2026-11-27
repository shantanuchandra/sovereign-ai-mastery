#!/usr/bin/env python3
"""Synthetic local lexical retrieval and lifecycle lab. No external requests or model."""
from collections import Counter
from datetime import date
import hashlib
import json
import math
from pathlib import Path
import re
import sqlite3
from tempfile import TemporaryDirectory

IDENT=re.compile(r'^[a-z][a-z0-9_]{0,40}$')

def identifier(value):
    if not isinstance(value,str) or not IDENT.fullmatch(value):raise ValueError('invalid identifier')
    return value

def tokens(text):return re.findall(r'\w+',text.casefold())

def vector(text):return dict(Counter(tokens(text)))

def similarity(a,b):
    denom=math.sqrt(sum(v*v for v in a.values())*sum(v*v for v in b.values()))
    return sum(v*b.get(k,0) for k,v in a.items())/denom if denom else 0

class Pipeline:
    def __init__(self,root,site='PLANT-A',country='UAE',airgap=True):
        if not isinstance(site,str) or not site.strip() or not isinstance(country,str) or not country.strip() or type(airgap) is not bool:raise ValueError('explicit site, country and Boolean connectivity policy required')
        self.root=Path(root)
        if self.root.is_symlink():raise ValueError('symlink root rejected')
        marker=self.root/'.module08-lab'
        if self.root.exists():
            if not marker.is_file() or marker.is_symlink() or marker.read_text()!='synthetic-v1':raise ValueError('not an owned lab directory')
        else:
            self.root.mkdir(parents=True);marker.write_text('synthetic-v1')
        self.root=self.root.resolve();self.site=site;self.country=country;self.airgap=airgap
        for name in ('store.sqlite','ledger.sqlite'):
            if (self.root/name).is_symlink():raise ValueError('symlink database rejected')
        if (self.root/'store.sqlite').exists() and not (self.root/'ledger.sqlite').exists():raise ValueError('missing deletion ledger; fail closed')
        self.ledger=sqlite3.connect(self.root/'ledger.sqlite')
        self.ledger.executescript('CREATE TABLE IF NOT EXISTS tombstones(tenant TEXT,id TEXT,PRIMARY KEY(tenant,id)); CREATE TABLE IF NOT EXISTS backups(name TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS events(action TEXT,tenant TEXT,id TEXT);')
        self.db=sqlite3.connect(self.root/'store.sqlite')
        self.db.execute('PRAGMA foreign_keys=ON')
        if self.db.execute('PRAGMA foreign_keys').fetchone()[0]!=1:raise RuntimeError('foreign keys unavailable')
        self.db.executescript('''CREATE TABLE IF NOT EXISTS docs(id TEXT PRIMARY KEY,tenant TEXT,classification TEXT,owner TEXT,expires TEXT,source_hash TEXT,format TEXT);
        CREATE TABLE IF NOT EXISTS chunks(id TEXT PRIMARY KEY,doc TEXT REFERENCES docs(id) ON DELETE CASCADE,text TEXT,vector TEXT);''')
        self.apply_tombstones()

    def close(self):self.db.close();self.ledger.close()

    def owned_file(self,name):
        identifier(name)
        p=self.root/(name+'.sqlite')
        if p.is_symlink():raise ValueError('symlink artifact rejected')
        return p

    def ingest(self,record):
        if not isinstance(record,dict):raise ValueError('record must be object')
        doc=identifier(record.get('id'));tenant=identifier(record.get('tenant'))
        if record.get('site')!=self.site or record.get('country')!=self.country or record.get('preprocess_site')!=self.site:raise ValueError('BLOCKED: declared site/country conflict')
        transport=record.get('transport')
        if transport not in ('local','media','network'):raise ValueError('unknown transport')
        if self.airgap and transport=='network':raise ValueError('BLOCKED: physical air-gap conflict')
        if record.get('classification') not in ('public','internal','restricted'):raise ValueError('classification required')
        if not isinstance(record.get('owner'),str) or not record['owner'].strip():raise ValueError('owner required')
        try:expiry=date.fromisoformat(record.get('expires')).isoformat()
        except (ValueError,TypeError):raise ValueError('valid expiry date required') from None
        kind=record.get('format');body=record.get('body')
        if kind=='record':
            if not isinstance(body,dict) or not body or not all(isinstance(k,str) and isinstance(v,str) for k,v in body.items()):raise ValueError('structured fields must be strings')
            source=json.dumps(body,ensure_ascii=False,sort_keys=True)
            text=' '.join(body[k] for k in sorted(body))
        elif kind in ('text','ocr','transcript') and isinstance(body,str):source=text=body
        else:raise ValueError('unsupported synthetic format')
        if not tokens(text):raise ValueError('empty content')
        if self.ledger.execute('SELECT 1 FROM tombstones WHERE tenant=? AND id=?',(tenant,doc)).fetchone():raise ValueError('retired identifier cannot be reused')
        words=text.split();parts=[' '.join(words[i:i+24]) for i in range(0,len(words),24)]
        with self.db:
            self.db.execute('INSERT INTO docs VALUES(?,?,?,?,?,?,?)',(doc,tenant,record['classification'],record['owner'],expiry,hashlib.sha256(source.encode()).hexdigest(),kind))
            for i,part in enumerate(parts):self.db.execute('INSERT INTO chunks VALUES(?,?,?,?)',(f'{doc}_{i}',doc,part,json.dumps(vector(part),ensure_ascii=False)))
        with self.ledger:self.ledger.execute('INSERT INTO events VALUES(?,?,?)',('ingest',tenant,doc))
        return {'id':doc,'chunks':len(parts),'classification':record['classification'],'provenance':'sha256 of canonical source; not anonymity'}

    def query(self,tenant,text,as_of):
        identifier(tenant);day=date.fromisoformat(as_of).isoformat()
        if not isinstance(text,str):raise ValueError('query must be text')
        q=vector(text);result=[]
        # Caller-supplied tenant scope is applied before scoring. Authentication is not implemented.
        rows=self.db.execute('SELECT d.id,d.classification,c.id,c.text,c.vector,d.source_hash FROM docs d JOIN chunks c ON c.doc=d.id WHERE d.tenant=? AND d.expires>?',(tenant,day))
        for doc,classification,chunk,content,v,source_hash in rows:
            if self.ledger.execute('SELECT 1 FROM tombstones WHERE tenant=? AND id=?',(tenant,doc)).fetchone():continue
            score=similarity(q,json.loads(v))
            if score>0:result.append({'document':doc,'chunk':chunk,'classification':classification,'score':score,'text':content,'source_hash':source_hash})
        with self.ledger:self.ledger.execute('INSERT INTO events VALUES(?,?,NULL)',('query',tenant))
        return sorted(result,key=lambda r:(-r['score'],r['chunk']))[:5]

    def snapshot(self,name):
        p=self.owned_file(name)
        if p.exists():raise ValueError('snapshot already exists')
        target=sqlite3.connect(p)
        try:self.db.backup(target)
        finally:target.close()
        with self.ledger:self.ledger.execute('INSERT INTO backups VALUES(?)',(name,))
        return p

    def apply_tombstones(self):
        with self.db:
            for tenant,doc in self.ledger.execute('SELECT tenant,id FROM tombstones'):
                self.db.execute('DELETE FROM docs WHERE tenant=? AND id=?',(tenant,doc))

    def retire(self,tenant,doc):
        identifier(tenant);identifier(doc)
        # Durable tombstone precedes deletion; query filtering also checks this ledger.
        with self.ledger:self.ledger.execute('INSERT OR IGNORE INTO tombstones VALUES(?,?)',(tenant,doc))
        self.apply_tombstones()
        with self.ledger:self.ledger.execute('INSERT INTO events VALUES(?,?,?)',('retire',tenant,doc))
        return {'state':'UNVERIFIED' if self.ledger.execute('SELECT 1 FROM backups').fetchone() else 'REVIEW_REQUIRED','limits':'Logical deletion only; unknown copies and physical remnants not assessed.'}

    def expire(self,as_of):
        day=date.fromisoformat(as_of).isoformat()
        rows=list(self.db.execute('SELECT tenant,id FROM docs WHERE expires<=?',(day,)))
        for tenant,doc in rows:self.retire(tenant,doc)
        return len(rows)

    def restore(self,name):
        p=self.owned_file(name)
        if not self.ledger.execute('SELECT 1 FROM backups WHERE name=?',(name,)).fetchone() or not p.is_file():raise ValueError('unknown or missing snapshot')
        source=sqlite3.connect(p)
        try:source.backup(self.db)
        finally:source.close()
        self.apply_tombstones()

    def remove_snapshot(self,name):
        p=self.owned_file(name)
        if not self.ledger.execute('SELECT 1 FROM backups WHERE name=?',(name,)).fetchone():raise ValueError('unknown snapshot')
        p.unlink(missing_ok=True)
        with self.ledger:self.ledger.execute('DELETE FROM backups WHERE name=?',(name,))


def demo():
    records=json.loads(Path(__file__).with_name('records.json').read_text())
    with TemporaryDirectory(prefix='module08-') as temp:
        p=Pipeline(Path(temp)/'lab')
        try:
            for r in records:p.ingest(r)
            before=p.query('plant_a','pump pressure','2026-11-26')
            p.snapshot('before_retirement');decision=p.retire('plant_a','manual_a')
            p.restore('before_retirement');after=p.query('plant_a','pump pressure','2026-11-26')
            p.remove_snapshot('before_retirement')
            print(json.dumps({'synthetic':True,'before_count':len(before),'retirement':decision,'after_restore_count':len(after),'limits':'Lexical toy vectors; no semantic model, secure erasure or production assurance.'},indent=2))
        finally:p.close()

if __name__=='__main__':demo()
