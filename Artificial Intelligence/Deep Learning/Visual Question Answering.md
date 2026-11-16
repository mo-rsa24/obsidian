---
aliases: [visual question answering, VQA, VQA model, question-answering model]
standard: vault-note v2
---

# Visual Question Answering

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. Used by [[BLIP-VQA]]. The questions are cut from the prompt with [[Noun Phrase]] parsing.

**Visual question answering, VQA, is a model that is given an image and a question in words and answers it; BLIP-VQA keeps the chance that the answer is yes.**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the journey's chapters need. The Textbooks and Videos groups of the card are not built; waiting: `/concept-link build a card for Visual Question Answering`.
> - No claim is marked stated.

## What the chapters need

**Visual, question, answering.** Visual means the input is a picture, a question is a short sentence about it, and answering means the model returns an answer. BLIP-VQA does not use the word answer: it uses the model's chance of saying yes *(cited: T2I-CompBench++ page 6)*.

**Toy.** For "a cat and a dog" the questions are "a cat?" and "a dog?". On a clear pair the chances of yes are 0.9566 and 0.6428, and on a fused animal 0.0332 and 0.4207. *(shown: journey chapter 3)*

**The model used.** BLIP base VQA, `model_base_vqa_capfilt_large`, at 480 pixels *(cited: protocol)*. The paper asks one object and attribute pair per question so the model is not confused by a long prompt.

**What it misses.** The model answers whether a thing is there, so a fused animal still answers 0.4207 on "a dog?". CO3 notes it can be unreliable on rare concepts.

## Where to learn this

**Visual Question Answering**, a model that answers a question about a picture. Also: VQA, VQA model, question-answering model.

**Papers**

- [T2I-CompBench++ paper, page 6](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/benchmarks/t2i-compbench-benchmark-for-compositional-text-to-image-generation.pdf#page=6): Figure 3, the question for each noun phrase and the product of the chances of yes.

**Our plans and chapters**

- [Journey chapter 3, how the number is made](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/03-blip-vqa.md#how-the-number-is-made): the questions, the chances and the product.
