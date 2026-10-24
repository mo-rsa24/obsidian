---
aliases: [ELBO, evidence lower bound, variational lower bound, variational bound, the ELBO, negative ELBO, VAE ELBO, diffusion ELBO]
standard: vault-note v2
---

# Evidence Lower Bound

Up: [[Generative Modeling]]

Artificial Intelligence, Generative Modeling. A learner's note on the VAE's two loss terms during training is in [[Training Dynamics]].

**The evidence lower bound is a quantity that sits below log p(x) for every choice of approximate posterior q(z), so maximising it pushes the likelihood up when log p(x) itself cannot be computed.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the ELBO writes the rest around it.
> - The placement is unsure. The two best places are `Artificial Intelligence/Generative Modeling/`, since both the VAE and diffusion train on it, and `Mathematics/Statistics/`, as part of variational inference.

## Where to learn this

**Evidence lower bound (ELBO)**. Also: ELBO, variational lower bound, negative ELBO.

**Textbooks**

- Understanding deep learning, sections 17.3 and 17.4: [pages 344 to 348](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=344). Derives the VAE's ELBO with Jensen's inequality, then shows when the bound is tight and splits it into reconstruction loss minus the KL distance to the prior.
- The little book of generative AI foundations, section 2.4: [pages 45 to 47](../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=45). Rewrites p(x) as an expectation over Q(z), applies log E ≥ E log, and shows the bound is exact when Q(z) = p(z | x).
- The little book of generative AI foundations, sections 4.2.3 to 4.3.3: [pages 75 to 81](../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=75). The diffusion ELBO, with the forward process playing Q(z), expanded into prior-matching, step-wise KL and reconstruction terms.
- Probabilistic machine learning: advanced topics, section 10.1: [pages 466 to 468](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=466). The ELBO as the objective of variational inference, read two ways: expected log joint plus entropy, and expected log-likelihood minus KL to the prior.
- Pattern recognition and machine learning, section 10.1: [page 479](../../Mathematics/references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=479). The decomposition ln p(X) = L(q) + KL(q ‖ p) (equation 10.2), with L(q) the lower bound that variational inference maximises.

**Videos**

- CS231n lecture 13, 1:02:50 to 1:09:19: [watch](https://www.youtube.com/watch?v=zbHXQRUNlH0&t=3770s). Derives the ELBO from Bayes' rule: a reconstruction term, a KL term to the prior, and a KL term to the true posterior that is at least 0 and is dropped. Caption-read.
- CS229 lecture 10, 20:33 to 24:09: [watch](https://www.youtube.com/watch?v=sUS-eTa0l6s&t=1233s). Shows Jensen's bound becomes an equality when Q(z) = p(z | x; θ) and names the result the ELBO, the same bound diffusion models use. Caption-read.
- CME296 lecture 4, 31:07 to 46:46: [watch](https://www.youtube.com/watch?v=WUUq6TVAu8U&t=1867s). Derives the VAE ELBO on the board, then discusses the weight on the KL term and posterior collapse. Caption-read.
- CME296 lecture 1, 56:48 to 1:05:11: [watch](https://www.youtube.com/watch?v=tr-CUpw--ck&t=3408s). Derives the diffusion ELBO: multiply and divide by q(x_{1:T} | x_0), write it as an expectation over forward trajectories, apply Jensen. Caption-read.

**Papers**

- Chan 2024, Tutorial on diffusion models for imaging and vision: [pages 5 to 7](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=5). Definition 1.3 gives the VAE's ELBO and the next pages show it lower-bounds log p(x).
- Chan 2024, the same tutorial: [pages 25 to 28](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=25). The diffusion ELBO's three terms (Theorem 2.3), then rewritten with x_0 in the conditioning as one KL per step (Theorem 2.4).

**Our plans and chapters**

- [The ELBO, telescoped into one KL per step](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/13-the-training-loss-two-ways.md#133-the-elbo-telescoped-into-one-kl-per-step), deep-learning/diffusion-models/01-poe-derivation-foundations, section 13.3. The diffusion ELBO worked down to a KL per step.
- [The ELBO to the epsilon loss](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/21-the-elbo-to-the-epsilon-loss.md), deep-learning/diffusion-models/01-poe-derivation-foundations, plan 21. From the bound to the noise-prediction loss diffusion models train on.
- [A VAE on MNIST, from the ELBO](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/plans/05-a-vae-on-mnist-from-the-elbo.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, plan 05. Derives the VAE's ELBO and trains a VAE on MNIST from it.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-22. Each textbook and paper page range was read in the PDF with pdftotext; the Probabilistic machine learning: advanced topics pages were first found through its back-of-book index (PDF pages 1256 to 1273, PDF page = printed page + 33). Each video row was read in its course's caption-read lecture map under `~/.claude/cache/captions/`, and its description paraphrases the map, never the machine-translated captions. Each plan and chapter was read at its title and description. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start.
