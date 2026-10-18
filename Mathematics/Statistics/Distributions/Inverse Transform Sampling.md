---
aliases: [inverse transform sampling, inverse CDF sampling, inverse-CDF sampling, inverse transform, inverse transformation method, quantile function sampling, sampling by the inverse CDF, probability integral transform, drawing from a CDF]
sources:
  - "Introduction to Probability for Data Science (Chan), section 4.8 Generating Random Numbers, Examples 4.31 and 4.32, PDF pages 248 to 251; Exercises 10 and 14, PDF pages 255 and 256"
  - "Pattern Recognition and Machine Learning (Bishop), section 11.1.1 Standard distributions, equations 11.5 to 11.7, PDF page 542; Exercise 11.2, PDF page 572"
  - "Drawing samples by hand, section 13 of volume L3 of the diffusion-models journey, Example 2 and Proof 1 (local file, path under Taught in)"
---

# Inverse Transform Sampling

Up: [[Distributions]] · [[Multivariate Normal Distribution]] ➡️

Mathematics, Statistics, Distributions. Needs: what a cumulative distribution function (CDF) is, and how to undo an exponential with a logarithm ([[Solving For The Exponent With Logarithms]]). Every number in this note is invented or computed from a formula; no real data is used.

> [!warning] Unfinished
> - The three drawn pictures (form, mechanism, deep-dive sheet) are not made, and their prompts are not written, because this filing was asked to leave pictures out. No output picture is rendered either: `~/.vault-sandbox` is missing on this machine, so there was no plotting library. To make it: `uv venv ~/.vault-sandbox` then `uv pip install --python ~/.vault-sandbox/bin/python pandas numpy scipy matplotlib statsmodels openpyxl`.
> - No quiz page covers this note yet. The Worked Examples table below has no quiz question attached to any row.
> - The `## Videos` section at the end is empty and waits for the video scout.
> - 2 claims are marked stated and keep nothing unfinished.

**Inverse transform sampling turns the random numbers every computer has (uniform between 0 and 1) into random numbers with any one-variable distribution you can write a CDF for.** Draw a uniform number $u$, find the $x$ whose CDF value is $u$, and keep that $x$. The $x$ values you collect follow the distribution.

**Where you work.** Any folder with Python 3.10 or later. Nothing is installed: the scripts use the standard library and run with `python3 -I`.

## Table of contents

