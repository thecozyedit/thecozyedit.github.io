import json, re, html, os
from PIL import Image
OUT = "/home/claude/site/dist"
os.makedirs(OUT, exist_ok=True)
TAG = "cozeyditweb-20"
PIN = "https://www.pinterest.com/thecozyedithomegifts/"
D = "As an Amazon Associate I earn from qualifying purchases."

items = json.load(open("/home/claude/phase2/plan.json")) + json.load(open("/home/claude/phase3/plan2.json"))

def blurb(o):
    d = o["description"]
    d = d.replace(" " + D, "").replace(D, "")
    d = re.sub(r"^.*?\(affiliate link\):\s*", "", d) if "(affiliate link)" in d else d.split(": ", 1)[-1]
    return d.strip()

GUIDES = [
 ("gifts-for-her", "Cozy Gifts for Her", "Cozy Gifts for Her", "Soft, warm and a little indulgent. Gifts for the women on your list who love a slow night in.", "Cozy gift ideas for her: throws, silk pillowcases, robes, bath sets and more picks for wives, moms, sisters and friends.", "blanket"),
 ("homebody-gifts", "Gifts for Homebodies", "Gifts for Homebodies", "For the people who'd always rather stay in. Comfort upgrades for reading, lounging and long weekends at home.", "Gift ideas for homebodies and introverts: weighted blankets, book lights, puzzles, tea and cozy loungewear.", "home"),
 ("kitchen-gifts-for-her", "Kitchen Gifts for Her", "Kitchen Gifts for Her", "Pretty, useful kitchen finds for coffee lovers, matcha drinkers and anyone who likes a well-stocked counter.", "Kitchen gift ideas for her: milk frothers, gooseneck kettles, coffee makers, matcha sets and countertop upgrades.", "cup"),
 ("home-cook-gifts", "Gifts for the Home Cook", "Gifts for the Home Cook", "Tools that make everyday cooking easier, from a trusty skillet to gadgets they'll use every week.", "Gift ideas for home cooks: cast iron skillets, meat thermometers, knife sets, Instant Pot and spice organizers.", "pan"),
 ("stocking-stuffers-for-women", "Stocking Stuffers for Women", "Stocking Stuffers for Women", "Small, giftable favorites that fit in a stocking and actually get used.", "Stocking stuffer ideas for women: lip masks, hand cream sets, tumblers, cocoa bombs and other small gifts.", "stocking"),
 ("housewarming-gifts", "Housewarming Gift Ideas", "Housewarming Gift Ideas", "Easy, thoughtful gifts for a new home or a first apartment.", "Housewarming gift ideas: charcuterie boards, oil dispensers, reed diffusers, pillow covers and more for new homeowners.", "key"),
 ("cozy-christmas-gifts", "Cozy Christmas Gift Ideas", "Cozy Christmas Gift Ideas", "Holiday-ready picks for movie nights, Christmas morning and the whole countdown to the 25th.", "Cozy Christmas gift ideas: winter candles, holiday mugs, cocoa sets, Christmas pajamas, advent calendars and decor.", "tree"),
 ("beauty-stocking-stuffers", "At-Home Beauty Stocking Stuffers", "At-Home Beauty Stocking Stuffers", "Salon-style results at home. Beauty and self-care gifts she'll reach for every day.", "At-home beauty gift ideas and stocking stuffers: press-on nails, heatless curls, gel nail kits, face masks and more.", "sparkle"),
]

