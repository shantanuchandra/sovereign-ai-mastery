// The book's navigation is progressively enhanced; all links are plain HTML.
(()=>{'use strict';
  const links=[...document.querySelectorAll('.toc-chapter')];
  document.querySelectorAll('.toc-part').forEach(part=>{
    part.addEventListener('toggle',()=>{if(part.open)part.scrollIntoView({block:'nearest'});});
  });
  // Auto-expand the relevant section when a reader navigates to an indexed module.
  const hash=location.hash.match(/^#module-(\d{2})$/);
  if(hash){const n=Number(hash[1]);const group=links.find(x=>x.getAttribute('href')?.endsWith(`#module-${hash[1]}`))?.closest('.toc-part');if(group)group.open=true;}
})();