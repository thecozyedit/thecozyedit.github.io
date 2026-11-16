import json, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import FormulaRule

core = json.load(open("/home/claude/phase2/plan.json")) + json.load(open("/home/claude/phase3/plan2.json"))
bf = json.load(open("/home/claude/master/bf.json"))
posted = {1:"https://www.pinterest.com/pin/1092615559635809893/",2:"https://www.pinterest.com/pin/1092615559635809968/",3:"https://www.pinterest.com/pin/1092615559635810053/",
          4:"https://www.pinterest.com/pin/1092615559635908105/",5:"https://www.pinterest.com/pin/1092615559635908136/",6:"https://www.pinterest.com/pin/1092615559635908166/"}
SLUG = {"Cozy Gifts for Her":"gifts-for-her","Gifts for Homebodies":"homebody-gifts","Kitchen Gifts for Her":"kitchen-gifts-for-her","Gifts for the Home Cook":"home-cook-gifts",
 "Stocking Stuffers for Women":"stocking-stuffers-for-women","Housewarming Gift Ideas":"housewarming-gifts","Cozy Christmas Gift Ideas":"cozy-christmas-gifts","At-Home Beauty Stocking Stuffers":"beauty-stocking-stuffers"}

rows = []
for o in core:
    rows.append(dict(id=f"P{o['n']:03d}", product=o["product"], asin=o["asin"], board=o["board"], guide=SLUG[o["board"]], season="Holiday" if o["board"]=="Cozy Christmas Gift Ideas" else "Evergreen",
        rating=o["rating"], reviews=o["reviews"], title=o["title"], pin_date=o["date"], pin_status="Posted" if o["n"] in posted else "Scheduled", pin_url=posted.get(o["n"],""),
        site="Live", added="2026-10-23" if o["n"]<=30 else "2026-10-24", source="Batch 1" if o["n"]<=30 else "Batch 2", note=""))
for i, o in enumerate(bf):
    rows.append(dict(id=f"B{i+1:03d}", product=o["product"], asin=o["asin"], board=o["board"], guide="black-friday-gift-ideas", season="Black Friday",
        rating=o["rating"], reviews=o["reviews"], title=o["title"], pin_date="", pin_status="Not scheduled", pin_url="", site="Planned", added="2026-10-24", source="BF research", note=o.get("note","")))

wb = Workbook()
ws = wb.active; ws.title = "Products"
HDR = ["ID","Product","ASIN","Board","Website Guide","Season","Rating","Reviews","Pin Title","Pin Date","Pin Status","Pin URL","Site Status","Pinterest Link (cozeyditpin/beauty)","Website Link (cozeyditweb)","Date Added","Source","Notes"]
ws.append(["The Cozy Edit — Master Product List"]); ws["A1"].font = Font(name="Arial", size=14, bold=True, color="3B2A20")
ws.append(["One row per product. The website guides and the pin plan are built from this list. Yellow cells are inputs; link columns are formulas. No prices are stored or shown."])
ws["A2"].font = Font(name="Arial", size=9, italic=True, color="6E5646")
ws.append([])
ws.append(HDR)
H = 4
for c in ws[H]:
    c.font = Font(name="Arial", bold=True, color="FFFFFF", size=10); c.fill = PatternFill("solid", start_color="3B2A20"); c.alignment = Alignment(wrap_text=True, vertical="center")
thin = Side(style="thin", color="E2D5C4")
inp = PatternFill("solid", start_color="FFF8DC")
for i, r in enumerate(rows):
    R = H + 1 + i
    vals = [r["id"], r["product"], r["asin"], r["board"], r["guide"], r["season"], r["rating"], r["reviews"], r["title"], r["pin_date"], r["pin_status"], r["pin_url"], r["site"],
            f'="https://www.amazon.com/dp/"&C{R}&"?tag="&IF(D{R}="At-Home Beauty Stocking Stuffers","cozeyditbeauty-20","cozeyditpin-20")',
            f'="https://www.amazon.com/dp/"&C{R}&"?tag=cozeyditweb-20"', r["added"], r["source"], r["note"]]
    for j, v in enumerate(vals, 1):
        c = ws.cell(row=R, column=j, value=v)
        c.font = Font(name="Arial", size=9, color="000000" if j in (14,15) else "0000FF" if j in (2,3,4,6,7,8,9,11,13) else "000000")
        c.border = Border(bottom=thin)
        if j in (11, 13): c.fill = inp
    ws.cell(row=R, column=7).number_format = "0.0"