ICONS = {
 "blanket": '<path d="M4 7h16v10H4z"/><path d="M4 11h16M8 7v10"/><path d="M16 17c0 1.5 1 2 2 2"/>',
 "home": '<path d="M3.5 11 12 4l8.5 7"/><path d="M5.5 9.5V20h13V9.5"/><path d="M10 20v-5h4v5"/>',
 "cup": '<path d="M5 11h12v5a4 4 0 0 1-4 4H9a4 4 0 0 1-4-4z"/><path d="M17 12.5h1.5a2 2 0 0 1 0 4H17"/><path d="M9 3c-.8 1.2.8 2.3 0 3.5"/><path d="M12.5 3c-.8 1.2.8 2.3 0 3.5"/>',
 "pan": '<circle cx="10" cy="12" r="6"/><path d="M16 12h6"/>',
 "stocking": '<path d="M9 3h6v9l3 3a3 3 0 0 1-4.2 4.2L9 14.5z"/><path d="M9 6h6"/>',
 "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12 20 3M17 6l2 2M15 8l2 2"/>',
 "tree": '<path d="M12 3 6 11h3l-4 6h14l-4-6h3z"/><path d="M12 17v4"/>',
 "sparkle": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 16l.7 1.8 1.8.7-1.8.7L19 21l-.7-1.8-1.8-.7 1.8-.7z"/>',
}
def icon(k, size=28):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[k]}</svg>'

def link(asin):
    return f"https://www.amazon.com/dp/{asin}?tag={TAG}"

def head(title, desc, path):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="logo.png">
<link rel="icon" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;1,9..144,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="disclosure">{D} Links on this site go to Amazon.</div>
<header class="site-header">
  <a class="brand" href="index.html"><img src="logo.png" alt="" width="44" height="44"><span><em>the</em> Cozy Edit</span></a>
  <nav><a href="index.html#guides">Gift guides</a><a href="about.html">About</a><a href="{PIN}" rel="noopener" target="_blank">Pinterest</a></nav>
</header>
<main>
"""

FOOT = f"""</main>
<footer class="site-footer">
  <p><strong>The Cozy Edit</strong> · Cozy home and gift ideas for everyone on your list.</p>
  <p>{D} Product availability and details are set by Amazon and can change; check the listing before you buy.</p>
  <p><a href="about.html">About &amp; disclosure</a> · <a href="about.html#privacy">Privacy</a> · <a href="{PIN}" rel="noopener" target="_blank">Follow on Pinterest</a></p>
</footer>
</body>
</html>
"""

def card(o, i):
    return f"""<article class="pick">
  <div class="num">{i:02d}</div>
  <div class="pick-body">
    <h3>{html.escape(o['title'])}</h3>
    <p class="prod">{html.escape(o['product'])}</p>
    <p>{html.escape(blurb(o))}</p>
    <a class="btn" href="{link(o['asin'])}" target="_blank" rel="sponsored nofollow noopener">See it on Amazon</a>
  </div>
</article>"""

pages = {}
for slug, board, h1, intro, meta, ic in GUIDES:
    picks = [o for o in items if o["board"] == board]
    body = head(f"{h1} | The Cozy Edit", meta, slug) + f"""
<section class="guide-hero">
  <div class="hero-icon">{icon(ic, 40)}</div>
  <p class="eyebrow">Gift guide · {len(picks)} picks</p>
  <h1>{html.escape(h1)}</h1>
  <p class="lede">{html.escape(intro)}</p>
</section>
<section class="picks">
{chr(10).join(card(o, i+1) for i, o in enumerate(picks))}
</section>
<section class="more">
  <h2>More gift guides</h2>
  <div class="chips">{''.join(f'<a href="{s}.html">{html.escape(t)}</a>' for s,_,t,*_ in GUIDES if s != slug)}</div>
</section>
""" + FOOT
    pages[slug] = (body, len(picks))

cards = "\n".join(f"""<a class="guide-card" href="{s}.html">
  <div class="gc-icon">{icon(ic)}</div>
  <h3>{html.escape(t)}</h3>
  <p>{html.escape(intro)}</p>
  <span class="gc-count">{pages[s][1]} picks →</span>
