import urllib.parse as up
U=lambda p,w=600,h=600: f"https://images.unsplash.com/{p}?auto=format&fit=crop&w={w}&h={h}&q=70"
WHO=["her","him","mom","homebodies","coffee lovers","the always cold"]
BF=[("Kindle Paperwhite","photo-1676107779594-7a23bd99e07c","For anyone with a stack of books on the nightstand. No glare, and the battery lasts for weeks."),
    ("Breville espresso machine","photo-1620051787208-a45bc64e32ff","For the person quietly spending a fortune at the café. It grinds, tamps and steams milk at home."),
    ("Ninja air fryer","photo-1774074645537-f72f70d40d12","Crispy fries on a Tuesday night without heating up the whole kitchen.")]
def page(fonts,css,body,js=""):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>The Cozy Edit sample</title><link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet"><style>*{{box-sizing:border-box}}img,svg{{display:block}}a{{color:inherit;text-decoration:none}}a:focus-visible,[tabindex]:focus-visible{{outline:3px solid #E7B36A;outline-offset:3px}}@media (prefers-reduced-motion:reduce){{*{{transition:none!important;animation:none!important}}}}{css}</style></head><body>{body}<script>{js}</script></body></html>'''
def pat(svg,w,h): return "url(\"data:image/svg+xml,"+up.quote(f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}'>{svg}</svg>")+"\")"

# palette shared idea: late-night kitchen
# espresso #241812, roast #33231A, walnut #6B4529, copper #C27C4E, cream #F1E4CF, sage #8E9F7E, tomato #B9412F, lamp #F2C27B

