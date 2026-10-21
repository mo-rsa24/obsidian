# Fit y = a + b x to four points by the normal equations, by hand sums, then check with numpy.
import numpy as np

xs = [0.0, 1.0, 2.0, 3.0]
ys = [1.0, 3.0, 4.0, 4.0]
n = len(xs)
sx, sy = sum(xs), sum(ys)
sxx = sum(x * x for x in xs)
sxy = sum(x * y for x, y in zip(xs, ys))
print(f"n {n}, sum x {sx:g}, sum y {sy:g}, sum x^2 {sxx:g}, sum xy {sxy:g}")
xbar, ybar = sx / n, sy / n
Sxx = sum((x - xbar) ** 2 for x in xs)
Sxy = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
b = Sxy / Sxx
a = ybar - b * xbar
print(f"xbar {xbar:g}, ybar {ybar:g}, S_xx {Sxx:g}, S_xy {Sxy:g}, slope b {b:g}, intercept a {a:g}")
r = [y - (a + b * x) for x, y in zip(xs, ys)]
print("residuals", [round(v, 4) for v in r], f"RSS {sum(v * v for v in r):g}",
      f"sum r {sum(r):g}", f"sum x*r {sum(x * v for x, v in zip(xs, r)):g}")
b0 = sxy / sxx
r0 = [y - b0 * x for x, y in zip(xs, ys)]
print(f"no intercept: slope {b0:.4f}, residuals", [round(v, 4) for v in r0],
      f"RSS {sum(v * v for v in r0):.4f}, sum r {sum(r0):.4f}")
M = np.column_stack((np.ones(n), xs))
print("lstsq [a, b]:", np.round(np.linalg.lstsq(M, np.array(ys), rcond=None)[0], 4),
      " M^T M:", (M.T @ M).tolist(), " M^T y:", (M.T @ np.array(ys)).tolist())