</a>""" for s, b, t, intro, meta, ic in GUIDES)

index = head("The Cozy Edit | Cozy Home & Gift Guides", "Curated cozy home and gift ideas for her, homebodies, home cooks, stocking stuffers, housewarming and Christmas. New gift guides every week.", "index") + f"""
<section class="hero">
  <img src="logo.png" alt="The Cozy Edit logo" width="132" height="132" class="hero-logo">
  <h1>Cozy gifts for <em>everyone</em> on your list</h1>
  <p class="lede">Hand-picked home and gift ideas for homebodies, home cooks, and the women who have everything. Plus stocking stuffers, housewarming gifts and little self-care luxuries.</p>
  <a class="btn btn-lg" href="#guides">Browse the gift guides</a>
</section>
<section id="guides" class="guides">
  <h2>Gift guides</h2>
  <div class="grid">
{cards}
  </div>
</section>
<section class="how">
  <h2>How we pick</h2>
  <div class="how-grid">
    <div><h3>Well loved</h3><p>We favor products with strong ratings from thousands of Amazon shoppers.</p></div>
    <div><h3>Actually useful</h3><p>Gifts people reach for every day, not clutter that ends up in a drawer.</p></div>
    <div><h3>Cozy first</h3><p>Warm, soft, calming, homey. If it doesn't make home nicer, it isn't here.</p></div>
  </div>
</section>
""" + FOOT

about = head("About & Disclosure | The Cozy Edit", "About The Cozy Edit, our Amazon Associates disclosure and privacy notice.", "about") + f"""
<section class="prose">
  <h1>About The Cozy Edit</h1>
  <p>The Cozy Edit is a small, independent gift guide for cozy home finds: the blankets, mugs, kitchen tools and little luxuries that make home feel good. We publish curated guides for the people on your list and share new picks on <a href="{PIN}" target="_blank" rel="noopener">Pinterest</a>.</p>
  <h2 id="disclosure">Affiliate disclosure</h2>
  <p>The Cozy Edit is a participant in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to Amazon.com. {D}</p>
  <p>When you click a link on this site and buy something on Amazon, we may earn a small commission at no extra cost to you. It doesn't change what you pay or which products we feature.</p>
  <p>Prices, availability and product details are set by Amazon and can change at any time. Please check the Amazon listing before you buy.</p>
  <h2 id="privacy">Privacy</h2>
  <p>This site does not ask for or collect your personal information, and it has no sign-up forms or comments. It is hosted on GitHub Pages, which may log basic technical data such as IP addresses for security, as described in GitHub's privacy statement. Fonts are served by Google Fonts.</p>
  <p>When you click through to Amazon, Amazon may set cookies to track the referral and attribute purchases, as described in Amazon's privacy notice. We receive only aggregate reports of clicks and orders, never your name or personal details.</p>
  <p>Questions? Reach us through our Pinterest profile.</p>
