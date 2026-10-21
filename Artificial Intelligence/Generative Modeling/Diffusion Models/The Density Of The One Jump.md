---
aliases: [density of the one jump, the one jump's density, one-shot density, one-shot draw, one-shot forward draw, the one-shot draw and its density, "q(x_t | x_0)", density of q(x_t | x_0), forward density, forward process density, "N(x_t; sqrt(abar_t) x_0, (1 - abar_t) I)", exponent at the drawn point, "-|eps|^2 / 2", the exponent is the same at every step, displacement from the centre]
sources:
  - "Ho, Jain, Abbeel, Denoising Diffusion Probabilistic Models, NeurIPS 2020, equation (4): https://arxiv.org/abs/2006.11239"
  - "The Little Book of Generative AI Foundations, section 4.1.1, PDF p. 71, q(x_t | x_0) = N(x_t | sqrt(abar_t) x_0, (1 - abar_t) I): ../../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=71"
  - "Chan, Introduction to Probability for Data Science, Michigan Publishing 2021, Definition 5.22, the d-dimensional Gaussian density, PDF p. 306, with Definitions 5.3 and 5.16 (PDF pp. 266 and 287) and Theorem 5.19 (PDF p. 315): ../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=306"
standard: vault-note v2
---

# The Density Of The One Jump

Up: [[Diffusion Models]] · ⬅️ [[Running From Many Steps To One Jump]] · [[How The Density Follows From The Draw]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[From Many Steps To One Jump]] for the signal $\sqrt{\bar\alpha_t}$ and the noise variance $1 - \bar\alpha_t$, [[Sums Of Independent Gaussians#How the rule works|the sum of independent Gaussians]] for why all that noise is one draw, [[Scaling And Shifting A Random Variable#What scaling and shifting do|scaling and shifting]] for why adding a constant moves only the centre, and [[Diagonal Covariance#How it works|the diagonal Gaussian density]] with [[The Front Factor Of A Gaussian Density#The front factor from the bell's area|its front factor]] for the formula itself.

**For a fixed clean point, the noised point at step $t$ lands in a round Gaussian bell centred at $\sqrt{\bar\alpha_t}\,x_0$.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. It has no questions on this note yet.

> [!warning]- Unfinished
> - The deep-dive sheet is waiting: prompt 39 in the vault's `.prompts/Diffusion Models.md`.
> - The diffusion models quiz has no questions on this note yet.

Stated claims: 0.

**What it says.** All the noise the small steps add is one Gaussian draw, so the noised point is $x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon$ with a single standard normal $\varepsilon$. For a fixed clean point its density is $q(x_t \mid x_0) = \mathcal{N}(x_t;\ \sqrt{\bar\alpha_t}\,x_0,\ (1 - \bar\alpha_t) I)$.

**What stays fixed.** At the point the draw lands on, the exponent of that density is $-|\varepsilon|^2/2$ whatever $t$ is, because the variance $1 - \bar\alpha_t$ cancels. The next step in the walk differentiates exactly this exponent to get the score.

**Where it comes from.** The density form is *cited* from Ho et al., equation (4), and from [the little book, PDF p. 71](../../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=71). Every step from the draw to it is *derived* below.

**How steps are counted.** Steps are counted as the rebuild's code counts them, from 0, so $\bar\alpha_{50} = 0.4783$ and $\bar\alpha_{25} = 0.8356$, as in [[From Many Steps To One Jump]].

**Colours in this note.** <span style="color:#1565c0">**Blue is the clean point $x_0$ and the centre $\sqrt{\bar\alpha_t}\,x_0$ it is shrunk to**</span>, <span style="color:#00838f">**teal is the noisy point $x_t$**</span>, <span style="color:#6a1b9a">**purple is the standard normal draw $\varepsilon$**</span>, <span style="color:#2e7d32">**green is the kept signal share $\bar\alpha_t$**</span>, <span style="color:#ef6c00">**orange is the noise scale $\sqrt{1 - \bar\alpha_t}$, its variance $\sigma^2$ and the displacement $d$ it scales**</span>, <span style="color:#3949ab">**indigo is the front factor**</span>, and <span style="color:#757575">**grey is the centre without its square root**</span>. The first five mean the same as on the one-expert rebuild's step 4 page and in [[From Many Steps To One Jump]].

## Table of contents

- [[#The one-shot draw and its density]]
- [[#When to reach for the density]]
- [[#The form of the density]]
- [[#Try the density yourself]]
- [[#How the density follows from the draw]]
- [[#Other ways to get the density]]
- [[#Why the density matters]]
- [[#The density taught in, applied in]]

## The one-shot draw and its density

Navigation: 📋 [[#Table of contents|TOC]] | [[#When to reach for the density]] ➡️

Textbook: [The little book of generative AI foundations, section 4.1.1, the closed form and $q(x_t \mid x_0)$, PDF p. 71](../../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=71)

**The one jump's density**, also the forward density, the one-shot density or $q(x_t \mid x_0)$: for a clean point $x_0$ held fixed, the 2D Gaussian centred at $\sqrt{\bar\alpha_t}\,x_0$ with variance $1 - \bar\alpha_t$ on each axis. *Derived* in [[#How the density follows from the draw]].

**The one-shot draw** makes the noised point at step $t$ from the clean point and one standard normal draw: $x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon$. The draw is the sampler, and the density says how likely each landing point is.

**The toy numbers.** One clean point $x_0 = (0, 0.5)$ and one draw $\varepsilon = (0.3, -1.2)$, pushed to five steps of the 100-step cosine schedule by `density.py` and `every_t.py` in [[Running The Density Of The One Jump#Try the density yourself|the sandbox]].

<table>
<tr><th>step <i>t</i></th><th style="color:#2e7d32">ᾱ<sub><i>t</i></sub></th><th style="color:#1565c0">centre √ᾱ<sub><i>t</i></sub> <i>x</i><sub>0</sub></th><th style="color:#ef6c00">σ² = 1 − ᾱ<sub><i>t</i></sub></th><th style="color:#00838f">drawn point <i>x</i><sub><i>t</i></sub></th><th>|<i>d</i>|²</th><th>exponent −|<i>d</i>|²/(2σ²)</th><th style="color:#3949ab">front factor 1/(2πσ²)</th><th><i>q</i>(<i>x</i><sub><i>t</i></sub> | <i>x</i><sub>0</sub>)</th></tr>
<tr><td>0</td><td>0.9994</td><td>(0, 0.4998)</td><td>0.000631</td><td>(0.0075, 0.4697)</td><td>0.000966</td><td style="border:2px dashed #212121">−0.7650</td><td>252.1140</td><td>117.3172</td></tr>
<tr><td>25</td><td>0.8356</td><td>(0, 0.4571)</td><td>0.1644</td><td>(0.1216, −0.0295)</td><td>0.2515</td><td style="border:2px dashed #212121">−0.7650</td><td>0.9682</td><td>0.4505</td></tr>
<tr style="background:#fff8e1"><td><b>50</b></td><td><b>0.4783</b></td><td style="border:2px solid #212121"><b>(0, 0.3458)</b></td><td style="border:2px solid #212121"><b>0.5217</b></td><td style="border:2px solid #212121"><b>(0.2167, −0.5210)</b></td><td style="border:2px solid #212121"><b>0.7983</b></td><td style="border:2px dashed #212121"><b>−0.7650</b></td><td style="border:2px solid #212121"><b>0.3050</b></td><td style="border:2px solid #212121"><b>0.1419</b></td></tr>
<tr><td>75</td><td>0.1335</td><td>(0, 0.1827)</td><td>0.8665</td><td>(0.2793, −0.9344)</td><td>1.3258</td><td style="border:2px dashed #212121">−0.7650</td><td>0.1837</td><td>0.0855</td></tr>
<tr><td>99</td><td>0.0000</td><td>(0, 0.0002)</td><td>1.0000</td><td>(0.3000, −1.1998)</td><td>1.5300</td><td style="border:2px dashed #212121">−0.7650</td><td>0.1592</td><td>0.0741</td></tr>
</table>

**How to read this table.** Each row is one code step for the same clean point and the same draw. Green ᾱ<sub>t</sub> is the share of the clean point's variance kept, blue is the centre the bell sits on, orange σ² is the variance on each axis, and teal is where the draw lands. |d|² is the squared distance from the centre to the drawn point, and q is the front factor times e to the exponent.

**What to look for.** The dashed exponent column reads −0.7650 in every row, while q runs from 117.3172 at t = 0 down to 0.0741 at t = 99: only the front factor moves. The highlighted row, boxed, is the one worked by hand in [[How The Density Follows From The Draw#The exponent on the toy]]; ᾱ<sub>99</sub> is 2.4 × 10<sup>−7</sup>, which prints as 0.0000.

### The symbols: q, the bar and the two points

**What the symbols mean.** $q$ is the forward process's own distribution, fixed by the schedule and never learned; a learned model gets the letter $p$. $x_t$ is the noisy point and $x_0$ the clean point.

$$
\underbrace{q}_{\text{the forward process's density}}\big(\underbrace{\textcolor{#00838f}{x_t}}_{\text{one noisy draw}}\ \underbrace{\mid}_{\text{given}}\ \underbrace{\textcolor{#1565c0}{x_0}}_{\text{clean point, held fixed}}\big)
$$

**What the bar means.** The bar reads "given": the clean point is held fixed and only $\varepsilon$ is random. So $q(x_t \mid x_0)$ is how the noisy point is spread once the clean point is chosen, [Chan's conditional PDF, Definition 5.16, PDF p. 287](../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=287).

### The base word: density

**What the word means.** A density gives a height at each point of the plane. The chance of landing in a small patch is about that height times the patch's area.

$$
\underbrace{\Pr(\textcolor{#00838f}{x_t} \in \text{small patch})}_{\text{a probability}}
\;\approx\;
\underbrace{q(\textcolor{#00838f}{x_t} \mid \textcolor{#1565c0}{x_0})}_{\text{height}}
\times
\underbrace{\text{area of the patch}}_{\text{size}}
$$

**What it means.** At $t = 50$ the height at the drawn point is 0.1419, so a patch 0.01 by 0.01 there holds about $0.1419 \times 0.0001 = 0.0000142$ of the chance. A height is not a probability: at $t = 0$ the bell is only 0.0251 wide and its height at the drawn point is 117.3172.

### The qualifier: one jump

**What the words mean.** The density is of the one jump from the clean point to step $t$, which [[From Many Steps To One Jump#The base word: jump|the jump note]] takes apart word by word. It is not the density of one small step.

$$
\underbrace{\textcolor{#1565c0}{x_0} \longrightarrow \textcolor{#00838f}{x_t}}_{\text{the one jump: variance } 1 - \bar\alpha_t}
\qquad \text{against} \qquad
\underbrace{x_{t-1} \to x_t}_{\text{one small step: variance } \beta_t}
$$

**What it means.** At $t = 50$ the jump's bell has variance 0.5217 on each axis. The single small step at $t = 50$ adds only $\beta_{50} = 0.0315$, the fresh noise in [[From Many Steps To One Jump#Many steps collapse into one jump|the jump note's table]].

### All the words together: the formula

$$
q(x_t \mid x_0) = \mathcal{N}\big(x_t;\ \sqrt{\bar\alpha_t}\,x_0,\ (1 - \bar\alpha_t) I\big)
$$

$$
\underbrace{q(\textcolor{#00838f}{x_t}\mid\textcolor{#1565c0}{x_0})}_{\text{the noisy point given the clean point}}
=
\mathcal N\!\Big(
\textcolor{#00838f}{x_t};\
\underbrace{\sqrt{\textcolor{#2e7d32}{\bar\alpha_t}}\,\textcolor{#1565c0}{x_0}}_{\text{centre}},\
\underbrace{\textcolor{#ef6c00}{(1-\bar\alpha_t)}\,I}_{\text{same variance on both axes}}
\Big)
$$

**What the equation says.** Given the clean point, the noisy point is Gaussian, centred on the shrunken clean point with the complementary share of variance on each axis. At $t = 50$ that is a bell centred at $(0, 0.3458)$ with variance 0.5217.

### The consequence: only the height moves with t

$$
\underbrace{q(\textcolor{#00838f}{x_t} \mid \textcolor{#1565c0}{x_0})}_{\text{at the drawn point}}
=
\underbrace{\textcolor{#3949ab}{\frac{1}{2\pi(1 - \bar\alpha_t)}}}_{\text{the only part that moves}}
\times
\underbrace{e^{-|\textcolor{#6a1b9a}{\varepsilon}|^2/2}}_{e^{-0.765} \,=\, 0.4653 \text{ at every } t}
$$

**What it means.** Across the toy table the exponent stays at −0.7650 while $q$ falls from 117.3172 at $t = 0$ to 0.0741 at $t = 99$. [[#The exponent at the drawn point]] derives why.

## When to reach for the density

Navigation: ⬅️ [[#The one-shot draw and its density]] | 📋 [[#Table of contents|TOC]] | [[#The form of the density]] ➡️

**You need a height, not a sample.** Reach for it when you need how likely a noised point is: to write $\log q(x_t \mid x_0)$ and take its gradient for the score, or to check that a drawn point sits where the formula says.

**What goes wrong without it.** Without the density there is only the sampler, and nothing to differentiate.

## The form of the density

Navigation: ⬅️ [[#When to reach for the density]] | 📋 [[#Table of contents|TOC]] | [[#Try the density yourself]] ➡️

Textbook: [Chan, Introduction to Probability for Data Science, Definition 5.22, the d-dimensional Gaussian density, PDF p. 306](../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=306)

**The form, slot by slot.** With $\sigma^2 = 1 - \bar\alpha_t$ and the centre $\mu = \sqrt{\bar\alpha_t}\,x_0$:

$$
\begin{aligned}
x_t &= \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon, && \varepsilon \sim \mathcal{N}(0, I), \text{ the same shape as } x_0 \\
q(x_t \mid x_0) &= \frac{1}{2\pi\sigma^2} \exp\!\Big(-\frac{|x_t - \mu|^2}{2\sigma^2}\Big) && \text{in 2D} \\
d &= x_t - \mu = \sqrt{1 - \bar\alpha_t}\,\varepsilon \\
-\frac{|d|^2}{2\sigma^2} &= -\frac{|\varepsilon|^2}{2} && \text{the same at every } t
\end{aligned}
$$

$$
\begin{aligned}
\underbrace{\textcolor{#00838f}{x_t}}_{\text{one draw}}
&= \underbrace{\sqrt{\textcolor{#2e7d32}{\bar\alpha_t}}\,\textcolor{#1565c0}{x_0}}_{\mu\text{, the centre, } x_0 \text{ held fixed}}
+ \underbrace{\textcolor{#ef6c00}{\sqrt{1 - \bar\alpha_t}}\,\textcolor{#6a1b9a}{\varepsilon}}_{\text{the noise}} \\
q(\textcolor{#00838f}{x_t} \mid \textcolor{#1565c0}{x_0})
&= \underbrace{\textcolor{#3949ab}{\frac{1}{2\pi\sigma^2}}}_{\text{front factor: volume } 1}
\exp\!\Big(-\underbrace{\frac{|\textcolor{#00838f}{x_t} - \mu|^2}{2\textcolor{#ef6c00}{\sigma^2}}}_{\text{squared distance, in widths}}\Big) \\
\underbrace{\textcolor{#ef6c00}{d}}_{\text{displacement}}
&= \textcolor{#00838f}{x_t} - \mu = \textcolor{#ef6c00}{\sqrt{1 - \bar\alpha_t}}\,\textcolor{#6a1b9a}{\varepsilon} \\
\underbrace{-\frac{|\textcolor{#ef6c00}{d}|^2}{2\textcolor{#ef6c00}{\sigma^2}}}_{\text{exponent at the drawn point}}
&= -\frac{|\textcolor{#6a1b9a}{\varepsilon}|^2}{2}
\end{aligned}
$$

**What the equation says.** The draw lands at the centre plus a displacement, and the density is a front factor times $e$ to minus the squared distance over twice the variance. At the drawn point the displacement is $\sqrt{1 - \bar\alpha_t}\,\varepsilon$, so the exponent is $-|\varepsilon|^2/2$.

**Why the conditioning bar is there.** The bar holds $x_0$ fixed, so the centre is one point, $(0, 0.3458)$ at $t = 50$, and $q$ at $x_{50}$ is 0.1419. Without the bar, $q(x_t)$ [averages over every clean point in the data](../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=266). On a made-up data set of two clean points, $(0, 0.5)$ and $(0, -0.5)$, it is $(0.1419 + 0.2832)/2 = 0.2126$ at the same $x_{50}$.

**Why the square root on the centre is there.** The centre is the mean of the draw, and $\varepsilon$ averages to zero, so the mean is $\sqrt{\bar\alpha_t}\,x_0$. With the root the centre is $(0, 0.3458)$, the exponent −0.7650 at both $t = 50$ and $t = 25$, and $q = 0.1419$; without it the centre is $(0, 0.2391)$, the exponent −0.5987 at $t = 50$ and −0.6535 at $t = 25$, and $q = 0.1676$.

**Why the front factor $1/(2\pi\sigma^2)$ is there.** It makes the volume under the surface 1, as [[The Front Factor Of A Gaussian Density#The front factor from the bell's area|the front factor note]] proves by a grid sum. At $t = 50$ it is 0.3050 and the surface's volume over the square from −6 to 6 sums to 1.0000. Without it the volume is $2\pi\sigma^2 = 3.2782$, and the height at $x_{50}$ would read 0.4653.

**Why the divisor $2\sigma^2$ is there.** It measures the squared distance against the bell's width. With it the exponent at $x_{50}$ is $-0.7983/(2 \times 0.5217) = -0.765$ at every $t$; dividing by 2 alone gives −0.3991 at $t = 50$ and −0.1258 at $t = 25$, so it moves with $t$. Dividing by $\sigma^2$ alone gives −1.53, the exponent of a bell with half the draw's variance.

**Why the identity matrix is there.** The draw adds $\sigma\varepsilon$ to both coordinates with the same $\sigma$, so both get variance $\sigma^2$ and the contours are [circles](../../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=471). With $I$ the contour through $x_{50}$ is a circle of radius 0.8935 and the exponent there is −0.765. With $(1 - \bar\alpha_t)\,\mathrm{diag}(1, 2)$ in its place the exponent at $x_{50}$ would be −0.405 and $q$ 0.1439, a density that no longer matches the draw.

```python
import numpy as np
import matplotlib.pyplot as plt

BLUE, TEAL, ORANGE, INDIGO = "#1565c0", "#00838f", "#ef6c00", "#3949ab"
BOX = dict(fc="white", ec="none", alpha=0.85, pad=1.5)
k = np.arange(101)                                       # the 100-step cosine schedule
C = np.cos((k / 100 + 0.008) / 1.008 * np.pi / 2) ** 2
abar = np.cumprod(1 - np.clip(1 - C[1:] / C[:-1], 0, 0.999))
a = abar[50]; var = 1 - a; sd = np.sqrt(var)              # 0.4783, 0.5217, 0.7223
x0, eps = np.array([0.0, 0.5]), np.array([0.3, -1.2])
mu = np.sqrt(a) * x0                                       # the centre (0, 0.3458)
xt = mu + sd * eps                                         # the drawn point (0.2167, -0.5210)
front = 1 / (2 * np.pi * var)                              # 0.3050
def q(x1, x2):
    return front * np.exp(-((x1 - mu[0]) ** 2 + (x2 - mu[1]) ** 2) / (2 * var))
g = np.linspace(-1.6, 1.6, 401)
X1, X2 = np.meshgrid(g, g)
fig, (plane, cut) = plt.subplots(1, 2, figsize=(13, 5.8), gridspec_kw={"width_ratios": [1, 1.1]})
plane.contourf(X1, X2, q(X1, X2), levels=12, cmap="Greys", vmin=0, vmax=3 * front)
r = np.linalg.norm(xt - mu)                                # 0.8935, where the exponent is -0.765
th = np.linspace(0, 2 * np.pi, 300)
plane.plot(mu[0] + r * np.cos(th), mu[1] + r * np.sin(th), color=TEAL, lw=1.5)
plane.plot(mu[0] + sd * np.cos(th), mu[1] + sd * np.sin(th), color="#212121", lw=1.2)
plane.text(-0.95, 1.12, "1 sd = 0.7223, black circle", color="#424242", fontsize=11, bbox=BOX)
plane.text(-1.55, -1.25, f"the contour through x₅₀:\nexponent −0.765, q = {q(*xt):.4f}", color=TEAL, fontsize=11, bbox=BOX)
plane.plot(*x0, "*", color=BLUE, ms=16)
plane.text(0.1, 0.62, "clean point x₀ = (0, 0.5)", color=BLUE, fontsize=11, bbox=BOX)
plane.plot(*mu, "o", mfc="white", mec=BLUE, mew=2, ms=10)
plane.text(-1.5, 0.12, f"centre √ᾱ₅₀ x₀\n= (0, {mu[1]:.4f})", color=BLUE, fontsize=11, bbox=BOX)
plane.annotate("", xt, mu, arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2.5))
plane.text(0.2, -0.05, f"d = 0.7223 ε\n= ({sd * eps[0]:.4f}, {sd * eps[1]:.4f})", color=ORANGE, fontsize=11, bbox=BOX)
plane.plot(*xt, "o", color=TEAL, ms=10)
plane.text(xt[0] + 0.08, xt[1] - 0.15, f"x₅₀ = ({xt[0]:.4f}, {xt[1]:.4f})", color=TEAL, fontsize=11, bbox=BOX)
plane.set_aspect("equal"); plane.set_xlim(-1.6, 1.6); plane.set_ylim(-1.6, 1.6)
plane.set_xlabel("x₁", fontsize=12); plane.set_ylabel("x₂", fontsize=12)
plane.set_title("q(x | x₀) at t = 50, shaded by height", fontsize=12)
rr = np.linspace(0, 2.2, 300)
cut.plot(rr, front * np.exp(-rr ** 2 / (2 * var)), color="#424242", lw=2.5)
cut.plot(0, front, "o", color=INDIGO, ms=9)
cut.text(0.06, front + 0.006, f"front factor 1/(2π · {var:.4f}) = {front:.4f}", color=INDIGO, fontsize=11)
for dist, name, col in [(sd, "1 sd", "#616161"), (r, "x₅₀", TEAL)]:
    h = front * np.exp(-dist ** 2 / (2 * var))
    cut.plot([dist, dist], [0, h], color=col, ls="--", lw=1.2)
    cut.plot(dist, h, "o", color=col, ms=8)
    cut.text(dist + 0.06, h + 0.01, f"{name}: distance {dist:.4f}, height {h:.4f}", color=col, fontsize=11)
cut.text(0.9, 0.24, f"height = {front:.4f} · exp(−distance² / (2 · {var:.4f}))", fontsize=11)
cut.set_xlabel("distance from the centre", fontsize=11); cut.set_ylabel("density q", fontsize=11)
cut.set_ylim(0, 0.34); cut.set_xlim(0, 2.2)
cut.set_title("one slice through the centre", fontsize=12)
fig.savefig("forward-density-the-form-at-step-50.svg", format="svg", bbox_inches="tight")
```

![Left, the plane at t = 50 shaded grey by the height of q, with the blue star x0 = (0, 0.5), the blue ring at the centre (0, 0.3458), the orange arrow d = 0.7223 eps = (0.2167, -0.8668) to the teal drawn point (0.2167, -0.5210), the black one-sd circle of radius 0.7223 and the teal contour through the drawn point labelled exponent -0.765, q = 0.1419; right, the height along a line through the centre against the distance from it, 0.3050 at the centre, 0.1850 at one sd and 0.1419 at the drawn point's distance 0.8935|850](assets/forward-density-the-form-at-step-50.svg)

**How to read this.** On the left the axes are the two coordinates $x_1$ and $x_2$, and the grey shading is the height of $q(x \mid x_0)$ at $t = 50$, darkest at the blue ring, the centre $(0, 0.3458)$. The orange arrow is the displacement $d = 0.7223\,\varepsilon$ from the centre to the teal drawn point, and the teal circle through it is where the exponent is −0.765, a little outside the black one-sd circle. On the right the x-axis is the distance from the centre and the y-axis the height: 0.3050 at the centre, which is the indigo front factor, falling to 0.1419 at the drawn point's distance 0.8935.

## Try the density yourself

Navigation: ⬅️ [[#The form of the density]] | 📋 [[#Table of contents|TOC]] | [[#How the density follows from the draw]] ➡️

**In two lines.** Nine steps in an empty folder, from the cosine schedule to the centre without its square root, the density at two steps, SciPy's check and the same draw at five steps, each with its output read field by field, are in [[Running The Density Of The One Jump#Try the density yourself]]. The steps this note cites by number (5, 6, 7 and 8) are the broken centre, the density at two steps, the two bells and SciPy, and the five steps there.

## How the density follows from the draw

Navigation: ⬅️ [[#Try the density yourself]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to get the density]] ➡️

**In two lines.** The three moves from the one-shot draw to $q(x_t \mid x_0)$ (the noise as one draw, its centre, spread and shape, and the 2D Gaussian written out) are in [[How The Density Follows From The Draw]]. They end on the exponent below, which [[How The Density Follows From The Draw#The exponent on the toy|that note works on the toy]] at $t = 50$ and $t = 25$, with the broken centre drawn beside it.

### The exponent at the drawn point

**At the point the draw lands on, the exponent of $q(x_t \mid x_0)$ is $-|\varepsilon|^2/2$ at every $t$.** The displacement from the centre is $d = x_t - \sqrt{\bar\alpha_t}\,x_0 = \sqrt{1 - \bar\alpha_t}\,\varepsilon$, and the variance cancels:

$$
\begin{aligned}
|d|^2 &= (1 - \bar\alpha_t)\,|\varepsilon|^2 \\
-\frac{|d|^2}{2(1 - \bar\alpha_t)} &= -\frac{(1 - \bar\alpha_t)\,|\varepsilon|^2}{2(1 - \bar\alpha_t)} = -\frac{|\varepsilon|^2}{2}
\end{aligned}
$$

$$
-\frac{\big|\textcolor{#ef6c00}{\sqrt{1-\bar\alpha_t}}\,\textcolor{#6a1b9a}{\varepsilon}\big|^2}{2(1-\textcolor{#2e7d32}{\bar\alpha_t})}
=
-\frac{\underbrace{(1-\textcolor{#2e7d32}{\bar\alpha_t})}_{\text{from the squared displacement}}\,|\textcolor{#6a1b9a}{\varepsilon}|^2}{2\underbrace{(1-\textcolor{#2e7d32}{\bar\alpha_t})}_{\text{from the width}}}
=
-\frac{|\textcolor{#6a1b9a}{\varepsilon}|^2}{2}
=
-\frac{0.09+1.44}{2}
=
-0.765
$$

**What the equation says.** A later step makes the bell wider, and the draw lands proportionally farther from the centre, so the two effects cancel. Only the front factor $1/(2\pi(1 - \bar\alpha_t))$ changes with $t$, as [[Running The Density Of The One Jump#Try the density yourself|step 8 of the sandbox]] printed.

**Where it leads.** The score of $q(x_t \mid x_0)$ is the gradient of this exponent with respect to $x_t$, which the next piece of the walk takes. The front factor has no $x_t$ in it, and writing $x_t$ out cancels the clean point:

$$
\underbrace{x_t-\sqrt{\bar\alpha_t}\,x_0}_{d}=\big(\cancel{\sqrt{\bar\alpha_t}\,x_0}+\textcolor{#ef6c00}{\sqrt{1-\bar\alpha_t}}\,\textcolor{#6a1b9a}{\varepsilon}\big)-\cancel{\sqrt{\bar\alpha_t}\,x_0},
\qquad
\underbrace{\nabla_{x_t}\log q}_{\text{the score}}=-\frac{\textcolor{#ef6c00}{\sqrt{1-\bar\alpha_t}}\,\textcolor{#6a1b9a}{\varepsilon}}{1-\bar\alpha_t}=-\frac{\textcolor{#6a1b9a}{\varepsilon}}{\textcolor{#ef6c00}{\sqrt{1-\bar\alpha_t}}}
$$

**What the equation says.** At the drawn point the score is the draw, reversed and divided by the noise scale. At $t = 50$ it is $-(0.3, -1.2)/0.7223 = (-0.4153, 1.6613)$.

*🖼️ Diagram wanted: the deep-dive sheet composing the form, the mechanism and step 6's run. Prompt 39 in the vault's `.prompts/Diffusion Models.md`.*

## Other ways to get the density

Navigation: ⬅️ [[#How the density follows from the draw]] | 📋 [[#Table of contents|TOC]] | [[#Why the density matters]] ➡️

**One bell per coordinate.** When the covariance is diagonal, the 2D density is one 1D bell per coordinate multiplied, as [[Running The Density Of The One Jump#Try the density yourself|step 7 of the sandbox]] runs: $0.5280 \times 0.2688 = 0.1419$ at $t = 50$. It gives the same number and makes the independence of the coordinates visible.

**A library density.** `statistics.NormalDist` gives one coordinate's bell, and SciPy's `multivariate_normal(mean, cov).pdf` the whole vector. Step 7 runs SciPy and gets 0.1419 at $t = 50$ and 0.4505 at $t = 25$, equal to the hand formula to within $2.8 \times 10^{-17}$ (*shown*). It checks a hand formula; it does not show where the $-|\varepsilon|^2/2$ comes from.

**The log density**, when the next move is a gradient:

$$
\log q(x_t \mid x_0) = -\log\big(2\pi(1 - \bar\alpha_t)\big) - \frac{|x_t - \sqrt{\bar\alpha_t}\,x_0|^2}{2(1 - \bar\alpha_t)}
$$

$$
\underbrace{\log q(\textcolor{#00838f}{x_t} \mid \textcolor{#1565c0}{x_0})}_{-1.9523 \text{ at } x_{50}}
=
\underbrace{-\log\big(\textcolor{#3949ab}{2\pi(1 - \bar\alpha_t)}\big)}_{\text{no } x_t \text{ in it: } -1.1873 \text{ at } t = 50}
\;
\underbrace{-\,\frac{|\textcolor{#00838f}{x_t} - \sqrt{\textcolor{#2e7d32}{\bar\alpha_t}}\,\textcolor{#1565c0}{x_0}|^2}{2\textcolor{#ef6c00}{(1 - \bar\alpha_t)}}}_{\text{the exponent: } -0.765}
$$

**What the equation says.** The log turns the product into a sum of the log front factor and the exponent. The first term has no $x_t$ in it, so only the exponent survives differentiation.

## Why the density matters

Navigation: ⬅️ [[#Other ways to get the density]] | 📋 [[#Table of contents|TOC]] | [[#The density taught in, applied in]] ➡️

**What training compares.** Training a diffusion expert compares the network's output with the score of $q(x_t \mid x_0)$, and that score is the gradient of the exponent in [[#The exponent at the drawn point]].

**The score at the toy.** Because the exponent at the drawn point is $-|\varepsilon|^2/2$, the gradient there is $-\varepsilon/\sqrt{1 - \bar\alpha_t}$, *derived* in [[#The exponent at the drawn point]]. For the toy at $t = 50$ that is $-(0.3, -1.2)/0.7223 = (-0.4153, 1.6613)$, the rebuild's `p1.example_score` in `walk-numbers.json` (*cited*).

**Noise and score are one job.** That is why predicting the noise and predicting the score are the same job up to a scale. The cancellation only works with the square root on the centre.

## The density taught in, applied in

Navigation: ⬅️ [[#Why the density matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the `drip --math` walk of the forward process and the score in the reduce-reuse-recycle research repository, piece 1, [rung 4 as the walk kept it](../../../../PhD/reduce-reuse-recycle/artifacts/drips/forward-process-and-the-score/kept/04-the-one-shot-draw-and-its-density.md), which closes piece 1: the noise as one draw, $q(x_t \mid x_0)$ for a fixed $x_0$, the 2D isotropic density term by term, worked in 1D at $t = 50$ and on the 2D toy at $t = 50$ and $t = 25$, the exponent $-0.765$ at both, and the centre without its square root as the broken run

**Applied in:** [step 4](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-4-the-forward-process-and-the-cosine-schedule) and [step 5](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-5-the-noise-is-the-score-rescaled) of the one-expert rebuild walk in the reduce-reuse-recycle research repository. [Step 4](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step4-the-one-shot-density) writes $q(x_t \mid x_0)$ for the training pairs of one diffusion expert; step 5 takes the gradient of its log at the toy's $x_{50} = (0.2167, -0.521)$ to show that the noise, rescaled, is the score.

> [!note]- How this was checked
> Every number in the toy table and the exponent matches the outputs of the scripts in [[Running The Density Of The One Jump]], re-run byte for byte on 2026-10-21 on mscluster (Linux) with Python 3.12.10 in an empty `~/playground/sandbox/forward-density`. The table's centres and drawn points at $t = 0$, 75 and 99, the front factors, and the with-and-without moves (the two-point average 0.2126, the volume 1.0000 against 3.2782, the divisor moves −0.3991, −0.1258 and −1.53, the $\mathrm{diag}(1, 2)$ exponent −0.405 and $q$ 0.1439, the broken $q$ 0.1676, and the log density −1.9523) were computed that day by a throwaway script on the same `schedule.py` and `density.py`.
>
> The figure script was run on 2026-10-21 on mscluster with Python 3.12.10, matplotlib 3.10.8 and numpy 2.4.3 in that folder, by vault-writer, and its SVG was opened (rendered to PNG by PyMuPDF 1.27.2) before filing. It replaces drawn prompt 37 (the form) in `.prompts/Diffusion Models.md`, whose faithfulness note asked for exact positions and radii; prompt 38 (the mechanism) is replaced by the figure in [[How The Density Follows From The Draw]]. The prepared environment `~/.vault-sandbox` is missing on this machine; the system `python3` has matplotlib, numpy and SciPy 1.17.1.
>
> `schedule.py` is the same plain-Python cosine schedule as [[From Many Steps To One Jump]]. Its numbers match the rebuild's `rebuild/out/walk-numbers.json`: $\bar\alpha_{25} = 0.8356$, $\bar\alpha_{50} = 0.4783$, $\sqrt{1 - \bar\alpha_{25}} = 0.4054$, $\sqrt{1 - \bar\alpha_{50}} = 0.7223$, the toy's $x_{50} = (0.2167, -0.521)$ is `p1.example_x_t`, and $(-0.4153, 1.6613)$ is `p1.example_score`.
>
> Chan's PDF pp. 266, 287 and 306 were opened in the vault's shelf copy and read as text on 2026-10-21: p. 266 defines the marginal PDF (Definition 5.3), p. 287 the conditional PDF (Definition 5.16), and p. 306 gives the d-dimensional Gaussian density (Definition 5.22). Understanding Deep Learning's PDF p. 471 was opened: Figure C.4 and equation (C.24) show spherical covariance with circular contours and the 2D density as a product of two bells. The little book's PDF p. 71 was opened: it states $q(x_t \mid x_0) = \mathcal{N}(x_t \mid \sqrt{\bar\alpha_t}\,x_0, (1 - \bar\alpha_t) I)$ after combining the independent noise terms into one draw.
