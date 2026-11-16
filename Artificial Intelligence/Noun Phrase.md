---
aliases: [noun phrase, noun phrases, spaCy parsing, spaCy noun phrases, spaCy]
standard: vault-note v2
---

# Noun Phrase

Up: [[Artificial Intelligence]]

Artificial Intelligence. Used by [[BLIP-VQA]] to turn a prompt into questions. The placement is unsure, see the unfinished box.

**A noun phrase is a noun with the words that go with it, such as "a red flower" (stated, the grammar term); the journey uses spaCy to cut a prompt into noun phrases.**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the journey's chapters need. The Textbooks and Videos groups of the card are not built; waiting: `/concept-link build a card for Noun Phrase`.
> - 1 claim is marked stated (the grammar term) and keep nothing unfinished. The placement is unsure: filed at the top of Artificial Intelligence; the best two places are Artificial Intelligence, Large Language Models, beside Tokenization, or a Natural Language Processing family when it has a second note.

## What the chapters need

**What spaCy does here.** A language tool, spaCy, cuts the prompt into noun phrases and each phrase becomes a question: "a cat and a dog" gives "a cat?" and "a dog?" *(cited: journey chapter 3)*. The model is spaCy's `en_core_web_sm`, with the T2I-CompBench code at commit `4aa4042` unchanged *(cited: protocol)*.

**With an attribute.** In the colour and shape sets the question carries the attribute: "a red flower?" from "a red flower and a yellow vase" *(cited: journey chapter 3)*.

**A parser in another method.** SynGen uses a parser that finds each noun and the words that modify it, and it is tied to that parser: when the parser fails to find the relations it behaves like plain Stable Diffusion *(cited: SynGen paper page 10)*. On a two-noun prompt that limit never came into play.

**What is unknown here.** How spaCy decides where a phrase ends is not in the files read.

## Where to learn this

**Noun Phrase**, a noun with its modifiers. Also: noun phrases, spaCy parsing, spaCy noun phrases, spaCy.

**Papers**

- [SynGen paper, page 10](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/region-and-binding-failures/linguistic-binding-in-diffusion-models.pdf#page=10): the parser tie and its limits.
- [T2I-CompBench++ paper, page 6](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/benchmarks/t2i-compbench-benchmark-for-compositional-text-to-image-generation.pdf#page=6): one object and attribute pair per question.

**Our plans and chapters**

- [Journey chapter 3, how the number is made](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/03-blip-vqa.md#how-the-number-is-made): the prompt cut into noun phrases.
- [Journey paper reading, SynGen](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/sources/paper-readings/syngen.md): the parser limit against our runs.