last = H + len(rows)
widths = [7,38,13,30,26,13,7,9,36,11,13,40,11,52,52,11,12,30]
for j, w in enumerate(widths, 1): ws.column_dimensions[get_column_letter(j)].width = w
ws.freeze_panes = "C5"
ws.auto_filter.ref = f"A{H}:{get_column_letter(len(HDR))}{last}"
dv1 = DataValidation(type="list", formula1='"Not scheduled,Scheduled,Posted,Paused,Retired"', allow_blank=True); ws.add_data_validation(dv1); dv1.add(f"K5:K{last+200}")
dv2 = DataValidation(type="list", formula1='"Planned,Live,Featured,Retired"', allow_blank=True); ws.add_data_validation(dv2); dv2.add(f"M5:M{last+200}")
dv3 = DataValidation(type="list", formula1='"Evergreen,Holiday,Black Friday"', allow_blank=True); ws.add_data_validation(dv3); dv3.add(f"F5:F{last+200}")
ws.conditional_formatting.add(f"A5:R{last+200}", FormulaRule(formula=['$F5="Black Friday"'], fill=PatternFill("solid", start_color="F6E3D6")))

# Summary
s = wb.create_sheet("Summary")
s.append(["Product Summary"]); s["A1"].font = Font(name="Arial", size=14, bold=True, color="3B2A20")
s.append([]); s.append(["Board","Products","Posted pins","Live on site","Black Friday"])
for c in s[3]: c.font = Font(name="Arial", bold=True, color="FFFFFF"); c.fill = PatternFill("solid", start_color="3B2A20")
boards = list(SLUG.keys())
for k, b in enumerate(boards):
    R = 4 + k
    s.append([b, f'=COUNTIF(Products!$D$5:$D${last+200},A{R})', f'=COUNTIFS(Products!$D$5:$D${last+200},A{R},Products!$K$5:$K${last+200},"Posted")',
              f'=COUNTIFS(Products!$D$5:$D${last+200},A{R},Products!$M$5:$M${last+200},"Live")', f'=COUNTIFS(Products!$D$5:$D${last+200},A{R},Products!$F$5:$F${last+200},"Black Friday")'])
T = 4 + len(boards)
s.append(["Total", f"=SUM(B4:B{T-1})", f"=SUM(C4:C{T-1})", f"=SUM(D4:D{T-1})", f"=SUM(E4:E{T-1})"])
for c in s[T]: c.font = Font(name="Arial", bold=True)
s.column_dimensions["A"].width = 34
for col in "BCDE": s.column_dimensions[col].width = 14

# How to use
h = wb.create_sheet("How to Use")
lines = ["How to use this list",
 "1. Add a product: new row with Product, ASIN (from the Amazon URL /dp/XXXXXXXXXX), Board and Season. Link columns fill in automatically.",
 "2. Pins: set Pin Status to Scheduled and give a Pin Date; the daily posting task posts Scheduled pins in date order and records Posted + Pin URL.",
 "3. Website: Site Status = Live puts the product on its guide page; Featured adds it to the guide's rotating 'Featured this week' block; Retired removes it.",
 "4. Black Friday rows (shaded) feed the Black Friday Gift Ideas page, planned to go live Nov 10-16.",
 "5. Rules: never add prices, deal or '% off' claims; never edit or upload Amazon images; keep the disclosure on every pin and page.",
 "Tracking IDs: cozeyditpin-20 (Pinterest core boards), cozeyditbeauty-20 (beauty board), cozeyditweb-20 (website). Ratings and reviews were as listed on Amazon on the date added."]
for i, t in enumerate(lines, 1):
    h.cell(row=i, column=1, value=t).font = Font(name="Arial", size=14 if i == 1 else 10, bold=(i == 1))
h.column_dimensions["A"].width = 140
out = "/home/claude/master/The_Cozy_Edit_Master_Product_List.xlsx"
wb.save(out); print(out, len(rows), last)
