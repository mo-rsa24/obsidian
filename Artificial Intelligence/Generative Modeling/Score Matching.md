---
aliases: [score matching, denoising score matching, DSM, explicit score matching, implicit score matching, sliced score matching]
standard: vault-note v2
---

# Score Matching

Up: [[Generative Modeling]]

Artificial Intelligence, Generative Modeling. What it learns is the [[Score Function]], and [[Langevin Dynamics]] samples with what it learned.

**Score matching trains a network s_θ(x) to match the score ∇ₓ log p(x) of data whose density is unknown, and denoising score matching makes that practical by regressing onto the known score of a noised copy of each data point.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches score matching writes the rest around it.
> - The placement is unsure. The two best places are `Artificial Intelligence/Generative Modeling/` and `Artificial Intelligence/Generative Modeling/Diffusion Models/`.

## Where to learn this

**Score matching**, fitting a model's score to the data's score. Also: denoising score matching, DSM, implicit score matching, sliced score matching.

**Textbooks**

- The little book of generative AI foundations, sections 6.2 to 6.3: [pages 119 to 127](../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=119). Works the one-dimensional case first, removing the unknown data score from the Fisher divergence by integration by parts, then the d-dimensional loss, then denoising score matching as least-squares regression with a figure of individual denoising targets averaging to the noisy score.
- Probabilistic machine learning: advanced topics, section 24.3: [pages 879 to 882](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=879). Score matching as minimising the Fisher divergence for an energy model, then denoising score matching (Vincent's identity) and why a small noise level makes it high-variance, then sliced score matching at a cost linear in the dimension.
- Deep learning textbook, sections 18.4 to 18.5: [pages 633 to 636](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=633). Score matching as a way to train a model without its partition function, its per-example loss (equation 18.25), why it cannot handle discrete data, and denoising score matching.

**Videos**

- CME296 lecture 2, 18:33 to 21:08: [watch](https://www.youtube.com/watch?v=_WaR2fjZpEQ&t=1113s). Writes the score matching loss, notes it needs the unknown true score, and names implicit and sliced score matching as the older workarounds. Caption-read.
- CME296 lecture 2, 29:31 to 38:28: [watch](https://www.youtube.com/watch?v=_WaR2fjZpEQ&t=1771s). States denoising score matching (score matching on the noised distribution equals regression on the tractable conditional score, up to a constant) and sketches the proof by expanding the squared norm. Caption-read.
- Stanford CS236 lecture 12, 38:02 to 46:28: [watch](https://www.youtube.com/watch?v=Nci1Bepcy0g&t=2282s). Integration by parts removes the unknown data score from the Fisher divergence. Chapter-timed, from the video lessons index.
- Stanford CS236 lecture 13, 29:16 to 44:39: [watch](https://www.youtube.com/watch?v=8G-OsDs1RLI&t=1756s). Denoising score matching, derived. Chapter-timed, from the video lessons index.

**Papers**

- Chan 2024, Tutorial on diffusion models for imaging and vision, section 3.3: [pages 49 to 53](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=49). Explicit score matching against a kernel density estimate, implicit score matching, then denoising score matching, where s_θ(x + σz) is trained toward −z/σ, and its multi-noise-level loss.

**Our plans and chapters**

- [Chapter 13: Derive the training loss two ways: score matching and the ELBO](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/13-the-training-loss-two-ways.md), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 13. Hyvärinen's objective by integration by parts with its boundary term, then denoising score matching worked to its linear-model optimum −1/(1 + σ²).
- [Score matching: how the score gets learned](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/20-score-matching-the-training-objective.md), deep-learning/diffusion-models/01-poe-derivation-foundations, plan 20. The sitting that works that chapter, a branch taken after noise prediction is shown to be the score.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/ch6-score-based-models.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/ch6-score-based-models.jpg" width="200" alt="A cat fading to noise, the reverse SDE with its score term highlighted, a parameterised score box, and the score matching loss"></a> Sophia Tang, "Foundations of Schrödinger Bridges for Generative Modeling", chapter 6 figure: [the paper](https://arxiv.org/abs/2603.18992), [what it shows](/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/README.md#ch6-score-based-modelsjpg). A cat fades to noise along the forward SDE, the score term of the reverse SDE is highlighted and stood in for by a network s_θ(x, s), and the bottom box is the score-matching loss, the λ(t)-weighted squared gap between the two, fed by every frame of the noising row.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook and paper page range was read in the PDF with pdftotext, after the back-of-book indexes and the shelf index's chapter tables pointed to them ("score matching", "denoising score matching" and "sliced score matching" in Probabilistic machine learning: advanced topics and the Deep learning textbook). The Deep learning textbook's other index page, PDF page 529, is a short mention in the autoencoders chapter and has no line. The two CME296 rows were read in its caption-read lecture map under `~/.claude/cache/captions/` and paraphrase the map. The two CS236 rows are copied from the video lessons index, `Mathematics/references/videos/Video Lessons.md`, sections "Score matching" and "Denoising score matching", whose times are chapter boundaries. Each plan and chapter was read at its title and description.
