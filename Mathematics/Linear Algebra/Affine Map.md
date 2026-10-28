---
aliases: [affine map, affine maps, affine mapping, affine mappings, affine transformation, affine transformations, affine function, translation vector, affine combination, affine combinations, affine subspace, affine subspaces, support point, affine space]
link-skip: [affine coupling, affine autoregressive, affine scalar bijection, affine flow]
sources:
  - "Deisenroth, Faisal and Ong, Mathematics for Machine Learning, Cambridge University Press 2020, section 2.8, Definition 2.25 (affine subspace, support point) and Definition 2.26 (affine mapping, translation vector): the vault's shelf copy, Mathematics/references/textbooks/machine-learning/mathematics-for-machine-learning.pdf, PDF pages 67 to 69; https://mml-book.com"
  - "Anton and Rorres, Elementary Linear Algebra, section 8.1 Example 8 (translation is not linear), the remark after Theorem 3.4.2 (a line through x0 as a translation), section 10.9 (the translation vector): the vault's shelf copy, Mathematics/references/textbooks/linear-algebra/linear-algebra-textbook.pdf, PDF pages 464, 179 and 612"
  - "The and-vector idea map, claim 1, and its measured norms, in the poe_repair_min research repository: /home/molef/PhD/poe_repair_min-dog-and-rain/artifacts/ideas/the-and-vector-as-a-third-expert/IDEA_MAP.md and artifacts/results/what-the-and-vector-is-made-of/a-cat-and-a-dog-norms.json"
standard: vault-note v2
---

# Affine Map

Up: [[Linear Algebra]] · ⬅️ [[Linear Map]] · [[Eigenvalue]] ➡️

