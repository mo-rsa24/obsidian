# Fewest answered rows with zero disagreements for the 90% upper bound to be at most alpha.
# Solve (1 - alpha)^n <= delta for n by logs, then check by looping n upward.
# Nothing here uses judge outcomes: zero disagreements is the assumption.
import math

delta = 0.10


def bound(n):
    """Exact one-sided upper bound on the true rate after n rows with no disagreement."""
    return 1 - delta ** (1 / n)


print("worked solves")
for alpha in (0.20, 0.10, 0.07, 0.05, 0.01):
    x = math.log(delta) / math.log(1 - alpha)
    n = math.ceil(x)
    print(f"alpha {alpha:.2f}: ln(delta) {math.log(delta):.4f} / ln(1-alpha) {math.log(1 - alpha):.4f}"
          f" = {x:.2f} -> n = {n}; bound at n {bound(n):.6f}, at n-1 {bound(n - 1):.6f}")

print("the log base does not matter (alpha 0.10)")
print(f"  natural {math.log(delta) / math.log(0.9):.4f}  base 10 {math.log10(delta) / math.log10(0.9):.4f}")

print("substituting n back, alpha 0.10: (0.9)^n")
for n in (21, 22):
    print(f"  n {n}: 0.9^n = {0.9 ** n:.4f}  {'<=' if 0.9 ** n <= delta else '>'} {delta}")

print("check: loop n upward with the exact formula")
for alpha in (0.20, 0.10, 0.07, 0.05, 0.01):
    first = next(n for n in range(1, 10000) if bound(n) <= alpha)
    by_logs = math.ceil(math.log(delta) / math.log(1 - alpha))
    print(f"  alpha {alpha:.2f}: first n in the loop {first}, by logs {by_logs}, same: {first == by_logs}")

print("failure 1: forgetting to flip gives n <= 21.85 (alpha 0.10)")
for n in (1, 21):
    print(f"  n {n} would be allowed; its bound is {bound(n):.4f}, not at most 0.10")

print("failure 2: rounding to the nearest whole row (alpha 0.20)")
x = math.log(delta) / math.log(0.8)
print(f"  x {x:.2f} rounds to {round(x)}; bound at {round(x)} is {bound(round(x)):.4f}, above 0.20")
