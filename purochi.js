(()=>{'use strict';
const $=id=>document.getElementById(id);
const player=$('season-audio'),state=$('audio-state'),replay=$('replay-audio'),slow=$('slow-audio');
if(player){player.addEventListener('error',()=>{state.textContent='The Kannada audio is being prepared. Please try the written activity for now.'});player.addEventListener('canplay',()=>{state.textContent='Ready! Listen together and repeat after each line.'},{once:true});player.addEventListener('ended',()=>{state.textContent='Well done! Tap replay to practise again.'});replay?.addEventListener('click',()=>{if(player.error){state.textContent='Recording is currently unavailable. Please try again shortly.';return}player.currentTime=0;player.play().catch(()=>state.textContent='Tap the audio play control to start.')});slow?.addEventListener('click',()=>{let slower=slow.getAttribute('aria-pressed')!=='true';slow.setAttribute('aria-pressed',String(slower));player.playbackRate=slower?.8:1;slow.textContent=slower?'Normal speed':'0.8× slower';});}

/* Segment boundaries follow the six lines of the supplied 26-second recording.
   Audio currentTime is authoritative: pause, scrub, slow mode and replay stay synchronized. */
const seasonCues=[
  {at:0,month:'ಚೈತ್ರ · ವೈಶಾಖ',season:'ವಸಂತ ಋತು',label:'01 / 06 · SPRING',alt:'Spring blossoms',scene:'🌸 Flowers bloom in spring',words:['ಚೈತ್ರ','ವೈಶಾಖ','ವಸಂತ','ಋತು'],offsets:[0.34,1.36,2.78,3.54]},
  {at:4.35,month:'ಜ್ಯೇಷ್ಠ · ಆಷಾಢ',season:'ಗ್ರೀಷ್ಮ ಋತು',label:'02 / 06 · SUMMER',alt:'Mangoes and summer sunshine',scene:'☀️ Sunshine and mangoes in summer',words:['ಜ್ಯೇಷ್ಠ','ಆಷಾಢ','ಗ್ರೀಷ್ಮ','ಋತು'],offsets:[0.43,1.48,2.84,3.47]},
  {at:8.72,month:'ಶ್ರಾವಣ · ಭಾದ್ರಪದ',season:'ವರ್ಷ ಋತು',label:'03 / 06 · MONSOON',alt:'Monsoon rain and green fields',scene:'🌧️ Rainfall across the green fields',words:['ಶ್ರಾವಣ','ಭಾದ್ರಪದ','ವರ್ಷ','ಋತು'],offsets:[0.42,1.52,2.86,3.48]},
  {at:13.00,month:'ಆಶ್ವಯುಜ · ಕಾರ್ತಿಕ',season:'ಶರದೃತು',label:'04 / 06 · AUTUMN',alt:'Golden fields and clear skies',scene:'🍂 Leaves drift in the autumn breeze',words:['ಆಶ್ವಯುಜ','ಕಾರ್ತಿಕ','ಶರದೃತು'],offsets:[0.43,1.53,2.92]},
  {at:17.36,month:'ಮಾರ್ಗಶಿರ · ಪುಷ್ಯ',season:'ಹೇಮಂತ ಋತು',label:'05 / 06 · EARLY WINTER',alt:'Misty early winter sunrise',scene:'🌫️ Soft mist over the winter fields',words:['ಮಾರ್ಗಶಿರ','ಪುಷ್ಯ','ಹೇಮಂತ','ಋತು'],offsets:[0.36,1.43,2.83,3.49]},
  {at:21.67,month:'ಮಾಘ · ಫಾಲ್ಗುಣ',season:'ಶಿಶಿರ ಋತು',label:'06 / 06 · LATE WINTER',alt:'Cool, pale winter fields',scene:'❄️ Cool mist on late-winter mornings',words:['ಮಾಘ','ಫಾಲ್ಗುಣ','ಶಿಶಿರ','ಋತು'],offsets:[0.34,1.38,2.78,3.52]}
];
// Approximate word cues manually aligned against the supplied 26-second recording.
// We follow actual currentTime (not wall clock) for pause, slow playback and seeking.
const stage=$('sync-stage'),landscape=$('sync-landscape'),seasonCards=[...document.querySelectorAll('.season-card')];
const karaoke=$('sync-karaoke'),scenePlay=$('scene-play'),sceneLabel=$('scene-play-label');
let lastSeason=-1,lastWord=-1,animFrame=null;
function buildKaraoke(season){
  if(!karaoke)return;
  const first=document.createElement('div');first.className='p-karaoke-months';
  const second=document.createElement('div');second.className='p-karaoke-season';
  season.words.forEach((word,i)=>{
    const token=document.createElement('span');token.className='p-word';token.textContent=word;token.dataset.word=String(i);
    if(i<2){first.appendChild(token);if(i===0){const comma=document.createElement('span');comma.className='p-karaoke-comma';comma.textContent=',';first.appendChild(comma)}}
    else second.appendChild(token);
  });
  karaoke.replaceChildren(first,second);
}
function syncAudioScene(){
  if(!player||!stage)return;
  const time=Number.isFinite(player.currentTime)?player.currentTime:0;
  const duration=Number.isFinite(player.duration)&&player.duration>0?player.duration:26;
  let active=0;
  for(let i=seasonCues.length-1;i>=0;i--){if(time>=seasonCues[i].at){active=i;break}}
  const season=seasonCues[active];
  if(active!==lastSeason){
    lastSeason=active;lastWord=-1;
    stage.dataset.season=String(active);
    $('sync-months').textContent=season.month;
    $('sync-season').textContent=season.season;
    $('sync-label').textContent=season.label;
    $('scene-caption').textContent=season.scene;
    landscape?.setAttribute('aria-label',season.alt);
    buildKaraoke(season);
  }
  let word=-1;
  for(let i=season.offsets.length-1;i>=0;i--){if(time>=season.at+season.offsets[i]){word=i;break}}
  if(word!==lastWord){
    lastWord=word;
    karaoke?.querySelectorAll('.p-word').forEach((node,i)=>{
      node.classList.toggle('is-current',i===word);
      node.classList.toggle('is-spoken',i<word);
    });
  }
  const playing=!player.paused&&!player.ended;
  stage.classList.toggle('is-playing',playing);
  seasonCards.forEach((card,i)=>card.classList.toggle('is-speaking',playing&&i===active));
  const percentage=Math.min(100,Math.max(0,time/duration*100));
  $('sync-progress-fill').style.width=percentage+'%';
  $('sync-progress').setAttribute('aria-valuenow',String(Math.round(percentage)));
  if(scenePlay&&sceneLabel){
    scenePlay.setAttribute('aria-label',playing?'Pause Kannada narration and animation':'Play Kannada narration and animation');
    scenePlay.firstChild.textContent=playing?'Ⅱ ':'▶ ';
    sceneLabel.textContent=playing?'Pause animation':'Play animation';
  }
}
function stopFrames(){if(animFrame!==null){cancelAnimationFrame(animFrame);animFrame=null}}
function updateFrame(){syncAudioScene();if(player&&!player.paused&&!player.ended)animFrame=requestAnimationFrame(updateFrame);else animFrame=null}
function scheduleFrames(){stopFrames();syncAudioScene();if(player&&!player.paused&&!player.ended)animFrame=requestAnimationFrame(updateFrame)}
if(player&&stage){
  for(const eventName of ['timeupdate','play','playing','pause','seeked','seeking','loadedmetadata','ratechange','ended'])
    player.addEventListener(eventName,scheduleFrames);
  document.addEventListener('visibilitychange',()=>{
    if(document.hidden)stopFrames();else scheduleFrames()
  });
  seasonCards.forEach((card,i)=>{
    const seek=()=>{
      if(player.error)return;
      player.currentTime=seasonCues[i].at+0.15;
      scheduleFrames();
      player.play().catch(()=>{state.textContent='Tap the audio play control to start.'});
    };
    card.addEventListener('click',seek);
    card.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();seek()}});
    card.setAttribute('role','button');
    card.setAttribute('aria-label',seasonCues[i].month+' — '+seasonCues[i].season+'. Play from this season.');
  });
  syncAudioScene();
}
function startScene(){
  if(!player)return;
  if(player.paused){
    if(player.ended||(Number.isFinite(player.duration)&&player.currentTime>=player.duration-.15))player.currentTime=0;
    player.play().catch(()=>{state.textContent='Press the native audio play control to start.'});
  }else player.pause();
}
scenePlay?.addEventListener('click',startScene);
$('hero-start')?.addEventListener('click',e=>{
  if(!player)return;
  e.preventDefault();
  $('sync-stage')?.scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'center'});
  player.currentTime=0;
  player.play().catch(()=>{state.textContent='Tap Play animation on the illustrated scene.'});
});

