#!/usr/bin/env python3
"""Synthetic policy and key-version metadata only: no encryption, IdP, KMS or TEE."""
import copy
import json
import platform
import threading

ARTIFACTS = ('prompts','outputs','weights','embeddings','ocr','speech','diagnostics','logs','telemetry','backups','support','activation','updates','recovery','removable_media')

def boundary_state(declaration):
    """Known conflicts dominate omissions. Declarations never verify a facility."""
    if not isinstance(declaration, dict):
        return 'UNVERIFIED'
    conflicts = any(declaration.get(k) not in (None, 'BANK-A') for k in ARTIFACTS)
    conflicts |= declaration.get('operators') not in (None, 'onsite')
    conflicts |= declaration.get('network') not in (None, 'offline')
    conflicts |= declaration.get('media_reviewed') not in (None, True)
    if conflicts:
        return 'BLOCKED'
    if any(declaration.get(k) is None for k in ARTIFACTS + ('operators','network','media_reviewed')):
        return 'UNVERIFIED'
    return 'DECLARED_ONLY'

def local_declaration():
    return dict.fromkeys(ARTIFACTS, 'BANK-A') | {'operators':'onsite','network':'offline','media_reviewed':True}

class Denied(Exception):
    pass

class CustodyGate:
    def __init__(self):
        # These labels are public fixtures, not credentials or authentication.
        self.sessions = {'s-reader': 'reader', 's-admin': 'admin', 's-c1':'custodian1', 's-c2':'custodian2', 's-support':'support', 's-other':'other'}
        self.users = {
            'reader': {'tenant':'A','roles':{'reader'},'clearance':2,'expires':200,'active':True},
            'admin': {'tenant':'A','roles':{'key-admin'},'clearance':0,'expires':200,'active':True},
            'custodian1': {'tenant':'A','roles':{'custodian'},'clearance':0,'expires':200,'active':True},
            'custodian2': {'tenant':'A','roles':{'custodian'},'clearance':0,'expires':200,'active':True},
            'support': {'tenant':'A','roles':{'support'},'clearance':0,'expires':200,'active':True},
            'other': {'tenant':'B','roles':{'reader','custodian'},'clearance':3,'expires':200,'active':True},
        }
        self.keys = {'A-key': {'tenant':'A','current':1,'versions':{1:'active'},'revision':1}}
        self.resources = {'A-doc': {'tenant':'A','key':'A-key','version':1,'classification':2}, 'B-doc': {'tenant':'B','key':'B-key','version':1,'classification':1}}
        self.policy_revision = 1
        self.declaration = local_declaration()
        self.audit_available = True
        self.audit = []
        self.grants = {}
        self.counter = 0
        self.lock = threading.RLock()

    def _actor(self, session, now):
        actor = self.sessions.get(session)
        user = self.users.get(actor)
        if not user or not user['active'] or now >= user['expires']:
            raise Denied('IDENTITY')
        return actor, user

    def _ready(self):
        if boundary_state(self.declaration) != 'DECLARED_ONLY':
            raise Denied('BOUNDARY')
        if not self.audit_available:
            raise Denied('AUDIT')

    def _record(self, actor, operation, target, outcome):
        # No session handles, key bytes, document bodies or free-text errors.
        self.audit.append({'actor':actor,'operation':operation,'target':target,'outcome':outcome,'policy_revision':self.policy_revision})

    def access(self, session, resource, now=100):
        """Return version metadata after current RBAC/ABAC checks; never plaintext."""
        with self.lock:
            self._ready()
            actor, user = self._actor(session, now)
            item = self.resources.get(resource)
            if not item or item['tenant'] != user['tenant'] or 'reader' not in user['roles'] or user['clearance'] < item['classification']:
                raise Denied('PERMISSION')
            key = self.keys.get(item['key'])
            if not key or key['tenant'] != user['tenant'] or key['versions'].get(item['version']) not in ('active','retired'):
                raise Denied('KEY_UNAVAILABLE')
            self._record(actor, 'access-metadata', resource, 'ALLOWED')
            return {'resource':resource,'key_version':item['version'],'result':'METADATA_ONLY'}

    def approve_rotation(self, session, key_id, expected_revision, now=100, ttl=10):
        with self.lock:
            self._ready()
            actor, user = self._actor(session, now)
            key = self.keys.get(key_id)
            if not key or key['tenant'] != user['tenant'] or 'custodian' not in user['roles']:
                raise Denied('APPROVER')
            if key['revision'] != expected_revision or not isinstance(ttl, int) or isinstance(ttl, bool) or not 0 < ttl <= 10:
                raise Denied('STALE_OR_TTL')
            self.counter += 1
            grant_id = 'fixture-grant-' + str(self.counter)
            self.grants[grant_id] = {'actor':actor,'key':key_id,'revision':expected_revision,'policy':self.policy_revision,'expires':now+ttl,'used':False}
            return grant_id

    def rotate(self, session, key_id, expected_revision, approvals, now=100):
        with self.lock:
            self._ready()
            actor, user = self._actor(session, now)
            key = self.keys.get(key_id)
            if not key or key['tenant'] != user['tenant'] or 'key-admin' not in user['roles']:
                raise Denied('ADMIN')
            if key['revision'] != expected_revision:
                raise Denied('STALE_REVISION')
            if not isinstance(approvals, (list,tuple)) or len(approvals) != 2 or len(set(approvals)) != 2:
                raise Denied('TWO_APPROVALS')
            grants = [self.grants.get(g) for g in approvals]
            if any(not g or g['used'] or now >= g['expires'] or g['key'] != key_id or g['revision'] != expected_revision or g['policy'] != self.policy_revision for g in grants):
                raise Denied('GRANT')
            approvers = {g['actor'] for g in grants}
            if len(approvers) != 2 or actor in approvers:
                raise Denied('SEPARATION')
            for who in approvers:
                u = self.users.get(who)
                if not u or not u['active'] or now >= u['expires'] or u['tenant'] != user['tenant'] or 'custodian' not in u['roles']:
                    raise Denied('REVOKED_APPROVER')
            old = key['current']
            self._record(actor, 'rotate-metadata', key_id, 'AUTHORIZED')
            for g in grants:
                g['used'] = True
            key['versions'][old] = 'retired'
            key['current'] += 1
            key['versions'][key['current']] = 'active'
            key['revision'] += 1
            return copy.deepcopy(key)

