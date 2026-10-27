---
aliases: [binomial distribution, binomial, binomial count, binomial random variable, binomial probability, binomial tail, Bin(n, p), Bernoulli trials]
link-skip: [binomial algebra, Binomial algebra, binomial coefficient, binomial coefficients, binomial theorem, binomial expansion, binomial series, binomial formula, binomials, negative binomial, beta-binomial, log-binomial, multiplying binomials]
standard: vault-note v2
---

# Binomial Distribution

Up: [[Distributions]]

Mathematics, Statistics, Distributions. Its counting factor C(n, k) is taught in [[The Binomial Theorem]], and the exact bound in [[Selective Evaluation]] and the [[Rule Of Three]] are sums of its tail.

**The binomial distribution gives the chance of exactly k events in n independent trials that each succeed with the same chance p: C(n, k) pᵏ (1 − p)ⁿ⁻ᵏ, the number of orders the k events can sit in times the chance of any one order; its mean is np and its variance np(1 − p).**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the binomial distribution writes the rest around it.

## Where to learn this

**Binomial distribution**, P(X = k) = C(n, k) pᵏ (1 − p)ⁿ⁻ᵏ for k events in n independent trials. Also: binomial count, binomial random variable, Bin(n, p), Bernoulli trials.

**Textbooks**

- Introduction to statistics, Example 4.7: [page 88](../../references/textbooks/statistics/introduction-to-statistics.pdf#page=88). Works the probability of 4 heads in 6 fair tosses, C(6, 4)(1/2)⁴(1/2)² = 15/64, then states E[X] = np and Var[X] = np(1 − p).
- Introduction to probability for data science, section 3.5.2: [pages 159 to 162](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=159). Builds the PMF from three flips of a biased coin (3p²(1 − p) for two heads, from the three orders), then draws 5,000 Bin(10, 0.5) samples in Python and shows how p skews the shape and a large n makes it bell-shaped.
- Probabilistic machine learning: an introduction, section 2.4: [pages 73 to 74](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=73). The Bernoulli as one trial, the binomial as the count over N trials, with the PMF plotted for N = 10 at θ = 0.25 and 0.9 (figure 2.6).
- Mathematics for machine learning, Example 6.9: [page 212](../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=212). The binomial as m occurrences of X = 1 in N Bernoulli samples, with mean Nμ and variance Nμ(1 − μ), plotted for N = 15 and μ = 0.1, 0.4 and 0.75.
- Computer networking: a top-down approach, section 1.3.2: [pages 60 to 61](../../references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=60). Same calculation in networking: 35 users each active 10% of the time share a link, and the binomial tail gives a 0.0004 chance that 11 or more are active at once, so packet switching serves 35 users where circuit switching serves 10.
- Probabilistic machine learning: an introduction, section 18.2: [page 660](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=660). Same calculation in machine learning: a majority vote of M independent classifiers each right with θ = 0.51 is right with probability 1 − B(M/2, M, θ), 0.73 for M = 1,000 and 0.97 for M = 10,000.

**Videos**

- StatQuest, The Binomial Distribution and Test, Clearly Explained!!!, 0:00 to 15:46: [watch](https://www.youtube.com/watch?v=J8jNoF-K8E8&t=0s). Builds the formula from 2 of 3 people preferring orange (one order 0.125, three orders 0.375), then adds four bars, 0.273, 0.164, 0.055 and 0.008, into a one-tailed binomial test of 0.500 on 4 of 7. Whole video; the sampling and hypothesis-testing plans cite the two passages inside it.

**Our plans and chapters**

- [The binomial count](/home/molef/goal-setting/learning/mathematics/statistics/sampling/textbook/01-the-binomial-count.md), mathematics/statistics/sampling, chapter 1. A judge wrongly fails each of 8 good pages with chance 0.25: counting one order gives 0.033, and multiplying by the 8 orders gives the right 0.267, then the same count in plain Python and on 97 defects.
- [Count the chance of k events in n checks](/home/molef/goal-setting/learning/mathematics/statistics/sampling/plans/01-the-binomial-count.md), mathematics/statistics/sampling, plan 1. The plan for that chapter, opening on the StatQuest orange example.
- [The binomial distribution from counting](/home/molef/goal-setting/learning/ai-engineering/agent-evaluation/validating-an-llm-judge/plans/14-the-binomial-from-counting.md), ai-engineering/agent-evaluation/validating-an-llm-judge, plan 14. Derives the chance of k errors in n independent items from counting arrangements and computes no error in 8 items at a 25% error rate.
- [2.6 The build: exact_p on the binomial tail](/home/molef/goal-setting/learning/mathematics/statistics/hypothesis-testing/textbook/02-the-exact-test.md#26-the-build-exact_p-on-the-binomial-tail), mathematics/statistics/hypothesis-testing, chapter 2. Codes the binomial CDF and McNemar's exact test on it, where `exact_p(3, 0)` must print 0.2500.
- [Derive McNemar's exact test from a fair coin on the disagreements](/home/molef/goal-setting/learning/mathematics/statistics/hypothesis-testing/plans/05-the-exact-test-derived.md), mathematics/statistics/hypothesis-testing, plan 5. Treats the 8 disagreements between two prompts as fair coin tosses, so the p-value is a tail of Bin(8, ½).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27. Each textbook page was read in the PDF with pdftotext, first found through the books' back-of-book indexes and `find-examples.py --concept` and `--like "binomial distribution"`; the networking and ensemble pages share its binomial-tail shape. Pattern recognition and machine learning, section 2.1 (pages 87 to 90), teaches the same and has no line, to keep six. No lecture map holds a binomial segment. The StatQuest video has no chapter list (`cache-video-chapters.py` reads it as one chapter), so it is cited whole; the two passages it describes were caption-read by the sampling and hypothesis-testing passes. `find-figures.py` found no saved figure. Each plan and chapter was read at its heading and opening. The phrases in `link-skip` belong to [[The Binomial Theorem]] or to other distributions. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a cached chapter.
