U=lambda p,w=600,h=600: f"https://images.unsplash.com/{p}?auto=format&fit=crop&w={w}&h={h}&q=72"
WHO=[("Her","photo-1674475760738-8c7af859f821"),("Him","photo-1787724777367-ee027842b62a"),("Mom","photo-1531981936561-347fb37a966a"),("Homebodies","photo-1764425172300-d97c21f6043f"),("Coffee lovers","photo-1620051787208-a45bc64e32ff"),("The always cold","photo-1511401139252-f158d3209c17")]
FEAT=("Breville espresso machine","photo-1620051787208-a45bc64e32ff","For the person quietly spending a fortune at the café. It grinds, tamps and steams milk, right on the counter.")
SIDE=[("Kindle Paperwhite","photo-1676107779594-7a23bd99e07c","No glare, and the battery lasts for weeks."),
      ("Ninja air fryer","photo-1774074645537-f72f70d40d12","Crispy fries on a Tuesday, without heating the kitchen.")]
GRID=[("Sherpa throw blanket","photo-1770795945978-ac37aea6053b","The one everyone fights over on movie night."),
      ("Ember smart mug","photo-1514228742587-6b1558fcca3d","Keeps coffee hot for the slow sipper."),
      ("Enameled Dutch oven","photo-1682996055064-599bec77fc62","For Sunday stews and no-knead bread."),
      ("Candle gift set","photo-1612293905607-b003de9e54fb","Four winter scents for long evenings."),
      ("Plush fleece robe","photo-1770294759101-fae1377d4d34","Hotel-soft, for slow mornings."),
      ("Whiskey glasses set","photo-1767541865141-e4abf72e9dbc","Heavy-bottomed glasses that feel good in hand."),
      ("Gooseneck kettle","photo-1592417766326-088bf3da80c5","For the pour-over perfectionist."),
      ("Heated throw","photo-1511401139252-f158d3209c17","Warm in minutes, for the always cold.")]
CTA="Check today's price on Amazon"
def page(fonts,css,body,js=""):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>The Cozy Edit sample</title><link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet"><style>*{{box-sizing:border-box}}img{{display:block}}a{{color:inherit;text-decoration:none}}a:focus-visible{{outline:2px solid #E2B07A;outline-offset:4px}}@media (prefers-reduced-motion:reduce){{*{{transition:none!important;animation:none!important}}}}{css}</style></head><body>{body}<script>{js}</script></body></html>'''

