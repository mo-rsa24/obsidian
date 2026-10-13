# Generative Modeling

Artificial Intelligence, Generative Modeling. Models that learn a data distribution and draw new samples from it, one note per family of models.

- [[Diffusion Models]]: noising data in one jump to any level, composing two models by multiplying them and dividing out their shared background, and why adding two models' scores misses the noised product under the reverse process at any number of levels while annealed MCMC reaches it, and a model that outputs one energy per input, whose height lets a sampler accept or reject each move, holding the right width at any step size where unadjusted Langevin runs away past 2 / P, and lets two models be mixed; and the three ways to combine models, product (AND), mixture (OR) and negation (NOT), of which a score-only model can do the first and last but not the mixture.
- [[Artificial Intelligence/Generative Modeling/Variational Autoencoders/Training Dynamics|Training Dynamics]]: the learner's note on a variational autoencoder's reconstruction and KL losses during training, in the `Variational Autoencoders` folder.
