"""Black Friday mode (Parth, Nov 11): through Nov 30 the homepage and the Black Friday page lead with
"worth buying on Black Friday" for yourself and your home. Homepage blocks use data-until/data-from,
so the footer date-gate script switches back to the gift layout on Dec 1 (New York time).
Usage: python3 tools/bf_mode.py   (run from the repo root; idempotent)"""
import html, json, re, sys

P = json.load(open("tools/products.json"))
TAG = "cozeyditweb-20"
GROUPS = [
    ("Kitchen", ["B08QXB9BH5", "B06Y1YD5W7", "B01MCYAFOD", "B07C8V4FDR"]),
    ("Comfort and sleep", ["B073429DV2", "B0BZR6YBHK", "B081CHLF46", "B09VBTKKV4"]),
    ("Tech", ["B0BFC7WQ6R", "B07NQRM6ML", "B0D8JDPKKS", "B0CCP46DK9"]),
    ("Self-care", ["B0DYG4Q6PL", "B07G142F9Z", "B06WGP2CVL", "B01LSUQSB0"]),
]
NOTE = {  # self-purchase wording where the site note talks about "them"
    "B07NQRM6ML": "Keeps coffee at the exact temperature you like, all morning.",
    "B0D8JDPKKS": "Family sends photos from their phones and they show up on the frame.",
}
E = html.escape


def img(url, w, h):
    return re.sub(r"w=\d+&h=\d+", f"w={w}&h={h}", url)


def card(a):
    p = P[a]
    return (f'<a class="card" href="https://www.amazon.com/dp/{a}?tag={TAG}" target="_blank" rel="sponsored nofollow noopener">'
            f'<div class="ph"><img src="{img(p["img"], 500, 625)}" alt="" loading="lazy" data-pin-nopin="true"></div>'
            f'<h3>{E(p["name"])}</h3><p>{E(NOTE.get(a, p["note"]))}</p><span class="pill">Check today\'s price on Amazon</span></a>')


def bf_section():
    out = ['<section class="sec bfnow" data-until="2026-12-01"><h2 class="t">Our Black Friday list</h2>'
           '<p class="sub">Things we\'d buy for ourselves and our homes. Make your list now, then check today\'s price on Amazon that week.</p>']
    for name, asins in GROUPS:
        out.append(f'<h3 class="bfh">{E(name)}</h3><div class="grid">' + "".join(card(a) for a in asins) + "</div>")
    return "".join(out) + "</section>"


CSS = "[hidden]{display:none!important}.bfh{font-family:'Bodoni Moda',serif;font-weight:400;font-size:28px;color:var(--glow);margin:46px 0 18px;padding-bottom:10px;border-bottom:1px solid var(--line)}.bfnow .bfh:first-of-type{margin-top:8px}"
KINDLE_OLD = "For the person with a stack of books on the nightstand. No glare, and the battery lasts weeks."
KINDLE_NEW = "For anyone with a stack of books on the nightstand. No glare, and the battery lasts weeks."


def home(h):
    if "bfnow" in h:
        return h
    old_intro = re.search(r'<section class="intro">.*?</section>', h, re.S).group(0)
    new_intro = ('<section class="intro" data-until="2026-12-01"><h1>Worth buying on <i>Black Friday</i></h1><div>'
                 '<p>The bigger things for you and your home that people wait all year to buy: kitchen upgrades, better sleep, small tech and self-care.</p>'
                 '<p class="bf">Black Friday is November 27. Our list is ready.</p></div></section>')
    gift_intro = old_intro.replace('<section class="intro">', '<section class="intro" data-from="2026-12-01" hidden>', 1)
    gift_intro = re.sub(r'<p class="bf" data-until="2026-12-01">.*?</p>', "", gift_intro)
    h = h.replace(old_intro, new_intro + gift_intro, 1)
    i = h.index('<section class="window" data-from="2026-12-01" hidden>')
    j = h.index("</section>", i) + len("</section>")
    h = h[:j] + bf_section() + h[j:]
    return h.replace(KINDLE_OLD, KINDLE_NEW)


BF_SUBS = [
    ("<title>Black Friday Gift Ideas 2026 | The Cozy Edit</title>", "<title>Black Friday 2026: What's Worth Buying | The Cozy Edit</title>"),
    ('content="Black Friday Gift Ideas 2026 | The Cozy Edit"', 'content="Black Friday 2026: What\'s Worth Buying | The Cozy Edit"'),
    ("Black Friday gift ideas for 2026: espresso machines, air fryers, Kindle, LED face masks, heated massagers, digital frames and cozy gifts worth waiting for.",
     "What's worth buying on Black Friday 2026 for you and your home: espresso machines, air fryers, Kindle, LED face masks, heated massagers and digital frames."),
    ("<h1>Gifts worth <i>waiting for</i></h1>", "<h1>Worth buying on <i>Black Friday</i></h1>"),
    ("<p>Bigger gifts people tend to save for Black Friday. Check the prices that week.</p>",
     "<p>The bigger things for you and your home that people wait all year to buy. Make your list now, then check today's price on Amazon that week.</p>"),
    ("Everything we'd give, in the order we'd give it.", "Our picks, in the order we'd buy them."),
    ("Smaller gifts and easy extras.", "Smaller buys and easy extras."),
    ("Bigger-ticket gifts people wait all year for", "Bigger-ticket things people wait all year for"),
    ("Many popular gifts are discounted during Black Friday and Cyber Monday.", "Many popular items get price drops around Black Friday and Cyber Monday, but not all, so check before you buy."),
    (KINDLE_OLD, KINDLE_NEW),
]


def bf_page(h):
    for a, b in BF_SUBS:
        h = h.replace(a, b)
        h = h.replace(a.replace("'", "&#x27;"), b.replace("'", "&#x27;"))
    return h


if __name__ == "__main__":
    s = open("style.css").read()
    if ".bfh{" not in s:
        open("style.css", "w").write(s + "\n" + CSS + "\n@media(max-width:700px){.bfh{font-size:23px;margin:34px 0 14px}}\n")
    for f, fn in (("index.html", home), ("black-friday-gift-ideas.html", bf_page)):
        new = fn(open(f).read())
        open(f, "w").write(new)
    print("ok")
