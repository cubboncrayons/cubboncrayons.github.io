(()=>{'use strict';
const header=document.querySelector('.site-header'),nav=header?.querySelector('nav[aria-label="Main navigation"]');
if(!header||!nav||header.classList.contains('activities-header'))return;
const isKn=document.documentElement.lang==='kn',items=[
{href:'/#stories',text:isKn?'ಕಥೆಗಳು':'Stories'},
{href:'/activities.html',text:isKn?'ಚಟುವಟಿಕೆಗಳು':'Activities'},
{href:isKn?'/parent-corner-kannada.html':'/parent-corner.html',text:isKn?'ಪೋಷಕರಿಗಾಗಿ':'Parent Corner'},
{href:'/#our-story',text:isKn?'ನಮ್ಮ ಬಗ್ಗೆ':'Our story'}
];
for(const item of items){
 let link=[...nav.querySelectorAll('a')].find(a=>a.getAttribute('href')===item.href);
 if(!link){link=document.createElement('a');link.href=item.href;link.textContent=item.text}
 nav.appendChild(link); // Reorder the same existing links consistently; preserve aria-current and data attributes.
}
const btn=document.createElement('button');btn.type='button';btn.className='cc-menu-toggle';btn.setAttribute('aria-expanded','false');btn.setAttribute('aria-label',isKn?'ಮೆನು ತೆರೆಯಿರಿ':'Open navigation menu');
btn.innerHTML='<span aria-hidden="true">☰</span> <span>'+(isKn?'ಮೆನು':'Menu')+'</span>';
const navId='cc-main-nav';nav.id=navId;btn.setAttribute('aria-controls',navId);header.insertBefore(btn,nav);
function close(){nav.classList.remove('cc-open');btn.setAttribute('aria-expanded','false');btn.setAttribute('aria-label',isKn?'ಮೆನು ತೆರೆಯಿರಿ':'Open navigation menu')}
btn.addEventListener('click',()=>{const open=!nav.classList.contains('cc-open');nav.classList.toggle('cc-open',open);btn.setAttribute('aria-expanded',String(open));btn.setAttribute('aria-label',open?(isKn?'ಮೆನು ಮುಚ್ಚಿರಿ':'Close navigation menu'):(isKn?'ಮೆನು ತೆರೆಯಿರಿ':'Open navigation menu'))});
nav.addEventListener('click',e=>{if(e.target.closest('a'))close()});
document.addEventListener('click',e=>{if(!header.contains(e.target))close()});document.addEventListener('keydown',e=>{if(e.key==='Escape')close()});
})();