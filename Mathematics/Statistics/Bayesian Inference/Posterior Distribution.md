---
aliases: [posterior distribution, posterior, posterior probability, posterior density, posterior mean, maximum a posteriori, maximum a posteriori estimation, MAP, MAP estimate, MAP estimation]
standard: vault-note v2
---

# Posterior Distribution

Up: [[Bayesian Inference]]

Mathematics, Statistics, Bayesian Inference. [[Prior Distribution]] and [[Likelihood]] are its two inputs, joined by [[Bayes Theorem]].

**A posterior distribution is the distribution of an unknown parameter after the data are seen, proportional to the prior times the likelihood, and its peak is the maximum a posteriori (MAP) estimate.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the posterior writes the rest around it.

## Where to learn this

**Posterior distribution**, the belief about a parameter after the data. Also: posterior, posterior mean, maximum a posteriori, MAP.

**Textbooks**

- Introduction to probability for data science, section 8.3: [pages 527 to 529](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=527). Works the posterior of a Gaussian mean by completing the square, then draws it narrowing from prior-dominated to data-dominated as N grows from 0 to 20 (Figure 8.19, page 529).
- Introduction to probability for data science, section 8.3.1: [pages 519 to 520](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=519). The posterior f(θ | x) set beside the likelihood, which is not a PDF in θ, and a table of how ML and MAP differ.
- Mathematics for machine learning, section 6.3: [pages 190 to 192](../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=190). The sum and product rules, then Bayes' theorem giving the posterior from the prior, the likelihood and the marginal likelihood, also called the evidence.
- Probabilistic machine learning: an introduction, sections 4.6 to 4.6.2: [pages 149 to 151](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=149). The posterior as the representation of uncertainty about θ, computed in closed form for a coin as posterior Be(6, 3) from prior Be(2, 2) and likelihood Be(5, 2).

**Videos**

- TileStats, Bayesian statistics, the basics, 12:47 to 17:33: [watch](https://www.youtube.com/watch?v=5Vawq2b5F7c&t=767s). Computing the posterior distribution by simulation, in the chapter "How to compute the Posterior distribution with simulations". Chapter-timed.
- TileStats, Bayesian statistics, the basics, 19:37 to 23:00: [watch](https://www.youtube.com/watch?v=5Vawq2b5F7c&t=1177s). The posterior as prior times likelihood, in the chapter "Prior * Likelihood". Chapter-timed.
- ritvikmath, Conjugate Priors, 5:13 to 9:48: [watch](https://www.youtube.com/watch?v=mvGj4OKbDcY&t=313s). The mathematics of a conjugate prior, where the posterior comes out in the prior's own family. Chapter-timed.

**Our plans and chapters**

- [1. Tweedie's formula: denoiser output, posterior mean and score as one identity](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l4-continuous-time/01-tweedies-formula.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L4, section 1. A denoiser's output read as the posterior mean of the clean image.
- [Chapter 10: Multiply, divide and noise Gaussians by completing the square](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/10-completing-the-square.md), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 10. Section 10.4 derives the reverse posterior q(x_{t−1} | x_t, x_0) as a Gaussian.
- [Derive MAP, and draw the prior as a parent of θ](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/25-map-derived.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 25. The MAP estimate as the posterior's peak, worked on HHH with a Beta(2, 2) prior.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext; the probability for data science and Murphy pages were first found through their back-of-book indexes. The three video chapter lists were read with `cache-video-chapters.py`, so each line describes only the video's title and chapter titles. Each chapter and plan was read at its title and opening lines. The paper shelf's diffusion tutorial derives the reverse step's true posterior (Theorem 2.5, page 30), which teaches diffusion more than the posterior itself, so it has no line.
