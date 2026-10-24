---
aliases: [running the quarter turn and the fraction, the fraction in an empty folder, s3_curve.py, s4_fraction.py, remove_a_piece.py, reading the fraction output]
sources:
  - "Nichol, Dhariwal, Improved Denoising Diffusion Probabilistic Models, ICML 2021, section 3.2 and equation (17), the formula these runs compute, PDF p. 4: https://arxiv.org/pdf/2102.09672#page=4"
standard: vault-note v2
---

# Running The Quarter Turn And The Fraction

Up: [[Diffusion Models]] · ⬅️ [[Which Pieces Of C_k Change The Noise]] · [[Composition]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[The Quarter Turn And The Fraction]] and [[Which Pieces Of C_k Change The Noise]], whose figure scripts these runs make and run.

**The fraction's scripts, run in the quarter circle's folder from the curve's first step to β with and without each piece.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. It has no questions on this note yet.

> [!warning]- Unfinished
> - The diffusion models quiz has no questions on this note yet.

Stated claims: 0.

**How each run is read.** Every output is read field by field in [[#Reading the fraction output]]. The toy numbers are the table in [[The Quarter Turn And The Fraction#The fraction at four posts]].

## Try the fraction yourself

Navigation: [[#Reading the fraction output]] ➡️

**Where you work.** The folder [[Running The Quarter Circle Under The Cosine Schedule#Try the quarter circle yourself]] makes, with its `plane.py` and `cosine.py`. Python 3 with matplotlib; nothing here touches a real project.

**1. What you need** and **2. when it is missing**: [[Running The Quarter Circle Under The Cosine Schedule#Try the quarter circle yourself]], steps 1 and 2.

**3. The setup.** Work in the folder that note's step 3 makes, with `plane.py` and `cosine.py`. Save [[The Quarter Turn And The Fraction#The consequence: slow at both ends, fastest in the middle|step 3's script]] as `s3_curve.py`, [[The Quarter Turn And The Fraction#All the words together: the fraction|step 4's]] as `s4_fraction.py`, and [[Which Pieces Of C_k Change The Noise#Removing each piece, drawn|the removals']] as `remove_a_piece.py`.

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

Then the two pieces that do change the noise, the square and the division by 1 + δ, each removed:

```bash
python3 remove_a_piece.py
```

```text
no square:   C_51 0.69157 (with it 0.47826)   last step drops 0.015584 (with it 0.000243)
no division: C_100 0.000158   beta_50 0.032198 (with it 0.031546)   beta_99 -15.0 (with it 1.0)
saved quarter-turn-remove-a-piece.svg
```

**9. Clean up, and prove it.** The folder is the quarter circle's, so this removes its files too:

```bash
cd ~ && rm -r ~/playground/sandbox/schedule-figures
ls ~/playground/sandbox/schedule-figures; echo $?
```

You should see `ls: cannot access '/home-mscluster/mmolefe/playground/sandbox/schedule-figures': No such file or directory` (with your own home folder in the path), then `2`.

## Reading the fraction output

Navigation: ⬅️ [[#Try the fraction yourself]]

**Where "derived" points.** "Derived above" is [[The Quarter Turn And The Fraction#Step 4: the fraction]], and "derived below" is [[Which Pieces Of C_k Change The Noise#How the denominator cancels]].

| Step | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 4 | `C_1` | `0.99937` | the share kept after code step 0, $\bar\alpha_0$ | shown |
| 4 | first noise share | `0.000631`, `0.000247` | with and without the offset | shown |
| 5 | `f(0)` | `0.99984` | $\cos^2 0.714^\circ$, the denominator | shown |
| 6 | `post 51` | `0.47819 / 0.99984 = 0.47826` | numerator over denominator, $\bar\alpha_{50}$ | derived above |
| 6 | `largest gap` | `1.1e-16` | β with and without the denominator differ only by rounding in the last binary digit | derived below |
| 7 | `0.03155` | $\beta_{50}$ | the same as step 6, from the numerators alone | derived below |
| 8 | `t = 98` | `0.749939` both ways | the denominator cancels late in the schedule too | derived below |
| 8 | `no square` | `C_51 0.69157`, last step `0.015584` | $\cos\theta_k / \cos\theta_0$, the multiplier and not the share; it falls steeply into post 100 | shown, [[Which Pieces Of C_k Change The Noise#Removing each piece, drawn]] |
| 8 | `no division` | `C_100 0.000158`, `beta_50 0.032198` | post 100 at 90.72°; every step's noise moves | shown, same figure |
| 8 | `beta_99` | `-15.0`, and `1.0` with the division | $1 - C_{100}/C_{99}$; the rebuild clips them to 0 and 0.999 | shown; the clip is line 19 of [`rebuild/model.py`](../../../../PhD/reduce-reuse-recycle/rebuild/model.py) |

> [!note]- How this was checked
> The nine steps were run as written on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and matplotlib 3.10.8 from the machine's `python3`, in an empty folder made as the quarter circle's step 3 makes it, `~/playground/sandbox/quarter-turn-fraction`, by vault-writer. Every script was copied byte for byte from the notes' code blocks and scanned for en dashes, curly quotes and non-breaking spaces, and none was found. Every output above is that run's text, steps 4 to 8 match the earlier run in `~/playground/sandbox/schedule-figures` character for character, and the folder was removed afterwards (clean-up check returned 2).
>
> The prepared environment `~/.vault-sandbox` is missing on this machine.
