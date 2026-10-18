# Resample rows against whole products, when rows come in groups.  Verdicts are INVENTED.
# 105 rows = 8 products: each a good page (reviewer pass) plus its planted bad copies (reviewer fail).
import random
from math import sqrt

copies = [14] * 3 + [11] * 5                    # 3 x 14 + 5 x 11 = 97 copies
rows = []                                       # (product, reviewer verdict)
for i, c in enumerate(copies):
    rows.append((i, 1))
    rows += [(i, 0)] * c
assert len(rows) == 105


def kappa(sample):
    tp = sum(1 for _, g, v in sample if g == 1 and v == 1)
    fn = sum(1 for _, g, v in sample if g == 1 and v == 0)
    fp = sum(1 for _, g, v in sample if g == 0 and v == 1)
    tn = sum(1 for _, g, v in sample if g == 0 and v == 0)
    n = tp + fn + fp + tn
    a, b = (tp + fn) / n, (tp + fp) / n
    if a in (0, 1) or b in (0, 1):
        return None
    po = (tp + tn) / n
    pe = a * b + (1 - a) * (1 - b)
    return (po - pe) / (1 - pe)


def independent(seed):
    """The note's calibrated judge: every row's verdict is its own draw."""
    rnd = random.Random(seed)
    out = []
    for p, g in rows:
        c = 0.5 + 0.5 * rnd.random() ** 0.5
        out.append((p, g, g if rnd.random() < c else 1 - g))
    return out


def shared(seed, p_right=0.85):
    """Copies of one product share their fate: one draw per product decides all its copies."""
    rnd = random.Random(seed)
    fate = {}
    out = []
    for p, g in rows:
        if g == 1:
            right = rnd.random() < p_right
        else:
            if p not in fate:
                fate[p] = rnd.random() < p_right
            right = fate[p]
        out.append((p, g, g if right else 1 - g))
    return out


def ranges(data, K, seed):
    rnd = random.Random(seed)
    by = {i: [d for d in data if d[0] == i] for i in range(8)}
    res = {}
    for mode in ("rows", "products"):
        ks = []
        for _ in range(K):
            if mode == "rows":
                s = [rnd.choice(data) for _ in data]
            else:
                s = [d for i in [rnd.randrange(8) for _ in range(8)] for d in by[i]]
            k = kappa(s)
            if k is not None:
                ks.append(k)
        ks.sort()
        m = sum(ks) / len(ks)
        sd = sqrt(sum((x - m) ** 2 for x in ks) / len(ks))
        res[mode] = (ks[int(.05 * len(ks))], ks[int(.95 * len(ks)) - 1], sd)
    return res


print("A. verdicts drawn row by row (the case in How Sure Kappa Is), seed 1, 5000 resamples")
d = independent(1)
print(f"   kappa {kappa(d):.3f}")
for mode, (lo, hi, sd) in ranges(d, 5000, 7).items():
    print(f"   resample {mode:8s}: 90% range {lo:.2f} to {hi:.2f}, width {hi - lo:.2f}, sd {sd:.3f}")

print("B. copies of a product share their fate (one draw per product decides all its copies), seed 3")
d = shared(3)
print(f"   kappa {kappa(d):.3f}")
for mode, (lo, hi, sd) in ranges(d, 5000, 7).items():
    print(f"   resample {mode:8s}: 90% range {lo:.2f} to {hi:.2f}, width {hi - lo:.2f}, sd {sd:.3f}")

print("C. both cases over 30 different data seeds (1000 resamples each)")
for name, fn in (("independent", independent), ("shared", shared)):
    narrower, used, sr, sp = 0, 0, 0.0, 0.0
    for seed in range(1, 31):
        data = fn(seed)
        if kappa(data) is None:
            continue
        r = ranges(data, 1000, 7)
        used += 1
        sr += r["rows"][2]
        sp += r["products"][2]
        if r["rows"][2] < r["products"][2]:
            narrower += 1
    print(f"   {name:11s}: mean sd rows {sr / used:.3f}, mean sd products {sp / used:.3f}, "
          f"rows gave the smaller sd in {narrower} of {used} data sets")
