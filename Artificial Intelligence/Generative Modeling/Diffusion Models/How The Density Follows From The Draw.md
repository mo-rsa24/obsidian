---
aliases: [how the density follows from the draw, deriving the density of the one jump, the one jump's density derived, the exponent worked on the toy, the broken centre worked on the toy]
sources:
  - "Chan, Introduction to Probability for Data Science, Michigan Publishing 2021, Definition 5.22 (PDF p. 306), the diagonal case as a product of 1D Gaussians (PDF p. 307) and Theorem 5.19 (PDF p. 315): ../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=306"
  - "Ho, Jain, Abbeel, Denoising Diffusion Probabilistic Models, NeurIPS 2020, equation (4), the density derived here: https://arxiv.org/abs/2006.11239"
standard: vault-note v2
---

# How The Density Follows From The Draw

Up: [[Diffusion Models]] · ⬅️ [[The Density Of The One Jump]] · [[Running The Density Of The One Jump]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[The Density Of The One Jump]] for the density this note derives, [[From Many Steps To One Jump]] for the jump, and [[The Scaling Rule For Variance#Scaling a draw scales its variance by the square|the scaling rule for variance]].

**The density of the one jump follows from the one-shot draw in three moves.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. It has no questions on this note yet.

> [!warning]- Unfinished
> - The diffusion models quiz has no questions on this note yet.

Stated claims: 0.

**The three moves.** All the noise is one draw; holding the clean point fixed gives the centre, the spread and the Gaussian shape; and Chan's density, written out in 2D, is $q(x_t \mid x_0)$. The last section works the result on the toy at $t = 50$ and $t = 25$, with the centre's square root dropped beside it.

**Where the numbers come from.** The toy numbers are the table in [[The Density Of The One Jump#The one-shot draw and its density]], and every printed number is an output of [[Running The Density Of The One Jump]]. The result itself is stated in [[The Density Of The One Jump#The exponent at the drawn point]].

**Colours in this note.** <span style="color:#1565c0">**Blue is the clean point $x_0$ and the centre $\sqrt{\bar\alpha_t}\,x_0$**</span>, <span style="color:#00838f">**teal is the noisy point $x_t$**</span>, <span style="color:#6a1b9a">**purple is the standard normal draw $\varepsilon$**</span>, <span style="color:#2e7d32">**green is the kept signal share $\bar\alpha_t$**</span>, <span style="color:#ef6c00">**orange is the noise scale $\sqrt{1 - \bar\alpha_t}$, its variance $\sigma^2$ and the displacement $d$**</span>, <span style="color:#3949ab">**indigo is the front factor**</span>, and <span style="color:#757575">**grey is the centre without its square root**</span>, as in [[The Density Of The One Jump]].

## Table of contents

- [[#The noise is one draw]]
- [[#The centre, the spread and the shape]]
- [[#The 2D Gaussian written out]]
- [[#The exponent on the toy]]

## The noise is one draw

Navigation: 📋 [[#Table of contents|TOC]] | [[#The centre, the spread and the shape]] ➡️

**The noise is one draw.** [[From Many Steps To One Jump#How two steps become every step|The induction]] left $x_t = \sqrt{\bar\alpha_t}\,x_0 + n_t$, with $n_t$ a sum of independent Gaussian pieces of total variance $1 - \bar\alpha_t$. [[Sums Of Independent Gaussians#How the rule works|A sum of independent Gaussians is a Gaussian]], so $n_t$ is one draw of mean 0 and variance $1 - \bar\alpha_t$ per coordinate.

**One draw times its spread.** [[The Scaling Rule For Variance#Scaling a draw scales its variance by the square|The scaling rule]] writes such a draw as $\sqrt{1 - \bar\alpha_t}\,\varepsilon$ with one standard normal $\varepsilon$:

$$
x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon, \qquad \varepsilon \sim \mathcal{N}(0, I)
$$

$$
\underbrace{\textcolor{#00838f}{x_t}}_{\text{noisy point}}
=
\underbrace{\sqrt{\textcolor{#2e7d32}{\bar\alpha_t}}\,\textcolor{#1565c0}{x_0}}_{\text{kept clean signal}}
+
\underbrace{\textcolor{#ef6c00}{\sqrt{1 - \bar\alpha_t}}\,\textcolor{#6a1b9a}{\varepsilon}}_{\text{all the noise, one draw}},
\qquad
\underbrace{\textcolor{#6a1b9a}{\varepsilon} \sim \mathcal{N}(0, I)}_{\text{one standard normal per coordinate}}
$$

**What the equation says.** The noisy point is the clean point scaled once plus one scaled standard normal draw. At $t = 50$ it is $0.6916\,x_0 + 0.7223\,\varepsilon = (0, 0.3458) + (0.2167, -0.8668) = (0.2167, -0.5210)$.

**Why the square root on the noise is there.** The noise must have variance $1 - \bar\alpha_t$, and scaling a draw scales its variance by the square. At $t = 50$ the multiplier $\sqrt{0.5217} = 0.7223$ gives variance 0.5217; the multiplier 0.5217 itself would give $0.5217^2 = 0.2722$.

## The centre, the spread and the shape

Navigation: ⬅️ [[#The noise is one draw]] | 📋 [[#Table of contents|TOC]] | [[#The 2D Gaussian written out]] ➡️

Textbook: [Chan, Theorem 5.19, a scaled and shifted standard normal is Gaussian, PDF p. 315](../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=315)

**The centre and the spread.** Hold $x_0$ fixed. Then $\sqrt{\bar\alpha_t}\,x_0$ is a constant, and [[Scaling And Shifting A Random Variable#What scaling and shifting do|adding a constant]] moves the centre without changing the spread; each coordinate of $\varepsilon$ is its own independent draw, so the covariance is $(1 - \bar\alpha_t)$ times the identity:

$$
\begin{aligned}
\mathbb{E}[x_t] &= \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\mathbb{E}[\varepsilon] = \sqrt{\bar\alpha_t}\,x_0 \\
\operatorname{Cov}[x_t] &= \big(\sqrt{1 - \bar\alpha_t}\big)^2 \operatorname{Cov}[\varepsilon] = (1 - \bar\alpha_t)\,I
\end{aligned}
$$

$$
\begin{aligned}
\mathbb E[\textcolor{#00838f}{x_t}]
&=\sqrt{\textcolor{#2e7d32}{\bar\alpha_t}}\,\textcolor{#1565c0}{x_0}+\textcolor{#ef6c00}{\sqrt{1-\bar\alpha_t}}\,\underbrace{\mathbb E[\textcolor{#6a1b9a}{\varepsilon}]}_{0}
=\underbrace{\sqrt{\textcolor{#2e7d32}{\bar\alpha_t}}\,\textcolor{#1565c0}{x_0}}_{\mu} \\
\operatorname{Cov}[\textcolor{#00838f}{x_t}]
&=\underbrace{\big(\textcolor{#ef6c00}{\sqrt{1-\bar\alpha_t}}\big)^2}_{\text{the multiplier, squared}}\,\underbrace{\operatorname{Cov}[\textcolor{#6a1b9a}{\varepsilon}]}_{I}
=\underbrace{\textcolor{#ef6c00}{(1-\bar\alpha_t)}}_{\sigma^2}\,I
\end{aligned}
$$

**What the equation says.** The mean of the noisy point is the shrunken clean point, because the noise averages to zero. The covariance is the noise multiplier squared on each axis, with no cross term.

**The shape.** A standard normal draw scaled and shifted is still Gaussian, [Chan's Theorem 5.19](../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=315), with $\Sigma^{1/2} = \sqrt{1 - \bar\alpha_t}\,I$ here. So $q(x_t \mid x_0) = \mathcal{N}(x_t;\ \sqrt{\bar\alpha_t}\,x_0,\ (1 - \bar\alpha_t) I)$, the formula of [[The Density Of The One Jump#All the words together: the formula]].

## The 2D Gaussian written out

Navigation: ⬅️ [[#The centre, the spread and the shape]] | 📋 [[#Table of contents|TOC]] | [[#The exponent on the toy]] ➡️

Textbook: [Chan, Introduction to Probability for Data Science, Definition 5.22, the d-dimensional Gaussian density, PDF p. 306](../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=306)

**Write out the 2D Gaussian density.** With $\Sigma = \sigma^2 I$ in $d = 2$ dimensions, $\det\Sigma = \sigma^4$ and $\Sigma^{-1} = I/\sigma^2$, so [Chan's general formula](../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=306) becomes

$$
\begin{aligned}
\mathcal{N}(x; \mu, \Sigma) &= \frac{1}{(2\pi)^{d/2} \det(\Sigma)^{1/2}} \exp\!\Big(-\tfrac{1}{2}(x - \mu)^\top \Sigma^{-1} (x - \mu)\Big) \\
\mathcal{N}(x; \mu, \sigma^2 I) &= \frac{1}{2\pi\sigma^2} \exp\!\Big(-\frac{|x - \mu|^2}{2\sigma^2}\Big) \\
q(x_t \mid x_0) &= \frac{1}{2\pi(1 - \bar\alpha_t)} \exp\!\Big(-\frac{|x_t - \sqrt{\bar\alpha_t}\,x_0|^2}{2(1 - \bar\alpha_t)}\Big)
\end{aligned}
$$

$$
\begin{aligned}
\mathcal{N}(x; \mu, \sigma^2 I)
&= \underbrace{\frac{1}{\underbrace{(2\pi)^{2/2}}_{2\pi}\,\underbrace{(\sigma^4)^{1/2}}_{\sigma^2}}}_{\text{total volume } = 1}
\exp\!\Big(-\tfrac12 \underbrace{(x - \mu)^\top \tfrac{I}{\sigma^2} (x - \mu)}_{|x - \mu|^2 / \sigma^2}\Big) \\
q(\textcolor{#00838f}{x_t}\mid\textcolor{#1565c0}{x_0})
&=\underbrace{\textcolor{#3949ab}{\frac{1}{2\pi(1-\bar\alpha_t)}}}_{\text{height}}
\exp\Big(\underbrace{-\frac{|\textcolor{#00838f}{x_t}-\sqrt{\textcolor{#2e7d32}{\bar\alpha_t}}\,\textcolor{#1565c0}{x_0}|^2}{2\textcolor{#ef6c00}{(1-\bar\alpha_t)}}}_{\text{exponent}}\Big)
\end{aligned}
$$

**What the equation says.** $|x - \mu|^2$ is the squared distance from the centre, dividing by $2\sigma^2$ measures it against the width, and $\exp(-\cdot)$ makes the height fall as the point moves away. Put $\mu = \sqrt{\bar\alpha_t}\,x_0$ and $\sigma^2 = 1 - \bar\alpha_t$ and it is the density of the one jump.

**Why the power $d/2$ is there.** Each independent coordinate brings its own 1D front factor $1/\sqrt{2\pi\sigma^2}$, and the 2D front is [their product](../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=307). At $t = 50$ the 1D peak is 0.5523 and the 2D front is $0.5523^2 = 0.3050$; with the 1D front 0.5523 used in 2D, the volume would be $0.5523 \times 2\pi \times 0.5217 = 1.8105$.

**In one dimension first.** A clean value 0.5 at $t = 50$:

$$
\underbrace{0.6916 \times 0.5 = 0.3458}_{\text{centre } \sqrt{\bar\alpha_{50}} \times 0.5},
\qquad
\underbrace{\sqrt{0.5217} = 0.7223}_{\text{sd, the width}},
\qquad
\underbrace{\frac{1}{\sqrt{2\pi} \times 0.7223} = \frac{1}{1.8105} = 0.5523}_{\text{peak height}}
$$

**What the equation says.** The 1D bell for the clean value 0.5 sits at 0.3458 with width 0.7223. Its height at the centre is 0.5523, which [[Running The Density Of The One Jump#Try the density yourself|step 7 of the sandbox]] draws under 200,000 sampled draws.

## The exponent on the toy

Navigation: ⬅️ [[#The 2D Gaussian written out]] | 📋 [[#Table of contents|TOC]]

**What this section checks.** [[The Density Of The One Jump#The exponent at the drawn point]] shows that the exponent at the drawn point is $-|\varepsilon|^2/2$ at every $t$. Here it is worked on the toy, then broken by dropping the centre's square root.

**The worked numbers.** The 2D toy at $t = 50$, $x_0 = (0, 0.5)$, $\varepsilon = (0.3, -1.2)$, $|\varepsilon|^2 = 0.09 + 1.44 = 1.53$:

$$
\begin{aligned}
\text{centre:}\quad & \underbrace{0.6916}_{\sqrt{\bar\alpha_{50}}} \times \textcolor{#1565c0}{(0, 0.5)} = (0, 0.3458) \\
\textcolor{#00838f}{x_{50}}:\quad & (0, 0.3458) + \underbrace{0.7223 \times \textcolor{#6a1b9a}{(0.3, -1.2)}}_{d \,=\, (0.2167,\ -0.8668)} = (0.2167, -0.5210) \\
|d|^2:\quad & \underbrace{0.5217}_{1-\bar\alpha_{50}} \times \underbrace{1.53}_{|\varepsilon|^2} = 0.7983 \\
\text{exponent:}\quad & -0.7983 / (2 \times 0.5217) = -0.765 \\
\text{front factor:}\quad & \textcolor{#3949ab}{1 / (2\pi \times 0.5217) = 0.3050} \\
q:\quad & \underbrace{0.3050}_{\text{height}} \times \underbrace{e^{-0.765}}_{0.4653} = 0.1419
\end{aligned}
$$

**What the equation says.** The draw lands 0.8935 from the centre, which is $0.7223 \times 1.2369$, the noise scale times $|\varepsilon|$. The exponent there is −0.765 and the density 0.1419, the highlighted row of [[The Density Of The One Jump#The one-shot draw and its density|the toy table]].

**The same $\varepsilon$ at $t = 25$**, with $\sqrt{\bar\alpha_{25}} = 0.9141$ and $\sqrt{1 - \bar\alpha_{25}} = 0.4054$:

$$
\begin{aligned}
\textcolor{#00838f}{x_{25}}:\quad & (0, 0.4571) + \underbrace{0.4054 \times \textcolor{#6a1b9a}{(0.3, -1.2)}}_{d} = (0.1216, -0.0295) \\
|d|^2:\quad & 0.1644 \times 1.53 = 0.2515, \qquad \text{exponent } -0.2515 / (2 \times 0.1644) = -0.765 \\
q:\quad & \underbrace{\textcolor{#3949ab}{\frac{1}{2\pi \times 0.1644}}}_{0.9682} \times \underbrace{0.4653}_{e^{-0.765}} = 0.4505
\end{aligned}
$$

**What the equation says.** The draw lands closer to a closer centre, and the exponent is again −0.765. The narrower bell stands taller, so $q$ is 0.4505 here; at $t = 75$ the same move gives $0.1837 \times 0.4653 = 0.0855$.

**The broken run.** With the centre written as $\bar\alpha_t\,x_0$, the displacement picks up an extra piece that does not scale with $\varepsilon$:

$$
\begin{aligned}
d &= x_t - \bar\alpha_t\,x_0 = (\sqrt{\bar\alpha_t} - \bar\alpha_t)\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon \\
t = 50:\quad d &= (0.69159 - 0.47830) \times (0, 0.5) + (0.21669, -0.86677) = (0.2167, -0.7601)
\end{aligned}
$$

$$
\underbrace{d}_{\text{from the wrong centre}}
=
\underbrace{(\sqrt{\textcolor{#2e7d32}{\bar\alpha_t}} - \textcolor{#2e7d32}{\bar\alpha_t})\,\textcolor{#1565c0}{x_0}}_{(0,\ 0.10665) \text{ at } t = 50\text{: no } \varepsilon \text{ in it}}
+
\underbrace{\textcolor{#ef6c00}{\sqrt{1 - \bar\alpha_t}}\,\textcolor{#6a1b9a}{\varepsilon}}_{(0.21669,\ -0.86677)}
=
(0.2167, -0.7601)
$$

**What the equation says.** The displacement from the wrong centre is no longer $0.7223\,\varepsilon$, so the variance does not cancel. The exponent is −0.5987 at $t = 50$ and −0.6535 at $t = 25$, as [[Running The Density Of The One Jump#Try the density yourself|step 5 of the sandbox]] printed.

```python
import numpy as np
import matplotlib.pyplot as plt

BLUE, TEAL, ORANGE, GHOST = "#1565c0", "#00838f", "#ef6c00", "#757575"
BOX = dict(fc="white", ec="none", alpha=0.85, pad=1.5)
k = np.arange(101)                                       # the 100-step cosine schedule
C = np.cos((k / 100 + 0.008) / 1.008 * np.pi / 2) ** 2
abar = np.cumprod(1 - np.clip(1 - C[1:] / C[:-1], 0, 0.999))
x0, eps = np.array([0.0, 0.5]), np.array([0.3, -1.2])
th = np.linspace(0, 2 * np.pi, 300)
def ring(ax, c, r, **kw):
    ax.plot(c[0] + r * np.cos(th), c[1] + r * np.sin(th), **kw)
fig, (both, broken) = plt.subplots(1, 2, figsize=(13, 6.4), sharey=True)
for t, light, dy in [(25, "#80cbc4", 0.12), (50, TEAL, -0.18)]:
    a = abar[t]; sd = np.sqrt(1 - a)
    mu = np.sqrt(a) * x0; xt = mu + sd * eps
    q = np.exp(-eps @ eps / 2) / (2 * np.pi * (1 - a))
    ring(both, mu, np.linalg.norm(xt - mu), color=light, lw=2)
    both.plot(*mu, "o", mfc="white", mec=BLUE, mew=2, ms=9)
    both.annotate("", xt, mu, arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2.2))
    both.plot(*xt, "o", color=light, ms=10, mec=TEAL)
    both.text(xt[0] + 0.07, xt[1] + dy, f"t = {t}: x = ({xt[0]:.4f}, {xt[1]:.4f})\nd = {sd:.4f} ε, q = {q:.4f}",
              color=TEAL, fontsize=10.5, bbox=BOX)
    both.text(-1.55, mu[1] - 0.02, f"centre t = {t}: (0, {mu[1]:.4f})", color=BLUE, fontsize=10.5, va="center", bbox=BOX)
both.plot(*x0, "*", color=BLUE, ms=15)
both.text(0.08, 0.58, "x₀ = (0, 0.5)", color=BLUE, fontsize=11, bbox=BOX)
both.text(-1.55, -1.45, "each circle: exponent −0.765 = −|ε|²/2\nradius 0.4054 · 1.2369 = 0.5015 at t = 25\nradius 0.7223 · 1.2369 = 0.8935 at t = 50",
          color=TEAL, fontsize=10.5, bbox=BOX)
both.set_title("with the square root: both draws on the −0.765 contour", fontsize=12)
a = abar[50]; sd = np.sqrt(1 - a)
mu, wrong = np.sqrt(a) * x0, a * x0                       # (0, 0.3458) and (0, 0.2391)
xt = mu + sd * eps
dw = xt - wrong
ring(broken, mu, np.linalg.norm(sd * eps), color=TEAL, lw=1.5, alpha=0.5)
broken.plot(*mu, "o", mfc="white", mec=BLUE, mew=2, ms=9, alpha=0.5)
broken.text(0.1, 0.95, f"with the root: centre (0, {mu[1]:.4f}),\nits −0.765 contour through x₅₀", color=TEAL, fontsize=10.5, bbox=BOX)
ring(broken, wrong, np.linalg.norm(sd * eps), color=GHOST, lw=2, ls="--")
broken.plot(*wrong, "o", mfc="white", mec=GHOST, mew=2, ms=9)
broken.text(-1.55, 0.12, f"centre without the root\nᾱ₅₀ x₀ = (0, {wrong[1]:.4f})", color=GHOST, fontsize=10.5, bbox=BOX)
broken.annotate("", xt, wrong, arrowprops=dict(arrowstyle="->", color=GHOST, lw=2.2, ls="--"))
broken.plot(*xt, "o", color=TEAL, ms=10)
broken.text(-0.2, xt[1] - 0.42, f"x₅₀ = ({xt[0]:.4f}, {xt[1]:.4f})\nd = ({dw[0]:.4f}, {dw[1]:.4f}), not 0.7223 ε",
            color=TEAL, fontsize=10.5, bbox=BOX)
broken.text(-1.55, -1.45, f"grey dashed circle: where its exponent would be −0.765\nx₅₀ sits inside it, at distance {np.linalg.norm(dw):.4f}\nexponent −{dw @ dw / (2 * (1 - a)):.4f}, q = {np.exp(-dw @ dw / (2 * (1 - a))) / (2 * np.pi * (1 - a)):.4f}",
            color=GHOST, fontsize=10.5, bbox=BOX)
broken.plot(*x0, "*", color=BLUE, ms=15)
broken.set_title("without it, t = 50: x₅₀ falls off the −0.765 contour", fontsize=12)
for ax in (both, broken):
    ax.set_aspect("equal"); ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.6, 1.6)
    ax.set_xlabel("x₁", fontsize=12)
both.set_ylabel("x₂", fontsize=12)
fig.savefig("forward-density-the-exponent-contour-at-two-steps.svg", format="svg", bbox_inches="tight")
```

![Left, the blue star x0 = (0, 0.5) above two blue rings, the centres (0, 0.4571) at t = 25 and (0, 0.3458) at t = 50, each inside its own teal circle of radius 0.5015 and 0.8935, with an orange arrow 0.4054 eps and 0.7223 eps from each centre to a drawn point on its circle, q = 0.4505 and 0.1419; right, at t = 50 the grey ring of the centre without its root at (0, 0.2391), its grey dashed circle of radius 0.8935 and a grey dashed arrow (0.2167, -0.7601) to x50, which sits on the faint teal circle of the right centre and inside the grey one, exponent -0.5987, q = 0.1676|850](assets/forward-density-the-exponent-contour-at-two-steps.svg)

**How to read this.** Both panels are the plane $(x_1, x_2)$ on one scale, and each circle is the contour where the exponent is −0.765, drawn around its own centre. On the left the $t = 25$ draw lands on a circle of radius 0.5015 and the $t = 50$ draw on one of radius 0.8935: the same $\varepsilon$, scaled by 0.4054 and 0.7223, reaches the same contour both times. On the right the centre has lost its square root, so the drawn point sits 0.7904 from it, inside its grey −0.765 circle, and the exponent there is −0.5987.

> [!note]- How this was checked
> Every number here matches the outputs of the scripts in [[Running The Density Of The One Jump]], re-run byte for byte on 2026-10-21 on mscluster (Linux) with Python 3.12.10 in an empty `~/playground/sandbox/forward-density`. The 1D peak 0.5523, the 2D front factor $0.5523^2 = 0.3050$ and the volume 1.8105 were computed that day by a throwaway script on the same `schedule.py`.
>
> The figure script was run on 2026-10-21 on mscluster with Python 3.12.10, matplotlib 3.10.8 and numpy 2.4.3 in that folder, by vault-writer, and its SVG was opened (rendered to PNG by PyMuPDF 1.27.2) before filing; a second run from the code block as filed drew it pixel-identical. PyMuPDF does not draw dash patterns, so the broken circle is also named by its grey colour. The figure replaces drawn prompt 38 (the mechanism) in `.prompts/Diffusion Models.md`, whose faithfulness note asked for exact radii with each drawn point on its circle.
>
> Chan's PDF pp. 306, 307 and 315 were opened in the vault's shelf copy and read as text on 2026-10-21: p. 306 gives the d-dimensional Gaussian density (Definition 5.22), p. 307 writes a diagonal-covariance Gaussian as a product of 1D Gaussians, and p. 315 states Theorem 5.19.
