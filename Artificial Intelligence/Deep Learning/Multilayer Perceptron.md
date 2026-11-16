---
aliases: [multilayer perceptron, multi-layer perceptron, MLP]
standard: vault-note v2
---

# Multilayer Perceptron

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. Needs: [[Embedding]] for the vector it reads. Used by [[ImageReward]] and inside every [[Transformer]] block.

**A multilayer perceptron, MLP, is a small network of layers that turns a vector of numbers into another vector of numbers; in ImageReward it turns the image-and-prompt features into one number (stated for the general definition).**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the journey's chapters need. The Textbooks and Videos groups of the card are not built; waiting: `/concept-link build a card for Multilayer Perceptron`.
> - 1 claim is marked stated (the general definition) and keeps nothing unfinished.

## What the chapters need

**In ImageReward.** The image goes through BLIP's image encoder, the image features read the prompt's words by [[Cross-Attention]], and a small network, an MLP, turns the result into one number *(cited: ImageReward paper pages 4 and 7; journey chapter 2)*.

**Elsewhere in the vault.** The [[Transformer]] card lists a per-token MLP inside every block.

**What is unknown here.** The size of ImageReward's MLP and how many layers it has are not in the files the journey read.

## Where to learn this

**Multilayer Perceptron**, a small stack of layers on a vector. Also: multi-layer perceptron, MLP.

**Papers**

- [ImageReward paper, page 4](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/imagereward-human-preferences-for-text-to-image-generation.pdf#page=4): the BLIP backbone with cross attention and an MLP.
- [ImageReward paper, page 7](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/imagereward-human-preferences-for-text-to-image-generation.pdf#page=7): the model details the chapter cites.

**Our plans and chapters**

- [Journey chapter 2, how the number is made](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/02-imagereward.md#how-the-number-is-made): the MLP at the end of the picture.
