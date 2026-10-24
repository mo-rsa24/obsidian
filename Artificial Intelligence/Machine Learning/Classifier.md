---
aliases: [classifier, binary classification, multiclass classification, image classification, text classification, classification model, classification task, binary classifier]
link-skip: [classifier-free, classifier guidance, classifier-guided, classifier-based guidance]
standard: vault-note v2
---

# Classifier

Up: [[Machine Learning]]

Artificial Intelligence, Machine Learning. Its outputs are scored by [[Accuracy]] and by [[Precision And Recall]], trained with [[Cross-Entropy]], and turned into class probabilities by [[Softmax]].

**A classifier is a model that assigns each input one label from a fixed set of classes, such as spam or not spam, or one of three iris species, usually by first giving a probability for every class.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches classifiers writes the rest around it.

## Where to learn this

**Classifier**, a model that predicts a class label. Also: binary classification, multiclass classification, image classification.

**Textbooks**

- Hands-on large language models, chapter 4: [pages 160 to 171](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=160). Works a classifier end to end on real data: 5,331 positive and 5,331 negative Rotten Tomatoes reviews labelled by a pretrained model, then scored on 1,066 test reviews with an F1 score of 0.80.
- Probabilistic machine learning: an introduction, section 1.2.1: [pages 30 to 34](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=30). Classification on the iris data: 150 flowers with four measurements each and one of three species as the label, a fitted classifier, and its misclassification rate.
- Understanding deep learning, sections 5.4 to 5.5: [pages 78 to 83](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=78). A network becomes a binary classifier by predicting a Bernoulli probability through the logistic sigmoid, and a K-class classifier by predicting a categorical distribution through the softmax.
- Pattern recognition and machine learning, chapter 4 opening: [pages 198 to 200](../../Mathematics/references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=198). Class labels coded as 0 and 1 or as one-hot vectors, and the three ways to build a classifier: a discriminant function, a model of p(C | x), or a generative model through Bayes' theorem.

**Videos**

- CS231n lecture 2, 16:35 to 20:12: [watch](https://www.youtube.com/watch?v=pdqofxJeBN8&t=995s). Builds the nearest neighbour classifier: training memorises the data, prediction returns the label of the closest training image under the summed absolute pixel difference, worked on a small pixel grid. Caption-read.
- CS229 lecture 1, 12:39 to 14:39: [watch](https://www.youtube.com/watch?v=DATnpGoGhM8&t=759s). Separates regression (continuous y) from classification (discrete y) with a house against townhouse boundary, and frames next-token prediction as classification over the vocabulary. Caption-read.
- CS229 lecture 3, 34:43 to 37:45: [watch](https://www.youtube.com/watch?v=uJF_gL3jhxI&t=2083s). Sets up binary classification with y in {0, 1} and draws why least squares fails as a classifier: far-away points drag the line off the gap between classes. Caption-read.
- Luis Serrano, Logistic Regression and the Perceptron Algorithm: A friendly introduction, E-mail spam classifier, 0:41 to 7:19: [watch](https://www.youtube.com/watch?v=jbluHIgBmBo&t=41s). Opens the friendly introduction with a spam classifier for e-mail. Chapter-timed.

**Our plans and chapters**

- [Classical ML from Scratch](/home/molef/goal-setting/learning/machine-learning/classical-ml-from-scratch/MASTER_PLAN.md), machine-learning/classical-ml-from-scratch. Goal 1 classifies a toy dataset with logistic regression written by hand, and goal 7 builds a confusion matrix and ROC curve for a fitted classifier from raw predictions.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, first found through the shelf index's chapter tables (38 classification sections across the shelf) and the books' back-of-book indexes. The four lecture-map rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`; the Serrano chapter list was read with `cache-video-chapters.py`, and that line is described from its chapter and video titles only. The plan was read at its goals and definition of done. The learning tree's other plans that say "classifier" build rule-based tools that sort failures or image actions, so they have no line. Bare "classifier" is an alias because, of 25 sampled uses, every one outside "classifier-free guidance" and "classifier guidance" means a model that assigns classes, and those phrases are in link-skip. Bare "classification" is not: about 13 of 25 sampled uses mean the machine learning task, and the rest mean filing schemes, product taxonomies or labelling a document field.
