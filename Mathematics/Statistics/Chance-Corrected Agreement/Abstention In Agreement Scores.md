---
aliases: [abstention handling, handling abstention, abstention in agreement, CANNOT_ASSESS, can't assess, exclusion rule, negative recoding, three-class retention, covered accuracy, joint coverage, full-set accuracy bound, identification bound, review as abstention, sent to review]
sources:
  - Rao and Callison-Burch, agreement metrics for LLM judges, https://arxiv.org/abs/2606.00093
---

# Abstention In Agreement Scores

Up: [[Chance-Corrected Agreement]] · ⬅️ [[The 105-Row Gold Set]] · [[How Sure Kappa Is]] ➡️

Mathematics, Statistics, Chance-Corrected Agreement. Needs: [[Chance-Corrected Agreement]] for kappa and accuracy, and [[The 105-Row Gold Set]] for the 105-row design.

> [!warning] Unfinished
> - The three drawn pictures (form, mechanism, deep-dive sheet) are not drawn, and no output picture is rendered: `~/.vault-sandbox` is missing on this machine, so there was no plotting library. To make it: `uv venv ~/.vault-sandbox` then `uv pip install --python ~/.vault-sandbox/bin/python pandas numpy scipy matplotlib statsmodels openpyxl`.
> - No quiz page yet.
> - 0 claims are marked stated.

**Abstention handling** is the rule that decides what a judge's "I will not decide" counts as before agreement is scored, and it changes the score. This note takes Rao and Callison-Burch's three rules (section 5.1), runs each on the 105-row design with a judge that sends some rows to review, and adds their bound on the accuracy over all rows (section 5.2, equation 10).

**Where you work.** Any folder with Python 3 and nothing installed. The judge's outcomes are invented; the paper's own numbers are marked as cited.

## Table of contents

- [Three rules for a row the judge will not decide](#three-rules-for-a-row-the-judge-will-not-decide)
- [The three rules on 105 rows](#the-three-rules-on-105-rows)
- [Accuracy over all rows is only bounded](#accuracy-over-all-rows-is-only-bounded)
- [Other ways](#other-ways)
- [Taught in, applied in](#taught-in-applied-in)
- [How this was checked](#how-this-was-checked)

## Three rules for a row the judge will not decide

Navigation: 📋 [[#Table of contents]] | [[#The three rules on 105 rows]] ➡️

**A judge that abstains** gives a third answer besides pass and fail. Rao and Callison-Burch call it CANNOT_ASSESS, CA for short, and say it "carries information that UNMET does not", so the reader must decide what it stands for before computing agreement. In the v3 judge the review verdict is the abstention. Three rules recur (section 5.1, PDF page 7):

**Exclusion** drops a pair when either side abstains. The score then describes agreement among the rows neither side abstained on. The paper says it fits when a hidden pass-or-fail answer exists behind the abstention.

**Negative recoding** maps CA to the failing label on both sides and scores the two-class table. It fits when the target is pass against everything else. It no longer tells CA from fail, and a judge that abstains on uncertain negatives scores the same as one that answers fail on them.

**Three-class retention** keeps CA as its own label and scores a 3 by 3 table with multi-class accuracy or kappa. It fits when the criterion can be genuinely inapplicable.

**The rules change the number, not only its meaning.** On the paper's own data (nine criteria, 2,007 decisions, only the human abstains; Table 5, page 8) the rules give accuracy 0.647 (exclusion), 0.580 (recoding) and 0.548 (three-class), and kappa 0.040, 0.047 and 0.032. Accuracy moves about 10 points and kappa 0.015. The paper's takeaway is that numbers computed under different rules are not comparable, even on the same verdicts.

**Why this matters.** A report of "agreement 0.96" with no statement of the rule is not a number anyone can reproduce. Backing: cited (Rao and Callison-Burch, arXiv 2606.00093, section 5.1, Table 5).

## The three rules on 105 rows

Navigation: ⬅️ [[#Three rules for a row the judge will not decide]] | 📋 [[#Table of contents]] | [[#Accuracy over all rows is only bounded]] ➡️

**The table.** The 105-row design of [[The 105-Row Gold Set#The 105-row design]]: 8 good pages and 97 bad copies, and an invented judge with three verdicts.

| | judge passes | judge fails | judge sends to review | row total |
|---|---:|---:|---:|---:|
| reviewer: good | 7 | 0 | 1 | 8 |
| reviewer: bad | 3 | 70 | 24 | 97 |
| judge total | 10 | 70 | 25 | 105 |

Save the script as `abstention.py` in an empty folder.

```python
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
```

Run it:

```bash
python3 abstention.py
```

You should see:

```text
N = 105  judge passes/fails/reviews = 10 70 25
exclusion:  N_eff=80 accuracy=0.963 kappa=0.803 coverage=0.762
  full-set accuracy must lie in [0.733, 0.971] (width = uncovered share 0.238)
recoding:   N_eff=105 accuracy=0.962 kappa=0.757  (wrong passes 3, wrong fails 1)
three-class: N_eff=105 accuracy=0.733 kappa=0.292
bad products: passed 3 (0.031), failed 70, sent to a person 24 (0.247)
good pages: passed 7, failed 0, sent to a person 1
rows reaching a person: 25 of 105 = 0.238
bad passed 3 of 97: 90% upper bound 0.068
answered rows only (80): wrong passes 3 of 10 passes = 0.300
```

**Reading the output.**

| Line | Value | How to read it |
|---|---|---|
| `exclusion` | 80 rows, accuracy 0.963, kappa 0.803, coverage 0.762 | drop the 25 review rows; the 80 left are 7 good passed, 3 bad passed and 70 bad failed. Coverage is $80/105$ |
| `recoding` | 105 rows, accuracy 0.962, kappa 0.757 | review counts as fail: the 1 good page sent to review becomes a wrong fail, the 24 bad ones become right fails. 3 wrong passes and 1 wrong fail remain |
| `three-class` | 105 rows, accuracy 0.733, kappa 0.292 | review never matches the reviewer, who has only two labels, so all 25 review rows are disagreements: $77/105$ |
| `full-set accuracy must lie in` | [0.733, 0.971] | see the next section |
| `bad products` | passed 3 (0.031), failed 70, sent to a person 24 (0.247) | what happens to the costly cases |
| `rows reaching a person` | 25 of 105 = 0.238 | the work the review verdict hands to people |

The same decisions give accuracy 0.963, 0.962 and 0.733 under the three rules. Exclusion and recoding land within 0.001 of each other here: the 24 bad rows sent to review are right fails under recoding and absent under exclusion, so either way they do not lower accuracy. The three-class figure is lower because it scores all 25 reviews as disagreements.

**Answered rows alone mislead on the costly error.** On the 80 answered rows the judge passes 10 rows and 3 are wrong, a wrong-pass share of 0.300, and 3 of the 97 bad products got through (a 90% upper bound of 0.068 on that rate, from [[Selective Evaluation#The exact binomial upper bound]]). The 24 bad rows sent to a person never reach the customer, which no accuracy under exclusion or recoding says outright.

![the one 105-row table scored three ways, with the bar [0.733, 0.971] for accuracy over all rows.|800](assets/one-table-three-scores.webp)
*All judge verdicts and confidences in this picture are invented.*

**Why this matters.** The same table can be reported as 0.96 or as 0.73. Choose the rule from what review means in the rubric. Backing: shown (the run), cited (rules from section 5.1).

## Accuracy over all rows is only bounded

Navigation: ⬅️ [[#The three rules on 105 rows]] | 📋 [[#Table of contents]] | [[#Other ways]] ➡️

**Covered accuracy tells you nothing certain about the rows the judge skipped.** With joint coverage $\gamma$ (the share of rows neither side abstained on), covered accuracy $A_{\text{cov}}$ and the unknown accuracy $A_{\text{uncov}}$ on the skipped rows, Rao and Callison-Burch's equation (10), page 8, is:

$$
A_{\text{full}} = \gamma A_{\text{cov}} + (1-\gamma)A_{\text{uncov}}, \qquad A_{\text{full}} \in [\gamma A_{\text{cov}},\ \gamma A_{\text{cov}} + 1 - \gamma]
$$

The low end treats every skipped row as a disagreement, the high end as an agreement, and the width is exactly the skipped share $1 - \gamma$. On the 105 rows $\gamma = 80/105 = 0.762$ and $A_{\text{cov}} = 77/80 = 0.9625$:

$$
\begin{aligned}
\gamma A_{\text{cov}} &= \frac{80}{105}\cdot\frac{77}{80} = \frac{77}{105} \approx 0.733 \\[4pt]
\gamma A_{\text{cov}} + 1 - \gamma &= 0.733 + 0.238 \approx 0.971
\end{aligned}
$$

So accuracy over all 105 rows lies between 0.733 and 0.971, exactly the script's line. The low end equals the three-class accuracy, because both count every review row as a disagreement (derived). On the paper's real data the same step gives [0.548, 0.701] at $\gamma = 0.848$ and covered accuracy 0.647, and the recoded accuracy 0.580 lies inside it while estimating a different quantity (cited, page 9).

**This is not a confidence interval.** The paper says the interval comes from the missing rows and not from sampling, and that reporting a bootstrap interval without it, or the bound as a confidence interval, mixes the two uncertainties. The sampling side is in [[How Sure Kappa Is]].

**Why this matters.** The wider the review share, the wider the bound: at 24% of rows to a person, accuracy is known only to within 24 points. Backing: derived, shown (the run), cited (equation 10).

## Other ways

Navigation: ⬅️ [[#Accuracy over all rows is only bounded]] | 📋 [[#Table of contents]] | [[#Taught in, applied in]] ➡️

**Reweight the covered rows.** If the abstentions depend only on observed features, weighting the covered rows by one over their chance of being covered recovers the full table (the paper cites Little and Rubin, page 9). Not taught here.

**Choose what to abstain on.** [[Selective Evaluation]] picks the confidence cut-off so that the answered rows agree with people at a rate you set.

## Taught in, applied in

Navigation: ⬅️ [[#Other ways]] | 📋 [[#Table of contents]] | [[#How this was checked]] ➡️

**Taught in.**

- [The combined reading of validating an LLM judge](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/drips/combine-validating-an-llm-judge/COMBINE_MAP.md), idea 4, review as abstention: what a number covers when the judge will not call.

**Applied in.**

- The v3 product-content judge in the Dis-Chem product data repo: a judge that gives pass, warning, review or fail, where a review sends the row to a person. The question was which accuracy to report when about a quarter of rows are reviewed. Outcomes here are invented.

## How this was checked

Navigation: ⬅️ [[#Taught in, applied in]] | 📋 [[#Table of contents]]

> [!note]- How this was checked
> `abstention.py` was run on 2026-10-18 on a Mac with Python 3.12 (standard library only) with `python3 -I`, from an empty folder that was removed afterwards. Its output matches the saved output of the learning tree's `test-4-review-as-abstention.py` on every number. The rules, equation 10 and Table 5 were read from Rao and Callison-Burch, PDF pages 7 to 9. The prepared environment `~/.vault-sandbox` does not exist on this machine, so the standard library interpreter was used. The note has not been rendered in Obsidian. The script is also saved in this folder's `sandbox/`.
>
> Claims marked stated, 0.
