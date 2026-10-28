---
aliases: [classifier-free guidance, classifier free guidance, CFG]
link-skip: [context-free grammar]
standard: vault-note v2
---

# Classifier-Free Guidance

Up: [[Diffusion Models]]

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[Score Function]]. How the guidance scale differs from a temperature is in [[Three Things Called Annealing]], and guidance read as a product is in [[Product, Mixture And Negation]].

**Classifier-free guidance steers a diffusion model toward a condition by taking its unconditional prediction and adding ω times the difference between the conditional and unconditional predictions, both made by one network trained with the condition sometimes dropped.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches classifier-free guidance writes the rest around it.

## Where to learn this

**Classifier-free guidance (CFG)**, ε̂ = ε_∅ + ω(ε_c − ε_∅). Also: classifier free guidance, CFG.

**Textbooks**

- Probabilistic machine learning: advanced topics, section 25.6.3, Classifier-free guidance: [page 909](../../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=909). Derives the implicit classifier from Bayes' rule, log p(c|x) = log p(x|c) + log p(c) − log p(x), with one network that sets c = ∅ for the unconditional case, then writes the guided score.
- Understanding deep learning, section 18.6.3, Conditional generation: [page 379](../../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=379). Feeds the class into the U-Net the way the time step is added and trains on conditional and unconditional objectives by randomly dropping the class.

**Videos**

- CS231n lecture 14, 45:30 to 50:05: [watch](https://www.youtube.com/watch?v=Edr4uZFh4EE&t=2730s). Drops the label to a null value half the time in training and combines v_cfg = (1 + w) v_y − w v_null at sampling, where w = 0 recovers the conditional model, at twice the cost per step. Caption-read.
- CME296 lecture 4, 1:34:25 to 1:40:38: [watch](https://www.youtube.com/watch?v=WUUq6TVAu8U&t=5665s). Derives the implicit classifier from the conditional and unconditional predictions with a weight w of about 3, the condition dropped 10 to 20% of the time, at two forward passes per step. Caption-read.
- Umar Jamil, Coding Stable Diffusion from scratch, 22:20 to 31:00: [watch](https://www.youtube.com/watch?v=ZBKpAp_6TGI&t=1340s). Classifier-free guidance, and how it steers sampling toward the prompt. Chapter-timed, from the video lessons index.

**Papers**

- Liu and others 2022, Compositional visual generation with composable diffusion models, section 4.2: [page 7](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/sampling-composed-models/compositional-visual-generation-with-composable-diffusion-models.pdf#page=7). Composes concepts as p(x) ∏ p(c_i|x) and notes that with a single concept the sampler reduces to classifier-free guidance.
- Skreta and others 2025, Feynman-Kac correctors in diffusion, section 3.2: [page 4](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/sampling-composed-models/feynman-kac-correctors-in-diffusion.pdf#page=4). Reads guidance as an attempt to sample the geometric average of an unconditional and a conditional model, (1 − β)∇ log q¹ + β∇ log q², which the plain guided sampler does not reach.

**Our plans and chapters**

- [CFG trained on MNIST, a w sweep](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/plans/08-cfg-trained-on-mnist.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, plan 08. Trains a guided model on MNIST and sweeps the guidance weight w.
- [Classifier-free guidance as base plus omega times a difference](/home/molef/goal-setting/learning/deep-learning/diffusion-models/05-poe-composition-diffusion/plans/02-cfg-as-base-plus-omega-difference.md), deep-learning/diffusion-models/05-poe-composition-diffusion, plan 02. Rewrites the guidance update as u_base + ω(u_guided − u_unguided) by hand and names which term plays each role.
- [1.1 Classifier-free guidance, one concept, one line](/home/molef/goal-setting/learning/deep-learning/diffusion-models/10-plurality-and-timestep-scheduling/textbook/01-the-and-operator-derived.md#11-classifier-free-guidance-one-concept-one-line), deep-learning/diffusion-models/10-plurality-and-timestep-scheduling, chapter 01. States the single-concept form ε̂ = ε_∅ + ω(ε_c − ε_∅) as the starting point for the AND of n concepts.

**Scenes**

- [The SDXL notebook in ten parts, Guidance inside each PoE branch](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-poe). Classifier-free guidance applied to each prompt's branch before the PoE sum.
- [The SDXL notebook in ten parts, Training LoRA against the Mono teacher](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-lora). The student's guided PoE on prompts A and B trained toward a frozen teacher on the joint prompt, with gradients reaching only A and B.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook and paper page was read in the PDF with pdftotext, after finding it through the book's back-of-book index or the paper shelf index. Each video row was read in its course's caption-read lecture map under `~/.claude/cache/captions/` or in the video lessons index, and its description paraphrases that row. Each plan and chapter was read at its title and opening. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start.
