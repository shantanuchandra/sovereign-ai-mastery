#!/usr/bin/env python3
"""Build/run/probe only an owned synthetic container; no host ports, mounts or cloud."""
import json
import os
from pathlib import Path
import re
import subprocess
import time
import uuid

def command(*args, timeout=60):
    try:
        return subprocess.run(args, check=True, capture_output=True, text=True, timeout=timeout).stdout.strip()
    except subprocess.CalledProcessError as error:
        raise RuntimeError('Container command failed: ' + (error.stderr or '')[-2000:]) from error

def require_local_engine():
    context = os.environ.get('DOCKER_CONTEXT')
    if context:
        endpoint = command('docker', 'context', 'inspect', '--format', '{{.Endpoints.docker.Host}}', context)
    else:
        endpoint = os.environ.get('DOCKER_HOST') or command('docker', 'context', 'inspect', '--format', '{{.Endpoints.docker.Host}}')
    if not endpoint.startswith('unix://'):
        raise ValueError('Local Unix-socket Docker engine required; remote endpoints are not accepted')


def main():
    require_local_engine()
    docker_platform = command('docker', 'info', '--format', '{{.OSType}}/{{.Architecture}}', timeout=15)
    command('docker', 'pull', 'python:3.13-slim', timeout=300)
    base_digests = json.loads(command('docker', 'image', 'inspect', 'python:3.13-slim', '--format', '{{json .RepoDigests}}'))
    if not base_digests or not re.fullmatch(r'.+@sha256:[0-9a-f]{64}', base_digests[0]):
        raise RuntimeError('resolved base digest required')
    tag = 'sovereign-module09:lab-' + uuid.uuid4().hex[:12]
    container, image_built, report = None, False, {}
    try:
        command('docker', 'build', '--build-arg', 'BASE_IMAGE=' + base_digests[0], '--tag', tag, str(Path(__file__).parent), timeout=300)
        image_built = True
        container = command('docker', 'run', '--detach', '--rm', '--network', 'none',
                            '--read-only', '--cap-drop', 'ALL', '--security-opt', 'no-new-privileges',
                            '--memory', '128m', '--cpus', '1', '--pids-limit', '64', tag)
        if not re.fullmatch(r'[0-9a-f]{64}', container):
            raise RuntimeError('unexpected owned container ID')
        for attempt in range(20):
            try:
                command('docker', 'exec', container, 'python', '-c',
                        "from urllib.request import urlopen;assert urlopen('http://127.0.0.1:8080/health',timeout=2).status==200", timeout=5)
                break
            except RuntimeError:
                if attempt == 19:
                    raise
                time.sleep(.25)
        details = json.loads(command('docker', 'inspect', container))[0]
        host = details['HostConfig']
        assert host['NetworkMode'] == 'none' and host['ReadonlyRootfs'] and not host['Privileged']
        assert host['Memory'] == 128 * 1024**2 and host['NanoCpus'] == 1000000000
        assert host['PidsLimit'] == 64 and host['PortBindings'] in (None, {})
        assert 'ALL' in host['CapDrop'] and not details['Mounts']
        assert details['Config']['User'] == '65532:65532'
        profiles = []
        for concurrency in (1, 8):
            result = json.loads(command('docker', 'exec', container, 'python', 'bench.py', '--requests', '32', '--concurrency', str(concurrency)))
            assert result['successes'] + result['errors'] == 32
            profiles.append(result)
        assert profiles[0]['successes'] == 32
        report = {'container_test': 'synthetic CPU HTTP only', 'container_configuration_inspected': True, 'docker_platform': docker_platform,
                  'image_id': details['Image'], 'base_digests': base_digests,
                  'profiles': profiles}
    finally:
        if container and re.fullmatch(r'[0-9a-f]{64}', container):
            command('docker', 'rm', '--force', container)
        if image_built:
            command('docker', 'image', 'rm', tag)
    report['owned_container_and_tag_removed'] = True
    report['cleanup_limits'] = 'Base image and build cache can remain. No global prune; no mounts or cloud resources created.'
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
