"""Draws the three pictures for the vault note Gaussian Integral, section "The area under the bell",
from the prompts in ../Gaussian Integral.md. Every height, bar and printed number is computed here.

Run:  python3 make_figures.py
Writes SVG and PNG attempts to ~/.cache/codex-drop/obsidian/gaussian-integral/ and the WebP
(quality 90) to the note's assets/ folder. Each figure is laid out in 800-unit coordinates
(the reading width) and rasterised at 2x.
"""
import json, math, os, subprocess, sys
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, '..', '..', 'Mathematics', 'Calculus', 'Integration', 'assets'))
DROP = os.path.expanduser('~/.cache/codex-drop/obsidian/gaussian-integral')
SCALE = 2

INK, MUTE, BG, CARD, LINE = '#1e293b', '#5b6675', '#f6f8fb', '#ffffff', '#d5dde8'
BLUE, BLUE_T, BLUE_S = '#2563eb', '#dbe7fd', '#eef4ff'
ORANGE, ORANGE_T, ORANGE_S = '#e8710a', '#fde3c8', '#fff4ea'
GREEN, GREEN_T, GREEN_S = '#15803d', '#cdeed8', '#effaf2'
RED = '#c62828'
SANS, MONO = 'DejaVu Sans', 'DejaVu Sans Mono'

_fonts = {}


def width(t, size, bold=False, italic=False, mono=False):
    from PIL import ImageFont
    spec = (MONO if mono else SANS) + (':bold' if bold else '') + (':italic' if italic else '')
    if spec not in _fonts:
        path = subprocess.check_output(['fc-match', '-f', '%{file}', spec]).decode()
        _fonts[spec] = ImageFont.truetype(path, 200)
    return _fonts[spec].getlength(t) * size / 200


def bell(x, mu=0.0):
    return math.exp(-(x - mu) ** 2)


