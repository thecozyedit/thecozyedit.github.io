# "Editorial" guide layout (style C): dark, collage-first, short plain notes.
import html, re

# Per-guide content. notes: asin -> (short name, one plain line, short fact or "")
ED = {
 "homebody-gifts": dict(
  kicker="Gift guide", h1="The homebody's<br>perfect night in",
  intro="For the person who'd always rather stay in. Things they'll actually use, most of them every night.",
  notes={
   "B07X3BX7WM": ("Faux fur throw", "Fluffy on one side, sherpa on the other. The couch blanket nobody gives back.", "Reversible · machine washable"),
   "B0CFPJYX7P": ("Kindle Paperwhite", "For the person with a stack of books on the nightstand. No glare, and the battery lasts weeks.", "Waterproof · warm light"),
   "B073429DV2": ("Weighted blanket", "Heavy in the good way. Feels like a hug during a movie.", "15 lb · 48 x 72 in"),
   "B08GG42WXY": ("Clip-on book light", "Lets them read in bed without keeping anyone else awake.", "Rechargeable · clips on"),
   "B07G142F9Z": ("Heated neck massager", "Drapes over the shoulders after a long day. Heat plus kneading.", "Car adapter included"),
   "B081CHLF46": ("Sunrise alarm clock", "Wakes you with light that slowly gets brighter. Much nicer on dark winter mornings.", "Light + sound alarm"),
   "B0DLGGGYMN": ("Reading pillow", "Arms and a backrest for reading or watching TV in bed.", "Arms + backrest"),
   "B0062JSYEW": ("Tea sampler", "A sampler box of teas for slow evenings.", "Black, green and herbal"),
   "B08GHNRG5Q": ("Fuzzy slipper socks", "Thick, soft socks for padding around the house.", ""),
   "B0D13Z9HGV": ("1000-piece puzzle", "A stained-glass design that takes a few cozy evenings to finish.", ""),
   "B0F9SY9K29": ("Lounge set", "A matching two-piece set for lazy weekends.", ""),
   "B0H8S5DNQM": ("Cordless neck massager pillow", "Heated, cordless, and works on the couch or in the car.", ""),
   "B06WGP2CVL": ("Heated foot massager", "For tired feet at the end of the day.", ""),
   "B0BFC7WQ6R": ("Echo Spot", "A small smart alarm clock for the nightstand.", ""),
   "B0B17YZQ72": ("Kindle Paperwhite case", "An easy add-on if you're giving the Kindle.", ""),
  }),
}

def _row(i, a, n, note, link, thumb, cls="row"):
    im = f'<img src="https://images.unsplash.com/{thumb}?auto=format&fit=crop&w=160&h=160&q=65" alt="" width="64" height="64" loading="lazy" data-pin-nopin="true">' if thumb else ""
    return (f'<a class="{cls}" href="{link(a)}" target="_blank" rel="sponsored nofollow noopener">{im}'
            f'<span class="rt"><b>{i}. {html.escape(n)}</b><small>{html.escape(note)}</small></span><i>Shop →</i></a>')

def apply_ed(body, slug, main, link, IMG, bf_line):
    cfg = ED[slug]; notes = cfg["notes"]
    allp = [a for a in dict.fromkeys(re.findall(r"amazon\.com/dp/(\w+)", body)) if a in notes]
    rest = [a for a in allp if a not in main]
    top3 = [a for a in main if a in IMG][:3]
    col = "".join(f'<a href="{link(a)}" target="_blank" rel="sponsored nofollow noopener"><img src="https://images.unsplash.com/{IMG[a]}?auto=format&fit=crop&w=600&h=720&q=70" alt="{html.escape(notes[a][0])}" data-pin-nopin="true"><span class="lb">{main.index(a)+1}. {html.escape(notes[a][0])}</span></a>' for a in top3)
    hero = f"""<section class="ed-hero">
  <p class="k">{html.escape(cfg['kicker'])} · {len(allp)} finds</p>
  <h1>{cfg['h1']}</h1>
  <p class="ed-intro">{html.escape(cfg['intro'])}</p>
  {bf_line}
  <div class="col">{col}</div>
  <a class="shop" href="#list">Shop the list ↓</a>
</section>"""
    rows = "".join(_row(i, a, notes[a][0], notes[a][1], link, IMG.get(a)) for i, a in enumerate(main, 1))
    more = "".join(_row(len(main)+i, a, notes[a][0], notes[a][1], link, None, "row row-sm") for i, a in enumerate(rest, 1))
    lst = f'<section class="ed-list" id="list">{rows}</section>' + (f'<section class="ed-list ed-more"><h2>More ideas</h2>{more}</section>' if more else "")
    # strip old hero / blocks, insert new
    body = body.replace("<body>", '<body class="ed">', 1)
    body = re.sub(r'<section class="photo-hero".*?</section>', lambda m: hero, body, count=1, flags=re.S)
    for cls in ["bf-remind", ]:
        body = re.sub(r'<div class="bf-remind".*?</script>', "", body, count=1, flags=re.S)
    body = re.sub(r'<section class="toppick">.*?</section>', "", body, count=1, flags=re.S)
    body = re.sub(r'<section class="quickpick">.*?</section>', "", body, count=1, flags=re.S)
    body = re.sub(r'<section class="guide-intro">.*?</section>', "", body, count=1, flags=re.S)
    body = re.sub(r'<section class="moreideas">.*?</section>', "", body, count=1, flags=re.S)
    body, n = re.subn(r'<section class="picks">.*?\n</section>', lambda m: lst, body, count=1, flags=re.S)
    assert n == 1
    body = body.replace('<footer class="site-footer">', '<p class="ed-disc">Photos show similar items, not the exact product. Tap any item to see it on Amazon.</p>\n<footer class="site-footer">', 1)
    return body

