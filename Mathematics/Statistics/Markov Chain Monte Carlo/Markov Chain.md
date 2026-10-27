---
aliases: [Markov chain, Markov process, Markov property, Markov assumption, transition matrix, transition kernel, Markov kernel]
standard: vault-note v2
---

# Markov Chain

Up: [[Markov Chain Monte Carlo]]

Mathematics, Statistics, Markov Chain Monte Carlo. [[Stationary Distribution]] is where a chain settles, and [[Markov Chain Monte Carlo]] builds a chain whose stationary distribution is the one it wants to sample.

**A Markov chain is a sequence of random states in which the next state depends only on the current one, through fixed transition probabilities, and not on the path that led there.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches Markov chains writes the rest around it.
> - The [[Markov Chain Monte Carlo]] note does not list this note yet.

## Where to learn this

**Markov chain**, a random sequence that remembers only its current state. Also: Markov process, Markov property, transition matrix, transition kernel.

**Textbooks**

- Linear algebra textbook, section 10.4: [pages 565 to 571](../../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=565). Works transition matrices of small chains with numbers (Examples 1 and 2), state vectors stepped forward by multiplying by the matrix, and their limiting behaviour.
- Probabilistic machine learning: advanced topics, sections 2.6.1 to 2.6.2: [pages 79 to 82](../../references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=79). The Markov assumption, transition kernels and transition matrices, higher-order chains, and an application.
- Probabilistic machine learning: an introduction, section 3.5: [page 121](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=121). A first-order Markov model, its state transition matrix, and M'th-order models.
- Pattern recognition and machine learning, section 11.2.1: [pages 555 to 556](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=555). First-order Markov chains, homogeneous chains and transition probabilities, as the ground for MCMC.

**Videos**

- ritvikmath, Markov Chains, Transition Matrix, 3:06 to 4:09: [watch](https://www.youtube.com/watch?v=prZMpThbU3E&t=186s). Writes the example chain's transition probabilities as a matrix. Chapter-timed.
- ritvikmath, Markov Chains, 0:37 to 2:50: [watch](https://www.youtube.com/watch?v=prZMpThbU3E&t=37s). A Markov chain by example: its state space, and the assumption that the next state depends only on the current one. Chapter-timed, from the video lessons index.
- ritvikmath, Markov Chain Stationary Distribution, Markov Chain, 0:37 to 3:06: [watch](https://www.youtube.com/watch?v=4sXiCxZDrTU&t=37s). Sets up the chain whose long-run behaviour the rest of the video finds. Chapter-timed.
- CS229 lecture 11, 3:35 to 6:13: [watch](https://www.youtube.com/watch?v=dqUMCzWjZSI&t=215s). Diffusion generation as a learned Markov chain from white noise down to x₀, removing a little noise each step. Caption-read.

**Our plans and chapters**

- [1. A Markov chain, and what forgetting means](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/01-a-markov-chain-and-what-forgetting-means.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L3, section 1. Runs a two-state chain from two different starts and watches it forget where it began.
- [A Markov chain, and what forgetting means](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/10-a-markov-chain-and-forgetting.md), deep-learning/diffusion-models/02-sampler-correctors-for-composition, plan 10. The Markov property written down, then a chain run and watched forgetting its start.
- [The Markov property behind the branch probe](/home/molef/goal-setting/learning/deep-learning/diffusion-models/07-speciation-before-divergence/plans/02-markov-property-of-the-branch-probe.md), deep-learning/diffusion-models/07-speciation-before-divergence, plan 02. Why cloning a trajectory with fresh noise is a fair probe: the endpoint given x_t forgets the path.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/ch7-ctmc.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/ch7-ctmc.jpg" width="200" alt="Three grids of states at times t_(k-1), t_k and t_(k+1), the current state jumping to another along an arrow labelled with its rate Q_t, and the master equation beneath"></a> Sophia Tang, "Foundations of Schrödinger Bridges for Generative Modeling", chapter 7 figure: [the paper](https://arxiv.org/abs/2603.18992), [what it shows](/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/README.md#ch7-ctmcjpg). Three grids of states at successive times show the current state jumping to another at rate Q_t(x, y), and the master equation beneath moves the distribution by the mass flowing into x minus the mass flowing out. It is the continuous-time chain, with jump rates where a discrete chain has step probabilities.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook range was read with pdftotext, after finding it through the books' back-of-book indexes and the shelf index's chapter tables. The ritvikmath "Markov Chains" and "Markov Chain Stationary Distribution" chapter lists were read with cache-video-chapters.py and those lines are described from their chapter titles only; the 0:37 row is copied from the video lessons index, section "The Markov chain". The CS229 row was read in its caption-read lecture map. Each plan and chapter was read at its title and opening lines. "Transition matrix" is an alias: all 10 sampled learning-tree lines meant a Markov chain's matrix. The linear algebra textbook also uses the phrase for a change of basis, which the learning tree does not.
