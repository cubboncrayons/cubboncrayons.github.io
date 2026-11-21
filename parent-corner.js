'use strict';
(() => {
 const hubs={en:'/parent-corner.html',kn:'/parent-corner-kannada.html'};
 let saved=null;
 try{saved=localStorage.getItem('cc-parent-language');}catch{}
 if(hubs[saved])document.querySelectorAll('[data-parent-corner]').forEach(a=>a.href=hubs[saved]);
 document.querySelectorAll('[data-reading-language]').forEach(a=>a.addEventListener('click',()=>{
  try{localStorage.setItem('cc-parent-language',a.dataset.readingLanguage);}catch{}
 }));
 // Story links from the article open the matching existing three-page preview.
 const key=new URLSearchParams(location.search).get('preview');
 const choice=[...document.querySelectorAll('[data-book]')].find(b=>b.dataset.book===key);
 if(choice)choice.click();
})();
