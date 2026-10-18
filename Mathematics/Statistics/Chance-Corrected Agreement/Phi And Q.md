---
aliases: [kappa equals q times phi, kappa = q * phi, q factor, rate-mismatch factor, marginal normalization, kappa versus phi, Sahu and Demirtas identity, Rao equation 8]
sources:
  - Rao and Callison-Burch, agreement metrics for LLM judges, section 4.2, equations 7 and 8, https://arxiv.org/abs/2606.00093
  - Sahu and Demirtas (2024), credited by Rao and Callison-Burch for equation 8
---

# Phi And Q

Up: [[Chance-Corrected Agreement]] · [[Judge Leniency And The Gold Set]] ➡️

Mathematics, Statistics, Chance-Corrected Agreement. Needs: [[Chance-Corrected Agreement]] for kappa and the 20-product table, [[Correlation Coefficient]] for phi, and [[Arithmetic And Geometric Mean]] for why $q \le 1$. The map note keeps a short [[Chance-Corrected Agreement#Kappa as q times phi|summary]]; this note is the same result in full steps.

> [!question] Test yourself
> [Judge Agreement Quiz](https://claude.ai/artifact/RthoGPnogcnYFtTDMgPvqM) covers this folder. Its question "what does $q$ record in $\kappa = q\phi$" is answered under [[#What q records]].

> [!warning] Unfinished
> - The three drawn pictures (form, mechanism, deep-dive sheet) are not drawn, and no output picture is rendered: `~/.vault-sandbox` is missing on this machine, so there was no plotting library. To make it: `uv venv ~/.vault-sandbox` then `uv pip install --python ~/.vault-sandbox/bin/python pandas numpy scipy matplotlib statsmodels openpyxl`.
> - The quiz page above was built before this note and has not been extended with it.

**Kappa equals phi times a factor $q$ that is computed from the reviewer's and the judge's pass rates alone and equals 1 when they are equal.** This note takes kappa from its definition to that product one line at a time, runs it on four judges, shows where it misleads, and checks the product against kappa to four decimals.

**Two uses of the letters A and B.** Rao's identity names two products $A$ and $B$. The judges below are called judge A, judge B, judge C and judge D. They are unrelated: a bare $A$ or $B$ is always a product of counts, and a judge is always called "judge A".

**Where you work.** Any folder with Python 3.10 or later. Nothing is installed. Every judge outcome is invented.

## Table of contents

- [What q is and why it is here](#what-q-is-and-why-it-is-here)
- [What q records](#what-q-records)
- [Worked example on four judges](#worked-example-on-four-judges)
- [The method in numbered steps](#the-method-in-numbered-steps)
- [Where it goes wrong](#where-it-goes-wrong)
- [Check it by script](#check-it-by-script)
- [Other ways](#other-ways)
- [Taught in, applied in](#taught-in-applied-in)
- [How this was checked](#how-this-was-checked)
- [Videos](#videos)

## What q is and why it is here

Navigation: 📋 [[#Table of contents]] | [[#What q records]] ➡️

In plain words: phi and kappa are two scores for one judge and one reviewer. Phi asks whether the judge's pass and fail verdicts follow the reviewer's. Kappa asks that too, and also asks whether the judge passes about as often as the reviewer does. When the two pass rates match, the two scores are the same number. When they differ, kappa comes out smaller than phi, and $q$ is the number you multiply phi by to get kappa.

**$q$**, also the rate-mismatch factor, is a number between $0$ and $1$ computed from the two pass rates alone. Rao and Callison-Burch give it as their Eq. (8) and credit it to Sahu and Demirtas (2024).

**Why it is here.** A low kappa has two possible causes: the judge follows the reviewer poorly, or the judge passes at a different rate. $q$ separates them. If $q$ is near 1, the low kappa is a poor ordering. If $q$ is small, part of it is the pass rate.

**Why this matters.** A judge validated on kappa alone can be rejected for a rate that a threshold change would fix, or accepted when its rate happens to match. Backing: derived (the steps below), shown (the run), cited (Rao and Callison-Burch, arXiv 2606.00093, section 4.2, PDF pages 5 and 6).

## What q records

Navigation: ⬅️ [[#What q is and why it is here]] | 📋 [[#Table of contents]] | [[#Worked example on four judges]] ➡️

**$q$ is computed from the reviewer's pass rate and the judge's pass rate, and nothing else.** It is 1 exactly when the two rates are equal and smaller as they move apart. The same gap does not give the same $q$ at every level: a gap of 0.4 gives $q = 0.600$ at rates 0.5 and 0.1, and $q = 0.477$ at rates 0.95 and 0.55. It does not look at which products the judge got right.

Write $r = TP + FN$ for the number of products the reviewer passes and $j = TP + FP$ for the number the judge passes, out of $N$ products. The failures are then $N - r = FP + TN$ for the reviewer and $N - j = FN + TN$ for the judge. The two products of counts are

$$
A = (TP + FN)(FN + TN) = r\,(N - j), \qquad B = (TP + FP)(FP + TN) = j\,(N - r)
$$

so $A$ is the reviewer's passes times the judge's fails, and $B$ is the judge's passes times the reviewer's fails. They use only the two rows' and columns' totals, so $q$ cannot see the four cells inside.

1. Subtract: $A - B = r(N - j) - j(N - r) = rN - rj - jN + rj = N(r - j)$.
2. $A = B$ exactly when $N(r - j) = 0$, which is when $r = j$.
3. $q = \frac{2\sqrt{AB}}{A+B}$ is 1 exactly when $A = B$ ([[Arithmetic And Geometric Mean#Using it on q]]), so $q = 1$ exactly when $r = j$: the two pass rates $r/N$ and $j/N$ are equal.

On the 20-product table the reviewer passes 17 and the judge passes 18, so the rates are $17/20 = 0.85$ and $18/20 = 0.90$, $A = 17 \cdot 2 = 34$, $B = 18 \cdot 3 = 54$, and $A - B = -20 = 20 \cdot (17 - 18)$. The rates differ by 0.05, so $q$ is just under 1.

## Worked example on four judges

Navigation: ⬅️ [[#What q records]] | 📋 [[#Table of contents]] | [[#The method in numbered steps]] ➡️

The four judges read the same 20 products. The reviewer passes 17 and fails 3. Each judge's table is (TP, FN, FP, TN) with rows the reviewer and columns the judge, and every outcome is invented.

| judge | TP | FN | FP | TN | reviewer passes | judge passes |
|---|---:|---:|---:|---:|---:|---:|
| judge A | 16 | 1 | 2 | 1 | 17 | 18 |
| judge B | 17 | 0 | 2 | 1 | 17 | 19 |
| judge C | 17 | 0 | 3 | 0 | 17 | 20 |
| judge D | 14 | 3 | 0 | 3 | 17 | 14 |

**Judge A, every value.**

| Step | Value |
|---|---|
| $A = (TP+FN)(FN+TN)$ | $17 \cdot 2 = 34$ |
| $B = (TP+FP)(FP+TN)$ | $18 \cdot 3 = 54$ |
| top, $TP\cdot TN - FP\cdot FN$ | $16 \cdot 1 - 2 \cdot 1 = 14$ |
| $\kappa = 2 \cdot \text{top} / (A + B)$ | $28 / 88 = 0.3182$ |
| $q = 2\sqrt{AB} / (A + B)$ | $2 \cdot \sqrt{1836} / 88 = 85.697 / 88 = 0.9738$ |
| $\phi = \text{top} / \sqrt{AB}$ | $14 / 42.849 = 0.3267$ |
| $q \cdot \phi$ | $0.9738 \cdot 0.3267 = 0.3182$, equal to $\kappa$ |

**The four judges from the run** (the script is below).

| judge | $A$ | $B$ | top | $q$ | $\phi$ | $\kappa$ | $q\phi$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| judge A | 34 | 54 | 14 | 0.9738 | 0.3267 | 0.3182 | 0.3182 |
| judge B | 17 | 57 | 17 | 0.8413 | 0.5461 | 0.4595 | 0.4595 |
| judge C | 0 | 60 | 0 | 0.0000 | undefined | 0.0000 | undefined |
| judge D | 102 | 42 | 42 | 0.9091 | 0.6417 | 0.5833 | 0.5833 |

**Judge C passes every product.** $A = (17 + 0)(0 + 0) = 0$, so $q = 0$, and the top is $17 \cdot 0 - 3 \cdot 0 = 0$, so $\kappa = 0$ from the count form. Phi has the bottom $\sqrt{AB} = 0$ over a top of 0, which is undefined ([[Correlation Coefficient#Where it goes wrong]]). So $\kappa = q\phi$ cannot be evaluated for judge C, and kappa stands at 0 from its own formula.

**Judge D** passes 14 of 20 (a rate of 0.70) against the reviewer's 17 (0.85), a gap of 0.15. Judge A's rates are 0.90 and 0.85, a gap of 0.05. Judge D's $q$ is 0.9091 and judge A's is 0.9738, so the wider gap gives the lower $q$.

## The method in numbered steps

Navigation: ⬅️ [[#Worked example on four judges]] | 📋 [[#Table of contents]] | [[#Where it goes wrong]] ➡️

Textbook: [Introduction to probability for data science, PDF p. 278, the covariance expansion used in step 6](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=278)

**From kappa's definition to $\kappa = q\phi$.** With $r = TP + FN$, $j = TP + FP$ and $N$ products:

1. Kappa is $\kappa = \frac{p_o - p_e}{1 - p_e}$ with $p_o = \frac{TP + TN}{N}$ and $p_e = \frac{r}{N}\cdot\frac{j}{N} + \frac{N - r}{N}\cdot\frac{N - j}{N}$.
2. Multiply the top and the bottom of $\kappa$ by $N^2$:
$$
\kappa = \frac{N(TP + TN) - \big[\,rj + (N - r)(N - j)\,\big]}{N^2 - \big[\,rj + (N - r)(N - j)\,\big]}
$$
3. Multiply out $(N - r)(N - j) = N^2 - Nj - Nr + rj$, so the bracket is $rj + (N - r)(N - j) = N^2 - N(r + j) + 2rj$.
4. The bottom of $\kappa$ is $N^2 - \big[N^2 - N(r+j) + 2rj\big] = N(r + j) - 2rj$.
5. This is $A + B$: $A + B = r(N - j) + j(N - r) = Nr - rj + Nj - rj = N(r + j) - 2rj$. So the bottom of $\kappa$ is $A + B$.
6. The top of $\kappa$ is $N(TP + TN) - N^2 + N(r + j) - 2rj$. Group the first three terms: $N\,(TP + TN - N + r + j)$. Here $TP + TN - N = -(FN + FP)$ and $r + j = 2\,TP + FN + FP$, so the bracket is $2\,TP$. The top is $2N\cdot TP - 2rj = 2\big(N\cdot TP - (TP+FN)(TP+FP)\big)$, and the covariance steps 5 and 6 in [[Correlation Coefficient#The method in numbered steps]] show that $N\cdot TP - (TP + FN)(TP + FP) = TP\cdot TN - FP\cdot FN$. So the top is $2\,(TP\cdot TN - FP\cdot FN)$.
7. Put steps 5 and 6 together, which is Rao and Callison-Burch's Eq. (7):
$$
\kappa = \frac{2\,(TP\cdot TN - FP\cdot FN)}{A + B}
$$
8. Phi's top is $TP\cdot TN - FP\cdot FN$, the same quantity without the 2. Phi's bottom is $\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)} = \sqrt{j\cdot r\cdot(N - r)(N - j)}$, and $AB = r(N - j)\cdot j(N - r)$ has the same four factors, so the bottom is $\sqrt{AB}$:
$$
\phi = \frac{TP\cdot TN - FP\cdot FN}{\sqrt{AB}}
$$
9. Divide step 7 by step 8. The top $TP\cdot TN - FP\cdot FN$ cancels when it is not zero:
$$
\frac{\kappa}{\phi} = \frac{2\,(TP\cdot TN - FP\cdot FN)}{A + B}\cdot\frac{\sqrt{AB}}{TP\cdot TN - FP\cdot FN} = \frac{2\sqrt{AB}}{A + B} = q
$$
So $\kappa = q\,\phi$, Eq. (8). When the top is zero both $\kappa$ and $\phi$ have a zero top, and $\kappa = 0$.
10. $A + B \ge 2\sqrt{AB}$ by [[Arithmetic And Geometric Mean#The proof for two numbers]], so $q \le 1$ and $|\kappa| \le |\phi|$, with $q = 1$ exactly when $A = B$, which by [[#What q records]] is when the pass rates are equal.

**To redo it on new numbers.**

1. Fill the table: TP, FN, FP, TN.
2. Compute $A = (TP + FN)(FN + TN)$ and $B = (TP + FP)(FP + TN)$, and the top $TP\cdot TN - FP\cdot FN$.
3. $\kappa = 2\cdot\text{top} / (A + B)$ and $q = 2\sqrt{AB} / (A + B)$.
4. $\phi = \text{top} / \sqrt{AB}$, if $AB > 0$. If $AB = 0$, phi is undefined and kappa is 0.
5. Read $q$: near 1 means the pass rates are close, so a low kappa is a low phi. Small means the rates differ.

## Where it goes wrong

Navigation: ⬅️ [[#The method in numbered steps]] | 📋 [[#Table of contents]] | [[#Check it by script]] ➡️

**A judge that never passes a product the reviewer fails can still get a low kappa, because it passes too few.** Take 20 products where the reviewer passes 10 and fails 10. Judge E passes only 2 of the 10 the reviewer passes, and none of the 10 it fails: TP = 2, FN = 8, FP = 0, TN = 10. Every pass it gives is right.

| Step | Value |
|---|---|
| $A = 10 \cdot 18$ | 180 |
| $B = 2 \cdot 10$ | 20 |
| $q = 2\sqrt{3600} / 200$ | $120 / 200 = 0.6000$ |
| $\phi = \sqrt{B/A}$ | $\sqrt{20/180} = 0.3333$ |
| $\kappa = 2 \cdot 20 / 200$ | $0.2000$ |

The judge's kappa is 0.2000 against a phi of 0.3333, 40% lower, and $q$ is the 0.6000 that does it. Reading the low kappa as "it orders products badly" would be wrong: it orders them without one wrong pass and passes at a rate of 0.10 against the reviewer's 0.50. With judge E at 5 passes of 10 instead, $q$ is 0.8660, phi 0.5774 and kappa 0.5000.

**What this example does not show.** A judge that orders products exactly as the reviewer does and has a high phi together with a low kappa cannot be built at rates this far apart. With FP = 0, TN equals $N - r$ and TP equals $j$, so the top is $TP\cdot TN = j(N - r) = B$, and $\phi = B / \sqrt{AB} = \sqrt{B/A}$. A large gap between the rates, which makes $q$ small, makes $B/A$ small too and pulls phi down with it. Kappa then equals $2B/(A + B)$, which is $0.2$ for judge E. The run below shows $\sqrt{B/A}$ matching phi for both strict judges.

## Check it by script

Navigation: ⬅️ [[#Where it goes wrong]] | 📋 [[#Table of contents]] | [[#Other ways]] ➡️

**By hand.** Judge A in the table above: $q\phi = 0.9738 \cdot 0.3267 = 0.3182 = \kappa$.

**Try it yourself.** The script computes $A$, $B$, $q$, $\phi$ and $\kappa$ for the four judges, kappa a second way from the pass rates, the two strict judges, and 20000 random tables.

1. What you need: Python 3.10 or later. Check with `python3 --version`. You should see a line such as `Python 3.12.14`.
2. If it is missing: install Python 3 from python.org, or with `uv python install 3.12`. Not run on this machine, which already has it.
3. Setup:

```bash
mkdir phi_q_demo && cd phi_q_demo
```

4. Save this as `phi_q.py`:

```python
import random
from math import sqrt


def numbers(TP, FN, FP, TN):
    N = TP + FN + FP + TN
    A = (TP + FN) * (FN + TN)
    B = (TP + FP) * (FP + TN)
    top = TP * TN - FP * FN
    kappa = 2 * top / (A + B)
    q = 2 * sqrt(A * B) / (A + B)
    bottom = sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
    phi = top / bottom if bottom else None
    p_o = (TP + TN) / N
    p_e = ((TP + FN) / N) * ((TP + FP) / N) + ((FP + TN) / N) * ((FN + TN) / N)
    kappa_rates = (p_o - p_e) / (1 - p_e)
    return A, B, top, q, phi, kappa, kappa_rates


judges = {
    "judge A": (16, 1, 2, 1),
    "judge B": (17, 0, 2, 1),
    "judge C": (17, 0, 3, 0),
    "judge D": (14, 3, 0, 3),
}
print("judge     A    B   top      q    phi  kappa  kappa from rates  q*phi")
for name, table in judges.items():
    A, B, top, q, phi, kappa, kappa_rates = numbers(*table)
    phi_text = f"{phi:.4f}" if phi is not None else "undef"
    product = f"{q * phi:.4f}" if phi is not None else "undef"
    print(f"{name}  {A:>3}  {B:>3}  {top:>4}  {q:.4f}  {phi_text:>5}  {kappa:.4f}  {kappa_rates:>16.4f}  {product:>5}")

print()
print("a judge that never passes a product the reviewer fails, at a stricter pass rate")
for name, table in {"strict 5 of 10": (5, 5, 0, 10), "strict 2 of 10": (2, 8, 0, 10)}.items():
    A, B, top, q, phi, kappa, kappa_rates = numbers(*table)
    print(f"{name}: A {A}, B {B}, q {q:.4f}, phi {phi:.4f}, sqrt(B/A) {sqrt(B / A):.4f}, kappa {kappa:.4f}")

random.seed(0)
worst = 0.0
checked = 0
for _ in range(20000):
    table = [random.randint(0, 30) for _ in range(4)]
    A, B, top, q, phi, kappa, kappa_rates = numbers(*table) if sum(table) and (table[0] + table[1]) * (table[2] + table[3]) * (table[0] + table[2]) * (table[1] + table[3]) else (0, 0, 0, 0, None, 0, 0)
    if phi is None:
        continue
    checked += 1
    worst = max(worst, abs(kappa - q * phi), abs(kappa - kappa_rates))
print()
print(f"random tables checked: {checked}, largest |kappa - q*phi| or |kappa - kappa from rates|: {worst:.2e}")
```

5. Run it:

```bash
python3 phi_q.py
```

You should see:

```text
judge     A    B   top      q    phi  kappa  kappa from rates  q*phi
judge A   34   54    14  0.9738  0.3267  0.3182            0.3182  0.3182
judge B   17   57    17  0.8413  0.5461  0.4595            0.4595  0.4595
judge C    0   60     0  0.0000  undef  0.0000            0.0000  undef
judge D  102   42    42  0.9091  0.6417  0.5833            0.5833  0.5833

a judge that never passes a product the reviewer fails, at a stricter pass rate
strict 5 of 10: A 150, B 50, q 0.8660, phi 0.5774, sqrt(B/A) 0.5774, kappa 0.5000
strict 2 of 10: A 180, B 20, q 0.6000, phi 0.3333, sqrt(B/A) 0.3333, kappa 0.2000

random tables checked: 19907, largest |kappa - q*phi| or |kappa - kappa from rates|: 1.32e-15
```

6. Clean up, and prove it is gone by running the listing again:

```bash
cd .. && rm -r phi_q_demo && ls phi_q_demo
```

```text
ls: phi_q_demo: No such file or directory
```

**Reading the output.**

| Field | Value in this run | How to read it | Backing |
|---|---|---|---|
| `A`, `B`, `top` for judge A | 34, 54, 14 | the products and the top of the worked example | derived |
| `q` | 0.9738 | $2\sqrt{AB}/(A+B)$ | derived |
| `phi` | 0.3267 | top over $\sqrt{AB}$; `undef` for judge C, where the bottom is 0 | derived |
| `kappa` | 0.3182 | the count form, Eq. (7) | derived |
| `kappa from rates` | 0.3182 | $(p_o - p_e)/(1 - p_e)$ computed the usual way, equal to `kappa` for all four judges | shown |
| `q*phi` | 0.3182 | equal to `kappa` to four decimals for judges A, B and D | shown |
| `strict 2 of 10` | q 0.6000, phi 0.3333, kappa 0.2000 | the failure case; `sqrt(B/A)` equals phi | shown, derived |
| last line | 19907 tables, 1.32e-15 | on random tables where phi is defined, kappa, $q\phi$ and the rates form agree to floating-point error | shown |

**Why this matters.** The four-judge rows and the 19907 random tables are the same claim as steps 1 to 9, so an algebra slip would show as a gap in the last column. The hand-count and the formula agree to four decimals.

## Other ways

Navigation: ⬅️ [[#Check it by script]] | 📋 [[#Table of contents]] | [[#Taught in, applied in]] ➡️

**Other chance corrections.** Rao and Callison-Burch's footnote 2 names Brennan and Prediger (1981), Gwet (2008), and Byrt, Bishop and Carlin (1993) as other baselines; none removes the need for the pass rates and the table. $q$ is derived for Cohen's kappa only; this note does not relate Scott's pi ([[Chance-Corrected Agreement#Scott's pi]]) to phi. **Standard error.** At matched pass rates kappa and phi have the same large-sample variance (section 4.3); [[How Sure Kappa Is]] covers how noisy kappa is.

## Taught in, applied in

Navigation: ⬅️ [[#Other ways]] | 📋 [[#Table of contents]] | [[#How this was checked]] ➡️

**Taught in.**

- [Step 5 of the worked example for validating an LLM judge](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/drips/combine-validating-an-llm-judge/checks/worked-example-latex.md#step-5-raos-identity-kappa--q-times-phi), the 20-product table with kappa 0.3182, phi 0.3267 and $q$ 0.9738.
- [The script `test-jung.py` and its saved output](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/drips/combine-validating-an-llm-judge/checks/test-jung.out), the last line of which is the same $A = 34$, $B = 54$.
- [Rao and Callison-Burch, section 4.2](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/sources/agreement-metrics-for-llm-judges/paper/2606.00093.pdf#page=5), Eq. (7) and (8), the paragraph crediting Sahu and Demirtas and the one on a judge that orders items like the human but at a different rate (PDF pages 5 and 6).

**Applied in.**

- [[Chance-Corrected Agreement#Four judges on the same 20 products]]: the four judges' kappa and phi side by side.
- The v3 product-content judge in the Dis-Chem product data repo: kappa against phi on the gold set, to tell a poor ordering from a pass rate that differs from the reviewer's. Its real pass rates are not measured yet.

## How this was checked

Navigation: ⬅️ [[#Taught in, applied in]] | 📋 [[#Table of contents]] | [[#Videos]] ➡️

> [!note]- How this was checked
> `phi_q.py` was run on 2026-10-18 on a Mac with Python 3.12.14, standard library only, from an empty folder that was removed afterwards, the listing then failing as shown. A rerun gave the same output. The prepared environment `~/.vault-sandbox` is missing on this machine and was not needed. The four tables and the 20-product figures match the learning tree's saved `test-jung.out` (A = 34, B = 54, q 0.9738, phi 0.3267) and the four-judge kappas in [[Chance-Corrected Agreement#Four judges on the same 20 products]] (0.318, 0.459, 0.000, 0.583). Rao and Callison-Burch's Eq. (4), (7) and (8) and the crediting sentence were read on PDF pages 5 and 6. The page has not been rendered in Obsidian. Every judge outcome is invented, and none is a measurement of the v3 judge. No claim is marked stated.

## Videos

Navigation: ⬅️ [[#How this was checked]] | 📋 [[#Table of contents]]

<!-- video-table: phi-matthews-correlation rev=1 -->
Pedram Jahangiry, from the open web, on the Matthews correlation coefficient of a confusion matrix, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The coefficient is the correlation between actual and predicted: true positive times true negative minus false positive times false negative, over the square root of the four pair sums; it runs from minus 1 to 1 | Intuition, open web | [Jahangiry, Performance metrics for classification models, 16:22 to 18:24](https://www.youtube.com/watch?v=IDPmX6xT3Us&t=982s) |
| 2 | 100 cases with 2 defaulters and a model that always says no default: accuracy 98 percent, precision, recall and F1 all 0, and the coefficient read as 0 | Worked example, open web | [Jahangiry, Performance metrics for classification models, 18:54 to 20:30](https://www.youtube.com/watch?v=IDPmX6xT3Us&t=1134s) |

Nothing on Mahesh Huddar's channel covers the phi or Matthews coefficient, and no video on a listed creator does. The example skips the arithmetic of the denominator: with that table it is 0, so the coefficient is undefined and conventionally set to 0. He does not name the phi coefficient, which is the same quantity for any two yes-or-no columns. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

No video was found for q or for kappa = q times phi. For the mean inequality behind q, see the videos in [[Arithmetic And Geometric Mean]]; for correlation itself, those in [[Correlation Coefficient]].
