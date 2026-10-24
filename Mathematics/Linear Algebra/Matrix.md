---
aliases: [matrix, matrices, matrix multiplication, matrix product, matrix-vector product, matrix multiply]
link-skip: [build matrix, environment matrix, test matrix, confusion matrix, traceability matrix]
standard: vault-note v2
---

# Matrix

Up: [[Linear Algebra]]

Mathematics, Linear Algebra. [[Vector]] and [[Dot Product]] are the pieces a matrix product is built from.

**A matrix is a rectangular grid of numbers, and multiplying a vector by it applies a linear map: each output entry is the dot product of one row with the vector.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches matrices writes the rest around it.

## Where to learn this

**Matrix**, a grid of numbers that acts on vectors. Also: matrices, matrix multiplication, matrix product.

**Textbooks**

- Linear algebra textbook, section 1.3: [pages 39 to 52](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=39). Matrix notation, then the row-by-column product worked on a 2 by 3 times a 3 by 4 matrix (Example 5, page 43).
- Mathematics for machine learning, section 2.2: [pages 28 to 32](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=28). Matrix addition and multiplication, inverse and transpose, and a system of linear equations written compactly as one matrix equation.
- Deep learning textbook, section 2.2: [pages 50 to 51](../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=50). The matrix product, the element-wise product and its properties, as deep learning uses them.
- Probabilistic machine learning: an introduction, section 7.2: [pages 272 to 276](../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=272). Vector-vector, matrix-vector and matrix-matrix products, then manipulating a data matrix.

**Videos**

- tilestats, Matrices and matrix operations for beginners 1/2, Matrix multiplication, 8:31 to 12:27: [watch](https://www.youtube.com/watch?v=QtAZsWseIKk&t=511s). Matrix multiplication for beginners, followed in the next chapter by why the order matters. Chapter-timed.
- 3Blue1Brown, Linear transformations and matrices (Essence of linear algebra, chapter 3), Basis vectors and matrices, 3:32 to 6:18: [watch](https://www.youtube.com/watch?v=kYB8IZa5AuE&t=212s). A matrix read as where the basis vectors land. Chapter-timed.
- 3Blue1Brown, Matrix multiplication as composition (Essence of linear algebra, chapter 4), General matrix multiplication, 5:56 to 7:26: [watch](https://www.youtube.com/watch?v=XkY2DOUCWMU&t=356s). The product of two matrices as one transformation applied after another. Chapter-timed.
- Stanford CME295, lecture 1, 1:31:35 to 1:35:12: [watch](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5495s). Computes self-attention as softmax(QKᵀ/√d_k)V matrix by matrix, reading rows of Q as queries and columns of Kᵀ as keys. Caption-read.

**Our plans and chapters**

- [Multiply two matrices row by column and say why the order matters](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/03-multiply-two-matrices-row-by-column.md), deep-learning/transformers, chapter 03. The same two matrices multiplied in both orders, tracking where each entry comes from.
- [Say what a 2 by 2 matrix does to the plane: rotate, stretch or squash](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/04-say-what-a-2-by-2-matrix.md), deep-learning/transformers, chapter 04. The point [2, 1] sent through a rotation, a squash and a stretch.
- [Show an embedding table is a one-hot vector times a matrix](/home/molef/goal-setting/learning/deep-learning/transformers/plans/33-show-an-embedding-table-is-a-one.md), deep-learning/transformers, plan 33. A matrix product that picks out one row.
- [The matrix as a pile of rows](/home/molef/goal-setting/learning/deep-learning/diffusion-models/08-spectral-structure-of-the-correction/plans/04-matrix-as-stacked-rows.md), deep-learning/diffusion-models/08-spectral-structure-of-the-correction, plan 04. A 440 by 65,536 matrix read as 440 stacked corrections, and a matrix-vector product as 440 dot products.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after finding it through the back-of-book tables in `~/.claude/cache/book-indexes/` and the chapter tables in `Textbooks.md`. The tilestats and 3Blue1Brown chapter lists were read with cache-video-chapters.py, and those lines describe only the chapter and video titles. The CME295 row was read in its caption-read lecture map under `~/.claude/cache/captions/`. Each plan and chapter was read at its title and description. "matrix" alone was sampled in the learning tree (25 lines, 22 meaning this idea; the rest were a CI build matrix, an environment matrix and a test matrix, now in `link-skip`). "matrices" is listed as an alias because the linker adds only "s" or "es" for plurals. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
