---
aliases: [solving for the exponent, solve for the exponent, unknown in the exponent, variable in the exponent, exponential equation, exponential inequality, solving an exponential equation, solving an exponential inequality, solve for n with logs, clean rows needed, fewest clean rows, rows needed for a tolerance, ln(delta)/ln(1-alpha), dividing by a negative log flips the inequality]
sources:
  - "Algebra Handbook, version 3.5, October 2022: chapter 7 page 42 (multiplying or dividing an inequality by a negative number), chapter 15 pages 109, 110, 113 and 125 (exponent rules, log rules, converting forms, solving exponential equations): the vault's shelf copy, Mathematics/references/textbooks/algebra/algebra-handbook.pdf"
  - Jung, Brahman and Choi, Trust or Escalate, equation 4, as taught in Selective Evaluation, https://arxiv.org/abs/2407.18370
---

# Solving For The Exponent With Logarithms

Up: [[Logarithms]] · ⬅️ [[The Log Of A Power And Of A Quotient]]

Mathematics, Algebra, Logarithms. Needs: [[The Log Of A Power And Of A Quotient]] (the log of a power is the power times the log) and [[The Exponent Rules#Power of a power|the exponent rules]] (textbook, below).

> [!warning] Unfinished
> - The three drawn pictures (form, mechanism, deep-dive sheet) are not drawn, and no output picture is rendered. No picture prompts were written, as asked. `~/.vault-sandbox` is missing on this machine, so there was no plotting library; to make it: `uv venv ~/.vault-sandbox` then `uv pip install --python ~/.vault-sandbox/bin/python pandas numpy scipy matplotlib statsmodels openpyxl`.
> - No quiz page yet.
> - The `## Videos` section at the end is empty and waits for the video scout.
> - 3 claims are marked stated (in 4 places) and keep nothing unfinished: they are counted in the closing box.

**When the number you want sits in an exponent, as in $0.9^n \le 0.1$, adding, subtracting, multiplying and dividing cannot reach it, and a logarithm can: it brings the exponent down to a multiplier, and then an ordinary division finds it.** The one trap is that the division is by a negative number, which turns the "at most" sign around. This note does it on a real question: how many answered rows with no disagreement are needed before the true disagreement rate is known to be at most a stated tolerance.

**Where you work.** Any folder with Python 3 and nothing installed. The note holds no judge outcomes: the only assumption is that every answered row agreed, so there is nothing invented except the choice of tolerances.

## Table of contents

- [The question: how many clean rows](#the-question-how-many-clean-rows)
- [The method: take logs of both sides](#the-method-take-logs-of-both-sides)
- [The other route: the power one over n](#the-other-route-the-power-one-over-n)
- [Four more solves](#four-more-solves)
- [One way it goes wrong: forgetting to flip](#one-way-it-goes-wrong-forgetting-to-flip)
- [Check: loop n upward](#check-loop-n-upward)
- [Other ways](#other-ways)
- [Taught in, applied in](#taught-in-applied-in)
- [How this was checked](#how-this-was-checked)
- [Videos](#videos)

## The question: how many clean rows

Navigation: 📋 [[#Table of contents]] | [[#The method: take logs of both sides]] ➡️

**A judge that agreed with the reviewer on every one of $n$ rows has still not proved its true disagreement rate is zero, and $n$ decides how high that rate could still be.** With few rows a lucky streak is easy; with many it is not. The exact upper bound, defined in [[Selective Evaluation#The exact binomial upper bound]], is that after $n$ rows with no disagreement, the true rate $R$ satisfies

$$
R \le 1 - \delta^{1/n}
$$

where $\delta$ is the chance you accept of the bound being wrong. This note takes $\delta = 0.10$ throughout, which is the 90% bound of that note. The tolerance $\alpha$ is the rate you want the bound to be at most. So the question is: what is the smallest whole number $n$ with $1 - \delta^{1/n} \le \alpha$?

**Turn the bound into an equation with the unknown in the exponent.** Each line is one move.

1. Start from the requirement: $1 - \delta^{1/n} \le \alpha$.
2. Add $\delta^{1/n}$ to both sides and subtract $\alpha$ from both sides: $1 - \alpha \le \delta^{1/n}$.
3. Raise both sides to the power $n$. Both sides are positive, and a positive power keeps the order (stated; see the check below for numbers), so $(1-\alpha)^n \le \left(\delta^{1/n}\right)^n$.
4. The right side is $\delta^{(1/n)\cdot n} = \delta^1$ by the power-of-a-power rule ([exponent rules, handbook p. 109](../../references/textbooks/algebra/algebra-handbook.pdf#page=109)).

$$
(1-\alpha)^n \le \delta
$$

Read it in words: the chance that $n$ rows all agree, when the true disagreement rate is exactly $\alpha$, is $(1-\alpha)^n$; the requirement is that this chance is at most $\delta$. With $\alpha = 0.10$ and $\delta = 0.10$: $0.9^n \le 0.1$. Here $n$ is in the exponent.

**Why this matters.** The same equation answers "how many rows for a 10% tolerance" (22), "for 5%" (45) and "for 20%" (11), the numbers in the table of [[Selective Evaluation#Walking the threshold on 105 rows]]. Backing: derived (the four moves), cited (Jung et al. equation 4, in [[Selective Evaluation#The exact binomial upper bound]]).

## The method: take logs of both sides

Navigation: ⬅️ [[#The question: how many clean rows]] | 📋 [[#Table of contents]] | [[#The other route: the power one over n]] ➡️

Textbook: [Algebra handbook, ch. 15, p. 125, solving exponential equations](../../references/textbooks/algebra/algebra-handbook.pdf#page=125), with [log rules, p. 110](../../references/textbooks/algebra/algebra-handbook.pdf#page=110), [e and the natural log, p. 111](../../references/textbooks/algebra/algebra-handbook.pdf#page=111) and [multiplying or dividing an inequality by a negative number, ch. 7, p. 42](../../references/textbooks/algebra/algebra-handbook.pdf#page=42).

**To solve $(1-\alpha)^n \le \delta$ for $n$, take the natural log of both sides, bring $n$ down with the power rule, and divide by $\ln(1-\alpha)$, flipping the sign because that number is negative.** The handbook's page 125 shows the same method (isolate the exponential term, take logs, solve what remains) on equations whose answers are whole numbers. It does not cover an inequality, a negative log, a fractional answer or rounding, which the steps below add.

The numbered steps, for $\alpha = 0.10$, $\delta = 0.10$:

1. **Write the requirement.** $0.9^n \le 0.1$.
2. **Take the natural log of both sides.** The order is kept: $\ln$ is an increasing function, so for positive $u \le v$ we get $\ln u \le \ln v$ (stated; for example $2 \le 3$ and $\ln 2 = 0.693 \le \ln 3 = 1.099$). The inequality stays "$\le$":
$$
\ln\left(0.9^n\right) \le \ln 0.1
$$
3. **Bring $n$ down.** The power rule, $\ln(a^n) = n\ln a$ ([[The Log Of A Power And Of A Quotient]], handbook p. 110):
$$
n \ln 0.9 \le \ln 0.1
$$
4. **Put in the two logs.** $\ln 0.9 = -0.105361$ and $\ln 0.1 = -2.302585$. Both are negative because both numbers are below 1:
$$
-0.105361\,n \le -2.302585
$$
5. **Divide both sides by $-0.105361$, and flip the sign.** Dividing by a negative number reverses the order (handbook p. 42). Check it on small numbers: $2 \le 3$ is true; divide both by $-1$ and you get $-2$ and $-3$, and $-2 \le -3$ is false, while $-2 \ge -3$ is true. So "$\le$" becomes "$\ge$":
$$
n \ge \frac{-2.302585}{-0.105361} = 21.854
$$
6. **Round up to a whole number.** $n$ counts rows, and the requirement is $n \ge 21.854$, so the smallest whole number that passes is the next whole number above: $\lceil 21.854 \rceil = 22$. Rounding to the nearest number can land below the line (shown in [[#One way it goes wrong: forgetting to flip]]).
7. **Substitute back.** $0.9^{22} = 0.0985$, which is at most $0.1$. $0.9^{21} = 0.1094$, which is above $0.1$. So 22 is the smallest.

The general result for any $\alpha$ between 0 and 1:

$$
n \ge \frac{\ln \delta}{\ln(1-\alpha)}, \qquad n_{\min} = \left\lceil \frac{\ln \delta}{\ln(1-\alpha)} \right\rceil
$$

Both logs are negative whenever $\delta$ and $1-\alpha$ are below 1, so the ratio is positive, and the flip in step 5 happens for every $\alpha$.

**Worked on $\alpha = 0.20$, $\delta = 0.10$.** $\ln 0.8 = -0.223144$. The requirement $0.8^n \le 0.1$ becomes $n \ln 0.8 \le \ln 0.1$, that is $-0.223144\,n \le -2.302585$, and dividing by $-0.223144$ flips it to $n \ge 10.319$. The next whole number is 11. At $n = 11$ the bound is $1 - 0.1^{1/11} = 1 - 0.8111 = 0.1889$, so 18.9%, below 20%. At $n = 10$ it is $1 - 0.1^{1/10} = 1 - 0.7943 = 0.2057$, so 20.6%, above 20%.

**Why this matters.** Every row count in the judge-validation work, 11, 22, 32, 45, 230, comes out of this one division. Backing: derived (the steps), cited (handbook p. 125 for the method, p. 42 for the flip), shown (the run below).

<!-- worked-examples-table: logs-and-exponents rev=1 -->
Problems on the log rules and on solving for an unknown in the exponent, the move behind a moving average's half-life, from the easiest to the hardest:

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | Rewrite $\log_4 64 = x$ and $\ln e = x$ in exponential form and solve | Worked example | [[algebra-handbook.pdf#page=113\|Algebra handbook, examples 1 and 2, PDF p. 113]] | Easy | In the book, PDF p. 113, every step: $x = 3$ and $x = 1$ | quiz 0, KA1 |
| 2 | Condense $6 + \ln(3e^5)$ and $\log_4(1/16) - 6^{\log_6 4}$ with the product, power and quotient rules | Worked example | [[algebra-handbook.pdf#page=116\|Algebra handbook, PDF p. 116]] | Easy | In the book, PDF p. 116, every step: $11 + \ln 3$ and $-6$ | quiz 0, KA2 |
| 3 | Solve $2 + 4 \cdot 3^{x-2} = 110$: isolate the power, take logs, solve | Worked example | [[algebra-handbook.pdf#page=125\|Algebra handbook, PDF p. 125]] | Medium | In the book, PDF p. 125, every step: $x = 5$ | quiz 0, KA3 |
| 4 | A satellite's power is $P = 75e^{-t/125}$ watts: when does it fall to 7 watts? | Worked example | [[calculus-textbook.pdf#page=82\|Anton, Calculus, section 0.5, Example 3, PDF p. 82 (printed 58)]] | Medium | In the book, PDF p. 82, every step: $t = -125 \ln(7/75) \approx 296.4$ days | quiz 0, KA4 |

The ladder's own solve, the moving average's half-life $\ln 0.5 / \ln 0.999 = 692.8$ steps, is quiz 0's written question A2 and is worked in [[Solving For The Exponent With Logarithms]] and [[The Exponent Rules]]. Not banked: Anton's exercises 0.5 #25, #27 and #49 (PDF pp. 85 to 86), whose answers at PDF p. 1240 are final values only, and Murphy's section 4.4.2.2 (PDF p. 139), which derives the moving average's weights $\beta^k(1 - \beta)$ without a numeric question.
Read in full (by the bank search for quiz 0): algebra handbook PDF pp. 113, 115, 116, 124 and 125; Anton PDF pp. 81, 82, 85 to 87 and 1240; Murphy PDF pp. 139 to 140. Only found: algebra handbook PDF pp. 109 to 112 and 117 to 123, rule tables and further examples.
<!-- /worked-examples-table -->

## The other route: the power one over n

Navigation: ⬅️ [[#The method: take logs of both sides]] | 📋 [[#Table of contents]] | [[#Four more solves]] ➡️

**The power $1/n$ turns the requirement into the bound formula, which tests a given $n$ but cannot find $n$ alone; one log is still needed.** Same question, $\alpha = 0.20$, $\delta = 0.10$.

1. Start with $0.8^n \le 0.1$.
2. Raise both sides to the power $1/n$. For positive numbers a positive power keeps the order (stated), and $(0.8^n)^{1/n} = 0.8$ by the power-of-a-power rule:
$$
0.8 \le 0.1^{1/n}
$$
3. Move the terms: $1 - 0.1^{1/n} \le 0.2$. This is the bound formula of the first section. It is a test for one $n$ at a time:
   - $n = 11$: $0.1^{1/11} = e^{-2.302585/11} = e^{-0.209326} = 0.8111$, so the bound is $1 - 0.8111 = 0.1889$, at most $0.20$: passes.
   - $n = 10$: $0.1^{1/10} = e^{-0.230259} = 0.7943$, so the bound is $0.2057$, above $0.20$: fails.
4. To find $n$ without trying values, take the natural log of step 2's inequality: $\ln 0.8 \le \frac{1}{n}\ln 0.1$, that is $-0.223144 \le -\frac{2.302585}{n}$.
5. Multiply both sides by $n$, which is positive, so no flip: $-0.223144\,n \le -2.302585$.
6. Divide by $-0.223144$ and flip: $n \ge 10.319$. This is the other route's step 5, so both routes finish at 11.

*Derived.* The first route divides by a negative number once; this one multiplies by a positive $n$ and then divides by the same negative number. The flip is not avoidable on either.

## Four more solves

Navigation: ⬅️ [[#The other route: the power one over n]] | 📋 [[#Table of contents]] | [[#One way it goes wrong: forgetting to flip]] ➡️

**The same two lines, $n \ge \ln\delta / \ln(1-\alpha)$ and round up, on four more tolerances.** $\ln \delta = \ln 0.1 = -2.302585$ in every row. The two bounds are $1 - 0.1^{1/n}$ at the whole number and at the one below it.

| $\alpha$ | $\ln(1-\alpha)$ | $-2.302585 / \ln(1-\alpha)$ | $n$ | bound at $n$ | bound at $n-1$ |
|---:|---:|---:|---:|---:|---:|
| 0.20 | −0.2231 | 10.32 | 11 | 0.188869 | 0.205672 |
| 0.10 | −0.1054 | 21.85 | 22 | 0.099372 | 0.103849 |
| 0.07 | −0.0726 | 31.73 | 32 | 0.069428 | 0.071585 |
| 0.05 | −0.0513 | 44.89 | 45 | 0.049881 | 0.050986 |
| 0.01 | −0.0101 | 229.11 | 230 | 0.009961 | 0.010005 |

Every row has the bound at $n$ at or below $\alpha$ and the bound at $n - 1$ above it, so no smaller whole number works. The 0.20, 0.10 and 0.05 rows are the 11, 22 and 45 of [[Selective Evaluation#Walking the threshold on 105 rows]]. *Shown* by the run below.

## One way it goes wrong: forgetting to flip

Navigation: ⬅️ [[#Four more solves]] | 📋 [[#Table of contents]] | [[#Check: loop n upward]] ➡️

**Dividing by $-0.105361$ and keeping "$\le$" gives $n \le 21.854$, which is backwards: it lets in the smallest sample sizes and rules out the one that works.** Step 5 done wrongly:

$$
-0.105361\,n \le -2.302585 \;\;\xrightarrow{\text{no flip}}\;\; n \le 21.854
$$

That claims $n = 1$ is enough. At $n = 1$ the bound is $1 - 0.1^{1/1} = 0.9000$: one agreed row leaves the true rate possibly as high as 90%. It claims $n = 21$ is enough; its bound is $1 - 0.1^{1/21} = 0.1038$, above $0.10$. And it claims $n = 22$ is not enough, when $n = 22$ gives $0.0994$. A second slip is rounding to the nearest whole number: for $\alpha = 0.20$ the answer $10.32$ rounds to 10, whose bound is $0.2057$, above the $0.20$ it was meant to meet. The sign check catches the first slip in one line: plug in a number from the answer and see whether the original inequality holds.

## Check: loop n upward

Navigation: ⬅️ [[#One way it goes wrong: forgetting to flip]] | 📋 [[#Table of contents]] | [[#Other ways]] ➡️

**The check uses no algebra: try $n = 1, 2, 3, \dots$ with the exact formula $1 - \delta^{1/n}$ and stop at the first $n$ whose bound is at most $\alpha$.** If the log answer is right, the first stop is the same number.

Save as `clean_rows.py` in an empty folder (also saved in this folder's `sandbox/`):

```python
# Fewest answered rows with zero disagreements for the 90% upper bound to be at most alpha.
# Solve (1 - alpha)^n <= delta for n by logs, then check by looping n upward.
# Nothing here uses judge outcomes: zero disagreements is the assumption.
import math

delta = 0.10


def bound(n):
    """Exact one-sided upper bound on the true rate after n rows with no disagreement."""
    return 1 - delta ** (1 / n)


print("worked solves")
for alpha in (0.20, 0.10, 0.07, 0.05, 0.01):
    x = math.log(delta) / math.log(1 - alpha)
    n = math.ceil(x)
    print(f"alpha {alpha:.2f}: ln(delta) {math.log(delta):.4f} / ln(1-alpha) {math.log(1 - alpha):.4f}"
          f" = {x:.2f} -> n = {n}; bound at n {bound(n):.6f}, at n-1 {bound(n - 1):.6f}")

print("the log base does not matter (alpha 0.10)")
print(f"  natural {math.log(delta) / math.log(0.9):.4f}  base 10 {math.log10(delta) / math.log10(0.9):.4f}")

print("substituting n back, alpha 0.10: (0.9)^n")
for n in (21, 22):
    print(f"  n {n}: 0.9^n = {0.9 ** n:.4f}  {'<=' if 0.9 ** n <= delta else '>'} {delta}")

print("check: loop n upward with the exact formula")
for alpha in (0.20, 0.10, 0.07, 0.05, 0.01):
    first = next(n for n in range(1, 10000) if bound(n) <= alpha)
    by_logs = math.ceil(math.log(delta) / math.log(1 - alpha))
    print(f"  alpha {alpha:.2f}: first n in the loop {first}, by logs {by_logs}, same: {first == by_logs}")

print("failure 1: forgetting to flip gives n <= 21.85 (alpha 0.10)")
for n in (1, 21):
    print(f"  n {n} would be allowed; its bound is {bound(n):.4f}, not at most 0.10")

print("failure 2: rounding to the nearest whole row (alpha 0.20)")
x = math.log(delta) / math.log(0.8)
print(f"  x {x:.2f} rounds to {round(x)}; bound at {round(x)} is {bound(round(x)):.4f}, above 0.20")
```

Run it:

```bash
python3 -I clean_rows.py
```

You should see:

```text
worked solves
alpha 0.20: ln(delta) -2.3026 / ln(1-alpha) -0.2231 = 10.32 -> n = 11; bound at n 0.188869, at n-1 0.205672
alpha 0.10: ln(delta) -2.3026 / ln(1-alpha) -0.1054 = 21.85 -> n = 22; bound at n 0.099372, at n-1 0.103849
alpha 0.07: ln(delta) -2.3026 / ln(1-alpha) -0.0726 = 31.73 -> n = 32; bound at n 0.069428, at n-1 0.071585
alpha 0.05: ln(delta) -2.3026 / ln(1-alpha) -0.0513 = 44.89 -> n = 45; bound at n 0.049881, at n-1 0.050986
alpha 0.01: ln(delta) -2.3026 / ln(1-alpha) -0.0101 = 229.11 -> n = 230; bound at n 0.009961, at n-1 0.010005
the log base does not matter (alpha 0.10)
  natural 21.8543  base 10 21.8543
substituting n back, alpha 0.10: (0.9)^n
  n 21: 0.9^n = 0.1094  > 0.1
  n 22: 0.9^n = 0.0985  <= 0.1
check: loop n upward with the exact formula
  alpha 0.20: first n in the loop 11, by logs 11, same: True
  alpha 0.10: first n in the loop 22, by logs 22, same: True
  alpha 0.07: first n in the loop 32, by logs 32, same: True
  alpha 0.05: first n in the loop 45, by logs 45, same: True
  alpha 0.01: first n in the loop 230, by logs 230, same: True
failure 1: forgetting to flip gives n <= 21.85 (alpha 0.10)
  n 1 would be allowed; its bound is 0.9000, not at most 0.10
  n 21 would be allowed; its bound is 0.1038, not at most 0.10
failure 2: rounding to the nearest whole row (alpha 0.20)
  x 10.32 rounds to 10; bound at 10 is 0.2057, above 0.20
```

| Field | Value | How to read it |
|---|---|---|
| `x` after `=` | 21.85 for $\alpha$ 0.10 | $\ln\delta / \ln(1-\alpha)$, the line the inequality gives before rounding |
| `n = ` | 22 | `math.ceil(x)`, the next whole number at or above $x$ |
| `bound at n`, `at n-1` | 0.099372 and 0.103849 | $1 - \delta^{1/n}$ at $n$ and one below; the first is at most $\alpha$ and the second is above it |
| `natural` and `base 10` | 21.8543 twice | the ratio is the same in any log base, because both logs change by the same factor (change of base, handbook p. 110) |
| `0.9^n` rows | 0.1094 above 0.1, 0.0985 at most 0.1 | substituting $n$ back into the original inequality |
| `first n in the loop` | 22 | the first whole number whose exact bound is at most $\alpha$, found with no algebra |
| `same: True` | on all five rows | the loop and the log agree at 11, 22, 32, 45 and 230 |
| `failure 1`, `failure 2` | $n = 1$ and $n = 21$ pass wrongly; 10 rounds wrongly | the numbers behind [[#One way it goes wrong: forgetting to flip]] |

*Backing:* shown (the run). The loop compares the exact bound with $\alpha$ number by number and relies on none of the stated claims, so it confirms their result.

**Why this matters.** A second route that shares no step with the first is the only evidence that the flip and the rounding were done right. Backing: shown.

## Other ways

Navigation: ⬅️ [[#Check: loop n upward]] | 📋 [[#Table of contents]] | [[#Taught in, applied in]] ➡️

**Take the log in the base of the exponent.** The handbook's page 125 says to use the base that appears in the exponential. Here that is base 0.9, written $\log_{0.9}$. A log with a base below 1 is a decreasing function, so taking it flips the inequality at that step: $0.9^n \le 0.1$ becomes $n \ge \log_{0.9} 0.1$ (stated). Converting form ([handbook p. 113](../../references/textbooks/algebra/algebra-handbook.pdf#page=113)) and the change of base ([p. 110](../../references/textbooks/algebra/algebra-handbook.pdf#page=110)) give $\log_{0.9} 0.1 = \ln 0.1 / \ln 0.9 = 21.854$, the same number. The flip moved from the division to the log, and still happens once.

**Try values.** The loop above. It needs no logs and scales badly only when $n$ is in the millions.

**For an exact equation, not an inequality.** Set $(1-\alpha)^n = \delta$ and take logs the same way. There is no sign to flip, and the answer $n = \ln\delta / \ln(1-\alpha)$ is the boundary: any whole $n$ at or above it passes.

**A tolerance that is not a fixed rate.** When there are $k > 0$ disagreements, the bound is the binomial bound of [[Selective Evaluation#The exact binomial upper bound]] and has no closed form in $n$; the loop is the way to find $n$ there.

## Taught in, applied in

Navigation: ⬅️ [[#Other ways]] | 📋 [[#Table of contents]] | [[#How this was checked]] ➡️

**Taught in.**

- [Validating an LLM judge, plan 16, k errors and the 8-page floor](/Users/molefemolefe/goal-setting/learning/ai-engineering/agent-evaluation/validating-an-llm-judge/plans/16-k-errors-and-the-8-page-floor.md), whose target of 22 error-free rows for a 10% bound is the solve above.

**Applied in.**

- The v3 product-content judge in the Dis-Chem product data repo: a judge checked on 8 approved gold pages and 97 planted-defect copies. A tolerance of 5% on missed bad products needs 45 bad rows with none missed, and the 97 bad rows give a bound of 2.3% with none missed; see [[The 105-Row Gold Set#What the counts can certify]]. No real judge has been run on the set.
- The selective evaluator's cut-off walk on 105 calibration rows: how many answered rows a tolerance of 0.20, 0.10, 0.07 or 0.05 needs; see [[Selective Evaluation#Walking the threshold on 105 rows]].

## How this was checked

Navigation: ⬅️ [[#Taught in, applied in]] | 📋 [[#Table of contents]] | [[#Videos]] ➡️

> [!note]- How this was checked
> `clean_rows.py` was run on 2026-10-18 on a Mac with Python 3.12 (standard library only) with `python3 -I`, from an empty folder that was removed afterwards (the check afterwards found the folder gone). The printed lines are the ones in the note. The prepared environment `~/.vault-sandbox` does not exist on this machine, so the standard library interpreter was used and no output picture was rendered. The algebra handbook pages 42, 109, 110, 111, 113 and 125 were opened with PyMuPDF and read: page 42 states that multiplying or dividing an inequality by a negative number flips the sign; page 110 lists the power rule, the quotient rule and the change of base; page 113 converts between exponential and log form; page 125 solves exponential equations by isolating the term and taking logs, on whole-number answers only. The statements about the power one over n and about a log with a base below 1 were not found on those pages. The note has not been rendered in Obsidian.
>
> Claims marked stated, 3, in 4 places: that $\ln$ keeps the order of positive numbers, that raising positive numbers to a positive power keeps their order (used twice), and that a log with a base below 1 reverses the order. The loop in the check relies on none of them.

## Videos

<!-- video-table: exponent-inequality-with-logarithms rev=1 -->
Hasegi Inc., then TLMaths, both from the open web, on solving an inequality such as 0.5^x < 10^300 with logarithms, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | (1/2)^x < (1/2)^3 gives x > 3: a base below 1 makes the function fall, so the order reverses | Intuition, open web | [Hasegi Inc., Why an Exponential Inequality Flips When the Base Is Below 1, 0:03 to 1:32](https://www.youtube.com/watch?v=WzR5E7dGM7M&t=3s) |
| 2 | Write 1/2 as 2^(-1), compare exponents to get -x < -3, and multiplying both sides by -1 flips the sign: the same flip as dividing by a negative | Intuition, open web | [Hasegi Inc., Why an Exponential Inequality Flips When the Base Is Below 1, 1:32 to 2:05](https://www.youtube.com/watch?v=WzR5E7dGM7M&t=92s) |
| 3 | Solve 0.5^x < 10^300: take natural logs of both sides, bring both exponents down, divide by ln 0.5 = -0.693, which is negative, so the sign reverses and x > -996.57 | Worked example, open web | [TLMaths, Solving 0.5^x less than 10^300, 0:06 to 2:23](https://www.youtube.com/watch?v=nDr4CrZ_CO8&t=6s) |
| 4 | Why writing it as a log with base 0.5 in one step goes wrong (the flip is forgotten), and why to go through natural logs | Worked example, open web | [TLMaths, Solving 0.5^x less than 10^300, 2:23 to 3:27](https://www.youtube.com/watch?v=nDr4CrZ_CO8&t=143s) |

Neither video solves for a whole number of repeats or rounds the answer up, and neither starts from a base above 1 with a positive log. TLMaths refers to an earlier video of his for the base 2 case. Professor Leonard's logarithm lecture (Precalculus 64) was checked by chapter titles only, which name equations, so it is not linked. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->
