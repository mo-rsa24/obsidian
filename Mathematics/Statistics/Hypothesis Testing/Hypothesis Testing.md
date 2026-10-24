---
aliases: [hypothesis testing, hypothesis test, statistical hypothesis test, significance test, p-value, p value, null hypothesis, alternative hypothesis, statistical significance, statistically significant, significance level, type I error, type II error]
standard: vault-note v2
---

# Hypothesis Testing

Up: [[Statistics]]

Mathematics, Statistics. [[Confidence Interval]] sits in this folder, and [[Bootstrap]] can stand in for a test's sampling distribution.

**A hypothesis test asks whether data are surprising enough under a default claim, the null hypothesis, to reject it, and the p-value is the chance under that claim of a result at least as extreme as the one seen.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches hypothesis testing writes the rest around it.

- [[Confidence Interval]]: A confidence interval is a range computed from a sample by a procedure that, over many repeated samples, contains the true parameter a stated share of the time, such as 95%.

## Where to learn this

**Hypothesis testing**, deciding whether data reject a null hypothesis. Also: hypothesis test, p-value, null hypothesis, significance level, statistical significance.

**Textbooks**

- Introduction to probability for data science, section 9.3: [pages 582 to 592](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=582). Works with numbers: null and alternative hypotheses for a coin (page 583), the critical-value test, then the p-value computed for z = −1.92 in Python (page 588), and the Z-test and T-test.
- Introduction to statistics (Wits lecture notes), section 5.5: [pages 105 to 115](../../references/textbooks/statistics/introduction-to-statistics.pdf#page=105). What a statistical hypothesis is, type I and type II errors with α as the level of significance (page 106), worked tests on a single population mean, two-sided and one-sided, and the p-value (page 113).
- Probabilistic machine learning: an introduction, section 5.7: [pages 229 to 231](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=229). The Neyman-Pearson setup of a null against an alternative, simple and compound hypotheses, and the p-value as the probability under the null of a test statistic at least as large as the one observed (page 231).

**Videos**

- TileStats, The basic steps of hypothesis testing, 5:12 to 7:14: [watch](https://www.youtube.com/watch?v=R5KxCisLQuI&t=312s). The video's example, after its chapters on stating the hypotheses, choosing a significance level, computing the p-value and making a decision. Chapter-timed.
- StatQuest, Hypothesis Testing and The Null Hypothesis, Clearly Explained, 9:51 to 13:44: [watch](https://www.youtube.com/watch?v=0oc49DyA3hU&t=591s). The null hypothesis, after the chapters on rejecting and failing to reject a hypothesis. Chapter-timed.
- StatQuest, p-values: What they are and how to interpret them, 4:32 to 7:07: [watch](https://www.youtube.com/watch?v=vemZtEM63GY&t=272s). The p-value defined, before the chapter on thresholds for a statistically significant p-value. Chapter-timed.
- Professor Leonard, Statistics lecture 8.2, An Introduction to Hypothesis Testing, 21:04 to 32:54: [watch](https://www.youtube.com/watch?v=ev8cKdrdA4s&t=1264s). Null and alternative hypotheses, in a lecture that goes on to test statistics, tail tests and the p-value method. Chapter-timed.

**Our plans and chapters**

- [Test whether two models' accuracies differ](/home/molef/goal-setting/learning/mathematics/statistics/hypothesis-testing/plans/01-two-proportion-test.md), mathematics/statistics/hypothesis-testing, plan 01. A two-proportion test on two models' accuracies.
- [What a p-value can say](/home/molef/goal-setting/learning/mathematics/statistics/hypothesis-testing/textbook/03-what-the-test-answers.md), the same journey, chapter 03. With six tasters splitting 3 to 0, p = 0.25, and a large p means too few people rather than no difference.
- [Derive McNemar's exact test from a fair coin on the disagreements](/home/molef/goal-setting/learning/mathematics/statistics/hypothesis-testing/plans/05-the-exact-test-derived.md), the same journey, plan 05. An exact test built from a fair coin on the paired disagreements.
- [Hypothesis test, type I error, and many tests at once](/home/molef/goal-setting/learning/ai-engineering/agent-evaluation/selective-evaluation/plans/03-hypothesis-test-type-i-error-and-many-tests-at-once.md), ai-engineering/agent-evaluation/selective-evaluation, plan 03. The type I error, and what happens to it when many tests run at once.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext; the probability for data science and Murphy pages were first found through their back-of-book indexes. The four video chapter lists were read with `cache-video-chapters.py`, so each line describes only the video's title and chapter titles. Each plan and chapter was read at its title and opening lines. Pattern classification appendix A.6 (PDF page 724) also covers hypothesis testing and has no line only to keep the list short.
