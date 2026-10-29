---
aliases: [multivariate normal, multivariate Gaussian, Gaussian, normal distribution in d dimensions, normal distribution, Gaussian distribution, bell curve, normal density, Gaussian density, univariate Gaussian, univariate normal, Gaussian random variable, normal random variable, isotropic Gaussian, spherical Gaussian, isotropic normal]
sources:
  - "Wikipedia, Multivariate normal distribution: https://en.wikipedia.org/wiki/Multivariate_normal_distribution, read 2026-10-04, CC BY-SA 4.0"
  - "Wikipedia, Normal distribution: https://en.wikipedia.org/wiki/Normal_distribution, read 2026-10-04, CC BY-SA 4.0"
  - "Wikipedia, Variance: https://en.wikipedia.org/wiki/Variance, read 2026-10-04, CC BY-SA 4.0"
  - "NumPy reference, Generator.normal: https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html, read 2026-10-04"
  - "Bradley, Nakkiran, Berthelot, Thornton, Susskind, Mechanisms of Projective Composition of Diffusion Models, ICML 2025: https://arxiv.org/abs/2502.04549"
  - "Du, Durkan, Strudel, Tenenbaum, Dieleman, Fergus, Sohl-Dickstein, Doucet, Grathwohl, Reduce, Reuse, Recycle: Compositional Generation with Energy-Based Diffusion Models and MCMC, ICML 2023: https://arxiv.org/abs/2302.11552"
  - "Petersen, Pedersen, The Matrix Cookbook, version of 15 November 2012, section 8.1.8: https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf"
---

# Multivariate Normal Distribution

Up: [[Distributions]]

Mathematics, Statistics, Distributions. Needs: the one-dimensional normal density, which the learner's [Gaussian Bowl Sketchpad](https://claude.ai/artifact/2TarMifiFoFyoB23eQFR64) lets you drag by its mean and variance.

