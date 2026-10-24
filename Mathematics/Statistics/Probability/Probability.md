---
aliases: [probability, probability theory, probability space, sample space, event space, axioms of probability, probability axioms, classical probability]
standard: vault-note v2
---

# Probability

Up: [[Statistics]]

Mathematics, Statistics. [[Conditional Probability]], [[Bayes Theorem]], [[Statistical Independence]], [[Conditional Independence]], [[Random Variable]] and [[Expected Value]] sit in this folder, and [[Distributions]] holds the named distributions.

**Probability assigns each event, a set of possible outcomes, a number from 0 to 1 that measures how likely it is, following three axioms: no negative values, 1 for the whole sample space, and addition over disjoint events.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches probability writes the rest around it.

- [[Random Variable]]: A random variable is a function that gives each outcome of a random experiment a number, so that questions about outcomes become questions about numbers, such as the chance that X is at most 2.
- [[Conditional Probability]]: A conditional probability is the probability of A once B is known to have happened: P(A | B) = P(A and B) / P(B), the share of B's probability that also lies in A.
- [[Bayes Theorem]]: Bayes' theorem turns a conditional probability around: the probability of A given B equals the probability of B given A, times the probability of A, divided by the probability of B.
- [[Statistical Independence]]: Two events or random variables are independent when knowing one tells you nothing about the other, so the probability of both is the product of their separate probabilities.
- [[Conditional Independence]]: Two variables are conditionally independent given a third when, once the third is known, learning one tells you nothing more about the other: p(x, y | z) = p(x | z) p(y | z) for every z.
- [[Expected Value]]: The expected value of a random variable is its probability-weighted average, each value times its probability summed (or integrated for a continuous variable), which is the long-run average over many draws.

## Where to learn this

**Probability**, the measure of how likely an event is. Also: probability theory, probability space, sample space, axioms of probability.

**Textbooks**

- Pattern recognition and machine learning, section 1.2: [pages 31 to 34](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=31). Works with numbers: a red box picked 40% of the time and a blue box 60%, holding apples and oranges, from which joint, marginal and conditional probabilities and the sum and product rules are read.
- Introduction to probability for data science, sections 2.2 and 2.3: [pages 74 to 95](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=74). Probability as a measure of the size of a set, built from a sample space, an event space and a probability law (page 74), then the axioms and what follows from them, with dice worked through.
- Introduction to statistics (Wits lecture notes), sections 3.5 to 3.7.2: [pages 64 to 70](../../references/textbooks/statistics/introduction-to-statistics.pdf#page=64). The axioms, the subjective, relative-frequency and classical approaches, the addition rule and mutually exclusive events.
- Mathematics for machine learning, section 6.1: [pages 178 to 183](../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=178). Probability as a fraction of times or a degree of belief, the probability space, and random variables over a target space.
- Deep learning textbook, section 3.1: [pages 70 to 72](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=70). Why machine learning needs probability to handle uncertainty, and frequentist against Bayesian probability.

**Videos**

- Professor Leonard, Statistics lecture 4.2, Introduction to Probability, 6:00 to 9:00: [watch](https://www.youtube.com/watch?v=_EpXHuPnaK0&t=360s). The sample space, in the chapter of that name, before simple events. Chapter-timed.
- Professor Leonard, Statistics lecture 4.2, Introduction to Probability, 34:45 to 37:07: [watch](https://www.youtube.com/watch?v=_EpXHuPnaK0&t=2085s). Observed against classical probability. Chapter-timed.
- Professor Leonard, Statistics lecture 4.2, Introduction to Probability, 40:45 to 45:49: [watch](https://www.youtube.com/watch?v=_EpXHuPnaK0&t=2445s). The probability of selecting a part, in the chapter of that name. Chapter-timed.
- ritvikmath, Bayesians, Frequentists, and Parallel Universes, 1:09 to 2:19: [watch](https://www.youtube.com/watch?v=XmHPcdR3bWc&t=69s). What probability means, defined before the frequentist and Bayesian readings of it. Chapter-timed.

**Our plans and chapters**

- [Probability as a thing you can compute](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/01-probability-you-can-compute.md), deep-learning/diffusion-models/01-poe-derivation-foundations, plan 01. Events and P(A), with a sample space built and counted by hand.
- [Chapter 1: Compute conditionals and independence from a joint table](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/01-joint-tables-and-independence.md), the same journey, chapter 01. Section 1.1, an event is a subset.
- [What a probability of 1 minus δ is about](/home/molef/goal-setting/learning/ai-engineering/agent-evaluation/selective-evaluation/plans/02-what-a-probability-of-1-minus-delta-is-about.md), ai-engineering/agent-evaluation/selective-evaluation, plan 02. What a guarantee "with probability 1 − δ" is a probability over, when the calibration set is itself a random draw.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext. The Professor Leonard and ritvikmath chapter lists were read with `cache-video-chapters.py`, so each line describes only the video's title and chapter titles. Each plan and chapter was read at its title and opening lines. StatQuest has no basic probability video in its cached upload list, so the videos start with Professor Leonard.
