---
aliases: [sums of independent Gaussians, sum of independent Gaussians, sum of independent normals, sum of two Gaussians, Gaussian plus Gaussian, adding independent Gaussian noises, independent Gaussian noises add their variances, variances add, variance of a sum, variance of a weighted sum, variance of a linear combination, linear combination of independent Gaussians, "Var(a e_1 + b e_2) = a^2 + b^2", "sqrt(a^2 + b^2) eps", standard deviations do not add, merging two noises into one draw, cross term, Bienayme formula]
sources:
  - "Deisenroth, Faisal, Ong, Mathematics for Machine Learning, Cambridge University Press 2020, section 6.4.5: https://mml-book.github.io/"
  - "Chan, Introduction to Probability for Data Science, Michigan Publishing 2021, Theorems 5.4 and 5.12: https://probability4datascience.com/"
  - "Ho, Jain, Abbeel, Denoising Diffusion Probabilistic Models, NeurIPS 2020: https://arxiv.org/abs/2006.11239"
---

# Sums Of Independent Gaussians

Up: [[Multivariate Normal Distribution]] · ⬅️ [[Sampling A Diagonal Gaussian]] · [[Products And Quotients Of Diagonal Gaussians]] ➡️

Mathematics, Statistics, Distributions, Multivariate Normal Distribution. Needs: [[Sampling A Diagonal Gaussian]] for what one scaled draw $\sqrt{v}\,\varepsilon$ is.

