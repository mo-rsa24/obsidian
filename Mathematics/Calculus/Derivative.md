---
aliases: [derivative, second derivative, instantaneous rate of change]
link-skip: [financial derivative, derivative instrument, derivatives market, primary-image derivative, image derivative, Radon-Nikodym derivative]
standard: vault-note v2
---

# Derivative

Up: [[Calculus]]

Mathematics, Calculus. [[Gradient]] stacks the derivatives of a function of several inputs, and [[Chain Rule]] differentiates a composition.

**The derivative of a function at a point is the slope of its tangent line there, the limit of the rise over the run as the run shrinks to zero.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the derivative writes the rest around it.

## Where to learn this

**Derivative**, the slope of a function at a point. Also: second derivative, instantaneous rate of change.

**Textbooks**

- Calculus textbook, section 2.2: [pages 167 to 178](../references/textbooks/calculus/calculus-textbook.pdf#page=167). Defines the derivative function as a limit and works it for x² and other functions, then differentiability.
- Calculus textbook, section 2.1: [pages 155 to 166](../references/textbooks/calculus/calculus-textbook.pdf#page=155). The slope of the tangent line to a parabola (Example 1) and a particle's instantaneous velocity (Example 5), the two pictures the derivative comes from.
- Mathematics for machine learning, section 5.1: [pages 147 to 151](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=147). The derivative as the limit of a secant's slope (Figure 5.3), the derivative of a polynomial (Example 5.2), Taylor series and the differentiation rules.
- Calculus handbook, chapter 2: [page 17](../references/textbooks/calculus/calculus-handbook.pdf#page=17). The definition of a derivative and the basic rules on one page.

**Videos**

- Professor Leonard, Calculus 1 lecture 2.1, Introduction to the Derivative of a Function, Derivative calculation example, 5:34 to 16:01: [watch](https://www.youtube.com/watch?v=962lLfW-8Jo&t=334s). A derivative calculated from the definition as a worked example. Chapter-timed.
- Professor Leonard, Calculus 1 lecture 2.1, Introduction to the Derivative of a Function, Introduction to derivatives, 0:00 to 5:34: [watch](https://www.youtube.com/watch?v=962lLfW-8Jo&t=0s). What a derivative is, at the start of his first derivative lecture. Chapter-timed.
- 3Blue1Brown, The paradox of the derivative (Essence of calculus, chapter 2), Defining the derivative, 4:32 to 6:19: [watch](https://www.youtube.com/watch?v=9vKqVkMQHKk&t=272s). The derivative defined through a car's changing distance. Chapter-timed.
- tilestats, Understanding derivatives: the basics, 0:00 to 8:57: [watch](https://www.youtube.com/watch?v=rs2ZQeIjwhM&t=0s). A nine-minute introduction to derivatives. Whole video.

**Our plans and chapters**

- [Find a maximum by setting a derivative to zero, and check it](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/20-derivatives-and-maxima.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 20. The derivative of θ³(1 − θ), the likelihood of HHHT, set to zero and checked.
- [Read a slope and a derivative off 1 − d/L](/home/molef/goal-setting/learning/ai-engineering/string-similarity-measures/foundations/plans/07-a-calculus-primer-slope-and-the-derivative.md), ai-engineering/string-similarity-measures/foundations, plan 07. The derivative d/L² explains why short names are more sensitive to one edit.
- [Chapter 4: Differentiate by hand, from slope to gradient to the chain rule](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/04-differentiating-by-hand.md), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 4. The derivative as the first step toward the gradient of a sum of log-densities.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after finding it through the chapter tables in `Textbooks.md` and the back-of-book tables in `~/.claude/cache/book-indexes/`. The Leonard, 3Blue1Brown and tilestats chapter lists were read with cache-video-chapters.py, and those lines describe only the chapter and video titles; the tilestats video has no chapter list and is cited whole. Each plan and chapter was read at its title and description. "derivative" alone was sampled in the learning tree (25 lines, 21 meaning this idea; the rest were product-image derivatives and the Radon-Nikodym derivative of path measures). No finance file uses "derivative" yet; "financial derivative" and its neighbours are in `link-skip` for when one does. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
