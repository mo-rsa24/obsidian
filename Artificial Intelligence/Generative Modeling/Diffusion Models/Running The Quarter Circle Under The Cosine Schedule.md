---
aliases: [running the quarter circle under the cosine schedule, quarter circle sandbox, the quarter circle in an empty folder, the six moves at post 51, six_moves.py, reading the quarter-circle output]
sources:
  - "Nichol, Dhariwal, Improved Denoising Diffusion Probabilistic Models, ICML 2021, section 3.2 and equation (17), the formula these runs compute, PDF p. 4: https://arxiv.org/pdf/2102.09672#page=4"
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Trigonometry, the unit circle, PDF p. 10: ../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf#page=10"
standard: vault-note v2
---

# Running The Quarter Circle Under The Cosine Schedule

Up: [[Diffusion Models]] · ⬅️ [[How The Quarter Circle Gives The Multipliers]] · [[The Quarter Turn And The Fraction]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[The Quarter Circle Under The Cosine Schedule]] and [[How The Quarter Circle Gives The Multipliers]], whose figure scripts these runs make and run.

**The quarter circle's scripts, run in an empty folder from the plane and `cosine.py` to the six moves at post 51.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. It has no questions on this note yet.

> [!warning]- Unfinished
> - The diffusion models quiz has no questions on this note yet.

Stated claims: 0.