Mathematics, Linear Algebra. Needs: [[Linear Map#What a linear map is|linear map]], the rule that passes every weighted sum through.

**An affine map is a linear map plus a fixed vector, so it passes a weighted sum through only when the weights add up to 1.**

> [!question]- Test yourself
> No quiz page covers this note yet.

> [!warning]- Unfinished
> - The three drawn pictures (the form, the mechanism and the deep-dive sheet) are waiting: prompts 1 to 3 in the vault's `.prompts/Affine Map.md`.
> - No quiz page for this note yet.

Claims marked stated: 1.

Colour key for every equation in this note: $\color{#1f6fb4}{\text{blue}}$ is the linear part $L$, $\color{#d9822b}{\text{orange}}$ is the offset $c$, $\color{#2e8b57}{\text{green}}$ are the weights $a_i$.

## Table of contents

- [[#Words this uses]]
- [[#What an affine map is]]
- [[#Affine combination]]
- [[#Support point]]
- [[#Try an affine map yourself]]
- [[#Reading the affine-map output]]
- [[#How an affine map works]]
- [[#Other ways to write an affine map]]
- [[#Why affine maps matter]]
- [[#Affine map taught in, applied in]]
- [[#Where to learn this]]

## Words this uses

Navigation: 📋 [[#Table of contents|TOC]] | [[#What an affine map is]] ➡️

**Linear part**, the [[Linear Map#What a linear map is|linear map]] $L$ inside an affine map $f(x) = L(x) + c$.

**Offset**, also the translation vector, the fixed vector $c$ an affine map adds after its linear part. It is $f(0)$.

**Affine combination**, a weighted sum $\sum_i a_i e_i$ whose weights add up to 1.

**Support point**, also the anchor point, the point $x_0$ that a subspace is shifted by to make an affine subspace $x_0 + U$.

## What an affine map is

Navigation: ⬅️ [[#Words this uses]] | 📋 [[#Table of contents|TOC]] | [[#Affine combination]] ➡️

Textbook: [Mathematics for machine learning, Definition 2.26, PDF p. 68](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=68) (it finishes on [PDF p. 69](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=69)) · [Linear algebra textbook, Example 8, Translation Is Not Linear, PDF p. 464](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=464)

**Affine map**, also an affine mapping or affine transformation: $f(x) = L(x) + c$, a linear map $L$ followed by adding a fixed vector $c$. Mathematics for Machine Learning writes it $\varphi(x) = a + \Phi(x)$ and calls $a$ the translation vector. *Cited:* Definition 2.26.

**When to reach for it.** Whenever a rule multiplies and then adds a constant: $y = 3x + 2$, a neural-network layer $Wx + b$, a change of units such as Celsius to Fahrenheit. Treating such a rule as linear lets you split any weighted sum through it, and that is wrong for every set of weights that does not add to 1.

### Affine

Affine is the word for "linear, up to where the origin sits". Shift every output by the same vector and a linear map becomes an affine one; nothing else about its shape changes. The line $y = 3x + 2$ is the line $y = 3x$ lifted by 2.

### All the words together: the formula

$$
f(x) = L(x) + c
$$

$$
f(x) \;=\; \underbrace{\color{#1f6fb4}{L(x)}}_{\text{linear part: passes every weighted sum through}} \;+\; \underbrace{\color{#d9822b}{c}}_{\text{offset: the same vector for every input}}
$$

**What the equation says.** Apply a linear map, then add one fixed vector. In one dimension with $L(x) = 3x$ and $c = 2$, the input 1 goes to $3 + 2 = 5$ and the input 3 goes to $9 + 2 = 11$.

**Why the offset is there.** It moves the whole picture off the origin. With it, $f(0) = 2$; without it, $L(0) = 0$ (output line 1 of the run below).

### The consequence: 0 goes to the offset

$f(0) = L(0) + c = 0 + c = c$. So an affine map is linear only when $c = 0$, because a linear map must send 0 to 0 ([[Linear Map#The consequence: 0 goes to 0]]). *Derived* here, and worked in the linear algebra textbook's [Example 8](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=464) for $T(x) = x + x_0$. The 1-D picture of an offset is the algebra handbook's vertical translation $f(x) + k$ ([PDF p. 33](../references/textbooks/algebra/algebra-handbook.pdf#page=33)).

*🖼️ Diagram wanted: the form, an input arrow going through the linear part and then shifted by the offset arrow c, with 0 landing on c. Prompt 1 in the vault's `.prompts/Affine Map.md`.*

## Affine combination

Navigation: ⬅️ [[#What an affine map is]] | 📋 [[#Table of contents|TOC]] | [[#Support point]] ➡️

**An affine map keeps exactly the weighted sums whose weights add up to 1.**

### Combination

A combination is a weighted sum $\sum_i a_i e_i$ of some vectors $e_i$. The weights $a_i$ can be any numbers: $0.5\,e_1 + 0.5\,e_2$ is the midpoint, and $e_1 - e_2$ is a difference.

### Affine, when the weights add up to 1

$$
f\Big(\sum_i a_i e_i\Big) = \sum_i a_i\, f(e_i) \qquad \text{when } \sum_i a_i = 1
$$

$$
\underbrace{\color{#1f6fb4}{L}\Big(\sum_i \color{#2e8b57}{a_i} e_i\Big) + \color{#d9822b}{c}}_{\text{mix, then map: the offset once}}
\;=\;
\underbrace{\color{#1f6fb4}{L}\Big(\sum_i \color{#2e8b57}{a_i} e_i\Big) + \Big(\sum_i \color{#2e8b57}{a_i}\Big)\color{#d9822b}{c}}_{\text{map, then mix: the offset } \sum a_i \text{ times}}
$$

**What the equation says.** Map each vector and mix the outputs, and the offset comes along once per weight, $\sum_i a_i$ times in all. Mixing first and mapping adds it exactly once, so the two agree when $\sum_i a_i = 1$.

**Why the sum of weights is there.** It counts how many offsets the mixed outputs carry. With $f(x) = 3x + 2$ and weights 0.5 and 0.5 on the inputs 1 and 3: $f(0.5 \cdot 1 + 0.5 \cdot 3) = f(2) = 8$, and $0.5 \cdot f(1) + 0.5 \cdot f(3) = 0.5 \cdot 5 + 0.5 \cdot 11 = 8$ (output line 2).

### The consequence: a difference loses the offset

When the weights add up to 0, the combination is a pure difference. It has no anchor point, and mapping each part and mixing gives $L(\sum_i a_i e_i)$ with the offset missing: $f(1) - f(3) = 5 - 11 = -6 = L(-2)$, while $f(1 - 3) = f(-2) = -4$ (output line 3). The gap is $-4 - (-6) = 2$, exactly the offset. A difference of outputs is a direction, and it needs an origin added back before it means a point.

<table>
<tr><th>weights</th><th>sum of weights</th><th>f(combination)</th><th>combination of f's</th><th>gap</th></tr>
<tr style="background:#eef7f1"><td>0.5, 0.5 on 1 and 3</td><td><b>1</b></td><td>f(2) = 8</td><td>0.5·5 + 0.5·11 = 8</td><td><b>0</b></td></tr>
<tr><td>1, −1 on 1 and 3</td><td><b>0</b></td><td>f(−2) = −4</td><td>5 − 11 = −6</td><td><b>2 = c</b></td></tr>
<tr><td>2, 3 on 1 and 3</td><td><b>5</b></td><td>f(11) = 35</td><td>2·5 + 3·11 = 43</td><td><b>−8 = (1 − 5)·c</b></td></tr>
</table>

**How to read this table.** Each row mixes the inputs 1 and 3 with the weights in its first column, through $f(x) = 3x + 2$. The last column is $f(\text{combination})$ minus the combination of outputs.

**What to look for.** The highlighted row, weights adding to 1, has no gap. Every other row is off by $(1 - \sum_i a_i)\,c$: one offset for the difference, and minus four offsets for weights adding to 5 (the row that [[Linear Map#What a linear map is]] met as 35 against 43).

![Two panels. Left: the line f(x) = 3x + 2 through f(1) = 5 and f(3) = 11, with f(2) = 8 marked as the midpoint of the outputs. Right: f(x) = 3x + 2 and the dashed L(x) = 3x, with f(-2) = -4 on the first and f(1) - f(3) = -6 = L(-2) on the second, a gap of 2|900](assets/affine-map-sum-one-and-sum-zero.svg)

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
f = lambda x: 3 * x + 2
L = lambda x: 3 * x
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.2))
for ax in (a1, a2):
    ax.axhline(0, color="#999", lw=0.8); ax.axvline(0, color="#999", lw=0.8)
    ax.set_xlabel("input x"); ax.set_ylabel("output")
xs = [-0.5, 4]
a1.plot(xs, [f(x) for x in xs], color="#d9822b", lw=2, label="f(x) = 3x + 2")
for x in (1, 3):
    a1.plot([x], [f(x)], "o", color="#d9822b"); a1.annotate(f"f({x}) = {f(x)}", (x, f(x)), (x + 0.15, f(x) - 1.6), fontsize=10)
a1.plot([2], [8], "s", color="#2e8b57", ms=9)
a1.annotate("weights 0.5, 0.5 (sum 1):\nf(2) = 8 = 0.5·5 + 0.5·11", (2, 8), (-0.4, 10.5), fontsize=10, color="#2e8b57",
            arrowprops=dict(arrowstyle="->", color="#2e8b57"))
a1.set_title("Sum 1: the midpoint's output is the midpoint of the outputs", fontsize=10)
a1.set_xlim(-0.5, 4); a1.set_ylim(-1, 15); a1.legend(loc="lower right", fontsize=9)
xs = [-3, 1]
a2.plot(xs, [f(x) for x in xs], color="#d9822b", lw=2, label="f(x) = 3x + 2")
a2.plot(xs, [L(x) for x in xs], color="#1f6fb4", lw=2, ls="--", label="L(x) = 3x, offset removed")
a2.plot([-2], [-4], "o", color="#d9822b"); a2.annotate("f(1 − 3) = f(−2) = −4", (-2, -4), (-2.95, -1.6), fontsize=10, color="#d9822b")
a2.plot([-2], [-6], "o", color="#1f6fb4"); a2.annotate("f(1) − f(3) = −6 = L(−2)", (-2, -6), (-1.7, -7.4), fontsize=10, color="#1f6fb4")
a2.annotate("", (-2.2, -4), (-2.2, -6), arrowprops=dict(arrowstyle="<->", color="#c0392b"))
a2.text(-2.95, -5.1, "gap 2 = c", color="#c0392b", fontsize=10)
a2.set_title("Sum 0: the difference of outputs has lost the offset", fontsize=10)
a2.set_xlim(-3, 1); a2.set_ylim(-9, 5); a2.legend(loc="upper left", fontsize=9)
fig.tight_layout(); fig.savefig("assets/affine-map-sum-one-and-sum-zero.svg")
```

**How to read this.** In both panels the x axis is the input and the y axis the output. On the left, one line, $f(x) = 3x + 2$, and the green square at input 2 sits exactly halfway between the outputs 5 and 11. On the right, the solid line is $f$ and the dashed one is $L$, the same map without its offset: the difference of outputs, −6, lands on the dashed line, 2 below $f(-2) = -4$.

## Support point

Navigation: ⬅️ [[#Affine combination]] | 📋 [[#Table of contents|TOC]] | [[#Try an affine map yourself]] ➡️

Textbook: [Mathematics for machine learning, Definition 2.25, PDF p. 67](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=67) · [Linear algebra textbook, a line through x₀ as a translation, PDF p. 179](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=179)

**An affine subspace is a subspace slid away from the origin by one point, its support point.**

**Affine subspace**: $x_0 + U = \{x_0 + u : u \in U\}$ for a subspace $U$ and a point $x_0$. Mathematics for Machine Learning calls $U$ the direction space and $x_0$ the support point. *Cited:* Definition 2.25.

$$
\underbrace{\color{#d9822b}{x_0}}_{\text{support point}} \;+\; \underbrace{\color{#1f6fb4}{U}}_{\text{a subspace through the origin}}
$$

**What the equation says.** Take every vector of a subspace, which always contains 0, and add the same point $x_0$ to each. The line through the origin in direction $(1, 2)$ becomes the line through $x_0$ in the same direction.

**Why the support point is there.** It is the subspace's 0, moved. The linear algebra textbook's remark on [PDF p. 179](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=179) says the same in its words: the line through $x_0$ is the translation by $x_0$ of the line through the origin. With $x_0 = (0, 2)$ and direction $(1, 3)$, the line $\{(t, 3t + 2)\}$ is the graph of $f(x) = 3x + 2$, the line $y = 3x$ lifted by its support point.

**The link to affine combinations.** The difference of two points on the lifted line, $(1, 5) - (3, 11) = (-2, -6)$, lies on the unlifted line $y = 3x$: subtracting removed the support point. A sum of points with weights adding to 1, such as $0.5\,(1, 5) + 0.5\,(3, 11) = (2, 8)$, stays on the lifted line. *Derived* here.

## Try an affine map yourself

Navigation: ⬅️ [[#Support point]] | 📋 [[#Table of contents|TOC]] | [[#Reading the affine-map output]] ➡️

**1. What you need.** Python 3.6 or later:

```bash
python3 --version
```

You should see a version line. This run printed `Python 3.12.3`.

**2. When it is missing.** Install Python 3 from python.org, or run `uv python install 3.12`. Not run on this machine, which already has it.

**3. Make something to act on.** Make an empty folder and go into it:

```bash
mkdir -p ~/playground/sandbox/affine-map && cd ~/playground/sandbox/affine-map
```

Save this as `affine.py`. Line 2 is the affine map $f(x) = 3x + 2$ and line 3 the same map without its offset. Lines 9 and 10 are an affine map on the plane, $F(v) = \begin{pmatrix}2 & 1\\ 0 & 1\end{pmatrix} v + (1, -1)$. Line 13 holds four made-up vectors that stand for four encoded prompts: the joint prompt, two single prompts and the empty prompt.

```python
# An affine map is a linear map plus a fixed offset. Which combinations does it keep?
f = lambda x: 3 * x + 2       # affine: the linear map 3x plus the offset c = 2
L = lambda x: 3 * x           # the same map with the offset taken away
print(f"f(0) = {f(0)}, L(0) = {L(0)}")
print(f"weights 0.5 + 0.5 = 1:  f(0.5*1 + 0.5*3) = f(2) = {f(0.5 * 1 + 0.5 * 3)};  0.5*f(1) + 0.5*f(3) = {0.5 * f(1) + 0.5 * f(3)}")
print(f"weights 1 - 1 = 0:      f(1 - 3) = f(-2) = {f(1 - 3)};  f(1) - f(3) = {f(1) - f(3)};  L(1 - 3) = {L(1 - 3)}")

# The same test on the plane, with four made-up vectors standing for four encoded prompts.
def F(v):                     # the matrix [[2, 1], [0, 1]] times v, plus the offset (1, -1)
    return (2 * v[0] + v[1] + 1, v[1] - 1)
def combo(ws, vs):            # the weighted sum w1*v1 + w2*v2 + ...
    return tuple(sum(w * v[i] for w, v in zip(ws, vs)) for i in range(2))
e = {"joint": (4, 1), "a": (1, 2), "b": (2, 0), "empty": (0, 1)}
vs = [e["joint"], e["a"], e["b"], e["empty"]]
for name, ws in (("x_fix", (1, -1, -1, 1)), ("x_aff", (1, -1, -1, 2))):
    print(f"{name}: weights {ws} sum to {sum(ws)};  F(combination) = {F(combo(ws, vs))};  combination of F's = {combo(ws, [F(v) for v in vs])}")

# Every prompt shares its first position, the start token's vector h.
h = (5, 7)
print(f"position 0:  x_fix = h - h - h + h = {combo((1, -1, -1, 1), [h] * 4)};  x_aff = h - h - h + 2h = {combo((1, -1, -1, 2), [h] * 4)}")
```

**4. A look before.** Run it:

```bash
python3 affine.py
```

You should see:

![Six numbered output lines: f(0) = 2 and L(0) = 0; weights summing to 1 give 8.0 both ways; weights summing to 0 give f(-2) = -4 against f(1) - f(3) = -6 = L(1 - 3); x_fix with weights summing to 0 gives F(combination) = (3, -1) against (2, 0); x_aff with weights summing to 1 gives (4, 0) both ways; position 0 gives x_fix = (0, 0) and x_aff = (5, 7)|1000](assets/affine-map-which-combinations-it-keeps.png)

Line 1 (script line 4) is the look before anything is mixed: the affine map sends 0 to its offset 2, and the linear part sends 0 to 0.

**5. The failure without the technique.** Line 3 (script line 6) splits a difference through $f$ as if $f$ were linear: $f(1) - f(3) = -6$, which is $L(-2)$, while the true $f(-2) = -4$. The offset is missing.

**6. The technique.** Line 2 (script line 5) uses weights that add to 1: both orders give 8.0.

**7. Another way to get the same answer.** Line 5 (script lines 15 and 16, the second pass) does the same on the plane with four vectors and the weights $(1, -1, -1, 2)$, which add to 1. The combination is $(4 - 1 - 2 + 0,\ 1 - 2 - 0 + 2) = (1, 1)$, and $F(1, 1) = (2 + 1 + 1,\ 1 - 1) = (4, 0)$, the same as mixing the four outputs.

**8. More worked examples on the same setup.**

*Weights adding to 0 on the plane.* Line 4 (the first pass of script lines 15 and 16) uses $(1, -1, -1, 1)$. The combination is $(1, 0)$, and $F(1, 0) = (3, -1)$, but mixing the outputs gives $(2, 0) = L(1, 0)$: the offset $(1, -1)$ is missing, as on the number line.

*A position every vector shares.* Line 6 (script lines 19 and 20) gives all four vectors the same value $h = (5, 7)$, as a prompt's start token does. Weights adding to 0 cancel it to $(0, 0)$, and weights adding to 1 keep it as $h$ itself.

**9. Clean up, and prove it.**

```bash
cd ~ && rm -r ~/playground/sandbox/affine-map
ls ~/playground/sandbox/affine-map; echo $?
```

You should see `No such file or directory`, then `2`.

## Reading the affine-map output

Navigation: ⬅️ [[#Try an affine map yourself]] | 📋 [[#Table of contents|TOC]] | [[#How an affine map works]] ➡️

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | `f(0)`, `L(0)` | `2`, `0` | the affine map sends 0 to its offset; its linear part sends 0 to 0 | shown, derived above |
| 2 | weights 0.5 and 0.5 | `8.0` and `8.0` | weights adding to 1: mix then map equals map then mix | shown, derived below |
| 3 | weights 1 and −1 | `-4`; `-6`; `-6` | $f(-2)$, then $f(1) - f(3)$, then $L(-2)$: the difference of outputs equals the linear part alone | shown, derived below |
| 4 | `x_fix`, weights adding to 0 | `(3, -1)` against `(2, 0)` | on the plane the gap is $(1, -1)$, the offset | shown, derived below |
| 5 | `x_aff`, weights adding to 1 | `(4, 0)` against `(4, 0)` | weights adding to 1 pass through on the plane too | shown, derived below |
| 6 | position 0 | `(0, 0)`; `(5, 7)` | a shared vector cancels under weights adding to 0 and survives once under weights adding to 1 | shown |

## How an affine map works

Navigation: ⬅️ [[#Reading the affine-map output]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to write an affine map]] ➡️

Map each vector, mix the outputs, and collect the offsets, one step per line:

$$
\begin{aligned}
\sum_i a_i\, f(e_i) &= \sum_i a_i \big(L(e_i) + c\big) \\
&= \sum_i a_i L(e_i) + \Big(\sum_i a_i\Big) c \\
&= L\Big(\sum_i a_i e_i\Big) + \Big(\sum_i a_i\Big) c && L \text{ is linear} \\
&= f\Big(\sum_i a_i e_i\Big) + \Big(\sum_i a_i - 1\Big) c && \text{since } f(x) = L(x) + c
\end{aligned}
$$

Line 3 is the only place linearity is used. Line 4 reads the whole result: the mixed outputs are the output of the mix plus $(\sum_i a_i - 1)$ extra offsets. Weights adding to 1 leave no extra; weights adding to 0 leave one missing offset, $-c$.

**The worked numbers, on the table above.** Weights 0.5 and 0.5: $(1 - 1) \cdot 2 = 0$, no gap. Weights 1 and −1: $(0 - 1) \cdot 2 = -2$, so the mixed outputs, −6, sit 2 below $f(-2) = -4$. Weights 2 and 3: $(5 - 1) \cdot 2 = 8$, so the mixed outputs, 43, sit 8 above $f(11) = 35$.

**The method, to redo on new numbers.**

1. Write the rule as $L(x) + c$ and read off $c = f(0)$.
2. Add up the weights of the combination.
3. If they add to 1, the combination passes through: $f(\sum a_i e_i) = \sum a_i f(e_i)$.
4. If not, the mixed outputs carry $(\sum a_i - 1)\,c$ beyond the output of the mix. For a difference, add $c$ back to the mixed outputs before reading them as a point.

*🖼️ Diagram wanted: the mechanism, four arrows mixed with weights 1, −1, −1 and 1 losing the offset, and with 1, −1, −1 and 2 keeping it once. Prompt 2 in the vault's `.prompts/Affine Map.md`.*

*🖼️ Diagram wanted: the deep-dive sheet composing the form, the mechanism and the run. Prompt 3 in the same file.*

## Other ways to write an affine map

Navigation: ⬅️ [[#How an affine map works]] | 📋 [[#Table of contents|TOC]] | [[#Why affine maps matter]] ➡️

- **One bigger matrix.** Append a 1 to every input and the offset becomes one more column: $\begin{pmatrix} A & c \\ 0 & 1 \end{pmatrix}\begin{pmatrix} x \\ 1 \end{pmatrix} = \begin{pmatrix} Ax + c \\ 1 \end{pmatrix}$. This is how computer graphics moves points by a translation vector, in the linear algebra textbook's section 10.9 ([PDF p. 612](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=612)). *Derived* here by multiplying out.
- **A composition.** Mathematics for Machine Learning writes it as a linear map followed by a translation, $\varphi = \tau \circ \Phi$, both uniquely determined ([PDF p. 69](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=69)).
- **For a random variable**, $Y = aX + b$ is the one-number case, and [[Scaling And Shifting A Random Variable]] works out what it does to a mean and a variance.

## Why affine maps matter

Navigation: ⬅️ [[#Other ways to write an affine map]] | 📋 [[#Table of contents|TOC]] | [[#Affine map taught in, applied in]] ➡️

Any argument that splits a model's output over a sum of inputs is an affine-combination argument once the model has a bias, which nearly every layer does. The weights have to add to 1 for the split to be exact, and a difference of outputs has to have an origin added back before it means anything.

**A worked instance from the poe_repair_min research project.** SDXL's text encoder turns a prompt into a 77 by 2048 sequence of vectors, $E(\text{prompt})$. A candidate "and" vector was $x_{\text{fix}} = E(\text{"a cat and a dog"}) - E(\text{"a cat"}) - E(\text{"a dog"}) + E(\text{""})$, with weights $+1, -1, -1, +1$ adding to 0. If the network's noise prediction $f$ were affine in its condition, the matching combination of its outputs would equal $L(x_{\text{fix}})$, the offset missing. The repaired $x_{\text{aff}} = E(\text{"a cat and a dog"}) - E(\text{"a cat"}) - E(\text{"a dog"}) + 2E(\text{""})$ has weights adding to 1, so under that same assumption $f(x_{\text{aff}}) = f(E_{\text{joint}}) - f(E_{\text{cat}}) - f(E_{\text{dog}}) + 2f(E_{\text{empty}})$ exactly, which the project's walk reads as the extra expert that turns a product of experts into the guided joint prompt. *Cited:* claim 1 of the and-vector idea map. The network is not affine in its condition, so this is the best guess the arithmetic offers, not a guarantee. *Stated*, from the same walk.

**The check the project could run.** CLIP's start token has the same hidden state $h$ in every prompt, so position 0 of $x_{\text{fix}}$ is $h - h - h + h = 0$ and position 0 of $x_{\text{aff}}$ is $h - h - h + 2h = h$, the same cancellation as line 6 of the sandbox. Measured on mscluster84 on 2026-10-28: position 0 of $x_{\text{fix}}$ has norm 0.000 on both of SDXL's text encoders, and the start token's own norm is 1190 on CLIP ViT-L (70.2 on OpenCLIP ViT-bigG). So $x_{\text{fix}}$ throws away a vector of length 1190 that every real prompt carries, and $x_{\text{aff}}$ keeps it.

## Affine map taught in, applied in

Navigation: ⬅️ [[#Why affine maps matter]] | 📋 [[#Table of contents|TOC]] | [[#Where to learn this]] ➡️

**Taught in:** no plan or chapter teaches it yet. Chapter 10 of the from-scratch-to-SDXL journey's stochastic-processes volume uses an affine combination, reading classifier-free guidance's score $w\,\nabla \log p(y \mid c) + (1 - w)\,\nabla \log p(y)$ as [an affine combination of two scores](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/10-annealing-on-three-axes-and-annealed-importance-sampling.md): the weights $w$ and $1 - w$ add to 1.

**Applied in:** the and-vector idea walk in the poe_repair_min research repository (`artifacts/ideas/the-and-vector-as-a-third-expert/IDEA_MAP.md`, claim 1). The candidate "and" vector cancelled the prompts' shared start token because its weights added to 0, which zeroed a vector of norm 1190 that every prompt carries; changing the empty prompt's weight from 1 to 2 made the weights add to 1 and kept that vector.

## Where to learn this

Navigation: ⬅️ [[#Affine map taught in, applied in]] | 📋 [[#Table of contents|TOC]]

**Affine map**, a linear map plus a fixed offset. Also: affine mapping, affine transformation, translation vector, affine combination, affine subspace, support point.

**Textbooks**

- Mathematics for machine learning, section 2.8, Definition 2.26: [pages 68 to 69](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=68). The affine mapping φ(x) = a + Φ(x), the translation vector a, and that every affine mapping is a linear mapping followed by a translation.
- Mathematics for machine learning, section 2.8.1, Definition 2.25: [page 67](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=67). The affine subspace L = x₀ + U with its support point x₀ and direction space U; lines, planes and hyperplanes follow on page 68.
- Linear algebra textbook, section 8.1, Example 8: [page 464](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=464). Translation is not linear, because a linear transformation sends 0 to 0 and T(x) = x + x₀ does not.
- Linear algebra textbook, section 3.4: [page 179](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=179). The line through x₀ is the translation by x₀ of the line through the origin, and the same for planes.
- Linear algebra textbook, section 10.9: [page 612](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=612). The translation vector that moves every point of a drawing by the same amount.
- Algebra handbook, transformations: [page 33](../references/textbooks/algebra/algebra-handbook.pdf#page=33). Vertical translation f(x) + k, the one-number picture of an offset, among the graph transformations.

**Our plans and chapters**

- [10. Annealing on three axes, and annealed importance sampling](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/10-annealing-on-three-axes-and-annealed-importance-sampling.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L3, chapter 10. Guidance's score as an affine combination of two scores, weights w and 1 − w.

> [!note]- How this was checked
> `affine.py` was run on 2026-10-28 on the PC (WSL2 Ubuntu), with Python 3.12.3 and the standard library only, by vault-writer, in the empty folder `~/playground/sandbox/affine-map` with `HOME` pointed at a scratch folder, so every command above ran byte for byte and nothing was written outside the vault. It was run twice and printed the same six lines. The folder was removed afterwards and the clean-up check returned 2. The 1-D arithmetic f(0) = 2, f(2) = 8 = 0.5 · 5 + 0.5 · 11 and f(−2) = −4 against f(1) − f(3) = −6 is that run's lines 1 to 3. The terminal picture was rendered from the captured text by a script in DejaVu Sans Mono, never drawn, and opened before filing. The figure script above was run with `~/.vault-sandbox/bin/python` (matplotlib 3.11.2) and its picture opened. Every textbook page was opened with pdftotext and read: MML PDF p. 67 (Definition 2.25), p. 68 (planes, hyperplanes, the start of Definition 2.26) and p. 69 (its end, the translation vector); the linear algebra textbook PDF p. 179 (the remark after Theorem 3.4.2), p. 464 (Example 8) and p. 612 (section 10.9, translation vector); the algebra handbook p. 33. No book on the shelf defines "affine combination" by name: the shelf search found it only in the journey chapter listed above, so that word carries no textbook line. The project numbers were read from `a-cat-and-a-dog-norms.json` (summary, position_0: x_fix 0.0 on both encoders, the joint prompt's start token 1190.04 on CLIP ViT-L and 70.19 on bigG); the 77 by 2048 shape and the start token being identical across prompts are cited from the idea map, claim 1. The vault's repository is public, so the project's outputs are described in words here and no project output or code is copied in. "offset" and "anchor point" are not aliases, because "offset" alone means a Kafka or pagination offset in most of the learning tree; both are found through this note's Words this uses block.
