# Bootstrap Cohen's kappa for judge A on 20 products. Judge outcomes are INVENTED.
import random
from math import sqrt

# (reviewer verdict, judge verdict), 1 = pass.  TP=16, FN=1, FP=2, TN=1
products = [(1, 1)] * 16 + [(1, 0)] * 1 + [(0, 1)] * 2 + [(0, 0)] * 1
assert len(products) == 20


def kappa(sample, show=False):
    n = len(sample)
    tp = sum(1 for g, v in sample if g == 1 and v == 1)
    fn = sum(1 for g, v in sample if g == 1 and v == 0)
    fp = sum(1 for g, v in sample if g == 0 and v == 1)
    tn = sum(1 for g, v in sample if g == 0 and v == 0)
    a, b = (tp + fn) / n, (tp + fp) / n      # reviewer pass rate, judge pass rate
    if a in (0, 1) or b in (0, 1):
        if show:
            print(f"     TP={tp} FN={fn} FP={fp} TN={tn}: a column never changes, kappa undefined")
        return None
    po = (tp + tn) / n
    pe = a * b + (1 - a) * (1 - b)
    k = (po - pe) / (1 - pe)
    if show:
        print(f"     TP={tp} FN={fn} FP={fp} TN={tn}: po={po:.4f} a={a:.4f} b={b:.4f} pe={pe:.4f} kappa={k:.4f}")
    return k


print(f"kappa on the 20 products: {kappa(products, True):.4f}")
rnd = random.Random(11)
print("first three resamples of the 20 products:")
for r in range(1, 4):
    idx = [rnd.randrange(20) for _ in range(20)]
    print(f"  resample {r}: product numbers {sorted(i + 1 for i in idx)}")
    kappa([products[i] for i in idx], True)

rnd = random.Random(11)
K = 10000
ks, undefined = [], 0
for _ in range(K):
    k = kappa([products[rnd.randrange(20)] for _ in range(20)])
    if k is None:
        undefined += 1
    else:
        ks.append(k)
ks.sort()
m = sum(ks) / len(ks)
sd = sqrt(sum((v - m) ** 2 for v in ks) / len(ks))
print(f"{K} resamples: {len(ks)} usable, {undefined} undefined (dropped)")
print(f"mean of resampled kappas {m:.3f}, standard deviation (bootstrap standard error) {sd:.3f}")
print(f"5th percentile {ks[int(.05 * len(ks))]:.3f}, median {ks[len(ks) // 2]:.3f}, "
      f"95th percentile {ks[int(.95 * len(ks)) - 1]:.3f}")
print(f"share of usable resamples at or below 0: {sum(1 for v in ks if v <= 0) / len(ks):.3f}")
