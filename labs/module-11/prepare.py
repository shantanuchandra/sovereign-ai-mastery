"""Online public-artifact preparation only; do not run inside an asserted air gap."""
import hashlib,json,sys
from pathlib import Path
MODEL='HuggingFaceTB/SmolLM2-135M-Instruct'
REVISION='12fd25f77366fa6b3b4b768ec3050bf629380bac'
FILES=['README.md','config.json','generation_config.json','merges.txt','model.safetensors','special_tokens_map.json','tokenizer.json','tokenizer_config.json','vocab.json']

def main():
    from huggingface_hub import snapshot_download
    dest=Path(sys.argv[1]).resolve()
    if dest.exists() and any(dest.iterdir()):raise SystemExit('Use a new empty directory; existing artifacts are not overwritten')
    dest.mkdir(parents=True,exist_ok=True)
    snapshot_download(MODEL,revision=REVISION,allow_patterns=FILES,local_dir=dest,token=False)
    manifest=dict(model=MODEL,revision=REVISION,license_declaration='Apache-2.0 in pinned model card; inspect its linked full licence',license_url='https://www.apache.org/licenses/LICENSE-2.0',files={p:hashlib.sha256((dest/p).read_bytes()).hexdigest() for p in FILES})
    (dest/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(manifest,indent=2))
if __name__=='__main__':main()
