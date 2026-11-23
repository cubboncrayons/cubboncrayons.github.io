(()=>{'use strict';
const $=id=>document.getElementById(id);
const player=$('season-audio'),state=$('audio-state'),replay=$('replay-audio'),slow=$('slow-audio');
if(player){player.addEventListener('error',()=>{state.textContent='The Kannada audio is being prepared. Please try the written activity for now.'});player.addEventListener('canplay',()=>{state.textContent='Ready! Listen together and repeat after each line.'},{once:true});player.addEventListener('ended',()=>{state.textContent='Well done! Tap replay to practise again.'});replay?.addEventListener('click',()=>{if(player.error){state.textContent='Recording is currently unavailable. Please try again shortly.';return}player.currentTime=0;player.play().catch(()=>state.textContent='Tap the audio play control to start.')});slow?.addEventListener('click',()=>{let slower=slow.getAttribute('aria-pressed')!=='true';slow.setAttribute('aria-pressed',String(slower));player.playbackRate=slower?.8:1;slow.textContent=slower?'Normal speed':'0.8× slower';});}

/* Segment boundaries follow the six lines of the supplied 26-second recording.
   Audio currentTime is authoritative: pause, scrub, slow mode and replay stay synchronized. */
const seasonCues=[
  {at:0,month:'ಚೈತ್ರ · ವೈಶಾಖ',season:'ವಸಂತ ಋತು',label:'01 / 06 · SPRING',alt:'Spring blossoms'},
  {at:4.35,month:'ಜ್ಯೇಷ್ಠ · ಆಷಾಢ',season:'ಗ್ರೀಷ್ಮ ಋತು',label:'02 / 06 · SUMMER',alt:'Mangoes and summer sunshine'},
  {at:8.72,month:'ಶ್ರಾವಣ · ಭಾದ್ರಪದ',season:'ವರ್ಷ ಋತು',label:'03 / 06 · MONSOON',alt:'Monsoon rain and green fields'},
  {at:13.00,month:'ಆಶ್ವಯುಜ · ಕಾರ್ತಿಕ',season:'ಶರದೃತು',label:'04 / 06 · AUTUMN',alt:'Golden fields and clear skies'},
  {at:17.36,month:'ಮಾರ್ಗಶಿರ · ಪುಷ್ಯ',season:'ಹೇಮಂತ ಋತು',label:'05 / 06 · EARLY WINTER',alt:'Misty early winter sunrise'},
  {at:21.67,month:'ಮಾಘ · ಫಾಲ್ಗುಣ',season:'ಶಿಶಿರ ಋತು',label:'06 / 06 · LATE WINTER',alt:'Cool, pale winter fields'}
];
const stage=$('sync-stage'),landscape=$('sync-landscape'),seasonCards=[...document.querySelectorAll('.season-card')];
let lastSeason=-1;
function syncAudioScene(){
  if(!player||!stage)return;
  const elapsed=Number.isFinite(player.currentTime)?player.currentTime:0;
  const duration=Number.isFinite(player.duration)&&player.duration>0?player.duration:26;
  let active=0;
  for(let i=seasonCues.length-1;i>=0;i--){if(elapsed>=seasonCues[i].at){active=i;break}}
  if(active!==lastSeason){
    lastSeason=active;
    const s=seasonCues[active];
    stage.dataset.season=String(active);
    $('sync-months').textContent=s.month;
    $('sync-season').textContent=s.season;
    $('sync-label').textContent=s.label;
    landscape?.setAttribute('aria-label',s.alt);
  }
  const isPlaying=!player.paused&&!player.ended;
  stage.classList.toggle('is-playing',isPlaying);
  seasonCards.forEach((card,i)=>card.classList.toggle('is-speaking',isPlaying&&i===active));
  const percentage=Math.min(100,Math.max(0,elapsed/duration*100));
  $('sync-progress-fill').style.width=percentage+'%';
  $('sync-progress').setAttribute('aria-valuenow',String(Math.round(percentage)));
}
if(player&&stage){
  for(const name of ['timeupdate','play','playing','pause','seeked','seeking','loadedmetadata','ratechange','ended'])player.addEventListener(name,syncAudioScene);
  seasonCards.forEach((card,i)=>{
    const seek=()=>{
      if(player.error)return;
      player.currentTime=seasonCues[i].at;
      syncAudioScene();
      player.play().catch(()=>{state.textContent='Tap the audio play control to start.'});
    };
    card.addEventListener('click',seek);
    card.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();seek()}});
    card.setAttribute('role','button');
    card.setAttribute('aria-label',seasonCues[i].month+' — '+seasonCues[i].season+'. Play from this season.');
  });
  syncAudioScene();
}


