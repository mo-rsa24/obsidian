---
aliases: [product of experts, products of experts, product-of-experts, PoE]
link-skip: [and "poe, poe plan]
standard: vault-note v2
---

# Product Of Experts

Up: [[Generative Modeling]]

Artificial Intelligence, Generative Modeling. Needs: [[Energy-Based Model]]. Composing diffusion models as a product is in [[Composing Models With A Background]] and [[The Product As An Intersection]].

**A product of experts multiplies several models' densities and renormalises, p(x) ∝ p₁(x) p₂(x) ⋯, so the product is high only where every expert gives x some probability.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the product of experts writes the rest around it.

## Where to learn this

**Product of experts (PoE)**, p(x) ∝ ∏ pᵢ(x), equivalently a sum of energies. Also: products of experts, product-of-experts, PoE.

**Textbooks**

- Probabilistic machine learning: advanced topics, section 24.1.1, Example: products of experts (PoE): [page 873](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=873). Multiplies a model of thermally stable proteins by a model of proteins that bind, so the product favours only proteins both experts like, and does it by summing their energies (Figure 24.1).
- Deep learning, section 16.2.4, Energy-based models: [page 587](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=587). Reads each term of an energy function as an expert enforcing one soft constraint, so multiplying their probabilities enforces a complicated high-dimensional one (Hinton, 1999).
- Probabilistic machine learning: advanced topics, section 4.3.3, MRFs with latent variables: [page 206](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=206). Shows a restricted Boltzmann machine's p(x|z) as a product over its active hidden units, a distributed representation set against a mixture's single prototype.
- Computer vision textbook, section 10.3, Undirected graphical models: [page 225](../../Mathematics/references/textbooks/computer-vision/computer-vision-textbook.pdf#page=225). Names an undirected model whose every potential addresses all the variables a product of experts, before turning to cliques.

**Videos**

- Stanford CS236 lecture 11, 23:01 to 29:14: [watch](https://www.youtube.com/watch?v=m61KiAMCJ5Q&t=1381s). Composing normalised models into one. Chapter-timed, from the video lessons index.

**Papers**

- Liu and others 2022, Compositional visual generation with composable diffusion models, section 4.2: [page 7](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/sampling-composed-models/compositional-visual-generation-with-composable-diffusion-models.pdf#page=7). Concept conjunction (AND) as the product p(x) ∏ p(c_i|x) over diffusion models, one per concept.
- Skreta and others 2025, Feynman-Kac correctors in diffusion, Proposition 3.3: [page 5](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/sampling-composed-models/feynman-kac-correctors-in-diffusion.pdf#page=5). The weighted SDE that samples the product of two diffusion models' marginals, with the correction that adding their scores alone misses.
- Zhang and others 2025, Product of experts for visual generation, sections 2 and 3: [pages 2 to 3](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/sampling-composed-models/product-of-experts-for-visual-generation.pdf#page=2). Treats image and video generators, vision-language models and simulators as experts over parts of a scene and samples their product.

**Our plans and chapters**

- [PoE on two Gaussians, end to end](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/13-poe-on-two-gaussians.md), deep-learning/diffusion-models/01-poe-derivation-foundations, plan 13. Composes two 2D Gaussians three separate ways that must agree, then pushes the setup until they stop agreeing and names why.
- [The PoE rule, assembled](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/12-the-poe-rule-assembled.md), deep-learning/diffusion-models/01-poe-derivation-foundations, plan 12. Puts the scores, the subtracted unconditional term and epsilon as minus sigma times the score together into one rule.
- [Product of experts and its normaliser](/home/molef/goal-setting/learning/deep-learning/diffusion-models/05-poe-composition-diffusion/plans/07-poe-factorisation-and-normaliser.md), deep-learning/diffusion-models/05-poe-composition-diffusion, plan 07. Writes the product's density with its normalising constant by hand.
- [The assumption PoE rests on](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/02-the-assumption-poe-rests-on.md), deep-learning/diffusion-models/01-poe-derivation-foundations, plan 02. The conditional independence the derivation needs, and the tool that turns it into a formula.
- [Textbook: deriving product of experts from the ground up](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/00-index.md), deep-learning/diffusion-models/01-poe-derivation-foundations, the textbook index. Every chapter of the derivation in reading order.

**Scenes**

- [Kinds of composition notebook, Four kinds of composition](https://claude.ai/artifact/DBmJtn6xy75sPtQwPEvQZU#nb-sec5). Co-occurrence, contention and interaction computed as products of two experts' densities on one grid.
- [SDXL cross-attention, PoE and LoRA notebook, PoE fails on cat and dog](https://claude.ai/artifact/RP59hpFThMPmbftvvWPpbi#nb-sec13). Adding a cat expert's score to a dog expert's lands at the origin, distance 2 from both modes, while the two-mode mixture's score keeps both.
- [SDXL cross-attention, PoE and LoRA notebook, Guidance inside each PoE branch](https://claude.ai/artifact/RP59hpFThMPmbftvvWPpbi#nb-sec14). Classifier-free guidance applied to each prompt's branch before the PoE sum.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook and paper page was read in the PDF with pdftotext, after finding it through the book's back-of-book index or the paper shelf index. The video row was read in the video lessons index, and its description paraphrases that row. Each plan and chapter was read at its title and opening. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start.
