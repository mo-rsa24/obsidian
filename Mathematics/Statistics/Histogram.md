---
aliases: [histogram, frequency histogram, density histogram, histogram density estimate]
link-skip: [histogram of oriented gradients, histograms of oriented gradients, histogram equalization, color histogram, colour histogram]
standard: vault-note v2
---

# Histogram

Up: [[Statistics]]

Mathematics, Statistics. [[Probability Density Function]] is the curve a density histogram approaches as the data grow and the bins narrow, and [[Sampling From A Distribution]] checks its draws with one.

**A histogram splits the range of a variable into bins and draws one bar per bin, its height the count of data points that land there, or that count divided by the total and the bin width so the bars have area 1.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches histograms writes the rest around it.

## Where to learn this

**Histogram**, counts of data per bin drawn as bars. Also: frequency histogram, density histogram, histogram density estimate.

**Textbooks**

- Introduction to probability for data science, sections 3.2.4 to 3.2.5: [pages 129 to 136](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=129). Works a histogram of English letter frequencies and of N die throws approaching the PMF, then shows bins too wide and too narrow on 1,000 exponential draws, four bin-width rules (square root, Sturges, Rice, Scott) and a cross-validation score, with MATLAB and Python code.
- Pattern recognition and machine learning, section 2.5: [pages 139 to 141](../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=139). The histogram as a density estimate, p_i = n_i / (N Δ_i), drawn for three bin widths on 50 points from a two-Gaussian mixture, and why it scales badly as the dimension grows.

**Videos**

- StatQuest, Histograms, Clearly Explained, 0:34 to 3:42: [watch](https://www.youtube.com/watch?v=qBigTkBLU6g&t=34s). Builds a histogram by stacking measurements into bins. Chapter-timed.
- Professor Leonard, Statistics Lecture 2.2, Data visualization, 52:50 to 1:02:41: [watch](https://www.youtube.com/watch?v=AbHn39y8eUo&t=3170s). Draws the frequency distribution built earlier in the lecture as graphs. Chapter-timed.
- Professor Leonard, Statistics Lecture 2.2, Building the classes, 12:55 to 17:37: [watch](https://www.youtube.com/watch?v=AbHn39y8eUo&t=775s). Choosing the classes, the bins a frequency distribution and its histogram count into. Chapter-timed.
- TileStats, Monte Carlo simulations in R, Generate a histogram of the random numbers, 2:00 to 4:40: [watch](https://www.youtube.com/watch?v=tFsaxvQrfvo&t=120s). Draws a histogram of simulated random numbers in R. Chapter-timed.

**Our plans and chapters**

- [Write the inverse-CDF draw as a function and check its histogram](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/06-inverse-cdf-in-code.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 06. Checks draws from the exponential with rate 2 and from N(3, 4) by laying their histogram over the density.
- [Densities, and the Gaussian](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/03-densities-and-the-gaussian.md#2--histogram-a-real-latent-tensor-from-your-own-runs), deep-learning/diffusion-models/01-poe-derivation-foundations, plan 03, task 2. A density histogram of a real latent tensor from your own runs, counting the bars taller than 1.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook range was read with pdftotext, after finding it through the books' back-of-book indexes. The StatQuest, Professor Leonard and TileStats chapter lists were read with cache-video-chapters.py, and each line is described from its chapter title and the video title only. Each plan was read at its title, description and the cited task. Mathematics for machine learning names histograms only in its further-reading notes (PDF page 375) and was left out; the computer vision textbook's histograms are image descriptors (histograms of oriented gradients, colour histograms), a different use, and are kept out by the link-skip phrases.
