# Conversion upgrades for guide pages: top pick box, quick-pick table,
# stronger buttons, Black Friday reminder, shorter main list + "More ideas".
import html, re, datetime

BTN = "Check today's price on Amazon"
BF_DAY = datetime.date(2026, 11, 27)
CM_DAY = datetime.date(2026, 11, 30)

UPG = {
 "homebody-gifts": dict(
   top=("B073429DV2", "If you only get one gift for the homebody in your life, make it this. A weighted blanket turns every movie night and wind-down into a calm, all-over hug, and it's one of the most-loved comfort gifts of the last few years."),
   quick=[("Best overall", "B073429DV2"), ("Best for readers", "B0CFPJYX7P"), ("Best small gift", "B08GG42WXY"),
          ("Best for the couch", "B07X3BX7WM"), ("Best for dark mornings", "B081CHLF46")],
   main=["B073429DV2", "B0CFPJYX7P", "B08GG42WXY", "B07X3BX7WM", "B07G142F9Z", "B081CHLF46", "B0DLGGGYMN", "B0062JSYEW"],
 ),
 "black-friday-gift-ideas": dict(
   top=("B0CFPJYX7P", "The easiest Black Friday win on this list. The Kindle Paperwhite works for almost anyone who reads, from teens to grandparents, and it's the kind of bigger gift people wait for a deal on."),
   quick=[("Best overall", "B0CFPJYX7P"), ("Best for coffee lovers", "B00CH9QWOU"), ("Best for the kitchen", "B0C33CHG99"),
          ("Best for relaxing", "B07G142F9Z"), ("Best for mom or grandparents", "B0D8JDPKKS"), ("Best beauty splurge", "B0DYG4Q6PL")],
   main=["B0CFPJYX7P", "B00CH9QWOU", "B0C33CHG99", "B0D8JDPKKS", "B07G142F9Z", "B0DYG4Q6PL", "B06WGP2CVL", "B08X8JKC8F", "B0CLCH13T7"],
 ),
}

def bf_banner(today=None):
    today = today or datetime.date.today()
    if today > CM_DAY:
        return ""
    if today < BF_DAY:
        d = (BF_DAY - today).days
        when = "tomorrow" if d == 1 else f"in {d} days"
        msg = f"<strong>Black Friday is {when}</strong> (Friday, Nov 27) and Cyber Monday is Nov 30. Save this guide and check prices that week. Bigger gifts like these are often worth waiting for."
    elif today == BF_DAY:
        msg = "<strong>It's Black Friday.</strong> Check today's prices on the picks below. Deals can sell out or change quickly."
    else:
        msg = "<strong>Cyber Monday is Nov 30.</strong> Missed Black Friday? Check today's prices on the picks below before the weekend deals end."
    return f'<div class="bf-banner"><span class="bf-dot" aria-hidden="true"></span><p>{msg}</p></div>'

def _a(asin, link, cls="btn btn-buy", text=BTN):
    return f'<a class="{cls}" href="{link(asin)}" target="_blank" rel="sponsored nofollow noopener">{html.escape(text)} <span aria-hidden="true">→</span></a>'

def build_sections(slug, info, link):
    """info: asin -> dict(name, title, why, best)"""
    cfg = UPG[slug]
    ta, treason = cfg["top"]; t = info[ta]
    top = f"""<section class="toppick">
  <p class="tp-label">★ Our top pick</p>
  <div class="tp-body">
    <h2>{html.escape(t['title'])}</h2>
    <p class="prod">{html.escape(t['name'])}</p>
    <p>{html.escape(treason)}</p>
    {_a(ta, link, "btn btn-buy btn-lg")}
  </div>
</section>"""
    rows = "".join(f"""<tr><th scope="row">{html.escape(lbl)}</th><td>{html.escape(info[a]['title'])}</td><td>{_a(a, link, "btn btn-buy btn-sm", "Check price")}</td></tr>""" for lbl, a in cfg["quick"])
    quick = f"""<section class="quickpick">
  <h2>Quick picks</h2>
  <p class="qp-sub">Short on time? Start here.</p>
  <table><tbody>{rows}</tbody></table>
</section>"""
    main = cfg["main"]
    cards = []
    for i, a in enumerate(main, 1):
        o = info[a]
        best = f'<p class="bestfor"><strong>Best for:</strong> {html.escape(o["best"])}</p>' if o.get("best") else ""
        cards.append(f"""<article class="pick">
  <div class="num">{i:02d}</div>
  <div class="pick-body">
    <h3>{html.escape(o['title'])}</h3>
    <p class="prod">{html.escape(o['name'])}</p>
    <p>{html.escape(o['why'])}</p>
    {best}
    {_a(a, link)}
  </div>
</article>""")
    rest = [a for a in info if a not in main]
    more = ""
    if rest:
        lis = "".join(f"""<li><div><strong>{html.escape(info[a]['title'])}</strong><span>{html.escape(info[a]['why'].split('. ')[0].rstrip('.'))}.</span></div>{_a(a, link, "btn btn-buy btn-sm", "Check price")}</li>""" for a in rest)
        more = f"""<section class="moreideas">
  <h2>More ideas</h2>
  <ul>{lis}</ul>
</section>"""
    picks = f"""<section class="picks">
<h2 class="bf-sec">The shortlist</h2>
{chr(10).join(cards)}
</section>
{more}"""
    return top, quick, picks

