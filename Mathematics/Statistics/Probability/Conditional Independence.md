---
aliases: [conditional independence, conditionally independent, conditional independence assumption]
standard: vault-note v2
---

# Conditional Independence

Up: [[Probability]]

Mathematics, Statistics, Probability. It is [[Statistical Independence]] inside each slice of a third variable, and [[What An Expert Learns From Its Training Set]] leans on it for labels.

**Two variables are conditionally independent given a third when, once the third is known, learning one tells you nothing more about the other: p(x, y | z) = p(x | z) p(y | z) for every z.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches conditional independence writes the rest around it.

## Where to learn this

**Conditional independence**, independence that holds once a third variable is fixed. Also: conditionally independent, conditional independence assumption.

**Textbooks**

- Computer vision textbook, section 10.1: [pages 219 to 221](../../references/textbooks/computer-vision/computer-vision-textbook.pdf#page=219). Works it on a joint table of three discrete variables taking 4, 3 and 2 values, 24 probabilities in all, where x₁ and x₃ are dependent yet conditionally independent given x₂ (Figure 10.1, page 220).
- Mathematics for machine learning, section 6.4.5: [page 201](../../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=201). Definition 6.11, p(x, y | z) = p(x | z) p(y | z) for every z, read as "given knowledge about z, the distribution of x and y factorizes".
- Pattern recognition and machine learning, section 8.2: [pages 389 to 393](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=389). The definition p(a | b, c) = p(a | c), then three-node graphs where observing c makes a and b independent, and the head-to-head case where observing c makes them dependent.
- Deep learning textbook, section 3.7: [page 76](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=76). Conditional independence given z beside plain independence, with the notation x ⊥ y | z.

**Videos**

- CS229 lecture 5, 1:16:27 to 1:20:34: [watch](https://www.youtube.com/watch?v=zRdE8A4UZes&t=4587s). Makes the naive Bayes assumption that words are conditionally independent given the class, cutting the parameters from 2^d to 2d + 1. Caption-read.

**Our plans and chapters**

- [Check independence inside each slice of a third variable](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/04-conditional-independence.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 04. Conditional independence checked on the fuel gauge's table, sliced at G = 0.
- [Chapter 1: Compute conditionals and independence from a joint table](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/01-joint-tables-and-independence.md), deep-learning/diffusion-models/01-poe-derivation-foundations, chapter 01. Section 1.4 builds a conditionally independent table, and section 1.6 shows shared pixels breaking it.
- [Read every independence off a graph with d-separation](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/16-d-separation.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 16. Every conditional independence of a five-node Gaussian graph read off its arrows.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext; the computer vision, Mathematics for machine learning and Pattern recognition pages were first found through their back-of-book indexes. The CS229 row was read in its caption-read lecture map under `~/.claude/cache/captions/` and paraphrases the map. Each plan and chapter was read at its title and opening lines. No StatQuest, Professor Leonard or ritvikmath video in the cached upload lists covers conditional independence, so the videos hold one line. The composition note's alias "conditional independence of labels" is longer and stays with that note.
