---
aliases: [powers of Gaussians, power of a Gaussian, Gaussian raised to a power, power combination of Gaussians, weighted product of Gaussians, tempered Gaussian, positive-precision condition, positive precision condition, negation of Gaussians, q_a / q_b^alpha, guidance scale on Gaussians, powered Gaussian, one Gaussian to a power, sigma^2 / beta, variance over beta, component pair weights, pairwise component weights, w_ij, "N(mu_i; nu_j, S_i + L_j)"]
sources:
  - "Du, Durkan, Strudel, Tenenbaum, Dieleman, Fergus, Sohl-Dickstein, Doucet, Grathwohl, Reduce, Reuse, Recycle: Compositional Generation with Energy-Based Diffusion Models and MCMC, ICML 2023: https://arxiv.org/abs/2302.11552"
---

# Powers Of Gaussians

Up: [[Multivariate Normal Distribution]] · ⬅️ [[The Area A Product Loses]]

Mathematics, Statistics, Distributions, Multivariate Normal Distribution. Needs: [[Products And Quotients Of Diagonal Gaussians]].

> [!question] Test yourself
> [The diagonal Gaussian quiz](https://claude.ai/artifact/Vmd1FBg7oWwZq1onu9Jofa) covers the [[Multivariate Normal Distribution]] folder. This note's sections are not in it yet.

> [!warning] Unfinished
> - Prompt 10, the concept picture, is waiting to be drawn, in the vault's `.prompts/Multivariate Normal Distribution.md`.

**Raising a Gaussian density to a power $w$ multiplies its precision by $w$, so $q_a^{w_a} q_b^{w_b}$ is a Gaussian with precision $P = w_a / v_a + w_b / v_b$ and mean $(w_a m_a / v_a + w_b m_b / v_b) / P$, provided $P > 0$.** A product is $w_a = w_b = 1$, guidance at scale $\lambda$ is $w_b = \lambda$, and Du et al.'s negation $q_a / q_b^\alpha$ is $w_b = -\alpha$. A negative power subtracts precision, so the result stays a density only while the expert being divided out is broad enough: $\alpha / v_b < 1 / v_a$. *Derived* below.

**When to reach for it.** When a composition scales a score before adding it: a guidance weight, a negative prompt, a background divided out. The precision tells you, before sampling, whether the scaled combination is a density at all, and how wide it is.

**Try it on one pair.**

1. What you need: the prepared environment, as in step 1 of [[Sampling A Diagonal Gaussian#Try sampling yourself]].
2. Make an empty folder and work in it:

   ```bash
   mkdir -p ~/playground/sandbox/gaussian-powers && cd ~/playground/sandbox/gaussian-powers
   ```

3. Save this as `powers.py`. For six pairs of powers it computes the closed form, and separately weighs a grid of 1,601 points by $q_a^{w_a} q_b^{w_b}$ and measures the mean and variance of the weights:

   ```python
   # q_a^w_a * q_b^w_b for two Gaussians: precisions scale by the powers, then add.
   import numpy as np

   (ma, va), (mb, vb) = (-1.0, 0.5), (1.0, 0.8)      # expert a and expert b: mean, variance
   x = np.linspace(-8, 8, 1601)
   dx = x[1] - x[0]


   def log_gauss(z, m, v):
       return -(z - m) ** 2 / (2 * v) - 0.5 * np.log(2 * np.pi * v)


   print("  w_a   w_b   precision   mean       variance   grid mean  grid variance")
   for wa, wb in [(1, 1), (1, 2), (1, -0.5), (1.3, -0.3), (-0.5, 1), (-1, 1)]:
       P = wa / va + wb / vb                             # each precision times its power, added
       logq = wa * log_gauss(x, ma, va) + wb * log_gauss(x, mb, vb)
       if P <= 0:
           print(f"{wa:5.1f} {wb:5.1f}   {P:+.6f}   not a density: log height at x = -8, 0, 8 is "
                 f"{logq[0]:.1f}, {logq[800]:.1f}, {logq[-1]:.1f}")
           continue
       m, v = (wa * ma / va + wb * mb / vb) / P, 1 / P
       w = np.exp(logq - logq.max())
       w /= w.sum()
       gm = (w * x).sum()
       print(f"{wa:5.1f} {wb:5.1f}   {P:+.6f}   {m:+.6f}  {v:.6f}   {gm:+.6f}  {(w * (x - gm) ** 2).sum():.6f}")
   ```

4. Run it:

   ```bash
   ~/.vault-sandbox/bin/python powers.py
   ```

   You should see:

   ![Six pairs of powers: precision 3.25 for the product, mean 0.111 and variance 0.222 for b squared, precision 1.375 for a over the root of b, variance 0.449 for the notebook's weights, a grid that misreads a centre at 9 as 6.72, and precision -0.75 with the log height climbing to 50.1|900](assets/powers-of-two-gaussians.png)

5. Clean up, and prove it:

   ```bash
   cd ~ && rm -r ~/playground/sandbox/gaussian-powers
   ls ~/playground/sandbox/gaussian-powers; echo $?
   ```

   You should see `No such file or directory`, then `2`.

**Reading the output.**

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | product, precision | `+3.250000` | $2 + 1.25$: the plain product of [[Products And Quotients Of Diagonal Gaussians#How the product works]] | derived below |
| 2 | $w_b = 2$ | mean `+0.111111`, variance `0.222222` | guidance at scale 2: pulled past the product toward b, and narrower | derived below |
| 3 | $w_b = -0.5$, precision | `+1.375000` | negation with $\alpha = 0.5$: $2 - 0.625$, still positive | derived below |
| 4 | $1.3$ and $-0.3$ | mean `-1.337079`, variance `0.449438` | the powers in Du et al.'s notebook, cell 8, line 15; no single $\alpha$ gives them | derived below |
| 5 | $w_a = -0.5$, grid | `+6.721498`, `1.075543` | the closed form says mean 9 and variance 4, past the axis's end at 8, so the grid cuts the bell off and misreads it | shown |
| 6 | $w_a = -1$, precision | `-0.750000` | b over all of a: negative, so no density | derived below |
| 7 | its log height at 8 | `50.1` | the log climbs without limit toward the edge: no constant can give it area 1 | shown |

Every other row's grid columns agree with the closed form to six places.

**How powers work.** Raising to a power multiplies the log by it ([exponent rules](../../../references/textbooks/algebra/algebra-handbook.pdf#page=109): $(e^{u})^w = e^{wu}$):

$$
\begin{aligned}
\log\big(q_a^{w_a} q_b^{w_b}\big) &= -\frac{w_a (x - m_a)^2}{2 v_a} - \frac{w_b (x - m_b)^2}{2 v_b} + \text{const} \\
&= -\tfrac12 \left(\frac{w_a}{v_a} + \frac{w_b}{v_b}\right) x^2 + \left(\frac{w_a m_a}{v_a} + \frac{w_b m_b}{v_b}\right) x + \text{const}
\end{aligned}
$$

This is the shape of [[Products And Quotients Of Diagonal Gaussians#How the product works]] with each $1/v$ replaced by $w/v$, so [completing the square](../../../references/textbooks/algebra/algebra-handbook.pdf#page=74) gives precision $P = w_a/v_a + w_b/v_b$ and mean $B/P$, and the same rule that $P$ must be above 0. On the pair:

$$
\begin{aligned}
w_b = 2:&\quad P = 2 + 2.5 = 4.5, & B &= -2 + 2.5 = 0.5, & \text{mean } 0.111111,\ \text{var } 0.222222 \\
w_b = -0.5:&\quad P = 2 - 0.625 = 1.375, & B &= -2 - 0.625 = -2.625, & \text{mean } -1.909091,\ \text{var } 0.727273 \\
1.3,\ -0.3:&\quad P = 2.6 - 0.375 = 2.225, & B &= -2.6 - 0.375 = -2.975, & \text{mean } -1.337079,\ \text{var } 0.449438 \\
w_a = -0.5:&\quad P = -1 + 1.25 = 0.25, & B &= 1 + 1.25 = 2.25, & \text{mean } 9,\ \text{var } 4 \\
w_a = -1:&\quad P = -2 + 1.25 = -0.75
\end{aligned}
$$

*Derived.* The score of the result is $w_a s_a + w_b s_b$, each expert's score scaled by its power, which is why a diffusion sampler can apply any of these with scores alone. Which composition each power stands for is worked in [[Product, Mixture And Negation]].

**One Gaussian to a power.** With a single expert the rule reads: $\mathcal{N}(\mu, \sigma^2)$ raised to $\beta > 0$ and normalised is $\mathcal{N}(\mu, \sigma^2 / \beta)$, the same mean with the precision multiplied by $\beta$. Moving $\beta$ into the denominator of the exponent shows it in one line:

$$
\left(e^{-\frac{(x - \mu)^2}{2\sigma^2}}\right)^\beta = e^{-\frac{\beta (x - \mu)^2}{2\sigma^2}} = e^{-\frac{(x - \mu)^2}{2\,(\sigma^2 / \beta)}}
$$

$\mathcal{N}(3, 4)$ at $\beta = 2$ is $\mathcal{N}(3, 2)$, and expert a, $\mathcal{N}(-1, 0.5)$, at $\beta = 0.25$ is $\mathcal{N}(-1, 2)$. The score gives an independent check, because the score of a powered density is $\beta$ times the old score ([[The Tempered Density And Its Score]]): at $x = 5$, $2 \times \left(-(5 - 3)/4\right) = -1.0$ and the score of $\mathcal{N}(3, 2)$ is $-(5 - 3)/2 = -1.0$; at $x = 0$, $0.25 \times \left(-(0 + 1)/0.5\right) = -0.5$ and the score of $\mathcal{N}(-1, 2)$ is $-(0 + 1)/2 = -0.5$. *Derived.* At $\beta = 0$ the variance $\sigma^2 / \beta$ has no value and the powered height is 1 everywhere, which has no normaliser; that section works it.

*🖼️ Diagram wanted: the form, each expert's precision bar scaled by its power and added, with the bell it gives in four rows from the product to a total below zero. Prompt 10 in the vault's `.prompts/Multivariate Normal Distribution.md`.*

**Why this matters.** A negative prompt or a divided-out background can quietly produce something that is not a distribution. The check costs one subtraction: the kept expert's precision has to exceed the divided one's precision times its power. A pushed-away expert narrower than that makes the sampler chase a log height that grows toward the edges, as row 6 does.

**Taught in:** the `drip-read` walk of Du et al., Reduce, Reuse, Recycle, section 3, chunks 37, 40 and 41 (guidance as a product, equation 10 and its positive-precision condition, the notebook's weights), from the walk's answer keys `checks/negation.out` and `checks/guidance_on_the_object.out`. One Gaussian to a power: piece 2 of the `drip --math` walk of the sampler correctors for composition journey's plan 24, `plans/24-what-is-annealed.md`, lines 129 to 150, in `drips/24-what-is-annealed/`. The walk's paper note, `deep-learning/diffusion-models/02-sampler-correctors-for-composition/papers/reduce-reuse-recycle/reduce-reuse-recycle.md` in this vault, is not written yet; link it here when it is.

**Applied in:** nothing yet.

> [!note]- How this was checked
> Every output in this note was run by the writer in an empty folder, `~/playground/sandbox/gaussian-powers`, on the PC: Ubuntu under WSL2, through the prepared environment `~/.vault-sandbox/bin/python` (Python 3.11.13, NumPy 2.4.6), on 2026-10-13. The folder was removed afterwards and the clean-up check returned 2. Rows 1 to 4 and 6 match the walk's answer keys `checks/negation.out` and `checks/guidance_on_the_object.out` in the journey's `sources/reduce-reuse-recycle/`, both re-run in a sandbox the same day with output identical to the saved files; row 5's grid reading is new to this note and is explained by the closed form beside it. The terminal picture was rendered from the captured text by a script in DejaVu Sans Mono and opened before filing.
>
> The paragraph "One Gaussian to a power" in this note was added on 2026-10-17 on the cluster (mscluster, Linux) from piece 2 of the plan 24 walk. It runs nothing; its four scores were computed by the writer with `awk` and match the walk's numbers.
