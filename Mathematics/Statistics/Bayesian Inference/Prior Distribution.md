---
aliases: [prior distribution, prior, prior probability, prior density, prior belief, conjugate prior]
link-skip-in: [finance/]
link-skip: [prior to, prior work, prior art, prior empirical, prior resolution]
standard: vault-note v2
---

# Prior Distribution

Up: [[Bayesian Inference]]

Mathematics, Statistics, Bayesian Inference. [[Likelihood]] and [[Posterior Distribution]] sit beside this note, and [[Bayes Theorem]] combines the three.

**A prior distribution is the probability distribution placed on an unknown parameter before the data are seen, saying which values are believed likely and how strongly.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the prior writes the rest around it.

## Where to learn this

**Prior distribution**, the belief about a parameter before the data. Also: prior, prior probability, conjugate prior.

**Textbooks**

- Probabilistic machine learning: an introduction, sections 4.6.1 and 4.6.2: [pages 150 to 151](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=150). Works with numbers: a conjugate prior keeps the posterior in the prior's own family, shown on a coin with prior Be(2, 2) against the flat prior Be(1, 1) under the same likelihood Be(5, 2).
- Introduction to probability for data science, sections 8.3.1 and 8.3.2: [pages 519 to 521](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=519). The trio of likelihood, prior and posterior, the prior that ML lacks and MAP adds (page 520), and what a prior's shape says, from a delta prior that ignores the data to a uniform one (Figure 8.15, page 521).
- Mathematics for machine learning, section 6.3: [page 191](../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=191). The prior p(x) as what is known about an unobserved variable before observing y, inside Bayes' theorem.
- Deep learning textbook, section 5.6: [pages 151 to 152](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=151). The prior probability distribution p(θ) as knowledge of θ before observing data, usually chosen broad, then combined with the likelihood by Bayes' rule.

**Videos**

- TileStats, Bayesian statistics, the basics, 9:20 to 12:47: [watch](https://www.youtube.com/watch?v=5Vawq2b5F7c&t=560s). The prior distribution, in the chapter of that name, between Bayes' theorem and computing the posterior. Chapter-timed.
- ritvikmath, What the Heck is Bayesian Stats ??, 13:06 to 16:07: [watch](https://www.youtube.com/watch?v=-1dYY43DRMA&t=786s). Updating prior beliefs with the data. Chapter-timed.
- ritvikmath, Conjugate Priors, 9:48 to 17:33: [watch](https://www.youtube.com/watch?v=mvGj4OKbDcY&t=588s). The big idea behind a conjugate prior, after the chapter that works its mathematics. Chapter-timed.

**Our plans and chapters**

- [Derive MAP, and draw the prior as a parent of θ](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/25-map-derived.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 25. A Beta(2, 2) prior on a coin's θ, drawn as θ's parent in the graph and updated by HHH.
- [Write the Beta density and find its mode](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/24-beta-density.md), the same journey, plan 24. The Beta density and its mode, worked on Beta(2, 2) and Beta(5, 2), which plan 25 then uses as the coin's prior.
- [See MAP fix the overfit, and a wrong prior pull the fit away](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/26-map-fixes-and-pulls.md), the same journey, plan 26. Beta(2, 2) against a wrong Beta(1, 20) prior on the same flips.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext; the Murphy, probability for data science and Deep learning textbook pages were first found through their back-of-book indexes. The three video chapter lists were read with `cache-video-chapters.py`, so each line describes only the video's title and chapter titles. Each plan was read at its title and description. The bare word "prior" is an alias because about 20 of 25 sampled lines in the learning tree use it for a prior distribution; the lines that say "prior art", "prior work", "prior to" or "prior empirical" keep it plain.
