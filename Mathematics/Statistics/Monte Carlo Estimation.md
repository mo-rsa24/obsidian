---
aliases: [Monte Carlo, Monte Carlo estimate, Monte Carlo estimation, Monte Carlo estimator, Monte Carlo integration, Monte Carlo approximation, Monte Carlo simulation, Monte Carlo method]
link-skip: [Monte Carlo tree search, Monte Carlo dropout, Sequential Monte Carlo, Monte Carlo casino]
standard: vault-note v2
---

# Monte Carlo Estimation

Up: [[Statistics]]

Mathematics, Statistics. [[Sampling From A Distribution]] holds the card for drawing the samples, and [[Markov Chain Monte Carlo]] draws them with a chain when direct sampling is out of reach.

**Monte Carlo estimation replaces an expectation or an integral by the average of a function over random samples, so the answer is approximate and its error shrinks like one over the square root of the number of samples.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches Monte Carlo estimation writes the rest around it.

## Where to learn this

**Monte Carlo estimation**, averaging over random samples to approximate an expectation or an integral. Also: Monte Carlo, Monte Carlo estimate, Monte Carlo integration, Monte Carlo approximation.

**Textbooks**

- Probabilistic machine learning: advanced topics, section 11.2: [pages 510 to 513](../references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=510). Works π from 5,000 points in a square (3.10 with standard error 0.09), then the accuracy of the estimate, its standard error and the 95 percent interval (equation 11.10).
- Pattern recognition and machine learning, chapter 11 introduction: [pages 539 to 540](../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=539). An expectation approximated by a finite sum over independent samples (equation 11.2), with the estimator's variance (equation 11.3) and why its accuracy does not depend on the dimension.
- Deep learning textbook, section 17.1: [pages 606 to 608](../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=606). Why machine learning needs Monte Carlo estimates of sums and integrals, then the basics of Monte Carlo sampling and the variance of the estimate.
- Probabilistic machine learning: an introduction, section 2.8.7: [page 96](../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=96). Approximates the distribution of y = x² for a uniform x by squaring many samples.

**Videos**

- ritvikmath, Monte Carlo Simulations, 0:23 to 4:50: [watch](https://www.youtube.com/watch?v=EaR3C4e600k&t=23s). Darts in a square: the fraction landing in the circle estimates π/4, with the loop written as pseudocode. Caption-read, from the video lessons index.
- ritvikmath, Monte Carlo Simulations, 9:28 to 13:32: [watch](https://www.youtube.com/watch?v=EaR3C4e600k&t=568s). Estimates the expected number of rounds until two losses in a row by simulating a million games, against the exact 6 at p = 1/2. Caption-read, from the video lessons index.
- ritvikmath, Monte Carlo Simulations, 13:32 to 16:22: [watch](https://www.youtube.com/watch?v=EaR3C4e600k&t=812s). When to reach for simulation, and why it slows down as p nears 1. Caption-read, from the video lessons index.
- TileStats, Monte Carlo simulations in R, Dice roll simulations, 4:40 to 9:20: [watch](https://www.youtube.com/watch?v=tFsaxvQrfvo&t=280s). Simulates dice rolls in R to estimate probabilities. Chapter-timed.

**Our plans and chapters**

- [13. Drawing samples by hand: Monte Carlo, inverse transform and accept-reject](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/13-drawing-samples-by-hand.md#worked-examples), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L3, section 13. Example 1 estimates a tail probability and a mean from ten fixed normal draws by hand, with the standard error of the estimate.
- [Conditioning with densities](/home/molef/goal-setting/learning/mathematics/statistics/conditional-expectation/plans/06-conditioning-with-densities.md#3--write-the-monte-carlo-slice-check), mathematics/statistics/conditional-expectation, plan 06, task 3. Checks a conditional mean by Monte Carlo, averaging two million draws inside narrow windows.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook range was read with pdftotext, after finding it through the books' back-of-book indexes. The three ritvikmath rows are copied from the video lessons index, section "Estimating a number by simulation (Monte Carlo)". The TileStats chapter list was read with cache-video-chapters.py and the line is described from its chapter title only. Each plan and chapter was read at its title and the cited section. Understanding deep learning's Monte Carlo pages (PDF pages 395 to 397) are Monte Carlo value estimation in reinforcement learning and were left out. The longer names Markov chain Monte Carlo, Hamiltonian Monte Carlo and Langevin Monte Carlo belong to their own cards.
