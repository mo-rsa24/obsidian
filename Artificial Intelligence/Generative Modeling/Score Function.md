---
aliases: [score function, score, Stein score, Stein score function, Hyvärinen score, grad log p, gradient of the log density, gradient of the log-density, s(x)]
link-skip: [relevance score, retrieval score, reward score, BM25 score, similarity score, CLIP score, attention score]
link-only-in: [deep-learning/diffusion-models, deep-learning/generative-models]
standard: vault-note v2
---

# Score Function

Up: [[Generative Modeling]]

Artificial Intelligence, Generative Modeling. The composition notes use the word in [[The Order Of Multiplying And Noising#Words the two orders use]].

**The score of a density p is the gradient of its log, s(x) = ∇ₓ log p(x), an arrow at every point aimed where the density rises fastest.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the score writes the rest around it.

## Where to learn this

**Score function**, the Stein score ∇ₓ log p(x), taken with respect to the point and not the parameters. Also: score, Stein score, Hyvärinen score, gradient of the log density.

**Textbooks**

- The little book of generative AI foundations, section 6.1.1: [pages 114 to 115](../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=114). Defines s(x) = ∇ₓ log p(x) as a drift field, works the Gaussian's −(x − µ)/σ² and −Σ⁻¹(x − µ), and draws the field of a two-component mixture (Figure 6.1).
- Deep learning textbook, section 18.4: [pages 633 to 635](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=633). Names the score and the score-matching loss that compares model and data scores without ever estimating the normalising constant Z.
- Probabilistic machine learning: advanced topics, section 24.3: [pages 879 to 882](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=879). Separates the Stein score ∇ₓ log p from the Fisher score ∇_θ log p, shows an energy model's score is −∇ₓE_θ(x), and builds score matching on it.
- The little book of generative AI foundations, section 8.4: [pages 177 to 180](../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=177). Why the score ignores the partition function, since ∇ₓ log Z_θ = 0, and score matching as learning an energy's gradient.

**Videos**

- CME296 lecture 2, 4:44 to 14:26: [watch](https://www.youtube.com/watch?v=_WaR2fjZpEQ&t=284s). Defines the score ∇ₓ log p(x) and why it replaces ∇p(x): the normaliser drops out, the direction is unchanged, and it is numerically stable. Caption-read.
- CME296 lecture 2, 21:08 to 24:12: [watch](https://www.youtube.com/watch?v=_WaR2fjZpEQ&t=1268s). Computes the score of a 1D Gaussian, −(x − μ)/σ², and draws why it points toward the mean. Caption-read.
- CME296 lecture 2, 58:25 to 1:04:17: [watch](https://www.youtube.com/watch?v=_WaR2fjZpEQ&t=3505s). Derives that the score of q(x_t | x_0) in DDPM is −ε/√(1 − ᾱ_t), tying noise prediction to score prediction. Caption-read.
- Stanford CS236 lecture 13, 3:52 to 11:51: [watch](https://www.youtube.com/watch?v=8G-OsDs1RLI&t=232s). The score function defined as a vector field over data space. Chapter-timed, from the video lessons index.

**Papers**

- Chan 2024, Tutorial on diffusion models for imaging and vision: [pages 48 to 49](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=48). Defines the Stein score, separates it from the score in θ, works Gaussian and mixture examples, and reads the arrows on a contour plot as the drift.
- Chan 2024, the same tutorial: [page 51](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=51). Denoising score matching: s_θ(x + σz) is trained to equal −z/σ, so estimating the score is denoising (Theorem 3.3).

**Our plans and chapters**

- [The score function, defined and seen](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/07-the-score-function.md), deep-learning/diffusion-models/01-poe-derivation-foundations, plan 07. The definition s(x) = ∇ log p(x) and its field drawn.
- [Differentiate a quadratic form and read the Gaussian score](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/06-the-gaussian-score.md), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 6. The Gaussian's score derived, and how an anisotropic covariance bends it.
- [Predict a gradient or score field before it is plotted](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/05-predicting-a-score-field.md), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 5. A mixture's score as a weighted pull, and what the score cannot tell you.
- [Noise prediction is the score](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/11-noise-prediction-is-the-score.md), deep-learning/diffusion-models/01-poe-derivation-foundations, plan 11. The identity between the predicted noise and the score, derived twice in two notations.
- [Energy: p proportional to exp(−E)/Z, and why the score never sees Z](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/04-energy-and-the-missing-normaliser.md), deep-learning/diffusion-models/02-sampler-correctors-for-composition, plan 04. Why the normaliser vanishes from the score.

**Scenes**

- [SDXL cross-attention, PoE and LoRA notebook, PoE fails on cat and dog](https://claude.ai/artifact/RP59hpFThMPmbftvvWPpbi#nb-sec13). Adding a cat expert's score to a dog expert's lands at the origin, distance 2 from both modes, while the two-mode mixture's score keeps both.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/ch4-time-reversal.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/ch4-time-reversal.jpg" width="200" alt="Forward SDE paths fanning out from one start point beside reverse-time paths running back from the end point, each with its Fokker-Planck equation"></a> Sophia Tang, "Foundations of Schrödinger Bridges for Generative Modeling", chapter 4 figure: [the paper](https://arxiv.org/abs/2603.18992), [what it shows](/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/README.md#ch4-time-reversaljpg). The reverse-time SDE in the bottom-right box needs the forward drift f and one more term, σ² ∇ log p_{T−s}, so the score is the only thing a sampler must know to run the forward paths backwards.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-22. Each textbook and paper page range was read in the PDF with pdftotext; the Probabilistic machine learning: advanced topics pages were first found through its back-of-book index (PDF pages 1256 to 1273, PDF page = printed page + 33), whose "score function, 75, 77" entry is the Fisher score and was left out. The three CME296 rows were read in its caption-read lecture map under `~/.claude/cache/captions/`, and their descriptions paraphrase the map, never the machine-translated captions. The CS236 row is copied from the video lessons index, `Mathematics/references/videos/Video Lessons.md`, section "The score function", whose times are chapter boundaries. Each plan and chapter was read at its title and description. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map or the video lessons index.
