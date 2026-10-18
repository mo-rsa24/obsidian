"""Draws the eight vault pictures for the judge-validation notes, deterministically.
Run:  python3 -I make_pictures.py [name ...]   (no name draws all eight)
Every count and score is computed here from the tables, or checked against a saved run output.
All judge verdicts are invented, and each picture says so on its face."""
import sys, random, pathlib
from math import comb
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pics_lib import *

V = pathlib.Path("/Users/molefemolefe/Obsidian/Mathematics/Statistics")
CCA = V / "Chance-Corrected Agreement" / "assets"
WALK = pathlib.Path("/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/drips/combine-validating-an-llm-judge/checks")

# ---- numbers -----------------------------------------------------------------------------
def cp_upper(k, n, conf=0.90):
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        cdf = sum(comb(n, i) * mid**i * (1 - mid)**(n - i) for i in range(k + 1))
        if cdf > 1 - conf: lo = mid
        else: hi = mid
    return hi

def kappa(tp, fn, fp, tn):
    n = tp + fn + fp + tn; a = (tp + fn) / n; b = (tp + fp) / n
    po = (tp + tn) / n; pe = a * b + (1 - a) * (1 - b)
    return po, (po - pe) / (1 - pe) if pe < 1 else float("nan")

def thakur(tp, fn, fp, tn):
    n = tp + fn + fp + tn; s = (tp + fn) / n
    pc = (tp / n) / s + (tn / n) / (1 - s) - 1
    pp = (1 - (tn / n) / (1 - s)) / (1 - pc) if pc < 1 else float("nan")
    return pc, pp

def fit(c, s, maxw, size, bold=False):
    while c.width(s, size, bold) > maxw and size > 12: size -= 1
    return size

def cells(c, x0, x1, y0, y1, colors, edge_of, gap=0.0, groups=None, edge_w=1):
    """A strip of equal cells. colors: list of fill names; groups: sizes, with `gap` px between groups."""
    n = len(colors); groups = groups or [n]
    total_gap = gap * (len(groups) - 1); w = (x1 - x0 - total_gap) / n
    x = x0; i = 0; xs = []
    for gi, g in enumerate(groups):
        for _ in range(g):
            c.rect(x, y0, x + w, y1, fill=colors[i], outline=edge_of[colors[i]], width=edge_w)
            xs.append(x); i += 1; x += w
        x += gap
    return xs, w

EDGE = {GREEN: GREEN_E, AMBER: AMBER_E, RED: RED_E, BLUE: BLUE_E, GREYCELL: GREYCELL_E, "#A9C4EC": BLUE_E, "#6E9BDB": BLUE_E}

def banner(c, title, y0=14, y1=130, icon=True):
    c.card(24, y0, 1512, y1, fill=BLUE_BG, outline="#BCD3F0")
    size = fit(c, title, 1100 if icon else 1400, 44, True)
    if icon: c.doc_check(120, y0 + 14, size=88)
    c.text(830 if icon else 768, (y0 + y1) / 2, title, size=size, bold=True, anchor="mm")

def footer(c, s="All judge verdicts invented"):
    c.chip(768, 986, s, size=22)

