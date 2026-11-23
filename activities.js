(()=>{'use strict';
const groupButtons=[...document.querySelectorAll('[data-guide]')];
const ageButtons=[...document.querySelectorAll('[data-age]')];
const items=[...document.querySelectorAll('.activity-item[data-category]')];
const groups=[...document.querySelectorAll('.activity-group[data-group]')];
const count=document.getElementById('activity-count');
const empty=document.getElementById('activity-empty');
let guide='all',age='all';
function apply(){
 let visibleTotal=0;
 for(const item of items){
  const show=(guide==='all'||item.dataset.category===guide)&&(age==='all'||item.dataset.ages.split(' ').includes(age));
  item.hidden=!show;if(show)visibleTotal++;
 }
 for(const group of groups)group.hidden=![...group.querySelectorAll('.activity-item')].some(item=>!item.hidden);
 groupButtons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.guide===guide)));
 ageButtons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.age===age)));
 count.textContent=visibleTotal===0?'No matching activities':visibleTotal+' activities and upcoming ideas';
 empty.hidden=visibleTotal!==0;
}
groupButtons.forEach(b=>b.addEventListener('click',()=>{guide=b.dataset.guide;apply()}));
ageButtons.forEach(b=>b.addEventListener('click',()=>{age=b.dataset.age;apply()}));
document.querySelectorAll('[data-collection-link]').forEach(a=>a.addEventListener('click',()=>{guide=a.dataset.collectionLink;apply()}));
const anchors={'#parents':'parents','#grandparents':'grandparents','#family-games':'family-games'};
function useAnchor(){if(anchors[location.hash]){guide=anchors[location.hash];apply()}}
window.addEventListener('hashchange',useAnchor);
useAnchor();apply();
})();
// Family category navigation and age filtering.
