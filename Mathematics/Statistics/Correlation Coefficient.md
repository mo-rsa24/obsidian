---
aliases: [correlation, Pearson correlation, Pearson's r, covariance of two variables, Cov(X, Y), phi coefficient, Matthews correlation coefficient, MCC, correlation of two yes-or-no columns, binary correlation, Pearson correlation coefficient, correlation matrix]
sources:
  - "Introduction to Probability for Data Science, Definitions 5.12 and 5.13 and Theorems 3.6 and 5.3: the vault's shelf copy, Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf"
  - "Rao and Callison-Burch, agreement metrics for LLM judges, section 4.1, https://arxiv.org/abs/2606.00093"
---

# Correlation Coefficient

Up: [[Statistics]]

Mathematics, Statistics. Needs: the mean and variance of a variable. For two yes-or-no columns it needs nothing else.

> [!question] Test yourself
> No quiz page covers this note yet. The [Judge Agreement Quiz](https://claude.ai/artifact/RthoGPnogcnYFtTDMgPvqM) asks what phi is, and this note is where phi is built.

> [!warning] Unfinished
> - The three drawn pictures (form, mechanism, deep-dive sheet) are not drawn, and no output picture is rendered: `~/.vault-sandbox` is missing on this machine, so there was no plotting library. To make it: `uv venv ~/.vault-sandbox` then `uv pip install --python ~/.vault-sandbox/bin/python pandas numpy scipy matplotlib statsmodels openpyxl`.
> - No quiz page for this note yet.

**The correlation coefficient says how closely two columns of numbers rise and fall together, on a scale from $-1$ to $1$.** It is the covariance of the two columns divided by the product of their standard deviations. This note builds it from covariance and from the variance of a yes-or-no variable, then derives the form it takes when both columns hold only passes and fails, called phi.

**Where you work.** Any folder with Python 3.10 or later. Nothing is installed. The reviewer and judge verdicts are invented.

## Table of contents

- [What it is and why it is here](#what-it-is-and-why-it-is-here)
- [Worked example on the 20-product table](#worked-example-on-the-20-product-table)
- [The method in numbered steps](#the-method-in-numbered-steps)
- [Where it goes wrong](#where-it-goes-wrong)
- [Check it two ways](#check-it-two-ways)
- [Other ways](#other-ways)
- [Taught in, applied in](#taught-in-applied-in)
- [How this was checked](#how-this-was-checked)
- [Videos](#videos)

## What it is and why it is here

Navigation: 📋 [[#Table of contents]] | [[#Worked example on the 20-product table]] ➡️

Textbook: [Introduction to probability for data science, 5.2 joint expectation: covariance (Definition 5.12, Theorem 5.3), PDF p. 278](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=278) · [the correlation coefficient (Definition 5.13), PDF p. 279](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=279) · [why the joint expectation is the product $E[XY]$, PDF p. 274](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=274) · [the variance of a Bernoulli variable (Theorem 3.6), PDF p. 154](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=154). The PDF page numbers are the file's; the book prints numbers 16 lower (page 278 prints 262).

In plain words: a reviewer and a judge each give pass or fail on the same products. If the judge passes the products the reviewer passes and fails the ones the reviewer fails, the two columns move together and the correlation is near $1$. If the judge's verdicts tell you nothing about the reviewer's, it is near $0$. If the judge passes exactly what the reviewer fails, it is $-1$.

Three pieces make the number.

**Covariance of two variables**, $\text{Cov}(X, Y)$, is the average of (how far $X$ is above its mean) times (how far $Y$ is above its mean). When both are above their means together, or both below together, the product is positive and the average comes out positive. The textbook gives it as $\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)]$ and then, by multiplying the bracket out, as

$$
\text{Cov}(X, Y) = E[XY] - E[X]\,E[Y]
$$

The textbook also says why the joint expectation uses the product $XY$ and not a sum or a quotient (p. 274): the product is what measures how the two move together.

**Variance of a yes-or-no variable.** If $X$ is 1 with probability $p$ and 0 otherwise, then $E[X] = p$, $E[X^2] = p$ (since $1^2 = 1$ and $0^2 = 0$), and

$$
\text{Var}[X] = E[X^2] - E[X]^2 = p - p^2 = p(1 - p)
$$

This is Theorem 3.6 on p. 154.

**Correlation coefficient**, $\rho$, also Pearson's $r$: covariance divided by the product of the two standard deviations, so that the units cancel and the result stays between $-1$ and $1$.

$$
\rho = \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}[X]\,\text{Var}[Y]}}
$$

**Phi**, $\phi$, also the phi coefficient or the binary Matthews correlation coefficient (MCC), is $\rho$ when both columns are yes-or-no. Rao and Callison-Burch (section 4.1) prove that Pearson, Spearman, Kendall's $\tau_b$, phi and MCC are one number on binary verdicts, so a report needs only one of them.

**Why it is here.** [[Phi And Q]] writes Cohen's kappa as a factor times phi. This note is where phi comes from.

**Why this matters.** Phi asks whether the judge's verdicts follow the reviewer's, whatever the two pass rates are. Backing: cited (the textbook pages above), derived (the steps below), shown (the run).

## Worked example on the 20-product table

Navigation: ⬅️ [[#What it is and why it is here]] | 📋 [[#Table of contents]] | [[#The method in numbered steps]] ➡️

The same table as [[Chance-Corrected Agreement#The table and observed agreement]]. $X$ is the reviewer's verdict and $Y$ is the judge's, 1 for pass and 0 for fail.

| | judge passes | judge fails | reviewer total |
|---|---:|---:|---:|
| reviewer passes | TP = 16 | FN = 1 | 17 |
| reviewer fails | FP = 2 | TN = 1 | 3 |
| judge total | 18 | 2 | 20 |

The outcomes are invented. Every value, in order:

| Step | Value |
|---|---|
| $E[X]$, the share of products the reviewer passes | $17 / 20 = 0.85$ |
| $E[Y]$, the share the judge passes | $18 / 20 = 0.90$ |
| $E[XY]$, the share where both pass (the product is 1 only there) | $16 / 20 = 0.80$ |
| $\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$ | $0.80 - 0.85 \cdot 0.90 = 0.80 - 0.765 = 0.035$ |
| $\text{Var}[X] = 0.85 \cdot (1 - 0.85)$ | $0.85 \cdot 0.15 = 0.1275$ |
| $\text{Var}[Y] = 0.90 \cdot (1 - 0.90)$ | $0.90 \cdot 0.10 = 0.0900$ |
| $\text{Var}[X]\,\text{Var}[Y]$ | $0.1275 \cdot 0.09 = 0.011475$ |
| square root of that | $0.107121$ |
| $\phi = 0.035 / 0.107121$ | $0.3267$ |

Cross-check with the counts: $\phi = \frac{16 \cdot 1 - 2 \cdot 1}{\sqrt{18 \cdot 17 \cdot 3 \cdot 2}} = \frac{14}{\sqrt{1836}} = \frac{14}{42.849} = 0.3267$.

## The method in numbered steps

Navigation: ⬅️ [[#Worked example on the 20-product table]] | 📋 [[#Table of contents]] | [[#Where it goes wrong]] ➡️

**Deriving the count formula for phi.** Write the table's four counts as TP, FN, FP, TN and the number of products as $N = TP + FN + FP + TN$.

1. $X = 1$ on the $TP + FN$ products the reviewer passes, so $E[X] = \frac{TP + FN}{N}$.
2. $Y = 1$ on the $TP + FP$ products the judge passes, so $E[Y] = \frac{TP + FP}{N}$.
3. $XY = 1$ only where both are 1, which is the $TP$ products, so $E[XY] = \frac{TP}{N}$.
4. Put steps 1 to 3 into the covariance and bring everything over the common bottom $N^2$:
$$
\text{Cov}(X, Y) = \frac{TP}{N} - \frac{(TP + FN)(TP + FP)}{N^2} = \frac{N \cdot TP - (TP + FN)(TP + FP)}{N^2}
$$
5. Replace $N$ by $TP + FN + FP + TN$ and multiply out both products on the top:
$$
\begin{aligned}
N \cdot TP &= TP^2 + TP\cdot FN + TP\cdot FP + TP\cdot TN \\
(TP + FN)(TP + FP) &= TP^2 + TP\cdot FP + FN\cdot TP + FN\cdot FP
\end{aligned}
$$
6. Subtract the second line from the first. $TP^2$, $TP\cdot FN$ and $TP\cdot FP$ appear in both and cancel, leaving $TP\cdot TN - FN\cdot FP$:
$$
\text{Cov}(X, Y) = \frac{TP \cdot TN - FP \cdot FN}{N^2}
$$
7. The reviewer's pass probability is $\frac{TP + FN}{N}$ and the fail probability is $1 - \frac{TP + FN}{N} = \frac{FP + TN}{N}$, so
$$
\text{Var}[X] = \frac{(TP + FN)(FP + TN)}{N^2}, \qquad \text{Var}[Y] = \frac{(TP + FP)(FN + TN)}{N^2}
$$
8. Multiply the two variances. The four factors are exactly those in phi's bottom, and the square root of $N^4$ is $N^2$:
$$
\sqrt{\text{Var}[X]\,\text{Var}[Y]} = \frac{\sqrt{(TP + FN)(FP + TN)(TP + FP)(FN + TN)}}{N^2}
$$
9. Divide step 6 by step 8. The $N^2$ cancels:
$$
\phi = \frac{TP \cdot TN - FP \cdot FN}{\sqrt{(TP + FP)(TP + FN)(TN + FP)(TN + FN)}}
$$
This is Rao and Callison-Burch's Eq. (4).

**To redo it on new numbers.**

1. Fill the 2 by 2 table and read off TP, FN, FP, TN.
2. Compute the top, $TP \cdot TN - FP \cdot FN$.
3. Compute the four margins: the reviewer's passes and fails, the judge's passes and fails. Multiply them and take the square root.
4. Divide. If the bottom is zero, stop: phi is undefined (next section).

## Where it goes wrong

Navigation: ⬅️ [[#The method in numbered steps]] | 📋 [[#Table of contents]] | [[#Check it two ways]] ➡️

**A column that never changes has no correlation.** Take a judge that passes all 20 products while the reviewer still passes 17: TP = 17, FN = 0, FP = 3, TN = 0.

- $E[Y] = 1$, so $\text{Var}[Y] = 1 \cdot (1 - 1) = 0$.
- The bottom of phi has the factor $TN + FN = 0 + 0 = 0$, so it is $\sqrt{20 \cdot 17 \cdot 3 \cdot 0} = 0$.
- The top is $17 \cdot 0 - 3 \cdot 0 = 0$.
- So phi is $0 / 0$, undefined. Python's `statistics.correlation` stops with the message "at least one of the inputs is constant".

**Kappa on the same table is $0$.** The observed agreement is $\frac{17 + 0}{20} = 0.85$. The expected agreement, from a reviewer who passes 17 of 20 and a judge who passes all 20, is $0.85 \cdot 1 + 0.15 \cdot 0 = 0.85$. Kappa is $\frac{0.85 - 0.85}{1 - 0.85} = 0$. So a judge that passes everything has kappa $0$ and phi undefined, and the two numbers do not disagree: phi has no answer to give.

## Check it two ways

Navigation: ⬅️ [[#Where it goes wrong]] | 📋 [[#Table of contents]] | [[#Other ways]] ➡️

**By hand.** The worked example gives $0.3267$ by covariance and by counts, and the two rows above agree.

**Try it yourself.** The script computes phi by the count formula, by covariance over the Bernoulli variances, and with the standard library's Pearson correlation on 20 rows.

1. What you need: Python 3.10 or later (`statistics.correlation` arrived in 3.10). Check with `python3 --version`. You should see a line such as `Python 3.12.14`.
2. If it is missing: install Python 3 from python.org, or with `uv python install 3.12`. Not run on this machine, which already has it.
3. Setup:

```bash
mkdir correlation_demo && cd correlation_demo
```

4. Save this as `corr.py`:

```python
import statistics
from math import sqrt

TP, FN, FP, TN = 16, 1, 2, 1
# one row per product: (reviewer verdict, judge verdict), 1 = pass, 0 = fail
rows = [(1, 1)] * TP + [(1, 0)] * FN + [(0, 1)] * FP + [(0, 0)] * TN
x = [r for r, j in rows]
y = [j for r, j in rows]
N = len(rows)

# Route 1: the count formula
top = TP * TN - FP * FN
bottom = sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
phi_counts = top / bottom
print(f"counts:      top {top}, bottom {bottom:.4f}, phi {phi_counts:.6f}")

# Route 2: covariance divided by the two standard deviations
p_x = sum(x) / N
p_y = sum(y) / N
e_xy = sum(a * b for a, b in rows) / N
cov = e_xy - p_x * p_y
var_x = p_x * (1 - p_x)
var_y = p_y * (1 - p_y)
phi_cov = cov / sqrt(var_x * var_y)
print(f"covariance:  E[X] {p_x:.2f}, E[Y] {p_y:.2f}, E[XY] {e_xy:.2f}, Cov {cov:.4f}")
print(f"             Var X {var_x:.4f}, Var Y {var_y:.4f}, phi {phi_cov:.6f}")

# Route 3: the standard library's Pearson correlation on the two columns
phi_lib = statistics.correlation(x, y)
print(f"stdlib:      phi {phi_lib:.6f}")
print(f"agree to 12 decimals: {abs(phi_counts - phi_cov) < 1e-12 and abs(phi_counts - phi_lib) < 1e-12}")

# Failure: a judge that passes all 20 products (reviewer still passes 17)
TP, FN, FP, TN = 17, 0, 3, 0
y_all = [1] * 20
x_rev = [1] * 17 + [0] * 3
print()
print(f"pass-everything judge: Var Y = {1.0 * (1 - 1.0)}, bottom = {sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))}")
try:
    statistics.correlation(x_rev, y_all)
except statistics.StatisticsError as error:
    print(f"statistics.correlation raised: {error}")
p_o = (TP + TN) / 20
p_e = (17 / 20) * (20 / 20) + (3 / 20) * (0 / 20)
print(f"kappa for the same table: p_o {p_o:.2f}, p_e {p_e:.2f}, kappa {(p_o - p_e) / (1 - p_e):.4f}")
```

5. Run it:

```bash
python3 corr.py
```

You should see:

```text
counts:      top 14, bottom 42.8486, phi 0.326732
covariance:  E[X] 0.85, E[Y] 0.90, E[XY] 0.80, Cov 0.0350
             Var X 0.1275, Var Y 0.0900, phi 0.326732
stdlib:      phi 0.326732
agree to 12 decimals: True

pass-everything judge: Var Y = 0.0, bottom = 0.0
statistics.correlation raised: at least one of the inputs is constant
kappa for the same table: p_o 0.85, p_e 0.85, kappa 0.0000
```

6. Clean up, and prove it is gone by running the listing again:

```bash
cd .. && rm -r correlation_demo && ls correlation_demo
```

```text
ls: correlation_demo: No such file or directory
```

**Reading the output.**

| Field | Value in this run | How to read it | Backing |
|---|---|---|---|
| `counts` top, bottom, phi | 14, 42.8486, 0.326732 | the count formula, step 9 | derived |
| `E[X]`, `E[Y]`, `E[XY]` | 0.85, 0.90, 0.80 | steps 1 to 3 | derived |
| `Cov` | 0.0350 | $E[XY] - E[X]E[Y]$, which is $14 / 400$ from step 6 | derived |
| `Var X`, `Var Y` | 0.1275, 0.0900 | $p(1-p)$ for each column | cited, p. 154 |
| `covariance` phi | 0.326732 | covariance over the square root of the variances' product | derived |
| `stdlib` phi | 0.326732 | Pearson's $r$ computed on the 20 rows | shown |
| `agree to 12 decimals` | True | the three routes are one number | shown |
| `pass-everything judge` | Var Y = 0.0, bottom = 0.0 | the zero in the failure case | shown |
| `statistics.correlation raised` | the constant-input message | no value is returned | shown |
| `kappa for the same table` | 0.0000 | kappa does not need a spread in the judge's column | shown |

## Other ways

Navigation: ⬅️ [[#Check it two ways]] | 📋 [[#Table of contents]] | [[#Taught in, applied in]] ➡️

**Other agreement scores.** Cohen's kappa asks the same question with a correction for the two pass rates, taught in [[Phi And Q]] and [[Chance-Corrected Agreement]]. **Continuous columns.** For numbers that are not yes-or-no, the textbook's $\rho$ in this note is Pearson's $r$ unchanged, and Spearman and Kendall rank-based versions differ from it; Rao and Callison-Burch's Table 4 lists which to use for which kind of judgment, and this note does not teach them.

## Taught in, applied in

Navigation: ⬅️ [[#Other ways]] | 📋 [[#Table of contents]] | [[#How this was checked]] ➡️

**Taught in.**

- [Step 5 of the worked example for validating an LLM judge](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/drips/combine-validating-an-llm-judge/checks/worked-example-latex.md#step-5-raos-identity-kappa--q-times-phi), which states phi's formula and leaves its derivation out.
- [Rao and Callison-Burch, section 4.1](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/sources/agreement-metrics-for-llm-judges/paper/2606.00093.pdf#page=5), the proof that the five coefficients coincide on binary verdicts (PDF pages 4 and 5).

**Applied in.**

- [[Phi And Q]]: phi as the first factor in kappa, on a judge and a reviewer who each pass or fail 20 products.
- [[Chance-Corrected Agreement#phi]]: the summary of the same number on the same table.

## How this was checked

Navigation: ⬅️ [[#Taught in, applied in]] | 📋 [[#Table of contents]] | [[#Videos]] ➡️

> [!note]- How this was checked
> `corr.py` was run on 2026-10-18 on a Mac with Python 3.12.14, standard library only, from an empty folder that was removed afterwards, the listing then failing as shown. A rerun gave the same output. The prepared environment `~/.vault-sandbox` is missing on this machine and was not needed. The textbook's PDF pages 154, 274, 278 and 279 were opened and read as text: page 154 proves $\text{Var}[X] = p(1-p)$, page 278 defines covariance and proves $\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$, page 279 defines the correlation coefficient, and page 274 explains why the joint expectation is the product. Rao and Callison-Burch's section 4.1 was read on PDF page 5 (Eq. 3 to 6). The page has not been rendered in Obsidian. No claim is marked stated. The reviewer and judge verdicts are invented; none of it is a measurement of any real judge. The Where to learn this card at the end of the note was checked on 2026-10-24: each textbook range was read with pdftotext, the first StatQuest row was copied from the video lessons index, the TileStats and StatQuest covariance chapter lists were read with cache-video-chapters.py and described from their chapter titles only, and the plan was read at its title and description.

## Videos

Navigation: ⬅️ [[#How this was checked]] | 📋 [[#Table of contents]]

<!-- video-table: correlation-coefficient rev=1 -->
Mahesh Huddar, then StatQuest, on Pearson's correlation (covariance over the two standard deviations), in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Correlation runs from minus 1 to 1: perfect positive, perfect negative, and no linear relationship at 0 | Intuition | [Mahesh Huddar, How to find the coefficient of correlation, 0:31 to 2:23](https://www.youtube.com/watch?v=bXlYuKFGsZY&t=31s) |
| 2 | Four data points: the two means, the covariance, both variances, and r = covariance over root variance times root variance, which comes out 0 | Worked example | [Mahesh Huddar, How to find the coefficient of correlation, 2:23 to 6:10](https://www.youtube.com/watch?v=bXlYuKFGsZY&t=143s) |
| 3 | The denominator squeezes covariance into minus 1 to 1; covariance 116 with variances 101.8 and 160.3 gives 0.9 | Worked example | [StatQuest, Pearson's Correlation, Clearly Explained, 13:37 to 16:04](https://www.youtube.com/watch?v=xZ_z8KWkhXE&t=817s) |

Mahesh Huddar's example ends at 0, so it shows the arithmetic but not a strong relationship; StatQuest supplies the nonzero answer and assumes his variance and covariance videos. Neither proves that r stays between minus 1 and 1. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

<!-- video-table: phi-matthews-correlation rev=1 -->
Pedram Jahangiry, from the open web, on the Matthews correlation coefficient of a confusion matrix, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The coefficient is the correlation between actual and predicted: true positive times true negative minus false positive times false negative, over the square root of the four pair sums; it runs from minus 1 to 1 | Intuition, open web | [Jahangiry, Performance metrics for classification models, 16:22 to 18:24](https://www.youtube.com/watch?v=IDPmX6xT3Us&t=982s) |
| 2 | 100 cases with 2 defaulters and a model that always says no default: accuracy 98 percent, precision, recall and F1 all 0, and the coefficient read as 0 | Worked example, open web | [Jahangiry, Performance metrics for classification models, 18:54 to 20:30](https://www.youtube.com/watch?v=IDPmX6xT3Us&t=1134s) |

Nothing on Mahesh Huddar's channel covers the phi or Matthews coefficient, and no video on a listed creator does. The example skips the arithmetic of the denominator: with that table it is 0, so the coefficient is undefined and conventionally set to 0. He does not name the phi coefficient, which is the same quantity for any two yes-or-no columns. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## Where to learn this

**Correlation coefficient**, covariance divided by the product of the two standard deviations, so it runs from −1 to 1. Also: correlation, Pearson correlation, Pearson's r, correlation matrix.

**Textbooks**

- Introduction to probability for data science, sections 5.2.2 to 5.2.3: [pages 279 to 281](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=279). Defines ρ as covariance over the root of the two variances (Definition 5.13), reads it as the cosine of an angle so it stays between −1 and 1, relates it to independence (Theorem 5.5), and computes it in MATLAB and Python.
- Mathematics for machine learning, section 6.4.1: [page 197](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=197). Correlation as the normalised covariance (Definition 6.8), with a figure of positively and negatively correlated data.
- Probabilistic machine learning: an introduction, section 3.1.2: [pages 102 to 103](../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=102). The Pearson correlation, a figure of point clouds with their ρ showing it measures linearity and not slope, the correlation matrix, and spurious correlation between unrelated series.

**Videos**

- StatQuest, Pearson's Correlation, Clearly Explained, 13:37 to 16:04: [watch](https://www.youtube.com/watch?v=xZ_z8KWkhXE&t=817s). Squeezes a covariance of 116 with variances 101.8 and 160.3 into a correlation of 0.9. Caption-read, from the video lessons index.
- TileStats, Correlation: the basics, The Pearson correlation coefficient, 3:54 to 8:23: [watch](https://www.youtube.com/watch?v=SHlHqWYbs2w&t=234s). The Pearson correlation coefficient and its formula. Chapter-timed.
- TileStats, Correlation: the basics, How to interpret the coefficient, 8:23 to 12:40: [watch](https://www.youtube.com/watch?v=SHlHqWYbs2w&t=503s). What a given value of r does and does not say about the data. Chapter-timed.
- StatQuest, Covariance, Clearly Explained, Motivation for Correlation, 20:31 to 21:20: [watch](https://www.youtube.com/watch?v=qtaqvPAeEJY&t=1231s). Why covariance needs rescaling before two relationships can be compared. Chapter-timed.

**Our plans and chapters**

- [Compute correlation, and derive phi for two yes-or-no columns](/home/molef/goal-setting/learning/ai-engineering/agent-evaluation/validating-an-llm-judge/plans/q-times-phi-foundations/plans/02-the-correlation-coefficient.md), ai-engineering/agent-evaluation/validating-an-llm-judge, q-times-phi-foundations plan 02. Computes the correlation of a reviewer's and a judge's verdicts, then derives phi as its count formula.
