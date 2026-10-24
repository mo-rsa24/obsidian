---
aliases: [cosine similarity, cosine distance, cosine of the angle between]
standard: vault-note v2
---

# Cosine Similarity

Up: [[Linear Algebra]]

Mathematics, Linear Algebra. It divides the [[Dot Product]] by both vectors' [[Norm]]; [[The Cosine Wave]] covers the cosine function itself.

**Cosine similarity is the cosine of the angle between two vectors, their dot product divided by both lengths, so it compares direction and ignores length.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches cosine similarity writes the rest around it.
> - The placement is unsure. The two best places are `Mathematics/Linear Algebra/` and `Artificial Intelligence/`, beside [[Retrieval-Augmented Generation]], where most of its uses are.

## Where to learn this

**Cosine similarity**, the dot product divided by both lengths. Also: cosine distance.

**Textbooks**

- Mathematics for machine learning, section 3.4: [pages 82 to 83](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=82). Works cos ω = 3/√10 between [1, 1] and [1, 2] with numbers (Example 3.6), an angle of about 18 degrees.
- Linear algebra textbook, section 3.2: [pages 160 to 163](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=160). The cosine of the angle as u·v over the two norms, worked for a cube's diagonal and edge, and extended to Rⁿ by the Cauchy-Schwarz inequality.
- Hands-on large language models, chapter 4: [pages 177 to 179](../references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=177). Labels documents by the cosine similarity between document and label embeddings, drawn as an angle (Figure 4-15) and computed with scikit-learn.
- Probabilistic machine learning: an introduction, chapter 20: [page 752](../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=752). Ranks documents by cosine similarity to a query vector, and notes it equals the inner product for unit-norm vectors (Figure 20.43).

**Videos**

- The Organic Chemistry Tutor, Dot Product of Two Vectors, Finding the angle between, 15:30 to 30:42: [watch](https://www.youtube.com/watch?v=VzX8KJKFhlM&t=930s). Finding the angle between two vectors from their dot product and magnitudes, on examples. Chapter-timed.
- Stanford CME295, lecture 1, 30:04 to 35:12: [watch](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1804s). One-hot vectors for soft, teddy bear and book are all orthogonal, so cosine similarity cannot say soft and teddy bear are related. Caption-read.
- Stanford CME295, lecture 7, 27:29 to 37:45: [watch](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1649s). Retrieves RAG candidates by cosine similarity between query and chunk embeddings, then adds BM25 keyword scoring and hybrid search. Caption-read.
- Stanford CS229, lecture 13, 26:22 to 30:01: [watch](https://www.youtube.com/watch?v=lNTajqxxOn4&t=1582s). SimCLR's similarity matrix of dot products of normalised embeddings, whose diagonal should be large. Caption-read.

**Our plans and chapters**

- [Cosine similarity by hand on two short vectors](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/50-cosine-similarity-by-hand.md), ai-engineering/one-business-end-to-end, plan 50. The retriever's score computed by hand, twice, on three-dimensional vectors.
- [3. Cosine similarity](/home/molef/goal-setting/learning/deep-learning/diffusion-models/08-spectral-structure-of-the-correction/textbook/03-cosine.md), deep-learning/diffusion-models/08-spectral-structure-of-the-correction, chapter 03. A per-seed cosine of about 0.002 read against the chance scale for high-dimensional vectors.
- [Show when the dot product and cosine rank differently](/home/molef/goal-setting/learning/deep-learning/transformers/plans/18-show-when-the-dot-product-and-cosine.md), deep-learning/transformers, plan 18. Tripling a key's length moves its dot product from 0.7 to 2.1 while its cosine stays 0.7071.
- [Cosine: compare word-count directions](/home/molef/goal-setting/learning/ai-engineering/string-similarity-measures/textbook/19-cosine.md), ai-engineering/string-similarity-measures, chapter 19. Cosine on word-count vectors, and how one inserted space changes them.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after finding it through the back-of-book tables in `~/.claude/cache/book-indexes/` and the chapter tables in `Textbooks.md`. The Organic Chemistry Tutor chapter list was read with cache-video-chapters.py, and that line describes only the chapter title. The CME295 and CS229 rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`. Each plan and chapter was read at its title and description. Bare "cosine" also names the cosine noise schedule and the trigonometric function, which have their own notes, so only multi-word aliases are used. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
