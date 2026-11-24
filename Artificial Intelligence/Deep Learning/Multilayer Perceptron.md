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

**Scenes**

- [SDXL pipeline map, Add embedding](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#add-embedding). P and the size numbers' waves mapped to 1280 and added to the time vector.
- [SDXL pipeline map, Time embedding](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#time-embedding). The step number as cosine and sine waves, then two linear layers with SiLU to the 1280 time vector.
- [SDXL code walk, The caption acts: p and the size numbers become a second time vector](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#aug_embed). Six size numbers as 256 waves each, joined to p into 2816 and mapped to 1280.
- [SDXL code walk, Hidden: the time vector e_t is the two added](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#emb_sum). The 320 waves mapped to 1280 plus the caption-and-size vector, read by all 17 ResBlocks.
- [SDXL code walk, Hidden: two linear layers with SiLU between](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#timestep_mlp). The one TimestepEmbedding class used for time_embedding (320 → 1280) and add_embedding (2816 → 1280).
- [Readout Guidance loop walk, The head's time input: the U-Net's own time vector](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#h_time). The U-Net's sinusoid and two-layer embedding giving the head a 1280-number time vector, from different step numbers in training and at guidance.
- [Digit-map checkers by hand, The real system, stage by stage](https://claude.ai/artifact/MX2hKBUWBXSzPQSbaxysKC#real-system). One real canvas through the saved checker's twelve stages, and its readout MLP as 272 inputs, the 12 hidden units with the largest output-weight-times-activation, and the sum that gives the logit.
- [Digit-map checkers by hand, One logit, one chance](https://claude.ai/artifact/MX2hKBUWBXSzPQSbaxysKC#logit). The readout turning pooled numbers and time features into a logit and its sigmoid chance.