> [!question] Test yourself
> [The diagonal Gaussian quiz](https://claude.ai/artifact/Vmd1FBg7oWwZq1onu9Jofa) covers [[Diagonal Covariance]], [[Sampling A Diagonal Gaussian]] and [[Products And Quotients Of Diagonal Gaussians]], including the paper's Figure 12 and products of Gaussian mixtures, in 36 questions. Your attempts are saved on the page.

> [!warning] Unfinished
> - Only the diagonal case has a note yet. A full covariance, with the coordinates correlated, waits for a walk that uses one.

**A multivariate normal is a bell over many coordinates at once, set by a mean vector $\mu$ and [a covariance matrix](../../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=196) $\Sigma$.** In $d$ dimensions its density at a point $x$ is

$$
\mathcal{N}(x; \mu, \Sigma) = \frac{1}{(2\pi)^{d/2} \det(\Sigma)^{1/2}} \exp\!\left( -\tfrac{1}{2} (x - \mu)^\top \Sigma^{-1} (x - \mu) \right).
$$

The second argument is always a variance, so in one dimension this is $\mathcal{N}(\mu, \sigma^2)$. *Cited:* the Wikipedia page in the sources.

The notes below take the diagonal case, where every coordinate has its own variance and no two are correlated: what its density is, how to sample it, what adding independent Gaussian draws gives, and what multiplying, dividing and raising Gaussians to powers gives.

## Where you work

- Any terminal with Python 3 and `uv`. On the PC, that is Ubuntu under WSL.
- A new empty folder. Nothing here touches a real project.

**Prepare the sandbox.**

```bash
mkdir -p ~/playground/sandbox/numpy-arrays && cd ~/playground/sandbox/numpy-arrays
uv run --no-project --with numpy python -c "import numpy; print(numpy.__version__)"
```

You should see a version number; this run printed `2.4.6`.

## Notes in this folder

Read them in this order.

- [[Diagonal Covariance]]: one variance per coordinate, so the density is a product of one-dimensional bells.
- [[Sampling A Diagonal Gaussian]]: drawing points as the mean plus the square root of the variance times standard normal noise.
- [[Sums Of Independent Gaussians]]: why independent Gaussian noises add their variances, so $a\,e_1 + b\,e_2$ is one draw of variance $a^2 + b^2$, and what reusing a draw does instead.
- [[Running Sums Of Independent Gaussians]]: the sum rule run in an empty folder, from two fresh draws to a reused draw, one draw against two and the exact sums over every outcome.
- [[Products And Quotients Of Diagonal Gaussians]]: multiplying or dividing two Gaussians by adding or subtracting precisions, and the precision-weighted mean.
- [[The Area A Product Loses]]: the area a product of densities loses, which is the overlap of the two Gaussians and has no slope.
- [[Powers Of Gaussians]]: raising Gaussians to powers and combining them, and when the result still has positive precision.

## Where to learn this

**Gaussian**, the normal distribution, in one dimension or many: N(x; μ, σ²) on a line, N(x; μ, Σ) in d dimensions, and the isotropic N(x; μ, σ²I) that every diffusion noise term uses. Also: normal distribution, normal density, bell curve, Gaussian density, multivariate Gaussian, isotropic Gaussian.

**Textbooks**

- Introduction to probability for data science, section 4.6: [pages 227 to 238](../../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=227). The one-dimensional Gaussian random variable: its density with plots of μ and σ moving and widening the curve (page 228), the standard CDF Φ (page 230), and any Gaussian's probabilities through Φ, in Python.
- Introduction to probability for data science, section 5.6: [pages 306 to 307](../../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=306). The d-dimensional Gaussian density with Σ⁻¹, its mean vector and covariance, and the diagonal covariance that independent coordinates give.
- Mathematics for machine learning, section 6.5: [pages 203 to 210](../../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=203). The univariate and multivariate densities (equations 6.62 and 6.63, page 204) drawn with 100 samples, then marginals and conditionals, products, sums and linear maps, and sampling.
- Understanding deep learning, appendix C.3: [pages 470 to 471](../../../references/textbooks/machine-learning/understanding-deep-learning.pdf#page=470). The univariate density (equation C.21) and bivariate contours for spherical, diagonal and full covariance.
- Deep learning textbook, section 3.9.3: [pages 79 to 80](../../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=79). The density with its two parameters, the bell curve drawn with its peak and inflection points, and why the normal is the default choice.
- Computer vision textbook, sections 5 and 5.1, Types of covariance matrix: [pages 71 to 72](../../../references/textbooks/computer-vision/computer-vision-textbook.pdf#page=71). Spherical, diagonal and full covariances side by side (equation 5.3, figure 5.1): a spherical covariance is a multiple of the identity, its coordinates are independent, and its contours are circles.
- Probabilistic machine learning: an introduction, section 3.2.1: [pages 106 to 107](../../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=106). Surface and contour plots of full, diagonal and spherical 2d Gaussians (figures 3.5 and 3.6), and the isotropic covariance Σ = σ²I with its one free parameter σ².

**Videos**

- StatQuest, The Normal Distribution, Clearly Explained, 0:00 to 3:27: [watch](https://www.youtube.com/watch?v=rzFX5NWojp0&t=0s). The bell-shaped curve and what its mean and standard deviation set, in the video's opening chapter. Chapter-timed.
- StatQuest, The Main Ideas behind Probability Distributions, 2:15 to 5:14: [watch](https://www.youtube.com/watch?v=oI3hZJqXJuc&t=135s). A curve as a distribution, where probability is the area under it over an interval and never its height at a point. Chapter-timed, from the video lessons index.
- CS229 lecture 3, 13:36 to 18:36: [watch](https://www.youtube.com/watch?v=uJF_gL3jhxI&t=816s). Takes the Gaussian density apart: the normalising constant, the squared distance over 2σ², σ setting the width, and 99.7% of the mass within 3σ. Caption-read.
- CS229 lecture 5, 12:09 to 16:18: [watch](https://www.youtube.com/watch?v=zRdE8A4UZes&t=729s). Defines the multivariate Gaussian N(μ, Σ) and reads its exponent as a distance scaled by Σ⁻¹. Caption-read.

**Our plans and chapters**

- [Chapter 2: Read a density as area and draw a Gaussian from its covariance](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/02-densities-and-the-gaussian.md), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 02. The Gaussian formula from one dimension to many, read as area and drawn from its covariance.
- [Densities, and the Gaussian](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/03-densities-and-the-gaussian.md), the same journey, plan 03. The sitting that teaches densities over images and the Gaussian that every noise term uses.
- [Read a covariance as an ellipse](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/27-two-d-gaussian.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 27. The 2D Gaussian's covariance drawn as an ellipse, worked on two-pixel images.
- [Concentration of the norm of a high-dimensional Gaussian](/home/molef/goal-setting/learning/deep-learning/diffusion-models/05-poe-composition-diffusion/plans/11-high-dim-gaussian-norm.md), deep-learning/diffusion-models/05-poe-composition-diffusion, plan 11. Shows by hand that a standard isotropic Gaussian draw g has ‖g‖ near √D, then measures the spread narrowing at D = 10, 100 and 1000.

> [!note]- How this was checked
> `toy.py` is the learner's own file, copied byte for byte from the walk's playground. `clouds.py` and `overlap.py` are the walk's answer keys, copied unchanged from `checks/` in the journey's `sources/mechanisms-of-projective-composition/`; their outputs matched `checks/clouds.out` and `checks/overlap.out` exactly. `samples.py` matched `checks/samples.out` exactly, and `compose.py`, which prints more fields, agreed with every composed mean and variance in `checks/compose.out`. The learner's own `samples.py` in the playground still draws from `np.random`, so its printed numbers differ slightly from the seed-0 numbers here.
>
> The sketchpad values (2.0, 0.0293, 0.1995) come from the learner's screenshots of the Gaussian Bowl Sketchpad and match `gauss.py`'s output to the digits shown. The three clouds' values match plan 13 and the walk's answer key, `checks/toy.py` in the journey's `sources/mechanisms-of-projective-composition/`.
>
> The four terminal pictures were rendered from the captured text by a script in DejaVu Sans Mono, never drawn. The cloud picture is `clouds.py`'s own saved figure.
>
> The paper's Figure 12, left panel, is the authors' own image file `eg1.png`, copied byte for byte from the arXiv source package (`paper/source/figures/` in the journey's staged sources) into `references/`, and opened before filing. Its caption is the LaTeX caption in `src/appendix_notes.tex`, with markup removed and its cross-references written as the PDF prints them; the figure number is the one printed in `2502.04549.pdf`, version 3. Equation (17) was read in the same file, lines 105 to 111. The right panel was left out because its clean distributions flip each coordinate like a coin, equation (18), so once noised they are Gaussian mixtures rather than single Gaussians. The paper is under arXiv's non-exclusive distribution licence, which does not grant a reuse licence; the copy is here for study, with citation on the embed.
>
> References: [Multivariate normal distribution](https://en.wikipedia.org/wiki/Multivariate_normal_distribution), [Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution) and [Variance](https://en.wikipedia.org/wiki/Variance) on Wikipedia, CC BY-SA 4.0; [Generator.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html) and [scipy.stats.multivariate_normal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.multivariate_normal.html), BSD 3-Clause; and [the paper on arXiv](https://arxiv.org/abs/2502.04549). Each answered 200 on 2026-10-04. [Du et al. on arXiv](https://arxiv.org/abs/2302.11552) and [the Matrix Cookbook](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf) each answered 200 on 2026-10-13. No tldr-pages entry covers this. The sketchpad link is the learner's own private artifact and was not fetched.
>
> The card under Where to learn this was checked on 2026-10-24: every textbook page range was read with pdftotext, the two CS229 rows were read in their caption-read lecture map under `~/.claude/cache/captions/` and paraphrase the map, the StatQuest distributions row is copied from the video lessons index section "The Gaussian density and its formula", and the StatQuest normal distribution chapter list was read with `cache-video-chapters.py`, so its line describes only the video's title and chapter. Each plan and chapter was read at its title and description. Pattern recognition and machine learning section 2.3 (from PDF page 97) also teaches the Gaussian in full and has no line only to keep the list short.
>
> The isotropic lines were added on 2026-10-28. The computer vision textbook's pages 71 to 72 and Probabilistic machine learning's pages 106 to 107 were read with pdftotext, found through the shelf index's chapter title "5 The normal distribution" and Probabilistic machine learning's back-of-book entry "isotropic covariance matrix". Plan 11 was read at its title and description. The paper shelf has no paper that teaches the Gaussian itself, and `find-figures.py` found only a figure of a bridge between two Gaussians, which does not teach the density, so the card has no Papers or Figures group.
