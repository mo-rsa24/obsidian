# Thakur's leniency model (equations 4, 5, 18) on four judges, then a bootstrap for judge A.
# Cell order everywhere: (reviewer pass and judge pass, reviewer pass and judge fail,
#                         reviewer fail and judge pass, both fail).
import random


def thakur(tp, fn, fp, tn):
    n = tp + fn + fp + tn
    s = (tp + fn) / n  # share of items that are truly good
    t_p, t_n = tp / n, tn / n  # joint shares, as in Thakur's tP and tN
    pc = t_p / s + t_n / (1 - s) - 1
    pplus = (1 - t_n / (1 - s)) / (1 - pc) if pc < 1 else float("nan")
    return s, pc, pplus


judges = {
    "A": (16, 1, 2, 1),
    "B": (17, 0, 2, 1),
    "C rubber stamp": (17, 0, 3, 0),
    "D strict": (14, 3, 0, 3),
}
for name, c in judges.items():
    s, pc, pp = thakur(*c)
    print(f"{name:15s} {c}  s={s:.3f}  Pc={pc:.3f}  P+={pp:.3f}")

random.seed(0)
items = [(1, 1)] * 16 + [(1, 0)] * 1 + [(0, 1)] * 2 + [(0, 0)] * 1  # (reviewer pass, judge pass)
values = []
for _ in range(10000):
    r = [random.choice(items) for _ in items]
    tp = sum(1 for x, y in r if x and y)
    fn = sum(1 for x, y in r if x and not y)
    fp = sum(1 for x, y in r if not x and y)
    tn = sum(1 for x, y in r if not x and not y)
    if tp + fn == 0 or fp + tn == 0:
        continue
    pp = thakur(tp, fn, fp, tn)[2]
    if pp == pp:  # drop nan
        values.append(pp)
values.sort()
print(
    f"A bootstrap P+ ({len(values)} usable of 10000): "
    f"5%={values[int(.05 * len(values))]:.2f} "
    f"median={values[len(values) // 2]:.2f} "
    f"95%={values[int(.95 * len(values)) - 1]:.2f}"
)
