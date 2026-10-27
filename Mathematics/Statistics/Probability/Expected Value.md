---
aliases: [expected value, expectation, mean of a distribution, mean of a random variable, expectation of a random variable, expected value of a random variable]
link-skip: [data-quality expectation, Lakeflow expectations, Great Expectations, code expectation, expectation maximization, actual and expected, carries an expectation, outputs are expectations]
link-skip-in: [system-design/]
standard: vault-note v2
---

# Expected Value

Up: [[Probability]]

Mathematics, Statistics, Probability. Two of its rules already have notes: [[Scaling And Shifting A Random Variable]] and [[The Average Of A Product Of Independent Variables]]. [[Variance]] is the expected squared distance from it.

**The expected value of a random variable is its probability-weighted average, each value times its probability summed (or integrated for a continuous variable), which is the long-run average over many draws.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the expected value writes the rest around it.
> - The placement is unsure. The two best places are `Mathematics/Statistics/Probability/` and `Mathematics/Statistics/`, beside [[Variance]] and the two rule notes.

## Where to learn this

**Expected value**, E[X], the probability-weighted average of a random variable. Also: expectation, mean of a distribution.

**Textbooks**

- Introduction to probability for data science, section 3.4: [pages 141 to 151](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=141). Works with numbers: E[X] = Σ x p(x) and why it equals a dataset's average once repeated values are binned (pages 141 to 142), then its properties, worked on coins and dice, and the variance shortcut (page 151).
- Introduction to statistics (Wits lecture notes), section 4.2.3: [pages 81 to 82](../../references/textbooks/statistics/introduction-to-statistics.pdf#page=81). The expected value of a discrete random variable as the mean over many trials, with E[X] and Var[X] worked for the chapter's example (Example 4.2).
- Introduction to probability for data science, section 4.2: [pages 196 to 200](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=196). The integral definition for a continuous variable, with uniform and exponential worked examples (pages 196 to 197), then moments and variance.
- Mathematics for machine learning, section 6.4.1: [pages 193 to 194](../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=193). The expected value of a function of a random variable (Definition 6.3), and the mean as the expected value of the variable itself.
- Understanding deep learning, appendix C.2: [pages 466 to 469](../../references/textbooks/machine-learning/understanding-deep-learning.pdf#page=466). The expectation of a function under a distribution (equation C.8), the rules for manipulating expectations, the mean, the variance identity and standardisation.

**Videos**

- StatQuest, Expected Values, Main Ideas, 5:09 to 8:02: [watch](https://www.youtube.com/watch?v=KLs_7b7SKi4&t=309s). Calculating an expected value: each outcome times its probability, added up. Chapter-timed, from the video lessons index.
- StatQuest, Expected Values for Continuous Variables, 12:18 to 18:17: [watch](https://www.youtube.com/watch?v=OSPr6G6Ka-U&t=738s). Calculating the expected value of an exponential distribution, after deriving the formula for continuous variables. Chapter-timed.
- Stanford CS229, lecture 3, 11:33 to 21:01: [watch](https://www.youtube.com/watch?v=Mi8wnYc1m04&t=693s). Expectation of a function of a random variable. Chapter-timed, from the video lessons index.
- TileStats, Expected value vs mean, 4:36 to 6:35: [watch](https://www.youtube.com/watch?v=5Xs35Jnam5Q&t=276s). A weighted average set against the expected value. Chapter-timed.

**Our plans and chapters**

- [1. Expectation, and the best constant guess](/home/molef/goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/01-expectation-and-the-best-constant-guess.md), mathematics/statistics/conditional-expectation, section 1. A fair die's best constant guess under squared error is 3.5 pips, though the die never shows 3.5.
- [Expectation, and the best constant guess](/home/molef/goal-setting/learning/mathematics/statistics/conditional-expectation/plans/01-expectation-and-the-best-constant-guess.md), the same journey, plan 01. Probability-weighted averages for a fair die (3.5) and a loaded one (4.5), and why ignoring the weights gives the wrong answer.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext; the probability for data science pages were first found through the shelf index's most-looked-up table. The first StatQuest row and the CS229 row are copied from the sections "The expected value as a weighted sum" and "Expectation and marginals" in `Mathematics/references/videos/Video Lessons.md`; the other StatQuest and the TileStats chapter lists were read with `cache-video-chapters.py`, so those lines describe only each video's title and chapter titles. Each chapter and plan was read at its title and opening lines. Linearity of expectation and the expectation of a product already belong to [[Scaling And Shifting A Random Variable]] and [[The Average Of A Product Of Independent Variables]], so neither phrase is an alias here.
