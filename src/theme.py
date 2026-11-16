"""Look and section builders for The Cozy Edit. Every function returns an HTML string and escapes its text."""
import html
from urllib.parse import quote
from catalog import Product, link

E = html.escape
D = "As an Amazon Associate we earn from qualifying purchases."
PIN = "https://www.pinterest.com/thecozyedithomegifts/"
CTA = "Check today's price on Amazon"
CTA_SHORT = "See today's price"
GATE = "2026-12-01"
REL = 'target="_blank" rel="sponsored nofollow noopener"'
FONTS_URL = ("https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,wght@0,400;0,500;1,400;1,500"
             "&family=Karla:wght@400;700&display=swap")


def _u(pid: str, w: int, h: int) -> str:
    return f"https://images.unsplash.com/{pid}?auto=format&fit=crop&w={w}&h={h}&q=72"


def photo(p: Product, w: int, h: int, cls: str = "") -> str:
    c = f' class="{cls}"' if cls else ""
    if not p.photo:
        return f'<div class="tile"><i>{E(p.name)}</i></div>'
    return f'<img{c} src="{_u(p.photo, w, h)}" alt="" loading="lazy" data-pin-nopin="true">'


def _gate(gate: str) -> str:
    return {"": "", "until": f' data-until="{GATE}"', "from": f' data-from="{GATE}" hidden'}[gate]


def head(title, description, canonical, og_image, faq_ld: str = "", css_v: str = "1") -> str:
    t, d = E(title), E(description)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:site_name" content="The Cozy Edit">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{canonical}">
<meta name="google-site-verification" content="btfllhklqcuRzarbDspLUAOAM1I31pJbz2E-tKDyL0A" />
<meta name="p:domain_verify" content="0dc319a594b1644f61ebd275b5498a40"/>
<link rel="icon" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS_URL}" rel="stylesheet">
<link rel="stylesheet" href="style.css?v={css_v}">{faq_ld}
</head>
<body>
"""


def header() -> str:
    return f"""<div class="disc">{D}</div>
<header class="top"><nav><a href="index.html#guides">Gift guides</a><a href="black-friday-gift-ideas.html">Black Friday</a></nav><a class="wm" href="index.html">The Cozy Edit</a><nav class="r"><a href="about.html">About us</a></nav></header>
<main>
"""


def footer() -> str:
    return f"""</main>
<p class="foot-note">Photos show similar items, not the exact product. We don't list prices because they change daily.</p>
<footer class="site-footer">
  <p class="wm">The Cozy Edit</p>
  <p>{D} Product details are set by Amazon and can change, so check the listing before you buy.</p>
  <p><a href="about.html">About &amp; disclosure</a><a href="about.html#privacy">Privacy</a><a href="{PIN}" rel="noopener" target="_blank">Follow on Pinterest</a></p>