# ===== S1: SHOP WINDOW AFTER DARK (Newsreader + Hanken Grotesk) =====
c1=""":root{--esp:#1E1612;--roast:#2A1F19;--line:#3A2C24;--cream:#F0E6D8;--muted:#B9A794;--copper:#C98B5E;--glow:#E2B07A;--sage:#8C9A80}
body{margin:0;background:var(--esp);color:var(--cream);font-family:'Hanken Grotesk',sans-serif;font-size:16px}
.disc{font-size:12px;text-align:center;padding:9px;color:var(--muted);border-bottom:1px solid var(--line)}
header{max-width:1240px;margin:0 auto;padding:22px 32px;display:flex;justify-content:space-between;align-items:baseline}
.wm{font-family:'Newsreader',serif;font-size:28px;font-weight:400;letter-spacing:-.01em}.wm em{color:var(--glow)}
nav{display:flex;gap:30px;font-size:15px;color:var(--muted)}nav a:hover{color:var(--cream)}
.intro{max-width:1240px;margin:0 auto;padding:30px 32px 26px;display:flex;justify-content:space-between;align-items:flex-end;gap:40px}
h1{font-family:'Newsreader',serif;font-weight:300;font-size:clamp(40px,5vw,66px);line-height:1.04;margin:0;letter-spacing:-.015em;max-width:700px}
h1 i{font-weight:300}
.intro p{max-width:340px;margin:0;color:var(--muted);line-height:1.6;font-size:16px}
.bf{display:inline-block;margin-top:12px;color:var(--glow);font-size:14px}
.window{max-width:1240px;margin:0 auto;padding:0 32px;display:grid;grid-template-columns:1.55fr 1fr;gap:20px}
.feat,.side a{position:relative;display:block;overflow:hidden;border-radius:4px;background:var(--roast)}
.feat img{width:100%;height:100%;min-height:560px;object-fit:cover;transition:transform 1.2s ease}
.feat:hover img,.side a:hover img{transform:scale(1.035)}
.feat:after,.side a:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(30,22,18,0) 45%,rgba(30,22,18,.92) 100%)}
.cap{position:absolute;left:0;right:0;bottom:0;padding:30px;z-index:2}
.cap small{color:var(--glow);font-size:13px}
.cap h2{font-family:'Newsreader',serif;font-weight:400;font-size:38px;margin:6px 0 8px;line-height:1.05}
.cap p{margin:0 0 18px;color:#e2d5c3;max-width:440px;line-height:1.55}
.btn{display:inline-block;background:var(--cream);color:var(--esp);font-weight:600;font-size:15px;padding:13px 20px;border-radius:3px;transition:background .2s}
.feat:hover .btn,.btn:hover{background:var(--glow)}
.side{display:grid;grid-template-rows:1fr 1fr;gap:20px}
.side img{width:100%;height:100%;min-height:270px;object-fit:cover;transition:transform 1.2s ease}
.side .cap{padding:22px}.side .cap h2{font-size:26px;margin:0 0 4px}.side .cap p{font-size:15px;margin:0 0 10px}
.ul{font-weight:600;font-size:14px;border-bottom:1px solid var(--copper);padding-bottom:2px}
.sec{max-width:1240px;margin:0 auto;padding:96px 32px 0}
.sec-h{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:26px;gap:20px}
.sec-h h2{font-family:'Newsreader',serif;font-weight:300;font-size:42px;margin:0;letter-spacing:-.01em}
.sec-h a{color:var(--muted);font-size:15px}.sec-h a:hover{color:var(--cream)}
.who{display:grid;grid-template-columns:repeat(6,1fr);gap:14px}
.who a{position:relative;display:block;overflow:hidden;border-radius:4px}
.who img{width:100%;aspect-ratio:3/4;object-fit:cover;filter:brightness(.78) saturate(.9);transition:filter .4s,transform 1s}
.who a:hover img{filter:brightness(.95);transform:scale(1.04)}
.who span{position:absolute;left:14px;bottom:12px;font-family:'Newsreader',serif;font-size:22px;font-style:italic}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:34px 20px}
.card{display:block}
.card .ph{overflow:hidden;border-radius:4px;background:var(--roast)}
.card img{width:100%;aspect-ratio:4/5;object-fit:cover;transition:transform 1s}
.card:hover img{transform:scale(1.04)}
.card h3{font-family:'Newsreader',serif;font-weight:400;font-size:21px;margin:14px 0 4px}
.card p{margin:0 0 10px;color:var(--muted);font-size:15px;line-height:1.5}
.card .ul{color:var(--cream)}
.note{max-width:1240px;margin:0 auto;padding:90px 32px 50px;color:var(--muted);font-size:13px;display:flex;justify-content:space-between;gap:20px;border-top:1px solid var(--line);margin-top:90px;padding-top:26px}
@media(max-width:900px){header{padding:18px 20px}nav{display:none}.intro{flex-direction:column;align-items:flex-start;padding:18px 20px 22px;gap:14px}.window{grid-template-columns:1fr;padding:0 20px;gap:14px}.feat img{min-height:440px}.side{grid-template-rows:none;grid-template-columns:1fr 1fr;gap:14px}.side img{min-height:240px}.side .cap{padding:14px}.side .cap h2{font-size:20px}.side .cap p{display:none}.cap{padding:20px}.cap h2{font-size:30px}
.sec{padding:70px 20px 0}.sec-h h2{font-size:32px}.who{grid-template-columns:none;grid-auto-flow:column;grid-auto-columns:42%;overflow-x:auto;scroll-snap-type:x mandatory;margin:0 -20px;padding:0 20px}.who a{scroll-snap-align:start}.grid{grid-template-columns:1fr 1fr;gap:28px 14px}.card h3{font-size:18px}.card p{font-size:14px}.note{flex-direction:column;padding:26px 20px 40px}}"""
side="".join(f'<a href="#"><img src="{U(p,700,560)}" alt=""><div class="cap"><h2>{n}</h2><p>{d}</p><span class="ul">{CTA}</span></div></a>' for n,p,d in SIDE)
who1="".join(f'<a href="#"><img src="{U(p,400,540)}" alt=""><span>{n}</span></a>' for n,p in WHO)
grid1="".join(f'<a class="card" href="#"><div class="ph"><img src="{U(p,500,625)}" alt=""></div><h3>{n}</h3><p>{d}</p><span class="ul">{CTA}</span></a>' for n,p,d in GRID)
b1=f"""<div class="disc">As an Amazon Associate we earn from qualifying purchases.</div>
<header><div class="wm">The Cozy <em>Edit</em></div><nav><a href="#">Gift guides</a><a href="#">Black Friday</a><a href="#">About us</a></nav></header>
<section class="intro"><h1>Gifts for the people who'd rather <i>stay in</i></h1><div><p>We pick things we'd actually give: warm, useful, and good for a quiet night at home.</p><span class="bf">Black Friday is November 27. Our list is ready.</span></div></section>
<section class="window"><a class="feat" href="#"><img src="{U(FEAT[1],1100,900)}" alt=""><div class="cap"><small>Our Black Friday pick</small><h2>{FEAT[0]}</h2><p>{FEAT[2]}</p><span class="btn">{CTA}</span></div></a><div class="side">{side}</div></section>
<section class="sec"><div class="sec-h"><h2>Who are you shopping for?</h2><a href="#">All gift guides</a></div><div class="who">{who1}</div></section>
<section class="sec"><div class="sec-h"><h2>What we keep coming back to</h2><a href="#">See the full list</a></div><div class="grid">{grid1}</div></section>
<div class="note"><span>Photos show similar items, not the exact product.</span><span>We don't list prices because they change daily.</span></div>"""
import os; os.makedirs('out',exist_ok=True)
open('out/window.html','w').write(page('family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300;1,6..72,400&family=Hanken+Grotesk:wght@400;600',c1,b1))