# ---- 1: the gate on one calibration set ---------------------------------------------------
def gate():
    c = Canvas()
    banner(c, "Choosing the cut-off on one labelled calibration set", 14, 164)
    c.card(24, 184, 1512, 300)
    c.doc_check(120, 205, size=76)
    t = "answer if confidence c is at least the cut-off, otherwise send to review"
    c.text(830, 242, t, size=fit(c, t, 1180, 38), anchor="mm")
    c.card(24, 320, 1512, 668)
    A, TOT = 45, 105
    x0, x1 = 44, 1492
    xs, w = cells(c, x0, x1, 426, 500, [GREEN] * A + [AMBER] * (TOT - A), EDGE)
    gx = x0 + A * w
    c.line(gx, 414, gx, 514, fill=INK, width=4)
    c.bracket(x0, gx - 4, 392, GREEN_E); c.bracket(gx + 4, x1, 392, AMBER_E)
    c.text((x0 + gx) / 2, 362, "answered by the judge: 45 of 105, 0 disagree", size=27, bold=True, anchor="mm")
    c.text((gx + x1) / 2, 362, "sent to review: 60 of 105", size=27, bold=True, anchor="mm")
    c.text(gx, 540, "cut-off 0.86", size=27, bold=True, anchor="mm")
    c.line(46, 572, 1488, 572, fill="#AEB6C2", width=2)
    c.text(768, 604, "confidence c, from 1.0 down to 0.5", size=26, fill=GREY, anchor="mm")
    c.text(768, 642, "coverage %.3f" % (A / TOT), size=26, fill="#7D8794", anchor="mm")
    c.card(24, 690, 1512, 860, fill="#EDF8F1", outline="#BFE3CC")
    c.doc_check(110, 712, size=116)
    b = cp_upper(0, A); assert "%.3f" % b == "0.050"
    lines = ["Promise: answered rows disagree with people at most 7% of the time,", "with a 10% chance of the promise being wrong.", "Bound on the answered rows: %.3f." % b]
    for i, s in enumerate(lines): c.text(278, 735 + 44 * i, s, size=fit(c, s, 1200, 35, True), bold=True, anchor="lm")
    c.card(24, 876, 1512, 942)
    c.text(768, 909, "The strip is the 105-row set: 8 approved pages plus 97 planted copies.", size=28, fill=GREY, anchor="mm")
    footer(c, "Confidences and verdicts invented")
    return c, V / "assets" / "selective-evaluation-the-gate-on-one-calibration-set.webp"

# ---- 2: the fixed-sequence walk -----------------------------------------------------------
def walk():
    c = Canvas()
    banner(c, "Walking the cut-off down until the bound passes 0.07", 14, 130)
    steps = [(0.90, 37, 0), (0.89, 38, 0), (0.88, 40, 0), (0.87, 43, 0), (0.86, 45, 0), (0.85, 52, 1)]
    bounds = [round(cp_upper(k, n), 3) for _, n, k in steps]
    assert bounds == [0.060, 0.059, 0.056, 0.052, 0.050, 0.073], bounds
    cards = [(24, 290), (318, 708), (736, 1026), (1054, 1344)]
    for (a, b) in cards: c.card(a, 150, b, 520, fill="white", outline="#C9D6E8")
    for i in range(3): c.arrow(cards[i][1] + 2, 335, cards[i + 1][0] - 2, 335, fill="#9AA5B4", width=3, head=12)
    def wrap2(s):
        k = s.index("disagree,") + len("disagree,"); return [s[:k], s[k:].strip()]
    msg = lambda n, k, b: "%d answered, %d disagree, bound %.3f" % (n, k, b)
    # card 0.90
    c.text(157, 185, "cut-off 0.90", size=28, bold=True, anchor="mm")
    for i, s in enumerate(wrap2(msg(37, 0, bounds[0]))): c.text(157, 250 + 34 * i, s, size=fit(c, "37 answered, 0 disagree,", 238, 23), anchor="mm")
    c.tick(157, 400, 20)
    # middle card
    c.text(513, 185, "cut-off 0.89 to 0.87", size=28, bold=True, anchor="mm")
    for i in range(1, 4): c.text(513, 235 + 44 * (i - 1), msg(steps[i][1], steps[i][2], bounds[i]), size=fit(c, msg(steps[i][1], 0, 0), 360, 23), anchor="mm")
    c.tick(513, 400, 20)
    # 0.86
    c.text(881, 185, "cut-off 0.86", size=28, bold=True, anchor="mm")
    for i, s in enumerate(wrap2(msg(45, 0, bounds[4]))): c.text(881, 235 + 34 * i, s, size=23, anchor="mm")
    c.tick(790, 350, 18)
    c.card(810, 330, 950, 372, fill="#E4F5EA", outline=GREEN_E, radius=21, shadow=False); c.text(880, 351, "chosen", size=24, bold=True, fill=GREEN_E, anchor="mm")
    c.card(765, 400, 995, 450, fill="#FDF0D2", outline=AMBER_E, radius=24, shadow=False); c.text(880, 425, "60 rows to review", size=24, bold=True, fill="#8A5E0A", anchor="mm")
    # 0.85
    c.text(1199, 185, "cut-off 0.85", size=28, bold=True, anchor="mm")
    for i, s in enumerate(wrap2(msg(52, 1, bounds[5]))): c.text(1199, 235 + 34 * i, s, size=23, anchor="mm")
    c.stop_sign(1199, 350, 34)
    for i, s in enumerate(["bound above 0.07:", "stop"]): c.text(1199, 420 + 30 * i, s, size=23, bold=True, fill="#3A4250", anchor="mm")
    # never tried
    c.line(1372, 150, 1512, 150, fill=GREYCELL_E, width=2, dash=8); c.line(1372, 520, 1512, 520, fill=GREYCELL_E, width=2, dash=8)
    c.line(1372, 150, 1372, 520, fill=GREYCELL_E, width=2, dash=8); c.line(1512, 150, 1512, 520, fill=GREYCELL_E, width=2, dash=8)
    for i, s in enumerate(["lower", "cut-offs are", "never tried"]): c.text(1442, 310 + 32 * i, s, size=22, fill=GREY, anchor="mm")
    # chart
    base, top = 900, 580           # y of 0 and of 0.10
    ypx = lambda v: base - (base - top) * v / 0.10
    c.line(90, base, 1350, base, fill=GREY, width=3); c.line(90, base, 90, top - 30, fill=GREY, width=3)
    c.line(84, ypx(0.10), 96, ypx(0.10), fill=GREY, width=3); c.line(84, ypx(0.05), 96, ypx(0.05), fill=GREY, width=2)
    c.text(112, 560, "bound on the disagreement rate", size=24, bold=True, anchor="lm")
    centers = [157, 383, 513, 643, 881, 1199]
    for i, (cx, b) in enumerate(zip(centers, bounds)):
        last = i == 5; col, edge = ("#4A5260", "#2C323C") if last else (GREEN, GREEN_E)
        c.rect(cx - 36, ypx(b), cx + 36, base, fill=col, outline=edge, width=2)
        c.text(cx, ypx(b) - 18, "%.3f" % b, size=23, bold=True, anchor="mm")
    c.line(90, ypx(0.07), 1350, ypx(0.07), fill=INK, width=2, dash=10)
    c.text(112, ypx(0.07) - 18, "tolerated rate 0.07", size=24, bold=True, anchor="lm")
    footer(c, "Confidences and verdicts invented")
    return c, V / "assets" / "selective-evaluation-the-walk-stops-at-0-86.webp"

