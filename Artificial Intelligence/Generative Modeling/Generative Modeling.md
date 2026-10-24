# Generative Modeling

Artificial Intelligence, Generative Modeling. Models that learn a data distribution and draw new samples from it, one note per family of models.

- [[Diffusion Models]]: models that learn to undo a fixed noising process, in a folder: the forward process, and composition (combining trained models by multiplying what each believes), including the mosaic, blend or two animals one product gives, and the three things called annealing.
- [[Artificial Intelligence/Generative Modeling/Variational Autoencoders/Training Dynamics|Training Dynamics]]: the learner's note on a variational autoencoder's reconstruction and KL losses during training, in the `Variational Autoencoders` folder.
- [[Score Matching]]: Score matching trains a network s_θ(x) to match the score ∇ₓ log p(x) of data whose density is unknown, and denoising score matching makes that practical by regressing onto the known score of a noised copy of each data point.
- [[Energy-Based Model]]: An energy-based model defines a density through a scalar energy, p(x) = exp(−E(x))/Z, so low energy means high probability, and the normaliser Z is usually never computed.
- [[Product Of Experts]]: A product of experts multiplies several models' densities and renormalises, p(x) ∝ p₁(x) p₂(x) ⋯, so the product is high only where every expert gives x some probability.
- [[Variational Autoencoders]]: A variational autoencoder is an autoencoder whose encoder outputs a Gaussian over the latent code instead of a single code, trained on the evidence lower bound so that decoding a draw from the prior N(0, I) produces new data.
- [[Evidence Lower Bound]]: The evidence lower bound is a quantity that sits below log p(x) for every choice of approximate posterior q(z), so maximising it pushes the likelihood up when log p(x) itself cannot be computed.
- [[Score Function]]: The score of a density p is the gradient of its log, s(x) = ∇ₓ log p(x), an arrow at every point aimed where the density rises fastest.
