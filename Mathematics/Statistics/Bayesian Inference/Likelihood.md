---
aliases: [likelihood, likelihood function, maximum likelihood, maximum likelihood estimation, maximum-likelihood estimation, maximum likelihood estimate, MLE, log-likelihood, log likelihood, negative log-likelihood]
standard: vault-note v2
---

# Likelihood

Up: [[Bayesian Inference]]

Mathematics, Statistics, Bayesian Inference. [[Cross-Entropy]] is the negative log-likelihood under another name, and the [[Prior Distribution]] and [[Posterior Distribution]] sit beside this note.

**The likelihood is the probability of the observed data read as a function of the model's parameters, with the data held fixed, and maximum likelihood picks the parameters that make the data most probable.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the likelihood writes the rest around it.
> - The placement is unsure. The two best places are `Mathematics/Statistics/Bayesian Inference/` and `Mathematics/Statistics/`, since maximum likelihood is used without any prior.

## Where to learn this

**Likelihood**, the data's probability as a function of the parameters. Also: likelihood function, maximum likelihood, MLE, log-likelihood.

**Textbooks**

- Introduction to probability for data science, section 8.1: [pages 484 to 490](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=484). Works with numbers: the likelihood function built from the joint density, the i.i.d. likelihood and log-likelihood (page 486), and the ML estimate for Bernoulli data, drawn for N = 50 flips with 25 heads (θ = 0.5) and 12 heads (θ = 0.24) on page 490.
- Understanding deep learning, section 5.1: [pages 70 to 74](../../references/textbooks/machine-learning/understanding-deep-learning.pdf#page=70). Maximum likelihood as the recipe behind a network's loss: the product over training pairs, the log transform that keeps the maximum in place (page 73), and the negative log-likelihood to minimise (page 74).
- Probabilistic machine learning: an introduction, section 4.2: [pages 127 to 134](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=127). The definition, the iid likelihood and log likelihood (page 128), why MLE is justified, then the MLE worked for the Bernoulli, categorical, univariate and multivariate Gaussian, and linear regression.
- Deep learning textbook, section 5.5: [pages 147 to 151](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=147). Maximum likelihood as maximising the expected log probability under the empirical distribution, then the conditional log-likelihood and its properties.

**Videos**

- StatQuest, Maximum Likelihood For the Normal Distribution, step-by-step, 1:41 to 5:38: [watch](https://www.youtube.com/watch?v=Dn6b9fCIUpM&t=101s). The likelihood of a normal distribution worked on one data point, in the chapter "Example with one data point", before two points and n points. Chapter-timed.
- StatQuest, In Statistics, Probability is not Likelihood, 2:45 to 4:01: [watch](https://www.youtube.com/watch?v=pYxNSUDSFH4&t=165s). The likelihood, set against the probability in the video's opening chapter. Chapter-timed.
- StatQuest, Maximum Likelihood, clearly explained, 3:25 to 4:27: [watch](https://www.youtube.com/watch?v=XepXtl9YKwc&t=205s). Using maximum likelihood to find the best location for the centre of a normal distribution. Chapter-timed.
- CS229 lecture 3, 24:10 to 27:13: [watch](https://www.youtube.com/watch?v=uJF_gL3jhxI&t=1450s). Defines the likelihood L(θ) as the product of p(yⁱ | xⁱ; θ) over the examples, which iid allows, and compares two θ by which makes the data more likely. Caption-read.

**Our plans and chapters**

- [Read the likelihood as a function of θ with the data held fixed](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/21-the-likelihood.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 21. The likelihood of θ worked on the flips HHT.
- [Derive the maximum likelihood estimates for a coin and a Gaussian](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/22-mle-derived.md), the same journey, plan 22. θ = heads / n from HHT, and the Gaussian's variance from three draws.
- [Watch MLE give a tail probability 0 and a variance of nothing](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/23-mle-breaks.md), the same journey, plan 23. Where maximum likelihood breaks on zero counts and tiny samples.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext; the probability for data science and Understanding deep learning pages were first found through their back-of-book indexes. The CS229 row was read in its caption-read lecture map under `~/.claude/cache/captions/` and paraphrases the map. The three StatQuest chapter lists were read with `cache-video-chapters.py`, so each of those lines describes only the video's title and chapter titles. Each plan was read at its title and description. The journey's chapter 7, "The likelihood and MLE", is still an author's brief and has no line.
