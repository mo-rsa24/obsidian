---
aliases: [contrastive image-text training, contrastive language-image pretraining, CLIP model, CLIP, CLIP ViT-L/14, CLIP encoder]
standard: vault-note v2
---

# Contrastive Image-Text Training

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. Needs: [[Embedding]] for the arrows and [[Cosine Similarity]] for the angle. Used by [[CLIP Score]] and, for colour, by [[GenEval]].

**CLIP is trained on pairs of an image and its caption so that a picture and its caption land close together, which gives an image encoder and a text encoder that each turn their input into one arrow.**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the journey's chapters need. The Textbooks and Videos groups of the card are not built; waiting: `/concept-link build a card for Contrastive Image-Text Training`.
> - No claim is marked stated; the meaning of "contrastive" is listed as unknown.

## What the chapters need

**The idea.** CLIP is trained on image and text pairs so that a picture and its caption land close together *(cited: CLIP paper page 2, Figure 1)*. After training, the image encoder turns a picture into an arrow (a list of numbers) and the text encoder turns a sentence into another arrow, and the cosine between two arrows says how close the picture is to the sentence *(cited: journey chapter 1)*.

**Toy.** The picture of a mug and a wine glass and the prompt "a mug and a wine glass" each become an arrow. The two-object render's arrow sits close to the prompt's arrow and the cosine scaled by 100 is 26.7271, while the render with no mug gives 23.5954. *(shown: the journey's probe pair, see [[CLIP Score]])*

**Words the name uses.** The files read do not take "contrastive" apart, so what the training pushes apart is unknown here. The hand-worked CLIP sheet on the [[Embedding#Where to learn this|Embedding card]] shows the shared space and the training targets. "Image-text" is the pair of inputs and "training" is how the two encoders were made.

**Names of checkpoints in the journey.** `openai/clip-vit-large-patch14` scores CLIP score at the protocol's settings; ViT-B/32 is the smaller model of the earlier toy run; the GenEval paper's CLIPScore uses OpenCLIP ViT-H/14, a different model; GenEval's colour step uses CLIP ViT-L/14. See [[Vision Transformer]] for the letters.

**What it cannot do.** The paper lists counting as a weakness *(cited: page 19)*, and it does not evaluate generated images, so using its cosine as a score for a render is a later use *(cited: journey paper reading)*.

## Where to learn this

**Contrastive Image-Text Training**, a model trained on image and caption pairs. Also: contrastive language-image pretraining, CLIP model, CLIP, CLIP ViT-L/14, CLIP encoder.

**Papers**

- [CLIP paper, page 2](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/learning-transferable-visual-models-from-natural-language-supervision.pdf#page=2): Figure 1, the image and caption pairs landing close together.
- [CLIP paper, pages 18 and 19](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/learning-transferable-visual-models-from-natural-language-supervision.pdf#page=18): the stated limits, competitive with a supervised baseline on average, poor on fine-grained classes, struggles with counting.

**Our plans and chapters**

- [Journey chapter 1, how the number is made](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/01-clip-score.md#how-the-number-is-made): the two encoders, the cosine and the checkpoint.
- [Journey paper reading, CLIP](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/sources/paper-readings/clip.md): what the paper says about its own limits and the toy run against them.
- [The CLIP rebuild, rung 22: a batch of pairs is N classification questions with known answers](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/rebuild-clip-from-fundamentals.md#rung-22-a-batch-of-pairs-is-n-classification-questions-with-known-answers), papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers, beside the CLIP paper. Picture i was paired with caption i, so each question's answer is i and the other captions in the batch are the wrong answers; the rig's labels are 0, 1, 2, 3.
- [CLIP, read through a small network, section 6: a symmetric cross-entropy over the table](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/clip-read-through-a-small-network.md#6-a-symmetric-cross-entropy-over-the-table), papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers, beside the CLIP paper. Each picture is asked which caption is its own, each caption which picture is its own, and the loss is the mean of the two answers' surprise.

**Scenes**

- [CLIP module tree, Loss](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#loss). The symmetric loss on the 4 × 4 batch: image-to-caption and caption-to-image averaged.
- [CLIP code walk, Contrastive: the right answer for row i is column i](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6). The labels 0 to N − 1, each picture's right caption on the diagonal.
- [CLIP code walk, Contrastive: the symmetric cross-entropy](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6). Open_clip's ClipLoss: cross-entropy over captions and over pictures, averaged, 0.1698 on the rig.
