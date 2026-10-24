---
aliases: [Hamiltonian Monte Carlo, HMC, hybrid Monte Carlo, Hamiltonian dynamics, leapfrog integrator, leapfrog step, leapfrog steps]
standard: vault-note v2
---

# Hamiltonian Monte Carlo

Up: [[Markov Chain Monte Carlo]]

Mathematics, Statistics, Markov Chain Monte Carlo. [[Annealed MCMC]] uses its unadjusted form (U-HMC) to compose diffusion models, and [[Langevin Dynamics]] is the sampler without momentum.

**Hamiltonian Monte Carlo gives each sample a random momentum, moves it along the Hamiltonian dynamics of the target's energy with a few leapfrog steps, and accepts or rejects the end point, so it travels far in one move while keeping the target distribution.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches Hamiltonian Monte Carlo writes the rest around it.
> - The [[Markov Chain Monte Carlo]] note does not list this note yet.

## Where to learn this

**Hamiltonian Monte Carlo**, MCMC that adds a momentum and simulates its motion before the accept step. Also: HMC, hybrid Monte Carlo, Hamiltonian dynamics, leapfrog integrator.

**Textbooks**

- Pattern recognition and machine learning, section 11.5: [pages 564 to 569](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=564). Dynamical systems with position, momentum and the Hamiltonian, the leapfrog discretization, then hybrid Monte Carlo with its Metropolis accept step.
- Probabilistic machine learning: advanced topics, sections 12.5.1 to 12.5.4: [pages 543 to 547](../../references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=543). Hamiltonian mechanics, integrating Hamilton's equations (Euler, modified Euler, leapfrog), the HMC algorithm, and tuning its step count with NUTS and its step size.

**Videos**

- Meerkat Statistics, Hamiltonian Monte Carlo, 1:26 to 2:22: [watch](https://www.youtube.com/watch?v=2zr7cMjltAI&t=86s). The Hamiltonian physics mapped onto sampling. Chapter-timed, from the video lessons index.
- Meerkat Statistics, Hamiltonian Monte Carlo, 2:22 to 3:08: [watch](https://www.youtube.com/watch?v=2zr7cMjltAI&t=142s). Sampling a momentum for the sample. Chapter-timed, from the video lessons index.
- Meerkat Statistics, Hamiltonian Monte Carlo, 3:08 to 6:38: [watch](https://www.youtube.com/watch?v=2zr7cMjltAI&t=188s). Simulating the system's dynamics, position and momentum moving together. Chapter-timed, from the video lessons index.
- Meerkat Statistics, Hamiltonian Monte Carlo, 8:49 to 10:33: [watch](https://www.youtube.com/watch?v=2zr7cMjltAI&t=529s). The numerical error a finite step leaves, and the accept step that corrects it. Chapter-timed, from the video lessons index.
- Ben Lambert, The intuition behind Hamiltonian Monte Carlo, 10:17 to 16:58: [watch](https://www.youtube.com/watch?v=a-wydhEuAm0&t=617s). The joint distribution over position and momentum. Chapter-timed, from the video lessons index.

**Papers**

- Du and others 2023, Reduce, reuse, recycle: compositional generation with energy-based diffusion models and MCMC, appendix B.1: [pages 12 to 14](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/sampling-composed-models/compositional-generation-with-energy-based-diffusion-models-and-mcmc.pdf#page=12). HMC with the leapfrog integrator and its simplified accept probability (Algorithm 2), the unadjusted U-HMC, and partial momentum refreshment (Algorithm 3).
- Sjöberg and others 2023, MCMC-correction of score-based diffusion models for model composition, section 2.4: [page 4](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/sampling-composed-models/mcmc-correction-of-score-based-diffusion-models-for-model-composition.pdf#page=4). U-HMC with momenta and leapfrog steps under a learned score, and the accept step that turns it into standard HMC.

**Our plans and chapters**

- [9. Hamiltonian dynamics, and what momentum buys](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/09-hamiltonian-dynamics-and-what-momentum-buys.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L3, section 9. Why Langevin crawls through the low-density gap between two modes, and how momentum carries a sample across it.
- [The Hamiltonian corrector, and what momentum buys](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/23-the-hamiltonian-corrector.md), deep-learning/diffusion-models/02-sampler-correctors-for-composition, plan 23. Derives the Hamiltonian and its conservation, then builds momentum crossing a barrier Langevin cannot.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook range was read with pdftotext, after finding it through the books' back-of-book indexes. The five video rows are copied from the video lessons index, sections "Hamiltonian Monte Carlo" and "The leapfrog step"; Meerkat Statistics and Ben Lambert are open-web creators, because no listed creator has a Hamiltonian Monte Carlo video. Both paper ranges were read with pdftotext. Each plan and chapter was read at its title and opening lines. [[Annealed MCMC]] owns "U-HMC" and "unadjusted HMC" and no alias here repeats them. Probabilistic machine learning: an introduction names HMC in one sentence on PDF page 174 and was left out.
