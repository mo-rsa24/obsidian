---
aliases: [stochastic differential equation, SDE]
standard: vault-note v2
---

# Stochastic Differential Equation

Up: [[Differential Equations]]

Mathematics, Calculus, Differential Equations. [[Ordinary Differential Equation]] is the case with no noise, and [[Langevin Dynamics]] is one SDE.

**A stochastic differential equation is an ordinary differential equation with a random noise term added, dx = f(x, t) dt + g(t) dW, so its solution is a random path.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches SDEs writes the rest around it.
> - The placement is unsure. The two best places are `Mathematics/Calculus/Differential Equations/` and `Mathematics/Statistics/`, beside the stochastic processes that [[Langevin Dynamics]] sits among.

## Where to learn this

**Stochastic differential equation (SDE)**, a differential equation driven by noise. Also: SDE.

**Textbooks**

- Stochastic differential equations, chapter 1: [pages 11 to 18](../../references/textbooks/calculus/stochastic-differential-equations.pdf#page=11). An SDE as dX/dt = f(X) + g(X)ξ with white noise ξ, and the reasons to add noise to a differential equation.
- Stochastic differential equations, section 6.1: [pages 130 to 131](../../references/textbooks/calculus/stochastic-differential-equations.pdf#page=130). An ordinary differential equation driven by noise, integrated over time so the noise integral becomes Brownian motion.
- Stochastic differential equations, section 6.5: [pages 142 to 143](../../references/textbooks/calculus/stochastic-differential-equations.pdf#page=142). Itô processes, dX = F dt + G dB, and what it means for a process to solve an SDE.
- Stochastic differential equations, section 8.4: [pages 189 to 195](../../references/textbooks/calculus/stochastic-differential-equations.pdf#page=189). Simulating sample paths with Euler-Maruyama, its error on geometric Brownian motion, and the Milstein and Heun schemes.
- Probabilistic machine learning: advanced topics, section 25.4: [pages 900 to 904](../../references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=900). DDPM in the limit of infinitely many steps as an SDE, its reverse-time SDE, and the probability flow ODE beside it.
- The little book of generative AI foundations, section 5.1.1, Basic language for continuous-time motion: [page 91](../../references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=91). Introduces an SDE as the ODE dX_t = f dt plus a noise term, dX_t = f dt + σ dW_t.
- The little book of generative AI foundations, section 5.1.4, The Ornstein–Uhlenbeck process: [pages 96 to 97](../../references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=96). Works the Ornstein–Uhlenbeck SDE, a pull toward the origin plus noise, and solves it explicitly to show why it is called mean-reverting.
- The little book of generative AI foundations, sections 6.4.3 and 6.4.4: [pages 131 to 132](../../references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=131). Writes the general forward SDE of a diffusion model with its Fokker–Planck equation, then states the reverse-time SDE and the score's place in it.

**Videos**

- Stanford CME296, lecture 2, 1:04:17 to 1:20:50: [watch](https://www.youtube.com/watch?v=_WaR2fjZpEQ&t=3857s). Defines the Wiener process and derives the DDPM forward SDE dx = −½β(t)x dt + √β(t) dw with a Taylor expansion, reading the drift and the noise term. Caption-read.
- Stanford CME296, lecture 2, 1:22:53 to 1:28:36: [watch](https://www.youtube.com/watch?v=_WaR2fjZpEQ&t=4973s). Trains a time-conditioned score network and states the reverse-time SDE, whose drift gains a −g(t)² × score term. Caption-read.
- Stanford CME296, lecture 2, 1:28:36 to 1:30:41: [watch](https://www.youtube.com/watch?v=_WaR2fjZpEQ&t=5316s). Samples by solving the reverse SDE numerically with Euler-Maruyama. Caption-read.
- Stanford CS229, lecture 11, 43:11 to 50:37: [watch](https://www.youtube.com/watch?v=dqUMCzWjZSI&t=2591s). The forward SDE dx = drift·dt + g dW and Anderson's reverse-time SDE, whose noise stays Gaussian. Caption-read.

**Papers**

- Chan 2024, Tutorial on diffusion models for imaging and vision, sections 4.2 and 4.3: [pages 56 to 62](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=56). What an SDE is, drift plus Wiener noise, with Examples 4.3 and 4.4, then DDPM as a variance-preserving SDE (Theorem 4.1) and SMLD as a variance-exploding one (Theorems 4.3 and 4.4).

**Our plans and chapters**

- [Score-Based Generative Modelling through SDEs](/home/molef/goal-setting/learning/deep-learning/diffusion-models/03-score-sde/MASTER_PLAN.md), deep-learning/diffusion-models/03-score-sde. A journey that derives Song and others' 2021 SDE equations by hand and implements them.
- [VP and VE: one forward process, two schedules](/home/molef/goal-setting/learning/deep-learning/diffusion-models/03-score-sde/plans/01-vp-and-ve-one-forward-process-two-schedules.md), the same journey, plan 01. The forward SDE written once with a drift toward zero and once as variance exploding.
- [2. The reverse-time SDE](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l4-continuous-time/02-the-reverse-time-sde.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L4, section 2. Derives which process runs the forward SDE backward.
- [5. Itô's lemma](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/05-itos-lemma.md), the same journey, volume L3, section 5. The chain rule for a function of an SDE's solution.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/ch4-time-reversal.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/ch4-time-reversal.jpg" width="200" alt="Forward SDE paths fanning out from one start point beside reverse-time paths running back from the end point, each with its Fokker-Planck equation"></a> Sophia Tang, "Foundations of Schrödinger Bridges for Generative Modeling", chapter 4 figure: [the paper](https://arxiv.org/abs/2603.18992), [what it shows](/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/README.md#ch4-time-reversaljpg). Forward SDE paths fan out from one start point on the left, reverse-time paths run back from the end point on the right, and each panel carries the Fokker-Planck equation of the density slice its paths pass through.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook and paper page range was read in the PDF with pdftotext, after finding it through the chapter tables in `Textbooks.md`, the back-of-book tables in `~/.claude/cache/book-indexes/` and the tutorial's section in `papers/Papers.md`. Each video row was read in its course's caption-read lecture map under `~/.claude/cache/captions/`; the video lessons index row "Diffusion written as a forward SDE" (lecture 2, 1:14:31 to 1:22:54) overlaps the first row and was left out. Each plan and chapter was read at its title and description. "Langevin SDE" stays with [[Langevin Dynamics]], whose longer alias wins. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