</section>
""" + FOOT

CSS = """:root{--cream:#F6EFE6;--sand:#EFE4D6;--brown:#3B2A20;--mid:#6E5646;--line:#E2D5C4;--accent:#B5623B;--accent-d:#8F4A2B;--white:#FFFDF9}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--cream);color:var(--brown);font-family:Inter,system-ui,sans-serif;font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:var(--accent-d)}
h1,h2,h3{font-family:Fraunces,Georgia,serif;font-weight:500;line-height:1.15;margin:0 0 .4em}
h1 em,.brand em{font-style:italic;font-weight:400}
.disclosure{background:var(--brown);color:var(--sand);font-size:13px;text-align:center;padding:8px 16px}
.site-header{max-width:1080px;margin:0 auto;padding:18px 20px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--brown);font-family:Fraunces,Georgia,serif;font-size:22px}
.brand img{border-radius:50%}
nav{display:flex;gap:20px;flex-wrap:wrap}
nav a{color:var(--brown);text-decoration:none;font-weight:500;font-size:15px}
nav a:hover{color:var(--accent)}
main{max-width:1080px;margin:0 auto;padding:0 20px}
.hero{text-align:center;padding:48px 0 56px}
.hero-logo{border-radius:50%;margin-bottom:20px}
.hero h1{font-size:clamp(34px,5.5vw,56px);max-width:760px;margin:0 auto .3em}
.lede{font-size:18px;color:var(--mid);max-width:640px;margin:0 auto 28px}
.btn{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;font-weight:600;font-size:15px;padding:11px 20px;border-radius:999px;transition:background .15s}
.btn:hover{background:var(--accent-d)}
.btn-lg{padding:14px 28px;font-size:16px}
.guides h2,.how h2,.more h2{font-size:30px;margin-bottom:20px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:18px}
.guide-card{display:flex;flex-direction:column;background:var(--white);border:1px solid var(--line);border-radius:16px;padding:22px;text-decoration:none;color:var(--brown);transition:transform .15s,box-shadow .15s}
.guide-card:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(59,42,32,.08)}
.gc-icon,.hero-icon{width:52px;height:52px;border-radius:50%;background:var(--sand);display:flex;align-items:center;justify-content:center;color:var(--brown);margin-bottom:14px}
.guide-card h3{font-size:21px}
.guide-card p{color:var(--mid);font-size:14.5px;margin:0 0 14px;flex:1}
.gc-count{font-weight:600;color:var(--accent-d);font-size:14px}
.how{padding:56px 0 24px}
.how-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:24px}
.how-grid h3{font-size:19px}
.how-grid p{color:var(--mid);margin:0}
.guide-hero{text-align:center;padding:40px 0 32px;border-bottom:1px solid var(--line);margin-bottom:12px}
.hero-icon{width:72px;height:72px;margin:0 auto 14px}
.eyebrow{text-transform:uppercase;letter-spacing:.14em;font-size:12px;font-weight:600;color:var(--mid);margin:0 0 8px}
.guide-hero h1{font-size:clamp(30px,5vw,48px)}
.picks{max-width:760px;margin:0 auto}
.pick{display:flex;gap:20px;padding:26px 0;border-bottom:1px solid var(--line)}
.num{font-family:Fraunces,Georgia,serif;font-size:30px;color:var(--accent);min-width:46px;line-height:1}
.pick h3{font-size:23px;margin-bottom:2px}
.prod{font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--mid);margin:0 0 8px}
.pick p{margin:0 0 14px}
.more{max-width:760px;margin:0 auto;padding:40px 0}
.chips{display:flex;flex-wrap:wrap;gap:10px}
.chips a{background:var(--white);border:1px solid var(--line);border-radius:999px;padding:8px 16px;text-decoration:none;color:var(--brown);font-size:14px;font-weight:500}
.chips a:hover{border-color:var(--accent);color:var(--accent-d)}
.prose{max-width:720px;margin:0 auto;padding:40px 0}
.prose h1{font-size:40px}
.prose h2{font-size:24px;margin-top:1.4em}
.site-footer{border-top:1px solid var(--line);margin-top:48px;padding:28px 20px 40px;text-align:center;font-size:13.5px;color:var(--mid)}
.site-footer p{max-width:720px;margin:6px auto}
@media (max-width:560px){.pick{gap:12px}.num{font-size:24px;min-width:34px}.hero{padding:32px 0 40px}.site-header{justify-content:center}}
"""

open(f"{OUT}/index.html","w").write(index)
open(f"{OUT}/about.html","w").write(about)
for s,(b,_) in pages.items(): open(f"{OUT}/{s}.html","w").write(b)
open(f"{OUT}/style.css","w").write(CSS)
im = Image.open("/mnt/user-data/outputs/The_Cozy_Edit_Logo.png").convert("RGBA")
im.resize((264,264), Image.LANCZOS).save(f"{OUT}/logo.png", optimize=True)
im.resize((64,64), Image.LANCZOS).save(f"{OUT}/favicon.png", optimize=True)
open(f"{OUT}/.nojekyll","w").write("")
print({s:n for s,(b,n) in pages.items()})
