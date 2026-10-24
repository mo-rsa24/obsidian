---
aliases: [how the cosine wave works, deriving the Pythagorean identity, the slope of cos squared derived, the drops of cos squared, "drop ≈ slope × 0.2618", chain rule on cos squared]
sources:
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Trigonometry, version 2.4: the Pythagorean identities, PDF p. 9; period 2π, PDF p. 17; double angle formulas, sin 2θ = 2 sin θ cos θ, PDF p. 37: ../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=9"
  - "Anton, Bivens, Davis, Calculus, section 2.5 (derivatives of sine and cosine, x in radians), PDF p. 193, and section 2.6 (the chain rule), PDF p. 198: ../references/textbooks/calculus/calculus-textbook.pdf#page=193"
standard: vault-note v2
---

# How The Cosine Wave Works

Up: [[Trigonometry]] · ⬅️ [[The Cosine Wave]] · [[Running The Cosine Wave]] ➡️

Mathematics, Trigonometry. Needs: [[The Cosine Wave#The two shares|the two shares]] and [[The Cosine Wave#The quarter turn: where the square is flat|the slope of the square]], which this note derives.

**Pythagoras gives the two shares, and the chain rule gives the slope that keeps the square flat at both ends.**

> [!question]- Test yourself
> No quiz page covers this note yet.

> [!warning]- Unfinished
> - No quiz page for this note yet.

Stated claims: 0.

**The four steps.** The identity comes from Pythagoras divided by $r^2$, and the wave repeats because one full turn brings the point back. The slope of $\cos^2\theta$ is derived one move per line, and the drops in [[The Cosine Wave#The quarter turn and its table|the table]] follow from that slope.

**Where the numbers come from.** Every worked number is at 46.25° or on the 15° steps of the table in [[The Cosine Wave]], and every printed number is an output of [[Running The Cosine Wave]].

**Colours, as in The Cosine Wave.** <span style="color:#2e7d32">**Green is $\cos\theta$ and its square**</span>, <span style="color:#ef6c00">**orange is $\sin\theta$ and its square**</span>, <span style="color:#1565c0">**blue is the angle's 15° steps and the drop each makes**</span>, and <span style="color:#6d4c41">**brown is an angle in radians, such as the 15° step 0.2618**</span>.

## Table of contents

- [[#The identity]]
- [[#The wave]]
- [[#The slope]]
- [[#The drops]]

## The identity

Navigation: 📋 [[#Table of contents|TOC]] | [[#The wave]] ➡️

Textbook: [Whitney, Trigonometry handbook, the Pythagorean identities, PDF p. 9](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=9)

**The identity.** A point $(x, y)$ at distance $r$ satisfies [Pythagoras](../references/textbooks/geometry/geometry-handbook.pdf#page=80). Divide by $r^2$ and use $x / r = \cos\theta$, $y / r = \sin\theta$:

$$
\begin{aligned}
x^2 + y^2 &= r^2 && \text{Pythagoras on the triangle}\\
\frac{x^2}{r^2} + \frac{y^2}{r^2} &= 1 && \text{divide both sides by } r^2\\
\textcolor{#2e7d32}{\cos^2\theta} + \textcolor{#ef6c00}{\sin^2\theta} &= 1 && x/r = \cos\theta,\ y/r = \sin\theta
\end{aligned}
$$

$$
\textcolor{#2e7d32}{0.6915^2} + \textcolor{#ef6c00}{0.7224^2} = \textcolor{#2e7d32}{0.47819} + \textcolor{#ef6c00}{0.52181} = 1
$$

**What the derivation says.** The radius drops out, so the two squared legs fill exactly 1 on a circle of any size. At 46.25° the shares are 0.47819 and 0.52181.

## The wave

Navigation: ⬅️ [[#The identity]] | 📋 [[#Table of contents|TOC]] | [[#The slope]] ➡️

Textbook: [Whitney, Trigonometry handbook, period 2π for cosine, PDF p. 17](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=17)

**The wave.** As θ grows past π/2 the point moves into the left half of the circle, so $\cos\theta$ goes negative. Past $2\pi$ it is back where it started, so the curve repeats.

## The slope

Navigation: ⬅️ [[#The wave]] | 📋 [[#Table of contents|TOC]] | [[#The drops]] ➡️

Textbook: [Anton, Bivens, Davis, Calculus, section 2.6, the chain rule, PDF p. 198](../references/textbooks/calculus/calculus-textbook.pdf#page=198)

**The slope.** The [derivative of the cosine](../references/textbooks/calculus/calculus-textbook.pdf#page=193) is $-\sin\theta$ when θ is in radians, and the [chain rule](../references/textbooks/calculus/calculus-textbook.pdf#page=198) handles the square. The last line is the [double-angle rule](../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=37):

$$
\begin{aligned}
\frac{d}{d\theta}\,\textcolor{#2e7d32}{\cos^2\theta}
&= 2\textcolor{#2e7d32}{\cos\theta} \cdot \frac{d}{d\theta}\textcolor{#2e7d32}{\cos\theta} && \text{chain rule on } u^2,\ u = \cos\theta\\
&= 2\textcolor{#2e7d32}{\cos\theta} \cdot (-\textcolor{#ef6c00}{\sin\theta}) && \text{slope of the cosine, θ in radians}\\
&= -2\textcolor{#2e7d32}{\cos\theta}\,\textcolor{#ef6c00}{\sin\theta} && \text{collect the signs}\\
&= -\sin 2\theta && \sin 2\theta = 2\sin\theta\cos\theta
\end{aligned}
$$

$$
\theta = 0:\ -\sin 0 = 0,
\qquad
\theta = \tfrac{\pi}{4}:\ -\sin\tfrac{\pi}{2} = -1,
\qquad
\theta = \tfrac{\pi}{2}:\ -\sin \pi = 0
$$

**What the slope gives.** 0 at both ends of the quarter turn and −1 at π/4, as [[Running The Cosine Wave#Try the cosine wave yourself|step 6 of the run]] printed. [[The Cosine Wave#The quarter turn: where the square is flat|The quarter turn section]] works each piece with and without: the 2, the minus sign and the doubled angle.

## The drops

Navigation: ⬅️ [[#The slope]] | 📋 [[#Table of contents|TOC]]

**The drops.** Over one 15° step the square falls by about the slope at the step's middle times the step's length in radians:

$$
\begin{aligned}
\textcolor{#1565c0}{\text{drop over one 15° step}} &\approx \lvert\text{slope at the step's middle}\rvert \times \textcolor{#6d4c41}{\Delta\theta}\\
\textcolor{#6d4c41}{\Delta\theta} &= 15 \times \frac{\pi}{180} = \textcolor{#6d4c41}{0.2618}\ \text{rad}
\end{aligned}
$$

$$
\begin{aligned}
0° \to 15°,\ \text{middle } 7.5°:&\quad \sin 15° \times \textcolor{#6d4c41}{0.2618} = 0.2588 \times 0.2618 = \textcolor{#1565c0}{0.0678} && \text{measured } 0.067\\
30° \to 45°,\ \text{middle } 37.5°:&\quad \sin 75° \times \textcolor{#6d4c41}{0.2618} = 0.9659 \times 0.2618 = \textcolor{#1565c0}{0.2529} && \text{measured } 0.25
\end{aligned}
$$

**What the drops give.** The slopes near 0 at the ends give the 0.067 drops, and the slopes near −1 in the middle give the 0.25 drops. Each estimate is within 0.003 of the drop [[Running The Cosine Wave#Try the cosine wave yourself|step 4 of the run]] measured.

**Without the slope's 2.** The middle step's estimate would be $0.4830 \times 0.2618 = 0.1264$, half the 0.25 the table measured. The first step's would be 0.0339 against 0.067.

> [!note]- How this was checked
> The drop estimates (0.0678 and 0.2529 with the slope's 2, 0.0339 and 0.1264 without it) and the slopes at 0, π/4 and π/2 were printed on 2026-10-21 on mscluster (Linux) by a throwaway script run with Python 3.12.10 from the machine's `python3`, by vault-writer, in the empty folder `~/playground/sandbox/cosine-wave-v2`, which was removed afterwards. The shares 0.47819 and 0.52181 match the outputs in [[Running The Cosine Wave]].
>
> The textbook pages were opened and read as text with PyMuPDF: the trigonometry handbook's PDF pages 9 (the Pythagorean identities), 17 (period 2π for cosine) and 37 (double angle formulas); the geometry handbook's page 80; the calculus textbook's pages 193 (section 2.5, x in radians) and 198 (section 2.6, the chain rule). This note has no figure of its own: [[The Cosine Wave#The quarter turn: where the square is flat|the quarter-turn figure]] draws the slope's values.
