---
aliases: [determinant, det]
standard: vault-note v2
---

# Determinant

Up: [[Linear Algebra]]

Mathematics, Linear Algebra. Needs: [[Matrix]]. The determinant of a function's matrix of slopes is the [[Jacobian]]'s determinant, and a Gaussian's density divides by the square root of its covariance's determinant ([[Multivariate Normal Distribution]]).

**The determinant of a square matrix is the factor by which it scales area (in 2D) or volume (in 3D): 3 means it triples them, a negative sign means it flips orientation, and 0 means it flattens space and has no inverse.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the determinant writes the rest around it.

## Where to learn this

**Determinant**, the single number that settles what a square matrix does to space: the factor by which it scales area or volume, and zero when it squashes space flat. For a covariance matrix it scales the unit circle's area to the covariance ellipse's, after a square root. Also: determinant, det.

**Textbooks**

- Mathematics for machine learning, section 4.1: [pages 107 to 108](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=107). Example 4.2 reads the determinant as the signed volume of the parallelepiped the columns span: a 2 by 2 case as a parallelogram's area, with area 0 when the columns are dependent, then three columns in R³ worked to V = |det A| = 186.
- Linear algebra textbook, section 3.5: [page 192](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=192). Theorem 3.5.4: the absolute value of a 2 by 2 determinant is the area of the parallelogram the two rows span, and of a 3 by 3 determinant the volume of the parallelepiped.
- Deep learning textbook, section 2.11: [page 63](../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=63). The determinant is the product of the eigenvalues and its absolute value measures how much multiplying by the matrix expands or contracts space: 0 loses all volume along some direction, 1 preserves volume.
- Pattern classification, section 2.5.2: [page 54](../references/textbooks/machine-learning/pattern-classification.pdf#page=54). The contours of a Gaussian are hyperellipsoids whose volume is V = V_d |Σ|^(1/2) r^d, so the covariance's determinant sets how much volume the density spreads over.
- Algebra handbook, matrices, inverse of a 2 by 2 matrix: [page 93](../references/textbooks/algebra/algebra-handbook.pdf#page=93). The 2 by 2 determinant ad − bc, the rule that a matrix has an inverse only when its determinant is not 0, and a worked inverse that divides by the determinant.

**Our plans and chapters**

- [Chapter 2: Read a density as area and draw a Gaussian from its covariance](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/02-densities-and-the-gaussian.md#23-the-gaussian-formula-from-1d-to-multivariate), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 2, section 2.3. Uses det(Σ) in the Gaussian normaliser: σ² in one dimension, ab for diag(a, b), and worked example 2.3b computes det = 1 − 0.64 = 0.36 for a correlated 2 by 2 covariance before inverting it.
- [Jacobian](../Calculus/Jacobian.md#where-to-learn-this). The vault card for the determinant of a function's matrix of slopes, which gives how a change of variables scales area or volume.

**Scenes**

- [Gaussian bowl sketchpad, A surface you can turn](https://claude.ai/artifact/2TarMifiFoFyoB23eQFR64#surface-2d). The density as a surface with the normaliser included, the determinant of Σ and the normaliser printed live, the rings on the floor as level sets, and the height at the centre dropping by a factor of √2, from 0.0796 to 0.0563, when the determinant doubles.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-10. Each textbook page was read with pdftotext after the shelf index's chapter tables and the worked-example catalogue named it, and the statement each line gives is printed on that page; the 186 and the Theorem 3.5.4 wording were read from pages 108 and 192. The chapter 2 section was read at its derivation and worked example 2.3b. No Videos group: the lecture maps and the video lessons index hold no segment on the determinant, and the 3Blue1Brown determinant video has no cached chapter list on this machine, so no time could be confirmed. No Papers group: no shelf paper teaches the determinant. The bare word "Jacobian determinant" is the alias of the [[Jacobian]] card, so it is not repeated here.
