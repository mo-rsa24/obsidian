# Distributions

Mathematics, Statistics, Distributions. One note per family of distributions.

- [[Multivariate Normal Distribution]]: the Gaussian over several coordinates, set by a mean vector and a covariance matrix; the diagonal case stored as a (mean, per-coordinate variance) pair, sampled by a shift and a stretch, and multiplied or divided by adding and subtracting precisions; a product of two densities has area $\mathcal{N}(m_1; m_2, v_1 + v_2)$ rather than 1, which leaves its score unchanged; and a Gaussian raised to a power scales its precision, so a weighted product or a quotient is a Gaussian only while the precisions sum above 0, and one Gaussian to the power $\beta$ keeps its mean with variance $\sigma^2 / \beta$; and a product of two Gaussian mixtures is a mixture over every pair of components, each weighted by how much its pair overlaps.
