---
aliases: [probability distribution, distribution of a random variable, probability mass function, PMF]
---

# Distributions

Mathematics, Statistics, Distributions. One note per family of distributions, and one for the method that draws numbers from any of them.

- [[Inverse Transform Sampling]]: how to turn uniform random numbers into draws from any one-variable distribution by running its CDF backwards: the two-line proof, the exponential, a Rayleigh-type case and the discrete lookup on ten fixed uniforms, where it breaks (the Gaussian has no closed-form inverse, a product of densities has no CDF until normalised), and a 100000-draw check.
- [[Multivariate Normal Distribution]]: the Gaussian over several coordinates, set by a mean vector and a covariance matrix, in a folder: the diagonal case, sampling it, sums of independent draws and why their variances add, products and quotients (including products of Gaussian mixtures), the area a product loses, and powers.
- [[Probability Density Function]]: A probability density function describes a continuous random variable: it is never negative, its total area is 1, and the probability of landing in an interval is the area under it there, so its height at a point can exceed 1.
- [[Marginal Distribution]]: A marginal distribution is the distribution of one variable on its own, found from a joint distribution by summing (or, for densities, integrating) over every value of the other variables.

## Where to learn this

**Probability distribution**, the rule that says how likely each value of a random variable is: a probability mass function for a discrete variable, a density for a continuous one. Also: distribution of a random variable, probability mass function, PMF.

**Textbooks**

- Introduction to probability for data science, section 3.2: [pages 126 to 129](../../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=126). Works the PMF of the number of heads in two coin flips (Example 3.5), defines the PMF (Definition 3.2), and reads it as the ideal histogram a data set approaches.
- Mathematics for machine learning, section 6.2: [pages 184 to 188](../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=184). Discrete probabilities from a table of counts (Example 6.2), continuous probabilities with the density and the CDF (Definitions 6.1 and 6.2), and the two kinds side by side.
- Deep learning textbook, section 3.3: [pages 72 to 74](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=72). A probability distribution as a description of how likely each state is, with probability mass functions for discrete variables and density functions for continuous ones.

**Videos**

- StatQuest, The Main Ideas behind Probability Distributions, Statistical Distribution, 0:41 to 2:15: [watch](https://www.youtube.com/watch?v=oI3hZJqXJuc&t=41s). A distribution as the shape of how often each value turns up. Chapter-timed.
- StatQuest, The Main Ideas behind Probability Distributions, 2:15 to 5:14: [watch](https://www.youtube.com/watch?v=oI3hZJqXJuc&t=135s). A curve as a distribution, with probability read as area. Chapter-timed, from the video lessons index.
- Professor Leonard, Statistics Lecture 5.2: A Study of Probability Distributions, Mean, and Standard Deviation, 0:00 to 1:12:43: [watch](https://www.youtube.com/watch?v=WNgcmn5cXjI&t=0s). A full lecture on discrete probability distributions and the mean and standard deviation of one. Whole video.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook range was read with pdftotext, after finding it through the books' back-of-book indexes and the shelf index's chapter tables. The StatQuest and Professor Leonard chapter lists were read with cache-video-chapters.py; Leonard's lecture has no chapter list, so it is cited whole, and both are described from their titles only. The second StatQuest row also appears in the video lessons index, section "A density integrates to 1". No plan or compiled chapter in the learning tree is about probability distributions in general, so the card has no plans group. The bare word "distribution" is not an alias: in a sample of 25 learning-tree lines, about 7 meant a probability distribution in general, and the rest were file paths, named distributions (marginal, joint, null, Beta, normal, posterior) or other senses (a distribution fee, out-of-distribution).