CSS = """
body.ed{background:#2a211c;color:#f4ece2}
body.ed .disclosure{background:#1e1713;color:#bfae9e}
body.ed .site-header a,body.ed .site-header{color:#f4ece2}
body.ed .site-header nav a{color:#e8dccf}
body.ed .site-header .nav-bf{color:#d9a57a}
body.ed main{max-width:560px}
.ed-hero{padding:8px 0 4px}
.ed-hero .k{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:#d9a57a;margin:6px 0 0}
.ed-hero h1{font-family:'Playfair Display',Georgia,serif;font-weight:500;font-size:clamp(34px,8vw,48px);line-height:1.05;margin:8px 0 12px;color:#f4ece2}
.ed-intro{color:#d8cabb;font-size:16px;line-height:1.5;margin:0 0 14px}
.ed-bf{font-size:13.5px;color:#d9a57a;margin:0 0 16px}
.ed-hero .col{display:grid;grid-template-columns:1fr 1fr;gap:6px;border-radius:14px;overflow:hidden}
.ed-hero .col a{position:relative;display:block}
.ed-hero .col a:first-child{grid-row:span 2}
.ed-hero .col img{width:100%;height:100%;object-fit:cover;display:block;min-height:170px;background:#3a2e27}
.ed-hero .lb{position:absolute;left:8px;bottom:8px;background:rgba(255,248,240,.92);color:#2a211c;font-family:'Playfair Display',Georgia,serif;font-size:13px;padding:3px 10px;border-radius:999px}
.ed-hero .shop{display:block;text-align:center;border:1px solid #d9a57a;color:#f4ece2;text-decoration:none;border-radius:999px;padding:12px;margin:14px 0 18px;font-size:14px}
.ed-list{margin:0}
.ed-list h2{font-family:'Playfair Display',Georgia,serif;font-weight:500;font-size:24px;color:#f4ece2;margin:28px 0 4px}
.ed-list .row{display:flex;gap:12px;align-items:center;padding:13px 0;border-top:1px solid #4a3c33;text-decoration:none;color:#f4ece2}
.ed-list .row img{width:64px;height:64px;border-radius:10px;object-fit:cover;flex:none;background:#3a2e27}
.ed-list .rt{min-width:0}
.ed-list .row b{font-family:'Playfair Display',Georgia,serif;font-weight:500;font-size:17px;display:block}
.ed-list .row small{color:#bfae9e;font-size:13px;line-height:1.4;display:block}
.ed-list .row i{margin-left:auto;font-style:normal;color:#d9a57a;white-space:nowrap;padding-left:8px}
.ed-list .row:hover b{color:#d9a57a}
.ed-more .row b{font-size:15.5px}
body.ed .howpick,body.ed .faq{max-width:560px}
body.ed .howpick h2,body.ed .faq h2,body.ed .more h2,body.ed .pinbox h2{font-family:'Playfair Display',Georgia,serif;font-weight:500;color:#f4ece2}
body.ed .howpick p{color:#bfae9e}
body.ed .faq details{background:#33281f;border-color:#4a3c33}
body.ed .faq summary{color:#f4ece2}
body.ed .faq details p{color:#d8cabb}
body.ed .pinbox{background:#33281f;border-color:#4a3c33}
body.ed .pinbox p{color:#bfae9e}
body.ed .pinbox .eyebrow{color:#d9a57a}
body.ed .btn-ghost{color:#f4ece2;border-color:#d9a57a}
body.ed .more{max-width:560px}
body.ed .chips a{background:#33281f;border-color:#4a3c33;color:#f4ece2}
body.ed footer{border-color:#4a3c33;color:#9c8b7c}
body.ed footer a{color:#d9a57a}
.ed-disc{max-width:560px;margin:28px auto 0;padding:0 20px;font-size:12px;color:#9c8b7c;text-align:center}
"""
