---
aliases: [normaliser, normalizer, normalising constant, normalizing constant]
standard: vault-note v2
---

# Normaliser

Up: [[Distributions]]

Mathematics, Statistics, Distributions. Needs: [[Probability Density Function]]. The Gaussian's own normaliser is worked in [[The Front Factor Of A Gaussian Density]].

**A normaliser is the one number you divide a function by so that its total area (or sum) comes out as 1, which turns a bump of any size into a density.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the normaliser writes the rest around it.

## Where to learn this

**Normaliser**, the constant that rescales a function so its total area or sum is 1: to normalise is to scale to a standard size, here a total of 1, and the normaliser is the number you divide by. Also: normaliser, normalizer, normalising constant, normalizing constant.

**Textbooks**

- Deep learning textbook, section 16.2.3: [pages 584 to 585](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=584). Works the normaliser on one scalar: φ(x) = x² has a divergent Z and defines no distribution, while exp(−βx²) normalises to a Gaussian only for positive β.
- Probabilistic machine learning: an introduction, section 2.6: [page 82](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=82). The Gaussian density's factor 1/√(2πσ²) is "the normalization constant needed to ensure the density integrates to 1", with Exercise 2.12 on page 99 asking for its derivation.
- Probabilistic machine learning: an introduction, section 3.2: [page 105](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=105). The multivariate Gaussian's Z = (2π)^(D/2) |Σ|^(1/2) "just ensures that the pdf integrates to 1".
- Pattern recognition and machine learning, section 4.2: [page 216](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=216). The softmax, called the normalized exponential, divides each exponential by their sum so K positive numbers add to 1. This is the same division as dividing a bump by its area, with a sum in place of an integral.
- Pattern recognition and machine learning, section 11.6: [page 570](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=570). Writes p(z) = exp(−E(z))/Z_E and says a sampler needs the form only up to the constant, which is needed afterwards only to compare models.

**Videos**

- Organic Chemistry Tutor, Probability Density Functions, 0:52 to 3:39: [watch](https://www.youtube.com/watch?v=QKA4HNEw3aY&t=52s). Checks that a function is a density by integrating it and getting 1. Chapter-timed, from the video lessons index.
- Stanford CS229, lecture 3, 13:36 to 18:36: [watch](https://www.youtube.com/watch?v=uJF_gL3jhxI&t=816s). Takes the Gaussian density apart, the normalising constant first, then the squared distance and σ as the width. Caption-read.
- Stanford CS236, lecture 11, 6:45 to 15:31: [watch](https://www.youtube.com/watch?v=m61KiAMCJ5Q&t=405s). Why a probability model must be non-negative and integrate to 1. Chapter-timed, from the video lessons index.
- Stanford CME296, lecture 2, 4:44 to 14:26: [watch](https://www.youtube.com/watch?v=_WaR2fjZpEQ&t=284s). Defines the score and shows the normaliser Z drops out of it, so the direction is unchanged. Caption-read.

**Our plans and chapters**

- [Chapter 2: Read a density as area and draw a Gaussian from its covariance](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/02-densities-and-the-gaussian.md#23-the-gaussian-formula-from-1d-to-multivariate), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 2, section 2.3, "The normaliser, taken apart". The bump e^(−x²/(2σ²)) always peaks at 1 and has area σ√(2π) (1.2533, 2.5066 and 5.0133 at σ = 0.5, 1 and 2), so the density divides by it and the peak falls to 0.7979, 0.3989 and 0.1995.
- [The Front Factor Of A Gaussian Density](../../Calculus/Integration/The%20Front%20Factor%20Of%20A%20Gaussian%20Density.md). The same division as a vault note: one over the area of the bare bell, 1.2533 at width 0.5 and 5.0133 at width 2.
- [Gaussian Integral](../../Calculus/Integration/Gaussian%20Integral.md). The area under e^(−x²), √π = 1.772454, which is the number behind every Gaussian normaliser.
- [The Area A Product Loses](Multivariate%20Normal%20Distribution/The%20Area%20A%20Product%20Loses.md). Two multiplied densities leave an area of 0.075126, so the product needs its own normaliser, and the score does not change when it is divided out.
- [Why The Normaliser Has No Slope In X](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Composition/Why%20The%20Normaliser%20Has%20No%20Slope%20In%20X.md). The normaliser is one number for each β, so its slope in x is 0 and it drops out of the score.
- [Energy: p proportional to exp(-E)/Z, and why the score never sees Z](/home/molef/goal-setting/learning/deep-learning/diffusion-models/02-sampler-correctors-for-composition/plans/04-energy-and-the-missing-normaliser.md), deep-learning/diffusion-models/02-sampler-correctors-for-composition, plan 04. The energy form of a density and why the missing normaliser does not matter to a sampler that follows the score.

**Scenes**

- [Gaussian bowl sketchpad, One hump, three handles](https://claude.ai/artifact/2TarMifiFoFyoB23eQFR64#bell-1d). The peak 1/√(2πσ²) with the same σ² under the root and inside the exponent, the root drawn in blue as the normaliser, so making σ² four times bigger halves the peak from 0.3989 to 0.1995.
- [Gaussian bowl sketchpad, The 1D bowl you can widen](https://claude.ai/artifact/2TarMifiFoFyoB23eQFR64#bowl-1d). The log of the bell split into a blue constant, which is the log of the normaliser, and an orange quadratic bowl; going from σ² = 1 to 4 drops the constant by 0.6931 while the bowl term shrinks from −2 to −0.5.
- [Gaussian bowl sketchpad, A surface you can turn](https://claude.ai/artifact/2TarMifiFoFyoB23eQFR64#surface-2d). The density as a surface with the normaliser included, the determinant of Σ and the normaliser printed live, the rings on the floor as level sets, and the height at the centre dropping by a factor of √2, from 0.0796 to 0.0563, when the determinant doubles.
- [The height-and-area walk, Narrower means taller](https://claude.ai/code/artifact/72caec6e-b6a2-495e-86d3-b6e23c2d29c7). Frame 3: dragging σ in the formula while the peak 1/(σ√2π) passes 1 below σ = 0.3989 and the area stays 1.
- [The two-bump gradient walk, A log turns slope into ratio](https://claude.ai/code/artifact/4bb4eef7-4d8f-4cca-b4ef-0b5259338648). Frame 5: the standard normal at (3, 4) with a constant multiplier c, which is what a missing normaliser is, dragged from 0.001 to 1e6 while the log-slope stays (−3, −4).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-10. Each textbook page was read with pdftotext after searching the shelf for the word and for the worked-example shape "normalise to one", and the quoted phrases are printed on the page cited. The video times are rows of the lecture maps and of the video lessons index, and the lecture-map rows were read from the captions. The vault notes and the plan were read at their opening paragraph or title. No Papers group: the shelf papers that mention an unnormalised density (the energy-based composition paper, the product-of-experts paper) state it in passing and none teaches the normaliser. The words are the normaliser's own; "partition function" is not an alias, since it is the statistical physics name and the lecture and textbook lines above already carry it where they use it.
