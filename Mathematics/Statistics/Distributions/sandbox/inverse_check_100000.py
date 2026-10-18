"""Check: 100000 seeded draws against the exact values from the CDF. Standard library only.
Run with: python3 -I inverse_check_100000.py"""
import math
import random
from bisect import bisect_left

N = 100000
rng = random.Random(20261018)
U = [rng.random() for _ in range(N)]


def report(name, stat_value, exact, se):
    z = (stat_value - exact) / se
    print(f"{name:<44} sample {stat_value:.6f}  exact {exact:.6f}  gap {stat_value - exact:+.6f}  gap/SE {z:+.2f}")


print(f"seed 20261018, N = {N}, first three uniforms: {U[0]:.6f} {U[1]:.6f} {U[2]:.6f}")

print()
print("EXPONENTIAL rate 2: mean exact 1/2, sd exact 1/2, P(X < 0.5) exact 1 - exp(-1)")
X = [-math.log(1 - u) / 2 for u in U]
mean = sum(X) / N
report("mean", mean, 0.5, 0.5 / math.sqrt(N))
frac = sum(1 for x in X if x < 0.5) / N
p = 1 - math.exp(-1)
report("fraction below 0.5", frac, p, math.sqrt(p * (1 - p) / N))

print()
print("RAYLEIGH type: mean exact sqrt(pi/2), P(X < 1) exact 1 - exp(-1/2)")
R = [math.sqrt(-2 * math.log(1 - u)) for u in U]
mean = sum(R) / N
sd = math.sqrt(2 - math.pi / 2)
report("mean", mean, math.sqrt(math.pi / 2), sd / math.sqrt(N))
frac = sum(1 for r in R if r < 1) / N
p = 1 - math.exp(-0.5)
report("fraction below 1", frac, p, math.sqrt(p * (1 - p) / N))

print()
print("DISCRETE 1,2,3,4 with 0.1, 0.5, 0.3, 0.1")
cum = [0.1, 0.6, 0.9, 1.0]
counts = [0, 0, 0, 0]
for u in U:
    counts[bisect_left(cum, u)] += 1
for v, (cnt, pr) in enumerate(zip(counts, [0.1, 0.5, 0.3, 0.1]), start=1):
    report(f"fraction equal to {v}", cnt / N, pr, math.sqrt(pr * (1 - pr) / N))

print()
print("u IN PLACE OF 1 - u (exponential rate 2), same uniforms")
X2 = [-math.log(u) / 2 if u > 0 else float("inf") for u in U]
report("mean", sum(X2) / N, 0.5, 0.5 / math.sqrt(N))
report("fraction below 0.5", sum(1 for x in X2 if x < 0.5) / N, 1 - math.exp(-1), math.sqrt((1 - math.exp(-1)) * math.exp(-1) / N))
same = sum(1 for a, b in zip(X, X2) if abs(a - b) < 1e-12)
print(f"draws identical between the two rules: {same} of {N}")
corr_num = sum((a - 0.5) * (b - 0.5) for a, b in zip(X, X2)) / N
print(f"covariance of the two lists of draws: {corr_num:+.4f} (negative: a big draw in one is a small draw in the other)")

print()
print("A LINE FROM Selective Evaluation: c = 0.5 + 0.5 * random() ** 0.5")
print("Solving u = F(c) for c = 0.5 + 0.5 * sqrt(u) gives F(c) = 4 * (c - 0.5)**2 on 0.5 <= c <= 1")
C = [0.5 + 0.5 * u ** 0.5 for u in U]
report("fraction of c below 0.75", sum(1 for c in C if c < 0.75) / N, 4 * 0.25 ** 2, math.sqrt(0.25 * 0.75 / N))
report("mean of c (exact 0.5 + 0.5 * 2/3)", sum(C) / N, 0.5 + 0.5 * 2 / 3, math.sqrt(1 / 18 * 0.25 / N))
