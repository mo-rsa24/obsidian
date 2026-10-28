---
aliases: [probability density function, probability density, density function, density]
link-skip: [kernel density, mass density, population density]
standard: vault-note v2
---

# Probability Density Function

Up: [[Distributions]]

Mathematics, Statistics, Distributions. [[Inverse Transform Sampling]] turns a density's CDF into draws, and [[Multivariate Normal Distribution]] is the density met most often.

**A probability density function describes a continuous random variable: it is never negative, its total area is 1, and the probability of landing in an interval is the area under it there, so its height at a point can exceed 1.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches densities writes the rest around it.

## Where to learn this

**Probability density function**, the curve whose area over an interval is the probability of landing there. Also: density, probability density, density function.

**Textbooks**

- Introduction to probability for data science, section 4.1: [pages 188 to 195](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=188). Builds the intuition of probability per unit length, defines the PDF and its properties (Definitions 4.1 and 4.2), works several densities with numbers (Examples 4.1 to 4.3), and connects it to the PMF.
- Mathematics for machine learning, section 6.2.2: [pages 186 to 188](../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=186). The density and the CDF (Definitions 6.1 and 6.2), a uniform example (Example 6.3), and discrete against continuous distributions side by side.
- Pattern recognition and machine learning, section 1.2.1: [pages 36 to 37](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=36). The density's two conditions (equations 1.25 and 1.26), its link to the CDF, and why a density picks up a Jacobian factor under a change of variable.
- Deep learning textbook, section 3.3.2: [page 74](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=74). The properties a PDF must satisfy, and why p(x) gives the probability of a small region p(x)δx, not of a point.

**Videos**

- The Organic Chemistry Tutor, Probability Density Functions, 0:52 to 3:39: [watch](https://www.youtube.com/watch?v=QKA4HNEw3aY&t=52s). Verifies that a given function is a density by checking that its integral equals 1. Chapter-timed, from the video lessons index.
- StatQuest, The Main Ideas behind Probability Distributions, 2:15 to 5:14: [watch](https://www.youtube.com/watch?v=oI3hZJqXJuc&t=135s). A curve as a distribution, with probability read as area under it, not its height. Chapter-timed, from the video lessons index.
- Professor Leonard, Statistics Lecture 6.2, Continuous distributions, 0:00 to 41:13: [watch](https://www.youtube.com/watch?v=shrTfDUB9Hk&t=0s). Continuous random variables and their distributions, before the normal distribution. Chapter-timed.
- The Organic Chemistry Tutor, Probability Density Functions, 8:06 to 11:46: [watch](https://www.youtube.com/watch?v=QKA4HNEw3aY&t=486s). An exponential density integrated out to infinity, an improper integral. Chapter-timed, from the video lessons index.

**Our plans and chapters**

- [Chapter 2: Read a density as area and draw a Gaussian from its covariance](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/02-densities-and-the-gaussian.md#21-a-density-can-exceed-1), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 02, section 2.1. Why a density's height can pass 1 while its area stays 1, then density values worked by hand in section 2.2.
- [Densities, and the Gaussian](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/03-densities-and-the-gaussian.md), the same journey, plan 03. What p(x) means once x is continuous, read area first, then the unit, then the Gaussian.

**Scenes**

- [Kinds of composition notebook, the opening and its helpers](https://claude.ai/artifact/DBmJtn6xy75sPtQwPEvQZU#nb-sec1). The ideal expert's log-density on a grid, in four steps from the 2D Gaussian to its logsumexp form, then normalised so it integrates to 1.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook range was read with pdftotext, after finding it through the books' back-of-book indexes. The two Organic Chemistry Tutor rows and the StatQuest row are copied from the video lessons index, section "A density integrates to 1". The Professor Leonard chapter list was read with cache-video-chapters.py and the line is described from its chapter title only. Each plan and chapter was read at its title and opening lines. Probabilistic machine learning: an introduction defines the pdf in section 2.2.2.2 on PDF page 63 in a few lines and was left out. "PDF" is not an alias because the word names files throughout the learning tree. "Density" is an alias: in a sample of 25 learning-tree lines, all 25 meant a probability density.