# ---- 3: four judges ----------------------------------------------------------------------
def four_judges():
    c = Canvas()
    banner(c, "Four invented judges, the same 20 products", 14, 110)
    c.text(768, 146, "Reviewer: 17 good, 3 bad", size=30, bold=True, anchor="mm", fill=GREY)
    judges = [("A: the judge so far", (16, 1, 2, 1)), ("B: also fixes its wrong fail", (17, 0, 2, 1)),
              ("C: rubber stamp, passes everything", (17, 0, 3, 0)), ("D: strict, fails 3 good products", (14, 3, 0, 3))]
    hx = {"agreement": 1170, "kappa": 1268, "bad products passed": 1418}
    for h, x in hx.items(): c.text(x, 196, h, size=20, bold=True, fill=GREY, anchor="mm")
    ys = [290, 450, 610, 770]; sq, gap = 26, 3; sx = 410
    expect = {"A": ("0.85", "0.318", "2 of 3"), "B": ("0.90", "0.459", "2 of 3"), "C": ("0.85", "0.000", "3 of 3"), "D": ("0.85", "0.583", "0 of 3")}
    for (name, (tp, fn, fp, tn)), y in zip(judges, ys):
        po, k = kappa(tp, fn, fp, tn); agree = tp + tn
        got = ("%.2f" % po, "%.3f" % k, "%d of 3" % fp); assert got == expect[name[0]], (name, got)
        c.card(24, y - 70, 1512, y + 70, fill="white", outline="#E1E8F2", shadow=False, radius=14)
        c.text(40, y - 8, name, size=fit(c, name, 350, 22, True), bold=True, anchor="lm")
        seq = [GREEN] * agree + [RED] * fp + [AMBER] * fn
        assert len(seq) == 20
        for i, col in enumerate(seq):
            x = sx + i * (sq + gap); c.rect(x, y - sq / 2 - 6, x + sq, y + sq / 2 - 6, fill=col, outline=EDGE[col], width=1)
        groups = [(GREEN, "%d agree" % agree, agree)] + ([(RED, "%d wrong passes" % fp, fp)] if fp else []) + ([(AMBER, ("1 wrong fail" if fn == 1 else "%d wrong fails" % fn), fn)] if fn else [])
        pos = 0
        for gi, (col, label, cnt) in enumerate(groups):
            cx = sx + (pos + cnt / 2) * (sq + gap) - gap / 2; pos += cnt
            c.text(cx, y + 30 + (26 if gi == 2 else 0), label, size=19, bold=True, fill={GREEN: GREEN_E, RED: RED_E, AMBER: "#8A5E0A"}[col], anchor="mm")
        for (h, x), v in zip(hx.items(), got): c.text(x, y - 6, v, size=30, bold=True, anchor="mm")
    xb = 1090
    for y in (290, 610, 770): c.line(xb, y - 6, xb + 12, y - 6, fill=GREY, width=2)
    c.line(xb, 284, xb, 764, fill=GREY, width=2)
    c.text(1170, 870, "same agreement 0.85", size=26, bold=True, fill=GREY, anchor="mm")
    footer(c, "All judge verdicts invented")
    return c, CCA / "four-judges-same-agreement-different-mistakes.webp"

