---
aliases: [normaliser of a tempered density, normalizer of a tempered density, normaliser of a powered density, log Z_beta, Z_beta = sqrt(8 pi / beta)]
---

# Why The Normaliser Has No Slope In X

Up: [[Composition]] · ⬅️ [[The Tempered Density And Its Score]]

Artificial Intelligence, Generative Modeling, Diffusion Models, Composition. Needs: [[The Tempered Density And Its Score]].

> [!question] Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. This note's sections are not in it yet.

> [!warning] Unfinished
> - Prompt 31, the concept picture, is stuck after three revisions and waits for a word from the learner (left-panel curves not one shift apart), in the vault's `.prompts/Diffusion Models.md`.
> - `zslope.py` was run with the system Python in place of the prepared environment; run it once through `~/.vault-sandbox/bin/python` to confirm.

Textbook: [calculus textbook, Theorem 2.3.1, p. 179](../../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=179), and the dummy variable on [p. 392](../../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=392)

**$Z_\beta = \int p(u)^\beta\,du$ is one number for each $\beta$, because the integral uses up its variable $u$ and the point $x$ never enters it; a function that stays the same when $x$ changes has slope 0, so $\nabla_x \log Z_\beta = 0$ and the temperature score is $\beta$ times the score.** Other names for the same fact: $Z_\beta$ has zero slope, the normaliser is constant in the state, the normaliser drops out of the score, the derivative of a constant is 0. [[The Tempered Density And Its Score]] uses it in one line. This subsection says why it holds, checks it on numbers, and shows the one direction in which $Z_\beta$ does move. The plan behind this walk writes the state as $y$; this note writes $x$.

**The integral uses up its variable.** Written with its own letter,

$$
Z_\beta = \int_{-\infty}^{\infty} p(u)^\beta\,du
$$

$u$ runs over the whole real line and is summed away, and what is left is an area: one number. The calculus book calls such a letter a [dummy variable](../../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=392), since it "plays no role in the end result" (*cited*, p. 392). Writing $\int p(x)^\beta\,dx$ gives the same number, and the $x$ inside that integral is not the point where $\pi_\beta$ is evaluated. Only $\beta$ and the shape of $p$ can change the number. *Derived.*

**A constant has slope 0.** The slope of $f$ at $x$ is the limit of the [difference quotient](../../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=167) $\big(f(x + \delta) - f(x)\big)/\delta$ as the step $\delta$ shrinks. When $f(x) = c$ at every $x$,

$$
\frac{f(x + \delta) - f(x)}{\delta} = \frac{c - c}{\delta} = \frac{0}{\delta} = 0 \qquad \text{for every step } \delta \neq 0
$$

so the limit is 0. The calculus book proves its Theorem 2.3.1 the same way (*cited*, p. 179). With $f(x) = \log Z_\beta$:

$$
\begin{aligned}
\nabla_x \log \pi_\beta(x) &= \beta\,\nabla_x \log p(x) - \nabla_x \log Z_\beta \\
&= \beta\,\mathrm{score}(x) - 0
\end{aligned}
$$

*Derived.*

**Worked on $\mathcal{N}(3, 4)$ at $\beta = 2$.** [[The Log Of A Power And Of A Quotient]] found $\log Z_2 = 1.265512$, so $\log \pi_2(x) = -(x - 3)^2/4 - 1.265512$. One step of $\delta = 0.01$ from $x = 5$:

$$
\begin{aligned}
\log \pi_2(5) &= -\frac{2^2}{4} - 1.265512 = -1 - 1.265512 = -2.265512 \\
\log \pi_2(5.01) &= -\frac{2.01^2}{4} - 1.265512 = -1.010025 - 1.265512 = -2.275537 \\
\text{quotient} &= \frac{-2.275537 - (-2.265512)}{0.01} = \frac{-0.010025}{0.01} = -1.0025
\end{aligned}
$$

