"""Real local CPU thread experiment. No training, quantization or external inference."""
import os
os.environ.update(HF_HUB_OFFLINE='1',TRANSFORMERS_OFFLINE='1',HF_HUB_DISABLE_TELEMETRY='1',TOKENIZERS_PARALLELISM='false')
import argparse
import json
import platform
import socket
import subprocess
import sys
import tempfile
import time
from datetime import datetime,timezone
from pathlib import Path
from experiment import MODEL,REVISION,PROFILES,REPEATS,MAX_NEW_TOKENS,digest,verify_manifest,summarize,validate_record


def deny_network(*args,**kwargs):
    raise RuntimeError('Network call denied by Module 13 lab')


def worker(model_dir, threads, output):
    manifest=json.loads((model_dir/'manifest.json').read_text());verify_manifest(model_dir,manifest)
    socket.socket.connect=deny_network;socket.create_connection=deny_network;socket.getaddrinfo=deny_network
    import torch,transformers
    if torch.__version__.split('+',1)[0]!='2.9.1' or transformers.__version__!='4.57.3': raise ValueError('Use pinned dependency versions')
    torch.set_num_threads(threads);torch.manual_seed(0)
    from transformers import AutoTokenizer,AutoModelForCausalLM
    start=time.perf_counter()
    tokenizer=AutoTokenizer.from_pretrained(model_dir,local_files_only=True,trust_remote_code=False)
    model=AutoModelForCausalLM.from_pretrained(model_dir,local_files_only=True,trust_remote_code=False,dtype=torch.float32,use_safetensors=True).to('cpu').eval()
    load_seconds=time.perf_counter()-start
    cases=json.loads(Path(__file__).with_name('cases.json').read_text())
    encoded=[tokenizer.apply_chat_template([{'role':'user','content':c['prompt']}],add_generation_prompt=True,return_tensors='pt',return_dict=True) for c in cases]
    kwargs=dict(do_sample=False,max_new_tokens=MAX_NEW_TOKENS,pad_token_id=tokenizer.eos_token_id,use_cache=True)
    with torch.inference_mode(): model.generate(**encoded[0],**kwargs)
    rows=[]
    for repeat in range(REPEATS):
        for case,tokens in zip(cases,encoded):
            start=time.perf_counter()
            with torch.inference_mode(): generated=model.generate(**tokens,**kwargs)
            elapsed=time.perf_counter()-start
            continuation=generated[0,tokens['input_ids'].shape[-1]:]
            rows.append(dict(case,threads=threads,repeat=repeat,seconds=round(elapsed,6),input_tokens=int(tokens['input_ids'].shape[-1]),generated_tokens=len(continuation),output=tokenizer.decode(continuation,skip_special_tokens=True)))
    output.write_text(json.dumps(dict(rows=rows,load_seconds=load_seconds,torch=torch.__version__,transformers=transformers.__version__),ensure_ascii=False))


def main():
    p=argparse.ArgumentParser();p.add_argument('model_dir',type=Path);p.add_argument('output',type=Path);p.add_argument('--worker',type=int,choices=PROFILES);a=p.parse_args()
    if a.output.exists(): raise SystemExit('Use a new evidence path; existing output not overwritten')
    if a.worker: worker(a.model_dir,a.worker,a.output);return
    started=datetime.now(timezone.utc).isoformat()
    manifest=json.loads((a.model_dir/'manifest.json').read_text());verify_manifest(a.model_dir,manifest)
    rows=[];loads={}
    with tempfile.TemporaryDirectory(prefix='module13-workers-') as temp:
        for threads in PROFILES:
            part=Path(temp)/f'{threads}.json'
            subprocess.run([sys.executable,str(Path(__file__).resolve()),str(a.model_dir.resolve()),str(part),'--worker',str(threads)],check=True,timeout=300)
            result=json.loads(part.read_text());rows.extend(result['rows']);loads[str(threads)]=result['load_seconds']
    record=dict(schema='module13-inference-v1',started_utc=started,model=MODEL,revision=REVISION,artifact_hashes=manifest['files'],cases_sha256=digest(Path(__file__).with_name('cases.json')),platform=platform.platform(),machine=platform.machine(),python=platform.python_version(),torch=result['torch'],transformers=result['transformers'],settings=dict(device='cpu',dtype='float32',do_sample=False,max_new_tokens=MAX_NEW_TOKENS,use_cache=True,repeats=REPEATS,warmups_per_profile=1,profile_order=[1,2]),load_seconds=loads,rows=rows,summary=summarize(rows),network_guard='Python connect/create_connection/getaddrinfo denied; not OS isolation',status='REVIEW_REQUIRED',limits='Eight synthetic cases repeated three times per profile; profile order not counterbalanced; no production quality/load/p95, energy, peak-memory, quantization or training claim')
    validate_record(record,json.loads(Path(__file__).with_name('cases.json').read_text()))
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open('x') as f: f.write(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(record['summary'],indent=2));print(a.output)

if __name__=='__main__': main()
