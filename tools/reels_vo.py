"""9:16 TikTok videos with an AI voiceover (Piper TTS, runs offline), text boxes, no zoom.
Each product stays on screen for as long as its voice line takes (min 2.2 s), so the pacing is quick but readable.
Usage (repo root): python3 tools/reels_vo.py [V001 ...] [--voice /path/voice.onnx]  -> reels/V00x.mp4"""
import json, os, re, shutil, subprocess, sys, wave

sys.path.insert(0, os.path.dirname(__file__))
from bf_mode import GROUPS, P

FPS, W, H, MIN_SHOT, PAD = 30, 1080, 1920, 2.2, 0.35
VOICE = os.environ.get("VOICE", "/tmp/voices/en_US-lessac-medium.onnx")
CTA = "Prices change fast, so check today's price. The full list is on screen."
SPECS = {
    "V001": ("Kitchen", "4 kitchen things worth buying this Black Friday",
             "Four kitchen things actually worth buying this Black Friday.",
             ["The Ninja CREAMi. It turns frozen fruit into ice cream.",
              "The Instant Pot. Pressure cooker, slow cooker and rice cooker in one.",
              "Nespresso Vertuo. Coffee and espresso with one button.",
              "A Cuisinart bread maker. Add the ingredients, press start, fresh bread."]),
    "V002": ("Comfort and sleep", "4 sleep upgrades worth buying this Black Friday",
             "Four sleep and comfort upgrades worth buying this Black Friday.",
             ["A weighted blanket. Heavy in the good way, like a hug on movie night.",
              "A heated throw. Warms up in minutes, for anyone who's always cold.",
              "A sunrise alarm clock. It wakes you with light that slowly gets brighter.",
              "Sleep headphones. Thin speakers in a soft headband, comfy for side sleepers."]),
    "V003": ("Tech", "4 small tech finds worth buying this Black Friday",
             "Four small tech finds worth buying this Black Friday.",
             ["The Echo Spot. A small smart alarm clock for your nightstand.",
              "The Ember mug. It keeps your coffee at the exact temperature you like.",
              "A Frameo photo frame. The family sends pictures straight from their phones.",
              "A mug warmer. Keeps coffee warm all morning, then turns itself off."]),
    "V004": ("Self-care", "4 self-care things worth buying this Black Friday",
             "Four self-care things worth buying this Black Friday.",
             ["The Shark LED face mask. Red light at home, a real splurge.",
              "A heated neck massager. Heat and kneading after a long day.",
              "A heated foot massager. For tired feet at the end of the day.",
              "The Revlon hot-air brush. Dries and adds volume in one go."]),
}


def tts(text, path, voice):
    subprocess.run([sys.executable, "-m", "piper", "-m", voice, "-f", path], input=text.encode(), check=True,
                   capture_output=True)
    with wave.open(path) as w:
        return w.getnframes() / w.getframerate()


def photo(url):
    return (re.sub(r"w=\d+&h=\d+", "w=1080&h=1920", url).replace("q=72", "q=80")
            .replace("fit=crop", "fit=crop&crop=entropy"))


