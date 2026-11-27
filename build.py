#!/usr/bin/env python3
"""Koran 27 — The World in One Page.

Draws the 27 November 2026 front page as a flat editorial newspaper
illustration (1024x1024 PNG) with PIL only. No network, no randomness,
no external assets: every pixel is drawn from the six verified stories
in notes.md. Run: python3 build.py  ->  entry.png
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 40

PAPER = (247, 241, 229)
INK = (26, 26, 26)
RED = (176, 30, 36)
BLUE = (24, 84, 160)
GREY = (96, 92, 84)
CARD = (255, 253, 247)
LINE = (201, 194, 178)
NAVY = (29, 43, 69)
NAVY_CLOUD = (46, 61, 92)
RAIN = (140, 170, 210)
YELLOW = (250, 204, 21)
BALLOON = (214, 48, 49)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_ITALIC = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap; returns a list of lines that fit max_width."""
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        cur = ""
        for word in words:
            trial = (cur + " " + word).strip()
            if draw.textlength(trial, font=fnt) <= max_width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def centered(draw, text, y, fnt, fill, cx=W // 2, tracking=0):
    """Draw text centered on cx; tracking adds extra px between chars."""
    if tracking == 0:
        draw.text((cx - draw.textlength(text, font=fnt) / 2, y),
                  text, font=fnt, fill=fill)
        return
    widths = [draw.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += w + tracking


def lightning(draw, cx, cy, scale, fill=YELLOW):
    """Flat lightning bolt polygon centred on (cx, cy)."""
    pts = [
        (cx + 6 * scale, cy - 26 * scale),
        (cx - 10 * scale, cy + 2 * scale),
        (cx - 1 * scale, cy + 2 * scale),
        (cx - 6 * scale, cy + 26 * scale),
        (cx + 10 * scale, cy - 2 * scale),
        (cx + 1 * scale, cy - 2 * scale),
    ]
    draw.polygon(pts, fill=fill)


def flame(draw, cx, cy, scale):
    """Flat flame: orange outer teardrop, yellow inner teardrop."""
    outer = [
        (cx, cy - 24 * scale),
        (cx + 13 * scale, cy - 2 * scale),
        (cx + 9 * scale, cy + 14 * scale),
        (cx - 9 * scale, cy + 14 * scale),
        (cx - 13 * scale, cy - 2 * scale),
    ]
    inner = [
        (cx, cy - 8 * scale),
        (cx + 6 * scale, cy + 4 * scale),
        (cx + 4 * scale, cy + 13 * scale),
        (cx - 4 * scale, cy + 13 * scale),
        (cx - 6 * scale, cy + 4 * scale),
    ]
    draw.polygon(outer, fill=(214, 104, 24))
    draw.polygon(inner, fill=YELLOW)


def ballot(draw, x, y, size, fill=BLUE):
    """Ballot box with a white check mark."""
    draw.rectangle([x, y, x + size, y + size], fill=fill)
    draw.rectangle([x + size * 0.18, y - size * 0.28,
                    x + size * 0.82, y - size * 0.10], fill=fill)
    check = [(x + size * 0.16, y + size * 0.55),
             (x + size * 0.38, y + size * 0.78),
             (x + size * 0.86, y + size * 0.22),
             (x + size * 0.86, y + size * 0.38),
             (x + size * 0.40, y + size * 0.94),
             (x + size * 0.16, y + size * 0.70)]
    draw.polygon(check, fill=(255, 255, 255))


def shop_bag(draw, x, y, size):
    """Green shopping bag with a white percent sign."""
    draw.rectangle([x, y, x + size, y + size], fill=(26, 128, 84))
    draw.arc([x + size * 0.28, y - size * 0.30,
              x + size * 0.72, y + size * 0.30],
             start=180, end=360, fill=(26, 128, 84), width=max(2, size // 10))
    pct = font(SANS_BOLD, int(size * 0.52))
    draw.text((x + size * 0.22, y + size * 0.30), "%",
              font=pct, fill=(255, 255, 255))


def storm_panel(img, x, y, w, h):
    """Flat illustration: storm clouds, rain, lightning, grounded balloon.

    Drawn on its own canvas first so clouds and rain are clipped to the
    panel instead of spilling onto the paper.
    """
    panel = Image.new("RGB", (w, h), NAVY)
    p = ImageDraw.Draw(panel)
    for cx, cy, rx, ry in [(70, 42, 78, 30), (165, 26, 92, 34),
                           (265, 44, 84, 30), (315, 66, 58, 22)]:
        p.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=NAVY_CLOUD)
    for i in range(9):
        rx = 28 + i * 38
        p.line([(rx, 108), (rx - 10, 158)], fill=RAIN, width=4)
    lightning(p, w // 2 - 18, 148, 1.15)
    p.ellipse([w - 118, 138, w - 38, 178], fill=BALLOON)
    p.ellipse([w - 106, 148, w - 50, 168], fill=(232, 84, 84))
    p.text((14, h - 30), "NEW YORK  •  PARADE TO SAT 8:30AM",
           font=font(SANS_BOLD, 14), fill=(255, 255, 255))
    img.paste(panel, (x, y))


def story_card(draw, x, y, w, h, bar, icon, kicker, kicker_color,
               headline, deck):
    draw.rectangle([x, y, x + w, y + h], fill=CARD, outline=LINE, width=1)
    draw.rectangle([x, y, x + 8, y + h], fill=bar)
    tx = x + 66
    tw = w - 66 - 16
    icon(draw, x + 18, y + 26)
    draw.text((tx, y + 12), kicker, font=font(SANS_BOLD, 18),
              fill=kicker_color)
    hl = wrap(draw, headline, font(SERIF_BOLD, 28), tw)
    cy = draw_lines(draw, hl, tx, y + 36, font(SERIF_BOLD, 28), INK, 33)
    dk = wrap(draw, deck, font(SERIF, 18), tw)
    draw_lines(draw, dk, tx, cy + 5, font(SERIF, 18), (58, 56, 50), 23)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Top red bar.
    d.rectangle([0, 0, W, 14], fill=RED)

    # Masthead.
    centered(d, "THE WORLD", 26, font(SERIF_BOLD, 112), INK)
    d.line([(MARGIN, 152), (W - MARGIN, 152)], fill=INK, width=3)
    d.line([(MARGIN, 159), (W - MARGIN, 159)], fill=INK, width=1)
    centered(d, "FRIDAY, 27 NOVEMBER 2026", 172, font(SANS_BOLD, 29),
             RED, tracking=6)
    centered(d, "Six stories that defined the day — in one page", 210,
             font(SERIF_ITALIC, 24), GREY)
    d.line([(MARGIN, 246), (W - MARGIN, 246)], fill=INK, width=3)

    # ---- Lead story: the storm that stole Thanksgiving ----
    lx, lw = MARGIN, 556
    ly = 260
    d.text((lx, ly), "UNITED STATES  •  WEATHER", font=font(SANS_BOLD, 21),
           fill=RED)
    hl = wrap(d, "The storm that stole Thanksgiving",
              font(SERIF_BOLD, 52), lw)
    cy = draw_lines(d, hl, lx, ly + 30, font(SERIF_BOLD, 52), INK, 58)
    deck = ("A nor'easter battered the East Coast, cut power to "
            "800,000 homes and forced the first postponement of the "
            "Macy's parade in 100 years.")
    cy = draw_lines(d, wrap(d, deck, font(SERIF, 23), lw), lx, cy + 8,
                    font(SERIF, 23), (58, 56, 50), 29)
    d.text((lx, cy + 10), "800,000 without power  •  gusts to 70 mph",
           font=font(SANS_BOLD, 20), fill=BLUE)

    # Storm illustration panel, right of the lead.
    px, pw = 640, W - MARGIN - 640
    storm_panel(img, px, ly, pw, 252)

    d.line([(MARGIN, 540), (W - MARGIN, 540)], fill=INK, width=2)

    # ---- Four-story grid ----
    grid_y, card_h = 556, 154
    col_w = (W - 2 * MARGIN - 20) // 2
    story_card(d, MARGIN, grid_y, col_w, card_h, RED,
               lambda dr, x, y: lightning(dr, x + 20, y + 20, 0.85),
               "UKRAINE", RED,
               "Zelenskyy warns of a new strike on the power grid",
               "Kyiv braces as EU leaders split over a €45bn loan to "
               "fund Ukraine next year.")
    story_card(d, MARGIN + col_w + 20, grid_y, col_w, card_h, BLUE,
               lambda dr, x, y: ballot(dr, x + 2, y + 14, 36),
               "NEW ZEALAND", BLUE,
               "Final votes to decide a knife-edge parliament",
               "400,000 special votes counted as the final result "
               "tests the 67-seat majority.")
    story_card(d, MARGIN, grid_y + card_h + 16, col_w, card_h, (214, 104, 24),
               lambda dr, x, y: flame(dr, x + 20, y + 22, 0.95),
               "THAILAND", (186, 92, 16),
               "Blast at Bangkok refinery injures nine",
               "Bangchak shuts its Phra Khanong plant; three of the "
               "nine hurt are critical.")
    story_card(d, MARGIN + col_w + 20, grid_y + card_h + 16, col_w, card_h,
               (26, 128, 84),
               lambda dr, x, y: shop_bag(dr, x + 2, y + 8, 38),
               "BLACK FRIDAY", (22, 110, 70),
               "Deals deepen as shoppers hunt essentials",
               "Salesforce reports deeper November discounts; crowds "
               "chase gifts and groceries.")

    # ---- Sport strip ----
    sy = grid_y + 2 * card_h + 16 + 18
    d.line([(MARGIN, sy), (W - MARGIN, sy)], fill=INK, width=2)
    d.text((MARGIN, sy + 12), "SPORT", font=font(SANS_BOLD, 20), fill=RED)
    d.text((MARGIN + 92, sy + 11),
           "Steelers release Aaron Rodgers after ten starts  •  Sinner out "
           "of the Australian Open with a knee injury",
           font=font(SERIF, 21), fill=INK)
    d.line([(MARGIN, sy + 46), (W - MARGIN, sy + 46)], fill=INK, width=2)

    # ---- Footer ----
    centered(d, "Sources: The Times  •  WSJ  •  Reuters  •  AP  •  CNN  •  "
                "Newstalk ZB", sy + 62, font(SERIF_ITALIC, 19), GREY)
    centered(d, "Compiled on 27 November 2026  •  The World in One Page",
             sy + 90, font(SERIF_ITALIC, 19), GREY)

    img.save("entry.png", format="PNG")
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