const questions=[{month:'ಚೈತ್ರ, ವೈಶಾಖ',answer:'ವಸಂತ ಋತು',explain:'Spring · Flowers bloom'},{month:'ಜ್ಯೇಷ್ಠ, ಆಷಾಢ',answer:'ಗ್ರೀಷ್ಮ ಋತು',explain:'Summer · Sunshine and mangoes'},{month:'ಶ್ರಾವಣ, ಭಾದ್ರಪದ',answer:'ವರ್ಷ ಋತು',explain:'Monsoon · Rainy days'},{month:'ಆಶ್ವಯುಜ, ಕಾರ್ತಿಕ',answer:'ಶರದೃತು',explain:'Autumn · Clear skies'},{month:'ಮಾರ್ಗಶಿರ, ಪುಷ್ಯ',answer:'ಹೇಮಂತ ಋತು',explain:'Early winter · Misty mornings'},{month:'ಮಾಘ, ಫಾಲ್ಗುಣ',answer:'ಶಿಶಿರ ಋತು',explain:'Late winter · Cool mornings'}];
const names=questions.map(q=>q.answer);let index=0,answered=false;
function options(q,i){return [q.answer,names[(i+2)%6],names[(i+4)%6]].sort((a,b)=>names.indexOf(a)-names.indexOf(b))}
function render(){let q=questions[index];answered=false;$('quiz-count').textContent='Question '+(index+1)+' of '+questions.length;$('quiz-prompt').textContent=q.month+' — ಯಾವ ಋತು?';$('quiz-feedback').textContent='Choose an answer together.';$('quiz-next').hidden=true;const root=$('quiz-choices');root.replaceChildren();for(const name of options(q,index)){const b=document.createElement('button');b.type='button';b.lang='kn';b.textContent=name;b.addEventListener('click',()=>choose(name,b));root.appendChild(b)}}
function choose(name,button){if(answered)return;answered=true;const q=questions[index];let correct=name===q.answer;for(const b of $('quiz-choices').children){b.disabled=true;if(b.textContent===q.answer)b.classList.add('is-correct')}if(!correct)button.classList.add('is-wrong');$('quiz-feedback').textContent=correct?'ಚೆನ್ನಾಗಿದೆ! '+q.explain:'ಒಳ್ಳೆಯ ಪ್ರಯತ್ನ! ಸರಿಯಾದ ಉತ್ತರ: '+q.answer+' · '+q.explain;$('quiz-next').hidden=false;$('quiz-next').textContent=index===questions.length-1?'Play again ↺':'Next question →';}
$('quiz-next')?.addEventListener('click',()=>{index=index===questions.length-1?0:index+1;render()});$('quiz-restart')?.addEventListener('click',()=>{index=0;render()});if($('quiz-choices'))render();
$('share-activity')?.addEventListener('click',async()=>{const url='https://cubboncrayons.github.io/purochi.html';const title='ಪುರೋಚಿ · ಕನ್ನಡ ತಿಂಗಳುಗಳು ಮತ್ತು ಋತುಗಳು';try{if(navigator.share){await navigator.share({title,text:'A free Kannada family recitation from Cubbon Crayons',url});$('share-status').textContent='Thanks for sharing!';return}if(navigator.clipboard?.writeText){await navigator.clipboard.writeText(url);$('share-status').textContent='Activity link copied. Share it with your family!';return}throw Error('Unavailable')}catch(e){if(e.name==='AbortError')return;$('share-status').textContent='Share this link: '+url;}});
})();