---
aliases: [covariance, covariance matrix]
standard: vault-note v2
---

# Covariance

Up: [[Statistics]]

Mathematics, Statistics. [[Correlation Coefficient]] divides covariance by the two standard deviations, [[Variance]] is the covariance of a variable with itself, and [[Diagonal Covariance]] is the covariance matrix with zeros off its diagonal.

**Covariance measures how two random variables move together: the average product of their distances from their own means, positive when they rise together and negative when one rises as the other falls.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches covariance writes the rest around it.

## Where to learn this

**Covariance**, how two variables vary together, and the covariance matrix that holds it for every pair of coordinates. Also: covariance matrix.

**Textbooks**

- Introduction to probability for data science, section 5.2.2: [pages 277 to 279](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=277). Defines Cov(X, Y) = E[(X − µ_X)(Y − µ_Y)] (Definition 5.12), proves Cov(X, Y) = E[XY] − E[X]E[Y] and the rules for sums (Theorems 5.3 and 5.4), then divides by the standard deviations to get the correlation coefficient.
- Introduction to probability for data science, section 5.6.3: [pages 305 to 306](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=305). The covariance matrix of a random vector (Definition 5.20) and its properties (Theorem 5.13), leading into the multidimensional Gaussian.
- Mathematics for machine learning, sections 6.4.1 to 6.4.2: [pages 196 to 198](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=196). Univariate and multivariate covariance (Definitions 6.5 and 6.6), the covariance matrix with the variances on its diagonal, then the empirical covariance of a data set (Definition 6.9).
- Deep learning textbook, section 3.8: [pages 77 to 78](../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=77). Covariance as a measure of linear relation, why zero covariance is weaker than independence, and the covariance matrix (equation 3.14).
- Pattern recognition and machine learning, section 1.2.2: [page 39](../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=39). The covariance of two variables and of two vectors (equations 1.41 and 1.42).

**Videos**

- StatQuest, Covariance, Clearly Explained, How to calculate covariance, 7:32 to 17:00: [watch](https://www.youtube.com/watch?v=qtaqvPAeEJY&t=452s). Works the covariance of two measured variables step by step. Chapter-timed.
- StatQuest, Covariance, Clearly Explained, Why covariance is hard to interpret, 17:00 to 20:31: [watch](https://www.youtube.com/watch?v=qtaqvPAeEJY&t=1020s). Why the size of a covariance depends on the units, which motivates correlation. Chapter-timed.
- ritvikmath, The Covariance Matrix, 5:23 to 10:59: [watch](https://www.youtube.com/watch?v=152tSYtiQbw&t=323s). Computes a covariance matrix from data. Chapter-timed, from the video lessons index.
- ritvikmath, The Covariance Matrix, 2:40 to 5:23: [watch](https://www.youtube.com/watch?v=152tSYtiQbw&t=160s). What a covariance matrix holds: each coordinate's variance on the diagonal, each pair's covariance off it. Chapter-timed, from the video lessons index.
- CS229 lecture 5, 16:18 to 21:20: [watch](https://www.youtube.com/watch?v=zRdE8A4UZes&t=978s). Draws 2D Gaussians with identity, diagonal and full covariances, showing how the off-diagonal entry rotates the ellipse. Caption-read.

**Our plans and chapters**

- [Read a covariance as an ellipse](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/27-two-d-gaussian.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 27. Reads a covariance matrix as the ellipse of a 2D Gaussian, worked on two-pixel images.
- [Chapter 2: Read a density as area and draw a Gaussian from its covariance](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/02-densities-and-the-gaussian.md#24-from-covariance-to-contours), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 02, section 2.4. Every contour of a Gaussian is an ellipse whose axes follow the covariance's eigenvectors.
- [Many inputs: two spreads through one curve](/home/molef/goal-setting/learning/mathematics/statistics/sampling/textbook/11-many-inputs.md#why-the-cells-move-together-the-covariance), mathematics/statistics/sampling, chapter 11. Why errors in several inputs move together, through Σ_Y = AΣ_XAᵀ, and what breaks when the covariances are dropped.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook range was read with pdftotext, after finding it through the books' back-of-book indexes. The StatQuest chapter list was read with cache-video-chapters.py and the two lines are described from their chapter titles only. The two ritvikmath rows are copied from the video lessons index, section "The multivariate normal and its covariance matrix". The CS229 row was read in its caption-read lecture map. Each plan and chapter was read at its title and the opening lines of the cited section. TileStats' "Covariance and the correlation matrix" (chapter "Covariance matrix", 15:01) was cached and left out to keep the video list to the routed creators; Understanding deep learning's appendix (PDF page 468) and Probabilistic machine learning: an introduction (PDF page 101) also define covariance and were left out to keep the list short.