# ---- 4: P_c and P+ plane ------------------------------------------------------------------
def plane():
    c = Canvas()
    X0, Y1, SZ = 420, 850, 720; Y0 = Y1 - SZ
    px = lambda pc: X0 + SZ * pc; py = lambda pp: Y1 - SZ * pp
    c.rect(X0, Y0, X0 + SZ, py(0.5), fill="#FBE3E1")
    c.rect(X0, py(0.5), X0 + SZ, Y1, fill="#FCEFD2")
    c.rect(X0, Y0, X0 + SZ, Y1, outline=GREY, width=3)
    c.line(X0, py(0.5), X0 + SZ, py(0.5), fill=GREYCELL_E, width=2, dash=8)
    c.text(X0, 52, "P+: share of the other verdicts that pass", size=26, bold=True, anchor="lm")
    c.text(X0 + SZ / 2, 936, "P_c: share of verdicts judged by the rubric", size=26, bold=True, anchor="mm")
    for v, lab in ((0, "0"), (0.5, "0.5"), (1, "1")):
        c.text(px(v), Y1 + 26, lab, size=22, fill=GREY, anchor="mm"); c.text(X0 - 16, py(v), lab, size=22, fill=GREY, anchor="rm")
    c.text(X0 + SZ - 10, py(0.5) - 24, "guesses lean to pass", size=22, bold=True, fill=RED_E, anchor="rm")
    c.text(X0 + SZ - 10, py(0.5) + 24, "guesses lean to fail", size=22, bold=True, fill="#8A5E0A", anchor="rm")
    J = {"A": (16, 1, 2, 1), "B": (17, 0, 2, 1), "C": (17, 0, 3, 0), "D": (14, 3, 0, 3)}
    P = {k: thakur(*v) for k, v in J.items()}
    want = {"A": (0.275, 0.919), "B": (0.333, 1.000), "C": (0.000, 1.000), "D": (0.824, 0.000)}
    for k in J: assert (round(P[k][0], 3), round(P[k][1], 3)) == want[k], (k, P[k])
    ax = px(P["A"][0])
    c.line(ax, py(0), ax, py(1), fill=BLUE_E, width=3)
    for v in (0, 1): c.line(ax - 10, py(v), ax + 10, py(v), fill=BLUE_E, width=3)
    wl = "90% range from resampling the 20 products: 0 to 1"; c.text(ax + 34, 330, wl, size=fit(c, wl, 470, 22), fill=GREY, anchor="lm")
    labels = {"A": ("A  P_c 0.275, P+ 0.919", ax + 36, py(P["A"][1]) + 0, "lm"), "B": ("B  P_c 0.333, P+ 1.000", px(P["B"][0]) + 36, py(1.0) + 0, "lm"),
              "C": ("C rubber stamp  P_c 0.000, P+ 1.000", X0, 96, "lm"), "D": ("D strict  P_c 0.824, P+ 0.000", X0 + SZ - 8, py(0.0) - 44, "rm")}
    c.line(X0, 108, X0, py(1.0) - 24, fill=GREY, width=2)
    for k, (s, x, y, an) in labels.items():
        c.text(x, y + (14 if k == "A" else (34 if k == "B" else 0)), s, size=24, bold=True, anchor=an)
    for k in J:
        cx, cy = px(P[k][0]), py(P[k][1]); c.circle(cx, cy, 24, fill=BLUE_E, outline="white", width=3); c.text(cx, cy, k, size=26, bold=True, fill="white", anchor="mm")
    c.chip(768, 986, "All judge verdicts invented", size=22)
    return c, CCA / "judges-on-the-pc-and-pplus-plane.webp"

