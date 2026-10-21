---
aliases: [variance, Var(X), "Var[X]", sigma squared, average squared miss from the mean, standard deviation, scaling rule for variance, scale property of variance, variance of a scaled variable, scaling a random variable, "Var(cX) = c^2 Var(X)", "Var(aX) = a^2 Var(X)", "Var[cX] = c² Var[X]", scaling a draw scales its variance]
sources:
  - "Introduction to Probability for Data Science, Definition 3.7 (variance), Theorem 3.4 (E[cX] = cE[X]), Theorem 3.5 (moment, scale and shift properties of variance) and Theorems 5.4 and 5.5 (the variance of a sum): the vault's shelf copy, Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf, PDF pages 147, 150 to 152, 278 and 279"
  - "Petersen, Pedersen, The Matrix Cookbook, version of 15 November 2012, section 6.2.1, equation (313): https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf"
  - "Wikipedia, Variance: https://en.wikipedia.org/wiki/Variance, read 2026-10-20, CC BY-SA 4.0"
  - "Python documentation, statistics module: https://docs.python.org/3/library/statistics.html, read 2026-10-20"
---

# Variance

Up: [[Statistics]] · [[Scaling And Shifting A Random Variable]] ➡️

Mathematics, Statistics. Needs: the mean of a random variable, its [expectation](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=141), read as a long-run average.

> [!question] Test yourself
> No quiz page covers this note yet.

> [!warning] Unfinished
> - The three drawn pictures for the scaling rule (the form, the mechanism and the deep-dive sheet) are waiting: prompts 1 to 3 in the vault's `.prompts/Variance.md`.
> - No quiz page for this note yet.

Claims marked stated: 0.

**Variance is the average squared miss from the mean, $\operatorname{Var}(X) = \mathbb{E}[(X - \mu)^2]$, and its square root is the standard deviation.** Multiplying a random draw by a fixed number $c$ multiplies its variance by $c^2$ and its standard deviation by $|c|$. That is why a formula that wants noise of variance $v$ multiplies a unit-variance draw by $\sqrt{v}$, never by $v$.

## Where you work

Any terminal with Python 3.8 or later (`statistics.fmean` arrived in 3.8), and a new empty folder. The scripts use the standard library only, so nothing is installed. Every number in them is made up or comes from a public noise schedule.

## Table of contents

