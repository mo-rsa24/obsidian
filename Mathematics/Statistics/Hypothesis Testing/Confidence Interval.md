---
aliases: [confidence interval, confidence level, interval estimate, margin of error, frequentist confidence interval]
standard: vault-note v2
---

# Confidence Interval

Up: [[Hypothesis Testing]]

Mathematics, Statistics, Hypothesis Testing. [[Bootstrap]] already holds the percentile interval, and [[How Sure Kappa Is]] puts an interval on kappa.

**A confidence interval is a range computed from a sample by a procedure that, over many repeated samples, contains the true parameter a stated share of the time, such as 95%.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches confidence intervals writes the rest around it.
> - The placement is unsure. The two best places are `Mathematics/Statistics/Hypothesis Testing/` and `Mathematics/Statistics/`, beside [[Bootstrap]].

## Where to learn this

**Confidence interval**, a range for an unknown parameter at a stated confidence level. Also: confidence level, interval estimate, margin of error.

**Textbooks**

- Introduction to statistics (Wits lecture notes), section 5.3: [pages 99 to 103](../../references/textbooks/statistics/introduction-to-statistics.pdf#page=99). Works with numbers: three cases for an interval on a population mean (σ known, a large sample, a small sample with the t table), ending with a 95% interval for a container's mean from n = 7, a mean of 283.5 and s = 8.0186.
- Introduction to probability for data science, section 9.1: [pages 559 to 574](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=559). The estimator as a random variable, the definition with a confidence level of 1 − α (page 563), why the 95% belongs to the random interval and not to the parameter (page 564), then the construction from the sample average, the standard error and Student's t.
- Probabilistic machine learning: an introduction, sections 4.7.4 and 4.7.5: [pages 177 to 179](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=177). The frequentist definition over hypothetical repeated datasets, and why a 95% confidence interval is not a 95% Bayesian credible interval.

**Videos**

- Professor Leonard, Statistics lecture 7.3, Confidence Interval for the Sample Mean, Population Std Dev Known, 20:35 to 23:40: [watch](https://www.youtube.com/watch?v=kv8u7yl6VQk&t=1235s). The lecture's worked example, in the chapter "Example", after its chapters on point estimates, the margin of error and the steps. Chapter-timed.
- StatQuest, Confidence Intervals, Clearly Explained, 2:55 to 3:41: [watch](https://www.youtube.com/watch?v=TqOeMYtOc1w&t=175s). Defines a confidence interval, right after the chapter that calculates bootstrapped means. Chapter-timed.
- TileStats, Confidence intervals, simply explained, 5:19 to 8:02: [watch](https://www.youtube.com/watch?v=cTy1FmXFoA4&t=319s). The 95% confidence interval, built on the standard error of the mean from the chapters before it. Chapter-timed.

**Our plans and chapters**

- [What a 95% interval claims, on one side or two](/home/molef/goal-setting/learning/mathematics/statistics/sampling/textbook/05-what-an-interval-claims.md), mathematics/statistics/sampling, chapter 05. The 95% belongs to the procedure over repeated runs and never to the one interval in hand, on the 97-defect check run 100 times.
- [The normal interval from a standard error](/home/molef/goal-setting/learning/mathematics/statistics/sampling/textbook/06-the-normal-interval.md), the same journey, chapter 06. The interval p̂ ± z·se worked on 3 wrong passes in 97 planted defects at 95%.
- [Find both ends of the exact interval from two one-sided bounds](/home/molef/goal-setting/learning/mathematics/statistics/sampling/plans/11-the-exact-interval-derived.md), the same journey, plan 11. The exact interval for a proportion, built from two one-sided bounds.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext; the probability for data science pages were first found through its back-of-book index. The three video chapter lists were read with `cache-video-chapters.py`, so each line describes only the video's title and chapter titles. Each chapter and plan was read at its title and opening lines. The bootstrap confidence interval is left to [[Bootstrap]], which owns that name; the sampling journey's plans 08 and 10 cover the same ground as chapters 05 and 06 and have no line.
