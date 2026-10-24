---
aliases: [loss function, loss, cost function, objective function, error function, training objective]
link-skip-in: [finance/]
link-skip: [job loss, your loss is capped, behavioral loss, profit and loss]
standard: vault-note v2
---

# Loss Function

Up: [[Machine Learning]]

Artificial Intelligence, Machine Learning. Three losses have their own notes: [[Mean Squared Error]], [[Mean Absolute Error]] and [[Cross-Entropy]]. [[Gradient Descent]] is how a loss gets minimised.

**A loss function turns a model's predictions on the training data into one number that says how badly the model fits, and training means changing the parameters to make that number small.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches loss functions writes the rest around it.

## Where to learn this

**Loss function**, the number training minimises. Also: loss, cost function, objective function, training objective.

**Textbooks**

- Understanding deep learning, section 2.2.2: [pages 33 to 35](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=33). Works the idea with numbers: each choice of intercept and slope for a line through twelve points gets one loss (7.07, 10.28 and 0.20), lower meaning a better fit, and the loss over all parameters is drawn as a surface whose lowest point is the best line.
- Pattern recognition and machine learning, section 1.5.2: [page 60](../../Mathematics/references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=60). A loss matrix for cancer diagnosis that charges 1000 for missing a cancer and 1 for a false alarm, and the decision rule that minimises the expected loss.
- Understanding deep learning, sections 5.1 to 5.2: [pages 70 to 74](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=70). A recipe that builds a loss for any kind of output from maximum likelihood: choose a distribution over the output, have the network predict its parameters, and minimise the negative log-likelihood.
- Probabilistic machine learning: an introduction, section 1.2.1: [page 34](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=34). An asymmetric loss for iris flowers where one species is poisonous, the empirical risk as the average loss over the training set, and the zero-one loss that turns it into the misclassification rate.
- Mathematics for machine learning, section 8.2.2: [page 266](../../Mathematics/references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=266). Defines the loss ℓ(yₙ, ŷₙ) as a non-negative number for one prediction and training as minimising its average over independent and identically distributed examples.

**Videos**

- CS231n lecture 2, 53:50 to 57:30: [watch](https://www.youtube.com/watch?v=pdqofxJeBN8&t=3230s). Defines the loss as the average of per-example losses that optimisation will minimise, after showing data a line cannot separate. Caption-read.
- CS229 lecture 2, 14:39 to 17:41: [watch](https://www.youtube.com/watch?v=cmNIMjPYdgM&t=879s). Chooses the line that minimises prediction errors on the training data, empirical risk minimisation, and contrasts it with a nearest-neighbour average. Caption-read.
- CS229 lecture 7, 7:38 to 15:43: [watch](https://www.youtube.com/watch?v=fRM41w9jzQo&t=458s). The loss for a nonlinear model: squared error for regression, and the negative log-likelihood of the softmax for k classes. Caption-read.
- 3Blue1Brown, Gradient descent, how neural networks learn, Cost functions, 3:01 to 6:55: [watch](https://www.youtube.com/watch?v=IHZwWFHWa-w&t=181s). The cost function of a digit-recognising network, the segment that sets up what gradient descent will minimise. Chapter-timed.

**Our plans and chapters**

- [Classical ML from Scratch](/home/molef/goal-setting/learning/machine-learning/classical-ml-from-scratch/MASTER_PLAN.md), machine-learning/classical-ml-from-scratch. Goal 1 derives linear and logistic regression from a loss function and gradient descent, with no library `.fit()`.
- [Choose the training objective yourself: hide a word or predict neighbours](/home/molef/goal-setting/learning/deep-learning/transformers/plans/35-choose-the-training-objective-yourself-hide.md), deep-learning/transformers, plan 35. You decide what a small network is asked to predict so that words from one topic end up close, before seeing the journey's answer.
- [Derive the training loss two ways: score matching and the ELBO](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/13-the-training-loss-two-ways.md), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 13. A diffusion model's training loss reached by two routes that meet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, first found through the books' back-of-book indexes ("loss function", "cost function", "objective function"). Understanding deep learning's notes to chapter 2 (PDF page 37) separate the words: a loss is one data point's term, the cost is the total minimised, and an objective is anything maximised or minimised; the Deep learning textbook names all of them as one on PDF page 98. Neither has its own line. The three lecture rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`. The 3Blue1Brown chapter list was read with `cache-video-chapters.py` and the line is described from its chapter and video titles only; ritvikmath's "Loss Functions : Data Science Basics" was also read and left out, since its chapter titles ("Introduction", "Classification", "Zero Loss") do not say which losses it teaches. Each plan and chapter was read at its title and opening lines. Bare "loss" is an alias because 958 of the learning tree's uses sit under deep-learning against 21 under finance, and the link-skip phrases cover the money sense. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map or a cached chapter list.
