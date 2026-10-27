---
aliases: [dot product, inner product, scalar product]
standard: vault-note v2
---

# Dot Product

Up: [[Linear Algebra]]

Mathematics, Linear Algebra. [[Cosine Similarity]] divides the dot product by both lengths, and [[Attention]] scores keys by it.

**The dot product of two vectors multiplies them entry by entry and adds the results, which equals their two lengths times the cosine of the angle between them.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the dot product writes the rest around it.

## Where to learn this

**Dot product**, the sum of entry-by-entry products. Also: inner product, scalar product.

**Textbooks**

- Linear algebra textbook, section 3.2: [pages 159 to 164](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=159). Works u·v = ‖u‖‖v‖cos θ with numbers on two vectors 45 degrees apart (Example 5, page 160), then derives the component formula and the Cauchy-Schwarz inequality.
- Linear algebra textbook, section 3.2, Application of dot products to ISBN numbers: [page 165](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=165). Forms an ISBN's check digit as the dot product of its first nine digits with the weights (1, …, 9), then takes the remainder on division by 11, the same weighted-sum shape as a GS1 barcode check digit.
- Mathematics for machine learning, section 3.2: [pages 78 to 80](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=78). The dot product, then general inner products and the symmetric positive definite matrices that define them.
- Understanding deep learning, appendix B.3.4: [page 457](../references/textbooks/machine-learning/understanding-deep-learning.pdf#page=457). The dot product as a sum of products and as ‖a‖‖b‖cos θ, in two lines.
- Probabilistic machine learning: an introduction, section 7.2.1: [page 272](../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=272). The inner product as the first of the vector-vector products.

**Videos**

- The Organic Chemistry Tutor, Dot Product of Two Vectors, Introduction to dot products, 0:00 to 2:08: [watch](https://www.youtube.com/watch?v=VzX8KJKFhlM&t=0s). Opens a video of dot products computed on example vectors. Chapter-timed.
- 3Blue1Brown, Dot products and duality (Essence of linear algebra, chapter 9), Geometric interpretation, 1:24 to 3:56: [watch](https://www.youtube.com/watch?v=LyGKycYT2v0&t=84s). The dot product as the length of one vector's projection times the other's length. Chapter-timed.
- Professor Leonard, Calculus 3 lecture 11.3, Using the Dot Product, Calculating the dot product, 6:44 to 9:54: [watch](https://www.youtube.com/watch?v=TKlGMRghcDs&t=404s). Calculating dot products on the board, at the start of a full lecture on using them. Chapter-timed.
- Stanford CS229, lecture 16, 15:07 to 18:09: [watch](https://www.youtube.com/watch?v=hHC-SF3utxg&t=907s). The dot product of two random ±1 vectors of dimension d_h has size about √d_h, which is why attention divides by it. Caption-read.

**Our plans and chapters**

- [1. The dot product](/home/molef/goal-setting/learning/deep-learning/diffusion-models/08-spectral-structure-of-the-correction/textbook/01-dot-product.md), deep-learning/diffusion-models/08-spectral-structure-of-the-correction, chapter 01. The dot product as arithmetic, built for computing every correction row against one direction.
- [Find a length, a unit vector and an angle from two lengths and a dot product](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/02-find-a-length-a-unit-vector.md), deep-learning/transformers, chapter 02. The dot product of [3, 0] and [2, 2] is 6, turned into an angle.
- [Simulate the variance of a dot product at three sizes](/home/molef/goal-setting/learning/deep-learning/transformers/plans/07-simulate-the-variance-of-a-dot-product.md), deep-learning/transformers, plan 07. How the spread of a dot product grows with the number of coordinates, measured.
- [Compute vectors, the dot product, length and the angle between them](/home/molef/goal-setting/learning/ai-engineering/string-similarity-measures/foundations/plans/06-vectors-dot-product-and-length.md), ai-engineering/string-similarity-measures/foundations, plan 06. The dot product of two word-count vectors.
- [Dot, norm and cosine refresher, page 3](/home/molef/goal-setting/learning/deep-learning/diffusion-models/08-spectral-structure-of-the-correction/textbook/refresher-dot-norm-cosine.pdf#page=3), deep-learning/diffusion-models/08-spectral-structure-of-the-correction, textbook refresher. Reads the dot product as an agreement score between two vectors, then a matrix-vector product as stacked dot products.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/clip-by-hand-thumbnail.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/clip-by-hand-thumbnail.jpg" width="200" alt="A hand-worked sheet: three text-image pairs encoded on two sides, projected into a yellow shared embedding space, then softmax similarity matrices and cross-entropy gradients against identity targets"></a> Prof. Tom Yeh on X, "CLIP by hand": [the post](https://x.com/ProfTomYeh/status/2094791189371261274), [what it shows](/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/README.md#clip-by-hand-thumbnailjpg). Step 9 takes the dot product of every text vector with every image vector in the shared 2-number space, one cell per sentence-picture pair, and the post closes on the point that matching a picture with a sentence comes down to that single dot product.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after finding it through the back-of-book tables in `~/.claude/cache/book-indexes/` and the chapter tables in `Textbooks.md`. The Organic Chemistry Tutor, 3Blue1Brown and Leonard chapter lists were read with cache-video-chapters.py, and those lines describe only the chapter and video titles. The CS229 row was read in its caption-read lecture map under `~/.claude/cache/captions/`. Each plan and chapter was read at its title and description. "dot-product attention" stays with [[Attention]], whose longer alias wins. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
