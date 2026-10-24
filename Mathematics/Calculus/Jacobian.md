---
aliases: [Jacobian, Jacobian matrix, Jacobian determinant]
standard: vault-note v2
---

# Jacobian

Up: [[Calculus]]

Mathematics, Calculus. [[Gradient]] is the one-output case, and [[Chain Rule]] multiplies Jacobians along a composition.

**The Jacobian of a function from n inputs to m outputs is the m by n matrix of all its partial derivatives, and its determinant measures how much the function scales area or volume.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the Jacobian writes the rest around it.

## Where to learn this

**Jacobian**, the matrix of partial derivatives. Also: Jacobian matrix, Jacobian determinant.

**Textbooks**

- Mathematics for machine learning, section 5.3: [pages 155 to 160](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=155). Gradients of vector-valued functions as the Jacobian, then the Jacobian determinant as an area scale worked to |det J| = 3 (page 158).
- Calculus textbook, section 14.7: [pages 1082 to 1091](../references/textbooks/calculus/calculus-textbook.pdf#page=1082). The Jacobian of a change of variables in two variables (Definition 14.7.1, page 1086) and three (Definition 14.7.3, page 1090), and why it scales area in a double integral.
- Deep learning textbook, section 4.3.1: [pages 102 to 103](../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=102). The Jacobian matrix J with entries ∂fᵢ/∂xⱼ, and the Hessian as the Jacobian of the gradient.
- Probabilistic machine learning: an introduction, section 7.8.5: [page 299](../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=299). The Jacobian inside a short chapter on matrix calculus, after directional and total derivatives.

**Videos**

- Stanford CS229, lecture 8, 42:49 to 48:29: [watch](https://www.youtube.com/watch?v=ne2ngVAoMG8&t=2569s). Derives the backward rule for u = Wz + b: the Jacobian entries are ∂uⱼ/∂zᵢ = Wⱼᵢ, so ∂J/∂z = Wᵀ ∂J/∂u. Caption-read.
- Stanford CS231n, lecture 4, 1:04:33 to 1:11:16: [watch](https://www.youtube.com/watch?v=25zD5qJHYsk&t=3873s). Scalar derivative, gradient vector and Jacobian matrix side by side, and ReLU's diagonal Jacobian that is never built. Caption-read.
- Stanford CS229, lecture 8, 55:50 to 58:57: [watch](https://www.youtube.com/watch?v=ne2ngVAoMG8&t=3350s). An elementwise activation has a diagonal Jacobian with σ′(zᵢ) on the diagonal. Caption-read.
- Professor Leonard, Calculus 3 lecture 14.8, How to Change Variables in Multiple Integrals (Using the Jacobian), 0:00 to 1:40:05: [watch](https://www.youtube.com/watch?v=VVPu5fWssPg&t=0s). A full lecture on the Jacobian of a change of variables in a multiple integral. Whole video.

**Our plans and chapters**

- [1. Log-sum-exp and the softmax gradient](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l0-simple-maths/01-log-sum-exp-and-the-softmax-gradient.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L0, section 1. The softmax Jacobian diag(p) − ppᵀ, derived inside a worked example.
- [9. Hamiltonian dynamics, and what momentum buys](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/09-hamiltonian-dynamics-and-what-momentum-buys.md), the same journey, volume L3, section 9. Each leapfrog shear has Jacobian determinant 1, so a full step preserves volume.
- [Spectrum of the score Jacobian](/home/molef/goal-setting/learning/deep-learning/diffusion-models/05-poe-composition-diffusion/plans/56-score-jacobian-spectrum.md), deep-learning/diffusion-models/05-poe-composition-diffusion, plan 56. The eigenvalues of a learned score's Jacobian, computed.
- [Mathematics: Calculus](/home/molef/goal-setting/learning/mathematics/calculus/MASTER_PLAN.md), mathematics/calculus. Its third goal computes the gradient, Jacobian and Hessian by hand and by finite differences; no plan files exist under it yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after finding it through the back-of-book tables in `~/.claude/cache/book-indexes/` and the chapter tables in `Textbooks.md`; the calculus textbook's section 14.7 starts on PDF page 1082, one earlier than its chapter table says. The CS229 and CS231n rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`. Leonard's 14.8 has no chapter list and is cited whole, read with cache-video-chapters.py. No 3Blue1Brown video on the Jacobian is in the cached upload list. Each plan and chapter was read at its title and description. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