> [!question] Test yourself
> [The diagonal Gaussian quiz](https://claude.ai/artifact/Vmd1FBg7oWwZq1onu9Jofa) covers the [[Multivariate Normal Distribution]] folder. This note's sections are not in it yet.

> [!warning] Unfinished
> - The NumPy scripts in [[#Try the rule yourself]] were not run: this note was written on the cluster, where the prepared environment `~/.vault-sandbox/bin/python` does not exist. Steps 4 to 8 each wait for their output and its rendered picture; only step 8's `exact_sums.py`, which needs the standard library alone, has run. The first machine that has the environment runs them and fills [[#Reading the sums output]].
> - Prompts 12, 13 and 14 (the form, the mechanism, the deep-dive sheet) are waiting to be drawn, in the vault's `.prompts/Multivariate Normal Distribution.md`. The deep-dive sheet's run pane waits for the sandbox output too.

Stated claims in this note: 2, each marked *stated* where it sits.

**Independent Gaussian noises add their variances**, also the variance of a sum or the sum of independent normals: if $e_1$ and $e_2$ are independent draws from $\mathcal{N}(0, 1)$ and $a$, $b$ are fixed numbers, then $Z = a\,e_1 + b\,e_2$ is Gaussian with mean 0 and variance $a^2 + b^2$, so it can be replaced by one draw, $\sqrt{a^2 + b^2}\;\varepsilon$ with $\varepsilon \sim \mathcal{N}(0, 1)$. The variances add, and the [standard deviations](../../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=150) do not: $a = 3$, $b = 4$ gives variance 25 and standard deviation 5, where adding the standard deviations would give 7. *Derived* in [[#How the rule works]].

## Where you work

The setup is in [[Multivariate Normal Distribution#Where you work]]: any terminal with Python 3, and a new empty folder. The scripts below run through the prepared environment, `~/.vault-sandbox/bin/python`, which holds NumPy.

## Table of contents

- [[#When to reach for the rule]]
- [[#The form of the rule]]
- [[#Try the rule yourself]]
- [[#Reading the sums output]]
- [[#How the rule works]]
- [[#Other ways to combine noises]]
- [[#Why the rule matters]]
- [[#The rule taught in, applied in]]

## When to reach for the rule

Navigation: 📋 [[#Table of contents|TOC]] | [[#The form of the rule]] ➡️

When two or more independent noises land on the same number and you want to know how spread out the total is, or want to draw it once instead of several times. The diffusion forward process is the case that matters here: each small step adds fresh noise, and collapsing two steps into one leaves $\sqrt{\alpha_2(1 - \alpha_1)}\,e_1 + \sqrt{1 - \alpha_2}\,e_2$, which this rule turns into a single draw of variance $1 - \alpha_1\alpha_2$.

Without the rule, the natural guess is to add the coefficients, $\sqrt{0.08} + \sqrt{0.2} = 0.730056$, and call that the standard deviation. That number is right only when the two noises are the same draw. For fresh draws the standard deviation is $\sqrt{0.28} = 0.529150$, so the guess overstates the spread by 38%.

## The form of the rule

Navigation: ⬅️ [[#When to reach for the rule]] | 📋 [[#Table of contents|TOC]] | [[#Try the rule yourself]] ➡️

```text
Z   = a * e_1 + b * e_2            e_1, e_2 ~ N(0, 1), drawn independently; a, b fixed numbers
Var(Z) = a^2 + b^2                  square each weight, then add; never add the weights
Z   ~ sqrt(a^2 + b^2) * eps         one draw eps ~ N(0, 1) does the work of two
in R^d, e_k ~ N(0, I):  Cov(Z) = (a^2 + b^2) I
```

**Independent**, the word the rule rests on, means $e_2$ is drawn knowing nothing of $e_1$. In words: the square of the sum's spread is the sum of the squared spreads, because the cross term averages to zero. Make independence false by reusing the draw, $e_2 = e_1$, and on the forward-process numbers the variance goes from 0.28 to 0.532982.

*🖼️ Diagram wanted: the form, two weighted noise bells, a and b, squared into two variance bars that stack into one bar of height a² + b², beside the wrong route where the weights are stacked first. Prompt 12 in the vault's `.prompts/Multivariate Normal Distribution.md`.*

## Try the rule yourself

Navigation: ⬅️ [[#The form of the rule]] | 📋 [[#Table of contents|TOC]] | [[#Reading the sums output]] ➡️

The forward-process numbers run through every step: $\alpha_1 = 0.9$, $\alpha_2 = 0.8$, so $a = \sqrt{0.8 \times 0.1} = \sqrt{0.08}$ and $b = \sqrt{1 - 0.8} = \sqrt{0.2}$. Every script draws one million values from a seeded generator.

**1. What you need, and the check.**

```bash
~/.vault-sandbox/bin/python -c "import numpy; print(numpy.__version__)"
```

You should see a version number.

**2. When it is missing.** Make the environment once on this machine, by hand:

```bash
uv venv ~/.vault-sandbox
uv pip install --python ~/.vault-sandbox/bin/python pandas numpy scipy matplotlib statsmodels openpyxl
```

**3. Make an empty folder and work in it.**

```bash
mkdir -p ~/playground/sandbox/sum-of-gaussians && cd ~/playground/sandbox/sum-of-gaussians
```

**4. A look before: two fresh draws.** Save this as `look.py`. It prints each draw's mean and variance and the average of their product, the cross term's expectation:

```python
import numpy as np

rng = np.random.default_rng(0)
N = 1_000_000
e1 = rng.standard_normal(N)
e2 = rng.standard_normal(N)
print("e1: mean", round(float(e1.mean()), 3), "var", round(float(e1.var()), 3))
print("e2: mean", round(float(e2.mean()), 3), "var", round(float(e2.var()), 3))
print("average of e1 * e2:", round(float((e1 * e2).mean()), 3))
```

```bash
~/.vault-sandbox/bin/python look.py
```

Not run on this machine; the output is owed. The closed form says each mean is near 0, each variance near 1, and the average product near 0, each within about 0.003 for a million draws (derived: the standard error of a mean of a million unit-variance values is $1/\sqrt{10^6} = 0.001$).

**5. The failure: the second noise reuses the first.** Save this as `reused.py`:

```python
import numpy as np

rng = np.random.default_rng(0)
N = 1_000_000
a, b = np.sqrt(0.8 * 0.1), np.sqrt(1 - 0.8)
e1 = rng.standard_normal(N)
z = a * e1 + b * e1
print("e2 = e1:  var", round(float(z.var()), 4), "| a^2 + b^2", round(a**2 + b**2, 4), "| (a + b)^2", round((a + b) ** 2, 4))
```

```bash
~/.vault-sandbox/bin/python reused.py
```

Not run on this machine; the output is owed. The closed form says the measured variance sits near $(a + b)^2 = 0.5330$, not near $a^2 + b^2 = 0.28$, within about 0.002 (derived: the standard error of a sample variance is about $\sigma^2\sqrt{2/N} = 0.000754$ here).

**6. The technique: a fresh second noise.** Save this as `fresh.py`:

```python
import numpy as np

rng = np.random.default_rng(0)
N = 1_000_000
a, b = np.sqrt(0.8 * 0.1), np.sqrt(1 - 0.8)
e1 = rng.standard_normal(N)
e2 = rng.standard_normal(N)
z = a * e1 + b * e2
print("fresh e2: var", round(float(z.var()), 4), "| a^2 + b^2", round(a**2 + b**2, 4), "| 1 - alpha_1 alpha_2", round(1 - 0.9 * 0.8, 4))
```

```bash
~/.vault-sandbox/bin/python fresh.py
```

Not run on this machine; the output is owed. The closed form says the measured variance sits near 0.28, within about 0.001 (derived: $0.28\sqrt{2/10^6} = 0.000396$), and the last two fields print `0.28` exactly.

**7. Another way to get the same answer: one draw.** Save this as `one_draw.py`. It compares the two-draw sum with one draw scaled by $\sqrt{a^2 + b^2}$, quantile by quantile, so the shapes are compared as well as the variances:

```python
import numpy as np

rng = np.random.default_rng(0)
N = 1_000_000
a, b = np.sqrt(0.08), np.sqrt(0.2)
two = a * rng.standard_normal(N) + b * rng.standard_normal(N)
one = np.sqrt(a**2 + b**2) * rng.standard_normal(N)
q = [0.05, 0.25, 0.5, 0.75, 0.95]
print("two draws, quantiles", np.round(np.quantile(two, q), 3).tolist())
print("one draw,  quantiles", np.round(np.quantile(one, q), 3).tolist())
```

```bash
~/.vault-sandbox/bin/python one_draw.py
```

Not run on this machine; the output is owed. Both lines should sit near the quantiles of $\mathcal{N}(0, 0.28)$: $-0.870$, $-0.357$, $0$, $0.357$, $0.870$ (computed by the writer with Python's `statistics.NormalDist(0, 0.28 ** 0.5).inv_cdf`).

**8. More worked examples on the same setup.** Save this as `more.py`. It runs the two hand examples, equal weights and the 3-4-5 case, and prints each variance beside $a^2 + b^2$ and each standard deviation beside the wrong guess $a + b$:

```python
import numpy as np

rng = np.random.default_rng(0)
N = 1_000_000
for a, b in [(1.0, 1.0), (3.0, 4.0)]:
    z = a * rng.standard_normal(N) + b * rng.standard_normal(N)
    print(f"a {a} b {b}: var {z.var():.3f} (a^2 + b^2 = {a * a + b * b}), std {z.std():.3f} (a + b = {a + b})")
```

```bash
~/.vault-sandbox/bin/python more.py
```

Not run on this machine; the output is owed. The closed form says the first line sits near variance 2 and standard deviation 1.414, against $a + b = 2$, and the second near variance 25 and standard deviation 5, against $a + b = 7$.

Then one by hand, before running anything: two forward steps with $\alpha_1 = 0.95$ and $\alpha_2 = 0.7$. Compute the noise variance both ways, $\alpha_2(1 - \alpha_1) + (1 - \alpha_2)$ and $1 - \alpha_1\alpha_2$.

> [!example]- The answer
> $0.7 \times 0.05 + 0.3 = 0.035 + 0.3 = 0.335$, and $1 - 0.95 \times 0.7 = 1 - 0.665 = 0.335$. To check it with the sandbox, add `(np.sqrt(0.7 * 0.05), np.sqrt(1 - 0.7))` to the list in `more.py`; its variance should sit near 0.335.

Then the rule with no sampling at all. Save this as `exact_sums.py`. It needs only the standard library, so `python3` runs it where the prepared environment is missing. It lists every equally likely outcome and averages over them, so each number is exact: two independent $\pm 1$ coins, the same coin used twice ($Y = X$), and the noise scales of the 100-step cosine schedule at $t = 25$ and $t = 50$ applied to two independent four-value draws ($\pm\sqrt{1.5}$, $\pm\sqrt{0.5}$, each a quarter of the time, mean 0 and mean square 1):

```python
from itertools import product
from math import sqrt
from statistics import fmean

coin = [1.0, -1.0]
pairs = list(product(coin, coin))                     # four equally likely outcomes
print("sums", [x + y for x, y in pairs], "squares", [(x + y) ** 2 for x, y in pairs], "mean", fmean([(x + y) ** 2 for x, y in pairs]))
print("cross products", [x * y for x, y in pairs], "average", fmean([x * y for x, y in pairs]))
print("Y = X: X + Y is", [2 * x for x in coin], "variance", fmean([(2 * x) ** 2 for x in coin]), "cross term", fmean([x * x for x in coin]))

four = [sqrt(1.5), -sqrt(1.5), sqrt(0.5), -sqrt(0.5)]  # each a quarter of the time: mean 0, mean square 1
a, b = 0.4054, 0.7223                                  # noise scales at t = 25 and t = 50
z = [a * u + b * v for u, v in product(four, four)]   # sixteen equally likely outcomes
var = fmean([v * v for v in z])
print(f"mean {fmean(z):.4f}  variance {var:.4f}  a^2 + b^2 {a * a + b * b:.4f}  typical miss {sqrt(var):.4f}  a + b {a + b:.4f}")
```

```bash
python3 exact_sums.py
```

![Two coins: sums 2, 0, 0, -2 with mean square 2 and cross products averaging 0; the same coin twice gives variance 4 and cross term 1; the schedule noises 0.4054 and 0.7223 give variance 0.6861 and typical miss 0.8283, against 1.1277 for the added scales|1000](assets/sums-exact-coins-and-schedule-noises.png)

**9. Clean up, and prove it.**

```bash
cd ~ && rm -r ~/playground/sandbox/sum-of-gaussians
ls ~/playground/sandbox/sum-of-gaussians; echo $?
```

You should see `No such file or directory`, then `2`.

## Reading the sums output

Navigation: ⬅️ [[#Try the rule yourself]] | 📋 [[#Table of contents|TOC]] | [[#How the rule works]] ➡️

The "This run" column is empty until the sandbox runs. The value each field should sit near is derived below.

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | step 4, average of `e1 * e2` | owed | the cross term's expectation; near 0 because the draws are independent | derived below |
| 2 | step 5, `e2 = e1: var` | owed | near 0.5330: reusing the draw puts the cross term $2ab = 0.252982$ back | derived below |
| 3 | step 6, `fresh e2: var` | owed | near 0.28: the cross term is gone and the variances add | derived below |
| 4 | step 6, `1 - alpha_1 alpha_2` | owed | `0.28`, the one-jump variance; equal to field 3's closed form for any two alphas | derived below |
| 5 | step 7, both quantile lines | owed | the same five numbers to about two decimals: one scaled draw has the same distribution as the two-draw sum | cited below (the shape step) |
| 6 | step 8, `std` beside `a + b` | owed | near 1.414 against 2, and near 5 against 7: standard deviations do not add | derived below |

From `exact_sums.py`, which ran, numbered as on its picture:

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | coins, mean of the squared sums | `2.0` | the sums 2, 0, 0, $-2$ square to 4, 0, 0, 4; the mean is 0, so their average is the variance, $2 = 1 + 1$ | shown |
| 2 | cross products, average | `0.0` | $xy$ is $+1$ on two outcomes and $-1$ on two, so the cross term of step 3 below averages to 0 | shown |
| 3 | Y = X, variance | `4.0` | $X + X = 2X$, and the scaling rule in [[Variance#Scaling a draw scales its variance by the square]] gives $2^2 \times 1 = 4$, not 2 | derived below |
| 4 | Y = X, cross term | `1.0` | $x \cdot x = 1$ on both faces: the cross term no longer cancels, and $1 + 2 \times 1 + 1 = 4$ | derived below |
| 5 | schedule noises, variance | `0.6861` | $0.4054^2 + 0.7223^2 = 0.1644 + 0.5217$, exact over the sixteen outcomes even though the draws are not Gaussian | derived below |
| 6 | typical miss | `0.8283` | $\sqrt{0.6861}$, the standard deviation of the sum | shown |
| 7 | a + b | `1.1277` | the wrong route, adding the typical misses; it overstates 0.8283 by 36% | shown |

## How the rule works

Navigation: ⬅️ [[#Reading the sums output]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to combine noises]] ➡️

Textbook: [mathematics for machine learning, section 6.4.5, p. 200](../../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=200) for $V[x + y] = V[x] + V[y]$ when $x$ and $y$ are independent, and [probability for data science, Theorem 5.12, p. 299](../../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=299) for the sum of two Gaussians being Gaussian.

Set up the sum with $a$, $b$ fixed and $e_1$, $e_2$ independent standard normals, $Z = a\,e_1 + b\,e_2$. Five steps give its variance.

1. The mean. By [linearity of expectation](../../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=66), and each $e_k$ has mean 0:

   $$\mathbb{E}[Z] = a\,\mathbb{E}[e_1] + b\,\mathbb{E}[e_2] = 0$$

2. Square the sum:

   $$Z^2 = a^2 e_1^2 + 2ab\,e_1 e_2 + b^2 e_2^2$$

3. Take the expectation term by term, linearity again:

   $$\mathbb{E}[Z^2] = a^2\,\mathbb{E}[e_1^2] + 2ab\,\mathbb{E}[e_1 e_2] + b^2\,\mathbb{E}[e_2^2]$$

4. A standard normal has mean 0 and variance 1, so its second moment is $\mathbb{E}[e_k^2] = 1$. For independent variables [the expectation of a product is the product of the expectations](../../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=280), so the cross term vanishes:

   $$\mathbb{E}[e_1 e_2] = \mathbb{E}[e_1]\,\mathbb{E}[e_2] = 0 \times 0 = 0$$

5. [The variance is the second moment minus the squared mean](../../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=200):

   $$\operatorname{Var}(Z) = \mathbb{E}[Z^2] - (\mathbb{E}[Z])^2 = a^2 + b^2 - 0 = a^2 + b^2$$

$$\boxed{\operatorname{Var}(a\,e_1 + b\,e_2) = a^2 + b^2}$$

In $\mathbb{R}^d$ with spherical noise, $e_k \sim \mathcal{N}(0, I)$, the same five steps run coordinate by coordinate, and the cross term between two different coordinates vanishes for the same reason, so the covariance is $a^2 I + b^2 I = (a^2 + b^2) I$. *Derived.*

**The shape is a separate step.** The five steps give the variance of any sum of independent zero-mean, unit-variance draws, Gaussian or not. That the sum is still a bell, so one draw $\sqrt{a^2 + b^2}\,\varepsilon$ can replace it, needs Gaussian inputs: the [chapter 9.1](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/09-the-forward-process-by-hand.md#91-independent-gaussian-noises-add-their-variances) derivation does it in steps 5 to 7 with the [[Moment Generating Function#What the fingerprint is|moment generating function]], $\mathbb{E}[e^{\lambda e_1}] = e^{\lambda^2/2}$ by [completing the square](../../../references/textbooks/algebra/algebra-handbook.pdf#page=74) in the exponent, and the textbook's Theorem 5.12 does it by convolution. *Derived* in [[Moment Generating Function#The fingerprint of a sum is the product]]; *cited:* Theorem 5.12, in the textbook line above.

Two independent coin flips that land on $+1$ or $-1$ show where the two rules part. Their sum has variance $1 + 1 = 2$, as the five steps say, but it only takes the values $-2$, $0$ and $2$, so it is not $\mathcal{N}(0, 2)$. Its moment generating function at $\lambda = 1$ is $\cosh(1)^2 = 2.381098$, against $e^{1} = 2.718282$ for $\mathcal{N}(0, 2)$, run in [[Moment Generating Function#Where variance cannot tell two shapes apart]]. Variances add for any independent inputs, and the one-draw replacement holds only when the inputs are Gaussian.

### Why independence kills the cross term

The whole rule hangs on step 4. If the second noise reuses the first, $e_2 = e_1$, then $\mathbb{E}[e_1 e_2] = \mathbb{E}[e_1^2] = 1$, the cross term stays at $2ab$, and

$$\operatorname{Var}\big((a + b)\,e_1\big) = (a + b)^2 = a^2 + b^2 + 2ab$$

so the standard deviations add instead of the variances.

**The worked numbers.**

$$
\begin{aligned}
a = b = 1:&\quad \operatorname{Var} = 1 + 1 = 2, & \text{std } &\sqrt{2} = 1.414214, \text{ not } 2 \\
a = 3,\ b = 4:&\quad \operatorname{Var} = 9 + 16 = 25, & \text{std } &5, \text{ not } 7 \\
a = 0.4054,\ b = 0.7223:&\quad \operatorname{Var} = 0.1644 + 0.5217 = 0.6861, & \text{std } &\sqrt{0.6861} = 0.8283, \text{ not } 1.1277 \\
\alpha_1 = 0.9,\ \alpha_2 = 0.8:&\quad a^2 = 0.8 \times 0.1 = 0.08, & b^2 &= 1 - 0.8 = 0.2, \quad a^2 + b^2 = 0.28 \\
\text{one jump}:&\quad 1 - \alpha_1\alpha_2 = 1 - 0.72 = 0.28 \\
e_2 = e_1:&\quad 2ab = 2\sqrt{0.08}\sqrt{0.2} = 0.252982, & (a + b)^2 &= 0.28 + 0.252982 = 0.532982 \\
& \quad a + b = 0.282843 + 0.447214 = 0.730056
\end{aligned}
$$

The two forward-process routes agree for any alphas, because $\alpha_2(1 - \alpha_1) + (1 - \alpha_2) = \alpha_2 - \alpha_1\alpha_2 + 1 - \alpha_2 = 1 - \alpha_1\alpha_2$. *Derived;* every number above was recomputed by the writer.

*🖼️ Diagram wanted: the mechanism, the square of the sum laid out as a 2 by 2 grid of a²e₁², ab e₁e₂, ab e₂e₁ and b²e₂², the two off-diagonal cells averaging to zero for fresh draws and staying at ab for a reused draw. Prompt 13 in the vault's `.prompts/Multivariate Normal Distribution.md`.*

*🖼️ Diagram wanted: the deep-dive sheet composing the form, the mechanism and the forward-process worked numbers. Prompt 14 in the vault's `.prompts/Multivariate Normal Distribution.md`.*

## Other ways to combine noises

Navigation: ⬅️ [[#How the rule works]] | 📋 [[#Table of contents|TOC]] | [[#Why the rule matters]] ➡️

- **Correlated noises.** When the draws are not independent, step 4 keeps $\mathbb{E}[e_1 e_2]$, which for unit-variance, zero-mean draws is their [covariance](../../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=278) $\rho$, and the variance is $a^2 + b^2 + 2ab\rho$. Independence is $\rho = 0$, and the reused draw is $\rho = 1$. *Derived* from steps 3 and 4; the textbook's Theorem 5.4 on that page states $\operatorname{Var}[X + Y] = \operatorname{Var}[X] + 2\operatorname{Cov}(X, Y) + \operatorname{Var}[Y]$.
- **Many noises at once.** For $n$ independent unit draws, $\operatorname{Var}\big(\sum_k c_k e_k\big) = \sum_k c_k^2$, by the same steps with every cross term zero. *Derived.* This is the step the forward process repeats when it collapses $t$ steps into one.
- **Unequal variances.** For independent $X \sim \mathcal{N}(\mu_1, \sigma_1^2)$ and $Y \sim \mathcal{N}(\mu_2, \sigma_2^2)$, $X + Y \sim \mathcal{N}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$: write each as its mean plus $\sigma_k e_k$ and the rule applies with $a = \sigma_1$, $b = \sigma_2$. *Cited:* Theorem 5.12, linked in [[#How the rule works]].
- **Sampling instead of algebra.** Draw both noises and measure the variance, as in step 6. It needs no derivation but only agrees to within the sampling error, about $\sigma^2\sqrt{2/N}$.

## Why the rule matters

Navigation: ⬅️ [[#Other ways to combine noises]] | 📋 [[#Table of contents|TOC]] | [[#The rule taught in, applied in]] ➡️

Every step of a diffusion model's forward process adds noise drawn fresh, independent of all earlier draws (*stated*; it is how the process is defined, with $\varepsilon_t$ drawn anew at each step, in Ho et al.'s equation (2)). That independence is what lets $t$ steps collapse into the one-jump form $x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon$ in [[The Forward Process#How the jump works]], where the variance of the noise part is the sum of every step's squared weight. Training draws a noised point at any level in one line because of it.

A sampler or a training loop that reuses a noise draw by mistake still runs and still prints plausible numbers. On the two-step toy the reused draw nearly doubles the noise variance, 0.533 against 0.28, so the clouds come out wider than the schedule says (*stated*; the variance numbers are derived above, the claim that the code still runs is the writer's).

## The rule taught in, applied in

Navigation: ⬅️ [[#Why the rule matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the PoE derivation foundations journey's [chapter 9, section 9.1](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/09-the-forward-process-by-hand.md#91-independent-gaussian-noises-add-their-variances), lines 24 to 128: the statement, the five-step variance derivation, the moment generating function for the shape, worked example 9.1 (two forward steps with $\alpha_1 = 0.9$, $\alpha_2 = 0.8$, both ways 0.28) and the reused-draw failure, walked as piece 1 of 5 of the `drip --math` walk in `artifacts/drips/forward-process-by-hand/`
- the `/drip --math` walk of the forward process and the score in the reduce-reuse-recycle research repository (`artifacts/drips/forward-process-and-the-score/`), piece 1, rung 2: $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$ for independent zero-mean draws, derived by expanding $(X + Y)^2$ and killing $2\,\mathbb{E}[XY]$ by independence; two $\pm 1$ coins with mean square 2 and cross products averaging 0; $Y = X$ giving 4; and $0.4054\,\varepsilon_a + 0.7223\,\varepsilon_b$ with variance 0.6861 and typical miss 0.8283, against 1.1277 for added scales
- the same journey's [plan 09](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/09-the-forward-process.md), instructions 3.1, 3.3 and 3.4 at lines 236 to 264: the video's claim that independent spherical Gaussians combine with covariances adding, the sentence on why two noise terms become one draw, and the 0.28 computed both ways

**Applied in:** nothing yet.

**Used by other notes:** [[The Forward Process#How the jump works]], where the noise part's variance is $1 - \bar\alpha$; [[Kinds Of Composition#Mosaic, blend or two animals from one product]], where noising a pixel's cat and dog turns $\mathcal{N}(\mu, v)$ into $\mathcal{N}(\sqrt{\bar\alpha}\,\mu, \bar\alpha v + 1 - \bar\alpha)$; and [[When Neither Training Set Holds A And B]], where a trained expert's smoothing adds $h^2$ to each ring mode's variance.

> [!note]- How this was checked
> This note was written on 2026-10-20 on the cluster (mscluster, Linux) from piece 1 of the `drip --math` walk of chapter 9. The prepared environment `~/.vault-sandbox/bin/python` does not exist on this machine, so no NumPy sandbox command in this note was run and none carries output. `exact_sums.py` was run on 2026-10-21 by vault-writer with the cluster's Python 3.12.10 and the standard library only, in the empty folder `~/playground/sandbox/sum-of-gaussians`, which was removed afterwards; its picture was rendered from the captured text in DejaVu Sans Mono and opened before filing. Its 0.4054 and 0.7223 are $\sqrt{1 - \bar\alpha_{25}}$ and $\sqrt{1 - \bar\alpha_{50}}$ of the 100-step cosine schedule in `rebuild/out/walk-numbers.json` of the reduce-reuse-recycle repository. Every number in [[#How the rule works]], and every "should sit near" value in the sandbox, was recomputed by the writer with the standard library of the cluster's Python 3.12 (`math.sqrt` and `statistics.NormalDist`), and matches the walk's turn and chapter 9.1. The chapter's answer key, `checks/09_forward_closed_form.py`, is not on this machine.
>
> Each textbook page linked in this note was opened on the cluster with PyMuPDF and read before linking: mathematics for machine learning p. 200 (section 6.4.5, $V[x + y] = V[x] + V[y]$ for independent variables); probability for data science p. 150 (Definition 3.7, the standard deviation), p. 200 (Definition 4.6 and the $E[X^2] - \mu^2$ shortcut), p. 278 (Definition 5.12 and Theorem 5.4, the variance of a sum with its covariance term), p. 280 (the proof that $E[XY] = E[X]E[Y]$ for independent variables) and p. 299 (Theorem 5.12, the sum of two Gaussians); probabilistic machine learning p. 66 (equation 2.25, linearity of expectation); the algebra handbook p. 74 (completing the square). The moment generating function's pages (probability for data science pp. 340 to 345) are linked from [[Moment Generating Function]], which teaches it. The coin-flip numbers 2.381098 and 2.718282 are that note's step 6 output.
>
> The learner's LibreOffice notes are not reachable from the cluster, so none was read for this note.
