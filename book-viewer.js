'use strict';
const previewPages = {"umbrella": [{"src": "assets/previews/umbrella-01.webp", "label": "Cover · page 1", "width": 1400, "height": 1980}, {"src": "assets/previews/umbrella-02.webp", "label": "Story page · page 2", "width": 1400, "height": 1980}, {"src": "assets/previews/umbrella-06.webp", "label": "Tracing activity · page 6", "width": 1400, "height": 1980}], "park": [{"src": "assets/previews/park-01.webp", "label": "Cover · page 1", "width": 1400, "height": 1982}, {"src": "assets/previews/park-02.webp", "label": "Story page · page 2", "width": 1400, "height": 1982}, {"src": "assets/previews/park-04.webp", "label": "Tracing activity · page 4", "width": 1400, "height": 1982}], "amma": [{"src": "assets/previews/amma-01.webp", "label": "Cover · page 1", "width": 1400, "height": 1980}, {"src": "assets/previews/amma-03.webp", "label": "Story page · page 3", "width": 1400, "height": 1980}, {"src": "assets/previews/amma-06.webp", "label": "Tracing activity · page 6", "width": 1400, "height": 1982}], "idli": [{"src": "assets/previews/idli-01.webp", "label": "Cover · page 1", "width": 1400, "height": 1980}, {"src": "assets/previews/idli-03.webp", "label": "Story page · page 3", "width": 1400, "height": 1980}, {"src": "assets/previews/idli-04.webp", "label": "Tracing activity · page 4", "width": 1400, "height": 1980}], "ajja": [{"src": "assets/previews/ajja-01.webp", "label": "Cover · page 1", "width": 1400, "height": 1980}, {"src": "assets/previews/ajja-02.webp", "label": "Story page · page 2", "width": 1400, "height": 1980}, {"src": "assets/previews/ajja-04.webp", "label": "Tracing activity · page 4", "width": 1400, "height": 1980}]};
const dialog = document.querySelector('#book-viewer');
const pageTrack = document.querySelector('#viewer-pages');
const controls = document.querySelector('.viewer-controls');
const thumbnails = document.querySelector('#viewer-thumbnails');
const previous = document.querySelector('#viewer-previous');
const next = document.querySelector('#viewer-next');
const caption = document.querySelector('#viewer-caption');
const enlarge = document.querySelector('#viewer-enlarge');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
let pages = [], current = 0, trigger = null, scrollFrame = 0;

function updatePosition(index) {
  current = Math.max(0, Math.min(pages.length - 1, index));
  document.querySelector('#viewer-position').textContent = (current + 1) + ' of ' + pages.length;
  caption.textContent = pages[current].label;
  enlarge.href = pages[current].src;
  previous.disabled = current === 0;
  next.disabled = current === pages.length - 1;
  for (const [i, button] of [...thumbnails.children].entries()) {
    button.setAttribute('aria-current', String(i === current));
  }
}
function moveTo(index) {
  const destination = Math.max(0, Math.min(pages.length - 1, index));
  pageTrack.scrollTo({
    left: destination * pageTrack.clientWidth,
    behavior: reducedMotion.matches ? 'auto' : 'smooth'
  });
  updatePosition(destination);
}

if (dialog && typeof dialog.showModal === 'function') {
  for (const link of document.querySelectorAll('[data-preview]')) {
    link.setAttribute('aria-haspopup', 'dialog');
    link.addEventListener('click', event => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button !== 0) return;
      const card = link.closest('.card');
      const selected = previewPages[link.dataset.preview];
      if (!selected || !selected.length) return;
      event.preventDefault();
      trigger = link;
      pages = selected;
      const title = card.querySelector('h3').textContent;
      document.querySelector('#viewer-title').textContent = title;
      document.querySelector('#viewer-theme').textContent = card.querySelector('.tag').textContent;
      document.querySelector('#viewer-description').textContent = card.querySelector('.description').textContent;
      document.querySelector('#viewer-format').textContent = card.querySelector('.card-bottom > span').textContent;
      document.querySelector('#viewer-buy').href = card.querySelector('.card-buy').href;
      pageTrack.replaceChildren();
      thumbnails.replaceChildren();
      pages.forEach((page, i) => {
        const figure = document.createElement('figure');
        figure.className = 'viewer-slide';
        const image = document.createElement('img');
        image.src = page.src;
        image.alt = title + ' — ' + page.label;
        image.width = page.width;
        image.height = page.height;
        image.decoding = 'async';
        if (i > 0) image.loading = 'lazy';
        const error = document.createElement('p');
        error.className = 'viewer-image-error';
        error.hidden = true;
        error.textContent = 'This preview image could not load. Please close and try again.';
        image.addEventListener('error', () => { image.hidden = true; error.hidden = false; });
        figure.append(image, error);
        pageTrack.append(figure);
        const button = document.createElement('button');
        button.type = 'button';
        button.setAttribute('aria-label', 'Show ' + page.label + ', preview ' + (i + 1));
        const thumb = document.createElement('img');
        thumb.src = page.src;
        thumb.alt = '';
        thumb.width = 50;
        thumb.height = 71;
        button.append(thumb);
        button.addEventListener('click', () => moveTo(i));
        thumbnails.append(button);
      });
      controls.hidden = pages.length < 2;
      thumbnails.hidden = pages.length < 2;
      pageTrack.setAttribute('aria-label', pages.length > 1 ? 'Preview pages. Swipe sideways or use the page buttons.' : 'Selected original PDF pages');
      updatePosition(0);
      dialog.showModal();
      document.documentElement.classList.add('preview-open');
      requestAnimationFrame(() => { pageTrack.scrollTo({left: 0, behavior: 'auto'}); updatePosition(0); });
    });
  }
  dialog.querySelector('.viewer-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('close', () => {
    document.documentElement.classList.remove('preview-open');
    if (trigger) trigger.focus();
  });
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const rect = dialog.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
  });
  pageTrack.addEventListener('keydown', event => {
    if (pages.length < 2) return;
    if (event.key === 'ArrowRight') { event.preventDefault(); moveTo(current + 1); }
    if (event.key === 'ArrowLeft') { event.preventDefault(); moveTo(current - 1); }
    if (event.key === 'Home') { event.preventDefault(); moveTo(0); }
    if (event.key === 'End') { event.preventDefault(); moveTo(pages.length - 1); }
  });
  previous.addEventListener('click', () => moveTo(current - 1));
  next.addEventListener('click', () => moveTo(current + 1));
  pageTrack.addEventListener('scroll', () => {
    if (scrollFrame) return;
    scrollFrame = requestAnimationFrame(() => {
      if (pages.length && pageTrack.clientWidth) updatePosition(Math.round(pageTrack.scrollLeft / pageTrack.clientWidth));
      scrollFrame = 0;
    });
  }, { passive: true });
  window.addEventListener('resize', () => {
    if (dialog.open) pageTrack.scrollTo({left: current * pageTrack.clientWidth, behavior: 'auto'});
  });
}
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
