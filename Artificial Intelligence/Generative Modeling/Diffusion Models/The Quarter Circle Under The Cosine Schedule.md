---
aliases: [quarter circle under the cosine schedule, the quarter circle under C_k, cosine schedule on the circle, cosine schedule by hand on paper, polar reading of the cosine schedule, quarter circle, the quarter arc, position ruler, the arc as a ruler, the position p_k, "p_k = (k + 0.8) / 100.8", posts on the quarter arc, why the offset delta, why s = 0.008 moves post 0 off the axis, post 100 at 90.72 degrees]
sources:
  - "Nichol, Dhariwal, Improved Denoising Diffusion Probabilistic Models, ICML 2021, section 3.2 and equation (17), PDF p. 4: https://arxiv.org/pdf/2102.09672#page=4"
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Trigonometry, radians and degrees, PDF p. 7; the unit circle, PDF p. 10; polar coordinates, PDF p. 68: ../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf"
standard: vault-note v2
---

# The Quarter Circle Under The Cosine Schedule

Up: [[Diffusion Models]] · ⬅️ [[Running The Cosine Noise Schedule]] · [[How The Quarter Circle Gives The Multipliers]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[The Unit Circle]] for the circle itself, [[Polar Coordinates#The point: from length and angle to x and y|polar coordinates]] for $(\cos\theta, \sin\theta)$ as a point's two legs, [[Radians]] for π/2 as the quarter arc, [[The Cosine Noise Schedule]] for the boundary values $C_k$, and [[The Forward Process]] for the jump $x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon$.

**Every boundary value of the cosine schedule sits at a post on a quarter of the unit circle, and the point at that post is the forward jump's two multipliers.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. It has no questions on this note yet.

> [!warning]- Unfinished
> - The deep-dive sheet is waiting: prompt 45 in the vault's `.prompts/Diffusion Models.md`, with its slot in [[How The Quarter Circle Gives The Multipliers]]. The form is drawn by the script of step 1 here and step 2's there, and the mechanism by that note's script.
> - The diffusion models quiz has no questions on this note yet.

Stated claims: 0.

**What this note draws.** The quarter circle itself and step 1 of the build, where the 101 posts go. [[How The Quarter Circle Gives The Multipliers]] draws step 2, the point at post 51, and [[The Quarter Turn And The Fraction]] draws steps 3 and 4.

**Where the scripts run.** Each figure script imports `plane.py` and `cosine.py` and needs matplotlib, so run it in the folder that [[Running The Quarter Circle Under The Cosine Schedule#Try the quarter circle yourself|step 3 of the sandbox]] makes.

**Colours in this note.** <span style="color:#2e7d32">**Green is $\cos\theta$, the horizontal leg, and its square, the share kept**</span>, <span style="color:#ef6c00">**orange is $\sin\theta$, the vertical leg, and its square, the noise share**</span>, <span style="color:#1565c0">**blue is a post, its position $p_k$ and its angle $\theta_k$**</span>, and <span style="color:#9e9e9e">**grey is a case with a piece removed**</span>, as in [[The Cosine Noise Schedule]].

## Table of contents

- [[#The quarter circle under C_k]]
- [[#Step 1: the position ruler]]
- [[#Try the quarter circle yourself]]
- [[#How the quarter circle gives the multipliers]]
- [[#Other ways to see the quarter circle]]
- [[#Why the quarter circle matters]]
- [[#The quarter circle taught in, applied in]]

## The quarter circle under C_k

Navigation: 📋 [[#Table of contents|TOC]] | [[#Step 1: the position ruler]] ➡️

Textbook: [Whitney, Trigonometry handbook, polar coordinates, PDF p. 68](../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf#page=68)

**The quarter circle under $C_k$**, also the cosine schedule on the circle or its polar reading, is the quarter of the unit circle that the schedule's 101 posts sit on.

**When to reach for it.** When a schedule number such as $\bar\alpha_{50} = 0.4783$ has to be checked with a ruler, or when you need to see why the two multipliers' squares add to 1.

### The posts and their table

<table>
<tr><th>post k</th><th style="color:#1565c0">position p<sub>k</sub></th><th style="color:#1565c0">angle θ<sub>k</sub></th><th style="color:#2e7d32">cos θ<sub>k</sub></th><th style="color:#ef6c00">sin θ<sub>k</sub></th><th style="color:#9e9e9e">angle with δ = 0</th></tr>
<tr><td>0</td><td style="border:2px solid #212121">0.0079</td><td style="border:2px solid #212121">0.714°</td><td>0.99992</td><td>0.0125</td><td style="border:2px dashed #212121">0°</td></tr>
<tr><td>1</td><td>0.0179</td><td>1.607°</td><td>0.99961</td><td>0.0280</td><td>0.9°</td></tr>
<tr style="background:#fff8e1"><td><b>51</b></td><td>0.5139</td><td>46.25°</td><td style="border:2px solid #212121"><b>0.6915</b></td><td style="border:2px solid #212121"><b>0.7224</b></td><td>45.9°</td></tr>
<tr><td>100</td><td style="border:2px solid #212121">1</td><td style="border:2px solid #212121">90°</td><td>0</td><td>1</td><td style="border:2px dashed #212121">90°</td></tr>
</table>

**How to read this table.** Each row is one fence post of the 100-step timetable. The position runs from 0 to 1 along the quarter arc, the angle is that position times 90°, and the last column is where the post would sit without the offset.

**What to look for.** The solid boxes at posts 0 and 100: the offset slides post 0 off the axis while post 100 stays on 90°. The highlighted row is the toy, whose point is step 50's two multipliers.

### Build the quarter circle by hand

**The arc.** The quarter arc is a piece of [[The Unit Circle#The circle: every point at distance 1|the unit circle]], drawn on [the plane with one point on the arc](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-plane). A point on it at angle θ is $(\cos\theta, \sin\theta)$, [[Polar Coordinates#The point: from length and angle to x and y|its two legs]], and the legs' squares add to 1, [[The Cosine Wave#The two shares|the two shares]].

**The angle as a length.** The angle can be read as [[Radians#Then the conversion: degrees to radians|an arc length]], so the quarter turn is π/2. Off the circle, $\cos^2$ is a function someone chose. On it, $\cos^2$ is [a length you can measure with a ruler](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step4-the-quarter-circle-by-hand), as the rebuild walk's "On paper 1 to 3" do by hand.

**The name, word by word.** "Quarter circle" is taken apart below: the circle first, then the quarter, then both together and what follows from them.

### The base word: circle

**What the word means.** A circle of radius 1 is every point at distance 1 from the origin, [[The Unit Circle#The circle: every point at distance 1|the unit circle]]:

$$
x^2 + y^2 = 1
$$

$$
\underbrace{\textcolor{#2e7d32}{x}^2}_{\text{horizontal leg, squared}}
+
\underbrace{\textcolor{#ef6c00}{y}^2}_{\text{vertical leg, squared}}
=
\underbrace{1}_{\text{the radius, squared}}
$$

**What the equation says.** Pythagoras on the triangle under any point: its two legs, squared, add to the radius squared. At post 51 the legs are 0.6915 and 0.7224, and $0.4782 + 0.5218 = 1$.

**Why the 1 is there.** The radius is 1, so the two squares split exactly 1 between them. On a circle of radius 2 the same angle gives legs 1.3830 and 1.4447, whose squares add to 4.

### Then the word: quarter

**What the word means.** A quarter circle is the part from 0° to 90°, where both legs are zero or positive. Its arc is π/2 = 1.5708 long, 15.71 cm on a 10 cm radius.

$$
0^\circ \le \theta \le 90^\circ
$$

$$
\underbrace{0^\circ}_{\text{on the x-axis}}
\le
\underbrace{\textcolor{#1565c0}{\theta}}_{\text{the angle}}
\le
\underbrace{90^\circ}_{\text{on the y-axis, }\pi/2}
$$

**What it means.** The schedule's angles run from 0.714° at post 0 to 90° at post 100, never past. On that stretch $\cos^2\theta$ falls once, from 1 to 0, so the share kept only ever goes down.

**Why only a quarter.** Past 90° the cosine turns negative and its square climbs back. Spread the posts over a half turn and post 51 sits at 92.50°, where $C_{51} = 0.0019$, while post 100 reaches 180° with $C_{100} = 1.0006$. The clean image would come back at the end.

### All the words together: the quarter circle

$$
(x, y) = (\cos\theta, \sin\theta), \qquad 0^\circ \le \theta \le 90^\circ
$$

$$
\big(\textcolor{#2e7d32}{x},\ \textcolor{#ef6c00}{y}\big)
=
\big(
\underbrace{\textcolor{#2e7d32}{\cos\theta}}_{\text{horizontal leg}},\
\underbrace{\textcolor{#ef6c00}{\sin\theta}}_{\text{vertical leg}}
\big),
\qquad
\underbrace{0^\circ \le \textcolor{#1565c0}{\theta} \le 90^\circ}_{\text{a quarter turn}}
$$

**What the equation says.** Every point of the quarter circle is named by one angle, and its two legs are the cosine and the sine of that angle. At 46.25° the point is (0.6915, 0.7224).

### The consequence: two shares of 1

On the circle the two squared legs always split 1 between them, and on the quarter both lie between 0 and 1:

$$
\cos^2\theta + \sin^2\theta = 1, \qquad 0 \le \cos^2\theta,\ \sin^2\theta \le 1
$$

$$
\underbrace{\textcolor{#2e7d32}{\cos^2\theta}}_{\text{share kept, close to }C_k}
+
\underbrace{\textcolor{#ef6c00}{\sin^2\theta}}_{\text{noise share, close to }1 - C_k}
=
1
$$

**What it means.** This is the split the forward jump needs: a share of the clean image's variance kept and a share of noise, adding to 1. [[The Cosine Wave#The two shares|The two shares]] proves the identity, and [[How The Quarter Circle Gives The Multipliers]] places the schedule's exact multipliers against it.

## Step 1: the position ruler

Navigation: ⬅️ [[#The quarter circle under C_k]] | 📋 [[#Table of contents|TOC]] | [[#Try the quarter circle yourself]] ➡️

**What step 1 does.** It places the [101 posts](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-posts) of the 100-step timetable on the quarter arc. "Position ruler" is two words: the ruler is the arc marked from 0 to 1, and a position is where one post sits on it.

### The base word: ruler

**What the word means.** Treat the quarter arc as a ruler, 0 on the x-axis and 1 on the y-axis, so a reading $p$ sits at angle $p \times 90^\circ$:

$$
\theta = p \cdot 90^\circ
$$

$$
\underbrace{\textcolor{#1565c0}{\theta}}_{\text{angle}}
=
\underbrace{\textcolor{#1565c0}{p}}_{\text{reading on the ruler, 0 to 1}}
\cdot
\underbrace{90^\circ}_{\text{the whole quarter, }\pi/2}
$$

**What the equation says.** The ruler's ticks 0, 0.25, 0.5, 0.75 and 1 sit at 0°, 22.5°, 45°, 67.5° and 90°. A reading of 0.5139 is 46.25°.

**Why the 90° is there.** It stretches the ruler's 1 to exactly the quarter turn. Read $p$ as radians instead and the ruler stops at 1 radian, 57.30°, where post 100 keeps 0.29194 of the signal, so the schedule never reaches pure noise.

### Then the word: position

**What the word means.** Each post $k$ gets its own reading on the ruler, its position $p_k$. Without the offset it is the fraction of the schedule done:

$$
p_k = k / T
$$

$$
\underbrace{\textcolor{#1565c0}{p_k}}_{\text{position of post }k}
=
\frac{\underbrace{k}_{\text{post number, 0 to 100}}}{\underbrace{T}_{\text{steps, 100}}}
$$

**What it means.** 101 posts mark the ends of 100 steps, like fence posts round 100 gaps, so the posts sit at 0, 0.01, …, 1. Each post sits 0.01 of the ruler, 0.9°, past the one before.

### All the words together: the position formula

The schedule adds an [offset](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-name-offset) δ = 0.008 and divides by 1 + δ. Post $k$ sits at [the schedule's position](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step4-where-the-position-goes):

$$
p_k = \frac{k/T + \delta}{1 + \delta} = \frac{k + 0.8}{100.8}, \qquad \theta_k = p_k \cdot 90^\circ
$$

$$
\underbrace{\textcolor{#1565c0}{p_k}}_{\text{position on the arc}}
=
\frac{
\underbrace{k/T}_{\text{post number as a fraction}}
+
\underbrace{\delta}_{\text{offset }0.008}
}{
\underbrace{1+\delta}_{\text{keeps post }T\text{ at }1}
}
=
\frac{k + 0.8}{100.8},
\qquad
\underbrace{\textcolor{#1565c0}{\theta_k}}_{\text{angle}}
=
p_k \cdot \underbrace{90^\circ}_{\pi/2}.
$$

**What the equation says.** Post 0 sits at 0.0079 of the way round (0.714°), post 51 at 0.5139 (46.25°) and post 100 at exactly 1 (90°). The frame on [where each post's position comes from](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-position-derived) moves every handle of this formula.

**Why the offset δ is there.** Adding 0.008 slides every post forward, so post 0 starts just off the x-axis, where $\cos^2$ is already falling. Without it the first step adds a noise share of 0.000247 instead of 0.000631, [[The Quarter Turn And The Fraction#The consequence: remove a piece|counted in the fraction note]].

**Why the division by 1 + δ is there.** It pulls the last post back to exactly 90°. Without it post 100 sits at 90.72° and keeps a share of 0.000158 instead of 0, as the rebuild walk shows when it [drops the rescale](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step4-dropping-the-rescale).

```python
import math
import matplotlib.pyplot as plt
from plane import save, BLUE, GREY, LIGHT_GREY
from cosine import T, delta, position, theta_deg


def no_division_deg(k):  # the position without the division by 1 + delta
    return (k / T + delta) * 90


for k in (0, 1, 51, 100):
    print(f"post {k:3d}  p {position(k):.4f}  {theta_deg(k):6.3f} deg    delta = 0: p {position(k, 0):.4f}  {theta_deg(k, 0):6.3f} deg"
          f"    no division: {no_division_deg(k):6.3f} deg")

fig, axs = plt.subplot_mosaic([["arc", "start"], ["arc", "end"]], figsize=(11, 5.5), width_ratios=[1.1, 1])
ax = axs["arc"]
ts = [math.radians(d / 4) for d in range(361)]
ax.plot([math.cos(t) for t in ts], [math.sin(t) for t in ts], color=LIGHT_GREY, lw=6)
for k in range(T + 1):
    t = math.radians(theta_deg(k))
    ax.plot(math.cos(t), math.sin(t), "o", color=BLUE, ms=3)
for p in (0, 0.25, 0.5, 0.75, 1):
    t = math.radians(p * 90)
    ax.plot([0.97 * math.cos(t), 1.03 * math.cos(t)], [0.97 * math.sin(t), 1.03 * math.sin(t)], color="black")
    ax.text(0.88 * math.cos(t), 0.88 * math.sin(t), f"{p:g}", ha="center", va="center", fontsize=10)
for k, label in ((0, "post 0, p = 0.0079, 0.714°"), (51, "post 51, p = 0.5139, 46.25°"), (100, "post 100, p = 1, 90°")):
    t = math.radians(theta_deg(k))
    ax.plot(math.cos(t), math.sin(t), "o", color=BLUE, ms=8)
    ax.text(1.08 * math.cos(t), 1.08 * math.sin(t) + 0.03, label, color=BLUE, fontsize=10)
ax.set_xlim(-0.05, 1.75)
ax.set_ylim(-0.1, 1.2)
ax.set_aspect("equal")
ax.spines[["top", "right"]].set_visible(False)
ax.set_title("the quarter arc as a ruler from 0 to 1: 101 posts", fontsize=12)

rows = ((2, BLUE, "o", lambda k: theta_deg(k)), (1, GREY, "o", lambda k: theta_deg(k, 0)), (0, GREY, "s", no_division_deg))
for name, lo, hi, ks in (("start", -0.2, 4.4, range(0, 6)), ("end", 86.0, 91.2, range(96, 101))):
    a = axs[name]
    for y, color, marker, angle_of in rows:
        for k in ks:
            a.plot(angle_of(k), y, marker, color=color, ms=7)
            a.text(angle_of(k), y + 0.3, str(k), ha="center", fontsize=9, color=color, clip_on=True)
    a.set_xlim(lo, hi)
    a.set_ylim(-0.6, 2.8)
    a.set_yticks([0, 1, 2], ["no ÷ (1 + δ)", "δ = 0", "δ = 0.008"])
    a.set_xlabel("angle in degrees")
    a.spines[["top", "right", "left"]].set_visible(False)
axs["end"].axvline(90, color="black", ls="--", lw=1)
axs["end"].text(90.05, 2.5, "90°, the y-axis", fontsize=9)
axs["end"].text(90.72, -0.55, "90.72°", ha="center", fontsize=9, color=GREY)
axs["start"].set_title("first posts: δ slides post 0 from 0° to 0.714°", fontsize=11)
axs["end"].set_title("last posts: without ÷ (1 + δ), post 100 overshoots to 90.72°", fontsize=11)
fig.tight_layout()
save(fig, "s1-position-ruler-posts.svg")
```

![Left, the quarter arc as a ruler from 0 to 1 with 101 blue posts and posts 0, 51 and 100 labelled with their positions and angles; right, two strips with one row per schedule, the first posts, where delta moves post 0 from 0 to 0.714 degrees, and the last posts, where both divided schedules end on 90 degrees and the schedule without the division by 1 + delta overshoots to 90.72 degrees|900](assets/s1-position-ruler-posts.svg)

**How to read this.** On the left both axes are in units of the radius, each blue dot is one post, and the black ticks are the ruler's 0, 0.25, 0.5, 0.75 and 1. On the right the x-axis is the angle in degrees, with one row per schedule: blue dots for the schedule, grey dots for δ = 0, grey squares for δ = 0.008 without ÷ (1 + δ), each numbered by its post.

**What to look at.** In the first strip, grey post 0 sits on 0° and blue post 0 on 0.714°. In the second, both rows of dots end on 90°, and the squares' post 100 overshoots to 90.72°.

### The consequence: move the posts

**What moves.** With δ = 0 the grey posts start on the x-axis, and the first step is 0.9° wide instead of 0.893°, beginning where $\cos^2$ is flat. Without the division by 1 + δ, post 100 overshoots to 90.72°.

**What it does to the point.** The point at each post moves with it, so both changes alter the multipliers. The figure zooms in on both ends of the arc, and [[The Quarter Turn And The Fraction#The consequence: remove a piece|the fraction note]] counts what each change does to the noise.

```python
import math
import matplotlib.pyplot as plt
from plane import BLUE, GREEN, GREY, LIGHT_GREY
from cosine import T, delta, theta_deg, C

plt.rcParams.update({"font.size": 11, "svg.fonttype": "path"})
BOX = dict(fc="white", ec="none", alpha=0.9, pad=1.5)
rad = math.radians


def no_division_deg(k):  # the position without the division by 1 + delta, times 90
    return (k / T + delta) * 90


def point(deg):
    return math.cos(rad(deg)), math.sin(rad(deg))


fig, (start, end) = plt.subplots(1, 2, figsize=(13, 5.5), gridspec_kw={"wspace": 0.3})
for ax, (lo, hi) in ((start, (-0.2, 1.95)), (end, (88.2, 90.75))):
    ts = [rad(lo + (hi - lo) * i / 400) for i in range(401)]
    ax.plot([math.cos(t) for t in ts], [math.sin(t) for t in ts], color=LIGHT_GREY, lw=4)

for deg, color, marker, text, xy in ((theta_deg(0), BLUE, "o", "post 0 at 0.714°", (0.99962, 0.0080)),
                                     (theta_deg(1), BLUE, "o", "post 1 at 1.607°", (0.99940, 0.0300)),
                                     (theta_deg(0, 0), GREY, "o", "δ = 0: post 0 at 0°, on the axis", (0.99925, 0.0040)),
                                     (theta_deg(1, 0), GREY, "o", "δ = 0: post 1 at 0.900°", (0.99962, 0.0190))):
    x, y = point(deg)
    start.plot(x, y, marker, color=color, ms=9)
    start.annotate(text, (x, y), xytext=xy, color=color, bbox=BOX, arrowprops={"arrowstyle": "-", "color": color})
start.axhline(0, color="black", lw=1)
start.text(0.99902, -0.0035, f"step 0 with δ: 0.893° wide, β₀ = {1 - C(1):.6f}\nwith δ = 0: 0.900° wide, β₀ = {1 - C(1, 0):.6f}",
           fontsize=10, bbox=BOX)
start.set_xlim(0.99900, 1.00006)
start.set_ylim(-0.006, 0.034)
start.set_title("the start: δ slides post 0 off the flat axis")

c100 = math.cos(rad(no_division_deg(100))) ** 2 / math.cos(rad(no_division_deg(0))) ** 2
for deg, color, marker, text, xy in ((theta_deg(100), BLUE, "o", "post 100 at 90°: leg 0, C₁₀₀ = 0", (0.0030, 1.000035)),
                                     (theta_deg(99), BLUE, "o", "post 99 at 89.107°", (0.0080, 0.99978)),
                                     (no_division_deg(100), GREY, "s",
                                      f"no ÷ (1 + δ): post 100 at 90.72°,\nleg cos 90.72° = {math.cos(rad(no_division_deg(100))):.4f}, C₁₀₀ = {c100:.6f}",
                                      (-0.0265, 0.99970)),
                                     (no_division_deg(99), GREY, "s", "no ÷: post 99 at 89.82°", (-0.0060, 0.99960))):
    x, y = point(deg)
    end.plot(x, y, marker, color=color, ms=9)
    end.annotate(text, (x, y), xytext=xy, color=color, bbox=BOX, arrowprops={"arrowstyle": "-", "color": color})
x, y = point(no_division_deg(100))
end.plot([0, x], [y, y], color=GREEN, lw=5)
end.text(x / 2, y + 0.000012, "leg left of the axis", color=GREEN, ha="center", fontsize=9)
end.axvline(0, color="black", ls="--", lw=1)
end.text(0.0004, 0.99952, "the y-axis, 90°", fontsize=9)
end.set_xlim(-0.031, 0.031)
end.set_ylim(0.99950, 1.00008)
end.set_title("the end: without ÷ (1 + δ), post 100 passes 90°")
for ax in (start, end):
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#eeeeee")
    ax.set_axisbelow(True)
    ax.ticklabel_format(useOffset=False)
start.set_xlabel("x, the horizontal leg (zoomed: 0.999 to 1)")
start.set_ylabel("y, the vertical leg")
end.set_xlabel("x, the horizontal leg")
end.set_ylabel("y, the vertical leg (zoomed: 0.9995 to 1)")
fig.savefig("quarter-circle-move-the-posts.svg", format="svg", bbox_inches="tight")
print("saved quarter-circle-move-the-posts.svg")
```

![Left, a zoomed window of the plane near (1, 0): blue posts 0 and 1 at 0.714 and 1.607 degrees on the arc, grey posts 0 and 1 with delta = 0 at 0 and 0.900 degrees, post 0 on the x-axis, and the first step's noise share 0.000631 against 0.000247; right, a zoomed window near (0, 1): blue post 100 on the y-axis at 90 degrees with C_100 = 0, grey post 100 without the division at 90.72 degrees left of the y-axis with its green horizontal leg cos 90.72 = -0.0126 and C_100 = 0.000158, and post 99 at 89.107 and 89.82 degrees|900](assets/quarter-circle-move-the-posts.svg)

**How to read this.** Each panel is a small window of the plane, stretched so the posts can be told apart, with the arc in light grey: blue is the schedule, grey the schedule with one piece removed. On the left, δ = 0 drops post 0 onto the x-axis, and the first step's noise share falls from 0.000631 to 0.000247.

**What to look at.** On the right, without ÷ (1 + δ) post 100 passes the y-axis to 90.72°. Its green horizontal leg points left, cos 90.72° = −0.0126, and its square keeps $C_{100} = 0.000158$ of the signal instead of 0.

## Try the quarter circle yourself

Navigation: ⬅️ [[#Step 1: the position ruler]] | 📋 [[#Table of contents|TOC]] | [[#How the quarter circle gives the multipliers]] ➡️

**In two lines.** Nine steps in an empty folder, from the plane and `cosine.py` to the six moves at post 51 in one run, each output read field by field, are in [[Running The Quarter Circle Under The Cosine Schedule#Try the quarter circle yourself]]. Its step 3 makes the folder that every figure script in this note runs in.

## How the quarter circle gives the multipliers

Navigation: ⬅️ [[#Try the quarter circle yourself]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to see the quarter circle]] ➡️

**In two lines.** Step 2 of the build, [[How The Quarter Circle Gives The Multipliers#Step 2: the point is the two multipliers|the point at post 51 as step 50's two multipliers]], and why that pair lies exactly on the circle and 0.0001 off the drawn point are in [[How The Quarter Circle Gives The Multipliers#How the quarter circle gives the multipliers]]. Its mechanism figure draws the quarter turn every 15°, the point at post 51 and the fraction in one picture.

## Other ways to see the quarter circle

Navigation: ⬅️ [[#How the quarter circle gives the multipliers]] | 📋 [[#Table of contents|TOC]] | [[#Why the quarter circle matters]] ➡️

**Drag it.** The scene Dissolving the Dog slides [the posts with δ](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-posts), and its [polar-coordinates frame](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-polar) draws the point's two legs.

**Only the numbers.** [[The Cosine Noise Schedule]] reads the same formula without the drawing, and is faster once the picture is in your head.

## Why the quarter circle matters

Navigation: ⬅️ [[#Other ways to see the quarter circle]] | 📋 [[#Table of contents|TOC]] | [[#The quarter circle taught in, applied in]] ➡️

**A circle keeps the total at 1.** The forward process mixes a clean image and noise so that their variance shares always add to 1, and a point on a circle of radius 1 is the simplest object with that property.

**What the drawing buys.** Once the schedule is a point walking a quarter turn, $0.6916$ and $0.7223$ at step 50 are two lengths you can measure on a 10 cm drawing. The offset is a small correction to where the walk begins.

## The quarter circle taught in, applied in

Navigation: ⬅️ [[#Why the quarter circle matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the [`drip --math` walk of the forward process and the score](../../../../PhD/reduce-reuse-recycle/artifacts/drips/forward-process-and-the-score/00-INDEX.md) in the reduce-reuse-recycle research repository, piece 2, rung 1: the learner's request to rebuild the boundary values from a Cartesian plane (the circle, the legs, the angle in degrees and radians, the position ruler), and then to see each step as a Python-drawn figure beside the code that drew it; and its [rung on where $p_k$ comes from](../../../../PhD/reduce-reuse-recycle/artifacts/drips/forward-process-and-the-score/kept/06-where-p-k-comes-from.md), as the walk kept it
- [step 4 of the one-expert rebuild walk](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-4-the-forward-process-and-the-cosine-schedule) in the same repository, its [On paper 4, where the position goes](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step4-where-the-position-goes), and On paper 5, the point at 46.25°

**Applied in:** wherever [[The Cosine Noise Schedule]] is applied: [step 4 of the one-expert rebuild walk](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-4-the-forward-process-and-the-cosine-schedule), whose [`cosine_beta_schedule`](../../../../PhD/reduce-reuse-recycle/rebuild/model.py) (lines 13 to 19) lays out the 100 noise levels one diffusion expert is trained on.

> [!note]- How this was checked
> The sandbox scripts and their outputs are checked in [[Running The Quarter Circle Under The Cosine Schedule]], whose box records the run.
>
> The two figure scripts here were run on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and matplotlib 3.10.8 from the machine's `python3`, in an empty `~/playground/sandbox/quarter-circle-retrofit` holding `plane.py` and the sandbox's `cosine.py`, by vault-writer, and the folder was removed afterwards. Each SVG was rendered to PNG by PyMuPDF and opened before filing. Step 1's figure here and step 2's in [[How The Quarter Circle Gives The Multipliers]] draw the form and replace prompt 43 in `.prompts/Diffusion Models.md`.
>
> The with-and-without numbers were computed that day by a throwaway script on the same `cosine.py`: radius 2, squares adding to 4.0000; the posts over a half turn, post 51 at 92.50° with $C_{51} = 0.0019$ and post 100 at 180° with $C_{100} = 1.0006$; $p$ read as radians, post 100 at 57.30° keeping 0.29194; and, without the division by $1 + \delta$, posts 0, 1, 51 and 100 at 0.720°, 1.620°, 46.620° and 90.720°, $\cos 90.72^\circ = -0.0126$ and $C_{100} = \cos^2 90.72^\circ / \cos^2 0.72^\circ = 0.000158$. The table's sine column and the stretch 1.00008 come from the same `cosine.py`.
>
> The trigonometry handbook's PDF pages 10 (the unit circle) and 68 (polar coordinates) were opened and read as text. Nichol and Dhariwal's page 4 was read as for [[The Cosine Noise Schedule]]. The scene frame anchors are as the walk's `dispatch.md` and the retrofit brief record them. No tldr-pages entry covers this.
