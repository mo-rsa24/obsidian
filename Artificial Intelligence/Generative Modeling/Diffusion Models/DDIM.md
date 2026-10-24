---
aliases: [DDIM, denoising diffusion implicit model, DDIM sampler]
standard: vault-note v2
---

# DDIM

Up: [[Diffusion Models]]

Artificial Intelligence, Generative Modeling, Diffusion Models. It samples a network trained exactly as in [[Diffusion Models]], on the noising of [[The Forward Process]].

**DDIM samples a trained diffusion model through a family of non-Markovian reverse steps that keep DDPM's marginals, and with its noise set to zero the sampler is deterministic and can skip most of the steps.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches DDIM writes the rest around it.

## Where to learn this

**DDIM**, the denoising diffusion implicit model. Also: denoising diffusion implicit model, DDIM sampler.

**Textbooks**

- Understanding deep learning, section 18.6: [pages 378 to 379](../../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=378). Shows on one-dimensional data that the same trained model serves a family of processes: five DDPM trajectories, five deterministic DDIM trajectories and an accelerated sampler that skips steps, each with its histogram against the true density (Figure 18.10).
- Probabilistic machine learning: advanced topics, section 25.5.1: [page 905](../../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=905). The non-Markovian forward step q(x_{t−1} ∣ x_t, x_0) and its reverse with the predicted x̂_0, which becomes fully deterministic when σ̃_t² = 0.

**Videos**

- CME296 lecture 1, 1:34:43 to 1:41:26: [watch](https://www.youtube.com/watch?v=tr-CUpw--ck&t=5683s). Builds DDIM as a family q_σ with the same marginals q(x_t ∣ x_0) as DDPM, where σ = 0 gives a deterministic sampler that predicts x_0 at each step. Caption-read.
- CME296 lecture 1, 1:41:26 to 1:46:02: [watch](https://www.youtube.com/watch?v=tr-CUpw--ck&t=6086s). Skips steps along a subsequence τ for a speed-up T/S of about 10 to 50 times, with FID plotted against the number of steps. Caption-read.
- CME296 lecture 1, 1:29:34 to 1:34:43: [watch](https://www.youtube.com/watch?v=tr-CUpw--ck&t=5374s). The problem DDIM solves: about 1,000 sampling steps, and why skipping steps with the stochastic DDPM update degrades quality. Caption-read.

**Papers**

- Chan 2024, Tutorial on diffusion models for imaging and vision, section 2.6: [pages 39 to 43](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=39). Why DDPM is slow, the noise in the x_{t−1} marginal replaced by an estimate, the DDIM transition distribution (Theorem 2.9), and the sampling step set beside DDPM's.

**Our plans and chapters**

- [DDIM as a discretised probability flow ODE](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l4-continuous-time/07-ddim-as-a-discretised-ode.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L4, section 7. Derives the DDIM update as one Euler step in rescaled coordinates and proves that for data at a single point it is exact at any step count.
- [DDIM as a discretised probability flow ODE](/home/molef/goal-setting/learning/deep-learning/diffusion-models/03-score-sde/plans/03-ddim-as-a-discretised-ode.md), deep-learning/diffusion-models/03-score-sde, plan 03. Works the same derivation as a 60-minute sitting, then samples the toy in 10, 50 and 1000 steps with DDIM, the ancestral sampler and plain Euler, and compares all three.
- [DDIM: the non-Markovian chain, and why determinism made the dial readable](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/32-ddim-non-markovian-and-deterministic-limit.md), deep-learning/diffusion-models/02-sampler-correctors-for-composition, plan 32. Derives DDIM's family of reverse steps, picks the member the project's scheduler uses, and checks that a fixed start retraces its path.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook and paper page range was read in the PDF with pdftotext; the textbook pages were found through the books' back-of-book indexes ("DDIM" and "denoising diffusion implicit model"). Understanding deep learning's other index page, PDF page 384, is a notes paragraph and has no line. The three CME296 rows were read in its caption-read lecture map under `~/.claude/cache/captions/` and paraphrase the map. The video lessons index sections "DDIM" and "DDIM as an ODE solver" cite the same lecture from 1:29:49, a start time read separately from the captions; the map rows are used here. Each plan and chapter was read at its title and description.
