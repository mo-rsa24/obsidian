---
aliases: [cosine schedule, cosine noise schedule, cosine beta schedule, cosine_beta_schedule, improved DDPM schedule, Nichol and Dhariwal schedule, boundary values, boundary value, cosine boundary values, C_k, "C_k = cos^2(theta_k) / cos^2(theta_0)", theta_k, the schedule's offset, offset delta, "s = 0.008", fence posts and gaps, "beta_t = 1 - C_{t+1} / C_t", noise share read off two posts]
sources:
  - "Nichol, Dhariwal, Improved Denoising Diffusion Probabilistic Models, ICML 2021, section 3.2 and equation (17), PDF p. 4: https://arxiv.org/pdf/2102.09672#page=4"
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Trigonometry, radians and degrees, PDF p. 7: ../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf#page=7"
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Trigonometry, the unit circle, PDF p. 10: ../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf#page=10"
standard: vault-note v2
---

# The Cosine Noise Schedule

Up: [[Diffusion Models]] · ⬅️ [[Running The Density Of The One Jump]] · [[How Each Piece Of The Cosine Schedule Works]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[The Forward Process]] for $\bar\alpha_t$ as the share of the clean signal's variance kept at step $t$, and [[From Many Steps To One Jump]] for why the noise share is $1 - \bar\alpha_t$.

**The cosine schedule is the timetable of noise levels: 101 boundary values $C_k$ around 100 steps.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. It has no questions on this note yet.

> [!warning]- Unfinished
> - The deep-dive sheet is waiting: prompt 42 in the vault's `.prompts/Diffusion Models.md`, with its slot in [[How Each Piece Of The Cosine Schedule Works]]. The form and the mechanism are drawn by the scripts in [[#The boundary values C_k]] and in that note.
> - The diffusion models quiz has no questions on this note yet.

Stated claims: 0.

**What a boundary value is.** For $T = 100$ steps the timetable lists 101 values $C_0, \dots, C_{100}$, like fence posts around 100 gaps, and $C_k$ is the share of the clean signal's variance still kept at boundary $k$. Each value is the squared cosine of an angle that sweeps a quarter turn, rescaled so the first one is exactly 1.

**Where the formula comes from.** The formula is *cited* from Nichol and Dhariwal, equation (17); this note takes it as given and computes it by hand. Why a squared cosine was chosen is not derived here, and the paper itself calls the choice arbitrary: "many other functions with similar shapes would work as well" (*cited*, p. 4).

**How steps are counted.** Steps are counted as the rebuild's code counts them, from 0, so the kept share after step $t$ is $\bar\alpha_t = C_{t+1}$: $C_{51} = 0.47826$ is the $\bar\alpha_{50} = 0.4783$ of [[From Many Steps To One Jump]]. [[Running The Cosine Noise Schedule#Try the boundary values yourself|Step 7 of the sandbox]] *shows* that match. Why it holds is the telescoping product in [[From Many Steps To One Jump#Other ways to see it]], written out in [[#The consequence: the kept share after step t is the next post]].

**Colours in this note.** <span style="color:#2e7d32">**Green is a boundary value $C_k$, the share kept**</span>, <span style="color:#ef6c00">**orange is a step's noise share $\beta_t$**</span>, <span style="color:#1565c0">**blue is a post's position and its angle $\theta_k$**</span>, <span style="color:#6a1b9a">**purple is the denominator $\cos^2\theta_0$**</span>, and <span style="color:#9e9e9e">**grey is a case with a piece removed**</span>. Every equation, the toy table and every figure use them.

## Table of contents

- [[#The boundary values C_k]]
- [[#Try the boundary values yourself]]
- [[#How each piece of C_k works]]
- [[#Other ways to get the boundary values]]
- [[#Why the boundary values matter]]
- [[#The cosine schedule taught in, applied in]]

## The boundary values C_k

Navigation: 📋 [[#Table of contents|TOC]] | [[#Try the boundary values yourself]] ➡️

Textbook: [Whitney, Trigonometry handbook, the unit circle, PDF p. 10](../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf#page=10)

**A boundary value $C_k$**, also the cosine boundary value or the paper's $\bar\alpha_t = f(t)/f(0)$, is the share of the clean signal's variance kept at post $k$ of the noise timetable.

**When to reach for it.** Whenever a diffusion model's noise levels have to be written down, or a number like $\bar\alpha_{50} = 0.4783$ has to be [traced to where it came from](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step4-four-posts-by-hand). Without the timetable, the forward jump in [[The Forward Process]] has no $\bar\alpha_t$ to use.

**The same thing in the code.** It is [the rebuild's `cosine_beta_schedule`](../../../../PhD/reduce-reuse-recycle/rebuild/model.py) up to the line that rescales (lines 13 to 17), written with the angle in degrees, which is easier by hand.

### The posts and their table

<table>
<tr><th>post k</th><th style="color:#1565c0">angle θ<sub>k</sub></th><th style="color:#2e7d32">C<sub>k</sub></th><th>kept share after step</th><th style="color:#ef6c00">noise β of the step ending at post k</th></tr>
<tr><td>0</td><td>0.714°</td><td style="border:2px solid #212121">1</td><td>before step 0</td><td></td></tr>
<tr><td>1</td><td>1.607°</td><td style="border:2px solid #212121">0.99937</td><td>ᾱ<sub>0</sub></td><td style="border:2px solid #212121">0.00063</td></tr>
<tr><td>26</td><td>23.929°</td><td>0.83562</td><td>ᾱ<sub>25</sub></td><td>0.01345</td></tr>
<tr><td>50</td><td>45.357°</td><td style="border:2px solid #212121">0.49384</td><td>ᾱ<sub>49</sub></td><td>0.03059</td></tr>
<tr style="background:#fff8e1"><td><b>51</b></td><td>46.25°</td><td style="border:2px solid #212121"><b>0.47826</b></td><td>ᾱ<sub>50</sub></td><td style="border:2px solid #212121">0.03155</td></tr>
<tr><td>76</td><td>68.571°</td><td>0.13349</td><td>ᾱ<sub>75</sub></td><td>0.0747</td></tr>
<tr><td>99</td><td>89.107°</td><td>0.00024</td><td>ᾱ<sub>98</sub></td><td>0.74994</td></tr>
<tr><td>100</td><td>90°</td><td style="border:2px solid #212121">0</td><td>ᾱ<sub>99</sub>, clipped</td><td style="border:2px dashed #212121">0.999</td></tr>
</table>

**How to read this table.** Each row is one post of the 100-step timetable. $C_k$ is the share of the clean signal's variance still kept there; it is the kept share $\bar\alpha$ after the step that ends at that post. The last column is that step's noise, $\beta_{k-1} = 1 - C_k / C_{k-1}$.

**What to look for.** The boxed column falls from 1 to 0. The highlighted row is the toy, $\bar\alpha_{50} = 0.4783$, and its $\beta_{50}$ is read off the boxed $C_{50}$ above it. The dashed cell is the clip: the raw last step would remove everything.

### The base word: schedule

A schedule is a timetable. $T = 100$ steps have 101 posts between and around them, the way 100 gaps need 101 fence posts, and the timetable lists one value per post:

$$
C_0,\ C_1,\ \dots,\ C_{100}, \qquad \text{step } t \text{ runs from post } t \text{ to post } t+1
$$

$$
\underbrace{\textcolor{#2e7d32}{C_0,\ C_1,\ \dots,\ C_{100}}}_{101\text{ posts}},
\qquad
\underbrace{\text{step }t}_{t\,=\,0,\dots,99}\ \text{runs from post }t\text{ to post }t+1
$$

**What the equation says.** A value sits on a post and a step sits between two posts. Step 50 runs from post 50 to post 51, so its kept share is $C_{51} = 0.47826$.

### The term's base word: boundary

**What the word means.** A boundary is a fence post: it sits where one step ends and the next begins. Post $k$ closes step $k - 1$ and opens step $k$, so [101 posts fence 100 steps](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-name-boundary-value).

$$
\text{post } k = \text{end of step } k - 1 = \text{start of step } k
$$

$$
\underbrace{\text{post }k}_{\text{a boundary}}
=
\underbrace{\text{end of step }k-1}_{\text{none at }k\,=\,0}
=
\underbrace{\text{start of step }k}_{\text{none at }k\,=\,100}
$$

**What it means.** Post 0 opens step 0 and closes nothing, and post 100 closes step 99 and opens nothing. That is why there is one more post than step.

### Then the word: value

**What the word means.** Each post carries one number, its value $C_k$: the share of the clean signal's variance still kept there. Drawn as a fence, [each post grows to that height](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-name-boundary-value).

$$
C_k = \bar\alpha_{k-1} \quad (k \ge 1), \qquad C_{51} = \bar\alpha_{50} = 0.47826
$$

$$
\underbrace{\textcolor{#2e7d32}{C_k}}_{\text{value at post }k}
=
\underbrace{\bar\alpha_{k-1}}_{\text{kept after step }k-1},
\qquad
\textcolor{#2e7d32}{C_{51}} = \bar\alpha_{50} = 0.47826
$$

**What it means.** The value at post 51 is what is left after step 50, a little under half. The values run from $C_0 = 1$ down to $C_{100} = 0$.

**The figure scripts.** Each one imports `cosine.py` from [[Running The Cosine Noise Schedule#Try the boundary values yourself|step 3 of the sandbox]] and needs matplotlib, so run it in that folder.

```python
import math
import matplotlib.pyplot as plt
from cosine import T, C

GREEN, ORANGE, BLUE, GREY = "#2e7d32", "#ef6c00", "#1565c0", "#9e9e9e"
plt.rcParams.update({"font.size": 11, "svg.fonttype": "path"})
BOX = dict(fc="white", ec="none", alpha=0.9, pad=1.5)
fig, (fence, first) = plt.subplots(1, 2, figsize=(13, 5), gridspec_kw={"width_ratios": [1.6, 1]})
for k in range(T + 1):
    fence.plot([k, k], [0, C(k)], color=GREEN, lw=1.2)
fence.axvspan(50, 51, color=ORANGE, alpha=0.25)
fence.text(52.5, 0.62, "step 50 runs\nfrom post 50 to post 51", color=ORANGE, bbox=BOX)
for k, text, xy in ((0, "post 0: C₀ = 1", (4, 1.04)), (51, "post 51: C₅₁ = 0.47826 = ᾱ₅₀", (56, 0.4)),
                    (100, "post 100: C₁₀₀ = 0", (72, 0.25))):
    fence.plot(k, C(k), "o", color=GREEN, ms=7)
    fence.annotate(text, (k, C(k)), xytext=xy, color=GREEN, bbox=BOX, arrowprops={"arrowstyle": "-", "color": GREEN})
fence.annotate("", (100, 1.12), (0, 1.12), arrowprops={"arrowstyle": "|-|", "color": "#424242"})
fence.text(50, 1.14, "100 gaps, one per step", ha="center")
fence.set_xlabel("post k (101 posts, 0 to 100)")
fence.set_ylabel("height of post k: C_k, share of the variance kept")
fence.set_xlim(-2, 102); fence.set_ylim(0, 1.22)
fence.set_title("the timetable as a fence: each post as tall as its boundary value")
for d, color, name in ((0.008, ORANGE, "δ = 0.008"), (0.0, GREY, "δ = 0")):
    sd = [math.sqrt(1 - C(t + 1, d) / C(t, d)) for t in range(10)]
    first.plot(range(10), sd, "o-", color=color, ms=6)
    first.text(9.3, sd[9] + (0.003 if d else -0.003), name, color=color, va="center")
    first.annotate(f"step 0: √β₀ = {sd[0]:.4f}", (0, sd[0]), xytext=(1.2, 0.019 if d else 0.011),
                   color=color, arrowprops={"arrowstyle": "-", "color": color})
first.axhline(1 / 127.5, color="#424242", ls="--", lw=1)
first.text(3.5, 0.003, "one pixel bin, 1/127.5 = 0.0078")
first.set_xlabel("step t"); first.set_ylabel("√β_t, typical size of the step's fresh noise")
first.set_xlim(-0.5, 11); first.set_ylim(0, 0.08)
first.set_title("the consequence of δ = 0: a smaller first step")
for ax in (fence, first):
    ax.spines[["top", "right"]].set_visible(False); ax.grid(color="#eeeeee"); ax.set_axisbelow(True)
fig.savefig("cosine-schedule-the-fence-of-101-posts.svg", format="svg", bbox_inches="tight")
```

![Left, 101 green posts at k = 0 to 100, each as tall as C_k, falling from 1 at post 0 through 0.47826 at post 51 to 0 at post 100, with an orange band marking step 50 between posts 50 and 51 and a bracket over the 100 gaps; right, the square root of beta for steps 0 to 9, orange with delta = 0.008 starting at 0.0251 and grey with delta = 0 starting at 0.0157, above a dashed line at the pixel bin 0.0078|900](assets/cosine-schedule-the-fence-of-101-posts.svg)

**How to read this.** On the left the x-axis is the post $k$ and each green line is one post, as tall as its value $C_k$; the orange band is step 50, the gap between posts 50 and 51. On the right the x-axis is the step $t$ and the y-axis $\sqrt{\beta_t}$, the typical size of that step's fresh noise: with the offset (orange) step 0 adds 0.0251, and with δ = 0 (grey) 0.0157. Look at the gap between the two curves at step 0, 3.2 pixel bins of 0.0078 against 2.0.

### Then the word: noise

Each step replaces a share of what is left with noise. That share is read off two neighbouring posts:

$$
\beta_t = 1 - \frac{C_{t+1}}{C_t}
$$

$$
\underbrace{\textcolor{#ef6c00}{\beta_t}}_{\text{noise share of step }t}
=
1-\underbrace{\frac{\textcolor{#2e7d32}{C_{t+1}}}{\textcolor{#2e7d32}{C_t}}}_{\text{fraction that survives the step}},
\qquad
\beta_{50} = 1 - \frac{0.47826}{0.49385} = 0.03155
$$

**What the equation says.** The ratio is the part of the signal that survives one step, so one minus it is the part replaced. The schedule is written in terms of the kept shares and the $\beta$s are derived from them, as the paper does (*cited*, p. 4).

**Why the ratio is there.** A step replaces a share of what its first post kept, so the survivor is the next post divided by this one: $0.47826 / 0.49384 = 0.96845$ at step 50. The difference $C_{50} - C_{51} = 0.01558$ in its place would make $\beta_{50}$ about half as large, a share of the clean signal's whole variance instead of what post 50 kept.

**Why the $1 -$ is there.** The ratio is the part that survives the step, and the noise share is the rest. Without the $1 -$, $\beta_{50}$ would read 0.96845, and step 50 would replace almost all of what was left.

**Why the denominator does not show here.** Each $C$ carries the same $\cos^2\theta_0$, so it [cancels in the ratio](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-normaliser-cancels): $1 - 0.47819/0.49377 = 0.031546$ with the numerators alone, the same $\beta_{50}$.

```python
import math
import matplotlib.pyplot as plt
from cosine import T, delta, C

GREEN, ORANGE, GREY = "#2e7d32", "#ef6c00", "#9e9e9e"
plt.rcParams.update({"font.size": 11, "svg.fonttype": "path"})
BOX = dict(fc="white", ec="none", alpha=0.9, pad=1.5)


def C_unsqueezed(k):  # the posts without the division by 1 + delta
    return math.cos(math.radians((k / T + delta) * 90)) ** 2 / math.cos(math.radians(delta * 90)) ** 2


fig, (mid, end) = plt.subplots(1, 2, figsize=(14, 5.2), gridspec_kw={"wspace": 0.3})
c50, c51 = C(50), C(51)
mid.bar([50, 51], [c50 - 0.4, c51 - 0.4], bottom=0.4, width=0.5, color=GREEN)
mid.bar(51, c50 - c51, bottom=c51, width=0.5, color=ORANGE, alpha=0.4)
mid.axhline(c50, color="#424242", ls=":", lw=1)
mid.text(49.75, c50 + 0.003, f"C₅₀ = {c50:.5f}", color=GREEN, bbox=BOX)
mid.text(50.78, c51 - 0.008, f"C₅₁ = {c51:.5f}", color=GREEN, bbox=BOX)
mid.text(50.3, 0.43, f"ratio C₅₁ / C₅₀\n= {c51 / c50:.5f}\nsurvives step 50", bbox=BOX)
mid.annotate(f"β₅₀ = 1 − {c51 / c50:.5f}\n= {1 - c51 / c50:.5f}\nof what post 50\nkept is replaced",
             (51.2, (c50 + c51) / 2), xytext=(51.4, 0.44), color=ORANGE, bbox=BOX,
             arrowprops={"arrowstyle": "-", "color": ORANGE})
mid.set_xticks([50, 51], ["post 50", "post 51"]); mid.set_xlim(49.5, 52.3); mid.set_ylim(0.40, 0.51)
mid.set_ylabel("C_k, share of the variance kept (y-axis from 0.40)")
mid.set_title("β₅₀ read off two neighbouring posts")
for k in (98, 99, 100):
    end.plot(k - 0.08, C(k), "o", color=GREEN, ms=8)
    end.plot(k + 0.08, C_unsqueezed(k), "s", color=GREY, ms=8)
end.plot([98 - 0.08, 99 - 0.08, 100 - 0.08], [C(k) for k in (98, 99, 100)], color=GREEN)
end.plot([98.08, 99.08, 100.08], [C_unsqueezed(k) for k in (98, 99, 100)], color=GREY, ls="--")
end.text(99.1, 0.00082, f"with ÷ (1 + δ): post 100 at 90°,\nC₁₀₀ = 0, so\nβ₉₉ = 1 − 0 / {C(99):.5f} = 1,\nclipped to 0.999",
         color=GREEN, bbox=BOX)
end.text(99.1, 0.00036, f"without: post 100 at 90.72°,\nC₁₀₀ = {C_unsqueezed(100):.6f}, so\n"
         f"β₉₉ = 1 − {C_unsqueezed(100):.6f} / {C_unsqueezed(99):.7f}\n= −{C_unsqueezed(100) / C_unsqueezed(99) - 1:.1f}, clipped to 0:\nthe last step adds no noise", color="#616161", bbox=BOX)
end.set_xticks([98, 99, 100], ["post 98", "post 99", "post 100"]); end.set_xlim(97.7, 101.6); end.set_ylim(0, 0.00112)
end.set_ylabel("C_k, share of the variance kept (y-axis to 0.0011)")
end.set_title("the consequence of no ÷ (1 + δ): the last post rises")
for ax in (mid, end):
    ax.spines[["top", "right"]].set_visible(False); ax.grid(color="#eeeeee", axis="y"); ax.set_axisbelow(True)
fig.savefig("cosine-schedule-beta-from-two-neighbouring-posts.svg", format="svg", bbox_inches="tight")
```

![Left, posts 50 and 51 as green bars on a y-axis from 0.40, C_50 = 0.49384 and C_51 = 0.47826, the orange slice between them labelled beta_50 = 1 - 0.96845 = 0.03155; right, posts 98, 99 and 100 on a y-axis to 0.0011, green with the division by 1 + delta falling to C_100 = 0 so beta_99 = 1 clipped to 0.999, grey without it falling to 0.0000099 at post 99 and rising to 0.000158 at post 100 so beta_99 = -15.0 clipped to 0|900](assets/cosine-schedule-beta-from-two-neighbouring-posts.svg)

**How to read this.** On the left the two green bars are posts 50 and 51 on a y-axis that starts at 0.40, and the orange slice is what step 50 replaces, 0.03155 of post 50's 0.49384. On the right the y-axis runs only to 0.0011 and shows the last three posts with the division by $1 + \delta$ (green) and without it (grey): without it post 100 sits at 90.72°, past the quarter turn, so its value rises to 0.000158 and $\beta_{99}$ comes out at −15.0, clipped to 0. Look at the grey line turning up at post 100, where the last step would add no noise at all.

### Then the shape word: cosine

The kept share follows a squared cosine as the post walks a quarter turn, from 0.714° to 90°:

$$
C_k \propto \cos^2\theta_k, \qquad 0.714^\circ \le \theta_k \le 90^\circ
$$

$$
\underbrace{\textcolor{#2e7d32}{C_k}}_{\text{share kept}}
\;\propto\;
\underbrace{\cos^2}_{\text{the shape}}\,
\underbrace{\textcolor{#1565c0}{\theta_k}}_{0.714^\circ\text{ to }90^\circ}
$$

**What it means.** [[The Cosine Wave#The quarter turn: where the square is flat|The square is flat at both ends]], so the schedule loses little signal in its first and last steps and most in the middle: 0.00063 at step 0, 0.03155 at step 50. [[The Quarter Turn And The Fraction#Step 3: the quarter turn, squared|Step 3 of the schedule build]] draws $C_k$ at all 101 posts.

**Why the cosine shape is there.** The squared cosine drops 0.067, 0.183, 0.25, 0.25, 0.183 and 0.067 over successive 15° stretches, slow at both ends. [A straight line in its place](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-name-cosine) drops 0.1667 every 15°, and its first step's noise share is 0.0100, 15.8 times the cosine's 0.000631.

### All the words together: the formula

$$
C_k = \frac{\cos^2\!\left(\dfrac{k/T+\delta}{1+\delta}\cdot\dfrac{\pi}{2}\right)}{\cos^2\!\left(\dfrac{\delta}{1+\delta}\cdot\dfrac{\pi}{2}\right)}, \qquad k = 0, 1, \dots, T
$$

$$
\underbrace{\textcolor{#2e7d32}{C_k}}_{\text{share kept at post }k}
=
\frac{
\underbrace{
\cos^2\!\left(
\underbrace{\textcolor{#1565c0}{\frac{k/T+\delta}{1+\delta}}}_{\text{position on the arc}}
\cdot
\underbrace{\frac{\pi}{2}}_{\text{quarter turn}}
\right)
}_{\text{squared cosine at post }k}
}{
\underbrace{
\textcolor{#6a1b9a}{\cos^2\!\left(\frac{\delta}{1+\delta}\cdot\frac{\pi}{2}\right)}
}_{\text{the same at post }0\text{, }0.99984}
},
\qquad k = 0, 1, \dots, T
$$

**What the equation says.** Find the post's [position](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step4-where-the-position-goes) on a quarter arc, turn it into an angle, square its cosine, and divide by the same square at post 0. [Term by term at post 51](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-one-boundary): position 0.5139, angle 46.25°, $\cos^2 = 0.47819$, divided by 0.99984 gives 0.47826.

**Why $k/T$ is there.** It turns post numbers 0 to 100 into positions 0 to 1. Without it the angle at post 51 would be 51 quarter turns (50.60 after the offset and the division, 4554°).

**Why δ is there.** The [offset](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-name-offset) 0.008 moves post 0 to 0.714°, off the flat start. Without it the first step's noise share is 0.000247 instead of 0.000631.

**Why the division by 1 + δ is there.** It keeps post 100 at exactly 90°. Without it [post 100 sits at 90.72°](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step4-dropping-the-rescale) and keeps 0.000158 of the signal. The frame on [where each post's position comes from](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-position-derived) switches this division on and off.

**Why π/2 and the square are there.** π/2 is [[Radians#Then the conversion: degrees to radians|the quarter turn in radians]], 90°. The square turns the [[Polar Coordinates#The point: from length and angle to x and y|horizontal leg]] into [[The Cosine Wave#The two shares|its share of 1]]: 0.6915 becomes 0.47819.

**Without π/2 or without the square.** With the position fed in as radians, post 100 stops at 1 radian, 57.30°, and keeps 0.29194, so the schedule never reaches pure noise. Without the square, $C_{51}$ is the multiplier 0.69157 instead of the share 0.47826.

**Why the denominator is there.** It makes $C_0 = 1$ exactly and cancels out of every $\beta_t$, [[The Quarter Turn And The Fraction#Step 4: the fraction|drawn as bars in step 4 of the schedule build]]. [[The Quarter Turn And The Fraction#The consequence: remove a piece|Removing each piece in turn]] shows that only the offset and the square change any step's noise.

**Without the denominator.** The [normaliser](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-name-normaliser) is $\cos^2\theta_0 = 0.99984$. Without it $C_0$ reads 0.99984 and every post sits lower by that factor, while $\beta_0$ stays 0.000631.

**Drawn.** [[How Each Piece Of The Cosine Schedule Works#How each piece of C_k works|The six moves at post 51]] are drawn there, with the denominator removed in a panel beside them.

### The consequence: the kept share after step t is the next post

Because each step's survivor is a ratio of two neighbouring posts, multiplying the survivors cancels every post in between:

$$
\bar\alpha_t = \prod_{j=0}^{t} (1 - \beta_j) = C_{t+1}
$$

$$
\underbrace{\bar\alpha_t}_{\text{kept after step }t}
=
\prod_{j=0}^{t}\underbrace{\frac{\textcolor{#2e7d32}{C_{j+1}}}{\textcolor{#2e7d32}{C_j}}}_{1-\textcolor{#ef6c00}{\beta_j}}
=
\frac{\cancel{C_1}}{C_0}\cdot\frac{\cancel{C_2}}{\cancel{C_1}}\cdots\frac{C_{t+1}}{\cancel{C_t}}
=
\frac{\textcolor{#2e7d32}{C_{t+1}}}{\textcolor{#2e7d32}{C_0}}
=
\textcolor{#2e7d32}{C_{t+1}}
$$

**What it means.** At step 50 the product of 51 survivors is $C_{51} = 0.47826$, and the product matches $C_{t+1}$ to within $1.7 \times 10^{-18}$ at every step up to 98. The clip breaks it at the last step only: $\beta_{99}$ is clipped from 1 to 0.999, so $\bar\alpha_{99} = 0.001 \times C_{99} = 2.4 \times 10^{-7}$ instead of $C_{100} = 0$.

## Try the boundary values yourself

Navigation: ⬅️ [[#The boundary values C_k]] | 📋 [[#Table of contents|TOC]] | [[#How each piece of C_k works]] ➡️

**In two lines.** Nine steps in an empty folder, from the formula as three functions to four boundaries by hand, the code's form beside $\bar\alpha$ and three more boundaries, each output read field by field, are in [[Running The Cosine Noise Schedule#Try the boundary values yourself]]. Its step 3 makes the `cosine.py` that every figure script in this note imports.

## How each piece of C_k works

Navigation: ⬅️ [[#Try the boundary values yourself]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to get the boundary values]] ➡️

**In two lines.** The formula run one move per line from the post number to $C_k$, drawn at post 51, then the angles of posts 0, 1, 51 and 100 on the unit circle with the broken runs beside them, are in [[How Each Piece Of The Cosine Schedule Works#How each piece of C_k works]]. The deep-dive sheet that composes them is still waiting there.

## Other ways to get the boundary values

Navigation: ⬅️ [[#How each piece of C_k works]] | 📋 [[#Table of contents|TOC]] | [[#Why the boundary values matter]] ➡️

**The code's form, in radians.** As in [[Running The Cosine Noise Schedule#Try the boundary values yourself|step 7 of the sandbox]]: `np.cos(((x / timesteps) + s) / (1 + s) * np.pi * 0.5) ** 2`, then divided by its first entry. It is what the rebuild runs, and it gives every boundary at once.

**Read them off $\bar\alpha$.** If a schedule's $\bar\alpha$ values are already printed, $C_{t+1} = \bar\alpha_t$ for this schedule while no $\beta$ is clipped, as step 7 shows.

**Drag them.** [Dissolving the Dog](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-2), Timetable 2 of 5, "Compute one Cₖ, piece by piece", has presets for $k = 0, 1, 51, 99$ and $\delta = 0$, and draws the angle on a quarter circle.

## Why the boundary values matter

Navigation: ⬅️ [[#Other ways to get the boundary values]] | 📋 [[#Table of contents|TOC]] | [[#The cosine schedule taught in, applied in]] ➡️

**Every number starts here.** Every number the forward process uses comes from these 101 values. The kept share $\bar\alpha_t$ is $C_{t+1}$, and each step's noise $\beta_t$ is read off two neighbouring boundaries, which is why the paper builds the schedule "in terms of $\bar\alpha_t$" and derives the $\beta$s from it (*cited*, p. 4).

**What tracing buys.** Tracing $0.4783$ back to $\cos^2 46.25^\circ$ is what makes the numbers in [[The Forward Process]], [[From Many Steps To One Jump]] and [[The Density Of The One Jump]] checkable by hand.

## The cosine schedule taught in, applied in

Navigation: ⬅️ [[#Why the boundary values matter]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the PoE derivation foundations journey's [chapter 9.3 on ᾱ from a β schedule](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/09-the-forward-process-by-hand.md#93-abar-from-a-beta-schedule-including-the-log-sum-shortcut), its paragraph "Where a schedule's βs come from": the schedule built from the curve ᾱ should follow, with $C_{51} = 0.4783$ computed by hand
- the [`drip --math` walk of the forward process and the score](../../../../PhD/reduce-reuse-recycle/artifacts/drips/forward-process-and-the-score/00-INDEX.md) in the reduce-reuse-recycle research repository, piece 2, [rung 1 as the walk kept it](../../../../PhD/reduce-reuse-recycle/artifacts/drips/forward-process-and-the-score/kept/05-the-cosine-boundary-values-by-hand.md): the definition with $T = 100$ and $\delta = 0.008$, the angle in degrees, $C_0 = 1$, $C_1 = 0.99937$, $C_{51} = 0.47826$ and $C_{100} = 0$ by hand, and the broken run without the offset

**Applied in:** [step 4 of the one-expert rebuild walk](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-4-the-forward-process-and-the-cosine-schedule) in the reduce-reuse-recycle research repository, whose [`cosine_beta_schedule`](../../../../PhD/reduce-reuse-recycle/rebuild/model.py) (lines 13 to 19) lays out the 100 noise levels one diffusion expert is trained on.

> [!note]- How this was checked
> The six sandbox scripts and their outputs are checked in [[Running The Cosine Noise Schedule]], whose box records the run. `same_as_code.py` there is the rebuild's `cosine_beta_schedule` (`rebuild/model.py`, lines 13 to 19) written without NumPy, and its values match the rebuild's `rebuild/out/walk-numbers.json`.
>
> The two figure scripts here were run on 2026-10-21 on mscluster (Linux) with Python 3.12.10, matplotlib 3.10.8 and the sandbox's `cosine.py`, in an empty `~/playground/sandbox/cosine-retrofit`, by vault-writer, and each SVG was opened (rendered to PNG by PyMuPDF 1.27.2) before filing. The fence here and the formula at post 51 in [[How Each Piece Of The Cosine Schedule Works]] replace drawn prompt 40 (the form), and the quarter circle there replaces prompt 41 (the mechanism), in `.prompts/Diffusion Models.md`, because their faithfulness notes fix exact heights, angles and lengths.
>
> The with-and-without numbers were computed that day by a throwaway script on the same `cosine.py`: $C_{50} = 0.49384$ and $\beta_{49} = 0.03059$; the ratio 0.96845 against the difference 0.01558 and the numerators alone 0.031546; without the division by $1 + \delta$, $C_{99} = 0.0000099$, $C_{100} = 0.000158$ and $\beta_{99} = -15.0$; positions fed in as radians, post 100 at 57.30° keeping 0.29194; a straight line in place of $\cos^2$, $\beta_0 = 0.0100$; without $k/T$, 50.60 quarter turns at post 51; and $\bar\alpha_t$ against $C_{t+1}$, largest gap $1.7 \times 10^{-18}$ up to step 98, with $\bar\alpha_{99} = 2.4 \times 10^{-7}$.
>
> Nichol and Dhariwal's section 3.2 and equation (17) were read from the arXiv PDF of 2102.09672 (version 1), page 4, fetched on 2026-10-21; the quotations are from that page. The trigonometry handbook's PDF pages 7 (radians and degrees, 360° and 2π in one rotation) and 10 (the unit circle, the x-coordinate is the cosine of the angle) were opened and read as text. The scene's Timetable 2 frame was read from its page source; its presets are $k = 0, 1, 51, 99$ and $\delta = 0$. The other scene frames linked here are as the walk's retrofit brief records them. No tldr-pages entry covers this.