</footer>
<script>(function(){{if(new Date()<new Date("{GATE}T00:00:00"))return;document.querySelectorAll("[data-until]").forEach(function(e){{e.remove()}});document.querySelectorAll("[data-from]").forEach(function(e){{e.hidden=false}})}})();</script>
<script async defer data-pin-hover="true" data-pin-tall="true" src="https://assets.pinterest.com/js/pinit.js"></script>
</body>
</html>
"""


def bf_line() -> str:
    return f'<p class="bf" data-until="{GATE}">Black Friday is November 27. Our list is ready.</p>'


def window(feat: Product, sides: list, label: str, gate: str = "") -> str:
    side = "".join(
        f'<a href="{link(p.asin)}" {REL}>{photo(p, 700, 580)}<div class="cap"><h3>{E(p.name)}</h3>'
        f'<p>{E(p.note)}</p><span class="pill">{CTA_SHORT}</span></div></a>' for p in sides)
    return (f'<section class="window"{_gate(gate)}><a class="feat" href="{link(feat.asin)}" {REL}>{photo(feat, 1100, 1000)}'
            f'<div class="cap"><small>{E(label)}</small><h2>{E(feat.name)}</h2><p>{E(feat.note)}</p>'
            f'<span class="pill solid">{CTA}</span></div></a><div class="side">{side}</div></section>')


def who_tiles(items: list) -> str:
    return '<div class="who">' + "".join(
        f'<a href="{E(href)}"><img src="{_u(pid, 400, 540)}" alt="" loading="lazy" data-pin-nopin="true"><span>{E(label)}</span></a>'
        for label, href, pid in items) + "</div>"


def product_card(p: Product) -> str:
    return (f'<a class="card" href="{link(p.asin)}" {REL}><div class="ph">{photo(p, 500, 625)}</div>'
            f'<h3>{E(p.name)}</h3><p>{E(p.note)}</p><span class="pill">{CTA}</span></a>')


def compact_row(p: Product) -> str:
    return (f'<a class="compact" href="{link(p.asin)}" {REL}><div class="cph">{photo(p, 160, 160)}</div>'
            f'<div class="ct"><h3>{E(p.name)}</h3><p>{E(p.note)}</p></div><span class="pill">{CTA_SHORT}</span></a>')


def faq(qa: list) -> str:
    if not qa:
        return ""
    return ('<section class="faq"><h2 class="t">Questions people ask</h2>'
            + "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in qa) + "</section>")


def pinbox(url, image, title, desc) -> str:
    d = f"{title}: {desc} {D}"
    share = (f"https://www.pinterest.com/pin/create/button/?url={quote(url, safe='')}"
             f"&media={quote(image, safe='')}&description={quote(d, safe='')}")
    return f"""<section class="pinbox">
  <img src="{image}" alt="Pinnable graphic for {E(title)}" width="1000" height="1500" loading="lazy" data-pin-description="{E(d)}" data-pin-url="{url}">
  <div><h2>Save this list on Pinterest</h2><p>Shopping later? Pin it to a board so it's there when you're ready. We add new gift guides every week.</p>
  <a class="pill solid-alt" href="{E(share)}" target="_blank" rel="noopener" data-pin-do="none">Save to Pinterest</a> <a class="pill" href="{PIN}" target="_blank" rel="noopener">Follow The Cozy Edit</a></div>
