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
- [[#The product of two Gaussians and the precision-weighted mean]]
- [[#The Gaussian mixture model]]
- [[#The product of two Gaussian mixtures]]
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
- [[#The arithmetic mean is at least the geometric mean (two numbers)]]
- [[#The correlation coefficient]]
- [[#The phi and Matthews correlation coefficient (a 2 by 2 table)]]
- [[#The bootstrap]]
- [[#Solving an inequality with the unknown in the exponent]]
- [[#Inverse transform sampling worked on the exponential]]
- [[#The noise prediction is the score, rescaled]]
- [[#Score matching]]
- [[#The kernel density estimate]]
- [[#Total variation distance]]
- [[#Compound interest, the annuity formula and the Rule of 72]]
- [[#Nominal against effective interest rates]]
- [[#Real return after inflation]]
- [[#The amortizing loan payment]]
- [[#Paying down a bond against investing]]
- [[#The access bond]]
- [[#The repo rate and the prime rate]]
- [[#The South African credit score]]
- [[#Home-loan affordability]]
- [[#Renting against buying]]
- [[#The primary residence exclusion]]
- [[#Net worth and the balance sheet]]
- [[#The savings rate]]
- [[#The emergency fund and sinking funds]]
- [[#Budgeting methods]]
- [[#Choosing a South African bank account]]
- [[#Savings accounts, notice deposits and fixed deposits]]
- [[#Money market funds against money market accounts and income funds]]
- [[#Asset classes]]
- [[#Volatility and the standard deviation]]
- [[#Diversification]]
- [[#The compound annual growth rate]]
- [[#Asset allocation]]
- [[#Rebalancing a portfolio]]
- [[#Index funds and ETFs]]
- [[#The unit trust against the ETF]]
- [[#Investment fees and the TER]]
- [[#South African investment platforms]]
- [[#The effective annual cost and early exit charges]]
- [[#How financial advisers are paid]]
- [[#The tax-free savings account]]
- [[#The retirement annuity]]
- [[#The TFSA against the retirement annuity]]
- [[#A retirement annuity against investing outside one]]
- [[#The provident fund and the two-pot system]]
- [[#The section 54 endowment]]
- [[#Life cover premium patterns]]
- [[#Marital regimes, wills and estate duty]]
- [[#Marginal against effective tax rate]]
- [[#South African tax brackets and rebates]]
- [[#South African capital gains tax]]
- [[#Medical tax credits]]
- [[#Filing the ITR12]]
- [[#Provisional tax]]
- [[#South African business structures]]
- [[#Double-entry bookkeeping]]
- [[#The three financial statements]]
- [[#Salary against dividend from a company]]
- [[#South African VAT]]

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

## The product of two Gaussians and the precision-weighted mean

<!-- video-table: product-of-two-gaussians rev=1 -->
Michel van Biezen, then Robert Ghrist from the open web, on multiplying two Gaussians, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The gain is the estimate's error over the sum of both errors, and the new value moves toward the reading by that share, so the surer of the two pulls harder | Intuition | [Van Biezen, Kalman Filter 3 of 55, 0:28 to 3:51](https://www.youtube.com/watch?v=fpRb1sjFz_M&t=28s) |
| 2 | One update with numbers: an estimate of 68 with error 2 and a reading of 75 with error 4 give 70.33 with error 1.33 | Worked example | [Van Biezen, Kalman Filter 6 of 55, 0:13 to 2:14](https://www.youtube.com/watch?v=SIQJaqYVtuE&t=13s) |
| 3 | The product of two one-dimensional Gaussians is a scaled Gaussian, found by simplifying the quadratic in the exponent | Proof, open web | [Ghrist, CalcBLUE 3, 18.4, 0:26 to 4:10](https://www.youtube.com/watch?v=lUORBdNccHc&t=26s) |
| 4 | The same product in several dimensions | Proof, open web | [Ghrist, CalcBLUE 3, 18.4, 4:10 to 5:53](https://www.youtube.com/watch?v=lUORBdNccHc&t=250s) |

Van Biezen works the product as a Kalman filter update and calls the two variances errors: his old value plus the gain times the difference is the precision-weighted mean rearranged, and his new error of 1.33 from 2 and 4 is the two precisions added. No listed creator derives the product of two Gaussian densities, so rows 3 and 4 come from the open web, and no row was found that computes the overlap Z. Rows 1 and 2 are read from automatic captions and good to about 30 seconds; rows 3 and 4 are chapter boundaries, so the sentence inside each is not checked.
<!-- /video-table -->

## The Gaussian mixture model

<!-- video-table: gaussian-mixture rev=1 -->
ritvikmath on the Gaussian mixture model, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Each class is its own Gaussian with a mean and a covariance, and π is the share of the data in each class | Intuition | [ritvikmath, Gaussian Mixture Model, 0:31 to 3:33](https://www.youtube.com/watch?v=EWd1xRkyEog&t=31s) |
| 2 | The density of one fish: π for tuna times the tuna Gaussian, plus π for salmon times the salmon Gaussian, because the fish came from one or the other | Worked example | [ritvikmath, Gaussian Mixture Model, 3:36 to 6:23](https://www.youtube.com/watch?v=EWd1xRkyEog&t=216s) |
| 3 | The same sum written for K components | Intuition | [ritvikmath, Gaussian Mixture Model, 7:58 to 8:43](https://www.youtube.com/watch?v=EWd1xRkyEog&t=478s) |

He goes on to fit the mixture with the EM algorithm, which composing experts does not need, and he never multiplies or noises a mixture. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## The product of two Gaussian mixtures

<!-- video-table: product-of-two-mixtures rev=1 -->
Chalmers' multiple object tracking course, from the open web, on multiplying a Gaussian mixture by a second factor, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Every pair of an old component and a measurement hypothesis becomes one new component, weighted by the old weight times an integral and normalised over all pairs | Intuition, open web | [Chalmers, Gaussian Sum Filtering: Prediction and Update, 2:38 to 3:38](https://www.youtube.com/watch?v=G_X_dMZUkdI&t=158s) |
| 2 | With Gaussian factors the integral is the predicted likelihood, which is the pair's overlap, and each new component's mean and covariance come from a Kalman update | Intuition, open web | [Chalmers, Gaussian Sum Filtering: Prediction and Update, 4:20 to 5:15](https://www.youtube.com/watch?v=G_X_dMZUkdI&t=260s) |
| 3 | Two components and two hypotheses give four numbered components | Worked example, open web | [Chalmers, Gaussian Sum Filtering: Prediction and Update, 6:05 to 7:04](https://www.youtube.com/watch?v=G_X_dMZUkdI&t=365s) |

No listed creator multiplies two mixtures. The second factor in this lecture is a measurement model with a detection probability and clutter rather than a second expert, so read each measurement hypothesis as one component of the second mixture; the Kalman update is the product of the pair's two Gaussians. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## The arithmetic mean is at least the geometric mean (two numbers)

<!-- video-table: am-gm-two-numbers rev=1 -->
MathOdyssey, then David Metzler, both from the open web, on the proof that (a + b)/2 is at least the square root of ab, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Subtract the geometric mean from the arithmetic mean, write a and b as squares of their roots, and the difference becomes (root a minus root b) squared over 2, which cannot be negative; equality only when a equals b | Proof, open web | [MathOdyssey, Proof of AM-GM for two positive numbers, 0:16 to 3:05](https://www.youtube.com/watch?v=8sMtm9JfMfI&t=16s) |
| 2 | Square both sides to find a hint, reach (a minus b) squared at least 0, then run the steps forwards as the proof | Proof, open web | [Metzler, Proof example: AM-GM Inequality, 4:35 to 7:58](https://www.youtube.com/watch?v=MVSmvLyowt0&t=275s) |

No listed creator proves the inequality, and no worked example with numbers was found. Metzler also shows how to find the proof (1:20 to 4:35) and proves that square roots keep an inequality (8:13 to 9:51). Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## The correlation coefficient

<!-- video-table: correlation-coefficient rev=1 -->
Mahesh Huddar, then StatQuest, on Pearson's correlation (covariance over the two standard deviations), in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Correlation runs from minus 1 to 1: perfect positive, perfect negative, and no linear relationship at 0 | Intuition | [Mahesh Huddar, How to find the coefficient of correlation, 0:31 to 2:23](https://www.youtube.com/watch?v=bXlYuKFGsZY&t=31s) |
| 2 | Four data points: the two means, the covariance, both variances, and r = covariance over root variance times root variance, which comes out 0 | Worked example | [Mahesh Huddar, How to find the coefficient of correlation, 2:23 to 6:10](https://www.youtube.com/watch?v=bXlYuKFGsZY&t=143s) |
| 3 | The denominator squeezes covariance into minus 1 to 1; covariance 116 with variances 101.8 and 160.3 gives 0.9 | Worked example | [StatQuest, Pearson's Correlation, Clearly Explained, 13:37 to 16:04](https://www.youtube.com/watch?v=xZ_z8KWkhXE&t=817s) |

Mahesh Huddar's example ends at 0, so it shows the arithmetic but not a strong relationship; StatQuest supplies the nonzero answer and assumes his variance and covariance videos. Neither proves that r stays between minus 1 and 1. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## The phi and Matthews correlation coefficient (a 2 by 2 table)

<!-- video-table: phi-matthews-correlation rev=1 -->
Pedram Jahangiry, from the open web, on the Matthews correlation coefficient of a confusion matrix, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The coefficient is the correlation between actual and predicted: true positive times true negative minus false positive times false negative, over the square root of the four pair sums; it runs from minus 1 to 1 | Intuition, open web | [Jahangiry, Performance metrics for classification models, 16:22 to 18:24](https://www.youtube.com/watch?v=IDPmX6xT3Us&t=982s) |
| 2 | 100 cases with 2 defaulters and a model that always says no default: accuracy 98 percent, precision, recall and F1 all 0, and the coefficient read as 0 | Worked example, open web | [Jahangiry, Performance metrics for classification models, 18:54 to 20:30](https://www.youtube.com/watch?v=IDPmX6xT3Us&t=1134s) |

Nothing on Mahesh Huddar's channel covers the phi or Matthews coefficient, and no video on a listed creator does. The example skips the arithmetic of the denominator: with that table it is 0, so the coefficient is undefined and conventionally set to 0. He does not name the phi coefficient, which is the same quantity for any two yes-or-no columns. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## The bootstrap

<!-- video-table: bootstrap-resampling rev=1 -->
StatQuest, then Joshua French from the open web, on the bootstrap (resampling a data set with replacement to get a standard error or an interval), in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Eight patients with a mean response of 0.5, and why repeating the whole experiment to see how far that mean moves is too costly | Intuition | [StatQuest, Bootstrapping Main Ideas, 0:17 to 2:18](https://www.youtube.com/watch?v=Xz0x-8-cgaQ&t=17s) |
| 2 | Draw from the eight values eight times with replacement, take the mean, repeat thousands of times; the four steps and the name for sampling with replacement | Worked example | [StatQuest, Bootstrapping Main Ideas, 2:18 to 5:22](https://www.youtube.com/watch?v=Xz0x-8-cgaQ&t=138s) |
| 3 | The standard error is the standard deviation of the bootstrap means; a 95 percent interval is the stretch that covers 95 percent of them | Definition | [StatQuest, Bootstrapping Main Ideas, 6:30 to 7:02](https://www.youtube.com/watch?v=Xz0x-8-cgaQ&t=390s) |
| 4 | A sample of numbers, 1000 resamples in R, the 2.5 and 97.5 percent quantiles of the resample means, and the interval 2.44 to 4.98 for a true mean of 3 | Worked example, code walk, open web | [Joshua French, Bootstrap confidence interval example, 2:12 to 6:12](https://www.youtube.com/watch?v=IBuJSRu9Quw&t=132s) |

StatQuest shows the eight values on screen without reading them out and gives no number for the standard error. French reaches an interval, not a standard error, and uses the percentile interval only. Neither covers when the bootstrap fails. Mahesh Huddar's channel has no video on it. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## Solving an inequality with the unknown in the exponent

<!-- video-table: exponent-inequality-with-logarithms rev=1 -->
Hasegi Inc., then TLMaths, both from the open web, on solving an inequality such as 0.5^x < 10^300 with logarithms, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | (1/2)^x < (1/2)^3 gives x > 3: a base below 1 makes the function fall, so the order reverses | Intuition, open web | [Hasegi Inc., Why an Exponential Inequality Flips When the Base Is Below 1, 0:03 to 1:32](https://www.youtube.com/watch?v=WzR5E7dGM7M&t=3s) |
| 2 | Write 1/2 as 2^(-1), compare exponents to get -x < -3, and multiplying both sides by -1 flips the sign: the same flip as dividing by a negative | Intuition, open web | [Hasegi Inc., Why an Exponential Inequality Flips When the Base Is Below 1, 1:32 to 2:05](https://www.youtube.com/watch?v=WzR5E7dGM7M&t=92s) |
| 3 | Solve 0.5^x < 10^300: take natural logs of both sides, bring both exponents down, divide by ln 0.5 = -0.693, which is negative, so the sign reverses and x > -996.57 | Worked example, open web | [TLMaths, Solving 0.5^x less than 10^300, 0:06 to 2:23](https://www.youtube.com/watch?v=nDr4CrZ_CO8&t=6s) |
| 4 | Why writing it as a log with base 0.5 in one step goes wrong (the flip is forgotten), and why to go through natural logs | Worked example, open web | [TLMaths, Solving 0.5^x less than 10^300, 2:23 to 3:27](https://www.youtube.com/watch?v=nDr4CrZ_CO8&t=143s) |

Neither video solves for a whole number of repeats or rounds the answer up, and neither starts from a base above 1 with a positive log. TLMaths refers to an earlier video of his for the base 2 case. Professor Leonard's logarithm lecture (Precalculus 64) was checked by chapter titles only, which name equations, so it is not linked. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## Inverse transform sampling worked on the exponential

<!-- video-table: inverse-transform-exponential-example rev=1 -->
Susu Zhang, then Marcus Pendergrass, both from the open web, on turning uniform random numbers into exponential ones with the inverse CDF, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | From the exponential density to its CDF 1 - e^(-λx), set equal to u, and solved for x = -(1/λ) ln(1 - u) | Worked example, open web | [Susu Zhang, Lec1 2 2 Example Exp, 0:06 to 4:22](https://www.youtube.com/watch?v=joBKfHH5bwc&t=6s) |
| 2 | The inverse as an R function, 1000 uniform draws, the transform with λ = 1, and a histogram laid over the exponential density | Code walk, open web | [Susu Zhang, Lec1 2 2 Example Exp, 4:22 to 10:22](https://www.youtube.com/watch?v=joBKfHH5bwc&t=262s) |
| 3 | 10,000 uniforms in Desmos, -ln(1 - u) for λ = 1, then multiplied by 2 to get λ = 1/2 | Worked example, open web | [Marcus Pendergrass, Using The Inverse CDF Method to Simulate Random Variables, 3:24 to 6:36](https://www.youtube.com/watch?v=xf-ltpf7rwQ&t=204s) |

Both work by simulating many draws and comparing to the density; neither turns two or three specific uniform numbers into exponential values by hand, and neither proves the transformed draws have the target CDF. Pendergrass cites the two facts he uses to his own course notes. The ritvikmath block above covers the CDF and the inverse. Mahesh Huddar's channel has no video on it. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## The noise prediction is the score, rescaled

<!-- video-table: noise-prediction-is-the-score rev=1 -->
Vizuara, then Deepia from the open web, on why a network that predicts the added noise is predicting the score, in the order to watch:

| Order | What it covers | Kind | Code it writes | Watch |
|---|---|---|---|---|
| 1 | Noise a clean point with a Gaussian of standard deviation σ, take the log of that Gaussian and its gradient: the score of the noised point given the clean one is −(x̃ − x)/σ² | Proof | | [Vizuara, Principles of Diffusion Models, lecture 6, 32:45 to 38:19](https://www.youtube.com/watch?v=6ELzfPXUqps&t=1965s) |
| 2 | That score points from the noised point back to the clean one, so it is the added noise, which is what a DDPM network is trained to predict | Intuition | | [Vizuara, Principles of Diffusion Models, lecture 6, 38:19 to 40:25](https://www.youtube.com/watch?v=6ELzfPXUqps&t=2299s) |
| 3 | The training loss in code, with the target score written as −(x − x̃)/σ² and reduced to −ε/σ | Code walk | the loss whose target is `-noise / sigma` | [Vizuara, Principles of Diffusion Models, lecture 6, 42:54 to 44:49](https://www.youtube.com/watch?v=6ELzfPXUqps&t=2574s) |
| 4 | The denoiser that minimises squared error returns the average clean point given the noisy one | Intuition, open web | | [Deepia, Unadjusted Langevin Algorithm, 1:34 to 5:43](https://www.youtube.com/watch?v=m0OTso2Dc2U&t=94s) |
| 5 | Tweedie's formula: that average gives the score of the whole noised distribution, the step from one point's score to the marginal score | Proof, open web | | [Deepia, Unadjusted Langevin Algorithm, 5:43 to 10:23](https://www.youtube.com/watch?v=m0OTso2Dc2U&t=343s) |

Vizuara noises with x̃ = x + σε and no shrinking of x, so the factor is 1/σ where a DDPM schedule has 1/√(1 − ᾱ_t); no listed creator covers the marginal step, so rows 4 and 5 come from Deepia on the open web. Rows 1 to 3 are read from automatic captions and good to about 30 seconds; rows 4 and 5 are chapter boundaries from the video's chapter list, so the sentence inside each is not checked.
<!-- /video-table -->

## Score matching

<!-- video-table: score-matching rev=1 -->
Stanford CS236, then Vizuara, on score matching, the loss that fits a model's score using only samples of the data, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The Fisher divergence, the squared distance between the model's score and the data's score | Intuition | [Stanford CS236, lecture 12, 34:37 to 38:02](https://www.youtube.com/watch?v=Nci1Bepcy0g&t=2077s) |
| 2 | Integration by parts removes the unknown data score from that loss | Proof | [Stanford CS236, lecture 12, 38:02 to 46:28](https://www.youtube.com/watch?v=Nci1Bepcy0g&t=2282s) |
| 3 | The score matching objective that results, which needs only samples | Intuition | [Stanford CS236, lecture 12, 46:28 to 50:36](https://www.youtube.com/watch?v=Nci1Bepcy0g&t=2788s) |
| 4 | What the two terms of that objective do: the trace pulls nearby points in toward the data, the norm makes the score zero on the data | Intuition | [Vizuara, Principles of Diffusion Models, lecture 6, 5:20 to 9:23](https://www.youtube.com/watch?v=6ELzfPXUqps&t=320s) |
| 5 | Why it is not used on images: the trace needs the whole D by D matrix, so its cost grows as D², 784² for a 28 by 28 image | Intuition | [Vizuara, Principles of Diffusion Models, lecture 6, 9:23 to 12:43](https://www.youtube.com/watch?v=6ELzfPXUqps&t=563s) |

Neither works score matching on numbers, and the denoising version that diffusion training uses is its own table. Rows 1 to 3 are chapter boundaries from CS236's chapter list, so the sentence inside each is not checked; rows 4 and 5 are read from Vizuara's automatic captions and good to about 30 seconds.
<!-- /video-table -->

## The kernel density estimate

<!-- video-table: kernel-density-estimate rev=1 -->
ritvikmath on the kernel density estimate, a normal curve centred on every data point and averaged, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Six fish weights and three candidate estimates: under-smoothed, over-smoothed and just right | Intuition | [ritvikmath, Kernel Density Estimation, 2:38 to 5:17](https://www.youtube.com/watch?v=t1PEhjyzxLA&t=158s) |
| 2 | A normal curve centred on each of three fish, averaged, and read off at 9.5 lb and at 14 lb | Worked example | [ritvikmath, Kernel Density Estimation, 5:32 to 10:13](https://www.youtube.com/watch?v=t1PEhjyzxLA&t=332s) |
| 3 | The formula, one over n times the sum of a kernel at x minus each data point, matched to the picture | Intuition | [ritvikmath, Kernel Density Estimation, 10:28 to 13:08](https://www.youtube.com/watch?v=t1PEhjyzxLA&t=628s) |
| 4 | The bandwidth h is each kernel's standard deviation, and it decides between too many peaks and too few | Intuition | [ritvikmath, Kernel Density Estimation, 14:10 to 15:44](https://www.youtube.com/watch?v=t1PEhjyzxLA&t=850s) |

ritvikmath works in one dimension and does not point out that a Gaussian kernel density estimate is a Gaussian mixture with one equal-weight component per data point. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## Total variation distance

<!-- video-table: total-variation-distance rev=1 -->
Mary Wootters, from the open web, on the total variation distance between two distributions, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | TV is half the sum of the absolute differences between the two probability tables, which equals the largest difference in probability the two give any one event | Intuition, open web | [Wootters, Total Variation Distance, 0:16 to 1:35](https://www.youtube.com/watch?v=aJP0Bj6jVkI&t=16s) |
| 2 | Two bar charts split where each is the higher: the two shaded areas are equal, and each one is the TV | Proof, open web | [Wootters, Total Variation Distance, 1:35 to 3:47](https://www.youtube.com/watch?v=aJP0Bj6jVkI&t=95s) |
| 3 | A fair coin against one that lands heads 0.6 of the time: TV = ½(0.1 + 0.1) = 0.1 | Worked example, open web | [Wootters, Total Variation Distance, 4:34 to 6:42](https://www.youtube.com/watch?v=aJP0Bj6jVkI&t=274s) |

No listed creator covers it. Wootters compares two known tables; she does not estimate TV from two sets of samples on a binning, so the floor that two draws of the same data reach is not covered. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## Compound interest, the annuity formula and the Rule of 72

<!-- video-table: compound-interest rev=1 -->
Professor Leonard, JK Math and the Organic Chemistry Tutor on compound interest, the annuity formula and the Rule of 72, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Interest earned on interest, and why compounding pulls away from simple interest | Intuition | [Leonard, Prealgebra 7.6, 19:00 to 22:57](https://www.youtube.com/watch?v=b3FZRzIov8E&t=1140s) |
| 2 | The compound interest formulas: once a year, n times a year, and continuously | Proof or rule | [Leonard, Precalculus 65, 1:30 to 9:32](https://www.youtube.com/watch?v=N1k25doMFww&t=90s) |
| 3 | Future value worked from the formula | Worked example | [Leonard, Precalculus 65, 9:32 to 18:45](https://www.youtube.com/watch?v=N1k25doMFww&t=572s) |
| 4 | Solving for the time a balance takes, with logarithms | Worked example | [Leonard, Precalculus 65, 26:10 to 37:38](https://www.youtube.com/watch?v=N1k25doMFww&t=1570s) |
| 5 | A stream of equal deposits written out as a geometric series | Proof, open web | [JK Math, Future Value of Annuities, 2:11 to 8:19](https://www.youtube.com/watch?v=55BAaHnH1JI&t=131s) |
| 6 | Summing that series into the annuity future value formula | Proof, open web | [JK Math, Future Value of Annuities, 8:19 to 11:00](https://www.youtube.com/watch?v=55BAaHnH1JI&t=499s) |
| 7 | The annuity formula used on a monthly deposit | Worked example | [Organic Chemistry Tutor, Future Value of an Ordinary Annuity, 5:28 to 10:03](https://www.youtube.com/watch?v=bcuXY8WkjF4&t=328s) |
| 8 | The Rule of 72 applied to a rate | Worked example | [Organic Chemistry Tutor, Rule of 72, 1:50 to 3:15](https://www.youtube.com/watch?v=91nnN2XwTMg&t=110s) |
| 9 | Where 72 comes from, and how close the estimate is | Proof | [Organic Chemistry Tutor, Rule of 72, 3:15 to 6:27](https://www.youtube.com/watch?v=91nnN2XwTMg&t=195s) |

None works in rand or with a rate quoted nominal annual compounded monthly, and Leonard does not cover annuities, so JK Math fills the derivation from the open web. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Nominal against effective interest rates

<!-- video-table: nominal-vs-effective-rate rev=1 -->
Two South African Grade 11 teachers, Professor Leonard and the Finance Storyteller on turning a quoted nominal rate into the effective annual rate, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What a nominal rate and an effective rate are, in the Grade 11 notation | Intuition, open web | [Online Maths by Miss Pythagoras, Grade 11 L4, 0:00 to 2:16](https://www.youtube.com/watch?v=9zy88LYBg2M&t=0s) |
| 2 | Deriving the conversion formula from m compoundings a year | Proof, open web | [Online Maths by Miss Pythagoras, Grade 11 L4, 2:16 to 4:23](https://www.youtube.com/watch?v=9zy88LYBg2M&t=136s) |
| 3 | Nominal to effective, then effective back to nominal | Worked example, open web | [Online Maths by Miss Pythagoras, Grade 11 L4, 4:23 to 7:55](https://www.youtube.com/watch?v=9zy88LYBg2M&t=263s) |
| 4 | A rate compounded monthly, worked in full | Worked example, open web | [24 minute lessons, Grade 11 Nominal and Effective, 5:58 to 12:16](https://www.youtube.com/watch?v=gq7ECefBC7g&t=358s) |
| 5 | Effective annual yield, compared across compounding frequencies | Worked example | [Leonard, Precalculus 65, 37:38 to 46:13](https://www.youtube.com/watch?v=N1k25doMFww&t=2258s) |
| 6 | The effective rate on credit card debt | Worked example, open web | [Finance Storyteller, Effective annual interest rate, 2:51 to 3:43](https://www.youtube.com/watch?v=L39WeJRWvvw&t=171s) |

None converts a prime-linked bond quote or a bank's rate sheet. The two Grade 11 lessons are found on the open web, as no listed creator teaches the South African notation. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Real return after inflation

<!-- video-table: real-return rev=1 -->
Initial Return and Farhat Lectures, both from the open web, on turning a nominal return into a real one, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | How inflation eats a nominal return and a deposit rate | Intuition, open web | [Initial Return, Nominal vs real return, 0:35 to 4:21](https://www.youtube.com/watch?v=B_fmz7B2_Ks&t=35s) |
| 2 | The Fisher equation | Proof or rule, open web | [Initial Return, Nominal vs real return, 4:21 to 7:42](https://www.youtube.com/watch?v=B_fmz7B2_Ks&t=261s) |
| 3 | Why subtracting inflation is only an approximation, and the exact real return from gross rates | Proof, open web | [Farhat Lectures, Nominal vs Real Interest Rates, 3:45 to 6:15](https://www.youtube.com/watch?v=u4exjDX_D8c&t=225s) |
| 4 | An 8% deposit against 5% inflation, exact and approximate | Worked example, open web | [Farhat Lectures, Nominal vs Real Interest Rates, 6:15 to 7:08](https://www.youtube.com/watch?v=u4exjDX_D8c&t=375s) |
| 5 | The nominal rate needed for a 3% real return | Worked example, open web | [Farhat Lectures, Nominal vs Real Interest Rates, 8:26 to 9:15](https://www.youtube.com/watch?v=u4exjDX_D8c&t=506s) |

No listed creator covers real return, and neither of these uses South African CPI or deflates a rand projection to today's money. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## The amortizing loan payment

<!-- video-table: amortization rev=1 -->
Humphrey Yang, Deasy Maths, Matty and Rowan Alexander on the amortizing loan payment, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | $400,000 over 30 years at 7%: the month-one payment of $2,660 splits into $2,333 interest and $327 principal, and $229,200 is still owed after 20 years | Worked example, open web | [Humphrey Yang, Pay Off Your Mortgage Early or Invest, 1:02 to 3:46](https://www.youtube.com/watch?v=Q9An1Guxhy0&t=62s) |
| 2 | Each payment discounted back to today, so the loan equals the present value of the payments | Proof, open web | [Deasy Maths, Deriving the Amortisation Formula, 1:08 to 4:39](https://www.youtube.com/watch?v=nKvzV779Tys&t=68s) |
| 3 | Summing that geometric series and solving for the payment | Proof, open web | [Deasy Maths, Deriving the Amortisation Formula, 4:39 to 8:49](https://www.youtube.com/watch?v=nKvzV779Tys&t=279s) |
| 4 | A South African bond's repayment schedule, and the month interest and capital are equal | Worked example, open web | [Rowan Alexander, Understanding Mortgage Bond Repayments, 1:10 to 4:22](https://www.youtube.com/watch?v=rAohANEQo-M&t=70s) |
| 5 | A South African home loan installment worked from the formula | Worked example, open web | [Matty, Home Loan Calculation (South Africa), 3:00 to 7:15](https://www.youtube.com/watch?v=7bgWbTW2MSc&t=180s) |
| 6 | Extra monthly payments on a South African bond, and the years they take off | Worked example, open web | [Rowan Alexander, How to Cut Years Off Your Bond Repayment, 3:03 to 5:35](https://www.youtube.com/watch?v=Xc4xELguatQ&t=183s) |
| 7 | Three pay-down strategies on one loan: half the payment every two weeks (paid off 6 years 1 month early), $200 a month extra, and a one-off windfall | Worked example, open web | [Humphrey Yang, Pay Off Your Mortgage Early or Invest, 9:36 to 11:39](https://www.youtube.com/watch?v=Q9An1Guxhy0&t=576s) |

No video compares the avalanche and snowball orders for paying off two debts, and none prices a bond at prime minus a margin. Humphrey Yang is a former adviser paid by ads and sponsors; Rowan Alexander points viewers to his bond originator. Rows 1 and 7 are read from automatic captions and good to about 30 seconds; rows 2 to 6 are chapter boundaries from each video's chapter list, so the sentence inside each is not checked.
<!-- /video-table -->

## Paying down a bond against investing

<!-- video-table: paying-down-the-bond-or-investing rev=1 -->
Humphrey Yang and Rowan Alexander on paying extra into a bond against investing the same money, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | An extra bond payment earns the bond's rate without risk, so it is compared with the expected return after tax | Proof or rule, open web | [Humphrey Yang, Pay Off Your Mortgage Early or Invest, 4:27 to 6:30](https://www.youtube.com/watch?v=Q9An1Guxhy0&t=267s) |
| 2 | $500 a month for 25 years: $473,000 invested at 8% against $188,000 of interest saved, and why those two figures do not compare directly | Worked example, open web | [Humphrey Yang, Pay Off Your Mortgage Early or Invest, 7:31 to 8:33](https://www.youtube.com/watch?v=Q9An1Guxhy0&t=451s) |
| 3 | In South Africa: savings earning 8% to 9% are taxed down to 5% to 7%, against prime saved inside the bond before tax | Worked example, open web | [Rowan Alexander, Managing and Using Access Bonds, 4:48 to 6:53](https://www.youtube.com/watch?v=NzpmMkiyOdc&t=288s) |

Humphrey Yang's example is American, where bond interest can be deducted; in South Africa it cannot on a home you live in, so an extra payment is worth more here. Rowan Alexander points viewers to his bond originator. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## The access bond

<!-- video-table: access-bond rev=1 -->
Rowan Alexander on what an access bond lets you take back out, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Paying more than the contract amount, R10,000 a month plus a R50,000 lump sum, and redrawing what was prepaid | Intuition, open web | [Rowan Alexander, Managing and Using Access Bonds, 0:43 to 2:04](https://www.youtube.com/watch?v=NzpmMkiyOdc&t=43s) |
| 2 | The two ways a bank treats a prepayment: the term shortens with the installment unchanged, or the installment is recalculated and access usually goes; test it with a R100 payment | Proof or rule, open web | [Rowan Alexander, Managing and Using Access Bonds, 2:04 to 4:28](https://www.youtube.com/watch?v=NzpmMkiyOdc&t=124s) |

He does not show what happens to the redraw facility when the bank re-rates the bond, and his later claim of a R2,000 gap between 20- and 30-year installments on R1m is wrong (R10,837 against R10,094 at 11.75%, a gap of R743), so that segment is left out. He points viewers to his bond originator. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## The repo rate and the prime rate

<!-- video-table: repo-and-prime rev=1 -->
Talking Money With Nozi and Genevieve Stafford Jack on the repo rate and the prime rate, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What the Reserve Bank is and does | Intuition, open web | [Talking Money With Nozi, What is the Repo Rate?, 0:10 to 0:48](https://www.youtube.com/watch?v=r96tHYx3zRA&t=10s) |
| 2 | The repo rate, and how banks set prime from it | Proof or rule, open web | [Talking Money With Nozi, What is the Repo Rate?, 0:48 to 4:38](https://www.youtube.com/watch?v=r96tHYx3zRA&t=48s) |
| 3 | What a repo cut or increase does to prime and to a bond installment | Proof or rule, open web | [Genevieve Stafford Jack, Prime Interest Rate vs Repo Rate, 1:24 to 8:59](https://www.youtube.com/watch?v=VH0WrQ_q-kk&t=84s) |

Neither works a 25 basis point change through a bond installment in rand, which §6.4 does. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## The South African credit score

<!-- video-table: credit-score rev=1 -->
Lomaku by Nokuhle, Money Marx, Financially Fabulous Females and Meerkat on the South African credit score, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | How credit works, from a lender's side | Intuition, open web | [Lomaku by Nokuhle, What is a Credit Score?, 2:18 to 5:36](https://www.youtube.com/watch?v=DeklDhuu-6I&t=138s) |
| 2 | Who keeps the score: the credit bureaus | Proof or rule, open web | [Money Marx, Credit Scores In South Africa Explained, 3:54 to 5:10](https://www.youtube.com/watch?v=I05NtbTwlmM&t=234s) |
| 3 | What the score number means, and report against history against score | Proof or rule, open web | [Lomaku by Nokuhle, What is a Credit Score?, 6:46 to 9:13](https://www.youtube.com/watch?v=DeklDhuu-6I&t=406s) |
| 4 | How the score is calculated | Proof or rule, open web | [Lomaku by Nokuhle, What is a Credit Score?, 9:13 to 12:04](https://www.youtube.com/watch?v=DeklDhuu-6I&t=553s) |
| 5 | What a high and a low score each cost you | Intuition, open web | [Financially Fabulous Females, Credit Scores in South Africa, 4:23 to 6:00](https://www.youtube.com/watch?v=yqHQFJX0OxA&t=263s) |
| 6 | Fixing an error on your credit report | Proof or rule, open web | [Meerkat, Credit scores fully explained in South Africa, 8:14 to 9:32](https://www.youtube.com/watch?v=6YiMxVZ9F4M&t=494s) |

None shows how a score moves the margin a bank quotes against prime, so there is no worked example of the rate it buys. Money Marx sells a paid course; Meerkat is a debt-counselling and finance company. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Home-loan affordability

<!-- video-table: home-loan-affordability rev=1 -->
Sebolelo, an estate agent, on what a bank's affordability test leaves out, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What a bank's approval does and does not tell you | Proof or rule, open web | [Sebolelo The Estate Agent, Why Banks Approve People for Houses They Can't Afford, 1:25 to 2:18](https://www.youtube.com/watch?v=3lbK8VDQd2Q&t=85s) |
| 2 | The test is a formula on income and existing debt | Proof or rule, open web | [Sebolelo The Estate Agent, Why Banks Approve People for Houses They Can't Afford, 2:18 to 3:08](https://www.youtube.com/watch?v=3lbK8VDQd2Q&t=138s) |
| 3 | Costs that keep rising after approval | Intuition, open web | [Sebolelo The Estate Agent, Why Banks Approve People for Houses They Can't Afford, 3:08 to 4:49](https://www.youtube.com/watch?v=3lbK8VDQd2Q&t=188s) |

No timed video states a bank's installment-to-income limit or works the largest bond for a given net income; the South African videos that do have no chapters and their captions were refused, and Louis Reynhardt's are held until his claims can be read. Sebolelo is paid on sales completing. Times are chapter boundaries read from the video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Renting against buying

<!-- video-table: rent-against-buy rev=1 -->
Ben Felix, Money with Carla and Rowan Alexander on renting against buying, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The cost of the capital tied up in a house, which the buyer pays even with no bond | Intuition, open web | [Ben Felix, Renting vs. Buying a Home: The 5% Rule, 2:20 to 3:37](https://www.youtube.com/watch?v=Uwl3-jBNEd4&t=140s) |
| 2 | The expected returns on property and on shares behind the rule | Proof or rule, open web | [Ben Felix, Renting vs. Buying a Home: The 5% Rule, 3:37 to 6:46](https://www.youtube.com/watch?v=Uwl3-jBNEd4&t=217s) |
| 3 | The unrecoverable costs of owning set against rent, worked | Worked example, open web | [Ben Felix, Renting vs. Buying a Home: The 5% Rule, 6:46 to 8:26](https://www.youtube.com/watch?v=Uwl3-jBNEd4&t=406s) |
| 4 | Opportunity cost: what the deposit would have earned invested | Intuition, open web | [Ben Felix, Renting vs. Buying a Home: The 5% Rule, 8:26 to 9:21](https://www.youtube.com/watch?v=Uwl3-jBNEd4&t=506s) |
| 5 | The total cost of ownership, then the financial indifference model | Proof, open web | [Ben Felix, Renting vs. Buying: What People Get Wrong, 3:41 to 9:12](https://www.youtube.com/watch?v=j4H9LL7A-nQ&t=221s) |
| 6 | A Cape Town property bought against rented, worked in rand | Worked example, open web | [Money with Carla, Buy or Rent in Cape Town? The Rule of 8.5%, 4:06 to 11:23](https://www.youtube.com/watch?v=wPT7fFpNL7I&t=246s) |
| 7 | Her South African version of the rule, 8.5% | Proof or rule, open web | [Money with Carla, Buy or Rent in Cape Town? The Rule of 8.5%, 20:07 to 23:20](https://www.youtube.com/watch?v=wPT7fFpNL7I&t=1207s) |
| 8 | The year buying overtakes renting in a R3m comparison | Worked example, open web | [Rowan Alexander, Buying or Renting: Which Builds More Wealth?, 7:33 to 8:05](https://www.youtube.com/watch?v=5hZSG0kxzQQ&t=453s) |

Every one assumes the buyer pays rent today, so the comparison carries over only through the unrecoverable costs of owning and the opportunity cost of the deposit, rows 1, 3 and 4; for someone who pays no rent the rent side is zero. Ben Felix uses Canadian figures and runs a portfolio management firm; Money with Carla sells a calculator and a course; Rowan Alexander points viewers to his bond originator. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## The primary residence exclusion

<!-- video-table: primary-residence-exclusion rev=1 -->
Lizelle Bruwer and the Vorsters on the capital gains exclusion for the home you live in, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What counts as a primary residence | Proof or rule, open web | [Lizelle Bruwer, Unit 5 CGT Primary residence exclusion, 0:00 to 2:05](https://www.youtube.com/watch?v=6FjNMuOFoUc&t=0s) |
| 2 | The exclusion, and the principles for applying it | Proof or rule, open web | [Lizelle Bruwer, Unit 5 CGT Primary residence exclusion, 2:05 to 5:42](https://www.youtube.com/watch?v=6FjNMuOFoUc&t=125s) |
| 3 | Case studies worked | Worked example, open web | [Lizelle Bruwer, Unit 5 CGT Primary residence exclusion, 5:42 to 10:34](https://www.youtube.com/watch?v=6FjNMuOFoUc&t=342s) |
| 4 | A seller's view: the exclusions, and the taxable part worked out | Worked example, open web | [Lydia and Andre Vorster, Capital Gains Tax on Property Explained, 2:30 to 5:28](https://www.youtube.com/watch?v=0oYXg1aYNFQ&t=150s) |
| 5 | Owning through a company or a trust, and what that does to the exclusion | Intuition, open web | [Lydia and Andre Vorster, Capital Gains Tax on Property Explained, 5:28 to 6:37](https://www.youtube.com/watch?v=0oYXg1aYNFQ&t=328s) |

The exclusion amount changes by budget, so it comes from the statutory pull; Lizelle Bruwer's lecture is from April 2020. The Vorsters are estate agents paid on a sale completing. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Net worth and the balance sheet

<!-- video-table: net-worth rev=1 -->
Accounting Stuff, the Organic Chemistry Tutor and Preet Banerjee on the balance sheet and net worth, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What a balance sheet is, at its simplest | Intuition, open web | [Accounting Stuff, The Balance Sheet for Beginners, 0:17 to 1:15](https://www.youtube.com/watch?v=CMv1zlZhb4Q&t=17s) |
| 2 | Assets less liabilities is equity, worked on a home | Worked example | [Organic Chemistry Tutor, Assets, Liabilities and Equity, 0:39 to 2:38](https://www.youtube.com/watch?v=_-lVFKG5_08&t=39s) |
| 3 | Building a basic balance sheet line by line | Worked example, open web | [Accounting Stuff, The Balance Sheet for Beginners, 2:18 to 5:11](https://www.youtube.com/watch?v=CMv1zlZhb4Q&t=138s) |
| 4 | A household's net worth worked out | Worked example, open web | [Preet Banerjee, How to Calculate Your Net Worth, 0:50 to 2:47](https://www.youtube.com/watch?v=KhSnNtdYR9Y&t=50s) |
| 5 | What to keep in mind: market value for assets, payoff value for debts | Proof or rule, open web | [Preet Banerjee, How to Calculate Your Net Worth, 2:47 to 4:12](https://www.youtube.com/watch?v=KhSnNtdYR9Y&t=167s) |

None links a month's surplus to the change in net worth, the stock and flow link §2 uses. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## The savings rate

<!-- video-table: savings-rate rev=1 -->
James Shack, The Plain Bagel and BeatTheBush on why the savings rate sets the years to financial independence, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The nest egg needed, from annual spending and a withdrawal rate | Worked example, open web | [The Plain Bagel, The Truth About FIRE, 2:27 to 6:12](https://www.youtube.com/watch?v=SEItn9Csitg&t=147s) |
| 2 | Years to retirement read off against the savings rate | Proof or rule, open web | [BeatTheBush, Why Savings Rate Matters, 2:55 to 6:55](https://www.youtube.com/watch?v=vsyPMyJBY40&t=175s) |
| 3 | A higher savings rate against a higher return: which moves the date more | Intuition, open web | [James Shack, The Maths Behind Early Retirement, 8:17 to 12:45](https://www.youtube.com/watch?v=QEGvePdq81E&t=497s) |

None derives the years-to-independence formula that §7 does, or shows income cancelling out of it. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## The emergency fund and sinking funds

<!-- video-table: emergency-and-sinking-funds rev=1 -->
Plan With Gloria, Jordan Budgets, Itumeleng Moloto and Money Marx on the emergency fund, against money saved for a known cost, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | General savings, a sinking fund for a known future cost, and an emergency fund for an unknown one | Intuition, open web | [Plan With Gloria, Savings, Sinking Funds and Emergency Funds, 1:39 to 4:27](https://www.youtube.com/watch?v=HtlmyOti44I&t=99s) |
| 2 | Setting aside small amounts each month toward a cost that is certain to arrive, so it never lands on a credit card | Intuition, open web | [Jordan Budgets, What Are Sinking Funds, 0:40 to 2:02](https://www.youtube.com/watch?v=eOV4azgirXU&t=40s) |
| 3 | How much to hold | Proof or rule, open web | [Itumeleng Moloto, How much to save in your emergency fund, 3:03 to 4:29](https://www.youtube.com/watch?v=fcZAe6JNfDk&t=183s) |
| 4 | What the money needs: reach on the day, no risk to the balance, and some interest | Proof or rule, open web | [Money Marx, Best Place To Keep Your Emergency Fund, 2:07 to 4:22](https://www.youtube.com/watch?v=43kYXgCQcrg&t=127s) |
| 5 | The South African places to keep it, side by side | Intuition, open web | [Money Marx, Best Place To Keep Your Emergency Fund, 4:22 to 9:32](https://www.youtube.com/watch?v=43kYXgCQcrg&t=262s) |
| 6 | The strategy he recommends, split across more than one place | Proof or rule, open web | [Money Marx, Best Place To Keep Your Emergency Fund, 9:32 to 15:59](https://www.youtube.com/watch?v=43kYXgCQcrg&t=572s) |

None sizes the fund from essential spending as months times the monthly burn, which §8 does, so there is no worked example here; Gloria's 3 to 6 months is the usual rule, stated without derivation. Gloria and Jordan sell budget templates; Money Marx sells a paid course, and his 2022 rates are re-pulled. Rows 1 and 2 are read from automatic captions and good to about 30 seconds; rows 3 to 6 are chapter boundaries from each video's chapter list, so the sentence inside each is not checked.
<!-- /video-table -->

## Budgeting methods

<!-- video-table: budgeting-methods rev=1 -->
WhiteBoard Finance, Clever Girl Finance, Don Invests and Jordan Budgets on the 50/30/20 and zero-based budgets, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The 50/30/20 rule: needs, wants, savings | Proof or rule, open web | [WhiteBoard Finance, The 50/30/20 Rule, 0:58 to 2:52](https://www.youtube.com/watch?v=HQzoZfc3GwQ&t=58s) |
| 2 | A 50/30/20 budget built, then debt payments placed in it | Worked example, open web | [Clever Girl Finance, Make The 50-30-20 Budget Work For You, 4:01 to 7:24](https://www.youtube.com/watch?v=hOPc0SFKBiw&t=241s) |
| 3 | A zero-based budget: every rand given a job | Intuition, open web | [Don Invests, Zero-Based Budgeting, 1:14 to 2:27](https://www.youtube.com/watch?v=EiDAFmjV7lQ&t=74s) |
| 4 | A zero-based budget built from a month's income | Worked example, open web | [Jordan Budgets, How To Create A Zero-Based Budget, 9:29 to 11:59](https://www.youtube.com/watch?v=jOql64qADUw&t=569s) |
| 5 | When each style suits, compared | Intuition, open web | [Don Invests, Zero-Based Budgeting, 5:50 to 9:25](https://www.youtube.com/watch?v=EiDAFmjV7lQ&t=350s) |

None covers pay-yourself-first as a method of its own, or the envelope and stokvel approach. All four are American. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Choosing a South African bank account

<!-- video-table: choosing-a-bank-account rev=1 -->
Money Marx on choosing a South African bank account, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Traditional banks, online-only banks and the newer app banks | Intuition, open web | [Money Marx, How To Choose The Best Bank Account, 1:03 to 4:50](https://www.youtube.com/watch?v=ffZPJhvfQU4&t=63s) |
| 2 | Five factors: what you transact, value and volume, pay-as-you-use against a bundle (track three months of fees, then switch), the fee types, and out-of-bundle rates | Proof or rule, open web | [Money Marx, How To Choose The Best Bank Account, 9:03 to 11:49](https://www.youtube.com/watch?v=ffZPJhvfQU4&t=543s) |

No fee or interest rate appears in rand, so the bank breakeven is computed from pulled rate sheets; the video, from February 2022, also lists two payment wallets as online banks. Money Marx sells a paid course. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## Savings accounts, notice deposits and fixed deposits

<!-- video-table: notice-and-fixed-deposits rev=1 -->
Anna Mogale, Sinikiwe Ngcobo, Money Marx, Ivyn Sambo and Yvonne of Freely on the savings account, the notice deposit and the fixed deposit, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What a savings account is, and the interest it pays | Intuition, open web | [Anna Mogale, Savings and Investment Account Options in SA, Part 1, 2:02 to 5:19](https://www.youtube.com/watch?v=IsmR1_vRenE&t=122s) |
| 2 | A notice deposit: a week's or a month's notice buys a higher rate, and keeping a fifth of the balance on call lowers it | Intuition, open web | [Sinikiwe Ngcobo, The 5 savings account types, 1:22 to 4:08](https://www.youtube.com/watch?v=7n282AiN0jA&t=82s) |
| 3 | Immediate-access accounts against notice accounts, product by product | Proof or rule, open web | [Anna Mogale, Immediate and Notice Savings Accounts in SA, Part 2, 2:20 to 11:39](https://www.youtube.com/watch?v=WXQXfanNuaU&t=140s) |
| 4 | December 2022's best 7-, 32-, 60- and 90-day rates, and the R1m to R5m minimums they needed | Worked example, open web | [Money Marx, Best Money Market Fund, 1:00 to 1:42](https://www.youtube.com/watch?v=-r68yDf0OnQ&t=60s) |
| 5 | 32-day notice rates at seven banks, November 2024 | Worked example, open web | [Ivyn Sambo, Best 32 Days Notice Account in South Africa, 1:25 to 5:19](https://www.youtube.com/watch?v=Ijup6nzVzlQ&t=85s) |
| 6 | Three concerns with a notice deposit: a penalty to leave early, high minimums, and one bank holding everything | Proof or rule, open web | [Money Marx, Best Money Market Fund, 1:42 to 2:44](https://www.youtube.com/watch?v=-r68yDf0OnQ&t=102s) |
| 7 | A fixed deposit: the amount at maturity is known on the day you lock it in, whatever rates do after | Intuition, open web | [Sinikiwe Ngcobo, The 5 savings account types, 4:08 to 5:30](https://www.youtube.com/watch?v=7n282AiN0jA&t=248s) |
| 8 | Three-year deposits of R50,000 at three banks, nominal against effective rate, ending near R66,000 | Worked example, open web | [Yvonne, 9 High Interest Fixed Deposit Accounts, 4:54 to 7:01](https://www.youtube.com/watch?v=BCxBwT6TIRQ&t=294s) |
| 9 | One-year deposits at five banks, with the monthly interest each pays | Worked example, open web | [Yvonne, 9 High Interest Fixed Deposit Accounts, 7:01 to 9:09](https://www.youtube.com/watch?v=BCxBwT6TIRQ&t=421s) |
| 10 | Her rule: instant access for emergency money, a fixed deposit for medium-term goals | Proof or rule, open web | [Yvonne, 9 High Interest Fixed Deposit Accounts, 9:09 to 9:30](https://www.youtube.com/watch?v=BCxBwT6TIRQ&t=549s) |

No video taxes a deposit's interest above the exemption, and none puts a 7-day and a 32-day deposit side by side on the same balance. The rates on screen are from 2021 to 2024 and are re-pulled before use; Yvonne's automatic captions garble some rates ("99.94%" is 9.94%). Money Marx sells a paid course. Rows 2, 4 and 6 to 10 are read from automatic captions and good to about 30 seconds; rows 1, 3 and 5 are chapter boundaries from each video's chapter list, so the sentence inside each is not checked.
<!-- /video-table -->

## Money market funds against money market accounts and income funds

<!-- video-table: money-market-and-income-funds rev=1 -->
Money Marx and an Ashburton fund manager on the money market fund, against a bank's money market account and against an income fund, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | A money market account at one bank, guaranteed and under the Banks Act, against a money market fund spread across issuers under the collective investment schemes law, paid out in one to five business days | Proof or rule, open web | [Money Marx, Best Money Market Fund, 3:05 to 5:27](https://www.youtube.com/watch?v=-r68yDf0OnQ&t=185s) |
| 2 | What a fund holds (paper lent for up to a year) and what it aims for, 1% to 3% above inflation | Intuition, open web | [Money Marx, Best Money Market Fund, 5:47 to 7:28](https://www.youtube.com/watch?v=-r68yDf0OnQ&t=347s) |
| 3 | What it is for, and why not for money needed in more than about a year | Proof or rule, open web | [Money Marx, Best Money Market Fund, 7:28 to 8:28](https://www.youtube.com/watch?v=-r68yDf0OnQ&t=448s) |
| 4 | Meant for one month to about a year, with next-day payout and no penalties, and not a call account | Proof or rule, open web | [Ashburton, Fixed income fund options, 41:20 to 43:45](https://www.youtube.com/watch?v=gY6GTYVLeF4&t=2480s) |
| 5 | Choosing a fund: size, minimums, return against its benchmark and CPI, then TER, TIC, adviser and platform fees, and the effective annual cost | Proof or rule, open web | [Money Marx, Best Money Market Fund, 8:28 to 12:50](https://www.youtube.com/watch?v=-r68yDf0OnQ&t=508s) |
| 6 | November 2022 funds side by side: TIC from 0.29% to 0.8%, EAC from 0.3%, minimums from R1,000 to R50,000 | Worked example, open web | [Money Marx, Best Money Market Fund, 12:50 to 14:54](https://www.youtube.com/watch?v=-r68yDf0OnQ&t=770s) |
| 7 | A call account near 3% against a money market fund at 4.3% against an income fund about 1% higher: in a low-rate year the extra 1% is a quarter more return | Worked example, open web | [Ashburton, Fixed income fund options, 17:00 to 19:49](https://www.youtube.com/watch?v=gY6GTYVLeF4&t=1020s) |
| 8 | What each may hold: the money market fund no corporate debt and nothing longer than 13 months, the income fund a third corporate debt at an average term near 3 years | Proof or rule, open web | [Ashburton, Fixed income fund options, 46:10 to 47:33](https://www.youtube.com/watch?v=gY6GTYVLeF4&t=2770s) |
| 9 | An income fund can be down over a few days, so hold it six months or longer, and split money across the two funds | Proof or rule, open web | [Ashburton, Fixed income fund options, 44:48 to 46:10](https://www.youtube.com/watch?v=gY6GTYVLeF4&t=2688s) |
| 10 | March and April 2020: the money market fund kept its capital while the income fund's monthly return fell from about 0.65% to 0.25% | Worked example, open web | [Ashburton, Fixed income fund options, 21:35 to 23:17](https://www.youtube.com/watch?v=gY6GTYVLeF4&t=1295s) |

Neither compares the funds after tax at a marginal rate, or with a fixed deposit maturing on a known date. Money Marx's line that no bank savings account can keep up with inflation is his opinion, on 2022 rates; the Ashburton presenter manages the two funds he compares and spoke in 2020, when rates were low. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## Asset classes

<!-- video-table: asset-classes rev=1 -->
Financially Fabulous Females, Money Marx and Ben Felix on the asset classes, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The four main classes, and the instruments inside each | Intuition, open web | [Financially Fabulous Females, Asset Classes Part 1, 1:15 to 6:14](https://www.youtube.com/watch?v=K2BLAvO6Yuk&t=75s) |
| 2 | Risk against reward across the classes | Proof or rule, open web | [Financially Fabulous Females, Asset Classes Part 1, 6:14 to 10:32](https://www.youtube.com/watch?v=K2BLAvO6Yuk&t=374s) |
| 3 | The South African classes, and how each has performed | Worked example, open web | [Money Marx, How To Determine Which Assets To Invest In, 4:48 to 11:30](https://www.youtube.com/watch?v=VCkkFlWz070&t=288s) |
| 4 | What bonds and listed property each add | Proof or rule, open web | [Ben Felix, Asset Allocation, 3:20 to 6:07](https://www.youtube.com/watch?v=7gkQHSW3hkE&t=200s) |

None compares the classes in real terms, after inflation and tax, which §10 does. Financially Fabulous Females is a commission-earning adviser; Money Marx sells a paid course; Ben Felix runs a portfolio management firm. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Volatility and the standard deviation

<!-- video-table: volatility rev=1 -->
Professor Leonard, Ryan O'Connell and Socratica on the standard deviation as the measure of risk, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What spread means, and the idea behind the standard deviation | Intuition | [Leonard, Statistics 3.3, 9:26 to 15:45](https://www.youtube.com/watch?v=4-FysvtxQEU&t=566s) |
| 2 | The standard deviation formula | Proof | [Leonard, Statistics 3.3, 15:45 to 22:20](https://www.youtube.com/watch?v=4-FysvtxQEU&t=945s) |
| 3 | A standard deviation calculated by hand | Worked example | [Leonard, Statistics 3.3, 25:51 to 36:43](https://www.youtube.com/watch?v=4-FysvtxQEU&t=1551s) |
| 4 | The empirical rule: how much of the data sits within one, two and three standard deviations | Proof or rule | [Leonard, Statistics 3.3, 1:13:43 to 1:23:37](https://www.youtube.com/watch?v=4-FysvtxQEU&t=4423s) |
| 5 | Reading a standard deviation on a bell curve and on real market returns, and three blind spots | Intuition, open web | [Ryan O'Connell, Standard Deviation in Finance, 2:43 to 4:38](https://www.youtube.com/watch?v=ExPK9V2wf1g&t=163s) |
| 6 | Turning daily volatility into an annual figure | Proof or rule, open web | [Socratica, Financial Volatility, 3:38 to 4:22](https://www.youtube.com/watch?v=xZ0knkuxxMI&t=218s) |

Leonard works on general data sets rather than returns, and none computes the volatility of a South African fund from its own monthly returns. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Diversification

<!-- video-table: diversification rev=1 -->
Ryan O'Connell, Eric Kelley, Pat Obi and Socratica on why combining assets lowers risk, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Risk that diversification removes, and risk it cannot | Intuition, open web | [Ryan O'Connell, Systematic Vs Unsystematic Risk, 0:00 to 4:57](https://www.youtube.com/watch?v=70mfXiCDnC4&t=0s) |
| 2 | The variance of a portfolio of two risky assets | Proof, open web | [Eric Kelley, Diversification with Two Assets, 5:02 to 6:56](https://www.youtube.com/watch?v=9gpbCi1g7w4&t=302s) |
| 3 | How the portfolio's risk falls as the weights change, then covariance and correlation | Proof, open web | [Eric Kelley, Diversification with Two Assets, 6:56 to 14:20](https://www.youtube.com/watch?v=9gpbCi1g7w4&t=416s) |
| 4 | Correlation, then the portfolio figures calculated | Worked example, open web | [Pat Obi, Portfolio Diversification, 12:48 to 20:03](https://www.youtube.com/watch?v=__p7EusowMI&t=768s) |
| 5 | The benefit worked on a portfolio's numbers | Worked example, open web | [Socratica, Financial Volatility, 5:37 to 9:52](https://www.youtube.com/watch?v=xZ0knkuxxMI&t=337s) |

None uses South African asset classes or a JSE and offshore split. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## The compound annual growth rate

<!-- video-table: cagr rev=1 -->
The Finance Storyteller, Initial Return and The Fintech Builder on the compound annual growth rate and the two kinds of average return, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Compound growth over several years, and what CAGR smooths into one rate | Intuition, open web | [Finance Storyteller, CAGR explained, 1:51 to 3:05](https://www.youtube.com/watch?v=F2mlD8Sf-fM&t=111s) |
| 2 | A CAGR computed from a start and an end value | Worked example, open web | [Finance Storyteller, CAGR explained, 3:05 to 4:27](https://www.youtube.com/watch?v=F2mlD8Sf-fM&t=185s) |
| 3 | The CAGR formula derived | Proof, open web | [Finance Storyteller, CAGR explained, 4:45 to 6:13](https://www.youtube.com/watch?v=F2mlD8Sf-fM&t=285s) |
| 4 | The arithmetic average return | Worked example, open web | [Initial Return, Arithmetic vs geometric average return, 1:30 to 4:40](https://www.youtube.com/watch?v=1HW3XCei_Bg&t=90s) |
| 5 | The geometric average return, which is the CAGR | Worked example, open web | [Initial Return, Arithmetic vs geometric average return, 4:40 to 10:31](https://www.youtube.com/watch?v=1HW3XCei_Bg&t=280s) |
| 6 | Why the two differ, and which one predicts what you end up with | Intuition, open web | [Initial Return, Arithmetic vs geometric average return, 10:31 to 14:03](https://www.youtube.com/watch?v=1HW3XCei_Bg&t=631s) |
| 7 | Volatility drag: +20% then −20% is a 4% loss, and the gap between the two averages is about half the variance | Proof, open web | [The Fintech Builder, Why +20% Then -20% Equals a 4% Loss, 5:26 to 7:08](https://www.youtube.com/watch?v=NCRrt5FljB8&t=326s) |

No listed creator covers CAGR, and none projects a portfolio forward from a CAGR in rand. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Asset allocation

<!-- video-table: asset-allocation rev=1 -->
Ben Felix and Money Marx on choosing how much goes in each asset class, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What goes into a risk profile: tolerance for loss, capacity for it, and need | Intuition, open web | [Ben Felix, Choosing an Asset Allocation, 0:49 to 3:08](https://www.youtube.com/watch?v=p25PPBgMiEk&t=49s) |
| 2 | Risk capacity against risk need, and how both change over time | Proof or rule, open web | [Ben Felix, Choosing an Asset Allocation, 5:29 to 9:44](https://www.youtube.com/watch?v=p25PPBgMiEk&t=329s) |
| 3 | Setting an allocation from a risk profile, with South African funds | Worked example, open web | [Money Marx, How To Determine Which Assets To Invest In, 11:30 to 16:19](https://www.youtube.com/watch?v=VCkkFlWz070&t=690s) |

Neither sets an allocation against Regulation 28 for money inside an RA. Ben Felix runs a portfolio management firm; Money Marx sells a paid course. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Rebalancing a portfolio

<!-- video-table: rebalancing rev=1 -->
Ryan O'Connell, Optimized Portfolio and freefincal on rebalancing a portfolio back to its target, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Why rebalancing means selling what rose and buying what fell | Intuition, open web | [Ryan O'Connell, Portfolio Rebalancing Explained, 0:20 to 1:12](https://www.youtube.com/watch?v=WEAACgD-eME&t=20s) |
| 2 | Two rules: rebalance on a calendar, or when a weight leaves a band | Proof or rule, open web | [Ryan O'Connell, Portfolio Rebalancing Explained, 1:12 to 2:48](https://www.youtube.com/watch?v=WEAACgD-eME&t=72s) |
| 3 | Narrow against wide bands, and what transaction costs do to the choice | Proof or rule, open web | [Ryan O'Connell, Portfolio Rebalancing Explained, 2:48 to 4:30](https://www.youtube.com/watch?v=WEAACgD-eME&t=168s) |
| 4 | Rebalancing each year, worked on a portfolio | Worked example, open web | [freefincal, Portfolio rebalancing: simple examples, 2:03 to 3:15](https://www.youtube.com/watch?v=U251Stb3o5c&t=123s) |
| 5 | The tax a sale triggers in a taxable account | Proof or rule, open web | [Optimized Portfolio, Portfolio Rebalancing Explained, 4:29 to 4:59](https://www.youtube.com/watch?v=IJxgI6P0beU&t=269s) |

None rebalances inside a TFSA, where a sale costs no tax but new money is capped, and freefincal's example uses Indian products. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Index funds and ETFs

<!-- video-table: index-funds-etfs rev=1 -->
Ben Felix and Money Marx on the index fund and the ETF, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What an index fund is | Intuition, open web | [Ben Felix, The Case for Index Funds, 0:51 to 2:53](https://www.youtube.com/watch?v=Nv5CiRSCVxA&t=51s) |
| 2 | Low fees, and what they are worth over time | Proof or rule, open web | [Ben Felix, The Case for Index Funds, 2:53 to 5:21](https://www.youtube.com/watch?v=Nv5CiRSCVxA&t=173s) |
| 3 | Index funds against active funds, and why few managers keep winning | Proof or rule, open web | [Ben Felix, The Case for Index Funds, 6:53 to 10:43](https://www.youtube.com/watch?v=Nv5CiRSCVxA&t=413s) |
| 4 | What an ETF is, on the JSE | Intuition, open web | [Money Marx, The Ultimate Guide To Investing In ETFs, 2:02 to 7:11](https://www.youtube.com/watch?v=dUc-q_k8V6Y&t=122s) |
| 5 | The costs of holding an ETF: TER, brokerage and platform fees | Proof or rule, open web | [Money Marx, The Ultimate Guide To Investing In ETFs, 12:03 to 20:41](https://www.youtube.com/watch?v=dUc-q_k8V6Y&t=723s) |
| 6 | Reading an ETF's minimum disclosure document | Worked example, open web | [Money Marx, The Ultimate Guide To Investing In ETFs, 23:23 to 31:00](https://www.youtube.com/watch?v=dUc-q_k8V6Y&t=1403s) |

Ben Felix uses Canadian and US funds; Money Marx's 2021 TERs and platforms are re-read from the investing reference before use. Neither shows the creation and redemption that keeps an ETF's price near its net asset value. Money Marx sells a paid course; Ben Felix runs a portfolio management firm. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## The unit trust against the ETF

<!-- video-table: unit-trust-against-etf rev=1 -->
Money Marx, The Money Maze, Talking Money With Nozi, EasyEquities and Ivyn Sambo on the unit trust against the ETF, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What a unit trust is | Intuition, open web | [Money Marx, ETFs vs Unit Trusts vs Index Funds, 0:50 to 3:11](https://www.youtube.com/watch?v=g_xGA44r0A8&t=50s) |
| 2 | Where the unit trust, the index fund and the ETF are alike and where they differ | Proof or rule, open web | [Money Marx, ETFs vs Unit Trusts vs Index Funds, 6:50 to 11:43](https://www.youtube.com/watch?v=g_xGA44r0A8&t=410s) |
| 3 | Same destination, different ride: the price you buy at, the net asset value | Intuition, open web | [The Money Maze, ETF vs Unit Trust: NAV, TER, 0:54 to 3:58](https://www.youtube.com/watch?v=DWu20SNecq8&t=54s) |
| 4 | Buying and trading each, then their fees and performance | Proof or rule, open web | [Talking Money With Nozi, Unit Trusts versus ETFs, 4:48 to 10:29](https://www.youtube.com/watch?v=75nOv9glnPI&t=288s) |
| 5 | The fee structures side by side, from a platform's webinar | Proof or rule, open web | [EasyEquities, ETFs vs Unit Trusts, 12:20 to 17:23](https://www.youtube.com/watch?v=I-s0zVNw0tQ&t=740s) |
| 6 | Performance data for each compared | Worked example, open web | [Ivyn Sambo, Unit Trusts vs. ETFs, 4:34 to 6:37](https://www.youtube.com/watch?v=QsgxFfjY2po&t=274s) |
| 7 | Active against passive funds, and which to choose | Intuition, open web | [Money Marx, ETFs vs Unit Trusts vs Index Funds, 11:43 to 20:32](https://www.youtube.com/watch?v=g_xGA44r0A8&t=703s) |

None prices one rand in a unit trust against the same rand in an ETF over years, with each layer of fees, and none adds the tax a taxable account pays on either. EasyEquities sells both through its platform, and Money Marx sells a paid course. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Investment fees and the TER

<!-- video-table: investment-fees rev=1 -->
The Plain Bagel, Money Marx and JustOneLap on what an investment's fees are and what they take, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What fees are, and the types an investor pays | Intuition, open web | [The Plain Bagel, Fees: How Investments Cost You, 0:31 to 3:56](https://www.youtube.com/watch?v=SQGddlVn8iI&t=31s) |
| 2 | Whether fees even matter, in rand over time | Intuition, open web | [Money Marx, Understanding The Fees on Your Investments, 1:38 to 4:02](https://www.youtube.com/watch?v=2m4D2sfR6Qg&t=98s) |
| 3 | What sits inside a total expense ratio | Proof or rule, open web | [JustOneLap, Definitive Guide to Investment Costs, 5:15 to 8:11](https://www.youtube.com/watch?v=9Gw30wDWOEY&t=315s) |
| 4 | A TER worked from a fund's own figures | Worked example, open web | [JustOneLap, Definitive Guide to Investment Costs, 8:11 to 14:11](https://www.youtube.com/watch?v=9Gw30wDWOEY&t=491s) |
| 5 | Admin, platform and brokerage fees, the layers above the fund | Proof or rule, open web | [Money Marx, Understanding The Fees on Your Investments, 4:02 to 12:13](https://www.youtube.com/watch?v=2m4D2sfR6Qg&t=242s) |
| 6 | Finding the fees on an ETF, then on a unit trust | Worked example, open web | [Money Marx, Understanding The Fees on Your Investments, 21:19 to 26:37](https://www.youtube.com/watch?v=2m4D2sfR6Qg&t=1279s) |

None derives the terminal-value gap between two fee levels, the (1 + r − f)ⁿ form §12 uses. Money Marx sells a paid course; JustOneLap belongs to an investment platform. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## South African investment platforms

<!-- video-table: investment-platforms rev=1 -->
Financial Bunny on choosing a South African investment platform, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | EasyEquities: what it offers and what it charges | Worked example, open web | [Financial Bunny, Which Investment Platform should I use, 4:13 to 9:47](https://www.youtube.com/watch?v=hZnuxUTMrCA&t=253s) |
| 2 | An app-based platform, then a money market option | Intuition, open web | [Financial Bunny, Which Investment Platform should I use, 9:47 to 13:50](https://www.youtube.com/watch?v=hZnuxUTMrCA&t=587s) |
| 3 | Standard Bank's offering | Intuition, open web | [Financial Bunny, Which Investment Platform should I use, 13:50 to 16:47](https://www.youtube.com/watch?v=hZnuxUTMrCA&t=830s) |

The video is from March 2021, and fees and products have changed since; the current fees are in the investing reference, and the fee layers themselves are in the investment fees table. It does not open a TFSA or place an ETF order on screen. Times are chapter boundaries read from the video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## The effective annual cost and early exit charges

<!-- video-table: effective-annual-cost rev=1 -->
Two fee-based advisers on The Enough Club and an Old Mutual presenter on the effective annual cost, commission and the charge for leaving early, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The rows of the cost table: investment management, administration (the platform) and "other" | Intuition, open web | [The Enough Club, How to Spot Rubbish Investment Products, 2:23 to 3:05](https://www.youtube.com/watch?v=3JotFH9N6pQ&t=143s) |
| 2 | Platform fees of 0.1% to 0.58% including VAT; a 10% return less a 1% fee leaves 9% | Worked example, open web | [The Enough Club, How to Spot Rubbish Investment Products, 5:05 to 6:07](https://www.youtube.com/watch?v=3JotFH9N6pQ&t=305s) |
| 3 | What "other" hides: brokerage, and commission on a policy-based product | Proof or rule, open web | [The Enough Club, How to Spot Rubbish Investment Products, 6:07 to 7:20](https://www.youtube.com/watch?v=3JotFH9N6pQ&t=367s) |
| 4 | Why a policy RA or endowment charges you to leave: the adviser's upfront commission is recovered from you over 5 to 10 years | Proof or rule, open web | [The Enough Club, How to Spot Rubbish Investment Products, 8:01 to 11:01](https://www.youtube.com/watch?v=3JotFH9N6pQ&t=481s) |
| 5 | The payback test: 3% in fees against 1% saves about R5,000 a year against a R15,000 penalty, so moving pays back in three years | Worked example, open web | [The Enough Club, How to Spot Rubbish Investment Products, 12:05 to 12:49](https://www.youtube.com/watch?v=3JotFH9N6pQ&t=725s) |
| 6 | One real old RA at 3.8% a year against 0.22% elsewhere, ten years from retirement, after a R10,000 to R12,000 penalty | Worked example, open web | [The Enough Club, How to Spot Rubbish Investment Products, 13:11 to 14:46](https://www.youtube.com/watch?v=3JotFH9N6pQ&t=791s) |
| 7 | Turning a year's fees into a percentage of average assets, row by row, on a 100-member fund | Worked example, open web | [Old Mutual, Retirement Savings Cost Disclosure, 22:21 to 25:28](https://www.youtube.com/watch?v=uR7V5QH7-y4&t=1341s) |
| 8 | What a good total is: institutional about 2%, retail 2.5% to 3%, a new fund 4% to 6% | Proof or rule, open web | [Old Mutual, Retirement Savings Cost Disclosure, 36:30 to 37:12](https://www.youtube.com/watch?v=uR7V5QH7-y4&t=2190s) |

Neither names section 54 of the Long-term Insurance Act or works an early termination charge from a quote's own table. The Enough Club advisers gain when a viewer moves to a provider they use, and Old Mutual is a product provider speaking to advisers in 2019. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## How financial advisers are paid

<!-- video-table: adviser-pay rev=1 -->
Honest Money on how South African financial advisers are paid, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Upfront fees | Proof or rule, open web | [Honest Money, From Commissions to Clarity, 4:06 to 7:16](https://www.youtube.com/watch?v=tG4mDA5xU5Q&t=246s) |
| 2 | The remuneration models, and the fees under each | Proof or rule, open web | [Honest Money, From Commissions to Clarity, 7:16 to 13:50](https://www.youtube.com/watch?v=tG4mDA5xU5Q&t=436s) |
| 3 | Commission-based models | Proof or rule, open web | [Honest Money, From Commissions to Clarity, 18:37 to 21:55](https://www.youtube.com/watch?v=tG4mDA5xU5Q&t=1117s) |

No video prices one adviser's commission on a real quote; the effective annual cost table works the cost that commission adds. Honest Money is an advice firm's channel, and its last chapter, from 21:55, is about the firm itself. Times are chapter boundaries read from the video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## The tax-free savings account

<!-- video-table: tfsa rev=1 -->
Money Marx, Lomaku by Nokuhle, Investec, Sinikiwe Ngcobo and CA Campus on the tax-free savings account, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What tax an ordinary investment pays on interest, dividends and gains, which is what a TFSA removes | Intuition, open web | [Money Marx, TFSA Explained, 0:34 to 3:03](https://www.youtube.com/watch?v=E9W9Y9KMUls&t=34s) |
| 2 | The same R1,000 a month invested with tax and without it | Worked example, open web | [Lomaku by Nokuhle, TFSA Explained with R1000/month, 0:19 to 2:34](https://www.youtube.com/watch?v=2esMiBnRH8I&t=19s) |
| 3 | A TFSA against ordinary savings, from a bank's side | Intuition, open web | [Investec, How do tax-free savings accounts work?, 3:45 to 5:00](https://www.youtube.com/watch?v=rtvI8NlDydE&t=225s) |
| 4 | The rules: the annual and lifetime limits and what counts toward them | Proof or rule, open web | [Money Marx, TFSA Explained, 3:35 to 5:46](https://www.youtube.com/watch?v=E9W9Y9KMUls&t=215s) |
| 5 | Working out the limits and the years to fill the lifetime one | Worked example, open web | [Money Marx, TFSA Explained, 6:44 to 8:11](https://www.youtube.com/watch?v=E9W9Y9KMUls&t=404s) |
| 6 | Why taking money out and putting it back uses up room for good | Intuition, open web | [Sinikiwe Ngcobo, The 5 savings account types, 6:33 to 8:37](https://www.youtube.com/watch?v=7n282AiN0jA&t=393s) |
| 7 | Section 12T of the Income Tax Act: the limits and the 40% penalty on going over | Proof or rule, open web | [CA Campus, Exempt Income: Tax Free investments, 1:52 to 5:32](https://www.youtube.com/watch?v=Mv66xvvJHWk&t=112s) |
| 8 | Section 12T on moving between providers and reinvesting | Proof or rule, open web | [CA Campus, Exempt Income: Tax Free investments, 5:32 to 7:18](https://www.youtube.com/watch?v=Mv66xvvJHWk&t=332s) |

The videos date from 2020 to 2025 and show an annual limit of R36,000; it is R46,000 from 2026/27 (§13), so every limit is read from the statutory pull. None works the capital gains tax a TFSA saves on a real projection. Money Marx sells a paid course; Investec is a bank selling a TFSA. Row 6 is read from automatic captions and good to about 30 seconds; the others are chapter boundaries from each video's chapter list, so the sentence inside each is not checked.
<!-- /video-table -->

## The retirement annuity

<!-- video-table: retirement-annuity rev=1 -->
Maya Fisher-French and Family Wealth on how a retirement annuity is taxed and what it costs you in freedom, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Contributions are deducted from taxable income | Proof or rule, open web | [Maya On Money, How Tax Works On Your Retirement Fund, 0:25 to 1:01](https://www.youtube.com/watch?v=O4zn1yzHurY&t=25s) |
| 2 | Growth inside the fund is not taxed | Proof or rule, open web | [Maya On Money, How Tax Works On Your Retirement Fund, 1:01 to 1:54](https://www.youtube.com/watch?v=O4zn1yzHurY&t=61s) |
| 3 | How withdrawals and the payout at retirement are taxed | Proof or rule, open web | [Maya On Money, How Tax Works On Your Retirement Fund, 1:54 to 2:48](https://www.youtube.com/watch?v=O4zn1yzHurY&t=114s) |
| 4 | The deduction as the main benefit | Proof or rule, open web | [Family Wealth, Pros and Cons: Retirement Annuities, 1:24 to 4:10](https://www.youtube.com/watch?v=NfrKsADsmtM&t=84s) |
| 5 | Less freedom in what it holds, under Regulation 28 | Proof or rule, open web | [Family Wealth, Pros and Cons: Retirement Annuities, 8:56 to 9:43](https://www.youtube.com/watch?v=NfrKsADsmtM&t=536s) |
| 6 | Why the deduction does not guarantee the best outcome | Intuition, open web | [Family Wealth, Pros and Cons: Retirement Annuities, 9:43 to 10:30](https://www.youtube.com/watch?v=NfrKsADsmtM&t=583s) |
| 7 | Contributions above the deductible limit, and how they come back tax-free later | Proof or rule, open web | [Family Wealth, Pros and Cons: Retirement Annuities, 12:48 to 16:30](https://www.youtube.com/watch?v=NfrKsADsmtM&t=768s) |

Neither works the deduction in rand at a given marginal rate; the Money with Carla table does that. Maya's 2021 video predates two-pot. Family Wealth is an advice practice. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## The TFSA against the retirement annuity

<!-- video-table: tfsa-against-ra rev=1 -->
Money Marx, Family Wealth and Talking Money With Nozi on the TFSA against the retirement annuity, point by point, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Contributions: deductible into an RA, from after-tax money into a TFSA | Proof or rule, open web | [Money Marx, TFSA vs Retirement Annuity, 3:52 to 4:58](https://www.youtube.com/watch?v=Vt2souiFcbY&t=232s) |
| 2 | The contribution limits on each | Proof or rule, open web | [Money Marx, TFSA vs Retirement Annuity, 4:58 to 6:06](https://www.youtube.com/watch?v=Vt2souiFcbY&t=298s) |
| 3 | The tax benefits compared, with the figures updated for 2026 | Worked example, open web | [Family Wealth, RA vs TFSA: Which One Wins? 2026, 3:35 to 6:22](https://www.youtube.com/watch?v=k99D3K6GqNw&t=215s) |
| 4 | What each may invest in, and when the money can be reached | Proof or rule, open web | [Money Marx, TFSA vs Retirement Annuity, 6:37 to 8:55](https://www.youtube.com/watch?v=Vt2souiFcbY&t=397s) |
| 5 | Tax when the money comes out, and how each treats creditors and estate duty | Proof or rule, open web | [Money Marx, TFSA vs Retirement Annuity, 8:55 to 10:32](https://www.youtube.com/watch?v=Vt2souiFcbY&t=535s) |
| 6 | Access and liquidity, including two-pot | Proof or rule, open web | [Family Wealth, RA vs TFSA: Which One Wins? 2026, 8:50 to 11:22](https://www.youtube.com/watch?v=k99D3K6GqNw&t=530s) |
| 7 | The two compared for one listener's question | Proof or rule, open web | [Talking Money With Nozi, RA vs TFSA: What's Best for You?, 5:15 to 7:34](https://www.youtube.com/watch?v=3eON2om3wVo&t=315s) |
| 8 | How to choose between them | Intuition, open web | [Money Marx, TFSA vs Retirement Annuity, 10:32 to 15:04](https://www.youtube.com/watch?v=Vt2souiFcbY&t=632s) |

Neither puts voluntary contributions to an employer's provident fund in the comparison, and Money Marx's 2021 video predates two-pot and the current limits, which Family Wealth's 2026 one covers. Money Marx sells a paid course; Family Wealth is an advice practice. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## A retirement annuity against investing outside one

<!-- video-table: ra-against-discretionary rev=1 -->
Money with Carla on a retirement annuity against investing the same money outside it, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | R2.2m of taxable income: a maxed RA cuts the tax by R157,000 at 45%, so the investor without one has only that much less to invest | Worked example, open web | [Money with Carla, The 19yr Rule, 1:03 to 3:27](https://www.youtube.com/watch?v=YvhqMnitZKk&t=63s) |
| 2 | Regulation 28: at most 75% in equities and 45% offshore | Proof or rule, open web | [Money with Carla, The 19yr Rule, 4:10 to 5:35](https://www.youtube.com/watch?v=YvhqMnitZKk&t=250s) |
| 3 | Return assumptions for an RA fund and two ETFs, and their 30-year values | Worked example, open web | [Money with Carla, The 19yr Rule, 6:58 to 8:24](https://www.youtube.com/watch?v=YvhqMnitZKk&t=418s) |
| 4 | Tax at the end: the first part of the retirement lump sum tax-free, the rest on the lump sum table, and gains outside at an effective 18% | Proof or rule, open web | [Money with Carla, The 19yr Rule, 8:24 to 10:08](https://www.youtube.com/watch?v=YvhqMnitZKk&t=504s) |
| 5 | The after-tax break-even year against each ETF | Worked example, open web | [Money with Carla, The 19yr Rule, 11:11 to 12:36](https://www.youtube.com/watch?v=YvhqMnitZKk&t=671s) |
| 6 | Her rule of thumb: under about 45, question whether an RA beats a discretionary ETF | Proof or rule, open web | [Money with Carla, The 19yr Rule, 13:18 to 15:02](https://www.youtube.com/watch?v=YvhqMnitZKk&t=798s) |

She models the 45% bracket and the R350,000 cap of 2025, so the arithmetic is redone at your own marginal rate and the current cap; the return gap is an assumption across funds with different start dates, and two-pot access and dividend tax on the ETF are left out. She sells a retirement calculator and a short course. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## The provident fund and the two-pot system

<!-- video-table: provident-fund-two-pot rev=1 -->
The FSCA, a Sanlam spokesperson, Lomaku by Nokuhle, Yvonne of Freely, SARS and Money with Carla on the provident fund and the two-pot system, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Employer funds, compulsory with the job, against voluntary funds such as an RA or a preservation fund; you can hold both | Proof or rule, open web | [FSCA 101, Understanding retirement funds, 2:47 to 4:30](https://www.youtube.com/watch?v=O9T4UaE6CXk&t=167s) |
| 2 | Pension against provident, and the 1 March 2021 change that put new provident money under the one-third cash rule | Proof or rule, open web | [FSCA 101, Understanding retirement funds, 5:55 to 6:59](https://www.youtube.com/watch?v=O9T4UaE6CXk&t=355s) |
| 3 | R100,000 built up before 1 March 2021 stays cashable; of R300,000 paid in after, one third is cash and two thirds buy an annuity | Worked example, open web | [FSCA 101, Understanding retirement funds, 7:40 to 10:06](https://www.youtube.com/watch?v=O9T4UaE6CXk&t=460s) |
| 4 | From 1 September 2024: the vested pot keeps the old money and the savings pot is seeded with 10% of it, up to R30,000 | Proof or rule, open web | [Prof Terrence Kommal, 2-Pot Retirement System, 3:26 to 5:31](https://www.youtube.com/watch?v=TvQSSglfbGc&t=206s) |
| 5 | A R1,000 contribution splits one third to the savings pot and two thirds to the retirement pot | Worked example, open web | [Prof Terrence Kommal, 2-Pot Retirement System, 9:15 to 9:35](https://www.youtube.com/watch?v=TvQSSglfbGc&t=555s) |
| 6 | A withdrawal is taxed at your marginal rate, one a tax year, and R1 taken now could have been R30 at retirement | Proof or rule, open web | [Prof Terrence Kommal, 2-Pot Retirement System, 12:39 to 13:19](https://www.youtube.com/watch?v=TvQSSglfbGc&t=759s) |
| 7 | Who may withdraw, how much, and limits on each withdrawal | Proof or rule, open web | [Yvonne, How and When to Withdraw Under Two Pot, 4:06 to 5:20](https://www.youtube.com/watch?v=fx-qAdST_1A&t=246s) |
| 8 | Three worked withdrawals | Worked example, open web | [Lomaku by Nokuhle, What Is The Two Pot System, 6:58 to 12:44](https://www.youtube.com/watch?v=cBrMU8fpkis&t=418s) |
| 9 | SARS's own withdrawal examples with its tax calculator | Worked example, open web | [SARS TV, Two-Pot and its Tax Implications, 5:02 to 6:09](https://www.youtube.com/watch?v=BlFmDJnW-fE&t=302s) |
| 10 | Two scenarios compared: withdrawing from the savings pot against leaving it invested | Worked example, open web | [Money with Carla, South Africa's New Two-Pot System Explained, 8:31 to 11:58](https://www.youtube.com/watch?v=qBlQE39jf_Y&t=511s) |
| 11 | Providers charge an admin fee on each withdrawal | Proof or rule, open web | [Prof Terrence Kommal, 2-Pot Retirement System, 15:45 to 16:05](https://www.youtube.com/watch?v=TvQSSglfbGc&t=945s) |
| 12 | On death the fund's trustees decide who receives the benefit, guided by your nomination form; it is protected from creditors and falls outside the estate | Proof or rule, open web | [FSCA 101, Understanding retirement funds, 18:45 to 20:53](https://www.youtube.com/watch?v=O9T4UaE6CXk&t=1125s) |

None compares extra voluntary contributions to a provident fund with a separate RA. The FSCA episode is from March 2024, before two-pot, and the Kommal interview leaves out the R2,000 minimum withdrawal; its guest works for a product provider. Rows 1 to 6, 11 and 12 are read from automatic captions and good to about 30 seconds; rows 7 to 10 are chapter boundaries from each video's chapter list, so the sentence inside each is not checked.
<!-- /video-table -->

## The section 54 endowment

<!-- video-table: section-54-endowment rev=1 -->
Financially Fabulous Females, Money Marx, Honest Money and Rebaone Nameng on the endowment, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Why advisers sell endowments first: forced discipline and high commission | Intuition, open web | [Financially Fabulous Females, South African Endowments, 0:41 to 1:22](https://www.youtube.com/watch?v=LAL6_bXoSw8&t=41s) |
| 2 | Taxed at about 30% inside the policy, so it pays off only in a high bracket; a minimum term of five years | Proof or rule, open web | [Financially Fabulous Females, South African Endowments, 1:22 to 2:44](https://www.youtube.com/watch?v=LAL6_bXoSw8&t=82s) |
| 3 | An earner on R1.9m: R18,000 of tax on a R100,000 gain outside against R12,000 inside, and R45,000 against R30,000 on R100,000 of interest | Worked example, open web | [Money Marx, Endowments, 0:21 to 1:24](https://www.youtube.com/watch?v=qvCa2et4jYE&t=21s) |
| 4 | The rule behind it: a flat 30% on income and an effective 12% on gains inside, against your marginal rate outside | Proof or rule, open web | [Money Marx, Endowments, 1:24 to 2:48](https://www.youtube.com/watch?v=qvCa2et4jYE&t=84s) |
| 5 | Against an RA: no Regulation 28 limits, the five-year restriction with one withdrawal allowed, payouts not taxed in your hands | Proof or rule, open web | [Money Marx, Endowments, 3:09 to 4:32](https://www.youtube.com/watch?v=qvCa2et4jYE&t=189s) |
| 6 | Paid directly to a nominated beneficiary instead of passing through the estate | Proof or rule, open web | [Financially Fabulous Females, South African Endowments, 3:45 to 4:25](https://www.youtube.com/watch?v=LAL6_bXoSw8&t=225s) |
| 7 | An endowment against a discretionary investment held outside one | Intuition, open web | [Honest Money, The Endowment Advantage, 1:10 to 7:40](https://www.youtube.com/watch?v=x4Sb5WCC8Ao&t=70s) |
| 8 | How each is taxed, for a high earner | Proof or rule, open web | [Honest Money, The Endowment Advantage, 7:40 to 12:26](https://www.youtube.com/watch?v=x4Sb5WCC8Ao&t=460s) |
| 9 | Endowments against unit trusts | Proof or rule, open web | [The loading zone with Rebaone Nameng, Endowments and Unit trusts, 6:46 to 9:46](https://www.youtube.com/watch?v=hWVwD6a5tBY&t=406s) |
| 10 | The 120% rule: R100,000 in years one and two caps year three at R120,000, and going over restarts the five years | Worked example, open web | [Money Marx, Endowments, 5:35 to 6:16](https://www.youtube.com/watch?v=qvCa2et4jYE&t=335s) |
| 11 | Who it suits: a 31% bracket or higher, and a goal more than five years away | Proof or rule, open web | [Money Marx, Endowments, 7:59 to 8:41](https://www.youtube.com/watch?v=qvCa2et4jYE&t=479s) |

None names section 54 of the Long-term Insurance Act, which sets the five-year restriction and the one withdrawal, none prices an early termination charge, and none works the comparison at the 41% bracket; Money Marx's rule row gives each bracket's rate, and none says whether the payout still counts toward estate duty. Financially Fabulous Females is a commission-earning adviser; Money Marx sells a paid course. Rows 7 to 9 are chapter boundaries from each video's chapter list, so the sentence inside each is not checked; the rest are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## Life cover premium patterns

<!-- video-table: life-cover-premium-patterns rev=1 -->
Three South African advisers on how a risk policy's premium grows, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Level, inflation-linked and age-rated premium patterns, and that some insurers let you switch later | Proof or rule, open web | [Financially Fabulous Females, How to Buy Life Insurance, 1:22 to 3:27](https://www.youtube.com/watch?v=pMJWbIeGvzI&t=82s) |
| 2 | For a 30-year-old, age-rated starts cheapest, then renewable, then level; renewable jumps at year 15 and every five years after | Proof or rule, open web | [Fincology, Your life policy premium increases, 0:20 to 1:23](https://www.youtube.com/watch?v=HXCXDtGesxs&t=20s) |
| 3 | At year 15 level is R3,523 against age-rated R3,604, so age-rated has overtaken | Worked example, open web | [Fincology, Your life policy premium increases, 1:23 to 2:06](https://www.youtube.com/watch?v=HXCXDtGesxs&t=83s) |
| 4 | Escalation compounds: average premiums rise about 12% a year against salaries at 4.2% | Proof or rule, open web | [Marnus Mostert, The Dark Side of Compound Interest on Premiums, 1:21 to 2:26](https://www.youtube.com/watch?v=4Zuj4oAu6Xs&t=81s) |
| 5 | Split by benefit: cover kept for life on a gentle fixed pattern, disability, which ends at retirement, on a cheaper steep one | Proof or rule, open web | [Marnus Mostert, The Dark Side of Compound Interest on Premiums, 3:48 to 5:13](https://www.youtube.com/watch?v=4Zuj4oAu6Xs&t=228s) |
| 6 | Benefit escalation is separate from premium escalation | Proof or rule, open web | [Financially Fabulous Females, How to Buy Life Insurance, 4:08 to 4:51](https://www.youtube.com/watch?v=pMJWbIeGvzI&t=248s) |
| 7 | Price guarantee periods, often 5 years at a bank and 10 to 15 elsewhere | Proof or rule, open web | [Financially Fabulous Females, How to Buy Life Insurance, 4:51 to 6:14](https://www.youtube.com/watch?v=pMJWbIeGvzI&t=291s) |

None sums the premiums paid under each pattern to retirement, which is the number that settles the choice, and none offsets cover an employer already pays for. All three presenters are advisers paid on the policies they discuss. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## Marital regimes, wills and estate duty

<!-- video-table: marriage-and-estate rev=1 -->
Legal Leaders, The Conversation Capital, Point in Limine and Shela on marital regimes, wills and estate duty in South Africa, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | In community of property, out of community, and out of community with the accrual system | Proof or rule, open web | [Legal Leaders, Antenuptial Contracts With and Without Accrual, 1:05 to 3:22](https://www.youtube.com/watch?v=ZakRV0v9mC0&t=65s) |
| 2 | Out of community with accrual, explained by a family lawyer | Proof or rule, open web | [The Conversation Capital, Types Of Marital Contracts, 10:25 to 12:08](https://www.youtube.com/watch?v=c65z9DTXHK0&t=625s) |
| 3 | Calculating the accrual claim, and what is excluded from it | Worked example, open web | [The Conversation Capital, Types Of Marital Contracts, 12:08 to 15:01](https://www.youtube.com/watch?v=c65z9DTXHK0&t=728s) |
| 4 | Pension money against estate assets on death | Proof or rule, open web | [The Conversation Capital, Types Of Marital Contracts, 35:13 to 37:23](https://www.youtube.com/watch?v=c65z9DTXHK0&t=2113s) |
| 5 | Appointing an executor, and who may and may not inherit under a will | Proof or rule, open web | [Point in Limine, Important Things to Know about Wills, 1:54 to 5:35](https://www.youtube.com/watch?v=m297oclyu5w&t=114s) |
| 6 | What marriage does to an existing will and to the estate | Proof or rule, open web | [Point in Limine, Important Things to Know about Wills, 9:06 to 10:56](https://www.youtube.com/watch?v=m297oclyu5w&t=546s) |
| 7 | The estate duty formula | Proof or rule, open web | [Shela, Wills and Estates 6: Estate Duty Addendum, 5:55 to 9:29](https://www.youtube.com/watch?v=GFFoSuw46lQ&t=355s) |
| 8 | What counts as deemed property in the estate | Proof or rule, open web | [Shela, Wills and Estates 6: Estate Duty Addendum, 15:58 to 20:43](https://www.youtube.com/watch?v=GFFoSuw46lQ&t=958s) |
| 9 | A full estate duty computation, then the executor's fee | Worked example, open web | [Shela, Wills and Estates 6: Estate Duty Addendum, 37:26 to 56:33](https://www.youtube.com/watch?v=GFFoSuw46lQ&t=2246s) |

None covers dying with no will under the Intestate Succession Act. Legal Leaders and the Conversation Capital guest are practising lawyers; Shela teaches law students for an exam, and every abatement, rate and fee ceiling comes from the statutory pull. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Marginal against effective tax rate

<!-- video-table: marginal-vs-effective-tax rev=1 -->
The Finance Storyteller on the marginal and the effective tax rate, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Tax brackets and a progressive rate | Intuition, open web | [Finance Storyteller, Marginal tax rate, 0:14 to 0:59](https://www.youtube.com/watch?v=bHGKwQGYlEY&t=14s) |
| 2 | The marginal and the average rate on one income | Worked example, open web | [Finance Storyteller, Marginal tax rate, 0:59 to 1:53](https://www.youtube.com/watch?v=bHGKwQGYlEY&t=59s) |
| 3 | Cutting a taxable income into its brackets | Worked example, open web | [Finance Storyteller, Marginal tax rate, 2:15 to 3:08](https://www.youtube.com/watch?v=bHGKwQGYlEY&t=135s) |
| 4 | What a raise and what a deduction are each worth: both move at the marginal rate | Proof or rule, open web | [Finance Storyteller, Marginal tax rate, 3:08 to 5:03](https://www.youtube.com/watch?v=bHGKwQGYlEY&t=188s) |
| 5 | How close the marginal and the average rate can get | Intuition, open web | [Finance Storyteller, Marginal tax rate, 5:03 to 6:22](https://www.youtube.com/watch?v=bHGKwQGYlEY&t=303s) |

The Finance Storyteller uses no country's real table; the South African brackets are in the brackets-and-rebates table and the statutory pull. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## South African tax brackets and rebates

<!-- video-table: tax-brackets-rebates rev=1 -->
Mtambo Chartered Accountants and Distance learning with Lee on working out South African income tax from the bracket table and the rebates, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Reading the SARS bracket table | Proof or rule, open web | [Mtambo Chartered Accountants, How to Calculate South African Income Tax, 0:00 to 2:54](https://www.youtube.com/watch?v=WGoLL85Err4&t=0s) |
| 2 | Tax on a taxable income worked from the table | Worked example, open web | [Mtambo Chartered Accountants, How to Calculate South African Income Tax, 2:54 to 7:27](https://www.youtube.com/watch?v=WGoLL85Err4&t=174s) |
| 3 | Taking off the rebates | Worked example, open web | [Mtambo Chartered Accountants, How to Calculate South African Income Tax, 7:27 to 9:47](https://www.youtube.com/watch?v=WGoLL85Err4&t=447s) |
| 4 | Building taxable income, then applying the rebates, a second time through | Worked example, open web | [Distance learning with Lee, Total tax payable with rebates, 1:25 to 7:05](https://www.youtube.com/watch?v=2yyNSH5cXdE&t=85s) |
| 5 | Using the monthly PAYE deduction table | Proof or rule, open web | [TMMBS TV, Pay As You Earn and UIF Deductions, 1:51 to 3:42](https://www.youtube.com/watch?v=YFAuLuLILoE&t=111s) |

None divides a year's tax into the monthly PAYE on a payslip, and the brackets on screen are those of 2023 to 2025, so the current table comes from the statutory pull. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## South African capital gains tax

<!-- video-table: capital-gains-tax rev=1 -->
SA Accounting Network and Anrich Marais on South African capital gains tax, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What a capital gain is | Intuition, open web | [SA Accounting Network, Capital Gains Tax, 1:00 to 2:30](https://www.youtube.com/watch?v=SHmvbQVODJs&t=60s) |
| 2 | What triggers it, and the basic formula, proceeds less base cost | Proof or rule, open web | [SA Accounting Network, Capital Gains Tax, 3:52 to 6:31](https://www.youtube.com/watch?v=SHmvbQVODJs&t=232s) |
| 3 | Inclusion rates, then the annual exclusion and other exemptions | Proof or rule, open web | [SA Accounting Network, Capital Gains Tax, 6:31 to 9:21](https://www.youtube.com/watch?v=SHmvbQVODJs&t=391s) |
| 4 | An individual's capital gains tax worked | Worked example, open web | [SA Accounting Network, Capital Gains Tax, 10:32 to 13:43](https://www.youtube.com/watch?v=SHmvbQVODJs&t=632s) |
| 5 | The sale of a second home, worked to the tax payable | Worked example, open web | [Anrich Marais, CGT on the Sale of a Second Home, 3:22 to 7:28](https://www.youtube.com/watch?v=9xRllJzww5Q&t=202s) |

Neither shows the effective rate a given bracket pays (40% of the marginal rate), and the exclusions on screen are those in force when each was recorded in 2023, so the current ones come from the statutory pull. Anrich Marais is a tax practitioner. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Medical tax credits

<!-- video-table: medical-tax-credits rev=1 -->
SA Accounting Network and CA Campus on the medical scheme fees credit and the additional medical expenses credit, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Section 6A, the fixed credit for scheme contributions, and section 6B, the additional credit for what you pay yourself | Proof or rule, open web | [SA Accounting Network, SARS Medical Tax Credits Explained, 2:09 to 3:32](https://www.youtube.com/watch?v=9UfDw6GwWIg&t=129s) |
| 2 | How the 7.5% of income floor works in section 6B | Proof or rule, open web | [SA Accounting Network, SARS Medical Tax Credits Explained, 5:09 to 6:32](https://www.youtube.com/watch?v=9UfDw6GwWIg&t=309s) |
| 3 | Calculations worked step by step | Worked example, open web | [SA Accounting Network, SARS Medical Tax Credits Explained, 18:00 to 22:50](https://www.youtube.com/watch?v=9UfDw6GwWIg&t=1080s) |
| 4 | The formula for a taxpayer under 65, then a comprehensive example | Worked example, open web | [CA Campus, Individuals: Medical rebates, 13:28 to 21:12](https://www.youtube.com/watch?v=6VSW9dQI5ho&t=808s) |

Neither sets the credit beside the RA deduction to show a credit off tax against a deduction off income, which §21 does. The monthly credit amounts change by budget and come from the statutory pull. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Filing the ITR12

<!-- video-table: itr12-filing rev=1 -->
SARS, Andre Bothma, Counttuts and The Tax Cafe on filing the ITR12 on eFiling, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Starting the return and completing the form | Worked example, open web | [SARS TV, How to submit your ITR12, 0:34 to 1:50](https://www.youtube.com/watch?v=ZZjVYJlYUSY&t=34s) |
| 2 | Checking the figures already filled in from IRP5 and IT3 certificates | Worked example, open web | [Andre Bothma, How to submit your 2023 tax return, 1:45 to 3:26](https://www.youtube.com/watch?v=htI3IBYquag&t=105s) |
| 3 | Declaring income the return did not fill in | Worked example, open web | [Andre Bothma, How to submit your 2023 tax return, 3:26 to 4:53](https://www.youtube.com/watch?v=htI3IBYquag&t=206s) |
| 4 | Capturing an IRP5, then interest and investment income, then medical details | Worked example, open web | [Counttuts, How to Submit Individual Returns With IRP5, 16:15 to 24:35](https://www.youtube.com/watch?v=4cmGz1y7RXA&t=975s) |
| 5 | Where retirement annuity contributions go on the return | Worked example, open web | [The Tax Cafe, Submitting an Income Tax Return (ITR12), 9:19 to 9:56](https://www.youtube.com/watch?v=PUYlo0NEH4Y&t=559s) |
| 6 | Calculating, submitting and reading the assessment | Worked example, open web | [SARS TV, How to submit your ITR12, 1:50 to 3:13](https://www.youtube.com/watch?v=ZZjVYJlYUSY&t=110s) |

Neither says when to accept an auto-assessment and when to edit it, and the eFiling screens change each year (SARS's video is from 2019, Bothma's from 2023). Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Provisional tax

<!-- video-table: provisional-tax rev=1 -->
SARS, Prof Jackie Arendse and Chikambure on provisional tax for an individual, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What provisional tax is | Intuition, open web | [SARS TV, Provisional Tax Explained, 0:27 to 1:05](https://www.youtube.com/watch?v=WKhfhEIIPy0&t=27s) |
| 2 | Who is a provisional taxpayer, and the exemptions and thresholds | Proof or rule, open web | [Prof Jackie Arendse, Are You a Provisional Taxpayer?, 3:08 to 8:20](https://www.youtube.com/watch?v=Dx6JORirgZo&t=188s) |
| 3 | The rules for the first and the second payment | Proof or rule, open web | [Prof Jackie Arendse, Calculating Provisional Tax, 2:34 to 6:38](https://www.youtube.com/watch?v=oOf_4w0JjQ4&t=154s) |
| 4 | The basic amount, then the first payment calculated | Worked example, open web | [Prof Jackie Arendse, Calculating Provisional Tax, 6:38 to 14:08](https://www.youtube.com/watch?v=oOf_4w0JjQ4&t=398s) |
| 5 | The second payment calculated | Worked example, open web | [Prof Jackie Arendse, Calculating Provisional Tax, 16:58 to 19:05](https://www.youtube.com/watch?v=oOf_4w0JjQ4&t=1018s) |
| 6 | Penalties and interest for paying too little or too late | Proof or rule, open web | [Chikambure, Provisional Tax Explained Simply, 6:19 to 7:32](https://www.youtube.com/watch?v=MEifer7q0is&t=379s) |

All three are about an individual; none works a company's two payments against its own year-end. Prof Arendse runs tax training courses. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## South African business structures

<!-- video-table: business-structures rev=1 -->
Brendmo Business Hub and Anrich Marais on the South African business structures, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The sole proprietorship: you and the business are one person in law and for tax | Intuition, open web | [Brendmo Business Hub, Business Structures In South Africa, 0:59 to 2:45](https://www.youtube.com/watch?v=f1Gd_JjJ1wI&t=59s) |
| 2 | Partnerships, then the private company (Pty) Ltd | Proof or rule, open web | [Brendmo Business Hub, Business Structures In South Africa, 2:45 to 9:48](https://www.youtube.com/watch?v=f1Gd_JjJ1wI&t=165s) |
| 3 | Sole proprietor against Pty Ltd on tax, for one viewer's figures | Worked example, open web | [Anrich Marais, Sole Proprietor vs Private Company, 1:16 to 5:07](https://www.youtube.com/watch?v=5H-zzohQr-Q&t=76s) |
| 4 | Compliance, and moving from one structure to the other | Proof or rule, open web | [Anrich Marais, Sole Proprietor vs Private Company, 5:07 to 8:00](https://www.youtube.com/watch?v=5H-zzohQr-Q&t=307s) |
| 5 | The personal services provider rule, which can tax a one-person company at a higher rate | Proof or rule, open web | [Anrich Marais, Sole Proprietor vs Private Company, 8:00 to 12:09](https://www.youtube.com/watch?v=5H-zzohQr-Q&t=480s) |

Neither covers limited liability in a claim against the business in any depth. Brendmo sells business services; Anrich Marais is a tax practitioner. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Double-entry bookkeeping

<!-- video-table: double-entry rev=1 -->
Accounting Stuff and Concierge CPA on debits, credits and double entry, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What double entry is, against keeping a single list | Intuition, open web | [Accounting Stuff, Double-Entry Accounting in 2 Minutes, 0:07 to 2:54](https://www.youtube.com/watch?v=cjO8qHM5Wjg&t=7s) |
| 2 | Debits and credits as economic benefit, and which accounts sit on which side | Proof or rule, open web | [Accounting Stuff, Debits and Credits Explained, 0:55 to 2:46](https://www.youtube.com/watch?v=VhwZ9t2b3Zk&t=55s) |
| 3 | The arithmetic behind the rule, from the accounting equation | Proof, open web | [Accounting Stuff, Debits and Credits Explained, 2:46 to 4:09](https://www.youtube.com/watch?v=VhwZ9t2b3Zk&t=166s) |
| 4 | Why every journal entry keeps the equation balanced | Proof, open web | [Concierge CPA, Why Debits and Credits Still Confuse You, 3:56 to 7:04](https://www.youtube.com/watch?v=R_C1Yahl8VA&t=236s) |
| 5 | Four entries posted: rent paid, revenue on account, equipment on a loan, cash from the owner | Worked example, open web | [Concierge CPA, Why Debits and Credits Still Confuse You, 9:19 to 11:56](https://www.youtube.com/watch?v=R_C1Yahl8VA&t=559s) |
| 6 | A T-account worked and closed | Worked example, open web | [Accounting Stuff, T-Accounts in 2 Minutes, 1:53 to 5:20](https://www.youtube.com/watch?v=HxzOssLqF0I&t=113s) |
| 7 | A journal entry written and posted | Worked example, open web | [Accounting Stuff, Journal Entries in 2 Minutes, 1:07 to 3:43](https://www.youtube.com/watch?v=-EfaH-hBnn0&t=67s) |
| 8 | Five practice questions: which account is debited and which credited | Worked example, open web | [Accounting Stuff, 5 Debit and Credit Practice Questions, 1:06 to 6:36](https://www.youtube.com/watch?v=yCOZ7aylC0c&t=66s) |

Neither builds a trial balance from the postings, which §25 ends on. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## The three financial statements

<!-- video-table: financial-statements rev=1 -->
Accounting Stuff, Brian Feroldi and Ryan O'Connell on the three financial statements and how they link, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What the financial statements are for | Intuition, open web | [Accounting Stuff, Financial Statements in 8 Minutes, 0:22 to 1:08](https://www.youtube.com/watch?v=Fi1wkUczuyk&t=22s) |
| 2 | The income statement | Proof or rule, open web | [Accounting Stuff, Financial Statements in 8 Minutes, 3:19 to 4:55](https://www.youtube.com/watch?v=Fi1wkUczuyk&t=199s) |
| 3 | The cash flow statement | Proof or rule, open web | [Accounting Stuff, Financial Statements in 8 Minutes, 4:55 to 8:02](https://www.youtube.com/watch?v=Fi1wkUczuyk&t=295s) |
| 4 | Profit flowing from the income statement into equity on the balance sheet | Proof or rule, open web | [Brian Feroldi, Connecting the Three Statements, 3:20 to 8:25](https://www.youtube.com/watch?v=pRfP-vIkMak&t=200s) |
| 5 | The income statement into the cash flow statement, then the balance sheet into it | Proof or rule, open web | [Brian Feroldi, Connecting the Three Statements, 8:25 to 18:14](https://www.youtube.com/watch?v=pRfP-vIkMak&t=505s) |
| 6 | A coffee stand's three statements built and tied together | Worked example, open web | [Brian Feroldi, How the 3 financial statements link, 7:37 to 9:16](https://www.youtube.com/watch?v=AXBuC2gi1N0&t=457s) |
| 7 | Borrowing, buying equipment and earning a profit, followed through all three | Worked example, open web | [Ryan O'Connell, The 3 Financial Statements Explained, 3:11 to 6:22](https://www.youtube.com/watch?v=CE9HnV3b_jY&t=191s) |

None uses South African terms such as the statement of financial position or a Pty Ltd's retained income. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Salary against dividend from a company

<!-- video-table: salary-against-dividend rev=1 -->
Brendmo Business Hub, SwiftReg and Chikambure on paying yourself from a company by salary, dividend or loan account, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | What decides between a salary and a dividend | Intuition, open web | [Brendmo Business Hub, Salary Or Dividend In South Africa?, 1:55 to 2:53](https://www.youtube.com/watch?v=3uX0iSidfIU&t=115s) |
| 2 | A salary: deductible to the company, taxed through PAYE | Proof or rule, open web | [Chikambure, How to Pay Yourself as a Director, 1:35 to 4:12](https://www.youtube.com/watch?v=i9m2KabLtMc&t=95s) |
| 3 | A dividend: company tax first, then dividends tax | Proof or rule, open web | [Chikambure, How to Pay Yourself as a Director, 4:12 to 6:18](https://www.youtube.com/watch?v=i9m2KabLtMc&t=252s) |
| 4 | Scenarios compared, and the dividend tax broken down | Worked example, open web | [Brendmo Business Hub, Salary Or Dividend In South Africa?, 2:53 to 5:50](https://www.youtube.com/watch?v=3uX0iSidfIU&t=173s) |
| 5 | One payout made each way | Worked example, open web | [Brendmo Business Hub, Salary Or Dividend In South Africa?, 5:50 to 7:10](https://www.youtube.com/watch?v=3uX0iSidfIU&t=350s) |
| 6 | The shareholder's loan account as a third route, and its tax risk | Proof or rule, open web | [SwiftReg, Salary vs Dividend vs Loan Accounts, 1:34 to 3:31](https://www.youtube.com/watch?v=8pTbp7y314I&t=94s) |

None derives the combined dividend rate of 27% then 20% (41.6%) that §27 uses. All three sell company registration or accounting services. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## South African VAT

<!-- video-table: vat rev=1 -->
Counttuts, Anrich Marais, SA Accounting Network and SARS on South African VAT, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Input VAT on what a business buys, output VAT on what it sells | Intuition, open web | [Counttuts, Input VAT vs Output VAT, 0:45 to 4:00](https://www.youtube.com/watch?v=IEf5W-nuv6A&t=45s) |
| 2 | Input VAT as an asset, output VAT as a liability, and when SARS refunds the difference | Proof or rule, open web | [Counttuts, Input VAT vs Output VAT, 4:00 to 6:33](https://www.youtube.com/watch?v=IEf5W-nuv6A&t=240s) |
| 3 | When registration is compulsory | Proof or rule, open web | [Anrich Marais, VAT in South Africa: The Basics, 4:45 to 6:25](https://www.youtube.com/watch?v=cQoGmQv35po&t=285s) |
| 4 | Zero-rated against exempt supplies | Proof or rule, open web | [SA Accounting Network, How does VAT work in South Africa, 10:55 to 13:14](https://www.youtube.com/watch?v=i6izUqHK7uA&t=655s) |
| 5 | The tax fraction, the VAT inside an inclusive price | Proof or rule, open web | [Anrich Marais, VAT in South Africa: The Basics, 1:04:30 to 1:05:20](https://www.youtube.com/watch?v=cQoGmQv35po&t=3870s) |
| 6 | Completing the VAT201 on eFiling | Worked example, open web | [SARS TV, How to Submit the VAT201 on eFiling, 1:14 to 2:32](https://www.youtube.com/watch?v=OTeDE3S7wCo&t=74s) |

None works output less input on a month of sales and purchases in rand. Anrich Marais is a tax practitioner. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->
