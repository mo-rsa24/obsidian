---
aliases: [zero-shot, zero shot, zero-shot classifier, zero-shot classification]
standard: vault-note v2
---

# Zero-Shot

Up: [[Machine Learning]]

Artificial Intelligence, Machine Learning. Needs: [[Classifier]]. Used by [[Contrastive Image-Text Training]] and [[GenEval]].

**Zero-shot means using a trained model on a task with no training on that task (stated, the general definition); CLIP is evaluated as a zero-shot classifier.**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the journey's chapters need. The Textbooks and Videos groups of the card are not built; waiting: `/concept-link build a card for Zero-Shot`.
> - 1 claim is marked stated (the general definition) and keeps nothing unfinished.

## What the chapters need

**In the CLIP paper.** CLIP is evaluated as a zero-shot classifier. On datasets with training splits, zero-shot CLIP is on average competitive with a simple supervised baseline *(cited: CLIP paper page 18)*. It is poor on fine-grained classification and can be near random on tasks unlikely to be in its pre-training data *(cited: pages 18 and 19)*.

**In GenEval.** The colour of each detected object is classified zero-shot by CLIP ViT-L/14 *(cited: GenEval paper page 5; facts table, section 4)*. Holes in an object get included in its mask and mislead this step *(cited: page 7)*.

**What is unknown here.** How the zero-shot classification is run, for example which sentences stand for the colours, is not in the files read.

## Where to learn this

**Zero-Shot**, a trained model used on a task it was not trained on. Also: zero shot, zero-shot classifier, zero-shot classification.

**Papers**

- [CLIP paper, pages 18 and 19](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/learning-transferable-visual-models-from-natural-language-supervision.pdf#page=18): the zero-shot results and limits.
- [GenEval paper, page 5](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/benchmarks/geneval-object-focused-framework-for-evaluating-text-to-image-alignment.pdf#page=5): the colour step.

**Our plans and chapters**

- [Journey paper reading, CLIP](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/sources/paper-readings/clip.md): the limits in plain words.
- [Journey chapter 4, how a pass is decided](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/04-geneval.md#how-a-pass-is-decided): the colour step.
