---
aliases: [scaling and shifting a random variable, shifting and scaling a random variable, shifting a random variable, shift property of variance, DC shift, "Var(X + c) = Var(X)", variance of aX + b, "Var(aX + b) = a^2 Var(X)", mean of aX + b, "E[aX + b] = aE[X] + b", "sd(aX + b) = |a| sd(X)", linearity of expectation, affine transformation of a random variable]
sources:
  - "Chan, Introduction to Probability for Data Science, Michigan Publishing 2021, Definition 3.4 (expectation), Theorem 3.4 (scale and DC shift of the expectation) and Theorem 3.5 (scale and DC shift of the variance) with its proof: the vault's shelf copy, Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf, PDF pages 141, 147, 151 and 152; https://probability4datascience.com/"
  - "The conditional-expectation journey, chapter 1, Example 1 (the fair die's mean 3.5 and variance 35/12): /home/molef/goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/01-expectation-and-the-best-constant-guess.md"
  - "Wikipedia, Variance, section Properties: https://en.wikipedia.org/wiki/Variance, read 2026-10-20, CC BY-SA 4.0"
  - "Wikipedia, Expected value, section Properties: https://en.wikipedia.org/wiki/Expected_value, read 2026-10-20, CC BY-SA 4.0"
---

# Scaling And Shifting A Random Variable

Up: [[Statistics]] · ⬅️ [[Running The Scaling Rule For Variance]] · [[The Average Of A Product Of Independent Variables]] ➡️

