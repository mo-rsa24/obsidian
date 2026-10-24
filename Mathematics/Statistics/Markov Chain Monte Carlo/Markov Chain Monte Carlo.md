---
aliases: [MCMC, Markov chain Monte Carlo, Metropolis-Hastings, Metropolis-Hastings algorithm, Metropolis algorithm, random walk Metropolis]
---

# Markov Chain Monte Carlo

Up: [[Statistics]]

Mathematics, Statistics. Needs: [[Distributions]].

**Markov chain Monte Carlo draws samples from a density by running [a chain](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/l3-stochastic-processes.pdf#page=4) whose moves [leave that density unchanged](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/l3-stochastic-processes.pdf#page=12), so after enough steps the chain's position is a sample.** These notes were met while composing diffusion models, in [[Composition]], and hold for any density.

## Notes in this folder

Read them in this order.

- [[Annealed MCMC]]: a few MCMC steps at every noise level, noisiest first, each aimed at that level's composed curve.
- [[Step Size And The Accept Step]]: why an unadjusted Langevin chain widens and then runs away past a step of 2 / P, and how an accept step holds the width.
- [[Markov Chain]]: A Markov chain is a sequence of random states in which the next state depends only on the current one, through fixed transition probabilities, and not on the path that led there.
- [[Stationary Distribution]]: A stationary distribution of a Markov chain is one the chain hands back unchanged after a step, so a chain started there stays there; detailed balance, equal probability flow each way between every pair of states, is the usual way to prove a chain has one.
- [[Hamiltonian Monte Carlo]]: Hamiltonian Monte Carlo gives each sample a random momentum, moves it along the Hamiltonian dynamics of the target's energy with a few leapfrog steps, and accepts or rejects the end point, so it travels far in one move while keeping the target distribution.
- [[Langevin Dynamics]]: Langevin dynamics draws samples from p by stepping along the score ∇ log p(x) and adding Gaussian noise at every step, so the walk settles into p rather than onto its peak.

## Where to learn this

**Markov chain Monte Carlo**, drawing samples from a density by running a chain whose long-run distribution is that density, most often with the Metropolis-Hastings accept step. Also: MCMC, Metropolis-Hastings, Metropolis algorithm, random walk Metropolis.

**Textbooks**

- Pattern recognition and machine learning, section 11.2: [pages 553 to 557](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=553). The Metropolis algorithm with a symmetric proposal, drawn as accepted and rejected steps on a 2D Gaussian, then Markov chains, detailed balance and the Metropolis-Hastings algorithm.
- Probabilistic machine learning: advanced topics, sections 12.1 to 12.2: [pages 526 to 531](../../references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=526). The Metropolis-Hastings algorithm (Algorithm 12.1), why it works, and the choice of proposal from the independence sampler to random walk Metropolis.
- Deep learning textbook, section 17.3: [pages 611 to 614](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=611). MCMC for energy-based models: running many chains in parallel, the distribution q(t) over their states converging to the target, and burning in.

**Videos**

- ritvikmath, Coding MCMC, 2:21 to 5:50: [watch](https://www.youtube.com/watch?v=KmqTrm-bn8k&t=141s). One chain written in Python, at its accept or reject step. Chapter-timed, from the video lessons index.
- ritvikmath, Markov Chain Monte Carlo, 4:07 to 8:24: [watch](https://www.youtube.com/watch?v=yApmR-c_hKU&t=247s). Drawing samples by running a Markov chain whose long-run distribution is the target. Chapter-timed, from the video lessons index.
- ritvikmath, Metropolis-Hastings, 7:50 to 12:04: [watch](https://www.youtube.com/watch?v=yCv2N7wGDCw&t=470s). Works out the acceptance probability for a candidate from detailed balance. Chapter-timed, from the video lessons index.
- DataMListic, Metropolis-Hastings Explained, 1:12 to 1:37: [watch](https://www.youtube.com/watch?v=7IpvsfRgTTY&t=72s). A chain run on a heat map: proposals turn green or red, and the samples gather where the density is high. Chapter-timed, from the video lessons index.
- Stanford CS236, lecture 12, 8:35 to 16:25: [watch](https://www.youtube.com/watch?v=Nci1Bepcy0g&t=515s). Sampling an energy-based model with MCMC, accepting or rejecting each move. Chapter-timed, from the video lessons index.

**Papers**

- Du and others 2023, Reduce, reuse, recycle: compositional generation with energy-based diffusion models and MCMC, section 2.2: [page 3](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/sampling-composed-models/compositional-generation-with-energy-based-diffusion-models-and-mcmc.pdf#page=3). Energy-based models and MCMC sampling, naming the unadjusted Langevin, MALA and Hamiltonian samplers the paper composes diffusion models with.

**Our plans and chapters**

- [3. Metropolis-Hastings, and why Z cancels](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/03-metropolis-hastings-and-why-z-cancels.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L3, section 3. Why a product of densities can be sampled without its normalising constant, because Z cancels in the accept ratio.
- [Metropolis-Hastings, run and watched](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/12-metropolis-hastings.md), deep-learning/diffusion-models/02-sampler-correctors-for-composition, plan 12. Justifies the accept-reject rule from detailed balance, then samples a two-Gaussian product at three proposal widths.
- [MCMC sampling](/home/molef/goal-setting/learning/deep-learning/diffusion-models/05-poe-composition-diffusion/plans/06-mcmc-basics.md), deep-learning/diffusion-models/05-poe-composition-diffusion, plan 06. Metropolis-Hastings on a 2D density, predicting the mixing before running it.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook range was read with pdftotext, after finding it through the books' back-of-book indexes. The five video rows are copied from the video lessons index, sections "The Markov chain", "Markov chain Monte Carlo", "The Metropolis-Hastings accept step" and "A Metropolis chain, drawn step by step"; DataMListic is not on the creator list and the user supplied that video. The paper page was read with pdftotext. Each plan and chapter was read at its title and description. Probabilistic machine learning: an introduction mentions MCMC in a paragraph on PDF page 173 and was left out.
