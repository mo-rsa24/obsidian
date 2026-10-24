---
aliases: [marginal distribution, marginal, marginal density, marginal probability, marginal PMF, marginal PDF, marginalise, marginalize, marginalising, marginalizing, marginalised, marginalized, marginalisation, marginalization, summing out, integrating out]
link-skip-in: [finance/, system-design/]
link-skip: [marginal rate, marginal tax, marginal tax rate, marginal cost, marginal revenue]
standard: vault-note v2
---

# Marginal Distribution

Up: [[Distributions]]

Mathematics, Statistics, Distributions. [[Probability Density Function]] holds the card for the densities a marginal is taken from, and [[Phi And Q]] uses the marginal pass rates of a 2 by 2 table.

**A marginal distribution is the distribution of one variable on its own, found from a joint distribution by summing (or, for densities, integrating) over every value of the other variables.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches marginals writes the rest around it.

## Where to learn this

**Marginal distribution**, one variable's distribution with the others summed or integrated out. Also: marginal, marginalise, marginal density, marginal probability, summing out, integrating out.

**Textbooks**

- Introduction to probability for data science, section 5.1.5: [page 266](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=266). Defines the marginal PMF and the marginal PDF (Definition 5.3) and works the marginals of a uniform joint density (Example 5.7).
- Pattern recognition and machine learning, section 1.2: [pages 32 to 33](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=32). The sum rule derived from counts in a grid of cells (Figure 1.10), with p(X) named the marginal probability because it is found by summing out Y (equation 1.10).
- Deep learning textbook, section 3.4: [pages 74 to 75](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=74). The marginal probability by the sum rule for discrete variables and by an integral for continuous ones, and where the name comes from.
- Mathematics for machine learning, section 6.3: [pages 189 to 190](../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=189). The sum rule, also called the marginalization property, beside the product rule and Bayes' theorem.
- Understanding deep learning, appendix C.1.2: [page 463](../../references/textbooks/machine-learning/understanding-deep-learning.pdf#page=463). Marginalization drawn on a joint distribution and its two marginals (Figure C.1).

**Videos**

- CS229 lecture 3, 23:01 to 26:37: [watch](https://www.youtube.com/watch?v=Mi8wnYc1m04&t=1381s). Joint and marginal densities, integrating one variable out. Chapter-timed, from the video lessons index.
- CME296 lecture 1, 46:33 to 56:16: [watch](https://www.youtube.com/watch?v=tr-CUpw--ck&t=2793s). Reviews marginalisation over T variables while setting up diffusion training, and shows that summing over every noise trajectory is intractable. Caption-read.
- CME296 lecture 3, 1:01:02 to 1:11:18: [watch](https://www.youtube.com/watch?v=agN3AlfGFrk&t=3662s). Builds the marginal probability path of flow matching as a mixture of conditional paths over the training points. Caption-read.

**Our plans and chapters**

- [Read a joint, a marginal and a conditional off one table](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/01-joint-marginal-conditional.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 01. Works marginals on the fuel gauge's eight-row table.
- [2. Joint and marginal: summing out and integrating out](/home/molef/goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/02-joint-and-marginal-summing-out.md), mathematics/statistics/conditional-expectation, chapter 02. Gets each variable's own distribution from a joint table, then from a joint density.
- [Sum a latent out to get a mixture](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/28-mixture-as-a-marginal.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 28. A Gaussian mixture read as the marginal of x once the cluster label z is summed out.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook range was read with pdftotext, after finding it through the books' back-of-book indexes and the shelf index's chapter tables. The CS229 row is copied from the video lessons index, section "Expectation and marginals". The two CME296 rows were read in their caption-read lecture map. Each plan and chapter was read at its title and description. [[Phi And Q]] owns "marginal normalization", which is a different phrase, so no alias clashes. The bare word "marginal" is an alias: in a sample of 25 learning-tree lines, 21 meant a probability marginal and 4 were finance (a marginal rate, a marginal tax rate), which the link-skip phrases exclude.