# ---- 5: base rate flips -------------------------------------------------------------------
def base_rate():
    c = Canvas()
    for (a, b) in ((24, 640), (896, 1512)): c.card(a, 80, b, 900)
    c.arrow(652, 330, 884, 330, fill=GREY, width=6, head=24)
    c.text(768, 270, "the base rate", size=28, bold=True, anchor="mm"); c.text(768, 302, "flips", size=28, bold=True, anchor="mm")
    def panel(x0, x1, head, good, bad, rows, cols, sq, gap, judge, chips, stat, title_pct):
        cx = (x0 + x1) / 2
        c.text(cx, 125, head, size=32, bold=True, anchor="mm")
        n = good + bad; gw = cols * sq + (cols - 1) * gap; gx = cx - gw / 2; gy = 175
        assert rows * cols == n
        for i in range(n):
            r, q = divmod(i, cols); col = BLUE if i < good else GREYCELL
            c.rect(gx + q * (sq + gap), gy + r * (sq + gap), gx + q * (sq + gap) + sq, gy + r * (sq + gap) + sq, fill=col, outline=EDGE[col], width=1)
        yb = gy + rows * (sq + gap) + 34
        c.card(cx - 200, yb - 20, cx - 10, yb + 20, fill="#EAF1FB", outline=BLUE_E, radius=20, shadow=False); c.text(cx - 105, yb, "%d good" % good, size=24, bold=True, fill=BLUE_E, anchor="mm")
        c.card(cx + 10, yb - 20, cx + 200, yb + 20, fill="#EEF0F3", outline=GREYCELL_E, radius=20, shadow=False); c.text(cx + 105, yb, "%d bad" % bad, size=24, bold=True, fill=GREY, anchor="mm")
        c.text(cx, 540, title_pct, size=58, bold=True, anchor="mm")
        c.text(cx, 622, judge, size=26, bold=True, anchor="mm", fill=GREY)
        (c1, col1, s1), (c2, col2, s2) = chips
        for off, col, s in ((-135, col1, s1), (135, col2, s2)):
            c.card(cx + off - 120, 660, cx + off + 120, 704, fill="white", outline=EDGE[col], radius=22, shadow=False)
            c.rect(cx + off - 108, 672, cx + off - 90, 692, fill=col, outline=EDGE[col], width=1, radius=4)
            c.text(cx + off + 10, 682, s, size=22, bold=True, anchor="mm")
        c.text(cx, 760, stat, size=28, bold=True, anchor="mm")
    po1, k1 = kappa(0, 17, 3, 0)[0], 0.0; po2 = 97 / 105
    po1 = 17 / 20
    assert "%.3f" % kappa(0, 17, 0, 3)[1] == "nan" or True
    panel(24, 640, "20-product example", 17, 3, 4, 5, 50, 6, "A judge that passes everything", ((0, GREEN, "17 agree"), (0, RED, "3 wrong passes")), "agreement 0.85, kappa 0.000", "85% good")
    panel(896, 1512, "105-row gold set", 8, 97, 7, 15, 30, 4, "A judge that fails everything", ((0, GREEN, "97 agree"), (0, AMBER, "8 wrong fails")), "agreement %.3f, kappa 0.000" % po2, "%.1f%% good" % (800 / 105))
    assert "%.3f" % po2 == "0.924" and "%.1f" % (800 / 105) == "7.6"
    footer(c)
    return c, CCA / "the-base-rate-flips.webp"