Without the $Z$ term the two logs are $-1$ and $-1.010025$: the same difference, $-0.010025$, and the same quotient. $\log Z_2$ sits in both values, so it cancels when one is subtracted from the other. The exact slope is $\beta\,\mathrm{score}(5) = 2 \times \big(-(5 - 3)/4\big) = -1.0$. The quotient misses it by the step divided by 4:

$$
\frac{-(2 + \delta)^2/4 - (-2^2/4)}{\delta} = \frac{-(4\delta + \delta^2)/4}{\delta} = -1 - \frac{\delta}{4}
$$

which is $-1.0025$ at $\delta = 0.01$ and $-1.00025$ at $\delta = 0.001$. *Derived*, and *shown* by `zslope.py` in step 9 of [[Three Things Called Annealing#Try the three knobs yourself]], rows 22 to 26 of [[Three Things Called Annealing#Reading the three-knobs output]].

**Worked in two dimensions.** For $h(x_1, x_2) = e^{-(x_1^2 + x_2^2)/2}$, the [exponent rules](../../../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=109) split the powered height into one factor per coordinate, and each factor is a [[Gaussian Integral#The area under the bell|Gaussian integral]] with area $\sqrt{2\pi/\beta}$:

$$
\begin{aligned}
Z_\beta &= \int\!\!\int e^{-\beta (u_1^2 + u_2^2)/2}\,du_1\,du_2 = \sqrt{2\pi/\beta} \times \sqrt{2\pi/\beta} = \frac{2\pi}{\beta} \\
Z_2 &= \pi = 3.141593, \qquad \log Z_2 = 1.144730
\end{aligned}
$$

Both $u_1$ and $u_2$ are used up, so $\log Z_2$ is 1.144730 at $(0, 0)$, at $(1, 2)$ and at every other point, and its gradient is $(0, 0)$. *Derived*, and *shown* by rows 27 and 28.

**Along $\beta$, $Z_\beta$ does move.** For the $\mathcal{N}(3, 4)$ height, $Z_\beta = \sqrt{8\pi/\beta}$, so by the [log rules](../../../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=110) and the [derivative of the log](../../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=216):

$$
\begin{aligned}
\log Z_\beta &= \tfrac{1}{2}\left(\log 8\pi - \log \beta\right) \\
\log Z_2 &= 1.265512, \qquad \log Z_{2.01} = 1.263018 \\
\text{quotient} &= \frac{1.263018 - 1.265512}{0.01} = -0.2494 \\
\frac{d}{d\beta} \log Z_\beta &= -\frac{1}{2\beta} = -0.25 \quad \text{at } \beta = 2
\end{aligned}
$$

*Derived*, and *shown* by rows 29 and 30. $Z_\beta$ is invisible to the score in $x$ and changes with $\beta$, so a method that compares a density at two temperatures has to account for the ratio of their normalisers. Annealed importance sampling, the sitting after this one in the same journey, derives an unbiased estimate of exactly such a ratio of normalisers across $\beta$. *Cited:* the journey's `plans/25-annealed-importance-sampling.md`, lines 24 and 55.

**Why it matters.** Every score-based sampler in this note follows $\nabla_x \log$ of a density it cannot normalise. The normaliser disappears from that slope because it is a number with no $x$ in it, and it reappears the moment a method moves along $\beta$.

*🖼️ Diagram wanted: the concept, $\log \pi_2$ and $\log \pi_2 + \log Z_2$ as two parallel curves with the same secant from $x = 5$ to $x = 5.01$, a flat line for $\log Z_2$ with slope 0, and beside it $\log Z_\beta$ against $\beta$ falling with slope $-0.25$ at $\beta = 2$. Prompt 31 in the same file.*

## Try it yourself

In the folder that steps 1 to 3 of [[Three Things Called Annealing#Try the three knobs yourself]] make, with the same prepared environment, and cleaned up by its last step.

Save this as `zslope.py`. It takes the slope of $\log \pi_2$ at $x = 5$ by a difference quotient with and without $\log Z_2$, computes the two-dimensional $Z_2$ by rectangles at three points that the sum never uses, and takes the slope of $\log Z_\beta$ along $\beta$:

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

Run it with `~/.vault-sandbox/bin/python zslope.py`. This output is from the system `python3`, standard library only:

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

Every field the run prints, read in order.

| # | Field | Expected value | How to read it | Backing |
|---|---|---|---|---|
| 1 | `zslope.py`, `step 0.01`, `log pi` quotient | `-1.002500` | the slope of $\log \pi_2$ at $x = 5$ by one step of 0.01: $\log \pi_2(5) = -2.265512$, $\log \pi_2(5.01) = -2.275537$, difference $-0.010025$ | shown; derived in [[Why The Normaliser Has No Slope In X]] |
| 2 | the `without Z` quotient | `-1.002500` | the same quotient with $\log Z_2$ left out: the constant sits in both values and cancels in the difference | shown; derived there |
| 3 | the `log Z_2` quotient | `0.000000` | $(c - c)/\delta$: the difference quotient of a constant is 0 at every step | shown; derived there |
| 4 | the `step 0.001` quotient | `-1.000250` | a step ten times smaller cuts the miss from 0.0025 to 0.00025: the miss is the step divided by 4 | shown; derived there |
| 5 | `exact beta * score at 5` | `-1.000000` | $2 \times (-(5 - 3)/4)$, the slope both quotients approach | derived there |
| 6 | `log Z_2` at three points | `1.144730` three times | the rectangle sum runs over $u$ and is handed the point without using it, so the value is the same everywhere and its gradient is $(0, 0)$ | shown; derived there |
| 7 | `closed form` | `3.141593` | $2\pi/\beta$ at $\beta = 2$ is $\pi$, matching the rectangle sum | derived there |
| 8 | `slope in beta`, `step 0.01` | `-0.249377` | $\log Z_\beta$ does change with $\beta$: from 1.265512 at $\beta = 2$ to 1.263018 at 2.01 | shown; derived there |
| 9 | `exact -1 / (2 beta)` | `-0.250000` | the exact slope of $\log Z_\beta$ in $\beta$ at $\beta = 2$ | derived there |


> [!note]- How this was checked
> This note was added on 2026-10-17 on the cluster (mscluster, Linux), from piece 2.2 of the same walk, "why Z_beta has zero slope". The cluster still has no `~/.vault-sandbox`, so `zslope.py` was run by the writer with the system `python3` (Python 3.12.10, standard library only) in the empty folder `~/playground/sandbox/z-slope`, which is not inside any repository. It ran in 0.02 seconds; the folder was removed afterwards and the clean-up check returned 2. The script and the output on the page were compared with the files that ran, by script, and both are identical. Every number matched the walk's to the digits it gave: $-2.265512$, $-2.275537$, $-1.0025$, $-1.00025$, $\pi = 3.141593$, $\log \pi = 1.144730$, $\log Z_{2.01} = 1.263018$ and the quotient $-0.2494$ (the run prints $-0.249377$). The output picture was rendered from the captured text by a script in DejaVu Sans Mono with the system `python3` and Matplotlib 3.11.2, never drawn, and opened before filing. The four calculus textbook pages were opened before linking, by reading each page's text stream with a short standard-library script, since the cluster has no PDF reader: page 167 holds Definition 2.2.1 with "the difference quotient", page 179 holds Theorem 2.3.1, "The derivative of a constant function is 0", proved by $(c - c)/h$, page 392 holds "the variable of integration in a definite integral plays no role in the end result, it is often referred to as a dummy variable", and page 216 opens section 3.2, the derivative of $\ln x$. Each got a row in the shelf index's "Pages looked up most". The exponent-rules and log-rules links reuse pages 109 and 110, which this note already links. The standard normal at $\beta = 0.5$ and $\beta = 2$ and the product's powered variances are left out on purpose: the walk holds those answers back for the learner's own check.
