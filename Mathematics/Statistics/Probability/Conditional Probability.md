---
aliases: [conditional probability, conditional distribution, conditional density, conditional PMF, conditional PDF, chain rule of probability, chain rule of conditional probabilities]
standard: vault-note v2
---

# Conditional Probability

Up: [[Probability]]

Mathematics, Statistics, Probability. [[Bayes Theorem]] turns it around, [[Statistical Independence]] is the case where conditioning changes nothing, and [[Marginal Distribution]] is the other half of a joint table.

**A conditional probability is the probability of A once B is known to have happened: P(A | B) = P(A and B) / P(B), the share of B's probability that also lies in A.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches conditional probability writes the rest around it.

## Where to learn this

**Conditional probability**, P(A | B) = P(A ∩ B) / P(B). Also: conditional distribution, conditional density, chain rule of probability.

**Textbooks**

- Introduction to probability for data science, section 2.4.1: [pages 97 to 100](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=97). Works with numbers: the definition as the share of B that also lies in A, then a die's chance of a 3 given an odd number and 12 equally likely points counted inside and outside two sets (pages 98 to 99), and why a conditional probability obeys the axioms.
- Introduction to statistics (Wits lecture notes), section 3.7.6: [pages 71 to 73](../../references/textbooks/statistics/introduction-to-statistics.pdf#page=71). The definition read as "the probability of A, given B has occurred", both ways round, before probability trees.
- Introduction to probability for data science, section 5.3: [pages 282 to 290](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=282). The conditional PMF p(x | y) = p(x, y) / p(y) for two random variables (page 283), then the conditional PDF.
- Deep learning textbook, sections 3.5 and 3.6: [page 75](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=75). The formula for P(y | x), defined only when P(x) > 0, and the chain rule that writes a joint as a product of conditionals.

**Videos**

- StatQuest, Conditional Probabilities, Clearly Explained, 4:45 to 8:00: [watch](https://www.youtube.com/watch?v=_IgyaD7vOOA&t=285s). Calculating conditional probabilities from the counts in a contingency table filled in the chapter before. Chapter-timed.
- StatQuest, Conditional Probabilities, Clearly Explained, 8:00 to 10:56: [watch](https://www.youtube.com/watch?v=_IgyaD7vOOA&t=480s). Calculating conditional probabilities from unconditional probabilities instead of counts. Chapter-timed.
- Professor Leonard, Statistics lecture 4.4, The Multiplication Rule for "And" Probabilities, 20:39 to 24:07: [watch](https://www.youtube.com/watch?v=05JCQswK3hE&t=1239s). Conditional probability explained, inside a lecture on the multiplication rule. Chapter-timed.

**Our plans and chapters**

- [Conditional probability from a table of counts](/home/molef/goal-setting/learning/ai-engineering/agent-evaluation/selective-evaluation/plans/01-conditional-probability-from-a-table-of-counts.md), ai-engineering/agent-evaluation/selective-evaluation, plan 01. A risk stated as a conditional probability, computed as a ratio of two counts.
- [Read a joint, a marginal and a conditional off one table](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/01-joint-marginal-conditional.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 01. The fuel gauge's eight rows, with battery and fuel each 0.9 and the gauge's chance of reading full set by both.
- [Chapter 1: Compute conditionals and independence from a joint table](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/01-joint-tables-and-independence.md), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 01. Section 1.2, conditioning as deleting what lies outside B and rescaling what is left.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext; the probability for data science and Deep learning textbook pages were first found through their back-of-book indexes. The three video chapter lists were read with `cache-video-chapters.py`, so each line describes only the video's title and chapter titles. Each plan and chapter was read at its title and opening lines.
