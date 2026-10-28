# Textbooks

The reference shelf for the moment a derivation stalls on a fundamental: a rule for logs, a trig
identity, a matrix derivative. Each book below lists its chapters with the PDF page each one starts
on, so a link can open the book at the right page.

## How a book is named and filed

**One folder per subject.** `general/` holds handbooks that span several subjects. A book goes in the
subject it mostly teaches, even when the shelf holds only one book on that subject, so that a link
written today still resolves when a second book arrives.

**Lowercase words joined by hyphens, named for what the file covers.** `algebra-handbook.pdf`,
`matrix-vector-multiplication.pdf`. No spaces, capitals, underscores or `&`, so a path works unquoted in
the shell and unescaped in a markdown link. Author and version live in this file, never in the name.

**A new book gets a section here when it lands**, with its chapter table, before anything links to it.

## How to link to a page

Add `#page=N` to the path, where N is the PDF's own page count from its first page. Chrome, Edge,
Firefox and Obsidian's built-in PDF viewer open the file at that page.

The shelf lives in the vault at `$HOME/Obsidian/Mathematics/references/textbooks/`.

**From a vault note**, link by filename. Every filename on the shelf is unique, so Obsidian finds it
wherever the note sits, and the text after `|` is what the reader sees:

```markdown
the [[algebra-handbook.pdf#page=109|exponent rules]]
```

**From the learning tree** (a journey plan, a source topic), Obsidian's links do not resolve, so the
link is the absolute path to the file:

```markdown
the [exponent rules](file:///home/molef/Obsidian/Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=109)
```

Written as plain text, the path is
`$HOME/Obsidian/Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=109`.

**Printed page numbers and PDF page numbers.** For the handbooks and own notes, the number printed on
the page equals the PDF page number. The GED handbook binds three handbooks together, each with its
own printed numbering, so its table gives PDF pages only. The published textbooks and lecture notes
start their printed numbering after front matter, and each one's section states its offset. Every
table on this page gives PDF pages.

## Pages looked up most

| Looking for | Book | PDF page |
| --- | --- | --- |
| exponent rules (product, quotient, power, zero and negative exponents) | [algebra handbook](algebra/algebra-handbook.pdf#page=109) | 109 |
| logarithm rules | [algebra handbook](algebra/algebra-handbook.pdf#page=110) | 110 |
| e and the natural log | [algebra handbook](algebra/algebra-handbook.pdf#page=111) | 111 |
| local linear approximation: f(x) ≈ f(x₀) + f′(x₀)(x − x₀), which at x₀ = 0 gives ln(1 − p) ≈ −p (section 3.5, definition with worked examples) | [calculus textbook](calculus/calculus-textbook.pdf#page=236) | 236 |
| converting between exponential and log form | [algebra handbook](algebra/algebra-handbook.pdf#page=113) | 113 |
| expanding and condensing log expressions | [algebra handbook](algebra/algebra-handbook.pdf#page=114) | 114 |
| what exponential curves look like | [algebra handbook](algebra/algebra-handbook.pdf#page=118) | 118 |
| what log curves look like | [algebra handbook](algebra/algebra-handbook.pdf#page=122) | 122 |
| solving exponential and log equations | [algebra handbook](algebra/algebra-handbook.pdf#page=125) | 125 |
| matrix derivatives | [matrix cookbook](linear-algebra/matrix-cookbook.pdf#page=8) | 8 |
| Gaussian identities | [matrix cookbook](linear-algebra/matrix-cookbook.pdf#page=40) | 40 |
| the area under a product of two Gaussian densities | [matrix cookbook](linear-algebra/matrix-cookbook.pdf#page=42) | 42 |
| completing the square | [algebra handbook](algebra/algebra-handbook.pdf#page=74) | 74 |
| matrix multiplication | [algebra handbook](algebra/algebra-handbook.pdf#page=91) | 91 |
| summation notation (Σ) and its properties | [algebra handbook](algebra/algebra-handbook.pdf#page=165) | 165 |
| square root and radical rules (√(a/b) = √a/√b, √a = a^½) | [algebra handbook](algebra/algebra-handbook.pdf#page=86) | 86 |
| the transpose of a matrix (Definition 7, rows become columns) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=49) | 49 |
| properties of the transpose, (AB)ᵀ = BᵀAᵀ (Theorem 1.4.8) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=62) | 62 |
| the dot product, multiply components and add (Definition 4) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=161) | 161 |
| convex combination: nonnegative weights summing to 1 | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=712) | 712 |
| matrix times vector, yᵢ = Σⱼ Aᵢⱼxⱼ | [matrix-vector multiplication](linear-algebra/matrix-vector-multiplication.pdf#page=1) | 1 |
| variance of a sum of random variables, V[x + y] (6.48) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=199) | 199 |
| gradient of a quadratic form | [matrix cookbook](linear-algebra/matrix-cookbook.pdf#page=11) | 11 |
| conditional Gaussian; a linear combination of Gaussians, so variances add | [matrix cookbook](linear-algebra/matrix-cookbook.pdf#page=41) | 41 |
| expectation of linear forms | [matrix cookbook](linear-algebra/matrix-cookbook.pdf#page=35) | 35 |
| the Jacobian as the m by n matrix of first-order partial derivatives (Definition 5.6) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=156) | 156 |
| gradients of matrices, and of vector-valued functions | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=155) | 155 |
| sum rule and marginalisation; product rule and Bayes' theorem | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=190) | 190 |
| the marginal likelihood (evidence) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=192) | 192 |
| mean, expected value, variance | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=193) | 193 |
| covariance (Definition 6.5) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=196) | 196 |
| the Gaussian distribution | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=203) | 203 |
| the univariate and multivariate Gaussian density formulas (6.62, 6.63) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=204) | 204 |
| change of variables for densities | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=220) | 220 |
| what a vector field is (Definition 15.1.1) | [calculus textbook](calculus/calculus-textbook.pdf#page=1109) | 1109 |
| gradient fields: a field that is the gradient of a function | [calculus textbook](calculus/calculus-textbook.pdf#page=1111) | 1111 |
| expectation (discrete): the definition, why it is the dataset average, with figure (intuition) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=141) | 141 |
| expectation (continuous): the integral definition with uniform and exponential worked examples | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=196) | 196 |
| conditional expectation: the definition for discrete and continuous variables | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=291) | 291 |
| conditional expectation: law of total expectation, with proof | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=292) | 292 |
| conditional expectation: E[X] = E[E[X|Y]] with a worked two-class example | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=293) | 293 |
| variance (continuous): the definition and the E[X²] − μ² shortcut, with proof | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=200) | 200 |
| variance: worked example for the uniform distribution | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=201) | 201 |
| variance (discrete): Var[X] = E[X²] − E[X]², Var[cX] = c²Var[X] and Var[X + c] = Var[X] (Theorem 3.5, with proof) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=151) | 151 |
| the Bernoulli random variable: two states 1 and 0 with probabilities p and 1 − p (Definition 3.8) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=153) | 153 |
| covariance: the definition, and Cov(X, Y) = E[XY] − E[X]E[Y] with proof | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=278) | 278 |
| covariance: why joint expectation is E[XY], through the angle between two vectors (intuition) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=274) | 274 |
| conditional probability: the definition P[A|B] = P[A ∩ B] / P[B], with intuition | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=97) | 97 |
| Bayes' rule: the theorem with proof, plus the law of total probability | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=105) | 105 |
| conditional independence (Definition 6.11) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=201) | 201 |
| Bayes' rule: worked examples (winning a match against three player types, a noisy channel) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=107) | 107 |
| the Gaussian distribution: the density and its two parameters, mean and variance | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=227) | 227 |
| the Gaussian distribution: plots of how μ and σ move and widen the curve (intuition) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=228) | 228 |
| the standard Gaussian's CDF Φ(x), and Φ(x) = ½(1 + erf(x/√2)) (Definition 4.15) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=230) | 230 |
| the multivariate Gaussian: the d-dimensional density with Σ⁻¹ (definition) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=306) | 306 |
| the multivariate Gaussian: its mean vector and covariance matrix, the diagonal case | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=307) | 307 |
| hypothesis testing: null and alternative hypotheses, the courtroom picture (intuition) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=582) | 582 |
| hypothesis testing: a worked die example with an estimator | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=583) | 583 |
| hypothesis testing: the p-value, with a worked number | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=588) | 588 |
| Type I and Type II errors, and the significance level α as the probability of a Type I error (section 5.5.1, definition) | [introduction to statistics](statistics/introduction-to-statistics.pdf#page=106) | 106 |
| maximum likelihood estimation: the likelihood function from the joint density (intuition) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=484) | 484 |
| maximum likelihood estimation: the i.i.d. likelihood and log-likelihood | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=486) | 486 |
| maximum likelihood estimation: the ML estimate, with a Bernoulli worked example | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=489) | 489 |
| law of large numbers: the sample average and its mean | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=367) | 367 |
| law of large numbers: the weak law, with proof by Chebyshev | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=370) | 370 |
| central limit theorem: the dice picture and what the theorem says (intuition) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=382) | 382 |
| central limit theorem: the theorem statement (Theorem 6.19) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=388) | 388 |
| joint distribution: the joint PMF, with figure | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=262) | 262 |
| marginal distribution: the marginal PMF and PDF by summing or integrating out one variable | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=266) | 266 |
| conditional distribution: the conditional PMF p(x|y) = p(x, y) / p(y) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=283) | 283 |
| backpropagation: the chain rule over a computational graph, then the algorithm (sections 6.5.1 to 6.5.4) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=220) | 220 |
| backpropagation: the algorithm for a fully-connected net (Algorithm 6.2 on PDF page 226, forward and backward passes 6.3 and 6.4 on 228 and 229) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=226) | 226 |
| backpropagation worked on a small network, then the algorithm and its summary (section 7.4; summary on page 120) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=117) | 117 |
| the score and score matching: what the score is and why matching it avoids the partition function (section 18.4 starts here) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=633) | 633 |
| denoising score matching: fitting the score of a noise-corrupted data distribution (section 18.5) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=635) | 635 |
| energy-based models: p̃(x) = exp(−E(x)), equation 16.7 | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=585) | 585 |
| Markov chain Monte Carlo: why a Markov chain is used to sample from p_model (section 17.3) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=611) | 611 |
| Metropolis-Hastings: named in a single sentence as an alternative to Gibbs sampling, with no derivation | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=615) | 615 |
| diffusion models: the overview and what the encoder and decoder do (chapter 18) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=362) | 362 |
| diffusion models: the forward process that adds noise (section 18.2) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=363) | 363 |
| diffusion models: the reverse process, starting from Bayes' rule on the forward step (section 18.3) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=369) | 369 |
| diffusion models: training and the loss (section 18.4) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=370) | 370 |
| the Gaussian, univariate: the density and its mean and variance (section 3.9.3) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=79) | 79 |
| the Gaussian, univariate: the density with parameters µ and σ² (equation C.21) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=470) | 470 |
| the multivariate Gaussian: spherical, diagonal and full covariance, drawn as contours | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=471) | 471 |
| KL divergence: definition and non-negativity (equation 3.50) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=90) | 90 |
| KL divergence: definition for densities (equation C.28) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=474) | 474 |
| cross-entropy: H(P, Q) = H(P) + D_KL(P‖Q), equation 3.51 | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=91) | 91 |
| cross-entropy loss: fitting a model by minimising the distance to the empirical distribution, equal to negative log-likelihood (section 5.7) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=85) | 85 |
| the score function s(x) = ∇ₓ log p(x) as a direction field, with the Gaussian worked example s(x) = −(x − µ)/σ² and the multivariate −Σ⁻¹(x − µ) (section 6.1.1, definition and worked example) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=114) | 114 |
| the score field drawn as arrows for a two-component Gaussian mixture, Figure 6.1 (section 6.1.1, intuition) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=115) | 115 |
| Langevin dynamics: the SDE dXₜ = ∇ log p*(Xₜ) dt + √2 dWₜ and its discrete update xₖ₊₁ = xₖ + ε∇ log p*(xₖ) + √(2ε) ξₖ, drift for exploitation and noise against collapse (section 6.1.2, definition) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=116) | 116 |
| Langevin dynamics as a sampler: with target N(0, I) it reduces to an Ornstein-Uhlenbeck process, and the target density is stationary (section 6.1.2 to 6.1.3, worked example) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=117) | 117 |
| the Fokker-Planck stationary solution: substitute p = p* into ∂ₜp = −∇·(p∇log p*) + Δp, use p*∇log p* = ∇p*, and the two terms cancel to 0 (section 6.1.3, derivation, key step the identity p∇log p = ∇p) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=118) | 118 |
| Fisher divergence: J(θ) = E over p_data of ‖sθ(x) − s_data(x)‖², the objective score matching rewrites (section 6.2, definition) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=119) | 119 |
| explicit and implicit score matching, 1D: the cross term E[sθ s_data] rewritten by integration by parts to −E[∂ₓ sθ], boundary term dropped (section 6.2.2, derivation, key step the vanishing boundary term) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=121) | 121 |
| score matching in d dimensions: the divergence replaces the derivative and the divergence theorem gives L_SM = E[½‖sθ‖² + ∇·sθ] (section 6.2.3, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=122) | 122 |
| integration by parts: the one-dimensional identity ∫u v′ dx = [uv] − ∫u′v dx stated and then applied to the score-matching cross term (section 6.2.2, definition in a box, with the application on PDF page 121) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=120) | 120 |
| the smoothed score under Gaussian corruption: s_σ(x̃) = (E[x | x̃] − x̃)/σ², derived through Bayes' rule and the Gaussian log-density, which is Tweedie's formula for Gaussian noise though the book never names it (section 6.3.1, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=124) | 124 |
| denoising score matching: the least-squares regression identity f* = E[Y | U], then L_DSM = E‖sθ(x̃) + ε/σ²‖², so regression on a known corruption recovers the noisy score (section 6.3.3, derivation, key step the conditional-mean identity) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=126) | 126 |
| multi-scale denoising score matching: the DSM loss averaged over noise levels σ₁ > … > σ_K, with a noise-conditional score sθ(x̃, σₖ) (section 6.4.1, definition) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=129) | 129 |
| annealed Langevin dynamics: Langevin updates run at each noise level from large σ to small σ, from x ~ N(0, σ₁²I) (section 6.4.2, definition) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=130) | 130 |
| the forward SDE dXₜ = f(Xₜ, t) dt + g(t) dWₜ and its marginal densities pₜ, with the Fokker-Planck equation they obey (section 6.4.3, definition) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=131) | 131 |
| the reverse-time SDE: dXₜ = [f − g(t)²∇log pₜ] dt + g(t) dW̄ₜ, stated under regularity conditions and not derived, with the score as the added correction (section 6.4.4, definition, and Figure 6.4 on PDF page 133) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=132) | 132 |
| noise prediction as a score: ∇ log q(xₜ | x₀) = −ε/√(1 − ᾱₜ), so a network that predicts ε predicts the conditional score (section 6.5.1, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=134) | 134 |
| Brownian motion (the Wiener process): the three defining properties W₀ = 0, independent increments, Wₜ₊Δₜ − Wₜ ~ N(0, Δₜ) (section 5.1.3, definition) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=95) | 95 |
| Brownian motion: E[Wₜ] = 0 and Var(Wₜ) = t by summing n independent Gaussian increments, and the √Δt scaling of a step (section 5.1.3, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=96) | 96 |
| the Ornstein-Uhlenbeck process dXₜ = −αXₜ dt + σ dWₜ, its drift-plus-noise update and the explicit solution Xₜ = X₀e^(−αt) + σ∫e^(−α(t−s))dWₛ (section 5.1.4, definition; the stochastic integral is written but not defined) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=97) | 97 |
| stochastic differential equations: dXₜ = f dt + σ dWₜ as the particle-level form of a drift plus noise, in the chapter's summary diagram (section 5.1, intuition; the general g(t) form is on PDF page 131) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=91) | 91 |
| deterministic density evolution, finite time: p₀(x₀)dx₀ = pₜ(xₜ)dxₜ gives pₜ(xₜ) = p₀(x₀)·|dxₜ/dx₀|⁻¹, and in d dimensions the Jacobian determinant (section 5.2.1, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=99) | 99 |
| the continuity (Liouville) equation in one dimension: ∂ₜp = −∂ₓ(pf), from probability inflow minus outflow across a small interval (section 5.2.2, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=101) | 101 |
| density change along a trajectory: d/dt log p(x(t), t) = −∂ₓf, by the chain rule and the transport terms cancelling (section 5.2.3, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=102) | 102 |
| the multidimensional continuity equation ∂ₜp = −∇·(pv), with det(I + A dt) = 1 + tr(A)dt giving the divergence as the rate of volume change (section 5.2.4, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=104) | 104 |
| the multidimensional continuity equation, final step: expand p(x + v dt, t + dt) to first order and take dt → 0 to reach ∂ₜp + ∇·(pv) = 0 (section 5.2.4, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=105) | 105 |
| the Fokker-Planck equation, derivation: write p(x, t + Δt) as an expectation over the Gaussian increment, Taylor-expand p(x − η), E[η] = 0 and E[η²] = σ²Δt leave ∂ₜp = (σ²/2)∂ₓₓp (section 5.3.1 to 5.3.2, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=107) | 107 |
| the Fokker-Planck equation, one dimension with drift: ∂ₜp = −∂ₓ(fp) + (σ²/2)∂ₓₓp, the Liouville transport term plus diffusion (section 5.3.2, derivation, continued on PDF page 108) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=108) | 108 |
| the Fokker-Planck equation in d dimensions: ∂ₜp = −∇·(pv) + (σ²/2)Δp with the Laplacian (section 5.3.3, definition), and drift against diffusion drawn for the OU process in Figure 5.3 (PDF page 109) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=109) | 109 |
| energy-based models: the energy Eθ(x), the Boltzmann form pθ(x) = exp(−Eθ(x))/Zθ and the partition function Zθ = ∫exp(−Eθ(x))dx (section 8.3.2, definition) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=173) | 173 |
| energy-based models, maximum likelihood: ∇θ log Zθ = −E over pθ of ∇θEθ, giving the data term minus model term contrastive gradient (section 8.3.4, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=176) | 176 |
| why the score ignores the partition function: ∇ₓ log pθ = −∇ₓEθ − ∇ₓ log Zθ and ∇ₓ log Zθ = 0 since Zθ does not depend on x (section 8.4.2, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=179) | 179 |
| score matching for an energy-based model: J_SM = E[½‖∇ₓEθ‖² − ∇²ₓEθ], which avoids the partition function (section 8.4.3, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=180) | 180 |
| the ELBO from Jensen's inequality: rewrite p(x) = E_Q[p(x, z)/Q(z)], then log E ≥ E log gives L(Q, θ; x) = E_Q[log p(x, z)] − E_Q[log Q(z)] (section 2.4.2, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=46) | 46 |
| when the ELBO is tight: equality holds exactly when Q(z) = p(z | x) (section 2.4.3, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=47) | 47 |
| the VAE ELBO in three equivalent forms, including log p(x) − KL(q ‖ posterior) and reconstruction minus KL to the prior (section 3.2.2, derivation, continued on PDF pages 62 and 63) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=61) | 61 |
| the DDPM forward process: q(xₜ | xₜ₋₁) = N(√(1 − βₜ) xₜ₋₁, βₜI), and by recursion and summing Gaussians xₜ = √ᾱₜ x₀ + √(1 − ᾱₜ) ε (section 4.1.1, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=70) | 70 |
| the DDPM forward process summarised: αₜ, ᾱₜ, the closed form q(xₜ | x₀) and the Markov factorisation (section 4.1.2, summary box) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=73) | 73 |
| the DDPM reverse process: the learned Markov chain pθ(xₜ₋₁ | xₜ) from p(x_T) = N(0, I), and why the true reverse step is intractable (sections 4.2.1 to 4.2.2, definition) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=74) | 74 |
| the diffusion ELBO: the forward process q(x₁:T | x₀) plays the role of Q(z), and the negative ELBO splits into prior-matching, step-wise KL and reconstruction terms (sections 4.2.3 and 4.3.3, derivation, with the split on PDF page 81) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=75) | 75 |
| the true reverse posterior of DDPM: q(xₜ₋₁ | xₜ, x₀) is Gaussian with mean µ̃ₜ and variance β̃ₜ = (1 − ᾱₜ₋₁)βₜ/(1 − ᾱₜ), by completing the square (section 4.4.1, derivation, algebra in Appendix B on PDF page 189) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=83) | 83 |
| the DDPM training objective: the KL between equal-variance Gaussians reduces to ‖µ̃ₜ − µθ‖², hence to ‖ε − εθ(xₜ, t)‖² and L_simple (section 4.4.3, derivation, key step the shared variance) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=86) | 86 |
| the DDPM training and sampling loop: sample t and ε, form xₜ, regress ε; sample from x_T ~ N(0, I) back to x₀ (section 4.4.4, worked algorithm) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=87) | 87 |
| completing the square for Gaussians: −½xᵀAx + bᵀx = −½(x − A⁻¹b)ᵀA(x − A⁻¹b) + ½bᵀA⁻¹b, applied to the PPCA posterior (Appendix A, derivation) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=185) | 185 |
| how to read an algorithm block: Algorithm 7.2, Newton's method for one variable, with its Objective, Input, Output, Initialization and Repeat-Until parts, and Example 7.3 set up on it (worked algorithm) | [optimization: principles and algorithms](optimization/optimization-principles-and-algorithms.pdf#page=203) | 203 |
| an algorithm block run one iteration per row: Table 7.1, Example 7.3's iterates xₖ, F(xₖ) and F′(xₖ) (worked example; Example 7.5 on PDF page 206 runs the same block and diverges) | [optimization: principles and algorithms](optimization/optimization-principles-and-algorithms.pdf#page=204) | 204 |
| gradient descent: ϕ ← ϕ − α ∂L/∂ϕ, α as the learning rate, line search, and the gradient zero at a minimum (section 6.1, definition) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=92) | 92 |
| steepest descent xₖ₊₁ = xₖ − αₖ∇f(xₖ) with the step chosen by exact line search, run by hand on ½x₁² + 9/2 x₂² in Example 11.1 (section 11.1, worked example; the zigzag is Figure 11.1 on PDF page 265) | [optimization: principles and algorithms](optimization/optimization-principles-and-algorithms.pdf#page=264) | 264 |
| the negative gradient points directly downhill: the method of steepest descent (section 4.3, intuition) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=101) | 101 |
| −∇f is the steepest descent direction (Corollary 2.13, with numbers in Example 2.14) | [optimization: principles and algorithms](optimization/optimization-principles-and-algorithms.pdf#page=53) | 53 |
| the Hessian matrix written out, always symmetric and the Jacobian of the gradient, and Theorem 2.21: a positive semidefinite Hessian means convex (definition and theorem) | [optimization: principles and algorithms](optimization/optimization-principles-and-algorithms.pdf#page=58) | 58 |
| a local minimum of a convex function is global, and a strictly convex function has only one (Theorem 5.9) | [optimization: principles and algorithms](optimization/optimization-principles-and-algorithms.pdf#page=140) | 140 |
| a convex set (Definition B.2) | [optimization: principles and algorithms](optimization/optimization-principles-and-algorithms.pdf#page=707) | 707 |
| critical points in one variable: a relative extremum on an open interval sits where the derivative is zero (Theorem 4.2.2) | [calculus textbook](calculus/calculus-textbook.pdf#page=269) | 269 |
| Euler's method for an ODE, derived from the tangent line | [calculus textbook](calculus/calculus-textbook.pdf#page=605) | 605 |
| the reparameterization trick: z = mu + Sigma^(1/2) eps, so the gradient passes the sampling (section 17.7) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=352) | 352 |
| an eigenvalue and its eigenvector (Definition 1), with Theorem 5.1.1 and worked examples on the next page | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=305) | 305 |
| a real symmetric matrix has real eigenvalues and orthogonal eigenvectors (Theorem 7.2.2) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=425) | 425 |
| the improper integral over the whole line, (-inf, +inf), as two one-sided limits split at a point (Definition 7.8.3) | [calculus textbook](calculus/calculus-textbook.pdf#page=574) | 574 |
| the fundamental theorem of calculus, part 1: evaluate a definite integral with any antiderivative (Theorem 5.6.1) | [calculus textbook](calculus/calculus-textbook.pdf#page=387) | 387 |
| the quotient rule (Theorem 2.4.2) | [calculus textbook](calculus/calculus-textbook.pdf#page=189) | 189 |
| elementary functions: what counts as one | [calculus textbook](calculus/calculus-textbook.pdf#page=427) | 427 |
| the integral of e^(-t^2) has no elementary form, and the error function it defines | [calculus textbook](calculus/calculus-textbook.pdf#page=428) | 428 |
| precision: the reciprocal of the variance, β = 1/σ² (section 1.2.4, definition) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=43) | 43 |
| Markov chain Monte Carlo: a proposal that depends on the current state, so the samples form a Markov chain, and the normalising constant may stay unknown (section 11.2, which opens at the foot of PDF page 553) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=554) | 554 |
| stationary (invariant) distribution of a Markov chain, and detailed balance (11.40) with the one-line proof that it leaves the distribution invariant (section 11.2.1) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=556) | 556 |
| Metropolis-Hastings: the acceptance probability (11.44), why the normalising constant is not needed, and the detailed-balance proof (section 11.2.2) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=557) | 557 |
| hybrid (Hamiltonian) Monte Carlo: leapfrog moves accepted or rejected by the Metropolis test on the Hamiltonian, (11.67) (section 11.5.2) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=568) | 568 |
| a linear transformation of a Gaussian: Y = aX + b for a standard Gaussian X, with its CDF and density (follow-up in section 4.7, density on PDF page 242) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=241) | 241 |
| the variance of a sample average: Var of the mean of N i.i.d. draws is σ²/N (section 6.3) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=368) | 368 |
| broadcasting: adding a vector to every row of a matrix by implicit copying (end of section 2.1) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=50) | 50 |
| the difference quotient (f(x + h) - f(x)) / h and the derivative as its limit (Definition 2.2.1) | [calculus textbook](calculus/calculus-textbook.pdf#page=167) | 167 |
| the derivative of a constant function is 0, by (c - c) / h = 0 (Theorem 2.3.1) | [calculus textbook](calculus/calculus-textbook.pdf#page=179) | 179 |
| the variable of integration in a definite integral is a dummy variable and plays no role in the result | [calculus textbook](calculus/calculus-textbook.pdf#page=392) | 392 |
| the derivative of ln x is 1 / x, from the difference quotient (section 3.2) | [calculus textbook](calculus/calculus-textbook.pdf#page=216) | 216 |
| variance under an affine map, V[Ax + b] = AΣAᵀ (a²σ² for a scalar), and V[x + y] = V[x] + V[y] for independent x, y (equations 6.51 and section 6.4.5) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=200) | 200 |
| the Bernoulli mean and variance, E[X] = p and Var[X] = p(1 − p), so an indicator's variance (Theorem 3.6) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=154) | 154 |
| a probability density function, defined with the unity condition that it integrates to 1 (Definition 4.1) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=190) | 190 |
| the CDF of an arbitrary Gaussian by standardising, F(x) = Φ((x − µ)/σ), with the upper tail 1 − Φ on the next page (Theorem 4.11) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=231) | 231 |
| substitution in a definite integral: change the limits to u = g(a), u = g(b), with a worked example (section 5.9, Method 2) | [calculus textbook](calculus/calculus-textbook.pdf#page=415) | 415 |
| iterated integrals: a double integral over a rectangle as two successive single integrals, holding one variable fixed (section 14.1, equations 6 and 7) | [calculus textbook](calculus/calculus-textbook.pdf#page=1027) | 1027 |
| the Gaussian integral: the normaliser of exp(−x²/2σ²) is √(2πσ²), squared and changed to polar coordinates, with hints (Exercise 2.12) | [probabilistic machine learning: an introduction](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=99) | 99 |
| the PDF of X + Y is the convolution of the two PDFs, derived from the CDF of the sum (section 5.5.2) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=298) | 298 |
| the sum of two independent Gaussians is Gaussian with means and variances added, proved by convolution (Theorem 5.12) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=299) | 299 |
| the CDF of the standard Gaussian, Φ, and its link to erf (Definition 4.15) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=230) | 230 |
| the Gaussian kernel density estimator: one Gaussian of width h on each data point, averaged (equation 2.250, section 2.5.1) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=142) | 142 |
| responsibility in a Gaussian mixture: the posterior of a component given x, by Bayes' theorem (equation 9.13) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=449) | 449 |
| the double integral as the limit of Riemann sums, each term the value times the area of a small cell (section 14.1, equation 4) | [calculus textbook](calculus/calculus-textbook.pdf#page=1026) | 1026 |
| tokenization: splitting raw text into words with a regular expression, on whitespace or on word characters (section 3.7) | [natural language processing with Python](natural-language-processing/natural-language-processing-with-python.pdf#page=131) | 131 |
| regular expression metacharacters: `[abc]`, the range `[A-Z0-9]`, `+` for one or more, `*`, `?`, `{m,n}` (Table 3-3, section 3.4) | [natural language processing with Python](natural-language-processing/natural-language-processing-with-python.pdf#page=123) | 123 |
| a text's vocabulary as a Python set: `set(text)`, `len(set(text))`, word types against tokens (section 1.1) | [natural language processing with Python](natural-language-processing/natural-language-processing-with-python.pdf#page=30) | 30 |
| recursion: a function that calls itself on a smaller instance, with a base case (section 4.7) | [natural language processing with Python](natural-language-processing/natural-language-processing-with-python.pdf#page=182) | 182 |
| dynamic programming: overlapping subproblems stored in a lookup table, bottom-up against top-down and memoization, on Sanskrit meters (section 4.7, through PDF page 189) | [natural language processing with Python](natural-language-processing/natural-language-processing-with-python.pdf#page=187) | 187 |
| softmax: K arbitrary outputs made non-negative and summing to one, softmaxₖ[z] = exp[zₖ]/Σ exp[zₖ′], with a picture of the categorical distribution it produces (section 5.5, equation 5.22) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=82) | 82 |
| softmax computed safely: subtract maxᵢ xᵢ before exponentiating so exp cannot overflow, and why the value is unchanged (section 4.1, equation 4.1) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=97) | 97 |
| the dot product in components, u · v = u₁v₁ + … + uₙvₙ, with worked examples in R³ and R⁴ (Definition 4, section 3.2) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=161) | 161 |
| the dot product geometrically, u · v = ‖u‖‖v‖cos θ, worked on two vectors at 45°, then the component form derived from the law of cosines (section 3.2) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=160) | 160 |
| the norm (length) of a vector, ‖v‖ = √(v₁² + … + vₙ²), with worked norms and unit vectors on the next page (section 3.2) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=156) | 156 |
| Euclidean distance between two points in Rⁿ, d(u, v) = ‖u − v‖ (Definition 2 and Example 4, section 3.2) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=159) | 159 |
| cosine similarity cos θ = v₁ᵀv₂ / (‖v₁‖‖v₂‖), and the dot product read as a scaled projection (section 1.1, boxed) | [the little book of generative AI foundations](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=13) | 13 |
| the angle between two vectors from the inner product, worked: cos ω = 3/√10, about 18° (Example 3.6) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=83) | 83 |
| independent events: P[A ∩ B] = P[A]P[B], and why, through conditional probability (Definition 2.23, section 2.4.2) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=101) | 101 |
| combinations: choosing k of n unordered, n! / (k!(n − k)!), so n(n − 1)/2 pairs (Theorem 1.7, section 1.5) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=51) | 51 |
| bootstrapping: K datasets drawn with replacement from the one you have, the bootstrapped mean and variance (Algorithm 2, section 9.2) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=579) | 579 |
| additivity: probabilities of disjoint events add, and why the three axioms (Axiom III, section 2.3) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=91) | 91 |
| precision and recall: TP/(TP + FP) and TP/(TP + FN), what high and low each mean (section 9.5, equations 9.42 and 9.43) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=618) | 618 |
| the harmonic mean: the reciprocal of the mean of reciprocals, worked on an average speed | [algebra handbook](algebra/algebra-handbook.pdf#page=170) | 170 |
| percent increase and decrease: the change divided by the original amount, worked | [pre-algebra handbook](general/pre-algebra-handbook.pdf#page=37) | 37 |
| Bellman's equation: the shortest-path label of a node is the minimum over incoming arcs of the upstream label plus the arc cost, λj = min(λi + cij) (Theorem 23.11) | [optimization: principles and algorithms](optimization/optimization-principles-and-algorithms.pdf#page=582) | 582 |
| union and intersection of two sets, defined with Venn diagrams (section 3.3, Definitions 8 and 9, intersection on PDF page 58) | [introduction to statistics](statistics/introduction-to-statistics.pdf#page=57) | 57 |
| the chain rule: the derivative of a composition f∘g from the derivatives of f and g, motivated by miles per gallon (section 2.6, Theorem 2.6.1 on the next page) | [calculus textbook](calculus/calculus-textbook.pdf#page=198) | 198 |
| the standard deviation: the square root of the variance, Var[X] = E[(X − µ)²] (Definition 3.7) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=150) | 150 |
| triangular matrices: lower triangular has zeros above the main diagonal, upper triangular below, drawn for 4 by 4 (section 1.7, Example 2) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=83) | 83 |
| Jensen's inequality: E[g(X)] ≥ g(E[X]) for convex g, flipped for concave g, motivated by E[X²] ≥ E[X]² (Theorem 6.10, section 6.2.3) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=352) | 352 |
| the standard error: the standard deviation of a sample average, se = σ/√N, then the critical value and margin of error (equations 9.7 to 9.9, section 9.1) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=568) | 568 |
| the binomial PMF: k successes in n independent trials, C(n, k)pᵏ(1 − p)ⁿ⁻ᵏ, so none in n has probability (1 − p)ⁿ (Definition 3.9, section 3.5.2) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=159) | 159 |
| radians: 2π in one turn, one radian is the radius wrapped along the circle, arc length S = rθ | [trigonometry handbook](trigonometry/trigonometry-handbook.pdf#page=7) | 7 |
| the graphs of the basic trigonometric functions, sine and cosine as waves | [trigonometry handbook](trigonometry/trigonometry-handbook.pdf#page=16) | 16 |
| dividing decimals in long-division form, a fraction turned into a decimal | [pre-algebra handbook](general/pre-algebra-handbook.pdf#page=30) | 30 |
| rounding rules, to a given decimal place | [pre-algebra handbook](general/pre-algebra-handbook.pdf#page=32) | 32 |
| ratios as fractions relating two counts | [pre-algebra handbook](general/pre-algebra-handbook.pdf#page=74) | 74 |
| the floor (greatest integer) function | [algebra handbook](algebra/algebra-handbook.pdf#page=25) | 25 |
| x mod n as the remainder of x divided by n, and the remainder of a sum or product taken part by part (section 8.2.2, RSA) | [computer networking: a top-down approach](system-design/computer-networking-a-top-down-approach.pdf#page=636) | 636 |
| modular arithmetic defined: a = b (mod m) when a − b is a multiple of m, and the residue as the remainder on division by m (section 10.14) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=669) | 669 |
| a check digit as a dot product then a remainder: ISBN-10's nine digits dotted with weights 1 to 9 give 152, and 152 mod 11 = 9 is the check digit (section 3.2, application) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=165) | 165 |
| vector addition and scalar multiplication by components, v + w = (v₁ + w₁, …) and kv = (kv₁, …), with a worked example (section 3.1, Definition 3) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=151) | 151 |
| the nth root as a power, ⁿ√a = a^(1/n), so the exponent rules apply to roots | [algebra handbook](algebra/algebra-handbook.pdf#page=86) | 86 |
| properties of inequalities: multiplying or dividing both sides by a negative number flips the sign | [algebra handbook](algebra/algebra-handbook.pdf#page=42) | 42 |
| absolute value inequalities, |x − a| < c split into −c < x − a < c | [algebra handbook](algebra/algebra-handbook.pdf#page=48) | 48 |
| multiplying binomials, the square of a difference | [algebra handbook](algebra/algebra-handbook.pdf#page=62) | 62 |
| the parabola: its vertex and which way it opens | [algebra handbook](algebra/algebra-handbook.pdf#page=73) | 73 |
| graphing simple rational functions a/(x − h) + k, such as 1 − d/L | [algebra handbook](algebra/algebra-handbook.pdf#page=139) | 139 |
| horizontal asymptotes and end behaviour of a rational function, worked | [algebra handbook](algebra/algebra-handbook.pdf#page=140) | 140 |
| sequences, recursive formulas and the nth term | [algebra handbook](algebra/algebra-handbook.pdf#page=163) | 163 |
| summation notation Σ, expanded term by term | [algebra handbook](algebra/algebra-handbook.pdf#page=165) | 165 |
| a proportion: count over total, then times 100 for a percentage | [introduction to statistics](statistics/introduction-to-statistics.pdf#page=21) | 21 |
| the mean, plain and frequency-weighted | [introduction to statistics](statistics/introduction-to-statistics.pdf#page=40) | 40 |
| sets and elements, X = {A, …} | [introduction to statistics](statistics/introduction-to-statistics.pdf#page=55) | 55 |
| E[XY] = E[X]E[Y] for independent variables | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=280) | 280 |
| precision and recall (equation 9.40) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=617) | 617 |
| the matrix product and the size it needs | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=43) | 43 |
| the inverse of a product, (AB)⁻¹ = B⁻¹A⁻¹ | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=60) | 60 |
| vectors as ordered n-tuples | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=150) | 150 |
| the angle and cosine in any number of dimensions, θ = cos⁻¹(u·v / ‖u‖‖v‖) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=162) | 162 |
| the theorem of Pythagoras in Rⁿ | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=174) | 174 |
| the theorem of Pythagoras, a² + b² = c² | [geometry handbook](geometry/geometry-handbook.pdf#page=80) | 80 |
| least squares | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=393) | 393 |
| quadratic forms (section 7.3) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=432) | 432 |
| the Woodbury identity (section 3.2.2) | [matrix cookbook](linear-algebra/matrix-cookbook.pdf#page=18) | 18 |
| the tangent slope as the limit of secant slopes | [calculus textbook](calculus/calculus-textbook.pdf#page=157) | 157 |
| the extended power rule, worked on 1/x | [calculus textbook](calculus/calculus-textbook.pdf#page=181) | 181 |
| first and second derivative tests for a local minimum | [calculus textbook](calculus/calculus-textbook.pdf#page=271) | 271 |
| sigma notation | [calculus textbook](calculus/calculus-textbook.pdf#page=364) | 364 |
| properties of sums: a constant that does not depend on the index comes outside, Σ c aₖ = c Σ aₖ (Theorem 5.4.1) | [calculus textbook](calculus/calculus-textbook.pdf#page=366) | 366 |
| the natural exponential function: e ≈ 2.718, eˣ positive and increasing, written exp(x) (section 0.5) | [calculus textbook](calculus/calculus-textbook.pdf#page=78) | 78 |
| the definite integral | [calculus textbook](calculus/calculus-textbook.pdf#page=377) | 377 |
| the derivative of tanh, sech² | [calculus textbook](calculus/calculus-textbook.pdf#page=501) | 501 |
| the Maclaurin series for eˣ | [calculus textbook](calculus/calculus-textbook.pdf#page=684) | 684 |
| the moment generating function, M(s) = E[e^{sX}], defined (Definition 6.1) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=340) | 340 |
| the moment generating function of a sum of independent variables is the product (Theorem 6.2) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=343) | 343 |
| the same moment generating function means the same distribution (Definition 12, property 2) | [introduction to statistics](statistics/introduction-to-statistics.pdf#page=83) | 83 |
| sinh and cosh defined from eˣ and e⁻ˣ | [calculus handbook](calculus/calculus-handbook.pdf#page=79) | 79 |
| the chain rule for several variables | [calculus textbook](calculus/calculus-textbook.pdf#page=973) | 973 |
| the gradient | [calculus textbook](calculus/calculus-textbook.pdf#page=987) | 987 |
| Minkowski loss: the conditional median for q = 1 | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=67) | 67 |
| bias squared plus variance plus noise (equation 3.41) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=168) | 168 |
| Gaussian classes with a shared covariance give a logistic posterior (section 4.2.1) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=216) | 216 |
| the Gaussian mixture model (equation 9.7) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=447) | 447 |
| EM for Gaussian mixtures (section 9.2.2) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=452) | 452 |
| probabilistic PCA (section 12.2) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=586) | 586 |
| mean squared error as bias squared plus variance (section 5.4.4) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=145) | 145 |
| indexes start from zero | [natural language processing with Python](natural-language-processing/natural-language-processing-with-python.pdf#page=34) | 34 |
| Itô's lemma: the stochastic chain rule, Theorem 7.3.1 (definition) | [stochastic differential equations](calculus/stochastic-differential-equations.pdf#page=156) | 156 |
| Itô's lemma: why the second-order term in dX stays, giving the extra drift tr(GᵀHG)/2 | [stochastic differential equations](calculus/stochastic-differential-equations.pdf#page=157) | 157 |
| Euler-Maruyama scheme: defined from an ODE driven by noise, with the Brownian increment (eq. 6.3) | [stochastic differential equations](calculus/stochastic-differential-equations.pdf#page=130) | 130 |
| Euler-Maruyama run in code: a scalar SDE solved and plotted | [SDEs in code, example 1](https://docs.sciml.ai/DiffEqDocs/stable/tutorials/sde_example/#Example-1:-Scalar-SDEs) | web |
| many sample paths of one SDE, with their mean and spread | [SDEs in code, ensembles](https://docs.sciml.ai/DiffEqDocs/stable/tutorials/sde_example/#Ensemble-Simulations) | web |
| the CDF of a continuous variable: F(x) = P[X ≤ x], the integral of the PDF up to x, with a uniform worked example (Definition 4.7, section 4.3.1) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=202) | 202 |
| the forward Kolmogorov (Fokker-Planck) equation, Theorem 9.5.1 | [stochastic differential equations](calculus/stochastic-differential-equations.pdf#page=214) | 214 |
| the stationary density of a scalar SDE, worked (eqs 9.6, 9.7) | [stochastic differential equations](calculus/stochastic-differential-equations.pdf#page=220) | 220 |
| the sum and difference rules for derivatives, (f + g)′ = f′ + g′ (Theorem 2.3.5) | [calculus textbook](calculus/calculus-textbook.pdf#page=182) | 182 |
| the gradient of a dot product, ∂(xᵀa)/∂x = aᵀ, and other gradient identities (section 5.5) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=164) | 164 |
| standardization: subtract the mean, divide by the standard deviation (section 10.6) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=342) | 342 |
| the transpose (Definition 2.4) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=31) | 31 |
| the identity matrix, I A = A I = A (equation 2.20) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=30) | 30 |
| the partial derivative: hold every other variable fixed and differentiate in one (Definition 13.3.1) | [calculus textbook](calculus/calculus-textbook.pdf#page=951) | 951 |
| symmetric central differences, (f(w + ε) − f(w − ε)) / 2ε, accurate to O(ε²), for checking a derivative numerically (equation 5.69) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=264) | 264 |
| the unit circle: the x-coordinate is the cosine of the angle and the y-coordinate is its sine | [trigonometry handbook](trigonometry/trigonometry-handbook.pdf#page=10) | 10 |
| a telescoping sum: each term cancels part of the next until only the first and last remain (section 9.3, equation 10) | [calculus textbook](calculus/calculus-textbook.pdf#page=644) | 644 |
| the conditional PDF: f(x | y) = f(x, y) / f(y) (Definition 5.16, at the foot of the page) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=287) | 287 |
| the product of two normals is proportional to a third normal, with its mean, covariance and constant (section 5.6, equations 5.14 and 5.15) | [computer vision textbook](computer-vision/computer-vision-textbook.pdf#page=76) | 76 |
| the gradient points in the direction of fastest increase, and its length is the largest slope (section 13.6, properties of the gradient) | [calculus textbook](calculus/calculus-textbook.pdf#page=988) | 988 |
| Leibniz's rule: differentiating under the integral sign, the gradient of an integral is the integral of the gradient (equation 18.14) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=623) | 623 |
| the derivative of ln u by the chain rule, u′ / u (section 3.2) | [calculus textbook](calculus/calculus-textbook.pdf#page=217) | 217 |
| doubling time and half-life of an exponential model, T = ln 2 / k, with the halving figure (section 8.2) | [calculus textbook](calculus/calculus-textbook.pdf#page=597) | 597 |
| absolute value: the distance from zero | [algebra handbook](algebra/algebra-handbook.pdf#page=15) | 15 |
| adding rational expressions over a common denominator | [algebra handbook](algebra/algebra-handbook.pdf#page=145) | 145 |
| perfect squares: (a + b)² = a² + 2ab + b² and (a − b)² = a² − 2ab + b² | [algebra handbook](algebra/algebra-handbook.pdf#page=66) | 66 |
| the likelihood function, and Bayes' theorem in words: posterior ∝ likelihood × prior (equations 1.43 and 1.44) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=41) | 41 |
| the continuous uniform density u(x; a, b) = 1 / (b − a) on [a, b], 0 outside (section 3.3.2) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=74) | 74 |
| the product rule, p(x, y) = p(y | x) p(x) (equation 6.22) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=191) | 191 |
| matrix-vector multiplication: each output is a weighted sum of the inputs, yᵢ = Σⱼ Aᵢⱼ xⱼ, with a worked 2 by 2 example | [matrix-vector multiplication](linear-algebra/matrix-vector-multiplication.pdf#page=1) | 1 |
| the log-sum-exp trick: log Σ exp(aₖ) = m + log Σ exp(aₖ − m) with m the largest term, so nothing overflows (section 2.5.4, equation 2.99) | [probabilistic machine learning: an introduction](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=80) | 80 |
| softmax temperature: dividing by T, low T puts the mass on the largest entry and high T spreads it, named from statistical physics (section 2.5.2, equation 2.94) | [probabilistic machine learning: an introduction](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=79) | 79 |
| linearity of expectation: E[aX + b] = aE[X] + b, and the expectation of a sum is the sum of expectations (equation 2.25) | [probabilistic machine learning: an introduction](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=66) | 66 |
| the basic Metropolis algorithm (1953): accept a candidate with min(1, p(z⋆)/p(z)) by comparing with a uniform draw u, and the samples form a Markov chain (equation 11.33) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=554) | 554 |
| a first-order Markov chain: p(z⁽ᵐ⁺¹⁾ | z⁽¹⁾, …, z⁽ᵐ⁾) = p(z⁽ᵐ⁺¹⁾ | z⁽ᵐ⁾) (section 11.2.1, equation 11.37, at the foot of the page) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=555) | 555 |
| the Hamiltonian: kinetic energy K(r) = ½‖r‖², total energy H = E + K, Hamilton's equations, with a note on William Rowan Hamilton (section 11.5.1, equations 11.56 to 11.59) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=565) | 565 |
| the leapfrog discretization: half step in momentum, full step in position, half step in momentum (equations 11.64 to 11.66) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=567) | 567 |
| each leapfrog step shears phase space without changing volume, and the hybrid Monte Carlo detailed-balance argument (Figure 11.14) | [pattern recognition and machine learning](machine-learning/pattern-recognition-and-machine-learning.pdf#page=569) | 569 |
| the Dirac distribution and the empirical distribution, one point mass of 1/m on each data point (section 3.9.5) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=81) | 81 |
| self-information with the natural log, measured in nats (section 3.13, equation 3.48) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=89) | 89 |
| overflow and underflow: finite bit patterns, rounding error, numbers near zero rounded to zero (section 4.1) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=96) | 96 |
| Adam: normalise the gradient by its squared magnitude so each direction moves a set distance (section 6.4) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=102) | 102 |
| the binomial mean, E[X] = np, with its variance, and the proof (Theorem 3.7) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=162) | 162 |
| the symmetry of the standard Gaussian CDF, Φ(y) = 1 − Φ(−y), and tail probabilities (Corollary 4.1) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=232) | 232 |
| the determinant of a triangular matrix is the product of its diagonal entries (Theorem 2.1.2) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=124) | 124 |
| composition of functions: (f ∘ g)(x) = f(g(x)), the function closest to the variable acts first | [algebra handbook](algebra/algebra-handbook.pdf#page=27) | 27 |
| the distributive property, a(b + c) = ab + ac, with the commutative and associative properties | [algebra handbook](algebra/algebra-handbook.pdf#page=16) | 16 |
| context recall for a retriever: of all the documents relevant to the query, the share retrieved; context precision on page 513, and NDCG, MAP and MRR only named (definition) | [AI engineering](ai-engineering/ai-engineering.pdf#page=514) | 514 |
| a linear mapping: Φ(λx + ψy) = λΦ(x) + ψΦ(y) for all vectors and scalars (Definition 2.15) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=54) | 54 |
| an affine subspace L = x₀ + U, a subspace shifted by its support point x₀ (Definition 2.25) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=67) | 67 |
| an affine mapping φ(x) = a + Φ(x), a linear mapping plus the translation vector a (Definition 2.26, continued on PDF page 69) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=68) | 68 |
| matrix transformations, and every linear transformation from Rⁿ to Rᵐ is one (Theorem 1.8.3; section 1.8 opens on PDF page 91) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=93) | 93 |
| a linear transformation between general vector spaces: T(ku) = kT(u) and T(u + v) = T(u) + T(v) (Definition 1, section 8.1) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=461) | 461 |
| translation is not linear: a linear transformation sends 0 to 0, so T(x) = x + x₀ is not one (Example 8, section 8.1) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=464) | 464 |
| a line or plane through x₀ is the translation by x₀ of the one through the origin (Remark after Theorem 3.4.2) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=179) | 179 |
| the translation vector of a translation in computer graphics (section 10.9) | [linear algebra textbook](linear-algebra/linear-algebra-textbook.pdf#page=612) | 612 |
| vertical translation f(x) + k, and the other graph transformations, in one table | [algebra handbook](algebra/algebra-handbook.pdf#page=33) | 33 |
| a linear combination of functions, a₁f₁ + a₂f₂ + … + aₙfₙ | [algebra handbook](algebra/algebra-handbook.pdf#page=53) | 53 |

## general/

### Pre-algebra handbook

`general/pre-algebra-handbook.pdf`, 107 pages. Earl L. Whitney, *Math Handbook of Formulas, Processes
and Tricks: Pre-Algebra*, version 2.5, 2022 (mathguy.us). Was `Pre-Algebra & Basic Statistics.pdf`.

| Chapter | PDF page |
| --- | --- |
| 1 Numbers | [8](general/pre-algebra-handbook.pdf#page=8) |
| 2 Measures and Weights | [17](general/pre-algebra-handbook.pdf#page=17) |
| 3 Operations | [20](general/pre-algebra-handbook.pdf#page=20) |
| 4 Fractions and Decimals | [24](general/pre-algebra-handbook.pdf#page=24) |
| 5 Percents | [33](general/pre-algebra-handbook.pdf#page=33) |
| 6 Exponents and Roots | [39](general/pre-algebra-handbook.pdf#page=39) |
| 7 Equations and Inequalities | [46](general/pre-algebra-handbook.pdf#page=46) |
| 8 Linear Functions | [55](general/pre-algebra-handbook.pdf#page=55) |
| 9 Probability and Statistics | [61](general/pre-algebra-handbook.pdf#page=61) |
| 10 Geometry Basics | [66](general/pre-algebra-handbook.pdf#page=66) |
| 11 Triangles | [70](general/pre-algebra-handbook.pdf#page=70) |
| 12 Quadrilaterals | [77](general/pre-algebra-handbook.pdf#page=77) |
| 13 Transformations | [81](general/pre-algebra-handbook.pdf#page=81) |
| 14 Polygons | [87](general/pre-algebra-handbook.pdf#page=87) |
| 15 Perimeter, Area and Volume | [90](general/pre-algebra-handbook.pdf#page=90) |

### GED handbook

`general/ged-handbook.pdf`, 93 pages. Earl L. Whitney, *Math Handbook of Formulas, Processes and
Tricks: High School Equivalency (GED) Exam*, version 2.2, 2017. Was
`Mathematics Handbook Of Formula Processes & Tricks.pdf`. Selected pages from three of the author's
handbooks, bound in order.

| Part | PDF page |
| --- | --- |
| Pre-algebra | [3](general/ged-handbook.pdf#page=3) |
| Algebra | [17](general/ged-handbook.pdf#page=17) |
| Geometry | [65](general/ged-handbook.pdf#page=65) |

## algebra/

### Algebra handbook

`algebra/algebra-handbook.pdf`, 187 pages. Earl L. Whitney, *Math Handbook of Formulas, Processes and
Tricks: Algebra and PreCalculus*, version 3.5, 2022. Was `AlgebraHandbook.pdf`.

| Chapter | PDF page |
| --- | --- |
| 1 Basics | [9](algebra/algebra-handbook.pdf#page=9) |
| 2 Operations | [15](algebra/algebra-handbook.pdf#page=15) |
| 3 Solving Equations | [18](algebra/algebra-handbook.pdf#page=18) |
| 4 Probability & Statistics | [20](algebra/algebra-handbook.pdf#page=20) |
| 5 Functions | [24](algebra/algebra-handbook.pdf#page=24) |
| 6 Linear Functions | [35](algebra/algebra-handbook.pdf#page=35) |
| 7 Inequalities | [42](algebra/algebra-handbook.pdf#page=42) |
| 8 Systems of Equations | [49](algebra/algebra-handbook.pdf#page=49) |
| 9 Exponents (Basic) and Scientific Notation | [56](algebra/algebra-handbook.pdf#page=56) |
| 10 Polynomials: Basic | [60](algebra/algebra-handbook.pdf#page=60) |
| 11 Quadratic Functions | [73](algebra/algebra-handbook.pdf#page=73) |
| 12 Complex Numbers | [80](algebra/algebra-handbook.pdf#page=80) |
| 13 Radicals | [86](algebra/algebra-handbook.pdf#page=86) |
| 14 Matrices | [90](algebra/algebra-handbook.pdf#page=90) |
| 15 Exponents and Logarithms | [109](algebra/algebra-handbook.pdf#page=109) |
| 16 Polynomials: Intermediate | [126](algebra/algebra-handbook.pdf#page=126) |
| 17 Rational Functions | [137](algebra/algebra-handbook.pdf#page=137) |
| 18 Conic Sections | [148](algebra/algebra-handbook.pdf#page=148) |
| 19 Sequences and Series | [163](algebra/algebra-handbook.pdf#page=163) |

### Quadratic functions

`algebra/quadratic-functions.pdf`, 4 pages. Own notes, 10 September 2021. Was `Quadratic Functions.pdf`.

### Rational functions

`algebra/rational-functions.pdf`, 8 pages. Own notes on domains of rational functions. Was
`Rational_Functions.pdf`.

## geometry/

### Geometry handbook

`geometry/geometry-handbook.pdf`, 137 pages. Earl L. Whitney, *Math Handbook of Formulas, Processes and
Tricks: Geometry*. Was `GeometryHandbook.pdf`.

| Chapter | PDF page |
| --- | --- |
| 1 Basic Geometry | [6](geometry/geometry-handbook.pdf#page=6) |
| 2 Proofs | [16](geometry/geometry-handbook.pdf#page=16) |
| 3 Parallel and Perpendicular Lines | [22](geometry/geometry-handbook.pdf#page=22) |
| 4 Triangles: Basic | [29](geometry/geometry-handbook.pdf#page=29) |
| 5 Polygons | [43](geometry/geometry-handbook.pdf#page=43) |
| 6 Quadrilaterals | [46](geometry/geometry-handbook.pdf#page=46) |
| 7 Transformations | [55](geometry/geometry-handbook.pdf#page=55) |
| 8 Similarity | [68](geometry/geometry-handbook.pdf#page=68) |
| 9 Right Triangles | [80](geometry/geometry-handbook.pdf#page=80) |
| 10 Circles | [92](geometry/geometry-handbook.pdf#page=92) |
| 11 Perimeter and Area | [98](geometry/geometry-handbook.pdf#page=98) |
| 12 Surface Area and Volume | [111](geometry/geometry-handbook.pdf#page=111) |

## trigonometry/

### Trigonometry handbook

`trigonometry/trigonometry-handbook.pdf`, 114 pages. Earl L. Whitney, *Math Handbook of Formulas,
Processes and Tricks: Trigonometry*. Was `TrigonometryHandbook.pdf`.

| Chapter | PDF page |
| --- | --- |
| 1 Functions and Special Angles | [7](trigonometry/trigonometry-handbook.pdf#page=7) |
| 2 Graphs of Trig Functions | [15](trigonometry/trigonometry-handbook.pdf#page=15) |
| 3 Inverse Trigonometric Functions | [33](trigonometry/trigonometry-handbook.pdf#page=33) |
| 4 Key Angle Formulas | [37](trigonometry/trigonometry-handbook.pdf#page=37) |
| 5 Identities and Equations | [43](trigonometry/trigonometry-handbook.pdf#page=43) |
| 6 Solving an Oblique Triangle | [51](trigonometry/trigonometry-handbook.pdf#page=51) |
| 7 Area of a Triangle | [65](trigonometry/trigonometry-handbook.pdf#page=65) |
| 8 Polar Coordinates | [68](trigonometry/trigonometry-handbook.pdf#page=68) |
| 9 Polar Functions | [73](trigonometry/trigonometry-handbook.pdf#page=73) |
| 10 Vectors | [83](trigonometry/trigonometry-handbook.pdf#page=83) |

## linear-algebra/

### Linear algebra textbook

`linear-algebra/linear-algebra-textbook.pdf`, 802 pages. Howard Anton and Chris Rorres, *Elementary
Linear Algebra: Applications Version*, 11th edition, Wiley, 2014. A published textbook, from systems
of equations through vector spaces, eigenvalues, inner products and the SVD. Was
`Elementary Linear Algebra 11th Edition.pdf`. The printed page number is the PDF page minus 14.

| Chapter | PDF page |
| --- | --- |
| 1 Systems of Linear Equations and Matrices | [15](linear-algebra/linear-algebra-textbook.pdf#page=15) |
| 1.1 Introduction to Systems of Linear Equations | [16](linear-algebra/linear-algebra-textbook.pdf#page=16) |
| 1.2 Gaussian Elimination | [25](linear-algebra/linear-algebra-textbook.pdf#page=25) |
| 1.3 Matrices and Matrix Operations | [39](linear-algebra/linear-algebra-textbook.pdf#page=39) |
| 1.4 Inverses; Algebraic Properties of Matrices | [53](linear-algebra/linear-algebra-textbook.pdf#page=53) |
| 1.5 Elementary Matrices and a Method for Finding A-1 | [66](linear-algebra/linear-algebra-textbook.pdf#page=66) |
| 1.6 More on Linear Systems and Invertible Matrices | [75](linear-algebra/linear-algebra-textbook.pdf#page=75) |
| 1.7 Diagonal, Triangular, and Symmetric Matrices | [81](linear-algebra/linear-algebra-textbook.pdf#page=81) |
| 1.8 Matrix Transformations | [89](linear-algebra/linear-algebra-textbook.pdf#page=89) |
| 1.9 Applications of Linear Systems | [98](linear-algebra/linear-algebra-textbook.pdf#page=98) |
| 1.10 Application: Leontief Input-Output Models | [110](linear-algebra/linear-algebra-textbook.pdf#page=110) |
| 2 Determinants | [119](linear-algebra/linear-algebra-textbook.pdf#page=119) |
| 2.1 Determinants by Cofactor Expansion | [119](linear-algebra/linear-algebra-textbook.pdf#page=119) |
| 2.2 Evaluating Determinants by Row Reduction | [127](linear-algebra/linear-algebra-textbook.pdf#page=127) |
| 2.3 Properties of Determinants; Cramer’s Rule | [132](linear-algebra/linear-algebra-textbook.pdf#page=132) |
| 3 Euclidean Vector Spaces | [145](linear-algebra/linear-algebra-textbook.pdf#page=145) |
| 3.1 Vectors in 2-Space, 3-Space, and n-Space | [145](linear-algebra/linear-algebra-textbook.pdf#page=145) |
| 3.2 Norm, Dot Product, and Distance in Rn | [156](linear-algebra/linear-algebra-textbook.pdf#page=156) |
| 3.3 Orthogonality | [169](linear-algebra/linear-algebra-textbook.pdf#page=169) |
| 3.4 The Geometry of Linear Systems | [178](linear-algebra/linear-algebra-textbook.pdf#page=178) |
| 3.5 Cross Product | [186](linear-algebra/linear-algebra-textbook.pdf#page=186) |
| 4 General Vector Spaces | [197](linear-algebra/linear-algebra-textbook.pdf#page=197) |
| 4.1 Real Vector Spaces | [197](linear-algebra/linear-algebra-textbook.pdf#page=197) |
| 4.2 Subspaces | [205](linear-algebra/linear-algebra-textbook.pdf#page=205) |
| 4.3 Linear Independence | [216](linear-algebra/linear-algebra-textbook.pdf#page=216) |
| 4.4 Coordinates and Basis | [226](linear-algebra/linear-algebra-textbook.pdf#page=226) |
| 4.5 Dimension | [235](linear-algebra/linear-algebra-textbook.pdf#page=235) |
| 4.6 Change of Basis | [243](linear-algebra/linear-algebra-textbook.pdf#page=243) |
| 4.7 Row Space, Column Space, and Null Space | [251](linear-algebra/linear-algebra-textbook.pdf#page=251) |
| 4.8 Rank, Nullity, and the Fundamental Matrix Spaces | [262](linear-algebra/linear-algebra-textbook.pdf#page=262) |
| 4.9 Basic Matrix Transformations in R2 and R3 | [273](linear-algebra/linear-algebra-textbook.pdf#page=273) |
| 4.10 Properties of Matrix Transformations | [284](linear-algebra/linear-algebra-textbook.pdf#page=284) |
| 4.11 Application: Geometry of Matrix Operators on R2 | [294](linear-algebra/linear-algebra-textbook.pdf#page=294) |
| 5 Eigenvalues and Eigenvectors | [305](linear-algebra/linear-algebra-textbook.pdf#page=305) |
| 5.1 Eigenvalues and Eigenvectors | [305](linear-algebra/linear-algebra-textbook.pdf#page=305) |
| 5.2 Diagonalization | [316](linear-algebra/linear-algebra-textbook.pdf#page=316) |
| 5.3 Complex Vector Spaces | [327](linear-algebra/linear-algebra-textbook.pdf#page=327) |
| 5.4 Application: Differential Equations | [340](linear-algebra/linear-algebra-textbook.pdf#page=340) |
| 5.5 Application: Dynamical Systems and Markov Chains | [346](linear-algebra/linear-algebra-textbook.pdf#page=346) |
| 6 Inner Product Spaces | [359](linear-algebra/linear-algebra-textbook.pdf#page=359) |
| 6.1 Inner Products | [359](linear-algebra/linear-algebra-textbook.pdf#page=359) |
| 6.2 Angle and Orthogonality in Inner Product Spaces | [369](linear-algebra/linear-algebra-textbook.pdf#page=369) |
| 6.3 Gram–Schmidt Process; QR-Decomposition | [378](linear-algebra/linear-algebra-textbook.pdf#page=378) |
| 6.4 Best Approximation; Least Squares | [392](linear-algebra/linear-algebra-textbook.pdf#page=392) |
| 6.5 Application: Mathematical Modeling Using Least Squares | [401](linear-algebra/linear-algebra-textbook.pdf#page=401) |
| 6.6 Application: Function Approximation; Fourier Series | [408](linear-algebra/linear-algebra-textbook.pdf#page=408) |
| 7 Diagonalization and Quadratic Forms | [415](linear-algebra/linear-algebra-textbook.pdf#page=415) |
| 7.1 Orthogonal Matrices | [415](linear-algebra/linear-algebra-textbook.pdf#page=415) |
| 7.2 Orthogonal Diagonalization | [423](linear-algebra/linear-algebra-textbook.pdf#page=423) |
| 7.3 Quadratic Forms | [431](linear-algebra/linear-algebra-textbook.pdf#page=431) |
| 7.4 Optimization Using Quadratic Forms | [443](linear-algebra/linear-algebra-textbook.pdf#page=443) |
| 7.5 Hermitian, Unitary, and Normal Matrices | [451](linear-algebra/linear-algebra-textbook.pdf#page=451) |
| 8 General Linear Transformations | [461](linear-algebra/linear-algebra-textbook.pdf#page=461) |
| 8.1 General Linear Transformations | [461](linear-algebra/linear-algebra-textbook.pdf#page=461) |
| 8.2 Compositions and Inverse Transformations | [472](linear-algebra/linear-algebra-textbook.pdf#page=472) |
| 8.3 Isomorphism | [480](linear-algebra/linear-algebra-textbook.pdf#page=480) |
| 8.4 Matrices for General Linear Transformations | [486](linear-algebra/linear-algebra-textbook.pdf#page=486) |
| 8.5 Similarity | [495](linear-algebra/linear-algebra-textbook.pdf#page=495) |
| 9 Numerical Methods | [505](linear-algebra/linear-algebra-textbook.pdf#page=505) |
| 9.1 LU-Decompositions | [505](linear-algebra/linear-algebra-textbook.pdf#page=505) |
| 9.2 The Power Method | [515](linear-algebra/linear-algebra-textbook.pdf#page=515) |
| 9.3 Comparison of Procedures for Solving Linear Systems | [523](linear-algebra/linear-algebra-textbook.pdf#page=523) |
| 9.4 Singular Value Decomposition | [528](linear-algebra/linear-algebra-textbook.pdf#page=528) |
| 9.5 Application: Data Compression Using Singular Value Decomposition | [535](linear-algebra/linear-algebra-textbook.pdf#page=535) |
| 10 Applications of Linear Algebra | [541](linear-algebra/linear-algebra-textbook.pdf#page=541) |
| 10.1 Constructing Curves and Surfaces Through Specified Points | [542](linear-algebra/linear-algebra-textbook.pdf#page=542) |
| 10.2 The Earliest Applications of Linear Algebra | [547](linear-algebra/linear-algebra-textbook.pdf#page=547) |
| 10.3 Cubic Spline Interpolation | [554](linear-algebra/linear-algebra-textbook.pdf#page=554) |
| 10.4 Markov Chains | [565](linear-algebra/linear-algebra-textbook.pdf#page=565) |
| 10.5 Graph Theory | [575](linear-algebra/linear-algebra-textbook.pdf#page=575) |
| 10.6 Games of Strategy | [584](linear-algebra/linear-algebra-textbook.pdf#page=584) |
| 10.7 Leontief Economic Models | [593](linear-algebra/linear-algebra-textbook.pdf#page=593) |
| 10.8 Forest Management | [602](linear-algebra/linear-algebra-textbook.pdf#page=602) |
| 10.9 Computer Graphics | [609](linear-algebra/linear-algebra-textbook.pdf#page=609) |
| 10.10 Equilibrium Temperature Distributions | [617](linear-algebra/linear-algebra-textbook.pdf#page=617) |
| 10.11 Computed Tomography | [627](linear-algebra/linear-algebra-textbook.pdf#page=627) |
| 10.12 Fractals | [638](linear-algebra/linear-algebra-textbook.pdf#page=638) |
| 10.13 Chaos | [653](linear-algebra/linear-algebra-textbook.pdf#page=653) |
| 10.14 Cryptography | [666](linear-algebra/linear-algebra-textbook.pdf#page=666) |
| 10.15 Genetics | [677](linear-algebra/linear-algebra-textbook.pdf#page=677) |
| 10.16 Age-Specific Population Growth | [687](linear-algebra/linear-algebra-textbook.pdf#page=687) |
| 10.17 Harvesting of Animal Populations | [697](linear-algebra/linear-algebra-textbook.pdf#page=697) |
| 10.18 A Least Squares Model for Human Hearing | [705](linear-algebra/linear-algebra-textbook.pdf#page=705) |
| 10.19 Warps and Morphs | [711](linear-algebra/linear-algebra-textbook.pdf#page=711) |
| 10.20 Internet Search Engines | [720](linear-algebra/linear-algebra-textbook.pdf#page=720) |
| A Working with Proofs | [729](linear-algebra/linear-algebra-textbook.pdf#page=729) |
| B Complex Numbers | [733](linear-algebra/linear-algebra-textbook.pdf#page=733) |
| Answers to Exercises | [741](linear-algebra/linear-algebra-textbook.pdf#page=741) |

### The Matrix Cookbook

`linear-algebra/matrix-cookbook.pdf`, 72 pages. Petersen and Pedersen, *The Matrix Cookbook*, version
of 15 November 2012. Was `matrixcookbook.pdf`.

| Section | PDF page |
| --- | --- |
| 1 Basics | [6](linear-algebra/matrix-cookbook.pdf#page=6) |
| 2 Derivatives | [8](linear-algebra/matrix-cookbook.pdf#page=8) |
| 3 Inverses | [17](linear-algebra/matrix-cookbook.pdf#page=17) |
| 4 Complex Matrices | [24](linear-algebra/matrix-cookbook.pdf#page=24) |
| 5 Solutions and Decompositions | [28](linear-algebra/matrix-cookbook.pdf#page=28) |
| 6 Statistics and Probability | [34](linear-algebra/matrix-cookbook.pdf#page=34) |
| 7 Multivariate Distributions | [37](linear-algebra/matrix-cookbook.pdf#page=37) |
| 8 Gaussians | [40](linear-algebra/matrix-cookbook.pdf#page=40) |
| 9 Special Matrices | [46](linear-algebra/matrix-cookbook.pdf#page=46) |
| 10 Functions and Operators | [58](linear-algebra/matrix-cookbook.pdf#page=58) |
| A One-dimensional Results | [64](linear-algebra/matrix-cookbook.pdf#page=64) |
| B Proofs and Details | [66](linear-algebra/matrix-cookbook.pdf#page=66) |

### Matrix multiplication

`linear-algebra/matrix-multiplication.pdf`, 16 pages. Own notes, 4 April 2024: the compatibility check
and the dot-product rule for each entry. Was `Linear Algebra.pdf`.

### Matrix-vector multiplication

`linear-algebra/matrix-vector-multiplication.pdf`, 1 page. Own notes. Was
`Martix Vector Multiplcation.pdf`.

### Function evaluation and the dot product

`linear-algebra/function-evaluation-vs-dot-product.pdf`, 1 page. Own notes, 25 March 2021. Was
`Function Evaluation vs Dot Product.pdf`.

### Euclidean vector spaces

`linear-algebra/euclidean-vector-spaces.pdf`, 50 pages. Own notes from the Linear Algebra: Vector Spaces
series, 5 December 2022. Was `Euclidean Vector Spaces.pdf`.

### Spectral normalization

`linear-algebra/spectral-normalization.pdf`, 5 pages. Own notes from the Matrix Decompositions series,
23 January 2022: the spectral norm, then spectral normalization for GANs. Was
`Spectral Normalization.pdf`.

## calculus/

### Calculus textbook

`calculus/calculus-textbook.pdf`, 1318 pages. Howard Anton, Irl Bivens and Stephen Davis, *Calculus:
Early Transcendentals*, 10th edition, Wiley, 2012. A published textbook, single-variable through
vector calculus: derivatives and the chain rule, integration techniques, Taylor series, partial
derivatives and gradients, multiple integrals and Jacobians. Was
`Calculus Early Transcendentals, 10th Edition ( PDFDrive ).pdf`. The printed page number is the PDF
page minus 24.

| Chapter | PDF page |
| --- | --- |
| 0 Before Calculus | [25](calculus/calculus-textbook.pdf#page=25) |
| 0.1 Functions | [25](calculus/calculus-textbook.pdf#page=25) |
| 0.2 New Functions from Old | [39](calculus/calculus-textbook.pdf#page=39) |
| 0.3 Families of Functions | [51](calculus/calculus-textbook.pdf#page=51) |
| 0.4 Inverse Functions; Inverse Trigonometric Functions | [62](calculus/calculus-textbook.pdf#page=62) |
| 0.5 Exponential and Logarithmic Functions | [76](calculus/calculus-textbook.pdf#page=76) |
| 1 Limits and Continuity | [91](calculus/calculus-textbook.pdf#page=91) |
| 1.1 Limits (An Intuitive Approach) | [91](calculus/calculus-textbook.pdf#page=91) |
| 1.2 Computing Limits | [104](calculus/calculus-textbook.pdf#page=104) |
| 1.3 Limits at Infinity; End Behavior of a Function | [113](calculus/calculus-textbook.pdf#page=113) |
| 1.4 Limits (Discussed More Rigorously) | [124](calculus/calculus-textbook.pdf#page=124) |
| 1.5 Continuity | [134](calculus/calculus-textbook.pdf#page=134) |
| 1.6 Continuity of Trigonometric, Exponential, and Inverse Functions | [145](calculus/calculus-textbook.pdf#page=145) |
| 2 The Derivative | [155](calculus/calculus-textbook.pdf#page=155) |
| 2.1 Tangent Lines and Rates of Change | [155](calculus/calculus-textbook.pdf#page=155) |
| 2.2 The Derivative Function | [167](calculus/calculus-textbook.pdf#page=167) |
| 2.3 Introduction to Techniques of Differentiation | [179](calculus/calculus-textbook.pdf#page=179) |
| 2.4 The Product and Quotient Rules | [187](calculus/calculus-textbook.pdf#page=187) |
| 2.5 Derivatives of Trigonometric Functions | [193](calculus/calculus-textbook.pdf#page=193) |
| 2.6 The Chain Rule | [198](calculus/calculus-textbook.pdf#page=198) |
| 3 Topics in Differentiation | [209](calculus/calculus-textbook.pdf#page=209) |
| 3.1 Implicit Differentiation | [209](calculus/calculus-textbook.pdf#page=209) |
| 3.2 Derivatives of Logarithmic Functions | [216](calculus/calculus-textbook.pdf#page=216) |
| 3.3 Derivatives of Exponential and Inverse Trigonometric Functions | [221](calculus/calculus-textbook.pdf#page=221) |
| 3.4 Related Rates | [228](calculus/calculus-textbook.pdf#page=228) |
| 3.5 Local Linear Approximation; Differentials | [236](calculus/calculus-textbook.pdf#page=236) |
| 3.6 L'Hôpital's Rule; Indeterminate Forms | [243](calculus/calculus-textbook.pdf#page=243) |
| 4 The Derivative in Graphing and Applications | [256](calculus/calculus-textbook.pdf#page=256) |
| 4.1 Analysis of Functions I: Increase, Decrease, and Concavity | [256](calculus/calculus-textbook.pdf#page=256) |
| 4.2 Analysis of Functions II: Relative Extrema; Graphing Polynomials | [268](calculus/calculus-textbook.pdf#page=268) |
| 4.3 Analysis of Functions III: Rational Functions, Cusps, and Vertical Tangents | [278](calculus/calculus-textbook.pdf#page=278) |
| 4.4 Absolute Maxima and Minima | [290](calculus/calculus-textbook.pdf#page=290) |
| 4.5 Applied Maximum and Minimum Problems | [298](calculus/calculus-textbook.pdf#page=298) |
| 4.6 Rectilinear Motion | [312](calculus/calculus-textbook.pdf#page=312) |
| 4.7 Newton's Method | [320](calculus/calculus-textbook.pdf#page=320) |
| 4.8 Rolle's Theorem; Mean-Value Theorem | [326](calculus/calculus-textbook.pdf#page=326) |
| 5 Integration | [340](calculus/calculus-textbook.pdf#page=340) |
| 5.1 An Overview of the Area Problem | [340](calculus/calculus-textbook.pdf#page=340) |
| 5.2 The Indefinite Integral | [346](calculus/calculus-textbook.pdf#page=346) |
| 5.3 Integration by Substitution | [356](calculus/calculus-textbook.pdf#page=356) |
| 5.4 The Definition of Area as a Limit; Sigma Notation | [364](calculus/calculus-textbook.pdf#page=364) |
| 5.5 The Definite Integral | [377](calculus/calculus-textbook.pdf#page=377) |
| 5.6 The Fundamental Theorem of Calculus | [386](calculus/calculus-textbook.pdf#page=386) |
| 5.7 Rectilinear Motion Revisited Using Integration | [400](calculus/calculus-textbook.pdf#page=400) |
| 5.8 Average Value of a Function and its Applications | [409](calculus/calculus-textbook.pdf#page=409) |
| 5.9 Evaluating Definite Integrals by Substitution | [414](calculus/calculus-textbook.pdf#page=414) |
| 5.10 Logarithmic and Other Functions Defined by Integrals | [420](calculus/calculus-textbook.pdf#page=420) |
| 6 Applications of the Definite Integral in Geometry, Science, and Engineering | [437](calculus/calculus-textbook.pdf#page=437) |
| 6.1 Area Between Two Curves | [437](calculus/calculus-textbook.pdf#page=437) |
| 6.2 Volumes by Slicing; Disks and Washers | [445](calculus/calculus-textbook.pdf#page=445) |
| 6.3 Volumes by Cylindrical Shells | [456](calculus/calculus-textbook.pdf#page=456) |
| 6.4 Length of a Plane Curve | [462](calculus/calculus-textbook.pdf#page=462) |
| 6.5 Area of a Surface of Revolution | [468](calculus/calculus-textbook.pdf#page=468) |
| 6.6 Work | [473](calculus/calculus-textbook.pdf#page=473) |
| 6.7 Moments, Centers of Gravity, and Centroids | [482](calculus/calculus-textbook.pdf#page=482) |
| 6.8 Fluid Pressure and Force | [491](calculus/calculus-textbook.pdf#page=491) |
| 6.9 Hyperbolic Functions and Hanging Cables | [498](calculus/calculus-textbook.pdf#page=498) |
| 7 Principles of Integral Evaluation | [512](calculus/calculus-textbook.pdf#page=512) |
| 7.1 An Overview of Integration Methods | [512](calculus/calculus-textbook.pdf#page=512) |
| 7.2 Integration by Parts | [515](calculus/calculus-textbook.pdf#page=515) |
| 7.3 Integrating Trigonometric Functions | [524](calculus/calculus-textbook.pdf#page=524) |
| 7.4 Trigonometric Substitutions | [532](calculus/calculus-textbook.pdf#page=532) |
| 7.5 Integrating Rational Functions by Partial Fractions | [538](calculus/calculus-textbook.pdf#page=538) |
| 7.6 Using Computer Algebra Systems and Tables of Integrals | [547](calculus/calculus-textbook.pdf#page=547) |
| 7.7 Numerical Integration; Simpson's Rule | [557](calculus/calculus-textbook.pdf#page=557) |
| 7.8 Improper Integrals | [571](calculus/calculus-textbook.pdf#page=571) |
| 8 Mathematical Modeling with Differential Equations | [585](calculus/calculus-textbook.pdf#page=585) |
| 8.1 Modeling with Differential Equations | [585](calculus/calculus-textbook.pdf#page=585) |
| 8.2 Separation of Variables | [592](calculus/calculus-textbook.pdf#page=592) |
| 8.3 Slope Fields; Euler's Method | [603](calculus/calculus-textbook.pdf#page=603) |
| 8.4 First-Order Differential Equations and Applications | [610](calculus/calculus-textbook.pdf#page=610) |
| 9 Infinite Series | [620](calculus/calculus-textbook.pdf#page=620) |
| 9.1 Sequences | [620](calculus/calculus-textbook.pdf#page=620) |
| 9.2 Monotone Sequences | [631](calculus/calculus-textbook.pdf#page=631) |
| 9.3 Infinite Series | [638](calculus/calculus-textbook.pdf#page=638) |
| 9.4 Convergence Tests | [647](calculus/calculus-textbook.pdf#page=647) |
| 9.5 The Comparison, Ratio, and Root Tests | [655](calculus/calculus-textbook.pdf#page=655) |
| 9.6 Alternating Series; Absolute and Conditional Convergence | [662](calculus/calculus-textbook.pdf#page=662) |
| 9.7 Maclaurin and Taylor Polynomials | [672](calculus/calculus-textbook.pdf#page=672) |
| 9.8 Maclaurin and Taylor Series; Power Series | [683](calculus/calculus-textbook.pdf#page=683) |
| 9.9 Convergence of Taylor Series | [692](calculus/calculus-textbook.pdf#page=692) |
| 9.10 Differentiating and Integrating Power Series; Modeling with Taylor Series | [702](calculus/calculus-textbook.pdf#page=702) |
| 10 Parametric and Polar Curves; Conic Sections | [716](calculus/calculus-textbook.pdf#page=716) |
| 10.1 Parametric Equations; Tangent Lines and Arc Length for Parametric Curves | [716](calculus/calculus-textbook.pdf#page=716) |
| 10.2 Polar Coordinates | [729](calculus/calculus-textbook.pdf#page=729) |
| 10.3 Tangent Lines, Arc Length, and Area for Polar Curves | [743](calculus/calculus-textbook.pdf#page=743) |
| 10.4 Conic Sections | [754](calculus/calculus-textbook.pdf#page=754) |
| 10.5 Rotation of Axes; Second-Degree Equations | [772](calculus/calculus-textbook.pdf#page=772) |
| 10.6 Conic Sections in Polar Coordinates | [778](calculus/calculus-textbook.pdf#page=778) |
| 11 Three-Dimensional Space; Vectors | [791](calculus/calculus-textbook.pdf#page=791) |
| 11.1 Rectangular Coordinates in 3-Space; Spheres; Cylindrical Surfaces | [791](calculus/calculus-textbook.pdf#page=791) |
| 11.2 Vectors | [797](calculus/calculus-textbook.pdf#page=797) |
| 11.3 Dot Product; Projections | [809](calculus/calculus-textbook.pdf#page=809) |
| 11.4 Cross Product | [819](calculus/calculus-textbook.pdf#page=819) |
| 11.5 Parametric Equations of Lines | [829](calculus/calculus-textbook.pdf#page=829) |
| 11.6 Planes in 3-Space | [837](calculus/calculus-textbook.pdf#page=837) |
| 11.7 Quadric Surfaces | [845](calculus/calculus-textbook.pdf#page=845) |
| 11.8 Cylindrical and Spherical Coordinates | [856](calculus/calculus-textbook.pdf#page=856) |
| 12 Vector-Valued Functions | [865](calculus/calculus-textbook.pdf#page=865) |
| 12.1 Introduction to Vector-Valued Functions | [865](calculus/calculus-textbook.pdf#page=865) |
| 12.2 Calculus of Vector-Valued Functions | [872](calculus/calculus-textbook.pdf#page=872) |
| 12.3 Change of Parameter; Arc Length | [882](calculus/calculus-textbook.pdf#page=882) |
| 12.4 Unit Tangent, Normal, and Binormal Vectors | [892](calculus/calculus-textbook.pdf#page=892) |
| 12.5 Curvature | [897](calculus/calculus-textbook.pdf#page=897) |
| 12.6 Motion Along a Curve | [906](calculus/calculus-textbook.pdf#page=906) |
| 12.7 Kepler's Laws of Planetary Motion | [919](calculus/calculus-textbook.pdf#page=919) |
| 13 Partial Derivatives | [930](calculus/calculus-textbook.pdf#page=930) |
| 13.1 Functions of Two or More Variables | [930](calculus/calculus-textbook.pdf#page=930) |
| 13.2 Limits and Continuity | [941](calculus/calculus-textbook.pdf#page=941) |
| 13.3 Partial Derivatives | [951](calculus/calculus-textbook.pdf#page=951) |
| 13.4 Differentiability, Differentials, and Local Linearity | [964](calculus/calculus-textbook.pdf#page=964) |
| 13.5 The Chain Rule | [973](calculus/calculus-textbook.pdf#page=973) |
| 13.6 Directional Derivatives and Gradients | [984](calculus/calculus-textbook.pdf#page=984) |
| 13.7 Tangent Planes and Normal Vectors | [995](calculus/calculus-textbook.pdf#page=995) |
| 13.8 Maxima and Minima of Functions of Two Variables | [1001](calculus/calculus-textbook.pdf#page=1001) |
| 13.9 Lagrange Multipliers | [1013](calculus/calculus-textbook.pdf#page=1013) |
| 14 Multiple Integrals | [1024](calculus/calculus-textbook.pdf#page=1024) |
| 14.1 Double Integrals | [1024](calculus/calculus-textbook.pdf#page=1024) |
| 14.2 Double Integrals over Nonrectangular Regions | [1033](calculus/calculus-textbook.pdf#page=1033) |
| 14.3 Double Integrals in Polar Coordinates | [1042](calculus/calculus-textbook.pdf#page=1042) |
| 14.4 Surface Area; Parametric Surfaces | [1050](calculus/calculus-textbook.pdf#page=1050) |
| 14.5 Triple Integrals | [1063](calculus/calculus-textbook.pdf#page=1063) |
| 14.6 Triple Integrals in Cylindrical and Spherical Coordinates | [1072](calculus/calculus-textbook.pdf#page=1072) |
| 14.7 Change of Variables in Multiple Integrals; Jacobians | [1083](calculus/calculus-textbook.pdf#page=1083) |
| 14.8 Centers of Gravity Using Multiple Integrals | [1095](calculus/calculus-textbook.pdf#page=1095) |
| 15 Topics in Vector Calculus | [1108](calculus/calculus-textbook.pdf#page=1108) |
| 15.1 Vector Fields | [1109](calculus/calculus-textbook.pdf#page=1109) |
| Gradient fields and conservative fields (15.1.3) | [1111](calculus/calculus-textbook.pdf#page=1111) |
| 15.2 Line Integrals | [1118](calculus/calculus-textbook.pdf#page=1118) |
| 15.3 Independence of Path; Conservative Vector Fields | [1135](calculus/calculus-textbook.pdf#page=1135) |
| 15.4 Green's Theorem | [1146](calculus/calculus-textbook.pdf#page=1146) |
| 15.5 Surface Integrals | [1154](calculus/calculus-textbook.pdf#page=1154) |
| 15.6 Applications of Surface Integrals; Flux | [1162](calculus/calculus-textbook.pdf#page=1162) |
| 15.7 The Divergence Theorem | [1172](calculus/calculus-textbook.pdf#page=1172) |
| 15.8 Stokes' Theorem | [1182](calculus/calculus-textbook.pdf#page=1182) |
| Appendices | [1193](calculus/calculus-textbook.pdf#page=1193) |
| A Graphing Functions Using Calculators and Computer Algebra Systems | [1193](calculus/calculus-textbook.pdf#page=1193) |
| B Trigonometry Review | [1205](calculus/calculus-textbook.pdf#page=1205) |
| C Solving Polynomial Equations | [1219](calculus/calculus-textbook.pdf#page=1219) |
| D Selected Proofs | [1226](calculus/calculus-textbook.pdf#page=1226) |
| Answers to Odd-Numbered Exercises | [1237](calculus/calculus-textbook.pdf#page=1237) |

### Calculus handbook

`calculus/calculus-handbook.pdf`, 242 pages. Earl, *Calculus Handbook*, version 5.6. A compact handbook for a
first-year course: limits, differentiation and its rules, integration techniques, hyperbolic functions,
definite and improper integrals, differential equations, vector calculus, series, and appendices of key
definitions, theorems and formulas. The printed page number equals the PDF page number. The table is from
the book's own contents pages.

| Chapter or topic | PDF page |
| --- | --- |
| 1 Functions and Limits | [8](calculus/calculus-handbook.pdf#page=8) |
| Functions | [8](calculus/calculus-handbook.pdf#page=8) |
| Continuity Examples | [10](calculus/calculus-handbook.pdf#page=10) |
| Limits | [11](calculus/calculus-handbook.pdf#page=11) |
| Techniques for Finding Limits | [12](calculus/calculus-handbook.pdf#page=12) |
| Indeterminate Forms | [14](calculus/calculus-handbook.pdf#page=14) |
| When Limits Fail to Exist | [16](calculus/calculus-handbook.pdf#page=16) |
| 2 Differentiation | [17](calculus/calculus-handbook.pdf#page=17) |
| Definition, Basic Rules, Product Rule | [17](calculus/calculus-handbook.pdf#page=17) |
| Quotient, Chain and Power Rules; Exponential and Logarithmic Functions | [18](calculus/calculus-handbook.pdf#page=18) |
| Trigonometric and Inverse Trigonometric Functions | [19](calculus/calculus-handbook.pdf#page=19) |
| Generalized Product Rule | [23](calculus/calculus-handbook.pdf#page=23) |
| Inverse Function Rule | [25](calculus/calculus-handbook.pdf#page=25) |
| Partial Differentiation | [26](calculus/calculus-handbook.pdf#page=26) |
| Implicit Differentiation | [27](calculus/calculus-handbook.pdf#page=27) |
| Logarithmic Differentiation | [30](calculus/calculus-handbook.pdf#page=30) |
| 3 Applications of Derivatives | [31](calculus/calculus-handbook.pdf#page=31) |
| Maxima and Minima (i.e., Extrema) | [31](calculus/calculus-handbook.pdf#page=31) |
| Inflection Points | [33](calculus/calculus-handbook.pdf#page=33) |
| Special Case: Extrema and Inflection Points of Polynomials | [34](calculus/calculus-handbook.pdf#page=34) |
| Relationship Among f(x), f'(x) and f''(x) | [35](calculus/calculus-handbook.pdf#page=35) |
| Curve Sketching | [39](calculus/calculus-handbook.pdf#page=39) |
| Determining the Shape of a Curve Based On Its Derivatives | [44](calculus/calculus-handbook.pdf#page=44) |
| Rolles's Theorem and the Mean Value Theorem (MVT) | [45](calculus/calculus-handbook.pdf#page=45) |
| Related Rates | [46](calculus/calculus-handbook.pdf#page=46) |
| Kinematics (Particle Motion) | [49](calculus/calculus-handbook.pdf#page=49) |
| Differentials | [52](calculus/calculus-handbook.pdf#page=52) |
| Curvature | [53](calculus/calculus-handbook.pdf#page=53) |
| Newton's Method | [54](calculus/calculus-handbook.pdf#page=54) |
| 4 Integration | [56](calculus/calculus-handbook.pdf#page=56) |
| Indefinite Integration (Antiderivatives) | [56](calculus/calculus-handbook.pdf#page=56) |
| Exponential and Logarithmic Functions | [57](calculus/calculus-handbook.pdf#page=57) |
| Trigonometric Functions | [57](calculus/calculus-handbook.pdf#page=57) |
| Inverse Trigonometric Functions | [60](calculus/calculus-handbook.pdf#page=60) |
| Selecting the Right Function for an Intergral | [62](calculus/calculus-handbook.pdf#page=62) |
| 5 Techniques of Integration | [63](calculus/calculus-handbook.pdf#page=63) |
| u -Substitution | [63](calculus/calculus-handbook.pdf#page=63) |
| Integration by Partial Fractions | [65](calculus/calculus-handbook.pdf#page=65) |
| Integration by Parts | [68](calculus/calculus-handbook.pdf#page=68) |
| Integration by Trigonometric Substitution | [72](calculus/calculus-handbook.pdf#page=72) |
| Gamma Function | [74](calculus/calculus-handbook.pdf#page=74) |
| Beta Function | [76](calculus/calculus-handbook.pdf#page=76) |
| Impossible Integrals | [78](calculus/calculus-handbook.pdf#page=78) |
| 6 Hyperbolic Functions | [79](calculus/calculus-handbook.pdf#page=79) |
| Definitions | [79](calculus/calculus-handbook.pdf#page=79) |
| Identities | [80](calculus/calculus-handbook.pdf#page=80) |
| Relationship to Trigonometric Functions | [81](calculus/calculus-handbook.pdf#page=81) |
| Inverse Hyperbolic Functions | [82](calculus/calculus-handbook.pdf#page=82) |
| Graphs of Hyperbolic Functions and Their Inverses | [83](calculus/calculus-handbook.pdf#page=83) |
| Derivatives | [84](calculus/calculus-handbook.pdf#page=84) |
| Integrals | [85](calculus/calculus-handbook.pdf#page=85) |
| 7 Definite Integrals | [87](calculus/calculus-handbook.pdf#page=87) |
| Riemann Sums | [87](calculus/calculus-handbook.pdf#page=87) |
| Rules of Definite Integration | [92](calculus/calculus-handbook.pdf#page=92) |
| Fundamental Theorems of Calculus | [92](calculus/calculus-handbook.pdf#page=92) |
| Properties of Definite Integrals | [94](calculus/calculus-handbook.pdf#page=94) |
| Solving Definite Integrals with Directed Line Segments | [95](calculus/calculus-handbook.pdf#page=95) |
| u -Subsitution | [96](calculus/calculus-handbook.pdf#page=96) |
| Special Techniques for Evaluation | [98](calculus/calculus-handbook.pdf#page=98) |
| Derivative of an Integral | [100](calculus/calculus-handbook.pdf#page=100) |
| 8 Applications of Integration | [101](calculus/calculus-handbook.pdf#page=101) |
| Area Under a Curve | [101](calculus/calculus-handbook.pdf#page=101) |
| Area Between Curves | [102](calculus/calculus-handbook.pdf#page=102) |
| Area in Polar Form | [103](calculus/calculus-handbook.pdf#page=103) |
| Areas of Limacons | [105](calculus/calculus-handbook.pdf#page=105) |
| Arc Length | [107](calculus/calculus-handbook.pdf#page=107) |
| Comparison of Formulas for Rectangular, Polar and Parametric Forms | [110](calculus/calculus-handbook.pdf#page=110) |
| Area of a Surface of Revolution | [111](calculus/calculus-handbook.pdf#page=111) |
| Volumes of Solids of Revolution | [112](calculus/calculus-handbook.pdf#page=112) |
| 9 Improper Integrals | [118](calculus/calculus-handbook.pdf#page=118) |
| Definite Integrals with Infinite Limits of Integration | [118](calculus/calculus-handbook.pdf#page=118) |
| Definite Integrals with Discontinuous Integrands | [119](calculus/calculus-handbook.pdf#page=119) |
| 10 Differential Equations | [120](calculus/calculus-handbook.pdf#page=120) |
| Definitions | [120](calculus/calculus-handbook.pdf#page=120) |
| Separable First Order Differential Equations | [121](calculus/calculus-handbook.pdf#page=121) |
| Slope Fields | [123](calculus/calculus-handbook.pdf#page=123) |
| Logistic Function | [124](calculus/calculus-handbook.pdf#page=124) |
| Numerical Methods | [125](calculus/calculus-handbook.pdf#page=125) |
| 11 Vector Calculus | [129](calculus/calculus-handbook.pdf#page=129) |
| Introduction | [129](calculus/calculus-handbook.pdf#page=129) |
| Special Unit Vectors | [129](calculus/calculus-handbook.pdf#page=129) |
| Vector Components | [129](calculus/calculus-handbook.pdf#page=129) |
| Properties of Vectors | [130](calculus/calculus-handbook.pdf#page=130) |
| Dot Product | [131](calculus/calculus-handbook.pdf#page=131) |
| Cross Product | [132](calculus/calculus-handbook.pdf#page=132) |
| Triple Products | [134](calculus/calculus-handbook.pdf#page=134) |
| Kinematics (Particle Motion) | [135](calculus/calculus-handbook.pdf#page=135) |
| Gradient | [136](calculus/calculus-handbook.pdf#page=136) |
| Divergence | [137](calculus/calculus-handbook.pdf#page=137) |
| Curl | [138](calculus/calculus-handbook.pdf#page=138) |
| Laplacian | [139](calculus/calculus-handbook.pdf#page=139) |
| 12 Sequences | [140](calculus/calculus-handbook.pdf#page=140) |
| Definitions and Types of Sequences | [140](calculus/calculus-handbook.pdf#page=140) |
| More Definitions and Theorems | [141](calculus/calculus-handbook.pdf#page=141) |
| Limits (Convergence and Divergence) | [142](calculus/calculus-handbook.pdf#page=142) |
| Basic Recursive Sequence Theory | [143](calculus/calculus-handbook.pdf#page=143) |
| 13 Series | [147](calculus/calculus-handbook.pdf#page=147) |
| Introduction | [147](calculus/calculus-handbook.pdf#page=147) |
| Key Properties | [148](calculus/calculus-handbook.pdf#page=148) |
| n-th Term Convergence Theorems | [148](calculus/calculus-handbook.pdf#page=148) |
| Power Series | [148](calculus/calculus-handbook.pdf#page=148) |
| Telescoping Series | [149](calculus/calculus-handbook.pdf#page=149) |
| Geometric Series | [150](calculus/calculus-handbook.pdf#page=150) |
| Estimating the Value of Series with Positive Terms | [151](calculus/calculus-handbook.pdf#page=151) |
| Riemann Zeta Function (p -Series) | [152](calculus/calculus-handbook.pdf#page=152) |
| Bernoulli Numbers | [156](calculus/calculus-handbook.pdf#page=156) |
| Convergence Tests | [158](calculus/calculus-handbook.pdf#page=158) |
| Alternating Series | [163](calculus/calculus-handbook.pdf#page=163) |
| Radius and Interval of Convergence of Power Series | [165](calculus/calculus-handbook.pdf#page=165) |
| Summary of Convergence/Divergence Tests | [168](calculus/calculus-handbook.pdf#page=168) |
| 14 Taylor and MacLaurin Series | [169](calculus/calculus-handbook.pdf#page=169) |
| Taylor Series | [169](calculus/calculus-handbook.pdf#page=169) |
| MacLaurin Series | [169](calculus/calculus-handbook.pdf#page=169) |
| LaGrange Remainder | [171](calculus/calculus-handbook.pdf#page=171) |
| 15 Miscellaneous Cool Stuff | [172](calculus/calculus-handbook.pdf#page=172) |
| e | [172](calculus/calculus-handbook.pdf#page=172) |
| Derivation of Euler's Formula | [173](calculus/calculus-handbook.pdf#page=173) |
| Logarithms of Negative Real Numbers and Complex Numbers | [175](calculus/calculus-handbook.pdf#page=175) |
| What Is i | [176](calculus/calculus-handbook.pdf#page=176) |
| z | [177](calculus/calculus-handbook.pdf#page=177) |
| Derivatives of a Circle | [178](calculus/calculus-handbook.pdf#page=178) |
| Derivatives of a Ellipse | [179](calculus/calculus-handbook.pdf#page=179) |
| Derivatives of a Hyperbola | [180](calculus/calculus-handbook.pdf#page=180) |
| 3 3 3 | [181](calculus/calculus-handbook.pdf#page=181) |
| Inflection Points of the PDF of the Normal Distribution | [182](calculus/calculus-handbook.pdf#page=182) |
| Appendix A: Key Definitions | [183](calculus/calculus-handbook.pdf#page=183) |
| Appendix B: Key Theorems | [203](calculus/calculus-handbook.pdf#page=203) |
| Appendix C: List of Key Derivatives and Integrals | [207](calculus/calculus-handbook.pdf#page=207) |
| Appendix D: Key Functions and Their Derivatives | [214](calculus/calculus-handbook.pdf#page=214) |
| Appendix E: Geometry and Trigonometry Formulas | [218](calculus/calculus-handbook.pdf#page=218) |
| Appendix F: Polar and Parametric Equations | [223](calculus/calculus-handbook.pdf#page=223) |
| Appendix G: Interesting Series | [234](calculus/calculus-handbook.pdf#page=234) |
| Index | [235](calculus/calculus-handbook.pdf#page=235) |
| Appendix A Key Definitions | [183](calculus/calculus-handbook.pdf#page=183) |
| Appendix B Key Theorems | [203](calculus/calculus-handbook.pdf#page=203) |
| Appendix C Key Derivatives and Integrals | [207](calculus/calculus-handbook.pdf#page=207) |
| Appendix D Functions and Their Derivatives | [215](calculus/calculus-handbook.pdf#page=215) |
| Appendix E Geometry and Trigonometry Formulas | [218](calculus/calculus-handbook.pdf#page=218) |

### Calculus practice problems

`calculus/calculus-practice-problems.pdf`, 626 pages. Patrick Jones and the Math Doctors, *Calculus:
1,001 Practice Problems For Dummies*, Wiley, 2014. A workbook: problems in Part I, worked answers in
Part II. Reach for it when a line asks the reader to practise a technique, and for the textbook when it
needs the technique taught. Was `Calculus Practice Problems For Dummies ( PDFDrive ).pdf`. The printed
page number is the PDF page minus 14.

| Chapter | PDF page |
| --- | --- |
| Part I: The Questions | [19](calculus/calculus-practice-problems.pdf#page=19) |
| 1 Algebra Review | [21](calculus/calculus-practice-problems.pdf#page=21) |
| 2 Trigonometry Review | [31](calculus/calculus-practice-problems.pdf#page=31) |
| 3 Limits and Rates of Change | [43](calculus/calculus-practice-problems.pdf#page=43) |
| 4 Derivative Basics | [57](calculus/calculus-practice-problems.pdf#page=57) |
| 5 The Product, Quotient, and Chain Rules | [63](calculus/calculus-practice-problems.pdf#page=63) |
| 6 Exponential and Logarithmic Functions and Tangent Lines | [69](calculus/calculus-practice-problems.pdf#page=69) |
| 7 Implicit Differentiation | [73](calculus/calculus-practice-problems.pdf#page=73) |
| 8 Applications of Derivatives | [77](calculus/calculus-practice-problems.pdf#page=77) |
| 9 Areas and Riemann Sums | [89](calculus/calculus-practice-problems.pdf#page=89) |
| 10 The Fundamental Theorem of Calculus and the Net Change Theorem | [93](calculus/calculus-practice-problems.pdf#page=93) |
| 11 Applications of Integration | [101](calculus/calculus-practice-problems.pdf#page=101) |
| 12 Inverse Trigonometric Functions, Hyperbolic Functions, and L’Hôpital’s Rule | [113](calculus/calculus-practice-problems.pdf#page=113) |
| 13 U-Substitution and Integration by Parts | [121](calculus/calculus-practice-problems.pdf#page=121) |
| 14 Trigonometric Integrals, Trigonometric Substitution, and Partial Fractions | [127](calculus/calculus-practice-problems.pdf#page=127) |
| 15 Improper Integrals and More Approximating Techniques | [135](calculus/calculus-practice-problems.pdf#page=135) |
| Part II: The Answers | [139](calculus/calculus-practice-problems.pdf#page=139) |
| 16 Answers and Explanations | [141](calculus/calculus-practice-problems.pdf#page=141) |

### Integration and series notes

`calculus/integration-and-series-notes.pdf`, 127 pages. *2nd Semester Calculus Lecture Manual*,
MATH1036/7, University of the Witwatersrand, 2013. Lecture notes, numbered from chapter 7: hyperbolic
functions, the definite integral, integration techniques, improper integrals, sequences and series.
Was `Calculus Semester 2 Notes.pdf`. No embedded outline; this table is from the printed contents. The
printed page number is the PDF page minus 2.

| Chapter | PDF page |
| --- | --- |
| 7 Hyperbolic Functions | [3](calculus/integration-and-series-notes.pdf#page=3) |
| 8 Integration Theory and Applications | [4](calculus/integration-and-series-notes.pdf#page=4) |
| 8.1 Riemann Sums and Area Approximation | [4](calculus/integration-and-series-notes.pdf#page=4) |
| 8.2 Area with the Definite Integral | [12](calculus/integration-and-series-notes.pdf#page=12) |
| 8.3 Solids of Revolution | [26](calculus/integration-and-series-notes.pdf#page=26) |
| 8.4 Volumes by Slicing | [37](calculus/integration-and-series-notes.pdf#page=37) |
| 8.5 The Definite Integral as a Function | [41](calculus/integration-and-series-notes.pdf#page=41) |
| 9 Advanced Integration Techniques | [45](calculus/integration-and-series-notes.pdf#page=45) |
| 9.1 Inverse Trigonometric, Exponential and Logarithmic Integrals | [45](calculus/integration-and-series-notes.pdf#page=45) |
| 9.2 Integration by Parts Revisited | [50](calculus/integration-and-series-notes.pdf#page=50) |
| 9.3 Trigonometric Substitutions | [53](calculus/integration-and-series-notes.pdf#page=53) |
| 9.4 Trigonometric Integrals | [57](calculus/integration-and-series-notes.pdf#page=57) |
| 9.5 Partial Fraction Decomposition | [64](calculus/integration-and-series-notes.pdf#page=64) |
| 10 Improper Integrals | [75](calculus/integration-and-series-notes.pdf#page=75) |
| 10.1 Type I: Infinite Interval of Integration | [76](calculus/integration-and-series-notes.pdf#page=76) |
| 10.2 Type II: Infinite Discontinuities | [81](calculus/integration-and-series-notes.pdf#page=81) |
| 11 Infinite Sequences and Series | [87](calculus/integration-and-series-notes.pdf#page=87) |
| 11.1 Sequences | [87](calculus/integration-and-series-notes.pdf#page=87) |
| 11.2 Series | [92](calculus/integration-and-series-notes.pdf#page=92) |
| 11.3 Convergence Tests for Series | [96](calculus/integration-and-series-notes.pdf#page=96) |

### The gamma function

`calculus/gamma-function.pdf`, 5 pages. Own notes from the Mathematical Statistics series, 2 September
2021: the gamma function and a proof by induction that Γ(n) = (n − 1)!. Was `Gamma Function.pdf`.

### Stochastic differential equations

`calculus/stochastic-differential-equations.pdf`, 429 pages. Uffe Høgsbro Thygesen, *Stochastic Differential
Equations for Science and Engineering*, 1st edition, CRC Press, 2023, in the author's preprint of 11 July 2023
from DTU Orbit (page numbers differ from the printed book; solutions to selected exercises are included). A
published textbook in preprint form: probability spaces and conditional expectation, Brownian motion, the Itô
integral and Itô's lemma, Euler-Maruyama and other numerical schemes, the forward and backward Kolmogorov
(Fokker-Planck) equations, filtering and stochastic control. Was
`Thygesen_2023_SDEs_for_science_and_engineering_PREPRINT.pdf`. The printed page number is the PDF page minus
10; the solutions restart their own numbering at 1 on PDF page 386.

| Chapter | PDF page |
| --- | --- |
| 1 Introduction | [11](calculus/stochastic-differential-equations.pdf#page=11) |
| Part I Fundamentals | [19](calculus/stochastic-differential-equations.pdf#page=19) |
| 2 Diffusive Transport and Random Walks | [20](calculus/stochastic-differential-equations.pdf#page=20) |
| 2.1 Diffusive Transport | [21](calculus/stochastic-differential-equations.pdf#page=21) |
| 2.2 Advective and Diffusive Transport | [28](calculus/stochastic-differential-equations.pdf#page=28) |
| 2.3 Diffusion in More Than One Dimension | [29](calculus/stochastic-differential-equations.pdf#page=29) |
| 2.4 Relative Importance of Advection and Diffusion | [31](calculus/stochastic-differential-equations.pdf#page=31) |
| 2.5 The Motion of a Single Molecule | [33](calculus/stochastic-differential-equations.pdf#page=33) |
| 2.6 Monte Carlo Simulation of Particle Motion | [35](calculus/stochastic-differential-equations.pdf#page=35) |
| 3 Stochastic Experiments and Probability Spaces | [40](calculus/stochastic-differential-equations.pdf#page=40) |
| 3.1 Stochastic Experiments | [41](calculus/stochastic-differential-equations.pdf#page=41) |
| 3.2 Random Variables | [45](calculus/stochastic-differential-equations.pdf#page=45) |
| 3.3 Expectation is Integration | [47](calculus/stochastic-differential-equations.pdf#page=47) |
| 3.4 Information is a σ-Algebra | [49](calculus/stochastic-differential-equations.pdf#page=49) |
| 3.5 Conditional Expectations | [51](calculus/stochastic-differential-equations.pdf#page=51) |
| 3.6 Independence and Conditional Independence | [56](calculus/stochastic-differential-equations.pdf#page=56) |
| 3.7 Linear Spaces of Random Variables | [58](calculus/stochastic-differential-equations.pdf#page=58) |
| 4 Brownian Motion | [74](calculus/stochastic-differential-equations.pdf#page=74) |
| 4.1 Stochastic processes and random functions | [75](calculus/stochastic-differential-equations.pdf#page=75) |
| 4.2 Definition of Brownian motion | [75](calculus/stochastic-differential-equations.pdf#page=75) |
| 4.3 Properties of Brownian Motion | [77](calculus/stochastic-differential-equations.pdf#page=77) |
| 4.4 Filtrations and accumulation of information | [88](calculus/stochastic-differential-equations.pdf#page=88) |
| 4.5 The martingale property | [89](calculus/stochastic-differential-equations.pdf#page=89) |
| 5 Linear Dynamic Systems | [101](calculus/stochastic-differential-equations.pdf#page=101) |
| 5.1 Linear Systems with Deterministic Inputs | [102](calculus/stochastic-differential-equations.pdf#page=102) |
| 5.2 Linear Systems in the Frequency Domain | [104](calculus/stochastic-differential-equations.pdf#page=104) |
| 5.3 A Linear System Driven by Noise | [106](calculus/stochastic-differential-equations.pdf#page=106) |
| 5.4 Stationary Processes in Time Domain | [108](calculus/stochastic-differential-equations.pdf#page=108) |
| 5.5 Stationary Processes in Frequency Domain | [110](calculus/stochastic-differential-equations.pdf#page=110) |
| 5.6 The Response to Noise | [111](calculus/stochastic-differential-equations.pdf#page=111) |
| 5.7 The White Noise Limit | [113](calculus/stochastic-differential-equations.pdf#page=113) |
| 5.8 Integrated White Noise is Brownian Motion | [115](calculus/stochastic-differential-equations.pdf#page=115) |
| 5.9 Linear Systems Driven by White Noise | [117](calculus/stochastic-differential-equations.pdf#page=117) |
| 5.10 The Ornstein-Uhlenbeck Process | [120](calculus/stochastic-differential-equations.pdf#page=120) |
| 5.11 The Noisy Harmonic Oscillator | [121](calculus/stochastic-differential-equations.pdf#page=121) |
| Part II Stochastic Calculus | [128](calculus/stochastic-differential-equations.pdf#page=128) |
| 6 Stochastic integrals | [129](calculus/stochastic-differential-equations.pdf#page=129) |
| 6.1 Ordinary Differential Equations Driven by Noise | [130](calculus/stochastic-differential-equations.pdf#page=130) |
| 6.2 Some Exemplary Equations | [132](calculus/stochastic-differential-equations.pdf#page=132) |
| 6.3 The Itô Integral and its Properties | [135](calculus/stochastic-differential-equations.pdf#page=135) |
| 6.4 A Cautionary Example: ∫ B dB | [139](calculus/stochastic-differential-equations.pdf#page=139) |
| 6.5 Itô Processes and Solutions to SDEs | [142](calculus/stochastic-differential-equations.pdf#page=142) |
| 6.6 Relaxing the L2 Constraint | [144](calculus/stochastic-differential-equations.pdf#page=144) |
| 6.7 Integration with Respect to Itô Processes | [145](calculus/stochastic-differential-equations.pdf#page=145) |
| 6.8 The Stratonovich Integral | [146](calculus/stochastic-differential-equations.pdf#page=146) |
| 6.9 Calculus of Cross-Variations | [148](calculus/stochastic-differential-equations.pdf#page=148) |
| 7 The Stochastic Chain Rule | [154](calculus/stochastic-differential-equations.pdf#page=154) |
| 7.1 The Chain Rule of Deterministic Calculus | [155](calculus/stochastic-differential-equations.pdf#page=155) |
| 7.2 Transformations of Random Variables | [155](calculus/stochastic-differential-equations.pdf#page=155) |
| 7.3 Itô's Lemma: The Stochastic Chain Rule | [156](calculus/stochastic-differential-equations.pdf#page=156) |
| 7.4 Some SDE's with Analytical Solutions | [159](calculus/stochastic-differential-equations.pdf#page=159) |
| 7.5 Dynamics of Derived Quantities | [163](calculus/stochastic-differential-equations.pdf#page=163) |
| 7.6 Coordinate Transformations | [165](calculus/stochastic-differential-equations.pdf#page=165) |
| 7.7 Time Change | [169](calculus/stochastic-differential-equations.pdf#page=169) |
| 7.8 Stratonovich Calculus | [172](calculus/stochastic-differential-equations.pdf#page=172) |
| 8 Existence, Uniqueness, and Numerics | [180](calculus/stochastic-differential-equations.pdf#page=180) |
| 8.1 The Initial Value Problem | [181](calculus/stochastic-differential-equations.pdf#page=181) |
| 8.2 Uniqueness of Solutions | [181](calculus/stochastic-differential-equations.pdf#page=181) |
| 8.3 Existence of Solutions | [185](calculus/stochastic-differential-equations.pdf#page=185) |
| 8.4 Numerical Simulation of Sample Paths | [189](calculus/stochastic-differential-equations.pdf#page=189) |
| 9 The Kolmogorov equations | [204](calculus/stochastic-differential-equations.pdf#page=204) |
| 9.1 Brownian Motion is a Markov Process | [205](calculus/stochastic-differential-equations.pdf#page=205) |
| 9.2 Diffusions are Markov Processes | [206](calculus/stochastic-differential-equations.pdf#page=206) |
| 9.3 Transition Probabilities and Densities | [207](calculus/stochastic-differential-equations.pdf#page=207) |
| 9.4 The Backward Kolmogorov Equation | [211](calculus/stochastic-differential-equations.pdf#page=211) |
| 9.5 The Forward Kolmogorov Equation | [214](calculus/stochastic-differential-equations.pdf#page=214) |
| 9.6 Different Forms of the Kolmogorov Equations | [216](calculus/stochastic-differential-equations.pdf#page=216) |
| 9.7 Drift, Noise Intensity, Advection, and Diffusion | [218](calculus/stochastic-differential-equations.pdf#page=218) |
| 9.8 Stationary Distributions | [219](calculus/stochastic-differential-equations.pdf#page=219) |
| 9.9 Detailed Balance and Reversibility | [222](calculus/stochastic-differential-equations.pdf#page=222) |
| Part III Applications | [245](calculus/stochastic-differential-equations.pdf#page=245) |
| 10 State Estimation | [246](calculus/stochastic-differential-equations.pdf#page=246) |
| 10.1 Recursive Filtering | [247](calculus/stochastic-differential-equations.pdf#page=247) |
| 10.2 Observation Models and the State Likelihood | [248](calculus/stochastic-differential-equations.pdf#page=248) |
| 10.3 The Recursions: Time Update and Data Update | [251](calculus/stochastic-differential-equations.pdf#page=251) |
| 10.4 The Smoothing Filter | [255](calculus/stochastic-differential-equations.pdf#page=255) |
| 10.5 Sampling Typical Tracks | [257](calculus/stochastic-differential-equations.pdf#page=257) |
| 10.6 Likelihood Inference | [258](calculus/stochastic-differential-equations.pdf#page=258) |
| 10.7 The Kalman Filter | [260](calculus/stochastic-differential-equations.pdf#page=260) |
| 10.8 Estimating States and Parameters as a Mixed-Effects Model | [267](calculus/stochastic-differential-equations.pdf#page=267) |
| 11 Expectations to the Future | [274](calculus/stochastic-differential-equations.pdf#page=274) |
| 11.1 Dynkin's Formula | [275](calculus/stochastic-differential-equations.pdf#page=275) |
| 11.2 Expected Exit Times from Bounded Domains | [276](calculus/stochastic-differential-equations.pdf#page=276) |
| 11.3 Absorbing Boundaries | [282](calculus/stochastic-differential-equations.pdf#page=282) |
| 11.4 The Expected Point of Exit | [285](calculus/stochastic-differential-equations.pdf#page=285) |
| 11.5 Recurrence of Brownian Motion | [287](calculus/stochastic-differential-equations.pdf#page=287) |
| 11.6 The Poisson Equation | [289](calculus/stochastic-differential-equations.pdf#page=289) |
| 11.7 Analysis of a Singular Boundary Point | [289](calculus/stochastic-differential-equations.pdf#page=289) |
| 11.8 Discounting and the Feynman-Kac Formula | [293](calculus/stochastic-differential-equations.pdf#page=293) |
| 12 Stochastic Stability Theory | [305](calculus/stochastic-differential-equations.pdf#page=305) |
| 12.1 The Stability Problem | [306](calculus/stochastic-differential-equations.pdf#page=306) |
| 12.2 The Sensitivity Equations | [307](calculus/stochastic-differential-equations.pdf#page=307) |
| 12.3 Stochastic Lyapunov Exponents | [310](calculus/stochastic-differential-equations.pdf#page=310) |
| 12.4 Extrema of the Stationary Distribution | [313](calculus/stochastic-differential-equations.pdf#page=313) |
| 12.5 A Worked Example: A Stochastic Predator-Prey Model | [316](calculus/stochastic-differential-equations.pdf#page=316) |
| 12.6 Geometric Brownian Motion Revisited | [320](calculus/stochastic-differential-equations.pdf#page=320) |
| 12.7 Stochastic Lyapunov Functions | [322](calculus/stochastic-differential-equations.pdf#page=322) |
| 12.8 Stability in Mean Square | [325](calculus/stochastic-differential-equations.pdf#page=325) |
| 12.9 Stochastic Boundedness | [328](calculus/stochastic-differential-equations.pdf#page=328) |
| 13 Dynamic Optimization | [335](calculus/stochastic-differential-equations.pdf#page=335) |
| 13.1 Markov Decision Problems | [336](calculus/stochastic-differential-equations.pdf#page=336) |
| 13.2 Controlled Diffusions and Performance Objectives | [339](calculus/stochastic-differential-equations.pdf#page=339) |
| 13.3 Verification and the Hamilton-Jacobi-Bellman Equation | [340](calculus/stochastic-differential-equations.pdf#page=340) |
| 13.4 Portfolio Selection | [342](calculus/stochastic-differential-equations.pdf#page=342) |
| 13.5 Multivariate Linear-Quadratic Control | [343](calculus/stochastic-differential-equations.pdf#page=343) |
| 13.6 Steady-State Control Problems | [346](calculus/stochastic-differential-equations.pdf#page=346) |
| 13.7 Designing an Autopilot | [350](calculus/stochastic-differential-equations.pdf#page=350) |
| 13.8 Designing a Fisheries Management System | [352](calculus/stochastic-differential-equations.pdf#page=352) |
| 13.9 A Fisheries Management Problem in 2D | [354](calculus/stochastic-differential-equations.pdf#page=354) |
| 13.10 Optimal Diel Vertical Migrations | [358](calculus/stochastic-differential-equations.pdf#page=358) |
| 14 Perspectives | [369](calculus/stochastic-differential-equations.pdf#page=369) |
| Solutions to selected exercises | [385](calculus/stochastic-differential-equations.pdf#page=385) |

### Stochastic differential equations in code

A web tutorial, not a PDF: the SciML *DifferentialEquations.jl* documentation's SDE tutorial, at
[docs.sciml.ai](https://docs.sciml.ai/DiffEqDocs/stable/tutorials/sde_example/). It writes the SDEs the Thygesen book above derives as Julia code with
`StochasticDiffEq.jl` and plots each solution, so it is the place to see Euler-Maruyama, an ensemble of
paths and the different noise shapes run. Link a section with its `#` anchor, as below; there are no
page numbers.

| Section | Link |
| --- | --- |
| Stochastic Differential Equations: what the tutorial assumes (the ODE tutorial) | [open](https://docs.sciml.ai/DiffEqDocs/stable/tutorials/sde_example/#Stochastic-Differential-Equations) |
| Example 1: a scalar SDE with linear drift and noise, solved by Euler-Maruyama (`EM`) and plotted | [open](https://docs.sciml.ai/DiffEqDocs/stable/tutorials/sde_example/#Example-1:-Scalar-SDEs) |
| Higher-order methods: `EM` against `SRIW1` and the analytic solution, adaptive and fixed steps | [open](https://docs.sciml.ai/DiffEqDocs/stable/tutorials/sde_example/#Using-Higher-Order-Methods) |
| Ensemble simulations: 1000 trajectories, their mean and quantiles, a time-point correlation | [open](https://docs.sciml.ai/DiffEqDocs/stable/tutorials/sde_example/#Ensemble-Simulations) |
| Example 2: stochastic Lorenz system, one noise term per variable (diagonal noise) | [open](https://docs.sciml.ai/DiffEqDocs/stable/tutorials/sde_example/#Example-2:-Systems-of-SDEs-with-Diagonal-Noise) |
| Example 3: one shared Wiener process driving a linear matrix SDE (scalar noise) | [open](https://docs.sciml.ai/DiffEqDocs/stable/tutorials/sde_example/#Example-3:-Systems-of-SDEs-with-Scalar-Noise) |
| Example 4: a 2×4 noise matrix, dense and sparse (non-diagonal noise) | [open](https://docs.sciml.ai/DiffEqDocs/stable/tutorials/sde_example/#Example-4:-Systems-of-SDEs-with-Non-Diagonal-Noise) |
| Example 5: passing a custom coloured noise process (only `EM` and `EulerHeun` accept it) | [open](https://docs.sciml.ai/DiffEqDocs/stable/tutorials/sde_example/#Example-5:-Colored-Noise) |
| Heston stochastic volatility model with correlated Wiener noise | [open](https://docs.sciml.ai/DiffEqDocs/stable/tutorials/sde_example/#Example:-Spatially-Colored-Noise-in-the-Heston-Model) |

## statistics/

### Introduction to statistics

`statistics/introduction-to-statistics.pdf`, 148 pages. Charles Chimedza and Nothabo Ndebele, *An
Introduction to Mathematical Statistics*, STAT2012 lecture notes, University of the Witwatersrand, 5 July
2016. Lecture notes: descriptive statistics, probability, random variables, estimation, confidence
intervals, hypothesis tests and simple regression. No embedded outline; this table is from the printed
contents. The printed page number is the PDF page minus 1.

| Chapter | PDF page |
| --- | --- |
| 1 Introduction to Mathematical Statistics | [10](statistics/introduction-to-statistics.pdf#page=10) |
| 1.3 Populations and Samples | [11](statistics/introduction-to-statistics.pdf#page=11) |
| 2 Descriptive Statistics | [18](statistics/introduction-to-statistics.pdf#page=18) |
| 2.2 Graphical Techniques | [18](statistics/introduction-to-statistics.pdf#page=18) |
| 2.3 Summary Statistics | [40](statistics/introduction-to-statistics.pdf#page=40) |
| 2.4 Measures of Location | [40](statistics/introduction-to-statistics.pdf#page=40) |
| 2.5 Box-and-Whisker Plot | [49](statistics/introduction-to-statistics.pdf#page=49) |
| 2.6 Measures of Dispersion | [50](statistics/introduction-to-statistics.pdf#page=50) |
| 3 Introduction to Probability | [54](statistics/introduction-to-statistics.pdf#page=54) |
| 3.4 Counting Methods: Permutations and Combinations | [59](statistics/introduction-to-statistics.pdf#page=59) |
| 3.5 Rules Governing Probability (Axioms) | [64](statistics/introduction-to-statistics.pdf#page=64) |
| 3.7 The Classical Approach | [66](statistics/introduction-to-statistics.pdf#page=66) |
| 4 Random Variables and Distributions | [80](statistics/introduction-to-statistics.pdf#page=80) |
| 4.2 Discrete Random Variables | [80](statistics/introduction-to-statistics.pdf#page=80) |
| 4.3 Moments and Moment Generating Functions of Discrete Random Variables | [82](statistics/introduction-to-statistics.pdf#page=82) |
| 4.4 Continuous Random Variables | [83](statistics/introduction-to-statistics.pdf#page=83) |
| 4.5 Empirical Distributions | [86](statistics/introduction-to-statistics.pdf#page=86) |
| 4.6 Some Discrete Distributions | [87](statistics/introduction-to-statistics.pdf#page=87) |
| 4.7 Some Common Continuous Empirical Distributions | [90](statistics/introduction-to-statistics.pdf#page=90) |
| 4.8 Memoryless Property | [92](statistics/introduction-to-statistics.pdf#page=92) |
| 5 Estimation and Hypothesis Testing | [96](statistics/introduction-to-statistics.pdf#page=96) |
| 5.2 Estimation | [96](statistics/introduction-to-statistics.pdf#page=96) |
| 5.3 Confidence Intervals | [99](statistics/introduction-to-statistics.pdf#page=99) |
| 5.4 Sampling to a Desired Precision | [103](statistics/introduction-to-statistics.pdf#page=103) |
| 5.5 Hypothesis Testing | [105](statistics/introduction-to-statistics.pdf#page=105) |
| 6 Introduction to Correlation and Regression Analysis | [116](statistics/introduction-to-statistics.pdf#page=116) |
| 6.3 Correlation | [117](statistics/introduction-to-statistics.pdf#page=117) |
| 6.4 Simple Linear Regression Analysis | [120](statistics/introduction-to-statistics.pdf#page=120) |
| 6.7 The Least Squares Technique | [128](statistics/introduction-to-statistics.pdf#page=128) |
| 6.9 Making Inferences about β0 and β1 | [133](statistics/introduction-to-statistics.pdf#page=133) |

### Introduction to probability for data science

`statistics/introduction-to-probability-for-data-science.pdf`, 709 pages. Stanley H. Chan, *Introduction to Probability for Data Science*, Michigan Publishing,
2021 (Purdue University; free electronic edition, first edition). A first course in probability written
for data science: each idea comes with a figure, a plain-words summary box ("What is conditional
expectation?") and a worked example, and the proofs are kept short. Chapters 1 to 5 build probability,
random variables and joint distributions; 6 to 9 cover sample statistics, the law of large numbers and
the central limit theorem, regression, maximum-likelihood and MAP estimation, confidence intervals and
hypothesis tests; 10 is random processes. Was `Introduction to Probability for Data Science (Stanley
Chan) (Z-Library).pdf`. The embedded outline lists sections without numbers; the numbers below follow
the printed contents. The printed page number is the PDF page minus 16.

| Chapter or section | PDF page |
| --- | --- |
| 1 Mathematical Background | [17](statistics/introduction-to-probability-for-data-science.pdf#page=17) |
| 1.1 Infinite Series | [18](statistics/introduction-to-probability-for-data-science.pdf#page=18) |
| 1.2 Approximation | [26](statistics/introduction-to-probability-for-data-science.pdf#page=26) |
| 1.3 Integration | [31](statistics/introduction-to-probability-for-data-science.pdf#page=31) |
| 1.4 Linear Algebra | [36](statistics/introduction-to-probability-for-data-science.pdf#page=36) |
| 1.5 Basic Combinatorics | [47](statistics/introduction-to-probability-for-data-science.pdf#page=47) |
| 2 Probability | [59](statistics/introduction-to-probability-for-data-science.pdf#page=59) |
| 2.1 Set Theory | [60](statistics/introduction-to-probability-for-data-science.pdf#page=60) |
| 2.2 Probability Space | [74](statistics/introduction-to-probability-for-data-science.pdf#page=74) |
| 2.3 Axioms of Probability | [90](statistics/introduction-to-probability-for-data-science.pdf#page=90) |
| 2.4 Conditional Probability | [96](statistics/introduction-to-probability-for-data-science.pdf#page=96) |
| 3 Discrete Random Variables | [119](statistics/introduction-to-probability-for-data-science.pdf#page=119) |
| 3.1 Random Variables | [121](statistics/introduction-to-probability-for-data-science.pdf#page=121) |
| 3.2 Probability Mass Function | [126](statistics/introduction-to-probability-for-data-science.pdf#page=126) |
| 3.3 Cumulative Distribution Functions (Discrete) | [137](statistics/introduction-to-probability-for-data-science.pdf#page=137) |
| 3.4 Expectation | [141](statistics/introduction-to-probability-for-data-science.pdf#page=141) |
| 3.5 Common Discrete Random Variables | [152](statistics/introduction-to-probability-for-data-science.pdf#page=152) |
| 4 Continuous Random Variables | [187](statistics/introduction-to-probability-for-data-science.pdf#page=187) |
| 4.1 Probability Density Function | [188](statistics/introduction-to-probability-for-data-science.pdf#page=188) |
| 4.2 Expectation, Moment, and Variance | [196](statistics/introduction-to-probability-for-data-science.pdf#page=196) |
| 4.3 Cumulative Distribution Function | [201](statistics/introduction-to-probability-for-data-science.pdf#page=201) |
| 4.4 Median, Mode, and Mean | [212](statistics/introduction-to-probability-for-data-science.pdf#page=212) |
| 4.5 Uniform and Exponential Random Variables | [217](statistics/introduction-to-probability-for-data-science.pdf#page=217) |
| 4.6 Gaussian Random Variables | [227](statistics/introduction-to-probability-for-data-science.pdf#page=227) |
| 4.7 Functions of Random Variables | [239](statistics/introduction-to-probability-for-data-science.pdf#page=239) |
| 4.8 Generating Random Numbers | [245](statistics/introduction-to-probability-for-data-science.pdf#page=245) |
| 5 Joint Distributions | [257](statistics/introduction-to-probability-for-data-science.pdf#page=257) |
| 5.1 Joint PMF and Joint PDF | [260](statistics/introduction-to-probability-for-data-science.pdf#page=260) |
| 5.2 Joint Expectation | [273](statistics/introduction-to-probability-for-data-science.pdf#page=273) |
| 5.3 Conditional PMF and PDF | [282](statistics/introduction-to-probability-for-data-science.pdf#page=282) |
| 5.4 Conditional Expectation | [291](statistics/introduction-to-probability-for-data-science.pdf#page=291) |
| 5.5 Sum of Two Random Variables | [296](statistics/introduction-to-probability-for-data-science.pdf#page=296) |
| 5.6 Random Vectors and Covariance Matrices | [302](statistics/introduction-to-probability-for-data-science.pdf#page=302) |
| 5.7 Transformation of Multidimensional Gaussians | [309](statistics/introduction-to-probability-for-data-science.pdf#page=309) |
| 5.8 Principal-Component Analysis | [319](statistics/introduction-to-probability-for-data-science.pdf#page=319) |
| 6 Sample Statistics | [335](statistics/introduction-to-probability-for-data-science.pdf#page=335) |
| 6.1 Moment-Generating and Characteristic Functions | [340](statistics/introduction-to-probability-for-data-science.pdf#page=340) |
| 6.2 Probability Inequalities | [349](statistics/introduction-to-probability-for-data-science.pdf#page=349) |
| 6.3 Law of Large Numbers | [367](statistics/introduction-to-probability-for-data-science.pdf#page=367) |
| 6.4 Central Limit Theorem | [382](statistics/introduction-to-probability-for-data-science.pdf#page=382) |
| 7 Regression | [405](statistics/introduction-to-probability-for-data-science.pdf#page=405) |
| 7.1 Principles of Regression | [410](statistics/introduction-to-probability-for-data-science.pdf#page=410) |
| 7.2 Overfitting | [434](statistics/introduction-to-probability-for-data-science.pdf#page=434) |
| 7.3 Bias and Variance Trade-Off | [445](statistics/introduction-to-probability-for-data-science.pdf#page=445) |
| 7.4 Regularization | [456](statistics/introduction-to-probability-for-data-science.pdf#page=456) |
| 8 Estimation | [481](statistics/introduction-to-probability-for-data-science.pdf#page=481) |
| 8.1 Maximum-Likelihood Estimation | [484](statistics/introduction-to-probability-for-data-science.pdf#page=484) |
| 8.2 Properties of ML Estimates | [507](statistics/introduction-to-probability-for-data-science.pdf#page=507) |
| 8.3 Maximum A Posteriori Estimation | [518](statistics/introduction-to-probability-for-data-science.pdf#page=518) |
| 8.4 Minimum Mean-Square Estimation | [536](statistics/introduction-to-probability-for-data-science.pdf#page=536) |
| 9 Confidence and Hypothesis | [557](statistics/introduction-to-probability-for-data-science.pdf#page=557) |
| 9.1 Confidence Interval | [559](statistics/introduction-to-probability-for-data-science.pdf#page=559) |
| 9.2 Bootstrapping | [575](statistics/introduction-to-probability-for-data-science.pdf#page=575) |
| 9.3 Hypothesis Testing | [582](statistics/introduction-to-probability-for-data-science.pdf#page=582) |
| 9.4 Neyman-Pearson Test | [593](statistics/introduction-to-probability-for-data-science.pdf#page=593) |
| 9.5 ROC and Precision-Recall Curve | [605](statistics/introduction-to-probability-for-data-science.pdf#page=605) |
| 10 Random Processes | [627](statistics/introduction-to-probability-for-data-science.pdf#page=627) |
| 10.1 Basic Concepts | [628](statistics/introduction-to-probability-for-data-science.pdf#page=628) |
| 10.2 Mean and Correlation Functions | [634](statistics/introduction-to-probability-for-data-science.pdf#page=634) |
| 10.3 Wide-Sense Stationary Processes | [646](statistics/introduction-to-probability-for-data-science.pdf#page=646) |
| 10.4 Power Spectral Density | [652](statistics/introduction-to-probability-for-data-science.pdf#page=652) |
| 10.5 WSS Process through LTI Systems | [659](statistics/introduction-to-probability-for-data-science.pdf#page=659) |
| 10.6 Optimal Linear Filter | [669](statistics/introduction-to-probability-for-data-science.pdf#page=669) |
| Appendix to chapter 10 | [686](statistics/introduction-to-probability-for-data-science.pdf#page=686) |
| Appendix | [697](statistics/introduction-to-probability-for-data-science.pdf#page=697) |

## machine-learning/

### Mathematics for machine learning

`machine-learning/mathematics-for-machine-learning.pdf`, 417 pages. Marc Peter Deisenroth, A. Aldo Faisal
and Cheng Soon Ong, *Mathematics for Machine Learning*, draft of 15 October 2019, Cambridge University
Press. Part I covers the foundations: linear algebra, analytic geometry, matrix decompositions, vector
calculus, probability and distributions, continuous optimisation. Part II applies them to linear
regression, dimensionality reduction, density estimation and classification. The printed page number is
the PDF page minus 6. The table is from the PDF's own outline, with each section's page found from its
heading in the text; Part II is listed down to the chapters and their first sections.

| Chapter or section | PDF page |
| --- | --- |
| 1 Introduction and Motivation | [17](machine-learning/mathematics-for-machine-learning.pdf#page=17) |
| 1.1 Finding Words for Intuitions | [18](machine-learning/mathematics-for-machine-learning.pdf#page=18) |
| 1.2 Two Ways to Read This Book | [19](machine-learning/mathematics-for-machine-learning.pdf#page=19) |
| 1.3 Exercises and Feedback | [22](machine-learning/mathematics-for-machine-learning.pdf#page=22) |
| 2 Linear Algebra | [23](machine-learning/mathematics-for-machine-learning.pdf#page=23) |
| 2.1 Systems of Linear Equations | [25](machine-learning/mathematics-for-machine-learning.pdf#page=25) |
| 2.2 Matrices | [28](machine-learning/mathematics-for-machine-learning.pdf#page=28) |
| 2.3 Solving Systems of Linear Equations | [33](machine-learning/mathematics-for-machine-learning.pdf#page=33) |
| 2.4 Vector Spaces | [41](machine-learning/mathematics-for-machine-learning.pdf#page=41) |
| 2.5 Linear Independence | [46](machine-learning/mathematics-for-machine-learning.pdf#page=46) |
| 2.6 Basis and Rank | [50](machine-learning/mathematics-for-machine-learning.pdf#page=50) |
| 2.7 Linear Mappings | [54](machine-learning/mathematics-for-machine-learning.pdf#page=54) |
| 2.8 Affine Spaces | [67](machine-learning/mathematics-for-machine-learning.pdf#page=67) |
| 3 Analytic Geometry | [76](machine-learning/mathematics-for-machine-learning.pdf#page=76) |
| 3.1 Norms | [77](machine-learning/mathematics-for-machine-learning.pdf#page=77) |
| 3.2 Inner Products | [78](machine-learning/mathematics-for-machine-learning.pdf#page=78) |
| 3.3 Lengths and Distances | [81](machine-learning/mathematics-for-machine-learning.pdf#page=81) |
| 3.4 Angles and Orthogonality | [82](machine-learning/mathematics-for-machine-learning.pdf#page=82) |
| 3.5 Orthonormal Basis | [84](machine-learning/mathematics-for-machine-learning.pdf#page=84) |
| 3.6 Orthogonal Complement | [85](machine-learning/mathematics-for-machine-learning.pdf#page=85) |
| 3.7 Inner Product of Functions | [86](machine-learning/mathematics-for-machine-learning.pdf#page=86) |
| 3.8 Orthogonal Projections | [87](machine-learning/mathematics-for-machine-learning.pdf#page=87) |
| 3.9 Rotations | [97](machine-learning/mathematics-for-machine-learning.pdf#page=97) |
| 4 Matrix Decompositions | [104](machine-learning/mathematics-for-machine-learning.pdf#page=104) |
| 4.1 Determinant and Trace | [105](machine-learning/mathematics-for-machine-learning.pdf#page=105) |
| 4.2 Eigenvalues and Eigenvectors | [111](machine-learning/mathematics-for-machine-learning.pdf#page=111) |
| 4.3 Cholesky Decomposition | [120](machine-learning/mathematics-for-machine-learning.pdf#page=120) |
| 4.4 Eigendecomposition and Diagonalization | [121](machine-learning/mathematics-for-machine-learning.pdf#page=121) |
| 4.5 Singular Value Decomposition | [125](machine-learning/mathematics-for-machine-learning.pdf#page=125) |
| 4.6 Matrix Approximation | [135](machine-learning/mathematics-for-machine-learning.pdf#page=135) |
| 4.7 Matrix Phylogeny | [140](machine-learning/mathematics-for-machine-learning.pdf#page=140) |
| 5 Vector Calculus | [145](machine-learning/mathematics-for-machine-learning.pdf#page=145) |
| 5.1 Differentiation of Univariate Functions | [147](machine-learning/mathematics-for-machine-learning.pdf#page=147) |
| 5.2 Partial Differentiation and Gradients | [152](machine-learning/mathematics-for-machine-learning.pdf#page=152) |
| 5.3 Gradients of Vector-Valued Functions | [155](machine-learning/mathematics-for-machine-learning.pdf#page=155) |
| 5.4 Gradients of Matrices | [161](machine-learning/mathematics-for-machine-learning.pdf#page=161) |
| 5.5 Useful Identities for Computing Gradients | [164](machine-learning/mathematics-for-machine-learning.pdf#page=164) |
| 5.6 Backpropagation and Automatic Differentiation | [165](machine-learning/mathematics-for-machine-learning.pdf#page=165) |
| 5.7 Higher-Order Derivatives | [170](machine-learning/mathematics-for-machine-learning.pdf#page=170) |
| 5.8 Linearization and Multivariate Taylor Series | [171](machine-learning/mathematics-for-machine-learning.pdf#page=171) |
| 6 Probability and Distributions | [178](machine-learning/mathematics-for-machine-learning.pdf#page=178) |
| 6.1 Construction of a Probability Space | [178](machine-learning/mathematics-for-machine-learning.pdf#page=178) |
| 6.2 Discrete and Continuous Probabilities | [184](machine-learning/mathematics-for-machine-learning.pdf#page=184) |
| 6.3 Sum Rule, Product Rule, and Bayes’ Theorem | [189](machine-learning/mathematics-for-machine-learning.pdf#page=189) |
| 6.4 Summary Statistics and Independence | [192](machine-learning/mathematics-for-machine-learning.pdf#page=192) |
| 6.5 Gaussian Distribution | [203](machine-learning/mathematics-for-machine-learning.pdf#page=203) |
| 6.6 Conjugacy and the Exponential Family | [211](machine-learning/mathematics-for-machine-learning.pdf#page=211) |
| 6.7 Change of Variables/Inverse Transform | [220](machine-learning/mathematics-for-machine-learning.pdf#page=220) |
| 7 Continuous Optimization | [231](machine-learning/mathematics-for-machine-learning.pdf#page=231) |
| 7.1 Optimization Using Gradient Descent | [233](machine-learning/mathematics-for-machine-learning.pdf#page=233) |
| 7.2 Constrained Optimization and Lagrange Multipliers | [239](machine-learning/mathematics-for-machine-learning.pdf#page=239) |
| 7.3 Convex Optimization | [242](machine-learning/mathematics-for-machine-learning.pdf#page=242) |
| 8 When Models Meet Data | [257](machine-learning/mathematics-for-machine-learning.pdf#page=257) |
| 8.1 Data, Models, and Learning | [257](machine-learning/mathematics-for-machine-learning.pdf#page=257) |
| 8.2 Empirical Risk Minimization | [264](machine-learning/mathematics-for-machine-learning.pdf#page=264) |
| 8.3 Parameter Estimation | [271](machine-learning/mathematics-for-machine-learning.pdf#page=271) |
| 8.4 Probabilistic Modeling and Inference | [278](machine-learning/mathematics-for-machine-learning.pdf#page=278) |
| 8.5 Directed Graphical Models | [284](machine-learning/mathematics-for-machine-learning.pdf#page=284) |
| 8.6 Model Selection | [289](machine-learning/mathematics-for-machine-learning.pdf#page=289) |
| 9 Linear Regression | [295](machine-learning/mathematics-for-machine-learning.pdf#page=295) |
| 9.1 Problem Formulation | [297](machine-learning/mathematics-for-machine-learning.pdf#page=297) |
| 9.2 Parameter Estimation | [298](machine-learning/mathematics-for-machine-learning.pdf#page=298) |
| 9.3 Bayesian Linear Regression | [309](machine-learning/mathematics-for-machine-learning.pdf#page=309) |
| 9.4 Maximum Likelihood as Orthogonal Projection | [319](machine-learning/mathematics-for-machine-learning.pdf#page=319) |
| 10 Dimensionality Reduction with Principal Component Analysis | [323](machine-learning/mathematics-for-machine-learning.pdf#page=323) |
| 10.1 Problem Setting | [324](machine-learning/mathematics-for-machine-learning.pdf#page=324) |
| 10.2 Maximum Variance Perspective | [326](machine-learning/mathematics-for-machine-learning.pdf#page=326) |
| 10.3 Projection Perspective | [331](machine-learning/mathematics-for-machine-learning.pdf#page=331) |
| 10.4 Eigenvector Computation and Low-Rank Approximations | [339](machine-learning/mathematics-for-machine-learning.pdf#page=339) |
| 10.5 PCA in High Dimensions | [341](machine-learning/mathematics-for-machine-learning.pdf#page=341) |
| 10.6 Key Steps of PCA in Practice | [342](machine-learning/mathematics-for-machine-learning.pdf#page=342) |
| 10.7 Latent Variable Perspective | [345](machine-learning/mathematics-for-machine-learning.pdf#page=345) |
| 11 Density Estimation with Gaussian Mixture Models | [354](machine-learning/mathematics-for-machine-learning.pdf#page=354) |
| 11.1 Gaussian Mixture Model | [355](machine-learning/mathematics-for-machine-learning.pdf#page=355) |
| 11.2 Parameter Learning via Maximum Likelihood | [356](machine-learning/mathematics-for-machine-learning.pdf#page=356) |
| 11.3 EM Algorithm | [366](machine-learning/mathematics-for-machine-learning.pdf#page=366) |
| 11.4 Latent-Variable Perspective | [369](machine-learning/mathematics-for-machine-learning.pdf#page=369) |
| 12 Classification with Support Vector Machines | [376](machine-learning/mathematics-for-machine-learning.pdf#page=376) |
| 12.1 Separating Hyperplanes | [378](machine-learning/mathematics-for-machine-learning.pdf#page=378) |
| 12.2 Primal Support Vector Machine | [380](machine-learning/mathematics-for-machine-learning.pdf#page=380) |
| 12.3 Dual Support Vector Machine | [389](machine-learning/mathematics-for-machine-learning.pdf#page=389) |
| 12.4 Kernels | [394](machine-learning/mathematics-for-machine-learning.pdf#page=394) |
| 12.5 Numerical Solution | [396](machine-learning/mathematics-for-machine-learning.pdf#page=396) |

### Pattern recognition and machine learning

`machine-learning/pattern-recognition-and-machine-learning.pdf`, 749 pages. Christopher M. Bishop, *Pattern Recognition and Machine Learning*, Springer, 2006
(first edition, Information Science and Statistics series). A Bayesian treatment of machine learning:
probability distributions (chapter 2 holds the Gaussian in full, with conditionals, marginals and Bayes'
theorem for Gaussians), linear models, neural networks, kernels, graphical models, EM, variational
inference, sampling, latent-variable models and sequential data. Was `Pattern Recogniton And Machine
Learning.pdf`. The embedded outline has chapters only; the section rows come from the printed contents, each moved to
the PDF page that prints its contents page number. The offset between printed and PDF pages drifts through this PDF: the printed page is the PDF page minus
19 at PDF page 100, minus 18 at page 200, minus 16 at page 500 and minus 14 at page 700, and the
back-of-book index finds it reaching minus 11 near the end. Convert a printed page through
`~/.claude/cache/book-indexes/pattern-recognition-and-machine-learning.json`, whose PDF pages were read
off the pages themselves, never by subtracting a fixed number. Appendix rows are the outline's own pages.

| Chapter or section | PDF page |
| --- | --- |
| 1 Introduction | [20](machine-learning/pattern-recognition-and-machine-learning.pdf#page=20) |
| 1.1 Example: Polynomial Curve Fitting | [23](machine-learning/pattern-recognition-and-machine-learning.pdf#page=23) |
| 1.2 Probability Theory | [31](machine-learning/pattern-recognition-and-machine-learning.pdf#page=31) |
| 1.3 Model Selection | [51](machine-learning/pattern-recognition-and-machine-learning.pdf#page=51) |
| 1.4 The Curse of Dimensionality | [52](machine-learning/pattern-recognition-and-machine-learning.pdf#page=52) |
| 1.5 Decision Theory | [57](machine-learning/pattern-recognition-and-machine-learning.pdf#page=57) |
| 1.6 Information Theory | [67](machine-learning/pattern-recognition-and-machine-learning.pdf#page=67) |
| 2 Probability Distributions | [86](machine-learning/pattern-recognition-and-machine-learning.pdf#page=86) |
| 2.1 Binary Variables | [87](machine-learning/pattern-recognition-and-machine-learning.pdf#page=87) |
| 2.2 Multinomial Variables | [93](machine-learning/pattern-recognition-and-machine-learning.pdf#page=93) |
| 2.3 The Gaussian Distribution | [97](machine-learning/pattern-recognition-and-machine-learning.pdf#page=97) |
| 2.4 The Exponential Family | [132](machine-learning/pattern-recognition-and-machine-learning.pdf#page=132) |
| 2.5 Nonparametric Methods | [139](machine-learning/pattern-recognition-and-machine-learning.pdf#page=139) |
| 3 Linear Models for Regression | [156](machine-learning/pattern-recognition-and-machine-learning.pdf#page=156) |
| 3.1 Linear Basis Function Models | [157](machine-learning/pattern-recognition-and-machine-learning.pdf#page=157) |
| 3.2 The Bias-Variance Decomposition | [166](machine-learning/pattern-recognition-and-machine-learning.pdf#page=166) |
| 3.3 Bayesian Linear Regression | [171](machine-learning/pattern-recognition-and-machine-learning.pdf#page=171) |
| 3.4 Bayesian Model Comparison | [180](machine-learning/pattern-recognition-and-machine-learning.pdf#page=180) |
| 3.5 The Evidence Approximation | [184](machine-learning/pattern-recognition-and-machine-learning.pdf#page=184) |
| 3.6 Limitations of Fixed Basis Functions | [191](machine-learning/pattern-recognition-and-machine-learning.pdf#page=191) |
| 4 Linear Models for Classification | [197](machine-learning/pattern-recognition-and-machine-learning.pdf#page=197) |
| 4.1 Discriminant Functions | [199](machine-learning/pattern-recognition-and-machine-learning.pdf#page=199) |
| 4.2 Probabilistic Generative Models | [214](machine-learning/pattern-recognition-and-machine-learning.pdf#page=214) |
| 4.3 Probabilistic Discriminative Models | [221](machine-learning/pattern-recognition-and-machine-learning.pdf#page=221) |
| 4.4 The Laplace Approximation | [231](machine-learning/pattern-recognition-and-machine-learning.pdf#page=231) |
| 4.5 Bayesian Logistic Regression | [235](machine-learning/pattern-recognition-and-machine-learning.pdf#page=235) |
| 5 Neural Networks | [243](machine-learning/pattern-recognition-and-machine-learning.pdf#page=243) |
| 5.1 Feed-forward Network Functions | [245](machine-learning/pattern-recognition-and-machine-learning.pdf#page=245) |
| 5.2 Network Training | [250](machine-learning/pattern-recognition-and-machine-learning.pdf#page=250) |
| 5.3 Error Backpropagation | [259](machine-learning/pattern-recognition-and-machine-learning.pdf#page=259) |
| 5.4 The Hessian Matrix | [267](machine-learning/pattern-recognition-and-machine-learning.pdf#page=267) |
| 5.5 Regularization in Neural Networks | [274](machine-learning/pattern-recognition-and-machine-learning.pdf#page=274) |
| 5.6 Mixture Density Networks | [290](machine-learning/pattern-recognition-and-machine-learning.pdf#page=290) |
| 5.7 Bayesian Neural Networks | [295](machine-learning/pattern-recognition-and-machine-learning.pdf#page=295) |
| 6 Kernel Methods | [309](machine-learning/pattern-recognition-and-machine-learning.pdf#page=309) |
| 6.1 Dual Representations | [311](machine-learning/pattern-recognition-and-machine-learning.pdf#page=311) |
| 6.2 Constructing Kernels | [312](machine-learning/pattern-recognition-and-machine-learning.pdf#page=312) |
| 6.3 Radial Basis Function Networks | [317](machine-learning/pattern-recognition-and-machine-learning.pdf#page=317) |
| 6.4 Gaussian Processes | [321](machine-learning/pattern-recognition-and-machine-learning.pdf#page=321) |
| 7 Sparse Kernel Machines | [342](machine-learning/pattern-recognition-and-machine-learning.pdf#page=342) |
| 7.1 Maximum Margin Classifiers | [343](machine-learning/pattern-recognition-and-machine-learning.pdf#page=343) |
| 7.2 Relevance Vector Machines | [362](machine-learning/pattern-recognition-and-machine-learning.pdf#page=362) |
| 8 Graphical Models | [376](machine-learning/pattern-recognition-and-machine-learning.pdf#page=376) |
| 8.1 Bayesian Networks | [377](machine-learning/pattern-recognition-and-machine-learning.pdf#page=377) |
| 8.2 Conditional Independence | [389](machine-learning/pattern-recognition-and-machine-learning.pdf#page=389) |
| 8.3 Markov Random Fields | [400](machine-learning/pattern-recognition-and-machine-learning.pdf#page=400) |
| 8.4 Inference in Graphical Models | [410](machine-learning/pattern-recognition-and-machine-learning.pdf#page=410) |
| 9 Mixture Models and EM | [440](machine-learning/pattern-recognition-and-machine-learning.pdf#page=440) |
| 9.1 K-means Clustering | [441](machine-learning/pattern-recognition-and-machine-learning.pdf#page=441) |
| 9.2 Mixtures of Gaussians | [447](machine-learning/pattern-recognition-and-machine-learning.pdf#page=447) |
| 9.3 An Alternative View of EM | [456](machine-learning/pattern-recognition-and-machine-learning.pdf#page=456) |
| 9.4 The EM Algorithm in General | [467](machine-learning/pattern-recognition-and-machine-learning.pdf#page=467) |
| 10.1 Variational Inference | [478](machine-learning/pattern-recognition-and-machine-learning.pdf#page=478) |
| 10.2 Illustration: Variational Mixture of Gaussians | [490](machine-learning/pattern-recognition-and-machine-learning.pdf#page=490) |
| 10.3 Variational Linear Regression | [502](machine-learning/pattern-recognition-and-machine-learning.pdf#page=502) |
| 10.4 Exponential Family Distributions | [506](machine-learning/pattern-recognition-and-machine-learning.pdf#page=506) |
| 10.5 Local Variational Methods | [509](machine-learning/pattern-recognition-and-machine-learning.pdf#page=509) |
| 10.6 Variational Logistic Regression | [514](machine-learning/pattern-recognition-and-machine-learning.pdf#page=514) |
| 10.7 Expectation Propagation | [521](machine-learning/pattern-recognition-and-machine-learning.pdf#page=521) |
| 11.1 Basic Sampling Algorithms | [542](machine-learning/pattern-recognition-and-machine-learning.pdf#page=542) |
| 11.2 Markov Chain Monte Carlo | [553](machine-learning/pattern-recognition-and-machine-learning.pdf#page=553) |
| 11.3 Gibbs Sampling | [558](machine-learning/pattern-recognition-and-machine-learning.pdf#page=558) |
| 11.4 Slice Sampling | [562](machine-learning/pattern-recognition-and-machine-learning.pdf#page=562) |
| 11.5 The Hybrid Monte Carlo Algorithm | [564](machine-learning/pattern-recognition-and-machine-learning.pdf#page=564) |
| 11.6 Estimating the Partition Function | [570](machine-learning/pattern-recognition-and-machine-learning.pdf#page=570) |
| 12.1 Principal Component Analysis | [577](machine-learning/pattern-recognition-and-machine-learning.pdf#page=577) |
| 12.2 Probabilistic PCA | [586](machine-learning/pattern-recognition-and-machine-learning.pdf#page=586) |
| 12.3 Kernel PCA | [602](machine-learning/pattern-recognition-and-machine-learning.pdf#page=602) |
| 12.4 Nonlinear Latent Variable Models | [607](machine-learning/pattern-recognition-and-machine-learning.pdf#page=607) |
| 13.1 Markov Models | [622](machine-learning/pattern-recognition-and-machine-learning.pdf#page=622) |
| 13.2 Hidden Markov Models | [625](machine-learning/pattern-recognition-and-machine-learning.pdf#page=625) |
| 13.3 Linear Dynamical Systems | [650](machine-learning/pattern-recognition-and-machine-learning.pdf#page=650) |
| 14.1 Bayesian Model Averaging | [669](machine-learning/pattern-recognition-and-machine-learning.pdf#page=669) |
| 14.2 Committees | [670](machine-learning/pattern-recognition-and-machine-learning.pdf#page=670) |
| 14.3 Boosting | [672](machine-learning/pattern-recognition-and-machine-learning.pdf#page=672) |
| 14.4 Tree-based Models | [678](machine-learning/pattern-recognition-and-machine-learning.pdf#page=678) |
| 14.5 Conditional Mixture Models | [681](machine-learning/pattern-recognition-and-machine-learning.pdf#page=681) |
| Appendix A Data Sets | [692](machine-learning/pattern-recognition-and-machine-learning.pdf#page=692) |
| Appendix B Probability Distributions | [699](machine-learning/pattern-recognition-and-machine-learning.pdf#page=699) |
| Appendix C Properties of Matrices | [708](machine-learning/pattern-recognition-and-machine-learning.pdf#page=708) |
| Appendix D Calculus of Variations | [715](machine-learning/pattern-recognition-and-machine-learning.pdf#page=715) |
| Appendix E Lagrange Multipliers | [718](machine-learning/pattern-recognition-and-machine-learning.pdf#page=718) |
| References | [722](machine-learning/pattern-recognition-and-machine-learning.pdf#page=722) |
| Index | [740](machine-learning/pattern-recognition-and-machine-learning.pdf#page=740) |

### Pattern classification

`machine-learning/pattern-classification.pdf`, 738 pages. Richard O. Duda, Peter E. Hart and David G.
Stork, *Pattern Classification*, second edition, Wiley (2001). A published textbook on statistical
pattern recognition: Bayesian decision theory and the normal density, maximum-likelihood and Bayesian
parameter estimation (with EM and hidden Markov models), nonparametric density estimation and
nearest-neighbour rules, linear discriminants and support vector machines, multilayer networks and
backpropagation, stochastic search and Boltzmann learning, decision trees and grammatical methods,
bias and variance, resampling and combining classifiers, and clustering. Appendix A collects the
linear algebra, probability, Gaussian integrals and information theory the book leans on. Was `PC2.pdf`.
A scanned copy of the printed book with no text layer stays outside the shelf; this copy has a text
layer and is the one to link.

**How this PDF is put together.** PDF pages 1 to 12 are scans of the printed book's cover and contents
and carry no text layer. From PDF page 13 on, the body is the authors' typeset manuscript, one file per
chapter (the PDF's title is `Chapter1.tex`), and each chapter is numbered from 1 again, starting at its
own contents page. Its pages therefore do not match the printed book's pages, and a page number quoted
from the printed book (such as the printed contents on PDF pages 3 to 12) will not open the right PDF
page.

**Page numbers.** Within a chapter, the PDF page is the printed page plus the PDF page of that chapter's
contents page, less 1: plus 12 in chapter 1, 36 in chapter 2, 104 in chapter 3, 184 in chapter 4, 258
in chapter 5, 330 in chapter 6, 408 in chapter 7, 458 in chapter 8, 528 in chapter 9, 602 in chapter 10
and 694 in Appendix A. Every section heading below was found on the page this predicts. Each chapter's
own contents page gives its bibliography and index a page or two early; the rows below give the pages
they really start on.

**Its index.** There is no index for the whole book. Each chapter ends with its own short index, in
that chapter's numbering: PDF pages 35 to 36, 102 to 104, 180 to 183, 256 to 258, 329 to 330, 405 to
407, 456 to 457, 525 to 527, 599 to 601, 690 to 693 and 733 to 735.

| Chapter or section | PDF page |
| --- | --- |
| Cover and contents of the printed book (scanned) | [1](machine-learning/pattern-classification.pdf#page=1) |
| 1 Introduction | [15](machine-learning/pattern-classification.pdf#page=15) |
| 1.1 Machine Perception | [15](machine-learning/pattern-classification.pdf#page=15) |
| 1.2 An Example | [15](machine-learning/pattern-classification.pdf#page=15) |
| 1.3 The Sub-problems of Pattern Classification | [23](machine-learning/pattern-classification.pdf#page=23) |
| 1.4 Learning and Adaptation | [28](machine-learning/pattern-classification.pdf#page=28) |
| 1.5 Conclusion | [29](machine-learning/pattern-classification.pdf#page=29) |
| 1 Index (PDF 35 to 36) | [35](machine-learning/pattern-classification.pdf#page=35) |
| 2 Bayesian decision theory | [39](machine-learning/pattern-classification.pdf#page=39) |
| 2.1 Introduction | [39](machine-learning/pattern-classification.pdf#page=39) |
| 2.2 Bayesian Decision Theory: Continuous Features | [43](machine-learning/pattern-classification.pdf#page=43) |
| 2.3 Minimum-Error-Rate Classification | [45](machine-learning/pattern-classification.pdf#page=45) |
| 2.4 Classifiers, Discriminants and Decision Surfaces | [49](machine-learning/pattern-classification.pdf#page=49) |
| 2.5 The Normal Density | [51](machine-learning/pattern-classification.pdf#page=51) |
| 2.6 Discriminant Functions for the Normal Density | [55](machine-learning/pattern-classification.pdf#page=55) |
| 2.7 *Error Probabilities and Integrals | [66](machine-learning/pattern-classification.pdf#page=66) |
| 2.8 *Error Bounds for Normal Densities | [67](machine-learning/pattern-classification.pdf#page=67) |
| 2.9 Bayes Decision Theory: Discrete Features | [72](machine-learning/pattern-classification.pdf#page=72) |
| 2.10 *Missing and Noisy Features | [75](machine-learning/pattern-classification.pdf#page=75) |
| 2.11 *Compound Bayes Decision Theory and Context | [77](machine-learning/pattern-classification.pdf#page=77) |
| 2 Problems | [80](machine-learning/pattern-classification.pdf#page=80) |
| 2 Index (PDF 102 to 104) | [102](machine-learning/pattern-classification.pdf#page=102) |
| 3 Maximum-likelihood and Bayesian parameter estimation | [107](machine-learning/pattern-classification.pdf#page=107) |
| 3.1 Introduction | [107](machine-learning/pattern-classification.pdf#page=107) |
| 3.2 Maximum Likelihood Estimation | [108](machine-learning/pattern-classification.pdf#page=108) |
| 3.3 Bayesian estimation | [113](machine-learning/pattern-classification.pdf#page=113) |
| 3.4 Bayesian Parameter Estimation: Gaussian Case | [115](machine-learning/pattern-classification.pdf#page=115) |
| 3.5 Bayesian Parameter Estimation: General Theory | [120](machine-learning/pattern-classification.pdf#page=120) |
| 3.6 *Sufficient Statistics | [125](machine-learning/pattern-classification.pdf#page=125) |
| 3.7 Problems of Dimensionality | [131](machine-learning/pattern-classification.pdf#page=131) |
| 3.8 *Expectation-Maximization (EM) | [136](machine-learning/pattern-classification.pdf#page=136) |
| 3.9 *Bayesian Belief Networks | [140](machine-learning/pattern-classification.pdf#page=140) |
| 3.10 *Hidden Markov Models | [146](machine-learning/pattern-classification.pdf#page=146) |
| 3 Problems | [158](machine-learning/pattern-classification.pdf#page=158) |
| 3 Index (PDF 180 to 183) | [180](machine-learning/pattern-classification.pdf#page=180) |
| 4 Nonparametric techniques | [187](machine-learning/pattern-classification.pdf#page=187) |
| 4.1 Introduction | [187](machine-learning/pattern-classification.pdf#page=187) |
| 4.2 Density estimation | [187](machine-learning/pattern-classification.pdf#page=187) |
| 4.3 Parzen Windows | [190](machine-learning/pattern-classification.pdf#page=190) |
| 4.4 k_n-Nearest-Neighbor Estimation | [202](machine-learning/pattern-classification.pdf#page=202) |
| 4.5 The Nearest-Neighbor Rule | [205](machine-learning/pattern-classification.pdf#page=205) |
| 4.6 *Metrics and Nearest-Neighbor Classification | [215](machine-learning/pattern-classification.pdf#page=215) |
| 4.7 *Fuzzy Classification | [220](machine-learning/pattern-classification.pdf#page=220) |
| 4.8 *Relaxation methods | [223](machine-learning/pattern-classification.pdf#page=223) |
| 4.9 *Approximations by Series Expansions | [226](machine-learning/pattern-classification.pdf#page=226) |
| 4.10 *Fisher Linear Discriminant | [228](machine-learning/pattern-classification.pdf#page=228) |
| 4.11 *Multiple Discriminant Analysis | [231](machine-learning/pattern-classification.pdf#page=231) |
| 4 Problems | [236](machine-learning/pattern-classification.pdf#page=236) |
| 4 Index (PDF 256 to 258) | [256](machine-learning/pattern-classification.pdf#page=256) |
| 5 Linear discriminant functions | [261](machine-learning/pattern-classification.pdf#page=261) |
| 5.1 Introduction | [261](machine-learning/pattern-classification.pdf#page=261) |
| 5.2 Linear Discriminant Functions and Decision Surfaces | [262](machine-learning/pattern-classification.pdf#page=262) |
| 5.3 Generalized Linear Discriminant Functions | [264](machine-learning/pattern-classification.pdf#page=264) |
| 5.4 The Two-Category Linearly-Separable Case | [269](machine-learning/pattern-classification.pdf#page=269) |
| 5.5 Minimizing the Perceptron Criterion Function | [272](machine-learning/pattern-classification.pdf#page=272) |
| 5.6 Relaxation Procedures | [281](machine-learning/pattern-classification.pdf#page=281) |
| 5.7 Nonseparable Behavior | [285](machine-learning/pattern-classification.pdf#page=285) |
| 5.8 Minimum Squared Error Procedures | [286](machine-learning/pattern-classification.pdf#page=286) |
| 5.9 *The Ho-Kashyap Procedures | [295](machine-learning/pattern-classification.pdf#page=295) |
| 5.10 *Linear Programming Algorithms | [302](machine-learning/pattern-classification.pdf#page=302) |
| 5.11 *Support Vector Machines | [307](machine-learning/pattern-classification.pdf#page=307) |
| 5.12 Multicategory Generalizations | [310](machine-learning/pattern-classification.pdf#page=310) |
| 5 Problems | [315](machine-learning/pattern-classification.pdf#page=315) |
| 5 Index (PDF 329 to 330) | [329](machine-learning/pattern-classification.pdf#page=329) |
| 6 Multilayer neural networks | [333](machine-learning/pattern-classification.pdf#page=333) |
| 6.1 Introduction | [333](machine-learning/pattern-classification.pdf#page=333) |
| 6.2 Feedforward operation and classification | [334](machine-learning/pattern-classification.pdf#page=334) |
| 6.3 Backpropagation algorithm | [340](machine-learning/pattern-classification.pdf#page=340) |
| 6.4 Error surfaces | [347](machine-learning/pattern-classification.pdf#page=347) |
| 6.5 Backpropagation as feature mapping | [351](machine-learning/pattern-classification.pdf#page=351) |
| 6.6 Backpropagation, Bayes theory and probability | [354](machine-learning/pattern-classification.pdf#page=354) |
| 6.7 *Related statistical techniques | [358](machine-learning/pattern-classification.pdf#page=358) |
| 6.8 Practical techniques for backpropagation | [359](machine-learning/pattern-classification.pdf#page=359) |
| 6.9 *Second-order methods | [371](machine-learning/pattern-classification.pdf#page=371) |
| 6.10 *Additional networks and training methods | [376](machine-learning/pattern-classification.pdf#page=376) |
| 6.11 Regularization and complexity adjustment | [381](machine-learning/pattern-classification.pdf#page=381) |
| 6 Problems | [388](machine-learning/pattern-classification.pdf#page=388) |
| 6 Index (PDF 405 to 407) | [405](machine-learning/pattern-classification.pdf#page=405) |
| 7 Stochastic methods | [411](machine-learning/pattern-classification.pdf#page=411) |
| 7.1 Introduction | [411](machine-learning/pattern-classification.pdf#page=411) |
| 7.2 Stochastic search | [412](machine-learning/pattern-classification.pdf#page=412) |
| 7.3 Boltzmann learning | [420](machine-learning/pattern-classification.pdf#page=420) |
| 7.4 *Boltzmann networks and graphical models | [431](machine-learning/pattern-classification.pdf#page=431) |
| 7.5 *Evolutionary methods | [433](machine-learning/pattern-classification.pdf#page=433) |
| 7.6 *Genetic Programming | [440](machine-learning/pattern-classification.pdf#page=440) |
| 7 Problems | [444](machine-learning/pattern-classification.pdf#page=444) |
| 7 Index (PDF 456 to 457) | [456](machine-learning/pattern-classification.pdf#page=456) |
| 8 Nonmetric methods | [461](machine-learning/pattern-classification.pdf#page=461) |
| 8.1 Introduction | [461](machine-learning/pattern-classification.pdf#page=461) |
| 8.2 Decision trees | [462](machine-learning/pattern-classification.pdf#page=462) |
| 8.3 CART | [463](machine-learning/pattern-classification.pdf#page=463) |
| 8.4 Other tree methods | [478](machine-learning/pattern-classification.pdf#page=478) |
| 8.5 *Recognition with strings | [480](machine-learning/pattern-classification.pdf#page=480) |
| 8.6 Grammatical methods | [489](machine-learning/pattern-classification.pdf#page=489) |
| 8.7 Grammatical inference | [496](machine-learning/pattern-classification.pdf#page=496) |
| 8.8 *Rule-based methods | [499](machine-learning/pattern-classification.pdf#page=499) |
| 8 Problems | [504](machine-learning/pattern-classification.pdf#page=504) |
| 8 Index (PDF 525 to 527) | [525](machine-learning/pattern-classification.pdf#page=525) |
| 9 Algorithm-independent machine learning | [531](machine-learning/pattern-classification.pdf#page=531) |
| 9.1 Introduction | [531](machine-learning/pattern-classification.pdf#page=531) |
| 9.2 Lack of inherent superiority of any classifier | [532](machine-learning/pattern-classification.pdf#page=532) |
| 9.3 Bias and variance | [543](machine-learning/pattern-classification.pdf#page=543) |
| 9.4 *Resampling for estimating statistics | [548](machine-learning/pattern-classification.pdf#page=548) |
| 9.5 Resampling for classifier design | [553](machine-learning/pattern-classification.pdf#page=553) |
| 9.6 Estimating and comparing classifiers | [560](machine-learning/pattern-classification.pdf#page=560) |
| 9.7 Combining classifiers | [573](machine-learning/pattern-classification.pdf#page=573) |
| 9 Problems | [579](machine-learning/pattern-classification.pdf#page=579) |
| 9 Index (PDF 599 to 601) | [599](machine-learning/pattern-classification.pdf#page=599) |
| 10 Unsupervised learning and clustering | [605](machine-learning/pattern-classification.pdf#page=605) |
| 10.1 Introduction | [605](machine-learning/pattern-classification.pdf#page=605) |
| 10.2 Mixture Densities and Identifiability | [606](machine-learning/pattern-classification.pdf#page=606) |
| 10.3 Maximum-Likelihood Estimates | [608](machine-learning/pattern-classification.pdf#page=608) |
| 10.4 Application to Normal Mixtures | [609](machine-learning/pattern-classification.pdf#page=609) |
| 10.5 Unsupervised Bayesian Learning | [619](machine-learning/pattern-classification.pdf#page=619) |
| 10.6 *Data Description and Clustering | [626](machine-learning/pattern-classification.pdf#page=626) |
| 10.7 Criterion Functions for Clustering | [631](machine-learning/pattern-classification.pdf#page=631) |
| 10.8 *Iterative Optimization | [637](machine-learning/pattern-classification.pdf#page=637) |
| 10.9 Hierarchical Clustering | [639](machine-learning/pattern-classification.pdf#page=639) |
| 10 Problems | [670](machine-learning/pattern-classification.pdf#page=670) |
| 10 Index (PDF 690 to 693) | [690](machine-learning/pattern-classification.pdf#page=690) |
| Appendix A Mathematical foundations | [697](machine-learning/pattern-classification.pdf#page=697) |
| A.1 Notation | [697](machine-learning/pattern-classification.pdf#page=697) |
| A.2 Linear algebra | [700](machine-learning/pattern-classification.pdf#page=700) |
| A.3 Lagrange optimization | [706](machine-learning/pattern-classification.pdf#page=706) |
| A.4 Probability Theory | [706](machine-learning/pattern-classification.pdf#page=706) |
| A.5 Gaussian derivatives and integrals | [718](machine-learning/pattern-classification.pdf#page=718) |
| A.6 Hypothesis testing | [724](machine-learning/pattern-classification.pdf#page=724) |
| A.7 Information theory | [726](machine-learning/pattern-classification.pdf#page=726) |
| A.8 Computational complexity | [728](machine-learning/pattern-classification.pdf#page=728) |
| A Index (PDF 733 to 735) | [733](machine-learning/pattern-classification.pdf#page=733) |

### Pattern classification solutions

`machine-learning/pattern-classification-solutions.pdf`, 446 pages. David G. Stork, *Solution Manual to
accompany Pattern Classification (2nd ed.)* by Duda, Hart and Stork, copyright 2001, this version dated
June 18, 2003. The instructor's solutions manual for the book above: worked solutions to every
chapter's problems, notes on its computer exercises, sample final exams with solutions, worked
examples by section, and the errata for the first to fifth printings. Was `Duda-problemsolutions.pdf`.
Problem numbers follow the book's, so a problem in the book's chapter is found here by its number.

**Page numbers.** The printed page number is the PDF page minus 2 (printed page 7, where chapter 2
starts, is PDF page 9). The PDF's embedded page labels only count PDF pages and do not match what is
printed. There is no index.

| Chapter or section | PDF page |
| --- | --- |
| Preface | [3](machine-learning/pattern-classification-solutions.pdf#page=3) |
| Contents | [5](machine-learning/pattern-classification-solutions.pdf#page=5) |
| 1 Introduction | [7](machine-learning/pattern-classification-solutions.pdf#page=7) |
| 2 Bayesian decision theory | [9](machine-learning/pattern-classification-solutions.pdf#page=9) |
| 2 Computer exercises | [76](machine-learning/pattern-classification-solutions.pdf#page=76) |
| 3 Maximum likelihood and Bayesian parameter estimation | [79](machine-learning/pattern-classification-solutions.pdf#page=79) |
| 3 Computer exercises | [132](machine-learning/pattern-classification-solutions.pdf#page=132) |
| 4 Nonparametric techniques | [133](machine-learning/pattern-classification-solutions.pdf#page=133) |
| 4 Computer exercises | [176](machine-learning/pattern-classification-solutions.pdf#page=176) |
| 5 Linear discriminant functions | [179](machine-learning/pattern-classification-solutions.pdf#page=179) |
| 5 Computer exercises | [219](machine-learning/pattern-classification-solutions.pdf#page=219) |
| 6 Multilayer neural networks | [221](machine-learning/pattern-classification-solutions.pdf#page=221) |
| 6 Computer exercises | [256](machine-learning/pattern-classification-solutions.pdf#page=256) |
| 7 Stochastic methods | [257](machine-learning/pattern-classification-solutions.pdf#page=257) |
| 7 Computer exercises | [278](machine-learning/pattern-classification-solutions.pdf#page=278) |
| 8 Nonmetric methods | [279](machine-learning/pattern-classification-solutions.pdf#page=279) |
| 8 Computer exercises | [296](machine-learning/pattern-classification-solutions.pdf#page=296) |
| 9 Algorithm-independent machine learning | [297](machine-learning/pattern-classification-solutions.pdf#page=297) |
| 9 Computer exercises | [306](machine-learning/pattern-classification-solutions.pdf#page=306) |
| 10 Unsupervised learning and clustering | [307](machine-learning/pattern-classification-solutions.pdf#page=307) |
| 10 Computer exercises | [357](machine-learning/pattern-classification-solutions.pdf#page=357) |
| Sample final exams and solutions | [359](machine-learning/pattern-classification-solutions.pdf#page=359) |
| Worked examples | [417](machine-learning/pattern-classification-solutions.pdf#page=417) |
| Errata in the text: first and second printings | [419](machine-learning/pattern-classification-solutions.pdf#page=419) |
| Errata in the text: fifth printing | [445](machine-learning/pattern-classification-solutions.pdf#page=445) |

### Probabilistic machine learning: an introduction

`machine-learning/probabilistic-machine-learning-an-introduction.pdf`, 863 pages. Kevin P. Murphy, *Probabilistic Machine Learning: An Introduction*, MIT Press,
copyright 2021, published 2022 (the first of two volumes; the second, *Probabilistic Machine Learning:
Advanced Topics*, is on the shelf as [the advanced-topics volume](machine-learning/probabilistic-machine-learning-advanced-topics.pdf),
with its own section below). The book builds machine learning from probability: Part I
covers probability, statistics, decision theory, information theory, linear algebra and optimisation;
Part II linear models; Part III neural networks; Part IV nonparametric models; Part V dimensionality
reduction, clustering and more. Sections marked with a star are optional. Was `Probabilistic Machine
Learning.pdf`. The table is from the PDF's own outline, with sections numbered in the printed order; the
printed page number is the PDF page minus 28. The notation appendix is listed as one row.

| Chapter or section | PDF page |
| --- | --- |
| Preface | [27](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=27) |
| 1 Introduction | [29](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=29) |
| 1.1 What is machine learning? | [29](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=29) |
| 1.2 Supervised learning | [29](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=29) |
| 1.3 Unsupervised learning | [41](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=41) |
| 1.4 Reinforcement learning | [44](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=44) |
| 1.5 Data | [46](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=46) |
| 1.6 Discussion | [53](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=53) |
| Part: I Foundations | [57](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=57) |
| 2 Probability: univariate models | [59](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=59) |
| 2.1 Introduction | [59](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=59) |
| 2.2 Random variables | [61](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=61) |
| 2.3 Bayes' rule | [69](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=69) |
| 2.4 Bernoulli and binomial distributions | [73](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=73) |
| 2.5 Categorical and multinomial distributions | [77](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=77) |
| 2.6 Univariate Gaussian (normal) distribution | [81](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=81) |
| 2.7 Some other common univariate distributions * | [85](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=85) |
| 2.8 Transformations of random variables * | [90](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=90) |
| 2.9 Exercises | [97](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=97) |
| 3 Probability: multivariate models | [101](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=101) |
| 3.1 Joint distributions for multiple random variables | [101](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=101) |
| 3.2 The multivariate Gaussian (normal) distribution | [104](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=104) |
| 3.3 Linear Gaussian systems * | [109](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=109) |
| 3.4 Mixture models | [112](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=112) |
| 3.5 Probabilistic graphical models * | [118](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=118) |
| 3.6 Exercises | [125](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=125) |
| 4 Statistics | [127](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=127) |
| 4.1 Introduction | [127](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=127) |
| 4.2 Maximum likelihood estimation (MLE) | [127](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=127) |
| 4.3 Empirical risk minimization (ERM) | [135](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=135) |
| 4.4 Other estimation methods * | [136](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=136) |
| 4.5 Regularization | [140](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=140) |
| 4.6 Bayesian statistics * | [149](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=149) |
| 4.7 Frequentist statistics * | [174](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=174) |
| 4.8 Exercises | [182](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=182) |
| 5 Decision theory | [187](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=187) |
| 5.1 Bayesian decision theory | [187](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=187) |
| 5.2 A/B testing * | [199](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=199) |
| 5.3 Bandit problems * | [204](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=204) |
| 5.4 Bayesian hypothesis testing | [212](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=212) |
| 5.5 Frequentist decision theory | [220](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=220) |
| 5.6 Empirical risk minimization | [224](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=224) |
| 5.7 Frequentist hypothesis testing * | [229](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=229) |
| 5.8 Exercises | [234](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=234) |
| 6 Information theory | [237](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=237) |
| 6.1 Entropy | [237](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=237) |
| 6.2 Relative entropy (KL divergence) * | [243](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=243) |
| 6.3 Mutual information * | [247](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=247) |
| 6.4 Exercises | [256](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=256) |
| 7 Linear algebra | [259](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=259) |
| 7.1 Introduction | [259](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=259) |
| 7.2 Matrix multiplication | [272](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=272) |
| 7.3 Matrix inversion | [279](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=279) |
| 7.4 Eigenvalue decomposition (EVD) | [282](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=282) |
| 7.5 Singular value decomposition (SVD) | [287](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=287) |
| 7.6 Other matrix decompositions * | [292](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=292) |
| 7.7 Solving systems of linear equations * | [294](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=294) |
| 7.8 Matrix calculus | [297](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=297) |
| 7.9 Exercises | [305](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=305) |
| 8 Optimization | [307](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=307) |
| 8.1 Introduction | [307](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=307) |
| 8.2 First-order methods | [314](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=314) |
| 8.3 Second-order methods | [320](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=320) |
| 8.4 Stochastic gradient descent | [327](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=327) |
| 8.5 Constrained optimization | [335](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=335) |
| 8.6 Proximal gradient method * | [342](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=342) |
| 8.7 Bound optimization * | [345](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=345) |
| 8.8 Blackbox and derivative free optimization | [356](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=356) |
| 8.9 Exercises | [358](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=358) |
| Part: II Linear models | [359](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=359) |
| 9 Linear discriminant analysis | [361](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=361) |
| 9.1 Introduction | [361](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=361) |
| 9.2 Gaussian discriminant analysis | [361](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=361) |
| 9.3 Naive Bayes classifiers | [370](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=370) |
| 9.4 Generative vs discriminative classifiers | [374](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=374) |
| 9.5 Exercises | [376](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=376) |
| 10 Logistic regression | [377](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=377) |
| 10.1 Introduction | [377](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=377) |
| 10.2 Binary logistic regression | [377](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=377) |
| 10.3 Multinomial logistic regression | [388](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=388) |
| 10.4 Robust logistic regression * | [397](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=397) |
| 10.5 Bayesian logistic regression * | [400](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=400) |
| 10.6 Exercises | [404](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=404) |
| 11 Linear regression | [407](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=407) |
| 11.1 Introduction | [407](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=407) |
| 11.2 Standard linear regression | [407](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=407) |
| 11.3 Ridge regression | [417](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=417) |
| 11.4 Robust linear regression * | [421](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=421) |
| 11.5 Lasso regression | [425](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=425) |
| 11.6 Bayesian linear regression * | [437](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=437) |
| 11.7 Exercises | [444](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=444) |
| 12 Generalized linear models * | [447](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=447) |
| 12.1 Introduction | [447](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=447) |
| 12.2 The exponential family | [447](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=447) |
| 12.3 Generalized linear models (GLMs) | [456](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=456) |
| 12.4 Probit regression | [460](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=460) |
| Part: III Deep neural networks | [465](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=465) |
| 13 Neural networks for unstructured data | [467](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=467) |
| 13.1 Introduction | [467](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=467) |
| 13.2 Multilayer perceptrons (MLPs) | [468](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=468) |
| 13.3 Backpropagation | [479](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=479) |
| 13.4 Training neural networks | [492](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=492) |
| 13.5 Regularization | [500](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=500) |
| 13.6 Other kinds of feedforward networks | [505](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=505) |
| 13.7 Exercises | [510](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=510) |
| 14 Neural networks for images | [511](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=511) |
| 14.1 Introduction | [511](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=511) |
| 14.2 Common layers | [512](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=512) |
| 14.3 Common architectures for image classification | [523](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=523) |
| 14.4 Other forms of convolution * | [528](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=528) |
| 14.5 Solving other discriminative vision tasks with CNNs | [531](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=531) |
| 14.6 Generating images by inverting CNNs * | [535](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=535) |
| 14.7 Adversarial Examples * | [542](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=542) |
| 15 Neural networks for sequences | [551](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=551) |
| 15.1 Introduction | [551](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=551) |
| 15.2 Recurrent neural networks (RNNs) | [551](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=551) |
| 15.3 1d CNNs | [564](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=564) |
| 15.4 Attention | [566](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=566) |
| 15.5 Transformers | [574](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=574) |
| 15.6 Efficient transformers * | [580](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=580) |
| 15.7 Language models and unsupervised representation learning | [584](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=584) |
| Part: IV Nonparametric models | [591](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=591) |
| 16 Exemplar-based methods | [593](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=593) |
| 16.1 K nearest neighbor (KNN) classification | [593](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=593) |
| 16.2 Learning distance metrics | [597](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=597) |
| 16.3 Kernel density estimation (KDE) | [605](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=605) |
| 17 Kernel methods | [613](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=613) |
| 17.1 Inferring functions from data | [613](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=613) |
| 17.2 Mercer kernels | [616](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=616) |
| 17.3 Gaussian processes | [622](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=622) |
| 17.4 Scaling GPs to large datasets | [630](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=630) |
| 17.5 Support vector machines (SVMs) | [633](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=633) |
| 17.6 Sparse vector machines | [646](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=646) |
| 17.7 Optimizing in function space * | [649](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=649) |
| 17.8 Exercises | [653](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=653) |
| 18 Trees, forests, bagging and boosting | [655](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=655) |
| 18.1 Classification and regression trees (CART) | [655](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=655) |
| 18.2 Ensemble learning | [660](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=660) |
| 18.3 Bagging | [661](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=661) |
| 18.4 Random forests | [662](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=662) |
| 18.5 Boosting | [663](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=663) |
| 18.6 Interpreting tree ensembles | [672](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=672) |
| Part: V Beyond supervised learning | [675](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=675) |
| 19 Learning with fewer labeled examples | [677](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=677) |
| 19.1 Data augmentation | [677](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=677) |
| 19.2 Transfer learning | [678](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=678) |
| 19.3 Semi-supervised learning | [684](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=684) |
| 19.4 Active learning | [696](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=696) |
| 19.5 Meta-learning * | [698](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=698) |
| 19.6 Few-shot learning * | [699](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=699) |
| 19.7 Exercises | [701](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=701) |
| 20 Dimensionality reduction | [703](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=703) |
| 20.1 Principal components analysis (PCA) | [703](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=703) |
| 20.2 Factor analysis * | [712](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=712) |
| 20.3 Autoencoders | [725](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=725) |
| 20.4 Manifold learning * | [734](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=734) |
| 20.5 Word embeddings | [751](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=751) |
| 20.6 Exercises | [758](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=758) |
| 21 Clustering | [761](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=761) |
| 21.1 Introduction | [761](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=761) |
| 21.2 Hierarchical agglomerative clustering | [763](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=763) |
| 21.3 K means clustering | [767](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=767) |
| 21.4 Clustering using mixture models | [775](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=775) |
| 21.5 Spectral clustering * | [780](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=780) |
| 21.6 Biclustering * | [783](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=783) |
| 22 Recommender systems | [787](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=787) |
| 22.1 Explicit feedback | [787](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=787) |
| 22.2 Implicit feedback | [792](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=792) |
| 22.3 Leveraging side information | [795](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=795) |
| 22.4 Exploration-exploitation tradeoff | [796](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=796) |
| 23 Graph embeddings * | [799](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=799) |
| 23.1 Introduction | [799](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=799) |
| 23.2 Graph Embedding as an Encoder/Decoder Problem | [800](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=800) |
| 23.3 Shallow graph embeddings | [802](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=802) |
| 23.4 Graph Neural Networks | [807](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=807) |
| 23.5 Deep graph embeddings | [811](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=811) |
| 23.6 Applications | [815](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=815) |
| Part: VI Appendix | [821](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=821) |
| Notation | [823](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=823) |
| Bibliography | [831](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=831) |

### Probabilistic machine learning: advanced topics

`machine-learning/probabilistic-machine-learning-advanced-topics.pdf`, 1,355 pages. Kevin P. Murphy,
*Probabilistic Machine Learning: Advanced Topics*, MIT Press, copyright 2023. This PDF is the author's
draft of August 2023 (its cover reads "Draft 08/2023"), released under a Creative Commons CC-BY-NC-ND
licence. It is the second of two volumes; the first is the introduction above. A published textbook at
research level: Part I revisits the fundamentals (probability, statistics, graphical models,
information theory, optimisation); Part II inference (Gaussian filtering and smoothing, message
passing, variational inference, Monte Carlo, MCMC, sequential Monte Carlo); Part III prediction
(generalized linear models, deep and Bayesian neural networks, Gaussian processes, beyond the iid
assumption); Part IV generation (VAEs, autoregressive models, normalizing flows, energy-based models,
diffusion models, GANs); Part V discovery (latent factor and state-space models, graph learning,
nonparametric Bayes, representation learning, interpretability); Part VI action (decision making,
reinforcement learning, causality). Was `Probabalistic Machine Learning Advance Topics Kevin P
Murphy.pdf`. The table is from the PDF's own outline: parts, chapters and sections, numbered in the
printed order. The outline's own Index and Bibliography bookmarks point at PDF pages 1253 and 1256,
which are wrong; the table gives the pages where each one starts. The printed page number is the PDF
page minus 33 throughout.

**Its index.** PDF pages 1256 to 1273 (printed 1223 to 1240), followed by the bibliography on PDF
pages 1274 to 1355. Entries cite printed page numbers, so the PDF page is the printed number plus 33:
"diffusion models, 857" opens at [890](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=890).
Each number is also a live link inside the PDF to the right page.

| Chapter or section | PDF page |
| --- | --- |
| Preface | [30](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=30) |
| 1 Introduction | [34](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=34) |
| Part: I Fundamentals | [36](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=36) |
| 2 Probability | [38](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=38) |
| 2.1 Introduction | [38](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=38) |
| 2.2 Some common probability distributions | [41](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=41) |
| 2.3 Gaussian joint distributions | [55](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=55) |
| 2.4 The exponential family | [66](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=66) |
| 2.5 Transformations of random variables | [77](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=77) |
| 2.6 Markov chains | [79](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=79) |
| 2.7 Divergence measures between probability distributions | [88](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=88) |
| 3 Statistics | [96](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=96) |
| 3.1 Introduction | [96](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=96) |
| 3.2 Bayesian statistics | [96](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=96) |
| 3.3 Frequentist statistics | [105](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=105) |
| 3.4 Conjugate priors | [116](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=116) |
| 3.5 Noninformative priors | [135](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=135) |
| 3.6 Hierarchical priors | [140](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=140) |
| 3.7 Empirical Bayes | [147](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=147) |
| 3.8 Model selection | [151](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=151) |
| 3.9 Model checking | [160](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=160) |
| 3.10 Hypothesis testing | [164](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=164) |
| 3.11 Missing data | [174](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=174) |
| 4 Graphical models | [176](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=176) |
| 4.1 Introduction | [176](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=176) |
| 4.2 Directed graphical models (Bayes nets) | [176](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=176) |
| 4.3 Undirected graphical models (Markov random fields) | [197](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=197) |
| 4.4 Conditional random fields (CRFs) | [218](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=218) |
| 4.5 Comparing directed and undirected PGMs | [226](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=226) |
| 4.6 PGM extensions | [234](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=234) |
| 4.7 Structural causal models | [244](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=244) |
| 5 Information theory | [250](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=250) |
| 5.1 KL divergence | [250](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=250) |
| 5.2 Entropy | [265](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=265) |
| 5.3 Mutual information | [269](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=269) |
| 5.4 Data compression (source coding) | [278](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=278) |
| 5.5 Error-correcting codes (channel coding) | [282](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=282) |
| 5.6 The information bottleneck | [283](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=283) |
| 6 Optimization | [288](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=288) |
| 6.1 Introduction | [288](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=288) |
| 6.2 Automatic differentiation | [288](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=288) |
| 6.3 Stochastic optimization | [298](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=298) |
| 6.4 Natural gradient descent | [306](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=306) |
| 6.5 Bound optimization (MM) algorithms | [314](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=314) |
| 6.6 Bayesian optimization | [324](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=324) |
| 6.7 Derivative-free optimization | [331](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=331) |
| 6.8 Optimal transport | [340](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=340) |
| 6.9 Submodular optimization | [349](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=349) |
| Part: II Inference | [370](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=370) |
| 7 Inference algorithms: an overview | [372](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=372) |
| 7.1 Introduction | [372](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=372) |
| 7.2 Common inference patterns | [373](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=373) |
| 7.3 Exact inference algorithms | [375](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=375) |
| 7.4 Approximate inference algorithms | [375](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=375) |
| 7.5 Evaluating approximate inference algorithms | [383](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=383) |
| 8 Gaussian filtering and smoothing | [386](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=386) |
| 8.1 Introduction | [386](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=386) |
| 8.2 Inference for linear-Gaussian SSMs | [390](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=390) |
| 8.3 Inference based on local linearization | [402](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=402) |
| 8.4 Inference based on the unscented transform | [406](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=406) |
| 8.5 Other variants of the Kalman filter | [410](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=410) |
| 8.6 Assumed density filtering | [418](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=418) |
| 8.7 Other inference methods for SSMs | [424](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=424) |
| 9 Message passing algorithms | [428](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=428) |
| 9.1 Introduction | [428](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=428) |
| 9.2 Belief propagation on chains | [428](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=428) |
| 9.3 Belief propagation on trees | [439](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=439) |
| 9.4 Loopy belief propagation | [444](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=444) |
| 9.5 The variable elimination (VE) algorithm | [455](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=455) |
| 9.6 The junction tree algorithm (JTA) | [461](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=461) |
| 9.7 Inference as optimization | [462](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=462) |
| 10 Variational inference | [466](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=466) |
| 10.1 Introduction | [466](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=466) |
| 10.2 Gradient-based VI | [472](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=472) |
| 10.3 Coordinate ascent VI | [482](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=482) |
| 10.4 More accurate variational posteriors | [498](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=498) |
| 10.5 Tighter bounds | [500](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=500) |
| 10.6 Wake-sleep algorithm | [502](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=502) |
| 10.7 Expectation propagation (EP) | [505](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=505) |
| 11 Monte Carlo methods | [510](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=510) |
| 11.1 Introduction | [510](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=510) |
| 11.2 Monte Carlo integration | [510](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=510) |
| 11.3 Generating random samples from simple distributions | [513](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=513) |
| 11.4 Rejection sampling | [514](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=514) |
| 11.5 Importance sampling | [517](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=517) |
| 11.6 Controlling Monte Carlo variance | [521](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=521) |
| 12 Markov chain Monte Carlo | [526](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=526) |
| 12.1 Introduction | [526](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=526) |
| 12.2 Metropolis-Hastings algorithm | [527](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=527) |
| 12.3 Gibbs sampling | [532](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=532) |
| 12.4 Auxiliary variable MCMC | [540](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=540) |
| 12.5 Hamiltonian Monte Carlo (HMC) | [543](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=543) |
| 12.6 MCMC convergence | [551](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=551) |
| 12.7 Stochastic gradient MCMC | [559](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=559) |
| 12.8 Reversible jump (transdimensional) MCMC | [563](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=563) |
| 12.9 Annealing methods | [566](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=566) |
| 13 Sequential Monte Carlo | [570](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=570) |
| 13.1 Introduction | [570](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=570) |
| 13.2 Particle filtering | [572](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=572) |
| 13.3 Proposal distributions | [580](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=580) |
| 13.4 Rao-Blackwellized particle filtering (RBPF) | [584](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=584) |
| 13.5 Extensions of the particle filter | [590](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=590) |
| 13.6 SMC samplers | [590](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=590) |
| Part: III Prediction | [600](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=600) |
| 14 Predictive models: an overview | [602](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=602) |
| 14.1 Introduction | [602](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=602) |
| 14.2 Evaluating predictive models | [605](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=605) |
| 14.3 Conformal prediction | [612](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=612) |
| 15 Generalized linear models | [616](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=616) |
| 15.1 Introduction | [616](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=616) |
| 15.2 Linear regression | [621](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=621) |
| 15.3 Logistic regression | [635](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=635) |
| 15.4 Probit regression | [646](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=646) |
| 15.5 Multilevel (hierarchical) GLMs | [650](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=650) |
| 16 Deep neural networks | [656](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=656) |
| 16.1 Introduction | [656](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=656) |
| 16.2 Building blocks of differentiable circuits | [656](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=656) |
| 16.3 Canonical examples of neural networks | [665](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=665) |
| 17 Bayesian neural networks | [672](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=672) |
| 17.1 Introduction | [672](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=672) |
| 17.2 Priors for BNNs | [672](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=672) |
| 17.3 Posteriors for BNNs | [676](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=676) |
| 17.4 Generalization in Bayesian deep learning | [690](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=690) |
| 17.5 Online inference | [697](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=697) |
| 17.6 Hierarchical Bayesian neural networks | [702](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=702) |
| 18 Gaussian processes | [706](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=706) |
| 18.1 Introduction | [706](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=706) |
| 18.2 Mercer kernels | [708](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=708) |
| 18.3 GPs with Gaussian likelihoods | [718](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=718) |
| 18.4 GPs with non-Gaussian likelihoods | [726](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=726) |
| 18.5 Scaling GP inference to large datasets | [730](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=730) |
| 18.6 Learning the kernel | [742](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=742) |
| 18.7 GPs and DNNs | [753](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=753) |
| 18.8 Gaussian processes for time series forecasting | [757](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=757) |
| 19 Beyond the iid assumption | [760](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=760) |
| 19.1 Introduction | [760](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=760) |
| 19.2 Distribution shift | [760](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=760) |
| 19.3 Detecting distribution shifts | [765](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=765) |
| 19.4 Robustness to distribution shifts | [770](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=770) |
| 19.5 Adapting to distribution shifts | [771](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=771) |
| 19.6 Learning from multiple distributions | [776](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=776) |
| 19.7 Continual learning | [783](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=783) |
| 19.8 Adversarial examples | [790](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=790) |
| Part: IV Generation | [796](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=796) |
| 20 Generative models: an overview | [798](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=798) |
| 20.1 Introduction | [798](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=798) |
| 20.2 Types of generative model | [798](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=798) |
| 20.3 Goals of generative modeling | [800](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=800) |
| 20.4 Evaluating generative models | [807](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=807) |
| 21 Variational autoencoders | [814](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=814) |
| 21.1 Introduction | [814](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=814) |
| 21.2 VAE basics | [814](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=814) |
| 21.3 VAE generalizations | [819](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=819) |
| 21.4 Avoiding posterior collapse | [829](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=829) |
| 21.5 VAEs with hierarchical structure | [832](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=832) |
| 21.6 Vector quantization VAE | [838](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=838) |
| 22 Autoregressive models | [844](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=844) |
| 22.1 Introduction | [844](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=844) |
| 22.2 Neural autoregressive density estimators (NADE) | [845](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=845) |
| 22.3 Causal CNNs | [845](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=845) |
| 22.4 Transformers | [847](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=847) |
| 23 Normalizing flows | [852](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=852) |
| 23.1 Introduction | [852](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=852) |
| 23.2 Constructing flows | [855](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=855) |
| 23.3 Applications | [869](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=869) |
| 24 Energy-based models | [872](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=872) |
| 24.1 Introduction | [872](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=872) |
| 24.2 Maximum likelihood training | [874](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=874) |
| 24.3 Score matching (SM) | [879](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=879) |
| 24.4 Noise contrastive estimation | [883](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=883) |
| 24.5 Other methods | [886](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=886) |
| 25 Diffusion models | [890](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=890) |
| 25.1 Introduction | [890](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=890) |
| 25.2 Denoising diffusion probabilistic models (DDPMs) | [890](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=890) |
| 25.3 Score-based generative models (SGMs) | [897](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=897) |
| 25.4 Continuous time models using differential equations | [900](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=900) |
| 25.5 Speeding up diffusion models | [904](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=904) |
| 25.6 Conditional generation | [908](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=908) |
| 25.7 Diffusion for discrete state spaces | [910](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=910) |
| 26 Generative adversarial networks | [916](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=916) |
| 26.1 Introduction | [916](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=916) |
| 26.2 Learning by comparison | [917](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=917) |
| 26.3 Generative adversarial networks | [927](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=927) |
| 26.4 Conditional GANs | [935](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=935) |
| 26.5 Inference with GANs | [936](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=936) |
| 26.6 Neural architectures in GANs | [937](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=937) |
| 26.7 Applications | [941](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=941) |
| Part: V Discovery | [948](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=948) |
| 27 Discovery methods: an overview | [950](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=950) |
| 27.1 Introduction | [950](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=950) |
| 27.2 Overview of Part V | [951](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=951) |
| 28 Latent factor models | [952](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=952) |
| 28.1 Introduction | [952](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=952) |
| 28.2 Mixture models | [952](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=952) |
| 28.3 Factor analysis | [963](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=963) |
| 28.4 LFMs with non-Gaussian priors | [982](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=982) |
| 28.5 Topic models | [986](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=986) |
| 28.6 Independent components analysis (ICA) | [994](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=994) |
| 29 State-space models | [1002](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1002) |
| 29.1 Introduction | [1002](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1002) |
| 29.2 Hidden Markov models (HMMs) | [1003](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1003) |
| 29.3 HMMs: applications | [1007](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1007) |
| 29.4 HMMs: parameter learning | [1013](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1013) |
| 29.5 HMMs: generalizations | [1020](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1020) |
| 29.6 Linear dynamical systems (LDSs) | [1029](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1029) |
| 29.7 LDS: applications | [1030](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1030) |
| 29.8 LDS: parameter learning | [1034](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1034) |
| 29.9 Switching linear dynamical systems (SLDSs) | [1038](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1038) |
| 29.10 Nonlinear SSMs | [1043](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1043) |
| 29.11 Non-Gaussian SSMs | [1044](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1044) |
| 29.12 Structural time series models | [1046](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1046) |
| 29.13 Deep SSMs | [1059](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1059) |
| 30 Graph learning | [1066](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1066) |
| 30.1 Introduction | [1066](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1066) |
| 30.2 Latent variable models for graphs | [1066](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1066) |
| 30.3 Graphical model structure learning | [1066](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1066) |
| 31 Nonparametric Bayesian models | [1070](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1070) |
| 31.1 Introduction | [1070](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1070) |
| 32 Representation learning | [1072](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1072) |
| 32.1 Introduction | [1072](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1072) |
| 32.2 Evaluating and comparing learned representations | [1072](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1072) |
| 32.3 Approaches for learning representations | [1079](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1079) |
| 32.4 Theory of representation learning | [1092](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1092) |
| 33 Interpretability | [1096](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1096) |
| 33.1 Introduction | [1096](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1096) |
| 33.2 Methods for interpretable machine learning | [1101](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1101) |
| 33.3 Properties: the abstraction between context and method | [1109](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1109) |
| 33.4 Evaluation of interpretable machine learning models | [1112](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1112) |
| 33.5 Discussion: how to think about interpretable machine learning | [1121](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1121) |
| Part: VI Action | [1126](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1126) |
| 34 Decision making under uncertainty | [1128](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1128) |
| 34.1 Statistical decision theory | [1128](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1128) |
| 34.2 Decision (influence) diagrams | [1134](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1134) |
| 34.3 A/B testing | [1138](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1138) |
| 34.4 Contextual bandits | [1142](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1142) |
| 34.5 Markov decision problems | [1151](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1151) |
| 34.6 Planning in an MDP | [1155](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1155) |
| 34.7 Active learning | [1159](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1159) |
| 35 Reinforcement learning | [1168](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1168) |
| 35.1 Introduction | [1168](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1168) |
| 35.2 Value-based RL | [1173](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1173) |
| 35.3 Policy-based RL | [1179](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1179) |
| 35.4 Model-based RL | [1186](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1186) |
| 35.5 Off-policy learning | [1193](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1193) |
| 35.6 Control as inference | [1200](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1200) |
| 36 Causality | [1206](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1206) |
| 36.1 Introduction | [1206](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1206) |
| 36.2 Causal formalism | [1208](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1208) |
| 36.3 Randomized control trials | [1215](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1215) |
| 36.4 Confounder adjustment | [1216](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1216) |
| 36.5 Instrumental variable strategies | [1230](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1230) |
| 36.6 Difference in differences | [1237](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1237) |
| 36.7 Credibility checks | [1241](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1241) |
| 36.8 The do-calculus | [1250](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1250) |
| 36.9 Further reading | [1253](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1253) |
| Index | [1256](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1256) |
| Bibliography | [1274](machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=1274) |

### Deep learning textbook

`machine-learning/deep-learning-textbook.pdf`, 801 pages. Ian Goodfellow, Yoshua Bengio and Aaron
Courville, *Deep Learning*, MIT Press, 2016 (the draft released on the book's website). A published
textbook in three parts: the applied maths a deep network rests on (linear algebra, probability and
information theory, numerical optimisation), modern practice (feedforward networks and back-propagation,
regularisation, optimisation, convolutional and recurrent nets), and research topics (autoencoders,
structured probabilistic models, Monte Carlo methods, score matching, approximate inference, Boltzmann
machines and other generative models). It predates diffusion models and does not cover them. Was
`Deep Learning.pdf`. No embedded outline; this table is from the printed contents, and each page was
checked against the heading printed on it. The page number printed on each page is the PDF page minus 16,
except the Index, which starts at PDF page 794. The back-of-book index cites a different printing, so
its numbers drift against this PDF (about one page near the front, about five near the back), and
adding 16 to an index number often misses. Convert an index entry through
`~/.claude/cache/book-indexes/deep-learning-textbook.json`, which moved each entry to the nearby page
that prints its term.

| Chapter or section | PDF page |
| --- | --- |
| 1 Introduction | [17](machine-learning/deep-learning-textbook.pdf#page=17) |
| 1.1 Who Should Read This Book? | [24](machine-learning/deep-learning-textbook.pdf#page=24) |
| 1.2 Historical Trends in Deep Learning | [27](machine-learning/deep-learning-textbook.pdf#page=27) |
| Part I: Applied Math and Machine Learning Basics | [45](machine-learning/deep-learning-textbook.pdf#page=45) |
| 2 Linear Algebra | [47](machine-learning/deep-learning-textbook.pdf#page=47) |
| 2.1 Scalars, Vectors, Matrices and Tensors | [47](machine-learning/deep-learning-textbook.pdf#page=47) |
| 2.2 Multiplying Matrices and Vectors | [50](machine-learning/deep-learning-textbook.pdf#page=50) |
| 2.3 Identity and Inverse Matrices | [52](machine-learning/deep-learning-textbook.pdf#page=52) |
| 2.4 Linear Dependence and Span | [53](machine-learning/deep-learning-textbook.pdf#page=53) |
| 2.5 Norms | [55](machine-learning/deep-learning-textbook.pdf#page=55) |
| 2.6 Special Kinds of Matrices and Vectors | [56](machine-learning/deep-learning-textbook.pdf#page=56) |
| 2.7 Eigendecomposition | [58](machine-learning/deep-learning-textbook.pdf#page=58) |
| 2.8 Singular Value Decomposition | [60](machine-learning/deep-learning-textbook.pdf#page=60) |
| 2.9 The Moore-Penrose Pseudoinverse | [61](machine-learning/deep-learning-textbook.pdf#page=61) |
| 2.10 The Trace Operator | [62](machine-learning/deep-learning-textbook.pdf#page=62) |
| 2.11 The Determinant | [63](machine-learning/deep-learning-textbook.pdf#page=63) |
| 2.12 Example: Principal Components Analysis | [64](machine-learning/deep-learning-textbook.pdf#page=64) |
| 3 Probability and Information Theory | [69](machine-learning/deep-learning-textbook.pdf#page=69) |
| 3.1 Why Probability? | [70](machine-learning/deep-learning-textbook.pdf#page=70) |
| 3.2 Random Variables | [72](machine-learning/deep-learning-textbook.pdf#page=72) |
| 3.3 Probability Distributions | [72](machine-learning/deep-learning-textbook.pdf#page=72) |
| 3.4 Marginal Probability | [74](machine-learning/deep-learning-textbook.pdf#page=74) |
| 3.5 Conditional Probability | [75](machine-learning/deep-learning-textbook.pdf#page=75) |
| 3.6 The Chain Rule of Conditional Probabilities | [75](machine-learning/deep-learning-textbook.pdf#page=75) |
| 3.7 Independence and Conditional Independence | [76](machine-learning/deep-learning-textbook.pdf#page=76) |
| 3.8 Expectation, Variance and Covariance | [76](machine-learning/deep-learning-textbook.pdf#page=76) |
| 3.9 Common Probability Distributions | [78](machine-learning/deep-learning-textbook.pdf#page=78) |
| 3.10 Useful Properties of Common Functions | [83](machine-learning/deep-learning-textbook.pdf#page=83) |
| 3.11 Bayes’ Rule | [86](machine-learning/deep-learning-textbook.pdf#page=86) |
| 3.12 Technical Details of Continuous Variables | [87](machine-learning/deep-learning-textbook.pdf#page=87) |
| 3.13 Information Theory | [89](machine-learning/deep-learning-textbook.pdf#page=89) |
| 3.14 Structured Probabilistic Models | [91](machine-learning/deep-learning-textbook.pdf#page=91) |
| 4 Numerical Computation | [96](machine-learning/deep-learning-textbook.pdf#page=96) |
| 4.1 Overﬂow and Underﬂow | [96](machine-learning/deep-learning-textbook.pdf#page=96) |
| 4.2 Poor Conditioning | [98](machine-learning/deep-learning-textbook.pdf#page=98) |
| 4.3 Gradient-Based Optimization | [98](machine-learning/deep-learning-textbook.pdf#page=98) |
| 4.4 Constrained Optimization | [109](machine-learning/deep-learning-textbook.pdf#page=109) |
| 4.5 Example: Linear Least Squares | [112](machine-learning/deep-learning-textbook.pdf#page=112) |
| 5 Machine Learning Basics | [114](machine-learning/deep-learning-textbook.pdf#page=114) |
| 5.1 Learning Algorithms | [115](machine-learning/deep-learning-textbook.pdf#page=115) |
| 5.2 Capacity, Overﬁtting and Underﬁtting | [126](machine-learning/deep-learning-textbook.pdf#page=126) |
| 5.3 Hyperparameters and Validation Sets | [136](machine-learning/deep-learning-textbook.pdf#page=136) |
| 5.4 Estimators, Bias and Variance | [138](machine-learning/deep-learning-textbook.pdf#page=138) |
| 5.5 Maximum Likelihood Estimation | [147](machine-learning/deep-learning-textbook.pdf#page=147) |
| 5.6 Bayesian Statistics | [151](machine-learning/deep-learning-textbook.pdf#page=151) |
| 5.7 Supervised Learning Algorithms | [156](machine-learning/deep-learning-textbook.pdf#page=156) |
| 5.8 Unsupervised Learning Algorithms | [162](machine-learning/deep-learning-textbook.pdf#page=162) |
| 5.9 Stochastic Gradient Descent | [167](machine-learning/deep-learning-textbook.pdf#page=167) |
| 5.10 Building a Machine Learning Algorithm | [169](machine-learning/deep-learning-textbook.pdf#page=169) |
| 5.11 Challenges Motivating Deep Learning | [171](machine-learning/deep-learning-textbook.pdf#page=171) |
| Part II: Deep Networks: Modern Practices | [182](machine-learning/deep-learning-textbook.pdf#page=182) |
| 6 Deep Feedforward Networks | [184](machine-learning/deep-learning-textbook.pdf#page=184) |
| 6.1 Example: Learning XOR | [187](machine-learning/deep-learning-textbook.pdf#page=187) |
| 6.2 Gradient-Based Learning | [193](machine-learning/deep-learning-textbook.pdf#page=193) |
| 6.3 Hidden Units | [207](machine-learning/deep-learning-textbook.pdf#page=207) |
| 6.4 Architecture Design | [213](machine-learning/deep-learning-textbook.pdf#page=213) |
| 6.5 Back-Propagation and Other Diﬀerentiation Algorithms | [220](machine-learning/deep-learning-textbook.pdf#page=220) |
| 6.6 Historical Notes | [240](machine-learning/deep-learning-textbook.pdf#page=240) |
| 7 Regularization for Deep Learning | [244](machine-learning/deep-learning-textbook.pdf#page=244) |
| 7.1 Parameter Norm Penalties | [246](machine-learning/deep-learning-textbook.pdf#page=246) |
| 7.2 Norm Penalties as Constrained Optimization | [253](machine-learning/deep-learning-textbook.pdf#page=253) |
| 7.3 Regularization and Under-Constrained Problems | [255](machine-learning/deep-learning-textbook.pdf#page=255) |
| 7.4 Dataset Augmentation | [256](machine-learning/deep-learning-textbook.pdf#page=256) |
| 7.5 Noise Robustness | [258](machine-learning/deep-learning-textbook.pdf#page=258) |
| 7.6 Semi-Supervised Learning | [259](machine-learning/deep-learning-textbook.pdf#page=259) |
| 7.7 Multi-Task Learning | [260](machine-learning/deep-learning-textbook.pdf#page=260) |
| 7.8 Early Stopping | [262](machine-learning/deep-learning-textbook.pdf#page=262) |
| 7.9 Parameter Tying and Parameter Sharing | [269](machine-learning/deep-learning-textbook.pdf#page=269) |
| 7.10 Sparse Representations | [270](machine-learning/deep-learning-textbook.pdf#page=270) |
| 7.11 Bagging and Other Ensemble Methods | [272](machine-learning/deep-learning-textbook.pdf#page=272) |
| 7.12 Dropout | [274](machine-learning/deep-learning-textbook.pdf#page=274) |
| 7.13 Adversarial Training | [284](machine-learning/deep-learning-textbook.pdf#page=284) |
| 7.14 Tangent Distance, Tangent Prop, and Manifold Tangent Classiﬁer | [286](machine-learning/deep-learning-textbook.pdf#page=286) |
| 8 Optimization for Training Deep Models | [290](machine-learning/deep-learning-textbook.pdf#page=290) |
| 8.1 How Learning Diﬀers from Pure Optimization | [291](machine-learning/deep-learning-textbook.pdf#page=291) |
| 8.2 Challenges in Neural Network Optimization | [298](machine-learning/deep-learning-textbook.pdf#page=298) |
| 8.3 Basic Algorithms | [310](machine-learning/deep-learning-textbook.pdf#page=310) |
| 8.4 Parameter Initialization Strategies | [317](machine-learning/deep-learning-textbook.pdf#page=317) |
| 8.5 Algorithms with Adaptive Learning Rates | [322](machine-learning/deep-learning-textbook.pdf#page=322) |
| 8.6 Approximate Second-Order Methods | [326](machine-learning/deep-learning-textbook.pdf#page=326) |
| 8.7 Optimization Strategies and Meta-Algorithms | [333](machine-learning/deep-learning-textbook.pdf#page=333) |
| 9 Convolutional Networks | [346](machine-learning/deep-learning-textbook.pdf#page=346) |
| 9.1 The Convolution Operation | [347](machine-learning/deep-learning-textbook.pdf#page=347) |
| 9.2 Motivation | [351](machine-learning/deep-learning-textbook.pdf#page=351) |
| 9.3 Pooling | [355](machine-learning/deep-learning-textbook.pdf#page=355) |
| 9.4 Convolution and Pooling as an Inﬁnitely Strong Prior | [361](machine-learning/deep-learning-textbook.pdf#page=361) |
| 9.5 Variants of the Basic Convolution Function | [363](machine-learning/deep-learning-textbook.pdf#page=363) |
| 9.6 Structured Outputs | [374](machine-learning/deep-learning-textbook.pdf#page=374) |
| 9.7 Data Types | [376](machine-learning/deep-learning-textbook.pdf#page=376) |
| 9.8 Eﬃcient Convolution Algorithms | [378](machine-learning/deep-learning-textbook.pdf#page=378) |
| 9.9 Random or Unsupervised Features | [379](machine-learning/deep-learning-textbook.pdf#page=379) |
| 9.10 The Neuroscientiﬁc Basis for Convolutional Networks | [380](machine-learning/deep-learning-textbook.pdf#page=380) |
| 9.11 Convolutional Networks and the History of Deep Learning | [387](machine-learning/deep-learning-textbook.pdf#page=387) |
| 10 Sequence Modeling: Recurrent and Recursive Nets | [389](machine-learning/deep-learning-textbook.pdf#page=389) |
| 10.1 Unfolding Computational Graphs | [391](machine-learning/deep-learning-textbook.pdf#page=391) |
| 10.2 Recurrent Neural Networks | [394](machine-learning/deep-learning-textbook.pdf#page=394) |
| 10.3 Bidirectional RNNs | [410](machine-learning/deep-learning-textbook.pdf#page=410) |
| 10.4 Encoder-Decoder Sequence-to-Sequence Architectures | [412](machine-learning/deep-learning-textbook.pdf#page=412) |
| 10.5 Deep Recurrent Networks | [414](machine-learning/deep-learning-textbook.pdf#page=414) |
| 10.6 Recursive Neural Networks | [416](machine-learning/deep-learning-textbook.pdf#page=416) |
| 10.7 The Challenge of Long-Term Dependencies | [417](machine-learning/deep-learning-textbook.pdf#page=417) |
| 10.8 Echo State Networks | [420](machine-learning/deep-learning-textbook.pdf#page=420) |
| 10.9 Leaky Units and Other Strategies for Multiple Time Scales | [422](machine-learning/deep-learning-textbook.pdf#page=422) |
| 10.10 The Long Short-Term Memory and Other Gated RNNs | [424](machine-learning/deep-learning-textbook.pdf#page=424) |
| 10.11 Optimization for Long-Term Dependencies | [429](machine-learning/deep-learning-textbook.pdf#page=429) |
| 10.12 Explicit Memory | [432](machine-learning/deep-learning-textbook.pdf#page=432) |
| 11 Practical Methodology | [437](machine-learning/deep-learning-textbook.pdf#page=437) |
| 11.1 Performance Metrics | [438](machine-learning/deep-learning-textbook.pdf#page=438) |
| 11.2 Default Baseline Models | [441](machine-learning/deep-learning-textbook.pdf#page=441) |
| 11.3 Determining Whether to Gather More Data | [442](machine-learning/deep-learning-textbook.pdf#page=442) |
| 11.4 Selecting Hyperparameters | [443](machine-learning/deep-learning-textbook.pdf#page=443) |
| 11.5 Debugging Strategies | [452](machine-learning/deep-learning-textbook.pdf#page=452) |
| 11.6 Example: Multi-Digit Number Recognition | [456](machine-learning/deep-learning-textbook.pdf#page=456) |
| 12 Applications | [459](machine-learning/deep-learning-textbook.pdf#page=459) |
| 12.1 Large-Scale Deep Learning | [459](machine-learning/deep-learning-textbook.pdf#page=459) |
| 12.2 Computer Vision | [468](machine-learning/deep-learning-textbook.pdf#page=468) |
| 12.3 Speech Recognition | [474](machine-learning/deep-learning-textbook.pdf#page=474) |
| 12.4 Natural Language Processing | [477](machine-learning/deep-learning-textbook.pdf#page=477) |
| 12.5 Other Applications | [494](machine-learning/deep-learning-textbook.pdf#page=494) |
| Part III: Deep Learning Research | [502](machine-learning/deep-learning-textbook.pdf#page=502) |
| 13 Linear Factor Models | [505](machine-learning/deep-learning-textbook.pdf#page=505) |
| 13.1 Probabilistic PCA and Factor Analysis | [506](machine-learning/deep-learning-textbook.pdf#page=506) |
| 13.2 Independent Component Analysis (ICA) | [507](machine-learning/deep-learning-textbook.pdf#page=507) |
| 13.3 Slow Feature Analysis | [509](machine-learning/deep-learning-textbook.pdf#page=509) |
| 13.4 Sparse Coding | [512](machine-learning/deep-learning-textbook.pdf#page=512) |
| 13.5 Manifold Interpretation of PCA | [515](machine-learning/deep-learning-textbook.pdf#page=515) |
| 14 Autoencoders | [518](machine-learning/deep-learning-textbook.pdf#page=518) |
| 14.1 Undercomplete Autoencoders | [519](machine-learning/deep-learning-textbook.pdf#page=519) |
| 14.2 Regularized Autoencoders | [520](machine-learning/deep-learning-textbook.pdf#page=520) |
| 14.3 Representational Power, Layer Size and Depth | [524](machine-learning/deep-learning-textbook.pdf#page=524) |
| 14.4 Stochastic Encoders and Decoders | [525](machine-learning/deep-learning-textbook.pdf#page=525) |
| 14.5 Denoising Autoencoders | [526](machine-learning/deep-learning-textbook.pdf#page=526) |
| 14.6 Learning Manifolds with Autoencoders | [531](machine-learning/deep-learning-textbook.pdf#page=531) |
| 14.7 Contractive Autoencoders | [537](machine-learning/deep-learning-textbook.pdf#page=537) |
| 14.8 Predictive Sparse Decomposition | [539](machine-learning/deep-learning-textbook.pdf#page=539) |
| 14.9 Applications of Autoencoders | [540](machine-learning/deep-learning-textbook.pdf#page=540) |
| 15 Representation Learning | [542](machine-learning/deep-learning-textbook.pdf#page=542) |
| 15.1 Greedy Layer-Wise Unsupervised Pretraining | [544](machine-learning/deep-learning-textbook.pdf#page=544) |
| 15.2 Transfer Learning and Domain Adaptation | [552](machine-learning/deep-learning-textbook.pdf#page=552) |
| 15.3 Semi-Supervised Disentangling of Causal Factors | [557](machine-learning/deep-learning-textbook.pdf#page=557) |
| 15.4 Distributed Representation | [562](machine-learning/deep-learning-textbook.pdf#page=562) |
| 15.5 Exponential Gains from Depth | [569](machine-learning/deep-learning-textbook.pdf#page=569) |
| 15.6 Providing Clues to Discover Underlying Causes | [570](machine-learning/deep-learning-textbook.pdf#page=570) |
| 16 Structured Probabilistic Models for Deep Learning | [574](machine-learning/deep-learning-textbook.pdf#page=574) |
| 16.1 The Challenge of Unstructured Modeling | [575](machine-learning/deep-learning-textbook.pdf#page=575) |
| 16.2 Using Graphs to Describe Model Structure | [579](machine-learning/deep-learning-textbook.pdf#page=579) |
| 16.3 Sampling from Graphical Models | [596](machine-learning/deep-learning-textbook.pdf#page=596) |
| 16.4 Advantages of Structured Modeling | [598](machine-learning/deep-learning-textbook.pdf#page=598) |
| 16.5 Learning about Dependencies | [598](machine-learning/deep-learning-textbook.pdf#page=598) |
| 16.6 Inference and Approximate Inference | [600](machine-learning/deep-learning-textbook.pdf#page=600) |
| 16.7 The Deep Learning Approach to Structured Probabilistic Models | [601](machine-learning/deep-learning-textbook.pdf#page=601) |
| 17 Monte Carlo Methods | [606](machine-learning/deep-learning-textbook.pdf#page=606) |
| 17.1 Sampling and Monte Carlo Methods | [606](machine-learning/deep-learning-textbook.pdf#page=606) |
| 17.2 Importance Sampling | [608](machine-learning/deep-learning-textbook.pdf#page=608) |
| 17.3 Markov Chain Monte Carlo Methods | [611](machine-learning/deep-learning-textbook.pdf#page=611) |
| 17.4 Gibbs Sampling | [615](machine-learning/deep-learning-textbook.pdf#page=615) |
| 17.5 The Challenge of Mixing between Separated Modes | [615](machine-learning/deep-learning-textbook.pdf#page=615) |
| 18 Confronting the Partition Function | [621](machine-learning/deep-learning-textbook.pdf#page=621) |
| 18.1 The Log-Likelihood Gradient | [622](machine-learning/deep-learning-textbook.pdf#page=622) |
| 18.2 Stochastic Maximum Likelihood and Contrastive Divergence | [623](machine-learning/deep-learning-textbook.pdf#page=623) |
| 18.3 Pseudolikelihood | [631](machine-learning/deep-learning-textbook.pdf#page=631) |
| 18.4 Score Matching and Ratio Matching | [633](machine-learning/deep-learning-textbook.pdf#page=633) |
| 18.5 Denoising Score Matching | [635](machine-learning/deep-learning-textbook.pdf#page=635) |
| 18.6 Noise-Contrastive Estimation | [636](machine-learning/deep-learning-textbook.pdf#page=636) |
| 18.7 Estimating the Partition Function | [639](machine-learning/deep-learning-textbook.pdf#page=639) |
| 19 Approximate Inference | [647](machine-learning/deep-learning-textbook.pdf#page=647) |
| 19.1 Inference as Optimization | [649](machine-learning/deep-learning-textbook.pdf#page=649) |
| 19.2 Expectation Maximization | [650](machine-learning/deep-learning-textbook.pdf#page=650) |
| 19.3 MAP Inference and Sparse Coding | [651](machine-learning/deep-learning-textbook.pdf#page=651) |
| 19.4 Variational Inference and Learning | [654](machine-learning/deep-learning-textbook.pdf#page=654) |
| 19.5 Learned Approximate Inference | [667](machine-learning/deep-learning-textbook.pdf#page=667) |
| 20 Deep Generative Models | [670](machine-learning/deep-learning-textbook.pdf#page=670) |
| 20.1 Boltzmann Machines | [670](machine-learning/deep-learning-textbook.pdf#page=670) |
| 20.2 Restricted Boltzmann Machines | [672](machine-learning/deep-learning-textbook.pdf#page=672) |
| 20.3 Deep Belief Networks | [676](machine-learning/deep-learning-textbook.pdf#page=676) |
| 20.4 Deep Boltzmann Machines | [679](machine-learning/deep-learning-textbook.pdf#page=679) |
| 20.5 Boltzmann Machines for Real-Valued Data | [692](machine-learning/deep-learning-textbook.pdf#page=692) |
| 20.6 Convolutional Boltzmann Machines | [699](machine-learning/deep-learning-textbook.pdf#page=699) |
| 20.7 Boltzmann Machines for Structured or Sequential Outputs | [701](machine-learning/deep-learning-textbook.pdf#page=701) |
| 20.8 Other Boltzmann Machines | [702](machine-learning/deep-learning-textbook.pdf#page=702) |
| 20.9 Back-Propagation through Random Operations | [703](machine-learning/deep-learning-textbook.pdf#page=703) |
| 20.10 Directed Generative Nets | [708](machine-learning/deep-learning-textbook.pdf#page=708) |
| 20.11 Drawing Samples from Autoencoders | [727](machine-learning/deep-learning-textbook.pdf#page=727) |
| 20.12 Generative Stochastic Networks | [730](machine-learning/deep-learning-textbook.pdf#page=730) |
| 20.13 Other Generation Schemes | [732](machine-learning/deep-learning-textbook.pdf#page=732) |
| 20.14 Evaluating Generative Models | [733](machine-learning/deep-learning-textbook.pdf#page=733) |
| 20.15 Conclusion | [736](machine-learning/deep-learning-textbook.pdf#page=736) |
| Bibliography | [737](machine-learning/deep-learning-textbook.pdf#page=737) |
| Index | [794](machine-learning/deep-learning-textbook.pdf#page=794) |

### Understanding deep learning

`machine-learning/understanding-deep-learning.pdf`, 541 pages. Simon J. D. Prince, *Understanding Deep
Learning*, MIT Press, December 2023; this file is the author's open copy dated 3 April 2024. A published
textbook that builds up from linear regression and shallow networks through loss functions, gradients and
backpropagation, convolutional nets, residual nets and transformers, to generative models (GANs,
normalizing flows, variational autoencoders, diffusion models), reinforcement learning, and why deep
learning works. Appendix C covers the probability it uses. Was `Underestand Deep Learning.pdf`. The table
is from the PDF's own outline, chapters and their first-level sections. The printed page number is the PDF
page minus 14 from chapter 1 on; the front matter is numbered in roman.

| Chapter or section | PDF page |
| --- | --- |
| Preface | [5](machine-learning/understanding-deep-learning.pdf#page=5) |
| Acknowledgements | [11](machine-learning/understanding-deep-learning.pdf#page=11) |
| 1 Introduction | [15](machine-learning/understanding-deep-learning.pdf#page=15) |
| 1.1 Supervised learning | [15](machine-learning/understanding-deep-learning.pdf#page=15) |
| 1.2 Unsupervised learning | [21](machine-learning/understanding-deep-learning.pdf#page=21) |
| 1.3 Reinforcement learning | [25](machine-learning/understanding-deep-learning.pdf#page=25) |
| 1.4 Ethics | [26](machine-learning/understanding-deep-learning.pdf#page=26) |
| 1.5 Structure of book | [29](machine-learning/understanding-deep-learning.pdf#page=29) |
| 1.6 Other books | [29](machine-learning/understanding-deep-learning.pdf#page=29) |
| 1.7 How to read this book | [30](machine-learning/understanding-deep-learning.pdf#page=30) |
| 2 Supervised learning | [31](machine-learning/understanding-deep-learning.pdf#page=31) |
| 2.1 Supervised learning overview | [31](machine-learning/understanding-deep-learning.pdf#page=31) |
| 2.2 Linear regression example | [32](machine-learning/understanding-deep-learning.pdf#page=32) |
| 2.3 Summary | [36](machine-learning/understanding-deep-learning.pdf#page=36) |
| 3 Shallow neural networks | [39](machine-learning/understanding-deep-learning.pdf#page=39) |
| 3.1 Neural network example | [39](machine-learning/understanding-deep-learning.pdf#page=39) |
| 3.2 Universal approximation theorem | [43](machine-learning/understanding-deep-learning.pdf#page=43) |
| 3.3 Multivariate inputs and outputs | [44](machine-learning/understanding-deep-learning.pdf#page=44) |
| 3.4 Shallow neural networks: general case | [47](machine-learning/understanding-deep-learning.pdf#page=47) |
| 3.5 Terminology | [49](machine-learning/understanding-deep-learning.pdf#page=49) |
| 3.6 Summary | [50](machine-learning/understanding-deep-learning.pdf#page=50) |
| 4 Deep neural networks | [55](machine-learning/understanding-deep-learning.pdf#page=55) |
| 4.1 Composing neural networks | [55](machine-learning/understanding-deep-learning.pdf#page=55) |
| 4.2 From composing networks to deep networks | [57](machine-learning/understanding-deep-learning.pdf#page=57) |
| 4.3 Deep neural networks | [59](machine-learning/understanding-deep-learning.pdf#page=59) |
| 4.4 Matrix notation | [62](machine-learning/understanding-deep-learning.pdf#page=62) |
| 4.5 Shallow vs. deep neural networks | [63](machine-learning/understanding-deep-learning.pdf#page=63) |
| 4.6 Summary | [66](machine-learning/understanding-deep-learning.pdf#page=66) |
| 5 Loss functions | [70](machine-learning/understanding-deep-learning.pdf#page=70) |
| 5.1 Maximum likelihood | [70](machine-learning/understanding-deep-learning.pdf#page=70) |
| 5.2 Recipe for constructing loss functions | [74](machine-learning/understanding-deep-learning.pdf#page=74) |
| 5.3 Example 1: univariate regression | [75](machine-learning/understanding-deep-learning.pdf#page=75) |
| 5.4 Example 2: binary classification | [78](machine-learning/understanding-deep-learning.pdf#page=78) |
| 5.5 Example 3: multiclass classification | [81](machine-learning/understanding-deep-learning.pdf#page=81) |
| 5.6 Multiple outputs | [83](machine-learning/understanding-deep-learning.pdf#page=83) |
| 5.7 Cross-entropy loss | [85](machine-learning/understanding-deep-learning.pdf#page=85) |
| 5.8 Summary | [86](machine-learning/understanding-deep-learning.pdf#page=86) |
| 6 Fitting models | [91](machine-learning/understanding-deep-learning.pdf#page=91) |
| 6.1 Gradient descent | [91](machine-learning/understanding-deep-learning.pdf#page=91) |
| 6.2 Stochastic gradient descent | [97](machine-learning/understanding-deep-learning.pdf#page=97) |
| 6.3 Momentum | [100](machine-learning/understanding-deep-learning.pdf#page=100) |
| 6.4 Adam | [102](machine-learning/understanding-deep-learning.pdf#page=102) |
| 6.5 Training algorithm hyperparameters | [105](machine-learning/understanding-deep-learning.pdf#page=105) |
| 6.6 Summary | [105](machine-learning/understanding-deep-learning.pdf#page=105) |
| 7 Gradients and initialization | [110](machine-learning/understanding-deep-learning.pdf#page=110) |
| 7.1 Problem definitions | [110](machine-learning/understanding-deep-learning.pdf#page=110) |
| 7.2 Computing derivatives | [111](machine-learning/understanding-deep-learning.pdf#page=111) |
| 7.3 Toy example | [114](machine-learning/understanding-deep-learning.pdf#page=114) |
| 7.4 Backpropagation algorithm | [117](machine-learning/understanding-deep-learning.pdf#page=117) |
| 7.5 Parameter initialization | [121](machine-learning/understanding-deep-learning.pdf#page=121) |
| 7.6 Example training code | [125](machine-learning/understanding-deep-learning.pdf#page=125) |
| 7.7 Summary | [125](machine-learning/understanding-deep-learning.pdf#page=125) |
| 8 Measuring performance | [132](machine-learning/understanding-deep-learning.pdf#page=132) |
| 8.1 Training a simple model | [132](machine-learning/understanding-deep-learning.pdf#page=132) |
| 8.2 Sources of error | [134](machine-learning/understanding-deep-learning.pdf#page=134) |
| 8.3 Reducing error | [138](machine-learning/understanding-deep-learning.pdf#page=138) |
| 8.4 Double descent | [141](machine-learning/understanding-deep-learning.pdf#page=141) |
| 8.5 Choosing hyperparameters | [146](machine-learning/understanding-deep-learning.pdf#page=146) |
| 8.6 Summary | [147](machine-learning/understanding-deep-learning.pdf#page=147) |
| 9 Regularization | [152](machine-learning/understanding-deep-learning.pdf#page=152) |
| 9.1 Explicit regularization | [152](machine-learning/understanding-deep-learning.pdf#page=152) |
| 9.2 Implicit regularization | [155](machine-learning/understanding-deep-learning.pdf#page=155) |
| 9.3 Heuristics to improve performance | [158](machine-learning/understanding-deep-learning.pdf#page=158) |
| 9.4 Summary | [168](machine-learning/understanding-deep-learning.pdf#page=168) |
| 10 Convolutional networks | [175](machine-learning/understanding-deep-learning.pdf#page=175) |
| 10.1 Invariance and equivariance | [175](machine-learning/understanding-deep-learning.pdf#page=175) |
| 10.2 Convolutional networks for 1D inputs | [177](machine-learning/understanding-deep-learning.pdf#page=177) |
| 10.3 Convolutional networks for 2D inputs | [184](machine-learning/understanding-deep-learning.pdf#page=184) |
| 10.4 Downsampling and upsampling | [185](machine-learning/understanding-deep-learning.pdf#page=185) |
| 10.5 Applications | [188](machine-learning/understanding-deep-learning.pdf#page=188) |
| 10.6 Summary | [193](machine-learning/understanding-deep-learning.pdf#page=193) |
| 11 Residual networks | [200](machine-learning/understanding-deep-learning.pdf#page=200) |
| 11.1 Sequential processing | [200](machine-learning/understanding-deep-learning.pdf#page=200) |
| 11.2 Residual connections and residual blocks | [203](machine-learning/understanding-deep-learning.pdf#page=203) |
| 11.3 Exploding gradients in residual networks | [206](machine-learning/understanding-deep-learning.pdf#page=206) |
| 11.4 Batch normalization | [206](machine-learning/understanding-deep-learning.pdf#page=206) |
| 11.5 Common residual architectures | [209](machine-learning/understanding-deep-learning.pdf#page=209) |
| 11.6 Why do nets with residual connections perform so well? | [213](machine-learning/understanding-deep-learning.pdf#page=213) |
| 11.7 Summary | [213](machine-learning/understanding-deep-learning.pdf#page=213) |
| 12 Transformers | [221](machine-learning/understanding-deep-learning.pdf#page=221) |
| 12.1 Processing text data | [221](machine-learning/understanding-deep-learning.pdf#page=221) |
| 12.2 Dot-product self-attention | [222](machine-learning/understanding-deep-learning.pdf#page=222) |
| 12.3 Extensions to dot-product self-attention | [227](machine-learning/understanding-deep-learning.pdf#page=227) |
| 12.4 Transformer layers | [229](machine-learning/understanding-deep-learning.pdf#page=229) |
| 12.5 Transformers for natural language processing | [230](machine-learning/understanding-deep-learning.pdf#page=230) |
| 12.6 Encoder model example: BERT | [233](machine-learning/understanding-deep-learning.pdf#page=233) |
| 12.7 Decoder model example: GPT3 | [236](machine-learning/understanding-deep-learning.pdf#page=236) |
| 12.8 Encoder-decoder model example: machine translation | [240](machine-learning/understanding-deep-learning.pdf#page=240) |
| 12.9 Transformers for long sequences | [241](machine-learning/understanding-deep-learning.pdf#page=241) |
| 12.10 Transformers for images | [242](machine-learning/understanding-deep-learning.pdf#page=242) |
| 12.11 Summary | [246](machine-learning/understanding-deep-learning.pdf#page=246) |
| 13 Graph neural networks | [254](machine-learning/understanding-deep-learning.pdf#page=254) |
| 13.1 What is a graph? | [254](machine-learning/understanding-deep-learning.pdf#page=254) |
| 13.2 Graph representation | [257](machine-learning/understanding-deep-learning.pdf#page=257) |
| 13.3 Graph neural networks, tasks, and loss functions | [259](machine-learning/understanding-deep-learning.pdf#page=259) |
| 13.4 Graph convolutional networks | [262](machine-learning/understanding-deep-learning.pdf#page=262) |
| 13.5 Example: graph classification | [265](machine-learning/understanding-deep-learning.pdf#page=265) |
| 13.6 Inductive vs. transductive models | [266](machine-learning/understanding-deep-learning.pdf#page=266) |
| 13.7 Example: node classification | [267](machine-learning/understanding-deep-learning.pdf#page=267) |
| 13.8 Layers for graph convolutional networks | [270](machine-learning/understanding-deep-learning.pdf#page=270) |
| 13.9 Edge graphs | [274](machine-learning/understanding-deep-learning.pdf#page=274) |
| 13.10 Summary | [275](machine-learning/understanding-deep-learning.pdf#page=275) |
| 14 Unsupervised learning | [282](machine-learning/understanding-deep-learning.pdf#page=282) |
| 14.1 Taxonomy of unsupervised learning models | [282](machine-learning/understanding-deep-learning.pdf#page=282) |
| 14.2 What makes a good generative model? | [283](machine-learning/understanding-deep-learning.pdf#page=283) |
| 14.3 Quantifying performance | [285](machine-learning/understanding-deep-learning.pdf#page=285) |
| 14.4 Summary | [287](machine-learning/understanding-deep-learning.pdf#page=287) |
| 15 Generative Adversarial Networks | [289](machine-learning/understanding-deep-learning.pdf#page=289) |
| 15.1 Discrimination as a signal | [289](machine-learning/understanding-deep-learning.pdf#page=289) |
| 15.2 Improving stability | [294](machine-learning/understanding-deep-learning.pdf#page=294) |
| 15.3 Progressive growing, minibatch discrimination, and truncation | [300](machine-learning/understanding-deep-learning.pdf#page=300) |
| 15.4 Conditional generation | [302](machine-learning/understanding-deep-learning.pdf#page=302) |
| 15.5 Image translation | [304](machine-learning/understanding-deep-learning.pdf#page=304) |
| 15.6 StyleGAN | [309](machine-learning/understanding-deep-learning.pdf#page=309) |
| 15.7 Summary | [311](machine-learning/understanding-deep-learning.pdf#page=311) |
| 16 Normalizing flows | [317](machine-learning/understanding-deep-learning.pdf#page=317) |
| 16.1 1D example | [317](machine-learning/understanding-deep-learning.pdf#page=317) |
| 16.2 General case | [320](machine-learning/understanding-deep-learning.pdf#page=320) |
| 16.3 Invertible network layers | [322](machine-learning/understanding-deep-learning.pdf#page=322) |
| 16.4 Multi-scale flows | [330](machine-learning/understanding-deep-learning.pdf#page=330) |
| 16.5 Applications | [331](machine-learning/understanding-deep-learning.pdf#page=331) |
| 16.6 Summary | [334](machine-learning/understanding-deep-learning.pdf#page=334) |
| 17 Variational autoencoders | [340](machine-learning/understanding-deep-learning.pdf#page=340) |
| 17.1 Latent variable models | [340](machine-learning/understanding-deep-learning.pdf#page=340) |
| 17.2 Nonlinear latent variable model | [341](machine-learning/understanding-deep-learning.pdf#page=341) |
| 17.3 Training | [344](machine-learning/understanding-deep-learning.pdf#page=344) |
| 17.4 ELBO properties | [347](machine-learning/understanding-deep-learning.pdf#page=347) |
| 17.5 Variational approximation | [349](machine-learning/understanding-deep-learning.pdf#page=349) |
| 17.6 The variational autoencoder | [349](machine-learning/understanding-deep-learning.pdf#page=349) |
| 17.7 The reparameterization trick | [352](machine-learning/understanding-deep-learning.pdf#page=352) |
| 17.8 Applications | [353](machine-learning/understanding-deep-learning.pdf#page=353) |
| 17.9 Summary | [356](machine-learning/understanding-deep-learning.pdf#page=356) |
| 18 Diffusion models | [362](machine-learning/understanding-deep-learning.pdf#page=362) |
| 18.1 Overview | [362](machine-learning/understanding-deep-learning.pdf#page=362) |
| 18.2 Encoder (forward process) | [363](machine-learning/understanding-deep-learning.pdf#page=363) |
| 18.3 Decoder model (reverse process) | [369](machine-learning/understanding-deep-learning.pdf#page=369) |
| 18.4 Training | [370](machine-learning/understanding-deep-learning.pdf#page=370) |
| 18.5 Reparameterization of loss function | [374](machine-learning/understanding-deep-learning.pdf#page=374) |
| 18.6 Implementation | [376](machine-learning/understanding-deep-learning.pdf#page=376) |
| 18.7 Summary | [381](machine-learning/understanding-deep-learning.pdf#page=381) |
| 19 Reinforcement learning | [387](machine-learning/understanding-deep-learning.pdf#page=387) |
| 19.1 Markov decision processes, returns, and policies | [387](machine-learning/understanding-deep-learning.pdf#page=387) |
| 19.2 Expected return | [391](machine-learning/understanding-deep-learning.pdf#page=391) |
| 19.3 Tabular reinforcement learning | [395](machine-learning/understanding-deep-learning.pdf#page=395) |
| 19.4 Fitted Q-learning | [399](machine-learning/understanding-deep-learning.pdf#page=399) |
| 19.5 Policy gradient methods | [402](machine-learning/understanding-deep-learning.pdf#page=402) |
| 19.6 Actor-critic methods | [407](machine-learning/understanding-deep-learning.pdf#page=407) |
| 19.7 Offline reinforcement learning | [408](machine-learning/understanding-deep-learning.pdf#page=408) |
| 19.8 Summary | [409](machine-learning/understanding-deep-learning.pdf#page=409) |
| 20 Why does deep learning work? | [415](machine-learning/understanding-deep-learning.pdf#page=415) |
| 20.1 The case against deep learning | [415](machine-learning/understanding-deep-learning.pdf#page=415) |
| 20.2 Factors that influence fitting performance | [416](machine-learning/understanding-deep-learning.pdf#page=416) |
| 20.3 Properties of loss functions | [420](machine-learning/understanding-deep-learning.pdf#page=420) |
| 20.4 Factors that determine generalization | [424](machine-learning/understanding-deep-learning.pdf#page=424) |
| 20.5 Do we need so many parameters? | [428](machine-learning/understanding-deep-learning.pdf#page=428) |
| 20.6 Do networks have to be deep? | [431](machine-learning/understanding-deep-learning.pdf#page=431) |
| 20.7 Summary | [432](machine-learning/understanding-deep-learning.pdf#page=432) |
| 21 Deep learning and ethics | [434](machine-learning/understanding-deep-learning.pdf#page=434) |
| 21.1 Value alignment | [434](machine-learning/understanding-deep-learning.pdf#page=434) |
| 21.2 Intentional misuse | [440](machine-learning/understanding-deep-learning.pdf#page=440) |
| 21.3 Other social, ethical, and professional issues | [442](machine-learning/understanding-deep-learning.pdf#page=442) |
| 21.4 Case study | [444](machine-learning/understanding-deep-learning.pdf#page=444) |
| 21.5 The value-free ideal of science | [445](machine-learning/understanding-deep-learning.pdf#page=445) |
| 21.6 Responsible AI research as a collective action problem | [446](machine-learning/understanding-deep-learning.pdf#page=446) |
| 21.7 Ways forward | [447](machine-learning/understanding-deep-learning.pdf#page=447) |
| 21.8 Summary | [448](machine-learning/understanding-deep-learning.pdf#page=448) |
| Appendix A: Notation | [450](machine-learning/understanding-deep-learning.pdf#page=450) |
| Appendix B: Mathematics | [453](machine-learning/understanding-deep-learning.pdf#page=453) |
| Functions | [453](machine-learning/understanding-deep-learning.pdf#page=453) |
| Binomial coefficients | [455](machine-learning/understanding-deep-learning.pdf#page=455) |
| Vector, matrices, and tensors | [456](machine-learning/understanding-deep-learning.pdf#page=456) |
| Special types of matrix | [459](machine-learning/understanding-deep-learning.pdf#page=459) |
| Matrix calculus | [461](machine-learning/understanding-deep-learning.pdf#page=461) |
| Appendix C: Probability | [462](machine-learning/understanding-deep-learning.pdf#page=462) |
| Random variables and probability distributions | [462](machine-learning/understanding-deep-learning.pdf#page=462) |
| Expectation | [466](machine-learning/understanding-deep-learning.pdf#page=466) |
| Normal probability distribution | [470](machine-learning/understanding-deep-learning.pdf#page=470) |
| Sampling | [473](machine-learning/understanding-deep-learning.pdf#page=473) |
| Distances between probability distributions | [473](machine-learning/understanding-deep-learning.pdf#page=473) |
| Bibliography | [476](machine-learning/understanding-deep-learning.pdf#page=476) |
| Index | [527](machine-learning/understanding-deep-learning.pdf#page=527) |

### The little book of generative AI foundations

`machine-learning/the-little-book-of-generative-ai-foundations.pdf`, 195 pages. Tianhua Chen, University of Huddersfield, *The Little Book of Generative AI Foundations: An
Intuitive Mathematical Primer*, arXiv 2605.29713 version 2 (cs.LG), preprint of 8 September 2026. A
preprint primer that derives the mathematics of the main generative-model families step by step. It runs
from PCA and autoencoders through probabilistic PCA, the evidence lower bound and EM, the variational
autoencoder and DDPM, then the calculus of continuous-time generative modelling (Brownian motion, the
Ornstein-Uhlenbeck process, the Liouville and Fokker-Planck equations), score matching, Langevin dynamics
and the reverse-time SDE, normalising flows, autoregressive models, GANs and energy-based models. The
appendices work Gaussian algebra (completing the square) and the DDPM reverse posterior. The equations
are not numbered, so a row below names the section a derivation sits in. It has no Itô lemma, no probability
flow ODE, no Tweedie's formula and no classifier-free guidance. Was `2605.29713v2.pdf`. The table is from the
PDF's own outline plus the contents pages, every section and subsection, with each page found from its
heading in the text. The printed page number is the PDF page minus 7 for chapters 1 to 8, the closing
remarks and the appendices (printed page 1 is PDF page 8; printed 3 is PDF 10, printed 106 is PDF 113); the
preface is numbered in roman, with i on PDF page 2.

| Chapter or section | PDF page |
| --- | --- |
| Preface | [2](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=2) |
| 1 Linear Algebra Foundations: From PCA to Autoencoders | [8](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=8) |
| 1.1 Matrices as Linear Transformations: Basis Directions, Projections, and Composition | [10](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=10) |
| 1.1.1 Matrices as Transformations of Basis Directions | [10](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=10) |
| 1.1.2 Two Views of Matrix Multiplication | [12](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=12) |
| 1.2 Eigenvectors, Eigenvalues, and a Matrix’s Natural Coordinate System | [14](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=14) |
| 1.3 Principal Component Analysis via Variance Maximisation | [16](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=16) |
| 1.3.1 Formulating PCA | [16](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=16) |
| 1.3.2 Solving the PCA optimisation problem | [18](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=18) |
| 1.3.3 PCA for dimensionality reduction | [19](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=19) |
| 1.4 PCA as a Change of Basis: Similarity Transformations and SVD | [20](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=20) |
| 1.4.1 Trace, similarity transformations, and variance preservation | [21](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=21) |
| 1.4.2 PCA as a similarity transformation | [22](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=22) |
| 1.4.3 From eigen-decomposition to singular value decomposition | [24](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=24) |
| 1.5 From PCA to Autoencoders: Reconstruction, Subspaces, and Manifolds | [25](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=25) |
| 1.5.1 From variance maximisation to reconstruction | [26](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=26) |
| 1.5.2 When does a linear autoencoder recover PCA? | [28](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=28) |
| 1.5.3 From linear subspaces to nonlinear manifolds | [30](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=30) |
| Summary and References (chapter 1) | [32](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=32) |
| 2 Probabilistic PCA: A Bridge to Latent-Variable Generative Modelling | [34](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=34) |
| 2.1 Formulation of Probabilistic PCA | [35](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=35) |
| 2.2 Why PPCA Is Analytically Tractable | [38](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=38) |
| 2.2.1 From Likelihood to Marginalisation | [38](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=38) |
| 2.2.2 Deriving and Interpreting the Marginal Distribution | [40](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=40) |
| 2.3 Learning PPCA: Three Optimisation Perspectives | [42](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=42) |
| 2.3.1 Direct analytic maximum likelihood | [43](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=43) |
| 2.3.2 Gradient-based optimisation | [43](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=43) |
| 2.3.3 Expectation–Maximisation (EM) | [44](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=44) |
| 2.4 Jensen’s Inequality and the Evidence Lower Bound | [45](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=45) |
| 2.4.1 From Marginal Likelihood to Jensen’s Inequality | [45](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=45) |
| 2.4.2 Deriving the Evidence Lower Bound | [46](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=46) |
| 2.4.3 When does the bound become exact? | [47](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=47) |
| 2.5 Expectation–Maximisation: Maximising the Lower Bound | [48](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=48) |
| 2.5.1 The two EM steps | [48](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=48) |
| 2.5.2 Applying EM to PPCA | [50](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=50) |
| 2.5.3 From PPCA to Regularised Latent Representations | [52](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=52) |
| Summary and References (chapter 2) | [52](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=52) |
| 3 The Variational Autoencoder: From Probabilistic Latent Variables to Variational Inference | [54](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=54) |
| 3.1 From Autoencoder to Variational Autoencoder | [55](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=55) |
| 3.1.1 Making the encoder probabilistic | [56](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=56) |
| 3.1.2 Making the decoder probabilistic | [58](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=58) |
| 3.1.3 Prior and Learning Difficulty | [59](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=59) |
| 3.2 From Intractable Likelihood to the ELBO | [60](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=60) |
| 3.2.1 Introducing the variational posterior | [60](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=60) |
| 3.2.2 Three Equivalent Forms of the ELBO | [61](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=61) |
| 3.3 Learning the Variational Autoencoder: Reparameterisation and Optimisation | [64](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=64) |
| Summary and References (chapter 3) | [67](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=67) |
| 4 Denoising Diffusion Probabilistic Models | [68](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=68) |
| 4.1 The Forward Diffusion Process: From Data to Noise | [70](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=70) |
| 4.1.1 Gaussian Noising and the Closed-Form Forward Process | [70](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=70) |
| 4.1.2 The forward chain and the Markov assumption | [72](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=72) |
| 4.2 The Reverse Process and the ELBO Formulation | [73](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=73) |
| 4.2.1 The learned reverse chain | [74](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=74) |
| 4.2.2 Why the reverse process is difficult | [74](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=74) |
| 4.2.3 The Diffusion ELBO | [75](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=75) |
| 4.3 From the Diffusion ELBO to a Step-wise Objective | [77](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=77) |
| 4.3.1 Expanding the Diffusion ELBO | [77](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=77) |
| 4.3.2 Rewriting the ELBO with Bayes’ rule | [79](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=79) |
| 4.3.3 From the global ELBO to local learning terms | [80](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=80) |
| 4.4 From the True Reverse Posterior to DDPM Learning | [82](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=82) |
| 4.4.1 The true reverse posterior from known forward quantities | [83](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=83) |
| 4.4.2 Reparameterising the posterior through the noise variable | [84](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=84) |
| 4.4.3 Parameterising the learned reverse process and deriving the practical DDPM objective | [85](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=85) |
| 4.4.4 How training and sampling work | [87](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=87) |
| Summary and References (chapter 4) | [88](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=88) |
| 5 Calculus Foundations for Continuous Time Generative Modelling | [89](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=89) |
| 5.1 From Discrete Updates to Continuous Motion | [91](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=91) |
| 5.1.1 Basic Language for Continuous-Time Motion | [91](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=91) |
| 5.1.2 Deterministic Contraction | [92](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=92) |
| 5.1.3 Brownian Motion | [95](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=95) |
| 5.1.4 The Ornstein–Uhlenbeck Process | [96](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=96) |
| 5.2 Deterministic Density Evolution | [98](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=98) |
| 5.2.1 Finite-Time Density Transformation | [99](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=99) |
| 5.2.2 Infinitesimal Density Evolution in One Dimension: The Liouville Equation | [100](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=100) |
| 5.2.3 Density Change Along a Trajectory | [102](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=102) |
| 5.2.4 Divergence and the Multidimensional Liouville Equation | [103](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=103) |
| 5.3 Stochastic Density Evolution and the Fokker–Planck Equation | [106](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=106) |
| 5.3.1 Pure Brownian Diffusion as Gaussian Smoothing | [106](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=106) |
| 5.3.2 From Brownian Diffusion to the Fokker–Planck Equation | [107](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=107) |
| 5.3.3 Multidimensional Form and Interpretation | [109](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=109) |
| Summary and References (chapter 5) | [110](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=110) |
| 6 Score-Based Generative Modelling and Continuous-Time Diffusion | [111](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=111) |
| 6.1 From the Score Function to Langevin Sampling | [113](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=113) |
| 6.1.1 The Score Function as a Probabilistic Drift Field | [114](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=114) |
| 6.1.2 Langevin Dynamics: Score Plus Noise | [115](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=115) |
| 6.1.3 Target and Stationary Distributions | [117](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=117) |
| 6.2 Learning the Score: Fisher Divergence and Score Matching | [119](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=119) |
| 6.2.1 Expanding the Fisher Divergence | [119](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=119) |
| 6.2.2 The One-Dimensional Case | [120](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=120) |
| 6.2.3 Extension to Multiple Dimensions | [121](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=121) |
| 6.3 Stabilising Learning: Denoising Score Matching via Corruption | [123](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=123) |
| 6.3.1 Gaussian Corruption and Smoothed Scores | [123](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=123) |
| 6.3.2 The Intractability of the Noisy Score | [125](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=125) |
| 6.3.3 Denoising Score Matching as Regression | [125](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=125) |
| 6.4 From Multi-Scale Score Learning to Continuous-Time Diffusion | [128](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=128) |
| 6.4.1 Multi-Scale Denoising Score Matching | [128](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=128) |
| 6.4.2 Annealed Langevin Dynamics | [130](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=130) |
| 6.4.3 From Discrete Noise Levels to a Continuous Diffusion Process | [131](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=131) |
| 6.4.4 Reverse-Time Dynamics and the Role of the Score | [132](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=132) |
| 6.5 Discrete Diffusion Models Through the Score-Based Lens | [134](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=134) |
| 6.5.1 Noise Prediction and Conditional Scores | [134](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=134) |
| 6.5.2 A Unified View of Score-Based Diffusion | [135](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=135) |
| Summary and References (chapter 6) | [136](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=136) |
| 7 Exact Density Models: Normalising Flows and Autoregressive Factorisations | [138](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=138) |
| 7.1 Normalising Flows: Exact Density via Invertible Transformations | [140](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=140) |
| 7.1.1 Revisiting the Change-of-Variables Formula | [140](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=140) |
| 7.1.2 Planar Flows | [143](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=143) |
| 7.2 Normalising Flows in Practice: Coupling Layers and Composition | [147](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=147) |
| 7.2.1 Affine Coupling Layers and Triangular Jacobians | [147](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=147) |
| 7.2.2 Stacking Flows: Likelihood Evaluation and Sampling | [150](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=150) |
| 7.3 Autoregressive Factorisation as a Generative Model | [152](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=152) |
| 7.3.1 The Chain Rule as an Exact Density Model | [153](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=153) |
| 7.3.2 Conditional Parameterisation and Generation | [154](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=154) |
| 7.3.3 Parallel Training, Sequential Sampling, and Masking | [156](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=156) |
| Summary and References (chapter 7) | [157](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=157) |
| 8 Beyond Likelihoods: Generative Adversarial Networks and Energy-Based Models | [159](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=159) |
| 8.1 Generative Adversarial Networks: Learning by Comparison | [161](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=161) |
| 8.1.1 The Generator as an Implicit Sampling Mechanism | [161](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=161) |
| 8.1.2 The Discriminator and the Adversarial Game | [162](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=162) |
| 8.1.3 The Optimal Discriminator | [163](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=163) |
| 8.1.4 From the Optimal Discriminator to Jensen–Shannon Divergence | [165](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=165) |
| 8.2 Geometric Optimisation and Wasserstein GANs | [166](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=166) |
| 8.2.1 Generator Optimisation and the Non-Saturating Loss | [167](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=167) |
| 8.2.2 From Overlap to Wasserstein Geometry | [168](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=168) |
| 8.2.3 The Wasserstein GAN Objective | [170](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=170) |
| 8.2.4 Enforcing the Lipschitz Constraint | [171](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=171) |
| 8.3 Energy-Based Models: Foundations and Learning | [172](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=172) |
| 8.3.1 Energy as a Modelling Primitive | [173](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=173) |
| 8.3.2 From Energies to Unnormalised Distributions | [173](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=173) |
| 8.3.3 Learning Energy Landscapes | [175](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=175) |
| 8.3.4 Maximum Likelihood and the Contrastive Gradient | [175](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=175) |
| 8.4 Energy Gradients, Score Fields, and Diffusion | [177](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=177) |
| 8.4.1 Sampling as Energy-Guided Dynamics | [178](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=178) |
| 8.4.2 Energy Gradients and Scores | [178](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=178) |
| 8.4.3 Score Matching as Energy-Gradient Learning | [179](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=179) |
| 8.4.4 Diffusion as Multi-Scale Energy-Gradient Learning | [180](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=180) |
| Summary and References (chapter 8) | [182](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=182) |
| Closing Remarks | [183](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=183) |
| Appendix A: Gaussian Algebra and Completing the Square | [185](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=185) |
| Appendix B: Diffusion Reverse-Posterior Derivations | [189](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=189) |
| References | [193](machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=193) |

## computer-vision/

### Computer vision textbook

`computer-vision/computer-vision-textbook.pdf`, 667 pages. Simon J. D. Prince, *Computer Vision: Models,
Learning, and Inference*, Cambridge University Press, 2012; this file is the author's draft of 7 July
2012. A published textbook that treats vision as probabilistic modelling: probability and the normal
distribution, learning and inference, regression and classification, graphical models, image
preprocessing, camera geometry, and models for shape, identity, tracking and visual words. Was
`Computer Vision.pdf`. The table is from the PDF's own outline for the parts and chapters, with each
section's page from the printed contents. The printed page number is the PDF page minus 2.

| Chapter or section | PDF page |
| --- | --- |
| 1 Introduction | [17](computer-vision/computer-vision-textbook.pdf#page=17) |
| Part I: Probability | [23](computer-vision/computer-vision-textbook.pdf#page=23) |
| 2 Introduction to probability | [27](computer-vision/computer-vision-textbook.pdf#page=27) |
| 2.1 Random variables | [27](computer-vision/computer-vision-textbook.pdf#page=27) |
| 2.2 Joint probability | [28](computer-vision/computer-vision-textbook.pdf#page=28) |
| 2.3 Marginalization | [29](computer-vision/computer-vision-textbook.pdf#page=29) |
| 2.4 Conditional probability | [30](computer-vision/computer-vision-textbook.pdf#page=30) |
| 2.5 Bayes’ rule | [32](computer-vision/computer-vision-textbook.pdf#page=32) |
| 2.6 Independence | [33](computer-vision/computer-vision-textbook.pdf#page=33) |
| 2.7 Expectation | [33](computer-vision/computer-vision-textbook.pdf#page=33) |
| 3 Common probability distributions | [37](computer-vision/computer-vision-textbook.pdf#page=37) |
| 3.1 Bernoulli distribution | [38](computer-vision/computer-vision-textbook.pdf#page=38) |
| 3.2 Beta distribution | [39](computer-vision/computer-vision-textbook.pdf#page=39) |
| 3.3 Categorical distribution | [40](computer-vision/computer-vision-textbook.pdf#page=40) |
| 3.4 Dirichlet distribution | [41](computer-vision/computer-vision-textbook.pdf#page=41) |
| 3.5 Univariate normal distribution | [42](computer-vision/computer-vision-textbook.pdf#page=42) |
| 3.6 Normal-scaled inverse gamma distribution | [42](computer-vision/computer-vision-textbook.pdf#page=42) |
| 3.7 Multivariate normal distribution | [43](computer-vision/computer-vision-textbook.pdf#page=43) |
| 3.8 Normal inverse Wishart distribution | [44](computer-vision/computer-vision-textbook.pdf#page=44) |
| 3.9 Conjugacy | [44](computer-vision/computer-vision-textbook.pdf#page=44) |
| 4 Fitting probability models | [51](computer-vision/computer-vision-textbook.pdf#page=51) |
| 4.1 Maximum likelihood | [51](computer-vision/computer-vision-textbook.pdf#page=51) |
| 4.2 Maximum a posteriori | [52](computer-vision/computer-vision-textbook.pdf#page=52) |
| 4.3 The Bayesian approach | [52](computer-vision/computer-vision-textbook.pdf#page=52) |
| 4.4 Worked example 1: univariate normal | [53](computer-vision/computer-vision-textbook.pdf#page=53) |
| 4.5 Worked example 2: categorical distribution | [62](computer-vision/computer-vision-textbook.pdf#page=62) |
| 5 The normal distribution | [71](computer-vision/computer-vision-textbook.pdf#page=71) |
| 5.1 Types of covariance matrix | [71](computer-vision/computer-vision-textbook.pdf#page=71) |
| 5.2 Decomposition of covariance | [73](computer-vision/computer-vision-textbook.pdf#page=73) |
| 5.3 Linear transformations of variables | [74](computer-vision/computer-vision-textbook.pdf#page=74) |
| 5.4 Marginal distributions | [74](computer-vision/computer-vision-textbook.pdf#page=74) |
| 5.5 Conditional distributions | [75](computer-vision/computer-vision-textbook.pdf#page=75) |
| 5.6 Product of two normals | [76](computer-vision/computer-vision-textbook.pdf#page=76) |
| 5.7 Change of variable | [77](computer-vision/computer-vision-textbook.pdf#page=77) |
| Part II: Machine learning for machine vision | [81](computer-vision/computer-vision-textbook.pdf#page=81) |
| 6 Learning and inference in vision | [85](computer-vision/computer-vision-textbook.pdf#page=85) |
| 6.1 Computer vision problems | [85](computer-vision/computer-vision-textbook.pdf#page=85) |
| 6.2 Types of model | [86](computer-vision/computer-vision-textbook.pdf#page=86) |
| 6.3 Example 1: regression | [87](computer-vision/computer-vision-textbook.pdf#page=87) |
| 6.4 Example 2: binary classification | [90](computer-vision/computer-vision-textbook.pdf#page=90) |
| 6.5 Which type of model should we use? | [93](computer-vision/computer-vision-textbook.pdf#page=93) |
| 6.6 Applications | [95](computer-vision/computer-vision-textbook.pdf#page=95) |
| 7 Modeling complex data densities | [103](computer-vision/computer-vision-textbook.pdf#page=103) |
| 7.1 Normal classification model | [103](computer-vision/computer-vision-textbook.pdf#page=103) |
| 7.2 Hidden variables | [107](computer-vision/computer-vision-textbook.pdf#page=107) |
| 7.3 Expectation maximization | [108](computer-vision/computer-vision-textbook.pdf#page=108) |
| 7.4 Mixture of Gaussians | [110](computer-vision/computer-vision-textbook.pdf#page=110) |
| 7.5 The t-distribution | [117](computer-vision/computer-vision-textbook.pdf#page=117) |
| 7.6 Factor analysis | [122](computer-vision/computer-vision-textbook.pdf#page=122) |
| 7.7 Combining models | [128](computer-vision/computer-vision-textbook.pdf#page=128) |
| 7.8 Expectation maximization in detail | [129](computer-vision/computer-vision-textbook.pdf#page=129) |
| 7.9 Applications | [134](computer-vision/computer-vision-textbook.pdf#page=134) |
| 8 Regression models | [145](computer-vision/computer-vision-textbook.pdf#page=145) |
| 8.1 Linear regression | [145](computer-vision/computer-vision-textbook.pdf#page=145) |
| 8.2 Bayesian linear regression | [149](computer-vision/computer-vision-textbook.pdf#page=149) |
| 8.3 Non-linear regression | [152](computer-vision/computer-vision-textbook.pdf#page=152) |
| 8.4 Kernels and the kernel trick | [157](computer-vision/computer-vision-textbook.pdf#page=157) |
| 8.5 Gaussian process regression | [158](computer-vision/computer-vision-textbook.pdf#page=158) |
| 8.6 Sparse linear regression | [159](computer-vision/computer-vision-textbook.pdf#page=159) |
| 8.7 Dual linear regression | [163](computer-vision/computer-vision-textbook.pdf#page=163) |
| 8.8 Relevance vector regression | [165](computer-vision/computer-vision-textbook.pdf#page=165) |
| 8.9 Regression to multivariate data | [167](computer-vision/computer-vision-textbook.pdf#page=167) |
| 8.10 Applications | [167](computer-vision/computer-vision-textbook.pdf#page=167) |
| 9 Classification models | [173](computer-vision/computer-vision-textbook.pdf#page=173) |
| 9.1 Logistic regression | [173](computer-vision/computer-vision-textbook.pdf#page=173) |
| 9.2 Bayesian logistic regression | [178](computer-vision/computer-vision-textbook.pdf#page=178) |
| 9.3 Non-linear logistic regression | [183](computer-vision/computer-vision-textbook.pdf#page=183) |
| 9.4 Dual logistic regression | [185](computer-vision/computer-vision-textbook.pdf#page=185) |
| 9.5 Kernel logistic regression | [187](computer-vision/computer-vision-textbook.pdf#page=187) |
| 9.6 Relevance vector classification | [188](computer-vision/computer-vision-textbook.pdf#page=188) |
| 9.7 Incremental fitting and boosting | [192](computer-vision/computer-vision-textbook.pdf#page=192) |
| 9.8 Classification trees | [196](computer-vision/computer-vision-textbook.pdf#page=196) |
| 9.9 Multi-class logistic regression | [199](computer-vision/computer-vision-textbook.pdf#page=199) |
| 9.10 Random trees, forests, and ferns | [200](computer-vision/computer-vision-textbook.pdf#page=200) |
| 9.11 Relation to non-probabilistic models | [202](computer-vision/computer-vision-textbook.pdf#page=202) |
| 9.12 Applications | [203](computer-vision/computer-vision-textbook.pdf#page=203) |
| Part III: Connecting local models | [215](computer-vision/computer-vision-textbook.pdf#page=215) |
| 10 Graphical models | [219](computer-vision/computer-vision-textbook.pdf#page=219) |
| 10.1 Conditional independence | [219](computer-vision/computer-vision-textbook.pdf#page=219) |
| 10.2 Directed graphical models | [221](computer-vision/computer-vision-textbook.pdf#page=221) |
| 10.3 Undirected graphical models | [225](computer-vision/computer-vision-textbook.pdf#page=225) |
| 10.4 Comparing directed and undirected graphical models | [227](computer-vision/computer-vision-textbook.pdf#page=227) |
| 10.5 Graphical models in computer vision | [229](computer-vision/computer-vision-textbook.pdf#page=229) |
| 10.6 Inference in models with many unknowns | [231](computer-vision/computer-vision-textbook.pdf#page=231) |
| 10.7 Drawing samples | [233](computer-vision/computer-vision-textbook.pdf#page=233) |
| 10.8 Learning | [235](computer-vision/computer-vision-textbook.pdf#page=235) |
| 11 Models for chains and trees | [245](computer-vision/computer-vision-textbook.pdf#page=245) |
| 11.1 Models for chains | [246](computer-vision/computer-vision-textbook.pdf#page=246) |
| 11.2 MAP inference for chains | [248](computer-vision/computer-vision-textbook.pdf#page=248) |
| 11.3 MAP inference for trees | [253](computer-vision/computer-vision-textbook.pdf#page=253) |
| 11.4 Marginal posterior inference for chains | [256](computer-vision/computer-vision-textbook.pdf#page=256) |
| 11.5 Marginal posterior inference for trees | [264](computer-vision/computer-vision-textbook.pdf#page=264) |
| 11.6 Learning in chains and trees | [264](computer-vision/computer-vision-textbook.pdf#page=264) |
| 11.7 Beyond chains and trees | [265](computer-vision/computer-vision-textbook.pdf#page=265) |
| 11.8 Applications | [268](computer-vision/computer-vision-textbook.pdf#page=268) |
| 12 Models for grids | [281](computer-vision/computer-vision-textbook.pdf#page=281) |
| 12.1 Markov random fields | [282](computer-vision/computer-vision-textbook.pdf#page=282) |
| 12.2 MAP inference for binary pairwise MRFs | [286](computer-vision/computer-vision-textbook.pdf#page=286) |
| 12.3 MAP inference for multi-label pairwise MRFs | [295](computer-vision/computer-vision-textbook.pdf#page=295) |
| 12.4 Multi-label MRFs with non-convex potentials | [298](computer-vision/computer-vision-textbook.pdf#page=298) |
| 12.5 Conditional random fields | [302](computer-vision/computer-vision-textbook.pdf#page=302) |
| 12.6 Higher order models | [305](computer-vision/computer-vision-textbook.pdf#page=305) |
| 12.7 Directed models for grids | [306](computer-vision/computer-vision-textbook.pdf#page=306) |
| 12.8 Applications | [306](computer-vision/computer-vision-textbook.pdf#page=306) |
| Part IV: Preprocessing | [323](computer-vision/computer-vision-textbook.pdf#page=323) |
| 13 Image preprocessing and feature extraction | [327](computer-vision/computer-vision-textbook.pdf#page=327) |
| 13.1 Per-pixel transformations | [327](computer-vision/computer-vision-textbook.pdf#page=327) |
| 13.2 Edges, corners, and interest points | [338](computer-vision/computer-vision-textbook.pdf#page=338) |
| 13.3 Descriptors | [343](computer-vision/computer-vision-textbook.pdf#page=343) |
| 13.4 Dimensionality reduction | [347](computer-vision/computer-vision-textbook.pdf#page=347) |
| Part V: Models for geometry | [357](computer-vision/computer-vision-textbook.pdf#page=357) |
| 14 The pinhole camera | [361](computer-vision/computer-vision-textbook.pdf#page=361) |
| 14.1 The pinhole camera | [361](computer-vision/computer-vision-textbook.pdf#page=361) |
| 14.2 Three geometric problems | [369](computer-vision/computer-vision-textbook.pdf#page=369) |
| 14.3 Homogeneous coordinates | [373](computer-vision/computer-vision-textbook.pdf#page=373) |
| 14.4 Learning extrinsic parameters | [375](computer-vision/computer-vision-textbook.pdf#page=375) |
| 14.5 Learning intrinsic parameters | [377](computer-vision/computer-vision-textbook.pdf#page=377) |
| 14.6 Inferring 3D world points | [378](computer-vision/computer-vision-textbook.pdf#page=378) |
| 14.7 Applications | [380](computer-vision/computer-vision-textbook.pdf#page=380) |
| 15 Models for transformations | [391](computer-vision/computer-vision-textbook.pdf#page=391) |
| 15.1 2D transformation models | [391](computer-vision/computer-vision-textbook.pdf#page=391) |
| 15.2 Learning in transformation models | [398](computer-vision/computer-vision-textbook.pdf#page=398) |
| 15.3 Inference in transformation models | [403](computer-vision/computer-vision-textbook.pdf#page=403) |
| 15.4 Three geometric problems for planes | [404](computer-vision/computer-vision-textbook.pdf#page=404) |
| 15.5 Transformations between images | [409](computer-vision/computer-vision-textbook.pdf#page=409) |
| 15.6 Robust learning of transformations | [412](computer-vision/computer-vision-textbook.pdf#page=412) |
| 15.7 Applications | [417](computer-vision/computer-vision-textbook.pdf#page=417) |
| 16 Multiple cameras | [425](computer-vision/computer-vision-textbook.pdf#page=425) |
| 16.1 Two-view geometry | [426](computer-vision/computer-vision-textbook.pdf#page=426) |
| 16.2 The essential matrix | [429](computer-vision/computer-vision-textbook.pdf#page=429) |
| 16.3 The fundamental matrix | [434](computer-vision/computer-vision-textbook.pdf#page=434) |
| 16.4 Two-view reconstruction pipeline | [437](computer-vision/computer-vision-textbook.pdf#page=437) |
| 16.5 Rectification | [441](computer-vision/computer-vision-textbook.pdf#page=441) |
| 16.6 Multi-view reconstruction | [445](computer-vision/computer-vision-textbook.pdf#page=445) |
| 16.7 Applications | [449](computer-vision/computer-vision-textbook.pdf#page=449) |
| Part VI: Models for vision | [459](computer-vision/computer-vision-textbook.pdf#page=459) |
| 17 Models for shape | [463](computer-vision/computer-vision-textbook.pdf#page=463) |
| 17.1 Shape and its representation | [464](computer-vision/computer-vision-textbook.pdf#page=464) |
| 17.2 Snakes | [465](computer-vision/computer-vision-textbook.pdf#page=465) |
| 17.3 Shape templates | [470](computer-vision/computer-vision-textbook.pdf#page=470) |
| 17.4 Statistical shape models | [473](computer-vision/computer-vision-textbook.pdf#page=473) |
| 17.5 Subspace shape models | [477](computer-vision/computer-vision-textbook.pdf#page=477) |
| 17.6 Three-dimensional shape models | [484](computer-vision/computer-vision-textbook.pdf#page=484) |
| 17.7 Statistical models for shape and appearance | [484](computer-vision/computer-vision-textbook.pdf#page=484) |
| 17.8 Non-Gaussian statistical shape models | [489](computer-vision/computer-vision-textbook.pdf#page=489) |
| 17.9 Articulated models | [494](computer-vision/computer-vision-textbook.pdf#page=494) |
| 17.10 Applications | [495](computer-vision/computer-vision-textbook.pdf#page=495) |
| 18 Models for style and identity | [505](computer-vision/computer-vision-textbook.pdf#page=505) |
| 18.1 Subspace identity model | [508](computer-vision/computer-vision-textbook.pdf#page=508) |
| 18.2 Probabilistic linear discriminant analysis | [516](computer-vision/computer-vision-textbook.pdf#page=516) |
| 18.3 Non-linear identity models | [519](computer-vision/computer-vision-textbook.pdf#page=519) |
| 18.4 Asymmetric bilinear models | [520](computer-vision/computer-vision-textbook.pdf#page=520) |
| 18.5 Symmetric bilinear and multilinear models | [526](computer-vision/computer-vision-textbook.pdf#page=526) |
| 18.6 Applications | [530](computer-vision/computer-vision-textbook.pdf#page=530) |
| 19 Temporal models | [539](computer-vision/computer-vision-textbook.pdf#page=539) |
| 19.1 Temporal estimation framework | [539](computer-vision/computer-vision-textbook.pdf#page=539) |
| 19.2 Kalman filter | [542](computer-vision/computer-vision-textbook.pdf#page=542) |
| 19.3 Extended Kalman filter | [552](computer-vision/computer-vision-textbook.pdf#page=552) |
| 19.4 Unscented Kalman filter | [556](computer-vision/computer-vision-textbook.pdf#page=556) |
| 19.5 Particle filtering | [560](computer-vision/computer-vision-textbook.pdf#page=560) |
| 19.6 Applications | [565](computer-vision/computer-vision-textbook.pdf#page=565) |
| 20 Models for visual words | [573](computer-vision/computer-vision-textbook.pdf#page=573) |
| 20.1 Images as collections of visual words | [573](computer-vision/computer-vision-textbook.pdf#page=573) |
| 20.2 Bag of words | [575](computer-vision/computer-vision-textbook.pdf#page=575) |
| 20.3 Latent Dirichlet allocation | [578](computer-vision/computer-vision-textbook.pdf#page=578) |
| 20.4 Single author-topic model | [584](computer-vision/computer-vision-textbook.pdf#page=584) |
| 20.5 Constellation models | [587](computer-vision/computer-vision-textbook.pdf#page=587) |
| 20.6 Scene models | [592](computer-vision/computer-vision-textbook.pdf#page=592) |
| 20.7 Applications | [592](computer-vision/computer-vision-textbook.pdf#page=592) |
| Part VII: Appendices | [599](computer-vision/computer-vision-textbook.pdf#page=599) |
| Appendix A Notation | [601](computer-vision/computer-vision-textbook.pdf#page=601) |
| Appendix B Optimization | [603](computer-vision/computer-vision-textbook.pdf#page=603) |
| Appendix C Linear algebra | [615](computer-vision/computer-vision-textbook.pdf#page=615) |

## optimization/

### Optimization: principles and algorithms

`optimization/optimization-principles-and-algorithms.pdf`, 738 pages. Michel Bierlaire, *Optimization:
Principles and Algorithms*, EPFL Press, second edition, 2018. A published textbook that starts from
writing a problem down (objective function, constraints, minima), works through gradients, Hessians,
convexity and optimality conditions, then teaches the algorithms that solve them: Newton's method,
quasi-Newton, conjugate gradient, steepest descent with line search, trust regions, BFGS, Gauss-Newton,
simplex, interior points, SQP, network flows and discrete optimization. Was
`OptimizationPrinciplesAlgorithms2018.pdf`. The table is from the PDF's own outline, parts, chapters and
their first-level sections. The printed page number is the PDF page minus 18 from chapter 1 on.

**Why it is on the shelf: it teaches how to read pseudocode.** Every algorithm is a numbered block with
the same parts (`Objective`, `Input`, `Output`, `Initialization`, `Repeat … Until`), placed after the
definition it implements and followed by worked examples that run it iteration by iteration with real
numbers. Newton's method for one variable is the clearest instance: the linear model it is built on is
Definition 7.2 ([201](optimization/optimization-principles-and-algorithms.pdf#page=201)), the block is Algorithm 7.2 ([203](optimization/optimization-principles-and-algorithms.pdf#page=203)), and Examples 7.3, 7.4 and 7.5 ([203](optimization/optimization-principles-and-algorithms.pdf#page=203), [204](optimization/optimization-principles-and-algorithms.pdf#page=204),
[206](optimization/optimization-principles-and-algorithms.pdf#page=206)) run it from fixed starting points, the last one diverging. The same pairing holds for conjugate
gradient (Algorithm 9.2 and Example 9.8, both [248](optimization/optimization-principles-and-algorithms.pdf#page=248)) and for line search (Examples 11.3 and 11.4 at [273](optimization/optimization-principles-and-algorithms.pdf#page=273)
and [278](optimization/optimization-principles-and-algorithms.pdf#page=278) run Algorithms 11.3 and 11.4). The definitions used most by generative-model papers are early:
gradient [50](optimization/optimization-principles-and-algorithms.pdf#page=50), directional derivative and descent direction [51](optimization/optimization-principles-and-algorithms.pdf#page=51), Hessian [57](optimization/optimization-principles-and-algorithms.pdf#page=57), convex function [48](optimization/optimization-principles-and-algorithms.pdf#page=48),
conditioning [63](optimization/optimization-principles-and-algorithms.pdf#page=63), and the necessary optimality conditions [133](optimization/optimization-principles-and-algorithms.pdf#page=133).

| Chapter or section | PDF page |
| --- | --- |
| I Formulation and analysis of the problem | [19](optimization/optimization-principles-and-algorithms.pdf#page=19) |
| 1 Formulation | [23](optimization/optimization-principles-and-algorithms.pdf#page=23) |
| 1.1 Modeling | [23](optimization/optimization-principles-and-algorithms.pdf#page=23) |
| 1.2 Problem transformations | [34](optimization/optimization-principles-and-algorithms.pdf#page=34) |
| 1.3 Hypotheses | [38](optimization/optimization-principles-and-algorithms.pdf#page=38) |
| 1.4 Problem definition | [39](optimization/optimization-principles-and-algorithms.pdf#page=39) |
| 1.5 Exercises | [44](optimization/optimization-principles-and-algorithms.pdf#page=44) |
| 2 Objective function | [47](optimization/optimization-principles-and-algorithms.pdf#page=47) |
| 2.1 Convexity and concavity | [47](optimization/optimization-principles-and-algorithms.pdf#page=47) |
| 2.2 Differentiability: the first order | [49](optimization/optimization-principles-and-algorithms.pdf#page=49) |
| 2.3 Differentiability: the second order | [57](optimization/optimization-principles-and-algorithms.pdf#page=57) |
| 2.4 Linearity and non linearity | [60](optimization/optimization-principles-and-algorithms.pdf#page=60) |
| 2.5 Conditioning and preconditioning | [63](optimization/optimization-principles-and-algorithms.pdf#page=63) |
| 2.6 Exercises | [68](optimization/optimization-principles-and-algorithms.pdf#page=68) |
| 3 Constraints | [69](optimization/optimization-principles-and-algorithms.pdf#page=69) |
| 3.1 Active constraints | [70](optimization/optimization-principles-and-algorithms.pdf#page=70) |
| 3.2 Linear independence of the constraints | [74](optimization/optimization-principles-and-algorithms.pdf#page=74) |
| 3.3 Feasible directions | [78](optimization/optimization-principles-and-algorithms.pdf#page=78) |
| 3.4 Elimination of constraints | [93](optimization/optimization-principles-and-algorithms.pdf#page=93) |
| 3.5 Linear constraints | [96](optimization/optimization-principles-and-algorithms.pdf#page=96) |
| 3.6 Exercises | [109](optimization/optimization-principles-and-algorithms.pdf#page=109) |
| 4 Introduction to duality | [111](optimization/optimization-principles-and-algorithms.pdf#page=111) |
| 4.1 Constraint relaxation | [111](optimization/optimization-principles-and-algorithms.pdf#page=111) |
| 4.2 Duality in linear optimization | [120](optimization/optimization-principles-and-algorithms.pdf#page=120) |
| 4.3 Exercises | [126](optimization/optimization-principles-and-algorithms.pdf#page=126) |
| II Optimality conditions | [129](optimization/optimization-principles-and-algorithms.pdf#page=129) |
| 5 Unconstrained optimization | [133](optimization/optimization-principles-and-algorithms.pdf#page=133) |
| 5.1 Necessary optimality conditions | [133](optimization/optimization-principles-and-algorithms.pdf#page=133) |
| 5.2 Sufficient optimality conditions | [138](optimization/optimization-principles-and-algorithms.pdf#page=138) |
| 5.3 Exercises | [143](optimization/optimization-principles-and-algorithms.pdf#page=143) |
| 6 Constrained optimization | [145](optimization/optimization-principles-and-algorithms.pdf#page=145) |
| 6.1 Convex constraints | [146](optimization/optimization-principles-and-algorithms.pdf#page=146) |
| 6.2 Lagrange multipliers: necessary conditions | [151](optimization/optimization-principles-and-algorithms.pdf#page=151) |
| 6.3 Lagrange multipliers: sufficient conditions | [170](optimization/optimization-principles-and-algorithms.pdf#page=170) |
| 6.4 Sensitivity analysis | [177](optimization/optimization-principles-and-algorithms.pdf#page=177) |
| 6.5 Linear optimization | [183](optimization/optimization-principles-and-algorithms.pdf#page=183) |
| 6.6 Quadratic optimization | [189](optimization/optimization-principles-and-algorithms.pdf#page=189) |
| 6.7 Exercises | [192](optimization/optimization-principles-and-algorithms.pdf#page=192) |
| III Solving equations | [195](optimization/optimization-principles-and-algorithms.pdf#page=195) |
| 7 Newton's method | [199](optimization/optimization-principles-and-algorithms.pdf#page=199) |
| 7.1 Equation with one unknown | [199](optimization/optimization-principles-and-algorithms.pdf#page=199) |
| 7.2 Systems of equations with multiple unknowns | [210](optimization/optimization-principles-and-algorithms.pdf#page=210) |
| 7.3 Project | [216](optimization/optimization-principles-and-algorithms.pdf#page=216) |
| 8 Quasi-Newton methods | [219](optimization/optimization-principles-and-algorithms.pdf#page=219) |
| 8.1 Equation with one unknown | [219](optimization/optimization-principles-and-algorithms.pdf#page=219) |
| 8.2 Systems of equations with multiple unknowns | [226](optimization/optimization-principles-and-algorithms.pdf#page=226) |
| 8.3 Project | [234](optimization/optimization-principles-and-algorithms.pdf#page=234) |
| IV Unconstrained optimization | [235](optimization/optimization-principles-and-algorithms.pdf#page=235) |
| 9 Quadratic problems | [239](optimization/optimization-principles-and-algorithms.pdf#page=239) |
| 9.1 Direct solution | [239](optimization/optimization-principles-and-algorithms.pdf#page=239) |
| 9.2 Conjugate gradient method | [240](optimization/optimization-principles-and-algorithms.pdf#page=240) |
| 9.3 Project | [250](optimization/optimization-principles-and-algorithms.pdf#page=250) |
| 10 Newton's local method | [253](optimization/optimization-principles-and-algorithms.pdf#page=253) |
| 10.1 Solving the necessary optimality conditions | [253](optimization/optimization-principles-and-algorithms.pdf#page=253) |
| 10.2 Geometric interpretation | [254](optimization/optimization-principles-and-algorithms.pdf#page=254) |
| 10.3 Exercises | [262](optimization/optimization-principles-and-algorithms.pdf#page=262) |
| 11 Descent methods and line search | [263](optimization/optimization-principles-and-algorithms.pdf#page=263) |
| 11.1 Preconditioned steepest descent | [264](optimization/optimization-principles-and-algorithms.pdf#page=264) |
| 11.2 Exact line search | [269](optimization/optimization-principles-and-algorithms.pdf#page=269) |
| 11.3 Inexact line search | [281](optimization/optimization-principles-and-algorithms.pdf#page=281) |
| 11.4 Steepest descent method | [295](optimization/optimization-principles-and-algorithms.pdf#page=295) |
| 11.5 Newton method with line search | [295](optimization/optimization-principles-and-algorithms.pdf#page=295) |
| 11.6 The Rosenbrock problem | [299](optimization/optimization-principles-and-algorithms.pdf#page=299) |
| 11.7 Convergence | [302](optimization/optimization-principles-and-algorithms.pdf#page=302) |
| 11.8 Project | [306](optimization/optimization-principles-and-algorithms.pdf#page=306) |
| 12 Trust region | [309](optimization/optimization-principles-and-algorithms.pdf#page=309) |
| 12.1 Solving the trust region subproblem | [312](optimization/optimization-principles-and-algorithms.pdf#page=312) |
| 12.2 Calculation of the radius of the trust region | [318](optimization/optimization-principles-and-algorithms.pdf#page=318) |
| 12.3 The Rosenbrock problem | [326](optimization/optimization-principles-and-algorithms.pdf#page=326) |
| 12.4 Project | [327](optimization/optimization-principles-and-algorithms.pdf#page=327) |
| 13 Quasi-Newton methods | [329](optimization/optimization-principles-and-algorithms.pdf#page=329) |
| 13.1 BFGS | [329](optimization/optimization-principles-and-algorithms.pdf#page=329) |
| 13.2 Symmetric update of rank 1 (SR1) | [335](optimization/optimization-principles-and-algorithms.pdf#page=335) |
| 13.3 The Rosenbrock problem | [338](optimization/optimization-principles-and-algorithms.pdf#page=338) |
| 13.4 Comments | [338](optimization/optimization-principles-and-algorithms.pdf#page=338) |
| 13.5 Project | [344](optimization/optimization-principles-and-algorithms.pdf#page=344) |
| 14 Least squares problem | [347](optimization/optimization-principles-and-algorithms.pdf#page=347) |
| 14.1 The Gauss-Newton method | [352](optimization/optimization-principles-and-algorithms.pdf#page=352) |
| 14.2 Kalman filter | [355](optimization/optimization-principles-and-algorithms.pdf#page=355) |
| 14.3 Orthogonal regression | [359](optimization/optimization-principles-and-algorithms.pdf#page=359) |
| 14.4 Project | [361](optimization/optimization-principles-and-algorithms.pdf#page=361) |
| 15 Direct search methods | [365](optimization/optimization-principles-and-algorithms.pdf#page=365) |
| 15.1 Nelder-Mead | [366](optimization/optimization-principles-and-algorithms.pdf#page=366) |
| 15.2 Torczon's multi-directional search | [372](optimization/optimization-principles-and-algorithms.pdf#page=372) |
| 15.3 Project | [375](optimization/optimization-principles-and-algorithms.pdf#page=375) |
| V Constrained optimization | [377](optimization/optimization-principles-and-algorithms.pdf#page=377) |
| 16 The simplex method | [381](optimization/optimization-principles-and-algorithms.pdf#page=381) |
| 16.1 The simplex algorithm | [381](optimization/optimization-principles-and-algorithms.pdf#page=381) |
| 16.2 The simplex tableau | [394](optimization/optimization-principles-and-algorithms.pdf#page=394) |
| 16.3 The initial tableau | [403](optimization/optimization-principles-and-algorithms.pdf#page=403) |
| 16.4 The revised simplex algorithm | [412](optimization/optimization-principles-and-algorithms.pdf#page=412) |
| 16.5 Exercises | [413](optimization/optimization-principles-and-algorithms.pdf#page=413) |
| 16.6 Project | [414](optimization/optimization-principles-and-algorithms.pdf#page=414) |
| 17 Newton's method for constrained optimization | [417](optimization/optimization-principles-and-algorithms.pdf#page=417) |
| 17.1 Projected gradient method | [417](optimization/optimization-principles-and-algorithms.pdf#page=417) |
| 17.2 Preconditioned projected gradient | [423](optimization/optimization-principles-and-algorithms.pdf#page=423) |
| 17.3 Dikin's method | [425](optimization/optimization-principles-and-algorithms.pdf#page=425) |
| 17.4 Project | [430](optimization/optimization-principles-and-algorithms.pdf#page=430) |
| 18 Interior point methods | [433](optimization/optimization-principles-and-algorithms.pdf#page=433) |
| 18.1 Barrier methods | [433](optimization/optimization-principles-and-algorithms.pdf#page=433) |
| 18.2 Linear optimization | [440](optimization/optimization-principles-and-algorithms.pdf#page=440) |
| 18.3 Project | [461](optimization/optimization-principles-and-algorithms.pdf#page=461) |
| 19 Augmented Lagrangian method | [463](optimization/optimization-principles-and-algorithms.pdf#page=463) |
| 19.1 Lagrangian penalty | [465](optimization/optimization-principles-and-algorithms.pdf#page=465) |
| 19.2 Quadratic penalty | [467](optimization/optimization-principles-and-algorithms.pdf#page=467) |
| 19.3 Double penalty | [468](optimization/optimization-principles-and-algorithms.pdf#page=468) |
| 19.4 Project | [478](optimization/optimization-principles-and-algorithms.pdf#page=478) |
| 20 Sequential quadratic programming | [481](optimization/optimization-principles-and-algorithms.pdf#page=481) |
| 20.1 Local sequential quadratic programming | [482](optimization/optimization-principles-and-algorithms.pdf#page=482) |
| 20.2 Globally convergent algorithm | [489](optimization/optimization-principles-and-algorithms.pdf#page=489) |
| 20.3 Project | [502](optimization/optimization-principles-and-algorithms.pdf#page=502) |
| VI Networks | [505](optimization/optimization-principles-and-algorithms.pdf#page=505) |
| 21 Introduction and definitions | [509](optimization/optimization-principles-and-algorithms.pdf#page=509) |
| 21.1 Graphs | [510](optimization/optimization-principles-and-algorithms.pdf#page=510) |
| 21.2 Cuts | [512](optimization/optimization-principles-and-algorithms.pdf#page=512) |
| 21.3 Paths | [513](optimization/optimization-principles-and-algorithms.pdf#page=513) |
| 21.4 Trees | [516](optimization/optimization-principles-and-algorithms.pdf#page=516) |
| 21.5 Networks | [519](optimization/optimization-principles-and-algorithms.pdf#page=519) |
| 21.6 Flow decomposition | [528](optimization/optimization-principles-and-algorithms.pdf#page=528) |
| 21.7 Minimum spanning trees | [538](optimization/optimization-principles-and-algorithms.pdf#page=538) |
| 21.8 Exercises | [542](optimization/optimization-principles-and-algorithms.pdf#page=542) |
| 22 The transhipment problem | [547](optimization/optimization-principles-and-algorithms.pdf#page=547) |
| 22.1 Formulation | [547](optimization/optimization-principles-and-algorithms.pdf#page=547) |
| 22.2 Optimality conditions | [553](optimization/optimization-principles-and-algorithms.pdf#page=553) |
| 22.3 Total unimodularity | [554](optimization/optimization-principles-and-algorithms.pdf#page=554) |
| 22.4 Modeling | [557](optimization/optimization-principles-and-algorithms.pdf#page=557) |
| 22.5 Exercises | [567](optimization/optimization-principles-and-algorithms.pdf#page=567) |
| 23 Shortest path | [569](optimization/optimization-principles-and-algorithms.pdf#page=569) |
| 23.1 Properties | [570](optimization/optimization-principles-and-algorithms.pdf#page=570) |
| 23.2 The shortest path algorithm | [576](optimization/optimization-principles-and-algorithms.pdf#page=576) |
| 23.3 Dijkstra's algorithm | [584](optimization/optimization-principles-and-algorithms.pdf#page=584) |
| 23.4 The longest path problem | [589](optimization/optimization-principles-and-algorithms.pdf#page=589) |
| 23.5 Exercises | [592](optimization/optimization-principles-and-algorithms.pdf#page=592) |
| 24 Maximum flow | [595](optimization/optimization-principles-and-algorithms.pdf#page=595) |
| 24.1 The Ford-Fulkerson algorithm | [595](optimization/optimization-principles-and-algorithms.pdf#page=595) |
| 24.2 The minimum cut problem | [601](optimization/optimization-principles-and-algorithms.pdf#page=601) |
| 24.3 Exercises | [606](optimization/optimization-principles-and-algorithms.pdf#page=606) |
| VII Discrete optimization | [609](optimization/optimization-principles-and-algorithms.pdf#page=609) |
| 25 Introduction to discrete optimization | [613](optimization/optimization-principles-and-algorithms.pdf#page=613) |
| 25.1 Modeling | [613](optimization/optimization-principles-and-algorithms.pdf#page=613) |
| 25.2 Classical problems | [625](optimization/optimization-principles-and-algorithms.pdf#page=625) |
| 25.3 The curse of dimensionality | [632](optimization/optimization-principles-and-algorithms.pdf#page=632) |
| 25.4 Relaxation | [634](optimization/optimization-principles-and-algorithms.pdf#page=634) |
| 25.5 Exercises | [637](optimization/optimization-principles-and-algorithms.pdf#page=637) |
| 26 Exact methods for discrete optimization | [643](optimization/optimization-principles-and-algorithms.pdf#page=643) |
| 26.1 Branch and bound | [644](optimization/optimization-principles-and-algorithms.pdf#page=644) |
| 26.2 Cutting planes | [655](optimization/optimization-principles-and-algorithms.pdf#page=655) |
| 26.3 Exercises | [662](optimization/optimization-principles-and-algorithms.pdf#page=662) |
| 26.4 Project | [663](optimization/optimization-principles-and-algorithms.pdf#page=663) |
| 27 Heuristics | [665](optimization/optimization-principles-and-algorithms.pdf#page=665) |
| 27.1 Greedy heuristics | [666](optimization/optimization-principles-and-algorithms.pdf#page=666) |
| 27.2 Neighborhood and local search | [674](optimization/optimization-principles-and-algorithms.pdf#page=674) |
| 27.3 Variable neighborhood search | [687](optimization/optimization-principles-and-algorithms.pdf#page=687) |
| 27.4 Simulated annealing | [692](optimization/optimization-principles-and-algorithms.pdf#page=692) |
| 27.5 Conclusion | [700](optimization/optimization-principles-and-algorithms.pdf#page=700) |
| 27.6 Project | [700](optimization/optimization-principles-and-algorithms.pdf#page=700) |
| VIII Appendices | [703](optimization/optimization-principles-and-algorithms.pdf#page=703) |
| Notations | [705](optimization/optimization-principles-and-algorithms.pdf#page=705) |
| Definitions | [707](optimization/optimization-principles-and-algorithms.pdf#page=707) |
| Theorems | [713](optimization/optimization-principles-and-algorithms.pdf#page=713) |
| Projects | [717](optimization/optimization-principles-and-algorithms.pdf#page=717) |
| References | [720](optimization/optimization-principles-and-algorithms.pdf#page=720) |
| Bibliography | [721](optimization/optimization-principles-and-algorithms.pdf#page=721) |
| Index | [730](optimization/optimization-principles-and-algorithms.pdf#page=730) |

**Algorithms.** Each block starts on the page given; its worked examples follow within a few pages.

| Algorithm | PDF page |
| --- | --- |
| Algorithm 7.1 Machine epsilon | [202](optimization/optimization-principles-and-algorithms.pdf#page=202) |
| Algorithm 7.2 Newton’s method: one variable | [203](optimization/optimization-principles-and-algorithms.pdf#page=203) |
| Algorithm 7.3 Newton’s method: n variables | [212](optimization/optimization-principles-and-algorithms.pdf#page=212) |
| Algorithm 8.1 Finite difference Newton’s method: one variable | [221](optimization/optimization-principles-and-algorithms.pdf#page=221) |
| Algorithm 8.2 Secant method: one variable | [224](optimization/optimization-principles-and-algorithms.pdf#page=224) |
| Algorithm 8.3 Finite difference Newton’s method: n variables | [226](optimization/optimization-principles-and-algorithms.pdf#page=226) |
| Algorithm 8.4 Secant method: n variables | [232](optimization/optimization-principles-and-algorithms.pdf#page=232) |
| Algorithm 9.1 Quadratic problems: direct solution | [240](optimization/optimization-principles-and-algorithms.pdf#page=240) |
| Algorithm 9.2 Conjugate gradient method | [248](optimization/optimization-principles-and-algorithms.pdf#page=248) |
| Algorithm 10.1 Newton’s local method | [254](optimization/optimization-principles-and-algorithms.pdf#page=254) |
| Algorithm 10.2 Newton’s local method by quadratic modeling | [257](optimization/optimization-principles-and-algorithms.pdf#page=257) |
| Algorithm 11.1 Preconditioned steepest descent method | [269](optimization/optimization-principles-and-algorithms.pdf#page=269) |
| Algorithm 11.2 Initialization of the exact line search | [270](optimization/optimization-principles-and-algorithms.pdf#page=270) |
| Algorithm 11.3 Exact line search: quadratic interpolation | [272](optimization/optimization-principles-and-algorithms.pdf#page=272) |
| Algorithm 11.4 Exact line search: golden section | [278](optimization/optimization-principles-and-algorithms.pdf#page=278) |
| Algorithm 11.5 Line search | [292](optimization/optimization-principles-and-algorithms.pdf#page=292) |
| Algorithm 11.6 Steepest descent method | [295](optimization/optimization-principles-and-algorithms.pdf#page=295) |
| Algorithm 11.7 Modified Cholesky factorization | [296](optimization/optimization-principles-and-algorithms.pdf#page=296) |
| Algorithm 11.8 Newton algorithm with line search | [297](optimization/optimization-principles-and-algorithms.pdf#page=297) |
| Algorithm 12.1 Intersection with the trust region | [316](optimization/optimization-principles-and-algorithms.pdf#page=316) |
| Algorithm 12.2 Dogleg method | [317](optimization/optimization-principles-and-algorithms.pdf#page=317) |
| Algorithm 12.3 Steihaug-Toint truncated conjugate gradient method | [318](optimization/optimization-principles-and-algorithms.pdf#page=318) |
| Algorithm 12.4 Newton’s method with trust region | [320](optimization/optimization-principles-and-algorithms.pdf#page=320) |
| Algorithm 13.1 Quasi-Newton BFGS method | [334](optimization/optimization-principles-and-algorithms.pdf#page=334) |
| Algorithm 13.2 Quasi-Newton SR1 method | [337](optimization/optimization-principles-and-algorithms.pdf#page=337) |
| Algorithm 14.1 Gauss-Newton method | [353](optimization/optimization-principles-and-algorithms.pdf#page=353) |
| Algorithm 14.2 The Kalman filter method | [357](optimization/optimization-principles-and-algorithms.pdf#page=357) |
| Algorithm 14.3 The Kalman filter method in real time | [360](optimization/optimization-principles-and-algorithms.pdf#page=360) |
| Algorithm 15.1 Nelder-Mead | [367](optimization/optimization-principles-and-algorithms.pdf#page=367) |
| Algorithm 15.2 Torczon’s multi-directional method | [373](optimization/optimization-principles-and-algorithms.pdf#page=373) |
| Algorithm 16.1 Vertex enumeration | [386](optimization/optimization-principles-and-algorithms.pdf#page=386) |
| Algorithm 16.2 Simplex method | [389](optimization/optimization-principles-and-algorithms.pdf#page=389) |
| Algorithm 16.3 Tableau pivoting | [399](optimization/optimization-principles-and-algorithms.pdf#page=399) |
| Algorithm 16.4 Simplex algorithm | [401](optimization/optimization-principles-and-algorithms.pdf#page=401) |
| Algorithm 16.5 Simplex algorithm in two phases | [409](optimization/optimization-principles-and-algorithms.pdf#page=409) |
| Algorithm 17.1 Projected gradient method | [419](optimization/optimization-principles-and-algorithms.pdf#page=419) |
| Algorithm 17.2 Preconditioned projected gradient method | [425](optimization/optimization-principles-and-algorithms.pdf#page=425) |
| Algorithm 17.3 Dikin’s method | [427](optimization/optimization-principles-and-algorithms.pdf#page=427) |
| Algorithm 18.1 Generic interior points algorithm | [448](optimization/optimization-principles-and-algorithms.pdf#page=448) |
| Algorithm 18.2 Interior point algorithm with restricted steps | [454](optimization/optimization-principles-and-algorithms.pdf#page=454) |
| Algorithm 18.3 Predictor-corrector interior point algorithm | [455](optimization/optimization-principles-and-algorithms.pdf#page=455) |
| Algorithm 18.4 Long step interior point algorithm | [458](optimization/optimization-principles-and-algorithms.pdf#page=458) |
| Algorithm 19.1 Augmented Lagrangian algorithm | [472](optimization/optimization-principles-and-algorithms.pdf#page=472) |
| Algorithm 20.1 Local SQP algorithm | [484](optimization/optimization-principles-and-algorithms.pdf#page=484) |
| Algorithm 20.2 Globalized SQP algorithm | [498](optimization/optimization-principles-and-algorithms.pdf#page=498) |
| Algorithm 21.1 Generation of a simple cycle ﬂow from a circulation | [530](optimization/optimization-principles-and-algorithms.pdf#page=530) |
| Algorithm 21.2 Circulation decomposition | [534](optimization/optimization-principles-and-algorithms.pdf#page=534) |
| Algorithm 21.3 Flow decomposition | [535](optimization/optimization-principles-and-algorithms.pdf#page=535) |
| Algorithm 21.4 Jarnik-Prim algorithm for minimum spanning tree | [541](optimization/optimization-principles-and-algorithms.pdf#page=541) |
| Algorithm 23.1 The shortest path algorithm | [578](optimization/optimization-principles-and-algorithms.pdf#page=578) |
| Algorithm 23.2 Dijkstra’s algorithm | [587](optimization/optimization-principles-and-algorithms.pdf#page=587) |
| Algorithm 24.1 Generation of an unsaturated path | [598](optimization/optimization-principles-and-algorithms.pdf#page=598) |
| Algorithm 24.2 Ford-Fulkerson algorithm | [599](optimization/optimization-principles-and-algorithms.pdf#page=599) |
| Algorithm 26.1 Branch and bound | [647](optimization/optimization-principles-and-algorithms.pdf#page=647) |
| Algorithm 26.2 Branch and bound for integer optimization | [652](optimization/optimization-principles-and-algorithms.pdf#page=652) |
| Algorithm 26.3 Gomory cuts for integer linear optimization | [661](optimization/optimization-principles-and-algorithms.pdf#page=661) |
| Algorithm 27.1 Nearest neighbor greedy algorithm | [667](optimization/optimization-principles-and-algorithms.pdf#page=667) |
| Algorithm 27.2 Insertion greedy algorithm | [671](optimization/optimization-principles-and-algorithms.pdf#page=671) |
| Algorithm 27.3 Local search | [675](optimization/optimization-principles-and-algorithms.pdf#page=675) |
| Algorithm 27.4 Local search: a variant | [677](optimization/optimization-principles-and-algorithms.pdf#page=677) |
| Algorithm 27.5 Neighborhood of size k for the knapsack problem | [681](optimization/optimization-principles-and-algorithms.pdf#page=681) |
| Algorithm 27.6 Variable Neighborhood Search | [687](optimization/optimization-principles-and-algorithms.pdf#page=687) |
| Algorithm 27.7 Simulated annealing | [694](optimization/optimization-principles-and-algorithms.pdf#page=694) |

## natural-language-processing/

### Natural language processing with Python

`natural-language-processing/natural-language-processing-with-python.pdf`, 504 pages, downloaded as
`NLTK.pdf`. Steven Bird, Ewan Klein and
Edward Loper, *Natural Language Processing with Python*, O'Reilly Media, first edition, 2009. A
published textbook that teaches Python and natural language processing together through the NLTK
library (Python 2 syntax): texts as lists of words and their vocabulary as a set, corpora, raw text,
regular expressions and tokenization, writing structured programs (sequences, functions, recursion,
dynamic programming), tagging, classification, information extraction, grammars and parsing, meaning,
and managing linguistic data. The table is from the PDF's own outline, chapters and their sections.
The printed page number is the PDF page minus 22 from chapter 1 on.

**What it teaches that the maths books do not.** Splitting text into words with a regular expression
(section 3.7, [131](natural-language-processing/natural-language-processing-with-python.pdf#page=131)), a text's vocabulary as `set(text)` ([30](natural-language-processing/natural-language-processing-with-python.pdf#page=30)),
and dynamic programming worked bottom-up and top-down on one small problem (section 4.7,
[187](natural-language-processing/natural-language-processing-with-python.pdf#page=187) to [189](natural-language-processing/natural-language-processing-with-python.pdf#page=189)). It names string edit distance only in an
exercise (Chapter 4 exercise 25, [198](natural-language-processing/natural-language-processing-with-python.pdf#page=198)) and uses `nltk.edit_dist` to rank spelling
candidates ([446](natural-language-processing/natural-language-processing-with-python.pdf#page=446)); it never derives the edit table.

| Chapter or section | PDF page |
| --- | --- |
| Preface | [11](natural-language-processing/natural-language-processing-with-python.pdf#page=11) |
| 1 Language Processing and Python | [23](natural-language-processing/natural-language-processing-with-python.pdf#page=23) |
| 1.1 Computing with Language: Texts and Words | [23](natural-language-processing/natural-language-processing-with-python.pdf#page=23) |
| 1.2 A Closer Look at Python: Texts as Lists of Words | [32](natural-language-processing/natural-language-processing-with-python.pdf#page=32) |
| 1.3 Computing with Language: Simple Statistics | [38](natural-language-processing/natural-language-processing-with-python.pdf#page=38) |
| 1.4 Back to Python: Making Decisions and Taking Control | [44](natural-language-processing/natural-language-processing-with-python.pdf#page=44) |
| 1.5 Automatic Natural Language Understanding | [49](natural-language-processing/natural-language-processing-with-python.pdf#page=49) |
| 1.6 Summary | [55](natural-language-processing/natural-language-processing-with-python.pdf#page=55) |
| 1.7 Further Reading | [56](natural-language-processing/natural-language-processing-with-python.pdf#page=56) |
| 1.8 Exercises | [57](natural-language-processing/natural-language-processing-with-python.pdf#page=57) |
| 2 Accessing Text Corpora and Lexical Resources | [61](natural-language-processing/natural-language-processing-with-python.pdf#page=61) |
| 2.1 Accessing Text Corpora | [61](natural-language-processing/natural-language-processing-with-python.pdf#page=61) |
| 2.2 Conditional Frequency Distributions | [74](natural-language-processing/natural-language-processing-with-python.pdf#page=74) |
| 2.3 More Python: Reusing Code | [78](natural-language-processing/natural-language-processing-with-python.pdf#page=78) |
| 2.4 Lexical Resources | [81](natural-language-processing/natural-language-processing-with-python.pdf#page=81) |
| 2.5 WordNet | [89](natural-language-processing/natural-language-processing-with-python.pdf#page=89) |
| 2.6 Summary | [95](natural-language-processing/natural-language-processing-with-python.pdf#page=95) |
| 2.7 Further Reading | [95](natural-language-processing/natural-language-processing-with-python.pdf#page=95) |
| 2.8 Exercises | [96](natural-language-processing/natural-language-processing-with-python.pdf#page=96) |
| 3 Processing Raw Text | [101](natural-language-processing/natural-language-processing-with-python.pdf#page=101) |
| 3.1 Accessing Text from the Web and from Disk | [102](natural-language-processing/natural-language-processing-with-python.pdf#page=102) |
| 3.2 Strings: Text Processing at the Lowest Level | [109](natural-language-processing/natural-language-processing-with-python.pdf#page=109) |
| 3.3 Text Processing with Unicode | [115](natural-language-processing/natural-language-processing-with-python.pdf#page=115) |
| 3.4 Regular Expressions for Detecting Word Patterns | [119](natural-language-processing/natural-language-processing-with-python.pdf#page=119) |
| 3.5 Useful Applications of Regular Expressions | [124](natural-language-processing/natural-language-processing-with-python.pdf#page=124) |
| 3.6 Normalizing Text | [129](natural-language-processing/natural-language-processing-with-python.pdf#page=129) |
| 3.7 Regular Expressions for Tokenizing Text | [131](natural-language-processing/natural-language-processing-with-python.pdf#page=131) |
| 3.8 Segmentation | [134](natural-language-processing/natural-language-processing-with-python.pdf#page=134) |
| 3.9 Formatting: From Lists to Strings | [138](natural-language-processing/natural-language-processing-with-python.pdf#page=138) |
| 3.10 Summary | [143](natural-language-processing/natural-language-processing-with-python.pdf#page=143) |
| 3.11 Further Reading | [144](natural-language-processing/natural-language-processing-with-python.pdf#page=144) |
| 3.12 Exercises | [145](natural-language-processing/natural-language-processing-with-python.pdf#page=145) |
| 4 Writing Structured Programs | [151](natural-language-processing/natural-language-processing-with-python.pdf#page=151) |
| 4.1 Back to the Basics | [152](natural-language-processing/natural-language-processing-with-python.pdf#page=152) |
| 4.2 Sequences | [155](natural-language-processing/natural-language-processing-with-python.pdf#page=155) |
| 4.3 Questions of Style | [160](natural-language-processing/natural-language-processing-with-python.pdf#page=160) |
| 4.4 Functions: The Foundation of Structured Programming | [164](natural-language-processing/natural-language-processing-with-python.pdf#page=164) |
| 4.5 Doing More with Functions | [171](natural-language-processing/natural-language-processing-with-python.pdf#page=171) |
| 4.6 Program Development | [176](natural-language-processing/natural-language-processing-with-python.pdf#page=176) |
| 4.7 Algorithm Design | [182](natural-language-processing/natural-language-processing-with-python.pdf#page=182) |
| 4.8 A Sample of Python Libraries | [189](natural-language-processing/natural-language-processing-with-python.pdf#page=189) |
| 4.9 Summary | [194](natural-language-processing/natural-language-processing-with-python.pdf#page=194) |
| 4.10 Further Reading | [195](natural-language-processing/natural-language-processing-with-python.pdf#page=195) |
| 4.11 Exercises | [195](natural-language-processing/natural-language-processing-with-python.pdf#page=195) |
| 5 Categorizing and Tagging Words | [201](natural-language-processing/natural-language-processing-with-python.pdf#page=201) |
| 5.1 Using a Tagger | [201](natural-language-processing/natural-language-processing-with-python.pdf#page=201) |
| 5.2 Tagged Corpora | [203](natural-language-processing/natural-language-processing-with-python.pdf#page=203) |
| 5.3 Mapping Words to Properties Using Python Dictionaries | [211](natural-language-processing/natural-language-processing-with-python.pdf#page=211) |
| 5.4 Automatic Tagging | [220](natural-language-processing/natural-language-processing-with-python.pdf#page=220) |
| 5.5 N-Gram Tagging | [224](natural-language-processing/natural-language-processing-with-python.pdf#page=224) |
| 5.6 Transformation-Based Tagging | [230](natural-language-processing/natural-language-processing-with-python.pdf#page=230) |
| 5.7 How to Determine the Category of a Word | [232](natural-language-processing/natural-language-processing-with-python.pdf#page=232) |
| 5.8 Summary | [235](natural-language-processing/natural-language-processing-with-python.pdf#page=235) |
| 5.9 Further Reading | [236](natural-language-processing/natural-language-processing-with-python.pdf#page=236) |
| 5.10 Exercises | [237](natural-language-processing/natural-language-processing-with-python.pdf#page=237) |
| 6 Learning to Classify Text | [243](natural-language-processing/natural-language-processing-with-python.pdf#page=243) |
| 6.1 Supervised Classification | [243](natural-language-processing/natural-language-processing-with-python.pdf#page=243) |
| 6.2 Further Examples of Supervised Classification | [255](natural-language-processing/natural-language-processing-with-python.pdf#page=255) |
| 6.3 Evaluation | [259](natural-language-processing/natural-language-processing-with-python.pdf#page=259) |
| 6.4 Decision Trees | [264](natural-language-processing/natural-language-processing-with-python.pdf#page=264) |
| 6.5 Naive Bayes Classifiers | [267](natural-language-processing/natural-language-processing-with-python.pdf#page=267) |
| 6.6 Maximum Entropy Classifiers | [272](natural-language-processing/natural-language-processing-with-python.pdf#page=272) |
| 6.7 Modeling Linguistic Patterns | [276](natural-language-processing/natural-language-processing-with-python.pdf#page=276) |
| 6.8 Summary | [278](natural-language-processing/natural-language-processing-with-python.pdf#page=278) |
| 6.9 Further Reading | [278](natural-language-processing/natural-language-processing-with-python.pdf#page=278) |
| 6.10 Exercises | [279](natural-language-processing/natural-language-processing-with-python.pdf#page=279) |
| 7 Extracting Information from Text | [283](natural-language-processing/natural-language-processing-with-python.pdf#page=283) |
| 7.1 Information Extraction | [283](natural-language-processing/natural-language-processing-with-python.pdf#page=283) |
| 7.2 Chunking | [286](natural-language-processing/natural-language-processing-with-python.pdf#page=286) |
| 7.3 Developing and Evaluating Chunkers | [292](natural-language-processing/natural-language-processing-with-python.pdf#page=292) |
| 7.4 Recursion in Linguistic Structure | [299](natural-language-processing/natural-language-processing-with-python.pdf#page=299) |
| 7.5 Named Entity Recognition | [303](natural-language-processing/natural-language-processing-with-python.pdf#page=303) |
| 7.6 Relation Extraction | [306](natural-language-processing/natural-language-processing-with-python.pdf#page=306) |
| 7.7 Summary | [307](natural-language-processing/natural-language-processing-with-python.pdf#page=307) |
| 7.8 Further Reading | [308](natural-language-processing/natural-language-processing-with-python.pdf#page=308) |
| 7.9 Exercises | [308](natural-language-processing/natural-language-processing-with-python.pdf#page=308) |
| 8 Analyzing Sentence Structure | [313](natural-language-processing/natural-language-processing-with-python.pdf#page=313) |
| 8.1 Some Grammatical Dilemmas | [314](natural-language-processing/natural-language-processing-with-python.pdf#page=314) |
| 8.2 What’s the Use of Syntax? | [317](natural-language-processing/natural-language-processing-with-python.pdf#page=317) |
| 8.3 Context-Free Grammar | [320](natural-language-processing/natural-language-processing-with-python.pdf#page=320) |
| 8.4 Parsing with Context-Free Grammar | [324](natural-language-processing/natural-language-processing-with-python.pdf#page=324) |
| 8.5 Dependencies and Dependency Grammar | [332](natural-language-processing/natural-language-processing-with-python.pdf#page=332) |
| 8.6 Grammar Development | [337](natural-language-processing/natural-language-processing-with-python.pdf#page=337) |
| 8.7 Summary | [343](natural-language-processing/natural-language-processing-with-python.pdf#page=343) |
| 8.8 Further Reading | [344](natural-language-processing/natural-language-processing-with-python.pdf#page=344) |
| 8.9 Exercises | [344](natural-language-processing/natural-language-processing-with-python.pdf#page=344) |
| 9 Building Feature-Based Grammars | [349](natural-language-processing/natural-language-processing-with-python.pdf#page=349) |
| 9.1 Grammatical Features | [349](natural-language-processing/natural-language-processing-with-python.pdf#page=349) |
| 9.2 Processing Feature Structures | [359](natural-language-processing/natural-language-processing-with-python.pdf#page=359) |
| 9.3 Extending a Feature-Based Grammar | [366](natural-language-processing/natural-language-processing-with-python.pdf#page=366) |
| 9.4 Summary | [378](natural-language-processing/natural-language-processing-with-python.pdf#page=378) |
| 9.5 Further Reading | [379](natural-language-processing/natural-language-processing-with-python.pdf#page=379) |
| 9.6 Exercises | [380](natural-language-processing/natural-language-processing-with-python.pdf#page=380) |
| 10 Analyzing the Meaning of Sentences | [383](natural-language-processing/natural-language-processing-with-python.pdf#page=383) |
| 10.1 Natural Language Understanding | [383](natural-language-processing/natural-language-processing-with-python.pdf#page=383) |
| 10.2 Propositional Logic | [390](natural-language-processing/natural-language-processing-with-python.pdf#page=390) |
| 10.3 First-Order Logic | [394](natural-language-processing/natural-language-processing-with-python.pdf#page=394) |
| 10.4 The Semantics of English Sentences | [407](natural-language-processing/natural-language-processing-with-python.pdf#page=407) |
| 10.5 Discourse Semantics | [419](natural-language-processing/natural-language-processing-with-python.pdf#page=419) |
| 10.6 Summary | [424](natural-language-processing/natural-language-processing-with-python.pdf#page=424) |
| 10.7 Further Reading | [425](natural-language-processing/natural-language-processing-with-python.pdf#page=425) |
| 10.8 Exercises | [426](natural-language-processing/natural-language-processing-with-python.pdf#page=426) |
| 11 Managing Linguistic Data | [429](natural-language-processing/natural-language-processing-with-python.pdf#page=429) |
| 11.1 Corpus Structure: A Case Study | [429](natural-language-processing/natural-language-processing-with-python.pdf#page=429) |
| 11.2 The Life Cycle of a Corpus | [434](natural-language-processing/natural-language-processing-with-python.pdf#page=434) |
| 11.3 Acquiring Data | [438](natural-language-processing/natural-language-processing-with-python.pdf#page=438) |
| 11.4 Working with XML | [447](natural-language-processing/natural-language-processing-with-python.pdf#page=447) |
| 11.5 Working with Toolbox Data | [453](natural-language-processing/natural-language-processing-with-python.pdf#page=453) |
| 11.6 Describing Language Resources Using OLAC Metadata | [457](natural-language-processing/natural-language-processing-with-python.pdf#page=457) |
| 11.7 Summary | [459](natural-language-processing/natural-language-processing-with-python.pdf#page=459) |
| 11.8 Further Reading | [459](natural-language-processing/natural-language-processing-with-python.pdf#page=459) |
| 11.9 Exercises | [460](natural-language-processing/natural-language-processing-with-python.pdf#page=460) |
| Afterword: The Language Challenge | [463](natural-language-processing/natural-language-processing-with-python.pdf#page=463) |
| Language Processing Versus Symbol Processing | [464](natural-language-processing/natural-language-processing-with-python.pdf#page=464) |
| Contemporary Philosophical Divides | [465](natural-language-processing/natural-language-processing-with-python.pdf#page=465) |
| NLTK Roadmap | [466](natural-language-processing/natural-language-processing-with-python.pdf#page=466) |
| Envoi... | [469](natural-language-processing/natural-language-processing-with-python.pdf#page=469) |
| Bibliography | [471](natural-language-processing/natural-language-processing-with-python.pdf#page=471) |
| NLTK Index | [481](natural-language-processing/natural-language-processing-with-python.pdf#page=481) |
| General Index | [485](natural-language-processing/natural-language-processing-with-python.pdf#page=485) |

### Hands-on large language models

`natural-language-processing/hands-on-large-language-models.pdf`, 598 pages, downloaded as
`Hands-On_Large_Language_Models_-_Jay_Alammar.pdf`. Jay Alammar and Maarten Grootendorst, *Hands-On
Large Language Models*, O'Reilly Media, first edition, September 2024. A published textbook that
teaches large language models intuition first, through many illustrations and working Python code:
tokens and embeddings, the inside of a transformer and its recent improvements, text classification,
clustering and topic modelling, prompt engineering, LangChain chains, memory and agents, semantic
search and retrieval-augmented generation, multimodal models, training embedding models by
contrastive learning, fine-tuning BERT-style classifiers, and fine-tuning generation models (supervised
fine-tuning, QLoRA, reward models, DPO). The table is from the PDF's own outline, chapters and their
sections; the book does not number its sections. The outline puts "Book Structure" on page 9 and the
table corrects it to 10.

**Page numbers.** This PDF was converted from the ebook with calibre, and many chapters end on an
OceanofPDF.com stamp. Its pages carry no printed page numbers and do not match the print edition's
pages, so a page number quoted from the print book will not open the right PDF page. Every number here
is a PDF page.

**Its index.** PDF pages 537 to 595. Entries name the section they point to rather than a page
("attention, Encoding and Decoding Context with Attention"), and each entry is a live link inside the
PDF to that section's page.

| Chapter or section | PDF page |
| --- | --- |
| Preface | [8](natural-language-processing/hands-on-large-language-models.pdf#page=8) |
| An Intuition-First Philosophy | [8](natural-language-processing/hands-on-large-language-models.pdf#page=8) |
| Prerequisites | [9](natural-language-processing/hands-on-large-language-models.pdf#page=9) |
| Book Structure | [10](natural-language-processing/hands-on-large-language-models.pdf#page=10) |
| Hardware and Software Requirements | [14](natural-language-processing/hands-on-large-language-models.pdf#page=14) |
| API Keys | [15](natural-language-processing/hands-on-large-language-models.pdf#page=15) |
| Conventions Used in This Book | [16](natural-language-processing/hands-on-large-language-models.pdf#page=16) |
| Using Code Examples | [17](natural-language-processing/hands-on-large-language-models.pdf#page=17) |
| O’Reilly Online Learning | [18](natural-language-processing/hands-on-large-language-models.pdf#page=18) |
| How to Contact Us | [18](natural-language-processing/hands-on-large-language-models.pdf#page=18) |
| Acknowledgments | [19](natural-language-processing/hands-on-large-language-models.pdf#page=19) |
| Part: I Understanding Language Models | [22](natural-language-processing/hands-on-large-language-models.pdf#page=22) |
| 1 An Introduction to Large Language Models | [23](natural-language-processing/hands-on-large-language-models.pdf#page=23) |
| What Is Language AI? | [24](natural-language-processing/hands-on-large-language-models.pdf#page=24) |
| A Recent History of Language AI | [25](natural-language-processing/hands-on-large-language-models.pdf#page=25) |
| The Moving Definition of a “Large Language Model” | [50](natural-language-processing/hands-on-large-language-models.pdf#page=50) |
| The Training Paradigm of Large Language Models | [51](natural-language-processing/hands-on-large-language-models.pdf#page=51) |
| Large Language Model Applications: What Makes Them So Useful? | [53](natural-language-processing/hands-on-large-language-models.pdf#page=53) |
| Responsible LLM Development and Usage | [55](natural-language-processing/hands-on-large-language-models.pdf#page=55) |
| Limited Resources Are All You Need | [56](natural-language-processing/hands-on-large-language-models.pdf#page=56) |
| Interfacing with Large Language Models | [57](natural-language-processing/hands-on-large-language-models.pdf#page=57) |
| Generating Your First Text | [61](natural-language-processing/hands-on-large-language-models.pdf#page=61) |
| Summary | [64](natural-language-processing/hands-on-large-language-models.pdf#page=64) |
| 2 Tokens and Embeddings | [67](natural-language-processing/hands-on-large-language-models.pdf#page=67) |
| LLM Tokenization | [68](natural-language-processing/hands-on-large-language-models.pdf#page=68) |
| Token Embeddings | [94](natural-language-processing/hands-on-large-language-models.pdf#page=94) |
| Text Embeddings (for Sentences and Whole Documents) | [100](natural-language-processing/hands-on-large-language-models.pdf#page=100) |
| Word Embeddings Beyond LLMs | [102](natural-language-processing/hands-on-large-language-models.pdf#page=102) |
| Embeddings for Recommendation Systems | [108](natural-language-processing/hands-on-large-language-models.pdf#page=108) |
| Summary | [113](natural-language-processing/hands-on-large-language-models.pdf#page=113) |
| 3 Looking Inside Large Language Models | [116](natural-language-processing/hands-on-large-language-models.pdf#page=116) |
| An Overview of Transformer Models | [117](natural-language-processing/hands-on-large-language-models.pdf#page=117) |
| Recent Improvements to the Transformer Architecture | [143](natural-language-processing/hands-on-large-language-models.pdf#page=143) |
| Summary | [157](natural-language-processing/hands-on-large-language-models.pdf#page=157) |
| Part: II Using Pretrained Language Models | [159](natural-language-processing/hands-on-large-language-models.pdf#page=159) |
| 4 Text Classification | [160](natural-language-processing/hands-on-large-language-models.pdf#page=160) |
| The Sentiment of Movie Reviews | [161](natural-language-processing/hands-on-large-language-models.pdf#page=161) |
| Text Classification with Representation Models | [163](natural-language-processing/hands-on-large-language-models.pdf#page=163) |
| Model Selection | [164](natural-language-processing/hands-on-large-language-models.pdf#page=164) |
| Using a Task-Specific Model | [166](natural-language-processing/hands-on-large-language-models.pdf#page=166) |
| Classification Tasks That Leverage Embeddings | [171](natural-language-processing/hands-on-large-language-models.pdf#page=171) |
| Text Classification with Generative Models | [180](natural-language-processing/hands-on-large-language-models.pdf#page=180) |
| Summary | [190](natural-language-processing/hands-on-large-language-models.pdf#page=190) |
| 5 Text Clustering and Topic Modeling | [192](natural-language-processing/hands-on-large-language-models.pdf#page=192) |
| ArXiv’s Articles: Computation and Language | [193](natural-language-processing/hands-on-large-language-models.pdf#page=193) |
| A Common Pipeline for Text Clustering | [194](natural-language-processing/hands-on-large-language-models.pdf#page=194) |
| From Text Clustering to Topic Modeling | [204](natural-language-processing/hands-on-large-language-models.pdf#page=204) |
| Summary | [233](natural-language-processing/hands-on-large-language-models.pdf#page=233) |
| 6 Prompt Engineering | [236](natural-language-processing/hands-on-large-language-models.pdf#page=236) |
| Using Text Generation Models | [236](natural-language-processing/hands-on-large-language-models.pdf#page=236) |
| Intro to Prompt Engineering | [244](natural-language-processing/hands-on-large-language-models.pdf#page=244) |
| Advanced Prompt Engineering | [250](natural-language-processing/hands-on-large-language-models.pdf#page=250) |
| Reasoning with Generative Models | [260](natural-language-processing/hands-on-large-language-models.pdf#page=260) |
| Output Verification | [270](natural-language-processing/hands-on-large-language-models.pdf#page=270) |
| Summary | [278](natural-language-processing/hands-on-large-language-models.pdf#page=278) |
| 7 Advanced Text Generation Techniques and Tools | [280](natural-language-processing/hands-on-large-language-models.pdf#page=280) |
| Model I/O: Loading Quantized Models with LangChain | [281](natural-language-processing/hands-on-large-language-models.pdf#page=281) |
| Chains: Extending the Capabilities of LLMs | [284](natural-language-processing/hands-on-large-language-models.pdf#page=284) |
| Memory: Helping LLMs to Remember Conversations | [293](natural-language-processing/hands-on-large-language-models.pdf#page=293) |
| Agents: Creating a System of LLMs | [306](natural-language-processing/hands-on-large-language-models.pdf#page=306) |
| Summary | [314](natural-language-processing/hands-on-large-language-models.pdf#page=314) |
| 8 Semantic Search and Retrieval-Augmented Generation | [316](natural-language-processing/hands-on-large-language-models.pdf#page=316) |
| Overview of Semantic Search and RAG | [317](natural-language-processing/hands-on-large-language-models.pdf#page=317) |
| Semantic Search with Language Models | [319](natural-language-processing/hands-on-large-language-models.pdf#page=319) |
| Retrieval-Augmented Generation (RAG) | [349](natural-language-processing/hands-on-large-language-models.pdf#page=349) |
| Summary | [358](natural-language-processing/hands-on-large-language-models.pdf#page=358) |
| 9 Multimodal Large Language Models | [360](natural-language-processing/hands-on-large-language-models.pdf#page=360) |
| Transformers for Vision | [361](natural-language-processing/hands-on-large-language-models.pdf#page=361) |
| Multimodal Embedding Models | [364](natural-language-processing/hands-on-large-language-models.pdf#page=364) |
| Making Text Generation Models Multimodal | [377](natural-language-processing/hands-on-large-language-models.pdf#page=377) |
| Summary | [395](natural-language-processing/hands-on-large-language-models.pdf#page=395) |
| Part: III Training and Fine-Tuning Language Models | [398](natural-language-processing/hands-on-large-language-models.pdf#page=398) |
| 10 Creating Text Embedding Models | [399](natural-language-processing/hands-on-large-language-models.pdf#page=399) |
| Embedding Models | [399](natural-language-processing/hands-on-large-language-models.pdf#page=399) |
| What Is Contrastive Learning? | [402](natural-language-processing/hands-on-large-language-models.pdf#page=402) |
| SBERT | [404](natural-language-processing/hands-on-large-language-models.pdf#page=404) |
| Creating an Embedding Model | [408](natural-language-processing/hands-on-large-language-models.pdf#page=408) |
| Fine-Tuning an Embedding Model | [426](natural-language-processing/hands-on-large-language-models.pdf#page=426) |
| Unsupervised Learning | [435](natural-language-processing/hands-on-large-language-models.pdf#page=435) |
| Summary | [443](natural-language-processing/hands-on-large-language-models.pdf#page=443) |
| 11 Fine-Tuning Representation Models for Classification | [446](natural-language-processing/hands-on-large-language-models.pdf#page=446) |
| Supervised Classification | [446](natural-language-processing/hands-on-large-language-models.pdf#page=446) |
| Few-Shot Classification | [459](natural-language-processing/hands-on-large-language-models.pdf#page=459) |
| Continued Pretraining with Masked Language Modeling | [468](natural-language-processing/hands-on-large-language-models.pdf#page=468) |
| Named-Entity Recognition | [475](natural-language-processing/hands-on-large-language-models.pdf#page=475) |
| Summary | [485](natural-language-processing/hands-on-large-language-models.pdf#page=485) |
| 12 Fine-Tuning Generation Models | [487](natural-language-processing/hands-on-large-language-models.pdf#page=487) |
| The Three LLM Training Steps: Pretraining, Supervised Fine-Tuning, and Preference Tuning | [487](natural-language-processing/hands-on-large-language-models.pdf#page=487) |
| Supervised Fine-Tuning (SFT) | [489](natural-language-processing/hands-on-large-language-models.pdf#page=489) |
| Instruction Tuning with QLoRA | [503](natural-language-processing/hands-on-large-language-models.pdf#page=503) |
| Evaluating Generative Models | [511](natural-language-processing/hands-on-large-language-models.pdf#page=511) |
| Preference-Tuning / Alignment / RLHF | [518](natural-language-processing/hands-on-large-language-models.pdf#page=518) |
| Automating Preference Evaluation Using Reward Models | [519](natural-language-processing/hands-on-large-language-models.pdf#page=519) |
| Preference Tuning with DPO | [528](natural-language-processing/hands-on-large-language-models.pdf#page=528) |
| Summary | [533](natural-language-processing/hands-on-large-language-models.pdf#page=533) |
| Afterword | [536](natural-language-processing/hands-on-large-language-models.pdf#page=536) |
| Index | [537](natural-language-processing/hands-on-large-language-models.pdf#page=537) |
| About the Authors | [597](natural-language-processing/hands-on-large-language-models.pdf#page=597) |

## ai-engineering/

### AI engineering

`ai-engineering/ai-engineering.pdf`, 991 pages, downloaded as `AI Engineering by Chip Huyen (1).pdf`
into the learning tree's `mathematics/` folder and moved onto the shelf. Chip Huyen, *AI Engineering:
Building Applications with Foundation Models*, O'Reilly Media, first edition, December 2024 (copyright
2025). A published textbook on building applications on top of foundation models: what AI engineering
is and its stack, how foundation models are made (training data, modelling, post-training, sampling),
evaluation (language-modelling metrics such as perplexity, exact evaluation, AI as a judge, ranking
models by comparison), evaluating AI systems and choosing a model, prompt engineering and defending
against prompt attacks, RAG and agents, finetuning (memory bottlenecks, parameter-efficient techniques, model
merging), dataset engineering, inference optimisation, and system architecture with user feedback.
The table is from the PDF's own outline, chapters and their sections; the book does not number its
sections. The outline puts three preface sections a page early ("What This Book Is About", "What This
Book Is Not", "Who This Book Is For"), and the table gives the pages they start on.

**Page numbers.** The PDF's own title reads "AI Engineering (for True Epub)": it was converted from the
ebook with calibre, and many chapters end on an OceanofPDF.com stamp. Its pages carry no printed page
numbers and do not match the print edition's pages, so a page number quoted from the print book will
not open the right PDF page. Every number here is a PDF page.

**Its index.** PDF pages 932 to 988. Entries name the section they point to rather than a page
("value vector (V), Attention mechanism"), and each entry is a live link inside the PDF to that
section's page.

| Chapter or section | PDF page |
| --- | --- |
| Preface | [9](ai-engineering/ai-engineering.pdf#page=9) |
| What This Book Is About | [12](ai-engineering/ai-engineering.pdf#page=12) |
| What This Book Is Not | [16](ai-engineering/ai-engineering.pdf#page=16) |
| Who This Book Is For | [18](ai-engineering/ai-engineering.pdf#page=18) |
| Navigating This Book | [19](ai-engineering/ai-engineering.pdf#page=19) |
| Conventions Used in This Book | [23](ai-engineering/ai-engineering.pdf#page=23) |
| Using Code Examples | [24](ai-engineering/ai-engineering.pdf#page=24) |
| O’Reilly Online Learning | [25](ai-engineering/ai-engineering.pdf#page=25) |
| How to Contact Us | [26](ai-engineering/ai-engineering.pdf#page=26) |
| Acknowledgments | [27](ai-engineering/ai-engineering.pdf#page=27) |
| 1 Introduction to Building AI Applications with Foundation Models | [32](ai-engineering/ai-engineering.pdf#page=32) |
| The Rise of AI Engineering | [34](ai-engineering/ai-engineering.pdf#page=34) |
| Foundation Model Use Cases | [57](ai-engineering/ai-engineering.pdf#page=57) |
| Planning AI Applications | [78](ai-engineering/ai-engineering.pdf#page=78) |
| The AI Engineering Stack | [91](ai-engineering/ai-engineering.pdf#page=91) |
| Summary | [113](ai-engineering/ai-engineering.pdf#page=113) |
| 2 Understanding Foundation Models | [119](ai-engineering/ai-engineering.pdf#page=119) |
| Training Data | [121](ai-engineering/ai-engineering.pdf#page=121) |
| Modeling | [135](ai-engineering/ai-engineering.pdf#page=135) |
| Post-Training | [169](ai-engineering/ai-engineering.pdf#page=169) |
| Sampling | [187](ai-engineering/ai-engineering.pdf#page=187) |
| Summary | [225](ai-engineering/ai-engineering.pdf#page=225) |
| 3 Evaluation Methodology | [232](ai-engineering/ai-engineering.pdf#page=232) |
| Challenges of Evaluating Foundation Models | [234](ai-engineering/ai-engineering.pdf#page=234) |
| Understanding Language Modeling Metrics | [240](ai-engineering/ai-engineering.pdf#page=240) |
| Exact Evaluation | [252](ai-engineering/ai-engineering.pdf#page=252) |
| AI as a Judge | [271](ai-engineering/ai-engineering.pdf#page=271) |
| Ranking Models with Comparative Evaluation | [295](ai-engineering/ai-engineering.pdf#page=295) |
| Summary | [309](ai-engineering/ai-engineering.pdf#page=309) |
| 4 Evaluate AI Systems | [315](ai-engineering/ai-engineering.pdf#page=315) |
| Evaluation Criteria | [316](ai-engineering/ai-engineering.pdf#page=316) |
| Model Selection | [355](ai-engineering/ai-engineering.pdf#page=355) |
| Design Your Evaluation Pipeline | [393](ai-engineering/ai-engineering.pdf#page=393) |
| Summary | [409](ai-engineering/ai-engineering.pdf#page=409) |
| 5 Prompt Engineering | [416](ai-engineering/ai-engineering.pdf#page=416) |
| Introduction to Prompting | [417](ai-engineering/ai-engineering.pdf#page=417) |
| Prompt Engineering Best Practices | [431](ai-engineering/ai-engineering.pdf#page=431) |
| Defensive Prompt Engineering | [462](ai-engineering/ai-engineering.pdf#page=462) |
| Summary | [490](ai-engineering/ai-engineering.pdf#page=490) |
| 6 RAG and Agents | [494](ai-engineering/ai-engineering.pdf#page=494) |
| RAG | [495](ai-engineering/ai-engineering.pdf#page=495) |
| Agents | [535](ai-engineering/ai-engineering.pdf#page=535) |
| Memory | [581](ai-engineering/ai-engineering.pdf#page=581) |
| Summary | [589](ai-engineering/ai-engineering.pdf#page=589) |
| 7 Finetuning | [594](ai-engineering/ai-engineering.pdf#page=594) |
| Finetuning Overview | [596](ai-engineering/ai-engineering.pdf#page=596) |
| When to Finetune | [601](ai-engineering/ai-engineering.pdf#page=601) |
| Memory Bottlenecks | [618](ai-engineering/ai-engineering.pdf#page=618) |
| Finetuning Techniques | [638](ai-engineering/ai-engineering.pdf#page=638) |
| Summary | [687](ai-engineering/ai-engineering.pdf#page=687) |
| 8 Dataset Engineering | [694](ai-engineering/ai-engineering.pdf#page=694) |
| Data Curation | [697](ai-engineering/ai-engineering.pdf#page=697) |
| Data Augmentation and Synthesis | [726](ai-engineering/ai-engineering.pdf#page=726) |
| Data Processing | [755](ai-engineering/ai-engineering.pdf#page=755) |
| Summary | [768](ai-engineering/ai-engineering.pdf#page=768) |
| 9 Inference Optimization | [773](ai-engineering/ai-engineering.pdf#page=773) |
| Understanding Inference Optimization | [775](ai-engineering/ai-engineering.pdf#page=775) |
| Inference Optimization | [808](ai-engineering/ai-engineering.pdf#page=808) |
| Summary | [845](ai-engineering/ai-engineering.pdf#page=845) |
| 10 AI Engineering Architecture and User Feedback | [852](ai-engineering/ai-engineering.pdf#page=852) |
| AI Engineering Architecture | [853](ai-engineering/ai-engineering.pdf#page=853) |
| User Feedback | [894](ai-engineering/ai-engineering.pdf#page=894) |
| Summary | [925](ai-engineering/ai-engineering.pdf#page=925) |
| Epilogue | [930](ai-engineering/ai-engineering.pdf#page=930) |
| Index | [932](ai-engineering/ai-engineering.pdf#page=932) |
| About the Author | [989](ai-engineering/ai-engineering.pdf#page=989) |

## software-engineering/

### Code simplicity

`software-engineering/code-simplicity.pdf`, 90 pages. Max Kanat-Alexander, *Code Simplicity*, O'Reilly Media, first edition, March 2012. A short published book arguing for
software design as a science with stated laws: the purpose of software, the equation of software design,
change and the three
flaws, defects and design, simplicity, complexity and when rewriting is justified, and testing.
Appendix A lists the laws and appendix B every fact, law, rule and definition in the book. Was `Code
Simplicity - Max Kanat-Alexander.pdf`; the copy carries it-ebooks.info stamps on its pages.

**Page numbers.** The printed page number is the PDF page minus 10 (printed page 1, where chapter 1
starts, is PDF page 11). The front matter is numbered in roman. There is no index; the table is the
PDF's own outline, chapters and their sections.

| Chapter or section | PDF page |
| --- | --- |
| Table of Contents | [5](software-engineering/code-simplicity.pdf#page=5) |
| Preface | [7](software-engineering/code-simplicity.pdf#page=7) |
| Conventions Used in This Book | [8](software-engineering/code-simplicity.pdf#page=8) |
| Attribution and Permissions | [8](software-engineering/code-simplicity.pdf#page=8) |
| Safari® Books Online | [8](software-engineering/code-simplicity.pdf#page=8) |
| How to Contact Us | [9](software-engineering/code-simplicity.pdf#page=9) |
| Acknowledgments | [10](software-engineering/code-simplicity.pdf#page=10) |
| Chapter 1. Introduction | [11](software-engineering/code-simplicity.pdf#page=11) |
| What’s Wrong with Computers? | [11](software-engineering/code-simplicity.pdf#page=11) |
| What Is a Program, Really? | [13](software-engineering/code-simplicity.pdf#page=13) |
| Chapter 2. The Missing Science | [15](software-engineering/code-simplicity.pdf#page=15) |
| Every Programmer Is a Designer | [16](software-engineering/code-simplicity.pdf#page=16) |
| The Science of Software Design | [17](software-engineering/code-simplicity.pdf#page=17) |
| Why Has There Been No Science of Software Design? | [19](software-engineering/code-simplicity.pdf#page=19) |
| Chapter 3. The Driving Forces of Software Design | [23](software-engineering/code-simplicity.pdf#page=23) |
| The Goals of Software Design | [26](software-engineering/code-simplicity.pdf#page=26) |
| Chapter 4. The Future | [29](software-engineering/code-simplicity.pdf#page=29) |
| The Equation of Software Design | [29](software-engineering/code-simplicity.pdf#page=29) |
| The Quality of Design | [36](software-engineering/code-simplicity.pdf#page=36) |
| Unforeseeable Consequences | [37](software-engineering/code-simplicity.pdf#page=37) |
| Chapter 5. Change | [41](software-engineering/code-simplicity.pdf#page=41) |
| Change in a Real-World Program | [41](software-engineering/code-simplicity.pdf#page=41) |
| The Three Flaws | [44](software-engineering/code-simplicity.pdf#page=44) |
| Incremental Development and Design | [50](software-engineering/code-simplicity.pdf#page=50) |
| Chapter 6. Defects and Design | [53](software-engineering/code-simplicity.pdf#page=53) |
| If It Ain’t Broken... | [54](software-engineering/code-simplicity.pdf#page=54) |
| Don’t Repeat Yourself | [55](software-engineering/code-simplicity.pdf#page=55) |
| Chapter 7. Simplicity | [57](software-engineering/code-simplicity.pdf#page=57) |
| Simplicity and the Equation of Software Design | [59](software-engineering/code-simplicity.pdf#page=59) |
| Simplicity Is Relative | [59](software-engineering/code-simplicity.pdf#page=59) |
| How Simple Do You Have to Be? | [61](software-engineering/code-simplicity.pdf#page=61) |
| Be Consistent | [63](software-engineering/code-simplicity.pdf#page=63) |
| Readability | [64](software-engineering/code-simplicity.pdf#page=64) |
| Simplicity Requires Design | [66](software-engineering/code-simplicity.pdf#page=66) |
| Chapter 8. Complexity | [69](software-engineering/code-simplicity.pdf#page=69) |
| Complexity and Purpose | [71](software-engineering/code-simplicity.pdf#page=71) |
| Bad Technologies | [72](software-engineering/code-simplicity.pdf#page=72) |
| Complexity and the Wrong Solution | [74](software-engineering/code-simplicity.pdf#page=74) |
| Complex Problems | [75](software-engineering/code-simplicity.pdf#page=75) |
| Handling Complexity | [76](software-engineering/code-simplicity.pdf#page=76) |
| Rewriting | [79](software-engineering/code-simplicity.pdf#page=79) |
| Chapter 9. Testing | [81](software-engineering/code-simplicity.pdf#page=81) |
| Appendix A. The Laws of Software Design | [83](software-engineering/code-simplicity.pdf#page=83) |
| Appendix B. Facts, Laws, Rules, and Definitions | [85](software-engineering/code-simplicity.pdf#page=85) |

## database-systems/

### Database systems textbook

`database-systems/database-systems-textbook.pdf`, 818 pages, 58 MB. Carlos Coronel and Steven Morris,
*Database Systems: Design, Implementation, and Management*, 12th edition, Cengage Learning, 2017. A
published undergraduate course textbook on relational databases, built around small worked databases
whose tables are printed in the text: data models, the relational model (keys, entity and referential
integrity, relational algebra, relationships), entity relationship modelling, normalization from first
normal form to Boyce-Codd and denormalization, SQL from table definition through joins, subqueries,
views and procedural SQL, the database design life cycle, transactions and concurrency control (ACID,
locking, time stamps, isolation levels, recovery from the transaction log), performance tuning and query
optimization, distributed databases and the CAP theorem, data warehouses and star schemas, Hadoop and
NoSQL, database connectivity and the cloud, and database administration and security. Each chapter ends
with key terms, review questions and problems; a glossary precedes the index. Was `Database Systems
Design, Implementation, and Management.pdf`, in the learning tree's `system-design/` folder.

**Page numbers.** The printed page number is the PDF page minus 26 (printed page 3, the first numbered
page of chapter 1, is PDF page 29; chapter 10's printed page 483 is PDF page 509). The front matter is
numbered in roman. The back-of-book index runs from PDF page 809 to 818 and gives printed pages, so add
26 to an index page to open it; the glossary runs from PDF page 795. The table is the PDF's own outline:
parts, chapters and their numbered sections, without each chapter's opening list, preview, summary, key
terms, review questions, problems and cases.

| Chapter or section | PDF page |
| --- | --- |
| Cover | [1](database-systems/database-systems-textbook.pdf#page=1) |
| Title | [2](database-systems/database-systems-textbook.pdf#page=2) |
| Statement | [3](database-systems/database-systems-textbook.pdf#page=3) |
| Copyright | [4](database-systems/database-systems-textbook.pdf#page=4) |
| Dedication | [5](database-systems/database-systems-textbook.pdf#page=5) |
| Brief Contents | [6](database-systems/database-systems-textbook.pdf#page=6) |
| Contents | [8](database-systems/database-systems-textbook.pdf#page=8) |
| Preface | [16](database-systems/database-systems-textbook.pdf#page=16) |
| Text Features | [21](database-systems/database-systems-textbook.pdf#page=21) |
| Additional Features | [23](database-systems/database-systems-textbook.pdf#page=23) |
| Acknowledgments | [25](database-systems/database-systems-textbook.pdf#page=25) |
| Part 1: Database Concepts | [27](database-systems/database-systems-textbook.pdf#page=27) |
| Ch 1: Database Systems | [28](database-systems/database-systems-textbook.pdf#page=28) |
| 1-1: Why Databases? | [29](database-systems/database-systems-textbook.pdf#page=29) |
| 1-2: Data versus Information | [30](database-systems/database-systems-textbook.pdf#page=30) |
| 1-3: Introducing the Database | [32](database-systems/database-systems-textbook.pdf#page=32) |
| 1-4: Why Database Design is Important | [37](database-systems/database-systems-textbook.pdf#page=37) |
| 1-5: Evolution of File System Data Processing | [40](database-systems/database-systems-textbook.pdf#page=40) |
| 1-7: Database Systems | [47](database-systems/database-systems-textbook.pdf#page=47) |
| 1-8: Preparing for Your Database Professional Career | [54](database-systems/database-systems-textbook.pdf#page=54) |
| Ch 2: Data Models | [61](database-systems/database-systems-textbook.pdf#page=61) |
| 2-1: Data Modeling and Data Models | [62](database-systems/database-systems-textbook.pdf#page=62) |
| 2-2: The Importance of Data Models | [63](database-systems/database-systems-textbook.pdf#page=63) |
| 2-3: Data Model Basic Building Blocks | [63](database-systems/database-systems-textbook.pdf#page=63) |
| 2-4: Business Rules | [65](database-systems/database-systems-textbook.pdf#page=65) |
| 2-5: The Evolution of Data Models | [67](database-systems/database-systems-textbook.pdf#page=67) |
| 2-6: Degrees of Data Abstraction | [83](database-systems/database-systems-textbook.pdf#page=83) |
| Part 2: Design Concepts | [97](database-systems/database-systems-textbook.pdf#page=97) |
| Ch 3: The Relational Database Model | [98](database-systems/database-systems-textbook.pdf#page=98) |
| 3-1: A Logical View of Data | [99](database-systems/database-systems-textbook.pdf#page=99) |
| 3-2: Keys | [102](database-systems/database-systems-textbook.pdf#page=102) |
| 3-3: Integrity Rules | [106](database-systems/database-systems-textbook.pdf#page=106) |
| 3-4: Relational Algebra | [108](database-systems/database-systems-textbook.pdf#page=108) |
| 3-5: The Data Dictionary and the System Catalog | [117](database-systems/database-systems-textbook.pdf#page=117) |
| 3-6: Relationships within the Relational Database | [119](database-systems/database-systems-textbook.pdf#page=119) |
| 3-7: Data Redundancy Revisited | [127](database-systems/database-systems-textbook.pdf#page=127) |
| 3-8: Indexes | [129](database-systems/database-systems-textbook.pdf#page=129) |
| 3-9: Codd’s Relational Database Rules | [130](database-systems/database-systems-textbook.pdf#page=130) |
| Ch 4: Entity Relationship (ER) Modeling | [143](database-systems/database-systems-textbook.pdf#page=143) |
| 4-1: The Entity Relationship Model (ERM) | [144](database-systems/database-systems-textbook.pdf#page=144) |
| 4-2: Developing an ER Diagram | [166](database-systems/database-systems-textbook.pdf#page=166) |
| 4-3: Database Design Challenges: Conflicting Goals | [173](database-systems/database-systems-textbook.pdf#page=173) |
| Ch 5: Advanced Data Modeling | [195](database-systems/database-systems-textbook.pdf#page=195) |
| 5-1: The Extended Entity Relationship Model | [196](database-systems/database-systems-textbook.pdf#page=196) |
| 5-2: Entity Clustering | [202](database-systems/database-systems-textbook.pdf#page=202) |
| 5-3: Entity Integrity: Selecting Primary Keys | [203](database-systems/database-systems-textbook.pdf#page=203) |
| Ch 6: Normalization of Database Tables | [227](database-systems/database-systems-textbook.pdf#page=227) |
| 6-1: Database Tables and Normalization | [228](database-systems/database-systems-textbook.pdf#page=228) |
| 6-2: The Need For Normalization | [228](database-systems/database-systems-textbook.pdf#page=228) |
| 6-3: The Normalization Process | [232](database-systems/database-systems-textbook.pdf#page=232) |
| 6-4: Improving the Design | [241](database-systems/database-systems-textbook.pdf#page=241) |
| 6-5: Surrogate Key Considerations | [245](database-systems/database-systems-textbook.pdf#page=245) |
| 6-6: Higher-Level Normal Forms | [246](database-systems/database-systems-textbook.pdf#page=246) |
| 6-7: Normalization and Database Design | [252](database-systems/database-systems-textbook.pdf#page=252) |
| 6-8: Denormalization | [255](database-systems/database-systems-textbook.pdf#page=255) |
| 6-9: Data-Modeling Checklist | [258](database-systems/database-systems-textbook.pdf#page=258) |
| Part 3: Advanced Design and Implementation | [271](database-systems/database-systems-textbook.pdf#page=271) |
| Ch 7: Introduction to Structured Query Language (SQL) | [272](database-systems/database-systems-textbook.pdf#page=272) |
| 7-1: Introduction to SQL | [273](database-systems/database-systems-textbook.pdf#page=273) |
| 7-2: Data Definition Commands | [275](database-systems/database-systems-textbook.pdf#page=275) |
| 7-3: Data Manipulation Commands | [290](database-systems/database-systems-textbook.pdf#page=290) |
| 7-4: SELECT Queries | [297](database-systems/database-systems-textbook.pdf#page=297) |
| 7-5: Additional Data Definition Commands | [309](database-systems/database-systems-textbook.pdf#page=309) |
| 7-6: Additional SELECT Query Keywords | [316](database-systems/database-systems-textbook.pdf#page=316) |
| 7-7: Joining Database Tables | [326](database-systems/database-systems-textbook.pdf#page=326) |
| Ch 8: Advanced SQL | [366](database-systems/database-systems-textbook.pdf#page=366) |
| 8-1: SQL Join Operators | [367](database-systems/database-systems-textbook.pdf#page=367) |
| 8-2: Subqueries and Correlated Queries | [375](database-systems/database-systems-textbook.pdf#page=375) |
| 8-3: SQL Functions | [387](database-systems/database-systems-textbook.pdf#page=387) |
| 8-4: Relational Set Operators | [397](database-systems/database-systems-textbook.pdf#page=397) |
| 8-5: Virtual Tables: Creating a View | [403](database-systems/database-systems-textbook.pdf#page=403) |
| 8-6: Sequences | [408](database-systems/database-systems-textbook.pdf#page=408) |
| 8-7: Procedural SQL | [413](database-systems/database-systems-textbook.pdf#page=413) |
| 8-8: Embedded SQL | [436](database-systems/database-systems-textbook.pdf#page=436) |
| Ch 9: Database Design | [465](database-systems/database-systems-textbook.pdf#page=465) |
| 9-1: The Information System | [466](database-systems/database-systems-textbook.pdf#page=466) |
| 9-2: The Systems Development Life Cycle | [468](database-systems/database-systems-textbook.pdf#page=468) |
| 9-3: The Database Life Cycle | [471](database-systems/database-systems-textbook.pdf#page=471) |
| 9-4: Conceptual Design | [483](database-systems/database-systems-textbook.pdf#page=483) |
| 9-5: DBMS Software Selection | [493](database-systems/database-systems-textbook.pdf#page=493) |
| 9-6: Logical Design | [494](database-systems/database-systems-textbook.pdf#page=494) |
| 9-7: Physical Design | [497](database-systems/database-systems-textbook.pdf#page=497) |
| 9-8: Database Design Strategies | [499](database-systems/database-systems-textbook.pdf#page=499) |
| 9-9: Centralized Versus Decentralized Design | [500](database-systems/database-systems-textbook.pdf#page=500) |
| Part 4: Advanced Database Concepts | [507](database-systems/database-systems-textbook.pdf#page=507) |
| Ch 10: Transaction Management and Concurrency Control | [508](database-systems/database-systems-textbook.pdf#page=508) |
| 10-1: What Is a Transaction? | [509](database-systems/database-systems-textbook.pdf#page=509) |
| 10-2: Concurrency Control | [516](database-systems/database-systems-textbook.pdf#page=516) |
| 10-3: Concurrency Control with Locking Methods | [521](database-systems/database-systems-textbook.pdf#page=521) |
| 10-4: Concurrency Control with Time Stamping Methods | [528](database-systems/database-systems-textbook.pdf#page=528) |
| 10-5: Concurrency Control with Optimistic Methods | [529](database-systems/database-systems-textbook.pdf#page=529) |
| 10-6: ANSI Levels of Transaction Isolation | [530](database-systems/database-systems-textbook.pdf#page=530) |
| 10-7: Database Recovery Management | [532](database-systems/database-systems-textbook.pdf#page=532) |
| Ch 11: Database Performance Tuning and Query Optimization | [541](database-systems/database-systems-textbook.pdf#page=541) |
| 11-1: Database Performance-Tuning Concepts | [542](database-systems/database-systems-textbook.pdf#page=542) |
| 11-2: Query Processing | [548](database-systems/database-systems-textbook.pdf#page=548) |
| 11-3: Indexes and Query Optimization | [552](database-systems/database-systems-textbook.pdf#page=552) |
| 11-4: Optimizer Choices | [554](database-systems/database-systems-textbook.pdf#page=554) |
| 11-5: SQL Performance Tuning | [557](database-systems/database-systems-textbook.pdf#page=557) |
| 11-6: Query Formulation | [560](database-systems/database-systems-textbook.pdf#page=560) |
| 11-7: DBMS Performance Tuning | [562](database-systems/database-systems-textbook.pdf#page=562) |
| 11-8: Query Optimization Example | [564](database-systems/database-systems-textbook.pdf#page=564) |
| Ch 12: Distributed Database Management Systems | [579](database-systems/database-systems-textbook.pdf#page=579) |
| 12-1: The Evolution of Distributed Database Management Systems | [580](database-systems/database-systems-textbook.pdf#page=580) |
| 12-2: DDBMS Advantages and Disadvantages | [582](database-systems/database-systems-textbook.pdf#page=582) |
| 12-3: Distributed Processing and Distributed Databases | [582](database-systems/database-systems-textbook.pdf#page=582) |
| 12-4: Characteristics of Distributed Database Management Systems | [585](database-systems/database-systems-textbook.pdf#page=585) |
| 12-5: DDBMS Components | [586](database-systems/database-systems-textbook.pdf#page=586) |
| 12-6: Levels of Data and Process Distribution | [587](database-systems/database-systems-textbook.pdf#page=587) |
| 12-7: Distributed Database Transparency Features | [590](database-systems/database-systems-textbook.pdf#page=590) |
| 12-8: Distribution Transparency | [591](database-systems/database-systems-textbook.pdf#page=591) |
| 12-9: Transaction Transparency | [594](database-systems/database-systems-textbook.pdf#page=594) |
| 12-10: Performance and Failure Transparency | [599](database-systems/database-systems-textbook.pdf#page=599) |
| 12-11: Distributed Database Design | [601](database-systems/database-systems-textbook.pdf#page=601) |
| 12-12: The CAP Theorem | [607](database-systems/database-systems-textbook.pdf#page=607) |
| 12-13: C. J. Date’s 12 Commandments for Distributed Databases | [609](database-systems/database-systems-textbook.pdf#page=609) |
| Ch 13: Business Intelligence and Data Warehouses | [615](database-systems/database-systems-textbook.pdf#page=615) |
| 13-1: The Need for Data Analysis | [616](database-systems/database-systems-textbook.pdf#page=616) |
| 13-2: Business Intelligence | [616](database-systems/database-systems-textbook.pdf#page=616) |
| 13-3: Decision Support Data | [628](database-systems/database-systems-textbook.pdf#page=628) |
| 13-4: The Data Warehouse | [633](database-systems/database-systems-textbook.pdf#page=633) |
| 13-5: Star Schemas | [636](database-systems/database-systems-textbook.pdf#page=636) |
| 13-6: Online Analytical Processing | [647](database-systems/database-systems-textbook.pdf#page=647) |
| 13-7: SQL Extensions for OLAP | [655](database-systems/database-systems-textbook.pdf#page=655) |
| Ch 14: Big Data Analytics and NoSQL | [674](database-systems/database-systems-textbook.pdf#page=674) |
| 14-1: Big Data | [675](database-systems/database-systems-textbook.pdf#page=675) |
| 14-2: Hadoop | [681](database-systems/database-systems-textbook.pdf#page=681) |
| 14-3: NoSQL | [688](database-systems/database-systems-textbook.pdf#page=688) |
| 14-4: Data Analytics | [696](database-systems/database-systems-textbook.pdf#page=696) |
| Part 5: Databases and the Internet | [705](database-systems/database-systems-textbook.pdf#page=705) |
| Ch 15: Database Connectivity and Web Technologies | [706](database-systems/database-systems-textbook.pdf#page=706) |
| 15-1: Database Connectivity | [707](database-systems/database-systems-textbook.pdf#page=707) |
| 15-2: Database Internet Connectivity | [718](database-systems/database-systems-textbook.pdf#page=718) |
| 15-3: Extensible Markup Language (XML) | [728](database-systems/database-systems-textbook.pdf#page=728) |
| 15-4: Cloud Computing Services | [735](database-systems/database-systems-textbook.pdf#page=735) |
| Part 6: Database Administration | [747](database-systems/database-systems-textbook.pdf#page=747) |
| Ch 16: Database Administration and Security | [748](database-systems/database-systems-textbook.pdf#page=748) |
| 16-1: Data as a Corporate Asset | [749](database-systems/database-systems-textbook.pdf#page=749) |
| 16-2: The Need for a Database and its Role in an Organization | [750](database-systems/database-systems-textbook.pdf#page=750) |
| 16-3: Introduction of a Database: Special Considerations | [752](database-systems/database-systems-textbook.pdf#page=752) |
| 16-4: The Evolution of Database Administration | [753](database-systems/database-systems-textbook.pdf#page=753) |
| 16-5: The Database Environment’s Human Component | [757](database-systems/database-systems-textbook.pdf#page=757) |
| 16-6: Security | [771](database-systems/database-systems-textbook.pdf#page=771) |
| 16-7: Database Administration Tools | [775](database-systems/database-systems-textbook.pdf#page=775) |
| 16-8: Developing a Data Administration Strategy | [781](database-systems/database-systems-textbook.pdf#page=781) |
| 16-9: The DBA’s Role in the Cloud | [782](database-systems/database-systems-textbook.pdf#page=782) |
| 16-10: The DBA at Work: Using Oracle for Database Administration | [783](database-systems/database-systems-textbook.pdf#page=783) |
| Glossary | [795](database-systems/database-systems-textbook.pdf#page=795) |
| Index | [809](database-systems/database-systems-textbook.pdf#page=809) |

## system-design/

### System design interview

`system-design/system-design-interview.pdf`, 269 pages. Alex Xu, *System Design Interview: An Insider's
Guide*, second edition according to the PDF's own title (the title page names no edition or year),
2020. A published interview-preparation book: scaling a web service from one server to millions of
users, back-of-the-envelope estimation, a four-step framework for the interview, then twelve worked
designs (a rate limiter, consistent hashing, a key-value store, a unique ID generator, a URL
shortener, a web crawler, a notification system, a news feed, a chat system, search autocomplete,
YouTube and Google Drive), each ending with its reference list. Was `System Design Interview by Alex
Xu.pdf`; five byte-identical copies of it were downloaded alongside.

**Page numbers.** calibre made this PDF from the ebook, so its pages carry no printed page numbers and
do not match the print edition's pages. Every number here is a PDF page. There is no index; the table
is the PDF's own outline.

| Chapter or section | PDF page |
| --- | --- |
| System Design Interview: An Insider’s Guide | [2](system-design/system-design-interview.pdf#page=2) |
| Forward | [4](system-design/system-design-interview.pdf#page=4) |
| 1 Scale from zero to millions of users | [5](system-design/system-design-interview.pdf#page=5) |
| 2 Back-of-the-envelope estimation | [34](system-design/system-design-interview.pdf#page=34) |
| 3 A framework for system design interviews | [42](system-design/system-design-interview.pdf#page=42) |
| 4 Design a rate limiter | [51](system-design/system-design-interview.pdf#page=51) |
| 5 Design consistent hashing | [71](system-design/system-design-interview.pdf#page=71) |
| 6 Design a key-value store | [87](system-design/system-design-interview.pdf#page=87) |
| 7 Design a unique ID generator in distributed systems | [110](system-design/system-design-interview.pdf#page=110) |
| 8 Design a URL shortener | [119](system-design/system-design-interview.pdf#page=119) |
| 9 Design a web crawler | [132](system-design/system-design-interview.pdf#page=132) |
| 10 Design a notification system | [151](system-design/system-design-interview.pdf#page=151) |
| 11 Design a news feed system | [166](system-design/system-design-interview.pdf#page=166) |
| 12 Design a chat system | [178](system-design/system-design-interview.pdf#page=178) |
| 13 Design a search autocomplete system | [200](system-design/system-design-interview.pdf#page=200) |
| 14 Design YouTube | [220](system-design/system-design-interview.pdf#page=220) |
| 15 Design Google Drive | [244](system-design/system-design-interview.pdf#page=244) |
| 16 The learning continues | [264](system-design/system-design-interview.pdf#page=264) |
| Afterword | [269](system-design/system-design-interview.pdf#page=269) |
### System design big archive

`system-design/system-design-big-archive.pdf`, 442 pages, 206 MB. ByteByteGo, *Big Archive: System
Design 2025* (the PDF's own title is "2025 Archive"), assembled in Google Docs. A collection of 213
short ByteByteGo posts, most of them one or two pages built around a single diagram: protocols and
networking, APIs and authentication (JWT, OAuth, SSO), databases and caches, Kubernetes, Docker and
cloud services, messaging (RabbitMQ, SQS, SNS), how named companies built their systems, design
patterns, and AI tooling (RAG, agents, MCP). It is a reference to look a diagram up in, not a course;
a few posts appear more than once. Was `Bytebytego_Big_Archive_System_Design_2025.pdf`.

**Page numbers.** The PDF's printed contents (PDF pages 2 to 7) give PDF pages, and the posts carry no
page numbers of their own. There is no index; the table is the PDF's own outline, one row per post.

| Chapter or section | PDF page |
| --- | --- |
| The 9 Algorithms That Dominate Our World | [8](system-design/system-design-big-archive.pdf#page=8) |
| How does gRPC work? | [12](system-design/system-design-big-archive.pdf#page=12) |
| Docker vs. Kubernetes. Which one should we use? | [14](system-design/system-design-big-archive.pdf#page=14) |
| What happens when you type google .com into a browser? | [18](system-design/system-design-big-archive.pdf#page=18) |
| A Cheatsheet on Infrastructure as Code Landscape | [20](system-design/system-design-big-archive.pdf#page=20) |
| A Crash Course on Architectural Scalability | [22](system-design/system-design-big-archive.pdf#page=22) |
| The Open Source AI Stack | [24](system-design/system-design-big-archive.pdf#page=24) |
| Cookies Vs Sessions Vs JWT Vs PASETO | [26](system-design/system-design-big-archive.pdf#page=26) |
| How TikTok Manages a 200K File Frontend MonoRepo? | [28](system-design/system-design-big-archive.pdf#page=28) |
| The Ultimate API Learning Roadmap | [30](system-design/system-design-big-archive.pdf#page=30) |
| 30 Useful AI Apps That Can Help You in 2025 | [32](system-design/system-design-big-archive.pdf#page=32) |
| 10 Essential Components of a Production Web Application | [34](system-design/system-design-big-archive.pdf#page=34) |
| Session, Cookie, JWT, Token, SSO, and OAuth 2.0 Explained in One Diagram | [36](system-design/system-design-big-archive.pdf#page=36) |
| DeepSeek 1-Pager | [38](system-design/system-design-big-archive.pdf#page=38) |
| My Favorite 10 Books for Software Developers | [40](system-design/system-design-big-archive.pdf#page=40) |
| What is an AI Agent? | [42](system-design/system-design-big-archive.pdf#page=42) |
| Git vs GitHub | [44](system-design/system-design-big-archive.pdf#page=44) |
| A Cheatsheet on Database Performance | [46](system-design/system-design-big-archive.pdf#page=46) |
| 18 Common Ports Worth Knowing | [48](system-design/system-design-big-archive.pdf#page=48) |
| Generative Adversarial Network (GAN) - AI by Hand ✍️ | [50](system-design/system-design-big-archive.pdf#page=50) |
| JWT 101: Key to Stateless Authentication | [51](system-design/system-design-big-archive.pdf#page=51) |
| A handy cheat sheet for the most popular cloud services | [53](system-design/system-design-big-archive.pdf#page=53) |
| 0 to 1.5 Billion Guests: Airbnb’s Architectural Evolution | [57](system-design/system-design-big-archive.pdf#page=57) |
| 12 Algorithms for System Design Interviews | [59](system-design/system-design-big-archive.pdf#page=59) |
| How Kubernetes Works? | [61](system-design/system-design-big-archive.pdf#page=61) |
| PostgreSQL 101: The Everything Database | [63](system-design/system-design-big-archive.pdf#page=63) |
| Top 12 Tips for API Security | [65](system-design/system-design-big-archive.pdf#page=65) |
| 24 Good Resources to Learn Software Architecture in 2025 | [67](system-design/system-design-big-archive.pdf#page=67) |
| SQS vs SNS vs EventBridge vs Kinesis | [69](system-design/system-design-big-archive.pdf#page=69) |
| Top 5 common ways to improve API performance | [71](system-design/system-design-big-archive.pdf#page=71) |
| xAI’s Grok-3 One-Pager | [73](system-design/system-design-big-archive.pdf#page=73) |
| 30 Free APIs for Developers | [75](system-design/system-design-big-archive.pdf#page=75) |
| The Generative AI Learning Roadmap | [77](system-design/system-design-big-archive.pdf#page=77) |
| HTTP/1 -> HTTP/2 -> HTTP/3 | [79](system-design/system-design-big-archive.pdf#page=79) |
| Structure of URL | [81](system-design/system-design-big-archive.pdf#page=81) |
| A Cheatsheet on Comparing Key-Value Stores | [83](system-design/system-design-big-archive.pdf#page=83) |
| Which Database Should I Use on AWS? | [85](system-design/system-design-big-archive.pdf#page=85) |
| What is MCP? | [87](system-design/system-design-big-archive.pdf#page=87) |
| How to Design a System like Instagram | [89](system-design/system-design-big-archive.pdf#page=89) |
| How to load your websites at lightning speed | [91](system-design/system-design-big-archive.pdf#page=91) |
| What is SSO (Single Sign-On)? | [93](system-design/system-design-big-archive.pdf#page=93) |
| How Java Virtual Threads Work? | [95](system-design/system-design-big-archive.pdf#page=95) |
| Redis VS Memcached | [97](system-design/system-design-big-archive.pdf#page=97) |
| The Shopify Tech Stack | [98](system-design/system-design-big-archive.pdf#page=98) |
| What is Retrieval-Augmented Generation (RAG)? | [102](system-design/system-design-big-archive.pdf#page=102) |
| How Two-factor Authentication (2FA) Works? | [104](system-design/system-design-big-archive.pdf#page=104) |
| How Amazon S3 Works? | [106](system-design/system-design-big-archive.pdf#page=106) |
| How to Learn Backend Development? | [108](system-design/system-design-big-archive.pdf#page=108) |
| A Simplified Git Workflow | [110](system-design/system-design-big-archive.pdf#page=110) |
| Virtualization vs Containerization | [112](system-design/system-design-big-archive.pdf#page=112) |
| How Netflix Built a Distributed Counter? | [114](system-design/system-design-big-archive.pdf#page=114) |
| How to Learn API Development? | [116](system-design/system-design-big-archive.pdf#page=116) |
| Must-Know Network Protocol Dependencies | [118](system-design/system-design-big-archive.pdf#page=118) |
| Top AI Coding Tools for Developers You Can Use in 2025 | [120](system-design/system-design-big-archive.pdf#page=120) |
| 18 Key Design Patterns Every Developer Should Know | [122](system-design/system-design-big-archive.pdf#page=122) |
| The Data Engineering Roadmap | [124](system-design/system-design-big-archive.pdf#page=124) |
| What do version numbers mean? | [128](system-design/system-design-big-archive.pdf#page=128) |
| Everyone talks about Transformers. How Transformers Architecture Works? | [130](system-design/system-design-big-archive.pdf#page=130) |
| Top YouTube Channels and Blogs for AI Learning in 2025 | [132](system-design/system-design-big-archive.pdf#page=132) |
| Top 20 System Design Concepts You Should Know | [134](system-design/system-design-big-archive.pdf#page=134) |
| 9 OOP Design Patterns You Must Know | [139](system-design/system-design-big-archive.pdf#page=139) |
| A Cheatsheet on REST API Design Best Practices | [143](system-design/system-design-big-archive.pdf#page=143) |
| Top 30 AWS Services That Are Commonly Used | [145](system-design/system-design-big-archive.pdf#page=145) |
| The Large-Language Model Glossary | [147](system-design/system-design-big-archive.pdf#page=147) |
| 9 Clean Code Principles To Keep In Mind | [149](system-design/system-design-big-archive.pdf#page=149) |
| The 4 Types of SQL Joins | [151](system-design/system-design-big-archive.pdf#page=151) |
| How to Learn Cloud Computing? | [153](system-design/system-design-big-archive.pdf#page=153) |
| Visualizing a SQL query | [155](system-design/system-design-big-archive.pdf#page=155) |
| Explaining JSON Web Token (JWT) with simple terms | [156](system-design/system-design-big-archive.pdf#page=156) |
| 12 MCP Servers You Can Use in 2025 | [158](system-design/system-design-big-archive.pdf#page=158) |
| How to Deploy Services | [160](system-design/system-design-big-archive.pdf#page=160) |
| The System Design Topic Map | [162](system-design/system-design-big-archive.pdf#page=162) |
| How Transformers Architecture Works? | [164](system-design/system-design-big-archive.pdf#page=164) |
| JWT Simply Explained | [166](system-design/system-design-big-archive.pdf#page=166) |
| The 5 Pillars of API Design | [168](system-design/system-design-big-archive.pdf#page=168) |
| How Computer Memory Works? | [170](system-design/system-design-big-archive.pdf#page=170) |
| Top Kubernetes Scaling Strategies You Must Know | [172](system-design/system-design-big-archive.pdf#page=172) |
| AI Agent versus MCP | [174](system-design/system-design-big-archive.pdf#page=174) |
| How does HTTPS work? | [176](system-design/system-design-big-archive.pdf#page=176) |
| How to Learn Kubernetes? | [178](system-design/system-design-big-archive.pdf#page=178) |
| Top 6 most commonly used Server Types | [180](system-design/system-design-big-archive.pdf#page=180) |
| Amazon Key Architecture with Third Party Integration | [182](system-design/system-design-big-archive.pdf#page=182) |
| How Do Companies Ship Code to Production? | [184](system-design/system-design-big-archive.pdf#page=184) |
| What is Event Sourcing? How is it different from normal CRUD design? | [186](system-design/system-design-big-archive.pdf#page=186) |
| How Data Lake Architecture Works? | [188](system-design/system-design-big-archive.pdf#page=188) |
| How Netflix Built a Distributed Counter | [190](system-design/system-design-big-archive.pdf#page=190) |
| Top 20 AI Concepts You Should Know | [194](system-design/system-design-big-archive.pdf#page=194) |
| The AI Application Stack for Building RAG Apps | [196](system-design/system-design-big-archive.pdf#page=196) |
| Shopify Tech Stacks and Tools | [198](system-design/system-design-big-archive.pdf#page=198) |
| AI Vs Machine Learning Vs Deep Learning Vs Generative AI | [200](system-design/system-design-big-archive.pdf#page=200) |
| How SQL Query Executes In A Database? | [202](system-design/system-design-big-archive.pdf#page=202) |
| Top 20 AI Agent Concepts You Should Know | [204](system-design/system-design-big-archive.pdf#page=204) |
| How RabbitMQ Works? | [206](system-design/system-design-big-archive.pdf#page=206) |
| RAG vs Agentic RAG | [208](system-design/system-design-big-archive.pdf#page=208) |
| A Cheatsheet on Kubernetes | [210](system-design/system-design-big-archive.pdf#page=210) |
| 6 Data Structures to Save Storage | [212](system-design/system-design-big-archive.pdf#page=212) |
| 5 Database Normal Forms Every Developer Should Know | [214](system-design/system-design-big-archive.pdf#page=214) |
| How CQRS Works? | [218](system-design/system-design-big-archive.pdf#page=218) |
| How MongoDB Works? | [220](system-design/system-design-big-archive.pdf#page=220) |
| The Generative AI Tech Stack | [222](system-design/system-design-big-archive.pdf#page=222) |
| 24 Good Resources to Learn Software Architecture in 2025 | [224](system-design/system-design-big-archive.pdf#page=224) |
| Database Index Types Every Developer Should Know | [226](system-design/system-design-big-archive.pdf#page=226) |
| The Agentic AI Learning Roadmap | [228](system-design/system-design-big-archive.pdf#page=228) |
| 12 MCP Servers You Can Use in 2025 | [230](system-design/system-design-big-archive.pdf#page=230) |
| Top 5 common ways to improve API performance | [232](system-design/system-design-big-archive.pdf#page=232) |
| REST API Vs. GraphQL | [234](system-design/system-design-big-archive.pdf#page=234) |
| Tokens vs API Keys | [236](system-design/system-design-big-archive.pdf#page=236) |
| The AWS Tech Stack | [238](system-design/system-design-big-archive.pdf#page=238) |
| 5 Data Structures That Make DB Queries Super Fast | [240](system-design/system-design-big-archive.pdf#page=240) |
| 12 MCP Servers You Can Use in 2025 | [242](system-design/system-design-big-archive.pdf#page=242) |
| MCP Versus A2A Protocol | [244](system-design/system-design-big-archive.pdf#page=244) |
| How can Cache Systems go wrong? | [246](system-design/system-design-big-archive.pdf#page=246) |
| 8 System Design Concepts Explained in 1 Diagram | [248](system-design/system-design-big-archive.pdf#page=248) |
| 16 Coding Patterns That Make Interviews Easy | [250](system-design/system-design-big-archive.pdf#page=250) |
| How to Learn Databases? | [252](system-design/system-design-big-archive.pdf#page=252) |
| What happens when you type a URL into a browser? | [254](system-design/system-design-big-archive.pdf#page=254) |
| How HTTPS Works? | [256](system-design/system-design-big-archive.pdf#page=256) |
| The Evolution of Scaling at Netflix | [258](system-design/system-design-big-archive.pdf#page=258) |
| What is the SOLID Principle? | [260](system-design/system-design-big-archive.pdf#page=260) |
| Common HTTP Status Codes | [262](system-design/system-design-big-archive.pdf#page=262) |
| How Clean Architecture Works? | [264](system-design/system-design-big-archive.pdf#page=264) |
| How does Docker Work? | [265](system-design/system-design-big-archive.pdf#page=265) |
| How Large Language Models Work? | [266](system-design/system-design-big-archive.pdf#page=266) |
| How Does SSO Work? | [268](system-design/system-design-big-archive.pdf#page=268) |
| Best Practices in API Design | [270](system-design/system-design-big-archive.pdf#page=270) |
| Key Terms in Domain-Driven Design | [272](system-design/system-design-big-archive.pdf#page=272) |
| Top AI Agent Frameworks You Should Know | [274](system-design/system-design-big-archive.pdf#page=274) |
| How OpenAI’s GPT-OSS 120B and 20B Models Work? | [276](system-design/system-design-big-archive.pdf#page=276) |
| The Modern Software Stack | [278](system-design/system-design-big-archive.pdf#page=278) |
| Concurrency is NOT Parallelism | [280](system-design/system-design-big-archive.pdf#page=280) |
| JWT vs PASETO: The Two Players of Token-Based Authentication | [282](system-design/system-design-big-archive.pdf#page=282) |
| The Linux Cron Cheatsheet | [284](system-design/system-design-big-archive.pdf#page=284) |
| AI Agent versus MCP | [286](system-design/system-design-big-archive.pdf#page=286) |
| The Lifecycle of a Kubernetes Pod | [288](system-design/system-design-big-archive.pdf#page=288) |
| CI/CD Pipeline Explained | [290](system-design/system-design-big-archive.pdf#page=290) |
| The Open Source RAG Stack | [291](system-design/system-design-big-archive.pdf#page=291) |
| What are some of the most popular versioning strategies? | [293](system-design/system-design-big-archive.pdf#page=293) |
| The Testing Pyramid | [294](system-design/system-design-big-archive.pdf#page=294) |
| 9 Docker Best Practices You Should Know | [295](system-design/system-design-big-archive.pdf#page=295) |
| Kubernetes Explained | [297](system-design/system-design-big-archive.pdf#page=297) |
| N8N versus LangGraph | [299](system-design/system-design-big-archive.pdf#page=299) |
| Where Do We Cache Data? | [301](system-design/system-design-big-archive.pdf#page=301) |
| Python vs Java | [303](system-design/system-design-big-archive.pdf#page=303) |
| Design Patterns Cheat Sheet | [305](system-design/system-design-big-archive.pdf#page=305) |
| CI/CD Simplified Visual Guide | [308](system-design/system-design-big-archive.pdf#page=308) |
| How Apache Kafka Works? | [310](system-design/system-design-big-archive.pdf#page=310) |
| Load Balancers vs API Gateways vs Reverse Proxy! And how can they Work Together? | [312](system-design/system-design-big-archive.pdf#page=312) |
| How Java Works | [314](system-design/system-design-big-archive.pdf#page=314) |
| How Gitflow Branching Works? | [316](system-design/system-design-big-archive.pdf#page=316) |
| The Life of a Redis Query | [318](system-design/system-design-big-archive.pdf#page=318) |
| 6 Steps to Create a New AI Model | [320](system-design/system-design-big-archive.pdf#page=320) |
| Cookies vs Sessions | [322](system-design/system-design-big-archive.pdf#page=322) |
| Access Control Clearly Explained | [324](system-design/system-design-big-archive.pdf#page=324) |
| Full Fine-Tuning vs LoRA vs RAG | [326](system-design/system-design-big-archive.pdf#page=326) |
| How Git Reset Works? | [328](system-design/system-design-big-archive.pdf#page=328) |
| Apache Kafka Explained (At the high level) | [330](system-design/system-design-big-archive.pdf#page=330) |
| MCP vs API: what’s the difference? | [332](system-design/system-design-big-archive.pdf#page=332) |
| TCP vs UDP | [334](system-design/system-design-big-archive.pdf#page=334) |
| A piece of knowledge each day: AI and Machine Learning (ML) | [335](system-design/system-design-big-archive.pdf#page=335) |
| How Python Works | [337](system-design/system-design-big-archive.pdf#page=337) |
| API Vs SDK! | [339](system-design/system-design-big-archive.pdf#page=339) |
| SQL Injection (SQLi) | [341](system-design/system-design-big-archive.pdf#page=341) |
| Types of AI Agents | [343](system-design/system-design-big-archive.pdf#page=343) |
| 24 Good Resources to Learn Software Architecture in 2025 | [345](system-design/system-design-big-archive.pdf#page=345) |
| Cross-Site Scripting (XSS) Attacks | [347](system-design/system-design-big-archive.pdf#page=347) |
| Docker vs Kubernetes | [349](system-design/system-design-big-archive.pdf#page=349) |
| Batch vs Stream Processing | [351](system-design/system-design-big-archive.pdf#page=351) |
| What are Modular Monoliths? | [353](system-design/system-design-big-archive.pdf#page=353) |
| Popular interview question: What is the difference between Process and Thread? | [355](system-design/system-design-big-archive.pdf#page=355) |
| How AI Agents Chain Tools, Memory, and Reasoning? | [356](system-design/system-design-big-archive.pdf#page=356) |
| Latency vs. Throughput | [358](system-design/system-design-big-archive.pdf#page=358) |
| Top 20 System Design Concepts You Should Know | [360](system-design/system-design-big-archive.pdf#page=360) |
| How to Debug a Slow API? | [362](system-design/system-design-big-archive.pdf#page=362) |
| How LLMs See the World | [364](system-design/system-design-big-archive.pdf#page=364) |
| RAG vs Fine-tuning: Which one should you use? | [366](system-design/system-design-big-archive.pdf#page=366) |
| IP Address Cheat Sheet Every Engineer Should Know | [369](system-design/system-design-big-archive.pdf#page=369) |
| Which Protocols Run on TCP and UDP | [371](system-design/system-design-big-archive.pdf#page=371) |
| Why is DeepSeek-OCR such a BIG DEAL? | [373](system-design/system-design-big-archive.pdf#page=373) |
| Servers You Should Know in Modern Systems | [375](system-design/system-design-big-archive.pdf#page=375) |
| The Building Blocks of Modern Networking | [376](system-design/system-design-big-archive.pdf#page=376) |
| Network Services That Power Modern Connectivity | [378](system-design/system-design-big-archive.pdf#page=378) |
| How to Design Good APIs | [380](system-design/system-design-big-archive.pdf#page=380) |
| Big Data Pipeline Cheatsheet for AWS, Azure, and Google Cloud | [382](system-design/system-design-big-archive.pdf#page=382) |
| How to Learn AWS? | [384](system-design/system-design-big-archive.pdf#page=384) |
| The AI Agent Tech Stack | [386](system-design/system-design-big-archive.pdf#page=386) |
| How to Build a Basic RAG Application on AWS? | [388](system-design/system-design-big-archive.pdf#page=388) |
| Types of Virtualization | [390](system-design/system-design-big-archive.pdf#page=390) |
| Cloudflare vs. AWS vs. Azure | [392](system-design/system-design-big-archive.pdf#page=392) |
| Popular Backend Tech Stack | [394](system-design/system-design-big-archive.pdf#page=394) |
| HTTP vs. HTTPS | [395](system-design/system-design-big-archive.pdf#page=395) |
| Forward Proxy versus Reverse Proxy | [397](system-design/system-design-big-archive.pdf#page=397) |
| Things Every Developer Should Know: Concurrency is NOT parallelism | [399](system-design/system-design-big-archive.pdf#page=399) |
| Virtualization vs. Containerization | [401](system-design/system-design-big-archive.pdf#page=401) |
| 5 REST API Authentication Methods | [403](system-design/system-design-big-archive.pdf#page=403) |
| How do AirTags work? | [405](system-design/system-design-big-archive.pdf#page=405) |
| What is a Firewall? | [407](system-design/system-design-big-archive.pdf#page=407) |
| Modem vs. Router | [409](system-design/system-design-big-archive.pdf#page=409) |
| What is a REST API? | [411](system-design/system-design-big-archive.pdf#page=411) |
| How Java HashMaps Work? | [413](system-design/system-design-big-archive.pdf#page=413) |
| Virtualization Explained: From Bare Metal to Hosted Hypervisors | [415](system-design/system-design-big-archive.pdf#page=415) |
| Database Types You Should Know in 2025 | [417](system-design/system-design-big-archive.pdf#page=417) |
| Apache Kafka vs. RabbitMQ | [419](system-design/system-design-big-archive.pdf#page=419) |
| The HTTP Mindmap | [421](system-design/system-design-big-archive.pdf#page=421) |
| How DNS Works | [423](system-design/system-design-big-archive.pdf#page=423) |
| Can a web server provide real-time updates? | [425](system-design/system-design-big-archive.pdf#page=425) |
| Evolution of HTTP | [427](system-design/system-design-big-archive.pdf#page=427) |
| System Performance Metrics Every Engineer Should Know | [429](system-design/system-design-big-archive.pdf#page=429) |
| Why Is Nginx So Popular? | [431](system-design/system-design-big-archive.pdf#page=431) |
| Network Debugging Commands Every Engineer Should Know | [433](system-design/system-design-big-archive.pdf#page=433) |
| Hub, Switch, & Router Explained | [435](system-design/system-design-big-archive.pdf#page=435) |
| Common Network Protocols Every Engineer Should Know | [437](system-design/system-design-big-archive.pdf#page=437) |
| 8 Popular Network Protocols | [439](system-design/system-design-big-archive.pdf#page=439) |
| A picture is worth a thousand words: 9 best practices for developing microservices | [441](system-design/system-design-big-archive.pdf#page=441) |
### Grokking the system design interview

`system-design/grokking-the-system-design-interview.pdf`, 25 pages. Junfan Zhu's study notes on
Educative's *Grokking the System Design Interview* course, dated 2021-04-12. This is not the course: it
is a 25-page excerpt and summary of it, typeset in LaTeX, covering a handful of the course's design
problems (URL shortening, Dropbox, Messenger, YouTube, typeahead, a rate limiter, a web crawler, the
Facebook news feed, Yelp, Ticketmaster) and its glossary of system design basics (load balancing,
caching, data partitioning, proxies, SQL and NoSQL, the CAP theorem, consistent hashing). Was `Grokking
the System Design Interview.pdf`.

**Page numbers.** The printed page number equals the PDF page number. There is no index; the table is
the PDF's own outline, topics and their sections.

| Chapter or section | PDF page |
| --- | --- |
| Course Links | [1](system-design/grokking-the-system-design-interview.pdf#page=1) |
| 1. Back-of-the-envelope estimation | [2](system-design/grokking-the-system-design-interview.pdf#page=2) |
| 2. Shortening URL | [3](system-design/grokking-the-system-design-interview.pdf#page=3) |
| 2.1. Encoding actual URL | [3](system-design/grokking-the-system-design-interview.pdf#page=3) |
| 2.2. Cache | [3](system-design/grokking-the-system-design-interview.pdf#page=3) |
| 2.3. Load Balancer (LB) | [3](system-design/grokking-the-system-design-interview.pdf#page=3) |
| 3. DropBox | [3](system-design/grokking-the-system-design-interview.pdf#page=3) |
| 3.1. Clarify Requirements and Goals of the System | [3](system-design/grokking-the-system-design-interview.pdf#page=3) |
| 4. Facebook Messenger | [4](system-design/grokking-the-system-design-interview.pdf#page=4) |
| 4.1. Message Handling | [4](system-design/grokking-the-system-design-interview.pdf#page=4) |
| 4.2. Storing and retrieving the messages from the database | [4](system-design/grokking-the-system-design-interview.pdf#page=4) |
| 5. YouTube | [5](system-design/grokking-the-system-design-interview.pdf#page=5) |
| 5.1. Metadata Sharding | [5](system-design/grokking-the-system-design-interview.pdf#page=5) |
| 5.2. Load Balancing | [6](system-design/grokking-the-system-design-interview.pdf#page=6) |
| 6. Designing Typeahead Suggestion | [7](system-design/grokking-the-system-design-interview.pdf#page=7) |
| 7. API Rate Limiter | [7](system-design/grokking-the-system-design-interview.pdf#page=7) |
| 8. Web Crawler | [8](system-design/grokking-the-system-design-interview.pdf#page=8) |
| 8.1. How to crawl? | [8](system-design/grokking-the-system-design-interview.pdf#page=8) |
| 8.2. Component Design | [8](system-design/grokking-the-system-design-interview.pdf#page=8) |
| 9. Facebook's Newsfeed | [9](system-design/grokking-the-system-design-interview.pdf#page=9) |
| 9.1. Feed generation | [9](system-design/grokking-the-system-design-interview.pdf#page=9) |
| 9.2. Feed publishing | [10](system-design/grokking-the-system-design-interview.pdf#page=10) |
| 9.3. Data Partitioning | [11](system-design/grokking-the-system-design-interview.pdf#page=11) |
| 10. Yelp | [11](system-design/grokking-the-system-design-interview.pdf#page=11) |
| 10.1. Dynamic size grids | [11](system-design/grokking-the-system-design-interview.pdf#page=11) |
| 11. Ticket Master | [12](system-design/grokking-the-system-design-interview.pdf#page=12) |
| 11.1. Active Reservations Service | [12](system-design/grokking-the-system-design-interview.pdf#page=12) |
| 11.2. Waiting Users Service | [12](system-design/grokking-the-system-design-interview.pdf#page=12) |
| 11.3. Concurrency | [13](system-design/grokking-the-system-design-interview.pdf#page=13) |
| 12. Load Balancing | [14](system-design/grokking-the-system-design-interview.pdf#page=14) |
| 12.1. Benefits | [14](system-design/grokking-the-system-design-interview.pdf#page=14) |
| 12.2. Algorithms | [14](system-design/grokking-the-system-design-interview.pdf#page=14) |
| 13. Caching | [15](system-design/grokking-the-system-design-interview.pdf#page=15) |
| 13.1. Cache Invalidation | [15](system-design/grokking-the-system-design-interview.pdf#page=15) |
| 13.2. Cache eviction policies | [16](system-design/grokking-the-system-design-interview.pdf#page=16) |
| 14. Data Partitioning | [16](system-design/grokking-the-system-design-interview.pdf#page=16) |
| 14.1. Partitioning Criteria | [16](system-design/grokking-the-system-design-interview.pdf#page=16) |
| 14.2. Common Problems of Data Partitioning | [17](system-design/grokking-the-system-design-interview.pdf#page=17) |
| 15. Proxy Server | [18](system-design/grokking-the-system-design-interview.pdf#page=18) |
| 15.1. Open Proxy | [18](system-design/grokking-the-system-design-interview.pdf#page=18) |
| 15.2. Reverse Proxy | [19](system-design/grokking-the-system-design-interview.pdf#page=19) |
| 16. SQL & NoSQL | [19](system-design/grokking-the-system-design-interview.pdf#page=19) |
| 16.1. SQL | [19](system-design/grokking-the-system-design-interview.pdf#page=19) |
| 16.2. NoSQL | [19](system-design/grokking-the-system-design-interview.pdf#page=19) |
| 16.3. Differences: SQL vs. NoSQL | [19](system-design/grokking-the-system-design-interview.pdf#page=19) |
| 16.4. Choose which? | [21](system-design/grokking-the-system-design-interview.pdf#page=21) |
| 17. CAP Theorem | [22](system-design/grokking-the-system-design-interview.pdf#page=22) |
| 18. Consistent Hashing | [22](system-design/grokking-the-system-design-interview.pdf#page=22) |
| 18.1. Improve caching system | [22](system-design/grokking-the-system-design-interview.pdf#page=22) |
| 18.2. Consistent Hashing | [24](system-design/grokking-the-system-design-interview.pdf#page=24) |
| 18.3. Algorithm | [24](system-design/grokking-the-system-design-interview.pdf#page=24) |
### Systems analysis and design

`system-design/systems-analysis-and-design.pdf`, 594 pages. Alan Dennis, Barbara Haley Wixom and
Roberta M. Roth, *Systems Analysis and Design*, fifth edition, John Wiley & Sons, 2012. A published
university textbook on the systems development life cycle: planning (the systems analyst's role,
project selection and management), analysis (requirements determination, use cases, process modelling
with data flow diagrams, data modelling with entity relationship diagrams), design (architecture, user
interface, program and data storage design) and implementation (testing, and converting to the new
system), ending with object-oriented analysis and design in UML. Was
`Systemanalysisanddesign.pdf`.

**Page numbers.** The printed page number is the PDF page minus 26 (printed page 5, where chapter 1
starts, is PDF page 31); the PDF's embedded page labels say the same. The front matter is numbered in
roman. The table is the PDF's own outline, parts and chapters.

**Its index.** PDF pages 573 to 589, with printed page numbers.

| Chapter or section | PDF page |
| --- | --- |
| Copyright | [6](system-design/systems-analysis-and-design.pdf#page=6) |
| Preface | [9](system-design/systems-analysis-and-design.pdf#page=9) |
| Brief Contents | [17](system-design/systems-analysis-and-design.pdf#page=17) |
| Contents | [19](system-design/systems-analysis-and-design.pdf#page=19) |
| Part One: Planning phase | [29](system-design/systems-analysis-and-design.pdf#page=29) |
| 1 The systems analyst and information systems development | [31](system-design/systems-analysis-and-design.pdf#page=31) |
| 2 Project selection and management | [71](system-design/systems-analysis-and-design.pdf#page=71) |
| Part Two: Analysis phase | [125](system-design/systems-analysis-and-design.pdf#page=125) |
| 3 Requirements determination | [127](system-design/systems-analysis-and-design.pdf#page=127) |
| 4 Use case analysis | [173](system-design/systems-analysis-and-design.pdf#page=173) |
| 5 Process modeling | [209](system-design/systems-analysis-and-design.pdf#page=209) |
| 6 Data modeling | [249](system-design/systems-analysis-and-design.pdf#page=249) |
| Part Three: Design phase | [283](system-design/systems-analysis-and-design.pdf#page=283) |
| 7 Moving into design | [285](system-design/systems-analysis-and-design.pdf#page=285) |
| 8 Architecture design | [307](system-design/systems-analysis-and-design.pdf#page=307) |
| 9 User interface design | [339](system-design/systems-analysis-and-design.pdf#page=339) |
| 10 Program design | [391](system-design/systems-analysis-and-design.pdf#page=391) |
| 11 Data storage design | [431](system-design/systems-analysis-and-design.pdf#page=431) |
| Part Four: Implementation phase | [469](system-design/systems-analysis-and-design.pdf#page=469) |
| 12 Moving into implementation | [471](system-design/systems-analysis-and-design.pdf#page=471) |
| 13 Transition to the new system | [497](system-design/systems-analysis-and-design.pdf#page=497) |
| 14 The movement to objects | [529](system-design/systems-analysis-and-design.pdf#page=529) |
| Index | [573](system-design/systems-analysis-and-design.pdf#page=573) |

### Computer networking: a top-down approach

`system-design/computer-networking-a-top-down-approach.pdf`, 867 pages. James F. Kurose and Keith W.
Ross, *Computer Networking: A Top-Down Approach*, seventh edition, Global Edition (ISBN 9781292153605),
Pearson, 2017. The standard networking course textbook, taught from the top of the stack down: the
application layer (HTTP, DNS, CDNs, sockets), the transport layer (UDP, reliable transfer, TCP and
congestion control), the network layer's data plane (routers, IPv4 addressing and subnets, NAT, DHCP,
IPv6) and control plane (routing algorithms, OSPF, BGP, SDN, ICMP), the link layer (Ethernet, ARP,
switches, VLANs, data center networks), wireless and mobile networks, network security (cryptography,
TLS, IPsec and VPNs, firewalls) and multimedia networking. Each chapter ends with homework problems and
a Wireshark lab. Section 6.7 follows one web page request through every layer.

**Page numbers.** The printed page number is the PDF page minus 2 (printed page 29, where chapter 1
starts, is PDF page 31). The back-of-book index runs from PDF page 813 to 854 and gives printed pages,
so add 2 to an index page to open it. The table is the PDF's own outline, chapters and their sections,
without the end-of-chapter problems, labs and interviews.

| Chapter or section | PDF page |
| --- | --- |
| Cover | [1](system-design/computer-networking-a-top-down-approach.pdf#page=1) |
| Title Page | [3](system-design/computer-networking-a-top-down-approach.pdf#page=3) |
| Copyright Page | [4](system-design/computer-networking-a-top-down-approach.pdf#page=4) |
| About the Authors | [5](system-design/computer-networking-a-top-down-approach.pdf#page=5) |
| Preface | [9](system-design/computer-networking-a-top-down-approach.pdf#page=9) |
| Contents | [21](system-design/computer-networking-a-top-down-approach.pdf#page=21) |
| Chapter 1: Computer Networks and the Internet | [31](system-design/computer-networking-a-top-down-approach.pdf#page=31) |
| 1.1. What Is the Internet? | [32](system-design/computer-networking-a-top-down-approach.pdf#page=32) |
| 1.2. The Network Edge | [39](system-design/computer-networking-a-top-down-approach.pdf#page=39) |
| 1.3. The Network Core | [51](system-design/computer-networking-a-top-down-approach.pdf#page=51) |
| 1.4. Delay, Loss, and Throughput in Packet-Switched Networks | [65](system-design/computer-networking-a-top-down-approach.pdf#page=65) |
| 1.5. Protocol Layers and Their Service Models | [77](system-design/computer-networking-a-top-down-approach.pdf#page=77) |
| 1.6. Networks Under Attack | [85](system-design/computer-networking-a-top-down-approach.pdf#page=85) |
| 1.7. History of Computer Networking and the Internet | [89](system-design/computer-networking-a-top-down-approach.pdf#page=89) |
| 1.8. Summary | [95](system-design/computer-networking-a-top-down-approach.pdf#page=95) |
| Chapter 2: Application Layer | [113](system-design/computer-networking-a-top-down-approach.pdf#page=113) |
| 2.1. Principles of Network Applications | [114](system-design/computer-networking-a-top-down-approach.pdf#page=114) |
| 2.2. The Web and HTTP | [128](system-design/computer-networking-a-top-down-approach.pdf#page=128) |
| 2.3. Electronic Mail in the Internet | [146](system-design/computer-networking-a-top-down-approach.pdf#page=146) |
| 2.4. DNS The Internet’s Directory Service | [156](system-design/computer-networking-a-top-down-approach.pdf#page=156) |
| 2.5. Peer-to-Peer Applications | [170](system-design/computer-networking-a-top-down-approach.pdf#page=170) |
| 2.6. Video Streaming and Content Distribution Networks | [177](system-design/computer-networking-a-top-down-approach.pdf#page=177) |
| 2.7. Socket Programming: Creating Network Applications | [187](system-design/computer-networking-a-top-down-approach.pdf#page=187) |
| 2.8. Summary | [200](system-design/computer-networking-a-top-down-approach.pdf#page=200) |
| Chapter 3: Transport Layer | [217](system-design/computer-networking-a-top-down-approach.pdf#page=217) |
| 3.1. Introduction and Transport-Layer Services | [218](system-design/computer-networking-a-top-down-approach.pdf#page=218) |
| 3.2. Multiplexing and Demultiplexing | [223](system-design/computer-networking-a-top-down-approach.pdf#page=223) |
| 3.3. Connectionless Transport: UDP | [230](system-design/computer-networking-a-top-down-approach.pdf#page=230) |
| 3.4. Principles of Reliable Data Transfer | [236](system-design/computer-networking-a-top-down-approach.pdf#page=236) |
| 3.5. Connection-Oriented Transport: TCP | [263](system-design/computer-networking-a-top-down-approach.pdf#page=263) |
| 3.6. Principles of Congestion Control | [291](system-design/computer-networking-a-top-down-approach.pdf#page=291) |
| 3.7. TCP Congestion Control | [299](system-design/computer-networking-a-top-down-approach.pdf#page=299) |
| 3.8. Summary | [314](system-design/computer-networking-a-top-down-approach.pdf#page=314) |
| Chapter 4: The Network Layer: Data Plane | [335](system-design/computer-networking-a-top-down-approach.pdf#page=335) |
| 4.1. Overview of Network Layer | [336](system-design/computer-networking-a-top-down-approach.pdf#page=336) |
| 4.2. What’s Inside a Router? | [343](system-design/computer-networking-a-top-down-approach.pdf#page=343) |
| 4.3. The Internet Protocol (IP): IPv4, Addressing, IPv6, and More | [359](system-design/computer-networking-a-top-down-approach.pdf#page=359) |
| 4.4. Generalized Forwarding and SDN | [384](system-design/computer-networking-a-top-down-approach.pdf#page=384) |
| 4.5. Summary | [391](system-design/computer-networking-a-top-down-approach.pdf#page=391) |
| Chapter 5: The Network Layer: Control Plane | [403](system-design/computer-networking-a-top-down-approach.pdf#page=403) |
| 5.1. Introduction | [404](system-design/computer-networking-a-top-down-approach.pdf#page=404) |
| 5.2. Routing Algorithms | [406](system-design/computer-networking-a-top-down-approach.pdf#page=406) |
| 5.3. Intra-AS Routing in the Internet: OSPF | [421](system-design/computer-networking-a-top-down-approach.pdf#page=421) |
| 5.4. Routing Among the ISPs: BGP | [425](system-design/computer-networking-a-top-down-approach.pdf#page=425) |
| 5.5. The SDN Control Plane | [437](system-design/computer-networking-a-top-down-approach.pdf#page=437) |
| 5.6. ICMP: The Internet Control Message Protocol | [449](system-design/computer-networking-a-top-down-approach.pdf#page=449) |
| 5.7. Network Management and SNMP | [451](system-design/computer-networking-a-top-down-approach.pdf#page=451) |
| 5.8. Summary | [456](system-design/computer-networking-a-top-down-approach.pdf#page=456) |
| Chapter 6: The Link Layer and LANs | [469](system-design/computer-networking-a-top-down-approach.pdf#page=469) |
| 6.1. Introduction to the Link Layer | [470](system-design/computer-networking-a-top-down-approach.pdf#page=470) |
| 6.2. Error-Detection and -Correction Techniques | [474](system-design/computer-networking-a-top-down-approach.pdf#page=474) |
| 6.3. Multiple Access Links and Protocols | [481](system-design/computer-networking-a-top-down-approach.pdf#page=481) |
| 6.4. Switched Local Area Networks | [497](system-design/computer-networking-a-top-down-approach.pdf#page=497) |
| 6.5. Link Virtualization: A Network as a Link Layer | [521](system-design/computer-networking-a-top-down-approach.pdf#page=521) |
| 6.6. Data Center Networking | [525](system-design/computer-networking-a-top-down-approach.pdf#page=525) |
| 6.7. Retrospective: A Day in the Life of a Web Page Request | [530](system-design/computer-networking-a-top-down-approach.pdf#page=530) |
| 6.8. Summary | [536](system-design/computer-networking-a-top-down-approach.pdf#page=536) |
| Chapter 7: Wireless and Mobile Networks | [549](system-design/computer-networking-a-top-down-approach.pdf#page=549) |
| 7.1. Introduction | [550](system-design/computer-networking-a-top-down-approach.pdf#page=550) |
| 7.2. Wireless Links and Network Characteristics | [555](system-design/computer-networking-a-top-down-approach.pdf#page=555) |
| 7.3. WiFi: 802.11 Wireless LANs | [562](system-design/computer-networking-a-top-down-approach.pdf#page=562) |
| 7.4. Cellular Internet Access | [581](system-design/computer-networking-a-top-down-approach.pdf#page=581) |
| 7.5. Mobility Management: Principles | [590](system-design/computer-networking-a-top-down-approach.pdf#page=590) |
| 7.6. Mobile IP | [600](system-design/computer-networking-a-top-down-approach.pdf#page=600) |
| 7.7. Managing Mobility in Cellular Networks | [604](system-design/computer-networking-a-top-down-approach.pdf#page=604) |
| 7.8. Wireless and Mobility: Impact on Higher-Layer Protocols | [610](system-design/computer-networking-a-top-down-approach.pdf#page=610) |
| 7.9. Summary | [612](system-design/computer-networking-a-top-down-approach.pdf#page=612) |
| Chapter 8: Security in Computer Networks | [623](system-design/computer-networking-a-top-down-approach.pdf#page=623) |
| 8.1. What Is Network Security? | [624](system-design/computer-networking-a-top-down-approach.pdf#page=624) |
| 8.2. Principles of Cryptography | [626](system-design/computer-networking-a-top-down-approach.pdf#page=626) |
| 8.3. Message Integrity and Digital Signatures | [640](system-design/computer-networking-a-top-down-approach.pdf#page=640) |
| 8.4. End-Point Authentication | [651](system-design/computer-networking-a-top-down-approach.pdf#page=651) |
| 8.5. Securing E-Mail | [656](system-design/computer-networking-a-top-down-approach.pdf#page=656) |
| 8.6. Securing TCP Connections: SSL | [661](system-design/computer-networking-a-top-down-approach.pdf#page=661) |
| 8.7. Network-Layer Security: IPsec and Virtual Private Networks | [667](system-design/computer-networking-a-top-down-approach.pdf#page=667) |
| 8.8. Securing Wireless LANs | [676](system-design/computer-networking-a-top-down-approach.pdf#page=676) |
| 8.9. Operational Security: Firewalls and Intrusion Detection Systems | [681](system-design/computer-networking-a-top-down-approach.pdf#page=681) |
| 8.10. Summary | [692](system-design/computer-networking-a-top-down-approach.pdf#page=692) |
| Chapter 9: Multimedia Networking | [705](system-design/computer-networking-a-top-down-approach.pdf#page=705) |
| 9.1. Multimedia Networking Applications | [706](system-design/computer-networking-a-top-down-approach.pdf#page=706) |
| 9.2. Streaming Stored Video | [711](system-design/computer-networking-a-top-down-approach.pdf#page=711) |
| 9.3. Voice-over-IP | [718](system-design/computer-networking-a-top-down-approach.pdf#page=718) |
| 9.4. Protocols for Real-Time Conversational Applications | [730](system-design/computer-networking-a-top-down-approach.pdf#page=730) |
| 9.5. Network Support for Multimedia | [739](system-design/computer-networking-a-top-down-approach.pdf#page=739) |
| 9.6. Summary | [756](system-design/computer-networking-a-top-down-approach.pdf#page=756) |
| References | [771](system-design/computer-networking-a-top-down-approach.pdf#page=771) |
| Index | [813](system-design/computer-networking-a-top-down-approach.pdf#page=813) |
| Back Cover | [867](system-design/computer-networking-a-top-down-approach.pdf#page=867) |
