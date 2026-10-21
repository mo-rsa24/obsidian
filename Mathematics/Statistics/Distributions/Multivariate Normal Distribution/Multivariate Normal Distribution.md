---
aliases: [multivariate normal, multivariate Gaussian, Gaussian, normal distribution in d dimensions]
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
- [[Products And Quotients Of Diagonal Gaussians]]: multiplying or dividing two Gaussians by adding or subtracting precisions, and the precision-weighted mean.
- [[The Area A Product Loses]]: the area a product of densities loses, which is the overlap of the two Gaussians and has no slope.
- [[Powers Of Gaussians]]: raising Gaussians to powers and combining them, and when the result still has positive precision.

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
