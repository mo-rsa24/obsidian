# test 4: the 105-row design (8 good, 97 bad) with a judge that may send rows to review.
# Judge outcomes are INVENTED. Reviewer label: good = pass, bad = not pass.
from math import comb, sqrt

# rows: (reviewer, judge) -> count
cells = {("good","pass"): 7, ("good","fail"): 0, ("good","review"): 1,
         ("bad","pass"): 3,  ("bad","fail"): 70, ("bad","review"): 24}
N = sum(cells.values())
print("N =", N, " judge passes/fails/reviews =",
      sum(v for (r,j),v in cells.items() if j=="pass"),
      sum(v for (r,j),v in cells.items() if j=="fail"),
      sum(v for (r,j),v in cells.items() if j=="review"))

def binary_stats(tp, fn, fp, tn):
    n = tp+fn+fp+tn; a=(tp+fn)/n; b=(tp+fp)/n; po=(tp+tn)/n
    pe=a*b+(1-a)*(1-b); k=(po-pe)/(1-pe) if pe<1 else float("nan")
    return n, po, k

# Rule 1: exclusion. Drop rows the judge sent to review.
tp,fn,fp,tn = cells[("good","pass")], cells[("good","fail")], cells[("bad","pass")], cells[("bad","fail")]
n1, acc1, k1 = binary_stats(tp,fn,fp,tn)
cov = n1 / N
print(f"exclusion:  N_eff={n1} accuracy={acc1:.3f} kappa={k1:.3f} coverage={cov:.3f}")
lo, hi = acc1*cov, acc1*cov + (1-cov)
print(f"  full-set accuracy must lie in [{lo:.3f}, {hi:.3f}] (width = uncovered share {1-cov:.3f})")

# Rule 2: negative recoding. review counts as not-pass (fail).
tp2, fn2 = cells[("good","pass")], cells[("good","fail")] + cells[("good","review")]
fp2, tn2 = cells[("bad","pass")], cells[("bad","fail")] + cells[("bad","review")]
n2, acc2, k2 = binary_stats(tp2,fn2,fp2,tn2)
print(f"recoding:   N_eff={n2} accuracy={acc2:.3f} kappa={k2:.3f}  (wrong passes {fp2}, wrong fails {fn2})")

# Rule 3: three-class retention. Reviewer has two labels, judge three; a review never matches.
cats = ["pass","fail","review"]
ref = {"good":"pass","bad":"fail"}
M = {(a,b):0 for a in cats for b in cats}
for (r,j),v in cells.items(): M[(ref[r],j)] += v
diag = sum(M[(c,c)] for c in cats)
po3 = diag / N
rows = {a: sum(M[(a,b)] for b in cats)/N for a in cats}
cols = {b: sum(M[(a,b)] for a in cats)/N for b in cats}
pe3 = sum(rows[c]*cols[c] for c in cats)
k3 = (po3-pe3)/(1-pe3)
print(f"three-class: N_eff={N} accuracy={po3:.3f} kappa={k3:.3f}")

# What matters for the costly error, read straight from the cells
bad = 97; good = 8
print(f"bad products: passed {cells[('bad','pass')]} ({cells[('bad','pass')]/bad:.3f}), failed {cells[('bad','fail')]}, sent to a person {cells[('bad','review')]} ({cells[('bad','review')]/bad:.3f})")
print(f"good pages: passed {cells[('good','pass')]}, failed {cells[('good','fail')]}, sent to a person {cells[('good','review')]}")
print(f"rows reaching a person: {sum(v for (r,j),v in cells.items() if j=='review')} of {N} = {sum(v for (r,j),v in cells.items() if j=='review')/N:.3f}")

def cp_upper(k, n, conf=0.90):
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid=(lo+hi)/2
        cdf=sum(comb(n,i)*mid**i*(1-mid)**(n-i) for i in range(k+1))
        if cdf>1-conf: lo=mid
        else: hi=mid
    return hi
print(f"bad passed 3 of 97: 90% upper bound {cp_upper(3,97):.3f}")
print(f"answered rows only (80): wrong passes 3 of 10 passes = {3/10:.3f}")
