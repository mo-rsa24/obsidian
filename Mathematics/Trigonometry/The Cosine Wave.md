---
aliases: [cosine wave, the cosine wave, graph of cosine, cosine graph, cos squared, "cos^2", "cos²θ", square of the cosine, Pythagorean identity, "cos^2 + sin^2 = 1", "cos²θ + sin²θ = 1", the two shares, quarter turn of the cosine, where cos squared is flat, slope of cos squared, "d/dθ cos²θ = −2 cos θ sin θ", "−sin 2θ", period of the cosine, "cos(θ + 2π) = cos θ", double angle in the slope, "sin 2θ = 2 sin θ cos θ", drop the square, cosine without the square]
sources:
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Trigonometry, version 2.4: the Pythagorean identities, PDF p. 9; graphs of the parent functions, cosine as a wave, PDF p. 16; period 2π, PDF p. 17; double angle formulas, sin 2θ = 2 sin θ cos θ, PDF p. 37: ../references/textbooks/trigonometry/trigonometry-handbook.pdf"
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Geometry, the Pythagorean theorem, PDF p. 80: ../references/textbooks/geometry/geometry-handbook.pdf#page=80"
  - "Nichol, Dhariwal, Improved Denoising Diffusion Probabilistic Models, ICML 2021, section 3.2, PDF p. 4: https://arxiv.org/pdf/2102.09672#page=4"
  - "Anton, Bivens, Davis, Calculus, section 2.5 (derivatives of sine and cosine, x in radians), PDF p. 193, and section 2.6 (the chain rule), PDF p. 198: ../references/textbooks/calculus/calculus-textbook.pdf"
standard: vault-note v2
---

# The Cosine Wave

Up: [[Trigonometry]] · ⬅️ [[Radians]] · [[How The Cosine Wave Works]] ➡️

