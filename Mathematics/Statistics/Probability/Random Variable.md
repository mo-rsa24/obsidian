---
aliases: [random variable, discrete random variable, continuous random variable]
standard: vault-note v2
---

# Random Variable

Up: [[Probability]]

Mathematics, Statistics, Probability. [[Distributions]] says how likely each of its values is, [[Expected Value]] and [[Variance]] summarise it, and [[Scaling And Shifting A Random Variable]] moves it.

**A random variable is a function that gives each outcome of a random experiment a number, so that questions about outcomes become questions about numbers, such as the chance that X is at most 2.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches random variables writes the rest around it.

## Where to learn this

**Random variable**, a number attached to each outcome. Also: discrete random variable, continuous random variable.

**Textbooks**

- Introduction to probability for data science, section 3.1: [pages 121 to 125](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=121). Works it on four outcomes ♣, ♢, ♡, ♠ mapped to the numbers 1 to 4, explains why a function is called a variable, then a die thrown twice (Example 3.4, page 125).
- Introduction to statistics (Wits lecture notes), section 4.2: [pages 80 to 81](../../references/textbooks/statistics/introduction-to-statistics.pdf#page=80). A discrete random variable and its probability distribution, with a worked example (Example 4.1) and its cumulative distribution.
- Mathematics for machine learning, section 6.1.2: [pages 180 to 181](../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=180). A random variable as a function from outcomes to a target space of states, discrete or continuous.
- Deep learning textbook, section 3.2: [page 72](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=72). A random variable as a description of possible states that needs a probability distribution beside it, and the discrete and continuous kinds.
- Understanding deep learning, appendix C.1: [page 462](../../references/textbooks/machine-learning/understanding-deep-learning.pdf#page=462). A random variable as an uncertain quantity, discrete or continuous, with its probability distribution.

**Videos**

- StatQuest, Expected Values for Continuous Variables, 1:30 to 3:42: [watch](https://www.youtube.com/watch?v=OSPr6G6Ka-U&t=90s). Discrete and continuous variables defined, before the exponential distribution. Chapter-timed.
- Professor Leonard, Statistics lecture 6.2, Introduction to the Normal Distribution and Continuous Random Variables, 0:00 to 41:13: [watch](https://www.youtube.com/watch?v=shrTfDUB9Hk&t=0s). Continuous distributions, the lecture's opening chapter on continuous random variables. Chapter-timed.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext. The two video chapter lists were read with `cache-video-chapters.py`, so each line describes only the video's title and chapter titles. No plan or compiled chapter in the learning tree is about random variables themselves, so the card has no plans group; the rest of Understanding deep learning's appendix C.1 (pages 462 to 465) covers joint, marginal and conditional probability rather than random variables.
