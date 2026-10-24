---
aliases: [radian, radians, rad, degrees and radians, degrees to radians, "rad = deg × π / 180", "rad = deg * pi / 180", radians as arc length, arc length, "s = r θ", one radian, "1 rad = 57.30°", "π/2 = 90°", the quarter turn in radians, math.radians, degrees fed in as radians]
sources:
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Trigonometry, version 2.4, radians and degrees, 2π radians in one rotation, one radian as the radius wrapped along the circle, the measure of an arc S = rθ, PDF p. 7: ../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=7"
  - "Anton, Bivens, Davis, Calculus, Appendix B, θ = s / r and s = rθ when θ is in radians, PDF p. 1207: ../references/textbooks/calculus/calculus-textbook.pdf#page=1207; section 2.5, the variable of the trigonometric functions measured in radians, PDF p. 193: ../references/textbooks/calculus/calculus-textbook.pdf#page=193"
  - "Python documentation, math.cos (cosine of x radians) and math.radians: https://docs.python.org/3/library/math.html#trigonometric-functions"
standard: vault-note v2
---

# Radians

Up: [[Trigonometry]] · ⬅️ [[Running The Unit Circle]] · [[The Cosine Wave]] ➡️

Mathematics, Trigonometry. Needs: [[The Unit Circle#The angle: one line from the origin|an angle as one line turned from the origin]].

**A radian measures an angle by the length of arc it cuts from a circle of radius 1.**

> [!question]- Test yourself
> No quiz page covers this note yet.

> [!warning]- Unfinished
> - No quiz page for this note yet.

Stated claims: 0.

**The toy angle.** Every number here is worked at 46.25°, the angle of post 51 in [[The Quarter Circle Under The Cosine Schedule]], which is 0.8072 radians. The quarter turn, 90°, is π/2 = 1.5708.

**Colours, the same in every equation and figure.** <span style="color:#6d4c41">**Brown is arc length, the angle in radians**</span>, <span style="color:#1565c0">**blue is the line from the origin and the angle in degrees**</span>, <span style="color:#2e7d32">**green is the cosine**</span>, and <span style="color:#9e9e9e">**grey is a case drawn for comparison**</span>. Brown means arc length in [[How The Quarter Circle Gives The Multipliers]] too, where purple is the denominator $\cos^2\theta_0$.

## Table of contents

- [[#The angle as a length]]
- [[#When to reach for radians]]
- [[#Try radians yourself]]
- [[#Reading the radians output]]
- [[#How radians work]]
- [[#Other ways to convert an angle]]
- [[#Why radians matter]]
- [[#Radians taught in, applied in]]

## The angle as a length

Navigation: 📋 [[#Table of contents|TOC]] | [[#When to reach for radians]] ➡️

Textbook: [Whitney, Trigonometry handbook, radians and degrees, PDF p. 7](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=7)

**Radian**, also rad, the angle as an arc length, or one radian: the angle whose arc is as long as the circle's radius, 57.30°. Measured in radians, an angle is the length of arc it cuts on radius 1, so a whole turn is $2\pi$ and the quarter turn is $\pi/2$.

**The arc laid flat.** The scene Dissolving the Dog [highlights the arc 0.8072 and lays it flat beside π/2 = 1.5708](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-radians), the whole quarter arc. It is the string of the table below, on radius 1.

### The angles and their arcs

<table>
<tr><th>degrees</th><th style="color:#6d4c41">radians</th><th style="color:#6d4c41">string on a 10 cm radius</th></tr>
<tr><td>0°</td><td>0</td><td>0 cm</td></tr>
<tr><td>15°</td><td>0.2618</td><td>2.62 cm</td></tr>
<tr><td>45°</td><td>0.7854</td><td>7.85 cm</td></tr>
<tr style="background:#fff8e1"><td><b>46.25°</b></td><td style="border:2px solid #212121"><b>0.8072</b></td><td style="border:2px solid #212121">8.07 cm</td></tr>
<tr><td>57.30°</td><td style="border:2px dashed #212121">1</td><td>10 cm, one radius</td></tr>
<tr><td>90°</td><td style="border:2px solid #212121">π/2 = 1.5708</td><td style="border:2px solid #212121">15.71 cm</td></tr>
<tr><td>180°</td><td>π = 3.1416</td><td>31.42 cm</td></tr>
<tr><td>360°</td><td>2π = 6.2832</td><td>62.83 cm</td></tr>
</table>

**How to read this table.** Each row is one angle measured twice: with a protractor in degrees, and with a string laid along the arc. The string column is the radian column times 10, because the radius is 10 cm.

**What to look for.** The boxed cells are the ones the cosine schedule uses: 46.25° at post 51 and the whole quarter turn. The dashed cell is one radian, the arc as long as the radius.

### The base word: radian

$$
s = r\,\theta
$$

$$
\underbrace{\textcolor{#6d4c41}{s}}_{\text{arc length}}
=
\underbrace{r}_{\text{radius}}\;
\underbrace{\textcolor{#6d4c41}{\theta}}_{\text{angle in radians}},
\qquad
\textcolor{#6d4c41}{0.8072} = 1 \cdot \textcolor{#6d4c41}{0.8072}
$$

**What the equation says.** On a circle of radius $r$, an angle of θ radians cuts an [arc of length](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=7) $r\theta$. With $r = 1$ the arc and the angle are the same number.

**Why the radius is there.** Draw the same 46.25° on a circle of radius 10 cm and the arc is $10 \cdot 0.8072 = 8.07$ cm. Without the radius the arc would be 0.8072 on every circle, its length only on radius 1. Dividing the arc by the radius, [θ = s / r](../references/textbooks/calculus/calculus-textbook.pdf#page=1207), gives 0.8072 at any size.

### Then the conversion: degrees to radians

$$
\theta_{\text{rad}} = \theta_{\text{deg}} \cdot \frac{\pi}{180}
$$

$$
\underbrace{\textcolor{#6d4c41}{\theta_{\text{rad}}}}_{\text{arc on radius }1}
=
\underbrace{\textcolor{#1565c0}{\theta_{\text{deg}}}}_{\text{protractor reading}}
\cdot
\underbrace{\frac{\pi}{180}}_{\text{radians per degree}}
=
\textcolor{#1565c0}{46.25} \cdot 0.017453
=
\textcolor{#6d4c41}{0.8072}
$$

**What the equation says.** Multiply degrees by π/180 to get radians. A quarter turn is $90 \cdot \pi/180 = \pi/2 = 1.5708$.

**Why π/180 is there.** A whole turn is 360° and also the whole circumference, $2\pi r$, which is $2\pi$ on radius 1, so one degree is $2\pi / 360 = \pi / 180 = 0.017453$ of a radian. With it, 46.25° becomes 0.8072 and the cosine is 0.6915. Without it, 46.25 is read as radians, so [[#The consequence: degrees fed in as radians|the line turns seven whole times and stops at 129.93°]], where the cosine is −0.6418.

```python
import math
from plane import plane, save, circle, angle, rad, BLUE

BROWN, LIGHT_BROWN = "#6d4c41", "#d7ccc8"  # arc length, as in the cosine schedule notes

for deg in (46.25, 90, math.degrees(1)):
    print(f"{deg:8.4f} deg  x pi / 180 = {deg * math.pi / 180:.4f} rad  = arc length on radius 1")

fig, ax = plane((-0.25, 1.4), (-0.25, 1.3))
circle(ax, upto=90)
for upto, lw, color in ((90, 7, LIGHT_BROWN), (46.25, 5, BROWN)):
    ts = [rad(d / 10) for d in range(0, int(upto * 10) + 1)]
    ax.plot([math.cos(t) for t in ts], [math.sin(t) for t in ts], color=color, lw=lw)
ax.plot([0, math.cos(rad(46.25))], [0, math.sin(rad(46.25))], color=BLUE, lw=2)
ax.plot([0, math.cos(1)], [0, math.sin(1)], color=BLUE, lw=1, ls=(0, (4, 3)))
angle(ax, 46.25, r=0.22)
ax.text(0.25, 0.08, "46.25°", color=BLUE)
ax.text(0.98, 0.42, "arc 0.8072\n= 0.8072 rad", color=BROWN)
ax.text(0.62, 0.92, "1 rad = 57.30°:\narc as long\nas the radius", color=BLUE, fontsize=9)
ax.text(-0.2, 1.1, "whole quarter arc: π/2 = 1.5708 rad = 90°", color=BROWN, fontsize=10)
ax.set_title("rad = deg × π / 180: 46.25 × π / 180 = 0.8072", fontsize=12)
save(fig, "t4-degrees-and-radians-arc.svg")
```

![A quarter of the unit circle with the arc from 0 to 46.25 degrees drawn thick brown and labelled 0.8072 rad, the rest of the quarter arc pale brown labelled pi over 2 = 1.5708 rad = 90 degrees, and a dashed line at one radian, 57.30 degrees|600](assets/t4-degrees-and-radians-arc.svg)

**How to read this.** Both axes are in units of the radius. The dark brown arc is 46.25° as a length, 0.8072 of a radius, and the pale arc runs on to the y-axis, the whole quarter turn, 1.5708. The dashed blue line marks where the arc reaches exactly one radius, at 57.30°.

### The consequence: degrees fed in as radians

Python's [`math.cos`](https://docs.python.org/3/library/math.html#math.cos) reads its input as radians. Give it the degree reading and it turns 46.25 radians instead:

$$
46.25 = 7 \cdot 2\pi + 2.2677, \qquad \cos(46.25) = -0.6418
$$

$$
\underbrace{46.25\ \text{rad}}_{\text{the degree number, read as radians}}
=
\underbrace{7 \cdot 2\pi}_{\text{seven whole turns},\ 43.9823}
+
\underbrace{\textcolor{#9e9e9e}{2.2677\ \text{rad}}}_{129.93^\circ}
\quad\Longrightarrow\quad
\cos(46.25) = \textcolor{#9e9e9e}{-0.6418}
\ \text{ against }\
\cos(\textcolor{#6d4c41}{0.8072}) = \textcolor{#2e7d32}{0.6915}
$$

**What goes wrong.** Whole turns change nothing, so the line ends at 129.93°, in the upper-left quarter, and its cosine is negative. Every later number built on it is wrong too: its square, $0.6418^2 = 0.4119$, is not the 0.4782 the schedule needs.

**Why the seven turns are there.** They are the part of 46.25 that brings the line back where it started. Take them away and $\cos(2.2677)$ is −0.6418, the same as $\cos(46.25)$.

```python
import math
from plane import plane, save, circle, rad, GREEN, BLUE, GREY

right = rad(46.25)
wrong = 46.25 % (2 * math.pi)
print(f"math.cos(math.radians(46.25)) = {math.cos(right):.4f}")
print(f"math.cos(46.25)               = {math.cos(46.25):.4f}  (46.25 rad = 7 turns + {wrong:.4f} rad = {math.degrees(wrong):.2f} deg)")

fig, ax = plane((-1.3, 1.3), (-0.45, 1.3))
circle(ax)
for t, color, label, dx in ((right, BLUE, "converted: 46.25°", 0.05), (wrong, GREY, f"not converted:\n46.25 rad lands at {math.degrees(wrong):.2f}°", -0.75)):
    x, y = math.cos(t), math.sin(t)
    ax.plot([0, x], [0, y], color=color, lw=2.5)
    ax.plot(x, y, "o", color=color, ms=8)
    ax.plot([x, x], [0, y], ":", color=GREEN)
    ax.text(x + dx, y + 0.08, label, color=color, fontsize=10)
    ax.text(x, -0.3, f"cos = {math.cos(t):.4f}", color=GREEN, ha="center", fontsize=10)
ax.set_title("cos reads its input in radians: 46.25 fed as degrees goes wrong", fontsize=12)
save(fig, "t8-degrees-fed-as-radians.svg")
```

![The unit circle with a blue line at 46.25 degrees whose cosine is 0.6915 and a grey line at 129.93 degrees, where 46.25 radians lands, whose cosine is -0.6418|600](assets/t8-degrees-fed-as-radians.svg)

**How to read this.** The x-axis runs from −1.3 to 1.3, so a point left of the y-axis has a negative cosine. The blue line is the angle converted first; the grey one is the same number taken as radians. Look at the two green readings: 0.6915 against −0.6418.

## When to reach for radians

Navigation: ⬅️ [[#The angle as a length]] | 📋 [[#Table of contents|TOC]] | [[#Try radians yourself]] ➡️

**An angle is going into code or calculus.** [`math.cos`](https://docs.python.org/3/library/math.html#math.cos) reads its input as radians, and calculus [measures trigonometric angles in radians](../references/textbooks/calculus/calculus-textbook.pdf#page=193). Convert a protractor reading before it goes in.

**What goes wrong without them.** 46.25 fed in as it stands gives −0.6418 where 0.6915 was meant, as [[#The consequence: degrees fed in as radians]] draws.

## Try radians yourself

Navigation: ⬅️ [[#When to reach for radians]] | 📋 [[#Table of contents|TOC]] | [[#Reading the radians output]] ➡️

**Where you work.** Python 3 with matplotlib, in the folder [[Running The Unit Circle#Try the unit circle yourself]] makes, with its `plane.py`.

**1. What you need.** Python 3 with matplotlib, checked by [[Running The Unit Circle#Try the unit circle yourself]], step 1.

**2. When it is missing.** Step 2 there says how to make the prepared environment.

**3. The setup.** Work in the folder that note's step 3 makes, with [plane.py](sandbox/plane.py) in it. Save the two scripts above as `t4_radians.py` and `t8_forgot_radians.py`.

**4. A look before: three angles as arcs.**

```bash
python3 t4_radians.py
```

```text
 46.2500 deg  x pi / 180 = 0.8072 rad  = arc length on radius 1
 90.0000 deg  x pi / 180 = 1.5708 rad  = arc length on radius 1
 57.2958 deg  x pi / 180 = 1.0000 rad  = arc length on radius 1
saved t4-degrees-and-radians-arc.svg
```

**5. The failure: degrees fed in as radians.**

```bash
python3 t8_forgot_radians.py
```

```text
math.cos(math.radians(46.25)) = 0.6915
math.cos(46.25)               = -0.6418  (46.25 rad = 7 turns + 2.2677 rad = 129.93 deg)
saved t8-degrees-fed-as-radians.svg
```

**6. The technique: multiply by π/180, or let `math.radians` do it.**

```bash
python3 -c "import math; print(46.25 * math.pi / 180, math.radians(46.25))"
```

```text
0.8072147790473774 0.8072147790473774
```

**7. Another way: measure the string.** On a 10 cm radius the arc is 10 times the radians:

```bash
python3 -c "import math; print(round(10 * math.radians(46.25), 2), round(10 * math.pi / 2, 2))"
```

```text
8.07 15.71
```

**8. More worked examples: back from radians to degrees.**

```bash
python3 -c "import math; print(round(math.degrees(1), 4), round(math.degrees(0.8072), 4))"
```

```text
57.2958 46.2492
```

**9. Clean up, and prove it.** [[Running The Unit Circle#Try the unit circle yourself]], step 9, removes the folder and checks it is gone.

## Reading the radians output

Navigation: ⬅️ [[#Try radians yourself]] | 📋 [[#Table of contents|TOC]] | [[#How radians work]] ➡️

| Step | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 4 | `46.2500 deg` | `0.8072 rad` | the arc post 51's angle cuts on radius 1 | derived below |
| 4 | `90.0000 deg` | `1.5708 rad` | the whole quarter arc, π/2 | derived below |
| 4 | `57.2958 deg` | `1.0000 rad` | one radian, the arc as long as the radius | derived below |
| 5 | `math.cos(46.25)` | `-0.6418` | 46.25 read as radians: 7 turns plus 2.2677 rad, at 129.93° | shown |
| 6 | both columns | `0.8072147790473774` | the formula and `math.radians` agree to the last digit | shown |
| 7 | `8.07 15.71` | cm | the string on a 10 cm radius for 46.25° and 90° | derived below |
| 8 | `46.2492` | deg | 0.8072 is a rounded radian, so it comes back 0.0008° short | shown |

## How radians work

Navigation: ⬅️ [[#Reading the radians output]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to convert an angle]] ➡️

Textbook: [Whitney, Trigonometry handbook, the measure of an arc S = rθ, PDF p. 7](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=7)

**The derivation, one step per line.** The circumference of a circle of radius $r$ is $2\pi r$, and one whole turn sweeps all of it. An angle that sweeps a share of the turn sweeps the same share of the circumference.

$$
\begin{aligned}
\text{circumference} &= 2\pi r \\
\text{share of the turn} &= \frac{\theta_{\text{deg}}}{360} \\
s &= 2\pi r \cdot \frac{\theta_{\text{deg}}}{360} \\
&= r \cdot \theta_{\text{deg}} \cdot \frac{\pi}{180} \\
&= r\,\theta_{\text{rad}} \\
1^\circ &= \frac{\pi}{180}\ \text{rad}, \qquad 1\ \text{rad} = \frac{180}{\pi}\ \text{degrees}
\end{aligned}
$$

$$
\begin{aligned}
\text{circumference} &= \underbrace{2\pi r}_{\text{one whole turn}} \\
\text{share of the turn} &= \underbrace{\frac{\textcolor{#1565c0}{\theta_{\text{deg}}}}{360}}_{\text{protractor reading over a full turn}} \\
\textcolor{#6d4c41}{s} &= \underbrace{2\pi r \cdot \frac{\textcolor{#1565c0}{\theta_{\text{deg}}}}{360}}_{\text{the same share of the circumference}} \\
&= r \cdot \underbrace{\textcolor{#1565c0}{\theta_{\text{deg}}} \cdot \frac{\pi}{180}}_{2\pi/360 \,=\, \pi/180} \\
&= r\,\underbrace{\textcolor{#6d4c41}{\theta_{\text{rad}}}}_{\text{call that the angle in radians}} \\
1^\circ &= \underbrace{\frac{\pi}{180}\ \text{rad}}_{0.017453\ \text{rad}}, \qquad 1\ \text{rad} = \underbrace{\frac{180}{\pi}\ \text{degrees}}_{57.2958^\circ}
\end{aligned}
$$

**What the derivation says.** The degree reading times π/180 is the angle in radians, and the arc is the radius times it, $s = r\theta$, as the [handbook derives](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=7). A whole turn is both 360° and $2\pi$ radians, which gives the last line.

**The worked numbers.**

$$
\begin{aligned}
\textcolor{#1565c0}{46.25} \cdot \frac{\pi}{180} &= \textcolor{#6d4c41}{0.8072} \\
\textcolor{#1565c0}{90} \cdot \frac{\pi}{180} &= \frac{\pi}{2} = \textcolor{#6d4c41}{1.5708} \\
\textcolor{#6d4c41}{s} = 10 \cdot \textcolor{#6d4c41}{0.8072} &= 8.07\ \text{cm on a 10 cm radius}
\end{aligned}
$$

## Other ways to convert an angle

Navigation: ⬅️ [[#How radians work]] | 📋 [[#Table of contents|TOC]] | [[#Why radians matter]] ➡️

**`numpy.deg2rad` and `numpy.rad2deg`.** They convert many angles at once, so they win when the angles sit in an array:

```bash
python3 -c "import numpy as np; print(np.deg2rad([46.25, 90]), np.rad2deg(1))"
```

```text
[0.80721478 1.57079633] 57.29577951308232
```

**Stay in fractions of a turn.** The schedule's code writes the angle as a position from 0 to 1 times `math.pi / 2`, so it never passes through degrees: [[The Quarter Circle Under The Cosine Schedule#Step 1: the position ruler|the position ruler]].

**Drag it.** The scene Dissolving the Dog, [frame "radians"](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-radians), measures the angle both ways.

## Why radians matter

Navigation: ⬅️ [[#Other ways to convert an angle]] | 📋 [[#Table of contents|TOC]] | [[#Radians taught in, applied in]] ➡️

**Where they are used.** Every `cos` in code takes radians, so the π/2 in the cosine schedule's formula is the quarter turn written as an arc. Calculus [measures trigonometric angles in radians](../references/textbooks/calculus/calculus-textbook.pdf#page=193) too, and that is what makes the slope of $\cos\theta$ equal $-\sin\theta$, which [[The Cosine Wave]] uses to show where $\cos^2$ is flat.

## Radians taught in, applied in

Navigation: ⬅️ [[#Why radians matter]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the `drip --math` walk of [the forward process and the score](../../../PhD/reduce-reuse-recycle/artifacts/drips/forward-process-and-the-score/00-INDEX.md) in the reduce-reuse-recycle research repository, [piece 2, rung 1 as the walk kept it](../../../PhD/reduce-reuse-recycle/artifacts/drips/forward-process-and-the-score/kept/05-the-cosine-boundary-values-by-hand.md): degrees and radians, the string along the arc, and the quarter turn as π/2
- step 4 of the one-expert rebuild walk in the same repository, [On paper 3: measure the angle twice](../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-4-the-forward-process-and-the-cosine-schedule)

**Applied in:** [[The Quarter Circle Under The Cosine Schedule]] and [[The Cosine Noise Schedule]], whose formula multiplies a position by π/2.

> [!note]- How this was checked
> The two figure scripts and the four one-line commands were run on 2026-10-21 on mscluster (Linux), with Python 3.12.10, numpy 2.4.3 and matplotlib 3.10.8 from the machine's `python3`, by vault-writer, in the empty folder `~/playground/sandbox/radians-v2`, which was removed afterwards. The prepared environment `~/.vault-sandbox` is missing on this machine. Every output above is that run's text, and the with-and-without numbers (7 · 2π = 43.9823, $\cos(2.2677) = -0.6418$, π/180 = 0.017453) were printed by the same `python3`.
>
> Each SVG was rasterised with PyMuPDF and opened, and a matplotlib PNG twin was opened to check the dashed line. The arc colour is brown, `#6d4c41`, held in the figure script itself: `plane.py` keeps its `PURPLE`, which [[The Quarter Turn And The Fraction]] and [[How The Quarter Circle Gives The Multipliers]] import for the denominator. The square 0.4119 is $0.6418^2$; the unrounded cosine squares to 0.41197.
>
> The trigonometry handbook's PDF page 7 (360° and 2π in one rotation, one radian as the radius wrapped along the circle, S = rθ) and the calculus textbook's PDF pages 1207 (θ = s / r) and 193 (the variable in sin x and cos x measured in radians) were opened and read as text with PyMuPDF. The Python documentation's math page states that `math.cos(x)` returns the cosine of x radians. The scene frame anchor is as the walk's `dispatch.md` records it.
>
> No tldr-pages entry covers this. No drawn picture is wanted: both pictures need exact arc lengths, angles and cosine readings, so the two SVGs carry the form and the mechanism.