class Canvas:
    def __init__(self, w, h, title):
        self.w, self.h, self.title = w, h, title
        self.parts, self.labels = [], []   # labels: (x0, y0, x1, y1, text) for the overlap check

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, t, size=20, fill=INK, bold=False, italic=False, mono=False, anchor='start', record=True):
        w = width(t, size, bold, italic, mono)
        x0 = {'start': x, 'middle': x - w / 2, 'end': x - w}[anchor]
        fam = MONO if mono else SANS
        self.add(f'<text x="{x0:.1f}" y="{y:.1f}" font-family="{fam}" font-size="{size:.1f}" '
                 f'font-weight="{700 if bold else 400}" font-style="{"italic" if italic else "normal"}" '
                 f'fill="{fill}">{escape(t)}</text>')
        if record:
            self.labels.append((x0, y - size * 0.78, x0 + w, y + size * 0.24, t))
        return x0 + w

    def math(self, x, y, runs, size, fill=INK, anchor='start', measure_only=False):
        """runs: list of (text, style). style: 'n' upright, 'i' italic, '^n'/'^i' superscript,
        'int' a large integral sign, 'lim' a (top, bottom) pair stacked as limits."""
        def piece_w(t, st):
            if st == 'int': return width(t, size * 1.45) * 0.92
            if st == 'lim': return max(width(t[0], size * .6), width(t[1], size * .6)) + size * .08
            sz = size * .66 if st.startswith('^') else size
            return width(t, sz, italic=st.endswith('i')) + (size * .04 if st.endswith('i') else 0)
        total = sum(piece_w(t, st) for t, st in runs)
        if measure_only: return total
        cx = {'start': x, 'middle': x - total / 2, 'end': x - total}[anchor]
        x0 = cx
        for t, st in runs:
            w = piece_w(t, st)
            if st == 'int':
                self.add(f'<text x="{cx:.1f}" y="{y + size * .2:.1f}" font-family="{SANS}" font-size="{size * 1.45:.1f}" fill="{fill}">∫</text>')
            elif st == 'lim':
                s2 = size * .6
                self.add(f'<text x="{cx:.1f}" y="{y - size * .78:.1f}" font-family="{SANS}" font-size="{s2:.1f}" fill="{fill}">{escape(t[0])}</text>')
                self.add(f'<text x="{cx - size * .12:.1f}" y="{y + size * .42:.1f}" font-family="{SANS}" font-size="{s2:.1f}" fill="{fill}">{escape(t[1])}</text>')
            else:
                sup = st.startswith('^')
                sz = size * .66 if sup else size
                yy = y - size * .42 if sup else y
                it = st.endswith('i')
                self.add(f'<text x="{cx:.1f}" y="{yy:.1f}" font-family="{SANS}" font-size="{sz:.1f}" '
                         f'font-style="{"italic" if it else "normal"}" fill="{fill}">{escape(t).replace(" ", chr(160))}</text>')
            cx += w
        self.labels.append((x0, y - size * 0.95, cx, y + size * 0.28, ''.join(t if isinstance(t, str) else ''.join(t) for t, _ in runs)))
        return x0, cx

    def card(self, x, y, w, h, fill=CARD, stroke=LINE, rx=16, sw=1.5):
        self.add(f'<rect x="{x:.1f}" y="{y + 4:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="#0f172a" fill-opacity="0.05"/>')
        self.add(f'<rect x="{x:.1f}" y="{y + 1.5:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="#0f172a" fill-opacity="0.05"/>')
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def line(self, x1, y1, x2, y2, col=INK, w=1.5, dash=None, op=1):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}" stroke-opacity="{op}" stroke-linecap="round"{d}/>')

    def arrowhead(self, x, y, ang, col, size=12):
        l = (x - size * math.cos(ang) + size * .45 * math.sin(ang), y - size * math.sin(ang) - size * .45 * math.cos(ang))
        r = (x - size * math.cos(ang) - size * .45 * math.sin(ang), y - size * math.sin(ang) + size * .45 * math.cos(ang))
        self.add(f'<polygon points="{x:.1f},{y:.1f} {l[0]:.1f},{l[1]:.1f} {r[0]:.1f},{r[1]:.1f}" fill="{col}"/>')

    def arrow(self, x1, y1, x2, y2, col=INK, w=2, head=12):
        ang = math.atan2(y2 - y1, x2 - x1)
        self.line(x1, y1, x2 - head * .8 * math.cos(ang), y2 - head * .8 * math.sin(ang), col, w)
        self.arrowhead(x2, y2, ang, col, head)

    def dot(self, x, y, r=4.5, col=INK):
        self.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>')

    def marker(self, x, y, n, r=14):
        self.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{RED}"/>')
        self.text(x, y + 6.5, str(n), 18, '#ffffff', bold=True, anchor='middle', record=False)

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" '
                f'role="img" aria-label="{escape(self.title)}">\n<rect width="{self.w}" height="{self.h}" fill="{BG}"/>\n'
                + '\n'.join(self.parts) + '\n</svg>\n')


class Plot:
    """Maps (x, height) to canvas pixels: x from lo to hi across [px0, px1], height 0 at y0, 1 at y0 - hpx."""
    def __init__(self, lo, hi, px0, px1, y0, hpx):
        self.lo, self.hi, self.px0, self.px1, self.y0, self.hpx = lo, hi, px0, px1, y0, hpx
    def X(self, x): return self.px0 + (x - self.lo) * (self.px1 - self.px0) / (self.hi - self.lo)
    def Y(self, h): return self.y0 - h * self.hpx
    def curve(self, f, a=None, b=None, n=400):
        a = self.lo if a is None else a; b = self.hi if b is None else b
        return [(self.X(a + (b - a) * i / n), self.Y(f(a + (b - a) * i / n))) for i in range(n + 1)]


def path(pts, close_to=None):
    d = 'M' + ' L'.join(f'{x:.2f} {y:.2f}' for x, y in pts)
    if close_to is not None:
        d += f' L{pts[-1][0]:.2f} {close_to:.2f} L{pts[0][0]:.2f} {close_to:.2f} Z'
    return d


def draw_bell(c, p, mu=0.0, stroke=BLUE, fill=BLUE_T, sw=3, fill_op=1.0, stroke_op=1.0, dash=None):
    pts = p.curve(lambda x: bell(x, mu))
    if fill:
        c.add(f'<path d="{path(pts, p.y0)}" fill="{fill}" fill-opacity="{fill_op}" stroke="none"/>')
    d = f' stroke-dasharray="{dash}"' if dash else ''
    c.add(f'<path d="{path(pts)}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-opacity="{stroke_op}" stroke-linejoin="round"{d}/>')