PAGE = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Bodoni+Moda:ital@1&display=swap" rel="stylesheet">
<style>*{margin:0;box-sizing:border-box}body{width:1080px;height:1920px;overflow:hidden;background:#000;font-family:'Archivo Black',sans-serif}
#bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
#shade{position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.15),rgba(0,0,0,0) 40%,rgba(0,0,0,.55))}
#cap{position:absolute;left:60px;right:60px;top:300px;text-align:center;color:#111;font-size:100px;line-height:1.25}
#cap span{background:#fff;padding:0 18px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
#num{position:absolute;top:150px;left:0;right:0;text-align:center;color:#FFD84D;font-size:140px;text-shadow:0 6px 30px rgba(0,0,0,.6)}
#name{position:absolute;left:60px;right:60px;bottom:330px;text-align:center}
#name span{background:#FFD84D;color:#111;font-size:76px;padding:6px 22px;line-height:1.35;box-decoration-break:clone;-webkit-box-decoration-break:clone}
#brand{position:absolute;bottom:150px;left:0;right:0;text-align:center;color:#fff;font:italic 46px 'Bodoni Moda',serif;text-shadow:0 2px 12px #000}
#end{position:absolute;inset:0;background:#111;display:none;flex-direction:column;align-items:center;justify-content:center;color:#fff;text-align:center;gap:50px}
#end b{font-size:104px;line-height:1.05}#end i{background:#FFD84D;color:#111;font-style:normal;font-size:62px;padding:10px 30px}
#end small{font-family:sans-serif;font-size:40px;opacity:.8}
</style></head><body><img id="bg"><div id="shade"></div><div id="num"></div><div id="cap"></div><div id="name"></div><div id="brand">The Cozy Edit</div>
<div id="end"><b>Full Black<br>Friday list</b><i>thecozyedit.github.io</i><small>check today's price before you buy</small></div>
<script>
const D=__DATA__,HOOK=__HOOK__,T=__TIMES__;  // T = [hookEnd, item1End, ..., itemNEnd, total]
D.forEach(d=>{const i=new Image();i.src=d.img});
window.TOTAL=T[T.length-1];
function show(t){const bg=document.getElementById('bg'),cap=document.getElementById('cap'),num=document.getElementById('num'),nm=document.getElementById('name'),end=document.getElementById('end');
 end.style.display='none';
 if(t<T[0]){bg.src=D[0].img;bg.style.filter='brightness(.6)';cap.innerHTML='<span>'+HOOK+'</span>';num.textContent='';nm.innerHTML='';return}
 let i=0;while(i<D.length&&t>=T[i+1])i++;
 if(i>=D.length){end.style.display='flex';return}
 bg.src=D[i].img;bg.style.filter='none';cap.innerHTML='';num.textContent=(i+1)+'/'+D.length;nm.innerHTML='<span>'+D[i].name+'</span>';}
</script></body></html>"""


def build(pg, vid, group, hook_text, hook_vo, lines, voice):
    tmp = f"/tmp/vo_{vid}"
    shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    asins = dict(GROUPS)[group]
    # 1) voice lines -> segment lengths
    segs, wavs = [], []
    for k, text in enumerate([hook_vo] + lines + [CTA]):
        wpath = f"{tmp}/l{k}.wav"
        d = tts(text, wpath, voice)
        seg = max(d + PAD, MIN_SHOT if 0 < k <= len(lines) else d + PAD)
        segs.append(seg); wavs.append((wpath, seg))
    times, acc = [], 0.0
    for s in segs:
        acc += s; times.append(round(acc, 3))
    # 2) voice track: each line padded with silence to its segment length
    parts = []
    for k, (wpath, seg) in enumerate(wavs):
        out = f"{tmp}/s{k}.wav"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wpath, "-af", f"apad=whole_dur={seg}",
                        "-ar", "44100", "-ac", "1", out], check=True)
        parts.append(out)
    open(f"{tmp}/a.txt", "w").write("".join(f"file '{p}'\n" for p in parts))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{tmp}/a.txt",
                    "-af", "loudnorm=I=-16:TP=-1.5", f"{tmp}/voice.wav"], check=True)
    # 3) frames
    data = json.dumps([{"img": photo(P[a]["img"]), "name": P[a]["name"]} for a in asins])
    html = PAGE.replace("__DATA__", data).replace("__HOOK__", json.dumps(hook_text)).replace("__TIMES__", json.dumps(times))
    pg.set_content(html, wait_until="networkidle")
    pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(800)
    for f in range(int(times[-1] * FPS)):
        pg.evaluate(f"show({f / FPS})")
        pg.screenshot(path=f"{tmp}/{f:04d}.jpg", type="jpeg", quality=90)
    os.makedirs("reels", exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{tmp}/%04d.jpg",
                    "-i", f"{tmp}/voice.wav", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", f"reels/{vid}.mp4"], check=True)
    shutil.copy(f"{tmp}/0010.jpg", f"reels/{vid}-cover.jpg")
    shutil.rmtree(tmp)
    return times[-1]


if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    voice = VOICE
    if "--voice" in sys.argv:
        voice = sys.argv[sys.argv.index("--voice") + 1]; args = [a for a in args if a != voice]
    want = args or list(SPECS)
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for vid in want:
            pg = b.new_page(viewport={"width": W, "height": H})
            print(vid, round(build(pg, vid, *SPECS[vid], voice), 1), "s"); pg.close()
        b.close()
