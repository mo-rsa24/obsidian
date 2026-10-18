"""The Gaussian quantile from the standard library, and a product of two densities that needs its area first.
Standard library only. Run with: python3 -I inverse_gaussian_and_product.py"""
import math
import random
from bisect import bisect_left
from statistics import NormalDist

U = [0.12, 0.85, 0.47, 0.93, 0.30, 0.66, 0.05, 0.71, 0.58, 0.24]

print("GAUSSIAN: F has no closed-form inverse; NormalDist().inv_cdf finds it numerically")
std = NormalDist(0.0, 1.0)
print(f"inv_cdf(0.975) = {std.inv_cdf(0.975):.6f}   cdf of that = {std.cdf(std.inv_cdf(0.975)):.6f}")
post = NormalDist(8 / 3, 2 / 3)
print(f"posterior N(8/3, (2/3)^2): ten draws from the ten fixed uniforms")
print(f"{'i':>2} {'u':>5} {'z = inv_cdf(u)':>15} {'x = 8/3 + 2/3 z':>16} {'inv_cdf on N(8/3,2/3)':>22}")
for i, u in enumerate(U, start=1):
    z = std.inv_cdf(u)
    print(f"{i:>2} {u:>5.2f} {z:>15.6f} {8 / 3 + 2 / 3 * z:>16.6f} {post.inv_cdf(u):>22.6f}")


def bisect_inverse(cdf, u, lo=-10.0, hi=10.0):
    steps = 0
    while hi - lo > 1e-12:
        mid = (lo + hi) / 2
        if cdf(mid) < u:
            lo = mid
        else:
            hi = mid
        steps += 1
    return (lo + hi) / 2, steps


x, steps = bisect_inverse(std.cdf, 0.975)
print(f"by bisection on the CDF: x = {x:.6f} after {steps} halvings of [-10, 10]")

print()
print("A PRODUCT OF TWO DENSITIES: N(0, 1) times N(1, 1)")
a, b = NormalDist(0, 1), NormalDist(1, 1)
lo, hi, n = -10.0, 10.0, 8000
h = (hi - lo) / n
xs = [lo + h * k for k in range(n + 1)]
prod = [a.pdf(x) * b.pdf(x) for x in xs]
cum = [0.0]
for k in range(n):
    cum.append(cum[-1] + (prod[k] + prod[k + 1]) / 2 * h)
area = cum[-1]
exact_area = NormalDist(0, math.sqrt(2)).pdf(1.0)
print(f"area under the product (trapezoids, {n} strips): {area:.6f}")
print(f"exact area, the N(0, 2) density at 1:           {exact_area:.6f}")
print(f"largest value of the running sum if used as a CDF: {cum[-1]:.6f}  (a CDF must end at 1)")
cdf_norm = [c / area for c in cum]
print(f"after dividing by the area, the sum ends at: {cdf_norm[-1]:.6f}")

rng = random.Random(7)
m = 100000
draws = []
for _ in range(m):
    u = rng.random()
    k = bisect_left(cdf_norm, u)
    if k == 0:
        draws.append(xs[0])
    else:
        c0, c1 = cdf_norm[k - 1], cdf_norm[k]
        t = (u - c0) / (c1 - c0) if c1 > c0 else 0.0
        draws.append(xs[k - 1] + t * h)
mean = sum(draws) / m
var = sum((d - mean) ** 2 for d in draws) / m
print(f"{m} draws, seed 7: mean {mean:.4f} (exact 0.5), variance {var:.4f} (exact 0.5)")