E_NEG_X2 = [('e', 'n'), ('−', '^n'), ('x', '^i'), ('²', '^n')]
E_NEG_X1_2 = [('e', 'n'), ('−(', '^n'), ('x', '^i'), ('+1)²', '^n')]
CENTRES = [-3 + 0.5 * k for k in range(13)]


# ---------------------------------------------------------------------------------------------
def fig_form():
    c = Canvas(800, 640, 'The Gaussian integral: each piece of the formula names one part of the bell picture')
    c.card(16, 16, 768, 608)
    # the integral, four chips
    size, base = 40, 128
    pieces = [('I', [('I', 'i')], BLUE_S, BLUE, 'area'),
              ('=', [('=', 'n')], None, None, None),
              ('lim', [('∫', 'int'), (('∞', '−∞'), 'lim')], '#f1f4f8', '#64748b', 'the whole line'),
              ('e', E_NEG_X2, ORANGE_S, ORANGE, 'height at x'),
              ('dx', [('d', 'n'), ('x', 'i')], ORANGE_S, ORANGE, 'thin width')]
    gap, pad = 30, 16
    widths = [c.math(0, 0, r, size, measure_only=True) + (2 * pad if fill else 0) for _, r, fill, _, _ in pieces]
    total = sum(widths) + gap * (len(pieces) - 1)
    x = 400 - total / 2
    chips = {}
    for (key, runs, fill, stroke, cap), w in zip(pieces, widths):
        if fill:
            top, bot = base - 62, base + 34
            c.add(f'<rect x="{x:.1f}" y="{top:.1f}" width="{w:.1f}" height="{bot - top:.1f}" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
            c.math(x + pad, base, runs, size)
            c.text(x + w / 2, bot + 30, cap, 19, MUTE, anchor='middle')
            chips[key] = (x, top, x + w, bot)
        else:
            c.math(x, base, runs, size)
        x += w + gap
    # the plot
    p = Plot(-3.5, 3.5, 66, 734, 548, 300)
    draw_bell(c, p)
    # number line with outward arrows at both ends
    c.line(44, p.y0, 756, p.y0, INK, 2)
    c.arrowhead(42, p.y0, math.pi, INK, 15)
    c.arrowhead(758, p.y0, 0, INK, 15)
    for k in range(-3, 4):
        c.line(p.X(k), p.y0 - 6, p.X(k), p.y0 + 6, INK, 2)
        c.text(p.X(k), p.y0 + 32, f'{k}'.replace('-', '-'), 19, INK, anchor='middle')
    c.text(758, p.y0 + 32, 'x', 20, INK, italic=True, anchor='middle')
    # the one strip near x = 1
    a, b = 0.9, 1.1
    sx0, sx1, stop = p.X(a), p.X(b), p.Y(bell(1.0))
    c.add(f'<rect x="{sx0:.1f}" y="{stop:.1f}" width="{sx1 - sx0:.1f}" height="{p.y0 - stop:.1f}" fill="{ORANGE_T}" fill-opacity="0.9" stroke="{ORANGE}" stroke-width="2.5"/>')
    # its width, dx, marked just above its top
    wy = stop - 14
    c.line(sx0, wy, sx1, wy, ORANGE, 2); c.line(sx0, wy - 6, sx0, wy + 6, ORANGE, 2); c.line(sx1, wy - 6, sx1, wy + 6, ORANGE, 2)
    dxl = c.math(p.X(1.0), wy - 14, [('d', 'n'), ('x', 'i')], 22, ORANGE, anchor='middle')
    # its height, e^(-x^2), marked on its left side
    hx = sx0 - 12
    c.line(hx, stop, hx, p.y0, ORANGE, 2); c.line(hx - 6, stop, hx + 6, stop, ORANGE, 2); c.line(hx - 6, p.y0, hx + 6, p.y0, ORANGE, 2)
    ehl = c.math(hx - 10, p.Y(0.17), E_NEG_X2, 24, ORANGE, anchor='end')
    # heights named: 1 at the peak, 0.3679 at x = -1
    c.dot(p.X(0), p.Y(1), 5, BLUE); c.text(p.X(0) + 14, p.Y(1) + 2, '1', 20, BLUE, bold=True)
    c.dot(p.X(-1), p.Y(bell(-1)), 5, BLUE); c.text(p.X(-1) - 12, p.Y(bell(-1)) - 6, f'{bell(-1):.4f}', 20, BLUE, bold=True, anchor='end')
    # leader lines, one per chip, ending on what it names
    lead = '#475569'
    def leader(x1, y1, x2, y2):
        c.line(x1, y1, x2, y2, lead, 1.8); c.dot(x2, y2, 4.5, lead)
    cap_bottom = base + 34 + 40
    ix = (chips['I'][0] + chips['I'][2]) / 2
    area_pt = (p.X(-0.55), p.Y(0.28))
    leader(ix, cap_bottom, *area_pt)
    ex = (chips['e'][0] + chips['e'][2]) / 2
    leader(ex, cap_bottom, hx, stop - 4)
    dx_c = (chips['dx'][0] + chips['dx'][2]) / 2
    leader(dx_c, cap_bottom, (dxl[0] + dxl[1]) / 2 + 4, wy - 14 - 22 * 0.8 - 6)
    # the limits chip: elbow above the chips, down the left margin, to the left outward arrow
    lx = (chips['lim'][0] + chips['lim'][2]) / 2
    top = chips['lim'][1]
    # one line naming both ends: up from the chip, across the top, down both margins to both arrows
    c.line(lx, top, lx, 38, lead, 1.8)
    route = [(36, p.y0 - 14), (30, p.y0 - 30), (30, 38), (770, 38), (770, p.y0 - 30), (764, p.y0 - 14)]
    c.add(f'<path d="{path(route)}" fill="none" stroke="{lead}" stroke-width="1.8" stroke-linejoin="round"/>')
    c.dot(36, p.y0 - 14, 4.5, lead); c.dot(764, p.y0 - 14, 4.5, lead)
    checks = {'peak_px': (p.X(0), p.Y(1)), 'h_at_1': bell(1.0), 'strip': [a, b], 'axis_y': p.y0,
              'leaders': [((ix, cap_bottom), area_pt)]}
    return c, checks


def fig_mechanism():
    c = Canvas(800, 560, 'Thirteen rectangles of width 0.5 measure the bell; sliding the bell left by 1 keeps its area')
    s = 50.0  # px per unit of x, shared by both panels; 260 px per unit of height, shared too
    hpx, y0 = 260, 404
    c.card(16, 16, 420, 528, BLUE_S, '#bcd0f7')
    c.card(452, 16, 332, 528, GREEN_S, '#b5dcc2')
    L = Plot(-3.5, 3.5, 51, 51 + 7 * s, y0, hpx)
    Rr = Plot(-3.3, 2.5, 470, 470 + 5.8 * s, y0, hpx)
    c.text(36, 58, 'rectangles', 24, INK, bold=True)
    c.text(472, 58, 'slid left by 1', 24, INK, bold=True)
    for p in (L, Rr):
        c.line(p.px0 - 6, p.Y(1), p.px1 + 6, p.Y(1), '#94a3b8', 1.2, '4 5')
    # left: 13 orange bars under the blue bell
    heights = [bell(x) for x in CENTRES]
    for x, h in zip(CENTRES, heights):
        c.add(f'<rect x="{L.X(x - .25):.2f}" y="{L.Y(h):.2f}" width="{s * .5:.2f}" height="{h * hpx:.2f}" fill="{ORANGE_T}" stroke="{ORANGE}" stroke-width="1.6"/>')
    c.line(L.px0 - 8, y0, L.px1 + 8, y0, INK, 2)
    draw_bell(c, L, fill=None)
    for x, h in zip(CENTRES, heights):   # the outer bars are under a pixel tall: drawn last so they show on the axis
        if h < 0.01:
            c.add(f'<rect x="{L.X(x - .25) + 1:.2f}" y="{L.Y(h) - 1.2:.2f}" width="{s * .5 - 2:.2f}" height="{max(h * hpx, 0) + 1.2:.2f}" fill="{ORANGE}" stroke="none"/>')
    for x in CENTRES:
        if bell(x) > 0.01:
            c.dot(L.X(x), L.Y(bell(x)), 3.2, ORANGE)
    printed = {}
    c.text(L.X(0), L.Y(1) - 12, '1', 20, ORANGE, bold=True, anchor='middle'); printed[0.0] = '1'
    for x in (0.5, 1.0, 1.5):
        t = f'{bell(x):.4f}'
        c.text(L.X(x + .25) + 6, L.Y(bell(x)) + 7, t, 20, ORANGE, bold=True); printed[x] = t
    c.math(L.X(-2.0), L.Y(0.62), E_NEG_X2, 24, BLUE, anchor='middle')
    for k in (-1, 0):
        c.line(L.X(k), y0, L.X(k), y0 + 7, INK, 2)
        c.text(L.X(k), y0 + 30, str(k), 19, INK, anchor='middle')
    c.text(L.px1 + 12, y0 + 30, 'x', 20, INK, italic=True, anchor='middle')
    wy = y0 + 46
    c.line(L.X(-2.25), wy, L.X(-1.75), wy, ORANGE, 2)
    c.line(L.X(-2.25), wy - 6, L.X(-2.25), wy + 6, ORANGE, 2); c.line(L.X(-1.75), wy - 6, L.X(-1.75), wy + 6, ORANGE, 2)
    c.line(L.X(-2.25), y0 + 2, L.X(-2.25), wy - 6, ORANGE, 1, '3 3'); c.line(L.X(-1.75), y0 + 2, L.X(-1.75), wy - 6, ORANGE, 1, '3 3')
    c.text(L.X(-2.0), wy + 26, 'width 0.5', 19, ORANGE, anchor='middle')
    total = sum(heights)
    c.text(226, 522, f'0.5 × {total:.4f} = {0.5 * total:.4f}', 24, INK, bold=True, anchor='middle')
    # right: faint blue bell behind, green bell slid left by 1
    draw_bell(c, Rr, 0.0, BLUE, None, 2.2, stroke_op=0.4, dash='7 5')
    draw_bell(c, Rr, -1.0, GREEN, GREEN_T, 3, fill_op=0.85)
    c.math(Rr.X(-1.0), Rr.Y(0.12), E_NEG_X1_2, 22, GREEN, anchor='middle')
    c.dot(Rr.X(0), Rr.Y(1), 5, BLUE); c.dot(Rr.X(-1), Rr.Y(1), 5, GREEN)
    ay = Rr.Y(1) - 18
    c.arrow(Rr.X(0), ay, Rr.X(-1) + 2, ay, INK, 2.2, 12)
    c.line(Rr.X(0), ay, Rr.X(0), Rr.Y(1) - 6, INK, 1.2, '2 3')
    c.line(Rr.X(-1), ay, Rr.X(-1), Rr.Y(1) - 6, INK, 1.2, '2 3')
    c.text(Rr.X(-0.5), ay - 14, 'slide by 1', 20, INK, anchor='middle')
    c.line(Rr.px0 - 8, y0, Rr.px1 + 8, y0, INK, 2)
    for k in (-1, 0):
        c.line(Rr.X(k), y0, Rr.X(k), y0 + 7, INK, 2)
        c.text(Rr.X(k), y0 + 30, str(k), 19, INK, anchor='middle')
    c.text(Rr.px1 + 12, y0 + 30, 'x', 20, INK, italic=True, anchor='middle')
    fine = 0.001 * sum(bell(-6 + 0.001 * i) for i in range(12000))
    fine_slid = 0.001 * sum(bell(-7 + 0.001 * i, -1.0) for i in range(12000))
    c.text(618, 522, f'same area: {fine_slid:.6f}', 24, INK, bold=True, anchor='middle')
    checks = {'bars': [(L.X(x - .25), L.X(x + .25), L.Y(bell(x))) for x in CENTRES], 'printed': printed,
              'sum': round(total, 4), 'area': round(0.5 * total, 4), 'fine': round(fine, 6), 'fine_slid': round(fine_slid, 6),
              'green_peak_px': Rr.X(-1), 'blue_peak_px_right': Rr.X(0), 'peak_y': Rr.Y(1), 'y0': y0, 'hpx': hpx,
              'left_px': (L.px0, L.px1), 'right_px': (Rr.px0, Rr.px1)}
    return c, checks


RUN = [
    '$ ~/.vault-sandbox/bin/python area.py',
    'heights at x = 0, 0.5, ..., 3:',
    '  x = 0.0   e^(-x^2) = 1.0000',
    '  x = 0.5   e^(-x^2) = 0.7788',
    '  x = 1.0   e^(-x^2) = 0.3679',
    '  x = 1.5   e^(-x^2) = 0.1054',
    '  x = 2.0   e^(-x^2) = 0.0183',
    '  x = 2.5   e^(-x^2) = 0.0019',
    '  x = 3.0   e^(-x^2) = 0.0001',
    'rectangles, width 0.5, x = -3..3: 13 of them',
    '  sum of heights: 3.5449',
    '  area: 1.7724',
    'rectangles, width 0.001, x = -6..6: 1.772454',
]
MARKERS = {2: 1, 4: 2, 8: 3, 9: 4, 10: 5, 11: 6, 12: 7}   # line index -> marker number, placed after the line's last field
CARDS = ['the peak: e⁰ = 1', 'one step out: e⁻¹, a third of the peak', 'at x = 3: e⁻⁹, the tail is gone',
         'one rectangle at each of −3, −2.5, ..., 3', "the peak plus each side's six heights",
         'width 0.5 times the sum of heights', 'width 0.001: the area to six decimals']


def fig_sheet():
    W = 800
    c = Canvas(W, 1500, 'Deep-dive sheet: the form, the mechanism, the area.py run, and reading it field by field')
    # pane 1, the form
    y = 16
    c.card(16, y, 768, 262)
    c.text(40, y + 40, 'The form', 24, INK, bold=True)
    c.math(400, y + 92, [('I', 'i'), (' = ', 'n'), ('∫', 'int'), (('∞', '−∞'), 'lim'), (' ', 'n')] + E_NEG_X2 + [(' d', 'n'), ('x', 'i')], 32, anchor='middle')
    p1 = Plot(-3.5, 3.5, 225, 575, y + 238, 112)
    draw_bell(c, p1)
    c.line(p1.px0 - 10, p1.y0, p1.px1 + 10, p1.y0, INK, 2)
    c.arrowhead(p1.px0 - 12, p1.y0, math.pi, INK, 11); c.arrowhead(p1.px1 + 12, p1.y0, 0, INK, 11)
    # pane 2, the mechanism
    y = 294
    c.card(16, y, 768, 236)
    c.text(40, y + 40, 'The mechanism', 24, INK, bold=True)
    p2 = Plot(-3.5, 3.5, 225, 575, y + 176, 130)
    for x in CENTRES:
        h = bell(x)
        c.add(f'<rect x="{p2.X(x - .25):.2f}" y="{p2.Y(h):.2f}" width="{p2.X(.25) - p2.X(-.25):.2f}" height="{h * 130:.2f}" fill="{ORANGE_T}" stroke="{ORANGE}" stroke-width="1.4"/>')
    c.line(p2.px0 - 10, p2.y0, p2.px1 + 10, p2.y0, INK, 2)
    draw_bell(c, p2, fill=None, sw=2.6)
    for x in CENTRES:
        h = bell(x)
        if h < 0.01:
            c.add(f'<rect x="{p2.X(x - .25) + 1:.2f}" y="{p2.Y(h) - 1.2:.2f}" width="{p2.X(.25) - p2.X(-.25) - 2:.2f}" height="{h * 130 + 1.2:.2f}" fill="{ORANGE}" stroke="none"/>')
    total = sum(bell(x) for x in CENTRES)
    c.text(p2.X(0), y + 214, f'0.5 × {total:.4f} = {0.5 * total:.4f}', 22, INK, bold=True, anchor='middle')
    # pane 3, the run (the focal pane)
    y = 546
    lh, fs = 36, 21
    ph = 72 + lh * len(RUN) + 24
    c.card(16, y, 768, ph, '#ffffff', '#9aa9bd', 16, 2.2)
    c.text(40, y + 40, 'The run', 24, INK, bold=True)
    c.add(f'<rect x="36" y="{y + 60}" width="728" height="{lh * len(RUN) + 22}" rx="12" fill="#fbfbf8" stroke="#e2e6ea"/>')
    cw = width('0', fs, mono=True)
    tx = 58
    run_boxes = []
    for i, line in enumerate(RUN):
        by = y + 60 + 34 + i * lh
        col = '#1d6b33' if i == 0 else INK
        # place each run of non-space characters at its exact column, so every space survives
        j = 0
        while j < len(line):
            if line[j] == ' ':
                j += 1; continue
            k = j
            while k < len(line) and line[k] != ' ':
                k += 1
            c.text(tx + j * cw, by, line[j:k], fs, col, mono=True, record=False)
            j = k
        c.labels.append((tx, by - fs * .78, tx + len(line) * cw, by + fs * .24, line))
        run_boxes.append((tx, by, tx + len(line) * cw))
        if i in MARKERS:
            c.marker(tx + len(line) * cw + 22, by - 7, MARKERS[i])
    # pane 4, reading it
    y = 546 + ph + 16
    ch, cg = 50, 10
    c.card(16, y, 768, 64 + 7 * (ch + cg) + 6)
    c.text(40, y + 40, 'Reading it', 24, INK, bold=True)
    for n, t in enumerate(CARDS, 1):
        cy = y + 60 + (n - 1) * (ch + cg)
        c.add(f'<rect x="36" y="{cy}" width="728" height="{ch}" rx="12" fill="#fff6f5" stroke="#f1c9c6" stroke-width="1.4"/>')
        c.marker(64, cy + ch / 2, n)
        c.text(92, cy + ch / 2 + 7.5, t, 21, INK)
    c.h = int(y + 64 + 7 * (ch + cg) + 6 + 16)
    checks = {'run': RUN, 'run_boxes': run_boxes, 'sum': round(total, 4), 'cards': CARDS, 'H': c.h,
              'pane2_bars': [(p2.X(x - .25), p2.X(x + .25)) for x in CENTRES], 'pane2_y0': p2.y0}
    return c, checks


def check_canvas(c):
    """No text off the canvas and no two labels overlapping."""
    problems = []
    for (x0, y0, x1, y1, t) in c.labels:
        if x0 < 0 or y0 < 0 or x1 > c.w or y1 > c.h:
            problems.append(f'off canvas: {t!r}')
    L = c.labels
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            a, b = L[i], L[j]
            if a[0] < b[2] - 1 and b[0] < a[2] - 1 and a[1] < b[3] - 1 and b[1] < a[3] - 1:
                problems.append(f'overlap: {a[4]!r} / {b[4]!r}')
    return problems


def main():
    import cairosvg
    from PIL import Image
    os.makedirs(DROP, exist_ok=True)
    report = {}
    for name, fn in [('the-area-under-the-bell-the-form', fig_form),
                     ('the-area-under-the-bell-the-mechanism', fig_mechanism),
                     ('the-area-under-the-bell-deep-dive-sheet', fig_sheet)]:
        c, checks = fn()
        svg = c.svg()
        import xml.dom.minidom
        xml.dom.minidom.parseString(svg)
        sp = os.path.join(DROP, name + '.svg'); pp = os.path.join(DROP, name + '.png')
        open(sp, 'w').write(svg)
        cairosvg.svg2png(bytestring=svg.encode(), write_to=pp, scale=SCALE)
        if '--save' in sys.argv:
            Image.open(pp).convert('RGB').save(os.path.join(ASSETS, name + '.webp'), 'WEBP', quality=90)
        checks['problems'] = check_canvas(c)
        checks['labels'] = [l[4] for l in c.labels]
        report[name] = checks
    json.dump(report, open(os.path.join(DROP, 'checks.json'), 'w'), indent=1, default=str)
    for k, v in report.items():
        print(k, 'problems:', v['problems'])


if __name__ == '__main__':
    main()
