# The 105-row design: 8 approved pages (good) and 97 planted-defect copies (bad).
# Every judge outcome below is INVENTED. Cell order: (tp, fn, fp, tn), reviewer first.
from math import comb


def agreement(tp, fn, fp, tn):
    n = tp + fn + fp + tn
    a, b = (tp + fn) / n, (tp + fp) / n
    po = (tp + tn) / n
    pe = a * b + (1 - a) * (1 - b)
    kappa = (po - pe) / (1 - pe) if pe < 1 else float("nan")
    pool = (a + b) / 2
    pes = pool**2 + (1 - pool) ** 2
    pi = (po - pes) / (1 - pes)
    wrong_pass_of_passes = fp / (tp + fp) if tp + fp else float("nan")
    miss = fp / (fp + tn)  # share of bad products the judge passed
    false_fail = fn / (tp + fn)  # share of good pages the judge failed
    return po, kappa, pi, wrong_pass_of_passes, miss, false_fail


def thakur(tp, fn, fp, tn):
    n = tp + fn + fp + tn
    s = (tp + fn) / n
    pc = (tp / n) / s + (tn / n) / (1 - s) - 1
    return pc, (1 - (tn / n) / (1 - s)) / (1 - pc) if pc < 1 else float("nan")


def cp_upper(k, n, conf=0.90):
    """Exact one-sided upper bound on a rate after k events in n trials."""
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        cdf = sum(comb(n, i) * mid**i * (1 - mid) ** (n - i) for i in range(k + 1))
        if cdf > 1 - conf:
            lo = mid
        else:
            hi = mid
    return hi


design = {
    "V2-like, catches about half": (8, 0, 48, 49),
    "good judge, 3 wrong passes, 1 wrong fail": (7, 1, 3, 94),
    "rubber stamp, passes all 105": (8, 0, 97, 0),
    "fail-everything, fails all 105": (0, 8, 0, 97),
}
for name, c in design.items():
    po, kappa, pi, wps, miss, ff = agreement(*c)
    pc, pp = thakur(*c)
    print(name, c)
    print(f"  po={po:.3f} kappa={kappa:.3f} pi={pi:.3f} wrong-of-passes={wps:.3f} "
          f"bad-missed={miss:.3f} good-failed={ff:.3f} Pc={pc:.3f} P+={pp:.3f}")

print("90% upper bound on a rate")
for label, k, n in [("bad missed 0 of 97", 0, 97), ("bad missed 3 of 97", 3, 97),
                    ("bad missed 0 of 8", 0, 8), ("bad missed 0 of 5", 0, 5),
                    ("bad missed 0 of 3", 0, 3), ("good failed 0 of 8", 0, 8),
                    ("good failed 1 of 8", 1, 8)]:
    print(f"  {label:20s} {cp_upper(k, n):.3f}")
need = next(n for n in range(1, 500) if cp_upper(0, n) <= 0.05)
print(f"bad cases needed for a 5% bound with 0 misses: {need}")
