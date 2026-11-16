import json, datetime as dt, urllib.parse as up
D = "As an Amazon Associate I earn from qualifying purchases."
CORE, BEAUTY = "cozeyditpin-20", "cozeyditbeauty-20"
I = "https://m.media-amazon.com/images/I/"
P = [
("Cozy Gifts for Her","B0BZR6YBHK","Bedsure Heated Throw Blanket",4.3,"10.1K","81qDj3mcqOL._AC_SL1500_.jpg","Heated Throw Blanket for Cold Nights","Soft heated throw with quick warm-up for chilly evenings on the couch. A cozy gift for her that gets used all winter."),
("Cozy Gifts for Her","B01LVU7THF","ZIMASILK Mulberry Silk Pillowcase",4.6,"52.2K","61h02IUI3OL._AC_SL1500_.jpg","Mulberry Silk Pillowcase","A smooth silk pillowcase that is gentle on hair and skin. Little luxury gift for her, mom, or your sister."),
("Cozy Gifts for Her","B01MFGN8S5","LifeAround2Angels Bath Bombs Gift Set",4.8,"46.5K","91dSs7Lcs4L._AC_SL1500_.jpg","Bath Bomb Gift Set for a Spa Night","Twelve fizzy bath bombs with shea and coconut for at-home spa nights. Easy self-care gift for her."),
("Cozy Gifts for Her","B0CG65PYBV","Rechargeable Hand Warmers, 2 Pack",4.6,"9.4K","719bvl0LppL._AC_SL1500_.jpg","Rechargeable Hand Warmers","Pocket-size, reusable hand warmers for cold commutes and winter walks. Practical cozy gift for her."),
("Gifts for Homebodies","B0062JSYEW","Taylors of Harrogate Tea Sampler",4.7,"29.8K","61MSYY5RLiL._AC_SL1500_.jpg","Tea Sampler Gift Box","Six classic teas in one pretty box for slow afternoons at home. Cozy gift for tea-loving homebodies."),
("Gifts for Homebodies","B0D13Z9HGV","Stained Glass Tree of Life 1000-Piece Puzzle",4.7,"2.9K","81hWonALyqL._AC_SL1500_.jpg","1000-Piece Puzzle for Cozy Nights In","A colorful stained-glass puzzle for long weekends in. Thoughtful gift for homebodies and puzzle lovers."),
("Gifts for Homebodies","B081CHLF46","JALL Sunrise Alarm Clock",4.3,"28.2K","61Hx5h-nysL._AC_SL1500_.jpg","Sunrise Alarm Clock for Dark Mornings","Wakes you with soft light instead of a loud alarm. Calming bedroom gift for homebodies."),
("Gifts for Homebodies","B0F9SY9K29","Trendy Queen Two-Piece Lounge Set",4.2,"3.7K","619CmfDPgVL._AC_SL1500_.jpg","Matching Lounge Set for Lazy Weekends","A soft two-piece set made for staying in. Cozy loungewear gift for her."),
("Kitchen Gifts for Her","B07GV2S1GS","Keurig K-Mini Coffee Maker",4.2,"109K","61rMfq0eODL._AC_SL1500_.jpg","Keurig K-Mini Single Serve Coffee Maker","Slim single-serve coffee maker for small kitchens and dorms. Kitchen gift idea for coffee lovers."),
("Kitchen Gifts for Her","B0C5GQ6DXM","TANG PIN Matcha Whisk and Bowl Set",4.7,"1.3K","616bcLZm5aL._AC_SL1500_.jpg","Matcha Whisk and Bowl Set","Everything for a cafe-style matcha ritual at home. Pretty kitchen gift for matcha lovers."),
("Kitchen Gifts for Her","B091GYGRZR","Moocoo Electric Wine Opener",4.7,"3K","61zslVgNQkS._AC_SL1500_.jpg","Electric Wine Opener With Charging Base","Opens a bottle at the push of a button. Hosting gift for wine lovers and holiday parties."),
("Kitchen Gifts for Her","B0CS3FBC6W","LAMU 2-Tier Lazy Susan Spice Organizer",4.7,"4.6K","71fghP75Q2L._AC_SL1500_.jpg","2-Tier Lazy Susan Spice Organizer","Turns a messy cabinet into a tidy, spinning spice station. Useful kitchen gift for her."),
("Kitchen Gifts for Her","B0BZYCJK89","Owala FreeSip Water Bottle, 24 oz",4.6,"143K","51VU5d5ySHL._AC_SL1500_.jpg","Owala FreeSip Water Bottle","The water bottle with a sip-or-swig lid that everyone is carrying. Everyday gift idea for her."),
("Gifts for the Home Cook","B06Y1YD5W7","Instant Pot Duo 7-in-1",4.7,"186.5K","71N1lhYC--L._AC_SL1500_.jpg","Instant Pot Duo 7-in-1 Pressure Cooker","Pressure cooker, slow cooker, rice cooker and more in one pot. Big-upgrade gift for the home cook."),
("Gifts for the Home Cook","B0FJQM8VTG","Electric Salt and Pepper Grinder Set",4.6,"5.2K","81dmiFkHSIL._AC_SL1500_.jpg","Electric Salt and Pepper Grinder Set","One-hand, rechargeable grinders that make seasoning easy. Kitchen gadget gift for anyone who loves to cook."),
("Gifts for the Home Cook","B08F79GXXM","Adjustable Kitchen Aprons, 2 Pack",4.6,"9.1K","71R9dGe+D2L._AC_SL1500_.jpg","Kitchen Aprons With Pockets","Two adjustable aprons with pockets for baking and holiday cooking. Simple gift for home cooks and bakers."),
("Gifts for the Home Cook","B00008WQ3L","Kamenstein 20-Jar Revolving Spice Rack",4.6,"15.8K","71AiuQKcleL._AC_SL1500_.jpg","Revolving Spice Rack With Spices","A countertop spice carousel that comes filled. Gift for home cooks setting up their kitchen."),
("Stocking Stuffers for Women","B074PVTPBW","Mighty Patch Original Pimple Patches",4.6,"186.8K","61p+1+md+8L._AC_SL1500_.jpg","Mighty Patch Pimple Patches","The cult-favorite overnight patches. Practical stocking stuffer for women and teens."),
("Stocking Stuffers for Women","B07QWBH37R","BomBombs Hot Chocolate Gift Set",4.6,"2.1K","81VIIczwzbL._AC_SL1500_.jpg","Hot Chocolate Bombs Gift Set","Melt-in-your-mug cocoa bombs for cozy winter nights. Sweet stocking stuffer for her."),
("Housewarming Gift Ideas","B0BJN5MHY1","Mrs. Meyer's Clean Day Gift Set",4.8,"3.3K","61JHTkKhBTL._AC_SL1500_.jpg","Mrs. Meyer's Clean Day Gift Set","Garden-scented hand soap and lotion for a fresh new kitchen. Easy housewarming gift."),
("Housewarming Gift Ideas","B09V7T4KLQ","MIULEE Velvet Throw Pillow Covers, 2 Pack",4.6,"69.8K","61R0FX7FAjL._AC_SL1500_.jpg","Velvet Throw Pillow Covers","Soft velvet covers that refresh a sofa instantly. Cozy housewarming gift for a first apartment."),
("Housewarming Gift Ideas","B0C7KQ6S3T","AlphaAcc Faux Potted Succulents",4.5,"802","71g+Mz6p9fL._AC_SL1500_.jpg","Faux Potted Succulents","Greenery with zero upkeep for shelves and desks. Simple housewarming gift for new homeowners."),
("Cozy Christmas Gift Ideas","B087X1X8VD","Gourmet Hot Cocoa Gift Set",4.5,"1.5K","814TzSv8lvL._AC_SL1500_.jpg","Gourmet Hot Cocoa Gift Set","A box of rich cocoa flavors for holiday movie nights. Cozy Christmas gift for the whole family."),
("Cozy Christmas Gift Ideas","B0BNKL2816","Keurig K-Cup Advent Calendar",4.4,"121","91qDwnUe49L._AC_SL1500_.jpg","Coffee Advent Calendar","A new coffee every morning in December. Fun Christmas countdown gift for coffee lovers."),
("Cozy Christmas Gift Ideas","B0F2MDFTK5","Amazon Essentials Christmas Pajamas",4.5,"441","71P8doK4MZL._AC_SL1500_.jpg","Cozy Christmas Pajamas","Soft holiday pajamas for Christmas morning photos. Festive gift for her and the family."),
("Cozy Christmas Gift Ideas","B0D896T46Y","Lighted Christmas Village Houses",4.3,"113","81296zu8AkL._AC_SL1500_.jpg","Lighted Christmas Village Houses","Glowing miniature houses for a cozy holiday mantel. Christmas decor gift for her."),
("At-Home Beauty Stocking Stuffers","B01LSUQSB0","REVLON One-Step Volumizer Hair Dryer",4.6,"352.9K","61SrWfdHa1L._AC_SL1500_.jpg","Revlon One-Step Volumizer","The viral hot-air brush for salon-style blowouts at home. Beauty gift idea for her."),
("At-Home Beauty Stocking Stuffers","B0BK9872HC","JODSONE Gel Nail Polish Kit with UV Light",4.4,"30.5K","71G-mlJMJsL._AC_SL1500_.jpg","Gel Nail Kit With UV Light","Everything for long-lasting gel nails at home. At-home beauty gift for her and teens."),
("At-Home Beauty Stocking Stuffers","B076Q6442Z","HEETA Scalp Massager Shampoo Brush",4.6,"154.4K","61aQt6lRLvL._AC_SL1500_.jpg","Scalp Massager Shampoo Brush","A soft silicone scalp brush that makes wash day feel like a spa. Tiny beauty stocking stuffer."),
("At-Home Beauty Stocking Stuffers","B08RD6S5HF","BAIMEI Gua Sha and Jade Roller Set",4.5,"38.2K","71ACduNmVAL._AC_SL1500_.jpg","Gua Sha and Ice Roller Set","Cooling face tools for a calming skincare routine. Self-care beauty stocking stuffer for her."),
]
order=[]; byb={}
for r in P: byb.setdefault(r[0],[]).append(r)
bs=list(byb)
while any(byb.values()):
    for b in bs:
        if byb[b]: order.append(byb[b].pop(0))
start=dt.date(2026,11,2); out=[]
for i,(board,asin,prod,rating,rev,img,title,desc) in enumerate(order):
    tag = BEAUTY if board.startswith("At-Home Beauty") else CORE
    link=f"https://www.amazon.com/dp/{asin}?tag={tag}"
    full=f"{title} (affiliate link): {desc} {D}"
    assert len(full)<=500 and len(title)<=100
    image=I+img
    out.append(dict(n=31+i,date=str(start+dt.timedelta(days=i//5)),board=board,asin=asin,product=prod,rating=rating,reviews=rev,tag=tag,link=link,image=image,title=title,description=full,
        create_url="https://www.pinterest.com/pin/create/button/?"+up.urlencode({"url":link,"media":image,"description":full})))
json.dump(out,open("/home/claude/phase3/plan2.json","w"),indent=1)
for o in out: print(o["n"],o["date"],o["board"],"|",o["title"])
