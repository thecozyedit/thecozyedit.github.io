"""Guide pins (H pins) redrawn in the site's late-night-kitchen look, with product photos.
Same headlines, product rotation and file names as render.py, so the pin plan doesn't change.
Usage: python3 render2.py [from_date]   (default 2026-11-09) -> /home/claude/thecozyedit.github.io/pins/v/<img>.jpg"""
import html, json, os, sys
sys.path.insert(0, "/home/claude/site")
from data import G
from config import C
import render as R
from catalog import load

CAT = load()
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,wght@0,400;0,500;1,400&family=Karla:wght@400;700&display=swap" rel="stylesheet">'
U = lambda p, w, h: f"https://images.unsplash.com/{p}?auto=format&fit=crop&w={w}&h={h}&q=80"
E = html.escape


def items(slug, rot):
    """(display name, photo) pairs in the same rotated order render.py uses for names."""
    names = [R.FIX.get(x, x) for x in R.names(slug)]
    asins = G[slug]["asins"]
    pairs = [(n, CAT.products[a].photo if a in CAT.products else None) for n, a in zip(names, asins)]
    k = rot % len(pairs)
    pairs = pairs[k:] + pairs[:k]
    return [p for p in pairs if p[1]] + [p for p in pairs if not p[1]]


BASE = """*{box-sizing:border-box;margin:0}
body{width:1000px;height:1500px;overflow:hidden;background:#1A1310 radial-gradient(ellipse 85% 560px at 50% 0,rgba(230,183,131,.18),transparent 70%) no-repeat;color:#EFE4D3;font-family:Karla,sans-serif}
.pin{width:1000px;height:1500px;padding:66px 64px 54px;display:flex;flex-direction:column}
.k{font-family:'Bodoni Moda',serif;font-style:italic;font-size:34px;color:#E6B783;text-align:center}
h1{font-family:'Bodoni Moda',serif;font-weight:400;font-size:var(--hs,84px);line-height:1.04;text-align:center;margin:12px 0 40px}h1 i{color:#E6B783}
.main{flex:1;display:flex;flex-direction:column;min-height:0}
.f{display:flex;justify-content:space-between;align-items:center;margin-top:34px}
.f b{font-family:'Bodoni Moda',serif;font-style:italic;font-weight:400;font-size:36px}
.cta{border:2px solid #C4865A;border-radius:999px;padding:12px 26px;font-weight:700;font-size:26px}
.ph{background:#261C17;overflow:hidden}.ph img{width:100%;height:100%;object-fit:cover;display:block}
.pill{position:absolute;left:14px;bottom:14px;background:rgba(26,19,16,.88);font-family:'Bodoni Moda',serif;font-size:27px;line-height:1.2;padding:7px 15px;border-radius:16px;max-width:calc(100% - 28px)}
.more{font-size:26px;color:#B3A08B;text-align:center;margin-top:18px}"""


def head(h):
    e, l1, l2 = h
    size = 84 if max(len(l1), len(l2)) <= 18 else (72 if max(len(l1), len(l2)) <= 23 else 62)
    return f'<p class="k">{E(e)}</p><h1 style="--hs:{size}px">{E(l1)}<br><i>{E(l2)}</i></h1>'


def foot():
    return '<div class="f"><b>thecozyedit.github.io</b><span class="cta">See the full list</span></div>'


def L_list(it, n):
    rows = "".join(f'<div class="r"><div class="ph c"><img src="{U(p,240,240)}"></div><span>{E(x)}</span></div>' for x, p in it[:5])
    css = ".r{display:flex;align-items:center;gap:28px;padding:16px 0;border-top:1px solid #3B2D25}.r:first-child{border-top:0}.c{width:132px;height:132px;border-radius:50%;flex:none}.r span{font-family:'Bodoni Moda',serif;font-size:42px;line-height:1.15}"
    return css, f'<div>{rows}</div><p class="more">+ {n-5} more in the full guide</p>'


def L_hook(it, n):
    (a, pa), rest = it[0], it[1:4]
    css = ".hero{position:relative;flex:1;border-radius:440px 440px 12px 12px}.names{font-family:'Bodoni Moda',serif;font-size:34px;text-align:center;margin-top:24px;color:#E6B783}"
    names = " &middot; ".join(E(x) for x, _ in rest)
    return css, f'<div class="ph hero"><img src="{U(pa,900,1000)}"><span class="pill">{E(a)}</span></div><p class="names">Also: {names}</p>'


def L_tiles(it, n):
    tiles = "".join(f'<div class="ph t"><img src="{U(p,500,500)}"><span class="pill">{E(x)}</span></div>' for x, p in it[:4])
    css = ".g{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:16px}.t{position:relative;border-radius:12px}"
    return css, f'<div class="g">{tiles}</div>'


def L_check(it, n):
    cells = "".join(f'<div class="cell"><div class="ph s"><img src="{U(p,360,360)}"></div><span>{E(x)}</span></div>' for x, p in it[:6])
    css = ".g{flex:1;display:grid;grid-template-columns:1fr 1fr 1fr;gap:26px 18px;align-content:start}.s{aspect-ratio:1;border-radius:150px 150px 10px 10px}.cell span{display:block;font-family:'Bodoni Moda',serif;font-size:28px;line-height:1.2;text-align:center;margin-top:12px}"
    return css, f'<div class="g">{cells}</div><p class="more">+ {n-6} more in the full guide</p>'


LAY = {"list": L_list, "hook": L_hook, "tiles": L_tiles, "check": L_check, "big": L_hook}


def page(slug, hi, lay, rot):
    it = items(slug, rot)
    css, body = LAY[lay](it, C[slug]["n"])
    return (f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{BASE}{css}</style></head><body><div class="pin">'
            f'{head(C[slug]["hl"][hi])}<div class="main">{body}</div>{foot()}</div></body></html>')


def jobs_from(date):
    """(img name, slug, hi, lay, rot) for scheduled pins from `date`; rot matches the job tuples render.py used."""
    sched = json.load(open("/home/claude/holiday/schedule.json"))
    out = []
    for x in sched:
        if x["date"] >= date:
            rot = int(x["img"].rsplit("-", 1)[1][2:] or 0)
            out.append((x["img"], x["slug"], x["hi"], x["lay"], rot))
    return out


if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    date = sys.argv[1] if len(sys.argv) > 1 else "2026-11-09"
    only = sys.argv[2].split(",") if len(sys.argv) > 2 else None
    out = os.environ.get("OUT", "/home/claude/thecozyedit.github.io/pins/v")
    jobs = [j for j in jobs_from(date) if not only or j[0] in only]
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1000, "height": 1500})
        for name, slug, hi, lay, rot in jobs:
            pg.set_content(page(slug, hi, lay, rot), wait_until="networkidle")
            pg.evaluate("document.fonts.ready")
            pg.screenshot(path=f"{out}/{name}.jpg", type="jpeg", quality=88)
        b.close()
    print(len(jobs), "pins rendered")
