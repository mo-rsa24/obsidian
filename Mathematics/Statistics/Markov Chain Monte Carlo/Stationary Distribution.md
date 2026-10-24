---
aliases: [stationary distribution, invariant distribution, equilibrium distribution, steady-state distribution, steady-state vector, detailed balance, detailed balance condition]
standard: vault-note v2
---

# Stationary Distribution

Up: [[Markov Chain Monte Carlo]]

Mathematics, Statistics, Markov Chain Monte Carlo. [[Markov Chain]] holds the card for the chain itself, and [[Langevin Dynamics]] is a sampler whose stationary distribution is the target density.

**A stationary distribution of a Markov chain is one the chain hands back unchanged after a step, so a chain started there stays there; detailed balance, equal probability flow each way between every pair of states, is the usual way to prove a chain has one.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches stationary distributions writes the rest around it.
> - The [[Markov Chain Monte Carlo]] note does not list this note yet.

## Where to learn this

**Stationary distribution**, the distribution a Markov chain leaves unchanged, and the detailed balance condition that guarantees it. Also: invariant distribution, equilibrium distribution, steady-state vector, detailed balance.

**Textbooks**

- Linear algebra textbook, section 10.4: [pages 568 to 571](../../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=568). Regular transition matrices (Definition 3), the powers Pⁿ and the state vectors Pⁿx converging to a fixed steady-state vector (Theorems 10.4.2 and 10.4.3), worked on the section's example chains.
- Probabilistic machine learning: advanced topics, section 2.6.4: [pages 84 to 88](../../references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=84). What a stationary distribution is, how to compute it, when it exists, and detailed balance.
- Pattern recognition and machine learning, section 11.2.1: [pages 555 to 556](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=555). Invariant distributions, detailed balance as a sufficient condition, and ergodicity, as the ground for Metropolis-Hastings.
- Stochastic differential equations, section 9.8: [pages 219 to 222](../../references/textbooks/calculus/stochastic-differential-equations.pdf#page=219). Stationary distributions of a diffusion process, how many there can be, and detailed balance in continuous time.

**Videos**

- ritvikmath, Markov Chain Stationary Distribution, Solving, 6:20 to 13:00: [watch](https://www.youtube.com/watch?v=4sXiCxZDrTU&t=380s). Solves for the example chain's stationary distribution. Chapter-timed.
- ritvikmath, Markov Chain Stationary Distribution, Steady State, 3:06 to 6:20: [watch](https://www.youtube.com/watch?v=4sXiCxZDrTU&t=186s). What it means for a chain to reach a steady state. Chapter-timed.
- ritvikmath, Markov Chains, The Steady State, 4:09 to 8:41: [watch](https://www.youtube.com/watch?v=prZMpThbU3E&t=249s). The steady state of the video's example chain. Chapter-timed.
- ritvikmath, Markov Chain Monte Carlo, 8:24 to 12:10: [watch](https://www.youtube.com/watch?v=yApmR-c_hKU&t=504s). The detailed balance condition. Chapter-timed, from the video lessons index.
- DataMListic, Metropolis-Hastings Explained, 1:37 to 2:00: [watch](https://www.youtube.com/watch?v=7IpvsfRgTTY&t=97s). Detailed balance as two probability flows between a pair of states, flow out equal to flow in. Chapter-timed, from the video lessons index.

**Our plans and chapters**

- [2. Stationarity and detailed balance](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/02-stationarity-and-detailed-balance.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L3, section 2. Names the distribution two runs of a chain meet at, and proves detailed balance is enough to make it stationary.
- [Stationary distributions and detailed balance](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/11-stationary-and-detailed-balance.md), deep-learning/diffusion-models/02-sampler-correctors-for-composition, plan 11. Checks by hand whether a chain's resting distribution is the product bell wanted, on a two-state matrix and a Gaussian.
- [Langevin's stationary distribution](/home/molef/goal-setting/learning/deep-learning/diffusion-models/06-diffusion-speciation-dynamics/plans/05-composition-and-the-experiment/plans/02-langevin-stationary-distribution.md), deep-learning/diffusion-models/06-diffusion-speciation-dynamics, plan 05.02. The stationary distribution of the Langevin process, built on the Boltzmann density.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook range was read with pdftotext, after finding it through the books' back-of-book indexes. The two ritvikmath chapter lists were read with cache-video-chapters.py and those lines are described from their chapter titles only. The ritvikmath detailed-balance row and the DataMListic row are copied from the video lessons index, sections "Markov chain Monte Carlo" and "A Metropolis chain, drawn step by step"; DataMListic is not on the creator list and the user supplied that video. Each plan and chapter was read at its title and opening lines. Probabilistic machine learning: advanced topics also derives detailed balance for Metropolis-Hastings in section 12.2.2 (PDF page 528), which sits on the [[Markov Chain Monte Carlo]] card's range.
