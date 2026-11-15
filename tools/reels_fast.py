"""Fast-cut 9:16 TikTok style: 1-second hook, hard cuts every ~0.5 s, zoom punches, big captions.
Usage (repo root): python3 tools/reels_fast.py [group]  -> reels/F00x.mp4"""
import json, os, re, shutil, subprocess, sys

sys.path.insert(0, os.path.dirname(__file__))
from bf_mode import GROUPS, P

FPS, W, H = 30, 1080, 1920
SPECS = [("F001", "Kitchen", "4 kitchen things worth buying this Black Friday"),
         ("F002", "Comfort and sleep", "4 sleep upgrades worth buying this Black Friday"),
         ("F003", "Tech", "4 small tech finds worth buying this Black Friday"),
         ("F004", "Self-care", "4 self-care things worth buying this Black Friday")]


def photo(url):
    return re.sub(r"w=\d+&h=\d+", "w=1080&h=1920", url).replace("q=72", "q=80")


def page(hook, items):
    data = json.dumps([{"img": photo(P[a]["img"]), "name": P[a]["name"]} for a in items])
    return """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Bodoni+Moda:ital@1&display=swap" rel="stylesheet">
<style>*{margin:0;box-sizing:border-box}body{width:1080px;height:1920px;overflow:hidden;background:#000;font-family:'Archivo Black',sans-serif}
#bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
#shade{position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.15),rgba(0,0,0,0) 40%,rgba(0,0,0,.55))}
#cap{position:absolute;left:60px;right:60px;top:300px;text-align:center;color:#fff;font-size:104px;line-height:1.02;text-shadow:0 6px 30px rgba(0,0,0,.6)}
#cap span{background:#fff;color:#111;padding:0 18px;box-decoration-break:clone;-webkit-box-decoration-break:clone;line-height:1.25}
#num{position:absolute;top:150px;left:0;right:0;text-align:center;color:#FFD84D;font-size:150px;text-shadow:0 6px 30px rgba(0,0,0,.6)}
#name{position:absolute;left:60px;right:60px;bottom:330px;text-align:center}
#name span{background:#FFD84D;color:#111;font-size:76px;padding:6px 22px;line-height:1.35;box-decoration-break:clone;-webkit-box-decoration-break:clone}
#brand{position:absolute;bottom:150px;left:0;right:0;text-align:center;color:#fff;font:italic 46px 'Bodoni Moda',serif;text-shadow:0 2px 12px #000}
#end{position:absolute;inset:0;background:#111;display:none;flex-direction:column;align-items:center;justify-content:center;color:#fff;text-align:center;gap:50px}
#end b{font-size:110px;line-height:1.05}#end i{background:#FFD84D;color:#111;font-style:normal;font-size:70px;padding:10px 30px}
</style></head><body><img id="bg"><div id="shade"></div><div id="num"></div><div id="cap"></div><div id="name"></div><div id="brand">The Cozy Edit</div>
<div id="end"><b>Full Black<br>Friday list</b><i>Link in bio</i></div>
<script>
const D=""" + data + """,HOOK=""" + json.dumps(hook) + """;
D.forEach(d=>{const i=new Image();i.src=d.img});
const HOOKT=1.0,PER=1.1,ENDT=1.4;window.TOTAL=HOOKT+D.length*PER+ENDT;
function show(t){const bg=document.getElementById('bg'),cap=document.getElementById('cap'),num=document.getElementById('num'),nm=document.getElementById('name'),end=document.getElementById('end');
 end.style.display='none';
 if(t<HOOKT){bg.src=D[0].img;const k=Math.min(t/0.12,1);cap.style.transform=`scale(${1.35-0.35*k})`;cap.innerHTML='<span>'+HOOK+'</span>';num.textContent='';nm.innerHTML='';bg.style.transform=`scale(${1.25-0.1*t})`;bg.style.filter='brightness(.6)';return}
 const u=t-HOOKT,i=Math.floor(u/PER);
 if(i>=D.length){end.style.display='flex';const k=Math.min((u-D.length*PER)/0.12,1);end.firstChild.style.transform=`scale(${1.3-0.3*k})`;return}
 const s=u-i*PER,half=s>=PER/2,k=Math.min((half?s-PER/2:s)/0.15,1);
 bg.src=D[i].img;bg.style.filter='none';
 bg.style.transformOrigin=half?'30% 40%':'50% 50%';
 bg.style.transform=half?`scale(${1.6-0.15*k})`:`scale(${1.25-0.2*k+0.03*s})`;
 cap.innerHTML='';num.textContent=(i+1)+'/'+D.length;num.style.transform=`scale(${1.4-0.4*Math.min(s/0.12,1)})`;
 nm.innerHTML='<span>'+D[i].name+'</span>';}
</script></body></html>"""


def render(pg, vid, html):
    tmp = f"/tmp/fast_{vid}"
    shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    pg.set_content(html, wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(800)
    total = pg.evaluate("TOTAL")
    for f in range(int(total * FPS)):
        pg.evaluate(f"show({f / FPS})")
        pg.screenshot(path=f"{tmp}/{f:04d}.jpg", type="jpeg", quality=90)
    os.makedirs("reels", exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{tmp}/%04d.jpg", "-c:v", "libx264",
                    "-pix_fmt", "yuv420p", "-crf", "20", "-movflags", "+faststart", f"reels/{vid}.mp4"], check=True)
    shutil.copy(f"{tmp}/0010.jpg", f"reels/{vid}-cover.jpg")
    shutil.rmtree(tmp)


if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    want = sys.argv[1:] or [s[0] for s in SPECS]
    groups = dict(GROUPS)
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width": W, "height": H})
        for vid, g, hook in SPECS:
            if vid in want:
                render(pg, vid, page(hook, groups[g])); print(vid)
        b.close()
