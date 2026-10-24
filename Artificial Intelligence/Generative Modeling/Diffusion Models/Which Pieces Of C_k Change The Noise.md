---
aliases: [which pieces of C_k change the noise, which pieces of the cosine schedule change beta, the denominator cancels in beta, why the ratio cancels the denominator, removing each piece of C_k drawn, the square removed and the division by 1 + delta removed]
sources:
  - "Nichol, Dhariwal, Improved Denoising Diffusion Probabilistic Models, ICML 2021, section 3.2 and equation (17), PDF p. 4: https://arxiv.org/pdf/2102.09672#page=4"
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Pre-Algebra, multiplying and dividing fractions, reducing a factor shared by numerator and denominator, PDF p. 25: ../../../Mathematics/references/textbooks/general/pre-algebra-handbook.pdf#page=25"
standard: vault-note v2
---

# Which Pieces Of C_k Change The Noise

Up: [[Diffusion Models]] · ⬅️ [[The Quarter Turn And The Fraction]] · [[Running The Quarter Turn And The Fraction]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[The Quarter Turn And The Fraction]] for the fraction $C_k = \cos^2\theta_k / \cos^2\theta_0$ and its four pieces, and [[The Cosine Noise Schedule]] for $\beta_t = 1 - C_{t+1}/C_t$.

**The denominator cancels out of every step's noise, while the square and the division by $1 + \delta$ each change it.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. It has no questions on this note yet.

> [!warning]- Unfinished
> - The diffusion models quiz has no questions on this note yet.

Stated claims: 0.

