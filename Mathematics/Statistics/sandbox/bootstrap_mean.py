# Bootstrap a mean of six MADE-UP values, with six resamples written out in full.
import random
from math import sqrt

x = [4, 6, 7, 9, 12, 14]          # made-up values (say, minutes to review six products)
n = len(x)
mean = sum(x) / n
print("values:", x, " n =", n)
print(f"mean = {sum(x)} / {n} = {mean:.4f}")

# The textbook route: the standard error of a mean is s / sqrt(n).
dev2 = [(v - mean) ** 2 for v in x]
print("squared distances from the mean:", [round(d, 4) for d in dev2], " sum =", round(sum(dev2), 4))
s_n1 = sqrt(sum(dev2) / (n - 1))     # divide by n - 1 (sample standard deviation)
s_n = sqrt(sum(dev2) / n)            # divide by n (what resampling imitates)
print(f"s (divide by n-1) = {s_n1:.4f}  ->  s/sqrt(n) = {s_n1 / sqrt(n):.4f}")
print(f"s (divide by n)   = {s_n:.4f}  ->  s/sqrt(n) = {s_n / sqrt(n):.4f}")

# Six resamples, every drawn value written out.
rnd = random.Random(2024)
print()
print("six resamples (positions 1..6 drawn with replacement):")
means = []
for k in range(1, 7):
    pos = [rnd.randrange(n) for _ in range(n)]
    drawn = [x[p] for p in pos]
    m = sum(drawn) / n
    means.append(m)
    print(f"  resample {k}: positions {[p + 1 for p in pos]} -> values {drawn} -> sum {sum(drawn)} -> mean {m:.4f}")
K = len(means)
mm = sum(means) / K
print(f"mean of the six means = {mm:.4f}")
d2 = [(m - mm) ** 2 for m in means]
print("squared distances:", [round(d, 4) for d in d2], " sum =", round(sum(d2), 4))
print(f"variance of the six means (divide by K = {K}) = {sum(d2) / K:.4f}")
print(f"bootstrap standard error from 6 resamples = {sqrt(sum(d2) / K):.4f}")

# The same, with many resamples.
for K in (100, 10000):
    rnd = random.Random(2024)
    ms = [sum(x[rnd.randrange(n)] for _ in range(n)) / n for _ in range(K)]
    mm = sum(ms) / K
    se = sqrt(sum((m - mm) ** 2 for m in ms) / K)
    print(f"K = {K:5d} resamples: mean of means {mm:.4f}, bootstrap standard error {se:.4f}")
ms.sort()
print(f"90% range of the K = 10000 resampled means: {ms[int(.05 * K)]:.3f} to {ms[int(.95 * K) - 1]:.3f}")