CSS = """
.btn-buy{background:var(--accent)}
.btn-lg{font-size:17px;padding:14px 26px}
.btn-sm{font-size:13.5px;padding:8px 14px;white-space:nowrap}
.bf-banner{display:flex;gap:12px;align-items:flex-start;background:#FFF4E5;border:1px solid #F0D2A8;border-radius:12px;padding:14px 18px;margin:24px 0 0}
.bf-banner p{margin:0;font-size:15px;color:var(--brown)}
.bf-dot{width:10px;height:10px;border-radius:50%;background:#C0392B;flex:none;margin-top:7px}
.toppick{background:var(--white);border:2px solid var(--accent);border-radius:18px;padding:26px 28px;margin:28px 0}
.tp-label{display:inline-block;background:var(--accent);color:#fff;font-weight:600;font-size:13px;letter-spacing:.08em;text-transform:uppercase;padding:5px 12px;border-radius:999px;margin:0 0 12px}
.toppick h2{font-family:Fraunces,Georgia,serif;font-weight:500;font-size:30px;margin:0 0 4px}
.toppick p{margin:0 0 16px}
.quickpick{margin:32px 0}
.quickpick h2{font-family:Fraunces,Georgia,serif;font-weight:500;font-size:28px;margin:0}
.qp-sub{color:var(--mid);margin:2px 0 12px}
.quickpick table{width:100%;border-collapse:collapse;background:var(--white);border:1px solid var(--line);border-radius:14px;overflow:hidden}
.quickpick th,.quickpick td{padding:13px 16px;border-bottom:1px solid var(--line);text-align:left;vertical-align:middle}
.quickpick tr:last-child th,.quickpick tr:last-child td{border-bottom:none}
.quickpick th{font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--accent-d);width:30%}
.quickpick td:last-child{text-align:right;width:1%}
.moreideas{margin:36px 0}
.moreideas h2{font-size:26px;margin:0 0 8px;padding-bottom:8px;border-bottom:2px solid var(--accent)}
.moreideas ul{list-style:none;margin:0;padding:0}
.moreideas li{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:14px 0;border-bottom:1px solid var(--line)}
.moreideas li div{display:flex;flex-direction:column}
.moreideas li span{color:var(--mid);font-size:14.5px}
@media(max-width:640px){
 .quickpick table,.quickpick tbody,.quickpick tr,.quickpick th,.quickpick td{display:block;width:auto}
 .quickpick tr{padding:12px 16px;border-bottom:1px solid var(--line)}
 .quickpick th,.quickpick td{border:none;padding:2px 0;text-align:left}
 .quickpick td:last-child{text-align:left;padding-top:8px}
 .moreideas li{flex-direction:column;align-items:flex-start}
 .toppick{padding:22px 18px}
}
"""

def apply(body, slug, info, link, today=None):
    """Swap the page's picks section for the upgraded layout."""
    top, quick, picks = build_sections(slug, info, link)
    new = bf_banner(today) + "\n" + top + "\n" + quick + "\n" + picks
    body2, n = re.subn(r'<section class="picks">.*?\n</section>', lambda m: new, body, count=1, flags=re.S)
    assert n == 1, slug
    return body2
