'use strict';
(()=>{
 const dialog=document.querySelector('.reading-room'),image=document.querySelector('#reading-page'),pane=document.querySelector('.reading-pane'),zoom=document.querySelector('[data-read-zoom]');
 let index=0,pages=[],opener=null;
 function show(i){
  index=Math.max(0,Math.min(pages.length-1,i));
  const link=pages[index],source=link.querySelector('img');
  image.src=link.href;image.alt=source.alt;image.width=source.width;image.height=source.height;
  document.querySelector('#reading-title').textContent=document.querySelector('#sample-title').textContent;
  document.querySelector('#reading-caption').textContent=link.closest('figure').querySelector('figcaption').textContent+' · '+(index+1)+' of '+pages.length;
  document.querySelector('[data-read-prev]').disabled=index===0;document.querySelector('[data-read-next]').disabled=index===pages.length-1;
  pane.classList.remove('zoomed');zoom.textContent='Zoom in';zoom.setAttribute('aria-pressed','false');pane.scrollTo(0,0);
 }
 document.querySelector('.sample-track').addEventListener('click',e=>{
  const a=e.target.closest('a');if(!a||!dialog.showModal)return;
  e.preventDefault();pages=[...document.querySelectorAll('.sample-page a')];opener=a;
  if(document.querySelector('#sample-play').getAttribute('aria-pressed')==='true')document.querySelector('#sample-play').click();
  show(pages.indexOf(a));dialog.showModal();
 });
 document.querySelector('[data-read-close]').addEventListener('click',()=>dialog.close());
 dialog.addEventListener('close',()=>opener?.focus({preventScroll:true}));
 document.querySelector('[data-read-prev]').addEventListener('click',()=>show(index-1));
 document.querySelector('[data-read-next]').addEventListener('click',()=>show(index+1));
 zoom.addEventListener('click',()=>{
  const active=pane.classList.toggle('zoomed');zoom.textContent=active?'Fit page':'Zoom in';zoom.setAttribute('aria-pressed',String(active));pane.scrollTo(0,0);
 });
 dialog.addEventListener('keydown',e=>{
  if(e.target===pane&&pane.classList.contains('zoomed'))return;
  if(e.key==='ArrowRight'){e.preventDefault();show(index+1);}
  if(e.key==='ArrowLeft'){e.preventDefault();show(index-1);}
 });
 document.querySelectorAll('[data-preview-book]').forEach(a=>a.addEventListener('click',()=>{
  document.querySelector('[data-book="'+a.dataset.previewBook+'"]').click();
 }));
})();