# ================= K1: OPEN SHELVES =================
WOOD=pat("<rect width='220' height='22' fill='#6B4529'/><path d='M0 7c50-4 90 3 140 0s60-3 80-1M0 15c40 3 100-3 150 1s50 1 70-1' stroke='#5A3921' stroke-width='1.4' fill='none'/>",220,22)
TILE=pat("<rect width='60' height='30' fill='#2A1C15'/><path d='M0 .5h60M.5 0v15M30.5 15v15M0 15.5h60' stroke='#33231A' stroke-width='1'/>",60,30)
GARL=pat("<path d='M0 4c15 14 45 14 60 0' fill='none' stroke='#4E6B45' stroke-width='5' stroke-linecap='round'/><path d='M10 9l-4 6M22 13l-1 7M38 13l1 7M50 9l4 6' stroke='#5F7F53' stroke-width='3' stroke-linecap='round'/><circle cx='30' cy='15' r='3' fill='#B9412F'/><circle cx='16' cy='12' r='2.2' fill='#B9412F'/>",60,24)
GLAZE=["#8E9F7E","#C27C4E","#D8C3A0","#7E8FA0","#B9412F","#C9A24A"]
c1=f""":root{{--esp:#241812;--roast:#33231A;--walnut:#6B4529;--copper:#C27C4E;--cream:#F1E4CF;--sage:#8E9F7E;--tom:#B9412F;--lamp:#F2C27B}}
body{{margin:0;background:var(--esp) {TILE};color:var(--cream);font-family:'Lora',Georgia,serif}}
.disc{{font-family:'Karla',sans-serif;font-size:12px;text-align:center;padding:8px;color:#b8a48e;background:#1b120d}}
header{{max-width:1180px;margin:0 auto;padding:20px 28px;display:flex;justify-content:space-between;align-items:center;font-family:'Karla',sans-serif}}
.wm{{font-family:'Caprasimo',serif;font-size:32px;color:var(--lamp)}}
nav{{display:flex;gap:28px;font-size:15px}}nav a:hover{{color:var(--lamp)}}
/* under-cabinet light strip */
.cab{{position:relative;max-width:1180px;margin:8px auto 0;height:26px;background:var(--roast);border-radius:0 0 6px 6px}}
.cab:after{{content:'';position:absolute;left:4%;right:4%;top:26px;height:260px;background:radial-gradient(ellipse at 50% 0,rgba(242,194,123,.30),rgba(242,194,123,0) 70%);pointer-events:none}}
.spot{{max-width:1180px;margin:0 auto;padding:46px 28px 0;display:grid;grid-template-columns:.95fr 1.05fr;gap:48px;align-items:end}}
h1{{font-family:'Caprasimo',serif;font-weight:400;font-size:clamp(44px,5.4vw,74px);line-height:1;margin:0 0 20px;color:var(--cream)}}
.lede{{font-size:19px;line-height:1.65;max-width:460px;color:#e4d4bd}}
.btn{{display:inline-block;margin-top:24px;background:var(--copper);color:#241812;padding:15px 26px;border-radius:999px;font-family:'Karla',sans-serif;font-weight:700;font-size:16px}}
.btn:hover{{background:var(--lamp)}}
.when{{font-family:'Karla',sans-serif;font-size:14px;color:#b8a48e;margin-top:12px}}
/* shelf with jars */
.shelf{{position:relative;padding-top:20px}}
.jars{{display:flex;gap:22px;align-items:flex-end;justify-content:center;padding:0 10px}}
.jar{{position:relative;flex:1;max-width:170px;text-align:center}}
.jar .lid{{height:22px;margin:0 14%;background:linear-gradient(#d18a5a,#9c5d34);border-radius:6px 6px 2px 2px}}
.jar .glass{{position:relative;border-radius:22px 22px 26px 26px;overflow:hidden;border:3px solid rgba(241,228,207,.28);box-shadow:inset 0 0 0 6px rgba(241,228,207,.06)}}
.jar img{{width:100%;aspect-ratio:3/4;object-fit:cover;filter:saturate(.9)}}
.jar .glass:after{{content:'';position:absolute;left:10%;top:8%;width:10%;height:60%;border-radius:20px;background:linear-gradient(rgba(255,255,255,.35),rgba(255,255,255,0))}}
.jar .lbl{{position:absolute;left:50%;bottom:16px;transform:translateX(-50%) rotate(-2deg);background:var(--cream);color:#3a271c;font-family:'Caprasimo',serif;font-size:15px;padding:6px 12px;border-radius:3px;white-space:nowrap}}
.jar:nth-child(2){{max-width:190px}}.jar:nth-child(2) .lbl{{transform:translateX(-50%) rotate(2deg)}}
.plank{{height:22px;background:{WOOD};border-radius:2px;box-shadow:0 14px 24px -10px rgba(0,0,0,.6)}}
.garland{{height:24px;background:{GARL} repeat-x;margin-top:-6px}}
.bfnote{{position:absolute;right:-6px;top:0;background:var(--tom);color:var(--cream);font-family:'Karla',sans-serif;font-weight:700;font-size:13px;padding:8px 12px;border-radius:4px;transform:rotate(5deg)}}
/* who: tins on a lower shelf */
.who{{max-width:1180px;margin:90px auto 0;padding:0 28px}}
.who h2,.picks h2{{font-family:'Caprasimo',serif;font-weight:400;font-size:40px;margin:0 0 8px}}
.who p.sub{{font-size:17px;color:#d8c6ad;margin:0 0 34px}}
.tins{{display:grid;grid-template-columns:repeat(6,1fr);gap:18px;align-items:end}}
.tin{{display:block;text-align:center;transition:transform .25s}}
.tin:hover{{transform:translateY(-6px)}}
.tin .t{{border-radius:10px 10px 6px 6px;position:relative;display:flex;align-items:center;justify-content:center;padding:0 8px}}
.tin .t:before{{content:'';position:absolute;left:-4px;right:-4px;top:-10px;height:14px;border-radius:6px;background:inherit;filter:brightness(.82)}}
.tin .t span{{background:var(--cream);color:#3a271c;font-family:'Caprasimo',serif;font-size:16px;line-height:1.15;padding:10px 8px;border-radius:4px;width:100%}}
.picks{{max-width:1180px;margin:90px auto 0;padding:0 28px 90px}}
.list{{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-top:26px}}
.it{{background:var(--roast);border-radius:14px;overflow:hidden;display:flex;flex-direction:column}}
.it img{{width:100%;aspect-ratio:4/3;object-fit:cover}}
.it div{{padding:18px 20px 22px;display:flex;flex-direction:column;flex:1}}
.it h3{{font-family:'Caprasimo',serif;font-weight:400;font-size:23px;margin:0 0 8px;color:var(--lamp)}}
.it p{{margin:0 0 16px;line-height:1.6;color:#e4d4bd;font-size:16px}}
.it a{{margin-top:auto;font-family:'Karla',sans-serif;font-weight:700;color:var(--cream);border-bottom:2px solid var(--copper);align-self:flex-start;padding-bottom:2px}}
.foot{{font-family:'Karla',sans-serif;font-size:13px;color:#a8947e;text-align:center;padding:0 28px 40px}}
@media(max-width:820px){{.spot{{grid-template-columns:1fr;padding-top:30px}}nav{{display:none}}.tins{{grid-template-columns:repeat(3,1fr);row-gap:34px}}.list{{grid-template-columns:1fr}}.jars{{gap:12px}}.jar .lbl{{font-size:13px}}.who{{margin-top:60px}}}}"""
heights=[150,190,130,170,150,185]
jars="".join(f'<a class="jar" href="#"><div class="lid"></div><div class="glass"><img src="{U(p,340,460)}" alt="{n}"><span class="lbl">{n.split()[0]}</span></div></a>' for n,p,_ in BF)
tins="".join(f'<a class="tin" href="#"><div class="t" style="background:{GLAZE[i]};height:{heights[i]}px"><span>For {n}</span></div></a>' for i,n in enumerate(WHO))
items="".join(f'<article class="it"><img src="{U(p,600,450)}" alt=""><div><h3>{n}</h3><p>{d}</p><a href="#">Check today\'s price on Amazon</a></div></article>' for n,p,d in BF)
b1=f"""<div class="disc">As an Amazon Associate we earn from qualifying purchases.</div>
<header><div class="wm">The Cozy Edit</div><nav><a href="#">Gift guides</a><a href="#">Black Friday</a><a href="#">About us</a></nav></header>
<div class="cab"></div>
<section class="spot"><div><h1>Gifts worth waiting for</h1><p class="lede">We keep the bigger presents on the top shelf until Black Friday. Here's what we'd reach for first on November 27.</p><a class="btn" href="#">See the Black Friday list</a><p class="when">20 days to go</p></div>
<div class="shelf"><span class="bfnote">Nov 27</span><div class="jars">{jars}</div><div class="plank"></div><div class="garland"></div></div></section>
<section class="who"><h2>Who are you shopping for?</h2><p class="sub">Every tin has a short list we'd actually give.</p><div class="tins">{tins}</div><div class="plank" style="margin-top:0"></div></section>
<section class="picks"><h2>Top of the shelf</h2><div class="list">{items}</div></section>
<p class="foot">Photos show similar items, not the exact product. We don't list prices because they change daily.</p>"""
open('shelf.html','w').write(page('family=Caprasimo&family=Lora:wght@400;500&family=Karla:wght@400;700',c1,b1))

