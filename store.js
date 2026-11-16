const filters = document.querySelector('#story-filters');
const filterButtons = [...filters.querySelectorAll('button')];
const cards = [...document.querySelectorAll('#story-list .card')];
const resultStatus = document.querySelector('#filter-status');

function setFilter(theme, announce = true) {
  let visible = 0;

  for (const card of cards) {
    card.hidden = theme !== 'all' && card.dataset.theme !== theme;
    visible += Number(!card.hidden);
  }
  for (const button of filterButtons) {
    button.setAttribute('aria-pressed', String(button.dataset.filter === theme));
  }
  if (announce) resultStatus.textContent = `${visible} stories shown`;
}

for (const button of filterButtons) {
  button.addEventListener('click', () => setFilter(button.dataset.filter));
}
filters.hidden = false;

function revealLinkedStory() {
  const linkedCard = cards.find(card => `#${card.id}` === window.location.hash);
  if (linkedCard?.hidden) {
    setFilter('all');
    linkedCard.scrollIntoView({ block: 'start' });
  }
}
window.addEventListener('hashchange', revealLinkedStory);

const dialog = document.querySelector('#sample-dialog');
const previewImage = document.querySelector('#sample-image');
const previewTitle = document.querySelector('#sample-title');
const previewCaption = document.querySelector('#sample-caption');
const fullImageLink = document.querySelector('#sample-full');
let previewTrigger;

if (typeof dialog.showModal === 'function') {
  for (const link of document.querySelectorAll('.preview')) {
    link.setAttribute('aria-haspopup', 'dialog');
    link.addEventListener('click', event => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;

      event.preventDefault();
      previewTrigger = link;
      previewTitle.textContent = link.closest('.card').querySelector('h3').textContent;
      previewImage.alt = link.dataset.caption;
      previewImage.src = link.href;
      previewCaption.textContent = link.dataset.caption;
      fullImageLink.href = link.href;
      dialog.showModal();
      dialog.scrollTop = 0;
    });
  }
  dialog.querySelector('.sample-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('close', () => previewTrigger?.focus());
}
