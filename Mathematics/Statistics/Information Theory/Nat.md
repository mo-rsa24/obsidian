---
aliases: [nat, nats, natural unit of information]
link-skip: [NAT gateway, NAT table, NAT translation table, NAT router, NAT rule, network address translation, SNAT, DNAT]
standard: vault-note v2
---

# Nat

Up: [[Information Theory]]

Mathematics, Statistics, Information Theory. [[Entropy]] and [[KL Divergence]] are each counted in bits or nats, and this note is the nat.

**A nat is the unit of information you get by counting with the natural log (base e), the way a bit is counted with the log base 2: an outcome of probability 1/e carries 1 nat, and 1 nat is 1.4427 bits.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the nat writes the rest around it.

## Where to learn this

**Nat**, the natural unit of information: a bit is one yes-or-no answer counted with the log base 2, and a nat is the same count made with the natural log, base e. Also: nat, nats, natural unit of information.

**Textbooks**

- Probabilistic machine learning: advanced topics, section 5.1.3.1: [page 255](../../references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=255). Names the nat as the "natural unit", gives 1 bit = 0.693 nats and 1 nat = 1.44 bits, then works a KL between two Bernoulli distributions as 0.692 nats (about 1 bit) one way and 1.38 nats (about 2 bits) the other.
- Deep learning textbook, section 3.13: [page 89](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=89). Defines the self-information −log P(x) in nats, says one nat is the information gained by seeing an event of probability 1/e, and says bits are a rescaling of nats.
- Pattern recognition and machine learning, section 1.6: [page 69](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=69). Switches entropy from base 2 to natural logs and says the two units differ by a factor of ln 2.
- AI engineering, chapter 3, Perplexity: [page 247](../../references/textbooks/ai-engineering/ai-engineering.pdf#page=247). Says TensorFlow and PyTorch report entropy and cross entropy in nats, so perplexity becomes e raised to the cross entropy instead of 2 raised to it.

**Our plans and chapters**

- [Chapter 2: Read a density as area and draw a Gaussian from its covariance](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/02-densities-and-the-gaussian.md#why-this-matters), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 2, "A nat, taken apart". Takes the unit apart on a fair coin (−ln 0.5 = 0.6931 nats = 1 bit, so 1 nat = 1.4427 bits) and converts a Gaussian normaliser's 60,223.56 nats to 86,884.2 bits.
- [Chapter 11: Compute KL, cross-entropy and conditional mutual information](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/11-kl-cross-entropy-and-cmi.md#111-kl-for-continuous-densities-worked-between-two-named-gaussians), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 11, section 11.1. KL between two named Gaussians worked by hand in nats: 0.4431 one way and 1.3069 the other.
- [Chapter 11: Compute KL, cross-entropy and conditional mutual information](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/11-kl-cross-entropy-and-cmi.md#114-cmi-from-a-table-in-bits-and-in-nats), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 11, section 11.4. Computes one conditional mutual information in bits, then converts it by multiplying by log 2.

**Scenes**

- [The wasted-bits walk, The wrong code costs extra](https://claude.ai/code/artifact/7aff7fa0-ee51-411d-8d97-a7233baa8519). Frame 1: the stacked bar H(p) plus the KL waste, with a switch from bits (1.5, 0.25 and 1.75) to nats (1.039721, 0.173287 and 1.213008).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-10. Each textbook page was read with pdftotext after the gather script and the shelf's worked-example catalogue named it, and the unit sentence quoted in each line is printed on that page. The two chapter 11 sections and the chapter 2 paragraph were read at their headings. No Videos group: the lecture maps, the video lessons index and the cached chapter lists hold no segment that teaches the nat, since the entropy videos on the shelf count in bits. No Papers group: the one shelf paper the gather script returned mentions nats only in its Papers.md summary, and the paper's own text has no passage on the unit. The card's words are lower-case nat and nats; the capitals NAT belong to [[Network Address Translation]], and lines naming a NAT gateway, table, router or rule stay plain through the link-skip list.
