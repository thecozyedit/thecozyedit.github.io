"""One product map and one guide list, built from the existing data files. Loading writes nothing."""
import html, json
from dataclasses import dataclass
from guides_meta import GUIDES, NEW, HOLIDAY, PH

TAG = "cozeyditweb-20"
BF = "black-friday-gift-ideas"
BF_TITLE = "Black Friday Gift Ideas 2026 | The Cozy Edit"
BF_DESC = ("Black Friday gift ideas for 2026: espresso machines, air fryers, Kindle, LED face masks, heated massagers, "
           "digital frames and cozy gifts worth waiting for.")
ALL_ORDER = [BF] + [g[0] for g in GUIDES] + [n[0] for n in NEW + HOLIDAY]


@dataclass(frozen=True)
class Product:
    asin: str
    name: str
    note: str
    photo: str | None


@dataclass(frozen=True)
class Guide:
    slug: str
    title: str
    description: str
    headline_html: str
    intro: str
    main: list
    more: list
    faq: list
    hero_photo: str


@dataclass
class Catalog:
    products: dict
    guides: list


def link(asin: str) -> str:
    return f"https://www.amazon.com/dp/{asin}?tag={TAG}"


def headline(h1: str) -> str:
    if "<br>" in h1:
        a, b = h1.split("<br>", 1)
        return f"{html.escape(a)} <i>{html.escape(b)}</i>"
    return html.escape(h1)


def _items():
    items = []
    for p in ["/home/claude/phase2/plan.json", "/home/claude/phase3/plan2.json",
              "/home/claude/master/bf.json", "/home/claude/batch4/plan4.json"]:
        items += json.load(open(p))
    return items


def load() -> Catalog:
    import ed, upgrade
    items = _items()
    copy = json.load(open("/home/claude/site/copy.json"))
    gc = json.load(open("/home/claude/site/guides_content.json"))
    bf = json.load(open("/home/claude/master/bf.json"))
    byasin = {}
    for o in items:
        byasin.setdefault(o["asin"], o)
    bfmap = {o["asin"]: o for o in bf}

    lists, titles, descs = {BF: [o["asin"] for o in bf]}, {BF: BF_TITLE}, {BF: BF_DESC}
    for slug, board, h1, _intro, meta, _ic in GUIDES:
        lists[slug] = list(dict.fromkeys(o["asin"] for o in items if o["board"] == board))
        titles[slug], descs[slug] = f"{h1} | The Cozy Edit", meta
    for slug, title, _h1, _lede, meta, _photo, asins in NEW + HOLIDAY:
        lists[slug], titles[slug], descs[slug] = list(asins), f"{title} | The Cozy Edit", meta

    def product(a):
        if a in ed._ALL:
            name, note = ed._ALL[a][0], ed._ALL[a][1]
        elif a in byasin and a in copy:
            name, note = byasin[a]["product"], copy[a][0]
        elif a in bfmap:
            name, note = bfmap[a]["product"], bfmap[a]["desc"]
        else:
            name, note = byasin[a]["product"], ""
        return Product(a, name, note, upgrade.IMG.get(a))

    products, guides = {}, []
    for slug in ALL_ORDER:
        main = list(upgrade.UPG[slug]["main"])
        more = [a for a in lists[slug] if a not in main]
        for a in main + more:
            products.setdefault(a, product(a))
        e = ed.ED[slug]
        guides.append(Guide(slug, titles[slug], descs[slug], headline(e["h1"]), e["intro"], main, more,
                            [tuple(x) for x in gc.get(slug, {}).get("faq", [])],
                            PH["bf" if slug == BF else slug]))
    return Catalog(products, guides)
