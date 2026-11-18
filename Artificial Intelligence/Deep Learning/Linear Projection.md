---
aliases: [linear projection, learned projection, projection layer, linear layer, text projection, image projection, visual projection]
standard: vault-note v2
---

# Linear Projection

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. In CLIP it follows [[Layer Normalization]] at the end of each tower, and [[Contrastive Image-Text Training]] compares what comes out. It is a different idea from [[Projection]], the shadow of a vector on a direction.

**A linear projection multiplies a vector by a learned matrix, so each output number is a weighted sum of the input numbers; CLIP uses one per tower to carry the picture's 768 numbers and the caption's 512 into one shared space of 512.**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the CLIP chapters need. The explanation beyond them is not written yet.

## What the chapters need

**The picture.**

<a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/miniature/m4-into-the-shared-space.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/miniature/m4-into-the-shared-space.png" width="200" alt="The two read-outs times W_t and the two summaries times W_i, divided by their lengths 5, 5, 5 and 10, landing as four unit vectors on a circle"></a> <a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv5-the-end-token-becomes-the-captions-point.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv5-the-end-token-becomes-the-captions-point.png" width="200" alt="The end token's attention bars over the seven tokens, then layer norm, projection, divide by length, the unit vector u"></a>

Left, the miniature: two caption read-outs times $W_t$ and two picture summaries times $W_i$ land in one 2-number space. Right, the real model: the end-of-text vector through layer norm, then the 512 × 512 projection, then division by its length.

**The idea.** A row of 768 numbers times a 768 × 512 matrix is a row of 512: each output number is the dot product of the input row with one column of the matrix. The matrix is learned in training like any other weight. CLIP's two towers end at different widths, 768 for pictures and 512 for captions, and the two projections $W_i$ and $W_t$ bring both to the same 512 so a picture and a caption can be compared *(cited: [the CLIP rebuild, rung 13](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/rebuild-clip-from-fundamentals.md#rung-13-a-linear-projection-is-one-matrix-product))*. The CLIP paper chose this plain product over a small nonlinear network *(cited: CLIP paper page 4)*.

**Words the name uses.** *Linear*: every output is a sum of the inputs times fixed weights, so doubling the input doubles the output and nothing bends; CLIP's projections add no bias either. *Projection*: from "throw forward". The vector is carried into another space, which may have a different width. The orthogonal [[Projection]] of linear algebra drops the part of a vector perpendicular to a direction; a learned projection has no such rule and can stretch, turn and mix the numbers.

**One number by hand, then from the real model.** In the miniature, the "cat" caption's read-out (1, 2) times $W_t=\begin{bmatrix}1 & 2\\ -2 & 1\end{bmatrix}$ gives (1·1 + 2·2, −2·1 + 1·2) = (5, 0), length 5 *(computed: the miniature's [answer key](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/substrate/clip_miniature_answer_key.json), entries `section3_projections` and `u_tilde`)*. In CLIP ViT-B/32, the end-of-text vector of "a cat and a dog" after layer norm times the 512 × 512 $W_t$ starts 0.2834, −0.1433, −0.5353 and has length 10.1063; the cat picture's summary times $W_i$ has length 11.2667 *(computed: journey 02's [CLIP numbers](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/clip_numbers.json), entries `eos_to_shared_space` and `summary_to_shared_space`)*.

## Where to learn this

**Linear Projection**, a learned matrix that carries a vector into another space. Also: learned projection, projection layer, linear layer, text projection, image projection.

**Textbooks**

- Probabilistic machine learning: advanced topics, section 16.2.1: [page 657](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=657). The linear layer f(x) = Wx + b as the most basic building block of a network, and why a stack of linear layers collapses to one matrix, which is what activation functions between them prevent.

**Videos**

