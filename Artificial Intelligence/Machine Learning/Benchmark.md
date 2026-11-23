---
aliases: [benchmark, benchmarks, benchmark prompt set]
link-only-in: [deep-learning/diffusion-models]
standard: vault-note v2
---

# Benchmark

Up: [[Machine Learning]]

Artificial Intelligence, Machine Learning. Used by [[T2I-CompBench]] and [[GenEval]].

**A benchmark is a fixed set of inputs together with the scorer that judges each, so that different methods are measured on the same thing (stated, the general definition; the two examples below are cited).**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the journey's chapters need. The Textbooks and Videos groups of the card are not built; waiting: `/concept-link build a card for Benchmark`.
> - 1 claim is marked stated (the general definition) and keeps nothing unfinished.

## What the chapters need

**T2I-CompBench++.** Eight sub-categories of 1,000 prompts each, 700 for training and 300 for testing, with a scorer chosen per sub-category *(cited: paper page 3)*.

**GenEval.** Six tasks and 553 prompts: single object 80, two object 99, counting 80, colors 94, position 100 and attribute binding 100 *(cited: paper Table 1, page 5)*.

**Our benchmark.** The animals set has 66 prompts, each rendered at 4 seeds, so each method has 264 images *(cited: journey chapter 5)*. The scorers give no threshold for good, so a benchmark number is read against a reference render for the same prompts.

**What it misses.** The same reference scores 27.0 to 31.1 on CLIP score and 0.48 to 0.88 on BLIP-VQA depending on the prompt set, so a number quoted without its prompt set means little.

## Where to learn this

**Benchmark**, a fixed set of prompts or inputs and the scorer for each. Also: benchmarks, benchmark prompt set.

**Papers**

- [T2I-CompBench++ paper, page 3](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/benchmarks/t2i-compbench-benchmark-for-compositional-text-to-image-generation.pdf#page=3): the eight sub-categories and the prompt split.
- [GenEval paper, page 5](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/benchmarks/geneval-object-focused-framework-for-evaluating-text-to-image-alignment.pdf#page=5): Table 1, the six tasks and 553 prompts.

**Our plans and chapters**

- [Journey chapter 5, from a score to a table cell](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/05-the-four-side-by-side.md#from-a-score-to-a-table-cell): the prompt set, the images and the cell.

**Scenes**

- [Outside Planners and Critics, Fix everything except the guidance rule](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p13). Holding the rest constant within each model so only the guidance rule and its settings change.
