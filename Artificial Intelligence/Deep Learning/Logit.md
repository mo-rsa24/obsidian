---
aliases: [logit, logits, logit vector, logit function, log-odds, log odds]
standard: vault-note v2
---

# Logit

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. [[Softmax]] turns logits into probabilities, and [[Temperature]] divides them first.

**A logit is the raw score a model gives one class or token before the softmax: any real number, negative allowed, with no need to sum to one; in statistics the logit of a probability p is its log-odds, log(p / (1 − p)), the inverse of the sigmoid.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches logits writes the rest around it.

## Where to learn this

**Logit**, the score before the softmax, and in statistics the log-odds log(p / (1 − p)). Also: logits, logit vector, logit function, log-odds.

**Textbooks**

- AI engineering, chapter 2, Sampling fundamentals: [pages 190 to 192](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=190). A language model outputs one logit per vocabulary token (figure 2-15); logits can be negative and do not sum to one, so a softmax converts them, and logits [1, 2] become probabilities [0.27, 0.73].
- Probabilistic machine learning: an introduction, section 2.4.2: [page 76](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=76). Shows the sigmoid's input a equals the log odds log(p / (1 − p)), and names the inverse of the sigmoid the logit function.
- Probabilistic machine learning: an introduction, section 2.5.2: [page 79](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=79). Calls the inputs to the softmax logits, "a generalization of the log odds", and writes a = Wx + b as the C-dimensional vector of logits.
- Pattern recognition and machine learning, section 4.2: [page 215](../../Mathematics/references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=215). Derives the two-class posterior as a sigmoid of a = ln(σ / (1 − σ)), the logit function, which is the log of the ratio of the two class probabilities.
- Deep learning textbook, section 3.10: [page 86](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=86). Notes that σ⁻¹(x), the inverse of the sigmoid, is called the logit in statistics and that machine learning uses that name more rarely, beside the softplus identities.

**Videos**

- CS231n lecture 2, 57:30 to 1:00:36: [watch](https://www.youtube.com/watch?v=pdqofxJeBN8&t=3450s). Turns a cat image's raw scores 3.2, 5.1 and −1.7 into probabilities with a softmax, giving the cat class 0.13, and names the raw scores logits. Caption-read.
- CS229 lecture 14, 29:06 to 36:12: [watch](https://www.youtube.com/watch?v=pwQ0l4hFCVI&t=1746s). Divides the logits (2, 1, −1) by a tiny temperature to get (200, 100, −100) and a near one-hot softmax, then top-k sampling on the logits. Caption-read.
- CS229 lecture 4, 7:07 to 11:39: [watch](https://www.youtube.com/watch?v=8gVi4Rk21Eg&t=427s). Rewrites the Bernoulli in exponential-family form and finds its natural parameter is η = log(φ / (1 − φ)), the log odds, whose inverse is the sigmoid. Caption-read.

**Our plans and chapters**

- [Find the gradient of the cross-entropy loss through a softmax](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/10-find-the-gradient-of-the-cross-entropy.md), deep-learning/transformers, chapter 10. Defines a logit as a score before the softmax, takes three cosines as the logits z = [0.9939, 0.1104, 0.7071], and finds the loss's gradient on each logit, including the competing ones.
- [Find the gradient of the cross-entropy loss through a softmax](/home/molef/goal-setting/learning/deep-learning/transformers/plans/10-find-the-gradient-of-the-cross-entropy.md), deep-learning/transformers, plan 10. The plan for that chapter: the gradient on the logits drawn as bars, and a broken run that treats each probability as depending only on its own logit.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27. Each textbook page was read in the PDF with pdftotext, first found through the books' back-of-book indexes ("logit", "logits", "log odds", "logit function"). Probabilistic machine learning: advanced topics, section 15.3 (page 636, logits in logistic regression) and section 15.3.3 (page 637, logit adjustment for class imbalance) teach narrower uses and have no line. The three lecture rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`. The two figures `find-figures.py` returned matched only the hover text of temperature marks and show no logit, so the card has no Figures group. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map.