# ================= K2: PENDANT LAMP OVER THE TABLE =================
RUNNER=pat("<rect width='24' height='24' fill='#F1E4CF'/><rect width='12' height='12' fill='#B9412F' opacity='.85'/><rect x='12' y='12' width='12' height='12' fill='#B9412F' opacity='.85'/><rect x='12' width='12' height='12' fill='#D9A08F'/><rect y='12' width='12' height='12' fill='#D9A08F'/>",24,24)
TABLE=pat("<rect width='300' height='40' fill='#4A2F1E'/><path d='M0 12c60-5 120 4 190 0s80-3 110 0M0 29c70 4 140-4 210 1s60 0 90-2' stroke='#3D2618' stroke-width='1.5' fill='none'/>",300,40)
MUGC=[("#B9412F","#F1E4CF"),("#8E9F7E","#F1E4CF"),("#D8C3A0","#3a271c"),("#7E8FA0","#F1E4CF"),("#C27C4E","#241812"),("#F1E4CF","#3a271c")]
c2=f""":root{{--esp:#1F1510;--roast:#2E2019;--copper:#C27C4E;--cream:#F1E4CF;--sage:#8E9F7E;--tom:#B9412F;--lamp:#F2C27B}}
body{{margin:0;background:var(--esp);color:var(--cream);font-family:'Karla',sans-serif}}
.disc{{font-size:12px;text-align:center;padding:8px;color:#a8947e}}
header{{max-width:1180px;margin:0 auto;padding:18px 28px;display:flex;justify-content:space-between;align-items:center;position:relative;z-index:3}}
.wm{{font-family:'Gloock',serif;font-size:30px}}
nav{{display:flex;gap:28px;font-size:15px}}nav a:hover{{color:var(--lamp)}}
.room{{position:relative;max-width:1180px;margin:0 auto;padding:0 28px;min-height:720px}}
.lamp{{position:absolute;left:62%;top:-90px;transform:translateX(-50%);width:200px;z-index:2;cursor:pointer;background:none;border:0;padding:0}}
.glow{{position:absolute;left:62%;top:60px;transform:translateX(-50%);width:820px;height:640px;background:radial-gradient(ellipse 48% 60% at 50% 0,rgba(242,194,123,.42),rgba(242,194,123,.12) 55%,rgba(242,194,123,0) 75%);clip-path:polygon(38% 0,62% 0,100% 100%,0 100%);opacity:0;animation:on 1.4s .5s forwards;pointer-events:none;transition:opacity .4s}}
.room.off .glow{{opacity:0!important;animation:none}}
@keyframes on{{0%{{opacity:0}}30%{{opacity:.6}}40%{{opacity:.2}}100%{{opacity:1}}}}
.copy{{position:relative;z-index:2;max-width:440px;padding-top:60px}}
h1{{font-family:'Gloock',serif;font-weight:400;font-size:clamp(44px,5.6vw,78px);line-height:1.02;margin:0 0 20px}}
.lede{{font-size:19px;line-height:1.6;color:#dccbb3}}
.btn{{display:inline-block;margin-top:22px;background:var(--cream);color:var(--esp);padding:15px 24px;border-radius:8px;font-weight:700;font-size:16px}}.btn:hover{{background:var(--lamp)}}
.hint{{font-size:14px;color:#a8947e;margin-top:12px}}
.table{{position:absolute;left:0;right:0;bottom:0;height:200px;background:{TABLE};border-top:10px solid #5C3B26}}
.runner{{position:absolute;left:44%;right:6%;bottom:56px;height:120px;background:{RUNNER};background-size:24px 24px;opacity:.95;transform:skewX(-8deg);box-shadow:0 10px 20px rgba(0,0,0,.35)}}
.plates{{position:absolute;left:44%;right:4%;bottom:70px;display:flex;justify-content:space-around;align-items:flex-end;z-index:2}}
.plate{{display:block;text-align:center;width:30%}}
.plate .rim{{border-radius:50%;background:#F7EEDF;padding:9%;box-shadow:0 18px 26px -10px rgba(0,0,0,.7),inset 0 0 0 4px #e6d6bd}}
.plate img{{width:100%;aspect-ratio:1;object-fit:cover;border-radius:50%}}
.plate span{{display:inline-block;margin-top:10px;font-family:'Gloock',serif;font-size:16px;color:var(--cream);background:rgba(31,21,16,.75);padding:4px 10px;border-radius:4px}}
.plate:hover .rim{{transform:translateY(-4px);transition:transform .2s}}
.holly{{position:absolute;left:calc(62% + 44px);top:150px;z-index:3}}
/* who: mugs on hooks */
.who{{max-width:1180px;margin:0 auto;padding:90px 28px 0}}
.who h2,.picks h2{{font-family:'Gloock',serif;font-weight:400;font-size:42px;margin:0 0 8px}}
.who p.sub{{font-size:17px;color:#cdbba3;margin:0}}
.rail{{height:10px;background:linear-gradient(#d18a5a,#8f5330);border-radius:5px;margin-top:36px}}
.mugs{{display:grid;grid-template-columns:repeat(6,1fr);gap:14px}}
.mug{{display:block;text-align:center}}
.mug svg{{width:100%;max-width:150px;margin:0 auto;transform-origin:50% 0;transition:transform .35s cubic-bezier(.3,1.5,.5,1)}}
.mug:hover svg,.mug:focus-visible svg{{transform:rotate(-8deg)}}
.mug b{{display:block;font-family:'Gloock',serif;font-weight:400;font-size:18px;margin-top:4px}}
.picks{{max-width:1180px;margin:0 auto;padding:90px 28px 80px}}
.row{{display:grid;grid-template-columns:180px 1fr auto;gap:28px;align-items:center;padding:22px 0;border-top:1px solid #3d2c22}}
.row img{{width:180px;height:180px;object-fit:cover;border-radius:50%;border:8px solid #F7EEDF}}
.row h3{{font-family:'Gloock',serif;font-weight:400;font-size:28px;margin:0 0 6px}}.row p{{margin:0;line-height:1.6;color:#dccbb3;max-width:520px;font-size:17px}}
.row a{{background:var(--copper);color:var(--esp);font-weight:700;padding:13px 18px;border-radius:8px;white-space:nowrap}}.row a:hover{{background:var(--lamp)}}
.foot{{font-size:13px;color:#a8947e;text-align:center;padding:0 28px 40px}}
@media(max-width:820px){{nav{{display:none}}.room{{min-height:0;padding-bottom:0}}.copy{{padding-top:20px}}.lamp{{position:relative;left:auto;top:auto;transform:none;margin:10px auto -10px;width:150px;display:block}}.glow{{left:50%;top:auto;margin-top:-30px;width:560px;height:520px}}.holly{{display:none}}
.table{{position:relative;height:auto;padding:30px 0 34px;margin:0 -28px}}.runner{{display:none}}.plates{{position:relative;left:auto;right:auto;bottom:auto;padding:0 12px;gap:10px}}.plate span{{font-size:13px}}
.mugs{{grid-template-columns:repeat(3,1fr);row-gap:20px}}.row{{grid-template-columns:96px 1fr;gap:16px}}.row img{{width:96px;height:96px;border-width:5px}}.row a{{grid-column:1/-1;text-align:center}}.row h3{{font-size:22px}}}}"""
lamp='<svg viewBox="0 0 200 230" aria-hidden="true"><path d="M100 0v110" stroke="#8f5330" stroke-width="3"/><path d="M80 110h40v14H80z" fill="#8f5330"/><path d="M100 120c-58 0-92 40-96 92h192c-4-52-38-92-96-92z" fill="#C27C4E"/><path d="M100 120c-58 0-92 40-96 92h30c4-42 28-80 66-92z" fill="#d89466"/><ellipse cx="100" cy="214" rx="44" ry="10" fill="#FFE2A8"/></svg>'
holly='<svg width="54" height="40" viewBox="0 0 54 40" aria-hidden="true"><path d="M26 22C14 6 2 14 4 22c6-2 10 2 8 8 8-2 12-4 14-8z" fill="#4E6B45"/><path d="M28 22C40 6 52 14 50 22c-6-2-10 2-8 8-8-2-12-4-14-8z" fill="#5F7F53"/><circle cx="24" cy="24" r="4" fill="#B9412F"/><circle cx="31" cy="25" r="4" fill="#B9412F"/><circle cx="27" cy="18" r="3.5" fill="#cf5340"/></svg>'
def mug(body,ink,i):
    return f'<svg viewBox="0 0 120 150" aria-hidden="true"><path d="M60 0v16" stroke="#8f5330" stroke-width="4" stroke-linecap="round"/><path d="M60 16c-6 0-8 6-4 10" fill="none" stroke="#8f5330" stroke-width="3"/><path d="M92 58c22 0 22 40 0 40" fill="none" stroke="{body}" stroke-width="10"/><path d="M18 30h76l-6 100c-1 10-7 14-16 14H40c-9 0-15-4-16-14z" fill="{body}"/><path d="M20 46h72" stroke="rgba(0,0,0,.12)" stroke-width="3"/></svg>'
