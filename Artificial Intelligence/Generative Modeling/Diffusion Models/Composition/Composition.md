---
aliases: [composition, compositional generation, composing models]
---

# Composition

Up: [[Diffusion Models]] · ⬅️ [[The Forward Process]]

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[The Forward Process]] for noise levels, and [[Multivariate Normal Distribution#Products and quotients of diagonal Gaussians]] for the arithmetic.

**Composing diffusion models means sampling from the product of what each trained model believes, with the background they share divided out once.** These notes run from the rule itself, to the samplers that reach the product, to what each expert learns from its training set, all on small Gaussian clouds you can check by hand.

## The rule

- [[Composing Models With A Background]]: the composition rule of Definition 5.1, multiplying experts and dividing out the background they share, on two-pixel and two-dimensional clouds.
- [[The Product As An Intersection]]: why the product is tall only where every expert is somewhat tall, and why its peak is a compromise none of them would pick.
- [[Kinds Of Composition]]: co-occurrence, intersection and interaction, told apart by which variables each expert scores.

## Sampling the product

- [[The Order Of Multiplying And Noising]]: why adding two models' scores and running the reverse process misses the product at every noise level, and what reaches it.
- [[The Energy Parameterisation]]: a model that outputs one height per input, so a sampler can accept or reject each move and models can be mixed.
- [[Product, Mixture And Negation]]: the product (AND), mixture (OR) and negation (NOT), and why a score-only model can do the first and last but not the mixture.

## What the experts learn

- [[What An Expert Learns From Its Training Set]]: an expert learns the density of what it is shown; labels matter only where a conditioning rule or a classifier reads them.
- [[When Neither Training Set Holds A And B]]: a product reaches a combination neither training set holds only where each expert has density there.

## The samplers it borrows

- [[Annealed MCMC]] and [[Step Size And The Accept Step]], in [[Markov Chain Monte Carlo]] under Mathematics.
