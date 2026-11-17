---
aliases: [QuickGELU, quick GELU, GELU, Gaussian error linear unit]
standard: vault-note v2
---

# QuickGELU

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. The activation inside the [[Multilayer Perceptron]] of every CLIP [[Transformer]] block.

**QuickGELU multiplies a number x by sigmoid(1.702 x), which passes large positive numbers almost unchanged, sends very negative numbers to about 0 and bends smoothly in between; it is a cheaper stand-in for GELU, which multiplies x by the standard normal's cumulative probability Φ(x).**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the CLIP chapters need. The explanation beyond them is not written yet.
> - No file in the learning tree draws the QuickGELU curve itself yet; the picture below is the textbooks' plot of GELU and Swish, which QuickGELU sits on.
> - Why 1.702 makes sigmoid(1.702 x) follow Φ(x) is derived nowhere in the learning tree yet; the CLIP rebuild lists it as a gap.

## What the chapters need

**The picture.** Understanding deep learning's Figure 3.13 on [page 51](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=51) plots the smooth activations, GELU among them, beside ReLU, and Swish in panel f. Probabilistic machine learning: advanced topics, Figure 16.2 on [page 658](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=658), plots sigmoid, swish and GELU with their slopes.

**The idea.**

$$\mathrm{QuickGELU}(x) = x\cdot\frac{1}{1+e^{-1.702x}}$$

The sigmoid runs from 0 for very negative x to 1 for very positive x. So the product is about x when x is large, about 0 when x is very negative, and curves smoothly through 0 in between. The exact GELU is $x\,\Phi(x)$; QuickGELU swaps $\Phi(x)$ for $\sigma(1.702x)$, one exponential instead of the error function. Understanding deep learning's Swish, $x/(1+e^{-\beta x})$ on [page 52](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=52), is the same function with β left free; QuickGELU fixes β at 1.702 *(cited: [the CLIP rebuild, rung 3](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/rebuild-clip-from-fundamentals.md#rung-3-a-smooth-gate-that-lets-positive-numbers-through))*.

**Words the name uses.** *Quick*: the fast version, one sigmoid in place of Φ. *G*, Gaussian: the exact GELU multiplies x by Φ(x), the chance that a standard Gaussian draw falls below x. *E*, error: Φ is written with the Gauss error function, $\Phi(x)=\tfrac12\big[1+\mathrm{erf}(x/\sqrt2)\big]$. *LU*, linear unit: like the rectified linear unit (ReLU), its output is about x itself for large positive x.

**One number from the real model.** On the caption "a cat and a dog", 98.85 percent of the 77 × 2048 numbers entering QuickGELU in CLIP's first text block are negative, so most of them come out near 0. On those same inputs QuickGELU and the exact GELU differ by at most 0.0203 *(computed: the code walk's [rig.json](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/code-walk/what-each-line-of-clip-computes/pictures/rig.json), entry `quickgelu`)*. Both CLIP towers use it, and so does SDXL's first text encoder; SDXL's second, OpenCLIP bigG, uses the exact GELU *(read: journey 02's [CLIP numbers](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/clip_numbers.json), the `activation` and `hidden_act` entries)*.

## Where to learn this

**QuickGELU**, x times sigmoid(1.702 x), the fast form of GELU. Also: quick GELU, GELU, Gaussian error linear unit.

**Textbooks**

- Understanding deep learning, chapter 3 notes: [pages 51 to 52](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=51). Figure 3.13 plots the activation functions, and page 52 names the Gaussian error linear unit among the smooth ones and gives Swish, x/(1 + exp[−βx]), which is QuickGELU when β = 1.702.
- Probabilistic machine learning: advanced topics, section 16.2: [page 658](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=658). Table 16.1 lists sigmoid, swish aσ(a) and GELU aΦ(a) with their ranges, and Figure 16.2 plots them with their gradients.

**Videos**

- CS231n lecture 6, 16:17 to 21:47: [watch](https://www.youtube.com/watch?v=aVJy4O5TOk8&t=977s). GELU as x times the Gaussian CDF and SiLU as x times sigmoid(x), two smooth versions of ReLU used in transformers, after why sigmoid's slope vanishes. Caption-read.
- CS231n lecture 4, 17:11 to 21:23: [watch](https://www.youtube.com/watch?v=25zD5qJHYsk&t=1031s). Why a network needs an activation at all (without one, W2 W1 collapses to one matrix), then ReLU, leaky ReLU, ELU, GELU, SiLU, sigmoid and tanh compared. Caption-read.
- CS229 lecture 7, 54:30 to 58:07: [watch](https://www.youtube.com/watch?v=fRM41w9jzQo&t=3270s). Sigmoid, tanh, leaky ReLU and GELU listed as other activations applied one number at a time. Caption-read.

**Our plans and chapters**

- [The CLIP rebuild, rung 3: a smooth gate that lets positive numbers through](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/rebuild-clip-from-fundamentals.md#rung-3-a-smooth-gate-that-lets-positive-numbers-through), papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers, beside the CLIP paper. `model.py` line 168, x · sigmoid(1.702 x), against the exact GELU, with the share of negative inputs in CLIP's first text block.
- [Compute exp and log by hand](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/01-compute-exp-and-log-by-hand.md#exp-and-log), deep-learning/transformers, chapter 01. The exponential inside the sigmoid, worked by hand.

**Scenes**

- [CLIP code walk, Hidden: QuickGELU](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#gelu). X times sigmoid(1.702 x), the activation inside every block's MLP.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-17. Each textbook page was read in the PDF with pdftotext, first found through the back-of-book tables in `~/.claude/cache/book-indexes/` ("GELU", "GeLU", "activation function, GeLU"). The three video rows were read in the caption-read lecture maps under `~/.claude/cache/captions/`. No paper on the shelf defines GELU or QuickGELU, so there is no papers group. The transformers journey has no chapter on activations. The worked number was read from `rig.json`, whose `quickgelu` entry measures the gap on the 77 × 2048 inputs of the first text block's MLP, and the activation names from `clip_numbers.json`. "QuickGELU" is matched only in that spelling. A script then opened every link.
