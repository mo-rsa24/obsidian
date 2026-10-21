---
aliases: [zslope.py, running the normaliser slope checks, the normaliser slope sandbox]
sources:
  - "Calculus textbook, the vault's shelf copy, Mathematics/references/textbooks/calculus/calculus-textbook.pdf: Definition 2.2.1, the difference quotient, PDF p. 167"
  - "Algebra handbook, the vault's shelf copy, Mathematics/references/textbooks/algebra/algebra-handbook.pdf: exponent formulas, PDF p. 109"
standard: vault-note v2
---

# Running Why The Normaliser Has No Slope In X

Up: [[Composition]] · ⬅️ [[The Slope Of The Normaliser In Beta]]

Artificial Intelligence, Generative Modeling, Diffusion Models, Composition. Needs: [[Why The Normaliser Has No Slope In X]] and [[The Slope Of The Normaliser In Beta]], the two facts this run checks.

**One script, `zslope.py`, checks on numbers that the normaliser has no slope in $x$ and a real slope in $\beta$.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. This note's sections are not in it yet.

> [!warning]- Unfinished
> - The [diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) does not cover this note's sections yet.

Claims marked stated: 0.

**How the run is read.** Every field is read in [[#Reading the output]], and rows 6 and 7 are worked by hand in [[#Worked in two dimensions]]. The toy numbers and the figures are in [[Why The Normaliser Has No Slope In X]] and [[The Slope Of The Normaliser In Beta]].

**Colours in this note.** <span style="color:#2e7d32">**Green is the normaliser $Z_\beta$**</span>, <span style="color:#ef6c00">**orange is the power $\beta$**</span>, and <span style="color:#6a1b9a">**purple is $u$, the variable the integral uses up**</span>, as in [[Why The Normaliser Has No Slope In X]].

## Try it yourself

Navigation: [[#Reading the output]] ➡️

**Where you work.** In the folder that steps 1 to 3 of [[Three Things Called Annealing#Try the three knobs yourself]] make, with the same prepared environment, and cleaned up by its last step.

**The script.** Save this as `zslope.py`. It takes the slope of $\log \pi_2$ at $x = 5$ by a difference quotient with and without $\log Z_2$, computes the two-dimensional $Z_2$ by rectangles at three points that the sum never uses, and takes the slope of $\log Z_\beta$ along $\beta$:

```python
# Z_beta has no slope in x and a real slope in beta, on the N(3, 4) height and a 2D height.
import math


def log_Z(beta):                                  # log of sqrt(8 pi / beta), the area under the N(3, 4) height to the power beta
    return 0.5 * (math.log(8 * math.pi) - math.log(beta))


def log_pi2(x):                                   # log pi_2(x) = 2 log h(x) - log Z_2
    return -(x - 3) ** 2 / 4 - log_Z(2)


print("slope in x at x = 5, beta = 2: (value at 5 + step - value at 5) / step")
for step in (0.01, 0.001):
    a, b = log_pi2(5), log_pi2(5 + step)
    a0, b0 = -(5 - 3) ** 2 / 4, -(5 + step - 3) ** 2 / 4
    print(f"  step {step:<6}  log pi     {a:.6f}  {b:.6f}  quotient {(b - a) / step:.6f}")
    print(f"               without Z  {a0:.6f}  {b0:.6f}  quotient {(b0 - a0) / step:.6f}")
    print(f"               log Z_2     {log_Z(2):.6f}   {log_Z(2):.6f}  quotient  {(log_Z(2) - log_Z(2)) / step:.6f}")
print(f"  exact beta * score at 5: {2 * (-(5 - 3) / 4):.6f}")

print("2D: Z_2 for exp(-(x1^2 + x2^2)/2) at three points, a rectangle sum against 2 pi / beta")
dx, n = 0.01, 600                                 # squares of side 0.01 from -6 to 6 in each coordinate


def Z2_at(x1, x2):                                # the sum runs over u; x1 and x2 are taken and never used
    row = [math.exp(-2 * (k * dx) ** 2 / 2) for k in range(-n, n + 1)]
    return sum(row) ** 2 * dx * dx                # the powered height splits into one factor per coordinate


for point in ((0, 0), (1, 2), (-3, 0.5)):
    Z = Z2_at(*point)
    print(f"  at {point}: Z_2 {Z:.6f}, log Z_2 {math.log(Z):.6f}")
print(f"  closed form 2 pi / 2 = {2 * math.pi / 2:.6f}, log {math.log(math.pi):.6f}")

print("slope in beta at beta = 2")
for step in (0.01, 0.001):
    print(f"  step {step:<6}  log Z  {log_Z(2):.6f}  {log_Z(2 + step):.6f}  quotient {(log_Z(2 + step) - log_Z(2)) / step:.6f}")
print(f"  exact -1 / (2 beta): {-1 / (2 * 2):.6f}")
```

**Run it** with `~/.vault-sandbox/bin/python zslope.py`. You should see:

```
slope in x at x = 5, beta = 2: (value at 5 + step - value at 5) / step
  step 0.01    log pi     -2.265512  -2.275537  quotient -1.002500
               without Z  -1.000000  -1.010025  quotient -1.002500
               log Z_2     1.265512   1.265512  quotient  0.000000
  step 0.001   log pi     -2.265512  -2.266512  quotient -1.000250
               without Z  -1.000000  -1.001000  quotient -1.000250
               log Z_2     1.265512   1.265512  quotient  0.000000
  exact beta * score at 5: -1.000000
2D: Z_2 for exp(-(x1^2 + x2^2)/2) at three points, a rectangle sum against 2 pi / beta
  at (0, 0): Z_2 3.141593, log Z_2 1.144730
  at (1, 2): Z_2 3.141593, log Z_2 1.144730
  at (-3, 0.5): Z_2 3.141593, log Z_2 1.144730
  closed form 2 pi / 2 = 3.141593, log 1.144730
slope in beta at beta = 2
  step 0.01    log Z  1.265512  1.263018  quotient -0.249377
  step 0.001   log Z  1.265512  1.265262  quotient -0.249938
  exact -1 / (2 beta): -0.250000
```

![The run of zslope.py, with the fields read in rows 1 to 9 of the table below marked on it|900](assets/normaliser-has-no-slope-in-x.png)

## Reading the output

Navigation: ⬅️ [[#Try it yourself]] | [[#Worked in two dimensions]] ➡️

Every field the run prints, read in order.

| # | Field | Expected value | How to read it | Backing |
|---|---|---|---|---|
| 1 | `zslope.py`, `step 0.01`, `log pi` quotient | `-1.002500` | the slope of $\log \pi_2$ at $x = 5$ by one step of 0.01: $\log \pi_2(5) = -2.265512$, $\log \pi_2(5.01) = -2.275537$, difference $-0.010025$ | shown; derived in [[Why The Normaliser Has No Slope In X#A constant has slope 0]] |
| 2 | the `without Z` quotient | `-1.002500` | the same quotient with $\log Z_2$ left out: the constant sits in both values and cancels in the difference | shown; derived there |
| 3 | the `log Z_2` quotient | `0.000000` | $(c - c)/\delta$: the difference quotient of a constant is 0 at every step | shown; derived there |
| 4 | the `step 0.001` quotient | `-1.000250` | a step ten times smaller cuts the miss from 0.0025 to 0.00025: the miss is the step divided by 4 | shown; derived there |
| 5 | `exact beta * score at 5` | `-1.000000` | $2 \times (-(5 - 3)/4)$, the slope both quotients approach | derived in [[Why The Normaliser Has No Slope In X#The normaliser has no slope in x]] |
| 6 | `log Z_2` at three points | `1.144730` three times | the rectangle sum runs over $u$ and is handed the point without using it, so the value is the same everywhere and its gradient is $(0, 0)$ | shown; derived in [[Why The Normaliser Has No Slope In X#The integral uses up its variable]] |
| 7 | `closed form` | `3.141593` | $2\pi/\beta$ at $\beta = 2$ is $\pi$, matching the rectangle sum | derived there |
| 8 | `slope in beta`, `step 0.01` | `-0.249377` | $\log Z_\beta$ does change with $\beta$: from 1.265512 at $\beta = 2$ to 1.263018 at 2.01 | shown; derived in [[The Slope Of The Normaliser In Beta#The normaliser moves along beta]] |
| 9 | `exact -1 / (2 beta)` | `-0.250000` | the exact slope of $\log Z_\beta$ in $\beta$ at $\beta = 2$ | derived there |

## Worked in two dimensions

Navigation: ⬅️ [[#Reading the output]] | [[#The run taught in, applied in]] ➡️

Textbook: [algebra handbook, exponent formulas, p. 109](../../../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=109)

**The same argument with two used-up variables.** For $h(x_1, x_2) = e^{-(x_1^2 + x_2^2)/2}$, the [exponent rules](../../../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=109) split the powered height into one factor per coordinate. Each factor is a [[Gaussian Integral#The area under the bell|Gaussian integral]] with area $\sqrt{2\pi/\beta}$.

$$
\begin{aligned}
Z_\beta &= \int\!\!\int e^{-\beta (u_1^2 + u_2^2)/2}\,du_1\,du_2 = \sqrt{2\pi/\beta} \times \sqrt{2\pi/\beta} = \frac{2\pi}{\beta} \\
Z_2 &= \pi = 3.141593, \qquad \log Z_2 = 1.144730
\end{aligned}
$$

$$
\textcolor{#2e7d32}{Z_2}
=
\underbrace{\int e^{-\textcolor{#ef6c00}{2}\,\textcolor{#6a1b9a}{u_1}^2/2}\,d\textcolor{#6a1b9a}{u_1}}_{\sqrt{2\pi/2} \,=\, 1.772454}
\times
\underbrace{\int e^{-\textcolor{#ef6c00}{2}\,\textcolor{#6a1b9a}{u_2}^2/2}\,d\textcolor{#6a1b9a}{u_2}}_{\sqrt{2\pi/2} \,=\, 1.772454}
=
\pi = 3.141593
$$

**What the equation says.** Both $u_1$ and $u_2$ are used up, so $\log Z_2$ is 1.144730 at $(0, 0)$, at $(1, 2)$ and at every other point. Its gradient is $(0, 0)$. *Derived*, and *shown* by rows 6 and 7 of [[#Reading the output]].

**Why the product of two factors is there.** The exponent rules turn a sum in the exponent into a product of heights, so the double integral is two single ones multiplied. One factor alone is 1.772454, with log 0.572365; the two together give $\pi$, with log 1.144730.

## The run taught in, applied in

Navigation: ⬅️ [[#Worked in two dimensions]]

**Taught in:**

- the sampler correctors for composition journey's [plan 24](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/24-what-is-annealed.md), lines 142 to 152, through piece 2.2 of the `drip --math` walk in the journey's `drips/24-what-is-annealed/`, "why Z_beta has zero slope", which checked the slope on numbers before trusting it

**Applied in:** no project section yet.

> [!note]- How this was checked
> This run was added on 2026-10-17 on the cluster (mscluster, Linux), from piece 2.2 of the same walk, "why Z_beta has zero slope", as part of [[Why The Normaliser Has No Slope In X]], and became its own note on 2026-10-21 when that note passed 400 lines. On the cluster, which has no `~/.vault-sandbox`, `zslope.py` was run by the writer with the system `python3` (Python 3.12.10, standard library only) in the empty folder `~/playground/sandbox/z-slope`, which is not inside any repository; it ran in 0.02 seconds, the folder was removed afterwards and the clean-up check returned 2. On 2026-10-21 on the PC (WSL2 Linux) it was run again by vault-writer through the prepared environment `~/.vault-sandbox/bin/python` (Python 3.11.13) in a fresh empty `~/playground/sandbox/z-slope`; the script and the output on the page were compared with the files that ran, by script, and both are identical. Every number matched the walk's to the digits it gave: $-2.265512$, $-2.275537$, $-1.0025$, $-1.00025$, $\pi = 3.141593$, $\log \pi = 1.144730$, $\log Z_{2.01} = 1.263018$ and the quotient $-0.2494$ (the run prints $-0.249377$). The output picture was rendered on 2026-10-17 from the captured text by a script in DejaVu Sans Mono with Matplotlib 3.11.2, never drawn, and opened before filing; the output it shows is identical to the 2026-10-21 run. The four calculus pages behind the readings (167, 179, 216 and 392) were opened with `pdftotext` on 2026-10-21, and each got a row in the shelf index's "Pages looked up most" on 2026-10-17; the algebra handbook's page 109 (the exponent formulas) was opened the same way. The single factor 1.772454 and its log 0.572365 in [[#Worked in two dimensions]] were printed by `sandbox/normaliser_toy_tables.py` beside this note, run that day in the same folder through the same environment.
