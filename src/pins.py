import json, re, html, subprocess, os
import importlib.util
spec = importlib.util.spec_from_file_location("b", "/home/claude/site/build.py")
# pull GUIDES + ICONS without running the site build: exec only the definitions
src = open("/home/claude/site/build.py").read()
ns = {}
exec(src.split("def link(")[0].replace('os.makedirs(OUT, exist_ok=True)',''), ns)
GUIDES, ICONS, items = ns["GUIDES"], ns["ICONS"], ns["items"]

THEMES = [  # bg, panel, ink, accent
 ("#EFE4D6", "#FBF6EF", "#3B2A20", "#B5623B"),
 ("#3B2A20", "#4A372B", "#F5EDE2", "#E3A47A"),
 ("#E7D3C2", "#F8EFE6", "#3B2A20", "#9C4F2F"),
 ("#5E6B57", "#6C7A64", "#F5EFE3", "#E6C79A"),
]
HEAD = {
 "gifts-for-her": ("Cozy Gifts", "for Her"),
 "homebody-gifts": ("Gifts for", "Homebodies"),
 "kitchen-gifts-for-her": ("Kitchen Gifts", "for Her"),
 "home-cook-gifts": ("Gifts for the", "Home Cook"),
 "stocking-stuffers-for-women": ("Stocking Stuffers", "for Women"),
 "housewarming-gifts": ("Housewarming", "Gift Ideas"),
 "cozy-christmas-gifts": ("Cozy Christmas", "Gift Ideas"),
 "beauty-stocking-stuffers": ("At-Home Beauty", "Stocking Stuffers"),
}
os.makedirs("/home/claude/logowork/pins", exist_ok=True)
pages = []
for gi, (slug, board, title, intro, meta, ic) in enumerate(GUIDES):
    picks = [o for o in items if o["board"] == board]
    bg, panel, ink, acc = THEMES[gi % len(THEMES)]
    l1, l2 = HEAD[slug]
    rows = "".join(f'<li><span class="n">{i+1:02d}</span>{html.escape(o["title"])}</li>' for i, o in enumerate(picks[:6]))
    more = f'<p class="more">+ {len(picks)-6} more ideas inside</p>' if len(picks) > 6 else ''
    svg = f'<svg width="120" height="120" viewBox="0 0 24 24" fill="none" stroke="{ink}" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round">{ICONS[ic]}</svg>'
    pages.append((slug, f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:F;font-weight:500;src:url(node_modules/@fontsource/fraunces/files/fraunces-latin-500-normal.woff2)}}
@font-face{{font-family:F;font-style:italic;font-weight:400;src:url(node_modules/@fontsource/fraunces/files/fraunces-latin-400-italic.woff2)}}
@font-face{{font-family:I;font-weight:500;src:url(node_modules/@fontsource/inter/files/inter-latin-500-normal.woff2)}}
body{{margin:0}}
.pin{{width:1000px;height:1500px;background:{bg};color:{ink};font-family:F,Georgia,serif;box-sizing:border-box;padding:80px 76px 70px;display:flex;flex-direction:column;position:relative;overflow:hidden}}
.top{{display:flex;justify-content:space-between;align-items:flex-start}}
.eyebrow{{font-family:I,sans-serif;font-size:28px;letter-spacing:6px;text-transform:uppercase;color:{acc}}}
h1{{font-weight:500;font-size:118px;line-height:.98;margin:34px 0 0;letter-spacing:-1.5px}}
h1 em{{font-style:italic;font-weight:400}}
.panel{{background:{panel};border-radius:36px;padding:46px 50px;margin-top:56px;flex:1}}
ul{{list-style:none;margin:0;padding:0}}
li{{font-size:44px;line-height:1.2;padding:17px 0;border-bottom:2px solid {ink}22;display:flex;gap:26px;align-items:baseline}}
li:last-child{{border-bottom:0}}
.n{{font-family:I,sans-serif;font-size:28px;color:{acc};min-width:44px}}
.more{{font-family:I,sans-serif;font-size:28px;margin:22px 0 0;color:{acc}}}
.foot{{display:flex;justify-content:space-between;align-items:center;margin-top:44px;font-family:I,sans-serif;font-size:28px;letter-spacing:1px}}
.brand{{font-family:F,serif;font-size:42px}}
.brand em{{font-style:italic;font-weight:400}}
</style></head><body><div class="pin">
<div class="top"><div><div class="eyebrow">Gift guide · {len(picks)} picks</div>
<h1>{html.escape(l1)}<br><em>{html.escape(l2)}</em></h1></div>{svg}</div>
<div class="panel"><ul>{rows}</ul>{more}</div>
<div class="foot"><span class="brand"><em>the</em> Cozy Edit</span><span>thecozyedit.github.io</span></div>
</div></body></html>"""))
for slug, h in pages:
    open(f"/home/claude/logowork/pin_{slug}.html", "w").write(h)
js = """const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1000,height:1500}});
for(const s of %s){await p.goto('file:///home/claude/logowork/pin_'+s+'.html');await p.waitForTimeout(300);await p.locator('.pin').screenshot({path:'/home/claude/logowork/pins/Guide_Pin_'+s+'.png'});}
await b.close();})();""" % json.dumps([s for s, _ in pages])
open("/home/claude/logowork/pinshot.js", "w").write(js)
subprocess.run(["node", "pinshot.js"], cwd="/home/claude/logowork", check=True)
print(os.listdir("/home/claude/logowork/pins"))
