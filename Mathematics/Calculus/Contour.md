---
aliases: [contour, contours, contour line, level set]
link-skip: [active contour, contour integral, contour detection, contour tracing, contour of the]
standard: vault-note v2
---

# Contour

Up: [[Calculus]]

Mathematics, Calculus. Needs: [[Gradient]]. For a density, a contour is every point of equal density, so [[Probability Density Function]] and [[Multivariate Normal Distribution]] are where the word is used most.

**A contour is a line along which a function has one height, the way a map's contour line follows a hillside at one elevation; for a density, every point on it has the same density.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the contour writes the rest around it.

## Where to learn this

**Contour**, a line of constant height: on a map it outlines a hill at one elevation, and for a function f(x, y) it is the set of points where f equals one value k, also called a level set. Also: contour, contours, contour line, level set.

**Textbooks**

- Calculus textbook, section 13.1: [pages 933 to 934](../references/textbooks/calculus/calculus-textbook.pdf#page=933). Cuts the surface z = f(x, y) with the plane z = k to define a level curve, then works two: y² − x² = k gives hyperbolas (crossing lines at k = 0) and 4x² + y² = k gives ellipses.
- Pattern recognition and machine learning, section 2.3: [page 103](../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=103). Figure 2.8 draws the contours of a 2D Gaussian for three covariances: tilted ellipses for a general one, axis-aligned ellipses for a diagonal one and concentric circles for the identity.
- Probabilistic machine learning: an introduction, section 3.2.2: [pages 107 to 108](../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=107). Shows the level sets of a Gaussian's log probability are sets of constant Mahalanobis distance, and with the covariance's eigendecomposition that they are ellipses, the eigenvectors giving the orientation and the eigenvalues the elongation.
- Calculus textbook, section 13.6: [page 989](../references/textbooks/calculus/calculus-textbook.pdf#page=989). Gradients are normal to level curves: at a point on the curve f(x, y) = c the gradient is perpendicular to the curve, so on a contour map it points across the contour lines.

**Videos**

- Stanford CS229, lecture 5, 16:18 to 21:20: [watch](https://www.youtube.com/watch?v=zRdE8A4UZes&t=978s). Draws 2D Gaussians as surfaces and as contour lines: identity covariance, diagonal covariances that stretch the axes, and full covariances that rotate the ellipse. Caption-read.
- Stanford CS229, lecture 2, 1:05:25 to 1:07:25: [watch](https://www.youtube.com/watch?v=cmNIMjPYdgM&t=3925s). Draws the contour lines of a quadratic loss and follows gradient descent across them: straight to the minimum for the full batch, a zigzag for SGD. Caption-read.

**Papers**

- Chan 2024, Tutorial on diffusion models for imaging and vision: [page 49](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=49). Figure 3.6 draws the score's arrows over the contour map of a two-Gaussian mixture, so each arrow shows which way a point travels across the contours towards a basin.

**Our plans and chapters**

- [Chapter 2: Read a density as area and draw a Gaussian from its covariance](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/02-densities-and-the-gaussian.md#24-from-covariance-to-contours), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 2, section 2.4. Turns a density level (a fraction r of the peak) into an ellipse: dividing by the peak cancels the normaliser, taking logs gives (x − μ)ᵀ Σ⁻¹ (x − μ) = k with k = −2 log r, and the semi-axes are √(kλ) along the eigenvectors.
- [The gradient field, drawn](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/06-the-gradient-field-drawn.md), deep-learning/diffusion-models/01-poe-derivation-foundations, plan 06. Draws the contour map of a two-bump function at levels 0.1 to 0.9, where one line is one set of inputs with the same value, then adds the gradient arrows and checks they meet the lines at right angles.

**Scenes**

- [Gaussian bowl sketchpad, The same density as rings](https://claude.ai/artifact/2TarMifiFoFyoB23eQFR64#rings-2d). The 2D density seen from above as rings, one ring for each whole value of the cost uᵀΣ⁻¹u from 1 outwards, which tilt and stretch as Σ and ρ are dragged.
- [Gaussian bowl sketchpad, A surface you can turn](https://claude.ai/artifact/2TarMifiFoFyoB23eQFR64#surface-2d). The density as a surface with the normaliser included, the determinant of Σ and the normaliser printed live, the rings on the floor as level sets, and the height at the centre dropping by a factor of √2, from 0.0796 to 0.0563, when the determinant doubles.
- [The height-and-area walk, Covariance sets the shape](https://claude.ai/code/artifact/72caec6e-b6a2-495e-86d3-b6e23c2d29c7). Frame 4: contours at 0.6, 0.3 and 0.1 of the peak, ellipses that turn to Σ's eigenvectors and stretch by √(kλ) as the entries of Σ are dragged.
- [The two-bump gradient walk, Every arrow leaves its line square](https://claude.ai/code/artifact/4bb4eef7-4d8f-4cca-b4ef-0b5259338648). Frame 2: the contour through a draggable dot with its tangent and its gradient, showing the gradient meets the contour line at a right angle.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-10. Each textbook page was read with pdftotext after the gather script and the worked-example catalogue named it, and the sentence each line describes is printed on that page. The two CS229 rows are lecture-map rows read from the captions, with the times printed as the map gives them. The Chan page and the two learning-tree files were read at the cited passage and heading. "Contour" alone is an ordinary English word (the outline of a shape), and the three learning-tree lines that use it outside the diffusion journeys all mean a level curve of a function; the link-skip list keeps the contour integral and the active contour of image segmentation plain. No Figures group: the figure index holds no figure of a contour.
