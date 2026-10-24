---
aliases: [ordinary differential equation, ODE, probability flow ODE, probability-flow ODE]
standard: vault-note v2
---

# Ordinary Differential Equation

Up: [[Differential Equations]]

Mathematics, Calculus, Differential Equations. [[Stochastic Differential Equation]] adds a noise term to one.

**An ordinary differential equation states how a quantity changes with one variable, such as dx/dt = f(x, t), and solving it means finding the path x(t) that obeys it from a starting value.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches ODEs writes the rest around it.

## Where to learn this

**Ordinary differential equation (ODE)**, an equation for a rate of change in one variable. Also: ODE.

**Textbooks**

- Calculus textbook, section 8.3: [pages 603 to 609](../../references/textbooks/calculus/calculus-textbook.pdf#page=603). Slope fields, then Euler's method worked as a table for y′ = y − x from y(0) = 2 with step 0.1 (Example 1, page 606), and its accuracy.
- Calculus textbook, section 8.1: [pages 585 to 591](../../references/textbooks/calculus/calculus-textbook.pdf#page=585). What a differential equation is, its order and solutions, initial-value problems, and models of population growth, cooling and springs.
- Calculus handbook, chapter 10: [pages 120 to 121](../../references/textbooks/calculus/calculus-handbook.pdf#page=120). Defines an ODE against a PDE, the order, linear ODEs and separable first-order ODEs.
- Calculus textbook, section 8.4, First-order differential equations and applications: [page 611](../../references/textbooks/calculus/calculus-textbook.pdf#page=611). Solves a first-order linear ODE with an integrating factor, the method a variance ODE needs.

**Videos**

- Professor Leonard, Introduction to Euler's Method (Differential Equations 41), Worked example and error, 32:45 to 56:31: [watch](https://www.youtube.com/watch?v=LV619RQ5rp4&t=1965s). Euler's method run on a worked example, and its error. Chapter-timed.
- Professor Leonard, Introduction to Differential Equations (Differential Equations 2), Ordinary Differential Equations versus Partial Order Differential Equations, 8:14 to 9:56: [watch](https://www.youtube.com/watch?v=EWVSxND_iWA&t=494s). What makes a differential equation ordinary rather than partial. Chapter-timed.
- Stanford CME296, lecture 3, 18:38 to 23:46: [watch](https://www.youtube.com/watch?v=agN3AlfGFrk&t=1118s). Writes the ODE dx/dt = u_t(x) and shows a Lipschitz u_t gives unique paths, with u = √x from x_0 = 0 as the counterexample where two paths solve it. Caption-read.
- Stanford CME296, lecture 2, 1:30:32 to 1:41:24: [watch](https://www.youtube.com/watch?v=_WaR2fjZpEQ&t=5432s). The probability flow ODE: with no random term it carries only discretisation error, unlike the reverse SDE, and its derivation is sketched. Caption-read, from the video lessons index.

**Papers**

- Chan 2024, Tutorial on diffusion models for imaging and vision, section 4.1: [pages 54 to 55](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=54). A recursion becomes an ODE as the step shrinks, and gradient descent becomes gradient flow (Examples 4.1 and 4.2).
- Chan 2024, the same tutorial, section 4.4: [page 63](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=63). Euler's method for an ODE as a tangent-line step, with a worked example (Example 4.8).

**Our plans and chapters**

- [The flow map of an ODE, refreshed](/home/molef/goal-setting/learning/deep-learning/diffusion-models/07-speciation-before-divergence/plans/01-flow-map-of-an-ode.md), deep-learning/diffusion-models/07-speciation-before-divergence, plan 01. Why a smooth ODE sends each starting state to exactly one endpoint.
- [The scheduler as an ODE solver](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/plans/12-the-scheduler-as-an-ode-solver.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, plan 12. A diffusion scheduler read as a numerical solver stepping an ODE.
- [3. The probability flow ODE](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l4-continuous-time/03-the-probability-flow-ode.md), the same journey, volume L4, section 3. The deterministic ODE with no noise term that carries the same densities as the reverse-time SDE.
- [DDIM as a discretised probability flow ODE](/home/molef/goal-setting/learning/deep-learning/diffusion-models/03-score-sde/plans/03-ddim-as-a-discretised-ode.md), deep-learning/diffusion-models/03-score-sde, plan 03. DDIM's update derived as a step of that ODE, reaching a sample in 10 or 50 steps.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook and paper page range was read in the PDF with pdftotext, after finding it through the chapter tables in `Textbooks.md`, the back-of-book tables in `~/.claude/cache/book-indexes/` and the tutorial's section in `papers/Papers.md`. The two Leonard chapter lists were read with cache-video-chapters.py, and those lines describe only the chapter and video titles. The CME296 lecture 3 row was read in its caption-read lecture map under `~/.claude/cache/captions/`, and the lecture 2 line is copied from the video lessons index, section "The probability flow ODE". 3Blue1Brown's "Differential equations, a tourist's guide" (DE1) was cached and left out only to keep four videos. The probability flow ODE is a separate idea and is not an alias here, so a later card for it takes "probability flow ODE" by its longer name; until then its lines sit on this card. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