**How each run is read.** Every output is read field by field in [[#Reading the quarter-circle output]]. The toy numbers are the table in [[The Quarter Circle Under The Cosine Schedule#The posts and their table]].

## Try the quarter circle yourself

Navigation: [[#Reading the quarter-circle output]] ➡️

**Where you work.** Python 3 with matplotlib, in a new empty folder; nothing here touches a real project. The scripts import `plane.py` and `cosine.py`, set up in step 3. For the build by hand: paper, a ruler, a protractor and a piece of string.

**1. What you need.** Python 3 with matplotlib:

```bash
python3 -c "import matplotlib; print(matplotlib.__version__)"
```

This run printed `3.10.8`.

**2. When it is missing.** Make the prepared environment once, `uv venv ~/.vault-sandbox` then `uv pip install --python ~/.vault-sandbox/bin/python pandas numpy scipy matplotlib statsmodels openpyxl`, and run every script with `~/.vault-sandbox/bin/python` in place of `python3`. Not run on this machine, whose `python3` already has matplotlib.

**3. The setup: the plane and the schedule.** Make the empty folder and confirm it is empty:

```bash
mkdir -p ~/playground/sandbox && mkdir ~/playground/sandbox/schedule-figures && cd ~/playground/sandbox/schedule-figures && ls -A | wc -l
```

You should see `0`. Copy [plane.py](../../../Mathematics/Trigonometry/sandbox/plane.py), the figure helper of the [[Trigonometry]] notes, into it. Save this as `cosine.py`:

```python
import math

T, delta = 100, 0.008


def position(k, d=delta):
    return (k / T + d) / (1 + d)


def theta_deg(k, d=delta):
    return position(k, d) * 90


def f(k, d=delta):
    return math.cos(math.radians(theta_deg(k, d))) ** 2


def C(k, d=delta):
    return f(k, d) / f(0, d)
```

**The figure scripts.** Save the script of [[The Quarter Circle Under The Cosine Schedule#All the words together: the position formula|step 1]] as `s1_posts.py` and the one under [[The Quarter Circle Under The Cosine Schedule#The consequence: move the posts|its consequence]] as `s1_consequence.py`. Save [[How The Quarter Circle Gives The Multipliers#Step 2: the point is the two multipliers|step 2's]] as `s2_point.py` and [[How The Quarter Circle Gives The Multipliers#The quarter circle's mechanism|the mechanism's]] as `mechanism.py`. [[Running The Quarter Turn And The Fraction]] runs its three scripts, `s3_curve.py`, `s4_fraction.py` and `remove_a_piece.py`, in this same folder.

**4. A look before: where the posts sit.**

```bash
python3 s1_posts.py
```

```text
post   0  p 0.0079   0.714 deg    delta = 0: p 0.0000   0.000 deg    no division:  0.720 deg
post   1  p 0.0179   1.607 deg    delta = 0: p 0.0100   0.900 deg    no division:  1.620 deg
post  51  p 0.5139  46.250 deg    delta = 0: p 0.5100  45.900 deg    no division: 46.620 deg
post 100  p 1.0000  90.000 deg    delta = 0: p 1.0000  90.000 deg    no division: 90.720 deg
saved s1-position-ruler-posts.svg
```

**5. The failure: no offset, and no division.** The middle columns of step 4 are the schedule with δ = 0: post 0 sits on the axis at 0.000°, and post 51 moves only 0.35°, to 45.900°. The last column drops the division by 1 + δ, and post 100 lands at 90.720°, past the quarter turn. Draw both on the plane:

```bash
python3 s1_consequence.py
```

```text
saved quarter-circle-move-the-posts.svg
```

**6. The technique: the point at post 51 and its multipliers.**

```bash
python3 s2_point.py
```

```text
post 51 at 46.25 deg: point (0.6915, 0.7224)
multipliers: sqrt(abar_50) = sqrt(C_51) = 0.6916   sqrt(1 - abar_50) = 0.7223
string along the arc: 0.8072 rad = 8.07 cm on a 10 cm radius
saved s2-circle-point-is-the-multipliers.svg
```

**7. Another way: all six moves at post 51 in one run.** Save this as `six_moves.py`:

```python
import math
from cosine import position, theta_deg

k = 51
p = position(k)
deg = theta_deg(k)
rad = math.radians(deg)
x, y = math.cos(rad), math.sin(rad)
f0 = math.cos(math.radians(theta_deg(0))) ** 2
C = x * x / f0
print(f"1 circle: x^2 + y^2 = {x * x + y * y:.4f}")
print(f"2 point at {deg:.2f} deg: ({x:.4f}, {y:.4f})")
print(f"3 angle: {deg:.2f} deg = {rad:.4f} rad, string {rad * 10:.2f} cm on a 10 cm radius")
print(f"4 position: p_{k} = ({k} + 0.8) / 100.8 = {p:.4f}, so {p:.4f} x 90 = {deg:.2f} deg")
print(f"5 multipliers: sqrt(C_{k}) {math.sqrt(C):.4f} against x {x:.4f}, sqrt(1 - C_{k}) {math.sqrt(1 - C):.4f} against y {y:.4f}")
print(f"6 fraction: C_{k} = {x * x:.5f} / {f0:.5f} = {C:.5f}")
```

```bash
python3 six_moves.py
```

![The six moves at post 51: the point (0.6915, 0.7224) on the circle, 46.25 degrees as 0.8072 radians and an 8.07 cm string, position 0.5139, multipliers 0.6916 and 0.7223, and C_51 = 0.47819 / 0.99984 = 0.47826|1000](assets/quarter-circle-the-six-moves-at-post-51.png)

**8. More worked examples.** The quarter turn every 15°, with the point at post 51 and the fraction, in one figure:

```bash
python3 mechanism.py
```

```text
saved quarter-circle-the-mechanism.svg
```

[[Running The Cosine Noise Schedule#Try the boundary values yourself]], steps 6 to 8, runs the same formula at posts 0, 1, 26, 51, 76, 99 and 100.

**9. Clean up, and prove it.** After [[Running The Quarter Turn And The Fraction]] has run its three scripts here, `s3_curve.py`, `s4_fraction.py` and `remove_a_piece.py`:

```bash
cd ~ && rm -r ~/playground/sandbox/schedule-figures
ls ~/playground/sandbox/schedule-figures; echo $?
```

You should see `ls: cannot access '/home-mscluster/mmolefe/playground/sandbox/schedule-figures': No such file or directory` (with your own home folder in the path), then `2`.

## Reading the quarter-circle output

Navigation: ⬅️ [[#Try the quarter circle yourself]]

**Where "derived" points.** Step 1 is derived in [[The Quarter Circle Under The Cosine Schedule#Step 1: the position ruler]], and the multipliers in [[How The Quarter Circle Gives The Multipliers#How the quarter circle gives the multipliers]].

| Step | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 4 | post 0, `p` | `0.0079`, `0.714 deg` | $0.8 / 100.8$: the offset alone | derived in step 1 |
| 4 | post 100, `p` | `1.0000` both ways | dividing by $1 + \delta$ lands both schedules on the last post | derived in step 1 |
| 4 | `no division` | `0.720 deg` to `90.720 deg` | $(k/T + 0.008) \times 90^\circ$: post 100 passes the quarter turn | derived in step 1 |
| 6 | `point` | `(0.6915, 0.7224)` | $\cos 46.25^\circ$ and $\sin 46.25^\circ$ | cited, [trigonometry handbook p. 10](../../../Mathematics/references/textbooks/trigonometry/trigonometry-handbook.pdf#page=10) |
| 6 | `multipliers` | `0.6916`, `0.7223` | $\sqrt{C_{51}} = \sqrt{\bar\alpha_{50}}$ and $\sqrt{1 - C_{51}}$ | derived in the multipliers note |
| 6 | `string` | `0.8072 rad`, `8.07 cm` | $46.25 \times \pi/180$, and 10 times that on a 10 cm radius | derived in [[Radians]] |
| 7, line 1 | `x^2 + y^2` | `1.0000` | the point is on the circle of radius 1 | derived in [[The Cosine Wave]] |
| 7, line 4 | `p_51` | `0.5139` | $51.8 / 100.8$, just past halfway along the arc | derived in step 1 |
| 7, line 6 | `C_51` | `0.47819 / 0.99984 = 0.47826` | the fraction of [[The Quarter Turn And The Fraction]], the $\bar\alpha_{50} = 0.4783$ of [[From Many Steps To One Jump]] | shown in [[Running The Cosine Noise Schedule#Try the boundary values yourself]], step 7 |

> [!note]- How this was checked
> The nine steps were run as written on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and matplotlib 3.10.8 from the machine's `python3`, in the empty folder `~/playground/sandbox/schedule-figures`, by vault-writer. Every script was copied byte for byte from the notes' code blocks and scanned for en dashes, curly quotes and non-breaking spaces, and none was found. Every output above is that run's text, and the folder was removed afterwards (clean-up check returned 2).
>
> The prepared environment `~/.vault-sandbox` is missing on this machine. `six_moves.py` printed the same six lines as the earlier run its picture was rendered from, in DejaVu Sans Mono, never drawn. The SVGs filed beside the notes were saved the same day by the same scripts in `~/playground/sandbox/quarter-circle-retrofit`, and differ from this run's only in matplotlib's date line and generated element ids.
