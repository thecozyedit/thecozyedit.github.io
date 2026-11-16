import json, datetime as dt, urllib.parse as up
D = "As an Amazon Associate I earn from qualifying purchases."
IM = {"B00CH9QWOU":"71BvCt6eAFL._SL1500_.jpg","B0C33CHG99":"81R9sA3IyBL._AC_SL1500_.jpg","B07C8V4FDR":"71r3Uk7ahjL._AC_SL1500_.jpg","B0FVXHV6GP":"51mC5L7eEWL._AC_SL1500_.jpg","B0CCP46DK9":"61SsDfH706L._AC_SL1500_.jpg","B00V9JP8EE":"41YMvPK9RFL._AC_SL1500_.jpg","B0DXHGTMQL":"61XTghTDE8L._AC_SL1500_.jpg","B08D3SDPXT":"71uKX+-4GmL._AC_SL1500_.jpg","B0CLCH13T7":"71Cdfx8DiGL._AC_SL1500_.jpg","B08X8JKC8F":"61j-4ib92YL._AC_SL1500_.jpg","B07G142F9Z":"81CKfov14pL._AC_SL1500_.jpg","B0H8S5DNQM":"71730btCSjL._AC_SL1500_.jpg","B06WGP2CVL":"61ZnmKypQNL._AC_SL1200_.jpg","B09VBTKKV4":"71zM0BLeLrL._AC_SL1500_.jpg","B0CFPJYX7P":"71YwNBmu+aL._AC_SL1500_.jpg","B0GJ5D2XP6":"71mEui6zWUL._AC_SL1500_.jpg","B0D8JDPKKS":"81mhPUK4EGL._AC_SL1500_.jpg","B0DYG4Q6PL":"71c4A5AT-OL._AC_SL1500_.jpg","B0D5MFLFM2":"71PzTq29oSL._SL1500_.jpg","B07R9SGCGQ":"81-4kxG3E8L._SL1500_.jpg","B0CNY1F31S":"71Ld+1SBc5L._AC_SL1500_.jpg","B0CGM2SWK2":"712vPB9eJIL._AC_SL1500_.jpg"}
bf = json.load(open("/home/claude/master/bf.json"))
BOARD = "Black Friday Gift Ideas"
out = []
start = dt.date(2026, 11, 8)
for i, o in enumerate(bf):
    link = f"https://www.amazon.com/dp/{o['asin']}?tag=cozeyditpin-20"
    image = "https://m.media-amazon.com/images/I/" + IM[o["asin"]]
    title = f"{o['title']} | Black Friday Gift Idea"
    desc = f"{o['title']} (affiliate link): {o['desc']} A Black Friday gift idea worth waiting for. {D}"
    assert len(title) <= 100 and len(desc) <= 500, (title, len(desc))
    out.append(dict(n=61+i, kind="product", date=str(start + dt.timedelta(days=i//5)), board=BOARD, category=o["board"], asin=o["asin"], product=o["product"],
        rating=o["rating"], reviews=o["reviews"], tag="cozeyditpin-20", link=link, image=image, title=title, description=desc,
        create_url="https://www.pinterest.com/pin/create/button/?"+up.urlencode({"url":link,"media":image,"description":desc})))
G = [("2026-10-25","black-friday-gift-ideas","Black Friday Gift Ideas",BOARD,"Black Friday Gift Ideas 2026","22 well-loved, bigger-ticket gifts worth waiting for, from espresso machines and air fryers to cozy heated massagers.",22),
     ("2026-10-27","homebody-gifts","Gifts for Homebodies","Gifts for Homebodies","8 Cozy Gifts for Homebodies","Comfort upgrades for reading, lounging and long weekends at home.",8),
     ("2026-10-29","gifts-for-her","Cozy Gifts for Her","Cozy Gifts for Her","8 Cozy Gifts for Her","Soft, warm and a little indulgent gifts for wives, moms, sisters and friends.",8),
     ("2026-10-31","kitchen-gifts-for-her","Kitchen Gifts for Her","Kitchen Gifts for Her","9 Kitchen Gifts for Her","Pretty, useful kitchen finds for coffee lovers and matcha drinkers.",9),
     ("2026-11-02","home-cook-gifts","Gifts for the Home Cook","Gifts for the Home Cook","8 Gifts for the Home Cook","Tools that make everyday cooking easier, from a trusty skillet to everyday gadgets.",8),
     ("2026-11-04","stocking-stuffers-for-women","Stocking Stuffers for Women","Stocking Stuffers for Women","Stocking Stuffers for Women She'll Use","Small, giftable favorites that fit in a stocking and actually get used.",6),
     ("2026-11-06","cozy-christmas-gifts","Cozy Christmas Gift Ideas","Cozy Christmas Gift Ideas","Cozy Christmas Gift Ideas","Holiday-ready picks for movie nights, Christmas morning and the countdown to the 25th.",7),
     ("2026-11-08","housewarming-gifts","Housewarming Gift Ideas","Housewarming Gift Ideas","Housewarming Gift Ideas for a New Home","Easy, thoughtful gifts for a new home or a first apartment.",6),
     ("2026-11-10","beauty-stocking-stuffers","At-Home Beauty Stocking Stuffers","At-Home Beauty Stocking Stuffers","At-Home Beauty Stocking Stuffers","Salon-style results at home: beauty and self-care gifts she'll reach for every day.",8)]
guides = []
for k, (date, slug, gname, board, title, blurb, n) in enumerate(G):
    link = f"https://thecozyedit.github.io/{slug}.html"
    image = f"https://thecozyedit.github.io/pins/{slug}.jpg"
    desc = f"{title}: {blurb} See all {n} picks in the full gift guide on The Cozy Edit. {D}"
    guides.append(dict(n=f"G{k+1}", kind="guide", date=date, board=board, category=gname, asin="", product=f"Gift-guide pin: {gname}", rating="", reviews="",
        tag="(website)", link=link, image=image, title=title, description=desc,
        create_url="https://www.pinterest.com/pin/create/button/?"+up.urlencode({"url":link,"media":image,"description":desc})))
json.dump(out, open("/home/claude/master/plan3.json","w"), indent=1)
json.dump(guides, open("/home/claude/master/guides.json","w"), indent=1)
for o in out + guides: print(o["n"], o["date"], o["board"], "|", o["title"])
