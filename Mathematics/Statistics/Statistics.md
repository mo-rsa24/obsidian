# Statistics

Mathematics, Statistics. The topics of probability and inference, one folder each, with notes that have not yet grown a folder listed beside them.

- [[Variance]]: how far a draw lands from its mean, as the average squared miss, and the standard deviation, its square root in the draw's own units.
- [[Covariance]]: Covariance measures how two random variables move together: the average product of their distances from their own means, positive when they rise together and negative when one rises as the other falls.
- [[The Scaling Rule For Variance]]: why multiplying a draw by $c$ multiplies its variance by $c^2$ and its standard deviation by $|c|$, so a wanted variance $v$ needs the multiplier $\sqrt{v}$; worked on a coin and on a 100-step cosine noise schedule.
- [[Running The Scaling Rule For Variance]]: the scaling rule run in an empty folder: a coin, the share slip, 200,000 scaled draws, the moment form, two coordinates and all five schedule levels, each output read field by field.
- [[Scaling And Shifting A Random Variable]]: the mean and variance of $aX + b$: the mean is scaled and shifted, the variance is scaled by $a^2$ and never feels the shift, worked on a fair die.
- [[The Average Of A Product Of Independent Variables]]: for independent $X$ and $Y$, $\mathbb{E}[g(X)\,h(Y)] = \mathbb{E}[g(X)]\,\mathbb{E}[h(Y)]$, because the joint table of chances splits into two single tables; worked on two dice and on a die with a coin, broken by reading one die twice, and the step that removes the cross term when variances add.
- [[Moment Generating Function]]: the fingerprint $M_Z(\lambda) = \mathbb{E}[e^{\lambda Z}]$ that fixes a distribution, the standard normal's $e^{\lambda^2/2}$ by completing the square, why the fingerprint of an independent sum is the product, and the coin-flip sum that has a bell's variance but not its shape.
- [[Central Limit Theorem]]: why a sum of many independent draws, scaled by $\frac{1}{\sqrt n}$, approaches the standard bell whatever one draw looks like: the fingerprints of a lopsided variable's scaled sums closing in on $e^{1/2}$, the two wrong scalings, what the fingerprints do not prove, and the fourth moment of a sum, $n\,\mathbb{E}[X^4] + 3n(n-1)(\mathbb{E}[X^2])^2$.
- [[Distributions]]: the named probability distributions, their densities, how they are stored in code, and how to draw numbers from them by the inverse CDF.
- [[Markov Chain Monte Carlo]]: drawing samples from a density with a chain whose moves leave it unchanged: annealed MCMC, and the step size and accept step.
- [[Least Squares Line]]: the straight line that makes the sum of squared vertical misses smallest, found from the two normal equations, $b = S_{xy}/S_{xx}$ and $a = \bar y - b\,\bar x$, worked on four points and broken by dropping the intercept.
- [[Correlation Coefficient]]: how closely two columns rise and fall together, as covariance over the product of the standard deviations, and phi, its form for two yes-or-no columns.
- [[Bootstrap]]: how much a number computed from one sample would move on another sample of the same size, found by resampling: the standard error, the middle-90% percentile range, and the failure when rows come in groups.
- [[Chance-Corrected Agreement]]: how far two raters agree beyond what their own yes-rates give by luck: percent agreement, Cohen's kappa, Scott's pi, phi and the factor linking kappa to phi, the kappa paradox, and which way a judge errs.
- [[Selective Evaluation]]: letting a judge answer only when it is confident, and choosing the confidence cut-off from a small labelled set so the answers agree with people at a rate you set.
- [[Probability]]: Probability assigns each event, a set of possible outcomes, a number from 0 to 1 that measures how likely it is, following three axioms: no negative values, 1 for the whole sample space, and addition over disjoint events.
- [[Histogram]]: A histogram splits the range of a variable into bins and draws one bar per bin, its height the count of data points that land there, or that count divided by the total and the bin width so the bars have area 1.
- [[Monte Carlo Estimation]]: Monte Carlo estimation replaces an expectation or an integral by the average of a function over random samples, so the answer is approximate and its error shrinks like one over the square root of the number of samples.
- [[Bayesian Inference]]: Bayesian inference treats an unknown parameter as a random variable, starts from a prior belief about it, and uses Bayes' theorem to turn that prior and the data's likelihood into a posterior distribution.
- [[Hypothesis Testing]]: A hypothesis test asks whether data are surprising enough under a default claim, the null hypothesis, to reject it, and the p-value is the chance under that claim of a result at least as extreme as the one seen.
- [[Information Theory]]: Information theory measures uncertainty and surprise in bits or nats.
- [[Sampling From A Distribution]]: Sampling from a distribution means producing random values whose long-run frequencies follow it, usually by transforming uniform random numbers the computer already has.
