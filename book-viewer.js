'use strict';
const previewPages = {"umbrella":[{"src":"assets/previews/umbrella-01.webp","label":"Cover · page 1","width":1400,"height":1980},{"src":"assets/previews/umbrella-02.webp","label":"Story page · page 2","width":1400,"height":1980},{"src":"assets/previews/umbrella-06.webp","label":"Tracing activity · page 6","width":1400,"height":1980}],"park":[{"src":"assets/previews/park-01.webp","label":"Cover · page 1","width":1400,"height":1982},{"src":"assets/previews/park-02.webp","label":"Story page · page 2","width":1400,"height":1982},{"src":"assets/previews/park-04.webp","label":"Tracing activity · page 4","width":1400,"height":1982}],"amma":[{"src":"assets/previews/amma-01.webp","label":"Cover · page 1","width":1400,"height":1980},{"src":"assets/previews/amma-03.webp","label":"Story page · page 3","width":1400,"height":1980},{"src":"assets/previews/amma-06.webp","label":"Tracing activity · page 6","width":1400,"height":1982}],"idli":[{"src":"assets/previews/idli-01.webp","label":"Cover · page 1","width":1400,"height":1980},{"src":"assets/previews/idli-03.webp","label":"Story page · page 3","width":1400,"height":1980},{"src":"assets/previews/idli-04.webp","label":"Tracing activity · page 4","width":1400,"height":1980}],"ajja":[{"src":"assets/previews/ajja-01.webp","label":"Cover · page 1","width":1400,"height":1980},{"src":"assets/previews/ajja-02.webp","label":"Story page · page 2","width":1400,"height":1980},{"src":"assets/previews/ajja-04.webp","label":"Tracing activity · page 4","width":1400,"height":1980}]};
(() => {
 const area=document.querySelector('.inline-preview'),track=document.querySelector('.sample-track'),chooser=document.querySelector('.preview-books');
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 const play=document.querySelector('#sample-play');
 let current=0,playing=!reduced.matches,visible=false,hovered=false;
 const dots=document.querySelector('.sample-dots');
 dots.hidden=false;
 dots.addEventListener('click',e=>{const button=e.target.closest('[data-slide]');if(button)move(Number(button.dataset.slide));});
 function frames(){return [...track.children];}
 function update(i){
  current=Math.max(0,Math.min(2,i));
  document.querySelector('#sample-position').textContent=(current+1)+' of 3';
  
  for(const dot of dots.querySelectorAll('button')){if(Number(dot.dataset.slide)===current)dot.setAttribute('aria-current','true');else dot.removeAttribute('aria-current');}
 }
 function move(i,auto=false){
  const page=frames()[i];if(!page)return;
  if(!auto)pause();
  track.scrollTo({left:page.offsetLeft-track.firstElementChild.offsetLeft,behavior:reduced.matches?'auto':'smooth'});update(i);
 }
 function pause(){document.querySelector('#sample-position').setAttribute('aria-live','polite');playing=false;play.textContent='Play';play.setAttribute('aria-label','Play page slideshow');play.setAttribute('aria-pressed','false');}
 play.addEventListener('click',()=>{playing=!playing;document.querySelector('#sample-position').setAttribute('aria-live',playing?'off':'polite');play.textContent=playing?'Pause':'Play';play.setAttribute('aria-label',playing?'Pause page slideshow':'Play page slideshow');play.setAttribute('aria-pressed',String(playing));});
 chooser.hidden=false;document.querySelector('.sample-controls').hidden=false;
 if(reduced.matches)pause();
 chooser.addEventListener('click',e=>{
  const button=e.target.closest('[data-book]');if(!button)return;
  const key=button.dataset.book,card=document.querySelector('[data-product="'+key+'"]'),title=card.querySelector('h3').textContent;
  for(const b of chooser.querySelectorAll('button'))b.setAttribute('aria-pressed',String(b===button));
  document.querySelector('#sample-title').textContent=title;
  document.querySelector('#sample-format').textContent=card.querySelector('.card-bottom>span').textContent;
  document.querySelector('#sample-buy').href=card.querySelector('.card-buy').href;
  document.querySelector('#sample-buy').setAttribute('aria-label','Buy '+title+' for 49 rupees');
  track.replaceChildren(...previewPages[key].map(p=>{
   const fig=document.createElement('figure');fig.className='sample-page';
   const link=document.createElement('a');link.href=p.src;link.target='_blank';link.rel='noopener';link.setAttribute('aria-label','Open '+p.label+' at full size');
   const img=document.createElement('img');img.src=p.src;img.width=p.width;img.height=p.height;img.alt=title+' — '+p.label;img.loading='lazy';
   const cap=document.createElement('figcaption');cap.textContent=p.label;link.append(img);fig.append(link,cap);return fig;
  }));
  track.scrollTo({left:0,behavior:'auto'});update(0);
  if(!reduced.matches&&track.animate)track.animate([{opacity:.4,transform:'translateY(8px)'},{opacity:1,transform:'none'}],{duration:400,easing:'ease-out'});
 });
 
 // Deep-link a specific product preview from activities or parenting articles.
 const requestedPreview=new URLSearchParams(location.search).get('preview');
 if(requestedPreview&&Object.prototype.hasOwnProperty.call(previewPages,requestedPreview)){
   const target=chooser.querySelector('[data-book="'+requestedPreview+'"]');
   if(target)target.click();
 }
 track.addEventListener('pointerdown',pause,{passive:true});
 track.addEventListener('keydown',e=>{if(e.key==='ArrowRight'){e.preventDefault();move(Math.min(2,current+1));}if(e.key==='ArrowLeft'){e.preventDefault();move(Math.max(0,current-1));}});
 track.addEventListener('scroll',()=>{
  const first=track.firstElementChild;const index=frames().reduce((best,p,i)=>Math.abs(p.offsetLeft-first.offsetLeft-track.scrollLeft)<Math.abs(frames()[best].offsetLeft-first.offsetLeft-track.scrollLeft)?i:best,0);update(index);
 },{passive:true});
 area.addEventListener('pointerenter',e=>{if(e.pointerType==='mouse')hovered=true;});area.addEventListener('pointerleave',()=>hovered=false);
 if('IntersectionObserver' in window)new IntersectionObserver(e=>visible=e[0].isIntersecting,{threshold:.2}).observe(track);
 setInterval(()=>{if(playing&&visible&&!hovered&&!document.hidden&&!reduced.matches&&!area.querySelector(':focus-visible'))move((current+1)%3,true);},5000);
 reduced.addEventListener('change',()=>{if(reduced.matches)pause();});
 document.querySelector('#sample-position').setAttribute('aria-live',playing?'off':'polite');update(0);
})();
const filterBar = document.querySelector('.story-filters');
if (filterBar) {
  const cards = [...document.querySelectorAll('.card')];
  filterBar.hidden = false;
  for (const button of filterBar.querySelectorAll('button')) {
    button.addEventListener('click', () => {
      let count = 0;
      for (const card of cards) {
        card.hidden = button.dataset.filter !== 'all' && card.dataset.theme !== button.dataset.filter;
        if (!card.hidden) count++;
      }
      for (const other of filterBar.querySelectorAll('button')) other.setAttribute('aria-pressed', String(other === button));
      document.querySelector('#filter-status').textContent = count + (count === 1 ? ' story shown' : ' stories shown');
    });
  }
}
