---
aliases: [precision and recall, recall and precision, precision@k, recall@k, F1 score, F-score, F-measure, precision-recall curve, PR curve]
standard: vault-note v2
---

# Precision And Recall

Up: [[Machine Learning]]

Artificial Intelligence, Machine Learning. They score a [[Classifier]] where [[Accuracy]] misleads, usually when one class is rare.

**Precision is the share of the items a model flagged that really are positive, TP / (TP + FP); recall is the share of the real positives it found, TP / (TP + FN); the F1 score is their harmonic mean.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches precision and recall writes the rest around it.

## Where to learn this

**Precision and recall**, with the F1 score that combines them. Also: F1 score, precision@k, recall@k, precision-recall curve.

**Textbooks**

- Hands-on large language models, chapter 4: [pages 169 to 171](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=169). Works the numbers on a real classification report for 1,066 movie reviews: precision 0.76 and 0.86, recall 0.88 and 0.72, F1 0.81 and 0.78, read off a confusion matrix of true and false positives and negatives.
- Probabilistic machine learning: an introduction, sections 5.1.3 to 5.1.4: [pages 191 to 196](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=191). The confusion matrix at a threshold τ, ROC curves, then precision, recall, the precision-recall curve, precision at K, and why F1 uses the harmonic mean rather than the average.
- Deep learning textbook, section 11.1: [pages 438 to 440](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=438). A test for a disease one person in a million has: always saying "absent" scores 99.9999% accuracy, so precision and recall are measured instead, traded along a PR curve and joined into an F-score.
- Natural language processing with Python, section 6.3: [pages 261 to 262](../../Mathematics/references/textbooks/natural-language-processing/natural-language-processing-with-python.pdf#page=261). Why accuracy misleads in search tasks, then precision, recall and the F-measure defined from true and false positives and negatives.
- Introduction to probability for data science, section 9.5.4: [pages 617 to 619](../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=617). Precision and recall in terms of detection and false-alarm rates, and the precision-recall curve computed in MATLAB and Python.

**Videos**

- CME295 lecture 1, 10:32 to 22:52: [watch](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=632s). Sorts language tasks into classification, multi-classification and generation, with precision, recall and F1 as the metrics for unbalanced classes. Caption-read.
- ritvikmath, Why is the Formula for F1-Score Unnecessarily Complicated?, Harmonic Approach, 6:10 to 13:37: [watch](https://www.youtube.com/watch?v=GCPDWXWN55U&t=370s). Arrives at F1 as the harmonic mean of precision and recall, after an additive and a multiplicative attempt. Chapter-timed.
- CME295 lecture 7, 47:31 to 57:44: [watch](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2851s). Retrieval metrics: recall@k and precision@k beside NDCG and MRR, and the MTEB benchmark. Caption-read.

**Our plans and chapters**

- [The prototype's baseline, scored with MLflow](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/plans/46-the-baseline.md), ai-engineering/prototype-product-data-validation-end-to-end, plan 46. You fill TP, FP, FN and TN by hand before opening the script, then derive precision, recall, specificity and F-beta for each check.
- [Measurement: before any new check](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/10-measurement.md), the same journey, chapter 10. Defines flag precision and recall for the prototype's checks, and when each is undefined.
- [recall@3 and MRR by hand](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/plans/08-recall-and-mrr-by-hand.md), ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions, plan 08. Recall at 3 for a retriever, computed by hand from ranked chunks.
- [Resolving your 429 description strings against 270 payees](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/29-d3-er-mech.md), data-engineering/many-sources-one-lakehouse, plan 29. An entity resolver scored by pairwise precision and recall against a rule-built baseline.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, first found through the books' back-of-book indexes ("recall", "precision-recall curve", "F1 score, confusion matrices") and the shelf's cached page text. The two lecture rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`. The ritvikmath chapter list was read with `cache-video-chapters.py` and the line is described from its chapter and video titles only; StatQuest's "The Confusion Matrix" was read too and left out, since none of its chapter titles names precision or recall. Each plan and chapter was read at its title, opening lines and the lines naming precision. Bare "precision" and "recall" are not aliases, because this learning tree also uses them for a Gaussian's inverse variance, numerical precision and memory recall; bare "F1" is not either, because most of its 371 uses are plan labels and proposition numbers. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map or a cached chapter list.
