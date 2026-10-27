---
aliases: [learning rate, learning rate schedule, learning rate warmup, learning rate decay]
standard: vault-note v2
---

# Learning Rate

Up: [[Machine Learning]]

Artificial Intelligence, Machine Learning. It sets the step in [[Gradient Descent]], which minimises a [[Loss Function]].

**The learning rate is the number that multiplies the gradient in each update, so it sets how far the parameters move per step: too small and training crawls, too large and the loss overshoots and can blow up.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the learning rate writes the rest around it.

## Where to learn this

**Learning rate**, the step size of a gradient update. Also: learning rate schedule, learning rate warmup, learning rate decay.

**Textbooks**

- Probabilistic machine learning: an introduction, section 8.2.2: [pages 316 to 317](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=316). Works a concrete case: steepest descent on one convex function from (0, 0) for 20 steps, where η = 0.1 creeps along the valley and η = 0.6 oscillates across it and never converges (figure 8.11).
- Probabilistic machine learning: an introduction, section 8.4.3: [pages 329 to 331](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=329). Choosing the learning rate for SGD from a plot of training loss against learning rate for a small network on FashionMNIST, then schedules: piecewise constant, exponential and polynomial decay, warmup and cyclical rates.
- Mathematics for machine learning, section 7.1.1: [page 235](../../Mathematics/references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=235). The step size, also called the learning rate: too small is slow, too large overshoots, and a step that raises the function is undone and retried smaller.
- AI engineering, chapter 7, Learning rate: [pages 684 to 685](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=684). The learning rate as a finetuning hyperparameter: typical values from 1e-7 to 1e-3, the pre-training rate times 0.1 to 1 as a start, and reading the loss curve for a rate that is too big or too small.
- Understanding deep learning, section 6.1, Gradient descent: [page 92](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=92). Writes the update φ ← φ − α ∂L/∂φ with α as the learning rate, and line search as the alternative that tries several step sizes.
- Optimization: principles and algorithms, section 11.1, Preconditioned steepest descent: [page 264](../../Mathematics/references/textbooks/optimization/optimization-principles-and-algorithms.pdf#page=264). Runs x_{k+1} = x_k − α_k ∇f(x_k) by hand on a two-variable quadratic in Example 11.1, with the step α_k chosen at each iteration.

**Videos**

- CS229 lecture 2, 38:50 to 41:50: [watch](https://www.youtube.com/watch?v=cmNIMjPYdgM&t=2330s). Shows what the step size does: too small converges slowly, too large overshoots and bounces across the bowl. Caption-read.
- CS231n lecture 3, 59:06 to 1:03:37: [watch](https://www.youtube.com/watch?v=dyNGd06MWn4&t=3546s). Choosing the learning rate (too high diverges, too low crawls), schedules such as dividing by 10 at fixed points, cosine, linear and inverse square root, linear warmup, and scaling the rate with batch size. Caption-read.
- CS231n lecture 6, 1:07:03 to 1:10:41: [watch](https://www.youtube.com/watch?v=aVJy4O5TOk8&t=4023s). A training recipe that runs a coarse learning rate search over one epoch, after first overfitting one example. Caption-read.

**Our plans and chapters**

- [Run a training loop and see what the learning rate does](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/14-run-a-training-loop-and-see-what.md), deep-learning/transformers, chapter 14. Works the same loop at learning rates 0.1 and 1.1 from a loss of 9.0: after five updates the first reaches 0.9664 and the second has grown to 55.7256.
- [Run a training loop and see what the learning rate does](/home/molef/goal-setting/learning/deep-learning/transformers/plans/14-run-a-training-loop-and-see-what.md), the same journey, plan 14. The sitting that types that loop in Python and plots both runs.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/reading-a-training-run/artifacts/figures/batch-size/ai-with-yoki-070-batch-size.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/reading-a-training-run/artifacts/figures/batch-size/ai-with-yoki-070-batch-size.jpg" width="140" alt="Six neon panels on batch size: the definition, batch size 1 against the full dataset, common sizes 32, 64 and 256, 1,000 examples at three batch sizes, a table of effects, and the learning-rate interaction"></a> YOKESWARAN AS (AI with YOKI) on X, "AI Learning 070: Batch Size": [the post](https://x.com/Yokii_26/status/2098780974041735312), [what it shows](/home/molef/goal-setting/learning/deep-learning/reading-a-training-run/artifacts/figures/batch-size/README.md#ai-with-yoki-070-batch-sizejpg). Panel 6 says batch size and learning rate move together: larger batches can usually take larger learning rates, smaller ones need smaller rates. It gives no rule; the training-failure catalog's check uses linear scaling, expected rate = reference rate × batch / reference batch, flagged outside 0.5 to 2.0 times that ([the reading](/home/molef/goal-setting/learning/deep-learning/reading-a-training-run/sources/batch-size/SOURCES.md#ai-learning-070-batch-size)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, first found through the books' back-of-book indexes ("learning rate", "learning rate schedule", "step-size"). Understanding deep learning names α the learning rate on PDF page 92 and lists the schedule among training hyperparameters on PDF page 105, and the Deep learning textbook covers adaptive learning rates in section 8.5 (PDF page 322); none has a line, to keep the list to the most direct pages. The three lecture rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`. The chapter and the plan were read at their titles and opening sections. "Step size" is not an alias: of 25 sampled uses in the learning tree, about 22 mean a Langevin or MCMC sampler's step, which [[Step Size And The Accept Step]] covers. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map.
