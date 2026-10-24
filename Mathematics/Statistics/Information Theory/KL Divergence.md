---
aliases: [KL divergence, Kullback-Leibler divergence, Kullback Leibler divergence, relative entropy, KL]
standard: vault-note v2
---

# KL Divergence

Up: [[Information Theory]]

Mathematics, Statistics, Information Theory. [[Entropy]] and [[Cross-Entropy]] are the two terms whose difference it is, and [[Evidence Lower Bound]] is written as a sum of KL terms.

**The KL divergence KL(p‖q) = Σ p(x) log (p(x)/q(x)) is the average extra cost, in bits or nats, of coding draws from p with a code built for q: never negative, zero only when p = q, and not symmetric.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the KL divergence writes the rest around it.

## Where to learn this

**KL divergence**, how far one distribution is from another as the expected log ratio of their probabilities. Also: Kullback-Leibler divergence, relative entropy, KL.

**Textbooks**

- Probabilistic machine learning: an introduction, section 6.2: [pages 243 to 246](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=243). The definition and its reading as extra bits, the closed form between two Gaussians (section 6.2.3), the proof that it is never negative, why maximum likelihood minimises it, and forward against reverse KL.
- Pattern recognition and machine learning, section 1.6.1: [pages 74 to 76](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=74). Relative entropy as the extra information needed to code with the wrong distribution (equation 1.113), then convexity and Jensen's inequality to prove KL(p‖q) ≥ 0.
- Probabilistic machine learning: advanced topics, section 5.1: [pages 250 to 256](../../references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=250). Why KL is the divergence that meets a list of desired properties, its chain rule, units and asymmetry, and minimising forwards against reverse KL.
- Understanding deep learning, appendix C.5: [pages 474 to 475](../../references/textbooks/machine-learning/understanding-deep-learning.pdf#page=474). The KL divergence defined for densities, why it is infinite where q is zero but p is not, and distances between two normal distributions.
- Deep learning textbook, section 3.13: [pages 90 to 92](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=90). The KL divergence after Shannon entropy, and how its asymmetry changes what minimising it in each direction gives (Figure 3.6).

**Videos**

- Luis Serrano, KL Divergence, 10:50 to 12:11: [watch](https://www.youtube.com/watch?v=sjgZxuCm_8Q&t=650s). Computes the KL number from the probabilities of a fair and a biased die. Chapter-timed, from the video lessons index.
- CME296 lecture 1, 1:05:11 to 1:09:22: [watch](https://www.youtube.com/watch?v=tr-CUpw--ck&t=3911s). Reviews KL divergence and states that the diffusion ELBO reduces to KL terms between the forward posterior and the model. Caption-read.
- CME296 lecture 1, 1:17:11 to 1:21:15: [watch](https://www.youtube.com/watch?v=tr-CUpw--ck&t=4631s). Shows the KL between two Gaussians collapsing to an L2 loss between predicted and added noise. Caption-read.
- Stanford CS236, lecture 4, 39:00 to 54:49: [watch](https://www.youtube.com/watch?v=bt3dqcbMLa0&t=2340s). KL defined, then maximum likelihood shown to be minimising KL. Chapter-timed, from the video lessons index.
- ritvikmath, The KL Divergence, 1:57 to 15:59: [watch](https://www.youtube.com/watch?v=q0AkK8aYbLY&t=117s). Why the formula has a ratio p over q, a log, and p out in front. Chapter-timed, from the video lessons index.

**Our plans and chapters**

- [Chapter 11: Compute KL, cross-entropy and conditional mutual information](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/11-kl-cross-entropy-and-cmi.md#111-kl-for-continuous-densities-worked-between-two-named-gaussians), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 11, section 11.1. KL as the extra nats per sample of the wrong code, worked between two named Gaussians.
- [What KL and mutual information measure](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/14-kl-and-mutual-information.md), the same journey, plan 14. Builds a KL checker in code, then derives KL from wasted bits to a closed form on paper.
- [Girsanov: the path KL is a control cost](/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/plans/02-girsanov-path-kl-is-a-control-cost.md), deep-learning/diffusion-models/04-schrodinger-bridges, plan 02. The KL between two diffusion processes over whole paths, read as a control cost and checked by Monte Carlo.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook range was read with pdftotext, after finding it through the books' back-of-book indexes and the shelf index's chapter tables. The Serrano, CS236 and ritvikmath rows are copied from the video lessons index, section "KL divergence". The two CME296 rows were read in their caption-read lecture map; the second fills the gap that index records, a KL between two Gaussians. Each plan and chapter was read at its title and the cited section. Serrano's "Why is KL Divergence not symmetric?" was cached (chapter "Numerical coin example", 4:58) and left out to keep the list to five. CME295 lecture 5 (53:52) and CS229 lecture 11 (1:06:48) also state KL, inside PPO and the diffusion loss, and were left out for the same reason.