Mathematics, Statistics. Needs: the mean of a random variable, its [expectation](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=141), read as a weighted average, and [[Variance#What variance measures|variance]], the average squared distance from the mean.

> [!question] Test yourself
> No quiz page covers this note yet.

> [!warning] Unfinished
> - The three drawn pictures (the form, the mechanism and the deep-dive sheet) are waiting: prompts 1 to 3 in the vault's `.prompts/Scaling And Shifting A Random Variable.md`.
> - No quiz page for this note yet.

Claims marked stated: 0.

**Multiply every value of a random quantity by a fixed number and add a fixed number, and its mean goes through the same multiply and add, while its spread only feels the multiply.** Variance averages the squared distances from the mean. Multiplying by $a$ multiplies every distance by $a$, so every squared distance by $a^2$. Adding $b$ moves every value and the mean by the same amount, so no distance changes. In symbols, for $Y = aX + b$: $\mathbb{E}[Y] = a\,\mathbb{E}[X] + b$, $\operatorname{Var}(Y) = a^2 \operatorname{Var}(X)$ and $\operatorname{sd}(Y) = |a|\operatorname{sd}(X)$.

## Where you work

Any terminal with Python 3.6 or later (the script uses f-strings) and a new empty folder. The script uses the standard library only, so nothing is installed. The die is made up; the one schedule number comes from a public cosine noise schedule.

## Table of contents

- [[#What scaling and shifting do]]
- [[#When to reach for it]]
- [[#The form of the rule]]
- [[#Try scaling and shifting yourself]]
- [[#Reading the die output]]
- [[#How scaling and shifting work]]
- [[#Where the rule goes wrong]]
- [[#Other ways to get the same numbers]]
- [[#Why the rule matters]]
- [[#Scaling and shifting taught in, applied in]]

## What scaling and shifting do

Navigation: 📋 [[#Table of contents|TOC]] | [[#When to reach for it]] ➡️

Textbook: [Introduction to probability for data science, Theorem 3.5 (ii) scale and (iii) DC shift, PDF p. 151](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=151) · [its proof, PDF p. 152](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=152) · [the same two properties for the mean, Theorem 3.4 (iii) and (iv), PDF p. 147](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=147). The book prints page numbers 16 lower (PDF page 151 prints 135).

Picture a die's six faces as dots on a number line, with the mean as a balance point between them. Doubling every face pushes each dot twice as far from the balance point, and the balance point doubles with them. Adding 1 to every face slides all six dots and the balance point one step right together, so every dot keeps its distance. Variance only ever looks at those distances, squared and averaged, so the doubling reaches it as a factor of 4 and the slide never reaches it.

**Scaling and shifting a random variable**, also the affine transformation $Y = aX + b$: $a$ is the scale (any fixed number, sign included) and $b$ is the shift. Its mean is $\mathbb{E}[aX + b] = a\,\mathbb{E}[X] + b$, its variance $\operatorname{Var}(aX + b) = a^2 \operatorname{Var}(X)$ and its standard deviation $\operatorname{sd}(aX + b) = |a| \operatorname{sd}(X)$. *Cited:* Theorems 3.4 and 3.5. *Derived* in [[#How scaling and shifting work]].

**Linearity of expectation**, here in its one-variable form $\mathbb{E}[aX + b] = a\,\mathbb{E}[X] + b$: a fixed multiplier comes out of an average, and a fixed number added to every value is added to the average. Its two-variable form, $\mathbb{E}[aX + bY] = a\,\mathbb{E}[X] + b\,\mathbb{E}[Y]$, is what [[Sums Of Independent Gaussians#How the rule works]] uses.

**Shift property of variance**, also the DC shift, $\operatorname{Var}(X + c) = \operatorname{Var}(X)$: adding a fixed number leaves the variance alone. The scale half of the rule, $\operatorname{Var}(cX) = c^2 \operatorname{Var}(X)$, has its own sandbox in [[Variance#Scaling a draw scales its variance by the square]].

## When to reach for it

Navigation: ⬅️ [[#What scaling and shifting do]] | 📋 [[#Table of contents|TOC]] | [[#The form of the rule]] ➡️

Whenever a formula multiplies a random quantity by a number and adds another number, and you need the mean and spread of what comes out. Sampling a Gaussian computes $m + s\,\varepsilon$ ([[Sampling A Diagonal Gaussian#How sampling works]]). The forward process, for a fixed clean point $x_0$, computes $\sqrt{1 - \bar\alpha_t}\,\varepsilon + \sqrt{\bar\alpha_t}\,x_0$ ([[The Forward Process#How the jump works]]). Converting units, such as degrees Celsius to Fahrenheit, $F = 1.8\,C + 32$, is the same rule.

Without it there are two slips, worked with their numbers in [[#Where the rule goes wrong]]: scaling the variance by $a$ instead of $a^2$, and letting the shift $b$ leak into the variance.

## The form of the rule

Navigation: ⬅️ [[#When to reach for it]] | 📋 [[#Table of contents|TOC]] | [[#Try scaling and shifting yourself]] ➡️

```text
Y = a * X + b                  a and b are fixed numbers, X a random quantity
E[Y]   = a * E[X] + b          the mean is scaled and shifted
Var(Y) = a**2 * Var(X)         the variance is scaled by a squared; b drops out
sd(Y)  = abs(a) * sd(X)        the standard deviation is scaled by |a|; b drops out
```

*🖼️ Diagram wanted: the form, the die's six stems scaled by 2 and slid by 1, its mean following both steps and its spread following only the first. Prompt 1 in the vault's `.prompts/Scaling And Shifting A Random Variable.md`.*

## Try scaling and shifting yourself

Navigation: ⬅️ [[#The form of the rule]] | 📋 [[#Table of contents|TOC]] | [[#Reading the die output]] ➡️

**1. What you need.** Python 3.6 or later:

```bash
python3 --version
```

You should see a version line. This run printed `Python 3.12.10`.

**2. When it is missing.** Install Python 3 from python.org, or run `uv python install 3.12`. Not run on this machine, which already has it. Where the prepared environment exists, `~/.vault-sandbox/bin/python` runs the script unchanged.

**3. Make something to act on.** Make an empty folder and go into it:

```bash
mkdir -p ~/playground/sandbox/scale-and-shift && cd ~/playground/sandbox/scale-and-shift
```

Save this as `scale_shift.py`. Line 4 makes the fair die: faces 1 to 6, each with probability one sixth, held as exact fractions so $35/12$ prints as a fraction.

```python
# The mean and variance of Y = aX + b, worked on a fair die and checked face by face.
from fractions import Fraction as F

faces = range(1, 7); p = F(1, 6)
mean = sum(p * x for x in faces); var = sum(p * (x - mean) ** 2 for x in faces)
print(f"X: mean {float(mean)}, variance {var} = {float(var):.4f}")
a, b = 2, 1
ys = [a * x + b for x in faces]
my = sum(p * y for y in ys); vy = sum(p * (y - my) ** 2 for y in ys)
print(f"Y = 2X + 1 face by face: values {ys}, mean {float(my)}, variance {vy} = {float(vy):.4f}, sd {float(vy) ** 0.5:.4f}")
print(f"by the rules: mean a*3.5 + b = {a * 3.5 + b}, variance a^2 * 35/12 = {a * a * 35 / 12:.4f}, sd |a| * sqrt(35/12) = {abs(a) * (35 / 12) ** 0.5:.4f}")
print(f"slip, a in place of a^2: {a * 35 / 12:.4f}; slip, b added to the variance: {a * a * 35 / 12 + b:.4f}")
a = -2
vz = sum(p * ((a * x + b) - (a * mean + b)) ** 2 for x in faces)
print(f"Z = -2X + 1: mean {float(a * mean + b)}, variance {float(vz):.4f}, sd {float(vz) ** 0.5:.4f} (|a| = 2, not -2)")
abar = 0.4783
print(f"the ladder: x_t = sqrt(abar) x0 + sqrt(1 - abar) eps at t = 50: noise coefficient {(1 - abar) ** 0.5:.4f}, its variance {1 - abar:.4f}; coefficient 1 - abar would give variance {(1 - abar) ** 2:.4f}")
```

**4. A look before: the die on its own.** Run it:

```bash
python3 scale_shift.py
```

You should see:

![Six output lines: the die's mean 3.5 and variance 35/12; Y = 2X + 1 face by face with values 3 to 13, mean 8.0, variance 35/3 = 11.6667 and sd 3.4157, matched by the rules; the two slips 5.8333 and 12.6667; Z = -2X + 1 with the same variance and sd; and the ladder's 0.7223, 0.5217 and 0.2722|1000](assets/scale-and-shift-a-fair-die.png)

Read the first line before anything is scaled: line 5 of the script averages the faces to the mean 3.5 and the squared misses to the variance $35/12 = 2.9167$ (marker 1).

**5. The failure without the rule.** Output line 4 (markers 7 and 8) is the two slips, computed by script line 12: scaling the variance by $a = 2$ instead of $a^2 = 4$ gives 5.8333, half the true 11.6667, and adding $b = 1$ to the variance gives 12.6667, one more than the truth.

**6. The technique.** Output line 3 (marker 6) applies the rule, script line 11: mean $2 \times 3.5 + 1 = 8.0$, variance $2^2 \times 35/12 = 11.6667$, standard deviation $|2| \times \sqrt{35/12} = 3.4157$.

**7. Another way to get the same answer: face by face.** Output line 2 (markers 2 to 5) never uses the rule. Script line 8 builds the six values of $Y$, $[3, 5, 7, 9, 11, 13]$, and line 9 averages them and their squared misses directly: mean 8.0, variance $35/3 = 11.6667$, sd 3.4157. The same three numbers as step 6.

**8. More worked examples on the same die.**

*A negative scale, $Z = -2X + 1$.* Output line 5 (markers 9 and 10), script lines 13 to 15: the mean flips to $-2 \times 3.5 + 1 = -6.0$, while the variance stays 11.6667 and the standard deviation stays 3.4157, because the square erases the sign and the standard deviation takes $|a| = 2$.

*The forward process at $t = 50$.* Output line 6 (markers 11 to 13), script lines 16 and 17, with $\bar\alpha_{50} = 0.4783$ from the 100-step cosine schedule: the noise coefficient $\sqrt{1 - 0.4783} = 0.7223$ gives the noise term variance $0.7223^2 \times 1 = 0.5217$, and using $1 - \bar\alpha$ itself as the coefficient would give $0.5217^2 = 0.2722$.

Run the script again and the same six lines come back: nothing in it is random.

**9. Clean up, and prove it.**

```bash
cd ~ && rm -r ~/playground/sandbox/scale-and-shift
ls ~/playground/sandbox/scale-and-shift; echo $?
```

You should see `No such file or directory`, then `2`.

## Reading the die output

Navigation: ⬅️ [[#Try scaling and shifting yourself]] | 📋 [[#Table of contents|TOC]] | [[#How scaling and shifting work]] ➡️

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | X, variance | `35/12 = 2.9167` | the die's average squared miss from 3.5, as an exact fraction and its decimal | shown, and worked by hand below |
| 2 | Y, values | `[3, 5, 7, 9, 11, 13]` | each face times 2 plus 1; the gaps between neighbours double from 1 to 2 | shown |
| 3 | Y, mean | `8.0` | the plain average of the six values, $48 / 6$, with no rule used | shown |
| 4 | Y, variance | `35/3 = 11.6667` | the average squared miss from 8, with no rule used | shown |
| 5 | Y, sd | `3.4157` | the square root of field 4 | shown |
| 6 | by the rules, variance | `11.6667` | $a^2 \times 35/12$, equal to field 4 | derived below |
| 7 | slip, $a$ in place of $a^2$ | `5.8333` | $2 \times 35/12 = 35/6$, half of field 4 | derived below |
| 8 | slip, $b$ added | `12.6667` | $35/3 + 1 = 38/3$, one more than field 4 | derived below |
| 9 | Z, mean | `-6.0` | $-2 \times 3.5 + 1$: the scale's sign reaches the mean | derived below |
| 10 | Z, sd | `3.4157` | the same as field 5; the variance on the same line is the same as field 4 | derived below |
| 11 | noise coefficient | `0.7223` | $\sqrt{1 - \bar\alpha_{50}} = \sqrt{0.5217}$, the scale $a$ on $\varepsilon$ | shown |
| 12 | its variance | `0.5217` | $a^2 \operatorname{Var}(\varepsilon) = 0.7223^2 \times 1$, the noise share $1 - \bar\alpha_{50}$ | derived below |
| 13 | the slipped variance | `0.2722` | $0.5217^2$, the variance squared a second time | derived below |

## How scaling and shifting work

Navigation: ⬅️ [[#Reading the die output]] | 📋 [[#Table of contents|TOC]] | [[#Where the rule goes wrong]] ➡️

Write $\mu = \mathbb{E}[X]$, let $X$ take the values $x$ with probabilities $p(x)$, and set $Y = aX + b$. The mean first, from the [definition of expectation](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=141), then the variance, one step per line:

$$
\begin{aligned}
\mathbb{E}[Y] &= \textstyle\sum_x (ax + b)\,p(x) = a \sum_x x\,p(x) + b \sum_x p(x) = a\mu + b \cdot 1 = a\mu + b \\
Y - \mathbb{E}[Y] &= (aX + b) - (a\mu + b) = aX - a\mu = a\,(X - \mu) \\
(Y - \mathbb{E}[Y])^2 &= a^2\,(X - \mu)^2 \\
\operatorname{Var}(Y) &= \mathbb{E}\big[a^2 (X - \mu)^2\big] = a^2\,\mathbb{E}\big[(X - \mu)^2\big] = a^2 \operatorname{Var}(X) \\
\operatorname{sd}(Y) &= \sqrt{a^2 \operatorname{Var}(X)} = \sqrt{a^2}\,\sqrt{\operatorname{Var}(X)} = |a|\,\operatorname{sd}(X)
\end{aligned}
$$

Line 1 splits the sum in two and uses that the probabilities add to 1. Line 2 is where the shift cancels: $b$ sits in the value and in the mean, and the subtraction removes both. Line 4 takes the fixed $a^2$ out of the average, the same move as line 1. Line 5 uses $\sqrt{a^2} = |a|$, which is why a standard deviation is never negative.

**The worked numbers, by hand, on a fair die with $Y = 2X + 1$.** Each face has probability $\tfrac16$, $\mu_X = 3.5$ and $\mu_Y = 2 \times 3.5 + 1 = 8$:

| $x$ | $y = 2x + 1$ | $x - 3.5$ | $y - 8$ | $(x - 3.5)^2$ | $(y - 8)^2$ |
|---|---|---|---|---|---|
| 1 | 3 | $-2.5$ | $-5$ | 6.25 | 25 |
| 2 | 5 | $-1.5$ | $-3$ | 2.25 | 9 |
| 3 | 7 | $-0.5$ | $-1$ | 0.25 | 1 |
| 4 | 9 | $+0.5$ | $+1$ | 0.25 | 1 |
| 5 | 11 | $+1.5$ | $+3$ | 2.25 | 9 |
| 6 | 13 | $+2.5$ | $+5$ | 6.25 | 25 |
| sum | 48 | 0 | 0 | 17.5 | 70 |

Every entry in the $y - 8$ column is twice the entry beside it, line 2 of the derivation on real numbers, and every squared miss is four times its neighbour. So:

$$
\begin{aligned}
\mathbb{E}[Y] &= 48 / 6 = 8 \\
\operatorname{Var}(X) &= 17.5 / 6 = 35/12 = 2.9167, & \operatorname{sd}(X) &= \sqrt{35/12} = 1.7078 \\
\operatorname{Var}(Y) &= 70 / 6 = 35/3 = 11.6667 = 4 \times 35/12, & \operatorname{sd}(Y) &= \sqrt{35/3} = 3.4157 = 2 \times 1.7078
\end{aligned}
$$

For $Z = -2X + 1$ the values are $-1, -3, -5, -7, -9, -11$ with mean $-36/6 = -6$, and the misses are $+5, +3, +1, -1, -3, -5$: the same six numbers as $y - 8$ in the reverse order, so the same squares, the same variance $35/3$ and the same standard deviation 3.4157.

**The method, to redo on new numbers.**

1. Write the quantity as $aX + b$ and read off $a$ (what multiplies $X$) and $b$ (what is added), each with its sign.
2. Find $\mathbb{E}[X]$ and $\operatorname{Var}(X)$, from the definition or from what you are given.
3. The mean: $\mathbb{E}[Y] = a\,\mathbb{E}[X] + b$.
4. The variance: square $a$, multiply, and leave $b$ out, $\operatorname{Var}(Y) = a^2 \operatorname{Var}(X)$.
5. The standard deviation: $|a| \operatorname{sd}(X)$, or the square root of step 4. It is never negative.
6. Check one value: pick any $x$, and confirm $y - \mathbb{E}[Y]$ equals $a$ times $x - \mathbb{E}[X]$.

To get a wanted variance $v$ from a draw of variance 1, run step 4 backwards: $a = \sqrt{v}$.

*🖼️ Diagram wanted: the mechanism, the die's six misses from 3.5 doubled into the misses from 8, with the shift by 1 moving the dots and the mean together. Prompt 2 in the vault's `.prompts/Scaling And Shifting A Random Variable.md`.*

*🖼️ Diagram wanted: the deep-dive sheet composing the form, the mechanism, the run and the slips. Prompt 3 in the same file.*

## Where the rule goes wrong

Navigation: ⬅️ [[#How scaling and shifting work]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to get the same numbers]] ➡️

**Scaling the variance by $a$ instead of $a^2$.** On the die, $2 \times 35/12 = 35/6 = 5.8333$ against the true $35/3 = 11.6667$ (output fields 7 and 4). The slip forgets that variance is built from squared misses. It hides when $a$ is near 1 and grows with $a$: by $a = 10$ it is off by a factor of 10.

**Adding the shift to the variance.** $35/3 + 1 = 38/3 = 12.6667$ (field 8). The shift moves the mean along with every value, so line 2 of the derivation removes it. Converting the die's pips to "pips plus 1" cannot make the die more spread out.

**Carrying the sign into the standard deviation.** For $Z = -2X + 1$, $-2 \times 1.7078 = -3.4157$ is a negative spread, which cannot exist. The standard deviation takes $|a|$ (field 10).

**The same slip in the forward process.** The noise at $t = 50$ should carry variance $1 - \bar\alpha_{50} = 0.5217$. Multiplying $\varepsilon$ by $0.5217$ itself gives $0.5217^2 = 0.2722$ (field 13), about half the noise the schedule asks for. Multiplying by $\sqrt{0.5217} = 0.7223$ gives the 0.5217 it asks for (field 12).

How to catch any of the three: run step 6 of the method on one value, or check that a pure shift left the variance unchanged.

<!-- worked-examples-table: mean-and-variance-scaled-shifted-summed rev=1 -->
Problems on the mean and variance from their definitions, under $aX + b$, and under sums of independent variables, from the easiest to the hardest:

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | The mean and variance of a count with $P(0) = 0.65$, $P(1) = 0.15$, $P(2) = 0.10$, $P(3) = 0.10$ | Worked example | [[introduction-to-statistics.pdf#page=82\|Introduction to Statistics, Example 4.2, PDF p. 82]] | Easy | In the book, PDF p. 82: 0.65 and 1.03 (exactly 1.0275); its working prints $4^2$ where $2^2$ is meant, and the final value is right | quiz 0, KD1 |
| 2 | Given $E[X] = 1$ and $E[X^2] = 3$, find $E[(aX + b)^2]$ | Worked example | [[introduction-to-probability-for-data-science.pdf#page=149\|Chan, Example 3.15, PDF p. 149]] | Easy | In the book, PDF p. 149: $3a^2 + 2ab + b^2$ | quiz 0, KD2 |
| 3 | Prove $\mathrm{Var}[X] = E[X^2] - \mu^2$, $\mathrm{Var}[cX] = c^2\mathrm{Var}[X]$ and $\mathrm{Var}[X + c] = \mathrm{Var}[X]$ | Exercise with the book's solution | [[introduction-to-probability-for-data-science.pdf#page=151\|Chan, Practice Exercise 3.6, PDF p. 151]] | Medium | In the book, PDF pp. 151 to 152, every step | quiz 0, KD3 |
| 4 | Simulate the sum of three dice and check mean 10.5 and variance 8.75; the printed listing's `randint(1,6)` gives 9 and 6 | Programming exercise, Python: `np.random.randint` | [[introduction-to-probability-for-data-science.pdf#page=236\|Chan, the dice listing, PDF pp. 236 to 237]] | Medium | [KD4 in the quiz 0 coverage file](/home-mscluster/mmolefe/PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-0.md#kd4-solution-three-dice-in-code) | quiz 0, KD4 |
| 5 | The sum of $N$ independent Gaussians is $\mathcal N(\sum\mu_n, \sum\sigma_n^2)$, by the product of moment generating functions | Worked example | [[introduction-to-probability-for-data-science.pdf#page=345\|Chan, Theorem 6.6, PDF p. 345]] | Hard | In the book, PDF p. 345; the Gaussian generating function is stated there, and the journey's chapter 9.1, step 5, derives it | quiz 0, KD5 |

The derivation of the $aX + b$ rules on a fair die is [[Scaling And Shifting A Random Variable]]. The Gaussian forms of these rules, $aX + b$ for a Gaussian and sums of Gaussian vectors, are banked by quiz 1.1 in [[#Mean and variance of a scaled sum of independent Gaussians (the forward draw)]]. Chan's dice listing has a bug: `np.random.randint(1,6)` draws only 1 to 5.
Read in full (by the bank search for quiz 0): Introduction to Statistics PDF pp. 80 to 83; Chan PDF pp. 149 to 152, 219, 220, 236, 237, 241, 242 and 345; Mathematics for Machine Learning PDF p. 207; Bishop PDF p. 78. Only found: Chan's Theorem 5.5 (PDF p. 279).
<!-- /worked-examples-table -->

## Other ways to get the same numbers

Navigation: ⬅️ [[#Where the rule goes wrong]] | 📋 [[#Table of contents|TOC]] | [[#Why the rule matters]] ➡️

- **List every value** and average directly, as step 7 of the sandbox does. Always right, and only possible when the values can be listed.
- **The moment form**, $\operatorname{Var}(Y) = \mathbb{E}[Y^2] - \mathbb{E}[Y]^2$ (Theorem 3.5 (i), [PDF p. 151](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=151)). On the die: $\mathbb{E}[Y^2] = (9 + 25 + 49 + 81 + 121 + 169)/6 = 454/6 = 227/3$, and $227/3 - 8^2 = 227/3 - 192/3 = 35/3$. *Derived* here.
- **Two random quantities at once**, $aX + bY$: the means combine the same way, and the variances add as $a^2 \operatorname{Var}(X) + b^2 \operatorname{Var}(Y)$ when $X$ and $Y$ are independent. That rule has its own note, [[Sums Of Independent Gaussians#How the rule works]].
- **A matrix in place of $a$**, $AX + b$ for a vector $X$: the covariance becomes $A \Sigma A^\top$ and $b$ still drops out, as [[The Scaling Rule For Variance#Other ways to change a spread]] states with its source.

## Why the rule matters

Navigation: ⬅️ [[#Other ways to get the same numbers]] | 📋 [[#Table of contents|TOC]] | [[#Scaling and shifting taught in, applied in]] ➡️

It reads the forward process off in one line. Fix the clean point $x_0$ and the formula $x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon$ is $aX + b$ with $X = \varepsilon$ (mean 0, variance 1), scale $a = \sqrt{1 - \bar\alpha_t}$ and shift $b = \sqrt{\bar\alpha_t}\,x_0$. So:

$$
\begin{aligned}
\mathbb{E}[x_t \mid x_0] &= a \cdot 0 + b = \sqrt{\bar\alpha_t}\,x_0 \\
\operatorname{Var}(x_t \mid x_0) &= a^2 \cdot 1 = 1 - \bar\alpha_t \\
t = 50: \quad & \text{mean } \sqrt{0.4783}\,x_0 = 0.6916\,x_0, \qquad \text{variance } 0.7223^2 = 0.5217
\end{aligned}
$$

The shift $\sqrt{\bar\alpha_t}\,x_0$ places the cloud and adds nothing to its spread; the scale on $\varepsilon$ alone sets the spread, which is why that scale is a square root. The same reading gives $x = m + s\,\varepsilon$ mean $m$ and variance $s^2$ in [[Sampling A Diagonal Gaussian#How sampling works]].

## Scaling and shifting taught in, applied in

Navigation: ⬅️ [[#Why the rule matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the conditional-expectation journey's [chapter 1, definitions](/home/molef/goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/01-expectation-and-the-best-constant-guess.md#definitions), linearity (1.2), $\mathbb{E}[aX + bY] = a\,\mathbb{E}[X] + b\,\mathbb{E}[Y]$, with its proof in [the proof worth knowing](/home/molef/goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/01-expectation-and-the-best-constant-guess.md#the-proof-worth-knowing); and its [Example 1](/home/molef/goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/01-expectation-and-the-best-constant-guess.md#worked-examples), the fair die's mean 3.5 and variance $35/12$, which this note's die starts from

**Applied in:** layer 1 of the composition ladder in the reduce-reuse-recycle research repository, one diffusion expert (`artifacts/drips/simple-distributions-rebuild/`), whose forward process $x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon$ needs these rules for its square roots: at $t = 50$ the noise coefficient is 0.7223 and its variance 0.5217, and using $1 - \bar\alpha$ itself as the coefficient would give 0.2722.

> [!note]- How this was checked
> `scale_shift.py` was run on 2026-10-20 on mscluster (Linux), with Python 3.12.10 and the standard library only, by vault-writer, in the empty folder `~/playground/sandbox/scale-and-shift` with `HOME` pointed at a scratch folder, so every command above ran byte for byte and nothing was written outside the vault. It was run twice and printed the same six lines. The folder was removed afterwards and the clean-up check returned 2. The prepared environment `~/.vault-sandbox` is missing on this machine and was not needed. The script is copied byte for byte from the quiz-preparation fill for node N13 of the composition ladder's quiz 0, and a copy sits at `sandbox/scale_shift.py` beside this note. The terminal picture was rendered from the captured text by a script in DejaVu Sans Mono, never drawn, and opened before filing. The textbook's PDF pages 141, 147, 151 and 152 were opened with PyMuPDF and read: Definition 3.4, Theorem 3.4 (iii) and (iv), Theorem 3.5 and its proof. The schedule numbers ($\bar\alpha_{50} = 0.4783$ and the noise coefficient 0.7223) match `p1.abar_50` and `p1.sqrt_1m_abar_50` in the rebuild's `rebuild/out/walk-numbers.json`. The hand tables and the moment-form check were computed with exact fractions. [Variance](https://en.wikipedia.org/wiki/Variance) and [Expected value](https://en.wikipedia.org/wiki/Expected_value) on Wikipedia (CC BY-SA 4.0) each answered 200 on 2026-10-20. No tldr-pages entry covers this.