**What this note does.** It works the cancellation of [[The Quarter Turn And The Fraction#Step 4: the fraction|step 4's denominator]] for every step $t$, then draws the two removals that the [[The Quarter Turn And The Fraction#The consequence: remove a piece|consequence table]] counts but its figures do not show.

**Where the scripts run.** The figure script imports `plane.py` and `cosine.py` and needs matplotlib, so run it in the folder that [[Running The Quarter Circle Under The Cosine Schedule#Try the quarter circle yourself|step 3 of the quarter circle's sandbox]] makes. [[Running The Quarter Turn And The Fraction]] runs it and reads its output.

**Colours in this note.** <span style="color:#2e7d32">**Green is the squared cosine $f(k) = \cos^2\theta_k$ and the boundary value $C_k$, the share kept**</span>, <span style="color:#ef6c00">**orange is a step's noise share $\beta_t$**</span>, <span style="color:#6a1b9a">**purple is the denominator $f(0) = \cos^2\theta_0$**</span>, and <span style="color:#9e9e9e">**grey is a case with a piece removed**</span>, as in [[The Cosine Noise Schedule]].

## Table of contents

- [[#How the denominator cancels]]
- [[#Removing each piece, drawn]]

## How the denominator cancels

Navigation: 📋 [[#Table of contents|TOC]] | [[#Removing each piece, drawn]] ➡️

Textbook: [Whitney, Pre-Algebra handbook, multiplying and dividing fractions, PDF p. 25](../../../Mathematics/references/textbooks/general/pre-algebra-handbook.pdf#page=25)

Write $f(k) = \cos^2\theta_k$, so $C_k = f(k)/f(0)$:

$$
\beta_t = 1 - \frac{C_{t+1}}{C_t} = 1 - \frac{f(t+1)/f(0)}{f(t)/f(0)} = 1 - \frac{f(t+1)}{f(t)}
$$

$$
\underbrace{\textcolor{#ef6c00}{\beta_t}}_{\text{step }t\text{'s noise share}}
=
1 - \frac{\textcolor{#2e7d32}{C_{t+1}}}{\textcolor{#2e7d32}{C_t}}
=
1 - \frac{\textcolor{#2e7d32}{f(t+1)}\,/\,\overbrace{\textcolor{#6a1b9a}{f(0)}}^{\text{the same }0.99984}}{\textcolor{#2e7d32}{f(t)}\,/\,\underbrace{\textcolor{#6a1b9a}{f(0)}}_{\text{the same }0.99984}}
=
1 - \underbrace{\frac{\textcolor{#2e7d32}{f(t+1)}}{\textcolor{#2e7d32}{f(t)}}}_{\text{numerators only}}
$$

**What the equation says.** $f(0)$ appears once on top and once underneath, and [dividing one fraction by another](../../../Mathematics/references/textbooks/general/pre-algebra-handbook.pdf#page=25) reduces a factor the two share, so it leaves every $\beta_t$ unchanged. Its one effect is $C_0 = f(0)/f(0) = 1$, and through $\bar\alpha_t = C_{t+1}$ the kept shares start from exactly 1. The scene [strikes the two 0.99984s out of β₅₀](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-normaliser-cancels) one step at a time.

**Why the ratio is there.** A ratio of two boundary values cancels the shared $f(0)$, and a difference would keep it. At step 50, $C_{50} - C_{51} = 0.0155790$ against $f(50) - f(51) = 0.0155765$, apart by the factor 1.00016, while $1 - C_{51}/C_{50}$ and $1 - f(51)/f(50)$ both give 0.031546.

**Why the 1 − is there.** The ratio $C_{51}/C_{50} = 0.96845$ is the share step 50 keeps, and the noise share is what is left of 1. Without the 1 − the step's noise would read 0.96845.

<table>
<tr><th>step t</th><th style="color:#2e7d32">C<sub>t</sub></th><th style="color:#2e7d32">C<sub>t+1</sub></th><th style="color:#2e7d32">f(t)</th><th style="color:#2e7d32">f(t+1)</th><th style="color:#ef6c00">β<sub>t</sub> from C</th><th style="color:#ef6c00">β<sub>t</sub> from f</th></tr>
<tr><td>0</td><td>1</td><td>0.9993687</td><td>0.9998446</td><td>0.9992134</td><td>0.000631</td><td>0.000631</td></tr>
<tr style="background:#fff8e1"><td><b>50</b></td><td>0.4938436</td><td>0.4782646</td><td>0.4937668</td><td>0.4781903</td><td style="border:2px solid #212121"><b>0.031546</b></td><td style="border:2px solid #212121"><b>0.031546</b></td></tr>
<tr><td>98</td><td>0.0009712</td><td>0.0002429</td><td>0.0009710</td><td>0.0002428</td><td>0.749939</td><td>0.749939</td></tr>
</table>

**How to read this table.** Each row is one step: the two boundary values it sits between, the same two without the denominator, and β worked from each pair. Every C is its f times 1.00016.

**What to look for.** The two β columns agree in every row, early, middle and late. The highlighted step 50 is the one [[The Quarter Turn And The Fraction#All the words together: the fraction|the fraction's β₅₀ display]] works.

## Removing each piece, drawn

Navigation: ⬅️ [[#How the denominator cancels]] | 📋 [[#Table of contents|TOC]]

**What this draws.** Two rows of [[The Quarter Turn And The Fraction#The consequence: remove a piece|the consequence table]]: the square removed, and the division by $1 + \delta$ removed. The offset's removal is the inset of [[The Quarter Turn And The Fraction#The consequence: slow at both ends, fastest in the middle|step 3's figure]], and the denominator's is [[The Quarter Turn And The Fraction#All the words together: the fraction|step 4's right panel]].

**The square removed.** The curve becomes $\cos\theta_k / \cos\theta_0$, the clean point's multiplier, which ends at slope −1 instead of flat. Its last step drops 0.015584 instead of 0.000243, and [[The Cosine Wave#The quarter turn: where the square is flat|the cosine wave's dashed tangent]] draws the same slope on one wave.

**The division by 1 + δ removed.** Post 100 sits at 90.72°, past the quarter turn, and keeps $C_{100} = 0.000158$, as the rebuild walk works when it [drops the rescale](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step4-dropping-the-rescale). Every step's noise moves a little, $\beta_{50}$ from 0.031546 to 0.032198, and $\beta_{99} = 1 - 0.000158/0.0000099 = -15.0$, which the rebuild's `np.clip(betas, 0, 0.999)` turns into 0. The frame on [where each post's position comes from](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-position-derived) has a switch for this division.

```python
import math
import matplotlib.pyplot as plt
from plane import save, GREEN, GREY
from cosine import T, theta_deg, C


def C_no_square(k):
    return math.cos(math.radians(theta_deg(k))) / math.cos(math.radians(theta_deg(0)))


def C_no_division(k):
    def f(j):
        return math.cos(math.radians((j / T + 0.008) * 90)) ** 2
    return f(k) / f(0)


def beta(Cf, t):
    return 1 - Cf(t + 1) / Cf(t)


print(f"no square:   C_51 {C_no_square(51):.5f} (with it {C(51):.5f})   last step drops {C_no_square(99):.6f} (with it {C(99):.6f})")
print(f"no division: C_100 {C_no_division(100):.6f}   beta_50 {beta(C_no_division, 50):.6f} (with it {beta(C, 50):.6f})   beta_99 {beta(C_no_division, 99):.1f} (with it {beta(C, 99):.1f})")

fig, (left, right) = plt.subplots(1, 2, figsize=(13, 4.8))
ks = range(T + 1)
left.plot(ks, [C_no_square(k) for k in ks], "o", color=GREY, ms=4)
left.plot(ks, [C(k) for k in ks], "o", color=GREEN, ms=4)
left.annotate("cos θ₅₁ / cos θ₀ = 0.69157", (51, C_no_square(51)), xytext=(58, 0.95), color=GREY, fontsize=10,
              arrowprops={"arrowstyle": "-", "color": GREY, "lw": 0.8})
left.annotate("cos² θ₅₁ / cos² θ₀ = 0.47826", (51, C(51)), xytext=(4, 0.32), color=GREEN, fontsize=10,
              arrowprops={"arrowstyle": "-", "color": GREEN, "lw": 0.8})
left.text(70, 0.66, "without the square:\nsteep end, the last step\ndrops 0.015584", color=GREY, fontsize=10)
left.text(4, 0.06, "with it: flat end,\nthe last step drops 0.000243", color=GREEN, fontsize=10)
left.set_xlabel("post k")
left.set_ylabel("Cₖ, share of the clean signal's variance kept")
left.set_xlim(-2, 102)
left.set_ylim(-0.05, 1.08)
left.spines[["top", "right"]].set_visible(False)
left.grid(color="#eeeeee")
left.set_title("remove the square: the end is no longer flat", fontsize=12)

end = range(95, T + 1)
right.plot(end, [C_no_division(k) for k in end], "s-", color=GREY, ms=6)
right.plot(end, [C(k) for k in end], "o-", color=GREEN, ms=6)
right.annotate("post 100 at 90.72°: C₁₀₀ = 0.000158", (100, C_no_division(100)), xytext=(97.1, 0.0050), color=GREY,
               fontsize=10, arrowprops={"arrowstyle": "-", "color": GREY, "lw": 0.8})
right.text(100, 0.0028, "post 100 at 90°:\nC₁₀₀ = 0", color=GREEN, fontsize=10, ha="right")
right.text(95.1, -0.0013, "β₉₉ = −15.0 without, clipped to 0;  1, clipped to 0.999, with\n"
                          "β₅₀ = 0.032198 without, 0.031546 with", fontsize=9)
right.set_xticks(list(end))
right.set_xlabel("post k")
right.set_ylabel("Cₖ")
right.set_ylim(-0.0016, 0.0065)
right.spines[["top", "right"]].set_visible(False)
right.grid(color="#eeeeee")
right.set_title("remove the ÷ (1 + δ): post 100 overshoots", fontsize=12)
fig.tight_layout()
save(fig, "quarter-turn-remove-a-piece.svg")
```

![Left, C_k against post k with the square in green, falling flat into post 100, and without it in grey, cos theta k over cos theta 0, reaching 0.69157 at post 51 and falling steeply into post 100; right, posts 95 to 100 with the division by 1 + delta in green ending at C_100 = 0 and without it in grey turning up to 0.000158 at post 100, with beta 99 = -15.0 clipped to 0 and beta 50 = 0.032198 against 0.031546 written beneath|900](assets/quarter-turn-remove-a-piece.svg)

**How to read this.** Both panels put the post $k$ on the x-axis and $C_k$ on the y-axis: green is the schedule, grey is the schedule with one piece removed. On the right the y-axis runs only to 0.0065 and shows posts 95 to 100. Look at the last step in each panel: grey falls 0.015584 into post 100 on the left, and turns up to 0.000158 on the right.

> [!note]- How this was checked
> The figure script was run on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and matplotlib 3.10.8 from the machine's `python3`, in the empty folder `~/playground/sandbox/quarter-turn-fraction`, with `plane.py` copied from the Trigonometry sandbox and `cosine.py` as [[Running The Quarter Circle Under The Cosine Schedule]] gives it; the folder was removed afterwards. Its SVG was rasterised with PyMuPDF 1.27.2 and opened before filing. The prepared environment `~/.vault-sandbox` is missing on this machine.
>
> The three-step table and the differences 0.0155790 and 0.0155765 were computed the same day by a throwaway script on the same `cosine.py`; $\beta_{50}$ = 0.031546 both ways is also step 8 of [[Running The Quarter Turn And The Fraction]]. The $\beta_{99}$ clip to 0 is line 19 of the rebuild's [`cosine_beta_schedule`](../../../../PhD/reduce-reuse-recycle/rebuild/model.py). The pre-algebra handbook's page 25 was opened with PyMuPDF and read: it reduces a factor shared by numerator and denominator when dividing fractions. The scene frame anchors are as the walk's `dispatch.md` and the retrofit brief record them.
