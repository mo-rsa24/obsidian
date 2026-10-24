---
aliases: [manifold, manifold hypothesis, data manifold, manifold assumption, manifold learning, low-dimensional manifold]
standard: vault-note v2
---

# Manifold

Up: [[Mathematics]]

Mathematics. Machine learning uses it through the manifold hypothesis, and an [[Encoder-Decoder]] with a nonlinear decoder learns one.

**A manifold is a space that looks flat close up around every point, like the surface of the earth; the manifold hypothesis says real data such as images fill only a thin, low-dimensional manifold inside their huge pixel space.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches manifolds writes the rest around it.
> - The placement is unsure. The two best places are `Mathematics/`, for the geometric object that more than one field uses, and `Artificial Intelligence/Deep Learning/`, for the manifold hypothesis that the learning tree uses it for.

## Where to learn this

**Manifold**, and the manifold hypothesis about data. Also: manifold hypothesis, data manifold, manifold assumption, manifold learning.

**Textbooks**

- Probabilistic machine learning: an introduction, sections 20.4.1 to 20.4.2: [pages 735 to 737](references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=735). Works a concrete case: a 64 × 57 image of the digit 6 is one point in a 3,648-dimensional space, random points there look nothing like a digit, and the images made by varying the digit's shape trace a manifold of intrinsic dimension 2.
- Deep learning textbook, section 5.11.3: [pages 177 to 179](references/textbooks/machine-learning/deep-learning-textbook.pdf#page=177). A manifold as a connected region that looks locally Euclidean, data lying near a one-dimensional manifold in two dimensions (figure 5.11), and the evidence for the manifold hypothesis, such as uniformly random pixels never looking like a natural image.
- The little book of generative AI foundations, section 1.5.3: [page 30](references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=30). A linear autoencoder's reconstructions fill one flat subspace, while a nonlinear decoder's reconstructions can form a curved low-dimensional manifold.

**Our plans and chapters**

- [The manifold hypothesis with a number attached](/home/molef/goal-setting/learning/deep-learning/diffusion-models/05-poe-composition-diffusion/plans/48-manifold-hypothesis-intrinsic-dimension.md), deep-learning/diffusion-models/05-poe-composition-diffusion, plan 48. Estimates the intrinsic dimension of a real image dataset in code, after predicting roughly what it should be.
- [Intrinsic dimension and how to measure it](/home/molef/goal-setting/learning/deep-learning/diffusion-models/06-diffusion-speciation-dynamics/plans/03-manifold-and-the-later-transition/plans/05-intrinsic-dimension.md), deep-learning/diffusion-models/06-diffusion-speciation-dynamics, plan 05 of the manifold scope. The same measurement inside a more deeply scaffolded sequence.
- [Tangent space, normal space, and splitting a displacement](/home/molef/goal-setting/learning/deep-learning/diffusion-models/06-diffusion-speciation-dynamics/plans/03-manifold-and-the-later-transition/plans/04-tangent-and-normal-split.md), the same scope, plan 04. A displacement split into the part along the manifold and the part off it.
- [The Manifold and the Later Transition](/home/molef/goal-setting/learning/deep-learning/diffusion-models/06-diffusion-speciation-dynamics/plans/03-manifold-and-the-later-transition/MASTER_PLAN.md), the same scope. Turns a diffusion sample's commitment to a class into geometry: intrinsic dimension and one sub-manifold per class.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, first found through the books' back-of-book indexes ("manifold", "manifold hypothesis") and the shelf index's chapter tables. The Deep learning textbook's section 14.6 on learning manifolds with autoencoders (from PDF page 532) and Understanding deep learning's manifold precision and recall for evaluating generative models (PDF page 287) have no line, to keep the list to the idea itself. There is no Videos group: no row in the four timed lecture maps, no section of the video lessons index and no upload title in the cached channel lists teaches the manifold or the manifold hypothesis. Each plan was read at its title and opening lines. Bare "manifold" is an alias because outside link paths every sampled use in the learning tree means the geometric object or the data manifold. A script then opened every link and confirmed the file exists and the page is inside the PDF.
