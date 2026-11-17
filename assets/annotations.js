/*
 * Reader marginalia, v1. No dependencies, no telemetry, no server.
 * Annotations live locally until a repo-scoped GitHub token is provided.
 * GitHub access token is kept ONLY in JS memory. The target repository is PUBLIC:
 * annotations/notes.json is a public file, so do not enter personal secrets.
 */
(()=>{'use strict';
  const repo=document.body.dataset.repo || 'shantanuchandra/sovereign-ai-mastery';
  const storageKey=`sovereign-ai-reader:annotations:${repo}:v1`;
  const noteList=document.querySelector('#notes-list');
  const status=document.querySelector('#sync-status');
  const toolbar=document.querySelector('#selection-toolbar');
  const dialog=document.querySelector('#note-dialog');
  const repoFile='annotations/notes.json';
  let notesRepo=repo;
  let annotations=[];
  let token=null;
  let selectionDraft=null;
  let activeEditId=null;
  let pendingSync=false;
  let syncing=false;
  const el=id=>document.getElementById(id);
  const uid=()=>`${Date.now()}-${Math.random().toString(36).slice(2,10)}`;
  const now=()=>new Date().toISOString();
  const currentContainers=()=>Array.from(document.querySelectorAll('[data-annotatable]'));
  const setStatus=msg=>{if(status)status.textContent=msg;};
  const route=()=>location.pathname.split('/').slice(-2).join('/');
  function readLocal(){try{return JSON.parse(localStorage.getItem(storageKey)||'[]')}catch{return []}}
  function persist(){try{localStorage.setItem(storageKey,JSON.stringify(annotations))}catch{setStatus('Local storage blocked')}}
  function allTextNodes(root){const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);const nodes=[];let n;while(n=w.nextNode()){if(n.parentElement?.closest('script,style,button,textarea'))continue;nodes.push(n);}return nodes;}
  function fullText(root){return allTextNodes(root).map(n=>n.data).join('');}
  function rangeInfo(){
    const s=window.getSelection();if(!s||s.isCollapsed||s.rangeCount===0)return null;
    const r=s.getRangeAt(0);const root=r.commonAncestorContainer.nodeType===1?r.commonAncestorContainer:r.commonAncestorContainer.parentElement;
    const container=root?.closest?.('[data-annotatable]');
    if(!container||!container.contains(r.startContainer)||!container.contains(r.endContainer))return null;
    const selected=r.toString();if(selected.trim().length<3||selected.length>900)return null;
    const before=document.createRange();before.selectNodeContents(container);before.setEnd(r.startContainer,r.startOffset);
    const start=before.toString().length;
    const text=fullText(container);
    return {pageId:container.dataset.pageId,route:route(),start,end:start+selected.length,quote:selected,prefix:text.slice(Math.max(0,start-40),start),suffix:text.slice(start+selected.length,start+selected.length+40),createdAt:now(),updatedAt:now()};
  }
  function hideToolbar(){toolbar.hidden=true;}
  function selectionHandler(){
    if(dialog.open)return;
    const info=rangeInfo();if(!info){hideToolbar();return;}
    selectionDraft=info;
    const r=window.getSelection().getRangeAt(0).getBoundingClientRect();
    toolbar.hidden=false;
    toolbar.style.left=`${Math.max(80,Math.min(innerWidth-90,r.left+r.width/2))}px`;
    toolbar.style.top=`${Math.max(62,r.top-9)}px`;
  }
  // Marks are stored as text offsets plus exact quote/context. If the chapter changes
  // and the quotation no longer matches, do NOT attach the mark to unrelated prose.
  function applyMark(a){
    const root=currentContainers().find(c=>c.dataset.pageId===a.pageId);if(!root)return;
    const text=fullText(root);let start=a.start;
    if(text.slice(start,a.end)!==a.quote){
      const candidates=[];let i=-1;while((i=text.indexOf(a.quote,i+1))!==-1)candidates.push(i);
      start=candidates.find(i=>text.slice(Math.max(0,i-40),i).endsWith(a.prefix)&&text.slice(i+a.quote.length,i+a.quote.length+40).startsWith(a.suffix));
      if(start===undefined)return;
    }
    const end=start+a.quote.length;let offset=0;const targets=[];
    for(const n of allTextNodes(root)){
      const from=Math.max(0,start-offset),to=Math.min(n.length,end-offset);
      if(from<to)targets.push({n,from,to});offset+=n.length;
      if(offset>=end)break;
    }
    for(const {n,from,to} of targets.reverse()){
      if(!n.parentNode)continue;
      // A saved mark might already split this text node. Idempotence is handled
      // through renderMarks' unwrap pass.
      const r=document.createRange();r.setStart(n,from);r.setEnd(n,to);
      const mark=document.createElement('mark');mark.className=`reader-mark ${a.kind==='note'?'has-note':''}`;mark.dataset.annotationId=a.id;
      try{r.surroundContents(mark)}catch{/* Leave the text untouched rather than move it. */}
    }
  }
  function renderMarks(){
    document.querySelectorAll('mark.reader-mark').forEach(mark=>mark.replaceWith(document.createTextNode(mark.textContent)));
    currentContainers().forEach(root=>root.normalize());
    const here=annotations.filter(a=>a.route===route()).sort((a,b)=>b.start-a.start);
    // Rendering the longest offsets first keeps selections stable on every repaint.
    here.forEach(applyMark);
  }
  function esc(s){return String(s||'').trim()}
  function renderNotes(){
    const local=annotations.filter(a=>a.route===route());
    el('notes-count').textContent=String(local.length);
    noteList.replaceChildren();
    if(!local.length){const empty=document.createElement('div');empty.className='empty-notes';empty.innerHTML='<span>“</span><p>Good reading leaves traces.<br>Select a passage to begin.</p>';noteList.append(empty);return;}
    for(const a of local.slice().sort((a,b)=>b.updatedAt.localeCompare(a.updatedAt))){
      const card=document.createElement('article');card.className='note-card';
      const page=document.createElement('div');page.className='note-page';page.textContent=a.kind==='highlight'?'HIGHLIGHT':'ANNOTATION';card.append(page);
      const quote=document.createElement('span');quote.className='note-quote';quote.textContent=`“${a.quote.length>180?a.quote.slice(0,180)+'…':a.quote}”`;card.append(quote);
      if(a.body){const text=document.createElement('div');text.className='note-body';text.textContent=a.body;card.append(text);}
      const meta=document.createElement('div');meta.className='note-meta';
      const jump=document.createElement('button');jump.textContent='Find in text ↗';jump.addEventListener('click',()=>{const m=[...document.querySelectorAll('mark.reader-mark')].find(x=>x.dataset.annotationId===a.id);if(m){m.scrollIntoView({behavior:'smooth',block:'center'});m.animate([{backgroundColor:'#d4a348'},{backgroundColor:''}],{duration:950});}});meta.append(jump);
      const edit=document.createElement('button');edit.textContent=a.body?'Edit note':'Add note';edit.addEventListener('click',()=>openDialog(a));meta.append(edit);card.append(meta);noteList.append(card);
    }
  }
  function render(){renderMarks();renderNotes();}
  function saveAnnotation(a){annotations=merge(annotations,[a]);persist();render();if(token)queueSync();else setStatus('Saved locally');}
  function clearSelection(){window.getSelection()?.removeAllRanges();hideToolbar();}
  function openDialog(a){activeEditId=a?.id||null;selectionDraft=a||selectionDraft;if(!selectionDraft)return;el('selected-quote').textContent=selectionDraft.quote;el('note-body').value=a?.body||'';clearSelection();dialog.showModal();el('note-body').focus();}
  function merge(one,two){const map=new Map();for(const a of [...one,...two]){if(!a||!a.id)continue;const prev=map.get(a.id);if(!prev||String(a.updatedAt||'')>=String(prev.updatedAt||''))map.set(a.id,a);}return [...map.values()];}
  function b64Encode(s){const bytes=new TextEncoder().encode(s);let chunk='';for(const b of bytes)chunk+=String.fromCharCode(b);return btoa(chunk);}
  function b64Decode(s){const raw=atob(s.replace(/\s/g,''));return new TextDecoder().decode(Uint8Array.from(raw,c=>c.charCodeAt(0)));}
  const url=()=>`https://api.github.com/repos/${notesRepo}/contents/${repoFile}`;
  async function loadRemote(auth=false){
    const headers={'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'};
    if(auth && token)headers.Authorization=`Bearer ${token}`;
    const res=await fetch(url()+'?ref=main',{headers,cache:'no-store'});
    if(res.status===404)return {sha:null,notes:[]};
    if(!res.ok)throw Error(`GitHub read failed (${res.status})`);
    const item=await res.json();const decoded=JSON.parse(b64Decode(item.content));
    if(decoded.schemaVersion!==1||!Array.isArray(decoded.annotations))throw Error('Unexpected GitHub notes format');
    return {sha:item.sha,notes:decoded.annotations};
  }
  async function sync(upload){
    if(syncing){pendingSync ||= upload;return;}
    syncing=true;setStatus(upload?'Syncing…':'Loading…');
    try{
      const remote=await loadRemote(Boolean(token));
      annotations=merge(remote.notes,annotations);persist();render();
      if(upload){
        if(!token)throw Error('Connect with a repository-scoped token first');
        const payload={schemaVersion:1,repository:notesRepo,updatedAt:now(),annotations};
        const res=await fetch(url(),{method:'PUT',headers:{'Accept':'application/vnd.github+json','Content-Type':'application/json','X-GitHub-Api-Version':'2022-11-28','Authorization':`Bearer ${token}`},body:JSON.stringify({message:'notes: sync reader annotations',branch:'main',content:b64Encode(JSON.stringify(payload,null,2)+'\n'),...(remote.sha?{sha:remote.sha}:{})})});
        if(!res.ok){let error='';try{error=(await res.json()).message||''}catch{}throw Error(`GitHub write failed (${res.status}): ${error}`);}
        setStatus('Synced to GitHub ✓');
      }else setStatus('GitHub notes loaded');
    }catch(err){setStatus('Sync failed');alert(err.message+'\nYour local notes are intact.');}
    finally{syncing=false;if(pendingSync){const next=pendingSync;pendingSync=false;if(next)void sync(true);}}
  }
  function queueSync(){pendingSync=true;if(!syncing){pendingSync=false;void sync(true);}}
  document.addEventListener('mouseup',e=>{if(e.target instanceof Element && e.target.closest('.selection-toolbar,.notes-rail,dialog'))return;setTimeout(selectionHandler,0)});
  document.addEventListener('keyup',e=>{if(e.key==='Shift'||e.key.startsWith('Arrow'))setTimeout(selectionHandler,0)});
  el('add-highlight').addEventListener('click',()=>{if(!selectionDraft)return;saveAnnotation({...selectionDraft,id:uid(),kind:'highlight',body:''});clearSelection();selectionDraft=null;});
  el('add-note').addEventListener('click',()=>openDialog(null));
  el('cancel-note').addEventListener('click',()=>dialog.close());
  el('note-form').addEventListener('submit',e=>{e.preventDefault();const body=el('note-body').value.trim();const a=activeEditId?annotations.find(x=>x.id===activeEditId):null;const data=a?{...a,kind:'note',body,updatedAt:now()}:{...selectionDraft,id:uid(),kind:'note',body,createdAt:now(),updatedAt:now()};if(data)saveAnnotation(data);dialog.close();selectionDraft=null;activeEditId=null;});
  document.addEventListener('click',e=>{const mark=e.target.closest('mark.reader-mark');if(mark){const a=annotations.find(x=>x.id===mark.dataset.annotationId);if(a)openDialog(a);}});
  el('connect-github').addEventListener('click',async()=>{
    const value=el('github-token').value.trim();
    const dest=el('notes-repo').value.trim();
    if(!/^(github_pat_|ghp_|gho_)/.test(value)){alert('Enter a fine-grained GitHub token with Contents read/write for the selected repository.');return;}
    if(!/^[A-Za-z0-9-]+\/[A-Za-z0-9._-]+$/.test(dest)){alert('Enter a repository as owner/repo.');return;}
    try{
      setStatus('Checking repository…');
      const res=await fetch(`https://api.github.com/repos/${dest}`,{headers:{'Accept':'application/vnd.github+json','Authorization':`Bearer ${value}`,'X-GitHub-Api-Version':'2022-11-28'}});
      if(!res.ok)throw Error(`Could not verify GitHub notes repository (${res.status}). Check token permissions.`);
      const details=await res.json();
      if(!details.private && !confirm('The selected notes repository is PUBLIC. All uploaded annotations will be public. Continue?')){setStatus('Sync not authorized');return;}
      notesRepo=dest;token=value;el('github-token').value='';
      el('disconnect-github').hidden=false;el('connect-github').textContent='Connected for this session';el('sync-details').open=false;
      setStatus(details.private?'Private repository connected':'Public repository connected');
      void sync(true);
    }catch(e){setStatus('Connection failed');alert(e.message);}
  });
  el('disconnect-github').addEventListener('click',()=>{token=null;notesRepo=repo;el('disconnect-github').hidden=true;el('connect-github').textContent='Connect & sync';setStatus('Disconnected');});
  el('sync-now').addEventListener('click',()=>void sync(Boolean(token)));
  el('show-all-notes').addEventListener('click',()=>{noteList.scrollIntoView({behavior:'smooth',block:'nearest'});});
  const mobile=el('notes-toggle');mobile?.addEventListener('click',()=>{const rail=el('reader-notes');const shown=rail.classList.toggle('is-visible');mobile.setAttribute('aria-expanded',String(shown));});
  const menu=document.querySelector('.mobile-menu');menu?.addEventListener('click',()=>{const side=el('book-sidebar');const show=side.classList.toggle('is-visible');menu.setAttribute('aria-expanded',String(show));});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'){hideToolbar();el('reader-notes')?.classList.remove('is-visible');el('book-sidebar')?.classList.remove('is-visible');}});
  annotations=readLocal();render();
  // Public repository, no authentication. Import existing GitHub notes on initial load
  // when local storage is empty; explicit Sync button remains available otherwise.
  if(!annotations.length)void sync(false);
})();