# ===== S2: SUPPER CLUB (Bodoni Moda + Karla), menu-like, lamp-lit =====
c2=""":root{--esp:#1A1310;--roast:#261C17;--line:#3B2D25;--cream:#EFE4D3;--muted:#B3A08B;--copper:#C4865A;--glow:#E6B783;--wine:#7A2E2A;--olive:#7E8A63}
body{margin:0;background:var(--esp) radial-gradient(ellipse 70% 520px at 50% 0,rgba(230,183,131,.13),transparent 70%) no-repeat;color:var(--cream);font-family:'Karla',sans-serif;font-size:16px}
.disc{font-size:12px;text-align:center;padding:9px;color:var(--muted)}
header{max-width:1240px;margin:0 auto;padding:16px 32px 0;display:grid;grid-template-columns:1fr auto 1fr;align-items:center}
.wm{font-family:'Bodoni Moda',serif;font-size:30px;font-weight:500;font-style:italic;text-align:center}
nav{display:flex;gap:26px;font-size:15px;color:var(--muted)}nav.r{justify-content:flex-end}nav a:hover{color:var(--cream)}
.hero{max-width:1240px;margin:0 auto;padding:54px 32px 0;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.hero .ph{position:relative;border-radius:200px 200px 4px 4px;overflow:hidden;display:block}
.hero .ph img{width:100%;aspect-ratio:4/5;object-fit:cover;transition:transform 1.2s}
.hero .ph:hover img{transform:scale(1.03)}
.sprig{position:absolute;right:18px;top:18px;background:rgba(26,19,16,.8);color:var(--glow);font-size:13px;padding:7px 12px;border-radius:999px}
.k{color:var(--glow);font-size:15px;margin:0 0 14px}
h1{font-family:'Bodoni Moda',serif;font-weight:400;font-size:clamp(40px,4.8vw,64px);line-height:1.06;margin:0 0 18px;letter-spacing:-.01em}
h1 i{color:var(--glow)}
.lede{color:#dccdb9;line-height:1.65;font-size:17px;max-width:470px;margin:0 0 26px}
.pick{display:flex;gap:16px;align-items:center;padding:16px 0;border-top:1px solid var(--line)}
.pick img{width:74px;height:74px;object-fit:cover;border-radius:50%}
.pick b{font-family:'Bodoni Moda',serif;font-weight:500;font-size:19px;display:block}
.pick small{color:var(--muted);font-size:14px}
.pick .go{margin-left:auto;white-space:nowrap;font-weight:700;font-size:14px;color:var(--glow)}
.pick:hover b{color:var(--glow)}
.btn{display:inline-block;margin-top:22px;background:var(--copper);color:var(--esp);font-weight:700;padding:14px 24px;border-radius:999px}.btn:hover{background:var(--glow)}
.sec{max-width:1240px;margin:0 auto;padding:110px 32px 0}
.sec h2{font-family:'Bodoni Moda',serif;font-weight:400;font-size:44px;margin:0 0 8px;text-align:center}
.sec .sub{text-align:center;color:var(--muted);margin:0 0 40px}
.names{display:grid;grid-template-columns:1.1fr 1fr;gap:50px;align-items:center}
.names ul{list-style:none;margin:0;padding:0}
.names li a{display:flex;justify-content:space-between;align-items:baseline;padding:14px 0;border-bottom:1px solid var(--line);font-family:'Bodoni Moda',serif;font-style:italic;font-size:34px;color:#cbbba6;transition:color .25s,padding .25s}
.names li a small{font-family:'Karla',sans-serif;font-style:normal;font-size:14px;color:var(--muted)}
.names li a:hover,.names li a.on{color:var(--cream);padding-left:10px}
.names .show{position:relative;border-radius:4px;overflow:hidden;aspect-ratio:4/5}
.names .show img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .5s}
.names .show img.on{opacity:1}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:40px 22px}
.card{display:block;text-align:center}
.card .ph{overflow:hidden;border-radius:120px 120px 4px 4px;background:var(--roast)}
.card img{width:100%;aspect-ratio:4/5;object-fit:cover;transition:transform 1s}
.card:hover img{transform:scale(1.05)}
.card h3{font-family:'Bodoni Moda',serif;font-weight:500;font-size:20px;margin:16px 0 4px}
.card p{margin:0 auto 12px;color:var(--muted);font-size:15px;line-height:1.5;max-width:240px}
.card .go{display:inline-block;font-weight:700;font-size:14px;border:1px solid var(--copper);border-radius:999px;padding:9px 16px;transition:background .2s,color .2s}
.card:hover .go{background:var(--copper);color:var(--esp)}
.note{text-align:center;color:var(--muted);font-size:13px;padding:90px 32px 50px}
@media(max-width:900px){header{grid-template-columns:1fr;padding:12px 20px 0}nav{display:none}.hero{grid-template-columns:1fr;padding:26px 20px 0;gap:30px}.hero .ph{border-radius:160px 160px 4px 4px}
.sec{padding:80px 20px 0}.sec h2{font-size:34px}.names{grid-template-columns:1fr}.names .show{display:none}.names li a{font-size:28px}.grid{grid-template-columns:1fr 1fr;gap:30px 14px}.card h3{font-size:17px}.card p{font-size:14px}.card .go{font-size:13px;padding:8px 12px}}"""
picks="".join(f'<a class="pick" href="#"><img src="{U(p,160,160)}" alt=""><span><b>{n}</b><small>{d}</small></span><span class="go">See price</span></a>' for n,p,d in SIDE)
names="".join(f'<li><a href="#" data-i="{i}"{" class=on" if i==0 else ""}>{n}<small>Gift guide</small></a></li>' for i,(n,p) in enumerate(WHO))
shows="".join(f'<img src="{U(p,700,875)}" alt=""{" class=on" if i==0 else ""}>' for i,(n,p) in enumerate(WHO))
grid2="".join(f'<a class="card" href="#"><div class="ph"><img src="{U(p,500,625)}" alt=""></div><h3>{n}</h3><p>{d}</p><span class="go">{CTA}</span></a>' for n,p,d in GRID)
b2=f"""<div class="disc">As an Amazon Associate we earn from qualifying purchases.</div>
<header><nav><a href="#">Gift guides</a><a href="#">Black Friday</a></nav><div class="wm">The Cozy Edit</div><nav class="r"><a href="#">About us</a></nav></header>
<section class="hero"><a class="ph" href="#"><img src="{U(FEAT[1],900,1125)}" alt="Espresso machine on a kitchen counter"><span class="sprig">Saved for Black Friday</span></a>
<div><p class="k">Black Friday is November 27</p><h1>The good stuff, <i>worth the wait</i></h1><p class="lede">{FEAT[2]} It's the one we'd hold out for. Here are two more on our list.</p>
<a class="pick" href="#"><img src="{U(FEAT[1],160,160)}" alt=""><span><b>{FEAT[0]}</b><small>Our top pick this year</small></span><span class="go">See price</span></a>{picks}
<a class="btn" href="#">See the whole Black Friday list</a></div></section>
<section class="sec"><h2>Who's on your list?</h2><p class="sub">Choose someone and we'll show you what we'd give them.</p><div class="names"><ul>{names}</ul><div class="show">{shows}</div></div></section>
<section class="sec"><h2>What we keep coming back to</h2><p class="sub">Cozy, useful, and easy to love.</p><div class="grid">{grid2}</div></section>
<p class="note">Photos show similar items, not the exact product. We don't list prices because they change daily.</p>"""
js2="""document.querySelectorAll('.names a').forEach(a=>a.addEventListener('mouseenter',()=>{const i=+a.dataset.i;document.querySelectorAll('.names a').forEach((x,j)=>x.classList.toggle('on',j==i));document.querySelectorAll('.show img').forEach((x,j)=>x.classList.toggle('on',j==i))}))"""
open('out/supper.html','w').write(page('family=Bodoni+Moda:ital,wght@0,400;0,500;1,400;1,500&family=Karla:wght@400;700',c2,b2,js2))
for n in ['window','supper']:
    open(f'out/view-{n}.html','w').write(f'<!doctype html><html><head><meta name="robots" content="noindex"><style>body{{margin:0;background:#777;display:flex;gap:20px;padding:20px;align-items:flex-start}}iframe{{border:0;box-shadow:0 4px 30px rgba(0,0,0,.4)}}</style></head><body><iframe src="{n}.html" width="1000" height="1600"></iframe><iframe src="{n}.html" width="390" height="1600"></iframe></body></html>')
