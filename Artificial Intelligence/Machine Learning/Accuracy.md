---
aliases: [accuracy, classification accuracy, test accuracy, top-1 accuracy, top-5 accuracy, misclassification rate]
link-skip: [media richness, factual accuracy]
standard: vault-note v2
---

# Accuracy

Up: [[Machine Learning]]

Artificial Intelligence, Machine Learning. It scores a [[Classifier]]; [[Precision And Recall]] replace it when one class is rare, and [[Abstention In Agreement Scores]] handles accuracy when some items get no answer.

**Accuracy is the share of predictions a classifier gets right, correct predictions divided by all predictions; one minus it is the misclassification rate.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches accuracy writes the rest around it.

## Where to learn this

**Accuracy**, the fraction of predictions that are correct. Also: classification accuracy, test accuracy, misclassification rate.

**Textbooks**

- Natural language processing with Python, section 6.3: [page 261](../../Mathematics/references/textbooks/natural-language-processing/natural-language-processing-with-python.pdf#page=261). Works it with numbers: 60 names right out of 80 is 60/80 = 75%, computed with `nltk.classify.accuracy`, then why 95% means little when one word sense makes up 19 of every 20 cases.
- Hands-on large language models, chapter 4: [pages 169 to 170](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=169). Accuracy of 0.80 over 1,066 test reviews in a classification report, defined from the confusion matrix beside precision, recall and F1.
- Deep learning textbook, section 11.1: [pages 438 to 439](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=438). Accuracy as the usual performance metric, and how a test for a one-in-a-million disease reaches 99.9999% accuracy by always saying "absent".
- Probabilistic machine learning: an introduction, section 1.2.1.4: [page 33](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=33). The misclassification rate on the training set, (1/N) Σ I(yₙ ≠ f(xₙ; θ)), as the measure classification training aims to lower.

**Videos**

- CS231n lecture 2, 41:27 to 46:03: [watch](https://www.youtube.com/watch?v=pdqofxJeBN8&t=2487s). Runs k-nearest neighbours on CIFAR-10's 10 classes: cross-validation picks k = 7 at about 28% to 29% accuracy against 10% for chance. Caption-read.
- CS229 lecture 6, 1:02:18 to 1:09:20: [watch](https://www.youtube.com/watch?v=llnEgyyuYkQ&t=3738s). Double descent, and the ImageNet v2 result where every model's accuracy dropped on new test images but their ranking held. Caption-read.
- CS231n lecture 6, 1:07:03 to 1:10:41: [watch](https://www.youtube.com/watch?v=aVJy4O5TOk8&t=4023s). A training recipe that watches training and validation accuracy side by side to catch overfitting. Caption-read.
- TileStats, U-Net clearly explained, Pixel accuracy, 17:22 to 18:29: [watch](https://www.youtube.com/watch?v=oxcgx75k6yU&t=1042s). Accuracy counted over pixels to score an image segmentation. Chapter-timed.

**Our plans and chapters**

- [Execution accuracy: compare rows, never query text](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/44-execution-accuracy.md), ai-engineering/one-business-end-to-end, plan 44. Builds the comparator that decides whether a SQL agent's answer matches each of forty gold row sets, so its accuracy can be counted.
- [The prototype's baseline, scored with MLflow](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/plans/46-the-baseline.md), ai-engineering/prototype-product-data-validation-end-to-end, plan 46. Binary decision accuracy reported beside precision, recall and abstention for each check, with counts and an uncertainty method.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, first found through the books' back-of-book indexes ("accuracy", "accuracy of classification", "accuracy, confusion matrices"). The three lecture rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`. The TileStats chapter list was read with `cache-video-chapters.py` and the line is described from its chapter and video titles only. Each plan was read at its title and description. Bare "accuracy" is an alias because about 22 of 25 sampled uses in the learning tree mean a model's or agent's share of correct answers; the link-skip phrases cover the data-quality sense (a scorecard of completeness, accuracy, consistency and media richness) and the factual accuracy of generated text. The aliases of [[Abstention In Agreement Scores]] ("covered accuracy", "full-set accuracy bound") were checked first and are left to that note. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map or a cached chapter list.