- [[#What variance measures]]
- [[#Scaling a draw scales its variance by the square]]
- [[#When to reach for the scaling rule]]
- [[#The form of the scaling rule]]
- [[#Try the scaling rule yourself]]
- [[#Reading the scaled output]]
- [[#How the scaling rule works]]
- [[#Other ways to change a spread]]
- [[#Why the scaling rule matters]]
- [[#The scaling rule taught in, applied in]]

## What variance measures

Navigation: 📋 [[#Table of contents|TOC]] | [[#Scaling a draw scales its variance by the square]] ➡️

Textbook: [Introduction to probability for data science, Definition 3.7, PDF p. 150](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=150) · [the continuous case, Definition 4.6, PDF p. 200](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=200). The book prints page numbers 16 lower (PDF page 150 prints 134).

**Variance**, also $\operatorname{Var}(X)$ or $\sigma^2$, is how far a random draw $X$ lands from its mean $\mu = \mathbb{E}[X]$ on average, measured as the average of the squared miss: $\operatorname{Var}(X) = \mathbb{E}[(X - \mu)^2]$. **Standard deviation**, $\sigma$, is its square root, and is in the same units as $X$. *Cited:* Definition 3.7.

The miss is squared because the plain misses average to nothing: $\mathbb{E}[X - \mu] = \mathbb{E}[X] - \mu = 0$ for every $X$. Squaring makes a miss below the mean count as much as one above it. *Derived* here.

**Worked by hand: a fair coin that pays $+1$ or $-1$.** Each face has probability $\tfrac12$.

$$
\begin{aligned}
\mu &= \tfrac12(+1) + \tfrac12(-1) = 0 \\
\text{misses} &= +1 - 0 = +1, \qquad -1 - 0 = -1 \\
\text{squared misses} &= 1, \qquad 1 \\
\operatorname{Var}(X) &= \tfrac12(1) + \tfrac12(1) = 1, \qquad \sigma = \sqrt{1} = 1
\end{aligned}
$$

A standard normal draw $\varepsilon \sim \mathcal{N}(0, 1)$ has the same two numbers, mean 0 and variance 1, by the definition of $\mathcal{N}(0, 1)$. That is why the coin is a fair stand-in for $\varepsilon$ in the worked examples below: only the mean and the variance enter the scaling rule. *Derived* in [[#How the scaling rule works]], where no step uses the shape of the distribution.

## Scaling a draw scales its variance by the square

Navigation: ⬅️ [[#What variance measures]] | 📋 [[#Table of contents|TOC]] | [[#When to reach for the scaling rule]] ➡️

Textbook: [Introduction to probability for data science, Theorem 3.5 (ii), PDF p. 151](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=151) · [its proof, PDF p. 152](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=152) · [$\mathbb{E}[cX] = c\,\mathbb{E}[X]$, Theorem 3.4, PDF p. 147](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=147).

**Scaling rule for variance**, also the scale property of variance or $\operatorname{Var}(cX) = c^2 \operatorname{Var}(X)$: multiplying a random draw by a fixed number $c$ multiplies its variance by $c^2$ and its standard deviation by $|c|$.

## When to reach for the scaling rule

Navigation: ⬅️ [[#Scaling a draw scales its variance by the square]] | 📋 [[#Table of contents|TOC]] | [[#The form of the scaling rule]] ➡️

Whenever a formula multiplies a random draw by a number and you need the spread of the result, or need the number that gives a wanted spread. The forward process multiplies $\varepsilon$ by $\sqrt{1 - \bar\alpha_t}$ ([[The Forward Process#How the jump works]]). Sampling a Gaussian multiplies it by $\sqrt{\sigma^2}$ ([[Sampling A Diagonal Gaussian#How sampling works]]). An average divides a sum by $N$, which divides its variance by $N^2$.

The slip it prevents is multiplying by the variance you want instead of its square root. That squares the variance a second time, and step 5 below shows it.

## The form of the scaling rule

Navigation: ⬅️ [[#When to reach for the scaling rule]] | 📋 [[#Table of contents|TOC]] | [[#Try the scaling rule yourself]] ➡️

```text
Y = c * X                      c is a fixed number, X a random draw
E[Y]   = c * E[X]              the mean is multiplied by c
Var(Y) = c**2 * Var(X)         the variance is multiplied by c squared
sd(Y)  = abs(c) * sd(X)        the standard deviation is multiplied by |c|
wanted variance v from a draw of variance 1:   c = sqrt(v)
```

*🖼️ Diagram wanted: the form, one unit-variance bell stretched by c into a bell whose width is |c| and whose variance is c². Prompt 1 in the vault's `.prompts/Variance.md`.*

## Try the scaling rule yourself

Navigation: ⬅️ [[#The form of the scaling rule]] | 📋 [[#Table of contents|TOC]] | [[#Reading the scaled output]] ➡️

**1. What you need.** Python 3.8 or later:

```bash
python3 --version
```

You should see a version line. This run printed `Python 3.12.10`.

**2. When it is missing.** Install Python 3 from python.org, or run `uv python install 3.12`. Not run on this machine, which already has it. Where the prepared environment exists, `~/.vault-sandbox/bin/python` runs every script below unchanged.

**3. Make something to act on.** Make an empty folder and go into it:

```bash
mkdir -p ~/playground/sandbox/variance-scaling && cd ~/playground/sandbox/variance-scaling
```

**4. A look before: the coin, then the coin times $c$.** Save this as `coin.py`. The number $c = 0.7223$ is the noise scale at code step $t = 50$ of a 100-step cosine schedule, where the clean point keeps $\bar\alpha_{50} = 0.4783$ of the variance:

```python
from statistics import fmean

def variance(values):
    mean = fmean(values)
    return fmean([(v - mean) ** 2 for v in values])

coin = [1.0, -1.0]          # a fair coin that pays +1 or -1, each face equally likely
c = 0.7223                  # the noise scale at code step t = 50
scaled = [c * v for v in coin]
for name, x in [("coin    ", coin), ("c * coin", scaled)]:
    mean = fmean(x)
    misses = [round((v - mean) ** 2, 4) for v in x]
    print(name, "values", x, "mean", mean, "squared misses", misses, "variance", round(variance(x), 4))
print("c squared", round(c ** 2, 4))
```

Both faces are equally likely, so the plain average over the two faces is the exact expectation.

```bash
python3 coin.py
```

You should see:

![The coin's squared misses are 1 and its variance 1; times c = 0.7223 the squared misses and the variance are both 0.5217, which is c squared|900](assets/variance-coin-scaled-by-c.png)

**5. The failure: multiplying by the variance share instead of its root.** The noise at $t = 50$ should carry the share $1 - \bar\alpha_{50} = 0.5217$ of the variance. Save this as `wrong_share.py`:

```python
from statistics import fmean

def variance(values):
    mean = fmean(values)
    return fmean([(v - mean) ** 2 for v in values])

coin = [1.0, -1.0]
share = 1 - 0.4783          # the noise share of the variance at t = 50
for name, factor in [("the share itself", share), ("its square root ", share ** 0.5)]:
    scaled = [factor * v for v in coin]
    print(f"multiply by {name} {factor:.4f}: variance {variance(scaled):.4f}, wanted {share:.4f}")
```

```bash
python3 wrong_share.py
```

![Multiplying by the share 0.5217 gives variance 0.2722; multiplying by its square root 0.7223 gives the wanted 0.5217|700](assets/variance-the-share-against-its-square-root.png)

Multiplying by the share squares it again, $0.5217^2 = 0.2722$, so the noise carries about half the variance it should.

**6. The technique: scale many standard-normal draws.** Save this as `scaled_normal.py`. It draws 200,000 values of $\varepsilon$ from one seeded generator and scales the same draws by three numbers: $c = 0.7223$, its negative, and $c = \sqrt{\beta_0} = \sqrt{0.000631} = 0.02512$, the noise scale of the schedule's first step:

```python
import random
from statistics import fmean, pvariance, pstdev

rng = random.Random(0)
eps = [rng.gauss(0.0, 1.0) for _ in range(200_000)]
print(f"eps itself:    mean {fmean(eps):+.4f}  variance {pvariance(eps):.6f}")
for c in [0.7223, -0.7223, 0.02512]:
    y = [c * e for e in eps]
    ratio = pvariance(y) / pvariance(eps)
    print(f"c = {c:+.5f}: mean {fmean(y):+.4f}  variance {pvariance(y):.6f}  ratio {ratio:.6f}  c squared {c * c:.6f}  sd {pstdev(y):.5f}  |c| {abs(c):.5f}")
```

```bash
python3 scaled_normal.py
```

You should see:

![200,000 standard-normal draws scaled by 0.7223, by -0.7223 and by 0.02512: each scaled variance over the draws' own variance equals c squared to six places|1000](assets/variance-a-scaled-standard-normal-draw.png)

Run it again and the same four lines come back, because the generator is seeded with 0.

**7. Another way to get the same answer: the moment form.** The variance is also $\mathbb{E}[Y^2] - \mathbb{E}[Y]^2$ (Theorem 3.5 (i) on [PDF p. 151](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=151)). Save this as `moment_form.py`:

```python
import random
from statistics import fmean, pvariance

rng = random.Random(0)
c = 0.7223
y = [c * rng.gauss(0.0, 1.0) for _ in range(200_000)]
print(f"average squared miss  {pvariance(y):.6f}")
print(f"E[Y^2] - E[Y]^2       {fmean([v * v for v in y]) - fmean(y) ** 2:.6f}")
```

```bash
python3 moment_form.py
```

![The average squared miss and the moment form both print 0.520635|420](assets/variance-the-moment-form.png)

The two agree to six places, and both equal step 6's variance for $c = 0.7223$, since the seed and the draws are the same.

**8. More worked examples: two coordinates scaled together.** The forward process noises a 2D point, so $\varepsilon$ has two independent standard-normal coordinates and both are multiplied by the same $c$. Save this as `two_coordinates.py`; its first line scales the walk's toy draw $\varepsilon = (0.3, -1.2)$:

```python
import random
from statistics import fmean

rng = random.Random(1)
c = 0.7223
print("one toy draw:", [round(c * e, 4) for e in (0.3, -1.2)])
pairs = [(rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)) for _ in range(200_000)]
y1 = [c * a for a, b in pairs]
y2 = [c * b for a, b in pairs]
m1, m2 = fmean(y1), fmean(y2)
var1 = fmean([(v - m1) ** 2 for v in y1])
var2 = fmean([(v - m2) ** 2 for v in y2])
cov12 = fmean([(a - m1) * (b - m2) for a, b in zip(y1, y2)])
print(f"covariance matrix of c * eps:  [[{var1:.4f}, {cov12:+.4f}], [{cov12:+.4f}, {var2:.4f}]]")
print(f"c squared times I:             [[{c * c:.4f}, +0.0000], [+0.0000, {c * c:.4f}]]")
```

```bash
python3 two_coordinates.py
```

![The toy draw (0.3, -1.2) becomes (0.2167, -0.8668); the measured covariance matrix of c times eps sits near c squared times the identity|850](assets/variance-two-coordinates-scaled-together.png)

Then the rule at every level of the schedule. Save this as `schedule_levels.py`. It holds five $\bar\alpha_t$ values of the 100-step cosine schedule, draws $c$ and $c^2$ side by side as bars of `#`, scales a four-value draw that is not a coin, repeats step 5's slip at $t = 25$, and scales the toy draw at $t = 25$ and $t = 75$:

```python
from math import sqrt
from statistics import fmean

abar = {0: 0.999369, 25: 0.835621, 50: 0.478265, 75: 0.133495, 99: 0.0}   # the 100-step cosine schedule
for t, a in abar.items():
    c = sqrt(1 - a)
    print(f"t = {t:2d}  c {c:.4f} {'#' * round(30 * c):<30}  c^2 {c * c:.4f} {'#' * round(30 * c * c)}")

c75 = sqrt(1 - abar[75])
four = [sqrt(1.5), -sqrt(1.5), sqrt(0.5), -sqrt(0.5)]   # each a quarter of the time: mean 0, mean square 1
scaled = [c75 * v for v in four]
print("four values times c75:", [round(v, 4) for v in scaled], "squares", [round(v * v, 4) for v in scaled])
print(f"mean {fmean(scaled):.4f}  mean square {fmean([v * v for v in scaled]):.4f}  c75 squared {c75 ** 2:.4f}")

share = 1 - abar[25]
print(f"t = 25, coin times the share {share:.4f}: variance {fmean([(share * v) ** 2 for v in (1.0, -1.0)]):.4f}")

for t in (25, 75):
    c = sqrt(1 - abar[t])
    print(f"t = {t}: toy draw (0.3, -1.2) becomes ({c * 0.3:.4f}, {c * -1.2:.4f}), covariance {c * c:.4f} I")
```

```bash
python3 schedule_levels.py
```

![The bars of c and c squared at t = 0, 25, 50, 75 and 99, the four-value draw times 0.9309 with mean square 0.8665, the share slip at t = 25 giving 0.0270, and the toy draw at t = 25 and t = 75|1000](assets/variance-the-noise-scale-across-the-schedule.png)

The bars are the point to see. For every $c$ below 1, $c^2$ is smaller than $c$, so at $t = 25$ the noise already moves a point 0.4054 on a typical draw while holding only 16% of the variance.

**9. Clean up, and prove it.**

```bash
cd ~ && rm -r ~/playground/sandbox/variance-scaling
ls ~/playground/sandbox/variance-scaling; echo $?
```

You should see `No such file or directory`, then `2`.

## Reading the scaled output

Navigation: ⬅️ [[#Try the scaling rule yourself]] | 📋 [[#Table of contents|TOC]] | [[#How the scaling rule works]] ➡️

From step 4, the coin:

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | coin, squared misses | `[1.0, 1.0]` | each face misses the mean 0 by 1, and $1^2 = 1$ | shown |
| 2 | coin, variance | `1.0` | the average of the squared misses; the coin has variance 1, like $\varepsilon$ | shown |
| 3 | c * coin, values | `[0.7223, -0.7223]` | each face multiplied by $c$; the mean stays 0, since $c \times 0 = 0$ | shown |
| 4 | c * coin, squared misses | `[0.5217, 0.5217]` | each miss is $c$ times the old miss, so its square is $c^2$ times the old square | derived below |
| 5 | c * coin, variance | `0.5217` | the average of two copies of $c^2$ is $c^2$ | derived below |
| 6 | c squared | `0.5217` | $0.7223^2$, equal to field 5, and equal to the noise share $1 - \bar\alpha_{50} = 1 - 0.4783$ | shown |

From step 6, the scaled standard-normal draws. Only what differs from the coin is new:

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | eps itself, variance | `0.997925` | the measured variance of 200,000 draws whose true variance is 1; a measured variance has standard error $\sqrt{2/n} = 0.0032$ here, so it sits 0.66 standard errors low | derived in [[Sampling A Diagonal Gaussian#How sampling works]] |
| 2 | c = +0.72230, variance | `0.520635` | the scaled draws' variance, a little under 0.5217 only because eps's own measured variance is a little under 1 | shown |
| 3 | ratio | `0.521717` | field 2 over field 1: exactly $c^2$, because the rule holds for the average over any list of numbers, not only in expectation | derived below |
| 4 | c squared | `0.521717` | equal to field 3 in all six places | shown |
| 5 | sd against \|c\| | `0.72155` against `0.72230` | the standard deviation is multiplied by $\lvert c\rvert$: $0.72230 \times \sqrt{0.997925} = 0.72155$ | derived below |
| 6 | the line for c = -0.72230 | same variance, ratio and sd | the square erases the sign of $c$; only the mean's sign flips | shown |
| 7 | c = +0.02512, ratio | `0.000631` | $0.02512^2 = 0.000631 = \beta_0$, the noise share at $t = 0$ | shown |

From step 8:

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | one toy draw | `[0.2167, -0.8668]` | $0.7223 \times 0.3$ and $0.7223 \times (-1.2)$: each coordinate is scaled by the same $c$ | shown |
| 2 | the two diagonal entries | `0.5227`, `0.5219` | each coordinate's variance, near $c^2 = 0.5217$; the standard error of each is $0.5217\sqrt{2/n} = 0.0016$, so the first sits 0.6 standard errors above it and the second 0.1 | derived below |
| 3 | the off-diagonal entry | `-0.0003` | the covariance of the two coordinates, near 0 because they were drawn independently | derived below |
| 4 | c squared times I | `[[0.5217, ...], [..., 0.5217]]` | the covariance the rule predicts, $c^2 I$ | derived below |

From `schedule_levels.py`, numbered as on its picture:

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | t = 25, c | `0.4054` | $\sqrt{1 - 0.835621}$, the noise's typical miss at $t = 25$ | shown |
| 2 | t = 25, c^2 | `0.1644` | its variance, $1 - \bar\alpha_{25}$; the bar is under half the length of the $c$ bar, because $c^2 < c$ whenever $0 < c < 1$ | derived below |
| 3 | mean square | `0.8665` | the four values $\pm 1.2247$, $\pm 0.7071$ have mean 0 and mean square $(1.5 + 0.5)/2 = 1$, so after scaling the mean square is the variance | shown |
| 4 | c75 squared | `0.8665` | equal to field 3: the rule needs only mean 0 and variance 1, not a coin and not a bell | derived below |
| 5 | coin times the share | `0.0270` | step 5's slip at $t = 25$: $0.1644^2 = 0.0270$, a sixth of the 0.1644 wanted | shown |
| 6 | t = 25 toy draw | `(0.1216, -0.4865)` | each coordinate times 0.4054; covariance $0.1644\,I$ | shown |
| 7 | t = 75 toy draw | `(0.2793, -1.1170)` | each coordinate times 0.9309; covariance $0.8665\,I$. Rounding $c$ to 0.9309 first gives $-1.1171$ and 0.8666, a last-place difference | shown |

## How the scaling rule works

Navigation: ⬅️ [[#Reading the scaled output]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to change a spread]] ➡️

Write $\mu = \mathbb{E}[X]$ and $Y = cX$. The mean first, then the variance, one step per line:

$$
\begin{aligned}
\mathbb{E}[Y] &= \mathbb{E}[cX] = c\,\mathbb{E}[X] = c\mu \\
Y - \mathbb{E}[Y] &= cX - c\mu = c\,(X - \mu) \\
(Y - \mathbb{E}[Y])^2 &= c^2\,(X - \mu)^2 \\
\operatorname{Var}(Y) &= \mathbb{E}\big[c^2 (X - \mu)^2\big] = c^2\,\mathbb{E}\big[(X - \mu)^2\big] = c^2 \operatorname{Var}(X) \\
\operatorname{sd}(Y) &= \sqrt{c^2 \operatorname{Var}(X)} = |c|\,\operatorname{sd}(X)
\end{aligned}
$$

Line 1 and line 4 use one fact twice: a fixed number comes out of an average (Theorem 3.4). Line 3 is $(ca)^2 = c^2 a^2$. No line uses the shape of the distribution, so the rule holds for the coin, for $\varepsilon$, and for any list of numbers averaged with equal weights. That last case is why step 6's ratio is $c^2$ to every printed place, while the variance itself is not.

**The worked numbers.** For a standard normal draw, $\operatorname{Var}(\varepsilon) = 1$, so $\operatorname{Var}(c\varepsilon) = c^2$:

$$
\begin{aligned}
t = 25: \quad & c = \sqrt{1 - \bar\alpha_{25}} = \sqrt{1 - 0.8356} = \sqrt{0.1644} = 0.4054, & \operatorname{Var}(c\varepsilon) &= 0.4054^2 \times 1 = 0.1644 \\
t = 50: \quad & c = \sqrt{1 - \bar\alpha_{50}} = \sqrt{1 - 0.4783} = \sqrt{0.5217} = 0.7223, & \operatorname{Var}(c\varepsilon) &= 0.7223^2 \times 1 = 0.5217 \\
t = 75: \quad & c = \sqrt{1 - \bar\alpha_{75}} = \sqrt{1 - 0.1335} = \sqrt{0.8665} = 0.9309, & \operatorname{Var}(c\varepsilon) &= 0.9309^2 \times 1 = 0.8665 \\
t = 0: \quad & c = \sqrt{\beta_0} = \sqrt{0.000631} = 0.02512, & \operatorname{Var}(c\varepsilon) &= 0.02512^2 \times 1 = 0.000631
\end{aligned}
$$

At $t = 50$ the noise term's variance is exactly the noise share $1 - \bar\alpha_{50}$, which is what the forward formula asks of it.

**Two coordinates.** With $\varepsilon = (\varepsilon_1, \varepsilon_2)$ independent and each of variance 1, scaling both by $c$ gives each coordinate variance $c^2$, and the covariance of the two stays $c^2 \operatorname{Cov}(\varepsilon_1, \varepsilon_2) = c^2 \times 0 = 0$. The covariance matrix is $c^2 I$, the matrix form $\operatorname{Var}[Ax] = A \operatorname{Var}[x] A^\top$ of [the matrix cookbook's linear forms](../references/textbooks/linear-algebra/matrix-cookbook.pdf#page=35) with $A = cI$.

![The coin's faces at -1 and +1 carry misses of 1 and squares of area 1; times c = 0.7223 the faces move to -0.7223 and +0.7223, each miss shrinks to 0.7223 and each square to area 0.5217, so the variance falls from 1 to 0.5217|500](assets/variance-the-mechanism.webp)

*🖼️ Diagram wanted: the deep-dive sheet composing the form, the mechanism and step 6's run. Prompt 3 in the same file.*

## Other ways to change a spread

Navigation: ⬅️ [[#How the scaling rule works]] | 📋 [[#Table of contents|TOC]] | [[#Why the scaling rule matters]] ➡️

- **Shifting**, $X + c$, moves the mean and leaves the variance alone (Theorem 3.5 (iii), [PDF p. 151](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=151)). That is why $\mu + \sigma\varepsilon$ has variance $\sigma^2$: the shift by $\mu$ adds nothing to the spread. [[Scaling And Shifting A Random Variable#How scaling and shifting work]] derives the scale and the shift together, $aX + b$, and works them on a fair die.
- **Adding an independent draw**, $X + Y$, adds the variances: $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + 2\operatorname{Cov}(X, Y) + \operatorname{Var}(Y)$, and the covariance is 0 when they are independent ([Theorem 5.4, PDF p. 278](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=278); [Theorem 5.5, PDF p. 279](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=279)). With the scaling rule this gives $\operatorname{Var}(aX + bY) = a^2\operatorname{Var}(X) + b^2\operatorname{Var}(Y)$, the line [[The Forward Process#How the jump works]] uses. The sum rule has its own note, [[Sums Of Independent Gaussians#How the rule works]].
- **A matrix instead of a number**, $Ax$, multiplies the covariance on both sides, $A \Sigma A^\top$, when the coordinates must be mixed rather than only stretched. The number $c$ is the case $A = cI$.

## Why the scaling rule matters

Navigation: ⬅️ [[#Other ways to change a spread]] | 📋 [[#Table of contents|TOC]] | [[#The scaling rule taught in, applied in]] ➡️

It is why the forward formula $x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon$ multiplies $\varepsilon$ by $\sqrt{1 - \bar\alpha_t}$ and not by $1 - \bar\alpha_t$. The formula multiplies a draw, so it needs a standard deviation, and the variance share has to be square-rooted to become one. The same reason puts `np.sqrt(var)` in every Gaussian sampler.

## The scaling rule taught in, applied in

Navigation: ⬅️ [[#Why the scaling rule matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the `/drip --math` walk of the forward process and the score in the reduce-reuse-recycle research repository, piece 1, rung 1: the definition as the average squared miss, the coin times $c = 0.7223$ with variance 0.5217, the $t = 0$ level with variance 0.000631, the toy draw $(0.3, -1.2)$ becoming $(0.2167, -0.8668)$, and why the forward formula takes a square root; then its worked example on the schedule: $c = 0.4054$ with variance 0.1644 at $t = 25$, $c = 0.9309$ with variance 0.8665 at $t = 75$, a four-value draw $\pm 1.2247$, $\pm 0.7071$ scaled by 0.9309, the share slip at $t = 25$ giving 0.0270, the toy draw at $t = 25$ and $t = 75$, and the bars of $c$ beside $c^2$ at five levels
- the sampling journey's [chapter 10, section 10.6](/home/molef/goal-setting/learning/mathematics/statistics/sampling/textbook/10-the-tangent-line-and-one-input.md#106-one-standard-error-through-the-slope), which applies Theorem 3.5 (ii) to the tangent line to carry one standard error through a slope
- the sampling journey's [chapter 6, section 6.2](/home/molef/goal-setting/learning/mathematics/statistics/sampling/textbook/06-the-normal-interval.md#62-the-standard-error), where dividing a sum by $N$ divides its variance by $N^2$
- the from-scratch-to-SDXL journey's [plan 06](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/plans/06-latent-diffusion-on-mnist-latents.md), line 124: latents with standard deviation $s$ leave signal $s^2\bar\alpha_n$, so the noise levels are wrong unless $s = 1$

**Applied in:** step 4 of the one-expert rebuild walk in the reduce-reuse-recycle research repository (`artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-4-the-forward-process-and-the-cosine-schedule`), which noises 2D points along a 100-step cosine schedule: the noise term's standard deviation is 0.7223 at $t = 50$ and 0.0251 at $t = 0$, so its variance is the noise share, 0.5217 and 0.000631.

> [!note]- How this was checked
> The five scripts were run on 2026-10-20 on mscluster (Linux), with Python 3.12.10 and the standard library only, in the empty folder `~/playground/sandbox/variance-scaling`, by vault-writer. `schedule_levels.py` was run on 2026-10-21 the same way, twice, with identical output; its five $\bar\alpha_t$ values were recomputed from the rebuild's `cosine_beta_schedule` (`rebuild/model.py`, $s = 0.008$, 100 steps) and match `rebuild/out/walk-numbers.json` to its four places. `scaled_normal.py` was run twice and printed the same lines. The folder was removed afterwards and the clean-up check returned 2. The prepared environment `~/.vault-sandbox` is missing on this machine and was not needed. The five terminal pictures were rendered from the captured text by a script in DejaVu Sans Mono, never drawn, and each was opened before filing. The textbook's PDF pages 147, 150, 151, 152, 200, 278 and 279 and the matrix cookbook's page 35 were opened and read as text. The schedule numbers ($\bar\alpha_{50} = 0.4783$, $\beta_0 = 0.000631$, and the noise scales 0.7223 and 0.0251) match the rebuild's `rebuild/out/walk-numbers.json`. [Variance](https://en.wikipedia.org/wiki/Variance) on Wikipedia (CC BY-SA 4.0) and the Python [statistics module](https://docs.python.org/3/library/statistics.html) documentation each answered 200 on 2026-10-20. No tldr-pages entry covers this.
