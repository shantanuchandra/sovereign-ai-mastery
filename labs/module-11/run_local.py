"""Real CPU generation from verified local files; Python network connections denied."""
import os
os.environ.update(HF_HUB_OFFLINE='1',TRANSFORMERS_OFFLINE='1',HF_HUB_DISABLE_TELEMETRY='1',TOKENIZERS_PARALLELISM='false')
import argparse,json,platform,socket,time
from datetime import datetime,timezone
from pathlib import Path
from evaluate import score_rows,verify_manifest

def deny_network(*args,**kwargs):raise RuntimeError('Network call denied by Module 11 lab')

def main():
    p=argparse.ArgumentParser();p.add_argument('model_dir',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
    if a.output.exists():raise SystemExit('Choose a new evidence path; existing evidence is not overwritten')
    started_utc=datetime.now(timezone.utc).isoformat()
    manifest=json.loads((a.model_dir/'manifest.json').read_text());verify_manifest(a.model_dir,manifest)
    from prepare import MODEL,REVISION,FILES
    if manifest.get('model')!=MODEL or manifest.get('revision')!=REVISION or set(manifest['files'])!=set(FILES):raise SystemExit('Unexpected model, revision or file inventory')
    # Process-local guard, not a physical firewall or proof about native libraries/OS.
    socket.socket.connect=deny_network;socket.create_connection=deny_network;socket.getaddrinfo=deny_network
    import torch,transformers
    from transformers import AutoTokenizer,AutoModelForCausalLM
    torch.set_num_threads(2);torch.manual_seed(0)
    start=time.perf_counter()
    tokenizer=AutoTokenizer.from_pretrained(a.model_dir,local_files_only=True,trust_remote_code=False)
    model=AutoModelForCausalLM.from_pretrained(a.model_dir,local_files_only=True,trust_remote_code=False,dtype=torch.float32,use_safetensors=True).to('cpu').eval()
    load_seconds=time.perf_counter()-start
    cases=json.loads(Path(__file__).with_name('cases.json').read_text());rows=[]
    for case in cases:
        tokens=tokenizer.apply_chat_template([{'role':'user','content':case['prompt']}],add_generation_prompt=True,return_tensors='pt',return_dict=True)
        start=time.perf_counter()
        with torch.inference_mode():output=model.generate(**tokens,do_sample=False,max_new_tokens=24,pad_token_id=tokenizer.eos_token_id)
        elapsed=time.perf_counter()-start;new=output[0,tokens['input_ids'].shape[-1]:]
        rows.append(dict(case,output=tokenizer.decode(new,skip_special_tokens=True),input_tokens=int(tokens['input_ids'].shape[-1]),generated_tokens=len(new),seconds=round(elapsed,6)))
    evidence=dict(started_utc=started_utc,model=manifest['model'],revision=manifest['revision'],artifact_hashes=manifest['files'],platform=platform.platform(),machine=platform.machine(),python=platform.python_version(),torch=torch.__version__,transformers=transformers.__version__,device='cpu',dtype='float32',threads=2,max_new_tokens=24,do_sample=False,load_seconds=round(load_seconds,6),network_guard='Python connect/create_connection/getaddrinfo denied; not OS isolation',rows=rows,exact_match=score_rows(rows),status='REVIEW_REQUIRED',limits='Eight synthetic cases, four per language; exact labels only, no production accuracy, p95, security or residency claim')
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n');print(json.dumps(evidence['exact_match'],ensure_ascii=False));print(a.output)
if __name__=='__main__':main()
