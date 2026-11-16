import json, datetime as dt, urllib.parse as up

D = "As an Amazon Associate I earn from qualifying purchases."
CORE, BEAUTY = "cozeyditpin-20", "cozeyditbeauty-20"

# board, asin, product, rating, reviews, image, title, description
P = [
("Cozy Gifts for Her","B07XGZLWRD","Bedsure GentleSoft Sherpa Fleece Throw",4.7,"98K","https://m.media-amazon.com/images/I/812P8C0ImSL._AC_SL1500_.jpg",
 "The Coziest Sherpa Throw Blanket","A thick, fuzzy sherpa throw she'll keep on the couch all winter. Easy cozy gift idea for her, mom, or your best friend."),
("Cozy Gifts for Her","B0CTJGJL2T","GODONLIF Candle Warmer Lamp with Timer",4.6,"11.5K","https://m.media-amazon.com/images/I/810vcJJDrkL._AC_SL1500_.jpg",
 "Candle Warmer Lamp With Timer","Melts her favorite candle from the top with no flame, and the timer shuts it off. A pretty, cozy home gift for candle lovers."),
("Cozy Gifts for Her","B0BYNYWKC7","EverFoams Memory Foam Fuzzy Slippers",4.6,"10.6K","https://m.media-amazon.com/images/I/71yhTG8TNrL._AC_SL1500_.jpg",
 "Fuzzy Memory Foam Slippers","Soft, plush house slippers with memory foam. A cozy gift for her that actually gets worn every day."),
("Cozy Gifts for Her","B084P26Q3R","PAVILIA Plush Fleece Robe",4.6,"13.2K","https://m.media-amazon.com/images/I/61VOJmplqeL._AC_SL1500_.jpg",
 "Plush Fleece Robe for Her","A warm, plush robe for slow mornings and self-care nights. Cozy Christmas gift idea for women."),
("Gifts for Homebodies","B08GG42WXY","Gritin Rechargeable Book Light",4.8,"56.4K","https://m.media-amazon.com/images/I/81n7M-T19NL._AC_SL1500_.jpg",
 "Rechargeable Book Light for Reading in Bed","Warm, eye-friendly clip-on light for night reading. Small, thoughtful gift for homebodies and book lovers."),
("Gifts for Homebodies","B073429DV2","YnM Weighted Blanket",4.6,"23.9K","https://m.media-amazon.com/images/I/61wqo9sOcAL._AC_SL1500_.jpg",
 "Weighted Blanket for Cozy Nights In","The kind of heavy, calming blanket homebodies never want to leave. Cozy gift idea for introverts and night-in lovers."),
("Gifts for Homebodies","B08GHNRG5Q","Fluffy Fuzzy Slipper Socks",4.6,"13.3K","https://m.media-amazon.com/images/I/71BCwXja2WL._AC_SL1500_.jpg",
 "Fuzzy Slipper Socks for Cozy Days","Ultra-soft fuzzy socks for lazy weekends at home. Easy homebody gift and stocking stuffer."),
("Gifts for Homebodies","B07X3BX7WM","Bedsure Faux Fur Sherpa Blanket",4.6,"36.7K","https://m.media-amazon.com/images/I/A1Ajfh3EvtL._AC_SL1500_.jpg",
 "Faux Fur Throw for the Couch","Fluffy faux fur on one side, sherpa on the other. A cozy gift for homebodies who live on the couch."),
("Kitchen Gifts for Her","B09D8T11YS","Zulay Handheld Milk Frother",4.4,"235K","https://m.media-amazon.com/images/I/811azKMn+yL._AC_SL1500_.jpg",
 "Handheld Milk Frother for Home Lattes","Cafe-style foam for lattes and matcha at home. A small kitchen gift for coffee lovers."),
("Kitchen Gifts for Her","B07G2MBM6L","Bodum Bistro Gooseneck Electric Kettle",4.4,"13.2K","https://m.media-amazon.com/images/I/61loaANnLDL._AC_SL1500_.jpg",
 "Gooseneck Kettle for Pour-Over and Tea","Sleek matte black gooseneck kettle for pour-over coffee and tea. Kitchen gift idea for her."),
("Kitchen Gifts for Her","B010TCP3SC","Dash Mini Waffle Maker",4.6,"158K","https://m.media-amazon.com/images/I/6172rXS7RSL._AC_SL1500_.jpg",
 "Mini Waffle Maker for Cozy Breakfasts","Tiny, cute, and makes weekend breakfasts fun. Fun kitchen gift and stocking stuffer for her."),
("Kitchen Gifts for Her","B09HSS42P7","Simple Modern Iced Coffee Tumbler",4.8,"25.7K","https://m.media-amazon.com/images/I/41TIpBX3FJL._AC_SL1500_.jpg",
 "Insulated Iced Coffee Tumbler","Keeps iced coffee cold for hours. Everyday gift idea for coffee lovers."),
("Gifts for the Home Cook","B00S93EQUK","Alpha Grillers Instant Read Meat Thermometer",4.8,"92.9K","https://m.media-amazon.com/images/I/81QdFq6WSiL._AC_SL1500_.jpg",
 "Instant-Read Meat Thermometer","Fast, accurate readings for perfect roasts and grilling. Practical gift for the home cook."),
("Gifts for the Home Cook","B0D2P1HSCV","Royal Craft Wood Bamboo Cutting Board Set",4.5,"54.2K","https://m.media-amazon.com/images/I/71jPNPg1E9L._AC_SL1500_.jpg",
 "Bamboo Cutting Board Set","Three sturdy bamboo boards for prep and serving. Kitchen gift idea for anyone who loves to cook."),
("Gifts for the Home Cook","B00G2XGC88","Lodge Cast Iron Skillet",4.7,"83.3K","https://m.media-amazon.com/images/I/71uh7OjLpFL._AC_SL1500_.jpg",
 "Classic Lodge Cast Iron Skillet","A pre-seasoned skillet that lasts for decades. Timeless gift for home cooks and foodies."),
("Gifts for the Home Cook","B0C1YBPJ43","Astercook 15-Piece Knife Set with Block",4.8,"4K","https://m.media-amazon.com/images/I/61TheuxRpFL._AC_SL1500_.jpg",
 "Kitchen Knife Set With Block","A full knife set with built-in sharpener. Big-upgrade gift for the home cook or a new kitchen."),
("Stocking Stuffers for Women","B07XXPHQZK","LANEIGE Lip Sleeping Mask",4.6,"37.7K","https://m.media-amazon.com/images/I/51VfrPOslWL._SL1500_.jpg",
 "Laneige Lip Sleeping Mask","The cult-favorite overnight lip mask. Easy stocking stuffer for women and teens."),
("Stocking Stuffers for Women","B0009F3R7E","Burt's Bees Hand Repair Gift Set",4.7,"13.7K","https://m.media-amazon.com/images/I/81tIwBYvjiL._SL1500_.jpg",
 "Burt's Bees Hand Repair Gift Set","Hand cream, cuticle cream and gloves for dry winter hands. Ready-to-gift stocking stuffer for her."),
("Stocking Stuffers for Women","B00VK5SG46","Burt's Bees Classics Gift Set",4.7,"11.8K","https://m.media-amazon.com/images/I/91dGmlpvdxL._SL1500_.jpg",
 "Burt's Bees Classics Gift Tin","Six travel-size favorites in a giftable tin. Stocking stuffer idea for mom, sister, or coworkers."),
("Stocking Stuffers for Women","B0CP9YB3Q4","STANLEY Quencher H2.0 Tumbler 30 oz",4.7,"207K","https://m.media-amazon.com/images/I/51-U5dEbEBL._AC_SL1500_.jpg",
 "Stanley Quencher Tumbler","The tumbler everyone wants this year. Gift idea for her that gets used every single day."),
("Housewarming Gift Ideas","B07DL7ZV31","SMIRLY Charcuterie Board Set",4.8,"21K","https://m.media-amazon.com/images/I/8142dAEim3L._AC_SL1500_.jpg",
 "Charcuterie Board Set for Hosting","Bamboo cheese board with knives and serving pieces. Housewarming gift for new homeowners who love to host."),
("Housewarming Gift Ideas","B0821Y5BS3","AOZITA Glass Olive Oil Dispenser",4.7,"53.2K","https://m.media-amazon.com/images/I/61OYm+qDfhL._AC_SL1500_.jpg",
 "Glass Olive Oil Dispenser Bottle","A pretty countertop upgrade for a new kitchen. Simple, useful housewarming gift idea."),
("Housewarming Gift Ideas","B0B24QJ217","Clean Linen Reed Diffuser Set",4.4,"4.5K","https://m.media-amazon.com/images/I/71G8H9JSwXL._AC_SL1500_.jpg",
 "Clean Linen Reed Diffuser","Makes a new place smell fresh and lived-in. Easy housewarming gift for a first apartment."),
("Cozy Christmas Gift Ideas","B0H6W64L4Q","Winter Candle Gift Set, 6-Pack",4.4,"1.3K","https://m.media-amazon.com/images/I/71SCSl9MuPL._AC_SL1500_.jpg",
 "Winter Candle Gift Set","Six holiday-scented soy candles for cozy winter nights. Christmas gift idea for her and candle lovers."),
("Cozy Christmas Gift Ideas","B0FK2VMH2D","BEDELITE Christmas Snowflake Throw",4.6,"243","https://m.media-amazon.com/images/I/81NIyAcL8YL._AC_SL1500_.jpg",
 "Christmas Snowflake Throw Blanket","A festive red snowflake throw for movie nights. Cozy Christmas gift and holiday decor."),
("Cozy Christmas Gift Ideas","B088GD7LCK","Lenox Holiday Stoneware Mug",4.7,"390","https://m.media-amazon.com/images/I/71V8cUNMfWL._AC_SL1500_.jpg",
 "Lenox Holiday Mug","A classic holiday mug for cocoa season. Small Christmas gift or stocking stuffer."),
("At-Home Beauty Stocking Stuffers","B0CM6FJX1X","Beetles French Tip Press-On Nails",4.5,"7.5K","https://m.media-amazon.com/images/I/71WQuNMFbdL._SL1500_.jpg",
 "French Tip Press-On Nails","Salon-look French tips at home in minutes. Beauty stocking stuffer for her."),
("At-Home Beauty Stocking Stuffers","B09S4PVZ81","Kitsch Satin Heatless Curls Set",4.2,"31.1K","https://m.media-amazon.com/images/I/811lhxniH3L._SL1500_.jpg",
 "Heatless Curls Overnight Set","Soft curls while you sleep, no heat needed. Beauty gift idea and stocking stuffer."),
("At-Home Beauty Stocking Stuffers","B09Z7L79K6","Large Hair Claw Clips",4.7,"15.7K","https://m.media-amazon.com/images/I/71s4ej71miL._SL1500_.jpg",
 "Large Hair Claw Clips","Strong, neutral claw clips for thick hair. Easy beauty stocking stuffer for women and teens."),
("At-Home Beauty Stocking Stuffers","B0B2RM68G2","BIODANCE Bio-Collagen Real Deep Mask",4.5,"50.6K","https://m.media-amazon.com/images/I/51ubxqzNGIL._SL1000_.jpg",
 "Biodance Overnight Collagen Mask","The viral Korean overnight face mask. Self-care gift and beauty stocking stuffer for her."),
]

# posting order: rotate boards so each day mixes boards; 3 per day
order = []
byb = {}
for row in P: byb.setdefault(row[0], []).append(row)
boards = list(byb)
while any(byb.values()):
    for b in boards:
        if byb[b]: order.append(byb[b].pop(0))

start = dt.date(2026,10,23)
out = []
for i,(board,asin,prod,rating,rev,img,title,desc) in enumerate(order):
    tag = BEAUTY if board.startswith("At-Home Beauty") else CORE
    link = f"https://www.amazon.com/dp/{asin}?tag={tag}"
    full = f"{title}: {desc} {D}"
    assert len(full) <= 500, (asin, len(full))
    create = "https://www.pinterest.com/pin/create/button/?" + up.urlencode({"url":link,"media":img,"description":full})
    out.append(dict(n=i+1, date=str(start+dt.timedelta(days=i//3)), board=board, asin=asin, product=prod,
        rating=rating, reviews=rev, tag=tag, link=link, image=img, title=title, description=full, create_url=create))
json.dump(out, open("/home/claude/phase2/plan.json","w"), indent=1)
print(len(out)); print(out[0]["create_url"][:200])
for o in out: print(o["n"], o["date"], o["board"], "|", o["title"], len(o["description"]))
