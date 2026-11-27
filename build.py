#!/usr/bin/env python3
"""Draw Koran 27 front page: 1024x1024, deterministic, no network, no randomness.
Writes entry.png next to this script. Run: python3 build.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1024, 1024

PAPER = (246, 241, 230)
INK = (26, 26, 26)
RED = (179, 38, 30)
BLUE = (29, 78, 137)
GOLD = (176, 124, 22)
GREY = (90, 86, 78)
LIGHT = (232, 226, 212)
DARKBLUE = (31, 42, 66)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

for p in (SERIF_B, SERIF_R, SERIF_I, SANS_B, SANS_R):
    assert os.path.exists(p), f"missing font {p}"


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, lines, font, fill, leading):
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += leading
    return y


def hline(d, x0, x1, y, fill=INK, w=2):
    d.line([(x0, y), (x1, y)], fill=fill, width=w)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

M = 40  # margin

# ---------- masthead ----------
d.rectangle([0, 0, W, 8], fill=RED)
f_title = F(SERIF_B, 108)
d.text((W // 2, 26), "THE WORLD", font=f_title, fill=INK, anchor="ma")
# thin double rule under title
hline(d, M, W - M, 150, INK, 3)
hline(d, M, W - M, 156, INK, 1)
f_date = F(SANS_B, 26)
d.text((W // 2, 166), "F R I D A Y ,  2 7  N O V E M B E R  2 0 2 6", font=f_date, fill=RED, anchor="ma")
f_tag = F(SERIF_I, 21)
d.text((W // 2, 202), "Six stories that defined the day — in one page",
       font=f_tag, fill=GREY, anchor="ma")
hline(d, M, W - M, 238, INK, 3)

# ---------- lead story ----------
LY = 258
# kicker
f_kick = F(SANS_B, 19)
d.text((M, LY), "UNITED STATES  •  WEATHER", font=f_kick, fill=RED)
f_head = F(SERIF_B, 47)
head_lines = wrap(d, "The storm that stole Thanksgiving", f_head, 560)
y = LY + 30
y = text_block(d, M, y, head_lines, f_head, INK, 54)
f_deck = F(SERIF_R, 21)
deck = ("A nor'easter battered the East Coast, cut power to "
        "800,000 homes and forced the first postponement in the "
        "Macy's parade's 100-year history.")
deck_lines = wrap(d, deck, f_deck, 560)
y = text_block(d, M, y + 8, deck_lines, f_deck, INK, 27)
f_fact = F(SANS_B, 18)
d.text((M, y + 10), "800,000 without power  •  gusts to 70 mph",
       font=f_fact, fill=BLUE)
d.text((M, y + 32), "100 balloons fly Saturday, 8:30am",
       font=f_fact, fill=BLUE)

# lead illustration: storm panel right
PX, PY, PW, PH = 640, LY + 6, 344, 252
d.rectangle([PX, PY, PX + PW, PY + PH], fill=DARKBLUE)
# clouds
for cx, cy, r in [(700, PY + 70, 52), (760, PY + 48, 62), (830, PY + 72, 50),
                  (900, PY + 60, 46), (940, PY + 84, 40)]:
    d.ellipse([cx - r, cy - r * 0.62, cx + r, cy + r * 0.62], fill=(58, 66, 92))
# rain streaks
for i, rx in enumerate(range(PX + 24, PX + PW - 10, 26)):
    d.line([(rx, PY + 120 + (i % 3) * 8), (rx - 8, PY + 168 + (i % 3) * 8)],
           fill=(140, 165, 200), width=4)
# lightning bolt
d.polygon([(800, PY + 130), (772, PY + 196), (790, PY + 196), (776, PY + 238),
           (822, PY + 168), (802, PY + 168)], fill=(255, 214, 64))
# grounded balloon (deflated, on the ground)
d.ellipse([868, PY + 168, 952, PY + 214], fill=(196, 52, 44))
d.ellipse([884, PY + 158, 936, PY + 188], fill=(220, 90, 80))
d.text((PX + 14, PY + PH - 32), "NEW YORK  •  100TH PARADE GROUNDED",
       font=F(SANS_B, 13), fill=(220, 225, 235))
d.rectangle([PX, PY, PX + PW, PY + PH], outline=INK, width=2)

hline(d, M, W - M, 540, INK, 2)

# ---------- grid 2x2 ----------
GRID_Y = 560
CELL_W, CELL_H = 462, 148
GAP_X, GAP_Y = 20, 16

stories = [
    ("UKRAINE", RED,
     "Zelenskyy warns of a new strike on the power grid",
     "Kyiv braces as EU leaders split over a €45bn loan to fund Ukraine next year."),
    ("NEW ZEALAND", BLUE,
     "Final votes to decide a knife-edge parliament",
     "The official count, 400,000 special votes included, tests the coalition's 67-seat majority."),
    ("THAILAND", (196, 90, 16),
     "Blast at Bangkok refinery injures nine",
     "Bangchak shuts every unit at its Phra Khanong plant; three of the hurt are critical."),
    ("BLACK FRIDAY", (22, 122, 62),
     "Deals deepen as shoppers hunt essentials",
     "Salesforce reports bigger November discounts than last year; crowds chase gifts and groceries."),
]


def icon(d, kind, x, y, s):
    """Small flat icon, s = box size."""
    if kind == 0:  # lightning / power
        d.polygon([(x + s * 0.55, y + 2), (x + s * 0.28, y + s * 0.58),
                   (x + s * 0.48, y + s * 0.58), (x + s * 0.38, y + s - 2),
                   (x + s * 0.72, y + s * 0.42), (x + s * 0.52, y + s * 0.42)],
                  fill=(255, 214, 64))
    elif kind == 1:  # ballot box
        d.rectangle([x + 4, y + s * 0.34, x + s - 4, y + s - 4], fill=(29, 78, 137))
        d.rectangle([x + s * 0.28, y + 2, x + s * 0.72, y + s * 0.34], fill=(29, 78, 137))
        d.line([(x + s * 0.24, y + s * 0.62), (x + s * 0.44, y + s * 0.82),
                (x + s * 0.78, y + s * 0.30)], fill=(255, 255, 255), width=5)
    elif kind == 2:  # flame
        d.polygon([(x + s * 0.5, y + 2), (x + s * 0.82, y + s * 0.42),
                   (x + s * 0.68, y + s * 0.42), (x + s * 0.78, y + s * 0.72),
                   (x + s * 0.5, y + s - 2), (x + s * 0.22, y + s * 0.72),
                   (x + s * 0.32, y + s * 0.42), (x + s * 0.18, y + s * 0.42)],
                  fill=(230, 90, 20))
        d.polygon([(x + s * 0.5, y + s * 0.5), (x + s * 0.66, y + s * 0.72),
                   (x + s * 0.5, y + s - 6), (x + s * 0.34, y + s * 0.72)],
                  fill=(255, 200, 40))
    else:  # shopping bag
        d.rectangle([x + 6, y + s * 0.3, x + s - 6, y + s - 4], fill=(22, 122, 62))
        d.arc([x + s * 0.28, y - 2, x + s * 0.72, y + s * 0.42], 180, 360,
              fill=(22, 122, 62), width=5)
        d.text((x + s // 2, y + s * 0.52), "%", font=F(SANS_B, 26),
               fill=(255, 255, 255), anchor="mm")


for i, (kick, col, head, summ) in enumerate(stories):
    cx = M + (i % 2) * (CELL_W + GAP_X)
    cy = GRID_Y + (i // 2) * (CELL_H + GAP_Y)
    d.rectangle([cx, cy, cx + CELL_W, cy + CELL_H], fill=(255, 255, 255),
                outline=(200, 194, 178), width=1)
    d.rectangle([cx, cy, cx + 6, cy + CELL_H], fill=col)
    icon(d, i, cx + 18, cy + 16, 44)
    tx = cx + 74
    d.text((tx, cy + 12), kick, font=F(SANS_B, 16), fill=col)
    f_gh = F(SERIF_B, 25)
    gh = wrap(d, head, f_gh, CELL_W - 92)
    yy = text_block(d, tx, cy + 36, gh, f_gh, INK, 29)
    f_gs = F(SERIF_R, 17)
    gs = wrap(d, summ, f_gs, CELL_W - 92)
    text_block(d, tx, yy + 4, gs, f_gs, (60, 58, 52), 21)

# ---------- sport strip + footer ----------
SY = GRID_Y + 2 * CELL_H + GAP_Y + 14
hline(d, M, W - M, SY, INK, 2)
f_sport_k = F(SANS_B, 17)
d.text((M, SY + 12), "SPORT", font=f_sport_k, fill=RED)
f_sport = F(SERIF_R, 20)
sport = ("Steelers release Aaron Rodgers after ten starts  •  "
         "Sinner out of the Australian Open with a knee injury")
d.text((M + 78, SY + 10), sport, font=f_sport, fill=INK)
hline(d, M, W - M, SY + 52, INK, 1)
f_foot = F(SERIF_I, 17)
d.text((W // 2, SY + 66),
       "Sources: The Times  •  WSJ  •  Reuters  •  AP  •  CNN  •  Newstalk ZB",
       font=f_foot, fill=GREY, anchor="ma")
d.text((W // 2, SY + 92), "Compiled on 27 November 2026  •  The World in One Page",
       font=F(SANS_R, 14), fill=GREY, anchor="ma")

out = os.path.join(HERE, "entry.png")
img.save(out, "PNG", optimize=True)
print("saved", out, os.path.getsize(out), "bytes")