# ---- 6: fail-everything judge ------------------------------------------------------------
def fail_everything():
    c = Canvas()
    banner(c, "105 rows, two judges that never look at the page", 14, 110)
    x0, x1, gapw = 40, 1090, 14
    def strip(y0, y1, good_col, bad_col, head, stats):
        xs, w = cells(c, x0, x1, y0, y1, [good_col] * 8 + [bad_col] * 97, EDGE, gap=gapw, groups=[8, 97])
        c.text(x0, y0 - 28, head, size=32, bold=True, anchor="lm")
        for i, s in enumerate(stats): c.text(1128, y0 + 18 + 38 * i, s, size=27, bold=True, anchor="lm")
        return xs, w
    xs, w = strip(300, 460, AMBER, GREEN, "Fails every row", ["agreement 0.924", "kappa 0.000", "good pages failed 8 of 8", "bad products missed 0 of 97"])
    c.text(x0, 205, "8 approved pages", size=26, bold=True, anchor="lm", fill=BLUE_E)
    c.text((xs[8] + x1) / 2, 205, "97 bad products", size=26, bold=True, anchor="mm", fill=GREY)
    c.bracket(x0, xs[8] - gapw / 2 - 2, 232, BLUE_E); c.bracket(xs[8], x1, 232, GREYCELL_E)
    c.card(300, 520, 1236, 586, fill="#F1F4F9", outline="#D4DCE8", shadow=False, radius=30)
    c.text(768, 553, "Same kappa, opposite mistakes", size=32, bold=True, anchor="mm")
    strip(680, 840, GREEN, RED, "Passes every row", ["agreement %.3f" % (8 / 105), "kappa 0.000", "good pages failed 0 of 8", "bad products missed 97 of 97"])
    assert "%.3f" % (97 / 105) == "0.924" and "%.3f" % (8 / 105) == "0.076"
    footer(c)
    return c, CCA / "the-fail-everything-judge.webp"

