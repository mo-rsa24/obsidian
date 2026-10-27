---
aliases: [eigenvalue, eigenvector, eigendecomposition, eigenvalue decomposition, eigen decomposition]
standard: vault-note v2
---

# Eigenvalue

Up: [[Linear Algebra]]

Mathematics, Linear Algebra. [[Singular Value Decomposition]] extends the idea to matrices that are not square.

**An eigenvector of a square matrix is a direction the matrix only stretches, Av = λv, and the eigenvalue λ is the stretch factor.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches eigenvalues writes the rest around it.

## Where to learn this

**Eigenvalue**, the stretch factor along an eigenvector, Av = λv. Also: eigenvector, eigendecomposition, eigenvalue decomposition.

**Textbooks**

- Mathematics for machine learning, section 4.2: [pages 111 to 119](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=111). Works the eigenvalues 5 and 2 and their eigenspaces for a 2 by 2 matrix (Example 4.5), then eigenvalues in a neural network and PageRank (Examples 4.7 and 4.9).
- Linear algebra textbook, section 5.1: [pages 305 to 315](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=305). Defines Ax = λx, finds eigenvalues from the characteristic polynomial, and bases for eigenspaces.
- Deep learning textbook, section 2.7: [pages 58 to 60](../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=58). The eigendecomposition, with a matrix drawn stretching the unit circle along its two eigenvectors (Figure 2.3).
- Probabilistic machine learning: an introduction, section 7.4: [pages 282 to 287](../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=282). The basics, diagonalisation, symmetric matrices, quadratic forms, whitening and the power method.
- Linear algebra textbook, section 7.2, Orthogonal diagonalization: [page 425](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=425). Theorem 7.2.2: a symmetric matrix has real eigenvalues, and eigenvectors from different eigenspaces are orthogonal.
- Linear algebra textbook, section 7.3, Example 3: [pages 437 to 438](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=437). The same 2 by 2 symmetric eigenproblem in geometry: [5, −2; −2, 8] has eigenvalues 4 and 9 with orthonormal eigenvectors (2, 1)/√5 and (−1, 2)/√5, which rotate 5x² − 4xy + 8y² = 36 onto the ellipse 4x′² + 9y′² = 36.

**Videos**

- tilestats, Eigenvectors and eigenvalues: the math step-by-step, Finding eigenvalues, 2:05 to 4:49: [watch](https://www.youtube.com/watch?v=JtcNe--fsyA&t=125s). Setting up the equation for the eigenvalues step by step. Chapter-timed.
- tilestats, Eigenvectors and eigenvalues: the math step-by-step, Calculating eigenvectors, 6:56 to 9:35: [watch](https://www.youtube.com/watch?v=JtcNe--fsyA&t=416s). Calculating the eigenvectors once the eigenvalues are known. Chapter-timed.
- 3Blue1Brown, Eigenvectors and eigenvalues (Essence of linear algebra, chapter 14), Geometric interpretation, 1:20 to 2:59: [watch](https://www.youtube.com/watch?v=PFDu9oVAE-g&t=80s). The vectors a transformation leaves on their own line. Chapter-timed.
- Stanford CS229, lecture 10, 1:03:26 to 1:05:29: [watch](https://www.youtube.com/watch?v=sUS-eTa0l6s&t=3806s). Recalls the eigendecomposition of a symmetric matrix A = UΛUᵀ with orthonormal U and eigenvalues sorted largest first, used for PCA. Caption-read.

**Our plans and chapters**

- [Symmetric eigendecomposition by hand](/home/molef/goal-setting/learning/deep-learning/diffusion-models/09-trajectory-manifold-by-hand/plans/06-symmetric-eigh-by-hand.md), deep-learning/diffusion-models/09-trajectory-manifold-by-hand, plan 06. Av = λv, the 2 by 2 characteristic polynomial, and what a symmetric positive semidefinite matrix guarantees.
- [6. Symmetric eigendecomposition, the Rayleigh quotient and spiked covariance](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l0-simple-maths/06-eigendecomposition-rayleigh-and-spiked-covariance.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L0, section 6. A symmetric matrix as a stretch along perpendicular axes, and the top eigenvector as the direction of most variance.
- [The generalised eigenvalue problem](/home/molef/goal-setting/learning/deep-learning/diffusion-models/05-poe-composition-diffusion/plans/15-generalised-eigenvalue-problem.md), deep-learning/diffusion-models/05-poe-composition-diffusion, plan 15. S_W⁻¹S_B w = λw solved by hand for two classes in two dimensions.
- [Mathematics: Linear Algebra](/home/molef/goal-setting/learning/mathematics/linear-algebra/MASTER_PLAN.md), mathematics/linear-algebra. Its third objective is eigen-structure, with a goal of eigenvalues by hand for 2 by 2 and 3 by 3 matrices and power iteration; no plan files exist under it yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after finding it through the back-of-book tables in `~/.claude/cache/book-indexes/` and the chapter tables in `Textbooks.md`. The tilestats and 3Blue1Brown chapter lists were read with cache-video-chapters.py, and those lines describe only the chapter and video titles. The CS229 row was read in its caption-read lecture map under `~/.claude/cache/captions/`. Each plan and chapter was read at its title and description. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
