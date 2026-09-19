const sections=[...document.querySelectorAll('.hero')];
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
const visible=new Set();
const motionButton=document.querySelector('.motion');
let paused=reduced.matches;
function syncMotion(){
 document.body.classList.toggle('paused',paused);
 motionButton.textContent=paused?'Enable motion':'Pause motion';
 motionButton.setAttribute('aria-pressed',String(paused));
 sections.forEach(s=>{const v=s.querySelector('video'); if(paused||!visible.has(s)){v.pause();if(paused)s.querySelector('.visual').classList.remove('has-video');}else if(v.dataset.src){if(!v.getAttribute('src'))v.src=v.dataset.src;v.play().catch(()=>s.querySelector('.visual').classList.remove('has-video'));}});
}
const observer=new IntersectionObserver(entries=>{
 for(const e of entries){if(e.isIntersecting)visible.add(e.target);else visible.delete(e.target);}
 const current=[...visible].sort((a,b)=>Math.abs(a.getBoundingClientRect().top)-Math.abs(b.getBoundingClientRect().top))[0];
 document.querySelectorAll('.rail a').forEach(a=>{const active=a.hash==='#'+current?.id;a.classList.toggle('active',active);if(active)a.setAttribute('aria-current','true');else a.removeAttribute('aria-current');});
 syncMotion();
},{threshold:.2});
sections.forEach(s=>{const v=s.querySelector('video');const config=window.BGM_MEDIA?.[s.id];if(config){v.dataset.src=typeof config==='string'?config:config.src;if(config.position){s.style.setProperty('--scene-position',config.position);}}
 v.addEventListener('playing',()=>{if(!paused&&visible.has(s))s.querySelector('.visual').classList.add('has-video');else v.pause();});
 v.addEventListener('error',()=>s.querySelector('.visual').classList.remove('has-video'));observer.observe(s);
});
motionButton.addEventListener('click',()=>{paused=!paused;syncMotion();});
reduced.addEventListener('change',()=>{paused=reduced.matches;syncMotion();});
document.addEventListener('visibilitychange',()=>{if(document.hidden)sections.forEach(s=>s.querySelector('video').pause());else syncMotion();});
let queued=false;
function animate(){queued=false;if(paused||innerWidth<=700)return;for(const s of visible){const p=Math.max(-1,Math.min(1,s.getBoundingClientRect().top/innerHeight));s.querySelector('img').style.transform=`scale(1.04) translateY(${p*1.5}%)`;}}
addEventListener('scroll',()=>{if(!queued){queued=true;requestAnimationFrame(animate);}},{passive:true});
syncMotion();
document.querySelectorAll('.plan-select').forEach(a=>a.addEventListener('click',()=>{const status=document.querySelector('#selected-plan');status.textContent='Let’s discuss: '+a.dataset.plan;status.hidden=false;}));
let toastTimer;
document.querySelector('.copy-page').addEventListener('click',async()=>{try{await navigator.clipboard.writeText('Business Growth Myanmar');const t=document.querySelector('#toast');t.textContent='Page name copied — Facebook မှာ ရှာနိုင်ပါတယ်။';t.classList.add('show');clearTimeout(toastTimer);toastTimer=setTimeout(()=>t.classList.remove('show'),4000);}catch{document.querySelector('#copy-dialog').showModal();}});
document.querySelector('#close-dialog').addEventListener('click',()=>document.querySelector('#copy-dialog').close());

// Pointer light is confined to surfaces; touch and reduced-motion stay still.
const finePointer=matchMedia('(hover: hover) and (pointer: fine)');
const reactive=[...document.querySelectorAll('.hero,.button,.plan-grid article')];
reactive.forEach(el=>{
 let frame=0,point;
 const reset=()=>{cancelAnimationFrame(frame);frame=0;el.classList.remove('pointer-lit');el.style.removeProperty('--tilt-x');el.style.removeProperty('--tilt-y');};
 el.addEventListener('pointermove',e=>{
  if(!finePointer.matches||reduced.matches||paused||e.pointerType==='touch')return;
  point={x:e.clientX,y:e.clientY};
  if(frame)return;
  frame=requestAnimationFrame(()=>{
   frame=0;const r=el.getBoundingClientRect();
   const x=Math.max(0,Math.min(1,(point.x-r.left)/r.width));
   const y=Math.max(0,Math.min(1,(point.y-r.top)/r.height));
   el.style.setProperty('--pointer-x',`${x*100}%`);el.style.setProperty('--pointer-y',`${y*100}%`);
   if(el.matches('.plan-grid article')){el.style.setProperty('--tilt-x',`${(0.5-y)*3}deg`);el.style.setProperty('--tilt-y',`${(x-0.5)*3}deg`);}
   el.classList.add('pointer-lit');
  });
 },{passive:true});
 el.addEventListener('pointerleave',reset);el.addEventListener('pointercancel',reset);
 motionButton.addEventListener('click',reset);reduced.addEventListener('change',reset);finePointer.addEventListener('change',reset);
});
