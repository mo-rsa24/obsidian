---
aliases: [mean squared error, MSE, squared error loss, squared error, least squares loss, quadratic loss, L2 loss]
standard: vault-note v2
---

# Mean Squared Error

Up: [[Machine Learning]]

Artificial Intelligence, Machine Learning. It is one [[Loss Function]], [[Mean Absolute Error]] is its absolute-value sibling, and [[Cross-Entropy]] is the loss used for classes instead.

**Mean squared error is the average of the squared differences between a model's predictions and the true values, so a miss of 2 costs four times a miss of 1.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches mean squared error writes the rest around it.

## Where to learn this

**Mean squared error (MSE)**, the average squared prediction error. Also: MSE, squared error loss, least squares loss, quadratic loss.

**Textbooks**

- Understanding deep learning, section 2.2.2: [pages 33 to 35](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=33). Works the least squares loss with numbers: twelve data points and three candidate lines scoring L = 7.07, 10.28 and 0.20, then the loss drawn as a surface over intercept and slope.
- Deep learning textbook, section 5.1.4: [pages 124 to 125](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=124). Defines MSE on a test set, then minimises it on the training set for linear regression by setting its gradient to zero, drawn on ten points.
- Understanding deep learning, section 5.3.1: [page 76](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=76). Derives the least squares loss as the negative log-likelihood of a normal distribution whose mean the network predicts.
- Probabilistic machine learning: an introduction, section 1.2.2: [page 36](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=36). Names (y − ŷ)² the quadratic or ℓ2 loss, calls its average over the training set the MSE, and ties it to a Gaussian output.
- Deep learning textbook, section 5.4.4: [pages 145 to 146](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=145). The MSE of an estimator split into squared bias plus variance, and the U-shaped generalisation curve that split explains.

**Videos**

- CS229 lecture 2, 23:44 to 29:14: [watch](https://www.youtube.com/watch?v=cmNIMjPYdgM&t=1424s). Writes the least squares cost J(θ) = ½ Σ (h_θ(x) − y)² and says why the error is squared and why the ½ leaves the minimiser alone. Caption-read.
- StatQuest, The Main Ideas of Fitting a Line to Data, Least Squares, 6:08 to 9:21: [watch](https://www.youtube.com/watch?v=PaFPbb66DxQ&t=368s). The least squares step of the line-fitting walk, which keeps the line with the smallest sum of squared residuals. Chapter-timed.
- CS229 lecture 3, 27:13 to 30:13: [watch](https://www.youtube.com/watch?v=uJF_gL3jhxI&t=1633s). Takes the log of a Gaussian likelihood and shows that maximising it is minimising the least squares cost. Caption-read.
- CME296 lecture 7, 45:15 to 49:28: [watch](https://www.youtube.com/watch?v=iNaRBp4T57Q&t=2715s). MSE as a reconstruction metric between an image and its reconstruction, and why it breaks under a shift of a few pixels and has no fixed scale. Caption-read.

**Our plans and chapters**

- [Expectation, and the best constant guess](/home/molef/goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/01-expectation-and-the-best-constant-guess.md), mathematics/statistics/conditional-expectation, chapter 01. Works the squared error of a constant guess on a fair die: 3.5 pips has the smallest average squared miss, 2.9167.
- [The conditional mean is the best guess](/home/molef/goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/05-the-conditional-mean-is-the-best-guess.md), the same journey, chapter 05. Proves that any guess's squared error splits into a shared floor plus a penalty for leaving the conditional mean, the proof behind the ideal denoiser.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext; the Deep learning textbook and Probabilistic machine learning pages were first found through their back-of-book indexes, and the Understanding deep learning pages through its index entry "least squares loss". Introduction to probability for data science treats mean squared error as an estimation criterion (section 8.4 from PDF page 536) and has no line, to keep the list to machine learning's use. The three lecture rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`, and their descriptions paraphrase the map. The StatQuest chapter list was read with `cache-video-chapters.py` and the line is described from its chapter and video titles only. Each chapter was read at its title and opening section. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map or a cached chapter list.
