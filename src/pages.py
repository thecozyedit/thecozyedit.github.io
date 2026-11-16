"""Assembles the homepage, guide pages and About page from the catalog and theme."""
import json, os
import theme as T
from catalog import Catalog, Guide, ALL_ORDER, BF
from guides_meta import PH

SITE = "https://thecozyedit.github.io/"
PINS = "/home/claude/thecozyedit.github.io/pins/v"
WHO = [("Her", "gifts-for-her"), ("Him", "gifts-for-him"), ("Mom", "christmas-gifts-for-mom"),
       ("Homebodies", "homebody-gifts"), ("Coffee lovers", "gifts-for-coffee-lovers"),
       ("The always cold", "gifts-for-someone-always-cold")]
WHO_PHOTOS = ["photo-1674475760738-8c7af859f821", "photo-1787724777367-ee027842b62a", "photo-1531981936561-347fb37a966a",
              "photo-1764425172300-d97c21f6043f", "photo-1620051787208-a45bc64e32ff", "photo-1511401139252-f158d3209c17"]
HOW = ("Well-reviewed things people actually use. Nobody pays to be on this list. We don't show prices because "
       "they change daily, so tap through to see today's price on Amazon.")
CSS_V = "1"


def page_url(path: str) -> str:
    return SITE if path == "index" else f"{SITE}{path}.html"


def pin_img(path: str) -> str:
    sl = {"index": BF, "about": "homebody-gifts"}.get(path, path)
    if not os.path.exists(f"{PINS}/{sl}-0l0.jpg"):
        sl = "cozy-christmas-gifts"
    return f"{SITE}pins/v/{sl}-0l0.jpg"


def _short(title: str) -> str:
    return title.replace(" | The Cozy Edit", "")


def _faq_ld(qa) -> str:
    if not qa:
        return ""
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]}
    return '\n<script type="application/ld+json">' + json.dumps(ld) + "</script>"


def _all_guides(c: Catalog):
    return [(g.slug, _short(g.title)) for g in c.guides]


def render_guide(g: Guide, c: Catalog) -> str:
    P = c.products
    label = "Our Black Friday pick" if g.slug == BF else "Our top pick"
    i = ALL_ORDER.index(g.slug)
    rel = [c.guides[(i + k) % len(c.guides)] for k in (1, 2, 3)]
    more = ("" if not g.more else '<section class="sec"><h2 class="t">More ideas</h2><p class="sub">Smaller gifts and easy extras.</p>'
            '<div class="compacts">' + "".join(T.compact_row(P[a]) for a in g.more) + "</div></section>")
    return (T.head(g.title, g.description, page_url(g.slug), pin_img(g.slug), _faq_ld(g.faq), CSS_V) + T.header()
            + f'<section class="intro"><h1>{g.headline_html}</h1><div><p>{T.E(g.intro)}</p>{T.bf_line()}</div></section>'
            + T.window(P[g.main[0]], [P[a] for a in g.main[1:3]], label)
            + '<section class="sec"><h2 class="t">The full list</h2><p class="sub">Everything we\'d give, in the order we\'d give it.</p>'
            + '<div class="grid">' + "".join(T.product_card(P[a]) for a in g.main) + "</div></section>"
            + more
            + f'<section class="sec"><h2 class="t">How we pick</h2><p class="how">{T.E(HOW)}</p></section>'
            + T.faq(g.faq)
            + T.pinbox(page_url(g.slug), pin_img(g.slug), _short(g.title), g.description)
            + '<section class="sec"><h2 class="t">Keep browsing</h2><p class="sub">More lists we think you\'ll like.</p>'
            + '<div class="who three">' + T.who_tiles([(_short(r.title), f"{r.slug}.html", r.hero_photo) for r in rel])[len('<div class="who">'):]
            + "</section>"
            + T.guide_list(_all_guides(c)) + T.footer())


