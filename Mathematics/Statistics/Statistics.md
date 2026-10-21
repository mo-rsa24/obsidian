# Statistics

Mathematics, Statistics. The topics of probability and inference, one folder each, with notes that have not yet grown a folder listed beside them.

- [[Variance]]: how far a draw lands from its mean, as the average squared miss, and why multiplying a draw by $c$ multiplies its variance by $c^2$ and its standard deviation by $|c|$.
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
