---
aliases: [running the unit circle, unit circle sandbox, reading the unit-circle output, the trigonometry sandbox folder]
sources:
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Trigonometry, version 2.4: the unit circle, PDF p. 10; polar coordinates, PDF p. 68, the formulas these runs check: ../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=10"
standard: vault-note v2
---

# Running The Unit Circle

Up: [[Trigonometry]] · ⬅️ [[Polar Coordinates]] · [[Radians]] ➡️

Mathematics, Trigonometry. Needs: [[The Unit Circle]] and [[Polar Coordinates]], whose figure scripts these runs make and check.

**The unit circle and polar coordinates, run in an empty folder from the circle every 15° to the way back from $(x, y)$.**

> [!question]- Test yourself
> No quiz page covers this note yet.

> [!warning]- Unfinished
> - No quiz page for this note yet.

Stated claims: 0.

**How each run is read.** Every output is read field by field in [[#Reading the unit-circle output]]. The toy numbers are the table in [[The Unit Circle#The angles and their table]].

**Colours, as in The Unit Circle.** <span style="color:#2e7d32">**Green is $\cos\theta$, the horizontal leg**</span>, <span style="color:#ef6c00">**orange is $\sin\theta$, the vertical leg**</span>, <span style="color:#1565c0">**blue is the point and its angle**</span>, and <span style="color:#757575">**grey is a case drawn for comparison**</span>.

## Try the unit circle yourself

Navigation: [[#Reading the unit-circle output]] ➡️

**Where you work.** Python 3 with matplotlib, in a new empty folder; nothing here touches a real project. Every figure script imports `plane.py`, saved in step 3. [[Radians]] and [[The Cosine Wave]] run their scripts in this same folder.

**1. What you need.** Python 3 with matplotlib:

```bash
python3 -c "import matplotlib; print(matplotlib.__version__)"
```

This run printed `3.10.8`.

**2. When it is missing.** Make the prepared environment once, `uv venv ~/.vault-sandbox` then `uv pip install --python ~/.vault-sandbox/bin/python pandas numpy scipy matplotlib statsmodels openpyxl`, and run every script below with `~/.vault-sandbox/bin/python` in place of `python3`. Not run on this machine, whose `python3` already has matplotlib.

**3. The setup: an empty folder and the plane.** Make the folder and confirm it is empty:

```bash
mkdir -p ~/playground/sandbox && mkdir ~/playground/sandbox/unit-circle-figures && cd ~/playground/sandbox/unit-circle-figures && ls -A | wc -l
```

You should see `0`. Copy [plane.py](sandbox/plane.py) from the `sandbox/` folder beside this note into it.

**What `plane.py` gives you.** `plane` draws Cartesian axes through the origin with equal scales, so a circle looks round, and `save` writes each figure as SVG. `angle` draws the arc that marks an angle, `circle` draws the unit circle up to a given degree, and the colours are held there.

**The script names.** Save each figure script under the short name the steps below use: from [[The Unit Circle]], `t1_triangle.py` (the right triangle), `t2_circle.py` (the circle every 15°), `t3_ray.py` (the line from the origin) and `t9_squares.py` (the squares and the sum); from [[Polar Coordinates]], `t5_polar.py` (the point) and `back.py` (the way back).

**4. A look before: the circle every 15°.**

```bash
python3 t2_circle.py
```

```text
  0 deg  point (1.000, 0.000)  x^2 + y^2 = 1.000
 15 deg  point (0.966, 0.259)  x^2 + y^2 = 1.000
 30 deg  point (0.866, 0.500)  x^2 + y^2 = 1.000
 45 deg  point (0.707, 0.707)  x^2 + y^2 = 1.000
 60 deg  point (0.500, 0.866)  x^2 + y^2 = 1.000
 75 deg  point (0.259, 0.966)  x^2 + y^2 = 1.000
 90 deg  point (0.000, 1.000)  x^2 + y^2 = 1.000
saved t2-unit-circle-sampled-points.svg
```

**5. The failure: reading a side without dividing by the hypotenuse.**

```bash
python3 t1_triangle.py
```

```text
hypotenuse 1: adjacent 0.6915  opposite 0.7224  adjacent / hypotenuse 0.6915
hypotenuse 2: adjacent 1.3830  opposite 1.4447  adjacent / hypotenuse 0.6915
saved t1-right-triangle-cosine.svg
```

On the triangle twice the size, the adjacent side alone reads 1.3830, which is no cosine at all. The ratio stays 0.6915.

**6. The technique: polar to Cartesian.**

```bash
python3 t5_polar.py
```

```text
polar (r = 1, theta = 46.25 deg)  ->  cartesian (0.6915, 0.7224)
saved t5-polar-to-cartesian.svg
```

**7. Another way to the same point: turn a line of length 1.**

```bash
python3 t3_ray.py
```

```text
ray at 46.25 deg ends at (0.6915, 0.7224), distance 1.0000 from the origin
saved t3-line-from-origin-angle.svg
```

**8. More worked examples.** Step 4 already printed the point at seven angles, 0° to 90° every 15°, each one row of [[The Unit Circle#The angles and their table|the table]]. These two run the squares taken away, the radius-2 circle and the way back from $(x, y)$:

```bash
python3 t9_squares.py
python3 back.py
```

```text
radius 1: legs 0.6915 and 0.7224  squares 0.4782 + 0.5218 = 1.0000
without the squares: 0.6915 + 0.7224 = 1.4139
the line x + y = 1 meets the 46.25 deg ray at distance 0.7073
radius 2: legs 1.3830 and 1.4447  squares 1.9128 + 2.0872 = 4.0000
saved t9-why-the-squares-and-the-sum.svg
hypot 1.0000  atan2 46.25 deg
cmath.polar  r 1.0000  phi 0.8072 rad = 46.25 deg
point (-x, -y): atan(y / x) 46.25 deg  atan2 226.25 deg
radius 2: hypot 2.0000  atan2 46.25 deg
```

**9. Clean up, and prove it.**

```bash
cd ~ && rm -r ~/playground/sandbox/unit-circle-figures
ls ~/playground/sandbox/unit-circle-figures; echo $?
```

You should see `ls: cannot access '/home-mscluster/mmolefe/playground/sandbox/unit-circle-figures': No such file or directory` (with your own home folder in the path), then `2`.

## Reading the unit-circle output

Navigation: ⬅️ [[#Try the unit circle yourself]]

| Step | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 4 | `x^2 + y^2` | `1.000` on every row | each sampled point is at distance 1 from the origin | derived in [[The Unit Circle#How the unit circle works]] |
| 4 | `30 deg  point` | `(0.866, 0.500)` | the dashed cell of the table: cos 30° and sin 30° | shown |
| 5 | `adjacent`, hypotenuse 2 | `1.3830` | a side alone depends on the triangle's size | shown |
| 5 | `adjacent / hypotenuse` | `0.6915` for both sizes | the ratio depends on the angle only | derived in [[The Unit Circle#How the unit circle works]] |
| 6 | `cartesian` | `(0.6915, 0.7224)` | $x = r\cos\theta$, $y = r\sin\theta$ with $r = 1$ | cited, trigonometry handbook p. 68 |
| 7 | `ends at` | `(0.6915, 0.7224)` | the same point as step 6, reached by turning a line | shown |
| 7 | `distance` | `1.0000` | `math.hypot(x, y)`, the length of the line | shown |
| 8 | `squares` | `0.4782 + 0.5218 = 1.0000` | the squared legs at 46.25° add to the squared radius | shown |
| 8 | `without the squares` | `1.4139` | the bare legs add to more than the radius | shown |
| 8 | `meets ... at distance` | `0.7073` | the line $x + y = 1$ passes inside the circle at 46.25° | shown |
| 8 | `radius 2: ... squares` | `1.9128 + 2.0872 = 4.0000` | at radius 2 the legs are $2\cos\theta$ and $2\sin\theta$ and their squares add to $2^2$ | shown |
| 8 | `hypot`, `atan2` | `1.0000`, `46.25 deg` | the way back: $r = \sqrt{x^2 + y^2}$ and the turn from $y/x$ | cited, trigonometry handbook p. 68 |
| 8 | `cmath.polar` | `r 1.0000  phi 0.8072 rad` | the same length and turn, the turn in radians | shown |
| 8 | `point (-x, -y)` | `46.25 deg` against `226.25 deg` | $\tan^{-1}(y/x)$ cannot tell opposite points apart; `atan2` can | shown |
| 8 | `radius 2: hypot` | `2.0000`, `46.25 deg` | the length doubles and the turn stays | shown |

> [!note]- How this was checked
> Steps 4 to 7 were first run on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and matplotlib 3.10.8 from the machine's `python3`, in the empty folder `~/playground/sandbox/unit-circle-figures`, by vault-writer. They were re-run the same day in a fresh empty folder built from the code blocks of [[The Unit Circle]] and [[Polar Coordinates]] as filed, printing the same lines byte for byte, and step 8's two scripts were run there for the first time. The prepared environment `~/.vault-sandbox` is missing on this machine and was not needed.
>
> The figure SVGs from the re-run differ from the embedded ones only in matplotlib's date stamp. Both folders were removed afterwards and the clean-up check returned 2.
