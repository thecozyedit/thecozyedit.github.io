"""'3 Cozy Finds' spotlight pins (S001–S010): three product photos + guide link, in the site's late-night kitchen look.
Render: python3 spotlight.py  (needs images.unsplash.com reachable). Output: /home/claude/thecozyedit.github.io/pins/s/S0xx.jpg"""
import os, sys
sys.path.insert(0, "/home/claude/site")
from catalog import load

SITE = "https://thecozyedit.github.io/"
# (id, guide slug, headline line 1, headline italic line 2, product names to feature [3, by catalog name])
SPECS = [
    ("S001", "homebody-gifts", "3 cozy finds for the", "homebody", None),
    ("S002", "gifts-for-someone-always-cold", "3 gifts for the friend who's", "always cold", None),
    ("S003", "black-friday-gift-ideas", "3 gifts worth waiting", "for Black Friday", None),
    ("S004", "gifts-for-coffee-lovers", "3 finds for the", "coffee lover", None),
    ("S005", "gifts-for-mom-who-has-everything", "3 gifts for the mom who", "has everything", None),
    ("S006", "gifts-for-him", "3 cozy gifts", "for him", None),
    ("S007", "gifts-for-her", "3 cozy gifts", "for her", None),
    ("S008", "stocking-stuffers-for-women", "3 stocking stuffers", "she'll actually use", None),
    ("S009", "cozy-christmas-gifts", "3 cozy finds for a", "slow Christmas morning", None),
    ("S010", "home-cook-gifts", "3 gifts for the", "home cook", None),
]

U = lambda p, w, h: f"https://images.unsplash.com/{p}?auto=format&fit=crop&w={w}&h={h}&q=80"


def html(head1, head2, prods):
    a, b, c = prods
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,wght@0,400;0,500;1,400&family=Karla:wght@400;700&display=swap" rel="stylesheet">
<style>*{{box-sizing:border-box;margin:0}}body{{width:1000px;height:1500px;background:#1A1310 radial-gradient(ellipse 80% 520px at 50% 0,rgba(230,183,131,.18),transparent 70%) no-repeat;color:#EFE4D3;font-family:Karla,sans-serif;padding:70px 64px 56px;display:flex;flex-direction:column}}
.k{{font-family:'Bodoni Moda',serif;font-style:italic;font-size:34px;color:#E6B783;text-align:center}}
h1{{font-family:'Bodoni Moda',serif;font-weight:400;font-size:76px;line-height:1.05;text-align:center;margin:10px 0 44px}}h1 i{{color:#E6B783}}
.g{{display:grid;grid-template-columns:1.15fr 1fr;grid-template-rows:1fr 1fr;gap:18px;flex:1}}
.c{{position:relative;overflow:hidden;background:#261C17}}.c img{{width:100%;height:100%;object-fit:cover;display:block}}
.c1{{grid-row:span 2;border-radius:420px 420px 10px 10px}}.c2,.c3{{border-radius:10px}}
.c span{{position:absolute;left:16px;bottom:16px;background:rgba(26,19,16,.86);color:#EFE4D3;font-family:'Bodoni Moda',serif;font-size:30px;padding:8px 18px;border-radius:999px}}
.f{{display:flex;justify-content:space-between;align-items:center;margin-top:40px;font-size:26px;color:#B3A08B}}
.f b{{font-family:'Bodoni Moda',serif;font-style:italic;font-weight:400;font-size:36px;color:#EFE4D3}}
.cta{{border:2px solid #C4865A;border-radius:999px;padding:12px 26px;color:#EFE4D3;font-weight:700}}</style></head><body>
<p class="k">The Cozy Edit</p><h1>{head1}<br><i>{head2}</i></h1>
<div class="g"><div class="c c1"><img src="{U(a.photo,700,1100)}"><span>{a.name}</span></div>
<div class="c c2"><img src="{U(b.photo,600,520)}"><span>{b.name}</span></div>
<div class="c c3"><img src="{U(c.photo,600,520)}"><span>{c.name}</span></div></div>
<div class="f"><b>thecozyedit.github.io</b><span class="cta">See the full list</span></div></body></html>"""


def picks(c, slug, names):
    g = next(g for g in c.guides if g.slug == slug)
    pool = [c.products[a] for a in g.main + g.more if c.products[a].photo]
    if names:
        pool = [p for n in names for p in pool if p.name == n] + pool
    out, seen = [], set()
    for p in pool:
        if p.photo not in seen:
            out.append(p); seen.add(p.photo)
        if len(out) == 3:
            return out


if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    c = load()
    out = "/home/claude/thecozyedit.github.io/pins/s"
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1000, "height": 1500})
        for sid, slug, h1, h2, names in SPECS:
            pg.set_content(html(h1, h2, picks(c, slug, names)), wait_until="networkidle")
            pg.wait_for_timeout(800)
            pg.screenshot(path=f"{out}/{sid}.jpg", type="jpeg", quality=90)
            print(sid, slug)
        b.close()