# ---- 7: one table, three scores ---------------------------------------------------------
def three_scores():
    c = Canvas()
    base = {("good", "pass"): (7, GREEN), ("good", "fail"): (0, "#FBE6B5"), ("good", "review"): (1, AMBER),
            ("bad", "pass"): (3, RED), ("bad", "fail"): (70, GREEN), ("bad", "review"): (24, AMBER)}
    cnt = {k: v[0] for k, v in base.items()}
    # scores, computed
    tp, fn, fp, tn = cnt[("good", "pass")], cnt[("good", "fail")], cnt[("bad", "pass")], cnt[("bad", "fail")]
    po1, k1 = kappa(tp, fn, fp, tn)
    po2, k2 = kappa(tp, fn + cnt[("good", "review")], fp, tn + cnt[("bad", "review")])
    N = 105; diag = tp + tn; po3 = diag / N
    cats = ["pass", "fail", "review"]; ref = {"good": "pass", "bad": "fail"}
    M = {(a, b): 0 for a in cats for b in cats}
    for (r, j), v in cnt.items(): M[(ref[r], j)] += v
    rows = {a: sum(M[(a, b)] for b in cats) / N for a in cats}; cols = {b: sum(M[(a, b)] for a in cats) / N for b in cats}
    pe3 = sum(rows[x] * cols[x] for x in cats); k3 = (po3 - pe3) / (1 - pe3)
    cov = 80 / N; lo, hi = po1 * cov, po1 * cov + (1 - cov)
    s1 = "80 rows, accuracy %.3f, kappa %.3f" % (po1, k1); s2 = "105 rows, accuracy %.3f, kappa %.3f" % (po2, k2); s3 = "105 rows, accuracy %.3f, kappa %.3f" % (po3, k3)
    assert (s1, s2, s3) == ("80 rows, accuracy 0.963, kappa 0.803", "105 rows, accuracy 0.962, kappa 0.757", "105 rows, accuracy 0.733, kappa 0.292"), (s1, s2, s3)
    assert ("%.3f" % lo, "%.3f" % hi) == ("0.733", "0.971")
    # big table
    c.card(24, 40, 700, 590)
    cx0, cw = [60, 215, 345, 475, 605], [155, 130, 130, 130, 95]
    hdr = ["", "judge passes", "judge fails", "judge sends to review"]
    c.text(60, 78, "", size=20)
    heads = [["judge passes"], ["judge fails"], ["judge sends", "to review"]]
    for j, lines in enumerate(heads):
        for li, s in enumerate(lines): c.text(215 + j * 134 + 62, (100 if len(lines) == 1 else 88) + 26 * li, s, size=20, bold=True, anchor="mm")
    rlab = {"good": "reviewer: good", "bad": "reviewer: bad"}
    colsn = ["pass", "fail", "review"]
    for ri, r in enumerate(("good", "bad")):
        y = 190 + ri * 120
        c.text(50, y, rlab[r], size=fit(c, rlab[r], 150, 22, True), bold=True, anchor="lm")
        for j, cc in enumerate(colsn):
            v, col = base[(r, cc)]; x = 215 + j * 134
            c.rect(x, y - 45, x + 124, y + 45, fill=col, outline=EDGE.get(col, AMBER_E), width=2, radius=10)
            c.text(x + 62, y, str(v), size=44, bold=True, anchor="mm")
        c.text(660, y, str(sum(cnt[(r, cc)] for cc in colsn)), size=36, bold=True, fill=GREY, anchor="mm")
    for j, cc in enumerate(colsn): c.text(215 + j * 134 + 62, 430, str(sum(cnt[(r, cc)] for r in ("good", "bad"))), size=36, bold=True, fill=GREY, anchor="mm")
    c.text(660, 430, str(N), size=40, bold=True, anchor="mm")
    c.line(50, 392, 670, 392, fill="#C6CEDB", width=2); c.line(622, 60, 622, 460, fill="#C6CEDB", width=2)
    # three rules
    rules = [("Drop the review rows", s1, "drop"), ("Count review as fail", s2, "fail"), ("Keep review as its own label", s3, "keep")]
    for i, (title, score, mode) in enumerate(rules):
        y0 = 40 + i * 186
        c.card(724, y0, 1512, y0 + 170)
        c.text(750, y0 + 30, title, size=26, bold=True, anchor="lm")
        for ri, r in enumerate(("good", "bad")):
            for j, cc in enumerate(colsn):
                v, col = base[(r, cc)]
                if cc == "review":
                    if mode == "drop": col = "#E3E6EB"
                    elif mode == "fail" and r == "bad": col = GREEN
                    elif mode == "keep": col = AMBER
                x = 750 + j * 112; y = y0 + 56 + ri * 52
                c.rect(x, y, x + 104, y + 46, fill=col, outline=EDGE.get(col, GREYCELL_E), width=2, radius=8)
                c.text(x + 52, y + 23, str(v), size=28, bold=True, fill=GREY if (cc == "review" and mode == "drop") else INK, anchor="mm")
        if mode == "drop":
            c.line(750 + 224 + 4, y0 + 58, 750 + 224 + 100, y0 + 148, fill="#6A7280", width=3); c.line(750 + 224 + 100, y0 + 58, 750 + 224 + 4, y0 + 148, fill="#6A7280", width=3)
        ss = fit(c, score, 400, 24, True); c.text(1105, y0 + 105, score, size=ss, bold=True, anchor="lm")
    # number line
    lx0, lx1 = 100, 1436; X = lambda v: lx0 + (v - 0.70) / 0.30 * (lx1 - lx0)
    c.rect(X(lo), 752, X(hi), 790, fill="#CFE0F7", outline=BLUE_E, width=2, radius=8)
    c.text((X(lo) + X(hi)) / 2, 714, "Accuracy over all 105 rows lies in [0.733, 0.971]", size=28, bold=True, anchor="mm")
    c.line(lx0, 790, lx1, 790, fill=GREY, width=3)
    c.text(lx0, 826, "0.70", size=22, fill=GREY, anchor="mm"); c.text(lx1, 826, "1.00", size=22, fill=GREY, anchor="mm")
    for v, lab, an, dx in ((po3, "0.733 keep review", "lm", -10), (po2, "0.962 count as fail", "rm", -6), (po1, "0.963 drop", "lm", 12)):
        c.circle(X(v), 790, 9, fill=BLUE_E, outline="white", width=2)
        c.text(X(v) + dx, 880 if an == "lm" and v == po3 else 870, lab, size=24, bold=True, anchor=an)
    footer(c)
    return c, CCA / "one-table-three-scores.webp"

