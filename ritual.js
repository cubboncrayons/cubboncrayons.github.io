'use strict';
(() => {
 const buttons=[...document.querySelectorAll('[data-ritual]')],image=document.querySelector('#ritual-image'),link=document.querySelector('#ritual-enlarge'),caption=document.querySelector('#ritual-caption'),focus=document.querySelector('.prompt-focus'),note=document.querySelector('.ritual-mobile-note');
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 const pages=[
  {src:'assets/previews/umbrella-02.webp',alt:'Original story page from Appi and the Little Blue Umbrella',caption:'Read · Original story page'},
  {src:'assets/previews/umbrella-02.webp',alt:'Original story page with its parent-prompt area highlighted',caption:'Talk · Notice the parent prompt'},
  {src:'assets/previews/umbrella-06.webp',alt:'Original umbrella tracing activity with its dotted paths',caption:'Trace · Original activity page'}
 ];
 let active=0;
 function select(i){
  if(!pages[i])return;
  const changed=active!==i;active=i;
  buttons.forEach((b,j)=>b.setAttribute('aria-pressed',String(i===j)));
  image.src=pages[i].src;image.alt=pages[i].alt;link.href=pages[i].src;
  caption.textContent=pages[i].caption;focus.hidden=i!==1;note.textContent=buttons[i].querySelector('.demo-copy').textContent;
  if(changed&&!reduced.matches&&image.animate)image.animate([{opacity:.35,transform:'translateY(8px)'},{opacity:1,transform:'none'}],{duration:420,easing:'ease-out'});
 }
 buttons.forEach((b,i)=>b.addEventListener('click',()=>select(i)));
 if('IntersectionObserver' in window){
  const observer=new IntersectionObserver(entries=>{
   if(!matchMedia('(min-width: 901px)').matches)return;
   const candidate=entries.filter(e=>e.isIntersecting).sort((a,b)=>Math.abs(a.boundingClientRect.top-innerHeight*.45)-Math.abs(b.boundingClientRect.top-innerHeight*.45))[0];
   if(candidate)select(Number(candidate.target.dataset.ritual));
  },{rootMargin:'-20% 0px -25% 0px',threshold:[.25,.6]});
  buttons.forEach(b=>observer.observe(b));
 }
 select(0);
})();
