---
aliases: [running the cosine noise schedule, cosine schedule sandbox, the boundary values in an empty folder, four boundaries by hand, reading the boundary-value output, the code's form beside abar, three more boundaries]
sources:
  - "Nichol, Dhariwal, Improved Denoising Diffusion Probabilistic Models, ICML 2021, section 3.2 and equation (17), the formula these runs compute, PDF p. 4: https://arxiv.org/pdf/2102.09672#page=4"
standard: vault-note v2
---

# Running The Cosine Noise Schedule

Up: [[Diffusion Models]] · ⬅️ [[How Each Piece Of The Cosine Schedule Works]] · [[The Quarter Circle Under The Cosine Schedule]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[The Cosine Noise Schedule]], the formula these runs compute.

**The cosine schedule's boundary values, run in an empty folder from the formula as three functions to four posts by hand.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. It has no questions on this note yet.

> [!warning]- Unfinished
> - The diffusion models quiz has no questions on this note yet.

Stated claims: 0.

**How each run is read.** The broken run, the code's form and the three more boundaries are read field by field under their own output, and the four boundaries by hand in [[#Reading the boundary-value output]]. The toy numbers are the table in [[The Cosine Noise Schedule#The posts and their table]].

**Colours in this note.** <span style="color:#2e7d32">**Green is a boundary value $C_k$**</span>, <span style="color:#ef6c00">**orange is a step's noise share $\beta_t$**</span>, <span style="color:#1565c0">**blue is a post's position and its angle $\theta_k$**</span>, and <span style="color:#6a1b9a">**purple is the denominator $\cos^2\theta_0$**</span>, as in [[The Cosine Noise Schedule]].

## Try the boundary values yourself

Navigation: [[#Reading the boundary-value output]] ➡️

**Where you work.** Any terminal with Python 3, and a new empty folder; nothing here touches a real project. The scripts use the standard library only (`math`), so `python3` runs them, and so does the prepared environment `~/.vault-sandbox/bin/python` where it exists.

**The figure scripts.** The four figure scripts in [[The Cosine Noise Schedule]] import the `cosine.py` of step 3 and also need matplotlib, so run them in this folder before step 9 removes it.

**1. What you need.** Python 3:

```bash
python3 --version
```

This run printed `Python 3.12.10`.

**2. When it is missing.** Install Python 3 from python.org, or run `uv python install 3.12`. Not run on this machine, which already has it.

**3. Make something to act on: the formula as three functions.** Make the empty folder and confirm it is empty:

```bash
mkdir ~/playground/sandbox/cosine-boundaries && cd ~/playground/sandbox/cosine-boundaries && ls -A | wc -l
```

You should see `0`. Save this as `cosine.py`. `d` lets a script switch the offset off:

```python
import math

T, delta = 100, 0.008


def theta_deg(k, d=delta):
    return (k / T + d) / (1 + d) * 90


def f(k, d=delta):
    return math.cos(math.radians(theta_deg(k, d))) ** 2


def C(k, d=delta):
    return f(k, d) / f(0, d)
```

**4. A look before: the angle, piece by piece.** Save this as `look.py`:

```python
from cosine import T, delta

print("boundary values", T + 1, " steps between them", T)
for k in (0, 1, 51, 100):
    pos = k / T
    shifted = pos + delta
    squeezed = shifted / (1 + delta)
    print(f"k = {k:3d}  k/T {pos:.2f}  + delta {shifted:.3f}  / (1 + delta) {squeezed:.5f}  x 90 = {squeezed * 90:.3f} deg")
```

```bash
python3 look.py
```

```text
boundary values 101  steps between them 100
k =   0  k/T 0.00  + delta 0.008  / (1 + delta) 0.00794  x 90 = 0.714 deg
k =   1  k/T 0.01  + delta 0.018  / (1 + delta) 0.01786  x 90 = 1.607 deg
k =  51  k/T 0.51  + delta 0.518  / (1 + delta) 0.51389  x 90 = 46.250 deg
k = 100  k/T 1.00  + delta 1.008  / (1 + delta) 1.00000  x 90 = 90.000 deg
```

101 posts for 100 gaps. The offset moves $k = 0$ to $0.714^\circ$, and dividing by $1.008$ brings $k = 100$ back to exactly $90^\circ$.

**5. The failure: no offset, and no denominator.** Save this as `broken.py`. It computes $C_1$ with $\delta = 0$, and $C_0$ without dividing by $\cos^2\theta_0$:

```python
import math
from cosine import C, f

right, plain = C(1), C(1, d=0.0)
print(f"with offset:     C_1 {right:.5f}  first noise share {1 - right:.6f}  sd {math.sqrt(1 - right):.4f}")
print(f"without offset:  C_1 {plain:.5f}  first noise share {1 - plain:.6f}  sd {math.sqrt(1 - plain):.4f}")
print(f"without the denominator:  C_0 {f(0):.5f}")
```

```bash
python3 broken.py
```

![Without the offset C_1 is 0.99975, so the first step's noise share is 0.000247 and its sd 0.0157 against 0.0251; without the denominator C_0 is 0.99984|880](assets/cosine-schedule-without-the-offset-or-the-denominator.png)

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | with offset, $C_1$ | `0.99937` | the share kept after the first step | shown |
| 2 | with offset, sd | `0.0251` | the first step's noise share is $1 - C_1 = 0.000631$, because the total variance is 1 and $C_0 = 1$; its square root is the typical size of the first step's noise | derived in [[From Many Steps To One Jump#How two steps become every step]] |
| 3 | without offset, $C_1$ | `0.99975` | $\cos^2 0.9^\circ$: the angle starts at $0^\circ$, so the first step barely moves | shown |
| 4 | without offset, share | `0.000247` | the first step's noise variance falls to about 0.39 of $0.000631$ | shown |
| 5 | without offset, sd | `0.0157` | against $0.0251$: the first step adds noise about 0.63 times as large | shown |
| 6 | without the denominator, $C_0$ | `0.99984` | $\cos^2 0.714^\circ$: the clean point would already have lost 0.016 % of its variance before any step | shown |

**6. The technique: four boundaries by hand.** Save this as `by_hand.py`. It prints every piece of the hand calculation at $k = 0, 1, 51, 100$:

```python
import math
from cosine import theta_deg, f

f0 = f(0)
for k in (0, 1, 51, 100):
    th = theta_deg(k)
    c = math.cos(math.radians(th))
    print(f"k = {k:3d}  theta {th:6.3f} deg  cos {c:.5f}  cos^2 {c * c:.5f}  C = {c * c:.5f} / {f0:.5f} = {c * c / f0:.5f}")
```

```bash
python3 by_hand.py
```

You should see:

![Four boundaries by hand: C_0 = 1, C_1 = 0.99937, C_51 = 0.47826 and C_100 = 0, each from its angle, cosine and squared cosine|1000](assets/cosine-schedule-four-boundaries-by-hand.png)

[[#Reading the boundary-value output]] reads each numbered field.

**7. Another way to get the same answer: the code's form, beside $\bar\alpha$.** Save this as `same_as_code.py`. It is the rebuild's `cosine_beta_schedule` in radians, followed by the product that makes $\bar\alpha$, so each boundary sits beside the kept share one step earlier:

```python
import math

T, s = 100, 0.008
C = [math.cos((k / T + s) / (1 + s) * math.pi / 2) ** 2 for k in range(T + 1)]
C = [c / C[0] for c in C]
betas = [min(max(1 - C[k + 1] / C[k], 0.0), 0.999) for k in range(T)]
abar, kept = [], 1.0
for b in betas:
    kept *= 1 - b
    abar.append(kept)
print("C_0", round(C[0], 5), " C_100", round(C[100], 5))
for k in (1, 26, 51, 76):
    print(f"C_{k} {C[k]:.5f}   abar_{k - 1} {abar[k - 1]:.5f}")
```

```bash
python3 same_as_code.py
```

![The code form gives C_0 = 1 and C_100 = 0, and C_1, C_26, C_51, C_76 equal abar_0, abar_25, abar_50, abar_75|420](assets/cosine-schedule-the-code-form-and-abar.png)

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | $C_0$ | `1.0` | the radians form agrees with step 6 | shown |
| 2 | $C_{100}$ | `0.0` | the quarter turn ends at $\pi/2$ | shown |
| 3, 4 | $C_1$, $\bar\alpha_0$ | `0.99937`, `0.99937` | the share kept after code step 0 is boundary 1: the rebuild's `walk-numbers.json` rounds it to $0.9994$ | shown |
| 5, 6 | $C_{51}$, $\bar\alpha_{50}$ | `0.47826`, `0.47826` | the $0.4783$ the other notes in this folder use | shown |

The rows for $k = 26$ and $k = 76$ match the same way: $0.83562$ and $0.13349$ are the $\bar\alpha_{25} = 0.8356$ and $\bar\alpha_{75} = 0.1335$ of `walk-numbers.json`.

**8. More worked examples.** The walk used $k = 0, 1, 51, 100$ and the broken run without the offset, all above. The scene's [Timetable 2 frame](https://claude.ai/artifact/X7QGLTxssbz41G7iTiRxC9#timetable-one-boundary) also offers $k = 99$. Save this as `more_boundaries.py`, which runs the same hand calculation at $k = 26$, $76$ and $99$:

```python
import math
from cosine import theta_deg, f

f0 = f(0)
for k in (26, 76, 99):
    th = theta_deg(k)
    c = math.cos(math.radians(th))
    print(f"k = {k:3d}  theta {th:6.3f} deg  cos {c:.5f}  cos^2 {c * c:.5f}  C = {c * c:.5f} / {f0:.5f} = {c * c / f0:.5f}")
```

```bash
python3 more_boundaries.py
```

![Three more boundaries: C_26 = 0.83562 at 23.929 degrees, C_76 = 0.13349 at 68.571 degrees, C_99 = 0.00024 at 89.107 degrees|1000](assets/cosine-schedule-three-more-boundaries.png)

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1, 2 | $k = 26$ | `23.929 deg`, `0.83562` | about a quarter of the way through, about five sixths of the variance is still kept: the curve is flat near the start | shown |
| 3, 4 | $k = 76$ | `68.571 deg`, `0.13349` | three quarters through, under a seventh is kept | shown |
| 5, 6 | $k = 99$, angle and cosine | `89.107 deg`, `0.01558` | less than one degree short of the quarter turn, the cosine is small | shown |
| 7 | $C_{99}$ | `0.00024` | squaring a small cosine makes it much smaller: $0.01558^2 = 0.00024$. One gap later, $C_{100} = 0$ | shown |

**9. Clean up, and prove it.**

```bash
cd ~ && rm -r ~/playground/sandbox/cosine-boundaries
ls ~/playground/sandbox/cosine-boundaries; echo $?
```

You should see `ls: cannot access '/home-mscluster/mmolefe/playground/sandbox/cosine-boundaries': No such file or directory` (with your own home folder in the path), then `2`.

## Reading the boundary-value output

Navigation: ⬅️ [[#Try the boundary values yourself]]

**Where "derived" points.** Every field marked derived is derived in [[How Each Piece Of The Cosine Schedule Works#How each piece of C_k works]].

From step 6:

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | $\theta_0$ | `0.714 deg` | $\frac{0.008}{1.008} \times 90^\circ$: the offset alone | derived |
| 2 | $\cos^2\theta_0$ | `0.99984` | the denominator every $C_k$ shares | derived |
| 3 | $C_0$ | `1.00000` | $0.99984 / 0.99984$: nothing lost before the first step | derived |
| 4 | $\theta_1$ | `1.607 deg` | $\frac{0.018}{1.008} \times 90^\circ$ | derived |
| 5 | $C_1$ | `0.99937` | $0.99921 / 0.99984$, the share kept after code step 0 | derived |
| 6 | $\theta_{51}$ | `46.250 deg` | $\frac{0.518}{1.008} \times 90^\circ$, just past halfway round | derived |
| 7 | $\cos\theta_{51}$ | `0.69151` | the horizontal reach of the angle on the unit circle | cited, [trigonometry handbook p. 10](../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf#page=10) |
| 8 | $C_{51}$ | `0.47826` | $0.47819 / 0.99984$: a little under half the variance kept | derived |
| 9 | $\theta_{100}$ | `90.000 deg` | $\frac{1.008}{1.008} \times 90^\circ$, exactly a quarter turn | derived |
| 10 | $C_{100}$ | `0.00000` | $\cos 90^\circ = 0$: nothing of the clean signal is kept at the last boundary | derived |

> [!note]- How this was checked
> The six scripts were run on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and the standard library only, in the empty folder `~/playground/sandbox/cosine-boundaries`, by vault-writer. The folder was removed afterwards and the clean-up check returned 2. The prepared environment `~/.vault-sandbox` is missing on this machine and was not needed.
>
> The same six scripts were re-run the same day from this note's code blocks, byte for byte, in a fresh empty folder `~/playground/sandbox/cosine-retrofit`, and printed the same lines as every output here; that folder was removed afterwards too.
>
> `same_as_code.py` is [the rebuild's `cosine_beta_schedule`](../../../../PhD/reduce-reuse-recycle/rebuild/model.py) (lines 13 to 19) written without NumPy. Its values match the rebuild's [`walk-numbers.json`](../../../../PhD/reduce-reuse-recycle/rebuild/out/walk-numbers.json): $\bar\alpha_0 = 0.9994$, $\bar\alpha_{25} = 0.8356$, $\bar\alpha_{50} = 0.4783$, $\bar\alpha_{75} = 0.1335$, $\beta_0 = 0.000631$, $\sqrt{1 - \bar\alpha_0} = 0.0251$. Every number in the walk's turn ($\theta_0$, $\theta_1$, $\theta_{51}$, their cosines and squares, $C_0$, $C_1$, $C_{51}$, $C_{100}$, and the broken run's $0.99975$, $0.000247$, $0.0157$ and $0.99984$) was reproduced by these scripts.
>
> The four terminal pictures were rendered from the captured text by a script in DejaVu Sans Mono, never drawn, and each was opened before filing.
