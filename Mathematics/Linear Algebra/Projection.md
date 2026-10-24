---
aliases: [vector projection, orthogonal projection, projection matrix, scalar projection, projection onto]
link-skip: [age-rated projection, real projection, projection table, projection lag, projection schema, projection head, output projection, QKV projection, learned projection, projection layer, Helmholtz projection, is a projection of]
link-not: [Projection]
standard: vault-note v2
---

# Projection

Up: [[Linear Algebra]]

Mathematics, Linear Algebra. [[Dot Product]] computes the shadow's length, and [[Orthogonality]] is what the remainder has with the direction.

**Projecting a vector onto a direction splits it into a shadow along that direction and a remainder perpendicular to it.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches projection writes the rest around it.

## Where to learn this

**Projection**, the shadow of a vector on a direction or a subspace. Also: vector projection, orthogonal projection, projection matrix.

**Textbooks**

- Linear algebra textbook, section 3.3: [pages 172 to 174](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=172). Drops a perpendicular from u to the line through a, proves the projection theorem (Theorem 3.3.2), and gives proj_a u as the orthogonal projection of u on a.
- Mathematics for machine learning, section 3.8: [pages 87 to 94](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=87). Projection onto a line through the origin (page 88), then onto a general subspace (page 91), each with its projection matrix, and a 2-dimensional dataset projected onto a line (Figure 3.9).

**Videos**

- Professor Leonard, Calculus 3 lecture 11.3, Using the Dot Product, Vector projection examples, 1:39:11 to 1:44:43: [watch](https://www.youtube.com/watch?v=TKlGMRghcDs&t=5951s). Vector projections worked as examples on the board. Chapter-timed.
- Professor Leonard, Calculus 3 lecture 11.3, Using the Dot Product, Vector projection formula, 1:35:10 to 1:39:11: [watch](https://www.youtube.com/watch?v=TKlGMRghcDs&t=5710s). The vector projection formula, after the scalar projection in the chapter before. Chapter-timed.
- Stanford CS229, lecture 10, 56:34 to 1:01:50: [watch](https://www.youtube.com/watch?v=sUS-eTa0l6s&t=3394s). Derives the closest point to x on the line through u by minimising ‖x − αu‖², giving α = uᵀx, the orthogonal projection, then extends it to an orthonormal set spanning a subspace. Caption-read.

**Our plans and chapters**

- [Projection onto a unit vector](/home/molef/goal-setting/learning/deep-learning/diffusion-models/08-spectral-structure-of-the-correction/plans/02-orthogonality-and-projection.md), deep-learning/diffusion-models/08-spectral-structure-of-the-correction, plan 02. The shadow of a vector on a unit direction, and why an orthonormal basis makes captured energies add.
- [5. Projection, centering and a matrix as stacked rows](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l0-simple-maths/05-projection-centering-and-stacked-rows.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L0, section 5. The projection that splits a vector into a shadow and a perpendicular remainder.
- [Projecting held-out vectors, and the k/d line](/home/molef/goal-setting/learning/deep-learning/diffusion-models/08-spectral-structure-of-the-correction/plans/11-subspace-projection-and-kd.md), deep-learning/diffusion-models/08-spectral-structure-of-the-correction, plan 11. Projection onto a fitted subspace, and why a random k-dimensional subspace captures k/d of any vector.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after finding it through the back-of-book tables in `~/.claude/cache/book-indexes/` and the chapter tables in `Textbooks.md`. The linear algebra textbook's section 6.3 (orthogonal projections onto a subspace, from PDF page 382) also teaches it and has no line only to keep the list short. The Leonard chapter list was read with cache-video-chapters.py, and those lines describe only the chapter titles. The CS229 row was read in its caption-read lecture map under `~/.claude/cache/captions/`. Each plan and chapter was read at its title and description. "Say what a projection computes, what it does, and what it means" (deep-learning/transformers, plan 23) is about the learned query, key and value matrices and was left out. "projection" alone was sampled in the learning tree (25 lines, about 11 meaning this idea; the rest were financial projections, a table as a projection of data, and projection layers), so only multi-word aliases are used; the note's own name still links, so the common other phrases are in `link-skip`. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
