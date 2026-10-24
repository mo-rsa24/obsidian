---
aliases: [how each piece of C_k works, the six moves of C_k, one boundary piece by piece, C_k at post 51 piece by piece, the cosine schedule's mechanism, the first two degrees with and without the offset, the broken runs of the cosine schedule]
sources:
  - "Nichol, Dhariwal, Improved Denoising Diffusion Probabilistic Models, ICML 2021, section 3.2 and equation (17), PDF p. 4: https://arxiv.org/pdf/2102.09672#page=4"
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Trigonometry, radians and degrees, PDF p. 7: ../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf#page=7"
standard: vault-note v2
---

# How Each Piece Of The Cosine Schedule Works

Up: [[Diffusion Models]] · ⬅️ [[The Cosine Noise Schedule]] · [[Running The Cosine Noise Schedule]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[The Cosine Noise Schedule]] for the formula and why each piece is there, and [[Polar Coordinates#The point: from length and angle to x and y|the unit circle]] for the cosine as a horizontal reach.

**One boundary value is six moves from its post number, worked here at post 51.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. It has no questions on this note yet.

> [!warning]- Unfinished
> - The deep-dive sheet is waiting: prompt 42 in the vault's `.prompts/Diffusion Models.md`.
> - The diffusion models quiz has no questions on this note yet.

Stated claims: 0.

**What this note does.** It runs the formula of [[The Cosine Noise Schedule#All the words together: the formula]] one move per line and draws those moves at post 51. Then it draws the angles of posts 0, 1, 51 and 100 on the unit circle, with the broken runs beside them.

**Where the numbers come from.** Every printed number is an output of [[Running The Cosine Noise Schedule]] or of the two figure scripts here. Each script imports the `cosine.py` of [[Running The Cosine Noise Schedule#Try the boundary values yourself|step 3 of the sandbox]] and needs matplotlib.

**Colours in this note.** <span style="color:#2e7d32">**Green is a boundary value $C_k$, the share kept**</span>, <span style="color:#1565c0">**blue is a post's position and its angle $\theta_k$**</span>, <span style="color:#6a1b9a">**purple is the denominator $\cos^2\theta_0$**</span>, and <span style="color:#9e9e9e">**grey is a case with a piece removed**</span>, as in [[The Cosine Noise Schedule]].

## How each piece of C_k works

Navigation: [[#The broken runs and the mechanism]] ➡️

Textbook: [Whitney, Trigonometry handbook, radians and degrees, PDF p. 7](../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf#page=7)

Write $p_k$ for [the position](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step4-where-the-position-goes) and read the formula from the inside out, one move per line:

$$
\begin{aligned}
u_k &= k/T \\
u_k + \delta &= k/T + \delta \\
p_k &= \frac{u_k + \delta}{1 + \delta} \\
\theta_k &= p_k \cdot \frac{\pi}{2} = p_k \cdot 90^\circ \\
f(k) &= \cos^2\theta_k \\
C_k &= \frac{f(k)}{f(0)}
\end{aligned}
$$

$$
\begin{aligned}
\underbrace{\textcolor{#1565c0}{u_k}}_{\text{1. position from 0 to 1}} &= 51/100 = 0.51 \\
\underbrace{\textcolor{#1565c0}{u_k} + \delta}_{\text{2. shift past 0}} &= 0.51 + 0.008 = 0.518 \\
\underbrace{\textcolor{#1565c0}{p_k}}_{\text{3. last post stays at 1}} &= 0.518 / 1.008 = 0.51389 \\
\underbrace{\textcolor{#1565c0}{\theta_k}}_{\text{4. a quarter turn}} &= 0.51389 \times 90^\circ = 46.25^\circ \\
\underbrace{f(k)}_{\text{5. a share from 0 to 1}} &= \cos^2 46.25^\circ = 0.69151^2 = 0.47819 \\
\underbrace{\textcolor{#2e7d32}{C_k}}_{\text{6. so } C_0 = 1} &= \frac{0.47819}{\textcolor{#6a1b9a}{0.99984}} = 0.47826
\end{aligned}
$$

**What the equation says.** Each line is one piece of [[The Cosine Noise Schedule#All the words together: the formula]], where every piece has its reason and its with-and-without move. At post 51 the six moves take the post number 51 to the share 0.47826.

**The six moves, drawn at post 51.** The left panel draws moves 1 to 6 on the curve $C$ against the position, and the right panel removes the denominator:

```python
import math
import matplotlib.pyplot as plt
from cosine import T, delta, theta_deg, f, C

GREEN, BLUE, PURPLE, GREY = "#2e7d32", "#1565c0", "#6a1b9a", "#9e9e9e"
plt.rcParams.update({"font.size": 11, "svg.fonttype": "path"})
BOX = dict(fc="white", ec="none", alpha=0.9, pad=1.5)
k = 51
u, shifted, p = k / T, k / T + delta, (k / T + delta) / (1 + delta)    # 0.51, 0.518, 0.51389
ps = [i / 1000 for i in range(1001)]
cos2 = [math.cos(q * math.pi / 2) ** 2 for q in ps]
fig, (move, zoom) = plt.subplots(1, 2, figsize=(14, 5.6), gridspec_kw={"width_ratios": [1.5, 1], "wspace": 0.28})
move.plot(ps, [c / f(0) for c in cos2], color=GREEN, lw=2.5)
move.plot(p, 0, "|", color=BLUE, ms=14, mew=2)
ruler = move.inset_axes([0.05, 0.1, 0.42, 0.2])
for x, y, text in ((u, 0.55, f"1. k/T = {u:.2f}"), (shifted, 0.55, f"2. + δ = {shifted:.3f}"), (p, -0.9, f"3. ÷ (1 + δ) = {p:.5f}")):
    ruler.plot(x, 0, "|", color=BLUE, ms=16, mew=2)
    ruler.text(x, y, text, color=BLUE, ha="center", fontsize=10)
ruler.annotate("", (shifted, 0.2), (u, 0.2), arrowprops={"arrowstyle": "->", "color": BLUE})
ruler.annotate("", (p, -0.2), (shifted, -0.2), arrowprops={"arrowstyle": "->", "color": BLUE})
ruler.axhline(0, color="#424242", lw=1)
ruler.set_xlim(0.505, 0.523); ruler.set_ylim(-1.3, 1.2); ruler.set_yticks([])
ruler.tick_params(labelsize=9); ruler.spines[["top", "right", "left"]].set_visible(False)
ruler.set_title("post 51's position, magnified", fontsize=10)
move.plot([p, p], [0, C(k)], color=BLUE, ls="--")
move.plot([0, p], [C(k), C(k)], color=GREEN, ls="--")
move.plot(p, C(k), "o", color=GREEN, ms=9)
move.text(p + 0.02, C(k) + 0.04, f"4. × 90° = {theta_deg(k):.2f}°\n5. cos² = {f(k):.5f}\n6. ÷ {f(0):.5f} = C₅₁ = {C(k):.5f}",
          color=GREEN, bbox=BOX)
move.text(0.62, 0.8, "C(p) = cos²(p · 90°) / cos²θ₀", color=GREEN, bbox=BOX)
move.set_xlabel("position p on the quarter arc (0 is 0°, 1 is 90°)")
move.set_ylabel("C, share of the variance kept")
move.set_xlim(0, 1.02); move.set_ylim(0, 1.05)
move.set_title("one boundary, piece by piece: post 51")
f_none = [math.cos(math.radians(theta_deg(j))) ** 2 for j in range(3)]
zoom.plot(range(3), [C(j) for j in range(3)], "o-", color=GREEN, ms=8)
zoom.plot(range(3), f_none, "s--", color=GREY, ms=7)
zoom.axhline(1, color=PURPLE, lw=1, ls=":")
zoom.text(0.12, 1.00008, f"with ÷ cos²θ₀: C₀ = {C(0):.5f}", color=GREEN, bbox=BOX)
zoom.text(0.95, 0.99962, f"without: C₀ = {f_none[0]:.5f},\nevery post × {f(0):.5f}", color="#616161", bbox=BOX)
b_with, b_without = 1 - C(1) / C(0), 1 - f_none[1] / f_none[0]
zoom.text(0.05, 0.99812, f"β₀ = {b_with:.6f} with,\n{b_without:.6f} without:\nthe factor cancels in the ratio", color=PURPLE, bbox=BOX)
zoom.set_xticks(range(3), [f"post {j}" for j in range(3)])
zoom.set_ylim(0.9978, 1.0003); zoom.set_xlim(-0.2, 2.3)
zoom.set_ylabel("C_k (y-axis from 0.9978)")
zoom.set_title("the consequence of no denominator: C₀ ≠ 1")
for ax in (move, zoom):
    ax.spines[["top", "right"]].set_visible(False); ax.grid(color="#eeeeee"); ax.set_axisbelow(True)
fig.savefig("cosine-schedule-one-boundary-at-post-51.svg", format="svg", bbox_inches="tight")
```

![Left, the green curve C against the position p on the quarter arc from 0 to 1, with post 51 marked at p = 0.51389 and C = 0.47826, a magnified ruler showing 0.51, then + delta = 0.518, then divided by 1 + delta = 0.51389, and the label 46.25 degrees, cos squared 0.47819, divided by 0.99984 gives 0.47826; right, posts 0, 1 and 2 on a y-axis from 0.9978, green with the denominator starting at 1 and grey without it starting at 0.99984, with beta_0 = 0.000631 both ways|900](assets/cosine-schedule-one-boundary-at-post-51.svg)

**How to read this.** On the left the x-axis is the position $p$ on the quarter arc and the green curve is $C$ at every position; the magnified ruler shows moves 1 to 3 taking post 51 from 0.51 to 0.518 and back to 0.51389, and the green label reads moves 4 to 6 off the curve at 46.25°. On the right the y-axis starts at 0.9978 and shows posts 0 to 2 with the denominator (green) and without it (grey). Look at post 0, 1 with the denominator and 0.99984 without, while $\beta_0$ prints 0.000631 both ways.

The geometry under these six moves, built by hand from an empty sheet (the circle, the legs $\cos\theta$ and $\sin\theta$ as the signal and noise multipliers, the angle as a string along the arc, the position ruler, the quarter turn and the fraction's two bars), is [[The Quarter Circle Under The Cosine Schedule#Build the quarter circle by hand]].

**The worked numbers** at posts 0, 1, 51 and 100 are the fields of [[Running The Cosine Noise Schedule#Reading the boundary-value output]]. $C_1 = 0.99937$ is the $\bar\alpha_0 = 0.9994$ in [the rebuild's `walk-numbers.json`](../../../../PhD/reduce-reuse-recycle/rebuild/out/walk-numbers.json), and $C_{51} = 0.47826$ is its $\bar\alpha_{50} = 0.4783$, as [[Running The Cosine Noise Schedule#Try the boundary values yourself|step 7 of the sandbox]] printed.

## The broken runs and the mechanism

Navigation: ⬅️ [[#How each piece of C_k works]]

**The broken run without the offset.** With $\delta = 0$ the angles start at $0^\circ$, so $\theta_1 = 0.9^\circ$ and $C_1 = \cos^2 0.9^\circ = 0.99975$. The first step's noise share is then $1 - 0.99975 = 0.000247$, with standard deviation $\sqrt{0.000247} = 0.0157$, against $0.000631$ and $0.0251$ with the offset.

**Why Nichol and Dhariwal add the offset.** They add it because "having tiny amounts of noise at the beginning of the process made it hard for the network to predict ϵ accurately enough", and pick $s = 0.008$ so that $\sqrt{\beta_0}$ sits just under the [pixel bin size $1/127.5 = 0.0078$](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-why-offset) (*cited*, p. 4). With this note's $T = 100$ the first step's standard deviation is $0.0251$, about three times that bin size (*derived*: $0.0251 / 0.0078 = 3.2$).

**The broken run without the denominator.** Without the denominator, $C_0$ would be $0.99984$ instead of 1.

**The mechanism, drawn.** One script draws each post's angle on the unit circle, its share bar, and the first two degrees with and without the offset:

```python
import math
import matplotlib.pyplot as plt
from cosine import theta_deg, C

GREEN, BLUE, GREY = "#2e7d32", "#1565c0", "#9e9e9e"
plt.rcParams.update({"font.size": 11, "svg.fonttype": "path"})
BOX = dict(fc="white", ec="none", alpha=0.9, pad=1.5)
fig = plt.figure(figsize=(13, 9.5))
circ = fig.add_axes([0.05, 0.36, 0.5, 0.6]); bars = fig.add_axes([0.62, 0.42, 0.35, 0.5])
first = fig.add_axes([0.08, 0.05, 0.85, 0.22])
arc = [math.radians(a / 10) for a in range(901)]
circ.plot([math.cos(a) for a in arc], [math.sin(a) for a in arc], color=GREY)
for k, xy in ((0, (1.03, 0.04)), (51, (0.72, 0.77)), (100, (0.04, 1.03))):
    a = math.radians(theta_deg(k))
    circ.plot([0, math.cos(a)], [0, math.sin(a)], color=BLUE, lw=2)
    circ.text(*xy, f"k = {k}, θ = {round(theta_deg(k), 3):g}°", color=BLUE, bbox=BOX)
a51 = math.radians(theta_deg(51))
circ.plot([math.cos(a51)] * 2, [0, math.sin(a51)], color="#424242", ls=":")
circ.plot([0, math.cos(a51)], [0, 0], color=GREEN, lw=5, solid_capstyle="butt")
circ.text(0.12, -0.09, f"cos θ₅₁ = {math.cos(a51):.4f}, the horizontal reach", color=GREEN)
circ.set_xlabel("cos θ"); circ.set_ylabel("sin θ")
circ.set_aspect("equal"); circ.set_xlim(-0.05, 1.45); circ.set_ylim(-0.15, 1.12)
circ.set_title("the post's angle on a quarter of the unit circle")
for row, k in enumerate((0, 1, 51, 100)):
    bars.barh(row, 1, color="white", edgecolor="#424242"); bars.barh(row, C(k), color=GREEN)
    bars.text(1.02, row, f"k = {k}: C = {round(C(k), 5):g}", va="center")
bars.set_yticks([]); bars.set_xlim(0, 1.6); bars.set_ylim(3.6, -0.6)
bars.set_xlabel("share of the variance kept (green) out of the outlined 1")
bars.set_title("C_k = cos²θ_k / cos²θ₀ as a share bar")
for d, color, style, name in ((0.008, BLUE, "-", ""), (0.0, GREY, "--", ", δ = 0")):
    for k in (0, 1):
        a = theta_deg(k, d)
        first.plot([0, 1], [0, a], color=color, ls=style, lw=2)
        first.text(1.01, a, f"k = {k}{name}: {round(a, 3):g}°", color=color if d else "#616161", va="center")
    share = 1 - C(1, d)
    first.text(0.03, 1.75 if d else 1.45, f"with δ = {d:g}: first noise share {share:.6f}, sd {math.sqrt(share):.4f}",
               color="#212121" if d else "#616161")
first.set_xlim(0, 1.25); first.set_ylim(-0.1, 2.0)
first.set_xlabel("distance along the ray (the radius is 1)"); first.set_ylabel("angle, degrees")
first.set_title("the first two degrees, magnified: each ray drawn as its angle in degrees")
for ax in (circ, bars, first):
    ax.spines[["top", "right"]].set_visible(False)
fig.savefig("cosine-schedule-the-mechanism-quarter-circle.svg", format="svg", bbox_inches="tight")
```

![Top left, a quarter of the unit circle with blue rays at k = 0 (0.714 degrees), k = 51 (46.25 degrees) and k = 100 (90 degrees), and a thick green segment along the cos axis from 0 to 0.6915 under the k = 51 ray; top right, four share bars outlined to 1 with the green kept share 1, 0.99937, 0.47826 and 0 for k = 0, 1, 51 and 100; bottom, the first two degrees magnified, blue rays at 0.714 and 1.607 degrees with the offset and grey rays at 0 and 0.9 degrees with delta = 0, and the lines first noise share 0.000631, sd 0.0251 and 0.000247, sd 0.0157|850](assets/cosine-schedule-the-mechanism-quarter-circle.svg)

**How to read this.** Top left, the axes are $\cos\theta$ and $\sin\theta$ and each blue ray is one post's angle; the thick green segment is post 51's horizontal reach, $\cos 46.25^\circ = 0.6915$. Top right, each bar is one post's $C_k$ as a green share of the outlined 1, from all green at post 0 to empty at post 100. The bottom panel stretches the first two degrees, with distance along a ray on the x-axis and its angle on the y-axis: posts 0 and 1 sit at 0.714° and 1.607° with the offset (blue) and at 0° and 0.9° with δ = 0 (grey).

*🖼️ Diagram wanted: the deep-dive sheet composing the form, the mechanism and step 6's run. Prompt 42 in the vault's `.prompts/Diffusion Models.md`.*

> [!note]- How this was checked
> The two figure scripts were run on 2026-10-21 on mscluster (Linux) with Python 3.12.10, matplotlib 3.10.8 and the sandbox's `cosine.py`, in an empty `~/playground/sandbox/cosine-retrofit`, by vault-writer, and each SVG was opened (rendered to PNG by PyMuPDF 1.27.2) before filing. The post-51 figure, with the fence in [[The Cosine Noise Schedule]], replaces drawn prompt 40 (the form), and the quarter circle replaces prompt 41 (the mechanism), in `.prompts/Diffusion Models.md`, because their faithfulness notes fix exact heights, angles and lengths. In both, grey replaces the prompts' orange for the δ = 0 case, because orange is a step's noise share in the note's colour key, and green replaces blue for the share kept; post 1's ray at 1.607° is drawn only in the magnified panel, where it can be told apart from post 0's.
>
> The worked numbers are the outputs of `by_hand.py` and `same_as_code.py` in [[Running The Cosine Noise Schedule]], re-run byte for byte on 2026-10-21. The quotation is from Nichol and Dhariwal's page 4, as read for [[The Cosine Noise Schedule]]. The trigonometry handbook's PDF page 7 (radians and degrees, 360° and 2π in one rotation) was opened and read as text.
