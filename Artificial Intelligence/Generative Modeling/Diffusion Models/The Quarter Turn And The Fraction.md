---
aliases: [the quarter turn of the cosine schedule, quarter turn and the fraction, C_k against k, the C_k curve, numerator and denominator of C_k, the C_k fraction, "C_k = cos^2(theta_k) / cos^2(theta_0)", why C_k divides by cos^2 theta_0, the denominator cancels in beta, first step noise without the offset, what each piece of C_k does]
sources:
  - "Nichol, Dhariwal, Improved Denoising Diffusion Probabilistic Models, ICML 2021, section 3.2 and equation (17), PDF p. 4: https://arxiv.org/pdf/2102.09672#page=4"
  - "Anton, Bivens, Davis, Calculus, section 2.5 (derivatives of sine and cosine), PDF p. 193, and section 2.6 (the chain rule), PDF p. 198: ../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf"
---

# The Quarter Turn And The Fraction

Up: [[Diffusion Models]] · ⬅️ [[The Quarter Circle Under The Cosine Schedule]] · [[Composition]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[The Quarter Circle Under The Cosine Schedule]] for where the posts sit, and [[The Cosine Wave]] for why $\cos^2$ is flat at 0° and 90°.

> [!question] Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. It has no questions on this note yet.

> [!warning] Unfinished
> - No drawn form, mechanism or deep-dive sheet is prompted for this note; prompt 44 in the vault's `.prompts/Diffusion Models.md` draws the fraction's two bars among its parts.
> - The diffusion models quiz has no questions on this note yet.

Stated claims: 0.

**Square the cosine at every post and divide by its value at post 0, and you have the 101 boundary values $C_k$.** This note draws the last two steps of the quarter-circle build: the squared cosine walked across all 101 posts, and the fraction that makes $C_0 = 1$. Then it removes each piece of the formula in turn and counts what changes.

**Colours, the same in every equation and figure.** Green is the squared cosine, $\cos^2\theta_k$ and $C_k$. Purple is the denominator $\cos^2\theta_0$. Grey is a case with a piece removed.

## Where you work

