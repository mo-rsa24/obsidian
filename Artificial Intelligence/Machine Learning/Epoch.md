---
aliases: [epoch, training epoch, number of epochs]
link-skip: [epoch time, Unix epoch, custom epoch]
standard: vault-note v2
---

# Epoch

Up: [[Machine Learning]]

Artificial Intelligence, Machine Learning. Epochs count passes of [[Gradient Descent]] over the training set.

**An epoch is one complete pass through the training data; with minibatches, one epoch is as many updates as there are batches in the dataset.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches epochs writes the rest around it.

## Where to learn this

**Epoch**, one full pass over the training set. Also: training epoch, number of epochs.

**Textbooks**

- AI engineering, chapter 7, Number of epochs: [pages 686 to 687](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=686). Puts numbers on the choice: 1 to 2 epochs may be enough for millions of examples, 4 to 10 can still help for thousands, and a training loss that keeps falling while the validation loss rises says to use fewer.
- Understanding deep learning, section 6.2.1: [page 99](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=99). Batches are drawn without replacement until the data is used up, and a single pass through the entire training set is an epoch.
- Deep learning textbook, section 7.8: [page 262](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=262). Learning curves over 250 epochs of a network on MNIST, where training loss keeps falling and validation loss turns back up, the picture behind early stopping.
- Hands-on large language models, chapter 10: [page 412](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=412). The `num_train_epochs` training argument in code, kept at 1 for speed with the advice to raise it.

**Videos**

- TileStats, Stochastic gradient descent (SGD) vs mini-batch GD, iterations vs epochs, Epochs vs iterations, 18:00 to 20:00: [watch](https://www.youtube.com/watch?v=Q0TtSM9aRew&t=1080s). The closing segment that separates an epoch from an iteration after batch, stochastic and mini-batch gradient descent. Chapter-timed.
- CS231n lecture 3, 36:29 to 43:01: [watch](https://www.youtube.com/watch?v=dyNGd06MWn4&t=2189s). Defines stochastic gradient descent on random minibatches of 256 examples and the epoch, then its failure modes. Caption-read.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page was read in the PDF with pdftotext, first found through the books' back-of-book indexes ("epoch", "epochs", "num_train_epochs parameter"). Probabilistic machine learning: an introduction mentions the epoch only in a footnote on reshuffling (PDF page 328) and has no line. The CS231n row was read in its caption-read lecture map under `~/.claude/cache/captions/`. The TileStats chapter list was read with `cache-video-chapters.py` and the line is described from its chapter and video titles only. There is no plans group: plans in the learning tree set epoch counts for their training runs, but none teaches the epoch as its idea.
