---
aliases: [the binomial theorem, binomial theorem, binomial expansion, binomial formula, expanding a power of a sum, "(a + b)^n", "(a + b)^n = sum C(n, k) a^(n - k) b^k", Pascal's triangle, Pascal triangle, Pascal's rule, Pascal's identity, binomial coefficient, binomial coefficients, n choose k, "C(n, k)"]
sources:
  - "Earl L. Whitney, Math Handbook of Formulas, Processes and Tricks: Algebra and PreCalculus, version 3.5, 2022, chapter 19, Pascal's Triangle (PDF p. 174) and Binomial Expansion, four steps on (2x - 3)^4 (PDF p. 175): the vault's shelf copy, Mathematics/references/textbooks/algebra/algebra-handbook.pdf"
  - "Chan, Introduction to Probability for Data Science, Michigan Publishing 2021, Theorem 1.2 (the binomial theorem, motivated by three coins, PDF p. 22), Theorem 1.3 (Pascal's identity, PDF p. 23), the induction proof and the line (p + (1 - p))^n = 1 (PDF p. 25), Theorem 1.7 (the number of combinations, PDF p. 51): the vault's shelf copy, Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf; https://probability4datascience.com/"
  - "Wikipedia, Binomial theorem: https://en.wikipedia.org/wiki/Binomial_theorem, read 2026-10-21, CC BY-SA 4.0"
  - "Wikipedia, Pascal's triangle: https://en.wikipedia.org/wiki/Pascal%27s_triangle, read 2026-10-21, CC BY-SA 4.0"
---

# The Binomial Theorem

Up: [[Algebra]] · ⬅️ [[Arithmetic And Geometric Mean]]

Mathematics, Algebra. Needs: multiplying out brackets, the [distributive property](../references/textbooks/algebra/algebra-handbook.pdf#page=16), and the [[The Exponent Rules#Zero exponent|zero exponent]], $a^0 = 1$.

> [!warning] Unfinished
> - The three drawn pictures (the form, the mechanism and the deep-dive sheet) are waiting: prompts 1 to 3 in the vault's `.prompts/The Binomial Theorem.md`.
> - No quiz page for this note yet.

Claims marked stated: 1.

**A power of a sum, such as $(2 + 3)^4$, multiplies out into one term for every way of choosing, from each bracket, either the first number or the second.** The terms that chose the second number $k$ times all look alike, $a^{n-k} b^k$, and there are $\binom{n}{k}$ of them, the number of ways to pick which $k$ brackets gave it. So $(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$. The counts $\binom{n}{k}$ are the rows of Pascal's triangle.

## Where you work

Any terminal with Python 3.8 or later (the script uses `math.comb`, added in 3.8) and a new empty folder. The script uses the standard library only, so nothing is installed, and every number in it is made up.

## Table of contents

- [[#What the binomial theorem says]]
- [[#When to reach for it]]
- [[#The form of the theorem]]
- [[#Try the binomial theorem yourself]]
- [[#Reading the binomial output]]
- [[#How the binomial theorem works]]
- [[#Other ways to expand a power of a sum]]
- [[#Why the binomial theorem matters]]
- [[#The binomial theorem taught in, applied in]]

## What the binomial theorem says

Navigation: 📋 [[#Table of contents|TOC]] | [[#When to reach for it]] ➡️

Textbook: [Algebra handbook, Binomial Expansion, PDF p. 175](../references/textbooks/algebra/algebra-handbook.pdf#page=175) · [Pascal's Triangle, PDF p. 174](../references/textbooks/algebra/algebra-handbook.pdf#page=174) · [Introduction to probability for data science, Theorem 1.2, PDF p. 22](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=22). Chan prints page numbers 16 lower (PDF page 22 prints 6).

Write $(a + b)^2$ as two brackets side by side, $(a + b)(a + b)$. Multiplying them out takes one number from the first bracket and one from the second, every way it can: $a \cdot a$, $a \cdot b$, $b \cdot a$, $b \cdot b$. Two of the four picks give the same thing, $ab$, so they merge into $2ab$, and $(a + b)^2 = a^2 + 2ab + b^2$. The 2 in front is a count of picks. With $n$ brackets there are $2^n$ picks, and the counts in front are the binomial coefficients.

**The binomial theorem**, also the binomial expansion or binomial formula: for any numbers $a$ and $b$ and any whole number $n \ge 0$,

$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k}\, a^{n-k}\, b^k .$$

*Cited:* Chan, Theorem 1.2, and the handbook's general formula on PDF p. 175. *Derived* in [[#How the binomial theorem works]].

**Binomial coefficient**, also "$n$ choose $k$", written $\binom{n}{k}$ or $C(n, k)$: the number of ways to choose $k$ things out of $n$ when the order does not matter, $\binom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$, where $n! = n \times (n - 1) \times \dots \times 1$ and $0! = 1$. *Cited:* [Chan, Theorem 1.7, PDF p. 51](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=51), which proves the count.

**Pascal's triangle**: the binomial coefficients laid out in rows, row $n$ holding $\binom{n}{0}$ to $\binom{n}{n}$. Each row starts and ends with 1, and every other entry is the sum of the two entries above it. That adding step is **Pascal's rule**, also Pascal's identity, $\binom{n}{k-1} + \binom{n}{k} = \binom{n+1}{k}$. *Cited:* the handbook, PDF p. 174, and [Chan, Theorem 1.3, PDF p. 23](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=23).

## When to reach for it

Navigation: ⬅️ [[#What the binomial theorem says]] | 📋 [[#Table of contents|TOC]] | [[#The form of the theorem]] ➡️

A power of a sum appears whenever independent trials multiply. Each of $n$ independent tries carries a factor (fail weight + succeed weight), and the product of $n$ such factors is $(\text{fail} + \text{succeed})^n$. The theorem sorts its $2^n$ pieces by how many successes each holds, which is how the chance of exactly $k$ successes gets its $\binom{n}{k}$. The moment generating function of a count of successes is also a power of a sum, as [[#Why the binomial theorem matters]] says.

Without it, $(a + b)^n$ gets written $a^n + b^n$, which drops every mixed term. On $(2 + 3)^4$ that gives 97 against the true 625, worked in [[#How the binomial theorem works]].

## The form of the theorem

Navigation: ⬅️ [[#When to reach for it]] | 📋 [[#Table of contents|TOC]] | [[#Try the binomial theorem yourself]] ➡️

```text
(a + b)**n = sum over k = 0, 1, ..., n of   C(n, k) * a**(n - k) * b**k
                                            |         |              |
                                            |         |              b's power counts up from 0 to n
                                            |         a's power counts down from n to 0
                                            how many picks give this term: row n of Pascal's triangle
n + 1 terms; in every term the two powers add to n
```

*🖼️ Diagram wanted: the form, four brackets (2 + 3) side by side with one pick highlighted per bracket, the 16 picks sorted into five piles by how many 3s they took, pile sizes 1, 4, 6, 4, 1. Prompt 1 in the vault's `.prompts/The Binomial Theorem.md`.*

## Try the binomial theorem yourself

Navigation: ⬅️ [[#The form of the theorem]] | 📋 [[#Table of contents|TOC]] | [[#Reading the binomial output]] ➡️

**1. What you need.** Python 3.8 or later:

```bash
python3 --version
```

You should see a version line. This run printed `Python 3.12.10`.

**2. When it is missing.** Install Python 3 from python.org, or run `uv python install 3.12`. Not run on this machine, which already has it.

**3. Make something to act on.** Make an empty folder and go into it:

```bash
mkdir -p ~/playground/sandbox/binomial-theorem && cd ~/playground/sandbox/binomial-theorem
```

Save this as `binomial.py`. Line 5 is the theorem itself, one term per $k$; lines 9 to 12 build Pascal's triangle by adding the two entries above, with no formula.

```python
# The binomial theorem, (a + b)^n = sum over k of C(n, k) a^(n - k) b^k, worked term by term and checked.
from math import comb

a, b, n = 2, 3, 4
terms = [comb(n, k) * a ** (n - k) * b ** k for k in range(n + 1)]
for k in range(n + 1):
    print(f"k = {k}: C(4, {k}) = {comb(n, k)}, 2^{n - k} = {a ** (n - k)}, 3^{k} = {b ** k}, term {terms[k]}")
print(f"the terms add to {sum(terms)}; (2 + 3)^4 = 5^4 = {(a + b) ** n}")
row = [1]
for r in range(1, 6):
    row = [1] + [row[i - 1] + row[i] for i in range(1, r)] + [1]
    print(f"Pascal row {r}: {row}, adds to {sum(row)} = 2^{r}")
print(f"row 5 from C(5, k): {[comb(5, k) for k in range(6)]}")
print(f"(x + 1)^5 at x = 2: 3^5 = {3 ** 5}, the six terms add to {sum(c * 2 ** (5 - k) for k, c in enumerate(row))}")
print(f"slip, no coefficients: 2^2 + 3^2 = {a ** 2 + b ** 2} against (2 + 3)^2 = {(a + b) ** 2}; the lost middle term 2 x 2 x 3 = {2 * a * b}")
print(f"slip at n = 4: 2^4 + 3^4 = {a ** 4 + b ** 4} against (2 + 3)^4 = {(a + b) ** 4}")
signed = [comb(4, k) * 2 ** (4 - k) * (-3) ** k for k in range(5)]
print(f"(2x - 3)^4 coefficients: {signed}; at x = 1 they add to {sum(signed)} = (2 - 3)^4 = {(2 - 3) ** 4}")
print(f"with 144 printed for 216 they add to {sum(signed) - 216 + 144}")
p = [comb(3, k) * 0.25 ** k * 0.75 ** (3 - k) for k in range(4)]
print(f"C(3, k) 0.25^k 0.75^(3 - k) for k = 0 to 3: {', '.join(f'{t:.6f}' for t in p)}; they add to {sum(p)} = (0.25 + 0.75)^3")
```

Run it:

```bash
python3 binomial.py
```

You should see:

![Eighteen output lines: the five terms of (2 + 3)^4, 16, 96, 216, 216 and 81, adding to 625 = 5^4; Pascal's rows 1 to 5 built by adding, row 5 matching C(5, k); (x + 1)^5 at x = 2 giving 243 both ways; the two slips 13 against 25 and 97 against 625; the handbook's (2x - 3)^4 adding to 1 at x = 1 and to -71 with its misprint; and the four probabilities 0.421875, 0.421875, 0.140625, 0.015625 adding to 1|1000](assets/binomial-theorem-worked-and-checked.png)

**4. A look before: the five terms on their own.** Output lines 1 to 5, from script lines 5 to 7, show each term of $(2 + 3)^4$ before anything is added: the count $\binom{4}{k}$, the power of 2 counting down, the power of 3 counting up, and their product (markers 1 to 3).

**5. The failure without the theorem.** Output lines 14 and 15, script lines 15 and 16: writing $(2 + 3)^2$ as $2^2 + 3^2$ gives 13 against 25, and $(2 + 3)^4$ as $2^4 + 3^4$ gives 97 against 625 (markers 10 to 13). Where each lost amount comes from is in [[#How the binomial theorem works]].

**6. The technique.** Output line 6, script line 8: the five terms add to 625, and $(2 + 3)^4 = 5^4 = 625$ computed directly (markers 4 and 5).

**7. Another way to get the coefficients: Pascal's triangle.** Output lines 7 to 11 build rows 1 to 5 by adding neighbours, script lines 9 to 12, and line 12 shows row 5 equal to $\binom{5}{k}$ from the formula (markers 6 to 8). Each row adds to $2^r$, the number of picks. Line 13 uses row 5 for $(x + 1)^5$ at $x = 2$: the six terms $32 + 80 + 80 + 40 + 10 + 1$ add to 243, which is $3^5$ (marker 9).

**8. More worked examples on the same script.**

*A negative second term, the handbook's $(2x - 3)^4$.* Output lines 16 and 17, script lines 17 to 19: the coefficients are $16, -96, 216, -216, 81$, signs alternating because $(-3)^k$ is negative for odd $k$. Putting $x = 1$ in turns the expansion into $(2 - 3)^4 = 1$, and the five coefficients add to 1 (markers 14 and 15). The handbook's last line on PDF p. 175 prints $144x^2$ where its own step 4 line, $(6)(4x^2)(9)$, gives $216x^2$; with 144 the coefficients add to $-71$ (marker 16), so the $x = 1$ check catches the misprint.

*The probability use.* Output line 18, script lines 20 and 21: $\binom{3}{k}\,0.25^k\,0.75^{3-k}$ for $k = 0$ to 3 gives $0.421875, 0.421875, 0.140625, 0.015625$, and they add to 1, which is $(0.25 + 0.75)^3 = 1^3$ (markers 17 and 18).

Run the script again and the same eighteen lines come back: nothing in it is random.

**9. Clean up, and prove it.**

```bash
cd ~ && rm -r ~/playground/sandbox/binomial-theorem
ls ~/playground/sandbox/binomial-theorem; echo $?
```

You should see `No such file or directory`, then `2`.

## Reading the binomial output

Navigation: ⬅️ [[#Try the binomial theorem yourself]] | 📋 [[#Table of contents|TOC]] | [[#How the binomial theorem works]] ➡️

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | term, $k = 0$ | `16` | $\binom{4}{0} \cdot 2^4 \cdot 3^0 = 1 \cdot 16 \cdot 1$: the one pick that took 2 from all four brackets | shown, and worked by hand below |
| 2 | $\binom{4}{1}$ | `4` | four ways to choose which one bracket gives the 3 | derived below |
| 3 | term, $k = 2$ | `216` | $6 \cdot 4 \cdot 9$: six picks with two 3s, each worth $2^2 \cdot 3^2 = 36$ | shown |
| 4 | the terms add to | `625` | $16 + 96 + 216 + 216 + 81$, the right side of the theorem | shown |
| 5 | $5^4$ | `625` | the left side, computed with no expansion; equal to field 4 | shown |
| 6 | Pascal row 5 | `[1, 5, 10, 10, 5, 1]` | built only by adding neighbours in row 4 | shown |
| 7 | row 5 adds to | `32 = 2^5` | every one of the $2^5$ picks counted once; $(1 + 1)^5$ | derived below |
| 8 | $\binom{5}{k}$ | `[1, 5, 10, 10, 5, 1]` | the factorial formula, equal to field 6 | shown |
| 9 | $(x + 1)^5$ at $x = 2$ | `243` | $32 + 80 + 80 + 40 + 10 + 1$, equal to $3^5$ | shown |
| 10 | slip, $2^2 + 3^2$ | `13` | the square with its middle term dropped | derived below |
| 11 | $(2 + 3)^2$ | `25` | the truth; field 11 minus field 10 is field 12 | shown |
| 12 | lost middle term | `12` | $2 \cdot 2 \cdot 3 = 2ab$, the two mixed picks | derived below |
| 13 | slip, $2^4 + 3^4$ | `97` | 528 short of 625: $96 + 216 + 216$ | derived below |
| 14 | $(2x - 3)^4$ coefficients | `[16, -96, 216, -216, 81]` | from $x^4$ down to $x^0$; the sign of $(-3)^k$ alternates | shown |
| 15 | at $x = 1$ | `1` | the coefficients add to $(2 - 3)^4 = 1$ | shown |
| 16 | with the misprint | `-71` | 144 in place of 216 moves the sum by $-72$ | shown |
| 17 | the four terms | `0.421875, 0.421875, 0.140625, 0.015625` | $\binom{3}{k}\,0.25^k\,0.75^{3-k}$ for $k = 0, 1, 2, 3$ | shown, and worked by hand below |
| 18 | they add to | `1.0` | $(0.25 + 0.75)^3 = 1$ | derived below |

## How the binomial theorem works

Navigation: ⬅️ [[#Reading the binomial output]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to expand a power of a sum]] ➡️

Textbook: [Algebra handbook, Binomial Expansion, four steps on $(2x - 3)^4$, PDF p. 175](../references/textbooks/algebra/algebra-handbook.pdf#page=175) · [Introduction to probability for data science, Theorem 1.2, PDF p. 22](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=22).

**What it is and why it is there.** Raising a sum to a power means multiplying the same bracket by itself, and multiplying brackets means taking one piece from each bracket in every possible way and adding the results. Many of those picks give the same product, so the theorem counts them instead of writing each one out. It is there because a power of a sum turns up wherever independent trials multiply, as in [[#When to reach for it]].

**Why the coefficients count choices.** Write the power as $n$ brackets and multiply them out by the [distributive property](../references/textbooks/algebra/algebra-handbook.pdf#page=16), [one pair of brackets at a time](../references/textbooks/algebra/algebra-handbook.pdf#page=62):

$$
\begin{aligned}
(a + b)^n &= \underbrace{(a + b)(a + b)\cdots(a + b)}_{n \text{ brackets}} \\
&= \text{the sum, over every way of taking } a \text{ or } b \text{ from each bracket, of the product taken} \\
\text{one pick that takes } b \text{ from } k \text{ brackets} &= \underbrace{a \cdots a}_{n-k}\;\underbrace{b \cdots b}_{k} = a^{n-k} b^k \\
\text{the number of such picks} &= \text{the ways to choose which } k \text{ of the } n \text{ brackets give } b = \binom{n}{k} \\
(a + b)^n &= \sum_{k=0}^{n} \binom{n}{k}\, a^{n-k} b^k
\end{aligned}
$$

Line 2 has $2^n$ picks in all, since each bracket offers two choices. Line 3 uses that multiplication can be done in any order, so only the count of $b$s matters. Line 5 groups the $2^n$ picks by that count. The picks are all counted once, so $\sum_k \binom{n}{k} = 2^n$, which is the theorem with $a = b = 1$. *Derived.*

Pascal's rule follows from one more bracket. $(a + b)^{n+1} = (a + b)^n (a + b)$, and a term $a^{n+1-k} b^k$ of the result comes from two places: a term of $(a + b)^n$ with $k$ $b$s times the new $a$, and a term with $k - 1$ $b$s times the new $b$. So its count is $\binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k}$, each entry the sum of the two above it. *Derived;* Chan proves the theorem by induction on this step, [PDF p. 25](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=25).

**A worked example: $(2 + 3)^4$ term by term.** Here $a = 2$, $b = 3$, $n = 4$. The coefficients are $\binom{4}{k} = \dfrac{24}{k!\,(4-k)!}$: $\dfrac{24}{1 \cdot 24} = 1$, $\dfrac{24}{1 \cdot 6} = 4$, $\dfrac{24}{2 \cdot 2} = 6$, $\dfrac{24}{6 \cdot 1} = 4$, $\dfrac{24}{24 \cdot 1} = 1$.

| $k$ | $\binom{4}{k}$ | $2^{4-k}$ | $3^k$ | term $= \binom{4}{k}\,2^{4-k}\,3^k$ | running sum |
|---|---|---|---|---|---|
| 0 | 1 | 16 | 1 | $1 \times 16 \times 1 = 16$ | 16 |
| 1 | 4 | 8 | 3 | $4 \times 8 \times 3 = 96$ | 112 |
| 2 | 6 | 4 | 9 | $6 \times 4 \times 9 = 216$ | 328 |
| 3 | 4 | 2 | 27 | $4 \times 2 \times 27 = 216$ | 544 |
| 4 | 1 | 1 | 81 | $1 \times 1 \times 81 = 81$ | 625 |

The sum is 625, and $(2 + 3)^4 = 5^4 = 5 \times 5 \times 5 \times 5 = 625$. The $3^0 = 1$ and $2^0 = 1$ in the first and last rows are the [zero exponent](../references/textbooks/algebra/algebra-handbook.pdf#page=109).

**A second worked example: $(x + 1)^5$ from Pascal's triangle.** Build the rows by adding neighbours, starting from row 0:

```text
row 0:          1
row 1:         1  1
row 2:        1  2  1
row 3:       1  3  3  1
row 4:      1  4  6  4  1
row 5:     1  5 10 10  5  1        1+4 = 5, 4+6 = 10, 6+4 = 10, 4+1 = 5
```

With $a = x$, $b = 1$ and every $1^k = 1$, the expansion is $(x + 1)^5 = x^5 + 5x^4 + 10x^3 + 10x^2 + 5x + 1$. At $x = 2$: $32 + 5 \times 16 + 10 \times 8 + 10 \times 4 + 5 \times 2 + 1 = 32 + 80 + 80 + 40 + 10 + 1 = 243 = 3^5$.

**The method, to redo on new numbers.** The handbook's four steps, with a check added.

1. Write the power as $(a + b)^n$ and read off $a$, $b$ (each with its sign) and $n$.
2. Write the $n + 1$ coefficients $\binom{n}{0}, \dots, \binom{n}{n}$: row $n$ of Pascal's triangle, or $\dfrac{n!}{k!\,(n-k)!}$.
3. Give the term with coefficient $\binom{n}{k}$ the factor $a^{n-k}$, the power counting down from $n$ to 0.
4. Give it the factor $b^k$, the power counting up from 0 to $n$. A negative $b$ carries its sign into every odd $k$, so the signs alternate.
5. Multiply each term's three factors and add the terms.
6. Check: compute $(a + b)^n$ directly from the numbers, or put $x = 1$ into an expansion in $x$, and compare with step 5. The coefficients alone must add to $2^n$.

**Where it goes wrong.** Dropping the coefficients, or the mixed terms with them. $(2 + 3)^2$ written as $2^2 + 3^2$ is $4 + 9 = 13$, against the true 25. The box below shows what went missing: the two mixed picks $2 \times 3$ and $3 \times 2$, together $2ab = 12$, and $13 + 12 = 25$.

```text
            2      3
     2  |   4  |   6  |
     3  |   6  |   9  |        4 + 6 + 6 + 9 = 25;   the diagonal alone, 4 + 9 = 13
```

The general form of the slip, $(a + b)^n = a^n + b^n$, keeps only the first and last terms. On $(2 + 3)^4$ it gives $16 + 81 = 97$ against 625, losing $96 + 216 + 216 = 528$, the three middle rows of the table above. It is true only when $n = 1$ or when $a$ or $b$ is 0. A wrong coefficient goes wrong more quietly: the handbook's printed $144x^2$ in place of $216x^2$ in $(2x - 3)^4$ looks plausible, and only a check finds it.

**Check it.** Two routes, each enough on its own.

- *Both sides as numbers.* The right side's terms add to 625 and the left side is $5^4 = 625$; for $(x + 1)^5$ at $x = 2$, 243 both ways. For $(2x - 3)^4$ at $x = 1$ the coefficients $16 - 96 + 216 - 216 + 81$ add to 1, which is $(2 - 3)^4$; with the misprint they add to $-71$.
- *The probability use.* With $a = 0.75$ and $b = 0.25$, the four terms of $(0.75 + 0.25)^3$ are

$$
\begin{aligned}
k = 0:&\quad \binom{3}{0}\,0.25^0\,0.75^3 = 1 \times 1 \times 0.421875 = 0.421875 \\
k = 1:&\quad \binom{3}{1}\,0.25^1\,0.75^2 = 3 \times 0.25 \times 0.5625 = 0.421875 \\
k = 2:&\quad \binom{3}{2}\,0.25^2\,0.75^1 = 3 \times 0.0625 \times 0.75 = 0.140625 \\
k = 3:&\quad \binom{3}{3}\,0.25^3\,0.75^0 = 1 \times 0.015625 \times 1 = 0.015625 \\
\text{sum}:&\quad 0.421875 + 0.421875 + 0.140625 + 0.015625 = 1 = (0.25 + 0.75)^3
\end{aligned}
$$

Each term is the chance of exactly $k$ successes in three independent tries that each succeed with probability 0.25: $\binom{3}{k}$ orders, each with chance $0.25^k\,0.75^{3-k}$. They add to 1 because the left side is $1^3$. *Cited:* Chan uses the theorem for this sum, $(p + (1 - p))^n = 1$, on [PDF p. 25](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=25), and motivates it with three coins on PDF p. 22. Every number above is output line 18 of the sandbox.

*🖼️ Diagram wanted: the mechanism, the 2 by 2 box of (2 + 3)^2 with its two mixed cells lit, beside Pascal's triangle rows 0 to 5 with each entry's two parents linked. Prompt 2 in the vault's `.prompts/The Binomial Theorem.md`.*

*🖼️ Diagram wanted: the deep-dive sheet composing the form, the mechanism, the (2 + 3)^4 table, the slip and the two checks. Prompt 3 in the same file.*

## Other ways to expand a power of a sum

Navigation: ⬅️ [[#How the binomial theorem works]] | 📋 [[#Table of contents|TOC]] | [[#Why the binomial theorem matters]] ➡️

- **Multiply the brackets out one at a time**, with the [FOIL or box method](../references/textbooks/algebra/algebra-handbook.pdf#page=62). Always right, and slow past $n = 3$: $(a + b)^4$ takes three rounds of multiplying and collecting.
- **Read the coefficients off Pascal's triangle** for small $n$, as in step 7 of the sandbox; it needs the rows above, and nothing else.
- **Use the factorial formula** for one coefficient deep in a large row, such as $\binom{20}{3} = \dfrac{20 \times 19 \times 18}{6} = 1140$, with no triangle. In Python, `math.comb(20, 3)` returns 1140; Chan, PDF p. 23, gives `scipy.special.comb` for the same.
- **Prove it by induction** instead of by counting picks: Chan's proof, PDF p. 25, assumes the case $n$, multiplies by one more $(a + b)$ and merges the two sums with Pascal's rule.

## Why the binomial theorem matters

Navigation: ⬅️ [[#Other ways to expand a power of a sum]] | 📋 [[#Table of contents|TOC]] | [[#The binomial theorem taught in, applied in]] ➡️

Counting successes in independent tries is a power of a sum. Three tries that each succeed with probability 0.25 give $(0.75 + 0.25)^3$, and the theorem splits it into the chances of 0, 1, 2 and 3 successes, 0.421875, 0.421875, 0.140625 and 0.015625, which add to 1. The [[Moment Generating Function#What the fingerprint is|moment generating function]] of such a count is a power of a sum of the same shape, so expanding it, or recognising it, uses this theorem. *Stated:* the writer's own knowledge; this note does not work that power.

## The binomial theorem taught in, applied in

Navigation: ⬅️ [[#Why the binomial theorem matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:** no learning-tree plan or chapter teaches it yet.

**Needed by:** the Moment Generating Function quiz, for its question on a sum of yes-or-no variables, listed as node N28 in [the quiz's coverage file](../Statistics/.quiz-prep/moment-generating-function-quiz.md).

> [!note]- How this was checked
> `binomial.py` was run on 2026-10-21 on mscluster (Linux), with Python 3.12.10 and the standard library only, by vault-writer, in the empty folder `~/playground/sandbox/binomial-theorem`. It was run twice and printed the same eighteen lines. The folder was removed afterwards and the clean-up check returned 2. The prepared environment `~/.vault-sandbox` is missing on this machine and was not needed. The terminal picture was rendered from the captured text by a script in DejaVu Sans Mono, never drawn, and opened before filing. The textbook pages were opened with PyMuPDF and read: the algebra handbook PDF pp. 16, 62, 109, 174 and 175, and Chan PDF pp. 22, 23, 25 and 51. The handbook's $144x^2$ misprint on PDF p. 175 was confirmed by rendering that page to an image: its step 4 line reads $(6)(4x^2)(9)$ and its final line reads $144x^2$. The hand tables were recomputed by the script, and `math.comb(20, 3)` was run separately and printed 1140. [Binomial theorem](https://en.wikipedia.org/wiki/Binomial_theorem) and [Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle) on Wikipedia (CC BY-SA 4.0) each answered 200 on 2026-10-21. No tldr-pages entry covers this.
