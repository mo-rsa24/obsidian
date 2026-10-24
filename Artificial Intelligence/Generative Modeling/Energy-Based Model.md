---
aliases: [energy-based model, energy based model, EBM, energy function]
standard: vault-note v2
---

# Energy-Based Model

Up: [[Generative Modeling]]

Artificial Intelligence, Generative Modeling. A diffusion model written as an energy is [[The Energy Parameterisation]], and the gradient that ignores the normaliser is the [[Score Function]].

**An energy-based model defines a density through a scalar energy, p(x) = exp(−E(x))/Z, so low energy means high probability, and the normaliser Z is usually never computed.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches energy-based models writes the rest around it.

## Where to learn this

**Energy-based model (EBM)**, a density written as exp(−E(x))/Z. Also: EBM, energy function.

**Textbooks**

- Deep learning textbook, sections 16.2.3 to 16.2.4: [pages 585 to 586](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=585). Works the normaliser on one scalar first: φ(x) = x² has a divergent Z and defines no distribution, while exp(−βx²) normalises only for β > 0; then names E(x) the energy function and p̃(x) = exp(−E(x)) an energy-based model.
- Probabilistic machine learning: advanced topics, sections 24.1 to 24.2: [pages 872 to 874](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=872). The EBM as a Gibbs distribution with energy E_θ and partition function Z_θ, two energies summed to multiply their densities (Figure 24.1) as a product of experts, and why maximum likelihood is hard when Z_θ is intractable.
- The little book of generative AI foundations, section 8.3: [pages 173 to 176](../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=173). The energy as a modelling primitive, the Boltzmann form and its partition function, and learning an energy landscape so data sits in its valleys.
- The little book of generative AI foundations, section 8.4.3, Score matching as energy-gradient learning: [page 179](../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=179). Shows the score of an energy-based model is −∇E(x), so the partition function drops out and score matching trains the energy without it.

**Videos**

- Stanford CS236 lecture 11, 4:42 to 6:45: [watch](https://www.youtube.com/watch?v=m61KiAMCJ5Q&t=282s). What an energy-based model is. Chapter-timed, from the video lessons index.
- Stanford CS236 lecture 11, 15:31 to 23:01: [watch](https://www.youtube.com/watch?v=m61KiAMCJ5Q&t=931s). The partition function, the constant that turns an energy into a density. Chapter-timed, from the video lessons index.
- Stanford CS236 lecture 11, 29:14 to 34:29: [watch](https://www.youtube.com/watch?v=m61KiAMCJ5Q&t=1754s). How an energy function is defined. Chapter-timed, from the video lessons index.
- Vizuara, Principles of Diffusion Models, lecture 5, 24:00 to 30:11: [watch](https://www.youtube.com/watch?v=zRyD7GQ9RHs&t=1440s). Why energy-based models are hard to train, and where the score comes in. Chapter-timed, from the video lessons index.

**Papers**

- Du and others 2023, Reduce, reuse, recycle: compositional generation with energy-based diffusion models and MCMC, sections 2.2 to 2.3: [pages 2 to 3](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/sampling-composed-models/compositional-generation-with-energy-based-diffusion-models-and-mcmc.pdf#page=2). EBMs and the MCMC samplers they need, then how a diffusion model can be read as one, with the noise prediction as the gradient of a learned scalar.
- Liu and others 2022, Compositional visual generation with composable diffusion models, sections 3.2 and 4.1: [page 5](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/sampling-composed-models/compositional-visual-generation-with-composable-diffusion-models.pdf#page=5). The EBM density p_θ(x) ∝ exp(−E_θ(x)), then diffusion models interpreted as energy-based models so their energies can be added.

**Our plans and chapters**

- [Partition function and free energy](/home/molef/goal-setting/learning/deep-learning/diffusion-models/05-poe-composition-diffusion/plans/14-partition-function-free-energy.md), deep-learning/diffusion-models/05-poe-composition-diffusion, plan 14. Computes Z and the free energy F for a 4-spin chain by hand, then checks them by brute-force enumeration in code.
- [Energy: p proportional to exp(-E)/Z, and why the score never sees Z](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/04-energy-and-the-missing-normaliser.md), deep-learning/diffusion-models/02-sampler-correctors-for-composition, plan 04. The energy form and why the normaliser drops out of the score.
- [A scalar energy whose gradient is the noise prediction](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/34-a-scalar-energy-whose-gradient-is-the-score.md), the same journey, plan 34. Asks whether a network's arrows are the slope of any height function, the step that turns a diffusion model into an energy model.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The vault was searched first: [[The Energy Parameterisation]] owns "energy-based diffusion model" and "scalar energy" but not "energy-based model", "EBM" or "energy function", so this is a new note rather than an extension of it. Each textbook and paper page range was read in the PDF with pdftotext, after the back-of-book indexes and the shelf index's chapter tables pointed to them ("energy-based model", "EBM" and "energy function"). The four video rows are copied from the video lessons index, `Mathematics/references/videos/Video Lessons.md`, sections "Energy-based models and the partition function" and "The energy of an energy-based model", whose times are chapter boundaries; no row in the four Stanford lecture maps teaches energy-based models. Each plan was read at its title and description.
