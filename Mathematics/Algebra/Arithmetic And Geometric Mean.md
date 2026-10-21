---
aliases: [AM-GM, AM-GM inequality, AM GM, arithmetic mean geometric mean inequality, inequality of arithmetic and geometric means, arithmetic mean, geometric mean, GM over AM]
sources:
  - "Algebra Handbook, version 3.5, October 2022, chapter 19, page 169, the arithmetic and geometric means: the vault's shelf copy, Mathematics/references/textbooks/algebra/algebra-handbook.pdf"
  - "Rao and Callison-Burch, agreement metrics for LLM judges, section 4.2, https://arxiv.org/abs/2606.00093"
---

# Arithmetic And Geometric Mean

Up: [[Algebra]] · ⬅️ [[Logarithms]] · [[The Binomial Theorem]] ➡️

Mathematics, Algebra. Needs: squares and square roots of positive numbers, and the two inequality moves of adding the same number to both sides and dividing both sides by a positive number.

> [!question] Test yourself
> No quiz page covers this note yet. The [Judge Agreement Quiz](https://claude.ai/artifact/RthoGPnogcnYFtTDMgPvqM) asks the question that sends a reader here: why $q \le 1$.

> [!warning] Unfinished
> - The three drawn pictures (form, mechanism, deep-dive sheet) are not drawn, and no output picture is rendered: `~/.vault-sandbox` is missing on this machine, so there was no plotting library. To make it: `uv venv ~/.vault-sandbox` then `uv pip install --python ~/.vault-sandbox/bin/python pandas numpy scipy matplotlib statsmodels openpyxl`.
> - No quiz page for this note yet.

**The arithmetic mean of two positive numbers is never smaller than their geometric mean, and the two are equal exactly when the numbers are equal.** This note proves that from the fact that a squared number is never negative, runs it on small numbers, and then uses it on the factor $q$ that links Cohen's kappa to phi.

**Where you work.** Any folder with Python 3. Nothing is installed; the script uses the standard library only.

## Table of contents

- [What it is and why it is here](#what-it-is-and-why-it-is-here)
- [Worked example on small numbers](#worked-example-on-small-numbers)
- [The proof for two numbers](#the-proof-for-two-numbers)
- [Using it on q](#using-it-on-q)
- [Where it goes wrong](#where-it-goes-wrong)
- [Check it with a script](#check-it-with-a-script)
- [Other ways](#other-ways)
- [Taught in, applied in](#taught-in-applied-in)
- [How this was checked](#how-this-was-checked)
- [Videos](#videos)

## What it is and why it is here

Navigation: 📋 [[#Table of contents]] | [[#Worked example on small numbers]] ➡️

Textbook: [Algebra handbook, ch. 19, p. 169, the arithmetic and geometric means](../references/textbooks/algebra/algebra-handbook.pdf#page=169)

**Arithmetic mean**, also the average: add the two numbers and halve the sum, $\frac{a+b}{2}$. **Geometric mean**: multiply the two numbers and take the square root of the product, $\sqrt{ab}$. Both are a "middle" of $a$ and $b$, and the inequality says which middle is larger.

A picture in numbers: take a rectangle with sides 2 and 8. Its area is $2 \cdot 8 = 16$ and its perimeter is $2 + 8 + 2 + 8 = 20$. The geometric mean is the side of the square with the same area, $\sqrt{16} = 4$. The arithmetic mean is the side of the square with the same perimeter, $\frac{2+8}{2} = 5$, since $4 \cdot 5 = 20$. That second square has area $5 \cdot 5 = 25$, larger than the rectangle's 16, and $5 \ge 4$. The proof below shows this holds for every pair, not only for 2 and 8.

**Why it is here.** In [[Phi And Q]], Cohen's kappa equals phi times $q = \frac{2\sqrt{AB}}{A+B}$. Dividing the top and bottom of $q$ by 2 turns it into the geometric mean of $A$ and $B$ over their arithmetic mean. The inequality is what makes $q$ at most 1, and the equality case says when $q$ is exactly 1.

**Why this matters.** Without the inequality there is no ceiling on $q$, so nothing says kappa cannot be larger than phi. With it, $q \le 1$ and kappa is never larger than phi in size. Backing: derived (the proof below), shown (the run).

## Worked example on small numbers

Navigation: ⬅️ [[#What it is and why it is here]] | 📋 [[#Table of contents]] | [[#The proof for two numbers]] ➡️

**Two and eight.** Every value, in the order the proof will use them.

| Step | Value |
|---|---|
| $\sqrt{2}$ | 1.41421 |
| $\sqrt{8}$ | 2.82843 |
| $\sqrt{2} - \sqrt{8}$ | $-1.41421$ |
| $(\sqrt{2} - \sqrt{8})^2$ | 2.00000, not negative |
| $a + b$ | $2 + 8 = 10$ |
| $ab$ and $\sqrt{ab}$ | $16$ and $4$ |
| $2\sqrt{ab}$ | $8$ |
| $a + b - 2\sqrt{ab}$ | $10 - 8 = 2$, the same number as the square above |
| arithmetic mean | $10 / 2 = 5$ |
| geometric mean | $4$ |
| arithmetic mean minus geometric mean | $5 - 4 = 1$, half of the 2.00000 above |

**The learner's numbers, 34 and 54**, the two products $A$ and $B$ of the 20-product table in [[Phi And Q]].

| Step | Value |
|---|---|
| $a + b$ | $34 + 54 = 88$ |
| $ab$ | $34 \cdot 54 = 1836$ |
| $\sqrt{ab}$ | $\sqrt{1836} = 42.849$ |
| $2\sqrt{ab}$ | $85.697$ |
| $(\sqrt{34} - \sqrt{54})^2 = a + b - 2\sqrt{ab}$ | $88 - 85.697 = 2.303$, not negative |
| arithmetic mean | $88 / 2 = 44$ |
| geometric mean | $42.849$ |
| arithmetic mean minus geometric mean | $44 - 42.849 = 1.151$, half of 2.303 |
| geometric mean over arithmetic mean | $42.849 / 44 = 0.9738$ |

## The proof for two numbers

Navigation: ⬅️ [[#Worked example on small numbers]] | 📋 [[#Table of contents]] | [[#Using it on q]] ➡️

Textbook: [Algebra handbook, ch. 7, p. 42, the addition and division properties of inequalities](../references/textbooks/algebra/algebra-handbook.pdf#page=42). That page teaches the two moves in steps 4 and 5. It does not teach this inequality, and the handbook's chapter 19 (p. 169) only defines the two means.

Let $a \ge 0$ and $b \ge 0$, so that $\sqrt{a}$ and $\sqrt{b}$ are real numbers.

1. A real number multiplied by itself is never negative: positive times positive is positive, negative times negative is positive, and zero times zero is zero. Apply that to the real number $\sqrt{a} - \sqrt{b}$:
$$
(\sqrt{a} - \sqrt{b})^2 \ge 0
$$
2. Multiply the bracket out, term by term:
$$
(\sqrt{a} - \sqrt{b})(\sqrt{a} - \sqrt{b}) = \sqrt{a}\sqrt{a} - \sqrt{a}\sqrt{b} - \sqrt{b}\sqrt{a} + \sqrt{b}\sqrt{b}
$$
3. Replace $\sqrt{a}\sqrt{a}$ by $a$ and $\sqrt{b}\sqrt{b}$ by $b$ (that is what a square root is), and replace $\sqrt{a}\sqrt{b}$ by $\sqrt{ab}$ in both middle terms:
$$
a - 2\sqrt{ab} + b \ge 0
$$
4. Add $2\sqrt{ab}$ to both sides. The inequality keeps its direction:
$$
a + b \ge 2\sqrt{ab}
$$
5. Divide both sides by 2, a positive number, so the direction is kept again:
$$
\frac{a + b}{2} \ge \sqrt{ab}
$$
That is the arithmetic mean at least the geometric mean.

**When they are equal.**

6. Steps 3 to 5 only added or divided by numbers, and each can be undone by subtracting or multiplying by the same number. So the two sides of step 5 are equal exactly when the two sides of step 1 are equal, which is when $(\sqrt{a} - \sqrt{b})^2 = 0$.
7. A product of two numbers is zero only when one of them is zero, so a square is zero only when the number is zero: $\sqrt{a} - \sqrt{b} = 0$, which is $\sqrt{a} = \sqrt{b}$.
8. Square both sides: $a = b$. In the other direction, $a = b$ gives $\sqrt{a} - \sqrt{b} = 0$. So the arithmetic and geometric means are equal exactly when $a = b$.

Backing: derived (the eight lines). The addition and division moves in steps 4 and 5 are cited to the handbook page above.

## Using it on q

Navigation: ⬅️ [[#The proof for two numbers]] | 📋 [[#Table of contents]] | [[#Where it goes wrong]] ➡️

**$q$ is the geometric mean of $A$ and $B$ over their arithmetic mean.** Steps, with $A > 0$ and $B > 0$:

1. Start from $q = \frac{2\sqrt{AB}}{A+B}$.
2. Divide the top and the bottom by 2:
$$
q = \frac{\sqrt{AB}}{(A+B)/2} = \frac{\text{geometric mean of } A, B}{\text{arithmetic mean of } A, B}
$$
3. The proof above gives $\frac{A+B}{2} \ge \sqrt{AB}$. Divide both sides by $\frac{A+B}{2}$, which is positive:
$$
1 \ge \frac{\sqrt{AB}}{(A+B)/2} = q
$$
4. The top and bottom of $q$ are both positive, so $q > 0$.
5. By step 8 of the proof, $q = 1$ exactly when $A = B$.

On the learner's numbers $A = 34$ and $B = 54$: $q = 42.849 / 44 = 0.9738$, which is below 1 because $34 \ne 54$. What $A = B$ means for the judge and the reviewer is worked in [[Phi And Q#What q records]].

## Where it goes wrong

Navigation: ⬅️ [[#Using it on q]] | 📋 [[#Table of contents]] | [[#Check it with a script]] ➡️

**The inequality never fails for non-negative numbers. What goes wrong is using one mean as a stand-in for the other.**

**Far apart.** With $A = 1$ and $B = 100$ the arithmetic mean is $50.5$ and the geometric mean is $10$, a gap of $40.5$, and $q = 10 / 50.5 = 0.1980$. A reader who treats "the middle of 1 and 100" as 50.5 is off from the geometric mean by a factor of five.

**Equal.** With $A = B = 40$ the arithmetic mean is $40$, the geometric mean is $\sqrt{1600} = 40$, the gap is $0$ and $q = 1.0000$. This is the only case where $q$ reaches 1.

**Negative numbers.** Step 1 needs $\sqrt{a}$ and $\sqrt{b}$ to be real, so $a, b \ge 0$ is required. With $a = -1$ and $b = -9$ the arithmetic mean is $-5$ and $\sqrt{ab} = \sqrt{9} = 3$, so the arithmetic mean is the smaller one and the inequality fails.

## Check it with a script

Navigation: ⬅️ [[#Where it goes wrong]] | 📋 [[#Table of contents]] | [[#Other ways]] ➡️

**By hand first.** For 2 and 8 the arithmetic mean is 5 and the geometric mean is 4. For 34 and 54 they are 44 and 42.849. In both, the gap equals half of $(\sqrt{a} - \sqrt{b})^2$: 1 and 1.151.

**Try it yourself.**

1. What you need: Python 3.10 or later. Check with `python3 --version`. You should see a line such as `Python 3.12.14`.
2. If it is missing: install Python 3 from python.org, or with `uv python install 3.12`. Not run on this machine, which already has it.
3. Setup: an empty folder to work in.

```bash
mkdir am_gm_demo && cd am_gm_demo
```

4. Save this as `am_gm.py`:

```python
from math import sqrt
import random


def means(a, b):
    return (a + b) / 2, sqrt(a * b)


print("a, b, arithmetic mean, geometric mean, gap, half of (sqrt a - sqrt b)^2")
for a, b in [(2, 8), (34, 54), (1, 100), (40, 40)]:
    am, gm = means(a, b)
    half_square = (sqrt(a) - sqrt(b)) ** 2 / 2
    print(f"{a:>3} {b:>3}  AM {am:7.4f}  GM {gm:7.4f}  gap {am - gm:7.4f}  half-square {half_square:7.4f}")

print()
print("q = 2 sqrt(AB) / (A + B), and the same number as GM / AM")
for A, B in [(34, 54), (1, 100), (40, 40)]:
    q = 2 * sqrt(A * B) / (A + B)
    am, gm = means(A, B)
    print(f"A {A:>3}  B {B:>3}  q {q:.4f}  GM/AM {gm / am:.4f}")

print()
random.seed(0)
smallest = min(
    (a + b) / 2 - sqrt(a * b)
    for a, b in ((random.uniform(0, 1000), random.uniform(0, 1000)) for _ in range(100000))
)
print(f"smallest AM - GM over 100000 random pairs in [0, 1000]: {smallest:.6f}")

a, b = -1, -9
print(f"negative inputs a={a} b={b}: AM {(a + b) / 2}, sqrt(ab) {sqrt(a * b)}, AM >= GM is {(a + b) / 2 >= sqrt(a * b)}")
```

5. Run it:

```bash
python3 am_gm.py
```

You should see:

```text
a, b, arithmetic mean, geometric mean, gap, half of (sqrt a - sqrt b)^2
  2   8  AM  5.0000  GM  4.0000  gap  1.0000  half-square  1.0000
 34  54  AM 44.0000  GM 42.8486  gap  1.1514  half-square  1.1514
  1 100  AM 50.5000  GM 10.0000  gap 40.5000  half-square 40.5000
 40  40  AM 40.0000  GM 40.0000  gap  0.0000  half-square  0.0000

q = 2 sqrt(AB) / (A + B), and the same number as GM / AM
A  34  B  54  q 0.9738  GM/AM 0.9738
A   1  B 100  q 0.1980  GM/AM 0.1980
A  40  B  40  q 1.0000  GM/AM 1.0000

smallest AM - GM over 100000 random pairs in [0, 1000]: 0.000000
negative inputs a=-1 b=-9: AM -5.0, sqrt(ab) 3.0, AM >= GM is False
```

6. Clean up, and prove it is gone by running the listing again:

```bash
cd .. && rm -r am_gm_demo && ls am_gm_demo
```

```text
ls: am_gm_demo: No such file or directory
```

**Reading the output.**

| Field | Value in this run | How to read it | Backing |
|---|---|---|---|
| `AM`, `GM` | 44.0000, 42.8486 for 34 and 54 | the arithmetic and geometric means | shown |
| `gap` | 1.1514 | $AM - GM$, never negative | shown, derived |
| `half-square` | 1.1514 | half of $(\sqrt{a} - \sqrt{b})^2$, the same number as the gap | derived in the proof, steps 1 to 5 |
| `q`, `GM/AM` | 0.9738 twice | $q$ and the ratio of the means are one number | derived in [[#Using it on q]] |
| `smallest AM - GM` | 0.000000 | over 100000 random pairs the gap is never negative | shown |
| negative inputs | `AM >= GM is False` | the inequality needs $a, b \ge 0$ | shown |

**Why this matters.** The run is the same claim as the proof on 100000 pairs, so a slip in the algebra would show as a negative gap.

## Other ways

Navigation: ⬅️ [[#Check it with a script]] | 📋 [[#Table of contents]] | [[#Taught in, applied in]] ➡️

**More than two numbers.** The handbook (p. 169) defines both means for $n$ values. The proof here covers two numbers only. **The harmonic mean**, the third classical mean, is defined on the next page (p. 170) and is not used here.

## Taught in, applied in

Navigation: ⬅️ [[#Other ways]] | 📋 [[#Table of contents]] | [[#How this was checked]] ➡️

**Taught in.**

- [Step 5 of the worked example for validating an LLM judge](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/drips/combine-validating-an-llm-judge/checks/worked-example-latex.md#step-5-raos-identity-kappa--q-times-phi), which states $q \le 1$ and leaves the inequality unproved.
- [Rao and Callison-Burch, section 4.2](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/sources/agreement-metrics-for-llm-judges/paper/2606.00093.pdf#page=5), which cites the inequality in one clause (PDF page 5).

**Applied in.**

- [[Phi And Q#The method in numbered steps]]: the factor linking kappa to phi is at most 1, and equals 1 when a judge and a reviewer pass at the same rate.
- [[Chance-Corrected Agreement#q]]: the summary of the same fact on the 20-product table.

## How this was checked

Navigation: ⬅️ [[#Taught in, applied in]] | 📋 [[#Table of contents]] | [[#Videos]] ➡️

> [!note]- How this was checked
> `am_gm.py` was run on 2026-10-18 on a Mac with Python 3.12.14, standard library only, from an empty folder that was removed afterwards, the listing then failing as shown. A rerun gave the same output. The prepared environment `~/.vault-sandbox` is missing on this machine and was not needed. The algebra handbook pages 42, 169 and 170 were opened and read as text: page 42 lists the addition and division properties of inequalities and does not mention the arithmetic-geometric mean inequality; pages 169 and 170 define the arithmetic, geometric and harmonic means and state no inequality between them. Rao and Callison-Burch's use of the inequality was read on PDF page 5. The page has not been rendered in Obsidian. No claim is marked stated.

## Videos

Navigation: ⬅️ [[#How this was checked]] | 📋 [[#Table of contents]]

<!-- video-table: am-gm-two-numbers rev=1 -->
MathOdyssey, then David Metzler, both from the open web, on the proof that (a + b)/2 is at least the square root of ab, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Subtract the geometric mean from the arithmetic mean, write a and b as squares of their roots, and the difference becomes (root a minus root b) squared over 2, which cannot be negative; equality only when a equals b | Proof, open web | [MathOdyssey, Proof of AM-GM for two positive numbers, 0:16 to 3:05](https://www.youtube.com/watch?v=8sMtm9JfMfI&t=16s) |
| 2 | Square both sides to find a hint, reach (a minus b) squared at least 0, then run the steps forwards as the proof | Proof, open web | [Metzler, Proof example: AM-GM Inequality, 4:35 to 7:58](https://www.youtube.com/watch?v=MVSmvLyowt0&t=275s) |

No listed creator proves the inequality, and no worked example with numbers was found. Metzler also shows how to find the proof (1:20 to 4:35) and proves that square roots keep an inequality (8:13 to 9:51). Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->