def demo():
    gate = CustodyGate()
    attempts = []
    def attempt(label, action):
        try:
            result = action()
            attempts.append({'case':label,'decision':'ALLOWED','result':result})
        except Denied as exc:
            attempts.append({'case':label,'decision':'DENIED','reason':str(exc)})
    attempt('administrator-read', lambda: gate.access('s-admin','A-doc'))
    attempt('cross-tenant-read', lambda: gate.access('s-other','A-doc'))
    attempt('reader-before-rotation', lambda: gate.access('s-reader','A-doc'))
    one = gate.approve_rotation('s-c1','A-key',1)
    two = gate.approve_rotation('s-c2','A-key',1)
    attempt('two-custodian-rotation',lambda: gate.rotate('s-admin','A-key',1,[one,two]))
    attempt('old-record-after-rotation',lambda: gate.access('s-reader','A-doc'))
    attempt('replay-rotation',lambda: gate.rotate('s-admin','A-key',2,[one,two]))
    attempt('support-read',lambda: gate.access('s-support','A-doc'))
    return {'module':16,'scope':'SYNTHETIC_METADATA_ONLY','python':platform.python_version(),'platform':platform.system()+' '+platform.machine(),'boundary_state':boundary_state(gate.declaration),'attempts':attempts,'audit':gate.audit,'limits':['No encryption/decryption or key material','No IdP, KMS, HSM, TEE or attestation','No physical, OS or production assurance']}

if __name__ == '__main__':
    print(json.dumps(demo(),indent=2,sort_keys=True))
