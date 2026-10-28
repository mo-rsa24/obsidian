---
aliases: [gradient, gradient vector]
link-skip: [linear-gradient, colour gradient, color gradient, gradient fill]
standard: vault-note v2
---

# Gradient

Up: [[Calculus]]

Mathematics, Calculus. [[Derivative]] is the one-input case, and [[Score Function]] is the gradient of a log density.

**The gradient of a function of several inputs is the vector of its partial derivatives, and it points in the direction the function increases fastest.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the gradient writes the rest around it.

## Where to learn this

**Gradient**, the vector of partial derivatives. Also: gradient vector.

**Textbooks**

- Mathematics for machine learning, section 5.2: [pages 152 to 154](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=152). Varies one input at a time to get partial derivatives, stacks them into the gradient, and computes one (Example 5.7).
- Calculus textbook, section 13.6: [pages 984 to 991](../references/textbooks/calculus/calculus-textbook.pdf#page=984). Directional derivatives, then the gradient (Definition 13.6.4, page 987) and why it points the way of fastest increase.
- Deep learning textbook, section 4.3: [pages 99 to 102](../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=99). The gradient as the vector of partial derivatives, the directional derivative, and steepest descent.
- Calculus handbook, chapter 11: [page 136](../references/textbooks/calculus/calculus-handbook.pdf#page=136). Scalar and vector fields, the del operator, and the gradient of a scalar field.

**Videos**

- The Organic Chemistry Tutor, 12:34 to 28:29: [watch](https://www.youtube.com/watch?v=CnVes9TdnPo&t=754s). Worked gradient problems. Chapter-timed, from the video lessons index.
- Leonard, Calculus 3, 13.6, 58:26 to 1:15:15: [watch](https://www.youtube.com/watch?v=tDPp5uWSIiU&t=3506s). The gradient defined, its properties, and why it points the way of fastest increase. Chapter-timed, from the video lessons index.
- Stanford CS231n, lecture 3, 26:53 to 29:25: [watch](https://www.youtube.com/watch?v=dyNGd06MWn4&t=1613s). The gradient as the vector of partial derivatives, the negative gradient as the steepest descent direction, and the numerical gradient from adding h = 0.00001 to each weight. Caption-read.
- Professor Dave, 2:09 to 9:36: [watch](https://www.youtube.com/watch?v=AXH9Xm6Rbfc&t=129s). Partial derivatives and the gradient as a vector, built up from a graph. Chapter-timed, from the video lessons index.

**Our plans and chapters**

- [Take a slope and the gradient of a function of two numbers](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/08-take-a-slope-and-the-gradient.md), deep-learning/transformers, chapter 08. The gradient of a squared loss in two numbers a and b, starting from a = 2 and b = 0.75.
- [From slope to gradient](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/05-from-slope-to-gradient.md), deep-learning/diffusion-models/01-poe-derivation-foundations, plan 05. The derivative as a slope, the partial derivative holding the rest fixed, and the gradient as the partials stacked.
- [The gradient field, drawn](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/06-the-gradient-field-drawn.md), the same journey, plan 06. The gradient drawn as arrows on a contour map, and the proof that gradients add.
- [The gradient as a field you can draw](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/02-the-gradient-as-a-field.md), deep-learning/diffusion-models/02-sampler-correctors-for-composition, plan 02. Eight arrows of a log density's gradient drawn by hand, then checked on a grid with NumPy.

**Scenes**

- [Kinds of composition notebook, 1. Example: same points, different labels](https://claude.ai/artifact/DBmJtn6xy75sPtQwPEvQZU#nb-sec2). The denoising loss and one gradient step, showing the gradient is identical under two labellings because no label enters the loss.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after finding it through the chapter tables in `Textbooks.md` and the back-of-book tables in `~/.claude/cache/book-indexes/`. The Organic Chemistry Tutor, Leonard and Professor Dave lines are copied from the video lessons index, section "The gradient". The CS231n row was read in its caption-read lecture map under `~/.claude/cache/captions/`. Each plan and chapter was read at its title and description. "gradient" alone was sampled in the learning tree (25 lines, all this idea), so it is an alias; "gradient of the log density" stays with [[Score Function]], whose longer alias wins. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
