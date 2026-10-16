---
aliases: [score, scores, the score, sample, samples, diffusion model, diffusion models, DDPM, denoising diffusion, forward process, forward diffusion, noising process, noising a cloud, closed-form forward process, q(x_t | x_0), "x_t = sqrt(abar) x_0 + sqrt(1 - abar) eps", alpha bar, abar, noise level, noise schedule level, composing diffusion models, composition of diffusion models, composition operator, composed distribution, compositional score, Definition 5.1, product of experts with a background, dividing out the background, background distribution, p_b, co-occurrence, hybrid, shared versus split, projective composition, the order of multiplying and noising, multiply then noise, noise each then multiply, noise-then-compose, compose-then-noise, score of a noised product, product of noised scores, sum of noised scores, summed score, summed scores, adding scores, why composition fails under reverse diffusion, reverse diffusion on a composed score, the sampler not the model, annealed MCMC, annealed Langevin, Algorithm 1, Reduce Reuse Recycle Algorithm 1, annealed MCMC sampling, steps per level, route A, route B, more levels do not help, Reverse (equal steps), mixtures commute with noising, Reduce Reuse Recycle equation 11, Reduce Reuse Recycle equation 12, energy parameterisation, energy parameterization, energy-based parameterisation, energy-based parameterization, energy-based diffusion model, energy-parameterised diffusion model, scalar energy, potential function, noise-conditional potential function, f_theta, "eps = -sigma_t grad f", unnormalised log density, unnormalized log-likelihood, accept step, accept-reject step, Metropolis correction, Metropolis-corrected sampler, Metropolis-adjusted Langevin, MALA, unadjusted Langevin, ULA, unadjusted Langevin algorithm, U-HMC, unadjusted HMC, acceptance rate, acceptance rate as a dial, share accepted, step size and the accept step, Langevin step-size bias, stability limit, 2 / P, light tails, lighter-than-Gaussian tails, transient chain, Table 1 of Reduce Reuse Recycle, sampler ladder, log-likelihood of samples, mixture composition, mixture of diffusion models, ratio of normalisers, Reduce Reuse Recycle equation 5, product of experts, product as an intersection, intersection of distributions, product of experts as intersection, the product's peak is a compromise, compromise peak, partly like each concept, Reduce Reuse Recycle equation 8, composition operators, compositional operators, product mixture and negation, AND OR NOT composition, mixture as a union, union of distributions, Reduce Reuse Recycle equation 9, negation, negation composition, negative prompt as negation, "q0 / q1^alpha", Reduce Reuse Recycle equation 10, guidance as a product, classifier-free guidance as a product of experts, classifier guidance as a product, which operators need heights, score models cannot mix, kinds of composition, types of composition, composition taxonomy, co-occurrence intersection interaction, intersection composition, interaction composition, interaction term, contention, chimera, concept bleeding, attribute leakage, catastrophic neglect, attribute binding, region-restricted product, product over a partition, product over the same variables, conditional independence of labels, wet dog, what an expert learns, an expert trained on A data learns concept A, a density expert learns its training set's density, labels in the DDPM loss, the loss never reads the label, hidden B, label noise in composition, contains A versus exactly A, conditioning scheme, multi-label conditioning, classifier guidance with missing labels, positive-unlabelled data, when neither training set holds A and B, compositional generalisation, compositional generalization, out-of-support generation, out-of-support composition, support of a product, intersection of supports, product's support is the intersection of supports, overlap removed, support kept from pretraining, pretraining support, expert that factorises over parts]
sources:
  - "Ho, Jain, Abbeel, Denoising Diffusion Probabilistic Models, NeurIPS 2020: https://arxiv.org/abs/2006.11239"
  - "Bradley, Nakkiran, Berthelot, Thornton, Susskind, Mechanisms of Projective Composition of Diffusion Models, ICML 2025: https://arxiv.org/abs/2502.04549"
  - "Du, Durkan, Strudel, Tenenbaum, Dieleman, Fergus, Sohl-Dickstein, Doucet, Grathwohl, Reduce, Reuse, Recycle: Compositional Generation with Energy-Based Diffusion Models and MCMC, ICML 2023: https://arxiv.org/abs/2302.11552"
  - "Wikipedia, Product of experts: https://en.wikipedia.org/wiki/Product_of_experts, read 2026-10-04, CC BY-SA 4.0"
  - "Hinton, Training Products of Experts by Minimizing Contrastive Divergence, Neural Computation 14(8), 1771 to 1800, 2002: https://doi.org/10.1162/089976602760128018"
  - "Liu, Li, Du, Torralba, Tenenbaum, Compositional Visual Generation with Composable Diffusion Models, ECCV 2022: https://arxiv.org/abs/2206.01714"
  - "Chefer, Alaluf, Vinker, Wolf, Cohen-Or, Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models, SIGGRAPH 2023: https://arxiv.org/abs/2301.13826"
  - "Bar-Tal, Yariv, Lipman, Dekel, MultiDiffusion: Fusing Diffusion Paths for Controlled Image Generation, ICML 2023: https://arxiv.org/abs/2302.08113"
  - "Geirhos, Jacobsen, Michaelis, Zemel, Brendel, Bethge, Wichmann, Shortcut Learning in Deep Neural Networks, Nature Machine Intelligence 2020: https://arxiv.org/abs/2004.07780"
---

# Diffusion Models

Artificial Intelligence, Generative Modeling. Needs: [[Multivariate Normal Distribution#Sampling a diagonal Gaussian]] for drawing a cloud, [[Multivariate Normal Distribution#Products and quotients of diagonal Gaussians]] for the arithmetic of composing, and [[NumPy#Broadcasting]] for noising many levels in one line.

> [!question] Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers [[#The forward process in one jump]], [[#Composing models with a background]] with the paper's figures, [[#Kinds of composition]], [[#What an expert learns from its training set]] and [[#When neither training set holds A and B]], in 41 questions. Your attempts are saved on the page.

> [!warning] Unfinished
> - One picture is still to be drawn: the deep-dive sheet for [[#Composing models with a background]], prompt 6 in the vault's `.prompts/Diffusion Models.md`. Its last render put the marked points off the note's saved figure, and it is stuck after three revisions.
> - Three pictures for [[#The order of multiplying and noising]] are waiting to be drawn: prompts 7, 8 and 9 in the same file.
> - Three pictures for [[#The energy parameterisation]] are waiting to be drawn: prompts 10, 11 and 12 in the same file.
> - One picture for [[#The product as an intersection]] is waiting to be drawn: prompt 13 in the same file.
> - Three pictures for [[#Product, mixture and negation]] are waiting to be drawn: prompts 14, 15 and 16 in the same file.
> - Two concept pictures are waiting to be drawn: [[#Annealed MCMC]], prompt 17, and [[#Step size and the accept step]], prompt 18, in the same file.
> - The quiz page covers the toy only; the paper's figures and [[#The product as an intersection]] added under [[#Composing models with a background]] are not in it yet, and [[#The order of multiplying and noising]] with [[#Annealed MCMC]], [[#The energy parameterisation]] with [[#Step size and the accept step]], and [[#Product, mixture and negation]] are not in it at all.
> - The reverse process is run in [[#Try the two orders yourself]] without a section of its own; it, the score and the training objective wait for a walk that reaches them.
> - [[#What an expert learns from its training set]] has not been run: this machine (the cluster) has no prepared environment `~/.vault-sandbox/bin/python`. Make it with `uv venv ~/.vault-sandbox` then `uv pip install --python ~/.vault-sandbox/bin/python pandas numpy scipy matplotlib statsmodels openpyxl`, run `labels.py`, and file its real output and output picture in place of the hand-worked lines.
> - Three pictures for [[#What an expert learns from its training set]] are waiting to be drawn: prompts 19, 20 and 21 in the same file. One concept picture for [[#Kinds of composition]] is waiting: prompt 22.
> - One concept picture for [[#When neither training set holds A and B]] is waiting to be drawn: prompt 23 in the same file.
> - The quiz page does not cover [[#Kinds of composition]], [[#What an expert learns from its training set]] or [[#When neither training set holds A and B]].
> - Every run below is a sandbox run. The overlap-dial idea and the idea of when a product reaches A and B, both in the reduce-reuse-recycle repository, apply [[#Kinds of composition]] and [[#What an expert learns from its training set]], in words only.
>
> Stated, not checked: 11 claims, marked where they sit.

**A diffusion model learns to undo a fixed noising process, and two trained models can be combined by multiplying what each believes and dividing out what they share.** This note covers the noising, written as one jump from a clean point to any noise level, and the composition rule that the Mechanisms of Projective Composition paper names in its Definition 5.1, both worked on the same small two-dimensional Gaussian clouds. It then shows, on a one-dimensional pair, why adding two models' scores and running the usual reverse process misses the product, and how annealed MCMC reaches the product with the same scores, and how a model that outputs one energy per input lets a sampler accept or reject each move, which holds the right width at any step size, and lets models be mixed, all following Reduce, Reuse, Recycle. It names the kinds of composition by which pixels each expert scores, and ends with what an expert learns from labelled data and what a product can reach when neither training set holds the combination. Every number can be checked by hand.

**Where you work.**

- Any terminal with Python 3, NumPy and Matplotlib. On the PC, that is Ubuntu under WSL, with the prepared environment `~/.vault-sandbox/bin/python`.
- A new empty folder. Nothing here touches a real project.

**Prepare the sandbox.**

```bash
mkdir -p ~/playground/sandbox/gaussian-clouds && cd ~/playground/sandbox/gaussian-clouds
~/.vault-sandbox/bin/python -c "import numpy; print(numpy.__version__)"
```

You should see a version number. This run printed `2.4.6`. If the environment is missing, [[Multivariate Normal Distribution#Try sampling yourself]] steps 1 and 2 say how to make it, or how to use `uv run` instead.

Both sections use the learner's `toy.py` and `samples.py`. Save them from [[Multivariate Normal Distribution#Try sampling yourself]], steps 3 and 5, into this folder.

## Table of contents

- [[#The forward process in one jump]]
- [[#Composing models with a background]]
- [[#The order of multiplying and noising]]
- [[#The energy parameterisation]]
- [[#Product, mixture and negation]]
- [[#What an expert learns from its training set]]

## The forward process in one jump

Navigation: 📋 [[#Table of contents|TOC]] | [[#Composing models with a background]] ➡️

**The forward process noises a clean point $x_0$ to level $\bar\alpha$ in one step, $x_t = \sqrt{\bar\alpha}\,x_0 + \sqrt{1 - \bar\alpha}\,\varepsilon$ with $\varepsilon \sim \mathcal{N}(0, I)$, so a cloud $\mathcal{N}(\mu, \sigma^2)$ becomes $\mathcal{N}(\sqrt{\bar\alpha}\,\mu,\ \bar\alpha\,\sigma^2 + 1 - \bar\alpha)$.** $\bar\alpha = 1$ is the clean data, and $\bar\alpha$ near 0 is almost pure noise. *Cited:* Ho et al., equation (4).

### When to reach for the jump

When you need a cloud at a given noise level without running every small step before it: to make training pairs, to see what a noise level does to two experts before composing them, or to check a toy against the closed form. The paper composes the experts after noising, at every level, so knowing what each level does to a cloud comes first.

### The form of the jump

```text
abar = np.array([<level 1>, <level 2>, ...])                    shape (L,); 1 is clean, near 0 is noise
a    = abar[:, None, None]                                       shape (L, 1, 1), one number per level
xt   = np.sqrt(a) * x0 + np.sqrt(1 - a) * rng.standard_normal((L, N, 2))     shape (L, N, 2)
mean: np.sqrt(level) * mu        variance: level * var + 1 - level            the closed form, per level
```

Both factors are square roots. They make the two parts' variances, $\bar\alpha$ and $1 - \bar\alpha$, add to 1 for unit-variance data.

![One clean cloud and one noise cloud mixed by the two square-root dials into the noised cloud|800](assets/forward-process-the-form.webp)

*The form, one clean cloud and one noise cloud mixed by the two square-root dials into the noised cloud.*

### Try the jump yourself

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

**6. Clean up, and prove it.** Keep the folder if you are going on to [[#Try composing yourself]]. Otherwise:

```bash
cd ~ && rm -r ~/playground/sandbox/gaussian-clouds
ls ~/playground/sandbox/gaussian-clouds; echo $?
```

You should see `No such file or directory`, then `2`.

### Reading the noised output

From step 4:

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | shape | `(3, 100000, 2)` | three levels, each a full cloud of 100,000 points in two coordinates | shown |
| 2 | level 0.5, measured mean | `[-1.41, 0.0]` | the cloud's centre moved toward 0 by $\sqrt{0.5} = 0.707$ | derived below |
| 3 | level 0.5, measured variance | `[1.0, 2.5]` | the narrow axis stayed at 1, the wide axis shrank from 4 toward 1 | derived below |
| 4 | level 0.5, closed form | `[-1.41, 0.0] [1.0, 2.5]` | $\sqrt{\bar\alpha}\,\mu$ and $\bar\alpha\,\sigma^2 + 1 - \bar\alpha$; equal to fields 2 and 3 | derived below |
| 5 | level 0.0058, measured variance | `[0.99, 1.02]` | almost pure noise: both axes close to 1, whatever the cloud was | derived below |

### How the jump works

One coordinate at a time, with [a Gaussian](../../Mathematics/references/textbooks/linear-algebra/matrix-cookbook.pdf#page=40) $x_0 \sim \mathcal{N}(m, v)$ and $\varepsilon \sim \mathcal{N}(0, 1)$ independent of it:

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

### One small step, fifty of them, and one jump

**Each small step shrinks the point by $\sqrt{1 - \beta_t}$ and adds noise of variance $\beta_t$, $q(x_t \mid x_{t-1}) = \mathcal{N}(\sqrt{1 - \beta_t}\,x_{t-1},\ \beta_t I)$, and chaining the steps up to level $t$ gives the one jump with $\bar\alpha_t = \prod_{s=1}^{t}(1 - \beta_s)$.** After enough steps $q(x_T)$ is close to $\mathcal{N}(0, I)$. *Cited:* Du et al., Reduce, Reuse, Recycle, section 2.1, paragraph 1 (`text/related_work.tex` lines 7 to 8).

On the one-dimensional toy, expert a is $\mathcal{N}(-1, 0.5)$ and the cosine schedule has 100 levels (the schedule built in [[#Try the two orders yourself]]). Save this as `forward_chain.py`, with `betas` and `abar` from that schedule:

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

Level 50 on this schedule leaves $\bar\alpha = 0.4938$, so the "half the signal left" level used in [[#The order of multiplying and noising]] ($\bar\alpha = 0.5$) sits at about level 50. *Inferred* from the 0.4938, not run at exactly 0.5 here; the exact-0.5 closed form is `-0.707107`, `0.750000`.

*Backing for the run:* `checks/forward_chain.py` and `checks/step5_noise_levels.out` in the journey's `sources/reduce-reuse-recycle/`, seed 0, re-run in an empty folder with the prepared environment and the same output.

### Other ways to noise

- **The step-by-step chain**, as in step 5, when the intermediate states matter, as in a sampler that walks back down. One jump is the shortcut when only the end state is needed.
- **A noise scale without the shrink**, $x_t = x_0 + \sigma_t\,\varepsilon$, the variance-exploding form the paper's Appendix K uses. Its $\sigma_t$ corresponds to $\sqrt{1 - \bar\alpha}$ here, and the clean part is not scaled down. *Cited:* the walk's notation table, from the paper's Appendix K.

### Why the jump matters

Training a diffusion model needs pairs of clean and noised points at random levels, and the jump makes each pair in one line. The paper's composition result holds at every noise level, so the clouds being composed in the next section are noised clouds, and this closed form says what they look like.

### The jump taught in, applied in

**Taught in:**

- the `drip-read` walk of the Mechanisms of Projective Composition paper note, step 3c, where the learner's `noised.py` printed level 0.5 as mean `[-1.41, -0]` and variance `[1, 2.51]`, within 0.05 of the closed form, with the closed-form print still owed
- the `drip-read` walk of Du et al., Reduce, Reuse, Recycle, section 2.1 paragraph 1 (the paper note is not written yet; link it here when it is): the single-step transition, and the agreement of 50 small steps with one jump on the toy
- the PoE derivation foundations journey's plan 09, `plans/09-the-forward-process.md`, task 1 at lines 138 to 168 (iterate the steps, then jump, and compare) and section 3 at lines 221 to 277 (derive the jump on paper)

**Applied in:** nothing yet.

**Before this note:** the learner's LibreOffice note `Artificial Intelligence/Machine Learning/Generative Models/Diffusion Models/Diffusion Models.odt` describes the forward process as a fixed Markov chain that adds Gaussian noise over $T = 1000$ steps and writes the single step $q(x_t \mid x_{t-1}) = \mathcal{N}(\sqrt{\alpha_t}\,x_{t-1}, (1 - \alpha_t) I)$, without the one-jump form.

## Composing models with a background

Navigation: ⬅️ [[#The forward process in one jump]] | 📋 [[#Table of contents|TOC]] | [[#The order of multiplying and noising]] ➡️

**Definition 5.1 of the Mechanisms of Projective Composition paper composes experts by multiplying them and dividing out the background once for each expert, $\mathcal{C}[p_b, p_1, p_2](x) = \frac{1}{Z}\,p_b(x)\,\frac{p_1(x)}{p_b(x)}\,\frac{p_2(x)}{p_b(x)}$, so each expert counts only where it differs from the background.** In score form, which is what a diffusion sampler adds, $\nabla \log \mathcal{C} = \nabla \log p_1 + \nabla \log p_2 - \nabla \log p_b$. *Cited:* the paper, equations (5) and (6).

### Words this uses

**Background**, $p_b$. The distribution of scenes with nothing in them: in the paper's images, an empty wall. In the toy below it is the wide round cloud $\mathcal{N}((0, 0), \operatorname{diag}(4, 4))$.

**Expert**, $p_i$. One model's distribution: scenes that contain object $i$. Where object $i$ is absent, an expert looks like the background.

**Co-occurrence.** Both objects in one scene, each in its own place. This is the composition you want.

**Hybrid.** One object that is a blend of both, at a value neither expert put there. This is the failure.

### The two-pixel picture

Treat each point $(x_0, x_1)$ as a tiny image with two pixels: $x_0$ is the left half of the scene and $x_1$ the right half. The paper's appendix maps coordinates to pixel regions the same way, with a mask $M_i$ around each object's location. *Cited:* the paper, Definition 5.2.

| Cloud | Mean | Variance | What it is in the scene |
|---|---|---|---|
| background $p_b$ | $(0, 0)$ | $(4, 4)$ | the empty wall |
| expert 1 | $(-2, 0)$ | $(1, 4)$ | an object in the left half: $x_0$ moves to $-2$, and $x_1$ stays exactly like the wall |
| expert 2, split | $(0, 2)$ | $(4, 1)$ | an object in the right half: $x_1$ moves to $2$, and $x_0$ stays like the wall |
| expert 2, shared | $(2, 0)$ | $(4, 1)$ | a different object in the left half: $x_0$ moves to $+2$. It also narrows the right half from variance 4 to 1, with its mean still 0, so it is not purely a left-half object |

In split, the experts want different pixels. In shared, both want the left pixel, one at $-2$ and the other at $+2$.

![The paper's Figure 2: four models that each draw one object at its own place on an empty floor, composed into scenes holding one, two, three and four objects|800](references/composition-paper-figure-2-one-object-per-model.png)

> **Figure 2.** Length-generalization, another capability of composition enabled by our framework. Diffusion models trained to generate a single object conditioned on location (left) can be composed at inference-time to generate images of multiple objects at specified locations (right). Notably, such images are strictly out-of-distribution for the individual models being composed. (Additional samples in Figure 10.)
>
> *Bradley et al., Mechanisms of Projective Composition of Diffusion Models, ICML 2025, [arXiv 2502.04549](https://arxiv.org/abs/2502.04549), Figure 2. arXiv non-exclusive distribution licence; copied for study with citation.*

This is split at image scale: each model $p_i$ moves only the patch where its object sits and leaves the rest of the floor like the empty background $p_b$, so composing them puts every object in one scene, as the toy's split puts $-2$ in the left half and $2$ in the right. *Shown* in the figure, with the caption.

### Why the background is divided out

On a half it does not care about, an expert repeats the wall. Multiply two experts and the wall's opinion of that half is counted twice. Dividing by $p_b$ once removes the extra copy. In split's right half, expert 1 is $\mathcal{N}(0, 4)$, identical to the wall, so $p_1 / p_b = 1$ there and only expert 2 decides: the composed right half is $\mathcal{N}(2, 1)$. Left in, the extra copy of the wall pulls it to $1.6$.

### When to reach for the composition rule

When two conditions should both appear in one sample: a cat and a dog, a red cube and a blue sphere. A diffusion sampler adds the two conditional scores and subtracts the unconditional one, and Definition 5.1 says which distribution that sum is the score of. The rule gives co-occurrence when each expert owns its own pixels and differs from the background only there (split). When two experts want the same pixels (shared), it returns a hybrid.

![The paper's Figure 1: photos of one dog plus Van Gogh's Starry Night give an oil painting of that dog|800](references/composition-paper-figure-1-content-and-style.png)

> **Figure 1.** Composing diffusion models via score combination. Given two diffusion models, it is sometimes possible to sample in a way that composes content from one model (e.g. your dog) with style of another model (e.g. oil paintings). We aim to theoretically understand this empirical behavior. Figure generated via score composition with SDXL fine-tuned on the author's dog; details in Appendix C.
>
> *Bradley et al., Mechanisms of Projective Composition of Diffusion Models, ICML 2025, [arXiv 2502.04549](https://arxiv.org/abs/2502.04549), Figure 1. arXiv non-exclusive distribution licence; copied for study with citation.*

The everyday use of the rule: one model supplies what is in the picture, the other how it is painted. The caption's "sometimes" is the question this section answers, and Figure 8 under [[#Why composition matters]] is the paper's guess at when. *Cited:* the caption.

### The form of a composition

```text
C[p_b, p_1, ..., p_k](x) = (1/Z) * p_b(x) * prod_i ( p_i(x) / p_b(x) )     the composed density
grad log C = sum_i grad log p_i  -  (k - 1) * grad log p_b                  the compositional score
for two experts:  C = p_1 * p_2 / p_b                                       one background divided out
```

For diagonal Gaussians, `p_1 * p_2 / p_b` is computed one coordinate at a time by adding and subtracting precisions, as in [[Multivariate Normal Distribution#Products and quotients of diagonal Gaussians]].

![The two-pixel scene as a wall with an object in each half, and the rule multiplying the two experts and dividing out one wall|800](assets/composition-the-form.webp)

*The form, the two-pixel scene as a wall with an object in each half, and the rule multiplying the two experts and dividing out one wall.*

### Try composing yourself

**1. What you need, and when it is missing.** As in the sandbox preparation above, with Matplotlib.

**2. Make something to act on.** `toy.py` in `~/playground/sandbox/gaussian-clouds`. Its `shared` and `split` lists hold the four clouds of [[#The two-pixel picture]].

**3. Look at it before.** The experts as clouds, shared beside split, are drawn in [[Multivariate Normal Distribution#Try sampling yourself]] step 7. Before plotting, the walk asked where expert 1 and expert 2 overlap. The learner predicted "blue and orange overlap more around the origin, and the origin is the centre of the overlap". The answer key's run, in [[Multivariate Normal Distribution#Try composing yourself]] step 3, puts the overlap at $(-1.2, 0)$ for shared and $(-1.6, 1.6)$ for split, with no background in the product.

**4. The failure, and the technique, in one picture.** Save this as `picture.py`. For each version it draws the wall in grey, expert 1 in blue and expert 2 in orange, each as the contour at 30% of its peak height. It marks the plain product $p_1 p_2$ with a purple cross and the composition $p_1 p_2 / p_b$ with a green dot and a green filled contour:

```python
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from toy import shared, split

g = np.linspace(-7, 7, 401)
X0, X1 = np.meshgrid(g, g)

def dens(m, v):
    return np.exp(-(X0 - m[0])**2 / (2 * v[0]) - (X1 - m[1])**2 / (2 * v[1]))

fig, axes = plt.subplots(1, 2, figsize=(11, 5.4), sharex=True, sharey=True)
for ax, (title, ps) in zip(axes, [("split: expert 2 owns the right half", split), ("shared: both experts want the left half", shared)]):
    (mb, vb), (m1, v1), (m2, v2) = ps
    P = 1 / v1 + 1 / v2 - 1 / vb
    m = (m1 / v1 + m2 / v2 - mb / vb) / P
    Pn = 1 / v1 + 1 / v2
    mn = (m1 / v1 + m2 / v2) / Pn
    ax.contour(X0, X1, dens(mb, vb), levels=[0.3], colors="0.6")
    ax.contour(X0, X1, dens(m1, v1), levels=[0.3], colors="tab:blue")
    ax.contour(X0, X1, dens(m2, v2), levels=[0.3], colors="tab:orange")
    ax.contourf(X0, X1, dens(m, 1 / P), levels=[0.3, 1.01], colors="tab:green", alpha=0.35)
    ax.plot(*m, "o", c="tab:green", ms=8)
    ax.plot(*mn, "x", c="tab:purple", ms=10, mew=2)
    ax.annotate(f"p1 p2 / p_b: ({m[0]:.1f}, {m[1]:.1f})", m, (-6.6, 5.6), color="tab:green", fontsize=11,
                arrowprops=dict(arrowstyle="->", color="tab:green"))
    ax.annotate(f"p1 p2, wall counted twice: ({mn[0]:.1f}, {mn[1]:.1f})", mn, (-6.6, -5.6), color="tab:purple", fontsize=11,
                arrowprops=dict(arrowstyle="->", color="tab:purple"))
    ax.text(2.3, -2.9, "p_b, the wall", color="0.45")
    ax.text(-3.6, -3.6, "p_1", color="tab:blue", fontsize=11)
    ax.text(*((3.6, 3.4) if m2[1] > 0 else (4.2, -1.4)), "p_2", color="tab:orange", fontsize=11)
    ax.axhline(0, c="0.85", lw=0.8); ax.axvline(0, c="0.85", lw=0.8)
    ax.set(title=title, xlim=(-7, 7), ylim=(-7, 7), aspect="equal", xlabel="x0, the left half", ylabel="x1, the right half")
fig.tight_layout()
fig.savefig("composition-split-and-shared.png", dpi=110)
print("saved composition-split-and-shared.png")
```

```bash
~/.vault-sandbox/bin/python picture.py
```

```text
saved composition-split-and-shared.png
```

![Split composes to (-2, 2), each object in its own half; shared composes to (-1.5, 0), one blended value in the left half|900](assets/composition-split-and-shared.png)

On the left, split: the green dot sits at $(-2, 2)$, expert 1's left value and expert 2's right value together. That is co-occurrence. The purple cross at $(-1.6, 1.6)$ is the product with the wall left in, pulled 0.4 toward the middle on both halves. On the right, shared: the green dot sits at $(-1.5, 0)$. The left half is $-1.5$, a value neither expert wanted, so the result is a hybrid, and dividing out the wall does not rescue it.

**5. Another way to get the same answer.** `compose.py` in [[Multivariate Normal Distribution#Try composing yourself]] step 5 prints the same four centres by precisions, and `grid_check.py` in step 6 there finds them without any formula.

**6. Clean up, and prove it.**

```bash
cd ~ && rm -r ~/playground/sandbox/gaussian-clouds
ls ~/playground/sandbox/gaussian-clouds; echo $?
```

You should see `No such file or directory`, then `2`.

### Reading the composition picture

| # | Mark | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | split, green dot | $(-2.0, 2.0)$ | each half took its own expert's value: co-occurrence | derived below |
| 2 | split, purple cross | $(-1.6, 1.6)$ | the plain product: the wall, counted twice, pulls both halves 20% toward 0 | derived below |
| 3 | shared, green dot | $(-1.5, 0.0)$ | the left half lands between $-2$ and $+2$: a hybrid | derived below |
| 4 | shared, purple cross | $(-1.2, 0.0)$ | the plain product, pulled further toward 0 | derived below |
| 5 | green filled contour | variance 1 on each axis | the composed cloud is round in both versions | derived below |

### How composition works

Per coordinate, with precision $P = 1/v_1 + 1/v_2 - 1/v_b$ and $B = m_1/v_1 + m_2/v_2 - m_b/v_b$, the composed mean is $B/P$ and the variance $1/P$. The derivation, step by step, is [[Multivariate Normal Distribution#How the product works]], and the formula in print is the [product of Gaussian densities](../../Mathematics/references/textbooks/linear-algebra/matrix-cookbook.pdf#page=42). The four halves of the toy:

$$
\begin{aligned}
\text{split, left: } & P = \tfrac{1}{1} + \tfrac{1}{4} - \tfrac{1}{4} = 1, & B &= \tfrac{-2}{1} + \tfrac{0}{4} - 0 = -2, & \text{mean } -2 \\
\text{split, right: } & P = \tfrac{1}{4} + \tfrac{1}{1} - \tfrac{1}{4} = 1, & B &= \tfrac{0}{4} + \tfrac{2}{1} - 0 = 2, & \text{mean } 2 \\
\text{shared, left: } & P = \tfrac{1}{1} + \tfrac{1}{4} - \tfrac{1}{4} = 1, & B &= \tfrac{-2}{1} + \tfrac{2}{4} - 0 = -1.5, & \text{mean } -1.5 \\
\text{shared, right: } & P = \tfrac{1}{4} + \tfrac{1}{1} - \tfrac{1}{4} = 1, & B &= \tfrac{0}{4} + \tfrac{0}{1} - 0 = 0, & \text{mean } 0
\end{aligned}
$$

In every half where one expert equals the wall, that expert's precision cancels the wall's, and the other expert decides alone. Shared's right half is $\mathcal{N}(0, 1)$: expert 2 narrowed it. Shared's left half is the one place where neither expert equals the wall, so both pull, weighted by their precisions 1 and $\frac{1}{4}$, and the mean lands at $-1.5$.

With the wall left in, drop the $-\frac{1}{4}$ terms: $P = 1.25$ on every half, and split's right half becomes $2 / 1.25 = 1.6$.

This toy is the paper's simplest setting, where each expert's projection is a coordinate restriction. Its Theorem 5.3 states the condition under which the composition is correct and can be sampled by reverse diffusion. *Cited:* the walk's read-ahead, `read-ahead/05-simple-construction.md`, chunks 47 to 49. The walk reaches it later; this section shows only the composed density.

The paper calls a composition correct when it is projective: seen through each expert's own window, the result looks exactly like that expert.

![The paper's Figure 4: the composed blob seen through two projection directions, each shadow matching one expert's shadow|800](references/composition-paper-figure-4-projective-composition.png)

> **Figure 4.** Distribution $\hat{p}$ is a projective composition of $p_1$ and $p_2$ w.r.t. projection functions $(\Pi_1, \Pi_2)$, because $\hat{p}$ has the same marginals as $p_1$ when both are post-processed by $\Pi_1$, and analogously for $p_2$.
>
> *Bradley et al., Mechanisms of Projective Composition of Diffusion Models, ICML 2025, [arXiv 2502.04549](https://arxiv.org/abs/2502.04549), Figure 4. arXiv non-exclusive distribution licence; copied for study with citation.*

In the toy, $\Pi_1$ keeps $x_0$ and $\Pi_2$ keeps $x_1$. Split passes the test: the composed left half is $\mathcal{N}(-2, 1)$, the same as expert 1's left half, and the composed right half is $\mathcal{N}(2, 1)$, the same as expert 2's right half. Shared fails it: its composed left half, $\mathcal{N}(-1.5, 1)$, matches neither expert 1's $\mathcal{N}(-2, 1)$ nor expert 2's $\mathcal{N}(2, 4)$. *Derived* from the four halves above.

![The paper's Figure 5: yellow objects composed with eight other colours, with R, G and B histograms showing which colours share yellow's B channel|800](references/composition-paper-figure-5-yellow-with-other-colours.png)

> **Figure 5.** **Composing yellow objects with objects of other colors.** Yellow objects successfully compose with blue, cyan and magenta objects but not with brown, gray, green, or red objects. Per the histograms (left), in RGB-colorspace yellow has R, G distributed like the background (gray) while B has a distinct distribution peaked closer to zero. Taking $M_\text{yellow} \approx \{B\}$, Theorem 5.3 predicts that standard diffusion can sample from compositions of yellow with any color where the B channel is distributed like the background: namely, blue, cyan, magenta per the histograms. (Other colors may theoretically compose per Theorem 6.1, but be difficult to sample.) (Additional samples in Figure 11.)
>
> *Bradley et al., Mechanisms of Projective Composition of Diffusion Models, ICML 2025, [arXiv 2502.04549](https://arxiv.org/abs/2502.04549), Figure 5. arXiv non-exclusive distribution licence; copied for study with citation.*

The same test on colour channels in place of pixels. Yellow differs from the grey background only in its B channel, the way expert 1 differs from the wall only in $x_0$. Blue, cyan and magenta keep B like the background, which is split, and they compose (ticks). Brown, gray, green and red move B too, which is shared, and their samples mostly hold a single object (crosses). The histograms sit on the right of the picture, although the caption says left. *Shown* in the figure, with the caption.

![The wall cancelling in each half an expert does not touch, and the two pulls meeting in shared's left half|800](assets/composition-the-mechanism.webp)

*The mechanism, the wall cancelling in each half an expert does not touch, and the two pulls meeting in shared's left half.*

*🖼️ Diagram wanted: the deep-dive sheet composing the form, the mechanism and the picture. Prompt 6 in the same file.*

### Other ways to compose

- **The plain product $p_1 p_2$**, the product of experts with no background. It counts the wall once per extra expert, so its centres sit nearer the middle, as the purple crosses show.
- **The Bayes composition**, $\nabla \log p_1 + \nabla \log p_2 - \nabla \log p_{\text{uncond}}$, two conditional scores minus the unconditional one. It is Definition 5.1 with the unconditional distribution as the background, and the paper's equation (1) is an instance of it. *Cited:* the walk's read-ahead, `read-ahead/03-prior-definitions.md`, on chunks 13 and 42.
- **Sampling-side corrections**, such as the annealed MCMC samplers of Du et al. (arXiv 2302.11552), which fix how the sum is sampled and leave the target density unchanged. [[#The order of multiplying and noising]] shows why the plain reverse process misses the target and how annealed Langevin reaches it. *Cited:* Du et al., abstract sentence 6 and section 4.1.

Choosing the unconditional model as the background, the Bayes composition, is where the rule most often goes wrong. The paper shows it on images and on exact-score toys.

![The paper's Figure 3: three experiments composing one to nine location models, the empty background succeeding up to four objects, the unconditional background failing from two, the cluttered background succeeding up to eight|900](references/composition-paper-figure-3-up-to-nine-objects.png)

> **Figure 3.** **Attempted compositional length-generalization up to 9 objects.** We attempt to compose via linear score combination the distributions $p_1$ through $p_9$ shown on the far left, where each $p_i$ is conditioned on a specific object location as described below. Settings (A) and (C) approximately satisfy the conditions of our theory of projective composition, and thus are expected to length-generalize at least somewhat, while setting (B) does not even approximately satisfy our conditions and indeed fails to length-generalize. **Experiment (A):** In this experiment, the distributions $p_i$ each contain a single object at a fixed location, and the background $p_b$ is empty. In this case any successful composition of more than one object represents length-generalization. We find that composition succeeds up to several objects, but then degrades as number of objects increases (see Section 5.3 for details). **Experiment (B):** Here the distributions $p_i$ are identical to (A), but the background $p_b$ is chosen as the unconditional distribution (i.e. a single object at a random location)— this the "Bayes composition" (Section 3). This composition entirely fails— remarkably, trying to compose many objects often produces no objects! **Experiment (C):** Here each distribution $p_i$ contains an object at a fixed location $i$, and 0-4 other objects (sampled uniformly) in random locations. The background distribution $p_b$ is a distribution of 1-5 objects (sampled uniformly) in random locations. In this case length-generalization means composition of more than 5 objects. This composition can length-generalize, but artifacts appear for large numbers of objects. See Section 5.3 for further discussion, and Table 1 for a quantitative analysis. In Section L we explore another configuration that improves length-generalization quality.
>
> *Bradley et al., Mechanisms of Projective Composition of Diffusion Models, ICML 2025, [arXiv 2502.04549](https://arxiv.org/abs/2502.04549), Figure 3. arXiv non-exclusive distribution licence; copied for study with citation.*

Column (A) is the toy's split with the empty wall as background, and it holds up to four objects before the scenes turn to coloured blobs. Column (B) keeps the same experts and swaps the wall for the unconditional model, which holds one object at a random place. Each expert's scene is empty away from its own object and this background is not, so the experts no longer differ from the background only on their own patch, and from two experts on the scenes come out with fewer objects than asked for, often none. *Cited:* the walk's read-ahead, `read-ahead/03-prior-definitions.md`, chunks 28 to 33.

![The paper's Figure 12, left: on 8-dimensional vectors, the empty background lights columns 0, 2, 4 and 6 brightly and the Bayes composition only dimly|440](references/composition-paper-figure-12-left-empty-background.png) ![The paper's Figure 12, right: with a cluttered background, both compositions light columns 0, 2, 4 and 6|440](references/composition-paper-figure-12-right-cluttered-background.png)

> **Figure 12.** Bayes composition vs. projective composition. All experiments use exact scores, which is possible since the diffusion-noised distributions are Gaussian mixtures. (Left) Distributions follow (17): each conditional $p_i$ activates index $i$ only, unconditional $p_u$ averages over the $p_i$, and background $p_b$ is all-zeros. We attempt to compose the conditions $p_0, p_2, p_4, p_6$ and hope to obtain the result $[1, 0, 1, 0, 1, 0]$. This requires length-generalization, since each of the conditionals $p_i$ contains only a single 1. The composition using the empty background $p_b$ (top) achieves this goal, while the Bayes composition using the unconditional $p_u$ (bottom) does not. Note that $[p_b, p_1, p_2, \ldots]$ satisfy Definition 5.2 while $[p_u, p_1, p_2, \ldots]$ does not. (Right) Distributions follow (18), where each conditional $p_i$ activates index $i$ on an independently 'cluttered' background. In this case the unconditional is similar to the cluttered background. Again we attempt to compose $p_0, p_2, p_4, p_6$, and in this case we find that the composition using $p_u$ works similarly well to $p_b$.
>
> *Bradley et al., Mechanisms of Projective Composition of Diffusion Models, ICML 2025, [arXiv 2502.04549](https://arxiv.org/abs/2502.04549), Figure 12, left and right panels. arXiv non-exclusive distribution licence; copied for study with citation.*

Figure 3's (A) against (B), with no trained model in the way. In each heatmap the columns are the eight coordinates; in the right-hand panels each row is one sample. On the left, the empty background lights columns 0, 2, 4 and 6 brightly in every row, and the Bayes composition lights them at about half strength. On the right, with a cluttered background, both light the same columns. The caption's target lists six entries where the panels have eight columns. *Shown:* read by eye from the panels.

### The product as an intersection

**Multiplying experts gives a density that is tall only where every expert is at least somewhat tall, which is why Du et al. call the product an "intersection"; its peak is a compromise between the experts, at a point where none of them is at its best.** *Cited:* Du et al., Reduce, Reuse, Recycle, section 3, paragraph 2 (`text/method.tex` lines 10 to 19): "Regions of high probability under $q^\text{prod}(x)$ will typically have high probability under *all* $q^i(x)$." The word "typically" matters, because the product's peak need not sit where any single expert peaks.

**When to reach for it.** When a composed sample looks like neither concept in full. The product rewards points that are partly like each expert, so a sample that is half of each is what the product asks for. Co-occurrence, a dog and a cat both present, needs places where every expert is high at once. Where those places barely overlap, the product picks the point in between. *Derived* from the product's definition, and shown on numbers below.

**Try it yourself.** The two experts are the pair in [[#The one-dimensional pair]], $a = \mathcal{N}(-1, 0.5)$ and $b = \mathcal{N}(1, 0.8)$, with a second pair of the same widths pulled apart to $\pm 4$.

1. You need the prepared environment: `~/.vault-sandbox/bin/python -c "import numpy, matplotlib"` prints nothing when both are there. If it fails, [[Multivariate Normal Distribution#Try sampling yourself]] steps 1 and 2 say how to make it.
2. Make an empty folder:

   ```bash
   mkdir -p ~/playground/sandbox/product-intersection && cd ~/playground/sandbox/product-intersection
   ```

3. Save this as `intersection.py`. For each pair it multiplies the experts point by point, divides by the area, finds the tallest point, and reads each expert's height there against that expert's own peak:

   ```python
   # Where a product of two experts is tall, and how tall each expert is there.
   import numpy as np
   import matplotlib
   matplotlib.use("Agg")
   import matplotlib.pyplot as plt

   def gauss(x, m, v):
       return np.exp(-(x - m) ** 2 / (2 * v)) / np.sqrt(2 * np.pi * v)

   x = np.linspace(-8, 8, 1601)                     # grid spacing 0.01
   dx = x[1] - x[0]
   pairs = {"near": ((-1.0, 0.5), (1.0, 0.8)),      # the chunk's pair
            "far":  ((-4.0, 0.5), (4.0, 0.8))}      # the same widths, pulled apart

   fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
   for ax, (name, ((ma, va), (mb, vb))) in zip(axes, pairs.items()):
       qa, qb = gauss(x, ma, va), gauss(x, mb, vb)
       raw = qa * qb
       Z = raw.sum() * dx
       prod = raw / Z
       i = int(prod.argmax())
       peak = (ma / va + mb / vb) / (1 / va + 1 / vb)   # precision-weighted mean
       print(f"{name}: product peaks at x = {x[i]:.2f} (closed form {peak:.4f}), area before dividing Z = {Z:.3g}")
       print(f"{name}: there, a is {qa[i]:.3g} against its own peak {qa.max():.3g}, {100 * qa[i] / qa.max():.3g}%")
       print(f"{name}: there, b is {qb[i]:.3g} against its own peak {qb.max():.3g}, {100 * qb[i] / qb.max():.3g}%")
       ax.plot(x, qa, color="tab:blue", label="expert a")
       ax.plot(x, qb, color="tab:orange", label="expert b")
       ax.plot(x, prod, color="tab:green", label="product, divided by Z")
       ax.axvline(x[i], color="grey", lw=0.8, ls="--")
       ax.set_xlim(-6, 6); ax.set_title(f"{name}: a = N({ma}, {va}), b = N({mb}, {vb})")
       ax.set_xlabel("x"); ax.set_ylabel("height")
   axes[0].legend(frameon=False)
   fig.tight_layout()
   fig.savefig("intersection.png", dpi=120)
   ```

4. Run it:

   ```bash
   ~/.vault-sandbox/bin/python intersection.py
   ```

   You should see:

   ```
   near: product peaks at x = -0.23 (closed form -0.2308), area before dividing Z = 0.0751
   near: there, a is 0.312 against its own peak 0.564, 55.3%
   near: there, b is 0.173 against its own peak 0.446, 38.8%
   far: product peaks at x = -0.92 (closed form -0.9231), area before dividing Z = 7.14e-12
   far: there, a is 4.28e-05 against its own peak 0.564, 0.00759%
   far: there, b is 1.2e-07 against its own peak 0.446, 2.69e-05%
   ```

   ![The run's six lines, with the product's peak and each expert's share of its own peak marked 1 to 6|800](assets/intersection-heights-at-the-product-peak.png)

   and the saved `intersection.png`:

   ![Left, the near pair: the green product peaks at -0.23 between the blue and orange experts, where both are partly tall. Right, the far pair: the green product peaks at -0.92 in the gap, where both experts are flat|900](assets/intersection-the-product-peaks-between-the-experts.png)

5. Clean up, and check the folder is gone:

   ```bash
   cd ~ && rm -r ~/playground/sandbox/product-intersection
   ls ~/playground/sandbox/product-intersection; echo $?
   ```

   You should see `No such file or directory` and `2`.

**Reading the intersection output.**

| # | Field | Value | How to read it | Backing |
|---|---|---|---|---|
| 1 | near, product peak | `-0.23` | between the experts' peaks at $-1$ and $1$, nearer $a$ because $a$ is narrower; the closed form agrees | derived below |
| 2 | near, $a$ at the peak | `55.3%` | expert $a$ is at a little over half its own best | shown, derived below |
| 3 | near, $b$ at the peak | `38.8%` | expert $b$ is at under two fifths of its own best. Neither is at its best; both are partly satisfied | shown, derived below |
| 4 | far, product peak | `-0.92` | the same weighted average of $-4$ and $4$, in the gap between them. `Z = 7.14e-12` is the area the raw product had: almost nothing overlaps | derived below |
| 5 | far, $a$ at the peak | `0.00759%` | expert $a$ gives this point almost no weight | shown |
| 6 | far, $b$ at the peak | `2.69e-05%` | nor does expert $b$. After dividing by $Z$ the product is still a full-height bell, centred on a point neither expert believes in | shown |

**How the intersection works.** The product's peak is the [[Multivariate Normal Distribution#How the product works|precision-weighted mean]] of the experts' means, worked there step by step:

$$x^\star = \frac{m_a/v_a + m_b/v_b}{1/v_a + 1/v_b} = \frac{-2 + 1.25}{3.25} = -0.230769$$

A Gaussian's height at $x$, as a share of its own peak, is $e^{-(x - m)^2 / (2v)}$, because the normalising constant cancels in the ratio:

$$\frac{q_a(x^\star)}{q_a(m_a)} = e^{-(0.769231)^2 / 1.0} = e^{-0.591716} = 0.5534$$

$$\frac{q_b(x^\star)}{q_b(m_b)} = e^{-(-1.230769)^2 / 1.6} = e^{-0.946746} = 0.3880$$

*Derived.* These match fields 2 and 3. For the far pair, $x^\star = (-8 + 5)/3.25 = -0.923077$, and the shares are $e^{-9.467456} = 7.73 \times 10^{-5}$ and $e^{-15.147929} = 2.64 \times 10^{-7}$. The run reads them at the grid point $-0.92$, which gives the slightly different $7.59 \times 10^{-5}$ and $2.69 \times 10^{-7}$ of fields 5 and 6.

Moving the experts apart never moves the peak away from the weighted average, and never shrinks the bell after dividing by $Z$. It only drives down how much either expert agrees with the peak. Du et al.'s appendix E shows the failure this leads to: "Our approach fails to generate products of distributions with no overlap". *Cited:* `text/appendix.tex` line 306. The walk reaches that figure at chunk 142.

**Why the intersection matters.** This is the one-dimensional picture of a hybrid. The background-divided toy above lands on $-1.5$ in shared's left half for the same reason: a product lands on points that are partly like each concept. The plain product has no background to divide out, so it shows the compromise with nothing else in the way.

![The product as an intersection, two experts and their product with each expert's share at the product's peak|800](assets/intersection-the-concept.webp)

*The product as an intersection, two experts and their product with each expert's share at the product's peak.*

**Taught in:** the `drip-read` walk of Du et al., Reduce, Reuse, Recycle, section 3, paragraph 2, chunk 34 (the product as an intersection, and the heights at its peak from the walk's answer key `checks/step6_product.out`). The walk's paper note, `deep-learning/diffusion-models/02-sampler-correctors-for-composition/papers/reduce-reuse-recycle/reduce-reuse-recycle.md` in this vault, is not written yet; link it here when it is.

### Why composition matters

The rule produces co-occurrence exactly when each expert differs from the background only on its own pixels. When two experts compete for the same pixels, it produces a hybrid, and no sampler can fix that, because the hybrid is the target density itself. This is the reading the learner's PhD proposal tests against the paper.

![The paper's Figure 7: "photo of a dog" plus "photo of a horse" gives one shaggy animal with a horse's body, "photo of a dog" plus "photo, with red hat" gives a dog wearing a red hat|800](references/composition-paper-figure-7-dog-horse-and-dog-hat.png)

> **Figure 7.** **Composing Entangled Concepts.** The left image composes the text-conditions "photo of a dog" with "photo of a horse", which both control the subject of the image, and produces unexpected results. In contrast, the right image composes "photo of a dog" with "photo, with red hat," which intuitively correspond to disentangled features. Both samples from SDXL using score-composition with an unconditional background; details in Appendix C.
>
> *Bradley et al., Mechanisms of Projective Composition of Diffusion Models, ICML 2025, [arXiv 2502.04549](https://arxiv.org/abs/2502.04549), Figure 7. arXiv non-exclusive distribution licence; copied for study with citation.*

The left image is the toy's shared case at full scale. Both prompts want the subject, the way both experts want $x_0$, and the result is one animal with a horse's body and stance under a dog's shaggy coat and head: a hybrid, like the toy's $-1.5$. The right image is split. The hat owns the top of the head, the dog owns the rest, and both appear. *Shown:* the animal's description is read by eye from the picture.

![The paper's Figure 8: two heatmaps of cosine similarity between concepts' CLIP directions, bright within dog, horse and cat and dim between dog and hat|800](references/composition-paper-figure-8-clip-cosine-similarity.png)

> **Figure 8.** Cosine similarity ($\frac{u^tv}{\|u\|\|v\|}$) between mean difference vectors $\mu_i - \mu_b$ and $\mu_j - \mu_b$, for each pair of concepts $i,j$, with $\mu_i$ estimated as either the average CLIP image embedding over several images representative of concept $i$ (left) or the CLIP text embedding for a single text description of concept $i$ (right). Details in Section D. Note that the groups of concepts {"dog", "horse", "cat"}, {"watercolor", "oil-painting"}, {"hat", "sunglasses"} have high intra- and low inter-group similarity. This suggests that concepts from different groups may successfully compose (such as "dog"+"hat" or "dog"+"oil-painting"), while concepts from the same group may not (such as "dog"+"horse"), consistent with the examples in Figures 1 and 7.
>
> *Bradley et al., Mechanisms of Projective Composition of Diffusion Models, ICML 2025, [arXiv 2502.04549](https://arxiv.org/abs/2502.04549), Figure 8. arXiv non-exclusive distribution licence; copied for study with citation.*

A way to tell shared from split before sampling. Each concept's direction away from the background, $\mu_i - \mu_b$, plays the part of the toy's "which half does this expert move". Split experts move different halves, so their directions are perpendicular and the cosine is 0. Read off the colour bar by eye, dog against horse is about 0.55 on image embeddings and 0.7 on text, while dog against hat is about 0.4 and 0.25, and Figures 7 and 1 came out as those numbers predict. The toy's split directions are $(-2, 0)$ and $(0, 2)$, with cosine exactly 0. Shared's are $(-2, 0)$ and $(2, 0)$, with cosine $-1$. *Derived* from the toy's means and the background mean $(0, 0)$.

The learner's [Gaussian Bowl Sketchpad](https://claude.ai/artifact/2TarMifiFoFyoB23eQFR64) shows one Gaussian's density as a surface. A page for this composition, with the wall, the two experts and the composed cloud, is being built in the journey's `artifacts/scenes/mechanisms-of-projective-composition/` and is not published yet.

### Kinds of composition

**"Composition" names at least three different operations, told apart by which variables each expert scores. Co-occurrence is a product over disjoint regions plus a layout. Intersection is a product over the same variables, which is what a product of experts computes. Interaction is the product plus a term that vanishes when the two labels are [conditionally independent](../../Mathematics/references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=201) given the image.** The operators are *derived* below. The three names are the walk's working names; the field's words for each are in the table.

**When to reach for it.** Before composing two concepts, ask which kind the pair is. A chest drain beside a pneumothorax edge is mostly different pixels, so it is co-occurrence. A shape that is both square-ish and circle-ish is one object scored by both experts, so it is intersection. A wet dog in the rain, or the lung pattern of tuberculosis with silicosis, is a change neither concept shows alone, so it is interaction. Each kind needs different training data and fails differently, and the plain product serves only intersection as written.

| Kind | What it is | The operator | What it needs from training data | How it fails | The field's words |
|---|---|---|---|---|---|
| co-occurrence | two concepts, each whole, each in its own region: a cat beside a dog | $p(\text{layout})\;p_A(x_S \mid \text{layout})\;p_B(x_{S'} \mid \text{layout})$, with $S$ and $S'$ disjoint sets of pixels | each concept alone, at many positions, over varied backgrounds; never the two together | **contention**: both experts score the same pixels, so the product lands on a chimera, the hybrid of the shared case above | Bradley et al.'s co-occurrence and projective composition (*cited*, above); catastrophic neglect when one subject vanishes and failed attribute binding (Chefer et al. 2023, *cited*); concept bleeding and attribute leakage (*stated*: common usage, no single source checked); region-restricted products in MultiDiffusion (Bar-Tal et al. 2023, *cited*) |
| intersection | one thing that satisfies both concepts on the same pixels | $p_A(x)\,p_B(x)$ | each expert must already give the overlap some density; a product intersects supports and creates none, as [[#When neither training set holds A and B]] runs | **empty intersection**: the supports barely meet, so the product peaks in a gap neither expert believes in, the far pair of [[#The product as an intersection]] | product of experts (Hinton 2002, *cited*); Du et al.'s "intersection" (*cited*, above); Composable Diffusion's AND (Liu et al. 2022, *cited*) |
| interaction | the concepts change each other: rain and a dog give a wet dog | the Bayes composition plus $\log \dfrac{p(A, B \mid x)}{p(A \mid x)\,p(B \mid x)}$ | joint samples showing the change, in whichever model carries it (see below) | **missing interaction**: a dry dog standing in rain | no single name found (*stated*) |

The split and shared toy above is co-occurrence done two ways: split gives each expert its own pixel, which is the operator in the first row, and shared makes both experts score $x_0$, which is contention. The ring-times-bar of Du et al.'s Figure 2, under [[#Product, mixture and negation]], is an intersection toy: both experts score both coordinates.

**How the interaction term arises.** Write each conditional with [Bayes' rule](../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=105), then divide:

$$
\begin{aligned}
p(x \mid A, B) &= \frac{p(A, B \mid x)\,p(x)}{p(A, B)} \\
\frac{p(x \mid A)\,p(x \mid B)}{p(x)} &= \frac{p(A \mid x)\,p(x)}{p(A)} \cdot \frac{p(B \mid x)\,p(x)}{p(B)} \cdot \frac{1}{p(x)} = \frac{p(A \mid x)\,p(B \mid x)\,p(x)}{p(A)\,p(B)} \\
\frac{p(x \mid A, B)}{p(x \mid A)\,p(x \mid B)/p(x)} &= \frac{p(A, B \mid x)}{p(A \mid x)\,p(B \mid x)} \cdot \frac{p(A)\,p(B)}{p(A, B)}
\end{aligned}
$$

Taking [logs](../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=110) turns the products into sums:

$$
\log p(x \mid A, B) = \log p(x \mid A) + \log p(x \mid B) - \log p(x) + \log \frac{p(A, B \mid x)}{p(A \mid x)\,p(B \mid x)} + \log \frac{p(A)\,p(B)}{p(A, B)}
$$

*Derived.* The last term holds no $x$, so its gradient is zero and the score form is exact without it: $\nabla \log p(x \mid A, B) = s(x \mid A) + s(x \mid B) - s(x) + \nabla \log \frac{p(A, B \mid x)}{p(A \mid x)\,p(B \mid x)}$. The interaction term is zero at every $x$ exactly when $p(A, B \mid x) = p(A \mid x)\,p(B \mid x)$ for every $x$, which is Definition 6.11 on the linked page. Composable Diffusion's AND is the first three terms. *Derived.*

**Where a wet dog has to come from.** When each label is fixed by the image, so $p(A \mid x)$ and $p(B \mid x)$ are each 0 or 1, the joint label is fixed too, $p(A, B \mid x) = p(A \mid x)\,p(B \mid x)$, and the interaction term is zero everywhere. The Bayes composition is then exactly $p(x)$ restricted to images that are both A and B, so wet dogs appear only if $p(x)$, the unconditional model, saw wet dogs. A plain product $p_A\,p_B$ has no $p(x)$ in it, so it can produce a wet dog only if expert A's or expert B's own training images held some. *Derived* from the identity above.

![The kinds of composition as three cards, each showing which pixels each expert scores and its failure|800](assets/kinds-of-composition-the-concept.webp)

*The kinds of composition as three cards, each showing which pixels each expert scores and its failure.*

### Composition taught in, applied in

**Taught in:**

- the `drip-read` walk of the Mechanisms of Projective Composition paper note, step 3a: the overlap prediction, the learner's question about the role of the background and the difference between shared and split, the re-teach with two-pixel images, and the per-coordinate derivation traced on paper
- the PoE derivation foundations journey's plan 13, `plans/13-poe-on-two-gaussians.md`, lines 173 to 182, which composes the same pair with the unconditional $\mathcal{N}(0, \operatorname{diag}(4, 4))$ as the background
- the `drip-idea` walk of the overlap dial in the reduce-reuse-recycle research repository, claim 1, round 2 (`artifacts/ideas/poe-overlap-dial/IDEA_MAP.md`): the learner's correction that composition is several operations, and the names co-occurrence, intersection, interaction and contention, for [[#Kinds of composition]]

**Applied in:** the overlap-dial idea in the reduce-reuse-recycle research repository, which asks how often a product of two 2D experts lands in the A-and-B region as the share of A-and-B points in each expert's training set is turned up from 0%. Its two-axis quadrant setup (A is $x_1 < 0$, B is $x_2 > 0$) is a co-occurrence toy, and the ring-times-bar it reuses is an intersection toy.

## The order of multiplying and noising

Navigation: ⬅️ [[#Composing models with a background]] | 📋 [[#Table of contents|TOC]] | [[#The energy parameterisation]] ➡️

**Multiplying two experts and then noising the product (equation 11 of Du et al.) gives a different curve from noising each expert and then multiplying (equation 12), at every noise level except none. Adding two diffusion models' scores gives the second curve, and the reverse process needs the first.** A mixture of two experts has no such problem: mixing then noising and noising then mixing give the same curve. *Cited:* Du et al., Reduce, Reuse, Recycle, section 4: "For $t>0$, this quantity is *not* equal to the sum of the scores of the two models".

### Words the two orders use

**Score.** The slope of the log of a density, $\nabla_x \log q(x)$. A diffusion model's network estimates it at every noise level. For $\mathcal{N}(m, v)$ it is $-(x - m)/v$, because [the log](../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=110) of the density is $-(x - m)^2 / (2v)$ plus a constant. *Derived.*

**Summed score.** Two models' scores added at the same point and the same level. The log of a product is the sum of the logs, so the summed score is the score of the product of the two *noised* experts. *Derived.* The product's missing area does not enter it: on this pair the clean product has area 0.075126, and dividing by that moves the log by a constant, which has slope 0. See [[Multivariate Normal Distribution#The area a product loses]].

**Multiply, then noise**, equation 11. Multiply the clean experts, then push the product through the forward process to level $\bar\alpha$. This is the curve a model trained on the product's own data would learn, and the one the reverse process assumes it is walking down.

**Noise each, then multiply**, equation 12. Push each expert to level $\bar\alpha$ on its own, then multiply. This is the curve the summed score belongs to.

The sampler correctors journey's notation calls equation 11's curve "noise-then-compose" and equation 12's "compose-then-noise". Those labels name the curves by a different convention from the order the operations run in, so check any use of them against the equation number.

### The one-dimensional pair

Every number below is on two one-dimensional experts, chosen unequal so the product's centre is not 0:

| Cloud | Mean | Variance |
|---|---|---|
| expert a | $-1$ | $0.5$ |
| expert b | $1$ | $0.8$ |
| their product, no noise | $-0.2308$ | $0.3077$ |

The product is narrower than either expert because precisions add: $1/0.5 + 1/0.8 = 3.25$, and $1/3.25 = 0.3077$. See [[Multivariate Normal Distribution#Products and quotients of diagonal Gaussians]].

### When to reach for the two orders

When two diffusion models are composed by adding their scores (a conjunction of two prompts, or a guidance term added to a model) and the samples come out wrong although each model samples well alone. Comparing the two orders on a case with exact scores says whether the fault lies in the models or in the sampler. Without that check, the natural move is to retrain or fine-tune models that were never the problem.

### The form of the two orders

```text
noising kernel:                      q(x_t | x_0) = N(x_t; sqrt(abar) x_0, 1 - abar)
eq 11, multiply, then noise:         q~_t(x_t)  is proportional to  integral of q1(x_0) q2(x_0) q(x_t | x_0) dx_0
eq 12, noise each, then multiply:    q_t(x_t)   is proportional to  [integral of q1(x_0) q(x_t | x_0) dx_0] x [integral of q2(x_0) q(x_t | x_0) dx_0]
score of eq 12:                      s1(x_t, abar) + s2(x_t, abar), the summed score
equal at abar = 1 for a product; equal at every abar for a mixture (q1 + q2) / 2
```

![The clean experts multiplied then noised in green against noised then multiplied in purple|800](assets/two-orders-the-form.webp)

*The form, the clean experts multiplied then noised in green against noised then multiplied in purple.*

### Try the two orders yourself

**1. What you need.** Python with NumPy, through the prepared environment:

```bash
~/.vault-sandbox/bin/python -c "import numpy; print(numpy.__version__)"
```

You should see a version number. This run printed `2.4.6`.

**2. When it is missing.** [[Multivariate Normal Distribution#Try sampling yourself]] steps 1 and 2 say how to make the environment, or how to use `uv run` instead.

**3. Make something to act on.** A new empty folder, and the two experts with the three pieces every script below uses: the forward jump from [[#The forward process in one jump]], the product rule, and the summed score. The last six lines build a 100-level cosine noise schedule for the two samplers in steps 5 and 8.

```bash
mkdir -p ~/playground/sandbox/two-orders && cd ~/playground/sandbox/two-orders
```

Save this as `experts.py`:

```python
import numpy as np

experts = [(-1.0, 0.5), (1.0, 0.8)]          # (mean, variance) of expert a and expert b


def noised(m, v, abar):
    """A Gaussian N(m, v) after the forward jump to level abar."""
    return np.sqrt(abar) * m, abar * v + 1 - abar


def product(m1, v1, m2, v2):
    """N(m1, v1) times N(m2, v2), renormalised: precisions add."""
    v = 1 / (1 / v1 + 1 / v2)
    return v * (m1 / v1 + m2 / v2), v


def summed_score(x, abar):
    """What adding the two models' scores gives at level abar."""
    return sum(-(x - noised(m, v, abar)[0]) / noised(m, v, abar)[1] for m, v in experts)


T = 100                                       # cosine schedule, 100 levels
u = np.arange(T + 1) / T
ac = np.cos((u + 0.008) / 1.008 * np.pi / 2) ** 2
ac = ac / ac[0]
betas = np.concatenate([[0.0], np.clip(1 - ac[1:] / ac[:-1], 0, 0.999)])
abars = np.cumprod(1 - betas)                 # abars[0] = 1 is clean, abars[T] is almost pure noise
```

**4. Look at it before.** Save this as `before.py`:

```python
from experts import experts, product

(ma, va), (mb, vb) = experts
m, v = product(ma, va, mb, vb)
print(f"the product at no noise: mean {m:.6f}, variance {v:.6f}")
```

```bash
~/.vault-sandbox/bin/python before.py
```

```text
the product at no noise: mean -0.230769, variance 0.307692
```

This is the target every sampler below is trying to reach.

**5. The failure: the reverse process on the summed score.** Start 100,000 points from pure noise and take one reverse step per level, each step using the summed score where a single model's score would go. Every score here is exact, so nothing a trained network could get wrong is in play. Save this as `reverse.py`:

```python
import numpy as np
from experts import experts, product, summed_score, T, betas, abars

rng = np.random.default_rng(0)
x = rng.standard_normal((100_000, 1))                      # start from pure noise
for t in range(T, 0, -1):                                  # one reverse step per level
    eps = -np.sqrt(1 - abars[t]) * summed_score(x, abars[t])
    mean = (x - betas[t] / np.sqrt(1 - abars[t]) * eps) / np.sqrt(1 - betas[t])
    x = mean + np.sqrt(betas[t]) * rng.standard_normal(x.shape)
m, v = product(*experts[0], *experts[1])
print(f"reverse process on the summed score: mean {x.mean():.4f}, variance {x.var():.4f}")
print(f"the product it was meant to reach:   mean {m:.4f}, variance {v:.4f}")
```

```bash
~/.vault-sandbox/bin/python reverse.py
```

You should see:

![The reverse process on the summed score ends at variance 0.2102, against the product's 0.3077|800](assets/two-orders-reverse-process-on-the-summed-score.png)

The cloud ends 32% narrower than the product, and its centre sits 0.07 too far toward 0. The line `eps = ...` turns the score into the noise estimate the reverse step of Du et al.'s equation 1 expects.

**6. The technique: build both orders on a grid.** Equations 11 and 12 are integrals over $x_0$. On a grid of 1,601 points, the noising kernel becomes a matrix `K`, whose entry `K[i, j]` is the noising density at `x[i]` given a clean point at `x[j]`, and each integral becomes `K @ density * dx`. Save this as `two_orders.py`:

```python
import numpy as np
from experts import experts

x = np.linspace(-8, 8, 1601)
dx = x[1] - x[0]
abar = 0.5                                                 # half the signal left


def gauss(z, m, v):
    return np.exp(-(z - m) ** 2 / (2 * v)) / np.sqrt(2 * np.pi * v)


def mean_var(p):
    p = p / (p.sum() * dx)
    m = (x * p).sum() * dx
    return m, ((x - m) ** 2 * p).sum() * dx


def slope_of_log(p, at=1.5):
    i = int(round((at - x[0]) / dx))
    return (np.log(p[i + 1]) - np.log(p[i - 1])) / (2 * dx)


(ma, va), (mb, vb) = experts
qa, qb = gauss(x, ma, va), gauss(x, mb, vb)
K = gauss(x[:, None], np.sqrt(abar) * x[None, :], 1 - abar)   # K[i, j] = q(x_t = x[i] | x_0 = x[j])
first = K @ (qa * qb) * dx                                    # equation 11: multiply, then noise
second = (K @ qa * dx) * (K @ qb * dx)                        # equation 12: noise each, then multiply
for name, p in [("multiply, then noise (eq 11)", first), ("noise each, then multiply (eq 12)", second)]:
    m, v = mean_var(p)
    print(f"{name:34s} mean {m:+.4f}  variance {v:.4f}  slope of log at 1.5 {slope_of_log(p):+.4f}")
```

```bash
~/.vault-sandbox/bin/python two_orders.py
```

You should see:

![Multiply then noise has variance 0.6538; noise each then multiply has variance 0.4091; their slopes at 1.5 differ|900](assets/two-orders-multiply-then-noise-against-noise-then-multiply.png)

With half the signal left, the curve a reverse process needs has variance 0.654, and the curve summed scores describe has variance 0.409. The two lines differ only in where `*` sits relative to `K @`.

**7. Another way to get the same answer: the closed form, at every level.** Both orders stay Gaussian, so each is two calls: `noised(*product(...))` for equation 11 and `product(*noised(...), *noised(...))` for equation 12. Save this as `closed_form.py`:

```python
from experts import experts, noised, product

(ma, va), (mb, vb) = experts
print("abar   multiply, then noise    noise each, then multiply   gap in variance")
for abar in (1.0, 0.9, 0.5, 0.1, 0.0):
    m1, v1 = noised(*product(ma, va, mb, vb), abar)
    m2, v2 = product(*noised(ma, va, abar), *noised(mb, vb, abar))
    print(f"{abar:4.1f}   mean {m1:+.4f} var {v1:.4f}   mean {m2:+.4f} var {v2:.4f}     {v1 - v2:+.4f}")
```

```bash
~/.vault-sandbox/bin/python closed_form.py
```

You should see:

![The two orders at five noise levels: equal with no noise, apart by 0.2448 at half the signal, N(0, 1) against N(0, 0.5) at pure noise|900](assets/two-orders-the-gap-at-every-noise-level.png)

The abar 0.5 line matches step 6 to four decimals. The gap is zero only with no noise, and it grows to 0.5 at pure noise.

**8. More worked examples on the same setup.**

*A mixture against a product.* The same grid, with the experts averaged instead of multiplied. Save this as `mixture.py`:

```python
import numpy as np
from experts import experts

x = np.linspace(-8, 8, 1601)
dx = x[1] - x[0]
abar = 0.5


def gauss(z, m, v):
    return np.exp(-(z - m) ** 2 / (2 * v)) / np.sqrt(2 * np.pi * v)


(ma, va), (mb, vb) = experts
qa, qb = gauss(x, ma, va), gauss(x, mb, vb)
K = gauss(x[:, None], np.sqrt(abar) * x[None, :], 1 - abar)
mix_then_noise = K @ (0.5 * qa + 0.5 * qb) * dx
noise_then_mix = 0.5 * (K @ qa * dx) + 0.5 * (K @ qb * dx)
print(f"mixture, largest difference in height between the two orders: {np.abs(mix_then_noise - noise_then_mix).max():.1e}")
mult_then_noise = K @ (qa * qb) * dx
noise_then_mult = (K @ qa * dx) * (K @ qb * dx)
a = mult_then_noise / (mult_then_noise.sum() * dx)
b = noise_then_mult / (noise_then_mult.sum() * dx)
print(f"product, largest difference in height between the two orders: {np.abs(a - b).max():.1e}")
```

```bash
~/.vault-sandbox/bin/python mixture.py
```

You should see:

![A mixture's two orders differ by 2.8e-16 in height, a product's by 0.14|800](assets/two-orders-a-mixture-commutes-a-product-does-not.png)

For the mixture the difference is rounding error. For the product it is 0.14 in height, on curves whose peaks are about 0.5 to 0.6 high.

*A sampler that reaches the product with the same summed score.* Annealed Langevin, the paper's Algorithm 1 with the Langevin step as its kernel: at every level, noisiest first, take ten small steps along the summed score, each with fresh noise, then carry the cloud to the next level unchanged. Save this as `annealed.py`:

```python
import numpy as np
from experts import experts, product, summed_score, T, abars

rng = np.random.default_rng(0)
x = rng.standard_normal((100_000, 1))
step = 0.01
for t in range(T, -1, -1):                                 # every level, noisiest first
    for i in range(10):                                    # ten Langevin steps at that level
        x = x + step * summed_score(x, abars[t]) + np.sqrt(2 * step) * rng.standard_normal(x.shape)
m, v = product(*experts[0], *experts[1])
print(f"annealed Langevin on the summed score: mean {x.mean():.4f}, variance {x.var():.4f}")
print(f"the product it was meant to reach:     mean {m:.4f}, variance {v:.4f}")
```

```bash
~/.vault-sandbox/bin/python annealed.py
```

You should see:

![Annealed Langevin on the summed score ends at variance 0.3124, against the product's 0.3077|800](assets/two-orders-annealed-langevin-on-the-summed-score.png)

The same scores as step 5, a different sampler, and the cloud lands within 1.5% of the product's variance. It costs 1,010 score evaluations per point against the reverse process's 100.

*More levels do not help.* Step 5 used 100 levels. If its 32% error came from steps that are too coarse, more levels would shrink it. Each reverse step on a Gaussian cloud is a linear map plus fresh noise, so the cloud's mean and variance can be followed exactly instead of sampled, and 10,000 levels cost nothing. Save this as `levels.py`:

```python
import numpy as np
from experts import experts, noised


def schedule(T):
    """The cosine schedule of experts.py, with T levels in place of 100."""
    u = np.arange(T + 1) / T
    ac = np.cos((u + 0.008) / 1.008 * np.pi / 2) ** 2
    ac = ac / ac[0]
    betas = np.concatenate([[0.0], np.clip(1 - ac[1:] / ac[:-1], 0, 0.999)])
    return betas, np.cumprod(1 - betas)


def reverse_exact(T, which):
    """The reverse process's mean and variance, followed exactly. The score is -P x + b at every level."""
    betas, abars = schedule(T)
    m, v = 0.0, 1.0                                         # start from pure noise
    for t in range(T, 0, -1):
        parts = [noised(mu, var, abars[t]) for mu, var in which]
        P = sum(1 / vt for mt, vt in parts)                 # precisions add
        b = sum(mt / vt for mt, vt in parts)
        c = 1 - betas[t] * P                                # x + beta * score = c x + beta b
        m = (c * m + betas[t] * b) / np.sqrt(1 - betas[t])
        v = c ** 2 * v / (1 - betas[t]) + betas[t]
    return m, v


print("levels   summed score: mean, variance   expert a alone: mean, variance")
for T in (10, 100, 1000, 10000):
    ms, vs = reverse_exact(T, experts)
    ma, va = reverse_exact(T, experts[:1])
    print(f"{T:6d}   {ms:+.6f}  {vs:.6f}            {ma:+.6f}  {va:.6f}")
print("targets: the product -0.230769  0.307692;  expert a -1.000000  0.500000")
```

```bash
~/.vault-sandbox/bin/python levels.py
```

You should see:

![With expert a alone the variance falls to 0.500043 at 10,000 levels; with the summed score it settles at 0.207390, far from the product's 0.307692|800](assets/two-orders-more-levels-do-not-help.png)

On expert a alone the error shrinks as the levels grow, from 0.545 at 10 levels to 0.500043 at 10,000. On the summed score the variance settles at 0.2074 and stays there, 32.6% below the product. The loop is fine; the curves it follows are the wrong ones.

*Route A and route B, level by level.* Step 7 printed both orders at five values of $\bar\alpha$. This prints them at the schedule's own levels, $t = 0$ clean to $t = 100$ noisiest, and finds where they differ most. Call equation 11's sequence route A and equation 12's route B. Save this as `route_b.py`:

```python
import numpy as np
from experts import experts, noised, product, abars

(ma, va), (mb, vb) = experts
print("  t   abar     route A (eq 11): mean, variance   route B (eq 12): mean, variance")
gaps = []
for t in range(0, 101):
    mA, vA = noised(*product(ma, va, mb, vb), abars[t])          # multiply, then noise
    mB, vB = product(*noised(ma, va, abars[t]), *noised(mb, vb, abars[t]))   # noise each, then multiply
    gaps.append((t, mA - mB, vA - vB))
    if t % 25 == 0:
        print(f"{t:3d}   {abars[t]:.4f}   {mA:+.4f}  {vA:.4f}                {mB:+.4f}  {vB:.4f}")
t_m, g_m, _ = max(gaps, key=lambda g: abs(g[1]))
t_v, _, g_v = max(gaps, key=lambda g: abs(g[2]))
print(f"mean gap, A minus B, largest at t = {t_m}: {g_m:+.6f};  variance gap largest at t = {t_v}: {g_v:+.6f}")
```

```bash
~/.vault-sandbox/bin/python route_b.py
```

You should see:

![Route A's variance runs 0.3077 to 1.0000 and route B's 0.3077 to 0.5000; the mean gap peaks at t = 56 and the variance gap at t = 100|900](assets/two-orders-route-a-and-route-b-level-by-level.png)

The two routes start as the same product at $t = 0$. Route B runs smoothly to $\mathcal{N}(0, 1/2)$, narrower than route A at every level past $t = 0$. The centres are furthest apart at $t = 56$, on the noisy side of the middle; a count that starts from the noisiest level puts the same peak at 44.

*Steps per level against step size.* `annealed.py` took 10 steps of size 0.01 at each level. Followed exactly, the same way as `levels.py`, here is what changing each of those two numbers does. Save this as `steps_per_level.py`:

```python
import numpy as np
from experts import experts, noised, T, abars


def annealed_exact(n_steps, step):
    """Annealed Langevin's mean and variance, followed exactly: every level, noisiest first."""
    m, v = 0.0, 1.0
    for t in range(T, -1, -1):
        parts = [noised(mu, var, abars[t]) for mu, var in experts]
        P = sum(1 / vt for mt, vt in parts)
        b = sum(mt / vt for mt, vt in parts)
        for i in range(n_steps):                            # x + step * (-P x + b) + sqrt(2 step) z
            m = (1 - step * P) * m + step * b
            v = (1 - step * P) ** 2 * v + 2 * step
    return m, v


for n, step in [(1, 0.01), (3, 0.01), (10, 0.01), (30, 0.01), (10, 0.001), (10, 0.03), (10, 0.1)]:
    m, v = annealed_exact(n, step)
    print(f"{n:2d} steps per level, step {step:<5}: mean {m:+.6f}, variance {v:.6f}")
P = 1 / 0.5 + 1 / 0.8
for step in (0.01, 0.03, 0.1):
    print(f"where one level's chain settles at step {step:<4} with no noise: variance {1 / (P * (1 - step * P / 2)):.6f}")
print("the product: mean -0.230769, variance 0.307692")
```

```bash
~/.vault-sandbox/bin/python steps_per_level.py
```

You should see:

![30 steps per level bring the mean to -0.230515 while the variance stays at 0.312800, beside 0.312775 where a chain at step 0.01 settles; step 0.1 ends at 0.367394|900](assets/two-orders-steps-per-level-against-step-size.png)

More steps per level bring the mean onto the product's: $-0.148$ with one step, $-0.2305$ with 30. The variance stops falling at about 0.3128, where an unadjusted chain at step 0.01 settles on the clean product whatever the number of steps. The step size sets the width: 10 steps of 0.1 end at 0.367394, exactly that chain's settled width at step 0.1. A step of 0.001 is too short to travel, and the mean stays at $-0.147$.

**9. Clean up, and prove it.**

```bash
cd ~ && rm -r ~/playground/sandbox/two-orders
ls ~/playground/sandbox/two-orders; echo $?
```

You should see `No such file or directory`, then `2`.

### Reading the two-orders output

**From step 6, `two_orders.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | multiply, then noise: variance | `0.6538` | the noised product's width, the curve the reverse process assumes at $\bar\alpha = 0.5$ | derived below |
| 2 | noise each, then multiply: variance | `0.4091` | the width of the curve the summed score belongs to; 0.245 narrower | derived below |
| 3 | multiply, then noise: slope of log at 1.5 | `-2.5437` | the score a model trained on the product would return at $x_t = 1.5$ | derived below |
| 4 | noise each, then multiply: slope of log at 1.5 | `-3.8238` | the summed score at the same point: $-2.9428 + (-0.8810)$, expert a's noised score plus expert b's | derived below |

**From step 7, `closed_form.py`**, which prints the same two curves at five levels:

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | gap at abar 1.0 | `+0.0000` | with no noise the two orders are the same product | derived below |
| 2 | gap at abar 0.5 | `+0.2448` | field 1 minus field 2 of step 6 | derived below |
| 3 | multiply, then noise at abar 0.0: variance | `1.0000` | anything noised all the way is $\mathcal{N}(0, 1)$ | derived below |
| 4 | noise each, then multiply at abar 0.0: variance | `0.5000` | two $\mathcal{N}(0, 1)$ multiplied: $\mathcal{N}(0, 1/2)$. The `-0.0000` beside field 3 is a negative zero from rounding | cited, section 4: the summed-score sequence ends at "$\mathcal{N}(0, I/2)$ at $t=T$" |

**From steps 5 and 8, `reverse.py` and `annealed.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | reverse process: variance | `0.2102` | 31.8% narrower than the product; followed exactly, with no sampling, the loop ends at 0.209963 | shown; the exact figure from the journey's answer key, `checks/reverse_diffusion.out` |
| 1 | annealed Langevin: variance | `0.3124` | within 1.5% of the product; followed exactly it ends at 0.313044, 1.7% wide | shown; the exact figure from `checks/annealed_mcmc.out` |
| 2 | the product: variance | `0.3077` | the target, as `before.py` printed | shown |

**From step 8, `mixture.py`:** field 1, `2.8e-16`, is floating-point rounding, so the mixture's two orders are the same curve. Field 2, `1.4e-01`, is the largest height difference between the product's two orders, both normalised to area 1.

**From step 8, `levels.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | summed score, 10,000 levels: variance | `0.207390` | however many levels, the reverse process on summed scores ends 32.6% below the product's 0.307692 | shown; the same figure as `checks/reverse_diffusion.out` |
| 2 | expert a alone, 10,000 levels: variance | `0.500043` | the same loop on one model reaches that model, so the loop is sound | shown; the same figure as `checks/reverse_diffusion.out` |

**From step 8, `route_b.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | route A at $t = 50$: variance | `0.6581` | the curve the reverse process assumes at level 50, $\bar\alpha = 0.4938$ | derived below |
| 2 | route B at $t = 50$: variance | `0.4103` | the curve the summed score belongs to at the same level, 0.248 narrower | derived below |
| 3 | mean gap, largest | `t = 56: -0.101825` | route A's centre sits 0.10 further from 0 than route B's; nowhere are the centres further apart | shown; the same figure as `checks/route_b_path.out` |
| 4 | variance gap, largest | `+0.500000` | at $t = 100$: $\mathcal{N}(0, 1)$ against $\mathcal{N}(0, 1/2)$ | derived below |

**From step 8, `steps_per_level.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | 30 steps per level: mean | `-0.230515` | within 0.0003 of the product's centre | shown; the same figure as `checks/annealed_mcmc.out` |
| 2 | 30 steps per level: variance | `0.312800` | still 1.7% wide, as with 10 steps | shown |
| 3 | where step 0.01 settles | `0.312775` | the width an unadjusted chain at step 0.01 keeps on the clean product, however many steps it takes | derived in [[#How the energy works]] |
| 4 | 10 steps of 0.1: variance | `0.367394` | the same width an unadjusted chain at step 0.1 settles at, 19.4% wide | derived in [[#How the energy works]] |

### How the two orders work

**Why a mixture survives the order and a product does not.** Noising a density is one integral against the kernel:

$$
q_t(x_t) = \int q(x_0)\, q(x_t \mid x_0)\, dx_0
$$

The integral is linear in $q$, so it passes through a weighted sum:

$$
\begin{aligned}
\int \left(\tfrac12 q^1 + \tfrac12 q^2\right)(x_0)\, q(x_t \mid x_0)\, dx_0
&= \tfrac12 \int q^1(x_0)\, q(x_t \mid x_0)\, dx_0 + \tfrac12 \int q^2(x_0)\, q(x_t \mid x_0)\, dx_0 \\
&= \tfrac12 q^1_t(x_t) + \tfrac12 q^2_t(x_t)
\end{aligned}
$$

For a product there is no such step. $\int q^1 q^2\, K\, dx_0$ is one integral of a product, and $\left(\int q^1 K\, dx_0\right)\left(\int q^2 K\, dx_0\right)$ is a product of two integrals; an integral of a product is not in general the product of the integrals. *Derived.* Step 8 shows it: $2.8 \times 10^{-16}$ for the mixture, $0.14$ for the product.

**The worked numbers at $\bar\alpha = 0.5$.** The jump sends $\mathcal{N}(m, v)$ to $\mathcal{N}(\sqrt{\bar\alpha}\,m,\ \bar\alpha v + 1 - \bar\alpha)$ ([[#How the jump works]]), and a product of Gaussians adds precisions.

Equation 11, multiply first:

$$
\begin{aligned}
v_p &= \frac{1}{1/0.5 + 1/0.8} = \frac{1}{3.25} = 0.307692, \qquad m_p = 0.307692 \times \left(\frac{-1}{0.5} + \frac{1}{0.8}\right) = 0.307692 \times (-0.75) = -0.230769 \\
\text{mean} &= \sqrt{0.5} \times (-0.230769) = -0.163178, \qquad \text{variance} = 0.5 \times 0.307692 + 0.5 = 0.653846
\end{aligned}
$$

Equation 12, noise each first:

$$
\begin{aligned}
\text{expert a} &\to \mathcal{N}(-0.707107,\ 0.5 \times 0.5 + 0.5) = \mathcal{N}(-0.707107,\ 0.75) \\
\text{expert b} &\to \mathcal{N}(0.707107,\ 0.5 \times 0.8 + 0.5) = \mathcal{N}(0.707107,\ 0.9) \\
\text{variance} &= \frac{1}{1/0.75 + 1/0.9} = \frac{1}{2.444444} = 0.409091 \\
\text{mean} &= 0.409091 \times \left(\frac{-0.707107}{0.75} + \frac{0.707107}{0.9}\right) = 0.409091 \times (-0.157135) = -0.064282
\end{aligned}
$$

The scores at $x_t = 1.5$:

$$
\begin{aligned}
\text{eq 11:}\quad & -\frac{1.5 - (-0.163178)}{0.653846} = -2.543685 \\
\text{eq 12:}\quad & -\frac{1.5 + 0.707107}{0.75} - \frac{1.5 - 0.707107}{0.9} = -2.942809 - 0.880992 = -3.823802
\end{aligned}
$$

**At the two ends.** With no noise, $\bar\alpha = 1$, the jump does nothing and both orders are the product $\mathcal{N}(-0.230769, 0.307692)$. With pure noise, $\bar\alpha = 0$, equation 11 gives $\mathcal{N}(0, 1)$ whatever was noised, while equation 12 multiplies two $\mathcal{N}(0, 1)$ curves: precision $1 + 1 = 2$, variance $\tfrac12$. In general:

$$
\begin{aligned}
\text{eq 11 variance} &= \bar\alpha\, v_p + 1 - \bar\alpha \\
\text{eq 12 variance} &= \left(\frac{1}{\bar\alpha v_a + 1 - \bar\alpha} + \frac{1}{\bar\alpha v_b + 1 - \bar\alpha}\right)^{-1}
\end{aligned}
$$

These print as the five rows of step 7. *Derived.*

**Why the reverse process misses.** Each reverse step moves a cloud from level $t$ to level $t - 1$ of one forward-noising sequence. Equation 12's curves, taken level by level, are not such a sequence: the paper says they "smoothly interpolate between $q^{\text{prod}}(x)$ at $t=0$ and $\mathcal{N}(0, I/2)$ at $t=T$, though this sequence of distributions does not correspond to the distributions that result from the standard forward diffusion process". *Cited:* section 4, the paragraph after equation 12. On the pair the reverse process ends at variance 0.2102, too narrow. *Shown*, step 5. Equation 12's curves are narrower than equation 11's at every level below none, step 7. That the narrow curves are what make the samples narrow is the writer's reading of the two outputs together. *Stated.*

**More levels do not close the gap.** Write the summed score at level $t$ as $-P_t x + b_t$, with $P_t$ the two noised experts' precisions added. One reverse step is then a linear map of $x$ plus fresh noise, and by the rule for [a linear combination of Gaussians](../../Mathematics/references/textbooks/linear-algebra/matrix-cookbook.pdf#page=41) the cloud's mean and variance move as

$$
\begin{aligned}
x' &= \frac{x + \beta_t\,(-P_t x + b_t)}{\sqrt{1 - \beta_t}} + \sqrt{\beta_t}\, z = \frac{c_t\, x + \beta_t b_t}{\sqrt{1 - \beta_t}} + \sqrt{\beta_t}\, z, \qquad c_t = 1 - \beta_t P_t \\
m' &= \frac{c_t\, m + \beta_t b_t}{\sqrt{1 - \beta_t}} \\
v' &= \frac{c_t^2\, v}{1 - \beta_t} + \beta_t
\end{aligned}
$$

*Derived.* Followed this way, expert a's own loop ends at 0.544959 with 10 levels and 0.500043 with 10,000: its error is the coarseness of the steps and it vanishes. The summed score's loop ends at 0.238425 with 10 levels and 0.207390 with 10,000: its error converges to a wrong width instead. *Shown*, step 8, `levels.py`. The paper's "Reverse (equal steps)" row, a model trained with enough extra levels that reverse diffusion costs as much as the MCMC samplers, makes the same point: "simply adding more time-steps does not solve compositional sampling". *Cited:* `text/results.tex` line 20.

**Route A and route B, level by level.** Route A is equation 11's sequence and route B equation 12's. On the schedule's levels, with $\bar\alpha$ the share of signal left:

| Level $t$ | $\bar\alpha$ | route A variance | route B variance |
|---|---|---|---|
| 0, clean | 1 | 0.308 | 0.308 |
| 25 | 0.847 | 0.414 | 0.340 |
| 50 | 0.494 | 0.658 | 0.410 |
| 75 | 0.144 | 0.900 | 0.475 |
| 100, noisiest | 0 | 1.000 | 0.500 |

Each column comes from the two variance formulas above. Route B runs smoothly from the product to $\mathcal{N}(0, 1/2)$, and the summed score is its exact score at every level. So the summed score is the right score for a different sequence. The mean gap is largest at $t = 56$, $-0.102$, and the variance gap at the noisiest level, 0.5. *Shown*, step 8, `route_b.py`.

**Why annealed Langevin reaches the product.** A Langevin chain that follows one score with small steps settles on the curve that score belongs to, whether or not that curve sits in a forward sequence. Annealed Langevin lets the cloud settle on equation 12's curve at each level, then moves to the next. At the last level, $\bar\alpha = 1$, equation 12's curve is the product. The remaining 1.7% matches the error the step size alone causes: ten times smaller steps at no noise bring a chain on this pair from 19.4% too wide to 1.7%. *Cited:* the journey's read-ahead, `read-ahead/00-abstract.md`, sentence 6, from `checks/langevin_chain.out`.

**The sampler, or the model.** Steps 5 and 8 use the same exact scores. One sampler misses by 31.8% of the product's variance and the other lands within 1.7%, so on this pair the failure is the sampler's. The paper's abstract says "We conclude that the sampler (not the model) is responsible for this failure". Its body is more careful, in section 4.1: the results "further imply that the choice of sampler may be responsible for prior failures in compositional generation". *Cited:* `text/abstract.tex` line 2 and `text/method.tex` line 131 of the paper's source.

The paper's Figure 2 shows the same two samplers on two-dimensional pairs:

![The paper's Figure 2: a ring of eight blobs times a vertical bar should give two blobs; reverse diffusion gives a ring, HMC gives the two blobs. Bottom row: two columns of three blobs added should give six; reverse diffusion smears them into three bars, HMC gives six|900](references/two-orders-paper-figure-2-product-and-mixture-toys.png)

> **Figure 2.** **An illustration of product and mixture compositional models, and the improved sampling performance of MCMC in both cases.** Left to right: Component distributions, ground truth composed distribution, reverse diffusion samples, HMC samples. Top: product, bottom: mixture. Reverse diffusion fails to sample from composed models.
>
> *Du, Durkan, Strudel, Tenenbaum, Dieleman, Fergus, Sohl-Dickstein, Doucet, Grathwohl, Reduce, Reuse, Recycle, ICML 2023, [arXiv 2302.11552](https://arxiv.org/abs/2302.11552), Figure 2. arXiv non-exclusive distribution licence; copied for study with citation.*

The top row is this section's failure at full scale: the true product keeps the top and bottom blobs, reverse diffusion with summed scores leaves samples all round the ring, and HMC, another MCMC sampler, recovers the two blobs. *Shown* in the figure. The sampler kept the ring and lost the bar, one of the two experts.

The walk redrew the top row with exact scores in place of trained networks, 5,000 samples per panel, counting a sample as on target when it lies within 0.1 of one of the two true blobs. The true product puts 96.8% there and reverse diffusion 55.6%. HMC with the settings the paper's appendix F prints reaches 69.0%, short of what the paper's panel shows; with 30 HMC steps per noise level it reaches 87.0%, and with 300 it reaches 91.5%, on 400 samples each. *Cited:* the journey's answer keys `checks/ring_times_bar.out` and `checks/ring_times_bar_more_steps.out`, three standard errors at most 2.1 points at 5,000 samples and 5.0 to 6.9 at 400. The same panels on the one-dimensional pair, 20,000 samples each: reverse diffusion ends at variance 0.2100 and annealed MCMC at 0.3076, against the product's 0.3077 (`checks/fig2_on_the_object.out`, tolerance 0.0092).

The bottom row is a mixture, where the noising order does not matter (step 8 above: $2.8 \times 10^{-16}$), and reverse diffusion still smears it. With exact scores the mixture's noised curves are one forward sequence, so the plain reverse process would be the right sampler, and the bottom row's failure has to come from how the two trained models were combined. The paper gives no cause: its appendix C.3 lists "products, tempering, and guidance" as the operators that do not commute with noising and leaves the mixture out, while the caption says reverse diffusion "fails to sample from composed models" of both rows. *Derived* for the commuting; *cited* for the caption and C.3, as the journey's read-ahead quotes them at chunk 36. A mixture's score needs each model's height as well as its slope, and the paper builds it from energy-parameterised models, assuming "this ratio [of normalizers] is 1"; [[#How the energy works]] and [[#Product, mixture and negation]] work that out on this pair. No released code builds this row. *Cited:* section 3, the mixture paragraph.

![The blur passing through a mixture and not through a product|800](assets/two-orders-the-mechanism.webp)

*The mechanism, the blur passing through a mixture and not through a product.*

![The deep-dive sheet composing the form, the mechanism and the run of closed_form.py|800](assets/two-orders-deep-dive-sheet.webp)

*The deep-dive sheet composing the form, the mechanism and the run of `closed_form.py`.*

### Annealed MCMC

**Annealed MCMC, the paper's Algorithm 1, takes a few MCMC steps at every noise level from the noisiest to the clean one, each aimed at that level's composed curve, and carries the cloud down to the next level unchanged.** With summed scores the curve at each level is route B, and route B ends at the product, so the cloud ends there too. *Cited:* section 4.1, Algorithm 1, `text/method.tex` lines 99 and 107 to 121 of the paper's source.

```text
x ~ p_T                                   start from pure noise
for t = T, T-1, ..., 0:                   every level, noisiest first
    repeat N times:  x ~ k_t( . | x)      an MCMC kernel aimed at level t's composed curve
    carry x to level t - 1 unchanged
return x
unadjusted Langevin kernel:  k_t: x + eta * s(x, t) + sqrt(2 eta) z,  s = the summed score
cost: N x (T + 1) score evaluations per sample; 10 x 101 = 1,010 against the reverse process's 100
```

*🖼️ Diagram wanted: the concept, route A and route B bells at five levels with the chain settling on route B at each. Prompt 17 in the vault's `.prompts/Diffusion Models.md`.*

**What each setting controls.** The number of steps per level sets how close the mean gets: $-0.148$ with one step of 0.01 per level, $-0.2286$ with 10, $-0.2305$ with 30, against the product's $-0.2308$. The step size sets the final width: 0.3128 at step 0.01, 0.3235 at 0.03, 0.3674 at 0.1, each the width an unadjusted chain at that step keeps on the clean product, derived in [[#How the energy works]]. More steps per level do not shrink it. A step too small for the steps given, 0.001 with 10 per level, never travels and ends at mean $-0.147$. *Shown*, step 8, `steps_per_level.py`.

**Score models allow only unadjusted kernels.** With the standard noise-predicting network there is no energy, so no Metropolis correction: the paper uses ULA, unadjusted Langevin, and U-HMC, unadjusted Hamiltonian Monte Carlo. ULA at one level is the reverse step "repeatedly running the diffusion reverse process at the same noise level with composed score functions". *Cited:* `text/method.tex` line 127. An accept step removes the width error at any step size; see [[#Step size and the accept step]].

### Other ways to get the noised product

- **Train one model on the product's own data.** Its score is equation 11's directly, and the plain reverse process works. It needs samples of the composition, which composing two models is meant to avoid. Nothing in the authors' 2D notebook computes equation 11: it would need a model trained on the product itself. *Cited:* the journey's read-ahead, `read-ahead/00-abstract.md`, sentence 5, which read all 47 cells of `notebooks/simple_distributions.ipynb`.
- **Repeat the reverse step at the same level.** Running the reverse process several times at one noise level with the summed score is a form of the Langevin sampler. *Cited:* section 4.1, paragraph 2.
- **Continuous-time samplers run across time** have the same problem as the reverse process, because they too move along the sequence of levels rather than sampling each level's curve. *Cited:* section 4.1, paragraph 3.
- **Metropolis-corrected samplers**, MALA and HMC with an accept-or-reject test, which need each model's energy and not only its score. *Cited:* the abstract, sentence 7. Run on this pair in [[#The energy parameterisation]].

### Why the two orders matter

Products are not the only casualty. The paper's appendix C finds "that products, tempering, and guidance applied to diffused distributions do not give diffusions of the modified target distributions" (*cited:* `text/appendix.tex` line 232). Any composition built by adding or scaling scores therefore asks the reverse process to walk a sequence it was not built for.

[[#Composing models with a background]] asks which density a composition defines, and its shared case is a hybrid that no sampler can turn into co-occurrence. This section asks whether the sampler reaches the density the composition defines. The two failures look alike in samples, and a change of sampler fixes only the second.

### The two orders taught in, applied in

**Taught in:**

- the `drip-read` walk of Du et al., Reduce, Reuse, Recycle, abstract sentences 5 and 6, and section 3, paragraph 1 (products lose their area, mixtures keep it, and the score ignores the area). The walk's paper note, `deep-learning/diffusion-models/02-sampler-correctors-for-composition/papers/reduce-reuse-recycle/reduce-reuse-recycle.md` in this vault, is not written yet; link it here when it is.
- the same walk, section 4, chunks 45 to 51: reverse diffusion on exact summed scores misses the product at any number of levels, equations 11 and 12 as route A and route B level by level, Algorithm 1 and what its steps per level and step size each control, and why only unadjusted samplers are open to a score model. Paper note at the same path, still to be written.
- the same journey's plan 24, `plans/24-what-is-annealed.md`, line 21 (which axis annealed MCMC moves along: the noise level, separated from temperature and guidance scale)
- the sampler correctors for composition journey's plan 14, `plans/14-the-two-gaussian-toy.md`, line 262 (compare the two orders at $\bar\alpha_t = 0.5$ on this pair), and plan 15, `plans/15-the-two-gaps.md`, lines 36 to 44 and 201 to 205 (the gap in mean and the gap in variance, derived in closed form)

**Applied in:** nothing yet.

## The energy parameterisation

Navigation: ⬅️ [[#The order of multiplying and noising]] | 📋 [[#Table of contents|TOC]] | [[#Product, mixture and negation]] ➡️

**An energy-parameterised diffusion model outputs one number per input, $f_\theta(x_t, t)$, and its noise prediction is that number's slope times minus the noise scale, $\epsilon_\theta = -\sigma_t \nabla_x f_\theta$. The number is the log of the noised density's height with its normaliser dropped, and two things need it that a score alone does not carry: the weights of a mixture, and the accept test of a Metropolis-corrected sampler.** *Cited:* Du et al., Reduce, Reuse, Recycle, section 2.3, equation 5 ("we have replaced $\epsilon_\theta(x, t)$ with $-\sigma_t \nabla_x f_\theta(x + \sigma_t \epsilon)$"), and section 4.2, paragraphs 1 and 2.

### Words the energy uses

**Energy $f$.** One number per input: the log of a density's height, up to a constant nobody knows. Du et al. write $e^{f} \propto q$, so $f$ is highest at the mode. A physicist's energy is $-f$, lowest at the mode, and the paper's own appendix D uses that sign, with $\epsilon = +\nabla f$. Check the sign before using a formula from either place. *Cited:* the journey's answer key `checks/energy_parameterisations.out`, last four lines.

**Noise scale $\sigma_t$.** The noise's standard deviation at level $t$: $\sqrt{1 - \bar\alpha}$ in [[#The forward process in one jump]]. Section 2.3 writes $\epsilon_\theta = -\nabla_x f_\theta$ in its sentence 5, with $\sigma_t$ folded into $f$; its equation 5 keeps $\sigma_t$ visible, and so does this note. *Cited:* section 2.3, sentences 3 and 5.

**Score.** As in [[#Words the two orders use]]: $\nabla_x \log q_t(x)$. With an energy model, the score is $\nabla_x f_\theta$ and nothing else.

**Accept step**, or Metropolis correction. Propose a move, keep it with a probability computed from the target's height at both ends, and otherwise stay where you were. **MALA**, the Metropolis-adjusted Langevin algorithm, is a Langevin step used as the proposal with an accept step after it. *Cited:* section 2.2, paragraph 3, sentences 5 and 6.

### When to reach for the energy

When composing models needs more than adding slopes. A mixture ("a cat or a dog") weights each model by how tall it is at the point, and a score carries no height; the paper's section 3 ends by saying the standard parameterisation supports "product and negation composition, but not mixture composition". And when a Langevin sampler at an affordable step size settles on the wrong width: an accept step removes that error, and the accept step compares heights. Without the energy, the only fix for the second problem is a smaller step, paid for in steps. *Cited:* section 3, last sentence, and section 4.2, paragraph 2.

The cost is one backward pass through the network for every noise prediction, because $\epsilon$ is now a gradient. For plain unconditional generation the paper prefers the score form for that reason. *Cited:* section 4.2, paragraph 3.

### The form of the energy parameterisation

```text
network:         f_theta(x_t, t)                      one number per input
noise estimate:  eps_theta(x_t, t) = -sigma_t * grad_x f_theta(x_t, t)       section 2.3, equation 5
score:           grad_x log q_t(x_t) = grad_x f_theta = -eps_theta / sigma_t
product:         f = f_1 + f_2                         the scores add, as in the two-orders section
mixture slope:   w_1(x) grad f_1 + w_2(x) grad f_2,    w_i(x) = q_i(x) / (q_1(x) + q_2(x)),  q_i = e^(f_i) / Z_i
accept test:     keep x_hat with probability  min(1, e^(f(x_hat) - f(x)) * k(x | x_hat) / k(x_hat | x))      section 2.2
the paper's f:   f_theta(x, t) = -||s_theta(x, t)||^2, with s_theta an ordinary vector-output network       section 4.2
```

The mixture line needs each $Z_i$, or at least their ratio. The accept line does not, because both heights belong to the same target and its $Z$ cancels.

![One network giving one number whose slope is the noise estimate and whose height feeds the mixture weights and the accept test|800](assets/energy-the-form.webp)

*The form, one network giving one number whose slope is the noise estimate and whose height feeds the mixture weights and the accept test.*

### Try the energy yourself

**1. What you need.** Python with NumPy, through the prepared environment:

```bash
~/.vault-sandbox/bin/python -c "import numpy; print(numpy.__version__)"
```

You should see a version number. This run printed `2.4.6`.

**2. When it is missing.** [[Multivariate Normal Distribution#Try sampling yourself]] steps 1 and 2 say how to make the environment, or how to use `uv run` instead.

**3. Make something to act on.** A new empty folder, and the same two experts as [[#The one-dimensional pair]], each now written as an energy beside its score. The product's energy is the two energies added, so its score is the summed score.

```bash
mkdir -p ~/playground/sandbox/energy-parameterisation && cd ~/playground/sandbox/energy-parameterisation
```

Save this as `experts.py`:

```python
import numpy as np

experts = [(-1.0, 0.5), (1.0, 0.8)]          # (mean, variance) of expert a and expert b


def noised(m, v, abar):
    """A Gaussian N(m, v) after the forward jump to level abar."""
    return np.sqrt(abar) * m, abar * v + 1 - abar


def expert_energy(x, m, v, abar=1.0):
    """f for one model: the log of its noised height, normaliser dropped. One number per point."""
    mt, vt = noised(m, v, abar)
    return (-(x - mt) ** 2 / (2 * vt)).sum(-1)


def expert_score(x, m, v, abar=1.0):
    """The gradient of expert_energy, written out. One number per coordinate."""
    mt, vt = noised(m, v, abar)
    return -(x - mt) / vt


def energy(x, abar=1.0):
    """The product's f: the two models' f added."""
    return sum(expert_energy(x, m, v, abar) for m, v in experts)


def summed_score(x, abar=1.0):
    """The product's score: the two models' scores added."""
    return sum(expert_score(x, m, v, abar) for m, v in experts)
```

**4. Look at it before.** Expert a at half the signal, on three points. Save this as `before.py`:

```python
import numpy as np
from experts import experts, expert_energy, expert_score

m, v = experts[0]                                  # expert a
abar = 0.5                                         # half the signal left
sigma = np.sqrt(1 - abar)                          # the noise scale at this level
x = np.array([[1.5], [0.0], [-1.0]])               # three points, one coordinate each
h = 1e-5
f = expert_energy(x, m, v, abar)
s = expert_score(x, m, v, abar)
slope = (expert_energy(x + h, m, v, abar) - expert_energy(x - h, m, v, abar)) / (2 * h)
print("f, one number per point:           ", f.round(6), "shape", f.shape)
print("score, one number per coordinate:  ", s.ravel().round(6), "shape", s.shape)
print("slope of f, difference quotient:   ", slope.round(6))
print("noise estimate eps = -sigma grad f:", (-sigma * slope).round(6))
```

```bash
~/.vault-sandbox/bin/python before.py
```

You should see:

![The energy gives one number per point, shape (3,); the score one per coordinate, shape (3, 1); the slope of f matches the score; eps at 1.5 is 2.08088|800](assets/energy-one-number-per-point-and-its-slope.png)

The slope of $f$, measured by nudging $x$, equals the score to six decimals, and minus $\sigma_t$ times it is the noise a network would predict. The energy's shape is `(3,)` where the score's is `(3, 1)`: one number per point against one per coordinate. For a 3 by 64 by 64 image the score has 12,288 numbers and the energy still has one.

**5. The failure: Langevin without an accept step.** A hundred thousand chains take 400 Langevin steps of size 0.1 on the product with no noise, using the summed score alone. Save this as `langevin.py`; it reads the step size from the command line:

```python
import sys
import numpy as np
from experts import summed_score

step = float(sys.argv[1])                          # step size, sigma_L^2 / 2 in equation 4
rng = np.random.default_rng(0)
x = rng.standard_normal((100_000, 1))
for k in range(400):
    x = x + step * summed_score(x) + np.sqrt(2 * step) * rng.standard_normal(x.shape)
P = 1 / 0.5 + 1 / 0.8                              # the product's precision, 3.25
print(f"Langevin, no accept step, step {step}: mean {x.mean():.4f}, variance {x.var():.4f}")
print(f"where this step size settles:         variance {1 / (P * (1 - step * P / 2)):.4f}")
print(f"the product:                          mean -0.2308, variance {1 / P:.4f}")
```

```bash
~/.vault-sandbox/bin/python langevin.py 0.1
```

You should see:

![Langevin without an accept step at step 0.1 ends at variance 0.3671, where the closed form says 0.3674, against the product's 0.3077|800](assets/energy-langevin-without-the-accept-step.png)

The chains settle 19.4% wider than the product. More steps will not help: 0.3674 is where this step size settles, derived in [[#How the energy works]].

**6. The technique: add the accept step.** The same proposals, each kept or rejected by comparing the product's energy at both ends. Save this as `mala.py`:

```python
import numpy as np
from experts import energy, summed_score

step = 0.1


def log_k(x_to, x_from):
    """Log of the Langevin move's probability from x_from to x_to, up to a constant."""
    return (-(x_to - x_from - step * summed_score(x_from)) ** 2).sum(-1) / (4 * step)


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    x = rng.standard_normal((100_000, 1))
    rates = []
    for k in range(400):
        prop = x + step * summed_score(x) + np.sqrt(2 * step) * rng.standard_normal(x.shape)
        log_a = energy(prop) - energy(x) + log_k(x, prop) - log_k(prop, x)
        accept = np.log(rng.random(len(x))) < log_a            # accept with probability min(1, e^log_a)
        x = np.where(accept[:, None], prop, x)
        rates.append(accept.mean())
    print(f"Langevin with the accept step, step {step}: mean {x.mean():.4f}, variance {x.var():.4f}")
    print(f"share of proposals accepted, last 100 steps:  {np.mean(rates[-100:]):.4f}")
    print(f"the product:                                  mean -0.2308, variance 0.3077")
```

```bash
~/.vault-sandbox/bin/python mala.py
```

You should see:

![Langevin with the accept step at step 0.1 ends at variance 0.3071 against the product's 0.3077, with 95.8% of proposals accepted|800](assets/energy-langevin-with-the-accept-step.png)

The same step size now lands within 0.0006 of the product's variance, inside the 0.0041 that sampling 100,000 chains allows. The line `log_a = energy(prop) - energy(x) + ...` is the only place the energy is used, and it is the line two score models could not write.

**7. Another way to get the same answer: a smaller step, with no accept step.** Run step 5 again with a step ten times smaller:

```bash
~/.vault-sandbox/bin/python langevin.py 0.01
```

You should see:

![Langevin without an accept step at step 0.01 ends at variance 0.3134, where the closed form says 0.3128, against the product's 0.3077|800](assets/energy-langevin-with-a-ten-times-smaller-step.png)

The error falls from 19.4% to 1.7%, and never to zero. Each step moves a tenth as far, so the chain needs about ten times as many steps to travel the same distance: an offset from the centre shrinks by a factor $e$ in about $1/(\text{step} \times 3.25)$ steps, 3.1 steps at 0.1 and 30.8 at 0.01. *Derived* in [[#How the energy works]].

**8. More worked examples on the same setup.**

*One proposal, by hand.* Fix the noise draw at 0.5 and trace one MALA step from $x = 1.5$, so every number can be checked on paper. Save this as `one_proposal.py`:

```python
import numpy as np
from mala import energy, summed_score, log_k, step

x = np.array([[1.5]])
z = 0.5                                                        # the noise draw, fixed for the hand check
prop = x + step * summed_score(x) + np.sqrt(2 * step) * z
d_f = energy(prop) - energy(x)
d_k = log_k(x, prop) - log_k(prop, x)
print(f"summed score at 1.5: {summed_score(x)[0, 0]:.6f}, proposal: {prop[0, 0]:.6f}")
print(f"f(proposal) - f(x): {d_f[0]:.6f}")
print(f"log k(x | proposal) - log k(proposal | x): {d_k[0]:.6f}")
print(f"accept probability: min(1, exp({(d_f + d_k)[0]:.6f})) = {min(1.0, float(np.exp((d_f + d_k)[0]))):.6f}")
```

```bash
~/.vault-sandbox/bin/python one_proposal.py
```

You should see:

![One proposal from 1.5 lands at 1.161107; the height rises by 1.719645, the move's asymmetry costs 1.440203, and the proposal is kept with probability 1|600](assets/energy-one-proposal-by-hand.png)

*A mixture needs the heights.* The slope of $\tfrac12 q_a + \tfrac12 q_b$ at 0, between the experts, three ways. Save this as `mixture.py`:

```python
import numpy as np
from experts import experts, expert_energy, expert_score

x = np.array([[0.0]])                                          # between the two experts
f = np.array([expert_energy(x, m, v) for m, v in experts])[:, 0]
log_z = np.array([0.5 * np.log(2 * np.pi * v) for m, v in experts])
s = np.array([expert_score(x, m, v) for m, v in experts])[:, 0, 0]
print(f"slopes at 0: expert a {s[0]:.6f}, expert b {s[1]:.6f}")
for name, log_h in [("from f, normalisers dropped", f), ("from f - log Z, true heights", f - log_z)]:
    share = np.exp(log_h) / np.exp(log_h).sum()
    print(f"{name:29s} shares {share.round(6)}  mixture slope {(share * s).sum():.6f}")
print(f"{'fixed weights of one half':29s} shares [0.5 0.5]  mixture slope {s.mean():.6f}")
mix = lambda z: sum(np.exp(expert_energy(z, m, v)) / np.sqrt(2 * np.pi * v) for m, v in experts)
h = 1e-5
print(f"slope of the true mixture's log, difference quotient: {((np.log(mix(x + h)) - np.log(mix(x - h))) / (2 * h))[0]:.6f}")
```

```bash
~/.vault-sandbox/bin/python mixture.py
```

You should see:

![The mixture's slope at 0 is -0.261437 from the true heights and by difference quotient; dropping the normalisers gives -0.073834 and fixed half weights give -0.375000|800](assets/energy-a-mixture-needs-the-heights.png)

Only the true heights give the true slope. The two slopes are fixed numbers, -2 and 1.25; what changes the answer is how much weight each gets, and the weight is a height.

*Step size, with and without the accept step.* Steps 5 and 6 at six step sizes, 200 steps each, on the clean product. Save this as `step_sizes.py`:

```python
import numpy as np
from experts import energy, summed_score

P = 1 / 0.5 + 1 / 0.8                                       # the product's precision, 3.25
print(f"unadjusted Langevin is stable only below step 2 / P = {2 / P:.6f}")


def run(step, accept_step, n_steps=200):
    rng = np.random.default_rng(0)
    x = rng.standard_normal((100_000, 1))
    log_k = lambda to, fr: (-(to - fr - step * summed_score(fr)) ** 2).sum(-1) / (4 * step)
    kept = []
    with np.errstate(over="ignore", invalid="ignore"):
        for k in range(n_steps):
            prop = x + step * summed_score(x) + np.sqrt(2 * step) * rng.standard_normal(x.shape)
            if not accept_step:
                x = prop
                continue
            log_a = energy(prop) - energy(x) + log_k(x, prop) - log_k(prop, x)
            accept = np.log(rng.random(len(x))) < log_a
            x = np.where(accept[:, None], prop, x)
            kept.append(accept.mean())
    return x.var(), np.mean(kept[-100:]) if kept else None


print("step   no accept step: variance (closed form)   with the accept step: variance, share accepted")
for step in (0.01, 0.3, 0.5, 0.6, 0.7, 0.8):
    v_ula, _ = run(step, False)
    v_mala, rate = run(step, True)
    closed = 1 / (P * (1 - step * P / 2)) if step < 2 / P else float("inf")
    print(f"{step:4.2f}   {v_ula:12.4g} ({closed:.4f})              {v_mala:.4f}, {rate:.4f}")
print("the product: variance 0.3077")
```

```bash
~/.vault-sandbox/bin/python step_sizes.py
```

You should see:

![Unadjusted Langevin follows the closed form to step 0.5, reaches 12.4 at 0.6 and runs away past 0.615; with the accept step every row stays near 0.308, and the share accepted falls from 0.9987 to 0.3779|900](assets/energy-step-size-and-the-accept-step.png)

Without the accept step the width follows the closed form up to step 0.6 and runs away beyond 0.615. With it, every row ends within 0.0022 of the product's 0.3077, inside the sampling tolerance of 0.0041, and the only thing the step size changes is how many proposals are kept.

*Light tails.* A target whose tails fall faster than a Gaussian's, $q(x) \propto e^{-x^4/4}$, with score $-x^3$. Save this as `light_tails.py`:

```python
import numpy as np

# target proportional to exp(-x^4 / 4): its score is -x^3, and its tails fall faster than a Gaussian's
print("one step with no noise from x = 5 at step 0.1, x - 0.1 x^3:", 5 - 0.1 * 5 ** 3)
for step in (0.01, 0.1, 0.3, 0.5):
    rng = np.random.default_rng(0)
    x = rng.standard_normal(100_000)
    with np.errstate(over="ignore", invalid="ignore"):
        for k in range(1000):
            x = x - step * x ** 3 + np.sqrt(2 * step) * rng.standard_normal(x.shape)
    gone = ~np.isfinite(x) | (np.abs(x) > 1e6)
    print(f"unadjusted, step {step}: {gone.sum()} of 100000 chains gone after 1000 steps")
rng = np.random.default_rng(0)
x = start = rng.standard_normal(100_000)
step, moved = 0.5, np.zeros(100_000, dtype=int)
log_k = lambda to, fr: -(to - fr + step * fr ** 3) ** 2 / (4 * step)
for k in range(200):
    prop = x - step * x ** 3 + np.sqrt(2 * step) * rng.standard_normal(x.shape)
    accept = np.log(rng.random(x.shape)) < -prop ** 4 / 4 + x ** 4 / 4 + log_k(x, prop) - log_k(prop, x)
    x = np.where(accept, prop, x)
    moved += accept
print(f"with the accept step, step 0.5, 200 steps: {(np.abs(x) > 1e6).sum()} chains gone, variance {x.var():.4f}")
print(f"  {(moved == 0).sum()} chains never moved; the ones that moved have variance {x[moved > 0].var():.4f}")
g = np.linspace(-6, 6, 120001)
p = np.exp(-g ** 4 / 4)
print(f"the target's own variance: {(g ** 2 * p).sum() / p.sum():.4f}")
```

```bash
~/.vault-sandbox/bin/python light_tails.py
```

You should see:

![Unadjusted at step 0.3, 99003 of 100000 chains fly off; with the accept step at 0.5 none do, 1317 never move, and the overall variance is 0.7771 against the target's 0.6760|800](assets/energy-light-tails-without-and-with-the-accept-step.png)

Unadjusted Langevin loses one chain in 100,000 at step 0.1 and 99,003 at step 0.3. With the accept step at 0.5 none fly off. 1,317 chains had every proposal rejected in 200 steps and sit where they started, which leaves the overall variance at 0.7771. Their starting points all lie between 2.41 and 4.73 from 0 (`checks/ula_light_tails.out`, the same seed). The chains that moved have 0.6804 against the target's 0.6760.

*Table 1 on the pair.* The paper's Table 1 compares samplers by a log-likelihood column, LL, and a variance column. This runs its samplers on the pair with exact scores, every row seeded the same, through Algorithm 1 with 10 Langevin steps or 3 HMC steps of 3 leapfrog steps per level, the counts of the paper's appendix F. MALA's step 0.6 and HMC's 1.05 are fixed across levels and chosen so that about 63% and 74% of proposals are accepted on average (`checks/sampler_ladder.out`), near the 60% and 70% that appendix B.3 aims for; the paper instead scales each level's step with $\beta_t$. LL here is the mean log height of the samples under the true product; Var gap is the size of the difference between the samples' variance and the product's. Save this as `ladder.py`:

```python
import numpy as np
from experts import energy, summed_score

T = 100                                                     # the cosine schedule of the two-orders section
u = np.arange(T + 1) / T
ac = np.cos((u + 0.008) / 1.008 * np.pi / 2) ** 2
ac = ac / ac[0]
betas = np.concatenate([[0.0], np.clip(1 - ac[1:] / ac[:-1], 0, 0.999)])
abars = np.cumprod(1 - betas)
VP = 1 / (1 / 0.5 + 1 / 0.8)                               # the product: precisions add
MP = VP * (-1 / 0.5 + 1 / 0.8)


def reverse(rng):
    x = rng.standard_normal((100_000, 1))
    for t in range(T, 0, -1):
        x = (x + betas[t] * summed_score(x, abars[t])) / np.sqrt(1 - betas[t]) + np.sqrt(betas[t]) * rng.standard_normal(x.shape)
    return x


def langevin(x, ab, step, rng, adjust):
    prop = x + step * summed_score(x, ab) + np.sqrt(2 * step) * rng.standard_normal(x.shape)
    if not adjust:
        return prop
    log_k = lambda to, fr: (-(to - fr - step * summed_score(fr, ab)) ** 2).sum(-1) / (4 * step)
    log_a = energy(prop, ab) - energy(x, ab) + log_k(x, prop) - log_k(prop, x)
    return np.where((np.log(rng.random(len(x))) < log_a)[:, None], prop, x)


def hmc(x, ab, eps, rng, adjust):
    p = rng.standard_normal(x.shape)
    xn, pn = x, p
    for i in range(3):                                      # 3 leapfrog steps
        pn = pn + 0.5 * eps * summed_score(xn, ab)
        xn = xn + eps * pn
        pn = pn + 0.5 * eps * summed_score(xn, ab)
    log_a = energy(xn, ab) - (pn ** 2).sum(-1) / 2 - energy(x, ab) + (p ** 2).sum(-1) / 2
    keep = (np.log(rng.random(len(x))) < log_a) | (not adjust)
    return np.where(keep[:, None], xn, x)


def annealed(kernel, n_steps, rng):
    """Algorithm 1: every level from noisiest to clean, n_steps of the kernel, the cloud carried down."""
    x = rng.standard_normal((100_000, 1))
    for t in range(T, -1, -1):
        for i in range(n_steps):
            x = kernel(x, abars[t], rng)
    return x


rows = [
    ("Reverse", reverse),
    ("ULA, step 0.01", lambda r: annealed(lambda x, ab, g: langevin(x, ab, 0.01, g, False), 10, r)),
    ("ULA, MALA's step 0.6", lambda r: annealed(lambda x, ab, g: langevin(x, ab, 0.6, g, False), 10, r)),
    ("MALA, step 0.6", lambda r: annealed(lambda x, ab, g: langevin(x, ab, 0.6, g, True), 10, r)),
    ("U-HMC, HMC's step 1.05", lambda r: annealed(lambda x, ab, g: hmc(x, ab, 1.05, g, False), 3, r)),
    ("HMC, step 1.05", lambda r: annealed(lambda x, ab, g: hmc(x, ab, 1.05, g, True), 3, r)),
]
print("sampler                  variance   LL (higher is better)   Var gap (lower is better)")
for name, run in rows:
    x = run(np.random.default_rng(0))
    ll = np.mean(-0.5 * np.log(2 * np.pi * VP) - (x - MP) ** 2 / (2 * VP))
    print(f"{name:24s} {x.var():8.4f}   {ll:8.4f}                {abs(x.var() - VP):.4f}")
print(f"the true product's own LL: {-0.5 * np.log(2 * np.pi * np.e * VP):.4f}")
```

```bash
~/.vault-sandbox/bin/python ladder.py
```

You should see:

![Reverse scores LL -0.6802, above the true product's own -0.8296; ULA at MALA's step 0.6 ends at variance 12.1045; MALA's variance gap is 0.0001|900](assets/energy-table-1-on-the-pair.png)

By the variance gap the adjusted samplers win: MALA 0.0001, HMC 0.0012, against ULA at a small step 0.0047 and the reverse process 0.0974. By LL the reverse process looks best of all, which is wrong; [[#Step size and the accept step]] works out why.

**9. Clean up, and prove it.**

```bash
cd ~ && rm -r ~/playground/sandbox/energy-parameterisation
ls ~/playground/sandbox/energy-parameterisation; echo $?
```

You should see `No such file or directory`, then `2`.

### Reading the energy output

**From step 4, `before.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | f, and its shape | `[-3.247547 -0.333333 -0.057191] shape (3,)` | one energy per point. At 1.5: $-(1.5 + 0.707107)^2 / (2 \times 0.75) = -3.247547$ | derived below |
| 2 | the score's shape | `shape (3, 1)` | one slope per coordinate of each point | shown |
| 3 | slope of f | `[-2.942809 -0.942809  0.390524]` | equals the score line above it: the score is the energy's gradient | shown |
| 4 | eps at 1.5 | `2.08088` | $-0.707107 \times (-2.942809) = 2.080880$. Positive: a point to the right of the data most likely got there by positive noise | derived below |

**From steps 5, 6 and 7, `langevin.py` and `mala.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | no accept step, step 0.1: variance | `0.3671` | 19.3% wider than the product; the closed form, 0.3674, is 19.4% | shown; the plan 36 reference reading is the same, mean -0.2323 and variance 0.3671 |
| 2 | where step 0.1 settles | `0.3674` | $1 / (3.25 \times (1 - 0.1 \times 3.25 / 2)) = 1 / 2.721875 = 0.367394$ | derived below |
| 3 | with the accept step: variance | `0.3071` | within 0.0006 of the product, inside the sampling tolerance of 0.0041 (three standard errors) | shown; matches `checks/mala_step.out` |
| 4 | share accepted | `0.9582` | about 95,820 of 100,000 proposals kept per step; the rest stay put | shown |
| 5 | no accept step, step 0.01: variance | `0.3134` | the closed form says 0.3128, 1.7% wide; the sampled value is within one standard error, 0.0014, of it | derived below |

**From step 8, `one_proposal.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | proposal | `1.161107` | $1.5 + 0.1 \times (-5.625) + \sqrt{0.2} \times 0.5$ | derived below |
| 2 | height change | `1.719645` | the proposal sits higher on the product than the start | derived below |
| 3 | asymmetry of the move | `-1.440203` | moving back from 1.161107 to 1.5 is less likely than moving forward | derived below |
| 4 | accept probability | `1.000000` | $e^{0.279442} = 1.32$ is above 1, so the move is always kept | derived below |

**From step 8, `mixture.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | normalisers dropped | `-0.073834` | weights from $e^{f}$ alone give expert a a share of 0.407 instead of 0.465 | derived below |
| 2 | true heights | `-0.261437` | the true mixture's slope | derived below |
| 3 | fixed half weights | `-0.375000` | the average of -2 and 1.25; a fixed weighting of scores cannot follow the shares as they change along the axis | derived below |
| 4 | difference quotient | `-0.261437` | measured on the mixture's own log; agrees with field 2 | shown |

**From step 8, `step_sizes.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | the stability limit | `0.615385` | $2 / P = 2 / 3.25$: below it an unadjusted chain settles, above it it runs away | derived below |
| 2 | no accept step, step 0.6: variance | `12.4` | the closed form says 12.3077, forty times the product's width, just under the limit | derived below |
| 3 | no accept step, step 0.7: variance | `5.185e+42` | past the limit every step multiplies the spread; after 200 steps it is astronomical | derived below |
| 4 | with the accept step, step 0.8: variance | `0.3082` | still the product's width, at a step past the limit | shown; `checks/mala_step.out` has 0.3088 after 50 steps |
| 5 | with the accept step, step 0.8: share accepted | `0.3779` | 38% of proposals kept; the step size now trades only how fast chains move | shown; `checks/mala_step.out` has 0.3782 |

**From step 8, `light_tails.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | unadjusted, step 0.3: chains gone | `99003` | 99% of chains past $10^6$ from 0 or overflowed after 1,000 steps | shown; the same figure as `checks/ula_light_tails.out` |
| 2 | with the accept step, step 0.5 | `0 chains gone` | every proposal that lands far out is rejected, because the target's height there is tiny | derived below |
| 3 | chains that never moved | `1317` | started far enough out that every proposal overshot and was rejected; they still carry their starting points | shown |
| 4 | the target's own variance | `0.6760` | a sum of $x^2 e^{-x^4/4}$ over a fine axis; the moving chains' 0.6804 is near it | shown |

**From step 8, `ladder.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | Reverse: LL | `-0.6802` | higher than the true product's own LL, field 2, for a cloud 32% too narrow | derived below |
| 2 | the true product's own LL | `-0.8296` | $-\tfrac12 \log(2\pi e \times 0.307692)$: the LL of perfect samples | derived below |
| 3 | ULA at MALA's step 0.6: variance | `12.1045` | an unadjusted chain at the adjusted sampler's step size, just under the 0.615 limit at the clean level | shown; the same figure as `checks/sampler_ladder.out` |
| 4 | MALA: Var gap | `0.0001` | the accept step holds the width at a step 60 times larger than ULA's 0.01 | shown |

### How the energy works

**The noise estimate is the energy's slope times $-\sigma_t$.** A trained noise predictor gives the score as $-\epsilon_\theta / \sigma_t$ (section 2.3, sentence 4). Define the score as the gradient of one scalar and solve for $\epsilon$:

$$
\begin{aligned}
\nabla_x \log q_t(x) &\approx -\frac{\epsilon_\theta(x, t)}{\sigma_t} \\
\nabla_x \log q_t(x) &= \nabla_x f_\theta(x, t) \\
\epsilon_\theta(x, t) &= -\sigma_t\, \nabla_x f_\theta(x, t)
\end{aligned}
$$

At expert a with half the signal left, $\mathcal{N}(-0.707107, 0.75)$ and $\sigma_t = \sqrt{0.5} = 0.707107$, at $x = 1.5$:

$$
\begin{aligned}
f &= -\frac{(1.5 + 0.707107)^2}{2 \times 0.75} = -\frac{4.871320}{1.5} = -3.247547 \\
\nabla f &= -\frac{1.5 + 0.707107}{0.75} = -2.942809 \\
\epsilon &= -0.707107 \times (-2.942809) = 2.080880
\end{aligned}
$$

*Derived.* Step 4 printed the same three numbers.

**The accept test needs heights, and not their normaliser.** Write the target as $q(x) = e^{f(x)} / Z$. By the [exponent rules](../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=109), dividing two powers of $e$ subtracts their exponents. The test compares the target at the proposal with the target at the start:

$$
\frac{q(\hat x)}{q(x)} = \frac{e^{f(\hat x)} / Z}{e^{f(x)} / Z} = e^{f(\hat x) - f(x)}
$$

$Z$ cancels because both heights belong to the same target, which is why an unnormalised $f$ is enough. *Derived.* Plan 13 of the journey works the same cancellation by hand.

The worked proposal, with the product's energy $f(x) = -(x + 1)^2 / 1 - (x - 1)^2 / 1.6$ and step 0.1:

$$
\begin{aligned}
\text{summed score at } 1.5 &= -\frac{2.5}{0.5} - \frac{0.5}{0.8} = -5 - 0.625 = -5.625 \\
\hat x &= 1.5 + 0.1 \times (-5.625) + \sqrt{0.2} \times 0.5 = 1.5 - 0.5625 + 0.223607 = 1.161107 \\
f(1.5) &= -6.25 - 0.15625 = -6.40625 \\
f(1.161107) &= -\frac{2.161107^2}{1} - \frac{0.161107^2}{1.6} = -4.670383 - 0.016222 = -4.686605 \\
f(\hat x) - f(x) &= -4.686605 + 6.40625 = 1.719645
\end{aligned}
$$

The move's own probability is a Gaussian centred one Langevin step ahead, with $\log k(\text{to} \mid \text{from}) = -(\text{to} - \text{from} - 0.1\, s(\text{from}))^2 / 0.4$:

$$
\begin{aligned}
s(1.161107) &= -\frac{2.161107}{0.5} - \frac{0.161107}{0.8} = -4.322214 - 0.201384 = -4.523598 \\
\log k(x \mid \hat x) &= -\frac{(1.5 - 1.161107 + 0.452360)^2}{0.4} = -\frac{0.791253^2}{0.4} = -1.565203 \\
\log k(\hat x \mid x) &= -\frac{(1.161107 - 1.5 + 0.5625)^2}{0.4} = -\frac{0.223607^2}{0.4} = -0.125000 \\
\log a &= 1.719645 + (-1.565203 + 0.125000) = 1.719645 - 1.440203 = 0.279442
\end{aligned}
$$

$e^{0.279442} = 1.32$, so the accept probability is $\min(1, 1.32) = 1$. *Derived.* Step 8 printed each line.

**Why a score alone cannot supply the height change.** The height change between two points is the integral of the slope along a path between them. A score model would need many evaluations along that path for every proposal, and a network that outputs a vector is not guaranteed to be the slope of any one function. When it is not, different paths give different answers: in the journey's check, a rotating field gives $+3.141593$ along a path over the top and $-3.141593$ along one underneath, between the same two points, so no single height difference exists for an accept test to use. A network that outputs $f$ is the slope of one function by construction. *Cited:* the journey's answer key `checks/curl_field.out`. One dimension cannot show this, because every one-dimensional field is a slope; it needs two.

**Why the accept step makes any step size exact.** Write $a(x \to \hat x) = \min\left(1, \frac{q(\hat x)\, k(x \mid \hat x)}{q(x)\, k(\hat x \mid x)}\right)$. Then the flow from $x$ to $\hat x$ is

$$
q(x)\, k(\hat x \mid x)\, a(x \to \hat x) = \min\big(q(x)\, k(\hat x \mid x),\ q(\hat x)\, k(x \mid \hat x)\big)
$$

which is the same expression with $x$ and $\hat x$ swapped, so the flow back equals the flow forward and $q$ is left unchanged by every step, whatever its size. *Derived.* The step size changes only how many proposals are kept: 95.8% at 0.1 here.

**Why the unadjusted chain settles too wide.** On a Gaussian with precision $P$ and centre $\mu$, one Langevin step is $x' = x - \eta P (x - \mu) + \sqrt{2\eta}\, z$. Its variance at rest $V$ satisfies

$$
\begin{aligned}
V &= (1 - \eta P)^2\, V + 2\eta \\
V &= \frac{2\eta}{1 - (1 - \eta P)^2} = \frac{2\eta}{2\eta P - \eta^2 P^2} = \frac{1}{P\,(1 - \eta P / 2)}
\end{aligned}
$$

With $P = 3.25$: $\eta = 0.1$ gives $1 / 2.721875 = 0.367394$, and $\eta = 0.01$ gives $1 / 3.197188 = 0.312775$. Only $\eta \to 0$ reaches $1/P = 0.307692$. An offset from $\mu$ shrinks by the factor $1 - \eta P$ per step, 0.675 at 0.1 and 0.9675 at 0.01, so it falls by $e$ in about $1/(\eta P)$ steps: 3.1 and 30.8. *Derived.*

**Why a mixture needs the heights.** The log of a sum does not split the way the log of a product does:

$$
\begin{aligned}
\nabla \log\big(\tfrac12 q_a + \tfrac12 q_b\big) &= \frac{\tfrac12 q_a \nabla \log q_a + \tfrac12 q_b \nabla \log q_b}{\tfrac12 q_a + \tfrac12 q_b} \\
&= w_a\, \nabla \log q_a + w_b\, \nabla \log q_b, \qquad w_a = \frac{q_a}{q_a + q_b}
\end{aligned}
$$

At $x = 0$ the heights are $q_a = 0.207554$ and $q_b = 0.238743$, so $w_a = 0.465058$ and the slope is $0.465058 \times (-2) + 0.534942 \times 1.25 = -0.930116 + 0.668678 = -0.261437$ (to rounding). With the normalisers dropped, the weights come from $e^{-1} = 0.367879$ and $e^{-0.625} = 0.535261$, so $w_a = 0.407333$ and the slope is $-0.073834$. *Derived.* The two experts' normalisers differ by $\sqrt{0.8 / 0.5} = 1.264911$; the paper builds its mixtures assuming "this ratio [of normalizers] is 1". *Cited:* section 3, the mixture paragraph. On this pair that assumption moves expert a's share at 0 from 0.465 to 0.407.

### Step size and the accept step

**An unadjusted Langevin chain on a Gaussian of precision $P$ settles at variance $1 / (P(1 - \eta P/2))$ and runs away once its step $\eta$ passes $2/P$. A Metropolis accept step holds the target's width at any step, and turns the share of proposals accepted into the dial for choosing the step.** The settled variance is derived in [[#How the energy works]].

![Settled variance against step size with and without the accept step, and the share accepted above|800](assets/step-size-and-the-accept-step-the-concept.webp)

*The concept, settled variance against step size with and without the accept step, and the share accepted above.*

**The stability limit.** One unadjusted step multiplies an offset from the centre by $1 - \eta P$. The offset shrinks only while that factor is between $-1$ and $1$:

$$
\begin{aligned}
|1 - \eta P| < 1 \quad &\Longleftrightarrow \quad 0 < \eta < \frac{2}{P} \\
\frac{2}{P} = \frac{2}{3.25} &= 0.615385 \\
\eta = 0.6: \quad \frac{1}{3.25\,(1 - 0.6 \times 3.25 / 2)} &= \frac{1}{3.25 \times 0.025} = 12.3077
\end{aligned}
$$

*Derived.* Step 8's `step_sizes.py` printed 12.4 at 0.6 and $5.2 \times 10^{42}$ at 0.7. With the accept step the variance stayed between 0.3055 and 0.3084 from step 0.01 to 0.8. *Shown.*

**Light tails break unadjusted Langevin at every step size.** On $q \propto e^{-x^4/4}$ one step without noise is $x \mapsto x - \eta x^3 = x(1 - \eta x^2)$. It overshoots further each time once $|1 - \eta x^2| > 1$, that is once $|x| > \sqrt{2/\eta}$, which is $\sqrt{20} = 4.4721$ at step 0.1. From 5: $5 - 0.1 \times 125 = -7.5$, then 34.69, then $-4139$. *Derived*, with the sequence from `checks/ula_light_tails.out`. A Gaussian's pull grows like $x$, so one small step is safe everywhere; this pull grows like $x^3$, so every step size has a distance past which chains are lost, and the noise eventually carries some chain there: 1 in 100,000 at step 0.1. *Shown*, step 8. The paper names this case: "targets with lighter-than-Gaussian tails where the ULA chain is transient". *Cited:* `text/method.tex` line 142. The accept step rejects a proposal that lands where the target's height is tiny, so no chain leaves; the cost is chains that start far out and stay stuck, 1,317 of 100,000 at step 0.5.

**The share accepted is a dial.** On the clean product:

| Step size | Share accepted | Variance with the accept step |
|---|---|---|
| 0.01 | 99.9% | 0.3055 |
| 0.3 | 79% | 0.3081 |
| 0.5 | 60% | 0.3084 |
| 0.8 | 38% | 0.3082 |

The width is right on every row; only the share changes, and it falls as the step grows. A sampler can therefore raise its step until the share reaches a target. The paper does this, choosing the multiplier of $\beta_t$ in each level's step "so that the average acceptance rate of MALA and HMC samplers across timesteps is approximately 60% and 70% respectively". *Cited:* `text/appendix.tex` line 154. An unadjusted sampler has no such reading, because it accepts every proposal.

**Table 1 on the pair, and where its LL column misleads.** The paper's Table 1 scores samplers on its 2D toys by LL, the "log-likelihood of generated samples under composed distribution", and Var, a difference of variances. For the energy model's product it gives Var 0.064 for reverse diffusion, 0.027 for ULA, 0.022 for U-HMC, 0.013 for MALA and 0.009 for HMC, and LL $-6.03$ for reverse diffusion against 2.73 for MALA. *Cited:* `table/toy2d.tex` and `text/results.tex` line 17. The ladder in step 8 agrees on Var: reverse diffusion worst, the unadjusted samplers next, the two adjusted ones best, with MALA and HMC in the opposite order. On LL it disagrees: reverse diffusion scores highest. The mean log height under the product of samples with mean $m$ and variance $v$ is

$$
\begin{aligned}
\text{LL} &= -\tfrac12 \log(2\pi V_P) - \frac{v + (m - M_P)^2}{2 V_P} \\
\text{reverse, } m = -0.1567,\ v = 0.2102: \quad \text{LL} &= -0.329611 - \frac{0.2102 + 0.005486}{0.615385} = -0.329611 - 0.350490 = -0.680101 \\
\text{the product itself, } v = V_P,\ m = M_P: \quad \text{LL} &= -0.329611 - \tfrac12 = -0.829611
\end{aligned}
$$

with $M_P = -0.230769$ and $V_P = 0.307692$. *Derived*, using [the log](../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=110) of the Gaussian density; the printed $-0.6802$ differs in the last place because $m$ and $v$ are rounded here. LL rises as $v$ falls, so a cloud squeezed onto the product's peak beats samples of the product itself. On the paper's toys reverse diffusion leaves samples where the product has almost no height, as on the ring in Figure 2, and LL punishes that; on the pair its error is a squeeze, and LL rewards it. *Stated*: the paper does not say why its reverse row scores low. LL ranks samplers only beside a measure of width, as Table 1 sets it beside Var.

**The paper's step-size claim does not hold on the pair.** Appendix B.3 says that for the unadjusted variants "we set step sizes to be the same as adjusted samplers, and found limited gains when step sizes were specifically tuned towards the un-adjusted samplers". *Cited:* `text/appendix.tex` line 154. On the pair, at the adjusted samplers' steps, ULA ends at variance 12.1 and U-HMC at 2.96; ULA at its own step of 0.01 ends within 0.0047. Retuning is the whole difference here. *Shown*, step 8, `ladder.py`. Whether the paper's image models behave like the pair is not tested here.

### Other ways to get heights

- **The score parameterisation**, the ordinary $\epsilon_\theta$ network. One forward pass per noise estimate and no backward pass. It supports products and negation, has no mixtures, and allows only unadjusted samplers. *Cited:* section 3, last sentence; section 4.2, paragraphs 2 and 3.
- **A smaller step with no accept step**, as in step 7: the error falls with the step and the cost rises with it. *Shown.*
- **Other energy forms.** Appendix D compares a denoising-autoencoder form $-\tfrac12\|x - s_\theta\|^2$, an L2 form $-\tfrac12\|s_\theta\|^2$ and an inner-product form $x \cdot s_\theta$. Section 4.2 chooses $-\|s_\theta\|^2$, and appendix D gives stability under sampling as the reason: the L2 and autoencoder forms can never exceed 0, while the inner-product form has no ceiling. By Table A1's FID the inner-product form scored 90.9 against 91.5, lower being better. The gradient appendix D prints for the autoencoder form has the opposite sign of a measured difference quotient. The authors' 2D notebook uses a third form, `((score - x) ** 2).sum(-1)`, the autoencoder form without its one half (cell 5, line 14), while their PyTorch reimplementation uses `0.5 * (unet_out ** 2)` (`composable_diffusion/unet.py` line 1401). *Cited:* the journey's read-ahead, `read-ahead/04-scaling-compositional-generation.md`, chunk 57, and `checks/energy_parameterisations.out`.
- **HMC**, Hamiltonian Monte Carlo, another Metropolis-corrected sampler, which adds a momentum to each chain and uses the same kind of accept test. The paper's best compositional results come from MALA and HMC. *Cited:* section 4.2, paragraph 5. Not run here.

### Why the energy matters

[[#The order of multiplying and noising]] shows that reverse diffusion on summed scores misses the product, and that a sampler which settles at each noise level reaches it. The energy is what makes that per-level sampler exact at a step size worth paying for: on this pair, step 0.1 without the accept step settles 19.4% too wide, and with it lands within 0.2%. The acceptance rate is also a dial the sampler can read: the paper tunes its step sizes automatically from it, which unadjusted samplers cannot do. *Cited:* section 4.2, paragraph 5.

It does not explain when, during a run, summed scores go wrong. That is the two-orders section's question; the energy is the corrector run once the error is known to exist.

### The energy taught in, applied in

**Taught in:**

- the `drip-read` walk of Du et al., Reduce, Reuse, Recycle, abstract sentences 2 and 7. The walk's paper note, `deep-learning/diffusion-models/02-sampler-correctors-for-composition/papers/reduce-reuse-recycle/reduce-reuse-recycle.md` in this vault, is not written yet; link it here when it is.
- the same walk, section 4, chunks 50 and 52 to 58: only unadjusted samplers for a score model, Table 1 run on the pair and its LL column, the energy written as minus the gradient of a scalar, the stability limit $2/P$, light tails, and the share accepted as the dial for the step. Paper note at the same path, still to be written.
- the same journey's plan 21, `plans/21-langevin-dynamics.md`, line 143 and lines 215 to 226 (the stability limit 0.615385 and the settled widths at steps 0.1 and 0.01)
- the sampler correctors for composition journey's plans 33 to 36: `plans/33-a-mixture-needs-heights.md`, line 21 (a separate unknown constant per expert changes the mixture's shares); `plans/34-a-scalar-energy-whose-gradient-is-the-score.md`, lines 21 to 23 (a field with and without a height behind it, and the paper's two sign conventions); `plans/35-an-energy-from-an-ordinary-network.md`, line 23 (the appendix D forms and the autoencoder form's sign slip); `plans/36-the-accept-step-needs-the-height.md`, line 21 and line 280 (unadjusted Langevin against MALA on this pair)
- the same journey's plan 13, `plans/13-why-unnormalised-is-enough.md`, lines 133 to 144 (the normaliser cancelling in the acceptance ratio)

**Applied in:** nothing yet.

## Product, mixture and negation

Navigation: ⬅️ [[#The energy parameterisation]] | 📋 [[#Table of contents|TOC]] | [[#What an expert learns from its training set]] ➡️

**Section 3 of Du et al. names three ways to combine models: the product (equation 8), high only where every expert is high; the mixture (equation 9), high wherever any expert is high; and negation (equation 10), high where one expert is high and another is not. The product and negation are built from scores alone. The mixture needs each model's height, so a model that only outputs scores can multiply and negate but cannot mix.** *Cited:* Du et al., Reduce, Reuse, Recycle, section 3 (`text/method.tex` lines 10 to 54): "with the standard $\epsilon_\theta(x, t)$-parameterization we can, in theory, utilize product and negation composition, but *not* mixture composition."

### Words the three operators use

**Product**, $q^\text{prod}(x) = \frac{1}{Z}\prod_i q^i(x)$ with $Z = \int \prod_i q^i(x)\,dx$. The paper calls it an "intersection". Its peak is a compromise between the experts: [[#The product as an intersection]].

**Mixture**, $q^\text{mix}(x) = \frac{1}{N}\sum_i q^i(x)$. The paper calls it a "union". It needs no $Z$, because averaging densities keeps area 1 ([[Multivariate Normal Distribution#The area a product loses]]).

**Negation**, $q^\text{neg}(x) \propto q^0(x) / q^1(x)^\alpha$. The power $\alpha$ sets how hard $q^1$ is pushed away; the paper's experiments use $\alpha = 0.5$. The paragraph names the two densities $p_0$ and $p_1$ and the equation writes $q^0$ and $q^1$; they are the same two.

**Guidance as a product.** Classifier and classifier-free guidance multiply two experts: one for how likely $x$ is at all, one for how likely the label $y$ is given $x$. Their product is proportional to $p(x \mid y)$ by Bayes' rule. *Cited:* section 3, paragraph 3: "The approaches to guidance discussed in Section 2 define product models with only two experts."

### When to reach for the three operators

When a prompt holds AND, OR and NOT, as in Figure 6 below. AND is a product, OR a mixture, NOT a negation, and they nest. Before running one on a diffusion model, ask which operator each word needs. AND and NOT are scores added and subtracted, which any diffusion model supports. OR is not, and adding or averaging scores in its place samples a different distribution from the one asked for, as step 5 shows. *Derived* below.

### The form of the three operators

```text
product   q_prod = (1/Z) * q_1 * q_2         score: s_1 + s_2                     slopes only
mixture   q_mix  = (q_1 + q_2) / 2           score: w_1 s_1 + w_2 s_2,            needs heights
                                             w_i = q_i / (q_1 + q_2)
negation  q_neg  ~ q_0 / q_1^alpha           score: s_0 - alpha * s_1             slopes only
          a density only while  1/v_0 - alpha / v_1 > 0   (Gaussians; the precisions)
guidance  p(x | y) ~ p(x) * p(y | x)         score: s_x + s_(y|x)                 a product of two experts
```

![The three operators as three cards, each with two expert bells and the result bell, and what each needs (slopes or heights)|800](assets/three-operators-the-form.webp)

*The form, the three operators as three cards, each with two expert bells and the result bell, and what each needs (slopes or heights).*

### Try the three operators yourself

**1. What you need.** Python with NumPy, through the prepared environment:

```bash
~/.vault-sandbox/bin/python -c "import numpy; print(numpy.__version__)"
```

You should see a version number. This run printed `2.4.6`.

**2. When it is missing.** [[Multivariate Normal Distribution#Try sampling yourself]] steps 1 and 2 say how to make the environment, or how to use `uv run` instead.

**3. Make something to act on.** A new empty folder, and the pair of [[#The one-dimensional pair]] with the pieces every script uses: the density on an axis, its moments, the forward jump, the score, and `power`, which combines two Gaussians raised to any powers ([[Multivariate Normal Distribution#Powers of Gaussians]]).

```bash
mkdir -p ~/playground/sandbox/three-operators && cd ~/playground/sandbox/three-operators
```

Save this as `experts.py`:

```python
import numpy as np

experts = [(-1.0, 0.5), (1.0, 0.8)]          # (mean, variance) of expert a and expert b
x = np.linspace(-8, 8, 1601)                  # the axis, spacing 0.01
dx = x[1] - x[0]


def gauss(z, m, v):
    return np.exp(-(z - m) ** 2 / (2 * v)) / np.sqrt(2 * np.pi * v)


def moments(p):
    """Area, mean and variance of heights p on the axis."""
    area = p.sum() * dx
    mean = (x * p).sum() * dx / area
    return area, mean, ((x - mean) ** 2 * p).sum() * dx / area


def noised(m, v, abar):
    """A Gaussian N(m, v) after the forward jump to level abar."""
    return np.sqrt(abar) * m, abar * v + 1 - abar


def score(z, m, v, abar=1.0):
    mt, vt = noised(m, v, abar)
    return -(z - mt) / vt


def power(m1, v1, w1, m2, v2, w2):
    """q1^w1 * q2^w2 for two Gaussians, renormalised: (mean, variance, precision)."""
    P = w1 / v1 + w2 / v2
    if P <= 0:
        return float("nan"), float("nan"), P
    return (w1 * m1 / v1 + w2 * m2 / v2) / P, 1 / P, P
```

**4. Look at it before: the product, and guidance as a product.** Save this as `product.py`:

```python
from experts import experts, x, dx, gauss, moments, noised, score, power

(ma, va), (mb, vb) = experts
qa, qb = gauss(x, ma, va), gauss(x, mb, vb)
Z = (qa * qb).sum() * dx                                      # equation 8's Z
i = 800                                                       # x[800] is 0
print(f"equation 8 at x = 0: q_a {qa[i]:.6f} times q_b {qb[i]:.6f} = {qa[i] * qb[i]:.6f}; over Z = {Z:.6f}: {qa[i] * qb[i] / Z:.6f}")
area, m, v = moments(qa * qb / Z)
print(f"the product: area {area:.6f}, mean {m:.6f}, variance {v:.6f}; the experts' variances {va} and {vb}")
mp, vp, _ = power(ma, va, 1, mb, vb, 1)
for abar in (1.0, 0.5):
    summed = score(1.5, ma, va, abar) + score(1.5, mb, vb, abar)
    print(f"guidance at x = 1.5, abar {abar}: scores added {summed:.6f}, the noised product's own slope {score(1.5, mp, vp, abar):.6f}")
```

```bash
~/.vault-sandbox/bin/python product.py
```

You should see:

![Equation 8 at 0 gives 0.049552 over Z = 0.075126, which is 0.659582; the product's variance is 0.307692; the added scores equal the product's slope with no noise, -5.625, and differ with half the signal left, -3.823802 against -2.543685|900](assets/three-operators-the-product-and-guidance.png)

The product is narrower than both experts, 0.308 against 0.5 and 0.8: it is stricter than either alone. With no noise, guidance's added scores are exactly the product's slope. With half the signal left they are not, which is [[#The order of multiplying and noising]] again, because guidance is a product.

**5. The failure, and the technique: a mixture's slope.** Save this as `mixture.py`:

```python
import numpy as np
from experts import experts, x, dx, gauss, moments, score

(ma, va), (mb, vb) = experts
qa, qb = gauss(x, ma, va), gauss(x, mb, vb)
area, m, v = moments(0.5 * qa + 0.5 * qb)                     # equation 9 with N = 2
print(f"the mixture: area {area:.6f}, mean {m:+.6f}, variance {v:.6f}")
ha, hb = gauss(0.0, ma, va), gauss(0.0, mb, vb)
sa, sb = score(0.0, ma, va), score(0.0, mb, vb)
wa = ha / (ha + hb)
print(f"at x = 0: heights {ha:.6f} and {hb:.6f}, shares {wa:.6f} and {1 - wa:.6f}")
print(f"at x = 0: slopes {sa:.6f} and {sb:.6f}")
print(f"  weighted by the shares (the true mixture): {wa * sa + (1 - wa) * sb:.6f}")
print(f"  added, as a product would:                 {sa + sb:.6f}")
print(f"  averaged with fixed halves:                {(sa + sb) / 2:.6f}")
for c in (2.0, 0.5):
    area, m, v = moments(qa + c * qb)                         # expert b's height off by a factor c
    print(f"expert b's height off by a factor {c}: mean {m:+.6f}, variance {v:.6f}")
```

```bash
~/.vault-sandbox/bin/python mixture.py
```

You should see:

![The mixture has area 1 and variance 1.65; at 0 the shares are 0.465 and 0.535 and the true slope is -0.261437, against -0.75 for added scores and -0.375 for averaged ones; with expert b's height doubled the mean moves to +0.333|850](assets/three-operators-the-mixture-and-its-slope.png)

The mixture is wider than both experts, 1.65 against 0.5 and 0.8, where the product was narrower. Two ways of building it from scores alone both miss its slope: adding gives the product's $-0.75$, and fixed halves give $-0.375$. Only the shares, which come from the heights, give $-0.261$. And a height known only up to a factor is not enough: doubling expert b's height moves the mixture's centre from 0 to 0.333.

**6. The technique for negation.** Save this as `negation.py`:

```python
from experts import experts, x, gauss, moments, noised, score, power

(ma, va), (mb, vb) = experts
alpha = 0.5
area, m, v = moments(gauss(x, ma, va) / gauss(x, mb, vb) ** alpha)   # equation 10 on the axis
mc, vc, P = power(ma, va, 1, mb, vb, -alpha)
print(f"a over b^{alpha}: on the axis mean {m:.6f}, variance {v:.6f}; closed form mean {mc:.6f}, variance {vc:.6f}, precision {P:.6f}")
print(f"slope at 1.5: score a - {alpha} score b = {score(1.5, ma, va) - alpha * score(1.5, mb, vb):.6f}; closed form {-(1.5 - mc) / vc:.6f}")
for name, args in [("b over a^0.5", (mb, vb, 1, ma, va, -0.5)), ("b over a", (mb, vb, 1, ma, va, -1.0)),
                   ("notebook, a^1.3 / b^0.3", (ma, va, 1.3, mb, vb, -0.3))]:
    mm, vv, PP = power(*args)
    print(f"{name:24s} precision {PP:+.6f}  mean {mm:.6f}  variance {vv:.6f}")
m1, v1 = noised(mc, vc, 0.5)
m2, v2, _ = power(*noised(ma, va, 0.5), 1, *noised(mb, vb, 0.5), -alpha)
print(f"abar 0.5: negate then noise variance {v1:.6f}; noise then negate variance {v2:.6f}")
```

```bash
~/.vault-sandbox/bin/python negation.py
```

You should see:

![a over the square root of b has mean -1.909 and variance 0.727 with precision 1.375; its slope at 1.5 is -4.6875 from scores alone; b over a has precision -0.75; the notebook's weights give variance 0.449; with half the signal left, negate then noise gives 0.864 and noise then negate 1.286|1000](assets/three-operators-negation.png)

Dividing by $\sqrt{b}$ moves expert a from $-1$ to $-1.909$, away from b, and widens it from 0.5 to 0.727. Its slope is expert a's score minus half of b's, so scores suffice. Swap the roles and divide b by all of a, and the precision is $-0.75$: the result grows without limit and is no density. With noise, the order matters the other way round from the product: noising first makes the negation too wide, 1.286 against 0.864, where it made the product too narrow.

**7. Another way to get the same answer.** Each script checks itself: `product.py` measures the product on the axis and `power` gives it in closed form; `negation.py` prints the axis and the closed form side by side and they agree to six places; `mixture.py`'s share-weighted slope matches the difference quotient of the mixture's own log in [[#Try the energy yourself]] step 8.

**8. More worked examples on the same setup.** *The paper's code, checked against its equations.* The authors' notebook builds negation in cell 8, line 15, as `1.3 * unorm_1 - 0.3 * unorm_2`, which is $q_a^{1.3} / q_b^{0.3}$. No $\alpha$ in equation 10 gives that. The fourth line of step 6 prints what it does on the pair: mean $-1.337$, variance $0.449$, against equation 10's $-1.909$ and $0.727$. The mixture in cell 7, lines 13 to 19, is `-jax.scipy.special.logsumexp(-concat_energy*3.5, -1)`, which raises each density to the power 3.5 before mixing; equation 9 has no such power. *Cited:* the journey's read-ahead, `read-ahead/03-compositional-generation-beyond-guidance.md`, chunks 38 and 40, quoting `notebooks/simple_distributions.ipynb`.

**9. Clean up, and prove it.**

```bash
cd ~ && rm -r ~/playground/sandbox/three-operators
ls ~/playground/sandbox/three-operators; echo $?
```

You should see `No such file or directory`, then `2`.

### Reading the three-operators output

**From step 4, `product.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | raw product at 0 | `0.049552` | $0.207554 \times 0.238743$: the two heights multiplied, before equation 8 divides | derived below |
| 2 | over $Z$ | `0.659582` | the product's true height at 0, once divided by its area 0.075126 | derived below |
| 3 | variance | `0.307692` | narrower than both experts: precisions add | derived below |
| 4 | guidance, no noise | `-5.625000` both | the added scores are the product's own slope | derived below |
| 5 | guidance, half the signal: added | `-3.823802` | equation 12's slope, the curve summed scores give | derived in [[#How the two orders work]] |
| 6 | the noised product's slope | `-2.543685` | equation 11's slope, the curve the reverse process needs | derived in [[#How the two orders work]] |

**From step 5, `mixture.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | area | `1.000000` | a mixture keeps area 1, with no $Z$ | derived below |
| 2 | variance | `1.650000` | wider than both experts | derived below |
| 3 | shares at 0 | `0.465058`, `0.534942` | each expert's height over the two heights added | derived in [[#How the energy works]] |
| 4 | the true slope | `-0.261437` | shares times slopes, added | derived in [[#How the energy works]] |
| 5 | scores added | `-0.750000` | the product's slope: an AND where an OR was asked for | derived below |
| 6 | scores averaged | `-0.375000` | fixed halves; wrong wherever the heights differ | derived below |
| 7 | height off by 2 | `+0.333333` | the centre moves toward the expert whose height was overstated | derived below |

**From step 6, `negation.py`:**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | $a / b^{0.5}$ | mean `-1.909091`, variance `0.727273` | moved away from b and widened; the axis and the closed form agree | derived below |
| 2 | its precision | `1.375000` | $2 - 0.5 \times 1.25$, positive, so a density | derived below |
| 3 | slope at 1.5 | `-4.687500` | $-5 - 0.5 \times (-0.625)$: scores alone | derived below |
| 4 | $b / a^{0.5}$ | precision `+0.25`, mean `9` | a density, but centred past the end of the axis at 8 | derived below |
| 5 | $b / a$ | precision `-0.75` | not a density; `nan` is the script refusing to divide | derived below |
| 6 | the notebook's weights | variance `0.449438` | what cell 8 actually samples on this pair | derived below |
| 7, 8 | the two orders at $\bar\alpha = 0.5$ | `0.863636`, `1.285714` | negate then noise against noise then negate: noising first is 49% too wide | derived below |

### How the three operators work

**Equation 8 at one point.** The heights at 0 are $q_a(0) = e^{-1}/\sqrt{\pi} = 0.207554$ and $q_b(0) = e^{-0.625}/\sqrt{1.6\pi} = 0.238743$:

$$
\begin{aligned}
q_a(0)\,q_b(0) &= 0.207554 \times 0.238743 = 0.049552 \\
Z &= \mathcal{N}(-1;\ 1,\ 1.3) = 0.075126 \\
q^\text{prod}(0) &= 0.049552 / 0.075126 = 0.659582
\end{aligned}
$$

*Derived;* $Z$ is worked in [[Multivariate Normal Distribution#The area a product loses]].

**Why guidance's scores add.** The log of a product is the sum of the logs ([log rules](../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=110)), and $\log p(y)$ does not depend on $x$:

$$
\begin{aligned}
p(x \mid y) &= \frac{p(x)\, p(y \mid x)}{p(y)} \\
\nabla_x \log p(x \mid y) &= \nabla_x \log p(x) + \nabla_x \log p(y \mid x) - 0
\end{aligned}
$$

On the pair, with expert a as $p(x)$ and expert b's shape as $p(y \mid x)$, at 1.5: $-\frac{2.5}{0.5} - \frac{0.5}{0.8} = -5 - 0.625 = -5.625$, and the product $\mathcal{N}(-0.230769, 0.307692)$ has slope $-\frac{1.730769}{0.307692} = -5.625$. *Derived.* That reading of the two experts is the walk's, from the sentence quoted under [[#Words the three operators use]].

**Why guidance shares the two-orders gap.** A guided sampler adds the two models' scores at each noise level, which is equation 12's curve, while the reverse process needs equation 11's. The gap in variance is 0 with no noise, 0.2448 at half the signal and 0.5 at pure noise ([[#Try the two orders yourself]] step 7), so it is largest at the noisiest steps. *Derived* from those rows. How large it is for a trained text-to-image model is not measured here.

**The mixture's moments.** Each expert contributes its own variance plus its mean squared, weighted by its share:

$$
\begin{aligned}
\text{mean} &= \tfrac12(-1) + \tfrac12(1) = 0 \\
\text{variance} &= \tfrac12(0.5 + 1) + \tfrac12(0.8 + 1) - 0^2 = 1.65
\end{aligned}
$$

If expert b's height is overstated by a factor 2, the shares become $\tfrac13$ and $\tfrac23$:

$$
\begin{aligned}
\text{mean} &= \tfrac13(-1) + \tfrac23(1) = 0.333333 \\
\text{variance} &= \tfrac13(1.5) + \tfrac23(1.8) - 0.333333^2 = 1.7 - 0.111111 = 1.588889
\end{aligned}
$$

*Derived.* This is the paper's "a different unknown ratio of normalizers would correspond to a weighted mixture", on numbers. *Cited:* section 3, the mixture paragraph.

**Why no fixed rule on scores builds a mixture.** The mixture's slope is $w_a s_a + w_b s_b$ with $w_a = q_a / (q_a + q_b)$ ([[#How the energy works]]). The shares change along the axis: expert a's is 0.939 at $-1$, 0.465 at 0 and 0.023 at 1 (`checks/mixture_score.out`). Adding scores fixes both weights at 1 and averaging fixes them at $\tfrac12$, and neither follows the shares. *Derived.*

**Negation as a power.** Raising a Gaussian to the power $w$ multiplies its precision by $w$ ([[Multivariate Normal Distribution#Powers of Gaussians]]), so with $\alpha = 0.5$:

$$
\begin{aligned}
P &= \frac{1}{0.5} - 0.5 \times \frac{1}{0.8} = 2 - 0.625 = 1.375, \qquad \text{variance } \frac{1}{1.375} = 0.727273 \\
\text{mean} &= \frac{-1/0.5 - 0.5 \times 1/0.8}{1.375} = \frac{-2.625}{1.375} = -1.909091 \\
\text{slope at } 1.5 &= -\frac{2.5}{0.5} - 0.5 \times \left(-\frac{0.5}{0.8}\right) = -5 + 0.3125 = -4.6875
\end{aligned}
$$

The result is a density only while $P > 0$, so the expert being pushed away must be broad enough, with $\alpha / v_1 < 1 / v_0$. Here $0.625 < 2$. For $b / a$, $1.25 - 2 = -0.75$. *Derived.*

**The two orders for negation.** At $\bar\alpha = 0.5$, negate then noise is $0.5 \times 0.727273 + 0.5 = 0.863636$. Noise each first, $a \to \mathcal{N}(-0.707107, 0.75)$ and $b \to \mathcal{N}(0.707107, 0.9)$, then negate: $P = \frac{1}{0.75} - \frac{0.5}{0.9} = 1.333333 - 0.555556 = 0.777778$, variance $1.285714$. Subtracting a noised precision removes less than subtracting a clean one, so the result is wider. *Derived.*

### Other ways to combine models

- **Background-divided composition**, $p_1 p_2 / p_b$, which is a product with one negation at power 1. [[#Composing models with a background]] works it on two-pixel scenes.
- **Guidance scale**, $\nabla \log p(x) + \lambda \nabla \log p(y \mid x)$, which is the product $p(x)\, p(y \mid x)^\lambda$: $\lambda = 2$ on the pair gives mean 0.111 and variance 0.222. *Cited:* `checks/guidance_on_the_object.out`.
- **A mixture from energy models.** [[#The energy parameterisation]] gives each model a height, which is what the mixture's shares need. The paper assumes the ratio of the normalisers is 1; step 5 shows what a factor of 2 does.

### Why the three operators matter

Which operator a prompt asks for decides whether a score model can serve it at all. AND and NOT can, OR cannot. "A cat or a dog" from a mixture gives one or the other per image, never both in one image, while "a cat and a dog" from a product gives whatever lies in both experts' high regions. If the cat expert is high only on images that are entirely cat, that shared region holds only blends, which is the hybrid of [[#Why composition matters]]. *Stated:* the link between what an expert's high region contains and a hybrid is the writer's reading of the two sections together.

![The paper's Figure 6: five columns of two generated horses, labelled "A horse", then AND "Grass plains", AND "A sandy beach", AND ("A sandy beach" OR "Grass plains"), and that AND NOT "Sunny"|900](references/three-operators-paper-figure-6-horses.png)

> **Figure 6.** Energy based parameterization enables high-resolution compositional text-to-image synthesis.
>
> *Du, Durkan, Strudel, Tenenbaum, Dieleman, Fergus, Sohl-Dickstein, Doucet, Grathwohl, Reduce, Reuse, Recycle, ICML 2023, [arXiv 2302.11552](https://arxiv.org/abs/2302.11552), Figure 6. arXiv non-exclusive distribution licence; copied for study with citation.*

The labels use all three operators nested: AND a product, OR a mixture, NOT a negation. Column 4's two images each show one place, sand or grass, as a mixture should. In column 5 the bottom horse stands under an overcast sky; the top image's sky is pale blue with no sun in view. The figure has no column sampled without composition, and no model or code was released, so none of it can be rerun. *Shown*, read by eye from the image; *cited* for the release, the journey's read-ahead, chunk 42.

*🖼️ Diagram wanted: the mechanism, slopes adding for the product and negation and height-weighted for the mixture. Prompt 15 in the same file.*

![The deep-dive sheet composing the form, the mechanism and the three runs|800](assets/three-operators-deep-dive-sheet.webp)

*The deep-dive sheet composing the form, the mechanism and the three runs.*

### The three operators taught in, applied in

**Taught in:** the `drip-read` walk of Du et al., Reduce, Reuse, Recycle, section 3, chunks 35 to 43 (equations 8, 9 and 10, guidance as a product, Figures 2 and 6, and the two notebook slips), with numbers from the walk's answer keys `checks/step6_product.out`, `guidance_on_the_object.out`, `mixture_score.out` and `negation.out`. The walk's paper note, `deep-learning/diffusion-models/02-sampler-correctors-for-composition/papers/reduce-reuse-recycle/reduce-reuse-recycle.md` in this vault, is not written yet; link it here when it is.

**Applied in:** nothing yet.

## What an expert learns from its training set

Navigation: ⬅️ [[#Product, mixture and negation]] | 📋 [[#Table of contents|TOC]]

**A diffusion expert trained with the noise-prediction loss learns the density of the points it is shown and never reads their labels. Labels change what is learned only in a part that reads them: a conditional model's rule for which samples train which condition, and a classifier used for guidance.** "An expert trained on A data learns the concept A" is true only in the first sense: it learns its training set, including whatever B points are hidden in it. *Derived* below from the loss, whose arguments hold no label.

### Words this section uses

**Hidden B.** A point that has property B but whose label does not say so. In the toy below, B is $x_2 > 0$ and the point $(-0.5, 0.5)$ is labelled only "A".

**"Contains A" and "exactly A".** Two rules for training a conditional model on points that carry several labels. Under "contains A", every point whose label set includes A trains the condition A. Under "exactly A", only points labelled A alone train it, and a point labelled {A, B} trains a separate condition.

**Guidance.** Adding a second score to steer sampling, here $\nabla \log p(B \mid x)$ from a classifier. [[#Product, mixture and negation]] shows it is a product of two experts.

### When to reach for it

When a plan says an expert "learns concept A", or proposes relabelling data to change what a composition produces. Ask which part of the system reads the label. If nothing does, relabelling changes nothing and only adding or removing points moves the expert. If a classifier reads it, a missing label teaches the classifier the wrong answer in exactly the region the composition is meant to reach.

### The form

```text
loss(theta) = mean over x0, t, eps of  || eps - eps_theta( sqrt(abar_t) * x0 + sqrt(1 - abar_t) * eps, t ) ||^2
                                          arguments: the point x0, the level t, the noise eps; no label
condition A trains on  { x0 : "A" in labels(x0) }        "contains A": every A-and-B point stays
                   or  { x0 : labels(x0) == {"A"} }      "exactly A": labelled A-and-B points leave
classifier p(B | x)  ->  share of training points near x labelled B        what cross-entropy fits
guided score  =  grad log p(x | A)  +  w * grad log p(B | x)                points toward B as labelled
```

![One training set flowing into three readers (the loss, the conditioning rule, the classifier) with the label reaching only the last two|800](assets/expert-and-labels-the-form.webp)

*The form, one training set flowing into three readers (the loss, the conditioning rule, the classifier) with the label reaching only the last two.*

### Try it yourself

> [!warning] Not run on this machine
> The cluster has no prepared environment, so nothing below has been run. The expected lines are worked by hand under [[#How the expert's training set works]], and the next machine with `~/.vault-sandbox/bin/python` runs it and files the real output.

1. You need the prepared environment: `~/.vault-sandbox/bin/python -c "import numpy"` prints nothing when it is there.
2. If it is missing, make it once: `uv venv ~/.vault-sandbox` then `uv pip install --python ~/.vault-sandbox/bin/python pandas numpy scipy matplotlib statsmodels openpyxl`.
3. Make an empty folder:

   ```bash
   mkdir -p ~/playground/sandbox/expert-and-labels && cd ~/playground/sandbox/expert-and-labels
   ```

4. Save this as `labels.py`. The three points are all A ($x_1 < 0$), and the third is also B ($x_2 > 0$). Set 1 labels it "A" only; set 2 labels it "A,B". The script computes expert A's loss and gradient for a small linear noise predictor, which set of points each conditioning rule hands to condition A, and what a classifier fit to the labels says about the top-left quadrant:

   ```python
   # What expert A learns under two labellings of the same three points.
   import numpy as np

   points = np.array([[-0.5, -0.5], [-0.6, -0.4], [-0.5, 0.5]])   # every point has x1 < 0, so all are A
   sets = {"set 1": ["A", "A", "A"],         # the third point also has x2 > 0 (B), unlabelled
           "set 2": ["A", "A", "A,B"]}       # the same points, the third labelled with both

   rng = np.random.default_rng(0)
   W = rng.standard_normal((2, 2))            # a linear noise predictor, eps_hat = x_t @ W
   abar = rng.uniform(0.1, 0.9, size=3)       # one noise level per point
   eps = rng.standard_normal((3, 2))          # one noise draw per point, shared by both sets

   def ddpm_loss_and_grad(x0):                # the label is not an argument
       xt = np.sqrt(abar)[:, None] * x0 + np.sqrt(1 - abar)[:, None] * eps
       r = xt @ W - eps
       return (r ** 2).sum(axis=1).mean(), 2 * xt.T @ r / len(x0)

   top_left = (points[:, 0] < 0) & (points[:, 1] > 0)    # the A-and-B quadrant
   results = {}
   for name, labels in sets.items():
       tags = [set(l.split(",")) for l in labels]
       contains = np.array(["A" in t for t in tags])
       exactly = np.array([t == {"A"} for t in tags])
       is_B = np.array(["B" in t for t in tags])
       results[name] = ddpm_loss_and_grad(points)
       print(f"{name}: share of condition A in A and B {top_left[contains].mean():.3f} (contains A), "
             f"{top_left[exactly].mean():.3f} (exactly A); classifier p(B | top-left) {is_B[top_left].mean():.3f}")

   (l1, g1), (l2, g2) = results["set 1"], results["set 2"]
   print(f"expert A: same loss {l1 == l2}, same gradient {np.array_equal(g1, g2)}")
   ```

5. Run it:

   ```bash
   ~/.vault-sandbox/bin/python labels.py
   ```

   You should see, by the hand working below (not yet run):

   ```
   set 1: share of condition A in A and B 0.333 (contains A), 0.333 (exactly A); classifier p(B | top-left) 0.000
   set 2: share of condition A in A and B 0.333 (contains A), 0.000 (exactly A); classifier p(B | top-left) 1.000
   expert A: same loss True, same gradient True
   ```

6. Clean up, and check the folder is gone:

   ```bash
   cd ~ && rm -r ~/playground/sandbox/expert-and-labels
   ls ~/playground/sandbox/expert-and-labels; echo $?
   ```

   You should see `No such file or directory` and `2`.

### Reading the labels output

| # | Field | Expected value | How to read it | Backing |
|---|---|---|---|---|
| 1 | share of condition A in A and B, contains A | `0.333` in both sets | one of the three points condition A trains on sits in the top-left quadrant, whatever its label says | derived below |
| 2 | the same, exactly A | `0.333` in set 1, `0.000` in set 2 | under "exactly A", honest labelling removes the A-and-B point from condition A, so $p(x \mid A)$ loses its mass there | derived below |
| 3 | classifier $p(B \mid \text{top-left})$ | `0.000` in set 1, `1.000` in set 2 | a classifier fit to set 1 learns that the top-left point is not B, which is the labels' mistake | derived below |
| 4 | expert A, same loss and same gradient | `True`, `True` | the unconditional expert sees identical numbers under both labellings, so training follows the same path | derived below |

### How the expert's training set works

1. **The loss holds no label.** The simplified DDPM loss is $L(\theta) = \mathbb{E}_{x_0, t, \varepsilon}\,\lVert \varepsilon - \varepsilon_\theta(\sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon,\ t) \rVert^2$. *Cited:* Ho et al., equation (14). Two training sets with the same points and different labels give the same $L$ and the same $\nabla_\theta L$ at every $\theta$, so gradient descent from the same start and seed follows the same path. *Derived.* This is field 4.
2. **What the loss fits.** Its minimiser predicts the noise that the noised training density's score implies, so a trained expert matches the training set's density smoothed by the noise. *Cited:* Ho et al., section 3.2, on the link to denoising score matching. In the toy, one point of three sits in the top-left quadrant, so an expert that fits the set well puts roughly a third of its mass there. *Stated:* how close a trained network comes to that third depends on its capacity and training, which is not measured here.
3. **The conditioning rule decides which points train condition A.** Under "contains A" all three points train it, and the top-left share is $1/3 = 0.333$ in both sets. Under "exactly A", set 2's third point is labelled {A, B} and trains another condition, so condition A trains on the two points at $(-0.5, -0.5)$ and $(-0.6, -0.4)$, neither in the top-left, and the share is $0/2 = 0$. The composed score $s(x \mid A) + s(x \mid B) - s(x)$ targets $p(x \mid A)\,p(x \mid B)/p(x)$, a product, and [[#The product as an intersection]] shows a product puts mass only where each factor has some. With $p(x \mid A)$ near zero on the top-left, the composition has little to find there. *Derived.* These are fields 1 and 2.
4. **A classifier learns the labels' share.** Over $n$ training points in a small region, $n_B$ of them labelled B, cross-entropy is $-[\,n_B \log q + (n - n_B) \log(1 - q)\,]$ for a predicted $q = p(B \mid x)$. Its derivative, $-n_B/q + (n - n_B)/(1 - q)$, is zero at $q = n_B / n$. *Derived.* In the top-left, $n = 1$: set 1 has $n_B = 0$, so $q = 0$, and set 2 has $n_B = 1$, so $q = 1$. This is field 3.
5. **Guidance then pushes away.** With $p(B \mid x)$ near 0 in the top-left and near 1 where labelled B points sit, $\nabla_x \log p(B \mid x)$ points out of the top-left toward those points, so the guided score $s(x \mid A) + w\,\nabla_x \log p(B \mid x)$ steers samples away from A-and-B. *Derived* from step 4; a trained classifier's exact gradient is not computed here.

The walk called step 5 a shortcut. Shortcut learning names a decision rule that does well on the training benchmark and fails to transfer, such as a classifier leaning on a feature that travels with the label. *Cited:* Geirhos et al. 2020, abstract. Here the classifier learns the labels' own mistake, which the field calls label noise, or positive-unlabelled data when only some positives carry the label. *Stated:* those two names are the writer's, not checked against a source.

![The three points in their quadrants under set 1 and set 2, with what each reader learns|800](assets/expert-and-labels-the-mechanism.webp)

*The mechanism, the three points in their quadrants under set 1 and set 2, with what each reader learns.*

### Other ways to keep labels from steering the result

- **One unconditional expert per concept**, each trained on its own subset. Nothing reads a label, so relabelling is a no-op and only the subset's points matter. This is what the field calls a product of experts.
- **A conditional model with "contains A" labels**, so every point with A in its label set trains condition A, and an A-and-B point keeps its mass in $p(x \mid A)$.
- **Classifier-free guidance** in place of a separate classifier. It still reads labels, through the condition, so the rule above still applies.

### Why the training set matters

The repaired claim: **a density expert learns its training set's density, and labels matter only where something reads them.** Before blaming a composition for missing the A-and-B region, count the A-and-B points each factor was trained on under the conditioning rule actually in use, and check whether a classifier in the loop was trained on labels that miss B.

![The deep-dive sheet composing the form, the mechanism and the expected output|800](assets/expert-and-labels-the-deep-dive.webp)

*The deep-dive sheet composing the form, the mechanism and the expected output.*

### When neither training set holds A and B

**A product of two experts has density only where both experts have density, so it reaches an A-and-B combination that neither training set contains only as far as something gives each expert density there.** If $p_A(x) = 0$ then $p_A(x)\,p_B(x) = 0$ whatever $p_B(x)$ is, so the product's support is the intersection of the two supports. *Derived:* this is the product rule for zero and needs no experiment. The field calls producing combinations never seen together compositional generalisation, or out-of-support generation. *Stated:* the walk's names, not checked against one source.

**When to reach for it.** When a plan hopes composition will produce a combination missing from every training set, such as chest X-rays with a pneumothorax and no chest drain, built from a pneumothorax expert and a no-drain expert. Before training anything, ask where each expert gets density in A-and-B. Turning the share of A-and-B points in each training set down to 0% is no experiment, because the product rule already fixes the answer: the product's mass in A-and-B falls to whatever smoothing leaves.

**The form.**

```text
support(p_A * p_B)  =  support(p_A)  ∩  support(p_B)
p_A(x) = 0   =>   p_A(x) * p_B(x) = 0, whatever p_B(x) is
a trained expert's density in A∩B  =  its training data there  +  the smoothing tail  +  anything the network adds
```

A trained expert matches its training set smoothed by the noise, as step 2 of [[#How the expert's training set works]] says. In 2D, an earlier walk measured trained MLP experts within 0.04 nats of the ideal smoothed-data experts, so there the third term is absent. *Cited:* run 2 of the overlap-dial walk, `artifacts/ideas/poe-overlap-dial/IDEA_MAP.md` line 157 in the reduce-reuse-recycle research repository.

**Try it yourself.** The two experts are the ones the authors' notebook composes in its ring-times-bar toy (`notebooks/simple_distributions.ipynb` in the reduce-reuse-recycle repository). Cell 14 builds a ring of 8 Gaussian modes at radius 0.5, cell 32 line 49 trains it with mode width 0.03, and cell 17 builds a bar uniform on $|x_1| < 0.2$, $|x_2| < 1$. The ring's modes at $(0, \pm 0.5)$ are 2 of the 8, so 25% of the ring's data already sits inside the bar. The script compares that pair with a second pair where neither expert has A-and-B: the ring without those two modes, and the bar with the band $0.4 < |x_2| < 0.6$ cut out. A width $h$ stands in for the smoothing a trained expert adds. The ring is smoothed by adding $h^2$ to each mode's variance, because [variances add](../../Mathematics/references/textbooks/linear-algebra/matrix-cookbook.pdf#page=41) when two independent Gaussians are summed. The bar's edges are blurred with the same width.

1. You need Python 3: `python3 --version` prints a version. The script imports only `math`, so no prepared environment or package is needed.
2. Make an empty folder:

   ```bash
   mkdir -p ~/playground/sandbox/product-support && cd ~/playground/sandbox/product-support
   ```

3. Save this as `support.py`. On a grid with spacing 0.005 it multiplies the two experts point by point and sums the result to get $Z$, the product's raw mass. It also measures the share of that mass within 0.1 of $(0, \pm 0.5)$, the A-and-B combination, and finds where the second pair's product is tallest:

   ```python
   # How much of a product of two experts survives when neither expert has density in A-and-B.
   import math

   S = 0.03                                   # each ring mode's width, as the notebook trains it
   MODES = [(0.5 * math.cos(2 * math.pi * k / 8), 0.5 * math.sin(2 * math.pi * k / 8)) for k in range(8)]
   KEPT = [m for m in MODES if abs(m[0]) > 0.2]            # drops the two modes at (0, +-0.5)

   def gauss1(x, m, s):
       return math.exp(-(x - m) ** 2 / (2 * s * s)) / (math.sqrt(2 * math.pi) * s)

   def ring(x, y, modes, h):                  # the ring, smoothed by width h
       s = math.sqrt(S * S + h * h)
       return sum(gauss1(x, mx, s) * gauss1(y, my, s) for mx, my in modes) / len(modes)

   def box1(x, lo, hi, h):                    # uniform on [lo, hi], smoothed by width h
       if h == 0:
           return 1.0 / (hi - lo) if lo < x < hi else 0.0
       cdf = lambda z: 0.5 * (1 + math.erf(z / (h * math.sqrt(2))))
       return (cdf(x - lo) - cdf(x - hi)) / (hi - lo)

   def bar(x, y, cut, h):                     # |x| < 0.2, |y| < 1; cut removes 0.4 < |y| < 0.6
       pieces = [(-1, -0.6), (-0.4, 0.4), (0.6, 1)] if cut else [(-1, 1)]
       total = sum(hi - lo for lo, hi in pieces)
       return box1(x, -0.2, 0.2, h) * sum(box1(y, lo, hi, h) * (hi - lo) for lo, hi in pieces) / total

   d = 0.005
   grid = [-1.2 + i * d for i in range(int(2.4 / d) + 1)]
   near = lambda x, y: math.hypot(x, abs(y) - 0.5) < 0.1   # within 0.1 of (0, 0.5) or (0, -0.5)
   for h in (0.0, 0.05, 0.1):
       out = []
       for name, modes, cut in (("full", MODES, False), ("overlap removed", KEPT, True)):
           Z = A = top = 0.0
           for x in grid:
               for y in grid:
                   p = ring(x, y, modes, h) * bar(x, y, cut, h) * d * d
                   Z += p
                   A += p if near(x, y) else 0.0
                   if p > top:
                       top, at = p, (x, y)
           out.append((name, Z, A / Z, at))
       (n1, z1, a1, _), (n2, z2, a2, at2) = out
       print(f"h = {h:.2f}  {n1}: Z = {z1:.3g}, share near (0, +-0.5) {a1:.3f}   "
             f"{n2}: Z = {z2:.3g}, share near (0, +-0.5) {a2:.3f}   Z ratio {z2 / z1:.3g}")
       print(f"          overlap removed: the product is tallest at ({at2[0]:.3f}, {at2[1]:.3f})")
   ```

4. Run it. It takes about 7 seconds:

   ```bash
   python3 support.py
   ```

   You should see:

   ```
   h = 0.00  full: Z = 0.313, share near (0, +-0.5) 0.996   overlap removed: Z = 1.6e-07, share near (0, +-0.5) 0.000   Z ratio 5.12e-07
             overlap removed: the product is tallest at (-0.200, 0.355)
   h = 0.05  full: Z = 0.324, share near (0, +-0.5) 0.741   overlap removed: Z = 0.0173, share near (0, +-0.5) 0.000   Z ratio 0.0535
             overlap removed: the product is tallest at (0.250, -0.340)
   h = 0.10  full: Z = 0.356, share near (0, +-0.5) 0.301   overlap removed: Z = 0.11, share near (0, +-0.5) 0.005   Z ratio 0.31
             overlap removed: the product is tallest at (0.240, -0.315)
   ```

   ![The run's six lines, with the overlap mass, the share near the missing combination and the tallest point marked 1 to 8|900](assets/support-the-product-without-overlap.png)

5. Clean up, and check the folder is gone:

   ```bash
   cd ~ && rm -r ~/playground/sandbox/product-support
   ls ~/playground/sandbox/product-support; echo $?
   ```

   You should see `No such file or directory` and `2`.

**Reading the support output.**

| # | Field | Value | How to read it | Backing |
|---|---|---|---|---|
| 1 | full, $Z$ at $h = 0$ | `0.313` | the product's raw mass: the two ring modes inside the bar carry all of it | derived below |
| 2 | full, share near $(0, \pm 0.5)$ | `0.996` | almost all of the product sits on those two modes, the A-and-B combination | derived below |
| 3 | overlap removed, $Z$ at $h = 0$ | `1.6e-07` | with neither expert holding A-and-B, the product has almost no mass anywhere: only the Gaussian tails of the 45-degree modes reach the bar's edge | derived below |
| 4 | overlap removed, share near $(0, \pm 0.5)$ | `0.000` | none of what is left is at the missing combination | shown |
| 5 | overlap removed, tallest point | `(-0.200, 0.355)` | after dividing by $Z$ the product is a full distribution, centred on the bar's edge beside a 45-degree mode, where neither expert is at its best: the empty intersection of [[#The product as an intersection]] | shown |
| 6 | overlap removed, $Z$ at $h = 0.1$ | `0.11` | smoothing gives the product mass back | shown |
| 7 | overlap removed, share near $(0, \pm 0.5)$ at $h = 0.1$ | `0.005` | the returned mass still lands beside the 45-degree modes, at $(0.240, -0.315)$, and not at the missing combination | shown |
| 8 | $Z$ ratio at $h = 0.1$ | `0.31` | 31% of the full pair's raw mass, which is why a sampler on smoothed experts still returns samples. They sit at the bar's edges | shown |

**How the support rule works.**

1. **The full pair.** At $h = 0$ only the two modes at $(0, \pm 0.5)$ lie inside the bar. Each carries weight $1/8$ and lies wholly where the bar's height is $1/(0.4 \times 2) = 1.25$, so $Z = 2 \times \tfrac18 \times 1.25 = 0.3125$. A 2D Gaussian of width 0.03 keeps $1 - e^{-(0.1/0.03)^2/2} = 1 - e^{-5.556} = 0.9961$ of its mass within 0.1 of its centre. *Derived.* These are fields 1 and 2.
2. **The pair with the overlap removed.** The nearest kept modes sit at $x_1 = \pm 0.5 \cos 45^\circ = \pm 0.3536$, which is $0.1536 = 5.12$ widths outside the bar's edge at 0.2. The share of such a Gaussian that crosses the edge is $\Phi(-5.12) = 1.54 \times 10^{-7}$. Four such modes, each of weight $1/6$, with 0.939 of each inside the kept band $|x_2| < 0.4$, under a bar of height $1/(0.4 \times 1.6)$, give $Z = 4 \times \tfrac16 \times 1.54 \times 10^{-7} \times 0.939 / 0.64 = 1.51 \times 10^{-7}$. *Derived.* The run's `1.6e-07` in field 3 is 6% higher because the grid's spacing of 0.005 is coarse against a tail this steep.
3. **What the rule leaves to smoothing.** The product is zero wherever either factor is zero, so all of field 6's mass comes from the smoothing tails, and those tails are thickest where the two supports are nearest each other. That is the bar's edge beside the 45-degree modes, and the missing combination is not there. *Shown* in fields 5 to 7.

![The product's support as the intersection of supports, the ring-times-bar with and without the overlap|800](assets/support-the-concept.webp)

*The product's support as the intersection of supports, the ring-times-bar with and without the overlap.*

**Three ways round it, strongest first.**

- **Support kept from pretraining.** Fine-tune both experts from one model pretrained on every combination. For chest X-rays that is all of NIH's films, which include pneumothorax without a drain. The product then reaches A-and-B through the pretrained density that each expert keeps. The cost is that the answer depends on how long each expert is fine-tuned, since fine-tuning may erase that support. *Stated.* The check in 2D: pretrain on all four quadrant cells, fine-tune copies at 0% overlap for 0 to $N$ steps, and plot the product's mass in A-and-B against steps.
- **An expert whose density factorises over image parts.** This is projective composition, from Bradley et al. 2025 ([arXiv 2502.04549](https://arxiv.org/abs/2502.04549)), set out above under [[#Composing models with a background]]. *Cited.* A pneumothorax expert that learned the lung and the chest wall as separate parts gives density to "pneumothorax lung, chest wall without a drain", because each part was seen somewhere. *Stated:* applying this to X-rays is the walk's reading. It cannot be tested on 2D MLP experts, which add nothing beyond their smoothed data (the 0.04 nats above). It needs a small image testbed with A and B in separate patches.
- **Fallback: use the 2D curve to calibrate samplers.** The 2D curve of A-and-B mass against overlap is fixed by the product rule before any training, so use it only as a known answer for checking samplers. This is the cheapest, and it gives up the medical question.

**Why this matters.** The repaired claim is that **a product reaches A-and-B only as far as each expert's density does, and generates combinations missing from training only when something gives each expert density there.** A plan that hopes composition will make the missing X-ray films has to name that something (pretrained support, or an expert that factorises over parts) before it runs.

### The training set taught in, applied in

**Taught in:**

- the `drip-idea` walk of the overlap dial in the reduce-reuse-recycle research repository, claim 1 ("an expert trained on A data learns the concept A"), round 2, the `example` and `break` controls (`artifacts/ideas/poe-overlap-dial/IDEA_MAP.md`)
- the `drip-idea` walk of when a product reaches A and B, in the same repository, claim 2 ("a product can put samples in A∩B that neither training set contains"), the `back 2` control (`artifacts/ideas/when-poe-reaches-a-and-b/IDEA_MAP.md`), for [[#When neither training set holds A and B]]

**Applied in:**

- the overlap-dial idea, which turns the share of A-and-B points in each expert's training set from 0% to 100% and counts how often the product lands in A-and-B. The repair says that dial moves the experts' mass and the labels do not, unless a conditioning rule or a classifier reads them.
- the idea of when a product reaches A and B, which asks whether two diffusion experts can generate chest X-rays with a pneumothorax and no drain when neither training set holds one. The support rule marks that claim wrong as stated: in 2D both of the learner's questions (does a product make A-and-B from hidden overlap, does stripping the overlap stop it) come out yes before training. The open choice is between pretrained support, an expert that factorises over parts, and keeping the 2D curve only for calibrating samplers.

> [!note]- How this was checked
> Every output above was run by the writer in an empty folder, `~/playground/sandbox/gaussian-clouds`, on the PC: Ubuntu under WSL2, through the prepared environment `~/.vault-sandbox/bin/python` (Python 3.11.13, NumPy 2.4.6, Matplotlib 3.11.2), on 2026-10-04. The folder was removed afterwards and the clean-up check returned 2.
>
> `toy.py` is the learner's own file from the walk's playground. `noised.py` is the learner's file with its print line rewritten to show the closed form beside each level, which the walk asked for. Its measured values matched the walk's answer key, `checks/noised.out`, to the digits shown. The four $\alpha$ values and $\bar\alpha = 0.4788$ in step 5 are plan 09's, line 143.
>
> The terminal picture was rendered from the captured text by a script in DejaVu Sans Mono, never drawn. The composition picture is `picture.py`'s own saved figure, checked by eye: the green dots sit at $(-2, 2)$ and $(-1.5, 0)$ and the purple crosses at $(-1.6, 1.6)$ and $(-1.2, 0)$.
>
> The paper's Figures 1, 2, 3, 4, 5, 7, 8 and 12 are the authors' own image files, copied byte for byte from the arXiv source package (`paper/source/figures/` in the journey's staged sources) into `references/`, and each was opened before filing. Each caption is the LaTeX caption from `src/intro.tex` (Figures 1, 2, 3), `src/projective_comp.tex` (4, 5), `src/practical.tex` (7, 8) and `src/appendix_notes.tex` (12), with LaTeX markup removed and every cross-reference written as the PDF prints it. The figure numbers are the ones printed in `2502.04549.pdf`, version 3. The paper is under arXiv's non-exclusive distribution licence, which does not grant a reuse licence; the copies are here for study, with citation on every embed. The lines under each caption tying a figure to the toy are the writer's, and each is marked shown, derived or cited.
>
> The runs in [[#The order of multiplying and noising]] were made by the writer in a second empty folder, `~/playground/sandbox/two-orders`, on the same PC and environment (Python 3.11.13, NumPy 2.4.6, Matplotlib 3.11.2), on 2026-10-09; the folder was removed afterwards and the clean-up check returned 2. The six scripts are shortened from the sampler correctors journey's answer keys in `sources/reduce-reuse-recycle/checks/`: `two_routes.py`, `mixture_score.py`, `reverse_diffusion.py` and `annealed_mcmc.py`. Every printed number matched those keys' outputs to the digits shown: variances 0.653846 and 0.409091, mixture difference 2.8e-16, reverse process mean -0.1567 and variance 0.2102, annealed Langevin mean -0.2273 and variance 0.3124, all with seed 0. The keys' exactly-followed figures, 0.209963 and 0.313044, are quoted from their `.out` files. The walk described the pair as two unit-variance experts; the numbers it quoted (0.654, 0.409, 0.308) belong to variances 0.5 and 0.8, which is the pair used here. With unit variances the product would have variance 0.5.
>
> The five output pictures were rendered from the captured text by a script in DejaVu Sans Mono, never drawn, and each was opened before filing. The paper's Figure 2 is the authors' `fig/comp_fig4.pdf` from the arXiv source package, converted to PNG at 150 dpi with `pdftoppm` and opened before filing; its caption is the LaTeX caption from `text/method.tex` lines 36 to 43 with markup removed. Quotations from the paper are from its source: `text/abstract.tex` line 2, `text/method.tex` lines 31 to 131, `text/appendix.tex` line 232. The figure numbers and equation numbers 11 and 12 are as the journey's read-ahead reads them from `2302.11552.pdf`.
>
> The re-teach in the walk described expert 2 in shared as an object in the left half only. It also narrows the right half, from variance 4 to 1, and the table and derivation here carry that.
>
> The runs in [[#The energy parameterisation]] were made by the writer in a third empty folder, `~/playground/sandbox/energy-parameterisation`, on the same PC and environment (Python 3.11.13, NumPy 2.4.6, Matplotlib 3.11.2), on 2026-10-13; the folder was removed afterwards and the clean-up check returned 2. The scripts are shortened from the journey's answer keys `checks/mala_step.py`, `checks/mixture_score.py` and `checks/energy_parameterisations.py`, and every shared number matched those keys' outputs to the digits shown: MALA variance 0.3071 and share accepted 0.9582 with seed 0; the hand proposal 1.161107, 1.719645, -1.440203 and 0.279442; the mixture shares 0.465058 and 0.534942 and slope -0.261437. The unadjusted run at step 0.1, mean -0.2323 and variance 0.3671, matches plan 36's reference reading. The run at step 0.01 and the normalisers-dropped mixture line are new to this note and were checked against the derivations in [[#How the energy works]]. The six output pictures were rendered from the captured text by a script in DejaVu Sans Mono, never drawn, and each was opened before filing. Quotations from Du et al. are as the journey's read-ahead quotes them from the paper's source: `text/related_work.tex` lines 57 to 65 and 89 to 100 (sections 2.2 and 2.3), `text/method.tex` lines 140 to 156 (section 4.2).
>
> The run in [[#The product as an intersection]] was made by the writer in a fourth empty folder, `~/playground/sandbox/product-intersection`, on the same PC and environment, on 2026-10-13; the folder was removed afterwards and the clean-up check returned 2. Its near-pair numbers match the walk's answer key `checks/step6_product.py` and `checks/step6_product.out` in the journey's `sources/reduce-reuse-recycle/`: peak at -0.23, expert a at 0.311840 of 0.564190 and expert b at 0.173266 of 0.446031. The far pair is new to this note and was checked against the derivation in the same subsection. `intersection.png` is the script's own saved figure, opened before filing; the terminal picture was rendered from the captured text by a script in DejaVu Sans Mono, never drawn, and opened before filing. The quotations are from `text/method.tex` lines 10 to 19 and `text/appendix.tex` line 306 of the arXiv source package.
>
> The runs in [[#Product, mixture and negation]] were made by the writer in a fifth empty folder, `~/playground/sandbox/three-operators`, on the same PC and environment (Python 3.11.13, NumPy 2.4.6), on 2026-10-13; the folder was removed afterwards and the clean-up check returned 2. The scripts are shortened from the walk's answer keys `checks/step6_product.py`, `guidance_on_the_object.py`, `mixture_score.py` and `negation.py` in the journey's `sources/reduce-reuse-recycle/`. All four keys were re-run in the same folder and their output matched the saved `.out` files byte for byte, and every number the three scripts print matched them to the digits shown. The three output pictures were rendered from the captured text by a script in DejaVu Sans Mono, never drawn, and each was opened before filing. The Figure 2 redraw numbers (96.8%, 55.6%, 69.0%, 87.0%, 91.5%, 0.2100, 0.3076) are quoted from `checks/ring_times_bar.out`, `ring_times_bar_more_steps.out` and `fig2_on_the_object.out`, not re-run here. The paper's Figure 6 is the authors' `fig/horse5.pdf` from the arXiv source package, converted to PNG at 110 dpi with `pdftoppm` and opened before filing; its caption is the LaTeX caption in `figText/text2im.tex` lines 1 to 7 with markup removed. The notebook lines were opened in the playground's reference copy of the authors' repository, `notebooks/simple_distributions.ipynb`, counting cells from 0: the factor 3.5 is on line 17 of cell 7, inside the method the read-ahead cites as lines 13 to 19, and `1.3 * unorm_1 - 0.3 * unorm_2` is line 15 of cell 8. Quotations from section 3 are from `text/method.tex` lines 10 to 54, read in the staged source.
>
> [[#Kinds of composition]] and [[#What an expert learns from its training set]] were written on 2026-10-14 on the cluster (mscluster, Linux), from one turn of the overlap-dial `drip-idea` walk. Nothing in them was run: the cluster has no `~/.vault-sandbox`, so `labels.py` and its expected output are worked by hand in [[#How the expert's training set works]], and the section stays in the unfinished box until a machine with the environment runs it. The identity for the interaction term is derived in the note; the walk's own draft, `composition-terms.md` in the research repository, writes it without the constant $\log \frac{p(A)\,p(B)}{p(A, B)}$, which changes the density and not the score. The textbook pages were opened before linking: Bayes' theorem on page 105 of the probability book (Theorem 2.7), conditional independence on page 201 of Mathematics for Machine Learning (Definition 6.11), log rules on page 110 of the algebra handbook. The arXiv abstracts of Liu et al., Chefer et al., Bar-Tal et al. and Geirhos et al. were fetched on 2026-10-14, and the quoted phrases ("catastrophic neglect", attribute binding, the definition of shortcuts) are from them; Hinton 2002's DOI resolved to Neural Computation 14(8), pages 1771 to 1800. Ho et al.'s equation (14) and section 3.2 are cited from the paper as already listed, not re-read in this session. No old LibreOffice note was read: `/mnt/c/Users/molef/LibreOffice/Learning/` does not exist on the cluster.
>
> The run in [[#When neither training set holds A and B]] was made by the writer on 2026-10-15 on the cluster (mscluster, Linux) in an empty folder, `~/playground/sandbox/product-support`, with the system `python3` (Python 3.14.4), standard library only. It took 7.2 seconds. The folder was removed afterwards and the clean-up check returned 2. The script and the output on the page were diffed against the files that ran, and both are identical. The ring, the bar and the mode width were read in the research repository's `notebooks/simple_distributions.ipynb`, counting cells from 0: `toy_gmm` in cell 14 (8 modes, radius 0.5), `bar` in cell 17 (uniform on $|x_1| < 0.2$, $|x_2| < 1$), and `toy_gmm(std=.03)` on line 49 of cell 32. The output picture was rendered from the captured text by a script in DejaVu Sans Mono, never drawn, and opened before filing. The 0.04 nats is quoted from the overlap-dial walk's run record, not re-run here. The variances-add link is the shelf index's own row for page 41 of the matrix cookbook. $\Phi$, the standard normal CDF, and the support of a density carry no textbook link, because this machine has no PDF reader to open a page and confirm it.
>
> References, each answering 200 on 2026-10-04: [Ho et al. on arXiv](https://arxiv.org/abs/2006.11239), [Bradley et al. on arXiv](https://arxiv.org/abs/2502.04549), [Du et al. on arXiv](https://arxiv.org/abs/2302.11552) (checked 2026-10-09), [Product of experts](https://en.wikipedia.org/wiki/Product_of_experts) on Wikipedia, CC BY-SA 4.0. Definition 5.1 and Definition 5.2 were read in the walk's read-ahead, `read-ahead/05-simple-construction.md`, which quotes the paper's source `src/composition.tex` lines 33 to 46. The sketchpad link is the learner's own private artifact and was not fetched. No tldr-pages entry covers this.
