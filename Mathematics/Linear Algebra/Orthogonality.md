---
aliases: [orthogonal, orthonormal, orthogonal vectors, orthogonal matrix, orthonormal basis]
standard: vault-note v2
---

# Orthogonality

Up: [[Linear Algebra]]

Mathematics, Linear Algebra. [[Dot Product]] is the test, and [[Projection]] splits a vector into orthogonal parts.

**Two vectors are orthogonal when their dot product is zero, meaning they are perpendicular; orthonormal vectors are orthogonal and also have length 1.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches orthogonality writes the rest around it.

## Where to learn this

**Orthogonality**, perpendicular vectors with dot product zero. Also: orthogonal, orthonormal, orthogonal matrix, orthonormal basis.

**Textbooks**

- Mathematics for machine learning, sections 3.4 and 3.5: [pages 82 to 85](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=82). Works the angle between [1, 1] and [1, 2] as about 18 degrees (Example 3.6), then defines orthogonal vectors, orthogonal matrices and orthonormal bases.
- Linear algebra textbook, section 3.3: [pages 169 to 171](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=169). Two vectors are orthogonal when u·v = 0 (Definition 1), with orthogonal sets such as the standard unit vectors.
- Deep learning textbook, section 2.6: [pages 57 to 58](../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=57). Unit vectors, orthogonal and orthonormal vectors, and orthogonal matrices, whose rows are fully orthonormal and whose inverse is cheap.
- Linear algebra textbook, section 7.1: [pages 415 to 422](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=415). Orthogonal matrices, whose inverse is their transpose, and their properties.
- Understanding deep learning, appendix B.4.3: [page 460](../references/textbooks/machine-learning/understanding-deep-learning.pdf#page=460). Orthogonal matrices as rotations and reflections, so their eigenvalues all have magnitude one.

**Videos**

- Professor Leonard, Calculus 3 lecture 11.3, Using the Dot Product, Orthogonal vectors check, 1:13:30 to 1:17:53: [watch](https://www.youtube.com/watch?v=TKlGMRghcDs&t=4410s). Checking whether given vectors are orthogonal, on the board. Chapter-timed.
- Professor Leonard, Calculus 3 lecture 11.3, Using the Dot Product, Orthogonal vectors, 51:43 to 53:47: [watch](https://www.youtube.com/watch?v=TKlGMRghcDs&t=3103s). Orthogonal vectors as the case where the dot product is zero, right after finding the angle. Chapter-timed.
- Stanford CME295, lecture 1, 30:04 to 35:12: [watch](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1804s). One-hot vectors over a three-token vocabulary are all orthogonal, so they cannot say two words are related. Caption-read.
- Stanford CS229, lecture 10, 48:57 to 56:34: [watch](https://www.youtube.com/watch?v=sUS-eTa0l6s&t=2937s). PCA on car mileage data, with each point written in an orthonormal basis as x = α₁u₁ + α₂u₂. Caption-read.

**Our plans and chapters**

- [Projection onto a unit vector](/home/molef/goal-setting/learning/deep-learning/diffusion-models/08-spectral-structure-of-the-correction/plans/02-orthogonality-and-projection.md), deep-learning/diffusion-models/08-spectral-structure-of-the-correction, plan 02. Why an orthonormal basis makes the energies captured along each direction add up.
- [Displacement orthogonal to the manifold](/home/molef/goal-setting/learning/deep-learning/diffusion-models/05-poe-composition-diffusion/plans/52-orthogonal-displacement.md), deep-learning/diffusion-models/05-poe-composition-diffusion, plan 52. A displacement split into tangential and normal parts by hand, then numerically on a known manifold.
- [Mathematics: Linear Algebra](/home/molef/goal-setting/learning/mathematics/linear-algebra/MASTER_PLAN.md), mathematics/linear-algebra. Its fourth objective is orthogonality: inner product spaces, Gram-Schmidt and orthogonal projections; no plan files exist under it yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after finding it through the back-of-book tables in `~/.claude/cache/book-indexes/` and the chapter tables in `Textbooks.md`. The Leonard chapter list was read with cache-video-chapters.py, and those lines describe only the chapter titles. The CME295 and CS229 rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`. Each plan was read at its title and description. "orthogonal" alone was sampled in the learning tree (25 lines, 24 meaning this idea and one figurative), so it is an alias; "orthonormal" has 20 uses, all this idea. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