- [What it is and why it is here](#what-it-is-and-why-it-is-here)
- [The proof in two lines](#the-proof-in-two-lines)
- [The method in numbered steps](#the-method-in-numbered-steps)
- [Worked example one, the exponential with rate 2](#worked-example-one-the-exponential-with-rate-2)
- [Worked example two, a Rayleigh-type case](#worked-example-two-a-rayleigh-type-case)
- [Worked example three, the discrete case](#worked-example-three-the-discrete-case)
- [Where it goes wrong](#where-it-goes-wrong)
- [Check it with 100000 draws](#check-it-with-100000-draws)
- [Problems to practise on](#problems-to-practise-on)
- [Where a product of densities comes in](#where-a-product-of-densities-comes-in)
- [Other ways](#other-ways)
- [Taught in, applied in](#taught-in-applied-in)
- [How this was checked](#how-this-was-checked)
- [Videos](#videos)

## What it is and why it is here

Navigation: 📋 [[#Table of contents]] | [[#The proof in two lines]] ➡️

In plain words: a computer can give you a number between 0 and 1 where every stretch of the same length is equally likely. You want waiting times, or sensor errors, or any other quantity that is not spread evenly. The CDF of the quantity tells you, for each value $x$, what share of draws should fall at or below $x$. That share is a number between 0 and 1. So run the CDF backwards: pick a share at random (the uniform number), and read off the value that has exactly that share of draws below it. Values that sit where the CDF climbs steeply get picked often, because a wide band of shares maps to a short stretch of $x$. Values where it climbs slowly get picked rarely.

### Inverse transform sampling

**Inverse transform sampling**, also inverse CDF sampling, the inverse transformation method, or sampling by the quantile function, draws $U$ uniform on $(0,1)$ and returns $X = F^{-1}(U)$, where $F$ is the CDF of the distribution wanted and $F^{-1}$ is its inverse, the quantile function. Backing: cited (Bishop, PDF p. 542: "we have to transform the uniformly distributed random numbers using a function which is the inverse of the indefinite integral of the desired distribution"; Chan, PDF p. 248, Example 4.31, which writes the transformation as $g(U) = F_X^{-1}(U)$).

### Probability integral transform

**The probability integral transform** is the same fact run the other way: if $X$ has a continuous, strictly increasing CDF $F$, then $F(X)$ is uniform on $(0,1)$. Backing: derived, in one line, in [[#The proof in two lines]].

**Why this matters.** Everything that simulates data starts from uniform numbers. This is the first method that turns them into a chosen distribution, and the other methods ([[#Other ways]]) are the ones to reach for when it cannot be used.

## The proof in two lines

Navigation: ⬅️ [[#What it is and why it is here]] | 📋 [[#Table of contents]] | [[#The method in numbered steps]] ➡️

Assume $F$ is continuous and strictly increasing wherever the density is positive, so $F^{-1}$ exists on $(0,1)$. Because $F$ is increasing, $F^{-1}(u) \le x$ holds exactly when $u \le F(x)$ (apply $F$ to both sides to go one way, and $F^{-1}$ to go the other). Then:

$$
P\big(F^{-1}(U) \le x\big) \;=\; P\big(U \le F(x)\big) \;=\; F(x).
$$

The first equality is the rule just stated. The second holds because a uniform $U$ on $(0,1)$ has $P(U \le t) = t$ for every $t$ between 0 and 1, and $F(x)$ is such a $t$. So the CDF of $F^{-1}(U)$ is $F$, which is what it means to have the distribution with CDF $F$. Backing: derived. Bishop sets this as Exercise 11.2 (PDF p. 572, no solution printed there) and the tutorial proves it as Proof 1.

The reverse direction: $P(F(X) \le u) = P\big(X \le F^{-1}(u)\big) = F\big(F^{-1}(u)\big) = u$, so $F(X)$ has the uniform CDF $u$ on $(0,1)$. Backing: derived.

## The method in numbered steps

Navigation: ⬅️ [[#The proof in two lines]] | 📋 [[#Table of contents]] | [[#Worked example one, the exponential with rate 2]] ➡️

Textbook: [Algebra handbook, ch. 15, converting between exponential and logarithmic forms, p. 113](../../references/textbooks/algebra/algebra-handbook.pdf#page=113)

1. **Write the CDF.** $F(x) = P(X \le x)$ as a formula in $x$. If you start from a density, integrate it from the lowest value up to $x$.
2. **Check it can be inverted.** $F$ must climb strictly from 0 to 1 with no jumps and no flat stretches. If it has jumps (a discrete variable), use the lookup in [[#Worked example three, the discrete case]].
3. **Set $u = F(x)$.**
4. **Solve for $x$.** Isolate the exponential or power, take the log or root, and keep the root that lies in the range of $x$. The result is $x = F^{-1}(u)$.
5. **Draw $u$** from a uniform generator on $(0,1)$.
6. **Compute $x = F^{-1}(u)$.** That $x$ is one draw. Repeat steps 5 and 6 for as many draws as you need.
7. **Check one draw.** Put $x$ back into $F$. You must get $u$ again, to rounding. Every table below has this column.

## Worked example one, the exponential with rate 2

Navigation: ⬅️ [[#The method in numbered steps]] | 📋 [[#Table of contents]] | [[#Worked example two, a Rayleigh-type case]] ➡️

The exponential with rate $\lambda = 2$ has CDF $F(x) = 1 - e^{-2x}$ for $x \ge 0$ (a waiting time in the units you like; the rate is 2 per unit, so there is no other unit here).

**Solve for $x$, one line at a time** (steps 3 and 4):

$$
\begin{aligned}
u &= 1 - e^{-2x} \\
1 - u &= e^{-2x} \\
\ln(1-u) &= -2x \quad \text{(take the natural log of both sides; $\ln e^{a} = a$)} \\
x &= -\tfrac{1}{2}\ln(1-u).
\end{aligned}
$$

For a general rate this reads $x = -\ln(1-u)/\lambda$, which is Chan's $g(U) = -\frac{1}{\lambda}\log(1-U)$ (PDF p. 248) and Bishop's $y = -\lambda^{-1}\ln(1-z)$ (PDF p. 542). Backing: cited, and derived above.

**One draw by hand.** $u = 0.12$. Then $1-u = 0.88$. $\ln 0.88 = -0.127833$. Negate it: $0.127833$. Halve it: $x = 0.063917$ (rounded from 0.0639167). Check: $1 - e^{-2 \times 0.063917} = 1 - e^{-0.127833} = 1 - 0.88 = 0.12$, which is $u$.

**Ten draws.** The ten fixed uniforms are 0.12, 0.85, 0.47, 0.93, 0.30, 0.66, 0.05, 0.71, 0.58, 0.24. Run `inverse_by_hand.py` ([[#Check it with 100000 draws|how to run it]]); the first block of its output is:

```text
EXPONENTIAL, rate 2: F(x) = 1 - exp(-2x), x = -ln(1 - u) / 2
 i     u   1-u   ln(1-u)  -ln(1-u)         x    F(x)
 1  0.12  0.88 -0.127833  0.127833  0.063917  0.1200
 2  0.85  0.15 -1.897120  1.897120  0.948560  0.8500
 3  0.47  0.53 -0.634878  0.634878  0.317439  0.4700
 4  0.93  0.07 -2.659260  2.659260  1.329630  0.9300
 5  0.30  0.70 -0.356675  0.356675  0.178337  0.3000
 6  0.66  0.34 -1.078810  1.078810  0.539405  0.6600
 7  0.05  0.95 -0.051293  0.051293  0.025647  0.0500
 8  0.71  0.29 -1.237874  1.237874  0.618937  0.7100
 9  0.58  0.42 -0.867501  0.867501  0.433750  0.5800
10  0.24  0.76 -0.274437  0.274437  0.137218  0.2400
```

**Reading the output.** Row 1 is the draw above.

| Field | Value in row 1 | How to read it | Backing |
|---|---|---|---|
| `u` | 0.12 | the uniform number, fixed so the table can be checked | shown |
| `1-u` | 0.88 | the share of draws above the answer | shown |
| `ln(1-u)` | −0.127833 | the natural log; negative because $1-u < 1$ | shown |
| `-ln(1-u)` | 0.127833 | the log made positive, so $x \ge 0$ | shown |
| `x` | 0.063917 | the draw: this column divided by the rate 2 | shown |
| `F(x)` | 0.1200 | the CDF put back; it must equal `u` | shown |

Every row's `F(x)` equals its `u`, so the inverse is right on all ten. The big uniforms (0.85, 0.93) give the large draws (0.948560, 1.329630) and the small ones the small draws, so $x$ rises with $u$.

**Same numbers as the tutorial.** The ten exponential draws match, to six places, the ten in Example 2 of [[#Taught in, applied in|the sampling tutorial]], which uses the same ten uniforms and the same formula. Backing: shown (the script output beside the tutorial's table, compared by eye on all ten).

## Worked example two, a Rayleigh-type case

Navigation: ⬅️ [[#Worked example one, the exponential with rate 2]] | 📋 [[#Table of contents]] | [[#Worked example three, the discrete case]] ➡️

A Rayleigh-type distribution here has CDF $F(x) = 1 - e^{-x^2/2}$ for $x \ge 0$. Same steps, with a square to undo as well:

$$
\begin{aligned}
u &= 1 - e^{-x^2/2} \\
1 - u &= e^{-x^2/2} \\
\ln(1-u) &= -x^2/2 \\
x^2 &= -2\ln(1-u) \\
x &= \sqrt{-2\ln(1-u)}.
\end{aligned}
$$

The last line keeps the positive root, because $x \ge 0$ on this distribution. The ten draws, from the second block of the same output:

```text
RAYLEIGH TYPE: F(x) = 1 - exp(-x^2 / 2), x = sqrt(-2 ln(1 - u))
 i     u   1-u   ln(1-u)  -2ln(1-u)         x    F(x)
 1  0.12  0.88 -0.127833   0.255667  0.505635  0.1200
 2  0.85  0.15 -1.897120   3.794240  1.947881  0.8500
 3  0.47  0.53 -0.634878   1.269757  1.126835  0.4700
 4  0.93  0.07 -2.659260   5.318520  2.306192  0.9300
 5  0.30  0.70 -0.356675   0.713350  0.844600  0.3000
 6  0.66  0.34 -1.078810   2.157619  1.468884  0.6600
 7  0.05  0.95 -0.051293   0.102587  0.320291  0.0500
 8  0.71  0.29 -1.237874   2.475749  1.573451  0.7100
 9  0.58  0.42 -0.867501   1.735001  1.317194  0.5800
10  0.24  0.76 -0.274437   0.548874  0.740860  0.2400
```

The columns read as in example one, except `-2ln(1-u)` is the quantity under the square root. Row 1: $\ln 0.88 = -0.127833$, times $-2$ is $0.255667$, and its square root is $0.505635$. Check: $1 - e^{-0.505635^2/2} = 1 - e^{-0.127833} = 0.12$.

**The scale matters.** Chan's Exercise 10 (PDF p. 255) has density $2xe^{-x^2}$, whose CDF is $1 - e^{-x^2}$ (integrate $2te^{-t^2}$ from 0 to $x$). Its inverse is $\sqrt{-\ln(1-u)}$, without the 2. The two cases differ only in scale. Backing: derived.

## Worked example three, the discrete case

Navigation: ⬅️ [[#Worked example two, a Rayleigh-type case]] | 📋 [[#Table of contents]] | [[#Where it goes wrong]] ➡️

A discrete variable has a CDF that jumps, so there is no $x$ with $F(x) = u$ for most $u$. The lookup that replaces the inverse: **the draw is the smallest value whose cumulative probability is at least $u$.** Chan's Example 4.32 (PDF pp. 249 to 251) draws the integers 1, 2, 3, 4 with probabilities 0.1, 0.5, 0.3, 0.1.

**Step 1, cumulative sums.** $0.1$; $0.1 + 0.5 = 0.6$; $0.6 + 0.3 = 0.9$; $0.9 + 0.1 = 1.0$. In tenths these are 1, 6, 9, 10.

**Step 2, intervals of $u$.** Value 1 owns $0 \le u \le 0.1$, value 2 owns $0.1 < u \le 0.6$, value 3 owns $0.6 < u \le 0.9$, value 4 owns $0.9 < u \le 1$. These are the intervals in Chan's $g(U)$ on PDF p. 250. Each interval's length is the probability of its value, which is why the value comes up with that probability.

**Step 3, look up each $u$.** $u = 0.12$: 0.12 is above 0.1, so not value 1; it is at most 0.6, so the draw is 2. The script's third block does this for all ten:

```text
DISCRETE: values 1,2,3,4 with probabilities 0.1, 0.5, 0.3, 0.1
cumulative sums in tenths: [1, 6, 9, 10]  as probabilities: [0.1, 0.6, 0.9, 1.0]
 i     u  u in tenths  first cumulative >= u  value
 1  0.12          1.2                    0.6      2
 2  0.85          8.5                    0.9      3
 3  0.47          4.7                    0.6      2
 4  0.93          9.3                    1.0      4
 5  0.30          3.0                    0.6      2
 6  0.66          6.6                    0.9      3
 7  0.05          0.5                    0.1      1
 8  0.71          7.1                    0.9      3
 9  0.58          5.8                    0.6      2
10  0.24          2.4                    0.6      2
```

The ten draws are 2, 3, 2, 4, 2, 3, 1, 3, 2, 2: one 1, five 2s, three 3s and one 4, which happens to be exactly 10 times the probabilities. That is luck of these ten uniforms, not something the method guarantees; the 100000-draw run below shows the real spread.

## Where it goes wrong

Navigation: ⬅️ [[#Worked example three, the discrete case]] | 📋 [[#Table of contents]] | [[#Check it with 100000 draws]] ➡️

### Using u in place of 1 - u

**The swap changes which $x$ goes with which $u$ and leaves the distribution alone.** With $x' = -\ln(u)/2$ in place of $x = -\ln(1-u)/2$: $1-U$ is also uniform on $(0,1)$, so $x'$ is a valid exponential draw with rate 2. What changes is the pairing, and it changes exactly: $x'(u) = x(1-u)$ for every $u$. The correct rule rises with $u$; the swapped rule falls with $u$. The fourth block of the output shows both for the ten uniforms:

```text
FAILURE 1: u in place of 1 - u (exponential rate 2)
 i     u  x with 1-u  x with u   x with u == x(1-u)
 1  0.12    0.063917  1.060132             1.060132
 2  0.85    0.948560  0.081259             0.081259
 3  0.47    0.317439  0.377511             0.377511
 4  0.93    1.329630  0.036285             0.036285
 5  0.30    0.178337  0.601986             0.601986
 6  0.66    0.539405  0.207758             0.207758
 7  0.05    0.025647  1.497866             1.497866
 8  0.71    0.618937  0.171245             0.171245
 9  0.58    0.433750  0.272364             0.272364
10  0.24    0.137218  0.713558             0.713558
draws ranked smallest to largest, by position i, with 1-u: [7, 1, 10, 5, 3, 9, 6, 8, 2, 4]
draws ranked smallest to largest, by position i, with u:   [4, 2, 8, 6, 9, 3, 5, 10, 1, 7]
```

Row 1: $u = 0.12$ gives 0.063917 with $1-u$ and 1.060132 with $u$, and 1.060132 is the first rule at $0.88$. The rank order is exactly reversed (position 4 is the largest draw under the correct rule and the smallest under the swap). In the 100000-draw run, 0 of 100000 draws are the same under the two rules, and the covariance of the two lists is −0.1608 against a variance of about 0.25, a correlation near −0.64. So the swap is harmless when only the distribution of the draws matters, and it is wrong when a table must reproduce a given list (the tutorial's ten rows), or when two samplers are fed the same $u$ and one uses each rule, since they then move in opposite directions. Backing: shown and derived.

A second, rarer difference: Python's `random.random()` returns numbers in $0 \le X < 1$, so $u = 0$ can occur and $\ln 0$ is undefined, while $1 - u$ is never 0. Backing: stated (from the language reference; not fetched here).

### A CDF with no closed-form inverse

**The Gaussian CDF has no formula you can solve for $x$**, so step 4 of the method cannot be done by hand. The inverse still exists, and a library computes it by a numerical routine: the standard library's `NormalDist().inv_cdf`. The script's first Gaussian block:

```text
GAUSSIAN: F has no closed-form inverse; NormalDist().inv_cdf finds it numerically
inv_cdf(0.975) = 1.959964   cdf of that = 0.975000
posterior N(8/3, (2/3)^2): ten draws from the ten fixed uniforms
 i     u  z = inv_cdf(u)  x = 8/3 + 2/3 z  inv_cdf on N(8/3,2/3)
 1  0.12       -1.174987         1.883342               1.883342
 2  0.85        1.036433         3.357622               3.357622
 3  0.47       -0.075270         2.616487               2.616487
 4  0.93        1.475791         3.650527               3.650527
 5  0.30       -0.524401         2.317066               2.317066
 6  0.66        0.412463         2.941642               2.941642
 7  0.05       -1.644854         1.570098               1.570098
 8  0.71        0.553385         3.035590               3.035590
 9  0.58        0.201893         2.801262               2.801262
10  0.24       -0.706303         2.195798               2.195798
by bisection on the CDF: x = 1.959964 after 45 halvings of [-10, 10]
```

`inv_cdf(0.975)` gives 1.959964, and putting that back through the CDF gives 0.975000. A plain halving search on the CDF reaches the same 1.959964 after 45 halvings of the interval from −10 to 10, so the number is findable without the library, at the cost of about 45 CDF evaluations per draw. For the two-sensor posterior in the tutorial, $x = 8/3 + (2/3)z$ with $z$ the standard normal quantile; row 1 gives $z = -1.174987$ and $x = 1.883342$, and all ten match the tutorial's posterior column. Chan uses the same route in Python, `sigma*stats.norm.ppf(U)+mu` (PDF p. 248, top). The library's inner method is not shown here. Backing: shown (the run), cited (Chan).

When no quantile routine exists either, the choices are a numerical search per draw, or a different sampler ([[#Other ways]]).

### Cumulative sums in floating point

**A cumulative sum of probabilities can miss its own target by the last digit.** The fifth block:

```text
FAILURE 2: float cumulative sums at a jump (u = 0.9 exactly)
float cumulative sums: [0.1, 0.6, 0.8999999999999999, 0.9999999999999999]
value for u = 0.9 with float sums:    4
value for u = 0.9 with integer tenths: 3
```

The third float sum is 0.8999999999999999, below 0.9, so $u = 0.9$ falls into value 4 when the table says value 3. Summing in whole tenths (1, 6, 9, 10) gives 3. Only a $u$ landing exactly on a boundary shows it. Backing: shown.

## Check it with 100000 draws

Navigation: ⬅️ [[#Where it goes wrong]] | 📋 [[#Table of contents]] | [[#Problems to practise on]] ➡️

**What you need:** Python 3.10 or later (`python3 --version`). If it is missing, install it from python.org. The scripts are in `sandbox/` beside this note: [inverse_by_hand.py](sandbox/inverse_by_hand.py), [inverse_gaussian_and_product.py](sandbox/inverse_gaussian_and_product.py), [inverse_check_100000.py](sandbox/inverse_check_100000.py). Copy them into an empty folder and run each from there. They write nothing.

```bash
python3 -I inverse_by_hand.py
python3 -I inverse_gaussian_and_product.py
python3 -I inverse_check_100000.py
```

The full outputs are saved beside this note: [inverse_by_hand-output.txt](assets/inverse_by_hand-output.txt), [inverse_gaussian_and_product-output.txt](assets/inverse_gaussian_and_product-output.txt), [inverse_check_100000-output.txt](assets/inverse_check_100000-output.txt).

**The check.** `inverse_check_100000.py` draws 100000 uniforms with `random.Random(20261018)`, runs them through the three samplers, and compares each statistic with the exact value from the CDF. The `gap/SE` column is the gap divided by the standard error that the exact distribution predicts for 100000 draws (for the mean, the exact standard deviation over $\sqrt{100000}$; for a fraction, $\sqrt{p(1-p)/100000}$).

```text
seed 20261018, N = 100000, first three uniforms: 0.856774 0.200892 0.780947

EXPONENTIAL rate 2: mean exact 1/2, sd exact 1/2, P(X < 0.5) exact 1 - exp(-1)
mean                                         sample 0.498471  exact 0.500000  gap -0.001529  gap/SE -0.97
fraction below 0.5                           sample 0.631530  exact 0.632121  gap -0.000591  gap/SE -0.39

RAYLEIGH type: mean exact sqrt(pi/2), P(X < 1) exact 1 - exp(-1/2)
mean                                         sample 1.251703  exact 1.253314  gap -0.001611  gap/SE -0.78
fraction below 1                             sample 0.394180  exact 0.393469  gap +0.000711  gap/SE +0.46

DISCRETE 1,2,3,4 with 0.1, 0.5, 0.3, 0.1
fraction equal to 1                          sample 0.100500  exact 0.100000  gap +0.000500  gap/SE +0.53
fraction equal to 2                          sample 0.499330  exact 0.500000  gap -0.000670  gap/SE -0.42
fraction equal to 3                          sample 0.302330  exact 0.300000  gap +0.002330  gap/SE +1.61
fraction equal to 4                          sample 0.097840  exact 0.100000  gap -0.002160  gap/SE -2.28

u IN PLACE OF 1 - u (exponential rate 2), same uniforms
mean                                         sample 0.500717  exact 0.500000  gap +0.000717  gap/SE +0.45
fraction below 0.5                           sample 0.631790  exact 0.632121  gap -0.000331  gap/SE -0.22
draws identical between the two rules: 0 of 100000
covariance of the two lists of draws: -0.1608 (negative: a big draw in one is a small draw in the other)

A LINE FROM Selective Evaluation: c = 0.5 + 0.5 * random() ** 0.5
Solving u = F(c) for c = 0.5 + 0.5 * sqrt(u) gives F(c) = 4 * (c - 0.5)**2 on 0.5 <= c <= 1
fraction of c below 0.75                     sample 0.250940  exact 0.250000  gap +0.000940  gap/SE +0.69
mean of c (exact 0.5 + 0.5 * 2/3)            sample 0.833156  exact 0.833333  gap -0.000177  gap/SE -0.47
```

**Reading it.** The exponential mean is 0.498471 against the exact $1/\lambda = 0.5$, a gap of −0.97 standard errors. The fraction below 0.5 is 0.631530 against the exact $1 - e^{-1} = 0.632121$ (the CDF at 0.5). The Rayleigh mean is 1.251703 against $\sqrt{\pi/2} = 1.253314$, and its fraction below 1 is 0.394180 against $1 - e^{-1/2} = 0.393469$. The discrete fractions sit within 0.0024 of 0.1, 0.5, 0.3 and 0.1.

**Is a gap of −2.28 standard errors a problem?** It is the fraction equal to 4 (0.097840 against 0.1). A single comparison that far out has chance 0.0226 under the exact distribution. Across the 12 comparisons in this run the chance that at least one reaches 2.28 is $1 - (1-0.0226)^{12} = 0.24$, so one such gap is ordinary. Backing: derived (the two arithmetic steps), with the 12 comparisons counted from the output. The comparisons are not fully independent because they reuse the same uniforms, so 0.24 is approximate (stated).

**The last two lines of the output** apply the method to a line from [[Selective Evaluation]]: `c = 0.5 + 0.5 * rnd.random() ** 0.5`. Solving $u = F(c)$ for $c = 0.5 + 0.5\sqrt{u}$ gives $F(c) = 4(c-0.5)^2$ on $0.5 \le c \le 1$, so that line draws from a density that rises linearly from 0 at $c = 0.5$ to 4 at $c = 1$. The run gives 0.250940 of the draws below 0.75 against $4 \times 0.25^2 = 0.25$ from the CDF.

**Clean-up.** Delete the empty folder; `ls` on its parent shows nothing of it.

## Problems to practise on

Navigation: ⬅️ [[#Check it with 100000 draws]] | 📋 [[#Table of contents]] | [[#Where a product of densities comes in]] ➡️

<!-- worked-examples-table: inverse-cdf-sampling rev=2 -->
Problems on turning uniform draws into samples by inverting a CDF, from the easiest to the hardest:

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | Turn uniform draws into exponential draws: solve F(x) = 1 − e^(−λx) for x, giving x = −(1/λ) ln(1 − u) | Worked example, with a Python listing | [[introduction-to-probability-for-data-science.pdf#page=248\|Chan, Example 4.31, PDF p. 248]] | Easy | In the book, PDF pp. 248 to 249: the CDF, the inverse, the histograms and the NumPy line | none: serves the product-of-experts sampling quiz |
| 2 | The same exponential with rate 2, then the two-sensor Gaussian posterior through the normal quantile function, on ten fixed uniforms, with a ten-row table to check against | Tutorial | [the sampling tutorial, Example 2](/Users/molefemolefe/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/13-drawing-samples-by-hand.md#worked-examples) | Easy | In the tutorial: five numbered steps, the ten-row table and a checking script, `verify_s13.py`, in the same folder | none: serves the product-of-experts sampling quiz |
| 3 | Draw the integers 1 to 4 with probabilities 0.1, 0.5, 0.3, 0.1: the CDF has jumps and no inverse, so the draw is read off which interval of [0, 1] the uniform falls in | Worked example, with a Python listing | [[introduction-to-probability-for-data-science.pdf#page=249\|Chan, Example 4.32, PDF pp. 249 to 251]] | Medium | In the book, PDF pp. 249 to 251: the interval table, the mapping figure and the `np.logical_and` code | none: serves the product-of-experts sampling quiz |
| 4 | Show that y = h⁻¹(z) has density p(y) when z is uniform on (0, 1) and h is the integral of p, which is why the method works | Exercise without one | [[pattern-recognition-and-machine-learning.pdf#page=572\|Bishop, Exercise 11.2, PDF p. 572]] | Medium | none: to be written. The setup is the text on PDF p. 542 (equations 11.5 and 11.6) | none: serves the product-of-experts sampling quiz |
| 5 | Find the transformation that makes a uniform variable Cauchy with density 1/(π(1 + y²)), and then check that y = b tan z + c is Cauchy | Exercise without one | [[pattern-recognition-and-machine-learning.pdf#page=572\|Bishop, Exercises 11.3 and 11.7, PDF p. 572]] | Medium | none: to be written. The Cauchy density is equation 11.8 on PDF p. 543 | none: serves the product-of-experts sampling quiz |
| 6 | A variable on [0, 1] has CDF x^α. Find the CDF of Y = −ln X, which is exponential with rate α, and with α = 1 is the exponential sampler run from a uniform | Exercise without one | [[introduction-to-probability-for-data-science.pdf#page=255\|Chan, Exercise 14, PDF pp. 255 to 256]] | Medium | none: to be written | none: serves the product-of-experts sampling quiz |
| 7 | A variable has density 2x e^(−x²) for x ≥ 0 (a Rayleigh density). Find the density of Y = 1 − e^(−X²), which is F(X) and comes out uniform. Reading the map backwards gives the Rayleigh sampler x = √(−ln(1 − u)) | Exercise without one | [[introduction-to-probability-for-data-science.pdf#page=255\|Chan, Exercise 10, PDF p. 255]] | Medium | none: to be written. The exercise stops at the density of Y; the sampler is the step to add | none: serves the product-of-experts sampling quiz |
| 8 | Sample from the piecewise exponential density q(z) = k_i λ_i exp(−λ_i (z − z_(i−1))) on z_(i−1) < z ≤ z_i: choose a piece by its mass, then invert the exponential inside it | Exercise without one | [[pattern-recognition-and-machine-learning.pdf#page=572\|Bishop, Exercise 11.9, PDF p. 572]] | Hard | none: to be written. The density is equation 11.17 on PDF p. 547; Exercise 11.8 on the same page gives the coefficients k_i | none: serves the product-of-experts sampling quiz |

No row asks the reader to write a sampler as a programming exercise: the books give code listings (rows 1 and 3) and the tutorial gives a checking script (row 2), and the exercises ask for derivations. No row inverts a CDF that has no closed form by a numerical search; the tutorial names that case in one line without working it. Mathematics for Machine Learning states the probability integral transform (Theorem 6.15, PDF p. 222) without a proof or an exercise, and the Murphy book is listed on the [[Textbooks]] shelf but its PDF is not on disk, so it was not searched.
Read in full: Chan PDF pp. 245 to 251 and 253 to 256, Bishop PDF pp. 542 to 545, 547 and 572 to 573, the tutorial's Example 2, and Mathematics for Machine Learning PDF pp. 221 to 223. Only found: the one-line mentions in the Goodfellow deep learning book (PDF p. 710) and in Understanding Deep Learning (appendix C.4, PDF p. 473), which are statements and not problems. Bishop's solutions manual is not on the shelf.
<!-- /worked-examples-table -->

## Where a product of densities comes in

Navigation: ⬅️ [[#Problems to practise on]] | 📋 [[#Table of contents]] | [[#Other ways]] ➡️

A product of experts multiplies the densities of several experts. Multiplying densities gives a function that is not a density, so it has no CDF until it is divided by its own area. **This method needs a CDF that ends at 1, and a product of densities does not end at 1 until it is normalised.** The second script shows the size of the gap for $N(0,1)$ times $N(1,1)$:

```text
A PRODUCT OF TWO DENSITIES: N(0, 1) times N(1, 1)
area under the product (trapezoids, 8000 strips): 0.219696
exact area, the N(0, 2) density at 1:           0.219696
largest value of the running sum if used as a CDF: 0.219696  (a CDF must end at 1)
after dividing by the area, the sum ends at: 1.000000
100000 draws, seed 7: mean 0.4973 (exact 0.5), variance 0.4990 (exact 0.5)
```

The area under the product is 0.219696, which equals the $N(0,2)$ density at 1 ([[The Area A Product Loses]] gives this area as a normal density of the difference of the two means, with the two variances added). The running sum of the product stops at 0.219696, so a uniform $u$ above that value would find no $x$. After dividing by the area the running sum ends at 1.000000, and the method applies as before, with the CDF built on a grid and inverted by lookup: 100000 draws gave mean 0.4973 and variance 0.4990 against the exact 0.5 and 0.5. Backing: shown (the run); the exact 0.5 and 0.5 are derived from the precision rule in [[Products And Quotients Of Diagonal Gaussians]].

**What this does not cover.** The sources read here (Chan PDF pp. 247 to 251, Bishop PDF p. 542) draw one variable at a time and say nothing about products of densities. The grid route above works for one coordinate. The tutorial states that high-dimensional diffusion targets "generally offer neither a convenient joint inverse CDF nor an affordable global envelope" (section 13, "The diffusion connection"), which is why sampling a full product takes more than this method. Backing: cited (the tutorial).

**Why this matters.** The normalising area is the reason the sampling section of a product-of-experts write-up cannot stop at "invert the CDF". The area is the first thing to compute, and where it cannot be computed the samplers in [[#Other ways]] take over.

## Other ways

Navigation: ⬅️ [[#Where a product of densities comes in]] | 📋 [[#Table of contents]] | [[#Taught in, applied in]] ➡️

**Equal probabilities are the discrete case with every share the same.** Step 3 of [[Bootstrap#The method in numbered steps]] picks a unit number from 1 to $n$ at random. With every probability $1/n$ the cumulative sums are $1/n, 2/n, \dots, 1$, and the smallest one at least $u$ is the unit number $\lceil nu \rceil$ (for $u > 0$). Backing: derived.

**A guaranteed bound on a rate** is a different job from drawing numbers: [[Selective Evaluation]] uses a line like the one above to invent a confidence for each row, and its bound comes from a calibration set.

**Accept-reject** draws from a proposal and keeps some of the draws, using the density and no inverse. The tutorial's section 13 works it on a two-place mixture whose CDF has no closed-form inverse.

**A chain** (Metropolis-Hastings, Langevin) gives samples when neither an inverse nor an envelope is affordable: see [[Markov Chain Monte Carlo]].

**Drawing a Gaussian from standard normal draws** by shifting and scaling is a separate, cheaper route when the target is Gaussian: [[Sampling A Diagonal Gaussian]].

**Seeded generators** supply the uniform numbers: [[Random Numbers From A Seeded Generator]].

## Taught in, applied in

Navigation: ⬅️ [[#Other ways]] | 📋 [[#Table of contents]] | [[#How this was checked]] ➡️

**Taught in.**

- [Drawing samples by hand, section 13 of volume L3](/Users/molefemolefe/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/13-drawing-samples-by-hand.md#worked-examples), Example 2: the exponential with rate 2 and the two-sensor posterior from ten fixed uniforms, and Proof 1, the inverse transform proof. Its numbers match the tables here (all ten exponential draws and all ten posterior draws).
- [[Worked Examples#Sampling from a distribution by the inverse CDF|The worked-examples index]]: eight problems from Chan, Bishop and the tutorial, listed above.

**Applied in.** None yet.

## How this was checked

Navigation: ⬅️ [[#Taught in, applied in]] | 📋 [[#Table of contents]] | [[#Videos]] ➡️

> [!note]- How this was checked
> The three scripts were run on 2026-10-18 on a Mac with Python 3.12 (standard library only) using `python3 -I`, each from an empty folder that was removed afterwards, which the clean-up check (the folder gone from its parent) confirmed. Seeds: 20261018 for the 100000 draws, 7 for the product draws; the first two scripts use fixed uniforms. Each script ran in under a tenth of a second. The textbook pages were read with PyMuPDF: Chan PDF pp. 247 to 251 and 255 to 256 (Examples 4.31 and 4.32, Exercises 10 and 14) and Bishop PDF pp. 542, 547 and 572 (equations 11.5 to 11.7, Exercise 11.2 and equation 11.17). Bishop p. 547 is read but not cited in the text: it holds the piecewise exponential density behind Exercise 11.9 in the table above, and nothing else here. The tutorial's ten exponential draws and ten posterior draws were compared with the script output; they agree to six places. `~/.vault-sandbox` does not exist on this machine. The note has not been rendered in Obsidian.
>
> Claims marked stated, 2: that `random.random()` can return 0; that the 0.24 chance is approximate because the comparisons reuse the same uniforms.

## Videos

<!-- video-table: inverse-transform-exponential-example rev=1 -->
Susu Zhang, then Marcus Pendergrass, both from the open web, on turning uniform random numbers into exponential ones with the inverse CDF, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | From the exponential density to its CDF 1 - e^(-λx), set equal to u, and solved for x = -(1/λ) ln(1 - u) | Worked example, open web | [Susu Zhang, Lec1 2 2 Example Exp, 0:06 to 4:22](https://www.youtube.com/watch?v=joBKfHH5bwc&t=6s) |
| 2 | The inverse as an R function, 1000 uniform draws, the transform with λ = 1, and a histogram laid over the exponential density | Code walk, open web | [Susu Zhang, Lec1 2 2 Example Exp, 4:22 to 10:22](https://www.youtube.com/watch?v=joBKfHH5bwc&t=262s) |
| 3 | 10,000 uniforms in Desmos, -ln(1 - u) for λ = 1, then multiplied by 2 to get λ = 1/2 | Worked example, open web | [Marcus Pendergrass, Using The Inverse CDF Method to Simulate Random Variables, 3:24 to 6:36](https://www.youtube.com/watch?v=xf-ltpf7rwQ&t=204s) |

Both work by simulating many draws and comparing to the density; neither turns two or three specific uniform numbers into exponential values by hand, and neither proves the transformed draws have the target CDF. Pendergrass cites the two facts he uses to his own course notes. The ritvikmath block above covers the CDF and the inverse. Mahesh Huddar's channel has no video on it. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->
