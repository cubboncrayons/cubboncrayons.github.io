(()=>{'use strict';
const menu=document.getElementById('activities-menu-toggle'),nav=document.getElementById('activities-site-nav');
function closeMenu(){nav?.classList.remove('is-open');menu?.setAttribute('aria-expanded','false');menu?.setAttribute('aria-label','Open site menu')}
menu?.addEventListener('click',()=>{const open=!nav.classList.contains('is-open');nav.classList.toggle('is-open',open);menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close site menu':'Open site menu')});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeMenu()});document.addEventListener('click',e=>{if(nav&&!nav.contains(e.target)&&!menu?.contains(e.target))closeMenu()});
nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
const ageButtons=[...document.querySelectorAll('[data-age]')],items=[...document.querySelectorAll('.activity-item')],planned=[...document.querySelectorAll('.upcoming-list li')];
const context=document.getElementById('collection-context'),clear=document.getElementById('clear-category'),empty=document.getElementById('activity-empty'),upEmpty=document.getElementById('upcoming-empty');
const allowed=['parents','grandparents','family-games'];const labels={parents:'With Parents',grandparents:'With Grandparents','family-games':'Family Games'};
let age='all',guide='all';
function matches(el){return (guide==='all'||el.dataset.category===guide)&&(age==='all'||el.dataset.ages.split(' ').includes(age))}
function update(){let shown=0,soon=0;items.forEach(el=>{el.hidden=!matches(el);if(!el.hidden)shown++});planned.forEach(el=>{el.hidden=!matches(el);if(!el.hidden)soon++});
ageButtons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.age===age)));context.textContent=guide==='all'?'All family activities':labels[guide];clear.hidden=guide==='all';empty.hidden=shown!==0;upEmpty.hidden=soon!==0;}
function filterCategory(v){guide=allowed.includes(v)?v:'all';update()}
ageButtons.forEach(b=>b.addEventListener('click',()=>{age=b.dataset.age;update()}));
clear?.addEventListener('click',()=>{guide='all';if(location.hash)history.replaceState(null,'',location.pathname+location.search);update()});
document.querySelectorAll('[data-collection-link]').forEach(link=>link.addEventListener('click',()=>{filterCategory(link.dataset.collectionLink);const target=link.dataset.collectionLink==='family-games'?'family-games':'discover';requestAnimationFrame(()=>document.getElementById(target)?.scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'}))}));
function handleHash(){const v=location.hash.slice(1);if(allowed.includes(v)){filterCategory(v)}else if(!location.hash){filterCategory('all')}}
window.addEventListener('hashchange',handleHash);handleHash();update();
})();