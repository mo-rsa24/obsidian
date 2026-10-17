---
aliases: [MCMC, Markov chain Monte Carlo]
---

# Markov Chain Monte Carlo

Up: [[Statistics]]

Mathematics, Statistics. Needs: [[Distributions]].

**Markov chain Monte Carlo draws samples from a density by running [a chain](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/l3-stochastic-processes.pdf#page=4) whose moves [leave that density unchanged](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/l3-stochastic-processes.pdf#page=12), so after enough steps the chain's position is a sample.** These notes were met while composing diffusion models, in [[Composition]], and hold for any density.

## Notes in this folder

Read them in this order.

- [[Annealed MCMC]]: a few MCMC steps at every noise level, noisiest first, each aimed at that level's composed curve.
- [[Step Size And The Accept Step]]: why an unadjusted Langevin chain widens and then runs away past a step of 2 / P, and how an accept step holds the width.
