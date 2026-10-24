---
aliases: [singular value decomposition, SVD, singular value, singular vector, truncated SVD]
standard: vault-note v2
---

# Singular Value Decomposition

Up: [[Linear Algebra]]

Mathematics, Linear Algebra. [[Eigenvalue]] covers the eigendecomposition the SVD is built from.

**The singular value decomposition writes any matrix as A = UΣVᵀ: a rotation, a stretch along perpendicular axes by the singular values, and another rotation.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the SVD writes the rest around it.

## Where to learn this

**Singular value decomposition (SVD)**, A = UΣVᵀ for any matrix. Also: SVD, singular values, singular vectors, truncated SVD.

**Textbooks**

- Mathematics for machine learning, section 4.5: [pages 125 to 134](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=125). Works an SVD by hand (Example 4.13, page 131) after its geometric picture (Example 4.12) and its construction from AᵀA, then reads movie ratings with it.
- Linear algebra textbook, section 9.4: [pages 528 to 534](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=528). Singular values, then the SVD in brief and expanded form, with Example 2 for a matrix that is not square.
- Linear algebra textbook, section 9.5: [pages 535 to 538](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=535). The reduced SVD, and compressing an image by keeping only the largest singular values.
- Probabilistic machine learning: an introduction, section 7.5: [pages 287 to 291](../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=287). The basics, the link to the eigendecomposition, the pseudo-inverse and the truncated SVD.

**Videos**

- tilestats, PCA and SVD: the math explained simply, The singular value decomposition, 16:47 to 22:59: [watch](https://www.youtube.com/watch?v=HZl32cDhWEM&t=1007s). The SVD as the second way to compute PCA, after the eigendecomposition method in the chapter before. Chapter-timed.
- StatQuest, Principal Component Analysis (PCA), Step-by-Step, Singular vector/value, Eigenvector/value and loading scores defined, 12:08 to 12:56: [watch](https://www.youtube.com/watch?v=FgakZw6K1QQ&t=728s). Names the singular vector and singular value inside a PCA worked on 2-dimensional data. Chapter-timed.

**Our plans and chapters**

- [SVD of your own 440 x 65,536 matrix](/home/molef/goal-setting/learning/deep-learning/diffusion-models/08-spectral-structure-of-the-correction/plans/06-svd-of-the-real-matrix.md), deep-learning/diffusion-models/08-spectral-structure-of-the-correction, plan 06. Stacks cached correction rows and runs the SVD on them in a notebook.
- [Singular values as per-direction gains](/home/molef/goal-setting/learning/deep-learning/diffusion-models/08-spectral-structure-of-the-correction/plans/07-singular-values-as-gains.md), the same journey, plan 07. What σᵢ measures, through Rvᵢ = σᵢuᵢ.
- [Mathematics: Linear Algebra](/home/molef/goal-setting/learning/mathematics/linear-algebra/MASTER_PLAN.md), mathematics/linear-algebra. Its fifth goal implements the SVD from the eigendecomposition of AᵀA and compresses an image with it; no plan files exist under it yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after finding it through the back-of-book tables in `~/.claude/cache/book-indexes/` and the chapter tables in `Textbooks.md`. The deep learning textbook's section 2.8 (PDF pages 60 to 61) also defines the SVD and has no line only to keep the list short. The tilestats and StatQuest chapter lists were read with cache-video-chapters.py, and those lines describe only the chapter and video titles. No 3Blue1Brown or Professor Leonard video covers the SVD. Each plan was read at its title and description. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