const scenePlay=$('scene-play'),sceneLabel=$('scene-play-label');
function startScene(){
  if(!player)return;
  if(player.paused){
    if(player.ended||player.currentTime>=player.duration-.15)player.currentTime=0;
    player.play().catch(()=>{state.textContent='Press the native audio play control to start.'});
  }else{player.pause()}
}
scenePlay?.addEventListener('click',startScene);
$('hero-start')?.addEventListener('click',e=>{
  // Gesture-triggered playback happens before scrolling, including on iOS.
  if(!player)return;
  e.preventDefault();
  $('listen-title')?.scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'start'});
  player.currentTime=0;
  player.play().catch(()=>{state.textContent='Tap Play animation on the illustrated scene.'});
});
if(player){
  const refreshPlay=()=>{
    if(!scenePlay)return;
    const running=!player.paused&&!player.ended;
    scenePlay.setAttribute('aria-label',running?'Pause Kannada narration and animation':'Play Kannada narration and animation');
    scenePlay.firstChild.textContent=running?'Ⅱ ':'▶ ';
    sceneLabel.textContent=running?'Pause animation':'Play animation';
  };
  for(const evt of ['play','pause','ended','playing'])player.addEventListener(evt,refreshPlay);
  refreshPlay();
}

const questions=[{month:'ಚೈತ್ರ, ವೈಶಾಖ',answer:'ವಸಂತ ಋತು',explain:'Spring · Flowers bloom'},{month:'ಜ್ಯೇಷ್ಠ, ಆಷಾಢ',answer:'ಗ್ರೀಷ್ಮ ಋತು',explain:'Summer · Sunshine and mangoes'},{month:'ಶ್ರಾವಣ, ಭಾದ್ರಪದ',answer:'ವರ್ಷ ಋತು',explain:'Monsoon · Rainy days'},{month:'ಆಶ್ವಯುಜ, ಕಾರ್ತಿಕ',answer:'ಶರದೃತು',explain:'Autumn · Clear skies'},{month:'ಮಾರ್ಗಶಿರ, ಪುಷ್ಯ',answer:'ಹೇಮಂತ ಋತು',explain:'Early winter · Misty mornings'},{month:'ಮಾಘ, ಫಾಲ್ಗುಣ',answer:'ಶಿಶಿರ ಋತು',explain:'Late winter · Cool mornings'}];
const names=questions.map(q=>q.answer);let index=0,answered=false;
function options(q,i){return [q.answer,names[(i+2)%6],names[(i+4)%6]].sort((a,b)=>names.indexOf(a)-names.indexOf(b))}
function render(){let q=questions[index];answered=false;$('quiz-count').textContent='Question '+(index+1)+' of '+questions.length;$('quiz-prompt').textContent=q.month+' — ಯಾವ ಋತು?';$('quiz-feedback').textContent='Choose an answer together.';$('quiz-next').hidden=true;const root=$('quiz-choices');root.replaceChildren();for(const name of options(q,index)){const b=document.createElement('button');b.type='button';b.lang='kn';b.textContent=name;b.addEventListener('click',()=>choose(name,b));root.appendChild(b)}}
function choose(name,button){if(answered)return;answered=true;const q=questions[index];let correct=name===q.answer;for(const b of $('quiz-choices').children){b.disabled=true;if(b.textContent===q.answer)b.classList.add('is-correct')}if(!correct)button.classList.add('is-wrong');$('quiz-feedback').textContent=correct?'ಚೆನ್ನಾಗಿದೆ! '+q.explain:'ಒಳ್ಳೆಯ ಪ್ರಯತ್ನ! ಸರಿಯಾದ ಉತ್ತರ: '+q.answer+' · '+q.explain;$('quiz-next').hidden=false;$('quiz-next').textContent=index===questions.length-1?'Play again ↺':'Next question →';}
$('quiz-next')?.addEventListener('click',()=>{index=index===questions.length-1?0:index+1;render()});$('quiz-restart')?.addEventListener('click',()=>{index=0;render()});if($('quiz-choices'))render();
$('share-activity')?.addEventListener('click',async()=>{const url='https://cubboncrayons.github.io/purochi.html';const title='ಪುರೋಚಿ · ಕನ್ನಡ ತಿಂಗಳುಗಳು ಮತ್ತು ಋತುಗಳು';try{if(navigator.share){await navigator.share({title,text:'A free Kannada family recitation from Cubbon Crayons',url});$('share-status').textContent='Thanks for sharing!';return}if(navigator.clipboard?.writeText){await navigator.clipboard.writeText(url);$('share-status').textContent='Activity link copied. Share it with your family!';return}throw Error('Unavailable')}catch(e){if(e.name==='AbortError')return;$('share-status').textContent='Share this link: '+url;}});
})();