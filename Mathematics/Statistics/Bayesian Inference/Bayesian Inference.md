---
aliases: [Bayesian inference, Bayesian statistics, Bayesian approach, Bayesian learning, Bayesian estimation, Bayesian parameter estimation, Bayesian updating, Bayesian update, Bayesian reasoning, posterior inference]
standard: vault-note v2
---

# Bayesian Inference

Up: [[Statistics]]

Mathematics, Statistics. [[Likelihood]], [[Prior Distribution]] and [[Posterior Distribution]] sit in this folder, and [[Bayes Theorem]] is the rule that joins them.

**Bayesian inference treats an unknown parameter as a random variable, starts from a prior belief about it, and uses Bayes' theorem to turn that prior and the data's likelihood into a posterior distribution.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches Bayesian inference writes the rest around it.

- [[Prior Distribution]]: A prior distribution is the probability distribution placed on an unknown parameter before the data are seen, saying which values are believed likely and how strongly.
- [[Likelihood]]: The likelihood is the probability of the observed data read as a function of the model's parameters, with the data held fixed, and maximum likelihood picks the parameters that make the data most probable.
- [[Posterior Distribution]]: A posterior distribution is the distribution of an unknown parameter after the data are seen, proportional to the prior times the likelihood, and its peak is the maximum a posteriori (MAP) estimate.

## Where to learn this

**Bayesian inference**, updating a prior into a posterior with the data. Also: Bayesian statistics, Bayesian approach, Bayesian updating, Bayesian estimation.

**Textbooks**

- Probabilistic machine learning: an introduction, sections 4.6 to 4.6.2: [pages 149 to 151](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=149). Works with numbers: the posterior built from a prior and a likelihood, conjugate priors, then a coin's beta-binomial model plotted as prior Be(2, 2), likelihood Be(5, 2) and posterior Be(6, 3) on page 151.
- Pattern classification, sections 3.3 and 3.4: [pages 113 to 119](../../references/textbooks/machine-learning/pattern-classification.pdf#page=113). Bayesian parameter estimation, worked for the mean of a Gaussian, whose posterior p(μ | D) sharpens as samples arrive (Figure 3.2, page 117).
- Mathematics for machine learning, section 8.4.2: [pages 279 to 281](../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=279). Bayesian inference as finding the whole posterior over parameters from a parameter prior and a likelihood, and the approximations (MCMC, variational inference) used when it has no closed form.
- Deep learning textbook, section 5.6: [pages 151 to 155](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=151). The Bayesian view of θ as uncertain, updated from a prior by Bayes' rule (equation 5.67), with Bayesian linear regression as the example and the MAP point estimate in section 5.6.1.

**Videos**

- TileStats, Bayesian statistics, the basics, 12:47 to 17:33: [watch](https://www.youtube.com/watch?v=5Vawq2b5F7c&t=767s). Computing the posterior distribution by simulation, in the chapter "How to compute the Posterior distribution with simulations". Chapter-timed.
- ritvikmath, What the Heck is Bayesian Stats ??, 6:17 to 8:34: [watch](https://www.youtube.com/watch?v=-1dYY43DRMA&t=377s). The Bayesian approach to the video's problem, right after the non-Bayesian approach to the same data. Chapter-timed.
- ritvikmath, Bayesians, Frequentists, and Parallel Universes, 3:43 to 5:08: [watch](https://www.youtube.com/watch?v=XmHPcdR3bWc&t=223s). Bayesian beliefs, set against the frequentist approach in the chapter before. Chapter-timed.

**Our plans and chapters**

- [Derive MAP, and draw the prior as a parent of θ](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/25-map-derived.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 25. A Beta(2, 2) prior updated by the flips HHH, with the prior drawn as a parent node of θ.
- [See MAP fix the overfit, and a wrong prior pull the fit away](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/26-map-fixes-and-pulls.md), the same journey, plan 26. The same flips under Beta(2, 2) and Beta(1, 20), where a good prior tames the overfit and a wrong one pulls the fit away.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext; the Murphy and Deep learning textbook pages were first found through their back-of-book indexes. The three video chapter lists were read with `cache-video-chapters.py`, so each line describes only the video's title and chapter titles. Each plan was read at its title and description. The word "Bayesian" alone is not an alias, because in the learning tree it mostly names a Bayesian network.
