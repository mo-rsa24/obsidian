# Video Lessons

The reference shelf for the moment a derivation stalls on a word a video could teach: an integral, a marginal, a gradient, a noise schedule written as code. Each section below holds one short table of timestamped segments for one concept, in the order to watch, tagged intuition, worked example, proof or code walk. It sits beside the [[Textbooks]] shelf, which links the same words to book pages, and belongs to the [[Mathematics]] map.

## How a table is kept here

**This note holds the source.** The text between the two comment lines of a section is the one copy that is edited. The plans and chapters that use the concept carry the same block right after the paragraph where the word first appears, so the table is one click away in the work and one note away for browsing.

**The revision number goes up by one each time a table changes.** The video-pulse skill run with `--sync` compares every copy with its source and brings them level.

**Times are either read from captions or taken from the video's chapter list.** Each table says which in its last line. Captions are automatic, so a caption-read time is good to about 30 seconds, and a chapter-timed row is good to the chapter.

## Contents

- [[#Substituting a new variable into an integral (u-substitution)]]
- [[#Area under a curve, and the integral over the whole line]]
- [[#Integration by parts]]
- [[#Double integrals and iterated integrals]]
- [[#When an integral to infinity diverges]]
- [[#The Gaussian integral]]
- [[#The gradient]]
- [[#Completing the square]]
- [[#A density integrates to 1]]
- [[#Expectation and marginals]]
- [[#Conditional expectation]]
- [[#KL divergence]]
- [[#The score function]]
- [[#Langevin sampling]]
- [[#Denoising score matching]]
- [[#The noise schedule written as code]]
- [[#The reverse step and the sampler loop]]
- [[#The epsilon loss written as code]]
- [[#The multivariate normal and its covariance matrix]]
- [[#Adding two independent Gaussians]]
- [[#NumPy arrays against Python lists]]
- [[#The forward process]]
- [[#Products of experts]]
- [[#Energy-based models and the partition function]]
- [[#Markov chain Monte Carlo]]
- [[#The Metropolis-Hastings accept step]]
- [[#Annealed Langevin sampling]]
- [[#Classifier-free guidance]]
- [[#Bayes' theorem]]
- [[#Estimating a number by simulation (Monte Carlo)]]
- [[#Inverse transform sampling]]
- [[#Accept-reject sampling]]
- [[#A Metropolis chain, drawn step by step]]
- [[#Tuning a Metropolis chain]]

## Substituting a new variable into an integral (u-substitution)

<!-- video-table: u-substitution rev=1 -->
Professor Leonard and the Organic Chemistry Tutor on u-substitution, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What substituting u does to an integral, the steps, and how to choose u | Intuition | [Leonard, Calculus 1, 4.2, 0:00 to 6:13](https://www.youtube.com/watch?v=aiBD9aI69C8&t=0s) |
| 2 | Transform the integral, solve it in u, then evaluate the new integral | Worked example | [Leonard, Calculus 1, 4.2, 6:13 to 14:07](https://www.youtube.com/watch?v=aiBD9aI69C8&t=373s) |
| 3 | An integrand of the form e to a function of x | Worked example | [Organic Chemistry Tutor, U-Substitution, 3:53 to 5:47](https://www.youtube.com/watch?v=sdYdnpYn-1o&t=233s) |
| 4 | A plain linear substitution, the shift u = x minus a | Worked example | [Organic Chemistry Tutor, U-Substitution, 11:39 to 13:38](https://www.youtube.com/watch?v=sdYdnpYn-1o&t=699s) |
| 5 | A definite integral, changing the bounds into u so no back-substitution is needed | Worked example | [Organic Chemistry Tutor, U-Substitution With Definite Integrals, 0:00 to 6:48](https://www.youtube.com/watch?v=tM4RWc9ryx0&t=0s) |

No video found proves the rule as the chain rule run backwards, and none works a substitution inside a double integral. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Area under a curve, and the integral over the whole line

<!-- video-table: area-and-whole-line-integrals rev=1 -->
Professor Leonard on the integral in that last check (area under a curve, then the integral over the whole line), in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Area under a curve as a limit of rectangles, and why the sum becomes an integral | Definition | [Calculus 1, 4.3, 22:51 to 53:00](https://www.youtube.com/watch?v=F0uuW-I6icY&t=1371s) |
| 2 | Area under x² on [0, 1] as a limit, which comes to 1/3 | Worked example | [Calculus 1, 4.3, 1:05:50 to 1:22:30](https://www.youtube.com/watch?v=F0uuW-I6icY&t=3950s) |
| 3 | Plug the bounds into the antiderivative, with no +C | Definition | [Calculus 1, 4.5, 0:01 to 8:00](https://www.youtube.com/watch?v=xjtEfS0vY2o&t=1s) |
| 4 | Why an infinite bound makes an integral improper | Definition | [Calculus 2, 7.6, 0:00 to 7:30](https://www.youtube.com/watch?v=g-M8FHslgdk&t=1s) |
| 5 | Replace the infinity by b, take a limit, and read convergent or divergent | Definition | [Calculus 2, 7.6, 15:00 to 24:30](https://www.youtube.com/watch?v=g-M8FHslgdk&t=900s) |
| 6 | An integral over (−∞, ∞): split at a point and take two limits | Worked example | [Calculus 2, 7.6, 1:19:30 to 1:34:00](https://www.youtube.com/watch?v=g-M8FHslgdk&t=4770s) |

Leonard has no video on a density integrating to 1 or on the Gaussian integral itself. Timestamps come from his auto-generated captions and are good to about 30 seconds.
<!-- /video-table -->

## Integration by parts

<!-- video-table: integration-by-parts rev=2 -->
Professor Leonard on integration by parts, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The formula, derived by integrating the product rule | Proof | [Calculus 2, 7.1, 0:31 to 8:15](https://www.youtube.com/watch?v=EOwjiFpDY_s&t=31s) |
| 2 | Choosing u and v, then x eˣ worked through | Worked example | [Calculus 2, 7.1, 8:27 to 17:00](https://www.youtube.com/watch?v=EOwjiFpDY_s&t=507s) |
| 3 | ln x from 1 to e, with the uv term evaluated at the bounds | Worked example | [Calculus 2, 7.1, 58:45 to 1:05:30](https://www.youtube.com/watch?v=EOwjiFpDY_s&t=3525s) |
| 4 | Parts twice, until the integral comes back and can be solved for | Worked example | [Calculus 2, 7.1, 46:00 to 50:00](https://www.youtube.com/watch?v=EOwjiFpDY_s&t=2760s) |
| 5 | The uv term vanishing at infinity: x eˣ from −∞ to 0. This is the boundary assumption in integration by parts | Worked example | [Calculus 2, 7.6, 1:00:00 to 1:17:00](https://www.youtube.com/watch?v=g-M8FHslgdk&t=3600s) |

These are single-variable. The score-matching derivation applies the same idea in each coordinate with the others held fixed, which Leonard does not cover. Timestamps are good to about 30 seconds.
<!-- /video-table -->

## Double integrals and iterated integrals

<!-- video-table: double-and-iterated-integrals rev=1 -->
Professor Leonard on double integrals and on doing them as two single integrals, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What a double integral measures and why it is a limit of sums over small rectangles | Intuition | [Calculus 3, 14.1, 10:43 to 30:15](https://www.youtube.com/watch?v=lv_awaaT6gY&t=643s) |
| 2 | Fubini: a double integral can be done as two single integrals, in either order | Intuition | [Calculus 3, 14.2, 11:45 to 13:27](https://www.youtube.com/watch?v=HxRG_phgGUw&t=705s) |
| 3 | Evaluating a double integral as two single integrals, inner first | Worked example | [Calculus 3, 14.2, 13:27 to 20:32](https://www.youtube.com/watch?v=HxRG_phgGUw&t=807s) |
| 4 | Swapping the order of integration | Worked example | [Calculus 3, 14.2, 55:45 to 1:06:50](https://www.youtube.com/watch?v=HxRG_phgGUw&t=3345s) |
| 5 | A u-substitution used inside a double integral | Worked example | [Calculus 3, 14.2, 1:06:50 to 1:21:08](https://www.youtube.com/watch?v=HxRG_phgGUw&t=4010s) |

Leonard states Fubini and works it but does not prove it. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## When an integral to infinity diverges

<!-- video-table: diverging-integrals rev=1 -->
Professor Leonard on when an integral to infinity is finite and when it diverges, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Replace the infinity by b, take a limit, and read convergent or divergent | Definition | [Calculus 2, 7.6, 15:00 to 24:30](https://www.youtube.com/watch?v=g-M8FHslgdk&t=900s) |
| 2 | ∫ 1/xⁿ from 1 to ∞ converges for n above 1 and diverges for n at most 1 | Proof | [Calculus 2, 7.6, 31:20 to 43:30](https://www.youtube.com/watch?v=g-M8FHslgdk&t=1880s) |
| 3 | An integral over (−∞, ∞): split at a point and take two limits | Worked example | [Calculus 2, 7.6, 1:19:30 to 1:34:00](https://www.youtube.com/watch?v=g-M8FHslgdk&t=4770s) |

Leonard does not cover e^(−x²) converging against e^(+x²) diverging. Row 2 runs the same limit test on a simpler function. Timestamps are good to about 30 seconds.
<!-- /video-table -->

## The Gaussian integral

<!-- video-table: gaussian-integral rev=1 -->
Why the area under a Gaussian is exactly 1, which starts from the integral of e^(−x²) equalling √π, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Squaring the integral and turning it into a double integral over the plane | Proof | [3Blue1Brown, 3:44 to 12:47](https://www.youtube.com/watch?v=cy8r7WSuT1I&t=224s) |
| 2 | The same argument written out step by step on a board | Proof | [Prime Newtons, 1:33 to 14:02](https://www.youtube.com/watch?v=yM_7mrfRW0o&t=93s) |
| 3 | Why a polar double integral carries an extra factor of r, which the proof above needs | Proof | [Leonard, Calculus 3, 14.3, 15:07 to 22:25](https://www.youtube.com/watch?v=HA41kYxVYnw&t=907s) |

Leonard's lecture has no Gaussian example. Start and end times are chapter boundaries from each video; what is said inside was judged from the chapter titles and not read from captions.
<!-- /video-table -->

## The gradient

<!-- video-table: gradient rev=1 -->
The gradient as a vector, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Partial derivatives and the gradient as a vector, built up from a graph | Definition | [Professor Dave, 2:09 to 9:36](https://www.youtube.com/watch?v=AXH9Xm6Rbfc&t=129s) |
| 2 | Worked gradient problems | Worked example | [The Organic Chemistry Tutor, 12:34 to 28:29](https://www.youtube.com/watch?v=CnVes9TdnPo&t=754s) |
| 3 | The gradient defined, its properties, and why it points the way of fastest increase | Definition and proof | [Leonard, Calculus 3, 13.6, 58:26 to 1:15:15](https://www.youtube.com/watch?v=tDPp5uWSIiU&t=3506s) |

Start and end times are chapter boundaries from each video; what is said inside was judged from the chapter titles and not read from captions.
<!-- /video-table -->

## Completing the square

<!-- video-table: completing-the-square rev=1 -->
Professor Leonard on completing the square, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Why adding the square of half the middle coefficient makes a perfect square | Intuition | [Intermediate Algebra, 11.1, 42:45 to 50:09](https://www.youtube.com/watch?v=LnqXd2iDFWk&t=2565s) |
| 2 | The process step by step on quadratics | Worked example | [Intermediate Algebra, 11.1, 50:09 to 1:00:58](https://www.youtube.com/watch?v=LnqXd2iDFWk&t=3009s) |
| 3 | Fractions and an odd middle term | Worked example | [Intermediate Algebra, 11.1, 1:06:49 to 1:15:55](https://www.youtube.com/watch?v=LnqXd2iDFWk&t=4009s) |
| 4 | Completing the square when x squared has a coefficient a in front | Worked example | [Precalculus 19, 28:21 to 38:16](https://www.youtube.com/watch?v=pYSYL_vy6YQ&t=1701s) |

Leonard does not complete the square inside a Gaussian exponent, which is the form this journey uses. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## A density integrates to 1

<!-- video-table: density-integrates-to-one rev=1 -->
StatQuest and the Organic Chemistry Tutor on a density integrating to 1, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | A curve as a distribution, with probability read as area | Intuition | [StatQuest, Main Ideas behind Probability Distributions, 2:15 to 5:14](https://www.youtube.com/watch?v=oI3hZJqXJuc&t=135s) |
| 2 | Verify a function is a density by checking that its integral equals 1 | Worked example | [Organic Chemistry Tutor, Probability Density Functions, 0:52 to 3:39](https://www.youtube.com/watch?v=QKA4HNEw3aY&t=52s) |
| 3 | An exponential density integrated out to infinity, an improper integral | Worked example | [Organic Chemistry Tutor, Probability Density Functions, 8:06 to 11:46](https://www.youtube.com/watch?v=QKA4HNEw3aY&t=486s) |

No video found proves that a density integrates to 1; these check it for given functions. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Expectation and marginals

<!-- video-table: expectation-and-marginals rev=1 -->
The expectation and marginal this step uses, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Expectation of a function of a random variable | Definition | [Stanford CS229, lecture 3, 11:33 to 21:01](https://www.youtube.com/watch?v=Mi8wnYc1m04&t=693s) |
| 2 | Joint and marginal densities: integrating one variable out | Definition | [Stanford CS229, lecture 3, 23:01 to 26:37](https://www.youtube.com/watch?v=Mi8wnYc1m04&t=1381s) |

Start and end times are chapter boundaries from each video; what is said inside was judged from the chapter titles and not read from captions.
<!-- /video-table -->

## Conditional expectation

<!-- video-table: conditional-expectation rev=1 -->
Stanford CS229, then Nazer from the open web, on conditional expectation, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Conditional expectation of one variable given another | Intuition | [Stanford CS229, lecture 3, 50:45 to 59:28](https://www.youtube.com/watch?v=Mi8wnYc1m04&t=3045s) |
| 2 | The definition, and the conditional expectation as a function of the conditioning variable | Intuition, open web | [Nazer, Probability 4.7, 1:14 to 3:45](https://www.youtube.com/watch?v=86m-cizvK14&t=74s) |
| 3 | Law of total expectation, the average of conditional averages | Intuition, open web | [Nazer, Probability 4.7, 5:41 to 7:03](https://www.youtube.com/watch?v=86m-cizvK14&t=341s) |
| 4 | A continuous case solved with a conditional density | Worked example, open web | [Nazer, Probability 4.7, 11:35 to 13:31](https://www.youtube.com/watch?v=86m-cizvK14&t=695s) |

Rows 2 to 4 are from the open web (Nazer) because no listed creator has them, and none of these videos reaches the posterior mean of a Gaussian given a noisy observation. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## KL divergence

<!-- video-table: kl-divergence rev=1 -->
Serrano, ritvikmath and Stanford CS236 on the KL divergence, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Comparing two distributions by how likely the same data is under each, with a biased die | Intuition | [Serrano, KL Divergence, 0:00 to 3:43](https://www.youtube.com/watch?v=sjgZxuCm_8Q&t=0s) |
| 2 | The KL number computed from the die probabilities | Worked example | [Serrano, KL Divergence, 10:50 to 12:11](https://www.youtube.com/watch?v=sjgZxuCm_8Q&t=650s) |
| 3 | Why the formula has a ratio p over q, a log, and p out in front | Intuition | [ritvikmath, The KL Divergence, 1:57 to 15:59](https://www.youtube.com/watch?v=q0AkK8aYbLY&t=117s) |
| 4 | KL defined, then maximum likelihood shown to be minimising KL | Proof | [Stanford CS236, lecture 4, 39:00 to 54:49](https://www.youtube.com/watch?v=bt3dqcbMLa0&t=2340s) |

None of these derives the KL divergence between two Gaussians, which is the closed form this journey needs. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## The score function

<!-- video-table: score-function rev=1 -->
The score in lecture form, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The score function defined, as a vector field over data space | Definition | [Stanford CS236, lecture 13, 3:52 to 11:51](https://www.youtube.com/watch?v=8G-OsDs1RLI&t=232s) |

Start and end times are chapter boundaries from each video; what is said inside was judged from the chapter titles and not read from captions.
<!-- /video-table -->

## Langevin sampling

<!-- video-table: langevin-sampling rev=1 -->
Following the score uphill with noise added, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Following the score uphill with noise added: Langevin sampling | Definition | [Stanford CS236, lecture 16, 5:30 to 9:30](https://www.youtube.com/watch?v=VsllsC2JMGY&t=330s) |

Start and end times are chapter boundaries from each video; what is said inside was judged from the chapter titles and not read from captions.
<!-- /video-table -->

## Denoising score matching

<!-- video-table: denoising-score-matching rev=1 -->
Denoising score matching itself, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Denoising score matching, derived | Proof | [Stanford CS236, lecture 13, 29:16 to 44:39](https://www.youtube.com/watch?v=8G-OsDs1RLI&t=1756s) |

Start and end times are chapter boundaries from each video; what is said inside was judged from the chapter titles and not read from captions.
<!-- /video-table -->

## The noise schedule written as code

<!-- video-table: noise-schedule-as-code rev=1 -->
The schedule and forward process written as code, to compare against task 2.1:

| Order | What it covers | Kind | Code it writes | Watch |
|---|---|---|---|---|
| 1 | The beta schedule, abar_t, and noising an image in one closed-form step | Code walk | the noise schedule and the forward process | [Vizuara, DDPM practical, 13:08 to 18:43](https://www.youtube.com/watch?v=6to_EG3SJgs&t=788s) |

Start and end times are chapter boundaries from the video; what is said inside was judged from the chapter title and not read from captions.
<!-- /video-table -->

## The reverse step and the sampler loop

<!-- video-table: reverse-step-and-sampler rev=1 -->
The reverse step and sampler loop, in lecture and in code, to compare against task 2.2:

| Order | What it covers | Kind | Code it writes | Watch |
|---|---|---|---|---|
| 1 | Diffusion and the reverse process | Proof | | [Stanford CS236, lecture 16, 19:05 to 29:42](https://www.youtube.com/watch?v=VsllsC2JMGY&t=1145s) |
| 2 | The reverse loop from noise to image | Code walk | the sampler loop | [Vizuara, DDPM practical, 39:32 to 41:43](https://www.youtube.com/watch?v=6to_EG3SJgs&t=2372s) |
| 3 | Sampling function of a small DDPM | Code walk | the sampling function | [Umar Jamil, 13:00 to 21:11](https://www.youtube.com/watch?v=I1sPXkm2NH4&t=780s) |

Start and end times are chapter boundaries from each video; what is said inside was judged from the chapter titles and not read from captions.
<!-- /video-table -->

## The epsilon loss written as code

<!-- video-table: epsilon-loss-as-code rev=1 -->
The epsilon loss written as code, in the order to watch:

| Order | What it covers | Kind | Code it writes | Watch |
|---|---|---|---|---|
| 1 | Adding noise to a batch and training the network to predict that noise | Code walk | the training step | [Vizuara, DDPM practical, 30:07 to 39:32](https://www.youtube.com/watch?v=6to_EG3SJgs&t=1807s) |
| 2 | A small DDPM end to end, training function first | Code walk | the training function and the sampling function | [Umar Jamil, 13:00 to 21:11](https://www.youtube.com/watch?v=I1sPXkm2NH4&t=780s) |

Start and end times are chapter boundaries from each video; what is said inside was judged from the chapter titles and not read from captions.
<!-- /video-table -->

## The multivariate normal and its covariance matrix

<!-- video-table: multivariate-normal rev=1 -->
Stanford CS229, then ritvikmath, on the multivariate normal and its covariance matrix, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The multivariate Gaussian density, written with a mean vector and a covariance matrix | Intuition | [Stanford CS229, Autumn 2018, lecture 5, 8:11 to 18:57](https://www.youtube.com/watch?v=nt63k3bfXS0&t=491s) |
| 2 | What a covariance matrix holds: each coordinate's variance on the diagonal, each pair's covariance off it | Intuition | [ritvikmath, The Covariance Matrix, 2:40 to 5:23](https://www.youtube.com/watch?v=152tSYtiQbw&t=160s) |
| 3 | Computing a covariance matrix from data | Worked example | [ritvikmath, The Covariance Matrix, 5:23 to 10:59](https://www.youtube.com/watch?v=152tSYtiQbw&t=323s) |

Neither video takes a diagonal covariance apart into one bell per coordinate. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Adding two independent Gaussians

<!-- video-table: sum-of-independent-gaussians rev=1 -->
3Blue1Brown on why adding two independent Gaussians gives a Gaussian, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What computing the sum of two random variables directly would look like | Intuition | [3Blue1Brown, Gaussian + Gaussian = Gaussian, 2:10 to 3:38](https://www.youtube.com/watch?v=d_qvLDhkg00&t=130s) |
| 2 | A visual argument that the sum of two independent Gaussians is again a Gaussian | Proof | [3Blue1Brown, Gaussian + Gaussian = Gaussian, 3:38 to 8:27](https://www.youtube.com/watch?v=d_qvLDhkg00&t=218s) |

No listed creator works the variance rule Var(aX + bY) = a²Var(X) + b²Var(Y) for independent X and Y, which gives the forward process its square roots. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## NumPy arrays against Python lists

<!-- video-table: numpy-arrays rev=1 -->
freeCodeCamp's NumPy course on arrays against lists, in the order to watch:

| Order | What it covers | Kind | Code it writes | Watch |
|---|---|---|---|---|
| 1 | Why a NumPy array beats a Python list, in speed and in what it can do | Intuition | | [freeCodeCamp, Python NumPy Tutorial for Beginners, 1:35 to 9:17](https://www.youtube.com/watch?v=QUT1VHiLmmI&t=95s) |
| 2 | Making an array and reading its shape, size and data type | Code walk | `np.array` and its `.shape`, `.size`, `.dtype` | [freeCodeCamp, Python NumPy Tutorial for Beginners, 11:08 to 16:08](https://www.youtube.com/watch?v=QUT1VHiLmmI&t=668s) |
| 3 | Arithmetic that acts on every entry at once | Code walk | `+`, `*` and `/` between arrays | [freeCodeCamp, Python NumPy Tutorial for Beginners, 35:45 to 38:20](https://www.youtube.com/watch?v=QUT1VHiLmmI&t=2145s) |

The course does not cover broadcasting by name or the seeded generator `np.random.default_rng`; it draws random numbers with the older global `np.random` functions. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## The forward process

<!-- video-table: forward-process rev=1 -->
Stanford CS236, then Vizuara, on the forward process, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The noising process that turns data into noise | Intuition | [Stanford CS236, lecture 16, 12:22 to 16:23](https://www.youtube.com/watch?v=VsllsC2JMGY&t=742s) |
| 2 | Many small noising steps combined into one transition to any noise level | Proof | [Stanford CS236, lecture 16, 16:23 to 19:05](https://www.youtube.com/watch?v=VsllsC2JMGY&t=983s) |
| 3 | Why each step scales the mean down as well as adding noise | Intuition | [Vizuara, Principles of Diffusion Models, lecture 3, 33:51 to 42:46](https://www.youtube.com/watch?v=Dx-1agEjlJs&t=2031s) |

Vizuara is added for row 3, which no CS236 chapter covers; neither noises a two-dimensional Gaussian cloud and checks the closed form. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Products of experts

<!-- video-table: product-of-experts rev=1 -->
Stanford CS236 on multiplying models into a product of experts, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Composing normalised models into one | Intuition | [Stanford CS236, lecture 11, 23:01 to 29:14](https://www.youtube.com/watch?v=m61KiAMCJ5Q&t=1381s) |
| 2 | The product of experts | Intuition | [Stanford CS236, lecture 11, 54:02 to 57:28](https://www.youtube.com/watch?v=m61KiAMCJ5Q&t=3242s) |

Neither segment composes diffusion models by adding their scores or divides out a background, and no listed creator does. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Energy-based models and the partition function

<!-- video-table: energy-based-models rev=1 -->
Stanford CS236 on energy-based models and the normalising constant they leave out, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What an energy-based model is | Intuition | [Stanford CS236, lecture 11, 4:42 to 6:45](https://www.youtube.com/watch?v=m61KiAMCJ5Q&t=282s) |
| 2 | Why a probability model must be non-negative and integrate to 1 | Intuition | [Stanford CS236, lecture 11, 6:45 to 15:31](https://www.youtube.com/watch?v=m61KiAMCJ5Q&t=405s) |
| 3 | The partition function, the constant that makes an energy into a density | Intuition | [Stanford CS236, lecture 11, 15:31 to 23:01](https://www.youtube.com/watch?v=m61KiAMCJ5Q&t=931s) |

None of these works the area a product of two Gaussians loses. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Markov chain Monte Carlo

<!-- video-table: markov-chain-monte-carlo rev=1 -->
ritvikmath on Markov chain Monte Carlo, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Drawing samples by running a Markov chain whose long-run distribution is the target | Intuition | [ritvikmath, Markov Chain Monte Carlo, 4:07 to 8:24](https://www.youtube.com/watch?v=yApmR-c_hKU&t=247s) |
| 2 | The detailed balance condition | Proof | [ritvikmath, Markov Chain Monte Carlo, 8:24 to 12:10](https://www.youtube.com/watch?v=yApmR-c_hKU&t=504s) |

Neither segment anneals a chain across noise levels or uses a gradient in its proposal. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## The Metropolis-Hastings accept step

<!-- video-table: metropolis-hastings rev=1 -->
ritvikmath, then Stanford CS236, on the Metropolis-Hastings accept step, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Working out the acceptance probability for a candidate | Proof | [ritvikmath, Metropolis-Hastings, 7:50 to 12:04](https://www.youtube.com/watch?v=yCv2N7wGDCw&t=470s) |
| 2 | Accepting or rejecting the candidate with that probability | Intuition | [ritvikmath, Metropolis-Hastings, 12:04 to 13:31](https://www.youtube.com/watch?v=yCv2N7wGDCw&t=724s) |
| 3 | The Metropolis algorithm, the special case with a symmetric proposal | Intuition | [ritvikmath, Metropolis-Hastings, 13:31 to 18:15](https://www.youtube.com/watch?v=yCv2N7wGDCw&t=811s) |
| 4 | Sampling an energy-based model with MCMC, accepting or rejecting each move | Intuition | [Stanford CS236, lecture 12, 8:35 to 16:25](https://www.youtube.com/watch?v=Nci1Bepcy0g&t=515s) |

None of these uses a Langevin step as the proposal (MALA) or reads the share of proposals accepted. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Annealed Langevin sampling

<!-- video-table: annealed-langevin rev=1 -->
Stanford CS236 on why Langevin sampling is annealed across noise levels, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Where plain Langevin sampling fails | Intuition | [Stanford CS236, lecture 14, 5:44 to 9:13](https://www.youtube.com/watch?v=E69Lp_T9nVg&t=344s) |
| 2 | What adding noise does for the score and for sampling | Intuition | [Stanford CS236, lecture 14, 9:13 to 19:08](https://www.youtube.com/watch?v=E69Lp_T9nVg&t=553s) |
| 3 | Sampling across many noise scales, noisiest first | Intuition | [Stanford CS236, lecture 14, 23:54 to 28:43](https://www.youtube.com/watch?v=E69Lp_T9nVg&t=1434s) |

CS236 anneals one model's score; it does not anneal a sum of two models' scores, which is what composition samples. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Classifier-free guidance

<!-- video-table: classifier-free-guidance rev=1 -->
Umar Jamil on classifier-free guidance:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Classifier-free guidance, and how it steers sampling toward the prompt | Intuition | [Umar Jamil, Coding Stable Diffusion from scratch, 22:20 to 31:00](https://www.youtube.com/watch?v=ZBKpAp_6TGI&t=1340s) |

Umar Jamil does not write guidance as a product of two experts or the guidance scale as a power. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Bayes' theorem

<!-- video-table: bayes-theorem rev=1 -->
3Blue1Brown, then StatQuest, on Bayes' theorem, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | From a worked example to the general formula | Intuition | [3Blue1Brown, Bayes theorem, the geometry of changing beliefs, 4:09 to 10:13](https://www.youtube.com/watch?v=HZGCoVF3YvM&t=249s) |
| 2 | Bayes' theorem derived step by step | Proof | [StatQuest, Bayes' Theorem, Clearly Explained, 5:21 to 9:12](https://www.youtube.com/watch?v=9wCnvr7Xw4E&t=321s) |

Both work with events, not densities, so neither divides a conditional density by a prior the way the composition rule does. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Estimating a number by simulation (Monte Carlo)

<!-- video-table: monte-carlo-estimate rev=1 -->
ritvikmath on estimating a number by simulation, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Darts in a square: the fraction landing in the circle estimates π/4, with the loop written as pseudocode | Worked example | [ritvikmath, Monte Carlo Simulations, 0:23 to 4:50](https://www.youtube.com/watch?v=EaR3C4e600k&t=23s) |
| 2 | The expected number of rounds until two losses in a row, derived by conditioning on the first rounds to (2 − p)/(1 − p)² | Proof | [ritvikmath, Monte Carlo Simulations, 4:50 to 9:28](https://www.youtube.com/watch?v=EaR3C4e600k&t=290s) |
| 3 | The same expectation by simulating a million games and averaging, against the exact 6 at p = 1/2 | Worked example, use case | [ritvikmath, Monte Carlo Simulations, 9:28 to 13:32](https://www.youtube.com/watch?v=EaR3C4e600k&t=568s) |
| 4 | When to reach for it, and why it slows down as p nears 1 | Intuition | [ritvikmath, Monte Carlo Simulations, 13:32 to 16:22](https://www.youtube.com/watch?v=EaR3C4e600k&t=812s) |
| 5 | One run answers one parameter value, and the number alone does not show where it came from | Intuition | [ritvikmath, Monte Carlo Simulations, 16:22 to 19:01](https://www.youtube.com/watch?v=EaR3C4e600k&t=982s) |

ritvikmath does not cover how fast the error shrinks as samples are added, or weighting samples drawn from a different distribution, which is what an importance-sampling estimate does. Times are read from the video's automatic captions and are good to about 30 seconds.
<!-- /video-table -->

## Inverse transform sampling

<!-- video-table: inverse-transform-sampling rev=1 -->
ritvikmath on inverse transform sampling, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Inverse transform sampling, the idea | Intuition | [ritvikmath, Inverse Transform Sampling, 0:07 to 1:39](https://www.youtube.com/watch?v=9ixzzPQWuAY&t=7s) |
| 2 | The uniform and the exponential distributions the example uses | Definition | [ritvikmath, Inverse Transform Sampling, 1:39 to 2:36](https://www.youtube.com/watch?v=9ixzzPQWuAY&t=99s) |
| 3 | The cumulative distribution function | Definition | [ritvikmath, Inverse Transform Sampling, 2:36 to 7:54](https://www.youtube.com/watch?v=9ixzzPQWuAY&t=156s) |
| 4 | Inverting the exponential CDF, and turning a uniform draw into an exponential one | Worked example | [ritvikmath, Inverse Transform Sampling, 7:54 to 10:04](https://www.youtube.com/watch?v=9ixzzPQWuAY&t=474s) |

The creator's own description says the exponential density on the board is missing its λ in front. Times are chapter boundaries read from the video's chapter list, because YouTube refused its captions on 2026-10-17; what is said inside was judged from the chapter titles and not read.
<!-- /video-table -->

## Accept-reject sampling

<!-- video-table: accept-reject-sampling rev=1 -->
ritvikmath on accept-reject sampling, which draws from a density known only up to its normalising constant, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Why accept-reject: inverse transform needs the CDF and its inverse, and this needs neither, nor the full density | Intuition | [ritvikmath, Accept-Reject Sampling, 0:00 to 1:09](https://www.youtube.com/watch?v=OXDqjdVVePY&t=0s) |
| 2 | Student exam scores whose density is known only up to its normalising constant, and why that integral is out of reach | Intuition, use case | [ritvikmath, Accept-Reject Sampling, 1:09 to 3:52](https://www.youtube.com/watch?v=OXDqjdVVePY&t=69s) |
| 3 | The method: an easy proposal g scaled by M into an envelope above f, then accept each draw with probability f/(M g) | Definition | [ritvikmath, Accept-Reject Sampling, 3:52 to 7:45](https://www.youtube.com/watch?v=OXDqjdVVePY&t=232s) |
| 4 | Bayes' rule shows the accepted draws have density f/NC; the overall acceptance probability NC/M comes out on the way | Proof | [ritvikmath, Accept-Reject Sampling, 8:05 to 12:04](https://www.youtube.com/watch?v=OXDqjdVVePY&t=485s) |
| 5 | Why it works: f/g is high for a point the target likes and the proposal rarely offers | Intuition | [ritvikmath, Accept-Reject Sampling, 12:28 to 15:10](https://www.youtube.com/watch?v=OXDqjdVVePY&t=748s) |
| 6 | A spiky target forces a huge M, so NC/M nears 0 and the sampler stalls | Intuition | [ritvikmath, Accept-Reject Sampling, 15:10 to 17:12](https://www.youtube.com/watch?v=OXDqjdVVePY&t=910s) |

ritvikmath never runs the exam-score example with numbers, and covers the CDF method row 1 contrasts against in his [inverse transform video](https://www.youtube.com/watch?v=9ixzzPQWuAY). Times are read from the video's automatic captions and are good to about 30 seconds.
<!-- /video-table -->

## A Metropolis chain, drawn step by step

<!-- video-table: metropolis-chain-drawn rev=1 -->
DataMListic on one Metropolis-Hastings chain, drawn step by step, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Proposing a new state from a symmetric proposal around the current one | Intuition | [DataMListic, Metropolis-Hastings Explained, 0:23 to 0:46](https://www.youtube.com/watch?v=7IpvsfRgTTY&t=23s) |
| 2 | Accept or reject: the acceptance probability is the minimum of 1 and the density ratio | Definition | [DataMListic, Metropolis-Hastings Explained, 0:46 to 1:12](https://www.youtube.com/watch?v=7IpvsfRgTTY&t=46s) |
| 3 | A chain run on a heat map: proposals turn green or red, and the samples gather where the density is high | Intuition | [DataMListic, Metropolis-Hastings Explained, 1:12 to 1:37](https://www.youtube.com/watch?v=7IpvsfRgTTY&t=72s) |
| 4 | Detailed balance as two probability flows between a pair of states, flow out equal to flow in | Intuition | [DataMListic, Metropolis-Hastings Explained, 1:37 to 2:00](https://www.youtube.com/watch?v=7IpvsfRgTTY&t=97s) |

DataMListic uses only a symmetric proposal, so the proposal-density ratio an asymmetric move needs never appears, and nothing is worked with numbers; the user supplied this video, and DataMListic is not on the creator list. Times are the video's own chapter boundaries, checked against its automatic captions to within a few seconds.
<!-- /video-table -->

## Tuning a Metropolis chain

<!-- video-table: tuning-a-metropolis-chain rev=1 -->
DataMListic on tuning a Metropolis chain, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Step sizes too small, too large and just right, and the 20 to 50 percent acceptance-rate target | Intuition | [DataMListic, Metropolis-Hastings Explained, 2:00 to 2:22](https://www.youtube.com/watch?v=7IpvsfRgTTY&t=120s) |
| 2 | Burn-in: discard the early samples so the chain forgets where it started | Intuition | [DataMListic, Metropolis-Hastings Explained, 2:22 to 2:34](https://www.youtube.com/watch?v=7IpvsfRgTTY&t=142s) |

DataMListic states the 20 to 50 percent rule without deriving it and never mentions effective sample size; the user supplied this video, and DataMListic is not on the creator list. Times are the video's own chapter boundaries, checked against its automatic captions to within a few seconds.
<!-- /video-table -->