The folder [[The Quarter Circle Under The Cosine Schedule#Try the quarter circle yourself]] makes, with its `plane.py` and `cosine.py`.

## Table of contents

- [[#The squared cosine and its fraction]]
- [[#Try the fraction yourself]]
- [[#Reading the fraction output]]
- [[#How the denominator cancels]]
- [[#Other ways to see the fraction]]
- [[#Why the fraction matters]]
- [[#The fraction taught in, applied in]]

## The squared cosine and its fraction

Navigation: 📋 [[#Table of contents|TOC]] | [[#Try the fraction yourself]] ➡️

Textbook: [Anton, Calculus, the chain rule, PDF p. 198](../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=198)

### The fraction at four posts

<table>
<tr><th>post k</th><th>angle θ<sub>k</sub></th><th style="color:#2e7d32">cos² θ<sub>k</sub></th><th style="color:#6a1b9a">cos² θ<sub>0</sub></th><th style="color:#2e7d32">C<sub>k</sub></th><th>C<sub>k</sub> with δ = 0</th></tr>
<tr><td>0</td><td>0.714°</td><td>0.99984</td><td style="border:2px solid #212121">0.99984</td><td style="border:2px solid #212121">1</td><td>1</td></tr>
<tr><td>1</td><td>1.607°</td><td>0.99921</td><td>0.99984</td><td style="border:2px solid #212121">0.99937</td><td style="border:2px dashed #212121">0.99975</td></tr>
<tr style="background:#fff8e1"><td><b>51</b></td><td>46.25°</td><td style="border:2px solid #212121"><b>0.47819</b></td><td>0.99984</td><td style="border:2px solid #212121"><b>0.47826</b></td><td>0.48430</td></tr>
<tr><td>100</td><td>90°</td><td>0</td><td>0.99984</td><td>0</td><td>0</td></tr>
</table>

**How to read this table.** Each row is one post. The green column divided by the purple column gives $C_k$, the share of the clean signal's variance kept at that post. The last column is the same calculation with the offset δ set to 0.

**What to look for.** The purple column never changes: one number divides every post. Post 1 is the first step, 0.99937 against 0.99975 without the offset. Post 51 is $\bar\alpha_{50} = 0.4783$.

### Step 3: the quarter turn, squared

Walk the post from 0 to 100 and the angle sweeps the quarter turn; [[The Cosine Wave#The quarter turn: where the square is flat|the square of its cosine]] falls from 1 to 0:

$$
\underbrace{\textcolor{#2e7d32}{C_k}}_{\text{share kept at post }k}
\;\propto\;
\underbrace{\textcolor{#2e7d32}{\cos^2\theta_k}}_{\text{squared horizontal leg}},
\qquad
\underbrace{\frac{d}{d\theta}\cos^2\theta = -2\cos\theta\sin\theta}_{0\text{ at }0^\circ\text{ and }90^\circ,\ -1\text{ at }45^\circ}
$$

**What the equation says.** The share kept follows the squared cosine, so it falls slowly near post 0, fastest near post 50 and slowly again near post 100. The slope, from the [derivative of the cosine](../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=193) and [the chain rule](../../../Mathematics/references/textbooks/calculus/calculus-textbook.pdf#page=198), is the product of the two legs.

**Why the offset matters here.** With δ = 0 post 0 sits at 0°, where the slope is exactly 0, so the first step loses only $1 - 0.99975 = 0.000247$ of the variance. With δ = 0.008 post 0 sits at 0.714°, the slope there is already −0.0249 per radian, and the first step loses 0.000631. Nichol and Dhariwal add the offset because "having tiny amounts of noise at the beginning of the process made it hard for the network to predict ϵ accurately enough" (*cited*, [p. 4](https://arxiv.org/pdf/2102.09672#page=4)).

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

### Step 4: the fraction

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

**What the equation says.** $C_k$ asks how many denominators fit in the numerator. At post 0 the two are the same number, so $C_0 = 1$ exactly: before the first step all of the clean signal is kept.

**Why the denominator is there.** The offset puts post 0 at 0.714°, where $\cos^2 = 0.99984$, not 1. Dividing by that one number stretches the whole curve by 1.00016 so it starts on 1.

**Why it changes no step's noise.** Each step's noise is $\beta_t = 1 - C_{t+1}/C_t$, a ratio of two boundary values, and the denominator sits on top and underneath:

$$
\beta_{50}
=
1-\frac{\cos^2\theta_{51}\,/\,\textcolor{#6a1b9a}{\cos^2\theta_0}}{\cos^2\theta_{50}\,/\,\textcolor{#6a1b9a}{\cos^2\theta_0}}
=
1-\underbrace{\frac{0.47819}{0.49377}}_{\text{numerators only}}
=
0.03155
$$

```python
import matplotlib.pyplot as plt
from plane import save, GREEN, PURPLE, GREY
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
right.plot(ts, beta_C, "o", color=GREEN, ms=7, mfc="none")
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

![Left, three bars at each of posts 0, 1, 51 and 100: the numerator cos squared theta k in green, the constant denominator 0.99984 in purple and their ratio C_k in dark green; right, beta t against step t on a log scale, rings computed with the denominator and dots without it, lying on top of each other from 0.000631 at step 0 to the clip 0.999 at step 99|900](assets/s4-the-fraction.svg)

**How to read this.** On the left the y-axis is a share from 0 to 1 and each group of three bars is one post: numerator, denominator, ratio. On the right the x-axis is the step $t$ and the y-axis is $\beta_t$ on a log scale, so the small early steps are visible; this axis is not linear. Look at the right panel: every grey dot sits inside its green ring.

### The consequence: remove a piece

<table>
<tr><th>piece removed</th><th>what changes, on the toy's numbers</th><th>where it shows</th></tr>
<tr><td>the offset δ</td><td>post 0 at 0°; the first step's noise share falls from 0.000631 to 0.000247, its typical size from 0.0251 to 0.0157</td><td>step 1's grey posts; step 3's inset</td></tr>
<tr><td>the division by 1 + δ</td><td>post 100 at 90.72°; C<sub>100</sub> = 0.000158 instead of 0, so the last step leaves some signal</td><td>one-line run, not drawn</td></tr>
<tr><td>the denominator cos² θ<sub>0</sub></td><td>C<sub>0</sub> = 0.99984 instead of 1; every C<sub>k</sub> is 0.016% low; every β<sub>t</sub> unchanged</td><td>step 4, both panels</td></tr>
<tr><td>the square</td><td>C<sub>51</sub> would be the multiplier 0.69157, not the share 0.47826, and the curve would end at slope −1 instead of flat</td><td>the dashed tangent in <a href="../../../Mathematics/Trigonometry/assets/t7-cosine-wave-quarter-turn.svg">the cosine wave</a></td></tr>
</table>

**How to read this table.** Each row switches off one piece of $C_k = \cos^2\theta_k / \cos^2\theta_0$ with the others kept, and gives the number that moves.

## Try the fraction yourself

Navigation: ⬅️ [[#The squared cosine and its fraction]] | 📋 [[#Table of contents|TOC]] | [[#Reading the fraction output]] ➡️

**1. What you need** and **2. when it is missing**: [[The Quarter Circle Under The Cosine Schedule#Try the quarter circle yourself]], steps 1 and 2.

**3. The setup.** Work in the folder that note's step 3 makes, with `plane.py` and `cosine.py`. Save the two scripts above as `s3_curve.py` and `s4_fraction.py`.

**4. A look before: the curve and its first step.**

```bash
python3 s3_curve.py
```

```text
C_0 = 1.00000
C_1 = 0.99937
C_51 = 0.47826
C_100 = 0.00000
first step's noise share: 1 - C_1 = 0.000631 with delta = 0.008, 0.000247 with delta = 0
saved s3-quarter-turn-cos-squared.svg
```

**5. The failure: no denominator.**

```bash
python3 -c "from cosine import f, C; print(round(f(0), 5), round(C(0), 5))"
```

```text
0.99984 1.0
```

Without the division, post 0 keeps 0.99984 of the signal before any step has run.

**6. The technique: the fraction, and β with and without it.**

```bash
python3 s4_fraction.py
```

```text
post   0: 0.99984 / 0.99984 = 1.00000
post   1: 0.99921 / 0.99984 = 0.99937
post  51: 0.47819 / 0.99984 = 0.47826
post 100: 0.00000 / 0.99984 = 0.00000
beta_0 0.000631 / 0.000631   beta_50 0.03155 / 0.03155   largest gap 1.1e-16
saved s4-the-fraction.svg
```

**7. Another way: β₅₀ from the numerators alone.**

```bash
python3 -c "from cosine import f; print(round(f(50), 5), round(f(51), 5), round(1 - f(51) / f(50), 5))"
```

```text
0.49377 0.47819 0.03155
```

**8. More worked examples: three steps, both ways.**

```bash
python3 -c "from cosine import f, C; print([(t, round(1 - C(t + 1) / C(t), 6), round(1 - f(t + 1) / f(t), 6)) for t in (0, 50, 98)])"
```

```text
[(0, 0.000631, 0.000631), (50, 0.031546, 0.031546), (98, 0.749939, 0.749939)]
```

**9. Clean up, and prove it**: [[The Quarter Circle Under The Cosine Schedule#Try the quarter circle yourself]], step 9.

## Reading the fraction output

Navigation: ⬅️ [[#Try the fraction yourself]] | 📋 [[#Table of contents|TOC]] | [[#How the denominator cancels]] ➡️

| Step | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 4 | `C_1` | `0.99937` | the share kept after code step 0, $\bar\alpha_0$ | shown |
| 4 | first noise share | `0.000631`, `0.000247` | with and without the offset | shown |
| 5 | `f(0)` | `0.99984` | $\cos^2 0.714^\circ$, the denominator | shown |
| 6 | `post 51` | `0.47819 / 0.99984 = 0.47826` | numerator over denominator, $\bar\alpha_{50}$ | derived above |
| 6 | `largest gap` | `1.1e-16` | β with and without the denominator differ only by rounding in the last binary digit | derived below |
| 7 | `0.03155` | $\beta_{50}$ | the same as step 6, from the numerators alone | derived below |
| 8 | `t = 98` | `0.749939` both ways | the denominator cancels late in the schedule too | derived below |

## How the denominator cancels

Navigation: ⬅️ [[#Reading the fraction output]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to see the fraction]] ➡️

Write $f(k) = \cos^2\theta_k$, so $C_k = f(k)/f(0)$:

$$
\beta_t = 1 - \frac{C_{t+1}}{C_t} = 1 - \frac{f(t+1)/f(0)}{f(t)/f(0)} = 1 - \frac{f(t+1)}{f(t)}
$$

$f(0)$ appears once on top and once underneath, so it leaves every $\beta_t$ unchanged. Its one effect is $C_0 = f(0)/f(0) = 1$, and through $\bar\alpha_t = C_{t+1}$ the kept shares start from exactly 1.

## Other ways to see the fraction

Navigation: ⬅️ [[#How the denominator cancels]] | 📋 [[#Table of contents|TOC]] | [[#Why the fraction matters]] ➡️

- **Drag it.** The scene Dissolving the Dog, [frame "one boundary"](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-one-boundary), draws the numerator, denominator and ratio bars with a switch that drops the denominator, and [frame "the quarter turn"](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-quarter-turn) walks the angle.
- **Only the numbers.** [[The Cosine Noise Schedule#Try the boundary values yourself]] computes the same four boundaries by hand.

## Why the fraction matters

Navigation: ⬅️ [[#Other ways to see the fraction]] | 📋 [[#Table of contents|TOC]] | [[#The fraction taught in, applied in]] ➡️

Every number the forward process uses comes from these 101 values: $\bar\alpha_t = C_{t+1}$ and $\beta_t$ from neighbouring posts. Knowing which piece does what tells you which ones touch the noise: the offset and the square change it, the denominator only relabels the start.

## The fraction taught in, applied in

Navigation: ⬅️ [[#Why the fraction matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the `drip --math` walk of the forward process and the score in the reduce-reuse-recycle research repository (`artifacts/drips/forward-process-and-the-score/`), piece 2, rung 1: the quarter turn, the fraction's numerator and denominator, why the offset, and the learner's request to see each step drawn by the code that computes it
- step 4 of the one-expert rebuild walk in the same repository (`artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md`), "On paper 5: play with the quarter turn" and "On paper 6, the fraction"

**Applied in:** wherever [[The Cosine Noise Schedule]] is applied: the rebuild's `cosine_beta_schedule` (`rebuild/model.py`, lines 13 to 19).

> [!note]- How this was checked
> The two scripts and the three one-line commands were run on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and matplotlib 3.10.8 from the machine's `python3`, in the empty folder `~/playground/sandbox/schedule-figures`, by vault-writer, which was removed afterwards (clean-up check returned 2). The prepared environment `~/.vault-sandbox` is missing on this machine. Every output above is that run's text. Each SVG was rasterised with PyMuPDF and opened, and a matplotlib PNG twin was opened beside it.
>
> The table's δ = 0 column is `C(k, 0)` from `cosine.py`; the consequence table's 0.000158 and 0.69157 were run in the same folder, as $\cos^2 90.72^\circ / \cos^2 0.72^\circ$ and $\cos 46.25^\circ / \cos 0.714^\circ$. The quotation is from Nichol and Dhariwal's page 4, as read for [[The Cosine Noise Schedule]]. The calculus textbook's PDF pages 193 and 198 were opened and read as text. The scene frame anchors are as the walk's `dispatch.md` records them. No tldr-pages entry covers this.
