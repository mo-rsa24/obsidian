---
aliases: [statistical independence, independence, independent events, independent random variables, statistically independent, mutually independent, independent and identically distributed]
link-skip-in: [finance/]
link-skip: [Parametrization Independence]
standard: vault-note v2
---

# Statistical Independence

Up: [[Probability]]

Mathematics, Statistics, Probability. Two of its consequences already have notes: [[The Average Of A Product Of Independent Variables]] and [[Sums Of Independent Gaussians]]. [[Conditional Independence]] is the same idea inside each slice of a third variable.

**Two events or random variables are independent when knowing one tells you nothing about the other, so the probability of both is the product of their separate probabilities.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches independence writes the rest around it.

## Where to learn this

**Statistical independence**, P(A ∩ B) = P(A) P(B). Also: independence, independent events, independent random variables.

**Textbooks**

- Introduction to statistics (Wits lecture notes), section 3.7.4: [pages 70 to 71](../../references/textbooks/statistics/introduction-to-statistics.pdf#page=70). Works with numbers: the product rule for independent events, with a man promoted with probability 0.3 and his wife, at another firm, with 0.7, so both are promoted with probability 0.21.
- Introduction to probability for data science, section 2.4.2: [pages 101 to 104](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=101). Independence of two events as P[A ∩ B] = P[A] P[B] (Definition 2.23) and as P[A | B] = P[A] (Definition 2.24), and why independent and disjoint are different ideas.
- Introduction to probability for data science, section 5.1.6: [pages 267 to 269](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=267). Independent random variables, whose joint PDF is the product of the marginals, checked on two joint PDFs (Examples 5.8 and 5.9), then independent and identically distributed sequences.
- Mathematics for machine learning, section 6.4.5: [pages 200 to 201](../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=200). Statistical independence of two random variables (Definition 6.10), why zero covariance does not imply it, and i.i.d. data.
- Deep learning textbook, section 3.7: [page 76](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=76). Independence as p(x, y) = p(x) p(y) for every pair of values, with the notation x ⊥ y.

**Videos**

- Professor Leonard, Statistics lecture 4.4, The Multiplication Rule for "And" Probabilities, 24:07 to 29:53: [watch](https://www.youtube.com/watch?v=05JCQswK3hE&t=1447s). Independent against dependent events. Chapter-timed.
- Professor Leonard, Statistics lecture 4.4, The Multiplication Rule for "And" Probabilities, 29:53 to 35:18: [watch](https://www.youtube.com/watch?v=05JCQswK3hE&t=1793s). The formulas for independent events. Chapter-timed.
- 3Blue1Brown, Why π is in the normal distribution, 13:15 to 15:18: [watch](https://www.youtube.com/watch?v=cy8r7WSuT1I&t=795s). Two demands on a density in the plane, that it depend only on distance from the centre and that x and y be independent, which make it the product g(x)·g(y). Caption-read, from the video lessons index.

**Our plans and chapters**

- [Check independence on a table](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/03-plain-independence.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 03. Independence checked on the fuel gauge's table.
- [Chapter 1: Compute conditionals and independence from a joint table](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/01-joint-tables-and-independence.md), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 01. Section 1.3, independence checked cell by cell.
- [Chance agreement under independence: Cohen's p_e](/home/molef/goal-setting/learning/ai-engineering/agent-evaluation/validating-an-llm-judge/plans/06-chance-agreement-p-e.md), ai-engineering/agent-evaluation/validating-an-llm-judge, plan 06. The agreement two independent raters reach by luck, from each one's pass rate.
- [Where independence fails, and r_t defined](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/15-where-independence-fails.md), deep-learning/diffusion-models/01-poe-derivation-foundations, plan 15. Where the independence behind the product-of-experts rule fails, and the residual r_t defined.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext; the probability for data science pages were first found through its back-of-book index. The two Professor Leonard chapter lists were read with `cache-video-chapters.py`, so those lines describe only the video's title and chapter titles. The 3Blue1Brown row is copied from the section "The Gaussian density and its formula" in `Mathematics/references/videos/Video Lessons.md`. Each plan and chapter was read at its title and opening lines. The bare word "independence" is an alias because nearly every sampled use in the learning tree is statistical; lines naming the paper "Parametrization Independence" keep it plain.
