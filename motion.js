'use strict';
(() => {
  const preference = matchMedia('(prefers-reduced-motion: reduce)');
  const hero = document.querySelector('.hero');
  const toggle = document.querySelector('.motion-toggle');
  const running = new Set();
  let userPaused = false, heroVisible = true;
  function syncHero() {
    if (hero) hero.classList.toggle('motion-paused', userPaused || !heroVisible || document.hidden || preference.matches);
  }
  function play(element, frames, options) {
    if (preference.matches || !element.animate) return;
    const animation = element.animate(frames, options);
    running.add(animation);
    animation.finished.catch(() => {}).finally(() => running.delete(animation));
  }
  if (toggle && hero) {
    toggle.hidden = false;
    toggle.addEventListener('click', () => {
      userPaused = !userPaused;
      toggle.setAttribute('aria-pressed', String(userPaused));
      toggle.textContent = userPaused ? 'Play book animation' : 'Pause book animation';
      syncHero();
    });
  }
  document.addEventListener('visibilitychange', syncHero);
  preference.addEventListener('change', () => {
    if (preference.matches) for (const animation of running) animation.cancel();
    syncHero();
  });
  if ('IntersectionObserver' in window) {
    if (hero) new IntersectionObserver(entries => {
      heroVisible = entries[0].isIntersecting;
      syncHero();
    }, {threshold: 0}).observe(hero);
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        observer.unobserve(entry.target);
        entry.target.classList.add('trace-visible');
        const siblings = [...entry.target.parentElement.children];
        const stagger = Math.min(siblings.indexOf(entry.target), 3) * 65;
        play(entry.target, [
          {opacity: 0, transform: 'translateY(12px)'},
          {opacity: 1, transform: 'translateY(0)'}
        ], {duration: 480, delay: Math.min(stagger, 120), easing: 'cubic-bezier(.2,.7,.2,1)'});
      });
    }, {threshold: .08});
    document.querySelectorAll('.card, .benefits article, .how-list li, .founder-note, .section-heading, .preview-summary').forEach(element => observer.observe(element));
  } else {
    document.querySelectorAll('.benefits article').forEach(element => element.classList.add('trace-visible'));
  }
  const filters = document.querySelector('.story-filters');
  if (filters) {
    let before = new Map();
    filters.addEventListener('click', event => {
      if (!event.target.closest('[data-filter]')) return;
      before = new Map([...document.querySelectorAll('.card:not([hidden])')].map(card => [card,card.getBoundingClientRect()]));
    }, true);
    filters.addEventListener('click', event => {
      if (!event.target.closest('[data-filter]') || preference.matches) return;
      for (const card of document.querySelectorAll('.card:not([hidden])')) {
        for (const animation of card.getAnimations()) animation.cancel();
        const old = before.get(card), current = card.getBoundingClientRect();
        play(card, [
          {opacity: old ? 1 : 0, transform: old ? 'translate('+(old.left-current.left)+'px,'+(old.top-current.top)+'px)' : 'translateY(10px)'},
          {opacity:1, transform:'translate(0,0)'}
        ], {duration:320, easing:'cubic-bezier(.2,.7,.2,1)'});
      }
    });
  }
  document.querySelectorAll('.faq-list details').forEach(detail => detail.addEventListener('toggle', () => {
    const content=detail.querySelector('p');
    if(detail.open && content)play(content,[{opacity:0,transform:'translateY(-6px)'},{opacity:1,transform:'none'}],{duration:260,easing:'ease-out'});
  }));
  document.querySelectorAll('.hero-copy .eyebrow, .hero-copy h1, .hero-copy .parent-moment, .hero-copy .intro, .hero-actions').forEach((element,i) => {
    play(element,[{opacity:0,transform:'translateY(14px)'},{opacity:1,transform:'none'}],{duration:460,delay:i*55,easing:'cubic-bezier(.2,.7,.2,1)',fill:'backwards'});
  });
  // Small desktop-only depth response; no perpetual JavaScript animation loop.
  const stage=document.querySelector('.book-stage');
  const fine=matchMedia('(hover: hover) and (pointer: fine)');
  let pointerFrame=0;
  function resetDepth(){stage?.style.removeProperty('--book-y');stage?.style.removeProperty('--book-x');}
  stage?.addEventListener('pointermove',event=>{
    if(preference.matches||!fine.matches||userPaused||document.hidden)return;
    if(pointerFrame)cancelAnimationFrame(pointerFrame);
    pointerFrame=requestAnimationFrame(()=>{
      const rect=stage.getBoundingClientRect();
      stage.style.setProperty('--book-y',(((event.clientX-rect.left)/rect.width-.5)*5).toFixed(2)+'deg');
      stage.style.setProperty('--book-x',(-((event.clientY-rect.top)/rect.height-.5)*3).toFixed(2)+'deg');
      pointerFrame=0;
    });
  },{passive:true});
  stage?.addEventListener('pointerleave',resetDepth);
  preference.addEventListener('change',resetDepth);
  toggle?.addEventListener('click',resetDepth);
  document.addEventListener('visibilitychange',()=>{if(document.hidden)resetDepth();});
  const reader=document.querySelector('.reading-room'),page=document.querySelector('#reading-page');
  if(reader){
    reader.addEventListener('toggle',()=>{
      if(reader.open)play(reader,[{opacity:.5,transform:'translateY(10px) scale(.985)'},{opacity:1,transform:'none'}],{duration:240,easing:'cubic-bezier(.2,.7,.2,1)'});
    });
    page?.addEventListener('load',()=>{
      if(reader.open)play(page,[{opacity:.45},{opacity:1}],{duration:220,easing:'ease-out'});
    });
  }
  syncHero();
})();
