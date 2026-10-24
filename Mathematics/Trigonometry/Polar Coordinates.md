---
aliases: [polar coordinates, polar, polar to Cartesian, polar to rectangular, "(r, θ) to (x, y)", "x = r cos θ", "y = r sin θ", Cartesian to polar, "r = √(x² + y²)", "θ = tan⁻¹(y / x)", atan2, polar axis, the pole]
sources:
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Trigonometry, version 2.4: the polar axis and the polar angle, PDF p. 8; cos θ = x / r and tan θ = y / x, PDF p. 9; polar coordinates, PDF p. 68: ../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=68"
standard: vault-note v2
---

# Polar Coordinates

Up: [[Trigonometry]] · ⬅️ [[The Unit Circle]] · [[Running The Unit Circle]] ➡️

Mathematics, Trigonometry. Needs: [[The Unit Circle#The circle: every point at distance 1|the unit circle]], whose points have the cosine as their x-coordinate, and [[The Unit Circle#The angle: one line from the origin|an angle as one line from the origin]].

**Polar coordinates name a point by how far out it is and how far it is turned.**

> [!question]- Test yourself
> No quiz page covers this note yet.

> [!warning]- Unfinished
> - No quiz page for this note yet.

Stated claims: 0.

**The toy angle.** Every number here is worked at 46.25°, the angle of post 51 in [[The Quarter Circle Under The Cosine Schedule]], as in [[The Unit Circle]].

**Colours, as in The Unit Circle.** <span style="color:#2e7d32">**Green is $\cos\theta$ and the horizontal leg $x$**</span>, <span style="color:#ef6c00">**orange is $\sin\theta$ and the vertical leg $y$**</span>, and <span style="color:#1565c0">**blue is the point, the line from the origin and its angle θ**</span>.

## Table of contents

- [[#Polar coordinates]]
- [[#When to reach for polar coordinates]]
- [[#Try polar coordinates yourself]]
- [[#How polar coordinates work]]
- [[#Other ways to convert]]
- [[#Why polar coordinates matter]]
- [[#Polar coordinates taught in, applied in]]

## Polar coordinates

Navigation: 📋 [[#Table of contents|TOC]] | [[#When to reach for polar coordinates]] ➡️

Textbook: [Whitney, Trigonometry handbook, polar coordinates, PDF p. 68](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=68)

### The base word: coordinates

**What the word means.** Coordinates are the numbers that name a point. The usual pair says how far right and how far up.

$$
(x,\ y) = (0.6915,\ 0.7224)
$$

$$
(\underbrace{\textcolor{#2e7d32}{x}}_{\text{how far right}},\ \underbrace{\textcolor{#ef6c00}{y}}_{\text{how far up}}) = (\textcolor{#2e7d32}{0.6915},\ \textcolor{#ef6c00}{0.7224})
$$

**What it means.** These are the point at 46.25° on the unit circle, named by its two legs.

### The qualifier: polar

**What the word means.** Polar names the point from the pole, the origin: how far out it is, and how far it is turned from the [polar axis](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=8), the positive x-axis.

$$
(r,\ \theta) = (1,\ 46.25^\circ)
$$

$$
(\underbrace{r}_{\text{how far out}},\ \underbrace{\textcolor{#1565c0}{\theta}}_{\text{how far turned}}) = (1,\ \textcolor{#1565c0}{46.25^\circ})
$$

**What it means.** It is the same point as $(0.6915, 0.7224)$, named by a length and a turn.

### The point: from length and angle to x and y

**All the words together.** The same point can be named two ways: by its length and angle, its [polar coordinates](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=68) $(r, \theta)$, or by its $(x, y)$. The scene Dissolving the Dog draws [the two legs and their share bar](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-polar), with $\cos^2\theta + \sin^2\theta = 1$ as one bar.

$$
x = r\cos\theta, \qquad y = r\sin\theta
$$

$$
\underbrace{\textcolor{#2e7d32}{x}}_{\text{horizontal leg}} = \underbrace{r}_{\text{length}}\ \textcolor{#2e7d32}{\cos\theta} = 1 \cdot 0.6915,
\qquad
\underbrace{\textcolor{#ef6c00}{y}}_{\text{vertical leg}} = r\ \textcolor{#ef6c00}{\sin\theta} = 1 \cdot 0.7224
$$

**What the equation says.** Drop a vertical from the point to the x-axis and you have a right triangle with hypotenuse $r$. Its legs are $r\cos\theta$ and $r\sin\theta$.

**Why the $r$ is there.** On the unit circle $r = 1$, so the legs are the cosine and sine themselves. A point at the same angle but twice as far out sits at $(1.3830, 1.4447)$; without the $r$ it would be read as $(0.6915, 0.7224)$, the unit circle's point.

```python
import math
from plane import plane, save, circle, angle, rad, GREEN, ORANGE, BLUE

r, theta = 1, 46.25
x, y = r * math.cos(rad(theta)), r * math.sin(rad(theta))
print(f"polar (r = {r}, theta = {theta} deg)  ->  cartesian ({x:.4f}, {y:.4f})")

fig, ax = plane((-0.3, 1.35), (-0.3, 1.25))
circle(ax, upto=90)
ax.plot([0, x], [0, y], color=BLUE, lw=2)
ax.plot([0, x], [0, 0], color=GREEN, lw=5)
ax.plot([x, x], [0, y], color=ORANGE, lw=5)
ax.plot([0, x], [y, y], ":", color=ORANGE)
ax.plot(x, y, "o", color=BLUE, ms=8)
angle(ax, theta, r=0.22)
ax.text(0.25, 0.08, "θ", color=BLUE)
ax.text(x / 2, -0.12, "x = r cos θ = 0.6915", color=GREEN, ha="center")
ax.text(x + 0.04, y / 2, "y = r sin θ\n= 0.7224", color=ORANGE, va="center")
ax.text(-0.04, y, "0.7224", color=ORANGE, ha="right", va="center", fontsize=10)
ax.text(x / 2 - 0.12, y / 2 + 0.08, "r = 1", color=BLUE, rotation=theta)
ax.text(x + 0.04, y + 0.05, "(r, θ) = (1, 46.25°)\n→ (0.6915, 0.7224)", color=BLUE, fontsize=10)
ax.set_title("a point given by its length and angle, read as (x, y)", fontsize=12)
save(fig, "t5-polar-to-cartesian.svg")
```

![The point (r, theta) = (1, 46.25 degrees) on the unit circle with its green horizontal leg x = r cos theta = 0.6915 and orange vertical leg y = r sin theta = 0.7224, projected onto both axes|600](assets/t5-polar-to-cartesian.svg)

**How to read this.** The blue line is $r = 1$ at angle θ. The green leg along the x-axis ends at 0.6915 and the orange leg ends level with 0.7224 on the y-axis. Those two numbers are the point's $(x, y)$.

### The consequence: x and y give back the length and the angle

**What changes.** Both names carry the same point, so $(x, y)$ converts back: the length is the [distance from the origin](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=68), and the angle is the one whose tangent is $y/x$, adjusted to the right quadrant.

$$
r = \sqrt{x^2 + y^2}, \qquad \theta = \tan^{-1}\frac{y}{x}
$$

$$
\underbrace{r}_{\text{how far out}} = \sqrt{\textcolor{#2e7d32}{0.4782} + \textcolor{#ef6c00}{0.5218}} = 1,
\qquad
\underbrace{\textcolor{#1565c0}{\theta}}_{\text{how far turned}} = \tan^{-1}\frac{\textcolor{#ef6c00}{0.7224}}{\textcolor{#2e7d32}{0.6915}} = \tan^{-1} 1.0446 = 46.25^\circ
$$

**What it means.** At $(1.3830, 1.4447)$ the same two lines give $r = 2$ and the same 46.25°: the length moved and the turn did not. [[Running The Unit Circle#Try the unit circle yourself|Step 8 of the sandbox]] prints both.

### Where this goes next

The two legs at 46.25° square to $0.4782 + 0.5218 = 1$. That split of 1 into two shares is [[The Cosine Wave#The two shares|the Pythagorean identity]], and the schedule reads its kept share and its noise share off it.

## When to reach for polar coordinates

Navigation: ⬅️ [[#Polar coordinates]] | 📋 [[#Table of contents|TOC]] | [[#Try polar coordinates yourself]] ➡️

**You know a length and a turn.** Reach for them when a point is given by how far out it is and how far it is turned, as each post of the cosine schedule is given by its angle, and you need its x and y.

**What goes wrong without them.** Reading the legs as the cosine and sine at a radius other than 1 is off by the radius: at radius 2 the x-coordinate is 1.3830, twice the cosine, as [[The Unit Circle#The consequence: a radius other than 1]] draws.

## Try polar coordinates yourself

Navigation: ⬅️ [[#When to reach for polar coordinates]] | 📋 [[#Table of contents|TOC]] | [[#How polar coordinates work]] ➡️

**In two lines.** The script above runs as step 6 of [[Running The Unit Circle#Try the unit circle yourself]], in the same empty folder as the unit circle's scripts. Step 7 reaches the same point by turning a line of length 1, and step 8 runs the back-conversion of [[#Other ways to convert]].

## How polar coordinates work

Navigation: ⬅️ [[#Try polar coordinates yourself]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to convert]] ➡️

Textbook: [Whitney, Trigonometry handbook, cos θ = x / r and tan θ = y / x, PDF p. 9](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=9)

**The derivation, one step per line.** The line from the origin to $(x, y)$ is the hypotenuse $r$ of a right triangle whose legs are $x$ and $y$.

$$
\begin{aligned}
\cos\theta &= \frac{x}{r}, \qquad \sin\theta = \frac{y}{r} \\
x &= r\cos\theta, \qquad y = r\sin\theta \\
r^2 &= x^2 + y^2 \\
\frac{y}{x} &= \frac{r\sin\theta}{r\cos\theta} = \tan\theta
\end{aligned}
$$

$$
\begin{aligned}
\textcolor{#2e7d32}{\cos\theta} &= \underbrace{\frac{\textcolor{#2e7d32}{x}}{r}}_{\text{adjacent over hypotenuse}}, \qquad \textcolor{#ef6c00}{\sin\theta} = \underbrace{\frac{\textcolor{#ef6c00}{y}}{r}}_{\text{opposite over hypotenuse}} \\
\textcolor{#2e7d32}{x} &= \underbrace{r\,\textcolor{#2e7d32}{\cos\theta}}_{\text{multiply by } r}, \qquad \textcolor{#ef6c00}{y} = r\,\textcolor{#ef6c00}{\sin\theta} \\
r^2 &= \underbrace{\textcolor{#2e7d32}{x}^2 + \textcolor{#ef6c00}{y}^2}_{\text{Pythagoras}} \\
\frac{\textcolor{#ef6c00}{y}}{\textcolor{#2e7d32}{x}} &= \underbrace{\frac{\cancel{r}\,\textcolor{#ef6c00}{\sin\theta}}{\cancel{r}\,\textcolor{#2e7d32}{\cos\theta}}}_{r \text{ cancels}} = \textcolor{#1565c0}{\tan\theta}
\end{aligned}
$$

**The worked numbers, at 46.25°.**

$$
\begin{aligned}
r = 1:\quad \textcolor{#2e7d32}{x} &= 0.6915, \qquad \textcolor{#ef6c00}{y} = 0.7224, \qquad \frac{0.7224}{0.6915} = 1.0446 \\
r = 2:\quad \textcolor{#2e7d32}{x} &= 1.3830, \qquad \textcolor{#ef6c00}{y} = 1.4447, \qquad \frac{1.4447}{1.3830} = 1.0446
\end{aligned}
$$

**What the derivation says.** Going out, $r$ multiplies both legs. Coming back, $r$ is the square root of the summed squares, and it cancels from $y/x$, so the ratio 1.0446 names the same turn at both lengths.

## Other ways to convert

Navigation: ⬅️ [[#How polar coordinates work]] | 📋 [[#Table of contents|TOC]] | [[#Why polar coordinates matter]] ➡️

**`math.hypot` and `math.atan2` in Python.** They give the length and the turn from $(x, y)$, and `atan2` picks the quadrant itself. The script is `back.py`, run as step 8 of [[Running The Unit Circle#Try the unit circle yourself|the sandbox]]:

```python
import math, cmath

x, y = math.cos(math.radians(46.25)), math.sin(math.radians(46.25))
print(f"hypot {math.hypot(x, y):.4f}  atan2 {math.degrees(math.atan2(y, x)):.2f} deg")
r, phi = cmath.polar(complex(x, y))
print(f"cmath.polar  r {r:.4f}  phi {phi:.4f} rad = {math.degrees(phi):.2f} deg")
print(f"point (-x, -y): atan(y / x) {math.degrees(math.atan(-y / -x)):.2f} deg  atan2 {math.degrees(math.atan2(-y, -x)) % 360:.2f} deg")
print(f"radius 2: hypot {math.hypot(2 * x, 2 * y):.4f}  atan2 {math.degrees(math.atan2(2 * y, 2 * x)):.2f} deg")
```

```text
hypot 1.0000  atan2 46.25 deg
cmath.polar  r 1.0000  phi 0.8072 rad = 46.25 deg
point (-x, -y): atan(y / x) 46.25 deg  atan2 226.25 deg
radius 2: hypot 2.0000  atan2 46.25 deg
```

**Why the quadrant matters.** The point $(-0.6915, -0.7224)$ has the same ratio $y/x$, so $\tan^{-1}(y/x)$ alone returns 46.25° for it too. `atan2` returns 226.25°, the turn that reaches it. Use `atan2` whenever $x$ can be negative.

**`cmath.polar` on a complex number.** It returns the length and the turn in radians at once, 0.8072 here, the same arc length [[Radians]] measures. It wins when the point is already a complex number $x + iy$.

## Why polar coordinates matter

Navigation: ⬅️ [[#Other ways to convert]] | 📋 [[#Table of contents|TOC]] | [[#Polar coordinates taught in, applied in]] ➡️

**Where they are used.** The cosine schedule gives each post by its angle on the quarter circle with $r = 1$, so its two multipliers are $(\cos\theta, \sin\theta)$, the point's legs. At step 50 the pair is $(0.6916, 0.7223)$, the point at 46.25° to within 0.0001, as [[How The Quarter Circle Gives The Multipliers#Step 2: the point is the two multipliers|the quarter circle note]] works.

## Polar coordinates taught in, applied in

Navigation: ⬅️ [[#Why polar coordinates matter]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the `drip --math` walk of [the forward process and the score](../../../PhD/reduce-reuse-recycle/artifacts/drips/forward-process-and-the-score/00-INDEX.md) in the reduce-reuse-recycle research repository, piece 2, rung 1: the cosine from the high-school triangle up, on Cartesian planes with sampled points and lines, ending at a point given by its length and angle and read as $(x, y)$
- step 4 of the one-expert rebuild walk in the same repository, [On paper 2](../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-4-the-forward-process-and-the-cosine-schedule): polar coordinates, the two legs and Pythagoras

**Applied in:** [[How The Quarter Circle Gives The Multipliers#Step 2: the point is the two multipliers|the quarter circle under the cosine schedule]], where the point at post 51, $r = 1$ at 46.25°, is read as its two legs, step 50's two multipliers.

> [!note]- How this was checked
> The figure script and `back.py` were run on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and matplotlib 3.10.8 from the machine's `python3`, by vault-writer, in an empty folder under `~/playground/sandbox/` that was removed afterwards. The figure script printed the same line as when first filed in [[The Unit Circle]], and its SVG differs from the embedded one only in matplotlib's date stamp. The SVG was rasterised with PyMuPDF and opened.
>
> The trigonometry handbook's PDF pages 8 (the polar axis is the positive x-axis, a polar angle positive anticlockwise), 9 (cos θ = x / r, sin θ = y / r, tan θ = y / x) and 68 ($r = \sqrt{x^2 + y^2}$, $\theta = \tan^{-1}(y/x)$ adjusted to the quadrant, $x = r\cos\theta$, $y = r\sin\theta$) were opened and read as text with PyMuPDF. The scene frame anchor is as the walk's `dispatch.md` records it.
>
> No drawn picture is wanted: the picture here needs exact lengths and positions, so the SVG carries the form and the mechanism.
