---
aliases: [running the cosine wave, cosine wave sandbox, reading the cosine-wave output, the slope of cos squared by a tiny step]
sources:
  - "Whitney, Math Handbook of Formulas, Processes and Tricks: Trigonometry, version 2.4: the Pythagorean identities, PDF p. 9, and graphs of the parent functions, PDF p. 16, the results these runs check: ../references/textbooks/trigonometry/trigonometry-handbook.pdf#page=9"
standard: vault-note v2
---

# Running The Cosine Wave

Up: [[Trigonometry]] · ⬅️ [[How The Cosine Wave Works]]

Mathematics, Trigonometry. Needs: [[The Cosine Wave]], whose three figure scripts these runs make and check, and [[Running The Unit Circle#Try the unit circle yourself|the unit circle sandbox]], whose folder they run in.

**The cosine's square run in an empty folder, from its value every 15° to its slope measured two ways.**

> [!question]- Test yourself
> No quiz page covers this note yet.

> [!warning]- Unfinished
> - No quiz page for this note yet.

Stated claims: 0.

**How each run is read.** Every output is read field by field in [[#Reading the cosine-wave output]]. The toy numbers are the table in [[The Cosine Wave#The quarter turn and its table]].

**Colours, as in The Cosine Wave.** <span style="color:#2e7d32">**Green is $\cos\theta$ and its square**</span>, <span style="color:#ef6c00">**orange is $\sin\theta$ and its square**</span>, <span style="color:#1565c0">**blue is the quarter turn and its drops**</span>, and <span style="color:#757575">**grey is a case drawn for comparison**</span>.

## Try the cosine wave yourself

Navigation: [[#Reading the cosine-wave output]] ➡️

**Where you work.** Python 3 with matplotlib, in the folder [[Running The Unit Circle#Try the unit circle yourself]] makes, with its `plane.py`. Nothing here touches a real project.

**1. What you need.** Python 3 with matplotlib, checked by [[Running The Unit Circle#Try the unit circle yourself]], step 1.

**2. When it is missing.** Step 2 there says how to make the prepared environment.

**3. The setup.** Work in the folder that note's step 3 makes, with [plane.py](sandbox/plane.py) in it. Save the three figure scripts of [[The Cosine Wave]] as `t6_shares.py` (under [[The Cosine Wave#The two shares|the two shares]]), `t7_wave.py` (under [[The Cosine Wave#The quarter turn: where the square is flat|the quarter turn]]) and `t10_drop_square.py` (under [[The Cosine Wave#The consequence: drop the square|the consequence]]).

**4. A look before: the square every 15°, and its drops.**

```bash
python3 -c "import math; xs = [round(math.cos(math.radians(d)) ** 2, 3) for d in range(0, 91, 15)]; print(xs); print([round(a - b, 3) for a, b in zip(xs, xs[1:])])"
```

```text
[1.0, 0.933, 0.75, 0.5, 0.25, 0.067, 0.0]
[0.067, 0.183, 0.25, 0.25, 0.183, 0.067]
```

**5. The failure: adding the legs without squaring them.**

```bash
python3 t6_shares.py
```

```text
cos^2 0.4782 + sin^2 0.5218 = 1.0000   without the squares: 0.6915 + 0.7224 = 1.4139
saved t6-pythagoras-shares.svg
```

**6. The technique: the slope at the two ends and the middle.**

```bash
python3 t7_wave.py
```

```text
theta 0     cos 1.0000  cos^2 1.0000  slope of cos 0.0000  slope of cos^2 0.0000
theta pi/4  cos 0.7071  cos^2 0.5000  slope of cos -0.7071  slope of cos^2 -1.0000
theta pi/2  cos 0.0000  cos^2 0.0000  slope of cos -1.0000  slope of cos^2 0.0000
saved t7-cosine-wave-quarter-turn.svg
```

**7. Another way to the slope: a tiny step either side.**

```bash
python3 -c "import math; h = 1e-6; f = lambda t: math.cos(t) ** 2; print([round((f(t + h) - f(t - h)) / (2 * h), 4) + 0 for t in (0, math.pi / 4, math.pi / 2)])"
```

```text
[0.0, -1.0, 0.0]
```

**8. More worked examples.** The first is the slope at 46.25°, two ways:

```bash
python3 -c "import math; t = math.radians(46.25); print(round(-2 * math.cos(t) * math.sin(t), 4), round(-math.sin(2 * t), 4))"
```

```text
-0.999 -0.999
```

The second is the quarter turn with the square dropped, beside the square:

```bash
python3 t10_drop_square.py
```

```text
cos² θ at 46.25 0.4782  first 15 drops 0.0670  last 15 drops 0.0670  slope at 0 0.0000  slope at pi/2 0.0000
cos θ  at 46.25 0.6915  first 15 drops 0.0341  last 15 drops 0.2588  slope at 0 0.0000  slope at pi/2 -1.0000
saved t10-drop-the-square.svg
```

**9. Clean up, and prove it.** [[Running The Unit Circle#Try the unit circle yourself]], step 9, removes the folder and checks it is gone.

## Reading the cosine-wave output

Navigation: ⬅️ [[#Try the cosine wave yourself]]

| Step | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 4 | first list | `1.0` to `0.0` | $\cos^2$ at 0°, 15°, …, 90° | shown |
| 4 | second list | `0.067` … `0.25, 0.25` … `0.067` | slow at both ends, fastest in the middle | derived in [[How The Cosine Wave Works#The drops]] |
| 5 | `cos^2 + sin^2` | `0.4782 + 0.5218 = 1.0000` | the two shares at 46.25° | derived in [[How The Cosine Wave Works#The identity]] |
| 5 | `without the squares` | `1.4139` | the legs alone overshoot 1 by 0.4139 | shown |
| 6 | `slope of cos^2` at 0 and π/2 | `0.0000` | flat at both ends of the quarter turn | derived in [[How The Cosine Wave Works#The slope]] |
| 6 | `slope of cos^2` at π/4 | `-1.0000` | the steepest point | derived in [[How The Cosine Wave Works#The slope]] |
| 6 | `slope of cos` at π/2 | `-1.0000` | without the square the end is not flat | derived in [[The Cosine Wave#The consequence: drop the square]] |
| 7 | the list | `[0.0, -1.0, 0.0]` | the slope measured by stepping $10^{-6}$ either side agrees with step 6 | shown |
| 8 | both | `-0.999` | $-2\cos\theta\sin\theta = -\sin 2\theta$ at 46.25° | derived in [[How The Cosine Wave Works#The slope]] |
| 8 | `first 15 drops`, `last 15 drops` | `0.0670`, `0.0670` for $\cos^2$; `0.0341`, `0.2588` for $\cos$ | with the square both ends ease; without it the end falls fastest | shown |
| 8 | `at 46.25` | `0.4782` against `0.6915` | the square is a share, the cosine alone a multiplier | shown |
| 8 | `slope at pi/2` | `0.0000` against `-1.0000` | the square is flat at the end, the cosine alone is not | derived in [[The Cosine Wave#The consequence: drop the square]] |

> [!note]- How this was checked
> Steps 4 to 8 were run on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and matplotlib 3.10.8 from the machine's `python3`, by vault-writer, in the empty folder `~/playground/sandbox/cosine-wave-v2`, with `t6_shares.py` and `t7_wave.py` taken from the code blocks of [[The Cosine Wave]] as filed. Every output above is that run's text; steps 4 to 7 and the first run of step 8 printed the same lines as their first run that day in `~/playground/sandbox/unit-circle-figures`. The folder was removed afterwards and the clean-up check returned 2. The prepared environment `~/.vault-sandbox` is missing on this machine and was not needed.
