---
aliases: [entropy, Shannon entropy, information entropy, differential entropy, binary entropy, counting entropy]
link-skip: [free entropy, free-entropy, maximum entropy classifier]
standard: vault-note v2
---

# Entropy

Up: [[Information Theory]]

Mathematics, Statistics, Information Theory. [[Cross-Entropy]] is its own card and measures one distribution's code on another's data, and [[KL Divergence]] is the gap between the two.

**Entropy is the average surprise of a random variable, H = −Σ p(x) log p(x): zero when one outcome is certain, largest when every outcome is equally likely, and the fewest bits per draw any code can average.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches entropy writes the rest around it.

## Where to learn this

**Entropy**, the expected surprise −log p(x) of a draw, in bits or nats. Also: Shannon entropy, differential entropy, binary entropy.

**Textbooks**

- Pattern recognition and machine learning, section 1.6: [pages 67 to 73](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=67). Works the entropy of an eight-state variable, 3 bits when uniform and 2 bits for an uneven one, links it to the shortest average code length, then differential entropy and why the Gaussian maximises it.
- Probabilistic machine learning: an introduction, section 6.1: [pages 237 to 242](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=237). Entropy of discrete variables with the Bernoulli curve and DNA sequence logos, then joint and conditional entropy, perplexity and differential entropy.
- Deep learning textbook, section 3.13: [pages 89 to 90](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=89). Self-information I(x) = −log P(x) in nats and bits, then the Shannon entropy as its expectation.
- Natural language processing with Python, chapter 6, Entropy and information gain: [pages 265 to 266](../../references/textbooks/natural-language-processing/natural-language-processing-with-python.pdf#page=265). Entropy of the labels in a name-gender task, and information gain for choosing a decision stump's feature.

**Videos**

- StatQuest, Entropy (for data science), Entropy defined for a coin, 9:35 to 10:45: [watch](https://www.youtube.com/watch?v=YtebGVx-Fxw&t=575s). The entropy of a coin flip. Chapter-timed.
- StatQuest, Entropy (for data science), Entropy is the expected value of surprise, 10:45 to 11:41: [watch](https://www.youtube.com/watch?v=YtebGVx-Fxw&t=645s). Entropy as the average of the surprise −log p over outcomes. Chapter-timed.
- StatQuest, Entropy (for data science), The entropy equation, 11:41 to 13:01: [watch](https://www.youtube.com/watch?v=YtebGVx-Fxw&t=701s). The entropy equation written out. Chapter-timed.
- 3Blue1Brown, Reinventing Entropy, Defining Entropy, 24:29 to 31:14: [watch](https://www.youtube.com/watch?v=l6DKRf-fAAM&t=1469s). Defines entropy after building information from compression. Chapter-timed.
- Luis Serrano, Shannon Entropy and Information Gain, General Formula, 19:44 to 21:16: [watch](https://www.youtube.com/watch?v=9r7FIXEAGvs&t=1184s). The general entropy formula reached from the video's ball-picking games. Chapter-timed.

**Our plans and chapters**

- [Chapter 11: Compute KL, cross-entropy and conditional mutual information](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/11-kl-cross-entropy-and-cmi.md#112-cross-entropy-is-entropy-plus-kl), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 11, section 11.2. Cross-entropy split into entropy plus KL.
- [Stirling's approximation and counting entropy](/home/molef/goal-setting/learning/deep-learning/diffusion-models/06-diffusion-speciation-dynamics/plans/00-foundation/plans/04-stirling-and-counting-entropy.md), deep-learning/diffusion-models/06-diffusion-speciation-dynamics, plan 00.04. The entropy of spin configurations as the log of a count, derived with Stirling's approximation.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook range was read with pdftotext, after finding it through the books' back-of-book indexes. The StatQuest, 3Blue1Brown and Luis Serrano chapter lists were read with cache-video-chapters.py, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title and the cited section. Cross-entropy is not an alias, because [[Cross-Entropy]] has its own card; relative entropy belongs to [[KL Divergence]]. "Free entropy", a log partition function, is a link-skip phrase: in a sample of 25 learning-tree lines using "entropy", about 6 meant free entropy and the rest meant information or counting entropy. The plans named for free entropy were left out for the same reason.
