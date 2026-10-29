
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>XATZO | Beyond the Unknown</title>
<style>
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:#07070c;color:#f5f0ff;font-family:Arial,sans-serif}
button,a{font:inherit}
button{cursor:pointer}
nav{position:sticky;top:0;z-index:10;background:#08080def;
backdrop-filter:blur(15px);border-bottom:1px solid #ffffff18;
padding:20px 7%;display:flex;justify-content:space-between;align-items:center}
.logo{font-size:25px;font-weight:900;letter-spacing:5px;color:#c69aff}
nav a{color:#ddd;text-decoration:none;margin-left:22px;font-size:13px}
nav a:hover{color:#c69aff}
.hero{min-height:85vh;display:grid;place-items:center;text-align:center;
position:relative;overflow:hidden;padding:60px 20px;
background:radial-gradient(ellipse at center,#261044 0%,#0a0913 43%,#07070c 75%)}
.hero:before{content:"";position:absolute;width:350px;height:350px;border:1px solid #b15cff40;border-radius:50%;animation:spin 20s linear infinite}
.hero:after{content:"";position:absolute;width:500px;height:500px;border:1px dashed #6b5cff30;border-radius:50%;animation:spin 35s linear infinite reverse}
.hero-inner{z-index:1}
.kicker{letter-spacing:6px;color:#bd8cff;font-size:12px}
h1{font-size:clamp(55px,12vw,115px);letter-spacing:8px;margin:20px 0;
background:linear-gradient(90deg,#fff,#c18aff,#6deaff);color:transparent;background-clip:text}
.subtitle{color:#aaa6bd;letter-spacing:2px}
.btn{border:1px solid #b77bff;background:#a855f71a;color:white;padding:14px 24px;border-radius:30px;margin:10px;transition:.25s}
.btn:hover{background:#a855f7;box-shadow:0 0 30px #a855f788;transform:translateY(-3px)}
section{padding:85px 8%;scroll-margin-top:75px}
.label{font-size:11px;letter-spacing:5px;color:#b88aff}
h2{font-size:clamp(30px,5vw,48px);margin:12px 0 35px}
.muted{color:#aaa6b9;line-height:1.8}
.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.card{background:linear-gradient(145deg,#171321,#0b0b12);border:1px solid #ffffff18;border-radius:20px;padding:25px 15px;text-align:center;overflow:hidden;transition:.3s}
.card:hover{transform:translateY(-7px);border-color:#a855f7;box-shadow:0 0 30px #a855f71b}
.card h3{letter-spacing:4px}
.character{height:240px;display:grid;place-items:center;position:relative;overflow:hidden}
.aura{position:absolute;width:155px;height:190px;border-radius:50%;filter:blur(22px);opacity:.6;animation:pulse 2.5s ease-in-out infinite alternate}
.noctyx .aura{background:#783bff}
.nv .aura{background:conic-gradient(#ff493d,#ffda4d,#45ffb0,#36cfff,#b35bff,#ff493d)}
.av .aura{background:#ff4b16}
.stick{position:relative;width:100px;height:180px;filter:drop-shadow(0 0 8px currentColor);color:#fff}
.head{position:absolute;width:29px;height:29px;border:4px solid currentColor;border-radius:50%;top:8px;left:36px;background:#08080d}
.bodyline{position:absolute;width:4px;height:67px;background:currentColor;top:38px;left:49px;border-radius:5px}
.arm{position:absolute;width:4px;height:51px;background:currentColor;top:43px;border-radius:5px}
.arm.left{left:31px;transform:rotate(35deg)}
.arm.right{left:66px;transform:rotate(-35deg)}
.leg{position:absolute;width:4px;height:65px;background:currentColor;top:98px;border-radius:5px}
.leg.left{left:38px;transform:rotate(17deg)}
.leg.right{left:59px;transform:rotate(-17deg)}
.noctyx .stick{color:#d7b6ff;transform:scale(1.06)}
.nv .stick{color:#d6fff8;transform:scale(.9)}
.av .stick{color:#ffd0a8;transform:scale(1.1)}
.card p{color:#aaa6b9;line-height:1.7;font-size:14px}
.reader-launch{background:linear-gradient(145deg,#151020,#0a0a12);border:1px solid #ffffff20;border-radius:24px;padding:45px 25px;text-align:center}
.reader-launch .book{font-size:55px;animation:float 3s ease-in-out infinite}
footer{text-align:center;padding:35px;color:#777;border-top:1px solid #ffffff15}
#whisper{position:fixed;bottom:22px;left:50%;transform:translateX(-50%);background:#191124;border:1px solid #9b62ff;padding:14px 20px;border-radius:12px;z-index:150;display:none;box-shadow:0 0 30px #8b5cf655;max-width:90%;text-align:center}

/* FULL-PAGE E-READER */
#reader{
 display:none;position:fixed;inset:0;z-index:1000;background:#08080d;
 width:100%;height:100%;height:100dvh;overflow:auto;
}
#reader.open{display:flex;flex-direction:column;animation:readerIn .35s ease}
.reader-top{
 display:flex;align-items:center;justify-content:space-between;gap:15px;
 padding:18px 5%;border-bottom:1px solid #ffffff18;background:#0c0b13;
 position:sticky;top:0;
}
.reader-brand{font-weight:900;letter-spacing:4px;color:#c69aff}
.reader-top button{margin:0}
.reader-workspace{
 flex:1;display:flex;flex-direction:column;align-items:center;
 justify-content:center;padding:35px 20px;min-height:0;
}
.reader-empty{text-align:center;max-width:560px}
.reader-empty .big-book{font-size:65px;filter:drop-shadow(0 0 25px #a855f7aa)}
.reader-empty h2{margin-bottom:12px}
.reader-empty p{color:#9995aa;line-height:1.8}
.reader-page{
 display:none;width:min(850px,100%);margin:auto;
 min-height:350px;padding:clamp(25px,6vw,75px);
 background:linear-gradient(145deg,#11101b,#0b0b12);
 border:1px solid #ffffff18;border-radius:16px;
 box-shadow:0 0 60px #8b5cf710;
}
.reader-page.visible{display:block;animation:pageIn .4s ease}
.reader-chapter{font-size:11px;letter-spacing:4px;color:#b88aff}
.reader-page h2{font-size:clamp(28px,5vw,46px);margin:22px 0}
.reader-text{font-size:17px;line-height:2.1;color:#d0cadd;white-space:pre-wrap}
.reader-bottom{padding:16px 5%;border-top:1px solid #ffffff18;background:#0c0b13}
.reader-controls{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.progress-track{height:3px;background:#292431;margin-top:14px;border-radius:10px;overflow:hidden}
.progress-fill{height:100%;width:0;background:linear-gradient(90deg,#a855f7,#45e9ff);transition:width .3s}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes pulse{from{transform:scale(.85);opacity:.35}to{transform:scale(1.12);opacity:.8}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
@keyframes readerIn{from{opacity:0;transform:scale(1.015)}to{opacity:1;transform:scale(1)}}
@keyframes pageIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
@media(max-width:700px){
 .cards{grid-template-columns:1fr}
 nav{padding:17px 5%}
 nav a{margin-left:9px;font-size:11px}
 .character{height:210px}
 section{padding:65px 6%}
 .reader-top{padding:13px 4%}
 .reader-workspace{padding:20px 12px}
 .reader-page{min-height:300px}
 .reader-text{font-size:15px}
}
@media(prefers-reduced-motion:reduce){
 *,*::before,*::after{animation-duration:.01ms!important;scroll-behavior:auto!important;transition-duration:.01ms!important}
}
</style>
</head>
<body>

<nav>
 <div class="logo">XATZO</div>
 <div><a href="#characters">CHARACTERS</a><a href="#read">E-READER</a></div>
</nav>

<header class="hero">
 <div class="hero-inner">
  <div class="kicker">A WORLD BEYOND THE KNOWN</div>
  <h1>XATZO</h1>
  <p class="subtitle">Three figures. Unanswered questions. Infinite possibilities.</p>
  <a href="#characters"><button class="btn">ENTER THE UNKNOWN ↘</button></a>
 </div>
</header>

<section id="characters">
 <div class="label">THE CHARACTER ARCHIVE</div>
 <h2>More than meets the eye.</h2>
 <p class="muted">Simple figures. Powerful auras. Their stories are waiting to be uncovered.</p>
 <div class="cards">

  <article class="card noctyx">
   <div class="character"><div class="aura"></div><div class="stick">
    <div class="head"></div><div class="bodyline"></div><div class="arm left"></div><div class="arm right"></div><div class="leg left"></div><div class="leg right"></div>
   </div></div>
   <h3>NOCTYX</h3>
   <p>Identity unknown. Motives concealed. Some questions are not meant to be answered yet.</p>
   <button class="btn" onclick="secret('noctyx')">Investigate</button>
  </article>

  <article class="card nv">
   <div class="character"><div class="aura"></div><div class="stick">
    <div class="head"></div><div class="bodyline"></div><div class="arm left"></div><div class="arm right"></div><div class="leg left"></div><div class="leg right"></div>
   </div></div>
   <h3>NV</h3>
   <p>THE YOUNGEST<br>Wielder of all elements. A spectrum of power surrounds this stickman.</p>
   <button class="btn" onclick="secret('nv')">Explore aura</button>
  </article>

  <article class="card av">
   <div class="character"><div class="aura"></div><div class="stick">
    <div class="head"></div><div class="bodyline"></div><div class="arm left"></div><div class="arm right"></div><div class="leg left"></div><div class="leg right"></div>
   </div></div>
   <h3>AV</h3>
   <p>THE OLDEST<br>A fire wielder, surrounded by the blazing energy of flame.</p>
   <button class="btn" onclick="secret('av')">Explore aura</button>
  </article>

 </div>
</section>

<section id="read">
 <div class="label">THE XATZO E-READER</div>
 <h2>Your reading space.</h2>
 <div class="reader-launch">
  <div class="book">📖</div>
  <h3>Enter the XATZO reader</h3>
  <p class="muted">A quiet, full-screen reading space. Nothing is loaded until you choose.</p>
  <button class="btn" onclick="openReader()">OPEN E-READER ↗</button>
 </div>
</section>

<section>
 <div class="label">A SMALL WARNING</div>
 <h2>Not everything is visible.</h2>
 <p class="muted">Some details reveal themselves only when you interact with them.</p>
 <p class="secret" onclick="secret('hidden')">There is something beneath the surface.</p>
 <p class="muted" style="font-size:11px">XATZO ARCHIVE // END OF VISIBLE RECORD // APP COMMING SOON</p>
</section>

<footer>XATZO · THE UNKNOWN REMAINS UNKNOWN</footer>
<div id="whisper"></div>

<!-- FULLSCREEN READER: EMPTY UNTIL USER CHOOSES A SAMPLE -->
<div id="reader" aria-hidden="true">
 <div class="reader-top">
  <div class="reader-brand">XATZO / READER</div>
  <button class="btn" onclick="closeReader()">✕ Close</button>
 </div>

 <div class="reader-workspace">
  <div id="readerEmpty" class="reader-empty">
   <div class="big-book">◈</div>
   <div class="label">A BLANK PAGE</div>
   <h2>Your story begins here.</h2>
   <p>No chapters are loaded. Choose the sample only if you want to preview the reader.</p>
   <button class="btn" onclick="loadSample()">LOAD SAMPLE STORY</button>
  </div>

  <article id="readerPage" class="reader-page">
   <div class="reader-chapter" id="chapterLabel"></div>
   <h2 id="chapterTitle"></h2>
   <div class="reader-text" id="chapterText"></div>
  </article>
 </div>

 <div class="reader-bottom">
  <div class="reader-controls">
   <button class="btn" id="prevBtn" onclick="changePage(-1)" disabled>← Previous</button>
   <span class="muted" id="pageCount">No story loaded</span>
   <button class="btn" id="nextBtn" onclick="changePage(1)" disabled>Next →</button>
  </div>
  <div class="progress-track"><div id="progressFill" class="progress-fill"></div></div>
 </div>
</div>

<script>
const chapters = [
 {title:"The First Sign",text:"The world seemed ordinary.\\n\\nThree simple figures stood beneath an unfamiliar sky.\\n\\nOne carried the glow of countless elements. One burned with the aura of fire. And one remained hidden behind an unanswered question.\\n\\nThis was only the beginning."},
 {title:"The Youngest and the Oldest",text:"NV, the youngest, stood surrounded by the shifting colours of every element.\\n\\nAV, the oldest, carried the fierce aura of fire.\\n\\nTheir powers were different. Their stories were not yet fully told.\\n\\nSomewhere beyond their sight, a mystery waited."},
 {title:"The Unanswered Name",text:"A strange presence lingered at the edge of awareness.\\n\\nNo clear face. No certain explanation. Only a feeling that something important remained concealed.\\n\\nThe name was NOCTYX.\\n\\nThe truth remained beyond reach."}
];

let current = 0;
let loaded = false;

function openReader(){
 const reader=document.getElementById("reader");
 reader.classList.add("open");
 reader.setAttribute("aria-hidden","false");
 document.body.style.overflow="hidden";
 document.getElementById("readerEmpty").style.display="block";
 document.getElementById("readerPage").classList.remove("visible");
 if(!loaded) document.getElementById("pageCount").textContent="No story loaded";
}
function closeReader(){
 const reader=document.getElementById("reader");
 reader.classList.remove("open");
 reader.setAttribute("aria-hidden","true");
 document.body.style.overflow="";
}
function loadSample(){
 loaded=true;
 current=0;
 document.getElementById("readerEmpty").style.display="none";
 document.getElementById("readerPage").classList.add("visible");
 renderChapter();
}
function renderChapter(){
 if(!loaded)return;
 document.getElementById("chapterLabel").textContent="CHAPTER "+String(current+1).padStart(2,"0");
 document.getElementById("chapterTitle").textContent=chapters[current].title;
 document.getElementById("chapterText").textContent=chapters[current].text;
 document.getElementById("pageCount").textContent=(current+1)+" / "+chapters.length;
 document.getElementById("prevBtn").disabled=current===0;
 document.getElementById("nextBtn").disabled=current===chapters.length-1;
 document.getElementById("progressFill").style.width=((current+1)/chapters.length*100)+"%";
}
function changePage(step){
 if(!loaded)return;
 current=Math.max(0,Math.min(chapters.length-1,current+step));
 renderChapter();
}
function secret(who){
 const messages={
  noctyx:"NOCTYX // The record ends here. No identity has been revealed.",
  nv:"NV // ALL ELEMENTS RESPOND. The youngest carries a spectrum of power.",
  av:"AV // FIRE ANSWERS. The oldest burns with elemental force.",
  hidden:"You found a hidden message. Keep looking. XATZO has more secrets than this page reveals."
 };
 const box=document.getElementById("whisper");
 box.textContent=messages[who]||messages.hidden;
 box.style.display="block";
 clearTimeout(window.whisperTimer);
 window.whisperTimer=setTimeout(()=>box.style.display="none",4500);
}
document.addEventListener("keydown",e=>{
 if(e.key==="Escape")closeReader();
 if(document.getElementById("reader").classList.contains("open")){
  if(e.key==="ArrowRight")changePage(1);
  if(e.key==="ArrowLeft")changePage(-1);
 }
 if(e.key.toLowerCase()==="x")secret("hidden");
});
</script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
