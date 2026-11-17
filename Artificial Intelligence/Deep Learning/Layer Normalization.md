---
aliases: [layer normalization, layer normalisation, layer norm, LayerNorm]
standard: vault-note v2
---

# Layer Normalization

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. It sits twice inside every [[Transformer]] block, and in CLIP it runs once more on the end-of-text vector just before the [[Linear Projection]].

**Layer normalization takes one position's vector, subtracts the mean of its own numbers, divides by their spread, then rescales each number with a learned scale and shift, so the next layer always sees numbers on the same scale.**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the CLIP chapters need. The explanation beyond them is not written yet.

## What the chapters need

**The picture.**

<a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv3-inside-one-text-block.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv3-inside-one-text-block.png" width="200" alt="Layer norm, attention, add, layer norm, MLP, add; below, the 7 by 7 causal mask with the end token's real weights in the bottom row"></a> <a href="/home/molef/goal-setting/learning/deep-learning/transformers/diagrams/transformers-17-layer-norm.svg"><img src="/home/molef/goal-setting/learning/deep-learning/transformers/diagrams/transformers-17-layer-norm.svg" width="200" alt="A vector's activations before and after layer normalisation"></a>

Left, one of CLIP's 12 text blocks: a layer norm box sits before the attention and another before the MLP. Right, the transformers journey's drawing of a vector's numbers before and after normalising.

