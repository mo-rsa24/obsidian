---
aliases: [variational autoencoder, variational auto-encoder, VAE]
standard: vault-note v2
---

# Variational Autoencoders

Up: [[Generative Modeling]]

Artificial Intelligence, Generative Modeling. Its training objective is the [[Evidence Lower Bound]], and a learner's note on its two losses during training is [[Artificial Intelligence/Generative Modeling/Variational Autoencoders/Training Dynamics|Training Dynamics]].

**A variational autoencoder is an autoencoder whose encoder outputs a Gaussian over the latent code instead of a single code, trained on the evidence lower bound so that decoding a draw from the prior N(0, I) produces new data.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the VAE writes the rest around it.

- [[Artificial Intelligence/Generative Modeling/Variational Autoencoders/Training Dynamics|Training Dynamics]]: how the reconstruction loss and the KL term pull against each other while a VAE trains, and how to read the two curves.

## Where to learn this

**Variational autoencoder (VAE)**, a latent-variable generative model trained on the ELBO. Also: VAE, variational auto-encoder.

**Textbooks**

- Understanding deep learning, sections 17.5 to 17.7: [pages 349 to 352](../../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=349). The variational approximation to the posterior, then the VAE itself: the encoder predicts μ and Σ, a sample goes through the decoder, the loss is the negative ELBO (Figure 17.9), and the reparameterisation trick lets gradients pass the sampling step (Figure 17.11).
- Probabilistic machine learning: advanced topics, section 21.2: [pages 814 to 819](../../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=814). The VAE as a deep latent variable model with its modelling assumptions, and CelebA faces reconstructed by a plain autoencoder, a β-VAE and a VAE side by side (Figure 21.3).
- The little book of generative AI foundations, chapter 3: [pages 54 to 67](../../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=54). From the deterministic autoencoder to the VAE, the ELBO in three equivalent forms, and the reparameterisation trick that makes joint training of encoder and decoder possible.

**Videos**

- CME296 lecture 4, 22:52 to 31:07: [watch](https://www.youtube.com/watch?v=WUUq6TVAu8U&t=1372s). The encoder outputs a mean and variance, z is sampled from that Gaussian and pushed toward a N(0, I) prior, and the decoder variance is fixed. Caption-read.
- CME296 lecture 4, 31:07 to 46:46: [watch](https://www.youtube.com/watch?v=WUUq6TVAu8U&t=1867s). Derives the VAE ELBO on the board (marginalise over z, bring in the encoder, apply Jensen, split into reconstruction and KL to the prior), then its weight and posterior collapse. Caption-read.
- CS231n lecture 13, 51:12 to 54:39: [watch](https://www.youtube.com/watch?v=zbHXQRUNlH0&t=3072s). Why a plain autoencoder cannot generate, and the variational idea of a latent z with a known prior that can be sampled and decoded. Caption-read.
- CS231n lecture 13, 1:09:19 to 1:12:25: [watch](https://www.youtube.com/watch?v=zbHXQRUNlH0&t=4159s). VAE training: the KL term pulls the encoder's Gaussian toward zero mean and unit variance, z is drawn with the reparameterisation trick, and the decoder reconstructs x. Caption-read.

**Papers**

- Chan 2024, Tutorial on diffusion models for imaging and vision, section 1: [pages 2 to 17](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=2). The VAE's building blocks, its evidence lower bound (Definition 1.3), the reparameterisation trick and its optimisation, as the ground the tutorial's diffusion models are built on.

**Our plans and chapters**

- [A VAE on MNIST, from the ELBO](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/plans/05-a-vae-on-mnist-from-the-elbo.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, plan 05. Times how convolution cost grows with image size, derives the VAE's ELBO and the reparameterisation trick, then builds the network on MNIST.
- [The VAE encoder, decoder, and the latent](/home/molef/goal-setting/learning/deep-learning/diffusion-models/latent-diffusion-architecture-rebuilt/plans/03-vae-latent.md), deep-learning/diffusion-models/latent-diffusion-architecture-rebuilt, plan 03. A toy VAE from 8 × 8 × 3 down to a 2 × 2 × 4 latent and back, the latent every later step of that model works on.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook and paper page range was read in the PDF with pdftotext, after the back-of-book indexes and the shelf index's chapter tables pointed to them ("variational autoencoder" and "VAE"). The CME296 and CS231n rows were read in their caption-read lecture maps under `~/.claude/cache/captions/` and paraphrase the map, never the machine-translated captions. The video lessons index section "The VAE and its ELBO" cites the same CME296 stretch from 22:56 and 31:19, read separately from the captions; the map rows are used here. Luis Serrano's "Denoising and Variational Autoencoders" has a chapter "Training a variational auto encoder" at 27:11 to 30:05 and was left out to keep four videos. Each plan was read at its title and description.
