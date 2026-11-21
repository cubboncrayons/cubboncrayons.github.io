(() => {
 const audio=document.querySelector('#welcome-audio'),group=document.querySelector('.welcome-choices'),status=document.querySelector('.welcome-status');
 if(!audio||!group)return;
 const buttons=[...group.querySelectorAll('button')],labels={kn:'ಕನ್ನಡದಲ್ಲಿ ಕೇಳಿ',en:'Listen in English'};
 let current=null,request=0;
 function sync(){
  for(const button of buttons){
   const active=button.dataset.language===current&&!audio.paused&&!audio.ended;
   button.setAttribute('aria-pressed',String(active));
   button.textContent=active?(current==='kn'?'ನಿಲ್ಲಿಸಿ · ಕನ್ನಡ':'Stop · English'):labels[button.dataset.language];
  }
 }
 group.hidden=false;
 buttons.forEach(button=>button.addEventListener('click',async()=>{
  const key=button.dataset.language,id=++request;status.textContent='';
  if(key===current&&!audio.paused){audio.pause();sync();return;}
  audio.pause();current=key;
  audio.src='assets/audio/welcome-'+key+'.mp3';audio.currentTime=0;
  try{await audio.play();}
  catch(error){if(id===request&&error.name!=='AbortError')status.textContent='Audio could not play. Please try again.';}
  if(id===request)sync();
 }));
 for(const event of ['play','pause','ended'])audio.addEventListener(event,sync);
 audio.addEventListener('error',()=>{sync();status.textContent='Audio could not load. Please try again.';});
 document.addEventListener('visibilitychange',()=>{if(document.hidden){++request;audio.pause();sync();}});
 window.addEventListener('pagehide',()=>audio.pause());
})();
