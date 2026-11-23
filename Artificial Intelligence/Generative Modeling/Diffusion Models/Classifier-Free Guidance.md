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
- Principles and practice of deep representation learning, section 7.4.1, Deriving classifier-free guidance: [page 314](../../../Mathematics/references/textbooks/machine-learning/deep-representation-learning.pdf#page=314). Starts from the classifier-guided denoiser with weight γ, uses Bayes' rule and Tweedie's formula to rewrite it as (1 − γ)E[x | x_t] + γE[x | x_t, y] (eq. 7.4.14), and trains one network for both by swapping the label for a null label ∅ with probability p_uncond.

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
- [The Stable Diffusion rebuild, section 8: classifier-free guidance](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/rebuild-stable-diffusion-from-fundamentals.md#8-classifier-free-guidance), papers/deep-learning/diffusion-models/compositional-diffusion-models, on the paper shelf. Ho and Salimans' w is diffusers' γ − 1, and at γ = 5 the guided arrow follows p(c | x) raised to the fifth power; on SDXL the two runs differ by 3.83 and the push is 19.13.
- [Stable Diffusion, read through a small network, section 7: classifier-free guidance pushes past the captioned guess](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/stable-diffusion-read-through-a-small-network.md#7-classifier-free-guidance-pushes-past-the-captioned-guess), papers/deep-learning/diffusion-models/compositional-diffusion-models, on the paper shelf. The network runs with the caption and without it, and γ times the difference of the two guesses is added to the empty-caption guess; on the miniature γ = 2 lands on the true noise.

**Scenes**

- [The SDXL notebook in ten parts, Guidance inside each PoE branch](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-poe). Classifier-free guidance applied to each prompt's branch before the PoE sum.
- [The SDXL notebook in ten parts, Training LoRA against the Mono teacher](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-lora). The student's guided PoE on prompts A and B trained toward a frozen teacher on the joint prompt, with gradients reaching only A and B.
- [SDXL as a latent diffusion model, The latent space lane](https://claude.ai/artifact/KPpMEVBfkJnq3mwgGSbyPs#latent-space). The sampling loop built once and called fifty times: expand, scale, call the UNet, guide, step.
- [SDXL pipeline map, Guidance](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#guidance). Ε̂ = ε_uncond + γ(ε_c − ε_uncond), the two runs combined.
- [SDXL code walk, The caption acts: the empty caption is all zeros](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#zeros). Force_zeros_for_empty_prompt: the empty run reads zeros for C and p, not the encoded empty string.
- [SDXL code walk, The caption acts: the empty run and the captioned run stacked as a batch of two](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#batch_of_two). One U-Net call computes both predictions, empty caption first.
- [SDXL code walk, Guidance: the two predictions combined, the caption's difference times γ](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#guidance). The two runs 0.89 degrees apart, their difference 3.83 multiplied by γ = 5.
- [Readout Guidance loop walk, Ordinary sampler: one U-Net call on the CFG batch, and the features](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#p_unet). The batch doubled to four, classifier-free guidance at γ = 7.5, the taps read.
- [CO3 Corrector Round, Three estimates](https://claude.ai/artifact/9hHS8hf9vtTWHikPVcm52x#estimates). Guidance moving each noise prediction along a line, and the Tweedie estimate as √ᾱ times the clean-latent guess.
- [CO3 Corrector Round, Paper and script](https://claude.ai/artifact/9hHS8hf9vtTWHikPVcm52x#disagree). Guidance 5.0 in section 4.1, 0.8 and 0.9 in appendix A.8, and CFG++ at 0.8 in the released script.
- [Outside Planners and Critics, Fix everything except the guidance rule](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p13). Holding the rest constant within each model so only the guidance rule and its settings change.
- [Outside Planners and Critics, A gain can vanish on another model](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p14). SAG's GenEval gain over CFG on SD3.5 and its result on FLUX.2, each against a printed 95% margin.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook and paper page was read in the PDF with pdftotext, after finding it through the book's back-of-book index or the paper shelf index. Each video row was read in its course's caption-read lecture map under `~/.claude/cache/captions/` or in the video lessons index, and its description paraphrases that row. Each plan and chapter was read at its title and opening. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start.