**The idea.** Layer norm treats the 512 numbers of one position as a small data set. It takes their mean μ and their spread σ, maps each number $h_d$ to $(h_d-\mu)/\sqrt{\sigma^2+\epsilon}$, then multiplies by a learned $\gamma_d$ and adds a learned $\beta_d$. Nothing is shared across positions or across the batch, so every position of every caption is normalised on its own. CLIP uses it five ways: before the attention and before the MLP in every block, after the text transformer, and before and after the vision transformer *(cited: [the CLIP rebuild, section 1](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/rebuild-clip-from-fundamentals.md#1-hidden-layernorm))*.

**Words the name uses.** *Layer*: the mean and spread come from one layer's numbers for one position, taken across its features. Batch normalization takes them across the examples in a batch instead, which is the difference the name marks. *Normalization*: shifting and scaling numbers to a standard form, here mean 0 and spread 1, before the learned γ and β move them again.

**One number from the real model.** The caption "a cat and a dog" reaches CLIP's final layer norm with its end-of-text vector at mean 0.0029 and spread 0.4635, its 512 values running from −2.8633 to 2.7615. After the subtract and divide they have mean 0 and spread 1.0. After γ (mean 0.9827) and β (mean 0.1125) they have mean 0.1217 and spread 1.0816. *(computed: the code walk's [rig.json](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/code-walk/what-each-line-of-clip-computes/pictures/rig.json), entry `layer_norm_eot`)*

## Where to learn this

**Layer Normalization**, one vector rescaled to mean 0 and spread 1 by its own numbers, then moved by a learned scale and shift. Also: layer normalisation, layer norm, LayerNorm.

**Textbooks**

- Understanding deep learning, chapter 11 notes: [pages 217 to 218](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=217). Sets LayerNorm beside BatchNorm, GroupNorm and InstanceNorm: it computes the statistics for each batch member separately, and Figure 11.14 on page 218 draws which numbers each scheme averages over.
- Probabilistic machine learning: an introduction, section 14.2.4: [page 522](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=522). Batch, layer, instance and group norm drawn side by side (Figure 14.14), with layer normalization as one set of statistics per example across its channels.
- Understanding deep learning, section 12.4: [page 230](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=230). The transformer layer as two residual blocks, each followed by LayerNorm (equation 12.13). CLIP puts the layer norm before each block's branch instead.

**Videos**

- CS229 lecture 7, 1:11:47 to 1:18:58: [watch](https://www.youtube.com/watch?v=fRM41w9jzQo&t=4307s). Defines layer normalization (subtract the mean, divide by the standard deviation, then β + γ times the result) and RMS normalization, and shows LN(αz) = LN(z), which keeps activations from exploding. Caption-read.
- CME295 lecture 2, 43:43 to 50:19: [watch](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2623s). Layer normalization in the add-and-norm blocks with its learned γ and β, the move from post-norm to pre-norm, and RMSNorm, which keeps only γ. Caption-read.
- CS224N 2023 lecture 8, 1:00:58 to 1:03:49: [watch](https://www.youtube.com/watch?v=LWMzyfvuehA&t=3658s). The mean and standard deviation taken across one word vector's own dimensions, then the learned gain and bias, in symbols only. From the video lessons index.
- Vizuara, LLMs from scratch lecture 20, 26:01 to 36:55: [watch](https://www.youtube.com/watch?v=G3W-LT79LSI&t=1561s). A LayerNorm class written in code with its mean, variance, epsilon, scale and shift, then tested. From the video lessons index.

**Papers**

- [CLIP paper, page 5](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/learning-transferable-visual-models-from-natural-language-supervision.pdf#page=5): the [EOS] activation "is layer normalized and then linearly projected", and the vision transformer gets an extra layer normalization on the combined patch and position embeddings.

**Our plans and chapters**

- [Normalise a vector by hand with layer norm](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/40-normalise-a-vector-by-hand-with-layer.md), deep-learning/transformers, chapter 40. Layer normalisation worked on [1, 2, 3, 4] by hand, then checked in code.
- [The CLIP rebuild, rung 1: the mean and the spread of one vector's own numbers](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/rebuild-clip-from-fundamentals.md#rung-1-the-mean-and-the-spread-of-one-vectors-own-numbers), papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers, beside the CLIP paper. μ = 0.0029 and σ = 0.4635 on the end-of-text vector going into CLIP's final layer norm.
- [The CLIP rebuild, rung 2: subtract the mean, divide by the spread, then rescale with learned numbers](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/rebuild-clip-from-fundamentals.md#rung-2-subtract-the-mean-divide-by-the-spread-then-rescale-with-learned-numbers), the same file. The subtract and divide give mean 0 and spread a hair under 1, then γ and β move the output to mean 0.1217 and spread 1.0816.
- [Keep activations at a stable scale through three layers](/home/molef/goal-setting/learning/deep-learning/transformers/plans/41-keep-activations-at-a-stable-scale-through.md), deep-learning/transformers, plan 41. The same operation built in code after each of three scaling layers and compared with the stack without it.

**Scenes**

- [CLIP code walk, Hidden: LayerNorm](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#ln). Layer norm run in float32, before the attention and before the MLP in every block, after the text transformer, and before and after the vision transformer.
- [CLIP code walk, Output: the class position times W_i](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#image_head). The class position after layer norm times W_i, the picture's vector.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv3-inside-one-text-block.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv3-inside-one-text-block.png" width="200" alt="Layer norm, attention, add, layer norm, MLP, add; below, the 7 by 7 causal mask"></a> Journey 02's network view, "Inside one text block": [what it shows](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/README.md). One of CLIP's 12 text blocks as attention then an MLP, each behind its own layer norm and wrapped in a residual add.
- <a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv5-the-end-token-becomes-the-captions-point.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv5-the-end-token-becomes-the-captions-point.png" width="200" alt="The end token's attention bars over the seven tokens, then layer norm, projection, divide by length, the unit vector u"></a> Journey 02's network view, "The end token becomes the caption's point": [what it shows](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/README.md). The end-of-text vector's first values before and after the final layer norm, then through the projection.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-17. Each textbook page was read in the PDF with pdftotext, first found through the back-of-book tables in `~/.claude/cache/book-indexes/` ("layer normalization", "LayerNorm"). Hands-on large language models (PDF page 152) only names RMSNorm in passing and has no line. The CS229 and CME295 rows were read in the caption-read lecture maps under `~/.claude/cache/captions/`; the CS224N and Vizuara rows are copied from the video lessons index, `Mathematics/references/videos/Video Lessons.md`, sections "Layer normalisation" and "Layer normalisation in code". CS231n lecture 6 at 3:37 also defines it and was left out to keep four videos. The CLIP paper sentence was read on page 5. Each plan and chapter was read at its heading and opening lines, and the worked number was read from `rig.json`, which matches journey 02's `clip_numbers.json` at every stored digit. "layer norm" sits in the Norm card's `link-skip`, so those lines link here and not to Norm. A script then opened every link.