</section>"""


def guide_list(guides: list) -> str:
    return ('<section class="sec" id="guides"><h2 class="t">Every gift guide</h2><ul class="guides-list">'
            + "".join(f'<li><a href="{E(s)}.html">{E(t)}</a></li>' for s, t in guides) + "</ul></section>")


CSS = """:root{--esp:#1A1310;--roast:#261C17;--line:#3B2D25;--cream:#EFE4D3;--muted:#B3A08B;--copper:#C4865A;--glow:#E6B783}
*{box-sizing:border-box}img{display:block}a{color:inherit;text-decoration:none}
a:focus-visible,summary:focus-visible{outline:2px solid var(--glow);outline-offset:4px}
body{margin:0;background:var(--esp) radial-gradient(ellipse 70% 560px at 50% 0,rgba(230,183,131,.14),transparent 70%) no-repeat;color:var(--cream);font-family:'Karla',sans-serif;font-size:16px;line-height:1.5;overflow-wrap:break-word}
h1,h2,h3,.wm{font-family:'Bodoni Moda',serif;font-weight:400}
.disc{font-size:12px;text-align:center;padding:9px 16px;color:var(--muted)}
.top{max-width:1240px;margin:0 auto;padding:14px 32px 0;display:grid;grid-template-columns:1fr auto 1fr;align-items:center}
.top .wm{font-size:32px;font-weight:500;font-style:italic}
.top nav{display:flex;gap:26px;font-size:15px;color:var(--muted)}.top nav.r{justify-content:flex-end}.top nav a:hover{color:var(--cream)}
.intro{max-width:1240px;margin:0 auto;padding:46px 32px 30px;display:flex;justify-content:space-between;align-items:flex-end;gap:40px}
.intro h1{font-size:clamp(36px,5vw,64px);line-height:1.06;margin:0;max-width:720px;letter-spacing:-.01em}
h1 i,h2 i{color:var(--glow)}
.intro p{max-width:360px;margin:0;color:var(--muted);line-height:1.6}
.intro p.bf{color:var(--glow);font-size:14px;margin-top:12px}
.window{max-width:1240px;margin:0 auto;padding:0 32px;display:grid;grid-template-columns:1.5fr 1fr;gap:20px}
.window[hidden]{display:none}
.feat,.side a{position:relative;display:block;overflow:hidden;background:var(--roast)}
.feat{border-radius:300px 300px 6px 6px;min-height:600px}.side a{border-radius:6px;min-height:290px}
.feat img,.side img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.2s ease}
.feat .tile,.side .tile{position:absolute;inset:0}
.feat:hover img,.side a:hover img{transform:scale(1.035)}
.feat:after,.side a:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(26,19,16,0) 40%,rgba(26,19,16,.94) 100%)}
.cap{position:absolute;left:0;right:0;bottom:0;padding:32px;z-index:2}
.cap small{color:var(--glow);font-size:14px}
.cap h2{font-size:38px;margin:6px 0 8px;line-height:1.08}
.cap p{margin:0 0 18px;color:#e2d5c3;max-width:460px;line-height:1.55}
.side{display:grid;grid-template-rows:1fr 1fr;gap:20px}
.side .cap{padding:22px}.side .cap h3{font-size:25px;margin:0 0 4px;line-height:1.1}.side .cap p{font-size:15px;margin:0 0 12px}
.pill{display:inline-block;color:var(--cream);border:1px solid var(--copper);border-radius:999px;padding:9px 16px;font-size:14px;font-weight:700;transition:background .2s,color .2s}
a:hover .pill,a.pill:hover{background:var(--copper);color:var(--esp)}
.pill.solid,.pill.solid-alt{background:var(--copper);color:var(--esp);border-color:var(--copper);padding:13px 22px;font-size:15px}
a:hover .pill.solid,.pill.solid-alt:hover{background:var(--glow);border-color:var(--glow)}
.tile{display:flex;align-items:center;justify-content:center;text-align:center;background:var(--roast);padding:16px;width:100%;height:100%;min-height:100%}
.tile i{font-family:'Bodoni Moda',serif;font-size:22px;color:var(--glow);line-height:1.2}
.sec{max-width:1240px;margin:0 auto;padding:100px 32px 0}
h2.t{font-size:44px;margin:0 0 6px;text-align:center;line-height:1.1}
.sub{text-align:center;color:var(--muted);margin:0 0 36px}
.who{display:grid;grid-template-columns:repeat(6,1fr);gap:14px}
.who.three{grid-template-columns:repeat(3,1fr)}
.who a{position:relative;display:block;overflow:hidden;border-radius:6px;background:var(--roast)}
.who img{width:100%;aspect-ratio:3/4;object-fit:cover;filter:brightness(.72) saturate(.9);transition:filter .4s,transform 1s}
.who.three img{aspect-ratio:4/3}
.who a:hover img{filter:brightness(.92);transform:scale(1.04)}
.who span{position:absolute;left:8px;right:8px;bottom:14px;text-align:center;font-family:'Bodoni Moda',serif;font-style:italic;font-size:23px;line-height:1.15}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:44px 22px}
.card{display:block;text-align:center;min-width:0}
.card .ph{overflow:hidden;border-radius:140px 140px 6px 6px;background:var(--roast);aspect-ratio:4/5}
.card img{width:100%;height:100%;object-fit:cover;transition:transform 1s}
.card:hover img{transform:scale(1.05)}
.card h3{font-weight:500;font-size:20px;margin:16px 0 4px;line-height:1.2}
.card p{margin:0 auto 14px;color:var(--muted);font-size:15px;line-height:1.5;max-width:250px}
.compacts{max-width:860px;margin:0 auto}
.compact{display:grid;grid-template-columns:72px 1fr auto;gap:18px;align-items:center;padding:16px 0;border-top:1px solid var(--line)}
.cph{width:72px;height:72px;border-radius:50%;overflow:hidden}.cph img{width:100%;height:100%;object-fit:cover}
.cph .tile{padding:6px}.cph .tile i{font-size:11px}
.compact h3{font-size:20px;margin:0 0 2px;font-weight:500}.compact p{margin:0;color:var(--muted);font-size:15px}
.compact:hover h3{color:var(--glow)}
.how{max-width:720px;margin:0 auto;text-align:center;color:var(--muted);font-size:17px;line-height:1.7}
.faq{max-width:760px;margin:0 auto;padding:100px 32px 0}
.faq details{border-top:1px solid var(--line);padding:18px 4px}.faq details:last-child{border-bottom:1px solid var(--line)}
.faq summary{cursor:pointer;font-family:'Bodoni Moda',serif;font-size:21px}
.faq details p{margin:10px 0 0;color:var(--muted)}
.pinbox{max-width:900px;margin:100px auto 0;padding:0 32px;display:grid;grid-template-columns:220px 1fr;gap:36px;align-items:center}
.pinbox img{width:100%;height:auto;border-radius:6px}
.pinbox h2{font-size:34px;margin:0 0 10px}.pinbox p{color:var(--muted);margin:0 0 20px}
.guides-list{list-style:none;padding:0;margin:30px auto 0;max-width:980px;columns:3;column-gap:40px}
.guides-list li{break-inside:avoid;border-top:1px solid var(--line)}
.guides-list a{display:block;padding:12px 0;font-family:'Bodoni Moda',serif;font-size:19px}
.guides-list a:hover{color:var(--glow)}
.about{max-width:1100px;margin:0 auto;padding:46px 32px 0;display:grid;grid-template-columns:1fr 1.1fr;gap:56px;align-items:center}
.about .ph{border-radius:300px 300px 6px 6px;overflow:hidden}.about .ph img{width:100%;aspect-ratio:4/5;object-fit:cover}
.about h1{font-size:clamp(36px,4.6vw,58px);margin:0 0 20px;line-height:1.06}
.about p,.prose p{color:#dccdb9;line-height:1.7;font-size:17px}
.prose{max-width:720px;margin:0 auto;padding:80px 32px 0}.prose h2{font-size:32px}
.foot-note{text-align:center;color:var(--muted);font-size:13px;padding:90px 32px 0;margin:0}
.site-footer{max-width:1240px;margin:30px auto 0;padding:30px 32px 50px;border-top:1px solid var(--line);text-align:center;color:var(--muted);font-size:14px}
.site-footer .wm{font-style:italic;font-size:24px;color:var(--cream);margin:0 0 8px}
.site-footer a{margin:0 12px;color:var(--glow)}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
@media(max-width:900px){
.top{grid-template-columns:1fr;text-align:center;padding:12px 20px 0;gap:6px}.top .wm{order:-1}.top nav,.top nav.r{justify-content:center;gap:20px;font-size:14px}
.top{display:flex;flex-wrap:wrap;justify-content:center;column-gap:20px}.top .wm{width:100%}
.intro{flex-direction:column;align-items:flex-start;padding:24px 20px 22px;gap:14px}
.window{grid-template-columns:1fr;padding:0 20px;gap:12px}.feat{border-radius:200px 200px 6px 6px;min-height:470px}
.side{grid-template-rows:none;grid-template-columns:1fr 1fr;gap:12px}.side a{min-height:250px}.side .cap{padding:12px}.side .cap h3{font-size:18px}.side .cap p{display:none}.side .pill{font-size:12px;padding:7px 10px}
.cap{padding:22px}.cap h2{font-size:30px}
.sec{padding:76px 20px 0}h2.t{font-size:32px}
.who{grid-template-columns:none;grid-auto-flow:column;grid-auto-columns:42%;overflow-x:auto;scroll-snap-type:x mandatory;margin:0 -20px;padding:0 20px}.who a{scroll-snap-align:start}.who span{font-size:20px}
.who.three{grid-auto-columns:70%}
.grid{grid-template-columns:1fr 1fr;gap:32px 12px}.card h3{font-size:17px}.card p{font-size:14px}.card .pill{font-size:12px;padding:8px 10px}
.tile i{font-size:17px}
.compact{grid-template-columns:60px 1fr;gap:14px}.cph{width:60px;height:60px}.compact .pill{grid-column:2;justify-self:start;font-size:12px;padding:7px 12px}.compact h3{font-size:18px}
.faq{padding:76px 20px 0}.faq summary{font-size:18px}
.pinbox{grid-template-columns:110px 1fr;gap:18px;padding:0 20px;margin-top:76px}.pinbox h2{font-size:24px}.pinbox .pill{margin-top:8px}
.guides-list{columns:1}
.about{grid-template-columns:1fr;padding:24px 20px 0;gap:28px}.about .ph{border-radius:200px 200px 6px 6px}
.prose{padding:60px 20px 0}.foot-note{padding:70px 20px 0}.site-footer{padding:26px 20px 40px}.site-footer a{display:inline-block;margin:4px 8px}}
"""
