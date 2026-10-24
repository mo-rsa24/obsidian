---
aliases: [Bayes' theorem, Bayes theorem, Bayes' rule, Bayes rule, Bayes's rule, Bayes's theorem, Bayes' formula, Bayes formula]
standard: vault-note v2
---

# Bayes Theorem

Up: [[Probability]]

Mathematics, Statistics, Probability. It rests on [[Conditional Probability]], and [[Bayesian Inference]] applies it to parameters, turning a [[Prior Distribution]] and a [[Likelihood]] into a [[Posterior Distribution]].

**Bayes' theorem turns a conditional probability around: the probability of A given B equals the probability of B given A, times the probability of A, divided by the probability of B.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches Bayes' theorem writes the rest around it.
> - The placement is unsure. The two best places are `Mathematics/Statistics/Probability/` and `Mathematics/Statistics/Bayesian Inference/`.

## Where to learn this

**Bayes' theorem**, P(A | B) = P(B | A) P(A) / P(B). Also: Bayes' rule, Bayes rule, Bayes' formula.

**Textbooks**

- Introduction to probability for data science, section 2.4.3: [pages 105 to 108](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=105). Works with numbers: the theorem with its proof and the law of total probability, then the chance of winning a match against three kinds of player you beat with probability 0.3, 0.4 and 0.5 (page 107), and which bit a noisy channel sent (page 108).
- Pattern recognition and machine learning, section 1.2: [pages 31 to 36](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=31). Works with numbers: a red box of 2 apples and 6 oranges and a blue box of 3 apples and 1 orange, the sum and product rules, Bayes' theorem (page 34), and the chance 2/3 that an orange came from the red box (page 36), with prior and posterior named there.
- Introduction to statistics (Wits lecture notes), sections 3.7.7 and 3.7.8: [pages 74 to 76](../../references/textbooks/statistics/introduction-to-statistics.pdf#page=74). Probability tree diagrams, the law of total probability, then Bayes' theorem for a posterior over several exhaustive events, with a worked example (Example 3.26).
- Mathematics for machine learning, section 6.3: [pages 189 to 192](../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=189). The sum rule and product rule, Bayes' theorem as their consequence, and the names prior, likelihood, posterior and evidence.
- Probabilistic machine learning: an introduction, section 2.3: [pages 69 to 72](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=69). Bayes' rule as the formula for a distribution over an unknown given data, summarised in words, and simple examples of Bayesian inference.

**Videos**

- 3Blue1Brown, Bayes theorem, the geometry of changing beliefs, 0:00 to 4:09: [watch](https://www.youtube.com/watch?v=HZGCoVF3YvM&t=0s). The video's opening example, which the next chapter turns into the formula. Chapter-timed.
- 3Blue1Brown, Bayes theorem, the geometry of changing beliefs, 4:09 to 10:13: [watch](https://www.youtube.com/watch?v=HZGCoVF3YvM&t=249s). From a worked example to the general formula. Chapter-timed, from the video lessons index.
- StatQuest, Bayes' Theorem, Clearly Explained, 5:21 to 9:12: [watch](https://www.youtube.com/watch?v=9wCnvr7Xw4E&t=321s). Bayes' theorem derived step by step. Chapter-timed, from the video lessons index.
- 3Blue1Brown, The quick proof of Bayes' theorem, 0:00 to 3:47: [watch](https://www.youtube.com/watch?v=U_85TaXbeIo&t=0s). A short proof of the theorem. Whole video.

**Our plans and chapters**

- [Turn a conditional around with Bayes' rule](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/02-bayes-rule.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 02. Bayes' rule worked on the fuel gauge's table.
- [Chapter 1: Compute conditionals and independence from a joint table](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/01-joint-tables-and-independence.md), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 01. Section 1.5 derives Bayes in two lines from the definition of a conditional.
- [Conditional expectation textbook, section 6.2, page 44](/home/molef/goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/conditional-expectation.pdf#page=44), mathematics/statistics/conditional-expectation, compiled textbook. Bayes' rule on densities, p(x | y) = p(x, y) / ∫ p(x′, y) dx′, read term by term as a slice divided by its area.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext; the probability for data science pages were first found through its back-of-book index. The two rows marked "from the video lessons index" are copied from the section "Bayes' theorem" in `Mathematics/references/videos/Video Lessons.md`; the other two 3Blue1Brown lines come from chapter lists read with `cache-video-chapters.py`, so they describe only each video's title and chapter titles. Each plan and chapter was read at its title and opening lines. Deep learning textbook section 3.11 (PDF page 86) also states Bayes' rule and has no line only to keep the list short.
