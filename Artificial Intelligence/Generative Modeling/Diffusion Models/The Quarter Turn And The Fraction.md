---
aliases: [the quarter turn of the cosine schedule, quarter turn and the fraction, C_k against k, the C_k curve, numerator and denominator of C_k, the C_k fraction, "C_k = cos^2(theta_k) / cos^2(theta_0)", why C_k divides by cos^2 theta_0, the denominator cancels in beta, first step noise without the offset, what each piece of C_k does, the quarter turn squared, the fraction's numerator and denominator, remove a piece of C_k]
sources:
  - "Nichol, Dhariwal, Improved Denoising Diffusion Probabilistic Models, ICML 2021, section 3.2 and equation (17), PDF p. 4: https://arxiv.org/pdf/2102.09672#page=4"
  - "Anton, Bivens, Davis, Calculus, section 2.5 (derivatives of sine and cosine), PDF p. 193, and section 2.6 (the chain rule), PDF p. 198: ../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf"
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Trigonometry, radians and degrees, one rotation is 360 degrees or 2 pi radians, PDF p. 7: ../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf#page=7"
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Pre-Algebra, multiplying and dividing fractions, reducing a factor shared by numerator and denominator, PDF p. 25: ../../../Mathematics/references/textbooks/general/pre-algebra-handbook.pdf#page=25"
standard: vault-note v2
---

# The Quarter Turn And The Fraction

Up: [[Diffusion Models]] · ⬅️ [[Running The Quarter Circle Under The Cosine Schedule]] · [[Which Pieces Of C_k Change The Noise]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[The Quarter Circle Under The Cosine Schedule]] for where the posts sit, and [[The Cosine Wave]] for why $\cos^2$ is flat at 0° and 90°.

**Square the cosine at every post and divide by its value at post 0, and you have the 101 boundary values $C_k$.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. It has no questions on this note yet.

> [!warning]- Unfinished
> - The diffusion models quiz has no questions on this note yet.

Stated claims: 0.

**What this note draws.** The last two steps of the quarter-circle build: the squared cosine walked across all 101 posts, and the fraction that makes $C_0 = 1$. Then it removes each piece of the formula in turn and counts what changes.

**Where the scripts run.** Each figure script imports `plane.py` and `cosine.py` and needs matplotlib, so run it in the folder that [[Running The Quarter Circle Under The Cosine Schedule#Try the quarter circle yourself|step 3 of the quarter circle's sandbox]] makes. [[Running The Quarter Turn And The Fraction]] runs both scripts there, with the removals script of [[Which Pieces Of C_k Change The Noise]], and reads every output.

**Colours in this note.** <span style="color:#2e7d32">**Green is the squared cosine $\cos^2\theta_k$ and the boundary value $C_k$, the share kept**</span>, <span style="color:#ef6c00">**orange is a step's noise share $\beta_t$ and the sine in the slope**</span>, <span style="color:#1565c0">**blue is a post's position $p_k$ and its angle $\theta_k$**</span>, <span style="color:#6a1b9a">**purple is the denominator $\cos^2\theta_0$**</span>, and <span style="color:#9e9e9e">**grey is a case with a piece removed**</span>, as in [[The Cosine Noise Schedule]].

## Table of contents

- [[#The squared cosine and its fraction]]
- [[#Step 3: the quarter turn, squared]]
- [[#Step 4: the fraction]]
- [[#Try the fraction yourself]]
- [[#How the denominator cancels]]
- [[#Other ways to see the fraction]]
- [[#Why the fraction matters]]
- [[#The fraction taught in, applied in]]

## The squared cosine and its fraction

Navigation: 📋 [[#Table of contents|TOC]] | [[#Step 3: the quarter turn, squared]] ➡️

**The boundary value as a fraction**, also the $C_k$ fraction or $\cos^2\theta_k / \cos^2\theta_0$: the squared cosine at post $k$ divided by the squared cosine at post 0, so that $C_0 = 1$.

**When to reach for it.** When you need to know which piece of the cosine schedule changes how much noise a step adds. Or when $C_0$ has to be exactly 1 although post 0 sits off the axis.

### The fraction at four posts

<table>
<tr><th>post k</th><th style="color:#1565c0">angle θ<sub>k</sub></th><th style="color:#2e7d32">cos² θ<sub>k</sub></th><th style="color:#6a1b9a">cos² θ<sub>0</sub></th><th style="color:#2e7d32">C<sub>k</sub></th><th style="color:#9e9e9e">C<sub>k</sub> with δ = 0</th></tr>
<tr><td>0</td><td>0.714°</td><td>0.99984</td><td style="border:2px solid #212121">0.99984</td><td style="border:2px solid #212121">1</td><td>1</td></tr>
<tr><td>1</td><td>1.607°</td><td>0.99921</td><td>0.99984</td><td style="border:2px solid #212121">0.99937</td><td style="border:2px dashed #212121">0.99975</td></tr>
<tr style="background:#fff8e1"><td><b>51</b></td><td>46.25°</td><td style="border:2px solid #212121"><b>0.47819</b></td><td>0.99984</td><td style="border:2px solid #212121"><b>0.47826</b></td><td>0.48430</td></tr>
<tr><td>100</td><td>90°</td><td>0</td><td>0.99984</td><td>0</td><td>0</td></tr>
</table>

**How to read this table.** Each row is one post. The green column divided by the purple column gives $C_k$, the share of the clean signal's variance kept at that post. The last column is the same calculation with the offset δ set to 0.

**What to look for.** The purple column never changes: one number divides every post. Post 1 is the first step, 0.99937 against 0.99975 without the offset. Post 51 is $\bar\alpha_{50} = 0.4783$.

## Step 3: the quarter turn, squared

Navigation: ⬅️ [[#The squared cosine and its fraction]] | 📋 [[#Table of contents|TOC]] | [[#Step 4: the fraction]] ➡️

Textbook: [Anton, Calculus, the chain rule, PDF p. 198](../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=198)

**What step 3 does.** Walk the post from 0 to 100 and the angle sweeps the quarter turn; [[The Cosine Wave#The quarter turn: where the square is flat|the square of its cosine]] falls from 1 to 0. "Quarter turn" is two words, taken apart below: the turn first, then the quarter, then both together and what follows from them.

### The base word: turn

**What the word means.** A turn is one full rotation round the circle, which is [360°, or 2π radians](../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf#page=7).

$$
1\ \text{turn} = 360^\circ = 2\pi\ \text{rad}
$$

$$
\underbrace{1\ \text{turn}}_{\text{one full rotation}}
=
\underbrace{360^\circ}_{\text{in degrees}}
=
\underbrace{\textcolor{#1565c0}{2\pi}\ \text{rad}}_{6.2832\text{, in radians}}
$$

**What it means.** Over one turn the cosine runs from 1 down to −1 and back to 1, so its square falls to 0 and climbs back to 1 twice. The schedule wants a share that only ever falls, so it uses part of a turn.

### Then the word: quarter

**What the word means.** A quarter turn is 90°, or π/2 = 1.5708 rad, and each post's angle is its position times it:

$$
\theta_k = p_k \cdot \frac{\pi}{2}
$$

$$
\underbrace{\textcolor{#1565c0}{\theta_k}}_{\text{post }k\text{'s angle}}
=
\underbrace{\textcolor{#1565c0}{p_k}}_{\text{position, 0 to 1}}
\cdot
\underbrace{\frac{\pi}{2}}_{\text{a quarter of }2\pi}
$$

**What the equation says.** The position runs from 0.0079 at post 0 to exactly 1 at post 100, so the angle runs from 0.714° to 90° and never past. Post 51's position, 0.51389, gives 46.25°.

**Why a quarter and not a whole turn.** Spread the posts over a whole turn and post 25 sits at 92.14° with $C_{25} = 0.0014$. Post 51, at 185°, is back up to $C_{51} = 0.9949$, and post 100 ends at $C_{100} = 1.0025$: the clean image returns.

### All the words together: the quarter turn, squared

The share kept follows the squared cosine of the angle, and its slope comes from the [derivative of the cosine](../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=193) and [the chain rule](../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=198):

$$
C_k \;\propto\; \cos^2\theta_k,
\qquad
\frac{d}{d\theta}\cos^2\theta = -2\cos\theta\sin\theta
$$

$$
\underbrace{\textcolor{#2e7d32}{C_k}}_{\text{share kept at post }k}
\;\propto\;
\underbrace{\textcolor{#2e7d32}{\cos^2\theta_k}}_{\text{squared horizontal leg}},
\qquad
\underbrace{\frac{d}{d\theta}\cos^2\theta = -2\,\textcolor{#2e7d32}{\cos\theta}\,\textcolor{#ef6c00}{\sin\theta}}_{0\text{ at }0^\circ\text{ and }90^\circ,\ -1\text{ at }45^\circ}
$$

**What the equation says.** The share kept follows [the squared cosine](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-name-cosine), so it falls slowly near post 0, fastest near post 50 and slowly again near post 100. The slope is twice the product of the two legs, and one leg is 0 at each end.

**Why the ∝ is there.** It reads "proportional to": $C_k$ is $\cos^2\theta_k$ times one fixed number, $1/\cos^2\theta_0 = 1.00016$, which step 4 supplies. With an equals sign in its place, $C_0$ would read 0.99984 instead of 1.

**Why the square is there.** It turns the horizontal leg, the clean point's multiplier, into its variance share, and it is what makes the end flat. Without it the curve is $\cos\theta_k / \cos\theta_0$: $C_{51} = 0.69157$, the drops per 15° grow from 0.034 to 0.259 instead of rising and falling, and the last step drops 0.015584 instead of 0.000243. [[#The consequence: remove a piece]] draws it.

**Why the factor 2 is there.** The chain rule multiplies the outer square's slope, $2\cos\theta$, by the inner cosine's slope, $-\sin\theta$. At post 51 the slope is −0.9990 per radian, and over the 0.015583 rad from post 50 it predicts a drop of 0.015568 against the measured $\cos^2\theta_{50} - \cos^2\theta_{51} = 0.015577$. Without the 2 the prediction would be 0.007784, half the drop the schedule makes.

**Why the offset matters here.** With δ = 0 post 0 sits at 0°, where the slope is exactly 0, so the first step loses only $1 - 0.99975 = 0.000247$ of the variance. With δ = 0.008 post 0 sits at 0.714°, where [the slope is already −0.0249 per radian](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-why-offset), and the first step loses 0.000631. Nichol and Dhariwal add the offset because "having tiny amounts of noise at the beginning of the process made it hard for the network to predict ϵ accurately enough" (*cited*, [p. 4](https://arxiv.org/pdf/2102.09672#page=4)).

### The consequence: slow at both ends, fastest in the middle

**What changes.** Walk the point [every 15° round the quarter turn](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-quarter-turn) and the square falls by 0.067, 0.183, 0.25, 0.25, 0.183 and 0.067. So the schedule adds little noise in its first and last steps and most in the middle.

<table>
<tr><th style="color:#1565c0">angle θ</th><th style="color:#2e7d32">cos² θ</th><th>drop over the next 15°</th><th>slope −2 cos θ sin θ, per radian</th><th style="color:#9e9e9e">drop without the square</th></tr>
<tr><td>0°</td><td>1</td><td style="border:2px solid #212121">0.067</td><td>0</td><td>0.034</td></tr>
<tr><td>15°</td><td>0.933</td><td>0.183</td><td>−0.5</td><td>0.100</td></tr>
<tr><td>30°</td><td>0.75</td><td>0.25</td><td>−0.866</td><td>0.159</td></tr>
<tr style="background:#fff8e1"><td><b>45°</b></td><td><b>0.5</b></td><td style="border:2px solid #212121"><b>0.25</b></td><td style="border:2px solid #212121"><b>−1</b></td><td>0.207</td></tr>
<tr><td>60°</td><td>0.25</td><td>0.183</td><td>−0.866</td><td>0.241</td></tr>
<tr><td>75°</td><td>0.067</td><td style="border:2px solid #212121">0.067</td><td>−0.5</td><td style="border:2px dashed #212121">0.259</td></tr>
<tr><td>90°</td><td>0</td><td></td><td>0</td><td></td></tr>
</table>

**How to read this table.** Each row is one angle on the quarter turn. The drop columns are how far the value falls before the next row, with the square and without it ($\cos\theta$ alone), and the slope is the rate at that angle.

**What to look for.** The boxed drops: 0.067 at both ends against 0.25 in the middle, where the slope reaches −1. Without the square the last drop is the largest, 0.259.

```python
import matplotlib.pyplot as plt
from plane import save, GREEN, GREY
from cosine import T, C

for k in (0, 1, 51, 100):
    print(f"C_{k} = {C(k):.5f}")
print(f"first step's noise share: 1 - C_1 = {1 - C(1):.6f} with delta = 0.008, {1 - C(1, 0):.6f} with delta = 0")

fig, ax = plt.subplots(figsize=(9, 5))
ks = range(T + 1)
ax.plot(ks, [C(k) for k in ks], "o", color=GREEN, ms=4)
for k, label, xy in ((0, "post 0: 1", (6, 1.03)), (1, "post 1: 0.99937", (10, 0.72)),
                     (51, "post 51: 0.47826", (22, 0.3)), (100, "post 100: 0", (78, 0.2))):
    ax.plot(k, C(k), "o", color="black", ms=8, mfc="none")
    ax.annotate(label, (k, C(k)), xytext=xy, fontsize=10, arrowprops={"arrowstyle": "-", "color": "black", "lw": 0.8})
ax.text(10, 0.82, "flat start", color=GREEN, fontsize=10)
ax.text(88, 0.1, "flat end", color=GREEN, fontsize=10)
ax.set_xlabel("post k")
ax.set_ylabel("C_k, share of the clean signal's variance kept")
ax.set_xlim(-2, 102)
ax.set_ylim(-0.05, 1.08)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(color="#eeeeee")
ax.set_title("C_k at all 101 posts: slow at both ends, fastest in the middle", fontsize=12)

inset = ax.inset_axes([0.55, 0.52, 0.42, 0.4])
for d, color, name in ((0.008, GREEN, "δ = 0.008"), (0.0, GREY, "δ = 0")):
    inset.plot([0, 1, 2], [C(k, d) for k in (0, 1, 2)], "o-", color=color, ms=5)
    inset.text(2.05, C(2, d), name, color=color, fontsize=9, va="center")
inset.text(0.05, 0.99905, "first step loses\n0.000631 (δ = 0.008)\n0.000247 (δ = 0)", fontsize=8)
inset.set_xticks([0, 1, 2])
inset.set_xlim(-0.1, 2.6)
inset.set_title("the first step, magnified", fontsize=9)
inset.tick_params(labelsize=8)
save(fig, "s3-quarter-turn-cos-squared.svg")
```

![C_k against post k for all 101 posts as green dots falling from 1 to 0, flat at both ends, with posts 0, 1, 51 and 100 ringed and labelled 1, 0.99937, 0.47826 and 0, and an inset magnifying posts 0 to 2 where the delta = 0 schedule in grey falls less over the first step|800](assets/s3-quarter-turn-cos-squared.svg)

**How to read this.** The x-axis is the post $k$ from 0 to 100 and the y-axis is $C_k$, the share kept; each green dot is one post. In the inset the y-axis runs only from about 0.998 to 1.000, so the first step's drop is visible. Look at the inset: the green line falls 0.000631 from post 0 to post 1, the grey one only 0.000247.

## Step 4: the fraction

Navigation: ⬅️ [[#Step 3: the quarter turn, squared]] | 📋 [[#Table of contents|TOC]] | [[#Try the fraction yourself]] ➡️

**What step 4 does.** It divides the squared cosine at every post by its value at post 0. "The fraction" has two parts, read top then bottom: the numerator, then the denominator.

### The numerator: the squared cosine at post k

**What it is.** The top of the fraction is step 3's squared cosine at post $k$, the share the schedule would keep before any correction.

$$
f(k) = \cos^2\theta_k
$$

$$
\underbrace{\textcolor{#2e7d32}{f(k)}}_{\text{numerator at post }k}
=
\underbrace{\textcolor{#2e7d32}{\cos^2\theta_k}}_{\text{squared horizontal leg}}
$$

**What it means.** At post 51 the numerator is $\cos^2 46.25^\circ = 0.47819$. At post 0 it is $\cos^2 0.714^\circ = 0.99984$, not 1, because the offset moved post 0 off the axis.

### The denominator: the same at post 0

**What it is.** The bottom of the fraction is the numerator's value at post 0, one number shared by every post, the [normaliser $\cos^2\theta_0$](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-name-normaliser).

$$
f(0) = \cos^2\theta_0 = 0.99984
$$

$$
\underbrace{\textcolor{#6a1b9a}{f(0)}}_{\text{denominator}}
=
\underbrace{\textcolor{#6a1b9a}{\cos^2\theta_0}}_{\text{the numerator at post 0}}
=
\underbrace{0.99984}_{\cos^2 0.714^\circ}
$$

**What it means.** With δ = 0 post 0 sits at 0° and the denominator is $\cos^2 0^\circ = 1$, so dividing by it would change nothing. The denominator is there only because the offset moved post 0.

### All the words together: the fraction

$$
C_k = \frac{\cos^2\theta_k}{\cos^2\theta_0},
\qquad
C_{51} = \frac{0.47819}{0.99984} = 0.47826
$$

$$
\underbrace{\textcolor{#2e7d32}{C_k}}_{\text{boundary value}}
=
\frac{
\underbrace{\textcolor{#2e7d32}{\cos^2\theta_k}}_{\text{numerator: squared cosine at post }k}
}{
\underbrace{\textcolor{#6a1b9a}{\cos^2\theta_0}}_{\text{denominator: the same at post }0,\ 0.99984}
},
\qquad
C_{51} = \frac{0.47819}{0.99984} = 0.47826
$$

**What the equation says.** $C_k$ asks how many denominators fit in the numerator. At post 0 the two are the same number, so $C_0 = 1$ exactly: before the first step all of the clean signal is kept. The scene's frame [one boundary, term by term](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-one-boundary) draws numerator, denominator and ratio as three bars.

**Why the denominator is there.** The offset puts post 0 at 0.714°, where $\cos^2 = 0.99984$, not 1. Dividing by that one number stretches the whole curve by 1.00016 so it starts on 1.

**Why it changes no step's noise.** Each step's noise is $\beta_t = 1 - C_{t+1}/C_t$, a ratio of two boundary values. The denominator sits on top and underneath, so [it cancels](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-normaliser-cancels):

$$
\beta_{50}
=
1-\frac{\cos^2\theta_{51}\,/\,\cos^2\theta_0}{\cos^2\theta_{50}\,/\,\cos^2\theta_0}
=
1-\frac{0.47819}{0.49377}
=
0.03155
$$

$$
\underbrace{\textcolor{#ef6c00}{\beta_{50}}}_{\text{step 50's noise share}}
=
1-\frac{\textcolor{#2e7d32}{\cos^2\theta_{51}}\,/\,\overbrace{\textcolor{#6a1b9a}{\cos^2\theta_0}}^{0.99984}}{\textcolor{#2e7d32}{\cos^2\theta_{50}}\,/\,\underbrace{\textcolor{#6a1b9a}{\cos^2\theta_0}}_{0.99984}}
=
1-\underbrace{\frac{\textcolor{#2e7d32}{0.47819}}{\textcolor{#2e7d32}{0.49377}}}_{\text{numerators only}}
=
\textcolor{#ef6c00}{0.03155}
$$

**What the equation says.** Opened up, both boundary values carry the same 0.99984 underneath, and [dividing one by the other](../../../Mathematics/references/textbooks/general/pre-algebra-handbook.pdf#page=25) strikes it out. What is left is the ratio of the numerators, 0.96845, so $\beta_{50} = 0.03155$ with the denominator or without it.

```python
import matplotlib.pyplot as plt
from plane import save, GREEN, ORANGE, PURPLE, GREY
from cosine import T, f, C

for k in (0, 1, 51, 100):
    print(f"post {k:3d}: {f(k):.5f} / {f(0):.5f} = {C(k):.5f}")
beta_C = [min(1 - C(t + 1) / C(t), 0.999) for t in range(T)]
beta_f = [min(1 - f(t + 1) / f(t), 0.999) for t in range(T)]
print(f"beta_0 {beta_C[0]:.6f} / {beta_f[0]:.6f}   beta_50 {beta_C[50]:.5f} / {beta_f[50]:.5f}   largest gap {max(abs(a - b) for a, b in zip(beta_C, beta_f)):.1e}")

fig, (left, right) = plt.subplots(1, 2, figsize=(13, 4.8))
for i, k in enumerate((0, 1, 51, 100)):
    for j, (value, color, name) in enumerate(((f(k), GREEN, "cos²θₖ"), (f(0), PURPLE, "cos²θ₀"), (C(k), "#1b5e20", "Cₖ"))):
        x = 5.5 * i + 1.5 * j
        left.bar(x, value, color=color, width=1.3)
        left.text(x, value + 0.02, f"{value:.5f}".rstrip("0").rstrip("."), ha="center", fontsize=8, rotation=90)
        left.text(x, -0.02, name, ha="center", va="top", fontsize=9, rotation=90)
    left.text(5.5 * i + 1.5, -0.3, f"post {k}", ha="center", fontsize=10)
left.set_ylim(-0.35, 1.3)
left.set_yticks([0, 0.25, 0.5, 0.75, 1])
left.set_xticks([])
left.spines[["top", "right", "bottom"]].set_visible(False)
left.set_title("numerator / denominator = Cₖ at four posts", fontsize=12)

ts = range(T)
right.plot(ts, beta_C, "o", color=ORANGE, ms=7, mfc="none")
right.plot(ts, beta_f, ".", color=GREY, ms=4)
right.set_yscale("log")
right.text(4, 0.0005, "β₀ = 0.000631 both ways", fontsize=10)
right.set_ylim(3e-4, 2)
right.text(42, 0.012, "β₅₀ = 0.03155 both ways", fontsize=10)
right.text(55, 0.6, "β₉₉ clipped to 0.999", fontsize=10)
right.text(2, 0.2, "rings: from Cₖ (with the denominator)\ndots: from cos²θₖ alone", fontsize=9)
right.set_xlabel("step t")
right.set_ylabel("βₜ = 1 − Cₜ₊₁ / Cₜ  (log scale)")
right.spines[["top", "right"]].set_visible(False)
right.grid(color="#eeeeee")
right.set_title("every step's noise is the same without the denominator", fontsize=12)
fig.tight_layout()
save(fig, "s4-the-fraction.svg")
```

![Left, three bars at each of posts 0, 1, 51 and 100: the numerator cos squared theta k in green, the constant denominator 0.99984 in purple and their ratio C_k in dark green; right, beta t against step t on a log scale, orange rings computed with the denominator and grey dots without it, lying on top of each other from 0.000631 at step 0 to the clip 0.999 at step 99|900](assets/s4-the-fraction.svg)

**How to read this.** On the left the y-axis is a share from 0 to 1 and each group of three bars is one post: numerator, denominator, ratio. On the right the x-axis is the step $t$ and the y-axis is $\beta_t$ on a log scale, so the small early steps are visible; this axis is not linear. Look at the right panel: every grey dot sits inside its orange ring.

### The consequence: remove a piece

| piece removed | what changes, on the toy's numbers | where it shows |
|---|---|---|
| the offset δ | post 0 at 0°; the first step's noise share falls from 0.000631 to 0.000247, its typical size from 0.0251 to 0.0157 | the grey posts of [[The Quarter Circle Under The Cosine Schedule#The consequence: move the posts]]; step 3's inset |
| the division by 1 + δ | post 100 at 90.72°; $C_{100} = 0.000158$ instead of 0, so the last step leaves some signal; $\beta_{50}$ moves from 0.031546 to 0.032198, and $\beta_{99}$ is −15.0, clipped to 0 | the right panel of [[Which Pieces Of C_k Change The Noise#Removing each piece, drawn]]; the rebuild walk [drops the rescale](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step4-dropping-the-rescale) by hand |
| the denominator $\cos^2\theta_0$ | $C_0 = 0.99984$ instead of 1; every $C_k$ is 0.016% low; every $\beta_t$ unchanged | step 4, both panels |
| the square | $C_{51}$ would be the multiplier 0.69157, not the share 0.47826, and the curve would end at slope −1 instead of flat | the left panel of [[Which Pieces Of C_k Change The Noise#Removing each piece, drawn]]; the dashed tangent in [[The Cosine Wave#The quarter turn: where the square is flat]] |

**How to read this table.** Each row switches off one piece of $C_k = \cos^2\theta_k / \cos^2\theta_0$ with the others kept, and gives the number that moves.

**What to look for.** Only the denominator's row leaves every $\beta_t$ as it was. The clip to 0 in the division's row is the rebuild's own `np.clip(betas, 0, 0.999)`.

**The removals, drawn.** [[Which Pieces Of C_k Change The Noise#Removing each piece, drawn]] draws the square and the division by $1 + \delta$ each removed, beside the schedule, with the script that computes them.

## Try the fraction yourself

Navigation: ⬅️ [[#Step 4: the fraction]] | 📋 [[#Table of contents|TOC]] | [[#How the denominator cancels]] ➡️

**In two lines.** Nine steps in the quarter circle's folder, from the curve and its first step to β with and without the denominator and two pieces removed, are in [[Running The Quarter Turn And The Fraction#Try the fraction yourself]]. Every output is read field by field in [[Running The Quarter Turn And The Fraction#Reading the fraction output]].

## How the denominator cancels

Navigation: ⬅️ [[#Try the fraction yourself]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to see the fraction]] ➡️

**In two lines.** The cancellation written for every step $t$, with steps 0, 50 and 98 worked both ways, is in [[Which Pieces Of C_k Change The Noise#How the denominator cancels]]. A ratio of two boundary values strikes the shared 0.99984 out, while a difference would keep it.

## Other ways to see the fraction

Navigation: ⬅️ [[#How the denominator cancels]] | 📋 [[#Table of contents|TOC]] | [[#Why the fraction matters]] ➡️

**Drag it.** The scene Dissolving the Dog, [frame "one boundary"](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-one-boundary), draws the numerator, denominator and ratio bars with a switch that drops the denominator. Its [frame "the quarter turn"](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-quarter-turn) walks the angle.

**Only the numbers.** [[Running The Cosine Noise Schedule#Try the boundary values yourself]] computes the same four boundaries by hand.

## Why the fraction matters

Navigation: ⬅️ [[#Other ways to see the fraction]] | 📋 [[#Table of contents|TOC]] | [[#The fraction taught in, applied in]] ➡️

**Every number comes from here.** Every number the forward process uses comes from these 101 values: $\bar\alpha_t = C_{t+1}$ and $\beta_t$ from neighbouring posts.

**Which pieces touch the noise.** Knowing which piece does what tells you which ones touch the noise: the offset and the square change it, the denominator only relabels the start.

## The fraction taught in, applied in

Navigation: ⬅️ [[#Why the fraction matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the [`drip --math` walk of the forward process and the score](../../../../PhD/reduce-reuse-recycle/artifacts/drips/forward-process-and-the-score/00-INDEX.md) in the reduce-reuse-recycle research repository, [piece 2, rung 1 as the walk kept it](../../../../PhD/reduce-reuse-recycle/artifacts/drips/forward-process-and-the-score/kept/05-the-cosine-boundary-values-by-hand.md): the quarter turn, the fraction's numerator and denominator, why the offset, and the learner's request to see each step drawn by the code that computes it
- [step 4 of the one-expert rebuild walk](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-4-the-forward-process-and-the-cosine-schedule) in the same repository, "On paper 5: play with the quarter turn" and "On paper 6, the fraction"

**Applied in:** wherever [[The Cosine Noise Schedule]] is applied: the rebuild's [`cosine_beta_schedule`](../../../../PhD/reduce-reuse-recycle/rebuild/model.py) (lines 13 to 19), whose line 17 divides by the post-0 value and line 18 takes the ratio that cancels it, for the 100 noise levels one diffusion expert is trained on.

> [!note]- How this was checked
> The two figure scripts were run on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and matplotlib 3.10.8 from the machine's `python3`, in the empty folder `~/playground/sandbox/quarter-turn-fraction`, with `plane.py` copied from the Trigonometry sandbox and `cosine.py` as [[Running The Quarter Circle Under The Cosine Schedule]] gives it; the folder was removed afterwards. The prepared environment `~/.vault-sandbox` is missing on this machine. Both scripts and the three one-line commands of [[Running The Quarter Turn And The Fraction]] printed the same text as the earlier run in `~/playground/sandbox/schedule-figures`, and each SVG was rasterised with PyMuPDF 1.27.2 and opened; `s4-the-fraction.svg` was redrawn that day with orange rings for $\beta_t$, the colour the cosine schedule notes give it.
>
> The table's δ = 0 column is `C(k, 0)` from `cosine.py`; the consequence table's 0.000158 and 0.69157 were run in the same folder, as $\cos^2 90.72^\circ / \cos^2 0.72^\circ$ and $\cos 46.25^\circ / \cos 0.714^\circ$. The with-and-without numbers in the chunks were computed the same day by a throwaway script on the same `cosine.py`: the slopes −0.02493, −0.99905 and, without the 2, −0.49952; the step from post 50, 0.015583 rad, predicting 0.015568 against 0.0155765 measured; a whole turn, post 25 at 92.14° with $C_{25} = 0.0014$, post 51 at 185° with $C_{51} = 0.9949$ and $C_{100} = 1.0025$; the drops per 15° with and without the square; and, through the removals script of [[Which Pieces Of C_k Change The Noise]], $\beta_{50} = 0.032198$ and $\beta_{99} = -15.0$ without the division by $1 + \delta$. The $\beta_{99}$ clip to 0 is line 19 of `rebuild/model.py`.
>
> The quotation is from Nichol and Dhariwal's page 4, as read for [[The Cosine Noise Schedule]]. The calculus textbook's PDF pages 193 and 198 were opened and read as text, and the trigonometry handbook's page 7 (one rotation is 360° or 2π) and the pre-algebra handbook's page 25 (dividing fractions) were opened with PyMuPDF and read. The scene frame anchors are as the walk's `dispatch.md` and the retrofit brief record them. No tldr-pages entry covers this.
