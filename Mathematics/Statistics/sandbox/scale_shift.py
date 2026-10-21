# The mean and variance of Y = aX + b, worked on a fair die and checked face by face.
from fractions import Fraction as F

faces = range(1, 7); p = F(1, 6)
mean = sum(p * x for x in faces); var = sum(p * (x - mean) ** 2 for x in faces)
print(f"X: mean {float(mean)}, variance {var} = {float(var):.4f}")
a, b = 2, 1
ys = [a * x + b for x in faces]
my = sum(p * y for y in ys); vy = sum(p * (y - my) ** 2 for y in ys)
print(f"Y = 2X + 1 face by face: values {ys}, mean {float(my)}, variance {vy} = {float(vy):.4f}, sd {float(vy) ** 0.5:.4f}")
print(f"by the rules: mean a*3.5 + b = {a * 3.5 + b}, variance a^2 * 35/12 = {a * a * 35 / 12:.4f}, sd |a| * sqrt(35/12) = {abs(a) * (35 / 12) ** 0.5:.4f}")
print(f"slip, a in place of a^2: {a * 35 / 12:.4f}; slip, b added to the variance: {a * a * 35 / 12 + b:.4f}")
a = -2
vz = sum(p * ((a * x + b) - (a * mean + b)) ** 2 for x in faces)
print(f"Z = -2X + 1: mean {float(a * mean + b)}, variance {float(vz):.4f}, sd {float(vz) ** 0.5:.4f} (|a| = 2, not -2)")
abar = 0.4783
print(f"the ladder: x_t = sqrt(abar) x0 + sqrt(1 - abar) eps at t = 50: noise coefficient {(1 - abar) ** 0.5:.4f}, its variance {1 - abar:.4f}; coefficient 1 - abar would give variance {(1 - abar) ** 2:.4f}")
