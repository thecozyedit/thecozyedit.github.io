import gen
from gen import U, WHO, FEAT, SIDE, CTA, page
GRID=list(gen.GRID)
GRID[0]=("Fuzzy memory foam slippers","photo-1543420629-5350879dd4cd","Soft, warm, and made for padding around at night.")
GRID[1]=("Holiday mug","photo-1606394784750-28e68c1e6c7e","For the first cocoa of the season.")
css=""":root{--esp:#1A1310;--roast:#261C17;--line:#3B2D25;--cream:#EFE4D3;--muted:#B3A08B;--copper:#C4865A;--glow:#E6B783}
body{margin:0;background:var(--esp) radial-gradient(ellipse 70% 560px at 50% 0,rgba(230,183,131,.14),transparent 70%) no-repeat;color:var(--cream);font-family:'Karla',sans-serif;font-size:16px}
.disc{font-size:12px;text-align:center;padding:9px;color:var(--muted)}
header{max-width:1240px;margin:0 auto;padding:14px 32px 0;display:grid;grid-template-columns:1fr auto 1fr;align-items:center}
.wm{font-family:'Bodoni Moda',serif;font-size:32px;font-weight:500;font-style:italic}
nav{display:flex;gap:26px;font-size:15px;color:var(--muted)}nav.r{justify-content:flex-end}nav a:hover{color:var(--cream)}
.intro{max-width:1240px;margin:0 auto;padding:46px 32px 30px;display:flex;justify-content:space-between;align-items:flex-end;gap:40px}
h1{font-family:'Bodoni Moda',serif;font-weight:400;font-size:clamp(40px,5vw,64px);line-height:1.06;margin:0;max-width:720px;letter-spacing:-.01em}
h1 i{color:var(--glow)}
.intro p{max-width:340px;margin:0;color:var(--muted);line-height:1.6}
.bf{display:inline-block;margin-top:12px;color:var(--glow);font-size:14px}
.window{max-width:1240px;margin:0 auto;padding:0 32px;display:grid;grid-template-columns:1.5fr 1fr;gap:20px}
.feat,.side a{position:relative;display:block;overflow:hidden;background:var(--roast)}
.feat{border-radius:300px 300px 6px 6px}
.side a{border-radius:6px}
.feat img{width:100%;height:100%;min-height:600px;object-fit:cover;transition:transform 1.2s ease}
.side img{width:100%;height:100%;min-height:290px;object-fit:cover;transition:transform 1.2s ease}
.feat:hover img,.side a:hover img{transform:scale(1.035)}
.feat:after,.side a:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(26,19,16,0) 45%,rgba(26,19,16,.93) 100%)}
.cap{position:absolute;left:0;right:0;bottom:0;padding:32px;z-index:2}
.cap small{color:var(--glow);font-size:14px}
.cap h2{font-family:'Bodoni Moda',serif;font-weight:400;font-size:38px;margin:6px 0 8px;line-height:1.08}
.cap p{margin:0 0 18px;color:#e2d5c3;max-width:460px;line-height:1.55}
.pill{display:inline-block;background:var(--copper);color:var(--esp);font-weight:700;font-size:15px;padding:13px 22px;border-radius:999px;transition:background .2s}
.feat:hover .pill{background:var(--glow)}
.side{display:grid;grid-template-rows:1fr 1fr;gap:20px}
.side .cap{padding:22px}.side .cap h2{font-size:25px;margin:0 0 4px}.side .cap p{font-size:15px;margin:0 0 12px}
.pill.o{background:transparent;color:var(--cream);border:1px solid var(--copper);padding:9px 16px;font-size:14px;transition:background .2s,color .2s}
a:hover .pill.o{background:var(--copper);color:var(--esp)}
.sec{max-width:1240px;margin:0 auto;padding:100px 32px 0}
.sec h2.t{font-family:'Bodoni Moda',serif;font-weight:400;font-size:44px;margin:0 0 6px;text-align:center}
.sec .sub{text-align:center;color:var(--muted);margin:0 0 36px}
.who{display:grid;grid-template-columns:repeat(6,1fr);gap:14px}
.who a{position:relative;display:block;overflow:hidden;border-radius:6px}
.who img{width:100%;aspect-ratio:3/4;object-fit:cover;filter:brightness(.72) saturate(.9);transition:filter .4s,transform 1s}
.who a:hover img{filter:brightness(.92);transform:scale(1.04)}
.who span{position:absolute;left:0;right:0;bottom:14px;text-align:center;font-family:'Bodoni Moda',serif;font-style:italic;font-size:23px}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:44px 22px}
.card{display:block;text-align:center}
.card .ph{overflow:hidden;border-radius:140px 140px 6px 6px;background:var(--roast)}
.card img{width:100%;aspect-ratio:4/5;object-fit:cover;transition:transform 1s}
.card:hover img{transform:scale(1.05)}
.card h3{font-family:'Bodoni Moda',serif;font-weight:500;font-size:20px;margin:16px 0 4px}
.card p{margin:0 auto 14px;color:var(--muted);font-size:15px;line-height:1.5;max-width:250px}
.more{text-align:center;margin-top:44px}.more a{color:var(--glow);border-bottom:1px solid var(--copper);padding-bottom:2px}
.note{text-align:center;color:var(--muted);font-size:13px;padding:90px 32px 50px}
@media(max-width:900px){header{grid-template-columns:1fr;text-align:center;padding:12px 20px 0}nav{display:none}.intro{flex-direction:column;align-items:flex-start;padding:24px 20px 22px;gap:14px}
.window{grid-template-columns:1fr;padding:0 20px;gap:14px}.feat{border-radius:200px 200px 6px 6px}.feat img{min-height:470px}.side{grid-template-rows:none;grid-template-columns:1fr 1fr;gap:12px}.side img{min-height:250px}.side .cap{padding:12px}.side .cap h2{font-size:19px}.side .cap p{display:none}.side .pill.o{font-size:12px;padding:7px 10px}.cap{padding:22px}.cap h2{font-size:30px}
.sec{padding:76px 20px 0}.sec h2.t{font-size:32px}.who{grid-template-columns:none;grid-auto-flow:column;grid-auto-columns:42%;overflow-x:auto;scroll-snap-type:x mandatory;margin:0 -20px;padding:0 20px}.who a{scroll-snap-align:start}
.grid{grid-template-columns:1fr 1fr;gap:32px 12px}.card h3{font-size:17px}.card p{font-size:14px}.card .pill.o{font-size:12px;padding:8px 10px}}"""
side="".join(f'<a href="#"><img src="{U(p,700,580)}" alt=""><div class="cap"><h2>{n}</h2><p>{d}</p><span class="pill o">See today\'s price</span></div></a>' for n,p,d in SIDE)
who="".join(f'<a href="#"><img src="{U(p,400,540)}" alt=""><span>{n}</span></a>' for n,p in WHO)
grid="".join(f'<a class="card" href="#"><div class="ph"><img src="{U(p,500,625)}" alt=""></div><h3>{n}</h3><p>{d}</p><span class="pill o">{CTA}</span></a>' for n,p,d in GRID)
body=f"""<div class="disc">As an Amazon Associate we earn from qualifying purchases.</div>
<header><nav><a href="#">Gift guides</a><a href="#">Black Friday</a></nav><div class="wm">The Cozy Edit</div><nav class="r"><a href="#">About us</a></nav></header>
<section class="intro"><h1>Gifts for the people who'd rather <i>stay in</i></h1><div><p>We pick things we'd actually give: warm, useful, and good for a quiet night at home.</p><span class="bf">Black Friday is November 27. Our list is ready.</span></div></section>
<section class="window"><a class="feat" href="#"><img src="{U(FEAT[1],1100,1000)}" alt=""><div class="cap"><small>Our Black Friday pick</small><h2>{FEAT[0]}</h2><p>{FEAT[2]}</p><span class="pill">{CTA}</span></div></a><div class="side">{side}</div></section>
<section class="sec"><h2 class="t">Who are you shopping for?</h2><p class="sub">Pick someone and we'll show you what we'd give them.</p><div class="who">{who}</div></section>
<section class="sec"><h2 class="t">What we keep coming back to</h2><p class="sub">Cozy, useful, and easy to love.</p><div class="grid">{grid}</div><p class="more"><a href="#">See every gift guide</a></p></section>
<p class="note">Photos show similar items, not the exact product. We don't list prices because they change daily.</p>"""
open('out/mix.html','w').write(page('family=Bodoni+Moda:ital,wght@0,400;0,500;1,400;1,500&family=Karla:wght@400;700',css,body))
open('out/view-mix.html','w').write('<!doctype html><html><head><meta name="robots" content="noindex"><style>body{margin:0;background:#777;display:flex;gap:20px;padding:20px;align-items:flex-start}iframe{border:0;box-shadow:0 4px 30px rgba(0,0,0,.4)}</style></head><body><iframe src="mix.html" width="1000" height="1600"></iframe><iframe src="mix.html" width="390" height="1600"></iframe></body></html>')
