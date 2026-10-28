---
aliases: [softmax, softmax function, softmax layer, softmax output, softmax weights]
standard: vault-note v2
---

# Softmax

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. It feeds [[Cross-Entropy]] when training a [[Classifier]], and it turns scores into weights inside [[Attention]].

**Softmax turns a list of real-valued scores (logits) into probabilities by exponentiating each one and dividing by the sum, so every output is positive, they add to one, and the largest score gets the largest share.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches softmax writes the rest around it.

## Where to learn this

**Softmax**, exp(zₖ) / Σⱼ exp(zⱼ). Also: softmax function, softmax layer, softmax weights.

**Textbooks**

- AI engineering, chapter 2, Sampling: [pages 192 to 194](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=192). Works it with numbers: logits [1, 2] give softmax probabilities [0.27, 0.73], and dividing by a temperature of 0.5 first gives [0.12, 0.88], drawn across temperatures in figure 2-16.
- Understanding deep learning, section 5.5: [pages 81 to 82](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=81). Softmax as the function that makes K arbitrary network outputs non-negative and [sum to one](../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=165), so they can be the parameters of a categorical distribution (figure 5.10).
- Probabilistic machine learning: an introduction, section 2.5.2: [pages 79 to 80](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=79). Defines softmax and logits, then divides by a temperature T to show it tends to the argmax as T goes to 0 and to uniform as T grows.
- Deep learning textbook, section 6.2.2.3: [pages 200 to 202](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=200). Softmax units for a multinoulli output: why [the log-likelihood undoes the exp](../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=110), saturation, and the numerically stable form that [subtracts the largest input](../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=109).
- Deep learning, section 4.1, Overflow and underflow: [page 97](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=97). Evaluates softmax(z) with z = x − max_i x_i, so the softmax neither overflows nor divides by zero.

**Videos**

- CS229 lecture 4, 52:29 to 54:29: [watch](https://www.youtube.com/watch?v=8gVi4Rk21Eg&t=3149s). Works the softmax numbers: raw scores 2, 1 and 0.1 are exponentiated and normalised into class probabilities. Caption-read.
- CS231n lecture 2, 57:30 to 1:00:36: [watch](https://www.youtube.com/watch?v=pdqofxJeBN8&t=3450s). Turns a cat image's scores 3.2, 5.1 and −1.7 into probabilities, giving the cat class 0.13, and names the raw scores logits. Caption-read.
- CS229 lecture 4, 39:50 to 44:27: [watch](https://www.youtube.com/watch?v=8gVi4Rk21Eg&t=2390s). Defines p(y = j | x) = exp(θⱼᵀx) / Σₗ exp(θₗᵀx) and draws each class's hyperplane in a two-dimensional picture of four classes. Caption-read.
- CME295 lecture 3, 50:44 to 1:00:15: [watch](https://www.youtube.com/watch?v=Q5baLehv5So&t=3044s). Writes softmax with temperature and factors out the largest logit to prove the distribution goes one-hot as T → 0 and uniform as T → ∞. Caption-read.

**Our plans and chapters**

- [Turn one question's chunk scores into softmax weights by hand](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/soft-retrieval-with-softmax-weights/plans/01-softmax-weights-by-hand.md), ai-engineering/llm-applications/retrieval-augmented-generation/soft-retrieval-with-softmax-weights, plan 01. One question's retrieval scores turned into softmax weights on paper before the notebook opens.
- [Turn scores into softmax weights and blend the values](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/20-turn-scores-into-softmax-weights-and-blend.md), deep-learning/transformers, chapter 20. A query's scores over three keys become softmax weights that blend the values, against keeping only the top hit.
- [Log-sum-exp and the softmax gradient](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l0-simple-maths/01-log-sum-exp-and-the-softmax-gradient.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L0, section 1. Proves that the gradient of log-sum-exp is the softmax, the step behind a Gaussian mixture's score.
- [Measure the softmax saturating at d = 1024 and fix it with the division](/home/molef/goal-setting/learning/deep-learning/transformers/plans/26-measure-the-softmax-saturating-at-d-1024.md), deep-learning/transformers, plan 26. Measures a softmax going one-hot when scores grow with dimension, and fixes it by dividing by the square root of d.
- [Show why softmax weights can never say "I don't know"](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/soft-retrieval-with-softmax-weights/plans/03-why-softmax-cannot-say-i-dont-know.md), the soft-retrieval journey, plan 03. Softmax weights do not change when every score shifts by the same amount, so a question with no answer still gives its best chunk weight 0.5284, and a cut-off has to use the raw cosine.

**Scenes**

- [The SDXL notebook in ten parts, Self-attention](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-attn). Self-attention among image tokens, a 4096 by 4096 map at full size.
- [The SDXL notebook in ten parts, Cross-attention](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-attn). Cross-attention from 4096 image tokens to 77 text tokens, softmax over each row, scaled by one over root d.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/clip-by-hand-thumbnail.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/clip-by-hand-thumbnail.jpg" width="200" alt="A hand-worked sheet: three text-image pairs encoded on two sides, projected into a yellow shared embedding space, then softmax similarity matrices and cross-entropy gradients against identity targets"></a> Prof. Tom Yeh on X, "CLIP by hand": [the post](https://x.com/ProfTomYeh/status/2094791189371261274), [what it shows](/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/README.md#clip-by-hand-thumbnailjpg). Steps 10 to 12 take the softmax of a 3 by 3 text-image score matrix by hand: e to every cell, sums along each row for image to text and each column for text to image, then a divide, giving one similarity matrix per direction. The video rounds e to 3 to keep the arithmetic hand-sized, so its cells are not true softmax values ([the reading](/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/sources/clip-embeddings/SOURCES.md#parked-not-yet-studied)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, first found through the books' back-of-book indexes and the shelf index's softmax row. Pattern recognition and machine learning uses the softmax for multiclass logistic regression (section 4.3.4, PDF page 216) and has no line, to keep four. The four lecture rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`. StatQuest's "Neural Networks Part 5: ArgMax and SoftMax" chapter list was read with `cache-video-chapters.py` (its SoftMax chapter runs 4:21 to 6:36) and left out to keep four lines. Each plan and chapter was read at its title and opening lines. The phrases "softmax loss" and "softmax(QK^T/sqrt(d))V" stay with [[Cross-Entropy]] and [[Attention]]. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map.