Mathematics, Trigonometry. Needs: [[The Unit Circle#The circle: every point at distance 1|the unit circle]] for the cosine as the point's x-coordinate, and [[Radians#Then the conversion: degrees to radians|radians]] for the angle as a length.

**The cosine wave is the point's x-coordinate on the unit circle, plotted against the angle.**

> [!question]- Test yourself
> No quiz page covers this note yet.

> [!warning]- Unfinished
> - No quiz page for this note yet.

Stated claims: 0.

**Its square is a share.** $\cos^2\theta$ is the part of 1 that the horizontal leg holds, and $\sin^2\theta$ holds the rest.

**The stretch the schedule uses.** Over the quarter turn from 0 to π/2 that share falls from 1 to 0, slowly at both ends and fastest in the middle. The cosine schedule is built on exactly that stretch.

**The toy angle.** Every worked number is at 46.25°, which is 0.8072 rad, the angle of post 51 in [[The Quarter Circle Under The Cosine Schedule]], as in [[The Unit Circle]].

**Colours, as in The Unit Circle and Radians.** <span style="color:#2e7d32">**Green is $\cos\theta$ and its square $\cos^2\theta$**</span>, <span style="color:#ef6c00">**orange is $\sin\theta$ and its square**</span>, <span style="color:#1565c0">**blue is the angle: the quarter turn, its 15° steps and the drop each step makes**</span>, <span style="color:#6d4c41">**brown is a length of arc, an angle in radians such as 2π or the 15° step 0.2618**</span>, and <span style="color:#757575">**grey is a case drawn for comparison**</span>.

**Line styles in the figures.** A solid green line is $\cos\theta$ and a dashed green line is $\cos^2\theta$. A short black line through a black dot is the tangent, the slope at that point.

## Table of contents

- [[#The square of the cosine]]
- [[#When to reach for the cosine wave]]
- [[#The wave and where it is flat]]
- [[#Try the cosine wave yourself]]
- [[#How the cosine wave works]]
- [[#Other ways to see the quarter turn]]
- [[#Why the cosine wave matters]]
- [[#The cosine wave taught in, applied in]]

## The square of the cosine

Navigation: 📋 [[#Table of contents|TOC]] | [[#When to reach for the cosine wave]] ➡️

Textbook: [Whitney, Trigonometry handbook, graphs of the parent functions, PDF p. 16](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=16)

**The cosine wave**, also the graph of cosine or the cosine graph: $\cos\theta$ plotted against the angle θ in radians, rising and falling between 1 and −1. *Cited* from the [graph of cosine, PDF p. 16](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=16).

**The square of the cosine**, also cos squared or $\cos^2\theta$: the share of 1 the horizontal leg holds once squared. *Derived* in [[#The two shares]] and [[#How the cosine wave works]].

### The quarter turn and its table

<table>
<tr><th style="color:#1565c0">angle</th><th style="color:#6d4c41">radians</th><th style="color:#2e7d32">cos θ</th><th style="color:#2e7d32">cos² θ</th><th style="color:#1565c0">drop from the row above</th><th>slope of cos² θ</th></tr>
<tr><td>0°</td><td>0</td><td>1</td><td style="border:2px solid #212121">1</td><td></td><td style="border:2px solid #212121">0</td></tr>
<tr><td>15°</td><td>0.2618</td><td>0.9659</td><td>0.933</td><td style="border:2px dashed #212121">0.067</td><td>−0.5</td></tr>
<tr><td>30°</td><td>0.5236</td><td>0.8660</td><td>0.75</td><td>0.183</td><td>−0.8660</td></tr>
<tr><td>45°</td><td>0.7854</td><td>0.7071</td><td>0.5</td><td style="border:2px dashed #212121">0.25</td><td style="border:2px solid #212121">−1</td></tr>
<tr style="background:#fff8e1"><td><b>46.25°</b></td><td>0.8072</td><td>0.6915</td><td style="border:2px solid #212121"><b>0.4782</b></td><td></td><td>−0.9990</td></tr>
<tr><td>60°</td><td>1.0472</td><td>0.5</td><td>0.25</td><td style="border:2px dashed #212121">0.25</td><td>−0.8660</td></tr>
<tr><td>75°</td><td>1.3090</td><td>0.2588</td><td>0.067</td><td>0.183</td><td>−0.5</td></tr>
<tr><td>90°</td><td>1.5708</td><td>0</td><td style="border:2px solid #212121">0</td><td style="border:2px dashed #212121">0.067</td><td style="border:2px solid #212121">0</td></tr>
</table>

**How to read this table.** Each row is one angle of the quarter turn. The drop column is how much $\cos^2$ lost since the row 15° earlier; the 46.25° row sits between two 15° rows, so it has no drop. The last column is the slope $-2\cos\theta\sin\theta$, in share per radian.

**What to look for.** The solid boxes: $\cos^2$ starts at 1 and ends at 0 with slope 0 at both ends, and is steepest, −1, at 45°. The dashed boxes: [$\cos^2$ every 15° drops](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-quarter-turn) 0.067 at the ends and 0.25 in the middle.

### The two shares

[Pythagoras](../references/textbooks/geometry/geometry-handbook.pdf#page=80) on [[Polar Coordinates#The point: from length and angle to x and y|the triangle with hypotenuse 1]] gives the [Pythagorean identity](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=9):

$$
\cos^2\theta + \sin^2\theta = 1
$$

$$
\underbrace{\textcolor{#2e7d32}{\cos^2\theta}}_{\text{horizontal leg, squared}}
+
\underbrace{\textcolor{#ef6c00}{\sin^2\theta}}_{\text{vertical leg, squared}}
=
\underbrace{1}_{\text{radius squared}},
\qquad
\textcolor{#2e7d32}{0.4782} + \textcolor{#ef6c00}{0.5218} = 1
$$

**What the equation says.** The two squared legs [split 1 into two shares](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-polar), at every angle. When one share grows the other shrinks by the same amount.

**Why the squares are there.** The legs themselves do not add to 1: $0.6915 + 0.7224 = 1.4139$. Only their squares do: $0.4782 + 0.5218 = 1$.

**What the schedule takes from it.** This split of 1 is what the cosine schedule uses. [[How The Quarter Circle Gives The Multipliers#Step 2: the point is the two multipliers|The kept share and the noise share]] are $\cos^2$ and $\sin^2$ of one angle.

```python
import math
import matplotlib.pyplot as plt
from plane import save, rad, GREEN, ORANGE, GREY, LIGHT_GREY

c, s = math.cos(rad(46.25)), math.sin(rad(46.25))
print(f"cos^2 {c * c:.4f} + sin^2 {s * s:.4f} = {c * c + s * s:.4f}   without the squares: {c:.4f} + {s:.4f} = {c + s:.4f}")

fig, ax = plt.subplots(figsize=(7.5, 3.2))
rows = [(3, 0, c * c, GREEN, f"cos²θ = 0.6915² = {c * c:.4f}"),
        (2, 0, s * s, ORANGE, f"sin²θ = 0.7224² = {s * s:.4f}"),
        (1, 0, c * c, GREEN, ""), (1, c * c, s * s, ORANGE, f"together: {c * c:.4f} + {s * s:.4f} = 1"),
        (0, 0, c, GREY, ""), (0, c, s, LIGHT_GREY, f"no squares: 0.6915 + 0.7224 = {c + s:.4f}")]
for y, left, width, color, label in rows:
    ax.barh(y, width, left=left, color=color, height=0.6)
    if label:
        ax.text(1.47, y, label, va="center", fontsize=10)
ax.axvline(1, color="black", ls=(0, (4, 3)))
ax.text(1.0, -0.75, "radius² = 1", ha="center")
ax.set_xlim(0, 2.6)
ax.set_ylim(-1, 3.5)
ax.set_yticks([])
ax.spines[["top", "right", "left"]].set_visible(False)
ax.set_title("at 46.25°: the squared legs fill exactly 1", fontsize=12)
save(fig, "t6-pythagoras-shares.svg")
```

![Four bars on a scale from 0: cos squared 0.4782 in green, sin squared 0.5218 in orange, the two stacked to exactly the dashed line at 1, and the unsquared legs stacked in grey overshooting to 1.4139|700](assets/t6-pythagoras-shares.svg)

**How to read this.** The x-axis is length from 0, and the dashed line is 1. The third bar is the first two placed end to end and stops exactly on the line. The grey bar, the legs without their squares, overshoots to 1.4139.

## When to reach for the cosine wave

Navigation: ⬅️ [[#The square of the cosine]] | 📋 [[#Table of contents|TOC]] | [[#The wave and where it is flat]] ➡️

**The situation.** A quantity has to fall from all of 1 to none of it over a fixed stretch, slowly at both ends and fastest in the middle. The square of the cosine over the quarter turn does exactly that, and [[The Cosine Noise Schedule#The boundary values C_k|the cosine noise schedule's boundary values]] use it for the share of signal kept.

**What goes wrong without it.** A straight line from 1 to 0 drops the same 0.1667 every 15°, so it loses as much at the very start as in the middle. The cosine alone, unsquared, drops 0.2588 in its last 15° and ends at slope −1, as [[#The consequence: drop the square]] draws.

## The wave and where it is flat

Navigation: ⬅️ [[#When to reach for the cosine wave]] | 📋 [[#Table of contents|TOC]] | [[#Try the cosine wave yourself]] ➡️

Textbook: [Whitney, Trigonometry handbook, graphs of the parent functions and their period, PDF p. 17](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=17)

"Cosine wave" is two words, taken apart below: the wave first, then the cosine, then both together, where the square is flat, and what follows from dropping the square.

### The base word: wave

**What the word means.** A wave rises, falls and comes back to where it started. The [graph of cosine](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=16) does this between 1 and −1, and repeats every $2\pi$, its [period](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=17).

$$
\cos(\theta + 2\pi) = \cos\theta
$$

$$
\underbrace{\textcolor{#2e7d32}{\cos(\theta + \textcolor{#6d4c41}{2\pi})}}_{\text{one full turn later}}
=
\underbrace{\textcolor{#2e7d32}{\cos\theta}}_{\text{the same height}},
\qquad
\textcolor{#2e7d32}{\cos(0.8072 + \textcolor{#6d4c41}{6.2832})} = \textcolor{#2e7d32}{\cos 0.8072} = \textcolor{#2e7d32}{0.6915}
$$

**What the equation says.** One full turn, $2\pi$ radians of arc, brings the point back to the same place, so the cosine repeats. At 46.25° the height one turn later is still 0.6915.

**Why the 2π is there.** Add half a turn, π, instead and the point lands opposite the centre: $\cos(0.8072 + \pi) = -0.6915$. Only the whole turn gives the height back.

### The qualifier: cosine

**What the word means.** The wave's height at angle θ is the cosine, the point's x-coordinate on [[The Unit Circle#The circle: every point at distance 1|the unit circle]]. Squared, it is the share the schedule keeps.

$$
y = \cos\theta
$$

$$
\underbrace{y}_{\text{height of the wave}}
=
\underbrace{\textcolor{#2e7d32}{\cos\theta}}_{\text{x-coordinate of the point at angle } \theta},
\qquad
\textcolor{#2e7d32}{\cos 0.8072} = \textcolor{#2e7d32}{0.6915}
$$

**What the equation says.** The wave is the cosine read off the circle at every angle. At 46.25° the point sits 0.6915 right of the centre, so the wave stands at 0.6915.

**Why the cosine's shape is there.** Swap the square of the cosine for a [straight line from 1 to 0](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-name-cosine), $1 - \theta / (\pi/2)$, and every 15° drops the same 0.1667. The cosine's square drops 0.067 in the first 15° and 0.25 next to 45°, so it saves its fast fall for the middle.

### All the words together: the formula

$$
y = \cos\theta, \qquad y = \cos^2\theta, \qquad \theta \in [0,\ 2\pi]
$$

$$
\underbrace{\textcolor{#2e7d32}{\cos\theta}}_{\text{x-coordinate at angle }\theta}
\qquad\text{and}\qquad
\underbrace{\textcolor{#2e7d32}{\cos^2\theta}}_{\text{share held by the horizontal leg}},
\qquad
\theta \in \underbrace{[0,\ \textcolor{#6d4c41}{2\pi}]}_{\text{one full turn}}
$$

**What the equation says.** The cosine goes negative in the left half of the circle, where the point sits left of the centre. Its square is never negative, and it repeats twice per turn.

**Why the quarter turn is shaded.** From 0 to π/2 the cosine falls from 1 to 0 without going negative, so on that stretch $\cos^2$ is a share falling from all of 1 to none of it. That stretch, shaded blue in the figure below, is the one the cosine schedule uses.

### The quarter turn: where the square is flat

The slope of $\cos^2\theta$ comes from the [derivative of the cosine](../references/textbooks/calculus/calculus-textbook.pdf#page=193) and the [chain rule](../references/textbooks/calculus/calculus-textbook.pdf#page=198), with θ in radians. The scene draws [the chain rule slope $-2\cos\theta\sin\theta$](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-why-offset) as tangents at the schedule's posts.

$$
\frac{d}{d\theta}\cos^2\theta = -2\cos\theta\sin\theta = -\sin 2\theta
$$

$$
\frac{d}{d\theta}\,\textcolor{#2e7d32}{\cos^2\theta}
=
\underbrace{2\textcolor{#2e7d32}{\cos\theta}}_{\text{outer square}}
\cdot
\underbrace{(-\textcolor{#ef6c00}{\sin\theta})}_{\text{inner cosine}}
=
-2\textcolor{#2e7d32}{\cos\theta}\textcolor{#ef6c00}{\sin\theta}
=
\underbrace{-\sin 2\theta}_{\text{double angle}}
$$

**What the equation says.** The slope is a product of the two legs. At 0 the vertical leg is 0, and at π/2 the horizontal leg is 0, so either way the product is 0 and the curve is flat.

**Why the 2 is there.** It is the outer square's own slope, $2u$ for $u^2$, and with it the slope at 45° is $-2 \cdot 0.7071 \cdot 0.7071 = -1$ (−0.9990 at 46.25°). Without it the steepest slope would read −0.5, and the drop it predicts from 30° to 45° is 0.1264 instead of the 0.25 the table measured ([[How The Cosine Wave Works#The drops|the drops]] derives both).

**Why the minus sign is there.** The cosine falls over the quarter turn, so its slope $-\sin\theta$ is negative. Without the minus the slope at 45° reads +1, a rise, while the table falls from 0.75 at 30° to 0.25 at 60°.

**Why the double angle is there.** The [double-angle rule](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=37) $\sin 2\theta = 2\sin\theta\cos\theta$ turns the slope into one sine at twice the angle, steepest where $2\theta = 90°$, so at θ = 45°, and never steeper than −1. At 46.25° it gives $-\sin 92.5° = -0.9990$, matching $-2\cos\theta\sin\theta$. Leave the angle undoubled and $-\sin 46.25° = -0.7224$, the slope of $\cos$ alone, not of its square.

```python
import math
import matplotlib.pyplot as plt
from plane import save, GREEN, BLUE, LIGHT_BLUE

ts = [i * 2 * math.pi / 720 for i in range(721)]
for name, t in (("0", 0), ("pi/4", math.pi / 4), ("pi/2", math.pi / 2)):
    c, s = math.cos(t), math.sin(t)
    print(f"theta {name:4s}  cos {c:.4f}  cos^2 {c * c:.4f}  slope of cos {round(-s, 4) + 0:.4f}  slope of cos^2 {round(-2 * c * s, 4) + 0:.4f}")

fig, ax = plt.subplots(figsize=(9, 4.2))
ax.axvspan(0, math.pi / 2, color=LIGHT_BLUE)
ax.text(math.pi / 4, -1.2, "the quarter turn, 0 to π/2", color=BLUE, ha="center", fontsize=10)
ax.plot(ts, [math.cos(t) for t in ts], color=GREEN, lw=2.5)
ax.plot(ts, [math.cos(t) ** 2 for t in ts], color=GREEN, lw=2, ls=(0, (5, 3)))
ax.text(4.0, -0.75, "cos θ", color=GREEN, fontsize=12)
ax.text(3.2, 0.82, "cos² θ (dashed)", color=GREEN, fontsize=12)
for t0, label in ((0, "flat at 0:\nslope −2 cos θ sin θ = 0"), (math.pi / 2, "flat at π/2:\nslope 0")):
    y0 = math.cos(t0) ** 2
    ax.plot([t0 - 0.35, t0 + 0.35], [y0, y0], color="black", lw=1.5)
    ax.plot(t0, y0, "o", color="black", ms=6)
    ax.text(t0 + 0.4, y0 + 0.05, label, fontsize=9)
ax.plot([math.pi / 2 - 0.3, math.pi / 2 + 0.3], [0.3, -0.3], color="black", lw=1, ls=(0, (2, 2)))
ax.text(math.pi / 2 + 0.3, -0.45, "cos alone has slope −1 here", fontsize=9)
ax.axhline(0, color="black", lw=0.8)
ax.set_xticks([0, math.pi / 2, math.pi, 3 * math.pi / 2, 2 * math.pi], ["0\n0°", "π/2\n90°", "π\n180°", "3π/2\n270°", "2π\n360°"])
ax.set_xlim(-0.1, 2 * math.pi + 0.1)
ax.set_ylim(-1.35, 1.35)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(color="#eeeeee")
ax.set_xlabel("θ in radians")
ax.set_title("one full turn of cos θ, and its square", fontsize=12)
save(fig, "t7-cosine-wave-quarter-turn.svg")
```

![The cosine as a solid green wave and its square as a dashed green wave for theta from 0 to 2 pi, with the quarter turn 0 to pi over 2 shaded light blue, flat tangent lines on the square at 0 and pi over 2, and a dashed tangent of slope -1 on the cosine at pi over 2|800](assets/t7-cosine-wave-quarter-turn.svg)

**How to read this.** The x-axis is the angle in radians, with degrees under each tick, and the y-axis runs from −1.35 to 1.35. The solid curve is $\cos\theta$ and the dashed curve $\cos^2\theta$. The short black lines through the two black dots are flat, slope 0, at 0 and at π/2.

### The consequence: drop the square

**What changes.** Without the square, the quarter turn still starts flat but no longer ends flat. The slope of $\cos\theta$ is $-\sin\theta$:

$$
\frac{d}{d\theta}\cos\theta = -\sin\theta
$$

$$
\underbrace{-\textcolor{#ef6c00}{\sin 0} = 0}_{\text{flat start, as with the square}}
\qquad
\underbrace{-\textcolor{#ef6c00}{\sin(\pi/2)} = -1}_{\text{steep end, where the square was flat}}
$$

**What the equation says.** At 0 the cosine is flat, like its square. At π/2 it falls at slope −1, the dashed tangent in the figure above and the black tangent in the right panel below.

**What it does to a schedule.** A schedule built on $\cos$ alone would lose its last bit of signal at full speed instead of easing in: its last 15° drops 0.2588 against 0.0670 with the square. Its value would also be a multiplier, 0.6915 at 46.25°, rather than a share, 0.4782.

```python
import math
import matplotlib.pyplot as plt
from plane import save, rad, GREEN, BLUE, GREY, LIGHT_BLUE

h = rad(15)
ts = [i * (math.pi / 2) / 360 for i in range(361)]
curves = (("cos² θ", lambda t: math.cos(t) ** 2, lambda t: -2 * math.cos(t) * math.sin(t), (0, (5, 3))),
          ("cos θ", math.cos, lambda t: -math.sin(t), "-"))
for name, f, slope, _ in curves:
    first, last = f(0) - f(h), f(math.pi / 2 - h) - f(math.pi / 2)
    print(f"{name:6s} at 46.25 {f(rad(46.25)):.4f}  first 15 drops {first:.4f}  last 15 drops {last:.4f}  "
          f"slope at 0 {round(slope(0), 4) + 0:.4f}  slope at pi/2 {round(slope(math.pi / 2), 4) + 0:.4f}")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), sharey=True)
for ax, (name, f, slope, ls), title in zip(axes, curves, ("with the square: cos² θ", "the square dropped: cos θ")):
    ax.axvspan(0, math.pi / 2, color=LIGHT_BLUE)
    if name == "cos θ":
        ax.plot(ts, [math.cos(t) ** 2 for t in ts], color=GREY, lw=1.5, ls=(0, (5, 3)))
        ax.annotate("cos² θ, for comparison", xy=(0.95, math.cos(0.95) ** 2), xytext=(0.05, 0.42),
                    color=GREY, fontsize=9, arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
    ax.plot(ts, [f(t) for t in ts], color=GREEN, lw=2.5, ls=ls)
    for t0 in (0, math.pi / 2):
        y0, m = f(t0), slope(t0)
        ax.plot([t0 - 0.22, t0 + 0.22], [y0 - 0.22 * m, y0 + 0.22 * m], color="black", lw=1.5)
        ax.plot(t0, y0, "o", color="black", ms=6)
    m_end = round(slope(math.pi / 2), 4) + 0
    ax.text(0.04, 1.08, "slope 0", fontsize=10)
    ax.text(math.pi / 2 + 0.03, 0.12 if m_end else 0.04, f"slope {m_end:g}".replace("-", "−"), fontsize=10)
    first, last = f(0) - f(h), f(math.pi / 2 - h) - f(math.pi / 2)
    for x, top, bottom in ((h, f(0), f(h)), (math.pi / 2 - h, f(math.pi / 2 - h), f(math.pi / 2))):
        ax.annotate("", xy=(x, bottom), xytext=(x, top), arrowprops=dict(arrowstyle="|-|", color=BLUE, lw=1.5, mutation_scale=4))
    ax.text(0.05, 0.16, f"first 15° drops {first:.4f}", color=BLUE, fontsize=10)
    ax.text(0.05, 0.04, f"last 15° drops {last:.4f}", color=BLUE, fontsize=10)
    ax.text(rad(46.25) + 0.04, f(rad(46.25)) + 0.04, f"{f(rad(46.25)):.4f} at 46.25°", color=GREEN, fontsize=9)
    ax.plot(rad(46.25), f(rad(46.25)), "o", color=GREEN, ms=5)
    ax.set_xticks([0, math.pi / 4, math.pi / 2], ["0\n0°", "π/4\n45°", "π/2\n90°"])
    ax.set_xlim(-0.25, math.pi / 2 + 0.35)
    ax.set_ylim(-0.12, 1.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#eeeeee")
    ax.set_xlabel("θ in radians")
    ax.set_title(title, fontsize=12)
save(fig, "t10-drop-the-square.svg")
```

![Two panels over the quarter turn 0 to pi over 2. Left, with the square: cos squared as a dashed green curve from 1 to 0, flat black tangents at both ends, 0.4782 at 46.25 degrees, first and last 15 degrees each dropping 0.0670. Right, the square dropped: cos as a solid green curve, flat at 0 but with a tangent of slope -1 at pi over 2, 0.6915 at 46.25 degrees, first 15 degrees dropping 0.0341 and last 15 degrees dropping 0.2588, with cos squared in dashed grey for comparison|900](assets/t10-drop-the-square.svg)

**How to read this.** In each panel the x-axis is the angle over the quarter turn, in radians with degrees under each tick, and the y-axis is the value from 0 to 1. The left panel is $\cos^2\theta$; the right panel is $\cos\theta$, with $\cos^2\theta$ in grey beside it. Look at the black tangent at π/2, flat on the left and slope −1 on the right, and at the blue bracket over the last 15°: 0.0670 against 0.2588.

## Try the cosine wave yourself

Navigation: ⬅️ [[#The wave and where it is flat]] | 📋 [[#Table of contents|TOC]] | [[#How the cosine wave works]] ➡️

**In two lines.** Nine steps in the folder of [[Running The Unit Circle#Try the unit circle yourself|the unit circle sandbox]], from the square every 15° to the three figure scripts above and the slope two ways, each output read field by field, are in [[Running The Cosine Wave#Try the cosine wave yourself]]. The steps this note cites by number are step 4 (the square every 15° and its drops) and step 6 (the slope at the two ends and the middle).

## How the cosine wave works

Navigation: ⬅️ [[#Try the cosine wave yourself]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to see the quarter turn]] ➡️

**In two lines.** [[How The Cosine Wave Works]] derives the identity from Pythagoras divided by $r^2$, the slope $-2\cos\theta\sin\theta = -\sin 2\theta$ one step per line with its values 0, −1 and 0, and the drops 0.067 and 0.25 as the slope at each 15° step's middle times 0.2618 rad. Its headings are [[How The Cosine Wave Works#The identity|the identity]], [[How The Cosine Wave Works#The wave|the wave]], [[How The Cosine Wave Works#The slope|the slope]] and [[How The Cosine Wave Works#The drops|the drops]].

## Other ways to see the quarter turn

Navigation: ⬅️ [[#How the cosine wave works]] | 📋 [[#Table of contents|TOC]] | [[#Why the cosine wave matters]] ➡️

**The unit circle.** Read the circle at 15° steps: each drop in $\cos^2$ is a drop in the squared horizontal leg, as in [[The Unit Circle#The circle: every point at distance 1]]. It shows where each number sits on the plane.

**Drag it.** The scene Dissolving the Dog, [frame "the quarter turn"](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-quarter-turn), moves the point at 15° presets and shows $\cos^2$ every 15° with its drops. It asks which turn drops most before it shows the answer.

## Why the cosine wave matters

Navigation: ⬅️ [[#Other ways to see the quarter turn]] | 📋 [[#Table of contents|TOC]] | [[#The cosine wave taught in, applied in]] ➡️

**Where the schedule uses it.** [[The Cosine Noise Schedule#The boundary values C_k|The cosine noise schedule]] keeps the share $\cos^2\theta_k$ of the clean signal at post $k$, with the angle walking this quarter turn. The flat start means the first steps add very little noise, and the flat end means the last bit of signal goes gently.

**Why it was chosen.** Nichol and Dhariwal designed it for "a linear drop-off of ᾱt in the middle of the process, while changing very little near the extremes" (*cited*, [section 3.2, p. 4](https://arxiv.org/pdf/2102.09672#page=4)). [[The Quarter Turn And The Fraction#Step 3: the quarter turn, squared|Step 3 of the schedule build]] plots it at all 101 posts.

## The cosine wave taught in, applied in

Navigation: ⬅️ [[#Why the cosine wave matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the `drip --math` walk of [the forward process and the score](../../../PhD/reduce-reuse-recycle/artifacts/drips/forward-process-and-the-score/00-INDEX.md) in the reduce-reuse-recycle research repository, [piece 2, rung 1 as the walk kept it](../../../PhD/reduce-reuse-recycle/artifacts/drips/forward-process-and-the-score/kept/05-the-cosine-boundary-values-by-hand.md): the two squared legs adding to 1, the quarter turn at 15° presets with its drops, and why $\cos^2$ is flat at 0 and π/2
- step 4 of the one-expert rebuild walk in the same repository, [On paper 2](../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-4-the-forward-process-and-the-cosine-schedule) (the two shares) and [On paper 5: play with the quarter turn](../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-4-the-forward-process-and-the-cosine-schedule)

**Applied in:** [[The Quarter Circle Under The Cosine Schedule]] and [[The Cosine Noise Schedule]], whose boundary values are $\cos^2$ on this quarter turn.

> [!note]- How this was checked
> The three figure scripts were run on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and matplotlib 3.10.8 from the machine's `python3`, by vault-writer, in the empty folder `~/playground/sandbox/cosine-wave-v2`, which was removed afterwards; the first two had earlier run in `~/playground/sandbox/unit-circle-figures` the same day and printed the same lines. The prepared environment `~/.vault-sandbox` is missing on this machine. The two older SVGs re-drew identical to the embedded ones apart from matplotlib's date stamp and random element ids, and every SVG was rasterised with PyMuPDF and opened, with a matplotlib PNG twin checked for the dashed curves and tangents, which PyMuPDF's SVG reader draws solid.
>
> The with-and-without numbers were printed by a throwaway script in the same folder: without the slope's 2, −0.5 at 45° and a predicted drop of 0.1264 from 30° to 45° (0.2529 with it, 0.25 measured); without the minus, +1 at 45°; with the angle undoubled, −0.7224 at 46.25° against −0.9990; half a turn, $\cos(0.8072 + \pi) = -0.6915$; a straight line, 0.1667 every 15°; and the drops at 7.5°, 0.0678 against 0.067 measured. The table's slope column is $-2\cos\theta\sin\theta$ at each angle, computed from the cosine and sine columns.
>
> The textbook pages were opened and read as text with PyMuPDF: the trigonometry handbook's PDF pages 9 (the Pythagorean identities), 16 (graphs of the parent functions, cosine and secant), 17 (period 2π for cosine) and 37 (double angle formulas); the geometry handbook's page 80; the calculus textbook's pages 193 (section 2.5, x in radians) and 198 (section 2.6, the chain rule). The scene frame anchors are as the walk's `dispatch.md` records them.
>
> No drawn picture is prompted for this note: every picture here needs exact positions and slopes, so code draws them. No tldr-pages entry covers this.
