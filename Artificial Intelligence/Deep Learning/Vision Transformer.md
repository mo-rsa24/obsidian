---
aliases: [vision transformer, ViT, ViT-L/14, ViT-B/32, ViT-H/14, clip-vit-large-patch14]
standard: vault-note v2
---

# Vision Transformer

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. Needs: [[Transformer]]. Used inside the CLIP models of [[Contrastive Image-Text Training]] and in the BLIP image encoder of [[ImageReward]].

**A vision transformer, ViT, is a transformer used as an image encoder: it reads a picture and returns arrows (stated, the standard definition; no file the journey read defines it).**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the journey's chapters need. The Textbooks and Videos groups of the card are not built; waiting: `/concept-link build a card for Vision Transformer`.
> - 2 claims are marked stated (the plain definition and the letters B and H) and keep nothing unfinished. No paper on ViT is on the journey's shelf.

## What the chapters need

**Where it appears.** The journey names a ViT in five places: the checkpoint `openai/clip-vit-large-patch14` that makes the CLIP score, the smaller ViT-B/32 of the earlier toy run, OpenCLIP ViT-H/14 in the GenEval paper's CLIPScore, CLIP ViT-L/14 reading colour in [[GenEval]], and the ViT-L image encoder inside the BLIP backbone of ImageReward *(cited: the journey's facts table, sections 1, 2 and 4)*.

**Reading the letters.** The same model is written two ways in the journey: the checkpoint `clip-vit-large-patch14` and "CLIP ViT-L/14", so L stands for large and 14 for patch14 *(shown: chapters 1 and 4)*. B and H in ViT-B/32 and ViT-H/14 are the same kind of size letter, base and huge *(stated: the files do not expand them)*.

**What is unknown here.** How a ViT cuts a picture into patches and what a patch is are not taught in the files the journey read. No paper on the shelf was read for it.

## Where to learn this

**Vision Transformer**, a transformer that reads images. Also: ViT, ViT-L/14, ViT-B/32, ViT-H/14, clip-vit-large-patch14.

**Our plans and chapters**

- [Journey chapter 1, what goes in](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/01-clip-score.md#what-goes-in-and-how-to-read-the-number): the CLIP checkpoint, with the input size marked unknown.
- [The facts table, section 2](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/sources/metric-answer-sheets/facts.md): the BLIP backbone with a ViT-L image encoder.
- [The CLIP rebuild, rung 11: a stride-32, size-32 convolution is one matrix product per patch](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/rebuild-clip-from-fundamentals.md#rung-11-a-stride-32-size-32-convolution-is-one-matrix-product-per-patch), papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers, beside the CLIP paper. Flattening each 32 × 32 tile and multiplying by the 768 filters matches conv1's output on patch 0 of the cat picture to 4.3 × 10⁻⁶.
- [CLIP, read through a small network, section 3: a picture becomes a vector through patches and a summary token](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/clip-read-through-a-small-network.md#3-a-picture-becomes-a-vector-through-patches-and-a-summary-token), papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers, beside the CLIP paper. The picture is cut into patches, each patch becomes a short vector, and a summary token that reads every patch is read out as the picture's vector.

**Scenes**

- [CLIP module tree, Image patches](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#image-patches). A stride-32 convolution cutting the 224-pixel picture into 7 × 7 patches, plus one class token, 50 tokens.
- [CLIP module tree, Image encoder](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#image-encoder). Twelve pre-norm transformer blocks with no mask, 12 heads × 64 = 768.
- [CLIP module tree, Image pool](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#image-pool). Token 0 taken, then layer norm, 768 out.
- [CLIP code walk, Image path: conv1 cuts the picture into patches](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#patch). Conv1 cutting the picture into 49 patches of 32 × 32.
- [CLIP code walk, Image path: a class row in front, a position row added](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#cls_pos). The class row put in front of the patches and a position row added to each.
