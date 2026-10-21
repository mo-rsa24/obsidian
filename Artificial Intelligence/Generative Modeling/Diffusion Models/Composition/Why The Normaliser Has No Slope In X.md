---
aliases: [normaliser of a tempered density, normalizer of a tempered density, normaliser of a powered density, log Z_beta, Z_beta = sqrt(8 pi / beta)]
sources:
  - "Calculus textbook, the vault's shelf copy, Mathematics/references/textbooks/calculus/calculus-textbook.pdf: Definition 2.2.1, the difference quotient, PDF p. 167; Theorem 2.3.1, the derivative of a constant, PDF p. 179; the dummy variable of a definite integral, PDF p. 392"
standard: vault-note v2
---

# Why The Normaliser Has No Slope In X

Up: [[Composition]] · ⬅️ [[The Tempered Density And Its Score]] · [[The Slope Of The Normaliser In Beta]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models, Composition. Needs: [[The Tempered Density And Its Score]].

**The normaliser $Z_\beta$ is one number for each $\beta$, so its slope in $x$ is 0 and the tempered score is $\beta$ times the score.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. This note's sections are not in it yet.

> [!warning]- Unfinished
> - The [diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) does not cover this note's sections yet.

Claims marked stated: 0.

**Other names for the same fact.** $Z_\beta$ has zero slope, the normaliser is constant in the state, the normaliser drops out of the score, the derivative of a constant is 0.

**Where it is used.** [[The Tempered Density And Its Score]] uses it in one line. This note says why it holds and checks it on numbers. [[The Slope Of The Normaliser In Beta]] shows the one direction in which $Z_\beta$ does move, and [[Running Why The Normaliser Has No Slope In X]] runs the script that checks both.

**A change of letter.** The plan behind this walk writes the state as $y$; this note writes $x$.

**Colours in this note.** <span style="color:#1565c0">**Blue is the point $x$ and the tempered log density $\log \pi_\beta(x)$**</span>, <span style="color:#757575">**grey is the log height without the normaliser, $\beta \log p(x)$**</span>, <span style="color:#2e7d32">**green is the normaliser $Z_\beta$ and its log**</span>, <span style="color:#ef6c00">**orange is the power $\beta$**</span>, <span style="color:#6a1b9a">**purple is $u$, the variable the integral uses up**</span>, and <span style="color:#827717">**olive is the step $\delta$**</span>.

## Table of contents

- [[#The normaliser has no slope in x]]
- [[#The integral uses up its variable]]
- [[#A constant has slope 0]]
- [[#The normaliser moves along beta]]
- [[#Try it yourself]]
- [[#Why the normaliser matters]]
- [[#The normaliser taught in, applied in]]

## The normaliser has no slope in x

Navigation: 📋 [[#Table of contents|TOC]] | [[#The integral uses up its variable]] ➡️

Textbook: [calculus textbook, Theorem 2.3.1, p. 179](../../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=179), and the dummy variable on [p. 392](../../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=392)

**Normaliser has no slope in x**, also the normaliser drops out of the score: $Z_\beta = \int p(u)^\beta\,du$ is one number for each $\beta$, because the integral uses up its variable $u$ and the point $x$ never enters it. A function that stays the same when $x$ changes has slope 0, so $\nabla_x \log Z_\beta = 0$ and the temperature score is $\beta$ times the score. *Derived* in the next two sections.

**The toy numbers.** Every example uses the $\mathcal{N}(3, 4)$ height $p(x) = e^{-(x - 3)^2/8}$, the bell without its front factor, at $\beta = 2$. [[The Log Of A Power And Of A Quotient]] found $\log Z_2 = 1.265512$, so $\log \pi_2(x) = -(x - 3)^2/4 - 1.265512$.

<table>
<tr><th>point <i style="color:#1565c0">x</i></th><th style="color:#757575">without <i>Z</i>: −(<i>x</i> − 3)²/4</th><th style="color:#2e7d32">log <i>Z</i><sub>2</sub></th><th style="color:#1565c0">log π<sub>2</sub>(<i>x</i>)</th><th>gap between the two</th></tr>
<tr><td>3</td><td>0.000000</td><td>1.265512</td><td>−1.265512</td><td>1.265512</td></tr>
<tr style="background:#fff8e1"><td><b>5</b></td><td style="border:2px solid #212121"><b>−1.000000</b></td><td style="border:2px solid #212121"><b>1.265512</b></td><td style="border:2px solid #212121"><b>−2.265512</b></td><td><b>1.265512</b></td></tr>
<tr><td>5.01</td><td style="border:2px dashed #212121">−1.010025</td><td style="border:2px dashed #212121">1.265512</td><td style="border:2px dashed #212121">−2.275537</td><td>1.265512</td></tr>
<tr><td>7</td><td>−4.000000</td><td>1.265512</td><td>−5.265512</td><td>1.265512</td></tr>
</table>

**How to read this table.** Each row is one point $x$. Grey is twice the log height, green is the log normaliser, and blue is grey minus green, the tempered log density.

**What to look for.** The green column never changes, so the gap between grey and blue is 1.265512 on every row. The highlighted row and the dashed row below it are the two values the slope at $x = 5$ is taken from in [[#A constant has slope 0]].

$$
\begin{aligned}
\nabla_x \log \pi_\beta(x) &= \beta\,\nabla_x \log p(x) - \nabla_x \log Z_\beta \\
&= \beta\,\mathrm{score}(x) - 0
\end{aligned}
$$

$$
\underbrace{\nabla_{\textcolor{#1565c0}{x}} \log \pi_{\textcolor{#ef6c00}{\beta}}(\textcolor{#1565c0}{x})}_{\text{the tempered score}}
=
\underbrace{\textcolor{#ef6c00}{\beta}\,\nabla_{\textcolor{#1565c0}{x}} \log p(\textcolor{#1565c0}{x})}_{\beta \text{ times the score}}
-
\underbrace{\nabla_{\textcolor{#1565c0}{x}} \log \textcolor{#2e7d32}{Z_{\beta}}}_{\text{the slope of one number: } 0}
$$

**What the equation says.** The slope in $x$ of the tempered log density is $\beta$ times the slope of the log height, minus the slope of $\log Z_\beta$. The last slope is 0, so only the first term is left. *Derived.*

**Why the $\beta$ is there.** The power becomes a multiplier on the log. At $x = 5$ the score is $-(5 - 3)/4 = -0.5$; with $\beta = 2$ the tempered score is $-1.0$, and without it the slope would be $-0.5$, the slope of the untempered log height.

**Why the minus $\log Z_\beta$ is there.** It makes $\pi_2$ a density: the area under $p^2$ is 3.544908 before dividing by $Z_2$ and 1.000000 after. Its slope term is 0, so the tempered score is $-1.0$ with it or without it.

```python
import numpy as np
import matplotlib.pyplot as plt

BLUE, GREY, GREEN = "#1565c0", "#757575", "#2e7d32"
logZ2 = 0.5 * (np.log(8 * np.pi) - np.log(2))                  # 1.265512
x = np.linspace(2, 7.5, 400)
fig, (left, right) = plt.subplots(1, 2, figsize=(12, 4.8))
left.plot(x, -(x - 3) ** 2 / 4, color=GREY, lw=2)
left.plot(x, -(x - 3) ** 2 / 4 - logZ2, color=BLUE, lw=2.5)
left.axhline(logZ2, color=GREEN, lw=2)
left.text(2.1, logZ2 + 0.25, f"log Z₂ = {logZ2:.6f}, slope 0", color=GREEN, fontsize=11)
left.text(5.75, -1.2, "without Z:\n−(x − 3)²/4", color=GREY, fontsize=11)
left.text(2.1, -2.9, "log π₂(x)", color=BLUE, fontsize=12)
for xb in (3, 5, 7):                                            # the gap is the same at every x
    top = -(xb - 3) ** 2 / 4
    left.annotate("", (xb, top - logZ2), (xb, top), arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.5))
    left.text(xb - 0.08, top - logZ2 / 2, f"{logZ2:.6f}", color=GREEN, fontsize=9, va="center", ha="right",
              bbox=dict(fc="white", ec="none", pad=0.5))
left.plot(5, -1 - logZ2, "o", color=BLUE)
left.annotate("x = 5: −2.265512,\nslope −1.0 on both curves", (5, -1 - logZ2), (2.2, -5.6), color=BLUE,
              fontsize=10, arrowprops=dict(arrowstyle="->", color=BLUE))
left.set(xlim=(2, 7.5), ylim=(-7, 2), xlabel="the point x", ylabel="log height")
left.set_title("in x: Z is one number", fontsize=12)
right.plot(x, -(x - 3) / 2, color=BLUE, lw=4, alpha=0.5)
right.plot(x, -(x - 3) / 2, color=GREY, lw=1.5, ls="--")
right.axhline(0, color=GREEN, lw=2)
right.plot(5, -1, "o", color=BLUE)
right.text(5.15, -0.9, "x = 5: β · score = −1.0", color=BLUE, fontsize=10)
right.text(2.1, 0.12, "slope of log Z₂ in x: 0 everywhere", color=GREEN, fontsize=11)
right.text(5.6, -1.75, "slope of both curves:\n−(x − 3)/2, one line", color=BLUE, fontsize=10)
right.set(xlim=(2, 7.5), ylim=(-2.5, 0.8), xlabel="the point x", ylabel="slope in x")
right.set_title("the slopes: Z adds nothing", fontsize=12)
fig.savefig("normaliser-has-no-slope-in-x-the-gap-is-the-same-everywhere.svg", format="svg", bbox_inches="tight")
```

![Left, the grey log height and the blue log pi_2 as two parabolas peaking at x = 3, held 1.265512 apart by green brackets at x = 3, 5 and 7, under a flat green line at log Z_2 = 1.265512; right, the slope in x of both curves as one line -(x - 3)/2 through -1.0 at x = 5, and the green slope of log Z_2 at 0 everywhere|800](assets/normaliser-has-no-slope-in-x-the-gap-is-the-same-everywhere.svg)

**How to read this.** On the left the x-axis is the point and the y-axis a log height; each curve is one function of $x$. The three green brackets are the same length, 1.265512, so blue is grey slid down by one number. On the right the y-axis is the slope in $x$: both curves share the line $-(x - 3)/2$, through $-1.0$ at $x = 5$, and $\log Z_2$'s slope is the flat green line at 0.

**Why this matters.** A score-based sampler can follow $\nabla_x \log \pi_\beta$ at any $\beta$ without computing an area.

## The integral uses up its variable

Navigation: ⬅️ [[#The normaliser has no slope in x]] | 📋 [[#Table of contents|TOC]] | [[#A constant has slope 0]] ➡️

Textbook: [calculus textbook, the dummy variable, p. 392](../../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=392)

### The base word: variable

**What the word means.** A variable is a letter that stands for any value in a range. In $Z_\beta$ the letter $u$ ranges over the whole real line.

$$
\underbrace{\textcolor{#6a1b9a}{u}}_{\text{any value in } (-\infty,\ \infty)}
$$

### The qualifier: dummy

**What the word means.** The calculus book calls the letter of a definite integral a [dummy variable](../../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=392), since it "plays no role in the end result" (*cited*, p. 392). Renaming it gives the same number.

$$
\int p(\textcolor{#6a1b9a}{u})^{\beta}\,d\textcolor{#6a1b9a}{u}
\;=\;
\underbrace{\int p(x)^{\beta}\,dx}_{\text{the same number}}
$$

**What it means.** The $x$ inside that second integral is not the point where $\pi_\beta$ is evaluated. It is the same running letter under another name.

### All the words together: the integral

$$
Z_\beta = \int_{-\infty}^{\infty} p(u)^\beta\,du
$$

$$
\underbrace{\textcolor{#2e7d32}{Z_{\textcolor{#ef6c00}{\beta}}}}_{\text{one number per } \beta}
=
\underbrace{\int_{-\infty}^{\infty}}_{\text{add over every } u}
\underbrace{p(\textcolor{#6a1b9a}{u})^{\textcolor{#ef6c00}{\beta}}}_{\text{height to the power } \beta}
\,\underbrace{d\textcolor{#6a1b9a}{u}}_{\text{width}}
$$

**What the equation says.** $u$ runs over the whole real line and is summed away, and what is left is an area: one number. Only $\beta$ and the shape of $p$ can change the number. *Derived.*

**Why the integral is there.** It turns a curve into a number. Without it, $p(u)^2$ is a different height at each $u$, 1 at $u = 3$ and $e^{-1} = 0.367879$ at $u = 5$; with it, rectangles of width 0.01 add to 3.544908, which is $\sqrt{8\pi/2}$.

**Why the power $\beta$ is there.** It is the only input that moves the number. At $\beta = 1$, 2 and 4 the area is 5.013257, 3.544908 and 2.506628.

### The consequence: one number for each beta

<table>
<tr><th>point <i style="color:#1565c0">x</i> handed in</th><th style="color:#ef6c00">power β</th><th style="color:#2e7d32"><i>Z</i><sub>β</sub> by rectangles</th><th>√(8π/β)</th><th style="color:#2e7d32">log <i>Z</i><sub>β</sub></th></tr>
<tr><td>0</td><td>2</td><td style="border:2px solid #212121">3.544908</td><td>3.544908</td><td>1.265512</td></tr>
<tr style="background:#fff8e1"><td><b>5</b></td><td><b>2</b></td><td style="border:2px solid #212121"><b>3.544908</b></td><td><b>3.544908</b></td><td><b>1.265512</b></td></tr>
<tr><td>7</td><td>2</td><td style="border:2px solid #212121">3.544908</td><td>3.544908</td><td>1.265512</td></tr>
<tr><td>5</td><td>1</td><td style="border:2px dashed #212121">5.013257</td><td>5.013257</td><td>1.612086</td></tr>
<tr><td>5</td><td>4</td><td style="border:2px dashed #212121">2.506628</td><td>2.506628</td><td>0.918939</td></tr>
</table>

**How to read this table.** Each row hands a rectangle sum over $u$ (width 0.01, from $-17$ to 23) a point $x$ and a power $\beta$. The sum takes $x$ and never uses it. The fourth column is the closed form.

**What to look for.** The three boxed rows change $x$ and print the same 3.544908. The two dashed rows change $\beta$ and print new numbers, so $Z_\beta$ is a function of $\beta$ alone.

$$
\textcolor{#2e7d32}{Z_2}\big|_{\textcolor{#1565c0}{x} = 0}
=
\textcolor{#2e7d32}{Z_2}\big|_{\textcolor{#1565c0}{x} = 5}
=
\textcolor{#2e7d32}{Z_2}\big|_{\textcolor{#1565c0}{x} = 7}
=
\underbrace{3.544908}_{\text{no } x \text{ in it}}
$$

**What it means.** A quantity that prints the same number at every $x$ has a [[#A constant has slope 0|slope of 0]] in $x$.

**Two dimensions.** The same holds with two used-up variables: for $e^{-(x_1^2 + x_2^2)/2}$ at $\beta = 2$, $Z_2 = \pi = 3.141593$ at every point, worked in [[Running Why The Normaliser Has No Slope In X#Worked in two dimensions]].

```python
import numpy as np
import matplotlib.pyplot as plt

PURPLE, GREEN, GREY, ORANGE = "#6a1b9a", "#2e7d32", "#9e9e9e", "#ef6c00"
u = -17 + 0.01 * np.arange(4001)                                 # the rectangles: width 0.01 from -17 to 23
h = np.exp(-(u - 3) ** 2 / 8)                                    # the N(3, 4) height
def Z_by_rectangles(x, beta):                                    # x is handed in and never used
    return np.sum(h ** beta) * 0.01
fig, (left, right) = plt.subplots(1, 2, figsize=(12, 4.6))
for beta, col in ((1, GREY), (2, GREEN), (4, GREY)):
    left.plot(u, h ** beta, color=col, lw=2 if beta == 2 else 1.2)
left.fill_between(u, h ** 2, color=GREEN, alpha=0.18)
left.text(3, 0.45, f"β = 2: area {Z_by_rectangles(5, 2):.6f} = Z₂", color=GREEN, fontsize=11, ha="center")
left.text(5.6, 0.75, f"β = 1: area {Z_by_rectangles(5, 1):.6f}", color="#616161", fontsize=10)
left.text(5.0, 0.93, f"β = 4: area {Z_by_rectangles(5, 4):.6f}", color="#616161", fontsize=10)
left.set(xlim=(-5, 11), ylim=(0, 1.08), xlabel="u, the variable the integral uses up", ylabel="height to the power β")
left.xaxis.label.set_color(PURPLE)
left.set_title("the area adds over every u", fontsize=12)
xs = np.arange(-2, 9)
for beta, col in ((1, "#616161"), (2, GREEN), (4, "#616161")):
    Zs = [Z_by_rectangles(x, beta) for x in xs]
    right.plot(xs, Zs, "o-", color=col, lw=1.5)
    right.text(8.3, Zs[-1], f"β = {beta}: {Zs[-1]:.6f}", color=col, fontsize=10, va="center")
right.set(xlim=(-2.5, 11.5), ylim=(2, 5.6), xlabel="the point x handed in", ylabel="Z of β, by rectangles")
right.set_title("handed any x, the same number; changed β, a new one", fontsize=12)
fig.savefig("normaliser-has-no-slope-in-x-the-area-has-no-x.svg", format="svg", bbox_inches="tight")
```

![Left, the N(3, 4) height raised to the powers 1, 2 and 4 against u, with the green area under the square shaded and labelled 3.544908 = Z_2, and the other two areas 5.013257 and 2.506628; right, the rectangle sum handed every whole x from -2 to 8 gives three flat rows of dots at 5.013257, 3.544908 and 2.506628|800](assets/normaliser-has-no-slope-in-x-the-area-has-no-x.svg)

**How to read this.** On the left the x-axis is $u$, the running letter, and the y-axis is the height to the power $\beta$; each area under a curve is one $Z_\beta$. On the right the x-axis is the point $x$ handed to the sum and the y-axis the sum it returns. Look at the green row: eleven points, one number, 3.544908.

**Why this matters.** The argument used nothing about the shape of $p$ or the number of coordinates, so it holds for any normaliser that integrates the state away. *Derived.*

## A constant has slope 0

Navigation: ⬅️ [[#The integral uses up its variable]] | 📋 [[#Table of contents|TOC]] | [[#The normaliser moves along beta]] ➡️

Textbook: [calculus textbook, Definition 2.2.1, the difference quotient, p. 167](../../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=167), and Theorem 2.3.1 on [p. 179](../../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=179)

### The base word: quotient

**What the word means.** A quotient is one number divided by another. Here the top is a change in height and the bottom a change in position.

$$
\underbrace{\frac{-0.010025}{0.01}}_{\text{rise over run}} = -1.0025
$$

### The qualifier: difference

**What the word means.** The top is a difference: the value after a step minus the value before it. At $x = 5$ with a step of 0.01, that is $-2.275537 - (-2.265512) = -0.010025$.

$$
\underbrace{f(\textcolor{#1565c0}{x} + \textcolor{#827717}{\delta}) - f(\textcolor{#1565c0}{x})}_{\text{after the step, minus before}}
$$

### All the words together: the quotient

The slope of $f$ at $x$ is the limit of the [difference quotient](../../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=167) as the step $\delta$ shrinks.

$$
\frac{f(x + \delta) - f(x)}{\delta}
$$

$$
\underbrace{\frac{f(\textcolor{#1565c0}{x} + \textcolor{#827717}{\delta}) - f(\textcolor{#1565c0}{x})}{\textcolor{#827717}{\delta}}}_{\text{rise over a run of } \delta}
\;\xrightarrow{\ \delta \to 0\ }\;
\underbrace{\text{the slope at } \textcolor{#1565c0}{x}}_{-1.0 \text{ for } \log \pi_2 \text{ at } 5}
$$

**What the equation says.** Step from $x$ by $\delta$, take the change in height, and divide by $\delta$. As the step shrinks the quotient closes on one number, the slope.

**Why the divisor $\delta$ is there.** It turns a change into a rate. Undivided, the change at $x = 5$ is $-0.010025$ at a step of 0.01 and $-0.001000$ at 0.001, shrinking to 0 with the step; divided, it is $-1.0025$ and $-1.00025$, closing on $-1$.

### The consequence: a constant's quotient is 0

When $f(x) = c$ at every $x$,

$$
\frac{f(x + \delta) - f(x)}{\delta} = \frac{c - c}{\delta} = \frac{0}{\delta} = 0 \qquad \text{for every step } \delta \neq 0
$$

$$
\frac{\overbrace{\textcolor{#2e7d32}{c}}^{\text{after}} - \overbrace{\textcolor{#2e7d32}{c}}^{\text{before}}}{\textcolor{#827717}{\delta}}
=
\underbrace{\frac{0}{\textcolor{#827717}{\delta}}}_{\text{no rise at any run}}
= 0
$$

**What the equation says.** A constant has the same value after the step as before, so the rise is 0 and every quotient is 0. The limit is 0, which the calculus book proves the same way as its Theorem 2.3.1 (*cited*, p. 179). With $f(x) = \log Z_\beta$ this is the 0 in [[#The normaliser has no slope in x|the tempered score]]. *Derived.*

**Worked on $\mathcal{N}(3, 4)$ at $\beta = 2$.** One step of $\delta = 0.01$ from $x = 5$:

$$
\begin{aligned}
\log \pi_2(5) &= -\frac{2^2}{4} - 1.265512 = -1 - 1.265512 = -2.265512 \\
\log \pi_2(5.01) &= -\frac{2.01^2}{4} - 1.265512 = -1.010025 - 1.265512 = -2.275537 \\
\text{quotient} &= \frac{-2.275537 - (-2.265512)}{0.01} = \frac{-0.010025}{0.01} = -1.0025
\end{aligned}
$$

**Why $\log Z_2$ cancels.** Without the $Z$ term the two logs are $-1$ and $-1.010025$: the same difference, $-0.010025$, and the same quotient. $\log Z_2$ sits in both values, so it cancels when one is subtracted from the other.

**The miss shrinks with the step.** The exact slope is $\beta\,\mathrm{score}(5) = 2 \times \big(-(5 - 3)/4\big) = -1.0$. The quotient misses it by the step divided by 4:

$$
\frac{-(2 + \delta)^2/4 - (-2^2/4)}{\delta} = \frac{-(4\delta + \delta^2)/4}{\delta} = -1 - \frac{\delta}{4}
$$

$$
\frac{-(2 + \textcolor{#827717}{\delta})^2/4 - (-2^2/4)}{\textcolor{#827717}{\delta}}
=
\underbrace{-1}_{\beta\,\mathrm{score}(5)}
\;
\underbrace{-\,\frac{\textcolor{#827717}{\delta}}{4}}_{\text{the miss}}
$$

**Why the $\delta/4$ is there.** Squaring $2 + \delta$ leaves a $\delta^2$, and $\delta^2/4$ divided by $\delta$ is $\delta/4$. It is $-1.25$ at $\delta = 1$, $-1.0025$ at 0.01 and $-1.00025$ at 0.001. *Derived*, and *shown* by `zslope.py` in [[Running Why The Normaliser Has No Slope In X#Try it yourself]], rows 1 to 5 of [[Running Why The Normaliser Has No Slope In X#Reading the output|its output]].

<table>
<tr><th>step <i style="color:#827717">δ</i></th><th style="color:#1565c0">log π<sub>2</sub>(5 + <i>δ</i>)</th><th>difference</th><th style="color:#1565c0">quotient</th><th style="color:#757575">quotient without <i>Z</i></th><th style="color:#2e7d32">quotient of log <i>Z</i><sub>2</sub></th><th>−1 − <i>δ</i>/4</th></tr>
<tr><td>1</td><td>−3.515512</td><td>−1.250000</td><td>−1.250000</td><td>−1.250000</td><td>0.000000</td><td>−1.250000</td></tr>
<tr><td>0.1</td><td>−2.368012</td><td>−0.102500</td><td>−1.025000</td><td>−1.025000</td><td>0.000000</td><td>−1.025000</td></tr>
<tr style="background:#fff8e1"><td><b>0.01</b></td><td><b>−2.275537</b></td><td><b>−0.010025</b></td><td style="border:2px solid #212121"><b>−1.002500</b></td><td style="border:2px solid #212121"><b>−1.002500</b></td><td style="border:2px solid #212121"><b>0.000000</b></td><td><b>−1.002500</b></td></tr>
<tr><td>0.001</td><td>−2.266512</td><td>−0.001000</td><td>−1.000250</td><td>−1.000250</td><td>0.000000</td><td>−1.000250</td></tr>
</table>

**How to read this table.** Each row is one step from $x = 5$. The three quotient columns are the slopes of the tempered log density, of the log height without $Z$, and of $\log Z_2$ alone.

**What to look for.** In the highlighted row the first two boxed quotients agree to every digit and the third is 0. Down the rows the quotient closes on $-1$, matching the last column at every step.

```python
import numpy as np
import matplotlib.pyplot as plt

BLUE, GREY, GREEN, OLIVE = "#1565c0", "#757575", "#2e7d32", "#827717"
logZ2 = 0.5 * (np.log(8 * np.pi) - np.log(2))
x = np.linspace(3.8, 6.4, 300)
fig, (left, right) = plt.subplots(1, 2, figsize=(12, 4.6))
for off, col, name in ((0, GREY, "without Z"), (logZ2, BLUE, "log π₂(x)")):
    left.plot(x, -(x - 3) ** 2 / 4 - off, color=col, lw=2)
    left.plot([5, 6], [-1 - off, -2.25 - off], "o-", color=OLIVE, lw=2)    # one step of 1 from x = 5
    left.text(3.85, -0.6 - off, name, color=col, fontsize=11)
    left.text(5.55, -1.3 - off, "quotient −1.25", color=OLIVE, fontsize=10)
left.set(xlim=(3.8, 6.4), ylim=(-4.4, 0.2), xlabel="the point x", ylabel="log height")
left.set_title("a step of δ = 1 from x = 5: the same rise over run", fontsize=12)
steps = np.array([1, 0.1, 0.01, 0.001])
q = -1 - steps / 4                                               # the quotient of either curve
right.semilogx(steps, q, "o-", color=BLUE, lw=2)
right.semilogx(steps, 0 * steps, "o-", color=GREEN, lw=2)
right.axhline(-1, color=BLUE, ls="--", lw=1)
for s, v in zip(steps, q):
    right.text(s, v - 0.08, f"{v:.5f}", color=BLUE, fontsize=9, ha="center", va="top")
right.text(0.8, 0.05, "log Z₂: (c − c)/δ = 0 at every step", color=GREEN, fontsize=11)
right.text(0.8, -0.93, "exact: β · score(5) = −1.0", color=BLUE, fontsize=10)
right.set(xlim=(1.6, 0.0006), ylim=(-1.45, 0.2), xlabel="the step δ, shrinking to the right", ylabel="difference quotient")
right.set_title("the quotient closes on −1; the constant's stays 0", fontsize=12)
fig.savefig("normaliser-has-no-slope-in-x-the-difference-quotient.svg", format="svg", bbox_inches="tight")
```

![Left, an olive step of 1 from x = 5 on the grey log height and on the blue log pi_2, two parallel chords each with quotient -1.25; right, the quotient against the step on a log axis, blue dots at -1.25, -1.025, -1.0025 and -1.00025 closing on the dashed line at -1, and green dots for log Z_2 at 0 at every step|800](assets/normaliser-has-no-slope-in-x-the-difference-quotient.svg)

**How to read this.** On the left the x-axis is the point and the y-axis a log height; each olive chord is one step of $\delta = 1$, and the two chords are parallel because the curves differ by a constant. On the right the x-axis is the step, shrinking to the right on a log scale, and the y-axis the quotient. Look at the blue dots closing on $-1$ while the green ones sit on 0 at every step.

**Why this matters.** The difference quotient checks a slope with no calculus, and a constant's quotient is 0 at every step, before any limit is taken.

## The normaliser moves along beta

Navigation: ⬅️ [[#A constant has slope 0]] | 📋 [[#Table of contents|TOC]] | [[#Try it yourself]] ➡️

**In two lines.** Along the power, $Z_\beta$ does move: for the $\mathcal{N}(3, 4)$ height $\log Z_\beta = \tfrac{1}{2}(\log 8\pi - \log \beta)$, which falls with slope $-1/(2\beta) = -0.25$ at $\beta = 2$. [[The Slope Of The Normaliser In Beta#The normaliser moves along beta]] derives it, checks it on a table and a figure, and says why a method across temperatures needs the ratio of normalisers.

## Try it yourself

Navigation: ⬅️ [[#The normaliser moves along beta]] | 📋 [[#Table of contents|TOC]] | [[#Why the normaliser matters]] ➡️

**In two lines.** `zslope.py` checks every slope in this note and in [[The Slope Of The Normaliser In Beta]] by difference quotients, run in the folder that steps 1 to 3 of [[Three Things Called Annealing#Try the three knobs yourself]] make. The script, its output and the output read field by field are in [[Running Why The Normaliser Has No Slope In X#Try it yourself]].

## Why the normaliser matters

Navigation: ⬅️ [[#Try it yourself]] | 📋 [[#Table of contents|TOC]] | [[#The normaliser taught in, applied in]] ➡️

**Scores never need it.** Every score-based sampler in this note follows $\nabla_x \log$ of a density it cannot normalise. The normaliser disappears from that slope because it is a number with no $x$ in it.

**Temperatures do.** It reappears the moment a method moves along $\beta$, as the ratio [[The Slope Of The Normaliser In Beta#Why the slope along beta matters|of two normalisers]].

## The normaliser taught in, applied in

Navigation: ⬅️ [[#Why the normaliser matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the sampler correctors for composition journey's [plan 24](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/24-what-is-annealed.md), lines 142 to 152 (the temperature score, and "The normaliser has no state dependence, so its derivative vanishes"), through piece 2.2 of the `drip --math` walk in the journey's `drips/24-what-is-annealed/`, "why Z_beta has zero slope"

**Applied in:** no project section yet.

> [!note]- How this was checked
> This note was added on 2026-10-17 on the cluster (mscluster, Linux), from piece 2.2 of the same walk, "why Z_beta has zero slope"; how `zslope.py` was run is in [[Running Why The Normaliser Has No Slope In X]]. On 2026-10-21 on the PC (WSL2 Linux) the three toy tables and every worked move in this note ($e^{-1} = 0.367879$, the areas 5.013257, 3.544908 and 2.506628, and the area 1.000000 after dividing by $Z_2$) were printed by `sandbox/normaliser_toy_tables.py` beside this note, run by vault-writer through the prepared environment `~/.vault-sandbox/bin/python` (Python 3.11.13) in the empty folder `~/playground/sandbox/z-slope`, which is not inside any repository. The three figure scripts on the page were run there with matplotlib 3.11.2 and numpy 2.4.6, and each SVG was opened through a PNG copy before filing; the folder was removed afterwards and the clean-up check returned 2. The textbook pages were opened that day with `pdftotext`: calculus page 167 holds Definition 2.2.1 with "the difference quotient", page 179 holds Theorem 2.3.1, "The derivative of a constant function is 0", proved by $(c - c)/h$, and page 392 holds "the variable of integration in a definite integral plays no role in the end result, it is often referred to as a dummy variable". The standard normal at $\beta = 0.5$ and $\beta = 2$ and the product's powered variances are left out on purpose: the walk holds those answers back for the learner's own check.