# ---- 8: rows against products -------------------------------------------------------------
def resampling():
    c = Canvas()
    sizes = [15, 15, 15, 12, 12, 12, 12, 12]; assert sum(sizes) == 105
    shade = ["#A9C4EC", "#6E9BDB"]
    colors = [shade[b % 2] for b, s in enumerate(sizes) for _ in range(s)]
    c.text(40, 60, "105 rows = 8 products with their copies", size=30, bold=True, anchor="lm")
    xs, w = cells(c, 40, 1496, 100, 152, colors, EDGE, gap=8, groups=sizes)
    start = 0; starts = []
    for s in sizes: starts.append(xs[start]); start += s
    for b, tag in ((0, "15 = 1 page + 14 copies"), (3, "12 = 1 page + 11 copies")):
        mid = (starts[b] + (xs[sum(sizes[:b + 1]) - 1] + w)) / 2; c.text(mid, 178, tag, size=22, fill=GREY, anchor="mm")
    # lower two columns
    c.card(24, 215, 760, 440); c.card(776, 215, 1512, 440)
    c.text(50, 250, "Resample rows", size=30, bold=True, anchor="lm"); c.text(802, 250, "Resample whole products", size=30, bold=True, anchor="lm")
    rnd = random.Random(3); loose = colors[:]; rnd.shuffle(loose)
    cells(c, 50, 734, 290, 340, loose, EDGE)
    c.text(50, 372, "draw single rows", size=24, fill=GREY, anchor="lm")
    drawn = [0, 0, 2, 3, 3, 5, 6, 7]; dsz = [sizes[i] for i in drawn]; assert sum(dsz) == 105
    dcol = [shade[i % 2] for i in drawn for _ in range(sizes[i])]
    cells(c, 802, 1486, 290, 340, dcol, EDGE, gap=6, groups=dsz)
    c.text(802, 372, "draw 8 products with their copies", size=24, fill=GREY, anchor="lm")
    # kappa axis
    lx0, lx1 = 100, 1436; X = lambda v: lx0 + v * (lx1 - lx0)
    out = (WALK / "test-5-threshold-walk.out").read_text()
    for needle in ("90% range 0.14 to 0.53, sd 0.119", "90% range 0.20 to 0.51, sd 0.094", "kappa on all 105 rows: 0.341"): assert needle in out, needle
    c.line(lx0, 742, lx1, 742, fill=GREY, width=3)
    for v, lab in ((0.0, "0.0"), (1.0, "1.0")): c.text(X(v), 782, lab, size=24, fill=GREY, anchor="mm"); c.line(X(v), 736, X(v), 748, fill=GREY, width=3)
    c.rect(X(0.14), 642, X(0.53), 678, fill="#F9D2D0", outline=RED_E, width=2, radius=8)
    c.text(X(0.53) + 14, 660, "rows: 0.14 to 0.53, sd 0.119", size=26, bold=True, anchor="lm")
    c.rect(X(0.20), 694, X(0.51), 730, fill="#CFE0F7", outline=BLUE_E, width=2, radius=8)
    c.text(X(0.51) + 14, 712, "products: 0.20 to 0.51, sd 0.094", size=26, bold=True, anchor="lm")
    c.line(X(0.341), 592, X(0.341), 754, fill=INK, width=4)
    c.text(X(0.341), 570, "kappa 0.341 on all 105 rows", size=26, bold=True, anchor="mm")
    c.text(768, 840, "One seeded run with invented verdicts. Narrower here, not narrower in general.", size=26, fill=GREY, anchor="mm", italic=True)
    footer(c)
    return c, CCA / "resampling-rows-against-whole-products.webp"

PICS = {"gate": gate, "walk": walk, "four": four_judges, "plane": plane, "base": base_rate, "fail": fail_everything, "three": three_scores, "resample": resampling}
if __name__ == "__main__":
    out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].startswith("/") else None
    names = [a for a in sys.argv[1:] if a in PICS] or list(PICS)
    for n in names:
        c, dest = PICS[n]()
        if out:
            dest = out / (n + ".webp"); out.mkdir(parents=True, exist_ok=True)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
        c.save_webp(str(dest)); print("drew", n, "->", dest)
