---
aliases: [the average of a product of independent variables, average of a product of independent variables, expectation of a product of independent variables, expected value of a product of independent variables, "E[XY] = E[X]E[Y]", "E[XY] = E[X] E[Y]", "E[g(X) h(Y)] = E[g(X)] E[h(Y)]", "E[f(X)g(Y)] = E[f(X)]E[g(Y)]", product of expectations, product of the expectations, average of a product, expectation of a product, independence factorises the average, independence factorizes the expectation, factoring the joint table]
sources:
  - "Chan, Introduction to Probability for Data Science, Michigan Publishing 2021, Definition 3.4 (expectation, PDF p. 141), Definition 5.4 (independent random variables, PDF p. 267), Definition 5.10 (joint expectation, PDF p. 273), Definition 5.12 and Theorems 5.3 and 5.4 (covariance, Cov(X, Y) = E[XY] - E[X]E[Y], and the variance of a sum, PDF p. 278), Theorem 5.5 (E[XY] = E[X]E[Y] for independent X and Y, PDF p. 279) with its proof by factoring the joint table and the line for any two functions (PDF p. 280): the vault's shelf copy, Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf; https://probability4datascience.com/"
  - "Earl L. Whitney, Math Handbook of Formulas, Processes and Tricks: Algebra and PreCalculus, version 3.5, 2022, Summation Properties (PDF p. 165): Mathematics/references/textbooks/algebra/algebra-handbook.pdf"
  - "Wikipedia, Independence (probability theory): https://en.wikipedia.org/wiki/Independence_(probability_theory), read 2026-10-21, CC BY-SA 4.0"
  - "Wikipedia, Expected value, section Properties: https://en.wikipedia.org/wiki/Expected_value, read 2026-10-21, CC BY-SA 4.0"
---

# The Average Of A Product Of Independent Variables

Up: [[Statistics]] · ⬅️ [[Scaling And Shifting A Random Variable]] · [[Moment Generating Function]] ➡️

