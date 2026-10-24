---
aliases: [Langevin dynamics, Langevin, Langevin sampling, Langevin Monte Carlo, Langevin MCMC, Langevin diffusion, Langevin equation, Langevin SDE, overdamped Langevin]
standard: vault-note v2
---

# Langevin Dynamics

Up: [[Markov Chain Monte Carlo]]

Mathematics, Statistics, Markov Chain Monte Carlo. Needs: [[Score Function]]. The annealed version and the step-size limit are in [[Annealed MCMC]] and [[Step Size And The Accept Step]].

**Langevin dynamics draws samples from p by stepping along the score ∇ log p(x) and adding Gaussian noise at every step, so the walk settles into p rather than onto its peak.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches Langevin dynamics writes the rest around it.
> - [[Annealed MCMC]] carries "ULA" and "unadjusted Langevin algorithm" as aliases, which name the update this note teaches; whether they move here is the learner's call.

## Where to learn this

**Langevin dynamics**, and the Langevin sampler built from it. Also: Langevin sampling, Langevin Monte Carlo, Langevin MCMC, Langevin diffusion, Langevin equation.

**Textbooks**

- The little book of generative AI foundations, sections 6.1.2 and 6.1.3: [pages 115 to 117](../../references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=115). The Langevin SDE dXₜ = ∇ log p*(Xₜ) dt + √2 dWₜ and its discrete update, drift for moving uphill and noise against collapse, then the Ornstein-Uhlenbeck case whose stationary law is the target.
- Probabilistic machine learning: advanced topics, sections 12.5.6 and 12.5.7: [pages 548 to 549](../../references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=548). Langevin Monte Carlo (MALA) as one-step HMC with an accept step, the Langevin diffusion SDE, the unadjusted algorithm, and the link to stochastic gradient descent.
- Probabilistic machine learning: advanced topics, section 24.2.1: [page 875](../../references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=875). Langevin MCMC on an energy-based model, where the score is −∇ₓE_θ(x) so the normaliser drops out (equation 24.18).
- The little book of generative AI foundations, section 6.4.2: [page 130](../../references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=130). Annealed Langevin dynamics: Langevin updates at each noise level from large σ to small.

**Videos**

- CME296 lecture 2, 14:26 to 18:33: [watch](https://www.youtube.com/watch?v=_WaR2fjZpEQ&t=866s). Following the score alone collapses onto the densest region, so Langevin sampling adds a noise term at each step. Caption-read.
- CME296 lecture 2, 53:42 to 58:25: [watch](https://www.youtube.com/watch?v=_WaR2fjZpEQ&t=3222s). Annealed Langevin dynamics, run at each noise level from the largest σ to the smallest with the score as a compass. Caption-read.
- Stanford CS236 lecture 16, 5:30 to 9:30: [watch](https://www.youtube.com/watch?v=VsllsC2JMGY&t=330s). Following the score uphill with noise added. Chapter-timed, from the video lessons index.
- Stanford CS236 lecture 14, 5:44 to 9:13: [watch](https://www.youtube.com/watch?v=E69Lp_T9nVg&t=344s). Where plain Langevin sampling fails. Chapter-timed, from the video lessons index.

**Papers**

- Chan 2024, Tutorial on diffusion models for imaging and vision: [pages 44 to 47](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=44). Langevin sampling as gradient ascent on log p plus noise (equation 3.1), Theorem 3.1 that p is its stationary law, and a Gaussian mixture sampled with and without the noise.
- Chan 2024, the same tutorial, section 5: [pages 66 to 72](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=66). The Langevin equation from physics: a pollen grain under drag and a random force, then the Wiener process.
- Du and others 2023, Reduce, reuse, recycle: [page 3](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/sampling-composed-models/compositional-generation-with-energy-based-diffusion-models-and-mcmc.pdf#page=3). Defines unadjusted Langevin dynamics (ULA) for energy-based models and adds the Metropolis correction that makes it MALA.

**Our plans and chapters**

- [Langevin dynamics and its stationary law](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/08-langevin-dynamics-and-its-stationary-law.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L3, section 8. Langevin dynamics after the Ornstein-Uhlenbeck process, and why p is what it settles into.
- [Annealed Langevin, worked by hand on two sensors](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/11-annealed-langevin-worked-by-hand-on-two-sensors.md), volume L3, section 11. The annealed sampler worked by hand.
- [Langevin dynamics, and p as its stationary law](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/21-langevin-dynamics.md), deep-learning/diffusion-models/02-sampler-correctors-for-composition, plan 21. The same law as the step before predictor-corrector sampling.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-22. Each textbook and paper page range was read in the PDF with pdftotext; the Probabilistic machine learning: advanced topics pages were first found through its back-of-book index (PDF pages 1256 to 1273, PDF page = printed page + 33). The two CME296 rows were read in its caption-read lecture map under `~/.claude/cache/captions/`, and their descriptions paraphrase the map, never the machine-translated captions. The two CS236 rows are copied from the video lessons index, `Mathematics/references/videos/Video Lessons.md`, sections "Langevin sampling" and "Annealed Langevin sampling", whose times are chapter boundaries. Each plan and chapter was read at its title and opening. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map or the video lessons index.