mugs="".join(f'<a class="mug" href="#">{mug(b,k,i)}<b>{n[0].upper()+n[1:]}</b></a>' for i,((b,k),n) in enumerate(zip(MUGC,WHO)))
plates="".join(f'<a class="plate" href="#"><div class="rim"><img src="{U(p,360,360)}" alt="{n}"></div><span>{n.split()[0]}</span></a>' for n,p,_ in BF)
rows2="".join(f'<article class="row"><img src="{U(p,360,360)}" alt=""><div><h3>{n}</h3><p>{d}</p></div><a href="#">Check today\'s price on Amazon</a></article>' for n,p,d in BF)
b2=f"""<div class="disc">As an Amazon Associate we earn from qualifying purchases.</div>
<header><div class="wm">The Cozy Edit</div><nav><a href="#">Gift guides</a><a href="#">Black Friday</a><a href="#">About us</a></nav></header>
<section class="room" id="room"><button class="lamp" onclick="document.getElementById('room').classList.toggle('off')" aria-label="Turn the lamp on or off">{lamp}</button><div class="glow"></div>{holly.replace('<svg','<svg class="holly"',1)}
<div class="copy"><h1>Gifts worth waiting for</h1><p class="lede">We set the table early this year. These are the bigger presents we'd hold out for, ready for Black Friday on November 27.</p><a class="btn" href="#">See the Black Friday list</a><p class="hint">20 days to go</p></div>
<div class="table"><div class="runner"></div><div class="plates">{plates}</div></div></section>
<section class="who"><h2>Who are you shopping for?</h2><p class="sub">Grab a mug. Each one has a short list behind it.</p><div class="rail"></div><div class="mugs">{mugs}</div></section>
<section class="picks"><h2>On the table this week</h2>{rows2}</section>
<p class="foot">Photos show similar items, not the exact product. We don't list prices because they change daily.</p>"""
open('lamp.html','w').write(page('family=Gloock&family=Karla:wght@400;700',c2,b2))

for n in ['shelf','lamp']:
    open(f'view-{n}.html','w').write(f'<!doctype html><html><head><meta name="robots" content="noindex"><style>body{{margin:0;background:#777;display:flex;gap:20px;padding:20px;align-items:flex-start}}iframe{{border:0;box-shadow:0 4px 30px rgba(0,0,0,.4)}}</style></head><body><iframe src="{n}.html" width="1000" height="1600"></iframe><iframe src="{n}.html" width="390" height="1600"></iframe></body></html>')
