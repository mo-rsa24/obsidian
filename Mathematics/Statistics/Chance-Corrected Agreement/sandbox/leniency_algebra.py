# Thakur's equations 4 and 5 solved for Pc and P+, step by step.
# Every judge outcome here is INVENTED. Cell order: (tp, fn, fp, tn), reviewer first.
from fractions import Fraction as F


def show(label, value):
    print(f"{label:32s} {float(value):.4f}   exact {value}")


tp, fn, fp, tn = 16, 1, 2, 1  # judge A of the 20-product table
n = tp + fn + fp + tn
s = F(tp + fn, n)
t_p, t_n = F(tp, n), F(tn, n)
print("judge A", (tp, fn, fp, tn), "n =", n)
show("s", s)
show("tP", t_p)
show("tN", t_n)

print("steps 1 and 2: divide equation 4 by s and equation 5 by (1 - s)")
a = t_p / s
b = t_n / (1 - s)
show("tP/s", a)
show("tN/(1-s)", b)

print("steps 3 and 4: open the bracket in equation 5, then add; the P+ terms cancel")
show("tP/s + tN/(1-s)", a + b)

print("step 5: the sum is 1 + Pc, so take 1 away")
pc = a + b - 1
show("Pc", pc)

print("step 6: P+ from equation 4")
show("1 - Pc", 1 - pc)
show("tP/s - Pc", a - pc)
pp_eq4 = (a - pc) / (1 - pc)
show("P+ from equation 4", pp_eq4)

print("step 7: P+ in Thakur's form")
show("1 - tN/(1-s)", 1 - b)
pp_paper = (1 - b) / (1 - pc)
show("P+ in Thakur's form", pp_paper)
print("the two forms equal:", pp_eq4 == pp_paper)

print("check: put Pc and P+ back into equations 4 and 5")
back_tp = s * (pc + (1 - pc) * pp_eq4)
back_tn = (1 - s) * (pc + (1 - pc) * (1 - pp_eq4))
show("equation 4 gives tP", back_tp)
show("equation 5 gives tN", back_tn)
print("both match the table:", back_tp == t_p and back_tn == t_n)

print("why the 1 is taken away: rubber stamp (17, 0, 3, 0)")
a2, b2 = F(17, 17), F(0, 3)
print("tP/s + tN/(1-s) =", a2 + b2, " so Pc =", a2 + b2 - 1)

print("failure: a perfect judge (17, 0, 0, 3)")
a3, b3 = F(17, 17), F(3, 3)
pc3 = a3 + b3 - 1
print("Pc =", pc3, " 1 - Pc =", 1 - pc3, " numerator 1 - tN/(1-s) =", 1 - b3)
try:
    print((1 - b3) / (1 - pc3))
except ZeroDivisionError as e:
    print("P+ = 0/0 ->", type(e).__name__)
s3 = F(17, 20)
for guess in (F(0), F(1, 2), F(1)):
    t4 = s3 * (pc3 + (1 - pc3) * guess)
    t5 = (1 - s3) * (pc3 + (1 - pc3) * (1 - guess))
    print(f"P+ = {guess}: equation 4 gives tP = {float(t4):.2f}, equation 5 gives tN = {float(t5):.2f}")
