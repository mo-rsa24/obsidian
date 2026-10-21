---
aliases: [normaliser along beta, log Z_beta along beta, d log Z_beta / d beta, slope of log Z_beta in beta, how Z_beta changes with beta]
sources:
  - "Algebra handbook, the vault's shelf copy, Mathematics/references/textbooks/algebra/algebra-handbook.pdf: logarithm formulas, PDF p. 110"
  - "Calculus textbook, the vault's shelf copy, Mathematics/references/textbooks/calculus/calculus-textbook.pdf: section 3.2, the derivative of ln x, PDF p. 216"
standard: vault-note v2
---

# The Slope Of The Normaliser In Beta

Up: [[Composition]] · ⬅️ [[Why The Normaliser Has No Slope In X]] · [[Running Why The Normaliser Has No Slope In X]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models, Composition. Needs: [[Why The Normaliser Has No Slope In X]] and [[The Log Of A Power And Of A Quotient]].

**The normaliser $Z_\beta$ has no slope in $x$, but it falls as the power $\beta$ grows.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. This note's sections are not in it yet.

> [!warning]- Unfinished
> - The [diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) does not cover this note's sections yet.

Claims marked stated: 0.

**The toy numbers.** The $\mathcal{N}(3, 4)$ height $p(x) = e^{-(x - 3)^2/8}$, the same one [[Why The Normaliser Has No Slope In X#The normaliser has no slope in x]] uses, with $Z_\beta = \sqrt{8\pi/\beta}$.

**Colours in this note.** <span style="color:#2e7d32">**Green is the normaliser $Z_\beta$ and its log**</span>, <span style="color:#ef6c00">**orange is the power $\beta$**</span>, and <span style="color:#1565c0">**blue is the point $x$ and the slope in $x$**</span>, as in [[Why The Normaliser Has No Slope In X]].

## Table of contents

- [[#The normaliser moves along beta]]
- [[#Why the slope along beta matters]]
- [[#The slope along beta taught in, applied in]]

## The normaliser moves along beta

Navigation: 📋 [[#Table of contents|TOC]] | [[#Why the slope along beta matters]] ➡️

Textbook: [algebra handbook, logarithm formulas, p. 110](../../../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=110), and the derivative of $\ln x$ in the [calculus textbook, p. 216](../../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=216)

**Slope of the normaliser in beta**, also the normaliser along $\beta$ or $\frac{d}{d\beta} \log Z_\beta$: $Z_\beta$ has [[Why The Normaliser Has No Slope In X#The normaliser has no slope in x|no slope in x]], but it does move along $\beta$. For the $\mathcal{N}(3, 4)$ height, $Z_\beta = \sqrt{8\pi/\beta}$, so by the [log rules](../../../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=110) and the [derivative of the log](../../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=216):

$$
\begin{aligned}
\log Z_\beta &= \tfrac{1}{2}\left(\log 8\pi - \log \beta\right) \\
\log Z_2 &= 1.265512, \qquad \log Z_{2.01} = 1.263018 \\
\text{quotient} &= \frac{1.263018 - 1.265512}{0.01} = -0.2494 \\
\frac{d}{d\beta} \log Z_\beta &= -\frac{1}{2\beta} = -0.25 \quad \text{at } \beta = 2
\end{aligned}
$$

$$
\log \textcolor{#2e7d32}{Z_{\textcolor{#ef6c00}{\beta}}}
=
\underbrace{\tfrac{1}{2}}_{\text{the square root}}
\Big(
\underbrace{\log 8\pi}_{\text{fixed}}
-
\underbrace{\log \textcolor{#ef6c00}{\beta}}_{\text{the only moving part}}
\Big),
\qquad
\frac{d}{d\textcolor{#ef6c00}{\beta}} \log \textcolor{#2e7d32}{Z_{\textcolor{#ef6c00}{\beta}}}
=
\underbrace{-\frac{1}{2\textcolor{#ef6c00}{\beta}}}_{-0.25 \text{ at } \beta = 2}
$$

**What the equation says.** $\log Z_\beta$ is a fixed number minus half of $\log \beta$, so it falls as $\beta$ grows. Its slope along $\beta$ is $-1/(2\beta)$, which is $-0.25$ at $\beta = 2$. *Derived*, and *shown* by rows 8 and 9 of [[Running Why The Normaliser Has No Slope In X#Reading the output|the run's output]].

**Why the $\tfrac{1}{2}$ is there.** It is the square root in $\sqrt{8\pi/\beta}$, brought down by the log rules. Without it $\log Z_2$ would be 2.531024, the log of $8\pi/2 = 12.566371$, and the slope $-1/\beta = -0.5$ instead of $-0.25$.

**Why the minus $\log \beta$ is there.** A higher power makes the bell narrower, so the area shrinks. From $\beta = 1$ to $\beta = 4$, $\log Z_\beta$ falls from 1.612086 to 0.918939, and $Z_4/Z_1 = 0.5$.

<table>
<tr><th style="color:#ef6c00">power β</th><th style="color:#2e7d32">log <i>Z</i><sub>β</sub></th><th style="color:#2e7d32">slope along β, −1/(2β)</th><th style="color:#1565c0">slope in <i>x</i> at 5, β · score(5)</th></tr>
<tr><td>0.5</td><td>1.958659</td><td>−1.000000</td><td>−0.250000</td></tr>
<tr><td>1</td><td>1.612086</td><td>−0.500000</td><td>−0.500000</td></tr>
<tr style="background:#fff8e1"><td><b>2</b></td><td style="border:2px solid #212121"><b>1.265512</b></td><td style="border:2px solid #212121"><b>−0.250000</b></td><td style="border:2px solid #212121"><b>−1.000000</b></td></tr>
<tr><td>2.01</td><td style="border:2px dashed #212121">1.263018</td><td>−0.248756</td><td>−1.005000</td></tr>
<tr><td>4</td><td>0.918939</td><td>−0.125000</td><td>−2.000000</td></tr>
</table>

**How to read this table.** Each row is one power $\beta$. The second column is the log normaliser, the third its slope along $\beta$, and the fourth the slope in $x$ at $x = 5$, which has no $Z$ term in it.

**What to look for.** The boxed and dashed cells are the step of 0.01 in $\beta$: $(1.263018 - 1.265512)/0.01 = -0.2494$ against the exact $-0.25$. The last column is $-0.5\beta$ on every row, untouched by the second.

```python
import numpy as np
import matplotlib.pyplot as plt

GREEN, ORANGE = "#2e7d32", "#ef6c00"
def log_Z(beta):
    return 0.5 * (np.log(8 * np.pi) - np.log(beta))
b = np.linspace(0.5, 4, 300)
fig, (left, right) = plt.subplots(1, 2, figsize=(12, 4.6))
left.plot(b, log_Z(b), color=GREEN, lw=2.5)
for beta in (0.5, 1, 2, 4):
    left.plot(beta, log_Z(beta), "o", color=GREEN)
    left.text(beta + 0.06, log_Z(beta) + 0.03, f"{log_Z(beta):.6f}", color=GREEN, fontsize=10)
left.plot([1.2, 2.8], [log_Z(2) + 0.2, log_Z(2) - 0.2], color="#1b5e20", ls="--", lw=1.5, zorder=3)   # slope -0.25
left.text(2.2, 1.42, "slope −1/(2β) = −0.25 at β = 2", color=GREEN, fontsize=10)
left.set(xlim=(0.4, 4.3), ylim=(0.8, 2.05), xlabel="the power β", ylabel="log Z_β")
left.xaxis.label.set_color(ORANGE)
left.set_title("in β: Z moves", fontsize=12)
right.plot(b, -0.5 * b, color=ORANGE, lw=2)
right.plot(b, -1 / (2 * b), color=GREEN, lw=2)
right.axhline(0, color=GREEN, lw=1.5, ls=":")
right.plot([2, 2], [-1, -0.25], "o", color="#212121")
right.annotate("slope in x at x = 5:\nβ · score(5) = −1.0", (2, -1), (0.5, -1.9), color=ORANGE, fontsize=10,
               arrowprops=dict(arrowstyle="->", color=ORANGE))
right.text(2.3, -0.42, "slope of log Z_β along β: −0.25", color=GREEN, fontsize=10)
right.text(0.5, 0.06, "slope of log Z_β along x: 0", color=GREEN, fontsize=10)
right.set(xlim=(0.4, 4.3), ylim=(-2.2, 0.3), xlabel="the power β", ylabel="slope")
right.set_title("x never sees Z; β does", fontsize=12)
fig.savefig("normaliser-has-no-slope-in-x-the-slope-along-beta.svg", format="svg", bbox_inches="tight")
```

![Left, log Z_beta falling against beta through 1.958659, 1.612086, 1.265512 and 0.918939 at beta = 0.5, 1, 2 and 4, with a dashed tangent of slope -0.25 at beta = 2; right, the orange line beta times score(5) through -1.0 at beta = 2, the green curve -1/(2 beta) through -0.25, and a dotted green line at 0 for the slope of log Z_beta along x|800](assets/normaliser-has-no-slope-in-x-the-slope-along-beta.svg)

**How to read this.** On the left the x-axis is the power and the y-axis $\log Z_\beta$; the dashed line is the tangent at $\beta = 2$. On the right the y-axis is a slope: orange is the slope in $x$ at $x = 5$, solid green the slope of $\log Z_\beta$ along $\beta$, and dotted green its slope along $x$. At $\beta = 2$ read $-1.0$ on the orange line and $-0.25$ on the green curve.

## Why the slope along beta matters

Navigation: ⬅️ [[#The normaliser moves along beta]] | 📋 [[#Table of contents|TOC]] | [[#The slope along beta taught in, applied in]] ➡️

**A method across temperatures needs the ratio.** $Z_\beta$ is invisible to the score in $x$ and changes with $\beta$, so a method that compares a density at two temperatures has to account for the ratio of their normalisers. Here $Z_{2.01}/Z_2 = 0.997509$. Annealed importance sampling, the sitting after this one in the same journey, derives an unbiased estimate of exactly such a ratio of normalisers across $\beta$ (*cited:* the journey's [plan 25](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/25-annealed-importance-sampling.md), lines 24 and 69).

**Scores never see it.** A sampler that follows $\nabla_x \log \pi_\beta$ walks a temperature schedule without this slope, because [[Why The Normaliser Has No Slope In X#A constant has slope 0|a constant has slope 0]] in $x$.

## The slope along beta taught in, applied in

Navigation: ⬅️ [[#Why the slope along beta matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the sampler correctors for composition journey's [plan 24](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/24-what-is-annealed.md), lines 142 to 152 (the temperature score, differentiated "holding the anneal parameter fixed"), through piece 2.2 of the `drip --math` walk in the journey's `drips/24-what-is-annealed/`, "why Z_beta has zero slope", which closed on the one direction in which $Z_\beta$ does move

**Applied in:** no project section yet.

> [!note]- How this was checked
> This section was written on 2026-10-17 on the cluster (mscluster, Linux) as part of [[Why The Normaliser Has No Slope In X]], from piece 2.2 of the same walk, and became its own note on 2026-10-21 when that note passed 400 lines. On 2026-10-21 on the PC (WSL2 Linux) the table's rows, $Z_4/Z_1 = 0.5$, $Z_{2.01}/Z_2 = 0.997509$, and the slip without the $\tfrac{1}{2}$ (2.531024, the log of 12.566371) were printed by `sandbox/normaliser_toy_tables.py` beside this note, run by vault-writer through the prepared environment `~/.vault-sandbox/bin/python` (Python 3.11.13) in the empty folder `~/playground/sandbox/z-slope`, which is not inside any repository. The figure script on the page was run there with matplotlib 3.11.2 and numpy 2.4.6, and its SVG was opened through a PNG copy before filing; the folder was removed afterwards and the clean-up check returned 2. The quotient $-0.2494$ matches the walk's; `zslope.py` prints $-0.249377$ in [[Running Why The Normaliser Has No Slope In X]]. The algebra handbook's page 110 (the logarithm formulas) and the calculus textbook's page 216 (section 3.2, the derivative of $\ln x$) were opened that day with `pdftotext`. Plan 25's lines 24 and 69 were read that day and say what the cited sentence says.
