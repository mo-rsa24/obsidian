"""Inverse transform sampling on ten fixed uniforms: exponential rate 2, Rayleigh, and a discrete lookup.
Standard library only. Run with: python3 -I inverse_by_hand.py"""
import math
from bisect import bisect_left

U = [0.12, 0.85, 0.47, 0.93, 0.30, 0.66, 0.05, 0.71, 0.58, 0.24]

print("EXPONENTIAL, rate 2: F(x) = 1 - exp(-2x), x = -ln(1 - u) / 2")
print(f"{'i':>2} {'u':>5} {'1-u':>5} {'ln(1-u)':>9} {'-ln(1-u)':>9} {'x':>9} {'F(x)':>7}")
expo = []
for i, u in enumerate(U, start=1):
    a = 1 - u
    b = math.log(a)
    c = -b
    x = c / 2
    expo.append(x)
    print(f"{i:>2} {u:>5.2f} {a:>5.2f} {b:>9.6f} {c:>9.6f} {x:>9.6f} {1 - math.exp(-2 * x):>7.4f}")

print()
print("RAYLEIGH TYPE: F(x) = 1 - exp(-x^2 / 2), x = sqrt(-2 ln(1 - u))")
print(f"{'i':>2} {'u':>5} {'1-u':>5} {'ln(1-u)':>9} {'-2ln(1-u)':>10} {'x':>9} {'F(x)':>7}")
for i, u in enumerate(U, start=1):
    a = 1 - u
    b = math.log(a)
    c = -2 * b
    x = math.sqrt(c)
    print(f"{i:>2} {u:>5.2f} {a:>5.2f} {b:>9.6f} {c:>10.6f} {x:>9.6f} {1 - math.exp(-x * x / 2):>7.4f}")

print()
print("DISCRETE: values 1,2,3,4 with probabilities 0.1, 0.5, 0.3, 0.1")
tenths = [1, 5, 3, 1]
cum_tenths = []
run = 0
for t in tenths:
    run += t
    cum_tenths.append(run)
print("cumulative sums in tenths:", cum_tenths, " as probabilities:", [c / 10 for c in cum_tenths])
print(f"{'i':>2} {'u':>5} {'u in tenths':>12} {'first cumulative >= u':>22} {'value':>6}")
for i, u in enumerate(U, start=1):
    u10 = round(u * 100) / 10          # u in tenths, exact to one decimal of a tenth
    k = bisect_left([c * 1.0 for c in cum_tenths], u10)
    print(f"{i:>2} {u:>5.2f} {u10:>12.1f} {cum_tenths[k] / 10:>22.1f} {k + 1:>6}")

print()
print("FAILURE 1: u in place of 1 - u (exponential rate 2)")
print(f"{'i':>2} {'u':>5} {'x with 1-u':>11} {'x with u':>9} {'x with u == x(1-u)':>20}")
for i, u in enumerate(U, start=1):
    x_good = -math.log(1 - u) / 2
    x_swap = -math.log(u) / 2
    x_pair = -math.log(1 - (1 - u)) / 2
    print(f"{i:>2} {u:>5.2f} {x_good:>11.6f} {x_swap:>9.6f} {x_pair:>20.6f}")
order_good = sorted(range(10), key=lambda i: -math.log(1 - U[i]) / 2)
order_swap = sorted(range(10), key=lambda i: -math.log(U[i]) / 2)
print("draws ranked smallest to largest, by position i, with 1-u:", [i + 1 for i in order_good])
print("draws ranked smallest to largest, by position i, with u:  ", [i + 1 for i in order_swap])

print()
print("FAILURE 2: float cumulative sums at a jump (u = 0.9 exactly)")
cum_float = []
run = 0.0
for p in [0.1, 0.5, 0.3, 0.1]:
    run += p
    cum_float.append(run)
print("float cumulative sums:", cum_float)
print("value for u = 0.9 with float sums:   ", bisect_left(cum_float, 0.9) + 1)
print("value for u = 0.9 with integer tenths:", bisect_left(cum_tenths, 9) + 1)
