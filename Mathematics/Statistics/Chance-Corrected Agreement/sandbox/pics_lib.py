"""Drawing helpers for the vault's judge-validation pictures: rounded cards, cells, text, icons.
Everything is drawn at 2x and reduced, so edges are smooth. Final size is W x H = 1536 x 1024 (3:2)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, S = 1536, 1024, 2
FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
ITAL = "/System/Library/Fonts/Supplemental/Arial Italic.ttf"

INK, GREY, PALE = "#1F2A3A", "#5B6675", "#E6EBF2"
GREEN, GREEN_E = "#5BC283", "#2E8B57"
AMBER, AMBER_E = "#F6BC47", "#C98A12"
RED, RED_E = "#E5625E", "#B03632"
BLUE, BLUE_E, BLUE_BG = "#4C7FD0", "#2F5FA8", "#EAF1FB"
GREYCELL, GREYCELL_E = "#B9C0CB", "#7C8593"
BG = "#F5F8FC"


class Canvas:
    def __init__(self):
        self.img = Image.new("RGB", (W * S, H * S), BG)
        self.d = ImageDraw.Draw(self.img)
        self._fonts = {}

    def font(self, size, bold=False, italic=False):
        key = (size, bold, italic)
        if key not in self._fonts:
            self._fonts[key] = ImageFont.truetype(BOLD if bold else (ITAL if italic else FONT), int(size * S))
        return self._fonts[key]

    # shapes -------------------------------------------------------------
    def rect(self, x0, y0, x1, y1, fill=None, outline=None, width=1, radius=0):
        box = [x0 * S, y0 * S, x1 * S, y1 * S]
        if radius:
            self.d.rounded_rectangle(box, radius=radius * S, fill=fill, outline=outline, width=int(width * S))
        else:
            self.d.rectangle(box, fill=fill, outline=outline, width=int(width * S))

    def card(self, x0, y0, x1, y1, fill="white", outline=PALE, width=2, radius=18, shadow=True):
        if shadow:
            sh = Image.new("RGBA", self.img.size, (0, 0, 0, 0))
            sd = ImageDraw.Draw(sh)
            sd.rounded_rectangle([x0 * S, (y0 + 4) * S, x1 * S, (y1 + 4) * S], radius=radius * S, fill=(40, 60, 100, 60))
            sh = sh.filter(ImageFilter.GaussianBlur(7 * S))
            self.img.paste(sh, (0, 0), sh)
            self.d = ImageDraw.Draw(self.img)
        self.rect(x0, y0, x1, y1, fill=fill, outline=outline, width=width, radius=radius)

    def line(self, x0, y0, x1, y1, fill=INK, width=2, dash=None):
        if dash:
            import math
            L = math.hypot(x1 - x0, y1 - y0); n = int(L // (dash * 2))
            for i in range(n + 1):
                a = i * dash * 2 / L; b = min((i * dash * 2 + dash) / L, 1)
                self.d.line([(x0 + (x1 - x0) * a) * S, (y0 + (y1 - y0) * a) * S, (x0 + (x1 - x0) * b) * S, (y0 + (y1 - y0) * b) * S], fill=fill, width=int(width * S))
        else:
            self.d.line([x0 * S, y0 * S, x1 * S, y1 * S], fill=fill, width=int(width * S))

    def circle(self, cx, cy, r, fill=None, outline=None, width=1):
        self.d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], fill=fill, outline=outline, width=int(width * S))

    def arrow(self, x0, y0, x1, y1, fill=GREY, width=3, head=12):
        import math
        self.line(x0, y0, x1, y1, fill=fill, width=width)
        a = math.atan2(y1 - y0, x1 - x0)
        p = [(x1, y1), (x1 - head * math.cos(a - 0.45), y1 - head * math.sin(a - 0.45)), (x1 - head * math.cos(a + 0.45), y1 - head * math.sin(a + 0.45))]
        self.d.polygon([(x * S, y * S) for x, y in p], fill=fill)

    def bracket(self, x0, x1, y, color, h=14):
        """A bracket whose ends point down from the bar at y."""
        self.line(x0, y, x1, y, fill=color, width=3)
        self.line(x0, y, x0, y + h, fill=color, width=3)
        self.line(x1, y, x1, y + h, fill=color, width=3)

    # text ---------------------------------------------------------------
    def text(self, x, y, s, size=22, bold=False, fill=INK, anchor="la", italic=False):
        self.d.text((x * S, y * S), s, font=self.font(size, bold, italic), fill=fill, anchor=anchor)

    def width(self, s, size=22, bold=False):
        return self.font(size, bold).getlength(s) / S

    def chip(self, cx, cy, s, size=20, fill="white", outline=PALE, color=GREY, pad=16):
        w = self.width(s, size) + 2 * pad
        self.card(cx - w / 2, cy - 22, cx + w / 2, cy + 22, fill=fill, outline=outline, radius=22, shadow=False)
        self.text(cx, cy, s, size=size, fill=color, anchor="mm")

    # icons --------------------------------------------------------------
    def doc_check(self, x, y, size=70, ok=True):
        self.rect(x, y, x + size * 0.78, y + size, fill="white", outline=GREYCELL, width=3, radius=6)
        for i in range(4):
            self.line(x + size * .15, y + size * (.2 + .15 * i), x + size * (.6 if i % 2 == 0 else .5), y + size * (.2 + .15 * i), fill=GREYCELL, width=3)
        cx, cy, r = x + size * .72, y + size * .78, size * .24
        self.circle(cx, cy, r, fill=GREEN_E if ok else RED_E)
        self.line(cx - r * .5, cy, cx - r * .1, cy + r * .45, fill="white", width=4)
        self.line(cx - r * .1, cy + r * .45, cx + r * .55, cy - r * .4, fill="white", width=4)

    def stop_sign(self, cx, cy, r=26):
        import math
        pts = [(cx + r * math.cos(math.pi / 8 + i * math.pi / 4), cy + r * math.sin(math.pi / 8 + i * math.pi / 4)) for i in range(8)]
        self.d.polygon([(x * S, y * S) for x, y in pts], fill="#4A5260", outline="#2C323C")
        self.text(cx, cy, "STOP", size=int(r * .5), bold=True, fill="white", anchor="mm")

    def tick(self, cx, cy, r=15):
        self.circle(cx, cy, r, fill=GREEN_E)
        self.line(cx - r * .5, cy, cx - r * .1, cy + r * .45, fill="white", width=3)
        self.line(cx - r * .1, cy + r * .45, cx + r * .55, cy - r * .4, fill="white", width=3)

    # output -------------------------------------------------------------
    def save_webp(self, path):
        out = self.img.resize((W, H), Image.LANCZOS)
        out.save(path, "WEBP", quality=90)
        return out
