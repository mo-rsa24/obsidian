---
aliases: [how the quarter circle gives the multipliers, the point is the two multipliers, signal multiplier and noise multiplier on the circle, the multipliers' point, the multipliers lie on the circle, "(sqrt(C_k))^2 + (sqrt(1 - C_k))^2 = 1", share is multiplier squared, the stretch 1.00008, the quarter circle's mechanism, the multipliers at post 51 worked]
sources:
  - "Nichol, Dhariwal, Improved Denoising Diffusion Probabilistic Models, ICML 2021, section 3.2 and equation (17), PDF p. 4: https://arxiv.org/pdf/2102.09672#page=4"
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Trigonometry, the unit circle, PDF p. 10; polar coordinates, PDF p. 68: ../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf"
standard: vault-note v2
---

# How The Quarter Circle Gives The Multipliers

Up: [[Diffusion Models]] · ⬅️ [[The Quarter Circle Under The Cosine Schedule]] · [[Running The Quarter Circle Under The Cosine Schedule]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[The Quarter Circle Under The Cosine Schedule]] for the posts and where post 51 sits, [[The Forward Process]] for the jump $x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon$, and [[The Scaling Rule For Variance#Scaling a draw scales its variance by the square|the scaling rule]] for why a multiplier squared is a share.

**The point at each post is the forward jump's two multipliers, to within 0.0001, and the multipliers themselves lie exactly on the circle.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. It has no questions on this note yet.

> [!warning]- Unfinished
> - The deep-dive sheet is waiting: prompt 45 in the vault's `.prompts/Diffusion Models.md`, with its slot at the end of [[#The quarter circle's mechanism]].
> - The diffusion models quiz has no questions on this note yet.

Stated claims: 0.

**What this note does.** It draws step 2 of the build, the point at post 51, then shows why the multipliers sit on the circle and how far they sit from the drawn point. Its mechanism figure puts the quarter turn, the point and the fraction in one picture.

