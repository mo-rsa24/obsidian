---
aliases: [density of the one jump, the one jump's density, one-shot draw, one-shot forward draw, the one-shot draw and its density, "q(x_t | x_0)", density of q(x_t | x_0), forward density, forward process density, "N(x_t; sqrt(abar_t) x_0, (1 - abar_t) I)", exponent at the drawn point, "-|eps|^2 / 2", the exponent is the same at every step, displacement from the centre]
sources:
  - "Ho, Jain, Abbeel, Denoising Diffusion Probabilistic Models, NeurIPS 2020, equation (4): https://arxiv.org/abs/2006.11239"
  - "The Little Book of Generative AI Foundations, section 4.1.1, PDF p. 71, q(x_t | x_0) = N(x_t | sqrt(abar_t) x_0, (1 - abar_t) I): ../../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=71"
  - "Chan, Introduction to Probability for Data Science, Michigan Publishing 2021, Definition 5.22, the d-dimensional Gaussian density, PDF p. 306: ../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=306"
---

# The Density Of The One Jump

Up: [[Diffusion Models]] · ⬅️ [[From Many Steps To One Jump]] · [[The Cosine Noise Schedule]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[From Many Steps To One Jump]] for the signal $\sqrt{\bar\alpha_t}$ and the noise variance $1 - \bar\alpha_t$, [[Sums Of Independent Gaussians#How the rule works|the sum of independent Gaussians]] for why all that noise is one draw, [[Scaling And Shifting A Random Variable#What scaling and shifting do|scaling and shifting]] for why adding a constant moves only the centre, and [[Diagonal Covariance#How it works|the diagonal Gaussian density]] with [[The Front Factor Of A Gaussian Density#The front factor from the bell's area|its front factor]] for the formula itself.

> [!question] Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. It has no questions on this note yet.

> [!warning] Unfinished
> - The form, the mechanism and the deep-dive sheet are waiting: prompts 37, 38 and 39 in the vault's `.prompts/Diffusion Models.md`.
> - The diffusion models quiz has no questions on this note yet.

Stated claims: 1.

**All the noise the small steps add is one Gaussian draw, so the noised point is $x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon$ with a single standard normal $\varepsilon$, and for a fixed clean point its density is $q(x_t \mid x_0) = \mathcal{N}(x_t;\ \sqrt{\bar\alpha_t}\,x_0,\ (1 - \bar\alpha_t) I)$.** At the point the draw lands on, the exponent of that density is $-|\varepsilon|^2/2$ whatever $t$ is, because the variance $1 - \bar\alpha_t$ cancels. The next step in the walk differentiates exactly this exponent to get the score. The density form is *cited* from Ho et al., equation (4), and from [the little book, PDF p. 71](../../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=71); every step from the draw to it is *derived* below.

Steps are counted as the rebuild's code counts them, from 0, so $\bar\alpha_{50} = 0.4783$ and $\bar\alpha_{25} = 0.8356$, as in [[From Many Steps To One Jump]].

## Where you work

Any terminal with Python 3. The scripts use the standard library only (`math` and `statistics`), so `python3` runs them, and so does the prepared environment `~/.vault-sandbox/bin/python` where it exists. A new empty folder; nothing here touches a real project.

## Table of contents

- [[#The one-shot draw and its density]]
- [[#Try the density yourself]]
- [[#Reading the density output]]
- [[#How the density follows from the draw]]
- [[#Other ways to get the density]]
- [[#Why the density matters]]
- [[#The density taught in, applied in]]

## The one-shot draw and its density

Navigation: 📋 [[#Table of contents|TOC]] | [[#Try the density yourself]] ➡️

**The one-shot draw makes the noised point at step $t$ from the clean point $x_0$ and one standard normal draw $\varepsilon$, $x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon$, and its density $q(x_t \mid x_0)$, also called the forward density or the one jump's density, is the 2D Gaussian centred at $\sqrt{\bar\alpha_t}\,x_0$ with variance $1 - \bar\alpha_t$ on each axis.** The bar in $q(x_t \mid x_0)$ reads "given $x_0$": the clean point is held fixed and only $\varepsilon$ is random.

**When to reach for it.** When you need how likely a noised point is, rather than one sample of it: to write $\log q(x_t \mid x_0)$ and take its gradient for the score, or to check that a drawn point sits where the formula says. Without the density there is only the sampler, and nothing to differentiate.

**The form.** With $\sigma^2 = 1 - \bar\alpha_t$ and the centre $\mu = \sqrt{\bar\alpha_t}\,x_0$:

```text
x_t = sqrt(abar_t) * x0 + sqrt(1 - abar_t) * eps          one draw; eps ~ N(0, I), the same shape as x0
mu  = sqrt(abar_t) * x0                                   the centre; x0 held fixed
q(x_t | x0) = 1 / (2 pi sigma^2) * exp(-|x_t - mu|^2 / (2 sigma^2)),   sigma^2 = 1 - abar_t     in 2D
d   = x_t - mu = sqrt(1 - abar_t) * eps                   the displacement from the centre
exponent at the drawn point = -|d|^2 / (2 sigma^2) = -|eps|^2 / 2,   the same at every t
```

Each piece of the density does one job. $|x_t - \mu|^2$ is the squared distance from the centre; $2\sigma^2$ sets how fast the bell falls away, so it sets the width; $1/(2\pi\sigma^2)$ makes the total volume under the surface 1, as [[The Front Factor Of A Gaussian Density#The front factor from the bell's area|the front factor note]] proves by a grid sum.

*🖼️ Diagram wanted: the form, the density formula with each slot labelled at t = 50 (prefactor 0.3050, squared distance 0.7983, width 2 × 0.5217), and a top-down bell centred at sqrt(abar) x0. Prompt 37 in the vault's `.prompts/Diffusion Models.md`.*

## Try the density yourself

Navigation: ⬅️ [[#The one-shot draw and its density]] | 📋 [[#Table of contents|TOC]] | [[#Reading the density output]] ➡️

**1. What you need.** Python 3:

```bash
python3 --version
```

This run printed `Python 3.12.10`.

**2. When it is missing.** Install Python 3 from python.org, or run `uv python install 3.12`. Not run on this machine, which already has it.

**3. Make something to act on: the cosine schedule.** Make the empty folder and confirm it is empty:

```bash
mkdir ~/playground/sandbox/forward-density && cd ~/playground/sandbox/forward-density && ls -A | wc -l
```

You should see `0`. Save this as `schedule.py`, the same 100-step cosine schedule as [[From Many Steps To One Jump#Try the two steps yourself]]:

```python
import math

T, s = 100, 0.008
C = [math.cos((k / T + s) / (1 + s) * math.pi / 2) ** 2 for k in range(T + 1)]
C = [c / C[0] for c in C]
betas = [min(max(1 - C[k + 1] / C[k], 0.0), 0.999) for k in range(T)]
abar = []
kept = 1.0
for b in betas:
    kept *= 1 - b
    abar.append(kept)
```

**4. A look before.** Save this as `look.py`:

```python
import math
from schedule import abar

for t in (25, 50):
    print(f"t = {t}: abar {abar[t]:.4f}  sqrt(abar) {math.sqrt(abar[t]):.4f}  1 - abar {1 - abar[t]:.4f}  sd {math.sqrt(1 - abar[t]):.4f}")
```

```bash
python3 look.py
```

```text
t = 25: abar 0.8356  sqrt(abar) 0.9141  1 - abar 0.1644  sd 0.4054
t = 50: abar 0.4783  sqrt(abar) 0.6916  1 - abar 0.5217  sd 0.7223
```

**5. The failure: the mean without its square root.** Writing the centre as $\bar\alpha_t\,x_0$ is the usual slip. The toy's clean point is $x_0 = (0, 0.5)$ and the draw is $\varepsilon = (0.3, -1.2)$. Save this as `broken_mean.py`:

```python
import math
from schedule import abar

x0, eps = (0.0, 0.5), (0.3, -1.2)
for t in (50, 25):
    a = abar[t]
    sd = math.sqrt(1 - a)
    xt = [math.sqrt(a) * c + sd * e for c, e in zip(x0, eps)]
    wrong = [a * c for c in x0]
    d = [x - m for x, m in zip(xt, wrong)]
    sq = d[0] ** 2 + d[1] ** 2
    print(f"t = {t}: wrong mean ({wrong[0]:.4f}, {wrong[1]:.4f})  d ({d[0]:.4f}, {d[1]:.4f})  d / sd ({d[0] / sd:.4f}, {d[1] / sd:.4f})  exponent {-sq / (2 * (1 - a)):.4f}")
```

```bash
python3 broken_mean.py
```

![The wrong centre (0, 0.2391) at t = 50 leaves a displacement (0.2167, -0.7601) that is not 0.7223 times eps, and the exponent moves from -0.5987 to -0.6535 between steps|1000](assets/forward-density-wrong-mean-without-the-root.png)

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | wrong mean, $t = 50$ | `(0.0000, 0.2391)` | $0.4783 \times 0.5$ (`sqrt(abar)` is the factor that belongs there), where the right centre is $0.6916 \times 0.5 = 0.3458$ | shown |
| 2 | displacement | `(0.2167, -0.7601)` | the drawn point $(0.2167, -0.5210)$ minus the wrong centre | shown |
| 3 | displacement over sd | `(0.3000, -1.0523)` | should give back $\varepsilon = (0.3, -1.2)$; the second coordinate is off by about $0.148$, the extra $(\sqrt{\bar\alpha} - \bar\alpha)\,x_0$ divided by $0.7223$ | derived below |
| 4 | exponent, $t = 50$ | `-0.5987` | no longer $-|\varepsilon|^2/2 = -0.765$ | shown |
| 5 | exponent, $t = 25$ | `-0.6535` | and it now changes with $t$, so the cancellation the score uses is gone | shown |

**6. The technique: the draw and its density at two steps.** Save this as `density.py`. The function `q` is the formula from [[#The one-shot draw and its density]]; the `if __name__ == "__main__":` line keeps its worked example from running when step 7 imports it:

```python
import math
from schedule import abar


def q(x, x0, a):
    """The one jump's density N(x; sqrt(a) x0, (1 - a) I) in 2D, with a the kept share abar_t."""
    var = 1 - a
    mean = [math.sqrt(a) * c for c in x0]
    sq = sum((xi - mi) ** 2 for xi, mi in zip(x, mean))
    return 1 / (2 * math.pi * var) * math.exp(-sq / (2 * var)), mean, sq


if __name__ == "__main__":
    x0, eps = (0.0, 0.5), (0.3, -1.2)
    for t in (50, 25):
        a = abar[t]
        sd = math.sqrt(1 - a)
        xt = [math.sqrt(a) * c + sd * e for c, e in zip(x0, eps)]
        dens, mean, sq = q(xt, x0, a)
        print(f"t = {t}: mean ({mean[0]:.4f}, {mean[1]:.4f})  x_t ({xt[0]:.4f}, {xt[1]:.4f})  |d|^2 {sq:.4f}")
        print(f"        exponent {-sq / (2 * (1 - a)):.4f}  prefactor {1 / (2 * math.pi * (1 - a)):.4f}  q {dens:.4f}")
    print(f"-|eps|^2 / 2 = {-(eps[0] ** 2 + eps[1] ** 2) / 2:.4f}")
```

```bash
python3 density.py
```

![The draw at t = 50 lands on (0.2167, -0.5210) with density 0.1419, at t = 25 on (0.1216, -0.0295) with density 0.4505, and the exponent is -0.7650 at both|900](assets/forward-density-the-jump-density-at-two-steps.png)

[[#Reading the density output]] reads each numbered field.

**7. Another way to get the same answer: two one-dimensional bells.** The covariance $(1 - \bar\alpha_t) I$ is diagonal, so the 2D density is the product of one bell per coordinate, as [[Diagonal Covariance#How it works]] derives. Python's own `statistics.NormalDist` gives each bell. Save this as `two_bells.py`:

```python
import math
from statistics import NormalDist
from schedule import abar
from density import q

x0, eps = (0.0, 0.5), (0.3, -1.2)
for t in (50, 25):
    a = abar[t]
    sd = math.sqrt(1 - a)
    xt = [math.sqrt(a) * c + sd * e for c, e in zip(x0, eps)]
    bells = [NormalDist(math.sqrt(a) * c, sd).pdf(x) for c, x in zip(x0, xt)]
    print(f"t = {t}: bells {bells[0]:.4f} x {bells[1]:.4f} = {bells[0] * bells[1]:.4f}  | q {q(xt, x0, a)[0]:.4f}")
```

Save this as `one_d.py`, the one-dimensional case the walk worked first, a clean point $0.5$ at $t = 50$:

```python
import math
from statistics import NormalDist
from schedule import abar

a = abar[50]
mean, sd = math.sqrt(a) * 0.5, math.sqrt(1 - a)
print(f"1D, x0 = 0.5, t = 50: mean {mean:.4f}  sd {sd:.4f}  peak {1 / (math.sqrt(2 * math.pi) * sd):.4f}  peak by NormalDist {NormalDist(mean, sd).pdf(mean):.4f}")
```

```bash
python3 two_bells.py
python3 one_d.py
```

![Two one-dimensional bells multiply to 0.1419 and 0.4505, equal to q, and the one-dimensional jump at t = 50 has mean 0.3458, sd 0.7223 and peak 0.5523|1000](assets/forward-density-two-bells-and-one-dimension.png)

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | product of bells, $t = 50$ | `= 0.1419` | the horizontal bell's $0.5280$ times the vertical bell's $0.2688$ | shown |
| 2 | `q`, $t = 50$ | `0.1419` | step 6's 2D formula, equal to field 1 | derived in [[Diagonal Covariance#How it works]] |
| 3 | product of bells, $t = 25$ | `= 0.4505` | equal to step 6's $q$ at $t = 25$ | shown |
| 4 | 1D mean | `0.3458` | $\sqrt{0.4783} \times 0.5 = 0.6916 \times 0.5$ | derived below |
| 5 | 1D sd | `0.7223` | $\sqrt{1 - 0.4783}$, the width of the bell | derived below |
| 6 | 1D peak | `0.5523` | the bell's height at its centre, $1/(\sqrt{2\pi} \times 0.7223)$; `NormalDist` agrees | shown |

**8. More worked examples: the same draw at five steps.** The walk used two forms, the 1D bell (step 7) and the 2D toy at two steps (step 6). This one runs the 2D toy across the schedule to show the exponent holding still. Save this as `every_t.py`:

```python
import math
from schedule import abar
from density import q

x0, eps = (0.0, 0.5), (0.3, -1.2)
for t in (0, 25, 50, 75, 99):
    a = abar[t]
    xt = [math.sqrt(a) * c + math.sqrt(1 - a) * e for c, e in zip(x0, eps)]
    dens, mean, sq = q(xt, x0, a)
    print(f"t = {t:2d}: 1 - abar {1 - a:.6f}  |d|^2 {sq:.6f}  exponent {-sq / (2 * (1 - a)):.4f}  q {dens:.4f}")
```

```bash
python3 every_t.py
```

![The exponent is -0.7650 at t = 0, 25, 50, 75 and 99 while q falls from 117.3172 to 0.0741|900](assets/forward-density-same-exponent-at-every-step.png)

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | exponent, $t = 0$ | `-0.7650` | $-1.53/2$, with a variance of only $0.000631$ | derived below |
| 2 | exponent, $t = 99$ | `-0.7650` | the same, with a variance of $1.000000$; $\bar\alpha_{99}$ is $2.4 \times 10^{-7}$ | derived below |
| 3 | `q`, $t = 0$ | `117.3172` | a density, not a probability: the bell is so narrow ($0.0251$ wide) that its height passes 1 | shown |
| 4 | `q`, $t = 99$ | `0.0741` | the front factor alone, $1/(2\pi) = 0.1592$, times $e^{-0.765} = 0.4653$: everything that changes with $t$ sits in the front factor | derived below |

**9. Clean up, and prove it.**

```bash
cd ~ && rm -r ~/playground/sandbox/forward-density
ls ~/playground/sandbox/forward-density; echo $?
```

You should see `ls: cannot access '/home-mscluster/mmolefe/playground/sandbox/forward-density': No such file or directory` (with your own home folder in the path), then `2`.

## Reading the density output

Navigation: ⬅️ [[#Try the density yourself]] | 📋 [[#Table of contents|TOC]] | [[#How the density follows from the draw]] ➡️

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | mean, $t = 50$, from step 6 | `(0.0000, 0.3458)` | the centre $\sqrt{\bar\alpha_{50}}\,x_0 = 0.6916 \times (0, 0.5)$: shrinking $x_0$ moves the centre toward the origin | derived below |
| 2 | $x_t$, $t = 50$ | `(0.2167, -0.5210)` | the centre plus $0.7223 \times (0.3, -1.2) = (0.2167, -0.8668)$; equal to `p1.example_x_t` in the rebuild's `walk-numbers.json` | derived below |
| 3 | $\lvert d \rvert^2$ | `0.7983` | squared distance from the centre, $0.5217 \times 1.53$ | derived below |
| 4 | exponent, $t = 50$ | `-0.7650` | $-0.7983 / (2 \times 0.5217)$ | derived below |
| 5 | prefactor, $t = 50$ | `0.3050` | $1/(2\pi \times 0.5217)$, the front factor that makes the volume 1 | derived below |
| 6 | `q`, $t = 50$ | `0.1419` | $0.3050 \times e^{-0.765} = 0.3050 \times 0.4653$ | derived below |
| 7 | $x_t$, $t = 25$ | `(0.1216, -0.0295)` | the same $\varepsilon$ scaled by $0.4054$, added to the centre $(0, 0.4571)$ | derived below |
| 8 | exponent, $t = 25$ | `-0.7650` | $-0.2515 / (2 \times 0.1644)$: the same number as field 4 | derived below |
| 9 | `q`, $t = 25$ | `0.4505` | $0.9682 \times 0.4653$: a narrower bell, so a larger front factor | derived below |
| 10 | $-\lvert\varepsilon\rvert^2/2$ | `-0.7650` | $-(0.3^2 + 1.2^2)/2 = -1.53/2$, equal to fields 4 and 8 | derived below |

## How the density follows from the draw

Navigation: ⬅️ [[#Reading the density output]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to get the density]] ➡️

Textbook: [Chan, Introduction to Probability for Data Science, Definition 5.22, the d-dimensional Gaussian density, PDF p. 306](../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=306)

**The noise is one draw.** [[From Many Steps To One Jump#How two steps become every step|The induction]] left $x_t = \sqrt{\bar\alpha_t}\,x_0 + n_t$, with $n_t$ a sum of independent Gaussian pieces of total variance $1 - \bar\alpha_t$. [[Sums Of Independent Gaussians#How the rule works|A sum of independent Gaussians is a Gaussian]], so $n_t$ is one draw of mean 0 and variance $1 - \bar\alpha_t$ per coordinate, and [[Variance#Scaling a draw scales its variance by the square|the scaling rule]] writes such a draw as $\sqrt{1 - \bar\alpha_t}\,\varepsilon$ with one standard normal $\varepsilon$:

$$
x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon, \qquad \varepsilon \sim \mathcal{N}(0, I)
$$

**Hold $x_0$ fixed.** Then $\sqrt{\bar\alpha_t}\,x_0$ is a constant, and [[Scaling And Shifting A Random Variable#What scaling and shifting do|adding a constant]] moves the centre without changing the spread. Each coordinate of $\varepsilon$ is its own independent draw, so the covariance is $(1 - \bar\alpha_t)$ times the identity:

$$
q(x_t \mid x_0) = \mathcal{N}\big(x_t;\ \sqrt{\bar\alpha_t}\,x_0,\ (1 - \bar\alpha_t) I\big)
$$

**Write out the 2D Gaussian density**<sub>[1](../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=306 "probability for data science p. 306, Definition 5.22"), [2](../../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=471 "understanding deep learning p. 471, spherical covariance and its circular contours")</sub>. With $\Sigma = \sigma^2 I$ in $d = 2$ dimensions, $\det\Sigma = \sigma^4$ and $\Sigma^{-1} = I/\sigma^2$, so the general formula becomes

$$
\begin{aligned}
\mathcal{N}(x; \mu, \Sigma) &= \frac{1}{(2\pi)^{d/2} \det(\Sigma)^{1/2}} \exp\!\Big(-\tfrac{1}{2}(x - \mu)^\top \Sigma^{-1} (x - \mu)\Big) \\
\mathcal{N}(x; \mu, \sigma^2 I) &= \frac{1}{2\pi\sigma^2} \exp\!\Big(-\frac{|x - \mu|^2}{2\sigma^2}\Big) \\
q(x_t \mid x_0) &= \frac{1}{2\pi(1 - \bar\alpha_t)} \exp\!\Big(-\frac{|x_t - \sqrt{\bar\alpha_t}\,x_0|^2}{2(1 - \bar\alpha_t)}\Big)
\end{aligned}
$$

### The exponent at the drawn point

**At the point the draw lands on, the displacement from the centre is $d = x_t - \sqrt{\bar\alpha_t}\,x_0 = \sqrt{1 - \bar\alpha_t}\,\varepsilon$, so the exponent of $q(x_t \mid x_0)$ is $-|\varepsilon|^2/2$ at every $t$.** The variance cancels:

$$
\begin{aligned}
|d|^2 &= (1 - \bar\alpha_t)\,|\varepsilon|^2 \\
-\frac{|d|^2}{2(1 - \bar\alpha_t)} &= -\frac{(1 - \bar\alpha_t)\,|\varepsilon|^2}{2(1 - \bar\alpha_t)} = -\frac{|\varepsilon|^2}{2}
\end{aligned}
$$

A later step makes the bell wider, and the draw lands proportionally farther from the centre, so the two effects cancel. Only the front factor $1/(2\pi(1 - \bar\alpha_t))$ changes with $t$, as step 8 printed. The score of $q(x_t \mid x_0)$ is the gradient of this exponent with respect to $x_t$, which the next piece of the walk takes.

**The worked numbers.** One dimension, clean point $0.5$ at $t = 50$:

$$
\text{mean } 0.6916 \times 0.5 = 0.3458, \qquad \text{sd } \sqrt{0.5217} = 0.7223, \qquad \text{peak } \frac{1}{\sqrt{2\pi} \times 0.7223} = \frac{1}{1.8105} = 0.5523
$$

The 2D toy at $t = 50$, $x_0 = (0, 0.5)$, $\varepsilon = (0.3, -1.2)$, $|\varepsilon|^2 = 0.09 + 1.44 = 1.53$:

$$
\begin{aligned}
\text{centre:}\quad & 0.6916 \times (0, 0.5) = (0, 0.3458) \\
x_{50}:\quad & (0, 0.3458) + 0.7223 \times (0.3, -1.2) = (0, 0.3458) + (0.2167, -0.8668) = (0.2167, -0.5210) \\
|d|^2:\quad & 0.5217 \times 1.53 = 0.7983 \\
\text{exponent:}\quad & -0.7983 / (2 \times 0.5217) = -0.765 \\
\text{prefactor:}\quad & 1 / (2\pi \times 0.5217) = 0.3050 \\
q:\quad & 0.3050 \times e^{-0.765} = 0.3050 \times 0.4653 = 0.1419
\end{aligned}
$$

The same $\varepsilon$ at $t = 25$, with $\sqrt{\bar\alpha_{25}} = 0.9141$ and $\sqrt{1 - \bar\alpha_{25}} = 0.4054$:

$$
\begin{aligned}
x_{25}:\quad & (0, 0.4571) + 0.4054 \times (0.3, -1.2) = (0.1216, -0.0295) \\
|d|^2:\quad & 0.1644 \times 1.53 = 0.2515, \qquad \text{exponent } -0.2515 / (2 \times 0.1644) = -0.765 \\
q:\quad & \frac{1}{2\pi \times 0.1644} \times 0.4653 = 0.9682 \times 0.4653 = 0.4505
\end{aligned}
$$

**The broken run.** With the centre written as $\bar\alpha_t\,x_0$, the displacement picks up an extra piece that does not scale with $\varepsilon$:

$$
\begin{aligned}
d &= x_t - \bar\alpha_t\,x_0 = (\sqrt{\bar\alpha_t} - \bar\alpha_t)\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon \\
t = 50:\quad d &= (0.69159 - 0.47830) \times (0, 0.5) + (0.21669, -0.86677) = (0, 0.10665) + (0.21669, -0.86677) = (0.2167, -0.7601)
\end{aligned}
$$

That is no longer $0.7223\,\varepsilon$, so the variance does not cancel: the exponent is $-0.5987$ at $t = 50$ and $-0.6535$ at $t = 25$, as step 5 printed.

*🖼️ Diagram wanted: the mechanism, the bell's circle at t = 25 and at t = 50 around its own centre, the same eps arrow scaled to each, both landing on the exponent -0.765 contour, with the wrong centre at t = 50 drawn dashed. Prompt 38 in the vault's `.prompts/Diffusion Models.md`.*

*🖼️ Diagram wanted: the deep-dive sheet composing the form, the mechanism and step 6's run. Prompt 39 in the vault's `.prompts/Diffusion Models.md`.*

## Other ways to get the density

Navigation: ⬅️ [[#How the density follows from the draw]] | 📋 [[#Table of contents|TOC]] | [[#Why the density matters]] ➡️

- **One bell per coordinate**, as in step 7, when the covariance is diagonal. It gives the same number and makes the independence of the coordinates visible.
- **A library density**, such as `statistics.NormalDist` for one coordinate, or a multivariate normal's `pdf` in SciPy for the whole vector (*stated*: not run here, since the prepared environment that holds SciPy is missing on this machine). It checks a hand formula; it does not show where the $-|\varepsilon|^2/2$ comes from.
- **The log density**, $\log q(x_t \mid x_0) = -\log(2\pi(1 - \bar\alpha_t)) - |x_t - \sqrt{\bar\alpha_t}\,x_0|^2 / (2(1 - \bar\alpha_t))$, when the next move is a gradient. The first term has no $x_t$ in it, so only the exponent survives differentiation.

## Why the density matters

Navigation: ⬅️ [[#Other ways to get the density]] | 📋 [[#Table of contents|TOC]] | [[#The density taught in, applied in]] ➡️

Training a diffusion expert compares the network's output with the score of $q(x_t \mid x_0)$, and that score is the gradient of the exponent in [[#The exponent at the drawn point]]. Because the exponent at the drawn point is $-|\varepsilon|^2/2$, the gradient there comes out as $-\varepsilon/\sqrt{1 - \bar\alpha_t}$: for the toy at $t = 50$ that is $-(0.3, -1.2)/0.7223 = (-0.4153, 1.6613)$, the rebuild's `p1.example_score` in `walk-numbers.json` (*cited*; the next piece of the walk derives it). That is why predicting the noise and predicting the score are the same job up to a scale. The cancellation only works with the square root on the centre.

## The density taught in, applied in

Navigation: ⬅️ [[#Why the density matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the `drip --math` walk of the forward process and the score in the reduce-reuse-recycle research repository (`artifacts/drips/forward-process-and-the-score/`), piece 1, rung 4, which closes piece 1: the noise as one draw, $q(x_t \mid x_0)$ for a fixed $x_0$, the 2D isotropic density term by term, worked in 1D at $t = 50$ and on the 2D toy at $t = 50$ and $t = 25$, the exponent $-0.765$ at both, and the centre without its square root as the broken run

**Applied in:** steps 4 and 5 of the one-expert rebuild walk in the reduce-reuse-recycle research repository (`artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-4-the-forward-process-and-the-cosine-schedule` and `#step-5-the-noise-is-the-score-rescaled`). Step 4 writes $q(x_t \mid x_0)$ for the training pairs of one diffusion expert; step 5 takes the gradient of its log at the toy's $x_{50} = (0.2167, -0.521)$ to show that the noise, rescaled, is the score.

> [!note]- How this was checked
> The seven scripts were run on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and the standard library only, in the empty folder `~/playground/sandbox/forward-density`, by vault-writer. `broken_mean.py`, `density.py`, `two_bells.py` and `every_t.py` were each run twice with identical output. The folder was removed afterwards and the clean-up check returned 2. The prepared environment `~/.vault-sandbox` is missing on this machine and was not needed.
>
> `schedule.py` is the same plain-Python cosine schedule as [[From Many Steps To One Jump]]. Its numbers match the rebuild's `rebuild/out/walk-numbers.json`: $\bar\alpha_{25} = 0.8356$, $\bar\alpha_{50} = 0.4783$, $\sqrt{1 - \bar\alpha_{25}} = 0.4054$, $\sqrt{1 - \bar\alpha_{50}} = 0.7223$, and the toy's $x_{50} = (0.2167, -0.521)$ is `p1.example_x_t`. Every number in the walk's turn (the 1D mean, sd and peak, both 2D worked examples, the exponent $-0.765$ and the broken centre $(0, 0.2391)$ with its displacement $(0.2167, -0.7601)$) was reproduced by these scripts.
>
> The four terminal pictures were rendered from the captured text by a script in DejaVu Sans Mono, never drawn, and each was opened before filing.
>
> Chan's PDF p. 306 was opened and read as text: Definition 5.22 gives the d-dimensional Gaussian density (5.35). Understanding Deep Learning's PDF p. 471 was opened: Figure C.4 and equation (C.24) show spherical covariance with circular contours and the 2D density as a product of two bells. The little book's PDF p. 71 was opened: it states $q(x_t \mid x_0) = \mathcal{N}(x_t \mid \sqrt{\bar\alpha_t}\,x_0, (1 - \bar\alpha_t) I)$ after combining the independent noise terms into one draw.
