# Compare two kappas by resampling.  Judge outcomes are INVENTED.
import random
from math import sqrt

# Part 1: judge A (16,1,2,1) against judge B (17,0,2,1) on the SAME 20 products.
# Each product: (reviewer, judge A, judge B), 1 = pass.  B differs from A on one product only.
prods = ([(1, 1, 1)] * 16      # both judges pass a good product
         + [(1, 0, 1)]         # A wrongly fails it, B passes it
         + [(0, 1, 1)] * 2     # both wrongly pass a bad product
         + [(0, 0, 0)])        # both correctly fail the bad product
assert len(prods) == 20


def kappa(pairs):
    n = len(pairs)
    tp = sum(1 for g, v in pairs if g == 1 and v == 1)
    fn = sum(1 for g, v in pairs if g == 1 and v == 0)
    fp = sum(1 for g, v in pairs if g == 0 and v == 1)
    tn = sum(1 for g, v in pairs if g == 0 and v == 0)
    a, b = (tp + fn) / n, (tp + fp) / n
    if a in (0, 1) or b in (0, 1):
        return None
    po = (tp + tn) / n
    pe = a * b + (1 - a) * (1 - b)
    return (po - pe) / (1 - pe)


def pct(sorted_values, lo=.05, hi=.95):
    n = len(sorted_values)
    return sorted_values[int(lo * n)], sorted_values[int(hi * n) - 1]


kA = kappa([(g, a) for g, a, b in prods])
kB = kappa([(g, b) for g, a, b in prods])
print(f"point values: kappa A {kA:.4f}, kappa B {kB:.4f}, difference {kB - kA:.4f}")

def table(pairs):
    return (sum(1 for g, v in pairs if g == 1 and v == 1), sum(1 for g, v in pairs if g == 1 and v == 0),
            sum(1 for g, v in pairs if g == 0 and v == 1), sum(1 for g, v in pairs if g == 0 and v == 0))


rnd = random.Random(5)
K = 10000
A, B, D, undefined = [], [], [], 0
for r in range(K):
    idx = [rnd.randrange(20) for _ in range(20)]
    s = [prods[i] for i in idx]                            # ONE resample of products, scored by both judges
    if r < 3:
        pa, pb = [(g, a) for g, a, b in s], [(g, b) for g, a, b in s]
        ka, kb = kappa(pa), kappa(pb)
        print(f"resample {r + 1}: product 17 drawn {idx.count(16)} times; "
              f"A table {table(pa)} kappa {ka if ka is None else round(ka, 4)}; "
              f"B table {table(pb)} kappa {kb if kb is None else round(kb, 4)}")
    ka, kb = kappa([(g, a) for g, a, b in s]), kappa([(g, b) for g, a, b in s])
    if ka is None or kb is None:
        undefined += 1
        continue
    A.append(ka); B.append(kb); D.append(kb - ka)
for name, v in (("kappa A", A), ("kappa B", B), ("B minus A (paired)", D)):
    v = sorted(v)
    lo, hi = pct(v)
    print(f"  {name:19s}: {len(v)} usable of {K}, 90% range {lo:.3f} to {hi:.3f}")
print(f"  share of paired resamples with B minus A at or below 0: {sum(1 for d in D if d <= 0) / len(D):.3f}")
print(f"  share of paired resamples with B minus A exactly 0: {sum(1 for d in D if d == 0) / len(D):.3f}")
print(f"  share of resamples that left out the one product where A and B differ: {(19 / 20) ** 20:.3f}")

# Part 2: the 105-row design from How Sure Kappa Is (same generator, seed 1), resampling whole products.
copies = [14] * 3 + [11] * 5
rows = []
for i, c in enumerate(copies):
    rows.append((i, 1))
    rows += [(i, 0)] * c


def make(sharp, seed=1):
    r = random.Random(seed)
    out = []
    for p, g in rows:
        c = 0.5 + 0.5 * r.random() ** 0.5
        right = r.random() < 1 - (1 - c) * sharp
        out.append((p, g, g if right else 1 - g))
    return out


cal, und = make(1.0), make(0.2)
print()
print("105 rows, the same rows scored by both invented judges, whole products resampled")
k1 = kappa([(g, v) for p, g, v in cal])
k2 = kappa([(g, v) for p, g, v in und])
print(f"point values: calibrated {k1:.3f}, underconfident {k2:.3f}, difference {k2 - k1:.3f}")
by = {i: [(cal[j][1], cal[j][2], und[j][2]) for j in range(105) if cal[j][0] == i] for i in range(8)}
rnd = random.Random(7)
A, B, D = [], [], []
for _ in range(5000):
    s = [t for i in [rnd.randrange(8) for _ in range(8)] for t in by[i]]
    ka, kb = kappa([(g, a) for g, a, b in s]), kappa([(g, b) for g, a, b in s])
    if ka is None or kb is None:
        continue
    A.append(ka); B.append(kb); D.append(kb - ka)
for name, v in (("calibrated", A), ("underconfident", B), ("difference (paired)", D)):
    v = sorted(v)
    lo, hi = pct(v)
    print(f"  {name:19s}: {len(v)} usable of 5000, 90% range {lo:.3f} to {hi:.3f}")
print(f"  share of paired resamples with the difference at or below 0: {sum(1 for d in D if d <= 0) / len(D):.4f}")