Mathematics, Statistics. Needs: the mean of a random variable, its [expectation](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=141), read as a weighted average, and [[Variance#What variance measures|variance]] for the slip and the cross term.

> [!warning] Unfinished
> - The three drawn pictures (the form, the mechanism and the deep-dive sheet) are waiting: prompts 1 to 3 in the vault's `.prompts/The Average Of A Product Of Independent Variables.md`.
> - No quiz page for this note yet.

Claims marked stated: 0.

**When two random quantities are independent, the average of their product is the product of their averages, and the same holds for any function of one times any function of the other.** Two fair dice each average 3.5, and the product of the two faces averages $3.5 \times 3.5 = 12.25$. The reason is that independence makes every cell of the joint table a product, so the sum over the table splits into a sum over one die times a sum over the other. In symbols: $\mathbb{E}[XY] = \mathbb{E}[X]\,\mathbb{E}[Y]$, and $\mathbb{E}[g(X)\,h(Y)] = \mathbb{E}[g(X)]\,\mathbb{E}[h(Y)]$.

## Where you work

Any terminal with Python 3.6 or later (the script uses f-strings) and a new empty folder. The script uses the standard library only, so nothing is installed. The dice and the coin are made up.

## Table of contents

- [[#What independence does to the average of a product]]
- [[#When to reach for it]]
- [[#The form of the rule]]
- [[#Try it on dice yourself]]
- [[#Reading the dice output]]
- [[#How the average of a product factors]]
- [[#Other ways to get the same average]]
- [[#Why the factoring matters]]
- [[#The average of a product taught in, applied in]]

## What independence does to the average of a product

Navigation: 📋 [[#Table of contents|TOC]] | [[#When to reach for it]] ➡️

Textbook: [Introduction to probability for data science, Theorem 5.5, PDF p. 279](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=279) · [its proof and the line for any two functions, PDF p. 280](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=280). Chan prints page numbers 16 lower (PDF page 279 prints 263).

Roll two dice and write the 36 possible pairs as a 6 by 6 table, the first die down the side and the second across the top. Each cell holds the product of its two faces. Because the dice do not influence each other, every cell is equally likely, and the table has a pattern: row $x$ is $x$ times the row $1, 2, 3, 4, 5, 6$. Every row's total is $x$ times 21, so the whole table's total is $21 \times 21$. Averaging the table is averaging one die and then multiplying by the average of the other.

**Independent random variables**: $X$ and $Y$ are independent when the chance of every pair of values is the product of the two single chances, $p_{X,Y}(x, y) = p_X(x)\,p_Y(y)$ for every $x$ and $y$. *Cited:* [Chan, Definition 5.4, PDF p. 267](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=267).

**The average of a product of independent variables**, also the expectation of a product of independent variables, or "independence factorises the average": for independent $X$ and $Y$ and any functions $g$ and $h$,

$$\mathbb{E}[g(X)\,h(Y)] = \mathbb{E}[g(X)]\;\mathbb{E}[h(Y)], \qquad \text{and with } g(x) = x,\ h(y) = y: \quad \mathbb{E}[XY] = \mathbb{E}[X]\;\mathbb{E}[Y].$$

*Cited:* Chan, Theorem 5.5 and the line under its proof, which writes the functions $f$ and $g$. *Derived* in [[#How the average of a product factors]]. The left side, the average of $XY$ over the joint table, is what Chan calls the [joint expectation, Definition 5.10, PDF p. 273](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=273).

## When to reach for it

Navigation: ⬅️ [[#What independence does to the average of a product]] | 📋 [[#Table of contents|TOC]] | [[#The form of the rule]] ➡️

Whenever an average has two independent pieces multiplied inside it. Two places use it constantly. Squaring a sum $X + Y$ makes a cross term $2XY$, and the rule turns its average into $2\,\mathbb{E}[X]\,\mathbb{E}[Y]$, which is 0 when either mean is 0: that is why variances of independent quantities add. And $e^{\lambda(X + Y)} = e^{\lambda X} e^{\lambda Y}$ is a product of a function of $X$ and a function of $Y$, so the rule turns the fingerprint of a sum into a product of fingerprints, in [[Moment Generating Function#The fingerprint of a sum is the product]].

Without independence the rule fails. The same die used twice gives $\mathbb{E}[X \cdot X] = 15.166667$, not $3.5^2 = 12.25$, worked in [[#How the average of a product factors]].

## The form of the rule

Navigation: ⬅️ [[#When to reach for it]] | 📋 [[#Table of contents|TOC]] | [[#Try it on dice yourself]] ➡️

```text
if   P(X = x and Y = y) = P(X = x) * P(Y = y)   for every pair x, y         (independence)
then E[ g(X) * h(Y) ]   = E[ g(X) ] * E[ h(Y) ]   for any functions g and h
     E[ X * Y ]         = E[ X ] * E[ Y ]          the case g(x) = x, h(y) = y
```

*🖼️ Diagram wanted: the form, the 6 by 6 table of two dice with each cell x times y, every row's total written as x times 21 at its right edge, and the grand total 21 times 21. Prompt 1 in the vault's `.prompts/The Average Of A Product Of Independent Variables.md`.*

## Try it on dice yourself

Navigation: ⬅️ [[#The form of the rule]] | 📋 [[#Table of contents|TOC]] | [[#Reading the dice output]] ➡️

**1. What you need.** Python 3.6 or later:

```bash
python3 --version
```

You should see a version line. This run printed `Python 3.12.10`.

**2. When it is missing.** Install Python 3 from python.org, or run `uv python install 3.12`. Not run on this machine, which already has it.

**3. Make something to act on.** Make an empty folder and go into it:

```bash
mkdir -p ~/playground/sandbox/average-of-a-product && cd ~/playground/sandbox/average-of-a-product
```

Save this as `product_of_averages.py`. Lines 4 and 5 make a fair die (faces 1 to 6, each $1/6$) and a fair coin that lands on $-1$ or $+1$ (each $1/2$), held as exact fractions. Lines 7 and 8 are the definition of an average: each value times its probability, added up.

```python
# For independent X and Y, E[g(X) h(Y)] = E[g(X)] E[h(Y)], worked on dice and a coin and checked by listing every outcome.
from fractions import Fraction as F

die = {x: F(1, 6) for x in range(1, 7)}
coin = {-1: F(1, 2), 1: F(1, 2)}

def E(pmf, f):
    return sum(f(v) * p for v, p in pmf.items())

ex = E(die, lambda x: x)
print(f"factored: E[X] = E[Y] = {ex} = {float(ex)}, E[X] E[Y] = {ex * ex} = {float(ex * ex)}")
for x in die:
    print(f"  x = {x}: products x*y for y = 1 to 6: {[x * y for y in die]}, row adds to {sum(x * y for y in die)} = {x} x 21")
total = sum(x * y for x in die for y in die)
print(f"listed: 36 cells, each 1/36, products add to {total} = 21 x 21, E[XY] = {total}/36 = {F(total, 36)} = {float(F(total, 36)):.6f}")
eg = E(die, lambda x: x * x); eh = E(coin, lambda y: F(2) ** y)
print(f"factored: E[X^2] = {eg} = {float(eg):.6f}, E[2^Y] = (2 + 0.5)/2 = {eh} = {float(eh)}, product {eg * eh} = {float(eg * eh):.6f}")
for y in coin:
    vals = [x * x * F(2) ** y for x in die]
    print(f"  y = {y:+d}: x^2 * 2^y = {', '.join(str(float(v)) for v in vals)}, adding to {float(sum(vals))}")
listed = sum(x * x * F(2) ** y for x in die for y in coin) / 12
print(f"listed: 12 outcomes, each 1/12, E[X^2 2^Y] = 227.5/12 = {listed} = {float(listed):.6f}")
same = sum(x * x * p for x, p in die.items())
print(f"slip, Y = X: P(X = 1 and Y = 1) = 1/6, not 1/6 x 1/6 = {F(1, 36)}; E[X X] = E[X^2] = {same} = {float(same):.6f}, not {float(ex * ex)}; gap {same - ex * ex} = {float(same - ex * ex):.6f}")
sums = [x + y for x in die for y in die]
m = F(sum(sums), 36); v = sum((s - m) ** 2 for s in sums) / 36
print(f"cross term: independent dice, Var(X + Y) = {v} = {float(v):.6f} = 35/12 + 35/12, cross term 2(E[XY] - E[X]E[Y]) = {2 * (F(total, 36) - ex * ex)}")
v2 = sum((2 * x - 7) ** 2 * p for x, p in die.items())
print(f"cross term: Y = X, Var(X + X) = Var(2X) = {v2} = {float(v2):.6f}, cross term 2(E[X^2] - E[X]^2) = {2 * (same - ex * ex)}")
```

Run it:

```bash
python3 product_of_averages.py
```

You should see:

![Fifteen output lines: E[X] = E[Y] = 3.5 and their product 12.25; the six rows of the dice table, each adding to x times 21; all 36 cells adding to 441, so E[XY] = 12.25; E[X^2] = 15.166667, E[2^Y] = 1.25 and their product 18.958333; the coin's two rows adding to 45.5 and 182.0, so the listed average is 18.958333; the slip Y = X giving 15.166667 with gap 2.916667; and the variance of a sum, 35/6 with cross term 0 for independent dice and 35/3 with cross term 35/6 for the same die twice|1000](assets/average-of-a-product-dice-and-coin.png)

**4. A look before: each die on its own.** Output line 1, script lines 10 and 11: one die averages $7/2 = 3.5$ (marker 1), before any product is formed.

**5. The failure without independence.** Output line 13, script lines 23 and 24: with $Y = X$ the pair $(1, 1)$ has chance $1/6$, where independence would need $1/36$, and the average of $X \cdot X$ is $91/6 = 15.166667$ against $3.5^2 = 12.25$ (markers 13 to 15).

**6. The technique.** Output line 1 again: the product of the two averages, $49/4 = 12.25$ (marker 2), with no table built.

**7. Another way to get the same answer: list all 36 cells.** Output lines 2 to 8, script lines 12 to 15, never use the rule. Each row of products adds to $x \times 21$ (markers 3 and 4), all 36 add to $441 = 21 \times 21$ (marker 5), and $441/36 = 49/4 = 12.25$ (marker 6), the same as step 6.

**8. More worked examples on the same setup.**

*Functions of each variable: $g(X) = X^2$ for the die and $h(Y) = 2^Y$ for the coin.* Output line 9, script lines 16 and 17: the factored route gives $\mathbb{E}[X^2] = 91/6 = 15.166667$, $\mathbb{E}[2^Y] = 5/4 = 1.25$ and their product $455/24 = 18.958333$ (markers 7 to 9). Output lines 10 to 12, script lines 18 to 22, list the 12 die-and-coin outcomes: the coin's $-1$ row adds to 45.5, its $+1$ row to 182.0, and $227.5/12 = 18.958333$ (markers 10 to 12).

*The cross term in a variance.* Output lines 14 and 15, script lines 25 to 29: for two independent dice the variance of the sum from all 36 sums is $35/6 = 5.833333 = 35/12 + 35/12$, and the cross term $2(\mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y])$ is 0 (markers 16 and 17). With the same die twice, $\operatorname{Var}(2X) = 35/3 = 11.666667$ and the cross term is $35/6$ (markers 18 and 19).

Run the script again and the same fifteen lines come back: nothing in it is random.

**9. Clean up, and prove it.**

```bash
cd ~ && rm -r ~/playground/sandbox/average-of-a-product
ls ~/playground/sandbox/average-of-a-product; echo $?
```

You should see `No such file or directory`, then `2`.

## Reading the dice output

Navigation: ⬅️ [[#Try it on dice yourself]] | 📋 [[#Table of contents|TOC]] | [[#How the average of a product factors]] ➡️

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | $\mathbb{E}[X] = \mathbb{E}[Y]$ | `7/2 = 3.5` | $(1 + 2 + 3 + 4 + 5 + 6)/6 = 21/6$, one die's average | shown, and worked by hand below |
| 2 | $\mathbb{E}[X]\,\mathbb{E}[Y]$ | `49/4 = 12.25` | the right side of the rule, $3.5 \times 3.5$ | derived below |
| 3 | row $x = 1$ adds to | `21 = 1 x 21` | $1 \cdot 1 + 1 \cdot 2 + \dots + 1 \cdot 6$ | shown |
| 4 | row $x = 6$ adds to | `126 = 6 x 21` | every row is $x$ times row 1, so its total is $x$ times 21 | shown |
| 5 | all 36 products add to | `441 = 21 x 21` | $(1 + 2 + \dots + 6) \times 21$, the six row totals added | derived below |
| 6 | $\mathbb{E}[XY]$ listed | `441/36 = 49/4 = 12.250000` | the left side, from the table, with no rule used; equal to field 2 | shown |
| 7 | $\mathbb{E}[X^2]$ | `91/6 = 15.166667` | $(1 + 4 + 9 + 16 + 25 + 36)/6$ | shown |
| 8 | $\mathbb{E}[2^Y]$ | `5/4 = 1.25` | $(2^{-1} + 2^{1})/2 = (0.5 + 2)/2$ | shown |
| 9 | factored product | `455/24 = 18.958333` | field 7 times field 8 | derived below |
| 10 | coin $-1$ row adds to | `45.5` | $x^2 \times 0.5$ for $x = 1$ to 6, $= 91 \times 0.5$ | shown |
| 11 | coin $+1$ row adds to | `182.0` | $x^2 \times 2$ for $x = 1$ to 6, $= 91 \times 2$ | shown |
| 12 | listed average | `227.5/12 = 455/24 = 18.958333` | the 12 equally likely outcomes averaged; equal to field 9 | shown |
| 13 | $P(X = 1, Y = 1)$ when $Y = X$ | `1/6` | not $1/36$: the joint table is not a product, so the rule's first step fails | shown |
| 14 | $\mathbb{E}[X \cdot X]$ | `91/6 = 15.166667` | the average of a die's square, not 12.25 | shown |
| 15 | gap | `35/12 = 2.916667` | field 14 minus field 2, which is $\operatorname{Var}(X)$ | derived below |
| 16 | $\operatorname{Var}(X + Y)$, independent | `35/6 = 5.833333` | from all 36 sums; the two variances $35/12$ added | shown |
| 17 | cross term, independent | `0` | $2(\mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]) = 2(12.25 - 12.25)$ | derived below |
| 18 | $\operatorname{Var}(2X)$ | `35/3 = 11.666667` | the same die twice; four times $35/12$ | shown |
| 19 | cross term, $Y = X$ | `35/6` | $2 \times 35/12$, twice field 15 | derived below |

## How the average of a product factors

Navigation: ⬅️ [[#Reading the dice output]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to get the same average]] ➡️

Textbook: [Introduction to probability for data science, Theorem 5.5, PDF p. 279](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=279) · [the proof by factoring the joint table, and the line for any two functions, PDF p. 280](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=280).

**What it is and why it is there.** An average over two random quantities is a sum over every pair of values they can take, each pair weighted by its chance. When the two are independent, each pair's chance is a product of two single chances, and the whole sum splits into two separate sums multiplied together. That split is the step that kills the cross term when variances add, and the step that turns the fingerprint of a sum into a product of fingerprints, as in [[#When to reach for it]].

**Why it factors.** Let $X$ take values $x$ with chances $p_X(x)$ and $Y$ take values $y$ with chances $p_Y(y)$, and let $g$ and $h$ be any functions. By the definition of an average over pairs, then one step per line:

$$
\begin{aligned}
\mathbb{E}[g(X)\,h(Y)] &= \sum_x \sum_y g(x)\,h(y)\;p_{X,Y}(x, y) \\
&= \sum_x \sum_y g(x)\,h(y)\;p_X(x)\,p_Y(y) \\
&= \sum_x g(x)\,p_X(x) \Big( \sum_y h(y)\,p_Y(y) \Big) \\
&= \sum_x g(x)\,p_X(x)\;\mathbb{E}[h(Y)] \\
&= \mathbb{E}[h(Y)] \sum_x g(x)\,p_X(x) \\
&= \mathbb{E}[h(Y)]\;\mathbb{E}[g(X)]
\end{aligned}
$$

Line 2 is independence, used once, on every cell. Line 3 pulls $g(x)\,p_X(x)$ out of the inner sum, because it does not change while $y$ runs: a [constant factor comes out of a sum](../references/textbooks/algebra/algebra-handbook.pdf#page=165). Line 4 recognises the bracket as the [definition of an average](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=141) for $h(Y)$, a fixed number. Line 5 pulls that number out of the outer sum, the same move. Line 6 recognises what is left as the average of $g(X)$. *Derived;* Chan's proof on PDF p. 280 is the same lines with $g(x) = x$ and $h(y) = y$.

**A worked example: two fair dice.** Each face has chance $\tfrac16$, and every pair has chance $\tfrac16 \times \tfrac16 = \tfrac{1}{36}$. One die averages $\mathbb{E}[X] = \tfrac{1 + 2 + 3 + 4 + 5 + 6}{6} = \tfrac{21}{6} = 3.5$. The table of products, with each row's total:

| $x$ \ $y$ | 1 | 2 | 3 | 4 | 5 | 6 | row total |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 2 | 3 | 4 | 5 | 6 | $21 = 1 \times 21$ |
| 2 | 2 | 4 | 6 | 8 | 10 | 12 | $42 = 2 \times 21$ |
| 3 | 3 | 6 | 9 | 12 | 15 | 18 | $63 = 3 \times 21$ |
| 4 | 4 | 8 | 12 | 16 | 20 | 24 | $84 = 4 \times 21$ |
| 5 | 5 | 10 | 15 | 20 | 25 | 30 | $105 = 5 \times 21$ |
| 6 | 6 | 12 | 18 | 24 | 30 | 36 | $126 = 6 \times 21$ |

The six row totals add to $21 + 42 + 63 + 84 + 105 + 126 = 441$, which is $(1 + 2 + \dots + 6) \times 21 = 21 \times 21$. So

$$
\mathbb{E}[XY] = \frac{441}{36} = \frac{21}{6} \times \frac{21}{6} = 3.5 \times 3.5 = 12.25 .
$$

The middle step is line 3 of the derivation on real numbers: the 21 inside every row total is $6\,\mathbb{E}[Y]$, factored out of the row.

**A second worked example: functions of each variable.** $X$ is a fair die, $Y$ an independent fair coin landing on $-1$ or $+1$, $g(X) = X^2$ and $h(Y) = 2^Y$.

$$
\begin{aligned}
\mathbb{E}[X^2] &= \tfrac{1 + 4 + 9 + 16 + 25 + 36}{6} = \tfrac{91}{6} = 15.166667 \\
\mathbb{E}[2^Y] &= \tfrac12 \cdot 2^{-1} + \tfrac12 \cdot 2^{1} = \tfrac{0.5 + 2}{2} = 1.25 \\
\mathbb{E}[X^2]\;\mathbb{E}[2^Y] &= \tfrac{91}{6} \times \tfrac{5}{4} = \tfrac{455}{24} = 18.958333
\end{aligned}
$$

Listing the 12 outcomes, each with chance $\tfrac16 \times \tfrac12 = \tfrac{1}{12}$: with $y = -1$ the values $x^2 \cdot 0.5$ are $0.5, 2, 4.5, 8, 12.5, 18$, adding to 45.5; with $y = +1$ the values $x^2 \cdot 2$ are $2, 8, 18, 32, 50, 72$, adding to 182. The average is $\tfrac{45.5 + 182}{12} = \tfrac{227.5}{12} = 18.958333$, the same number.

**The method, to redo on new numbers.**

1. Check independence: for every pair of values, the joint chance must equal the product of the two single chances. One pair that fails is enough to stop.
2. Write the average of $g(X)\,h(Y)$ as a sum over all pairs of $g(x)\,h(y)$ times the joint chance.
3. Replace each joint chance with $p_X(x)\,p_Y(y)$.
4. Split the double sum: pull $g(x)\,p_X(x)$ out of the sum over $y$.
5. Recognise the inner sum as $\mathbb{E}[h(Y)]$, a single number, and pull it out of the sum over $x$.
6. Recognise what is left as $\mathbb{E}[g(X)]$, and multiply the two averages.

**Where it goes wrong.** The rule needs independence, and the same quantity used twice is the plainest way to lose it. Take $Y = X$, one die read twice. Step 1 fails: $P(X = 1 \text{ and } Y = 1) = \tfrac16$, since $Y$ is 1 whenever $X$ is, where a product would give $\tfrac{1}{36}$. The table has only six possible cells, on its diagonal, so

$$
\mathbb{E}[X \cdot X] = \mathbb{E}[X^2] = \tfrac{91}{6} = 15.166667, \quad \text{not} \quad \mathbb{E}[X]^2 = 3.5^2 = 12.25 .
$$

The gap is $\tfrac{91}{6} - \tfrac{49}{4} = \tfrac{182 - 147}{12} = \tfrac{35}{12} = 2.916667$, which is the die's variance, because $\mathbb{E}[XY] - \mathbb{E}[X]\,\mathbb{E}[Y]$ is the covariance and the covariance of $X$ with itself is its variance ([Chan, Definition 5.12 and Theorem 5.3, PDF p. 278](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=278)). The rule is safe only when the two pieces come from separate, unlinked draws.

The other direction does not hold either: $\mathbb{E}[XY] = \mathbb{E}[X]\,\mathbb{E}[Y]$ can be true for two quantities that are not independent, and Chan builds such a pair from one four-valued variable on PDF p. 280 (Theorem 5.6). So the rule cannot be used backwards as a test of independence. *Cited.*

**Check it.** List every outcome and average directly, with no rule. For the dice, all 36 products add to 441 and $441/36 = 12.25$, equal to $3.5 \times 3.5$. For the die and the coin, the 12 values add to 227.5 and $227.5/12 = 18.958333$, equal to $15.166667 \times 1.25$. Both are output lines 8 and 12 of `product_of_averages.py`. A third check uses the variance of a sum, which by [Chan, Theorem 5.4, PDF p. 278](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=278) is $\operatorname{Var}(X) + \operatorname{Var}(Y) + 2(\mathbb{E}[XY] - \mathbb{E}[X]\,\mathbb{E}[Y])$: from all 36 sums of two independent dice it comes out $35/6 = 35/12 + 35/12$, so the cross term is 0, and for the same die twice $\operatorname{Var}(2X) = 35/3 = 35/12 + 35/12 + 2 \times 35/12$.

*🖼️ Diagram wanted: the mechanism, the double sum over the 6 by 6 table split into a column of die chances times a row of die chances, beside the same-die table with only its diagonal lit. Prompt 2 in the vault's `.prompts/The Average Of A Product Of Independent Variables.md`.*

*🖼️ Diagram wanted: the deep-dive sheet composing the form, the mechanism, the die-and-coin example, the slip and the check. Prompt 3 in the same file.*

## Other ways to get the same average

Navigation: ⬅️ [[#How the average of a product factors]] | 📋 [[#Table of contents|TOC]] | [[#Why the factoring matters]] ➡️

- **List every outcome** and average, as step 7 of the sandbox does. Always right, independent or not, and only possible when the outcomes can be listed: two dice have 36, ten dice have 60,466,176.
- **Through the covariance**, $\mathbb{E}[XY] = \operatorname{Cov}(X, Y) + \mathbb{E}[X]\,\mathbb{E}[Y]$ (Chan, Theorem 5.3, PDF p. 278). This holds for any pair, and the rule is the case where the covariance is 0. For $Y = X$ on a die: $35/12 + 49/4 = 35/12 + 147/12 = 182/12 = 91/6$.
- **Continuous quantities**: the sums become integrals over the joint density, and independence, $f_{X,Y}(x, y) = f_X(x)\,f_Y(y)$, splits the double integral the same way (Chan, Definition 5.4 on PDF p. 267, and "the continuous can be proved similarly" on PDF p. 280).

## Why the factoring matters

Navigation: ⬅️ [[#Other ways to get the same average]] | 📋 [[#Table of contents|TOC]] | [[#The average of a product taught in, applied in]] ➡️

It is what makes the noise in a diffusion model's forward process add by variances. Two fresh noise draws are independent with mean 0, so the cross term in the square of their weighted sum averages to $2ab \times 0 \times 0 = 0$ and the variances add, as [[Sums Of Independent Gaussians#Why independence kills the cross term]] works through. A draw reused in place of a fresh one is the same-die slip above, and its cross term stays. The same factoring, with $g$ and $h$ both $e^{\lambda \cdot}$, is why the fingerprint of an independent sum is the product of fingerprints in [[Moment Generating Function#The fingerprint of a sum is the product]].

## The average of a product taught in, applied in

Navigation: ⬅️ [[#Why the factoring matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:** no learning-tree plan or chapter teaches it in full yet. Two chapters use it without deriving it: the conditional-expectation journey's [chapter 5, worked examples](/home-mscluster/mmolefe/goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/05-the-conditional-mean-is-the-best-guess.md#worked-examples), where independence makes a mixed noise term vanish, and the PoE derivation foundations' [chapter 9.1, step 4](/home-mscluster/mmolefe/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/09-the-forward-process-by-hand.md#91-independent-gaussian-noises-add-their-variances), where it kills the cross term between two noise draws.

**Needed by:** the Moment Generating Function quiz, for its questions on the fingerprint of a sum and on noises added together, listed as node N10 in [the quiz's coverage file](.quiz-prep/moment-generating-function-quiz.md).

**Applied in:** the forward-process walk of the reduce-reuse-recycle research repository (`artifacts/drips/forward-process-and-the-score/`), rung 2, independent variances add: two independent coins on $\pm 1$ give a sum whose mean square is $2 = 1 + 1$, because the cross term $2XY$ averages to $2\,\mathbb{E}[X]\,\mathbb{E}[Y] = 0$, while the same coin used twice gives 4.

> [!note]- How this was checked
> `product_of_averages.py` was run on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and the standard library only, by vault-writer, in the empty folder `~/playground/sandbox/average-of-a-product`. It was run twice and printed the same fifteen lines. The folder was removed afterwards and the clean-up check returned 2. The prepared environment `~/.vault-sandbox` is missing on this machine and was not needed. The terminal picture was rendered from the captured text by a script in DejaVu Sans Mono, never drawn, and opened before filing. The textbook pages were opened with PyMuPDF and read: Chan PDF pp. 141, 267, 273, 278, 279 and 280, and the algebra handbook PDF p. 165. The hand tables and the covariance line were computed with exact fractions. The count $6^{10} = 60{,}466{,}176$ is plain arithmetic. [Independence (probability theory)](https://en.wikipedia.org/wiki/Independence_(probability_theory)) and [Expected value](https://en.wikipedia.org/wiki/Expected_value) on Wikipedia (CC BY-SA 4.0) each answered 200 on 2026-10-21. No tldr-pages entry covers this.
