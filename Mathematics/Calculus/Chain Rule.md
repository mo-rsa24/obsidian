---
aliases: [chain rule, multivariable chain rule, chain rule of calculus]
link-skip: [chain rule of probability, probability chain rule, chain rule for KL, chain rule for entropy, chain rule for mutual information]
standard: vault-note v2
---

# Chain Rule

Up: [[Calculus]]

Mathematics, Calculus. [[Backpropagation]] applies it backward through a network, one layer at a time.

**The chain rule differentiates a composition: the derivative of f(g(x)) is f′(g(x)) times g′(x), so rates of change multiply along the chain.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the chain rule writes the rest around it.

## Where to learn this

**Chain rule**, the derivative of a composition as a product of derivatives. Also: multivariable chain rule.

**Textbooks**

- Calculus textbook, section 2.6: [pages 198 to 202](../references/textbooks/calculus/calculus-textbook.pdf#page=198). Why rates of change multiply (Figure 2.6.1), the theorem, and Example 1 differentiating cos(x³).
- Calculus textbook, section 13.5: [pages 973 to 983](../references/textbooks/calculus/calculus-textbook.pdf#page=973). The chain rule for functions of several variables, with tree diagrams (Figures 13.5.2 and 13.5.3) and implicit differentiation.
- Mathematics for machine learning, sections 5.1.2 to 5.2.2: [pages 151 to 154](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=151). Works h(x) = (2x + 1)⁴ to 8(2x + 1)³ (Example 5.5), then partial derivatives by the chain rule (Example 5.6) and the multivariate chain rule as a matrix product.
- Deep learning textbook, section 6.5.2: [pages 221 to 223](../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=221). The chain rule of calculus for scalars, vectors and tensors, as the step backpropagation repeats.
- Calculus handbook, chapter 2: [page 18](../references/textbooks/calculus/calculus-handbook.pdf#page=18). The chain rule in Leibniz, Lagrange and differential notation, beside the quotient and power rules.

**Videos**

- Stanford CS231n, lecture 4, 43:34 to 50:29: [watch](https://www.youtube.com/watch?v=25zD5qJHYsk&t=2614s). Backprops f = (x + y)z with x = −2, y = 5, z = −4, where the chain rule gives df/dx = df/dy = −4 from upstream and local gradients. Caption-read.
- Professor Leonard, Calculus 1 lecture 2.6, Discussion of the Chain Rule for Derivatives of Functions, Deriving the chain rule formula, 5:59 to 8:37: [watch](https://www.youtube.com/watch?v=8dr1dZjfhmc&t=359s). The formula derived from a composition of two functions. Chapter-timed.
- 3Blue1Brown, Visualizing the chain rule and product rule (Essence of calculus, chapter 4), Chain rule, 8:41 to 14:36: [watch](https://www.youtube.com/watch?v=YG15m2VwSjA&t=521s). The chain rule seen as small nudges passing through one function after another. Chapter-timed.
- Professor Leonard, Calculus 3 lecture 13.5, The Chain Rule for Multivariable Functions, 0:00 to 2:11:52: [watch](https://www.youtube.com/watch?v=tXryaM-mTpY&t=0s). A full lecture on the chain rule for functions of several variables. Whole video.

**Our plans and chapters**

- [Apply the chain rule through two and three steps by hand](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/09-apply-the-chain-rule-through-two.md), deep-learning/transformers, chapter 09. Two and three nested functions differentiated on paper, then checked in Python.
- [Chapter 4: Differentiate by hand, from slope to gradient to the chain rule](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/04-differentiating-by-hand.md), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 4. The chain rule as the last of three hand-differentiation steps, aimed at the gradient of a log density.
- [5. Itô's lemma](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/05-itos-lemma.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L3, section 5. What the ordinary chain rule gains when the path is Brownian.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after finding it through the chapter tables in `Textbooks.md` and the back-of-book tables in `~/.claude/cache/book-indexes/`. The Leonard and 3Blue1Brown chapter lists were read with cache-video-chapters.py, and those lines describe only the chapter and video titles; Leonard's 13.5 has no chapter list and is cited whole. The CS231n row was read in its caption-read lecture map under `~/.claude/cache/captions/`; CS229 lecture 8 (19:06 to 23:08) also sets up the chain rule for a module and has no line only to keep the list short. Each plan and chapter was read at its title and description. "chain rule" was sampled in the learning tree (20 lines, 5 meaning the chain rule of probability), so those phrases are in `link-skip`. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
