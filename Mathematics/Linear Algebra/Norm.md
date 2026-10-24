---
aliases: [norm, vector norm, L2 norm, L1 norm, Euclidean norm, Manhattan norm, Lp norm, unit norm, unit vector]
link-skip: [layer norm, batch norm, group norm, RMS norm, RMSNorm, pre-norm, post-norm, add-and-norm, scipy.stats, norm.ppf, norm.cdf]
standard: vault-note v2
---

# Norm

Up: [[Linear Algebra]]

Mathematics, Linear Algebra. [[Dot Product]] gives the Euclidean norm as the square root of a vector dotted with itself.

**A norm measures a vector's size; the Euclidean norm, its length, is the square root of the sum of its squared entries.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the norm writes the rest around it.

## Where to learn this

**Norm**, the size of a vector. Also: vector norm, Euclidean norm, L2 norm, L1 norm, unit vector.

**Textbooks**

- Linear algebra textbook, section 3.2: [pages 156 to 159](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=156). The norm as length by Pythagoras (Definition 1), unit vectors and normalising (2, 2, −1) in Example 2, then distance in Rⁿ worked on two vectors in R⁴ (Example 4).
- Mathematics for machine learning, section 3.1: [pages 77 to 78](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=77). Norms in general, then the Manhattan and Euclidean norms with the set of vectors of norm 1 drawn for each (Figure 3.3).
- Deep learning textbook, section 2.5: [pages 55 to 56](../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=55). The Lp family, the L2 and squared L2 norms, the L1 norm and when machine learning prefers it, and the max norm.
- Understanding deep learning, appendix B.3.2: [page 456](../references/textbooks/machine-learning/understanding-deep-learning.pdf#page=456). The ℓp norm, the Euclidean norm as length, the ∞ norm, and the Frobenius norm of a matrix.

**Videos**

- The Organic Chemistry Tutor, Dot Product of Two Vectors, Vector magnitude, 8:21 to 13:04: [watch](https://www.youtube.com/watch?v=VzX8KJKFhlM&t=501s). The magnitude of a vector, computed on examples. Chapter-timed.
- Professor Leonard, Calculus 3 lecture 11.3, Using the Dot Product, Magnitude and dot products, 23:24 to 32:30: [watch](https://www.youtube.com/watch?v=TKlGMRghcDs&t=1404s). A vector's magnitude through its dot product with itself. Chapter-timed.

**Our plans and chapters**

- [2. The Euclidean norm](/home/molef/goal-setting/learning/deep-learning/diffusion-models/08-spectral-structure-of-the-correction/textbook/02-norm.md), deep-learning/diffusion-models/08-spectral-structure-of-the-correction, chapter 02. Row norms of 8.7 to 107.6 converted by hand into per-entry scales for a 65,536-entry vector.
- [Find a length, a unit vector and an angle from two lengths and a dot product](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/02-find-a-length-a-unit-vector.md), deep-learning/transformers, chapter 02. The length of [3, 4] and its unit vector, by hand.
- [Concentration of the norm of a high-dimensional Gaussian](/home/molef/goal-setting/learning/deep-learning/diffusion-models/05-poe-composition-diffusion/plans/11-high-dim-gaussian-norm.md), deep-learning/diffusion-models/05-poe-composition-diffusion, plan 11. Shows ‖g‖ concentrates at √D, measured at D = 10, 100 and 1000.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after finding it through the back-of-book tables in `~/.claude/cache/book-indexes/` and the chapter tables in `Textbooks.md`. The Organic Chemistry Tutor and Leonard chapter lists were read with cache-video-chapters.py, and those lines describe only the chapter and video titles; no 3Blue1Brown chapter is about the norm. Each plan and chapter was read at its title and description. "norm" alone was sampled in the learning tree (25 lines, 18 meaning a vector's norm; the other 7 were layer norm and SciPy's `norm` distribution), so it is an alias with those phrases in `link-skip`. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
