---
aliases: [forward process, forward diffusion, noising process, noising a cloud, closed-form forward process, "q(x_t | x_0)", x_t = sqrt(abar) x_0 + sqrt(1 - abar) eps, alpha bar, abar, noise level, noise schedule level]
sources:
  - "Ho, Jain, Abbeel, Denoising Diffusion Probabilistic Models, NeurIPS 2020: https://arxiv.org/abs/2006.11239"
  - "Bradley, Nakkiran, Berthelot, Thornton, Susskind, Mechanisms of Projective Composition of Diffusion Models, ICML 2025: https://arxiv.org/abs/2502.04549"
  - "Du, Durkan, Strudel, Tenenbaum, Dieleman, Fergus, Sohl-Dickstein, Doucet, Grathwohl, Reduce, Reuse, Recycle: Compositional Generation with Energy-Based Diffusion Models and MCMC, ICML 2023: https://arxiv.org/abs/2302.11552"
  - "Geirhos, Jacobsen, Michaelis, Zemel, Brendel, Bethge, Wichmann, Shortcut Learning in Deep Neural Networks, Nature Machine Intelligence 2020: https://arxiv.org/abs/2004.07780"
---

# The Forward Process

Up: [[Diffusion Models]] · [[Composition]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[Multivariate Normal Distribution#Sampling a diagonal Gaussian]] for drawing a cloud, and [[NumPy#Broadcasting]] for noising many levels in one line.

> [!question] Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers this note, with the rest of the [[Diffusion Models]] folder. Your attempts are saved on the page.

**The forward process noises a clean point $x_0$ to level $\bar\alpha$ in one step, $x_t = \sqrt{\bar\alpha}\,x_0 + \sqrt{1 - \bar\alpha}\,\varepsilon$ with $\varepsilon \sim \mathcal{N}(0, I)$, so a cloud $\mathcal{N}(\mu, \sigma^2)$ becomes $\mathcal{N}(\sqrt{\bar\alpha}\,\mu,\ \bar\alpha\,\sigma^2 + 1 - \bar\alpha)$.** $\bar\alpha = 1$ is the clean data, and $\bar\alpha$ near 0 is almost pure noise. *Cited:* Ho et al., equation (4).

## Where you work

The setup is in [[Diffusion Models#Where you work]]: any terminal with Python 3, NumPy and Matplotlib, a new empty folder, and the learner's `toy.py` and `samples.py` saved into it.

## Table of contents

- [[#When to reach for the jump]]
- [[#The form of the jump]]
- [[#Try the jump yourself]]
- [[#Reading the noised output]]
- [[#How the jump works]]
- [[#One small step, fifty of them, and one jump]]
- [[#Other ways to noise]]
- [[#Why the jump matters]]
- [[#The jump taught in, applied in]]

## When to reach for the jump

Navigation: 📋 [[#Table of contents|TOC]] | [[#The form of the jump]] ➡️

When you need a cloud at a given noise level without running every small step before it: to make training pairs, to see what a noise level does to two experts before composing them, or to check a toy against the closed form. The paper composes the experts after noising, at every level, so knowing what each level does to a cloud comes first.

## The form of the jump

Navigation: ⬅️ [[#When to reach for the jump]] | 📋 [[#Table of contents|TOC]] | [[#Try the jump yourself]] ➡️

```text
abar = np.array([<level 1>, <level 2>, ...])                    shape (L,); 1 is clean, near 0 is noise
a    = abar[:, None, None]                                       shape (L, 1, 1), one number per level
xt   = np.sqrt(a) * x0 + np.sqrt(1 - a) * rng.standard_normal((L, N, 2))     shape (L, N, 2)
mean: np.sqrt(level) * mu        variance: level * var + 1 - level            the closed form, per level
```

Both factors are square roots. They make the two parts' variances, $\bar\alpha$ and $1 - \bar\alpha$, add to 1 for unit-variance data.

![One clean cloud and one noise cloud mixed by the two square-root dials into the noised cloud|800](assets/forward-process-the-form.webp)

*The form, one clean cloud and one noise cloud mixed by the two square-root dials into the noised cloud.*

## Try the jump yourself

Navigation: ⬅️ [[#The form of the jump]] | 📋 [[#Table of contents|TOC]] | [[#Reading the noised output]] ➡️

**1. What you need, and when it is missing.** As in the sandbox preparation above.

**2. Make something to act on.** `toy.py` and `samples.py` in `~/playground/sandbox/gaussian-clouds`, as above. The cloud is expert 1, $\mathcal{N}((-2, 0), \operatorname{diag}(1, 4))$.

**3. The failure: the weights without their square roots.** Save this as `wrong_scale.py`:

```python
import numpy as np
from toy import shared
from samples import sample, rng, N

mu, var = shared[1]
x0 = sample(mu, var, N)
a = 0.5
xt = a * x0 + (1 - a) * rng.standard_normal((N, 2))
print("no square roots, level 0.5: var", np.round(xt.var(0), 2).tolist(), "| closed form", (a * var + 1 - a).tolist())
```

```bash
~/.vault-sandbox/bin/python wrong_scale.py
```

```text
no square roots, level 0.5: var [0.5, 1.25] | closed form [1.0, 2.5]
```

Without the square roots, each part's variance is multiplied by the square of its weight, $0.25$, and the cloud shrinks to half the variance the closed form says.

**4. The technique.** Save this as `noised.py`. It noises one cloud at three levels in one tensor and prints the closed form beside each measured level:

```python
import numpy as np
from toy import shared
from samples import sample, rng, N

mu, var = shared[1]
x0 = sample(mu, var, N)
abar = np.array([1.0, 0.5, 0.0058])
a = abar[:, None, None]
xt = np.sqrt(a) * x0 + np.sqrt(1 - a) * rng.standard_normal((3, N, 2))
print(xt.shape)
for index, level in enumerate(abar):
    print("level", level, "measured", np.round(xt[index].mean(0), 2).tolist(), np.round(xt[index].var(0), 2).tolist(),
          "| closed form", np.round(np.sqrt(level) * mu, 2).tolist(), np.round(level * var + 1 - level, 2).tolist())
```

```bash
~/.vault-sandbox/bin/python noised.py
```

You should see:

![One cloud noised at three levels, the measured mean and variance beside the closed form at each|900](assets/forward-process-one-jump-against-the-closed-form.png)

Every measured pair sits within 0.01 of the closed form. Nothing else is printed before the shape line, because `samples.py` keeps its own print loop under `if __name__ == "__main__":`. Without that line, the import prints the three clouds first: see [[Modules And Imports#Try it yourself]] step 6.

**5. Another way to get the same answer: many small steps.** The jump stands in for a chain of small steps $x_s = \sqrt{\alpha_s}\,x_{s-1} + \sqrt{1 - \alpha_s}\,\varepsilon_s$, with $\bar\alpha$ the product of the $\alpha_s$. Save this as `stepwise.py`; its four $\alpha$ values are plan 09's:

```python
import numpy as np

rng = np.random.default_rng(1)
alphas = np.array([0.9, 0.8, 0.95, 0.7])
x0 = np.full(200_000, 2.0)
x = x0.copy()
for a in alphas:
    x = np.sqrt(a) * x + np.sqrt(1 - a) * rng.standard_normal(x.shape)
abar = np.prod(alphas)
jump = np.sqrt(abar) * x0 + np.sqrt(1 - abar) * rng.standard_normal(x0.shape)
print("abar", round(float(abar), 4))
print("four steps: mean", round(float(x.mean()), 3), "var", round(float(x.var()), 3))
print("one jump:   mean", round(float(jump.mean()), 3), "var", round(float(jump.var()), 3))
print("closed form: mean", round(float(np.sqrt(abar) * 2.0), 3), "var", round(float(1 - abar), 3))
```

```bash
~/.vault-sandbox/bin/python stepwise.py
```

```text
abar 0.4788
four steps: mean 1.383 var 0.521
one jump:   mean 1.386 var 0.519
closed form: mean 1.384 var 0.521
```

Four steps and one jump land on the same distribution. Why they must is plan 09's derivation, section 3, worked there on paper.

**6. Clean up, and prove it.** Keep the folder if you are going on to [[Composing Models With A Background#Try composing yourself]]. Otherwise:

```bash
cd ~ && rm -r ~/playground/sandbox/gaussian-clouds
ls ~/playground/sandbox/gaussian-clouds; echo $?
```

You should see `No such file or directory`, then `2`.

## Reading the noised output

Navigation: ⬅️ [[#Try the jump yourself]] | 📋 [[#Table of contents|TOC]] | [[#How the jump works]] ➡️

From step 4:

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | shape | `(3, 100000, 2)` | three levels, each a full cloud of 100,000 points in two coordinates | shown |
| 2 | level 0.5, measured mean | `[-1.41, 0.0]` | the cloud's centre moved toward 0 by $\sqrt{0.5} = 0.707$ | derived below |
| 3 | level 0.5, measured variance | `[1.0, 2.5]` | the narrow axis stayed at 1, the wide axis shrank from 4 toward 1 | derived below |
| 4 | level 0.5, closed form | `[-1.41, 0.0] [1.0, 2.5]` | $\sqrt{\bar\alpha}\,\mu$ and $\bar\alpha\,\sigma^2 + 1 - \bar\alpha$; equal to fields 2 and 3 | derived below |
| 5 | level 0.0058, measured variance | `[0.99, 1.02]` | almost pure noise: both axes close to 1, whatever the cloud was | derived below |

## How the jump works

Navigation: ⬅️ [[#Reading the noised output]] | 📋 [[#Table of contents|TOC]] | [[#One small step, fifty of them, and one jump]] ➡️

One coordinate at a time, with [a Gaussian](../../../Mathematics/references/textbooks/linear-algebra/matrix-cookbook.pdf#page=40) $x_0 \sim \mathcal{N}(m, v)$ and $\varepsilon \sim \mathcal{N}(0, 1)$ independent of it:

$$
\begin{aligned}
x_t &= \sqrt{\bar\alpha}\,x_0 + \sqrt{1 - \bar\alpha}\,\varepsilon \\
\mathbb{E}[x_t] &= \sqrt{\bar\alpha}\,\mathbb{E}[x_0] + \sqrt{1 - \bar\alpha}\,\mathbb{E}[\varepsilon] = \sqrt{\bar\alpha}\,m \\
\operatorname{Var}[x_t] &= \bar\alpha \operatorname{Var}[x_0] + (1 - \bar\alpha) \operatorname{Var}[\varepsilon] = \bar\alpha\,v + 1 - \bar\alpha
\end{aligned}
$$

The variances add because $x_0$ and $\varepsilon$ are independent, and each is multiplied by the square of its weight. Without the square roots, step 3's weights $0.5$ and $0.5$ give $0.25\,v + 0.25$ instead: $0.5$ and $1.25$, as it printed.

The worked numbers for expert 1, $m = (-2, 0)$ and $v = (1, 4)$:

$$
\begin{aligned}
\bar\alpha = 0.5: \quad & \text{mean } \sqrt{0.5} \times (-2) = -1.414, & \text{variance } & 0.5 \times 1 + 0.5 = 1.0, \quad 0.5 \times 4 + 0.5 = 2.5 \\
\bar\alpha = 0.0058: \quad & \text{mean } \sqrt{0.0058} \times (-2) = -0.152, & \text{variance } & 0.0058 \times 1 + 0.9942 = 1.0, \quad 0.0058 \times 4 + 0.9942 = 1.017
\end{aligned}
$$

The narrow axis has variance 1 at every level, because noise of variance 1 replaces signal of variance 1. For the step-by-step chain, $\bar\alpha = 0.9 \times 0.8 \times 0.95 \times 0.7 = 0.4788$, and the closed form gives mean $\sqrt{0.4788} \times 2 = 1.384$ and variance $1 - 0.4788 = 0.521$, as step 5 printed.

![Expert 1's cloud at the three levels, its centre sliding toward 0 and its two axes heading toward variance 1|800](assets/forward-process-the-mechanism.webp)

*The mechanism, expert 1's cloud at the three levels, its centre sliding toward 0 and its two axes heading toward variance 1.*

![The deep-dive sheet composing the form, the mechanism and the run|800](assets/forward-process-deep-dive-sheet.webp)

*The deep-dive sheet composing the form, the mechanism and the run.*

## One small step, fifty of them, and one jump

Navigation: ⬅️ [[#How the jump works]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to noise]] ➡️

**Each small step shrinks the point by $\sqrt{1 - \beta_t}$ and adds noise of variance $\beta_t$, $q(x_t \mid x_{t-1}) = \mathcal{N}(\sqrt{1 - \beta_t}\,x_{t-1},\ \beta_t I)$, and chaining the steps up to level $t$ gives the one jump with $\bar\alpha_t = \prod_{s=1}^{t}(1 - \beta_s)$.** After enough steps $q(x_T)$ is close to $\mathcal{N}(0, I)$. *Cited:* Du et al., Reduce, Reuse, Recycle, section 2.1, paragraph 1 (`text/related_work.tex` lines 7 to 8).

On the one-dimensional toy, expert a is $\mathcal{N}(-1, 0.5)$ and the cosine schedule has 100 levels (the schedule built in [[The Order Of Multiplying And Noising#Try the two orders yourself]]). Save this as `forward_chain.py`, with `betas` and `abar` from that schedule:

```python
rng = np.random.default_rng(0)
x0 = -1.0 + np.sqrt(0.5) * rng.standard_normal((100_000, 1))
xs = x0.copy()
for t in range(1, 51):
    xs = np.sqrt(1 - betas[t]) * xs + np.sqrt(betas[t]) * rng.standard_normal(xs.shape)
jump = np.sqrt(abar[50]) * x0 + np.sqrt(1 - abar[50]) * rng.standard_normal(x0.shape)
```

It printed:

```
expert a after 50 small steps: mean -0.7026, variance 0.7518
expert a after one jump to t = 50: mean -0.7024, variance 0.7445
closed form at abar = 0.493844: mean -0.702740, variance 0.753078
product of (1 - beta_s) for s = 1..50: 0.493844  (this is abar at t = 50)
product of (1 - beta_s) for s = 1..T, as equation A2's text prints it: 2.43e-07  (the same for every t)
```

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | 50 small steps, mean and variance | `-0.7026`, `0.7518` | the chain's cloud at level 50, from 100,000 points | shown |
| 2 | one jump, mean and variance | `-0.7024`, `0.7445` | the same level reached in one line; within the run's three-standard-error tolerance of 0.0082 for the mean and 0.0101 for the variance of the chain | shown |
| 3 | closed form at $\bar\alpha = 0.493844$ | `-0.702740`, `0.753078` | $\sqrt{\bar\alpha}\,(-1)$ and $0.493844 \times 0.5 + 1 - 0.493844$ | derived in [[#How the jump works]] |
| 4 | product of $(1 - \beta_s)$ up to 50 | `0.493844` | the signal share left at level 50 | shown |
| 5 | product of all 100 factors | `2.43e-07` | the signal share at level 100: nothing of the clean point is left, so $q(x_T)$ is $\mathcal{N}(0, I)$ to within that share | shown |

Level 50 on this schedule leaves $\bar\alpha = 0.4938$, so the "half the signal left" level used in [[The Order Of Multiplying And Noising]] ($\bar\alpha = 0.5$) sits at about level 50. *Inferred* from the 0.4938, not run at exactly 0.5 here; the exact-0.5 closed form is `-0.707107`, `0.750000`.

*Backing for the run:* `checks/forward_chain.py` and `checks/step5_noise_levels.out` in the journey's `sources/reduce-reuse-recycle/`, seed 0, re-run in an empty folder with the prepared environment and the same output.

## Other ways to noise

Navigation: ⬅️ [[#One small step, fifty of them, and one jump]] | 📋 [[#Table of contents|TOC]] | [[#Why the jump matters]] ➡️

- **The step-by-step chain**, as in step 5, when the intermediate states matter, as in a sampler that walks back down. One jump is the shortcut when only the end state is needed.
- **A noise scale without the shrink**, $x_t = x_0 + \sigma_t\,\varepsilon$, the variance-exploding form the paper's Appendix K uses. Its $\sigma_t$ corresponds to $\sqrt{1 - \bar\alpha}$ here, and the clean part is not scaled down. *Cited:* the walk's notation table, from the paper's Appendix K.

## Why the jump matters

Navigation: ⬅️ [[#Other ways to noise]] | 📋 [[#Table of contents|TOC]] | [[#The jump taught in, applied in]] ➡️

Training a diffusion model needs pairs of clean and noised points at random levels, and the jump makes each pair in one line. The paper's composition result holds at every noise level, so the clouds being composed in the next section are noised clouds, and this closed form says what they look like.

## The jump taught in, applied in

Navigation: ⬅️ [[#Why the jump matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the `drip-read` walk of the Mechanisms of Projective Composition paper note, step 3c, where the learner's `noised.py` printed level 0.5 as mean `[-1.41, -0]` and variance `[1, 2.51]`, within 0.05 of the closed form, with the closed-form print still owed
- the `drip-read` walk of Du et al., Reduce, Reuse, Recycle, section 2.1 paragraph 1 (the paper note is not written yet; link it here when it is): the single-step transition, and the agreement of 50 small steps with one jump on the toy
- the PoE derivation foundations journey's plan 09, `plans/09-the-forward-process.md`, task 1 at lines 138 to 168 (iterate the steps, then jump, and compare) and section 3 at lines 221 to 277 (derive the jump on paper)

**Applied in:** nothing yet.

**Before this note:** the learner's LibreOffice note `Artificial Intelligence/Machine Learning/Generative Models/Diffusion Models/Diffusion Models.odt` describes the forward process as a fixed Markov chain that adds Gaussian noise over $T = 1000$ steps and writes the single step $q(x_t \mid x_{t-1}) = \mathcal{N}(\sqrt{\alpha_t}\,x_{t-1}, (1 - \alpha_t) I)$, without the one-jump form.

> [!note]- How this was checked
> The shared setup and sources are in the box at the end of [[Diffusion Models]].
