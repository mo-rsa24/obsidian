# Worked Examples

Built to: QUIZ_PREP_FORMAT v1

The reference shelf for the moment a concept needs practice: problems from the learner's books and tutorials that define a use case on one technique, from the easiest that shows the mechanic to the hardest that bites. Each section below holds one table for one concept, with where each problem is, how hard it is, and whether a full-steps solution exists. It sits beside the [[Textbooks]] shelf, which holds the books these rows open at a page, and the [[Video Lessons]] shelf, and belongs to the [[Mathematics]] map.

## How a table is kept here

**This note holds the source.** The text between the two comment lines of a section is the one copy that is edited. The notes that teach the concept carry the same block right after the passage that teaches it, so the problems are one click away in the work and one note away for browsing.

**The revision number goes up by one each time a table changes.** A copy never differs from its source: when a row changes here, every copy is replaced with the new block.

**Page numbers are PDF pages**, counted from the first page of the file, as the [[Textbooks]] shelf explains. A printed page number is the PDF page minus the book's offset (16 for Chan).

**A solution cell says one of three things.** A solution in the book or tutorial, with the page. A partial one, with what is missing. Or "none: to be written", which means the problem is real and a solution still has to be written to the full-steps standard before a quiz question uses it.

## Contents

- [[#Sampling from a distribution by the inverse CDF]]
- [[#Resampling (the bootstrap) to measure the spread of a statistic]]
- [[#The forward process, from one step to one jump]]
- [[#The noise is the score, the sampled-noise identity]]
- [[#The squared-error optimum is the conditional mean]]
- [[#The noise a network learns, the marginal identity]]
- [[#The denoising loss]]
- [[#Mean and variance of a scaled sum of independent Gaussians (the forward draw)]]
- [[#The score of a Gaussian]]
- [[#Least-squares regression and the best guess under squared error]]
- [[#Solving with logs and exponents]]
- [[#The chain rule and partial derivatives]]
- [[#Completing the square and the Gaussian density by hand]]
- [[#The mean and variance of one variable, scaled, shifted and summed]]
- [[#Bayes' rule and the law of total probability]]
- [[#The derivative of a log, and the slope of a log density]]
- [[#The moment generating function]]

## Sampling from a distribution by the inverse CDF

<!-- worked-examples-table: inverse-cdf-sampling rev=2 -->
Problems on turning uniform draws into samples by inverting a CDF, from the easiest to the hardest:

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | Turn uniform draws into exponential draws: solve F(x) = 1 − e^(−λx) for x, giving x = −(1/λ) ln(1 − u) | Worked example, with a Python listing | [[introduction-to-probability-for-data-science.pdf#page=248\|Chan, Example 4.31, PDF p. 248]] | Easy | In the book, PDF pp. 248 to 249: the CDF, the inverse, the histograms and the NumPy line | none: serves the product-of-experts sampling quiz |
| 2 | The same exponential with rate 2, then the two-sensor Gaussian posterior through the normal quantile function, on ten fixed uniforms, with a ten-row table to check against | Tutorial | [the sampling tutorial, Example 2](/Users/molefemolefe/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/13-drawing-samples-by-hand.md#worked-examples) | Easy | In the tutorial: five numbered steps, the ten-row table and a checking script, `verify_s13.py`, in the same folder | none: serves the product-of-experts sampling quiz |
| 3 | Draw the integers 1 to 4 with probabilities 0.1, 0.5, 0.3, 0.1: the CDF has jumps and no inverse, so the draw is read off which interval of [0, 1] the uniform falls in | Worked example, with a Python listing | [[introduction-to-probability-for-data-science.pdf#page=249\|Chan, Example 4.32, PDF pp. 249 to 251]] | Medium | In the book, PDF pp. 249 to 251: the interval table, the mapping figure and the `np.logical_and` code | none: serves the product-of-experts sampling quiz |
| 4 | Show that y = h⁻¹(z) has density p(y) when z is uniform on (0, 1) and h is the integral of p, which is why the method works | Exercise without one | [[pattern-recognition-and-machine-learning.pdf#page=572\|Bishop, Exercise 11.2, PDF p. 572]] | Medium | none: to be written. The setup is the text on PDF p. 542 (equations 11.5 and 11.6) | none: serves the product-of-experts sampling quiz |
| 5 | Find the transformation that makes a uniform variable Cauchy with density 1/(π(1 + y²)), and then check that y = b tan z + c is Cauchy | Exercise without one | [[pattern-recognition-and-machine-learning.pdf#page=572\|Bishop, Exercises 11.3 and 11.7, PDF p. 572]] | Medium | none: to be written. The Cauchy density is equation 11.8 on PDF p. 543 | none: serves the product-of-experts sampling quiz |
| 6 | A variable on [0, 1] has CDF x^α. Find the CDF of Y = −ln X, which is exponential with rate α, and with α = 1 is the exponential sampler run from a uniform | Exercise without one | [[introduction-to-probability-for-data-science.pdf#page=255\|Chan, Exercise 14, PDF pp. 255 to 256]] | Medium | none: to be written | none: serves the product-of-experts sampling quiz |
| 7 | A variable has density 2x e^(−x²) for x ≥ 0 (a Rayleigh density). Find the density of Y = 1 − e^(−X²), which is F(X) and comes out uniform. Reading the map backwards gives the Rayleigh sampler x = √(−ln(1 − u)) | Exercise without one | [[introduction-to-probability-for-data-science.pdf#page=255\|Chan, Exercise 10, PDF p. 255]] | Medium | none: to be written. The exercise stops at the density of Y; the sampler is the step to add | none: serves the product-of-experts sampling quiz |
| 8 | Sample from the piecewise exponential density q(z) = k_i λ_i exp(−λ_i (z − z_(i−1))) on z_(i−1) < z ≤ z_i: choose a piece by its mass, then invert the exponential inside it | Exercise without one | [[pattern-recognition-and-machine-learning.pdf#page=572\|Bishop, Exercise 11.9, PDF p. 572]] | Hard | none: to be written. The density is equation 11.17 on PDF p. 547; Exercise 11.8 on the same page gives the coefficients k_i | none: serves the product-of-experts sampling quiz |

No row asks the reader to write a sampler as a programming exercise: the books give code listings (rows 1 and 3) and the tutorial gives a checking script (row 2), and the exercises ask for derivations. No row inverts a CDF that has no closed form by a numerical search; the tutorial names that case in one line without working it. Mathematics for Machine Learning states the probability integral transform (Theorem 6.15, PDF p. 222) without a proof or an exercise, and the Murphy book is listed on the [[Textbooks]] shelf but its PDF is not on disk, so it was not searched.
Read in full: Chan PDF pp. 245 to 251 and 253 to 256, Bishop PDF pp. 542 to 545, 547 and 572 to 573, the tutorial's Example 2, and Mathematics for Machine Learning PDF pp. 221 to 223. Only found: the one-line mentions in the Goodfellow deep learning book (PDF p. 710) and in Understanding Deep Learning (appendix C.4, PDF p. 473), which are statements and not problems. Bishop's solutions manual is not on the shelf.
<!-- /worked-examples-table -->

## Resampling (the bootstrap) to measure the spread of a statistic

<!-- worked-examples-table: resampling-the-bootstrap rev=2 -->
Problems on resampling one small data set with replacement to get a standard error or an interval for a statistic, from the easiest to the hardest. They are meant to serve the Judge Agreement Quiz questions that need resampling: I1, I2, I3, I4, E5, G4 and X2.

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | Resample ten exam scores (72, 69, 75, 58, 67, 70, 60, 71, 59, 65) with replacement 1,000 times, take the median of each resample, and read off the bootstrapped variance, standard error and interval. Also: why sampling with replacement and not a shuffle | Worked example, with Python code: `bootstrap_se(x, stat, K)` | [[introduction-to-probability-for-data-science.pdf#page=578\|Chan 9.2, the method, PDF pp. 578 to 580]] and [[introduction-to-probability-for-data-science.pdf#page=581\|the code, PDF pp. 581 to 582]] | Easy | Partial. The book gives the algorithm, the code and the formulas (9.20 to 9.23) and prints no resulting number for these scores: none: to be written for the numbers | I1, I2 |
| 2 | Five invented record decisions, three right and two wrong: draw five cards with replacement by hand, then list all 3,125 resamples in code and read the 95% percentile interval, which comes out 0.2 to 1.0 | Tutorial, Python: `bootstrap_toy.py`, with `empirical_quantile(values, q)` | [the measurement chapter, section 10.4, "Rehearse bootstrap sampling"](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/10-measurement.md#104-the-prototypes-baseline-scored-with-mlflow) | Easy | In the chapter: the formula (10.16), the script and its expected output (accuracy 0.6000, interval 0.2000 to 1.0000) | I1, G4, I2 |
| 3 | A lognormal sample of 100 values: bootstrap a 95% interval for its skewness, with resample sizes 30, 70 and 10, and plot the histograms. A statistic that is not a mean, so no formula gives its spread | Programming exercise, Python or MATLAB: `bootstrap_ci_skewness(y, K, B)` | [[introduction-to-probability-for-data-science.pdf#page=624\|Chan, Exercise 4, PDF p. 624]] | Medium | none: to be written | X2 (practice only: its solution is still to be written) |
| 4 | Resample the 20 products behind one judge's agreement table (16 both pass, 1 reviewer-only pass, 2 judge-only passes, 1 both fail) 10,000 times and report the 5th, 50th and 95th percentiles of the agreement score P+, dropping resamples where it is undefined | Tutorial, Python (standard library): `bootstrap_pplus(items, n_resamples)` | [the check script, last line of test 3](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/drips/combine-validating-an-llm-judge/checks/test-3-and-gold-design.py) | Medium | Partial. Running the script prints 9,489 usable of 10,000, 5th percentile 0.00, median 0.92, 95th percentile 1.00; the script has no written steps: none: to be written for the steps | E5, X2 |
| 5 | Compare two systems scored on the same products: resample the products once per replicate, score both systems on that one resample, and take the interval of the difference. Then the exact paired test on the 15-case table | Tutorial | [the measurement chapter, section 10.4, "Bootstrap a paired change"](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/10-measurement.md#104-the-prototypes-baseline-scored-with-mlflow) | Medium | Partial. The chapter gives the formulas and the paired table; it works the exact test and not a bootstrap run: none: to be written for the bootstrap numbers | I3, I4 |
| 6 | The largest of 50 uniform draws on (0, θ) with θ = 1 estimates θ: find its distribution, show it equals θ with probability zero, and bootstrap its histogram to see where resampling fails | Programming exercise, Python or MATLAB: `bootstrap_max_hist(x, K)` | [[introduction-to-probability-for-data-science.pdf#page=624\|Chan, Exercise 5, PDF p. 624]] | Hard | none: to be written | G4 (practice only: its solution is still to be written) |

No row resamples a correlation coefficient: the nearest statistics are a median, a skewness and the agreement score P+, and the correlation case still has to be written. The kappa case is worked in the note this block sits in. The Rao and Callison-Burch interval for kappa 0.402 (page 7 of the paper) is a reported result with no steps, so it is not a row. Row 3 asks for subsamples of size B inside 100 values, which is a variant of the full-size resampling that row 1 describes.
Read in full: Chan PDF pp. 575 to 582 and 621 to 625, the measurement chapter's section 10.4 from "Rehearse bootstrap sampling" to the paired table, and the check script, which was also run. Only found: the bootstrap mentions in Bishop (PDF pp. 42, 661 and 671, which are bagging and error bars in a paragraph), the Goodfellow deep learning book (PDF p. 272) and Understanding Deep Learning (PDF p. 160), none of which works an example. No solutions exist on the shelf for Chan's exercises 4 and 5.
<!-- /worked-examples-table -->

## The forward process, from one step to one jump

<!-- worked-examples-table: diffusion-forward-process rev=1 -->
Problems on the forward process of a diffusion model, from one noising step to the one-jump form x_t = √ᾱ_t x_0 + √(1 − ᾱ_t) ε, from the easiest to the hardest. They serve quiz 1.2 of the composition ladder (layer 1, one diffusion expert), whose coverage file is [quiz 1.2's preparation](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2.md).

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | Make the toy noisy point x_50 from x_0 = (0, 0.5) and ε = (0.3, −1.2) on the T = 100 cosine schedule, giving (0.2167, −0.521) | Worked example | [the one-expert walk, step 5](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-5-the-noise-is-the-score-rescaled) | Easy | [S1 in quiz 1.2's solutions](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2-solutions.md#s1-the-toy-forward-draw-b1) | Quiz 1.2, B1 |
| 2 | Show z = aε₁ + bε₂ has mean 0 and variance a² + b², so one draw √(a² + b²)ε replaces two | Exercise without one | [[understanding-deep-learning.pdf#page=385\|UDL, Problem 18.2, PDF p. 385]] | Easy | [the forward-process chapter, section 9.1](../../../../goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/09-the-forward-process-by-hand.md#91-independent-gaussian-noises-add-their-variances), which derives and works the same statement | Quiz 1.2, B2 |
| 3 | Show one step √(1 − β_t)x_{t−1} + √β_t ε_t keeps variance I | Exercise without one | [[understanding-deep-learning.pdf#page=385\|UDL, Problem 18.1, PDF p. 385]] | Easy | [S2](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2-solutions.md#s2-one-step-keeps-the-variance-at-1-b3-udl-181) | Quiz 1.2, B3 |
| 4 | The two-step noise variance both ways with α = 0.9 and 0.8: 0.28 | Worked example | [the forward-process chapter, worked example 9.1](../../../../goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/09-the-forward-process-by-hand.md#91-independent-gaussian-noises-add-their-variances) | Easy | In the chapter, with `checks/09_forward_closed_form.py` | Quiz 1.2, B4 |
| 5 | Continue the two-step collapse to z_3 | Exercise without one | [[understanding-deep-learning.pdf#page=385\|UDL, Problem 18.3, PDF p. 385]] | Medium | [S3](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2-solutions.md#s3-three-steps-in-one-jump-b5-udl-183) | Quiz 1.2, B5 |
| 6 | A four-step toy schedule iterated and jumped; x_2 = 1.9616 | Worked example | [the forward-process chapter, worked example 9.2a](../../../../goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/09-the-forward-process-by-hand.md#92-reading-the-image-ladder-and-the-one-jump-form) | Medium | In the chapter, with a 200,000-sample check | Quiz 1.2, B6 |
| 7 | Show √(ᾱ_t / ᾱ_{t−1}) = √(1 − β_t) | Exercise without one | [[understanding-deep-learning.pdf#page=386\|UDL, Problem 18.9, PDF p. 386]] | Medium | [S4](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2-solutions.md#s4-the-ratio-of-consecutive-kept-shares-b7-udl-189) | Quiz 1.2, B7 |
| 8 | Telescope ᾱ_t to C_{t+1} on the cosine schedule, and find what the clip at 0.999 does to ᾱ_99 (2.43e-7, multiplier 2029) | Worked example | [the one-expert walk, step 4](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-4-the-forward-process-and-the-cosine-schedule) | Hard | In the step file | Quiz 1.2, B8 |
| 9 | Build the cosine schedule and print ᾱ at t = 0, 25, 50, 75, 99 (0.9994, 0.8356, 0.4783, 0.1335, 0.0) | Programming exercise, Python: `cosine_beta_schedule(T, s)` | [the one-expert walk, step 4, Build](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-4-the-forward-process-and-the-cosine-schedule) | Medium | The printed numbers against `python -m rebuild.walk_numbers` (`p1.abar_*`) | Quiz 1.2, B9 |

UDL's Notebooks 18.1 and 18.3 (the diffusion encoder and the reparameterised model) would make programming rows; they are on GitHub and were found, not read, so they are not rows yet. No book on the shelf works the cosine schedule, so row 8 comes from the step file.
Read in full: UDL PDF pp. 363 to 368 and 385 to 386, the forward-process chapter's sections 9.1 to 9.3, the one-expert walk's step 4. Only found: the Little Book's forward process (PDF pp. 70 to 73), which works no numbers and sets no exercises.
<!-- /worked-examples-table -->

## The noise is the score, the sampled-noise identity

<!-- worked-examples-table: noise-is-the-score-conditional rev=1 -->
Problems on ε = −√(1 − ᾱ_t)·∇log q(x_t | x_0), the identity for one clean point and one sampled noise, from the easiest to the hardest. They serve quiz 1.2 of the composition ladder.

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | The score of a 1D Gaussian, −(x − μ)/σ², by taking the log and differentiating | Worked example | [[the-little-book-of-generative-ai-foundations.pdf#page=114\|Little Book, section 6.1.1, PDF p. 114]] | Easy | In the book | Quiz 1.2, B10 |
| 2 | The toy score at x_50: −(0.3, −1.2)/0.7223 = (−0.4153, 1.6613) | Worked example | [the one-expert walk, step 5](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-5-the-noise-is-the-score-rescaled) | Easy | In the step file, against `p1.example_score` | Quiz 1.2, B11 |
| 3 | The score two ways at step 20 (−0.5521) and at three more steps | Worked example | [the forward-process chapter, worked example 9.5](../../../../goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/09-the-forward-process-by-hand.md#95-eps---sigma_t-grad-log-q) | Easy | In the chapter, with `checks/11_eps_is_score.py` | Quiz 1.2, B12 |
| 4 | The same score as −Σ⁻¹(x − μ) with Σ = (1 − ᾱ)I | Exercise without one | [[the-little-book-of-generative-ai-foundations.pdf#page=115\|Little Book, PDF p. 115]] | Medium | [S5](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2-solutions.md#s5-the-score-through-the-covariance-b13) | Quiz 1.2, B13 |
| 5 | The score grows 24.16-fold across a run while σ_t times it stays 0.5 | Worked example | [the forward-process chapter, worked example 9.6](../../../../goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/09-the-forward-process-by-hand.md#96-the-units-check) | Medium | In the chapter | Quiz 1.2, B14 |
| 6 | The unshrunk corruption x̃ = x + ε against the forward process's shrunk centre | Exercise without one | [[the-little-book-of-generative-ai-foundations.pdf#page=124\|Little Book, section 6.3.1, PDF p. 124]] | Medium | [S6](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2-solutions.md#s6-the-unshrunk-corruption-against-the-forward-process-b15) | Quiz 1.2, B15 |
| 7 | Take the score by autograd on log q(x_t \| x_0) and compare with −ε/√(1 − ᾱ_t) | Programming exercise, Python (PyTorch): `torch.autograd.grad` | [the one-expert walk, step 5, Build](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-5-the-noise-is-the-score-rescaled) | Medium | The printed line against `p1.example_score` | Quiz 1.2, B16 |

No shelf book poses the sampled-noise identity itself as an exercise; rows 4 and 6 turn the Little Book's statements into problems.
Read in full: the Little Book PDF pp. 114 to 127, the forward-process chapter's sections 9.5 and 9.6, the one-expert walk's step 5. Only found: Understanding Deep Learning's chapter 18, which reaches the ε loss through the ELBO and never names the score.
<!-- /worked-examples-table -->

## The squared-error optimum is the conditional mean

<!-- worked-examples-table: squared-error-optimum-conditional-mean rev=1 -->
Problems on why the best squared-error guess of a hidden quantity is its conditional mean, and on the error that is left over, from the easiest to the hardest. They serve quiz 1.2 of the composition ladder, where the hidden quantity is the added noise.

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | Guess a die from its parity: the errors 8/3, 35/12 and 11/3 | Worked example | [the conditional-expectation textbook, section 5](../../../../goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/05-the-conditional-mean-is-the-best-guess.md) | Easy | In the chapter, and in plan 05 task 2.2 | Quiz 1.2, B17 |
| 2 | Y = X + N: the best linear estimate aY of X and its error in terms of η = σ²_X/σ²_N | Exercise without one | [[introduction-to-probability-for-data-science.pdf#page=334\|Chan, Exercise 5.16, PDF p. 334]] | Medium | [S7](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2-solutions.md#s7-the-best-straight-line-denoiser-b18-chan-exercise-516) | Quiz 1.2, B18 |
| 3 | ML, MAP and MMSE estimates for an exponential likelihood and prior | Worked example | [[introduction-to-probability-for-data-science.pdf#page=543\|Chan, Example 8.22, PDF pp. 543 to 544]] | Medium | In the book | Quiz 1.2, B19 |
| 4 | The two-point toy x = ±1, x_t = x + g: the tanh denoiser's floor 0.4496 against the best line's 0.5 | Worked example | [the conditional-expectation textbook, section 5](../../../../goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/05-the-conditional-mean-is-the-best-guess.md) | Medium | In the chapter, and in plan 05 task 2.3 | Quiz 1.2, B20 |
| 5 | The conditional mean minimises the expected squared loss for a vector target | Exercise without one | [[pattern-recognition-and-machine-learning.pdf#page=83\|Bishop, Exercise 1.25, PDF p. 83]] | Medium | [S8](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2-solutions.md#s8-the-conditional-mean-for-a-vector-target-b21-bishop-125) | Quiz 1.2, B21 |
| 6 | A Gaussian posterior: its MMSE estimate and its MSE | Exercise without one | [[introduction-to-probability-for-data-science.pdf#page=553\|Chan, Exercise 8.5, PDF pp. 553 to 554]] | Hard | none: to be written | Quiz 1.2, B22 (practice only: its solution is still to be written) |

Chan proves the theorem (Theorem 8.2, PDF pp. 539 to 540) and the leftover error (PDF pp. 541 to 542) in symbols; Bishop's section 1.5.5 (PDF pp. 65 to 66) gives the same split as eq. 1.90. Bishop's solutions manual is not on the shelf, so row 5's solution is written.
Read in full: Chan PDF pp. 332 to 334 and 536 to 554, Bishop PDF pp. 65 to 67 and Exercises 1.25 and 1.26, the conditional-expectation plan 05. Only found: Murphy's MMSE estimate (Probabilistic Machine Learning, PDF p. 196), which states it without an exercise.
<!-- /worked-examples-table -->

## The noise a network learns, the marginal identity

<!-- worked-examples-table: noise-is-the-score-marginal rev=1 -->
Problems on E[ε | x_t] = −√(1 − ᾱ_t)·∇log q_t(x_t): averaging the one-clean-point identity over every clean point that could have made x_t, from the easiest to the hardest. They serve quiz 1.2 of the composition ladder.

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | The two-point toy by Bayes on densities, then by Tweedie's formula: 0.4621 both ways | Worked example | [the conditional-expectation textbook, section 6, Example 4](../../../../goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/06-conditioning-with-densities.md#worked-examples) | Medium | In the chapter, with `verify.py` | Quiz 1.2, B23 |
| 2 | Derive the smoothed score as the posterior average of conditional scores | Worked example (a derivation) | [[the-little-book-of-generative-ai-foundations.pdf#page=123\|Little Book, section 6.3, PDF pp. 123 to 126]] | Medium | In the book | Quiz 1.2, B24 |
| 3 | The slope a denoiser learns on N(0, 1) data, −1/(1 + σ²) = −0.8 at σ = 0.5 | Worked example | [the training-loss chapter, worked example 13.2](../../../../goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/13-the-training-loss-two-ways.md#132-denoising-score-matching-and-its-optimum) | Medium | In the chapter | Quiz 1.2, B25 |
| 4 | E[ε \| x_t] on N(0, I) data at the toy point: (0.1565, −0.3763), by the marginal score and by Gaussian conditioning | Exercise without one, constructed on [[introduction-to-probability-for-data-science.pdf#page=545\|Chan, Theorem 8.3, PDF p. 545]] | quiz 1.2's coverage file | Medium | [S9](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2-solutions.md#s9-the-noise-a-network-learns-on-gaussian-data-b26) | Quiz 1.2, B26 |
| 5 | E[ε \| x_t] on two clean points at the toy point: posterior 0.3339 and 0.6661, marginal score (−0.4154, 0.7784), noise (0.3, −0.5623) against the sampled (0.3, −1.2) | Worked example | [the training-loss chapter, section 13.5](../../../../goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/13-the-training-loss-two-ways.md#135-one-clean-point-against-all-of-them-the-score-the-network-learns), worked example 13.5 | Hard | [S10](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2-solutions.md#s10-the-noise-a-network-learns-on-two-clean-points-b27) | Quiz 1.2, B27 |
| 6 | Fit a slope by denoising score matching on 200,000 samples at σ = 0.5; seed 0 gives −0.797997 | Programming exercise, Python (NumPy): a least-squares fit of a·x̃ onto −ε/σ | [the score-matching plan, task 1.2](../../../../goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/20-score-matching-the-training-objective.md) | Medium | The training-loss chapter, worked example 13.2 step 5 | Quiz 1.2, B28 |

Goodfellow's section 18.5 (PDF p. 635) defines the smoothed density and sets no exercise, so it is not a row. Row 5 is also the training-loss chapter's worked example 13.5.
Read in full: the Little Book PDF pp. 123 to 127, the training-loss chapter's section 13.2, the conditional-expectation textbook's section 6 Example 4, Chan PDF p. 545. Only found: Goodfellow PDF p. 635.
<!-- /worked-examples-table -->

## The denoising loss

<!-- worked-examples-table: denoising-loss rev=1 -->
Problems on L = E ½‖ε̂(x_t, t) − ε‖², the loss a diffusion expert is trained on: its parts, its estimate on a batch, and the floor it cannot go below, from the easiest to the hardest. They serve quiz 1.2 of the composition ladder.

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | Read the training algorithm term by term: t uniform, ε standard normal, the squared miss | Worked example | [[understanding-deep-learning.pdf#page=377\|UDL, Algorithm 18.1, PDF p. 377]] | Easy | In the book | Quiz 1.2, B29 |
| 2 | One draw's loss with the untrained rule ε̂ = 2x_t: 0.0214, and 0.0428 without the ½ | Exercise without one, constructed on the step file | [the one-expert walk, step 8](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-8-the-denoising-loss) | Easy | [S11](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2-solutions.md#s11-one-draws-loss-and-what-the-half-does-b30) | Quiz 1.2, B30 |
| 3 | A three-draw batch mean, 0.3439, as the estimate of the expectation | Exercise without one, constructed on the step file | [the one-expert walk, step 8](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-8-the-denoising-loss) | Medium | [S12](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2-solutions.md#s12-a-batch-mean-stands-in-for-the-expectation-b31) | Quiz 1.2, B31 |
| 4 | The coefficient identity behind the reparameterised target | Exercise with the book's solution | [[understanding-deep-learning.pdf#page=386\|UDL, Problem 18.10, PDF p. 386]] | Medium | In the book's text, eq. 18.33, PDF p. 375 | Quiz 1.2, B32 |
| 5 | The first step's loss in noise form (eq. 18.37), factor 0.0251 on the cosine schedule | Exercise without one | [[understanding-deep-learning.pdf#page=386\|UDL, Problem 18.11, PDF p. 386]] | Hard | [S13](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2-solutions.md#s13-the-first-steps-loss-in-noise-form-b33-udl-1811) | Quiz 1.2, B33 |
| 6 | The floor: ᾱ_t for N(0, I) data (0.4783 at t = 50), 0.1019 at the two-point toy | Exercise without one, constructed on [[pattern-recognition-and-machine-learning.pdf#page=66\|Bishop eq. 1.90, PDF p. 66]] | quiz 1.2's coverage file | Hard | [S14](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-2-solutions.md#s14-the-floor-under-the-loss-b34) | Quiz 1.2, B34 |
| 7 | Write the loss, print 0.79 at initialisation on `bar(0.2)` and "parameters with a gradient: 45 of 45" | Programming exercise, Python (PyTorch): `loss_fn(model, x0)` | [the one-expert walk, step 8, Build](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-8-the-denoising-loss) | Medium | The printed lines against `p1.init_loss_on_bar` | Quiz 1.2, B35 |

UDL Problems 18.4 to 18.8 belong to the reverse step and the ELBO, and are left for the quiz that tests them. No book on the shelf computes the floor in the ε form; row 6 builds it from Bishop's split.
Read in full: UDL PDF pp. 370 to 378 and 385 to 386, the one-expert walk's step 8, Bishop PDF pp. 65 to 67. Only found: the Little Book's DDPM loss (PDF pp. 74 to 88), not opened past its contents.
<!-- /worked-examples-table -->

## Mean and variance of a scaled sum of independent Gaussians (the forward draw)

<!-- worked-examples-table: forward-draw-mean-and-variance rev=1 -->
Problems on the mean and variance of $a X + b$ and of a sum of independent Gaussians, the rule that makes $\sqrt{\bar\alpha}\,x_0 + \sqrt{1-\bar\alpha}\,\varepsilon$ a Gaussian with mean $\sqrt{\bar\alpha}\,x_0$ and variance $1-\bar\alpha$, from the easiest to the hardest:

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | $Y = aX + b$ for a standard Gaussian $X$: write its CDF as $\Phi((y-b)/a)$ and its density | Worked example | [[introduction-to-probability-for-data-science.pdf#page=241\|Chan, follow-up to Example 4.26, PDF pp. 241 to 242]] | Easy | In the book, PDF p. 242 | quiz 1.1, B1.1 |
| 2 | The mean and variance of a sum of two independent variables, then the covariance matrix of a sum of two independent random vectors | Exercise without one | [[pattern-recognition-and-machine-learning.pdf#page=78\|Bishop, Exercise 1.10, PDF p. 78]] and [[pattern-recognition-and-machine-learning.pdf#page=151\|Exercise 2.27, PDF p. 151]] | Easy | [S1 in the quiz 1.1 solutions](/home-mscluster/mmolefe/PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-1-solutions.md#s1-the-mean-and-variance-of-a-sum-of-independent-variables-b12-bishop-110-and-227), numbers printed by its check script | quiz 1.1, B1.2 |
| 3 | Show that $Y = \Sigma^{1/2}X + \mu$ has mean $\mu$ and covariance $\Sigma$ for $X \sim \mathcal N(0, I)$, which is how a Gaussian sample is made | Worked example | [[introduction-to-probability-for-data-science.pdf#page=315\|Chan, Theorem 5.19, PDF p. 315]] | Medium | In the book, PDF p. 315 | quiz 1.1, B1.4 |
| 4 | $y = Ax + b + w$ with independent Gaussian noise: write $p(y \mid x)$, then derive the mean and covariance of $p(y)$; with $A = \sqrt{\bar\alpha_{50}}\,I$ this is the forward process | Exercise without one | [[mathematics-for-machine-learning.pdf#page=229\|Mathematics for Machine Learning, Exercise 6.12 (a) and (b), PDF p. 229]] | Hard | [S2 in the quiz 1.1 solutions](/home-mscluster/mmolefe/PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-1-solutions.md#s2-a-linear-map-plus-independent-noise-b16-mml-612) | quiz 1.1, B1.6 |
| 5 | Chan states that $X_1 + X_2 \sim \mathcal N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$ but proves only $\sigma_1 = \sigma_2$: prove the general case | Exercise without one | [[introduction-to-probability-for-data-science.pdf#page=299\|Chan, Theorem 5.12, PDF pp. 299 to 300]] | Hard | [S3 in the quiz 1.1 solutions](/home-mscluster/mmolefe/PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-1-solutions.md#s3-two-gaussians-with-unequal-variances-b17-chan-theorem-512), by generating functions | quiz 1.1, B1.7 |
| 6 | Noise one cloud at three levels in one tensor and print the measured mean and variance beside the closed form, first with the square roots left off | Programming exercise, Python: `noised.py` | [[The Forward Process#Try the jump yourself]], steps 3 and 4 | Medium | In the note, with the expected output (variance 0.5 and 1.25 without the roots, 1.0 and 2.5 with them) | quiz 1.1, B1.8 |

The chapter's worked examples 9.1 (0.28 both ways) and 9.2a (the four-step schedule) are banked by quiz 1.2 in [[#The forward process, from one step to one jump]], so they are not repeated here. No book problem asks for the variance of the forward draw at a named step; rows 6 and 7 are the nearest, and the quiz's own numbers ($\bar\alpha_{50} = 0.4783$) are worked into their solutions. Chan's convolution proof of Theorem 5.12 is the reason for row 7: it is a special case printed as the general one.
Read in full: Chan PDF pp. 241 to 243, 298 to 300 and 309 to 316, Bishop's exercise statements 1.10 and 2.27, Mathematics for Machine Learning PDF pp. 228 to 230, the chapter's sections 9.1 and 9.2, and the vault note's steps 3 and 4. Only found: Mathematics for Machine Learning's variance under an affine map (PDF p. 200), stated without an exercise.
<!-- /worked-examples-table -->

## The score of a Gaussian

<!-- worked-examples-table: score-of-a-gaussian rev=2 -->
Problems on the score $\nabla_x \log p(x)$ of a Gaussian, $-(x-\mu)/\sigma^2$ in one dimension and $-\Sigma^{-1}(x-\mu)$ in $d$, from the easiest to the hardest:

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | The gradient of $x^\top A x$ for a symmetric and a non-symmetric $A$, then the 1D score at $x = 2$ for three Gaussians: $-2$, $-8$ and $+0.25$ | Tutorial | [the Gaussian-score chapter, section 6.1](/home-mscluster/mmolefe/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/06-the-gaussian-score.md#61-the-gradient-of-a-quadratic-form) | Easy | In the chapter, with the trap ($2Bx = (10, 12)$ against the true $(6, 14)$) and finite differences | quiz 1.1, B2.2 |
| 2 | Show that the mode of the 1D and the multivariate Gaussian is $\mu$ | Exercise without one | [[pattern-recognition-and-machine-learning.pdf#page=78\|Bishop, Exercise 1.9, PDF p. 78]] | Easy | [S4 in the quiz 1.1 solutions](/home-mscluster/mmolefe/PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-1-solutions.md#s4-the-mode-of-a-gaussian-is-its-mean-b23-bishop-19) | quiz 1.1, B2.3 |
| 3 | Four changes to a standard normal (times a constant, plus a constant in the log, a shift, plus 137 in the density) and what each does to its score | Tutorial | [the Gaussian-score chapter, section 6.3](/home-mscluster/mmolefe/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/06-the-gaussian-score.md#63-which-constants-and-shifts-leave-the-score-alone) | Medium | In the chapter, with the failure (the arrow 567 times too short when 137 is added) | quiz 1.1, B2.4 |
| 4 | The score at $(3, 4)$ under $\Sigma = \operatorname{diag}(1, 4)$ is $(-3, -1)$, 34.6952° off the direction to the mean, and it meets the contour ellipse at a right angle | Tutorial | [the Gaussian-score chapter, section 6.2](/home-mscluster/mmolefe/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/06-the-gaussian-score.md#62-the-anisotropic-score-follows-the-inverse-covariance) | Medium | In the chapter, checked by `checks/08_gaussian_score.py` | quiz 1.1, B2.5 |
| 5 | By the chain rule, differentiate $\exp(-\tfrac12 (x-\mu)^\top S^{-1}(x-\mu))$ in $x$ with the dimension of every partial; dividing by the function gives the score | Exercise without one | [[mathematics-for-machine-learning.pdf#page=177\|Mathematics for Machine Learning, Exercise 5.8 (a), PDF p. 177]] | Medium | [S5 in the quiz 1.1 solutions](/home-mscluster/mmolefe/PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-1-solutions.md#s5-the-chain-rule-through-the-gaussians-exponential-b26-mml-58a) | quiz 1.1, B2.6 |
| 6 | The maximum-likelihood mean and variance of i.i.d. Gaussians from the derivatives of the log-likelihood; the derivative in $\mu$ is the score in $x$ with its sign reversed | Exercise with the book's solution | [[introduction-to-probability-for-data-science.pdf#page=500\|Chan, Practice Exercise 8.5, PDF pp. 500 to 501]] | Hard | In the book, PDF p. 501 | quiz 1.1, B2.7 |

The little book's 1D score (PDF p. 114) and the step file's autograd check of the toy score (step 5) are banked by quiz 1.2 in [[#The noise is the score, the sampled-noise identity]], so they are not repeated here. No textbook on the shelf sets the Gaussian score in $x$ as an exercise; the books take derivatives in the parameters (row 7) or of the density (row 6). The journey's chapter 6 is where the score itself is worked.
Read in full: the little book PDF p. 114, Bishop's exercise statement 1.9, Mathematics for Machine Learning PDF p. 177, Chan PDF pp. 500 to 501, the chapter's sections 6.1 to 6.3 and the step file's step 5. Only found: the matrix cookbook's derivative of a quadratic form, and the deep learning textbook's score matching pages (PDF pp. 633 to 635), which define the score without an exercise.
<!-- /worked-examples-table -->

## Least-squares regression and the best guess under squared error

<!-- worked-examples-table: least-squares-regression rev=1 -->
Problems on choosing a guess or a line by minimising squared error: the best constant is the mean, the best line solves the normal equations, and the best function of the input is the conditional mean, from the easiest to the hardest:

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | The best constant guess for a fair die under squared error is 3.5, with error 2.9167; guesses 3 and 4 both cost 3.1667 | Tutorial | [the conditional-expectation chapter, section 1, Example 1](/home-mscluster/mmolefe/goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/01-expectation-and-the-best-constant-guess.md#worked-examples) | Easy | In the chapter, with a face-by-face check | quiz 1.1, B3.1 |
| 2 | The least-squares line through $(0, 1), (1, 3), (2, 4), (3, 4)$ is $y = 1.5 + x$ | Worked example | [[linear-algebra-textbook.pdf#page=404\|Anton, section 6.5, Example 1, PDF p. 404]] | Easy | In the book, PDF p. 404 | quiz 1.1, B3.2 |
| 3 | Starting salary against education score for six people, by the normal equations: 5,370 dollars per score point | Worked example | [[introduction-to-statistics.pdf#page=130\|Introduction to Statistics, Example 6.4, PDF pp. 130 to 131]] | Medium | In the book, PDF p. 131; its intercept 4,779 uses the rounded slope, and the unrounded one gives 4,777.78 | quiz 1.1, B3.3 |
| 4 | Example 6.4 without its sixth person: re-estimate both coefficients and predict the salary at score 2.8 | Exercise without one | [[introduction-to-statistics.pdf#page=132\|Introduction to Statistics, Exercise 6.5, PDF p. 132]] | Medium | [S6 in the quiz 1.1 solutions](/home-mscluster/mmolefe/PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-1-solutions.md#s6-example-64-without-its-sixth-person-b34-introduction-to-statistics-65): slope 5,492.42, intercept 4,484.85, 19,863.64 dollars at 2.8 | quiz 1.1, B3.4 |
| 5 | Write `fit_line(x, y)` with `np.linalg.lstsq` on the columns $(x, 1)$ and confirm the answer solves $X^\top X\theta = X^\top y$ on row 2's points | Programming exercise, Python: `fit_line(x, y)` | [[introduction-to-probability-for-data-science.pdf#page=414\|Chan, Theorem 7.1 and the Python listing, PDF pp. 414 to 416]] | Medium | [S7 in the quiz 1.1 solutions](/home-mscluster/mmolefe/PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-1-1-solutions.md#s7-a-line-fitted-by-lstsq-solves-the-normal-equations-b36-chan-theorem-71) | quiz 1.1, B3.6 |

The two-point toy's best line against its conditional mean (the conditional-expectation chapter, section 5, Example 3) is banked by quiz 1.2 in [[#The squared-error optimum is the conditional mean]]. No row reaches ridge regression: Chan's Exercise 10 (PDF p. 480) turns noisy inputs into a ridge penalty, and no passage teaches ridge to the full-steps standard yet. The vector-target version of row 5 (Bishop, Exercises 1.25 and 1.26, PDF p. 83) is quiz 1.2's.
Read in full: the conditional-expectation chapter's section 5 Example 3, Anton PDF pp. 401 to 404, Introduction to Statistics PDF pp. 128 to 135, and Chan PDF pp. 412 to 416, 475 to 476 and 480. Only found: the deep learning textbook's linear least squares example (PDF p. 112) and Mathematics for Machine Learning's chapter 9 (PDF p. 295), which has no exercises.
<!-- /worked-examples-table -->

## Solving with logs and exponents

<!-- worked-examples-table: logs-and-exponents rev=1 -->
Problems on the log rules and on solving for an unknown in the exponent, the move behind a moving average's half-life, from the easiest to the hardest:

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | Rewrite $\log_4 64 = x$ and $\ln e = x$ in exponential form and solve | Worked example | [[algebra-handbook.pdf#page=113\|Algebra handbook, examples 1 and 2, PDF p. 113]] | Easy | In the book, PDF p. 113, every step: $x = 3$ and $x = 1$ | quiz 0, KA1 |
| 2 | Condense $6 + \ln(3e^5)$ and $\log_4(1/16) - 6^{\log_6 4}$ with the product, power and quotient rules | Worked example | [[algebra-handbook.pdf#page=116\|Algebra handbook, PDF p. 116]] | Easy | In the book, PDF p. 116, every step: $11 + \ln 3$ and $-6$ | quiz 0, KA2 |
| 3 | Solve $2 + 4 \cdot 3^{x-2} = 110$: isolate the power, take logs, solve | Worked example | [[algebra-handbook.pdf#page=125\|Algebra handbook, PDF p. 125]] | Medium | In the book, PDF p. 125, every step: $x = 5$ | quiz 0, KA3 |
| 4 | A satellite's power is $P = 75e^{-t/125}$ watts: when does it fall to 7 watts? | Worked example | [[calculus-textbook.pdf#page=82\|Anton, Calculus, section 0.5, Example 3, PDF p. 82 (printed 58)]] | Medium | In the book, PDF p. 82, every step: $t = -125 \ln(7/75) \approx 296.4$ days | quiz 0, KA4 |

The ladder's own solve, the moving average's half-life $\ln 0.5 / \ln 0.999 = 692.8$ steps, is quiz 0's written question A2 and is worked in [[Solving For The Exponent With Logarithms]] and [[The Exponent Rules]]. Not banked: Anton's exercises 0.5 #25, #27 and #49 (PDF pp. 85 to 86), whose answers at PDF p. 1240 are final values only, and Murphy's section 4.4.2.2 (PDF p. 139), which derives the moving average's weights $\beta^k(1 - \beta)$ without a numeric question.
Read in full (by the bank search for quiz 0): algebra handbook PDF pp. 113, 115, 116, 124 and 125; Anton PDF pp. 81, 82, 85 to 87 and 1240; Murphy PDF pp. 139 to 140. Only found: algebra handbook PDF pp. 109 to 112 and 117 to 123, rule tables and further examples.
<!-- /worked-examples-table -->

## The chain rule and partial derivatives

<!-- worked-examples-table: chain-rule-and-partials rev=1 -->
Problems on differentiating a function of a function, and on partial derivatives and the gradient, from the easiest to the hardest:

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | Differentiate $e^{5x}$ | Exercise with the book's solution | [[calculus-practice-problems.pdf#page=71\|Calculus practice problems, #390, PDF p. 71]] | Easy | In the book, PDF p. 276, with the chain step: $5e^{5x}$ | quiz 0, KB1 |
| 2 | Differentiate $(x^2 + 3x)^{100}$ | Exercise with the book's solution | [[calculus-practice-problems.pdf#page=66\|Calculus practice problems, #352, PDF p. 66]] | Easy | In the book, PDF p. 262, every step: $100(2x + 3)(x^2 + 3x)^{99}$ | quiz 0, KB2 |
| 3 | Differentiate $\ln\sqrt{x^2 + 5}$: the log rule first, then the chain rule | Exercise with the book's solution | [[calculus-practice-problems.pdf#page=70\|Calculus practice problems, #379, PDF p. 70]] | Medium | In the book, PDF p. 271, every step: $x/(x^2 + 5)$ | quiz 0, KB3 |
| 4 | The gradient of $f = x^2 e^y$ at $(-2, 0)$, the largest rate of increase there, and its direction | Worked example | [[calculus-textbook.pdf#page=988\|Anton, Calculus, section 13.6, Example 4, PDF pp. 988 to 989]] | Hard | In the book, PDF p. 989, every value: $(-4, 4)$, $4\sqrt2 \approx 5.657$, $(-1/\sqrt2, 1/\sqrt2)$ | quiz 0, KB4 |

The journey's chapter 4.3 works $(x^2 + 1)^3$ at 1 to 24, with the outer slope taken at the wrong point giving 6; quiz 0's B questions use it. Not banked: Anton's exercises 13.3 #25 and #39 (PDF p. 961), whose answers at PDF p. 1282 are final values only.
Read in full (by the bank search for quiz 0): calculus practice problems PDF pp. 66 to 68, 70, 71, 262, 269 to 271 and 276; Anton PDF pp. 952 to 954, 960, 961, 988, 989 and 1282. Only found: Anton section 13.5's chain-rule examples (PDF pp. 975 and 977).
<!-- /worked-examples-table -->

## Completing the square and the Gaussian density by hand

<!-- worked-examples-table: completing-the-square-and-gaussian-density rev=1 -->
Problems on completing the square, from a plain quadratic to a Gaussian exponent, and on evaluating a Gaussian density at a number, from the easiest to the hardest:

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | Write $x^2 - 4x + 5$ as $(x - 2)^2 + 1$ | Worked example | [[calculus-textbook.pdf#page=44\|Anton, Calculus, Example 8, PDF p. 44 (printed 20)]] | Easy | In the book, PDF p. 44 | quiz 0, KC1 |
| 2 | Complete the square in $3x^2 + 18x - 21 = 0$ and solve | Worked example | [[algebra-handbook.pdf#page=74\|Algebra handbook, PDF p. 74]] | Easy | In the book, PDF p. 74, six numbered steps: $(x + 3)^2 = 16$, so $x = 1$ or $x = -7$ | quiz 0, KC2 and C3 |
| 3 | Evaluate $\mathcal N(0, 0.25)$ at 0 and 0.5 with `stats.norm.pdf` and by hand, then pass the variance where the standard deviation goes | Programming exercise, Python: `stats.norm.pdf(x, loc, scale)` | [[introduction-to-probability-for-data-science.pdf#page=228\|Chan, the Python listing, PDF p. 228]] | Medium | [KC3 in the quiz 0 coverage file](/home-mscluster/mmolefe/PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-0.md#kc3-solution-the-toy-gaussian-in-code): 0.7979 and 0.4839; the slip gives 1.5958 and 0.2160 | quiz 0, KC3 |
| 4 | Complete the square for the diffusion reverse posterior $q(x_{t-1} \mid x_t, x_0)$ | Worked example | [[the-little-book-of-generative-ai-foundations.pdf#page=189\|The little book of generative AI foundations, Appendix B, PDF pp. 189 to 192]] | Hard | In the book, every step: variance $(1 - \bar\alpha_{t-1})\beta_t / (1 - \bar\alpha_t)$ | quiz 0, KC4 |

No book works the Gaussian density at a number by hand: row 3's listing prints no values, so its solution is written. The derivation of the front factor is [[The Front Factor Of A Gaussian Density]]. Not banked: Bishop's Exercise 1.7 (the Gaussian integral in polar coordinates, PDF p. 78, no printed solution), Mathematics for Machine Learning's Exercise 6.10 (the product of two Gaussians, PDF p. 229, no printed solution), and Chan's Theorem 5.12 (PDF pp. 299 to 300), banked by quiz 1.1 in [[#Mean and variance of a scaled sum of independent Gaussians (the forward draw)]].
Read in full (by the bank search for quiz 0): algebra handbook PDF p. 74; Anton PDF p. 44; Chan PDF pp. 227 to 231; Bishop PDF p. 78; Mathematics for Machine Learning PDF pp. 206, 207, 228 and 229; the little book PDF pp. 185 to 192. Only found: Anton section 7.4, Example 6 (completing the square inside an integral, PDF p. 536).
<!-- /worked-examples-table -->

## The mean and variance of one variable, scaled, shifted and summed

<!-- worked-examples-table: mean-and-variance-scaled-shifted-summed rev=1 -->
Problems on the mean and variance from their definitions, under $aX + b$, and under sums of independent variables, from the easiest to the hardest:

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | The mean and variance of a count with $P(0) = 0.65$, $P(1) = 0.15$, $P(2) = 0.10$, $P(3) = 0.10$ | Worked example | [[introduction-to-statistics.pdf#page=82\|Introduction to Statistics, Example 4.2, PDF p. 82]] | Easy | In the book, PDF p. 82: 0.65 and 1.03 (exactly 1.0275); its working prints $4^2$ where $2^2$ is meant, and the final value is right | quiz 0, KD1 |
| 2 | Given $E[X] = 1$ and $E[X^2] = 3$, find $E[(aX + b)^2]$ | Worked example | [[introduction-to-probability-for-data-science.pdf#page=149\|Chan, Example 3.15, PDF p. 149]] | Easy | In the book, PDF p. 149: $3a^2 + 2ab + b^2$ | quiz 0, KD2 |
| 3 | Prove $\mathrm{Var}[X] = E[X^2] - \mu^2$, $\mathrm{Var}[cX] = c^2\mathrm{Var}[X]$ and $\mathrm{Var}[X + c] = \mathrm{Var}[X]$ | Exercise with the book's solution | [[introduction-to-probability-for-data-science.pdf#page=151\|Chan, Practice Exercise 3.6, PDF p. 151]] | Medium | In the book, PDF pp. 151 to 152, every step | quiz 0, KD3 |
| 4 | Simulate the sum of three dice and check mean 10.5 and variance 8.75; the printed listing's `randint(1,6)` gives 9 and 6 | Programming exercise, Python: `np.random.randint` | [[introduction-to-probability-for-data-science.pdf#page=236\|Chan, the dice listing, PDF pp. 236 to 237]] | Medium | [KD4 in the quiz 0 coverage file](/home-mscluster/mmolefe/PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-0.md#kd4-solution-three-dice-in-code) | quiz 0, KD4 |
| 5 | The sum of $N$ independent Gaussians is $\mathcal N(\sum\mu_n, \sum\sigma_n^2)$, by the product of moment generating functions | Worked example | [[introduction-to-probability-for-data-science.pdf#page=345\|Chan, Theorem 6.6, PDF p. 345]] | Hard | In the book, PDF p. 345; the Gaussian generating function is stated there, and the journey's chapter 9.1, step 5, derives it | quiz 0, KD5 |

The derivation of the $aX + b$ rules on a fair die is [[Scaling And Shifting A Random Variable]]. The Gaussian forms of these rules, $aX + b$ for a Gaussian and sums of Gaussian vectors, are banked by quiz 1.1 in [[#Mean and variance of a scaled sum of independent Gaussians (the forward draw)]]. Chan's dice listing has a bug: `np.random.randint(1,6)` draws only 1 to 5.
Read in full (by the bank search for quiz 0): Introduction to Statistics PDF pp. 80 to 83; Chan PDF pp. 149 to 152, 219, 220, 236, 237, 241, 242 and 345; Mathematics for Machine Learning PDF p. 207; Bishop PDF p. 78. Only found: Chan's Theorem 5.5 (PDF p. 279).
<!-- /worked-examples-table -->

## Bayes' rule and the law of total probability

<!-- worked-examples-table: bayes-rule rev=1 -->
Problems on conditioning, the law of total probability and Bayes' rule, up to a Gaussian prior times a Gaussian likelihood, from the easiest to the hardest:

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | One die: $P[3 \mid \text{odd}]$ and $P[\text{odd} \mid 3]$ | Worked example | [[introduction-to-probability-for-data-science.pdf#page=98\|Chan, Example 2.44, PDF p. 98]] | Easy | In the book, PDF p. 98: 1/3 and 1 | quiz 0, KE1 |
| 2 | Opponents are 50% A, 25% B and 25% C, and you win 0.3, 0.4 and 0.5 of matches against each: the chance of winning, then of having played A given a win | Worked example | [[introduction-to-probability-for-data-science.pdf#page=106\|Chan, Example 2.47, PDF pp. 106 to 107]] | Easy | In the book, PDF p. 107, every value: 0.375, then 0.4 | quiz 0, KE2 |
| 3 | A test with sensitivity 0.875 and specificity 0.975, prior 0.1: the chance of infection after a positive and after a negative result, then at a 1% prior | Worked example | [[probabilistic-machine-learning-an-introduction.pdf#page=70\|Murphy, section 2.3.1, PDF pp. 70 to 71]] | Medium | In the book, PDF p. 71, every value: 0.795 and 0.014; its count check prints 865 where 875 is meant | quiz 0, KE3 |
| 4 | A Gaussian prior on a mean times a Gaussian likelihood: the most probable mean, by setting the derivative of the log posterior to zero | Worked example | [[introduction-to-probability-for-data-science.pdf#page=523\|Chan, Example 8.19, PDF pp. 523 to 524]] | Hard | In the book, every step of the derivative route; the completed square on PDF p. 528 is asserted, not shown | quiz 0, KE4 |

The journey's chapter 1.5 works the librarians and farmers both ways (1/6); quiz 0's E2 uses it. Not banked: Bishop's Exercise 2.38 (PDF p. 153) and Murphy's Exercise 4.3 (PDF p. 184), which print no solution, and Introduction to Statistics Example 3.26 (PDF p. 76), which rounds $P(D)$ to 0.014 before dividing (exactly 0.01375, so its 0.536, 0.179 and 0.268 should be 0.545, 0.182 and 0.273).
Read in full (by the bank search for quiz 0): Chan PDF pp. 98, 106 to 108, 523, 524 and 526 to 528; Murphy PDF pp. 70, 71, 182 and 184; Introduction to Statistics PDF p. 76; Mathematics for Machine Learning PDF p. 228; Bishop PDF pp. 117 and 153. Only found: Chan's Examples 2.48 and 8.20, Bishop's Exercises 2.39 and 2.40.
<!-- /worked-examples-table -->

## The derivative of a log, and the slope of a log density

<!-- worked-examples-table: derivative-of-a-log rev=1 -->
Problems on differentiating a logarithm, where $(\ln g)' = g'/g$ and a constant factor drops out, up to the slope of a Gaussian's log density, from the easiest to the hardest:

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | Differentiate $\ln(x^2 + 1)$ | Worked example | [[calculus-textbook.pdf#page=217\|Anton, Calculus, section 3.2, Example 2, PDF p. 217]] | Easy | In the book, PDF p. 217: $2x/(x^2 + 1)$ | quiz 0, KF1 |
| 2 | Differentiate $\ln 5x$ and $\ln x^2$, and see the 5 drop out | Exercise with the book's solution (answers only) | [[calculus-textbook.pdf#page=219\|Anton, Calculus, exercises 3.2 #1 and #9, PDF p. 219]] | Easy | Answers $1/x$ and $2/x$ at PDF p. 1245; the steps in [KF2 in the quiz 0 coverage file](/home-mscluster/mmolefe/PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/.quiz-prep/quiz-0.md#kf2-solution-the-log-of-a-constant-times-x) | quiz 0, KF2 |
| 3 | Differentiate the normal density: $P'(x) = -(x - \mu)P(x)/\sigma^2$, so $P'/P = -(x - \mu)/\sigma^2$ | Worked example | [[calculus-handbook.pdf#page=182\|Calculus handbook, inflection points of the normal density, PDF p. 182]] | Medium | In the book, PDF p. 182, every step | quiz 0, KF3 |
| 4 | The maximum-likelihood mean of Gaussian data with $\sigma = 1$: differentiate the log-likelihood, where $-(N/2)\log 2\pi$ drops | Exercise with the book's solution | [[introduction-to-probability-for-data-science.pdf#page=491\|Chan, Practice Exercise 8.2, PDF p. 491]] | Medium | In the book, PDF p. 491, every step: $\hat\theta = \tfrac1N \sum x_n$ | quiz 0, KF4 |

The Gaussian score in $x$ itself, and Chan's Practice Exercise 8.5, are banked by quiz 1.1 in [[#The score of a Gaussian]]. Not banked: Bishop's Exercise 1.11 (PDF p. 78), which prints no solution.
Read in full (by the bank search for quiz 0): Anton PDF pp. 217 to 219 and 1245; calculus practice problems PDF pp. 70, 71, 270 and 277; calculus handbook PDF p. 182; Chan PDF pp. 486, 491, 492, 500 and 523; Bishop PDF pp. 46 and 78. Only found: calculus practice problems #386 to #389.
<!-- /worked-examples-table -->

## The moment generating function

<!-- worked-examples-table: moment-generating-function rev=1 -->
Problems on the moment generating function, from computing one on a list of values to proving the central limit theorem with it on coin flips, from the easiest to the hardest:

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | The fingerprint of a variable on 0, 1 and 2 with masses 2/6, 3/6 and 1/6 | Worked example | [[introduction-to-probability-for-data-science.pdf#page=340\|Chan, Example 6.1, PDF pp. 340 to 341]] | Easy | In the book, PDF p. 341: $1/3 + e^s/2 + e^{2s}/6$; the value at $s = 1$ is worked on the quiz page | MGF quiz, P1 |
| 2 | The first two moments of a Bernoulli variable from $1 - p + pe^s$ | Exercise with the book's solution | [[introduction-to-probability-for-data-science.pdf#page=342\|Chan, Practice Exercise 6.3, PDF p. 342]] | Easy | In the book, PDF p. 342, by derivatives at 0: $E[X] = E[X^2] = p$; the series route is on the quiz page | MGF quiz, P2 |
| 3 | A sum of $N$ independent Bernoulli($p$) variables is Binomial($N$, $p$), by matching fingerprints | Worked example (a theorem with its proof) | [[introduction-to-probability-for-data-science.pdf#page=343\|Chan, Theorem 6.3, PDF pp. 343 to 344]] | Medium | In the book, PDF pp. 343 to 344, every step; its sum on p. 344 runs over $n$ where the terms use $k$ | MGF quiz, P3 |
| 4 | The fingerprint of $Y = aX + b$ is $e^{bt}M_X(at)$, used on $3 + 2\varepsilon$ | Exercise without a solution | [[introduction-to-statistics.pdf#page=83\|Introduction to Statistics, section 4.3, property 4 under Definition 12, PDF p. 83]] | Medium | None in the book; written on the quiz page with a check against Chan's Table 6.1 | MGF quiz, P4 |
| 5 | A sum of independent Gaussians is Gaussian, with the means and the variances added | Worked example (a theorem with its proof) | [[introduction-to-probability-for-data-science.pdf#page=345\|Chan, Theorem 6.6, PDF p. 345]] | Medium | In the book, PDF p. 345, taking the Gaussian fingerprint as given; restated on two variables with numbers on the quiz page | MGF quiz, P5 |
| 6 | How fast the fingerprint of $Y_n = \frac{1}{\sqrt n}\sum c_i$, for fair $\pm 1$ coins, approaches $e^{s^2/2}$ | Exercise without a solution (video only) | [[introduction-to-probability-for-data-science.pdf#page=403\|Chan, chapter 6 problems, Exercise 20, PDF pp. 403 to 404]] | Hard | None in the book; written on the quiz page, $n = 3$ and $n = 4$ worked | MGF quiz, P6 |
| 7 | Exercise 20 itself: $E[Y_n] = 0$, $\mathrm{Var}[Y_n] = 1$, and $M_{Y_n}(s) \to e^{s^2/2}$ by the limit Chan uses on PDF p. 390 | Exercise without a solution (video only) | [[introduction-to-probability-for-data-science.pdf#page=403\|Chan, chapter 6 problems, Exercise 20, PDF pp. 403 to 404]] | Hard | None in the book; written on the quiz page, with the limit step of [[introduction-to-probability-for-data-science.pdf#page=390\|Chan's proof of the central limit theorem, PDF p. 390]] | MGF quiz, P7 |

The note that teaches the concept is [[Moment Generating Function]]. Exercise 20 is on PDF pp. 403 to 404 (printed 387 to 388); PDF pp. 387 to 388 hold the central limit theorem's own text. Not banked: Chan's Practice Exercises 6.1 and 6.2 (the Poisson and exponential fingerprints, PDF p. 341) and Theorems 6.4 and 6.5 (sums of binomials and of Poissons, PDF p. 344), each with the book's solution, kept as further practice.
Read in full (by the coverage audit of the moment generating function quiz): Chan PDF pp. 22, 280, 340 to 345, 387 to 391, 403 and 404; Introduction to Statistics PDF pp. 82 to 84. Only found: Chan's characteristic-function pages, PDF pp. 345 to 346.
<!-- /worked-examples-table -->
