---
aliases: [gradient descent, stochastic gradient descent, SGD, mini-batch gradient descent, minibatch gradient descent, batch gradient descent, steepest descent]
standard: vault-note v2
---

# Gradient Descent

Up: [[Machine Learning]]

Artificial Intelligence, Machine Learning. It minimises a [[Loss Function]], its step size is the [[Learning Rate]], one pass over the data is an [[Epoch]], and [[Backpropagation]] computes the gradient it needs.

**Gradient descent fits a model by repeatedly computing the gradient of the loss with respect to the parameters and moving the parameters a small step in the opposite, downhill direction; stochastic gradient descent estimates that gradient on a random batch of examples instead of the whole training set.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches gradient descent writes the rest around it.

## Where to learn this

**Gradient descent**, and its stochastic form (SGD). Also: stochastic gradient descent, SGD, mini-batch gradient descent, steepest descent.

**Textbooks**

- Understanding deep learning, section 6.1: [pages 91 to 93](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=91). Works gradient descent on the linear regression loss of twelve points: compute the derivatives, step downhill by α times them, and after four iterations the line is already close to the best fit (figure 6.1).
- Understanding deep learning, section 6.2: [pages 97 to 100](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=97). Stochastic gradient descent: the gradient of a random minibatch, the update rule with learning rate α, batches drawn without replacement until an epoch ends, and how the noise lets it leave a wrong valley.
- Mathematics for machine learning, section 7.1: [pages 233 to 237](../../Mathematics/references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=233). Gradient descent on the polynomial x⁴ + 7x³ + 5x² − 17x + 3 from x₀ = −10, the update x₁ = x₀ − γ∇f(x₀), then choosing the step size, momentum, and stochastic gradient descent (section 7.1.3).
- Deep learning textbook, section 5.9: [pages 167 to 168](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=167). The insight behind SGD: the gradient of an average loss is an expectation, so a uniformly drawn minibatch gives an estimate of it.
- Probabilistic machine learning: an introduction, section 8.4: [pages 327 to 328](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=327). SGD for finite-sum losses: minibatches of B examples as an unbiased gradient estimate, and convergence when the step size decays at the right rate.

**Videos**

- StatQuest, Gradient Descent, Step-by-Step, Gradient Descent optimization of a single variable, part 1, 5:38 to 9:08: [watch](https://www.youtube.com/watch?v=sDv4f4s2SB8&t=338s). The first single-variable optimisation in StatQuest's step-by-step walk of gradient descent. Chapter-timed.
- CS229 lecture 2, 33:14 to 37:19: [watch](https://www.youtube.com/watch?v=cmNIMjPYdgM&t=1994s). Builds gradient descent from the first-order Taylor approximation: step against the gradient with a step size α, and the risk of local minima without convexity. Caption-read.
- CS229 lecture 2, 43:51 to 49:22: [watch](https://www.youtube.com/watch?v=cmNIMjPYdgM&t=2631s). Mini-batch stochastic gradient descent: a small random batch per step, why batches must be random (all cats then all dogs fails), and why shuffling once beats sampling with replacement. Caption-read.
- CS231n lecture 3, 33:56 to 36:29: [watch](https://www.youtube.com/watch?v=dyNGd06MWn4&t=2036s). Writes the vanilla gradient descent loop (weights minus step size times gradient), traces its path on a loss contour plot, and gives stopping rules. Caption-read.

**Our plans and chapters**

- [Run a training loop and see what the learning rate does](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/14-run-a-training-loop-and-see-what.md), deep-learning/transformers, chapter 14. Works the updates by hand on a parameter moved from 0 toward a target of 3: the loss falls from 9.0 to 5.76 to 3.6864 at learning rate 0.1, then the same loop in Python.
- [Take one gradient step on W_Q and watch the query move toward the right key](/home/molef/goal-setting/learning/deep-learning/transformers/plans/24-take-one-gradient-step-on-w-q.md), the same journey, plan 24. One gradient step on an attention projection, checked by where the query moves.
- [Choose the optimiser yourself: plain gradient descent or Adam](/home/molef/goal-setting/learning/deep-learning/transformers/plans/15-choose-the-optimiser-yourself-plain-gradient-descent.md), the same journey, plan 15. You choose between plain gradient descent and Adam before the journey's own answer opens.
- [Classical ML from Scratch](/home/molef/goal-setting/learning/machine-learning/classical-ml-from-scratch/MASTER_PLAN.md), machine-learning/classical-ml-from-scratch. Goal 1 fits linear and logistic regression with a hand-written gradient descent.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/reading-a-training-run/artifacts/figures/batch-size/ai-with-yoki-070-batch-size.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/reading-a-training-run/artifacts/figures/batch-size/ai-with-yoki-070-batch-size.jpg" width="140" alt="Six neon panels on batch size: the definition, batch size 1 against the full dataset, common sizes 32, 64 and 256, 1,000 examples at three batch sizes, a table of effects, and the learning-rate interaction"></a> YOKESWARAN AS (AI with YOKI) on X, "AI Learning 070: Batch Size": [the post](https://x.com/Yokii_26/status/2098780974041735312), [what it shows](/home/molef/goal-setting/learning/deep-learning/reading-a-training-run/artifacts/figures/batch-size/README.md#ai-with-yoki-070-batch-sizejpg). Panel 2 sets batch size 1 (stochastic gradient descent: frequent, fast, noisy updates) against the full dataset (full-batch gradient descent: one stable, accurate, expensive update per epoch). Its claim that batch size 1 "can escape bad local minima" is stated with no evidence, the poster's strongest unbacked line ([the reading](/home/molef/goal-setting/learning/deep-learning/reading-a-training-run/sources/batch-size/SOURCES.md#ai-learning-070-batch-size)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, first found through the books' back-of-book indexes and the shelf index's chapter tables. Pattern recognition and machine learning covers sequential gradient descent briefly (PDF pages 163 and 258) and has no line. The three lecture rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`. The StatQuest chapter list was read with `cache-video-chapters.py` and the line is described from its chapter and video titles only; the chapter lists of StatQuest's "Stochastic Gradient Descent, Clearly Explained!!!" (its SGD chapter runs 4:47 to 10:53) and 3Blue1Brown's "Gradient descent, how neural networks learn" (6:55 to 11:18) were read too and left out to keep four lines. Each plan and chapter was read at its title and opening lines. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map or a cached chapter list.