- CS231n lecture 16, 25:59 to 31:30: [watch](https://www.youtube.com/watch?v=mQOK0Mfyrkk&t=1559s). LLaVA takes CLIP's per-patch features and maps them into the language model's input space with one trained linear layer. Caption-read.
- CME296 lecture 4, 1:12:12 to 1:17:51: [watch](https://www.youtube.com/watch?v=WUUq6TVAu8U&t=4332s). The vision transformer turns each image patch into a token with a learned projection, adds position embeddings, and reads the image off a CLS token. Caption-read.
- CS231n lecture 12, 1:06:12 to 1:11:20: [watch](https://www.youtube.com/watch?v=4howBU7THbM&t=3972s). SimCLR's nonlinear projection head g between the encoder and the contrastive loss, the choice the CLIP paper replaced with a linear projection. Caption-read.

**Papers**

- [CLIP paper, page 4](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/learning-transferable-visual-models-from-natural-language-supervision.pdf#page=4): "We instead use only a linear projection to map from each encoder's representation to the multi-modal embedding space", against the nonlinear projection of Bachman and others and Chen and others.
- [CLIP paper, page 5](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/learning-transferable-visual-models-from-natural-language-supervision.pdf#page=5): Figure 3's pseudocode, where the learned projections W_i and W_t carry each encoder's output into the shared space before the l2 normalisation.

**Our plans and chapters**

- [The CLIP rebuild, rung 13: a linear projection is one matrix product](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/rebuild-clip-from-fundamentals.md#rung-13-a-linear-projection-is-one-matrix-product), papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers, beside the CLIP paper. A row of 768 times the 768 × 512 $W_i$, each output a dot product with one column; length 11.2667 for the cat picture.
- [CLIP on one small network, 1.4: one shared space, project, then divide by length](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/textbook/01-clip-on-one-small-network.md#14-one-shared-space-project-then-divide-by-length), deep-learning/generative-models/02-stable-diffusion-and-clip, chapter 1. Both projections worked by hand on 2-number vectors, with the name taken apart word by word.
- [CLIP, read through a small network, section 4: a linear projection into one space, then unit length](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/clip-read-through-a-small-network.md#4-a-linear-projection-into-one-space-then-unit-length), papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers, beside the CLIP paper. One matrix per tower carries its vector into a shared space, then each is divided by its length.
- [Say what a projection computes, what it does, and what it means](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/23-say-what-a-projection-computes-what.md), deep-learning/transformers, chapter 23. The query, key and value matrices as learned projections of one word vector.
- [Multiply two matrices row by column](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/03-multiply-two-matrices-row-by-column.md), deep-learning/transformers, chapter 03. The row-by-column product every projection is made of.

**Scenes**

- [CLIP module tree, Text projection](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#text-projection). A linear layer, 512 in and 512 out, into the shared space.
- [CLIP module tree, Image projection](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#image-projection). A linear layer, 768 in and 512 out, into the shared space.
- [CLIP code walk, Output: the class position times W_i](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#image_head). The class position after layer norm times W_i, the picture's vector.
- [CLIP code walk, Output: the end-of-text position times W_t](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#text_head). The end-of-text position, found by text.argmax, after layer norm times W_t, the caption's vector.
- [Readout Guidance loop walk, The head: one bottleneck's layers, with its time projection](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#a_block_init). 1 × 1 down to 96 channels, 3 × 3, 1 × 1 up to 384, and a linear map from the time vector to the 96 inner channels.
- [Count head walk, Ours: pool each block to 32 × 32, project, sum, and read out a density](https://claude.ai/artifact/2VgqMaBHqrXNoHdTWjxro1#c_head). Each block pooled to 32 × 32 and projected to 128 channels, the three summed, one positive channel out.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/miniature/m4-into-the-shared-space.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/miniature/m4-into-the-shared-space.png" width="200" alt="The two read-outs times W_t and the two summaries times W_i landing as four unit vectors on a circle"></a> Journey 02's miniature, "Into the shared space": [what it shows](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/miniature/README.md). The caption read-outs times $W_t$ and the picture summaries times $W_i$, divided by their lengths 5, 5, 5 and 10.
- <a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv6-the-pictures-path.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv6-the-pictures-path.png" width="200" alt="The cat picture cut into a 7 by 7 grid, patches mapped to 768, 50 tokens, 12 blocks with no mask, the summary token projected to the unit vector v"></a> Journey 02's network view, "The picture's path": [what it shows](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/README.md). The summary token projected from 768 to 512 and divided by its length, 11.2667.
- <a href="/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/clip-by-hand-thumbnail.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/clip-by-hand-thumbnail.jpg" width="200" alt="A hand-worked sheet: three text-image pairs encoded on two sides, projected into a yellow shared embedding space, then softmax similarity matrices and cross-entropy gradients"></a> Prof. Tom Yeh on X, "CLIP by hand": [the post](https://x.com/ProfTomYeh/status/2094791189371261274), [what it shows](/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/README.md#clip-by-hand-thumbnailjpg). A linear layer projects 3-number text vectors and 4-number image vectors into one shared 2-number space, the same move as CLIP's 512 and 768 into 512. The sheet mean-pools each side before projecting, where CLIP reads one row ([End-of-Text Pooling](End-of-Text%20Pooling.md)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-17. The textbook page was read in the PDF with pdftotext, found through the back-of-book tables in `~/.claude/cache/book-indexes/` ("linear layer"). No shelf book's index has "linear projection". The three video rows were read in the caption-read lecture maps under `~/.claude/cache/captions/`. The two CLIP paper lines were read on pages 4 and 5. Each plan and chapter was read at its heading and opening lines. The worked numbers were read from the miniature's answer key and journey 02's `clip_numbers.json`. "projection" alone stays on the orthogonal [[Projection]] card, whose `link-skip` already sends "learned projection" and "projection layer" away from it; "linear layer" is an alias because the 5 sampled of its 18 uses in the learning tree all mean a weight matrix applied to a vector. A script then opened every link.
