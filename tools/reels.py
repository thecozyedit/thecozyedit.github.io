"""Vertical 9:16 short videos (1080x1920, ~10 s) for Instagram Reels, TikTok and YouTube Shorts.
Black Friday set (Nov 2026): one video per homepage group, using the site's product photos (Unsplash look-alikes).
Usage (repo root): python3 tools/reels.py  -> reels/R00x.mp4 (+ -cover.jpg)"""
import json, os, re, shutil, subprocess, sys

sys.path.insert(0, os.path.dirname(__file__))
from bf_mode import GROUPS, P, NOTE  # same products as the homepage Black Friday list

FPS, SEG, W, H = 30, 2.0, 1080, 1920
OUT = "reels"
SPECS = [  # id, group name, headline line 1, italic line 2
    ("R001", "Kitchen", "Kitchen upgrades", "worth the wait"),
    ("R002", "Comfort and sleep", "Sleep and comfort", "worth the wait"),
    ("R003", "Tech", "Small tech", "worth the wait"),
    ("R004", "Self-care", "Self-care", "worth the wait"),
]


def photo(url, w, h):
    return re.sub(r"w=\d+&h=\d+", f"w={w}&h={h}", url).replace("q=72", "q=80")


def page(h1, h2, asins):
    n = len(asins)
    slides = ""
    for i, a in enumerate(asins):
        p, d = P[a], i * SEG
        first = ";opacity:1;animation:none" if i == 0 else ""
        slides += (f'<div class="s" style="--d:{d}s{first}"><img src="{photo(p["img"], 1000, 1150)}" style="--d:{d}s">'
                   f'<span class="pill" style="--d:{d + .3}s">{p["name"]}</span></div>')
    end = n * SEG
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,wght@0,400;0,500;1,400&family=Karla:wght@400;700&display=swap" rel="stylesheet">
<style>*{{box-sizing:border-box;margin:0}}
body{{width:{W}px;height:{H}px;overflow:hidden;background:#1A1310 radial-gradient(ellipse 85% 700px at 50% 0,rgba(230,183,131,.2),transparent 70%) no-repeat;color:#EFE4D3;font-family:Karla,sans-serif;padding:150px 70px 120px;display:flex;flex-direction:column}}
.k{{font-family:'Bodoni Moda',serif;font-style:italic;font-size:44px;color:#E6B783;text-align:center}}
h1{{font-family:'Bodoni Moda',serif;font-weight:400;font-size:96px;line-height:1.03;text-align:center;margin:14px 0 54px}}h1 i{{color:#E6B783}}
.stage{{position:relative;flex:1;border-radius:480px 480px 14px 14px;overflow:hidden;background:#261C17}}
.s{{position:absolute;inset:0;opacity:0;animation:fade .6s ease-out var(--d) forwards}}
.s img{{width:100%;height:100%;object-fit:cover;display:block;animation:zoom 2.8s linear var(--d) forwards}}
.pill{{position:absolute;left:22px;bottom:22px;background:rgba(26,19,16,.88);font-family:'Bodoni Moda',serif;font-size:44px;padding:12px 24px;border-radius:22px;opacity:0;transform:translateY(14px);animation:up .5s ease-out var(--d) forwards}}
.endc{{position:absolute;inset:0;background:rgba(26,19,16,.8);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px;opacity:0;animation:fade .6s ease-out {end}s forwards}}
.endc p{{font-family:'Bodoni Moda',serif;font-size:70px;text-align:center;line-height:1.1}}.endc p i{{color:#E6B783}}
.endc span{{border:3px solid #C4865A;border-radius:999px;padding:18px 38px;font-weight:700;font-size:38px}}
.f{{display:flex;justify-content:center;margin-top:44px}}
.f b{{font-family:'Bodoni Moda',serif;font-style:italic;font-weight:400;font-size:46px}}
@keyframes fade{{to{{opacity:1}}}}@keyframes up{{to{{opacity:1;transform:none}}}}@keyframes zoom{{from{{transform:scale(1)}}to{{transform:scale(1.08)}}}}
</style></head><body>
<p class="k">Worth buying on Black Friday</p><h1>{h1}<br><i>{h2}</i></h1>
<div class="stage">{slides}<div class="endc"><p>Our full<br><i>Black Friday list</i></p><span>Link in bio</span></div></div>
<div class="f"><b>The Cozy Edit</b></div></body></html>"""


def render(pg, vid, html, dur):
    tmp = f"/tmp/reel_{vid}"
    shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    pg.set_content(html, wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
    frames = int(FPS * dur)
    for f in range(frames):
        pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={f * 1000 / FPS})")
        pg.screenshot(path=f"{tmp}/{f:04d}.jpg", type="jpeg", quality=90)
    os.makedirs(OUT, exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{tmp}/%04d.jpg",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-movflags", "+faststart", f"{OUT}/{vid}.mp4"], check=True)
    shutil.copy(f"{tmp}/{int(FPS * 0.5):04d}.jpg", f"{OUT}/{vid}-cover.jpg")
    shutil.rmtree(tmp)


if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    groups = dict(GROUPS)
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width": W, "height": H})
        for vid, g, h1, h2 in SPECS:
            asins = groups[g]
            render(pg, vid, page(h1, h2, asins), len(asins) * SEG + 2.0)
            print(vid, g)
        b.close()
