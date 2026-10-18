# How sure is kappa on the 105-row design? Confidences and verdicts are INVENTED (seeded).
# Resample rows one at a time, then resample whole products (a good page with its planted copies).
import random
from math import sqrt

products = [14] * 3 + [11] * 5  # planted copies per product: 3 x 14 + 5 x 11 = 97
rows = []
for i, nbad in enumerate(products):
    rows.append((i, 1))
    rows += [(i, 0)] * nbad
assert len(rows) == 105


def make(sharp, seed=1):
    """Row = (product, reviewer verdict, judge verdict). The judge is right with
    probability 1 - (1 - c) * sharp, where c is its confidence."""
    rnd = random.Random(seed)
    data = []
    for p, g in rows:
        c = 0.5 + 0.5 * rnd.random() ** 0.5
        right = rnd.random() < 1 - (1 - c) * sharp
        data.append((p, g, g if right else 1 - g))
    return data


def kappa(sample):
    tp = sum(1 for _, g, v in sample if g == 1 and v == 1)
    fn = sum(1 for _, g, v in sample if g == 1 and v == 0)
    fp = sum(1 for _, g, v in sample if g == 0 and v == 1)
    tn = sum(1 for _, g, v in sample if g == 0 and v == 0)
    n = tp + fn + fp + tn
    a, b = (tp + fn) / n, (tp + fp) / n
    if a in (0, 1) or b in (0, 1):
        return None  # a column that never changes leaves kappa undefined
    po = (tp + tn) / n
    pe = a * b + (1 - a) * (1 - b)
    return (po - pe) / (1 - pe)


for name, sharp in {"calibrated": 1.0, "underconfident": 0.2}.items():
    data = make(sharp)
    agree = sum(1 for _, g, v in data if g == v)
    print(f"{name}: agrees on {agree} of 105, kappa {kappa(data):.3f}")
    rnd = random.Random(7)
    by = {i: [d for d in data if d[0] == i] for i in range(8)}
    for mode in ("rows", "products"):
        ks = []
        for _ in range(5000):
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
        print(f"  resample {mode:8s}: {len(ks)} usable of 5000, "
              f"90% range {ks[int(.05 * len(ks))]:.2f} to {ks[int(.95 * len(ks)) - 1]:.2f}, sd {sd:.3f}")
