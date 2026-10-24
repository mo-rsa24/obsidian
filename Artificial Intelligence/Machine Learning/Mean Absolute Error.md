---
aliases: [mean absolute error, MAE, absolute error loss, L1 loss, least absolute deviation]
standard: vault-note v2
---

# Mean Absolute Error

Up: [[Machine Learning]]

Artificial Intelligence, Machine Learning. It is one [[Loss Function]], and [[Mean Squared Error]] is its squared sibling.

**Mean absolute error is the average of the absolute differences between predictions and true values, so a miss of 2 costs twice a miss of 1 and an outlier pulls the fit far less than under squared error.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches mean absolute error writes the rest around it.

## Where to learn this

**Mean absolute error (MAE)**, the average absolute prediction error. Also: MAE, L1 loss, least absolute deviation.

**Textbooks**

- Introduction to probability for data science, section 7.1.4: [pages 429 to 432](../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=429). Works a concrete case: a fourth-order polynomial fitted to 50 points is pulled off course by a handful of outliers under squared error, then refitted with the absolute error, solved as a linear programme with `scipy.optimize.linprog`.
- Deep learning textbook, section 6.2.1.2: [pages 196 to 197](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=196). Shows that minimising mean squared error predicts the mean of y for each x while minimising mean absolute error predicts the median, and why both train poorly with saturating output units.
- Probabilistic machine learning: an introduction, sections 5.1.5.2 to 5.1.5.3: [pages 196 to 197](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=196). The ℓ1 loss |h − a| as the outlier-robust alternative whose best estimate is the posterior median, drawn beside the ℓ2 loss and the Huber loss that blends them.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, found by searching the shelf's cached page text for "mean absolute error", "absolute loss" and "ℓ1 loss", since the back-of-book indexes list MAE only once (Probabilistic machine learning: advanced topics, page 1086). Understanding deep learning mentions mean absolute error only in the notes to chapter 5 (PDF page 87) and has no line. There is no Videos group: no lecture-map row teaches mean absolute error (the CS231n rows that say "MAE" mean masked autoencoders), and the one candidate chapter list read, ritvikmath's "Loss Functions : Data Science Basics", has no chapter whose title names regression losses. There is no plans group: the learning tree only uses MAE as a number (a forecasting backtest and a quantization plan) and has no plan or chapter that teaches it.