def render_home(c: Catalog) -> str:
    P, G = c.products, {g.slug: g for g in c.guides}
    bf, xmas = G[BF], G["cozy-christmas-gifts"]
    used = set(bf.main[:3]) | set(xmas.main[:3])
    picks = []
    for g in c.guides:
        a = next((a for a in g.main if P[a].photo and a not in used and a not in picks), None)
        if a:
            picks.append(a)
        if len(picks) == 8:
            break
    return (T.head("The Cozy Edit | Cozy Home & Gift Guides",
                   "Curated cozy home and gift ideas for her, homebodies, home cooks, stocking stuffers, housewarming and Christmas. New gift guides every week.",
                   page_url("index"), pin_img("index"), "", CSS_V) + T.header()
            + '<section class="intro"><h1>Gifts for the people who\'d rather <i>stay in</i></h1><div>'
            + "<p>We pick things we'd actually give: warm, useful, and good for a quiet night at home.</p>" + T.bf_line() + "</div></section>"
            + T.window(P[bf.main[0]], [P[a] for a in bf.main[1:3]], "Our Black Friday pick", gate="until")
            + T.window(P[xmas.main[0]], [P[a] for a in xmas.main[1:3]], "Our Christmas pick", gate="from")
            + '<section class="sec"><h2 class="t">Who are you shopping for?</h2><p class="sub">Pick someone and we\'ll show you what we\'d give them.</p>'
            + T.who_tiles([(lbl, f"{s}.html", pid) for (lbl, s), pid in zip(WHO, WHO_PHOTOS)]) + "</section>"
            + '<section class="sec"><h2 class="t">What we keep coming back to</h2><p class="sub">Cozy, useful, and easy to love.</p>'
            + '<div class="grid">' + "".join(T.product_card(P[a]) for a in picks) + "</div></section>"
            + T.guide_list(_all_guides(c)) + T.footer())


def render_about(c: Catalog) -> str:
    return (T.head("About & Disclosure | The Cozy Edit", "About The Cozy Edit, our Amazon Associates disclosure and privacy notice.",
                   page_url("about"), pin_img("about"), "", CSS_V) + T.header()
            + f'<section class="about"><div class="ph"><img src="https://images.unsplash.com/{PH["hero"]}?auto=format&fit=crop&w=900&h=1125&q=72" alt="" data-pin-nopin="true"></div>'
            + "<div><h1>About <i>The Cozy Edit</i></h1>"
            + "<p>We're a small, independent gift guide for cozy home finds: the blankets, mugs, kitchen tools and little luxuries that make home feel good. We put together lists for the people on yours, and share new picks on Pinterest.</p>"
            + "<p>We pick well-reviewed things people actually use every day. Nobody pays to be on a list.</p></div></section>"
            + '<section class="prose"><h2>Affiliate disclosure</h2>'
            + "<p>The Cozy Edit is a participant in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to Amazon.com. As an Amazon Associate we earn from qualifying purchases.</p>"
            + "<p>When you click a link on this site and buy something on Amazon, we may earn a small commission at no extra cost to you. It doesn't change what you pay or which products we feature.</p>"
            + "<p>Prices, availability and product details are set by Amazon and can change at any time. Please check the Amazon listing before you buy.</p></section>"
            + '<section class="prose" id="privacy"><h2>Privacy</h2>'
            + "<p>This site does not ask for or collect your personal information, and it has no sign-up forms or comments. It is hosted on GitHub Pages, which may log basic technical data such as IP addresses for security, as described in GitHub's privacy statement. Fonts are served by Google Fonts and photos by Unsplash.</p>"
            + "<p>When you click through to Amazon, Amazon may set cookies to track the referral and attribute purchases, as described in Amazon's privacy notice. We receive only aggregate reports of clicks and orders, never your name or personal details.</p>"
            + f'<p>Questions? Reach us through our <a href="{T.PIN}" rel="noopener" target="_blank">Pinterest profile</a>.</p></section>'
            + T.footer())