**Where the numbers come from.** Every printed number is an output of [[Running The Quarter Circle Under The Cosine Schedule]] or of the two figure scripts here. Each script imports the `plane.py` and `cosine.py` of [[Running The Quarter Circle Under The Cosine Schedule#Try the quarter circle yourself|step 3 of the sandbox]] and needs matplotlib.

**Colours in this note.** <span style="color:#2e7d32">**Green is $\cos\theta$, the horizontal leg, the clean point's multiplier $\sqrt{C_k} = \sqrt{\bar\alpha}$ and the share kept**</span>, <span style="color:#ef6c00">**orange is $\sin\theta$, the vertical leg, the noise multiplier $\sqrt{1 - \bar\alpha}$ and the noise share**</span>, <span style="color:#1565c0">**blue is a post and its angle $\theta_k$**</span>, <span style="color:#6a1b9a">**purple is the denominator $\cos^2\theta_0$**</span>, and <span style="color:#6d4c41">**brown is arc length, the string along the arc**</span>, as in [[The Cosine Noise Schedule]]. Brown is arc length, as in [[Radians]], and purple is the denominator.

## Table of contents

- [[#Step 2: the point is the two multipliers]]
- [[#How the quarter circle gives the multipliers]]
- [[#The quarter circle's mechanism]]

## Step 2: the point is the two multipliers

Navigation: 📋 [[#Table of contents|TOC]] | [[#How the quarter circle gives the multipliers]] ➡️

Textbook: [Whitney, Trigonometry handbook, polar coordinates, PDF p. 68](../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf#page=68)

At post 51 the point on the arc is, to within 0.0001, the pair of numbers the forward jump at step 50 multiplies by:

$$
(\cos 46.25^\circ,\ \sin 46.25^\circ) = (0.6915,\ 0.7224) \approx \big(\sqrt{\bar\alpha_{50}},\ \sqrt{1 - \bar\alpha_{50}}\big) = (0.6916,\ 0.7223)
$$

$$
\big(\textcolor{#2e7d32}{\cos 46.25^\circ},\ \textcolor{#ef6c00}{\sin 46.25^\circ}\big)
=
(0.6915,\ 0.7224)
\approx
\Big(
\underbrace{\textcolor{#2e7d32}{\sqrt{\bar\alpha_{50}}}}_{\text{clean point's multiplier, }0.6916},\
\underbrace{\textcolor{#ef6c00}{\sqrt{1-\bar\alpha_{50}}}}_{\text{noise multiplier, }0.7223}
\Big)
$$

**What the equation says.** [The two legs](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-polar) are the point's coordinates: the horizontal leg is how much of the clean image survives in $x_{50}$, and the vertical leg is how much noise is mixed in. Their squares, 0.4782 and 0.5218, are the kept share and the noise share, and they add to 1.

**Why only to within 0.0001.** The schedule divides by $\cos^2\theta_0 = 0.99984$, which stretches every multiplier $\sqrt{C_k}$ by $1/0.99992 = 1.00008$. At post 51 that moves 0.6915 to 0.6916.

**Why the string is there.** The angle 46.25° is 0.8072 rad, an arc 8.07 cm long on a 10 cm radius. The walk's "On paper 3" measures it with [a string along the arc](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-radians).

```python
import math
from plane import plane, save, circle, angle, GREEN, ORANGE, BLUE
from cosine import theta_deg, C

BROWN = "#6d4c41"  # arc length, the string
deg = theta_deg(51)
x, y = math.cos(math.radians(deg)), math.sin(math.radians(deg))
print(f"post 51 at {deg:.2f} deg: point ({x:.4f}, {y:.4f})")
print(f"multipliers: sqrt(abar_50) = sqrt(C_51) = {math.sqrt(C(51)):.4f}   sqrt(1 - abar_50) = {math.sqrt(1 - C(51)):.4f}")
print(f"string along the arc: {math.radians(deg):.4f} rad = {10 * math.radians(deg):.2f} cm on a 10 cm radius")

fig, ax = plane((-0.3, 1.75), (-0.35, 1.3), width=8)
circle(ax, upto=90)
ts = [math.radians(d / 10) for d in range(0, int(deg * 10) + 1)]
ax.plot([1.04 * math.cos(t) for t in ts], [1.04 * math.sin(t) for t in ts], color=BROWN, lw=3)
ax.text(1.06, 0.3, "string 0.8072 rad\n= 8.07 cm at 10 cm = 1", color=BROWN, fontsize=10)
for k, label in ((0, "post 0"), (100, "post 100")):
    t = math.radians(theta_deg(k))
    ax.plot(math.cos(t), math.sin(t), "o", color=BLUE, ms=6)
    ax.text(math.cos(t) + 0.04, math.sin(t) + 0.04, label, color=BLUE, fontsize=9)
ax.plot([0, x], [0, y], color=BLUE, lw=2)
ax.plot([0, x], [0, 0], color=GREEN, lw=6)
ax.plot([x, x], [0, y], color=ORANGE, lw=6)
ax.plot(x, y, "o", color=BLUE, ms=9)
angle(ax, deg, r=0.2)
ax.text(0.22, 0.06, "46.25°", color=BLUE, fontsize=10)
ax.text(x / 2, -0.13, "cos 46.25° = 0.6915", color=GREEN, ha="center")
ax.text(x / 2, -0.25, "√ᾱ₅₀ = 0.6916: the clean point's multiplier", color=GREEN, ha="center", fontsize=10)
ax.text(x - 0.03, y / 2, "sin 46.25° = 0.7224\n√(1 − ᾱ₅₀) = 0.7223:\nthe noise multiplier", color=ORANGE, ha="right", va="center", fontsize=10)
ax.text(x + 0.04, y + 0.05, "post 51", color=BLUE, fontsize=10)
ax.text(0.03, 1.15, "x² + y² = 0.4782 + 0.5218 = 1", fontsize=11)
ax.set_title("the point at post 51 is step 50's two multipliers, to within 0.0001", fontsize=12)
save(fig, "s2-circle-point-is-the-multipliers.svg")
```

![The quarter circle with posts 0 and 100 marked, a blue line to post 51 at 46.25 degrees, its green horizontal leg labelled cos 46.25 = 0.6915 beside the clean point's multiplier 0.6916, its orange vertical leg labelled sin 46.25 = 0.7224 beside the noise multiplier 0.7223, and a brown string along the arc of 0.8072 rad|750](assets/s2-circle-point-is-the-multipliers.svg)

**How to read this.** Both axes are in units of the radius. The green leg's length is the clean point's multiplier and the orange leg's length is the noise multiplier. Look at the two pairs of numbers on each leg: they differ in the fourth decimal only.

## How the quarter circle gives the multipliers

Navigation: ⬅️ [[#Step 2: the point is the two multipliers]] | 📋 [[#Table of contents|TOC]] | [[#The quarter circle's mechanism]] ➡️

Textbook: [Whitney, Trigonometry handbook, the unit circle, PDF p. 10](../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf#page=10)

### The multipliers lie on the circle

**The two multipliers are a point on the same circle.** The forward jump is $x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon$ ([[The Forward Process]]), with $\bar\alpha_t = C_{t+1}$. Its two multipliers satisfy

$$
\big(\sqrt{C_k}\big)^2 + \big(\sqrt{1 - C_k}\big)^2 = C_k + (1 - C_k) = 1
$$

$$
\underbrace{\big(\textcolor{#2e7d32}{\sqrt{C_k}}\big)^2}_{\text{clean point's multiplier, squared}}
+
\underbrace{\big(\textcolor{#ef6c00}{\sqrt{1 - C_k}}\big)^2}_{\text{noise multiplier, squared}}
=
\underbrace{\textcolor{#2e7d32}{C_k}}_{\text{share kept}}
+
\underbrace{\textcolor{#ef6c00}{1 - C_k}}_{\text{noise share}}
=
1
$$

**What the equation says.** Squaring each multiplier gives back its share, and the two shares add to 1 by construction. So at every post the pair (signal multiplier, noise multiplier) lies exactly on the circle of radius 1.

**Why the square roots are there.** The jump multiplies by the square root of each share, and squaring undoes it. Without the roots the pair at post 51 would be the shares themselves, (0.47826, 0.52174), whose squares add to 0.5009: a point inside the circle.

**Why the 1 − is there.** The noise share is whatever the kept share leaves of 1. Without it both multipliers at post 51 would be $\sqrt{C_{51}} = 0.6916$, and their squares would add to 0.9565.

### Share = multiplier²

**Why a share is a square.** Scaling a draw by $c$ scales its variance by $c^2$ ([[The Scaling Rule For Variance#Scaling a draw scales its variance by the square|the scaling rule]]). So $\cos\theta_k$ multiplies the clean image and $\cos^2\theta_k$ is the share of its variance that survives; $\sin\theta_k$ multiplies the noise and $\sin^2\theta_k$ is the noise's share.

**The identity.** [[The Cosine Wave#The two shares|The Pythagorean identity]] is the statement that the two shares add to 1.

### Close to the drawn point, not on it

The pair sits close to the drawn point $(\cos\theta_k, \sin\theta_k)$ but not on it, because the schedule divides by $\cos^2\theta_0$:

$$
\sqrt{C_k} = \frac{\cos\theta_k}{\cos\theta_0} = \cos\theta_k \times 1.00008
$$

$$
\underbrace{\textcolor{#2e7d32}{\sqrt{C_k}}}_{\text{clean point's multiplier}}
=
\frac{\underbrace{\textcolor{#2e7d32}{\cos\theta_k}}_{\text{drawn horizontal leg}}}{\underbrace{\textcolor{#6a1b9a}{\cos\theta_0}}_{0.99992}}
=
\textcolor{#2e7d32}{\cos\theta_k} \times \underbrace{1.00008}_{1/0.99992}
$$

**What the equation says.** The multiplier is the drawn $x$ stretched by $1/0.99992 = 1.00008$. At post 51 the two agree to 0.0001: 0.6915 drawn, 0.6916 multiplied.

**Why the division by $\cos\theta_0$ is there.** At post 0 the stretch does more: the drawn point is $(0.9999, 0.0125)$, while $C_0 = 1$ puts the multipliers at $(1, 0)$, so the clean image enters the first step unnoised. Without the division the multipliers at post 0 would be the drawn point itself.

### The worked numbers at post 51

$$
\begin{aligned}
\textcolor{#1565c0}{p_{51}} &= 51.8 / 100.8 = 0.5139 \\
\textcolor{#1565c0}{\theta_{51}} &= 0.5139 \times 90^\circ = 46.25^\circ \\
\textcolor{#2e7d32}{\cos 46.25^\circ} &= 0.6915, \qquad \textcolor{#ef6c00}{\sin 46.25^\circ} = 0.7224 \\
\textcolor{#2e7d32}{C_{51}} &= 0.47826 \\
\textcolor{#2e7d32}{\sqrt{C_{51}}} &= 0.6916 \\
\textcolor{#ef6c00}{\sqrt{1 - C_{51}}} &= \sqrt{0.52174} = 0.7223
\end{aligned}
$$

**What to look at.** The drawn legs and the multipliers differ in the fourth decimal: 0.6915 against 0.6916, and 0.7224 against 0.7223.

## The quarter circle's mechanism

Navigation: ⬅️ [[#How the quarter circle gives the multipliers]] | 📋 [[#Table of contents|TOC]]

**What it draws.** Walking the point round the quarter turn is the forward process. The squared horizontal leg falls slowly at both ends and fastest in the middle, post 51's point is the jump's two multipliers, and the fraction's denominator is one fixed bar.

```python
import math
import matplotlib.pyplot as plt
from plane import GREEN, ORANGE, BLUE, PURPLE, GREY, LIGHT_GREY
from cosine import theta_deg, f, C

plt.rcParams.update({"font.size": 11, "svg.fonttype": "path"})
rad = math.radians
fig = plt.figure(figsize=(10, 11.5))
turn, bars = fig.add_axes([0.04, 0.50, 0.38, 0.40]), fig.add_axes([0.50, 0.48, 0.48, 0.47])
point, frac = fig.add_axes([0.04, 0.05, 0.38, 0.40]), fig.add_axes([0.50, 0.12, 0.48, 0.26])

ts = [rad(d / 4) for d in range(361)]
for ax in (turn, point):
    ax.plot([math.cos(t) for t in ts], [math.sin(t) for t in ts], color=LIGHT_GREY, lw=4)
    ax.plot([0, 1.15], [0, 0], color="black", lw=1)
    ax.plot([0, 0], [0, 1.15], color="black", lw=1)
    ax.set_xlim(-0.08, 1.35); ax.set_ylim(-0.12, 1.3); ax.set_aspect("equal"); ax.axis("off")
squares = []
for i, d in enumerate(range(0, 91, 15)):
    x2 = math.cos(rad(d)) ** 2
    squares.append(x2)
    turn.plot([0, math.cos(rad(d))], [0, math.sin(rad(d))], color=BLUE, lw=1)
    turn.text(1.09 * math.cos(rad(d)), 1.09 * math.sin(rad(d)), f"{d}°", color=BLUE, ha="center", va="center")
    bars.barh(-1.4 * i, 1, color="#f1f1f1", height=0.6)
    bars.barh(-1.4 * i, x2, color=GREEN, height=0.6)
    bars.text(1.03, -1.4 * i, f"x² = {x2:.3f}".rstrip("0").rstrip("."), va="center", color=GREEN)
    bars.text(-0.03, -1.4 * i, f"{d}°", va="center", ha="right", color=BLUE)
turn.set_title("seven angles, every 15°", fontsize=12)
for i in range(6):
    drop = squares[i] - squares[i + 1]
    word = "slow" if i in (0, 5) else ("fastest" if i in (2, 3) else "")
    bars.annotate("", (squares[i + 1], -1.4 * i - 0.7), (squares[i], -1.4 * i - 0.7),
                  arrowprops={"arrowstyle": "|-|", "color": ORANGE, "lw": 2})
    bars.text(squares[i] + 0.03, -1.4 * i - 0.7, f"drop {drop:.3f}".rstrip("0") + (f", {word}" if word else ""),
              va="center", color=ORANGE, fontsize=10)
bars.set_xlim(-0.12, 1.32); bars.set_ylim(-8.8, 0.6); bars.axis("off")
bars.set_title("the horizontal leg squared: x² = cos² at each angle", fontsize=12)

deg = theta_deg(51)
x, y = math.cos(rad(deg)), math.sin(rad(deg))
point.plot([0, x], [0, y], color=BLUE, lw=2)
point.plot([0, x], [0, 0], color=GREEN, lw=6)
point.plot([x, x], [0, y], color=ORANGE, lw=6)
point.plot(x, y, "o", color=BLUE, ms=9)
point.text(x + 0.04, y + 0.06, "post 51", color=BLUE)
point.text(0.05, 1.22, f"point ({x:.4f}, {y:.4f})", color=BLUE)
point.text(0.05, 1.12, f"multipliers ({math.sqrt(C(51)):.4f}, {math.sqrt(1 - C(51)):.4f})")
point.set_title("post 51: the point and the two multipliers", fontsize=12)

frac.barh(1, f(51), color=GREEN, height=0.5)
frac.barh(0, f(0), color=PURPLE, height=0.5)
frac.text(f(51) + 0.02, 1, f"numerator {f(51):.5f}", va="center", color=GREEN)
frac.text(0.02, -0.45, f"denominator {f(0):.5f}", va="top", color=PURPLE)
frac.plot([0, 1], [0.5, 0.5], color="black", lw=1.5)
frac.text(1.08, 0.5, f"C₅₁ = {C(51):.5f}", color="white", fontsize=12, va="center",
          bbox=dict(boxstyle="round,pad=0.4", fc=GREEN, ec="none"))
frac.text(0, -1.3, "β_t = 1 − C_(t+1) / C_t", fontsize=12)
frac.text(0, -1.75, "the denominator cancels", fontsize=10, color=GREY)
frac.set_xlim(0, 1.45); frac.set_ylim(-1.9, 1.5); frac.axis("off")
frac.set_title("the fraction at post 51, on a scale from 0 to 1", fontsize=12)
fig.savefig("quarter-circle-the-mechanism.svg", format="svg", bbox_inches="tight")
print("saved quarter-circle-the-mechanism.svg")
```

![Top left, a quarter circle with blue rays every 15 degrees from 0 to 90; top right, one green bar per ray of length 1, 0.933, 0.75, 0.5, 0.25, 0.067 and 0, with orange drops of 0.067 and 0.183 at the slow ends and 0.25 twice in the fastest middle; bottom left, post 51's point with its green and orange legs, point (0.6915, 0.7224) and multipliers (0.6916, 0.7223); bottom right, a green numerator bar of 0.47819 over a purple denominator bar of 0.99984 giving C_51 = 0.47826, with beta_t = 1 - C_(t+1) / C_t and the denominator cancels|800](assets/quarter-circle-the-mechanism.svg)

**How to read this.** Top left, each blue ray is one angle; top right, each green bar is that ray's horizontal leg squared on a scale from 0 to 1, and each orange bracket is the drop to the next bar. Bottom left is post 51's point with its two legs, and bottom right the fraction at post 51, a green numerator over a purple denominator.

**What to look at.** The drops are 0.067, 0.183, 0.25, 0.25, 0.183 and 0.067: slow at both ends and fastest in the middle. The purple bar, 0.99984, is the same at every post, so it cancels out of every step's noise $\beta_t$, which [[The Quarter Turn And The Fraction#Step 4: the fraction|step 4 of the build]] draws at every step.

*🖼️ Diagram wanted: the deep-dive sheet composing the form, the mechanism and the six moves at post 51. Prompt 45 in the vault's `.prompts/Diffusion Models.md`.*

> [!note]- How this was checked
> The two figure scripts were run on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and matplotlib 3.10.8 from the machine's `python3`, in an empty `~/playground/sandbox/quarter-circle-retrofit` holding `plane.py` and the sandbox's `cosine.py`, by vault-writer, and the folder was removed afterwards. Each SVG was rendered to PNG by PyMuPDF and opened before filing. Step 2's figure, with step 1's in [[The Quarter Circle Under The Cosine Schedule]], replaces drawn prompt 43 (the form), and the mechanism figure replaces prompt 44, in `.prompts/Diffusion Models.md`, because their faithfulness notes fix exact angles, lengths and bar lengths. The string is brown and the $x^2$ bars green, where the prompts had purple and blue, to follow the cosine schedule's colour key.
>
> The with-and-without numbers were computed that day by a throwaway script on the same `cosine.py`: the shares as the pair, $0.47826^2 + 0.52174^2 = 0.5009$; both multipliers $\sqrt{C_{51}}$, squares adding to 0.9565; the stretch $1/\cos\theta_0 = 1.0000777$; and post 0's drawn point $(0.99992, 0.01247)$ against the multipliers $(1, 0)$. The worked numbers are the outputs of `s2_point.py` and `six_moves.py` in [[Running The Quarter Circle Under The Cosine Schedule]].
>
> The trigonometry handbook's PDF pages 10 (the unit circle) and 68 (polar coordinates) were opened and read as text. The scene frame anchors are as the walk's `dispatch.md` and the retrofit brief record them.
