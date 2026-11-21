'use strict';
(() => {
 const audio=document.querySelector('#site-welcome');
 if(!audio)return;
 const key='cc-welcome-spoken-v2',tracks=['kn','en'];
 let index=0,finished=false,pending=false,started=false,resume=false;
 try{if(sessionStorage.getItem(key)==='played')return;}catch{}
 audio.src='assets/audio/welcome-'+tracks[index]+'-v2.mp3';
 audio.volume=.85;
 function disarm(){
  document.removeEventListener('click',interaction,true);
  document.removeEventListener('touchend',interaction,true);
  document.removeEventListener('keydown',interaction,true);
 }
 function arm(){
  if(finished)return;
  document.addEventListener('click',interaction,true);
  document.addEventListener('touchend',interaction,{capture:true,passive:true});
  document.addEventListener('keydown',interaction,true);
 }
 function stop(){
  finished=true;resume=false;audio.pause();disarm();
 }
 function attempt(){
  if(finished||pending||document.hidden)return;
  pending=true;
  // Calling play here preserves the activation from the first real tap.
  const promise=audio.play();
  Promise.resolve(promise).then(()=>{
   pending=false;
   if(finished||document.hidden){audio.pause();return;}
   started=true;resume=false;disarm();
   try{sessionStorage.setItem(key,'played');}catch{}
  }).catch(error=>{
   pending=false;
   if(finished)return;
   if(error.name==='NotAllowedError'||error.name==='AbortError')arm();
   else stop();
  });
 }
 function interaction(event){
  if(event.type==='keydown'&&(event.key==='Escape'||event.ctrlKey||event.metaKey||event.altKey))return;
  if(event.isTrusted)attempt();
 }
 audio.addEventListener('ended',()=>{
  if(finished)return;
  index++;
  if(index>=tracks.length){stop();return;}
  audio.src='assets/audio/welcome-'+tracks[index]+'-v2.mp3';
  attempt();
 });
 audio.addEventListener('error',stop);
 document.addEventListener('keydown',event=>{if(event.key==='Escape')stop();});
 document.addEventListener('visibilitychange',()=>{
  if(document.hidden){
   resume=started&&!audio.paused&&!finished;
   audio.pause();
  }else if(!started||resume)attempt();
 });
 window.addEventListener('pagehide',stop);
 arm();attempt();
})();
