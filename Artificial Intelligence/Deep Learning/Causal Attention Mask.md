---
aliases: [causal attention mask, causal mask, causal masking, masked self-attention, causal self-attention]
standard: vault-note v2
---

# Causal Attention Mask

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. It is added to the scores inside [[Attention]] before the [[Softmax]], and it is the reason CLIP reads a caption out at its end token ([[End-of-Text Pooling]]).

**A causal attention mask adds 0 to the attention scores a position may use and −∞ to the scores of every later position, so after the softmax each position takes weight only from itself and the positions before it.**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the CLIP chapters need. The explanation beyond them is not written yet.

## What the chapters need

**The picture.**

<a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv4-the-cat-vector-cannot-see-dog.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv4-the-cat-vector-cannot-see-dog.png" width="200" alt="The tokens of a cat above and a cat and a dog below; the cat outputs match exactly and the end outputs differ"></a> <a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv3-inside-one-text-block.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv3-inside-one-text-block.png" width="200" alt="Layer norm, attention, add, layer norm, MLP, add; below, the 7 by 7 causal mask with the end token's real weights in the bottom row"></a>

Left, "a cat" and "a cat and a dog" run side by side: the "cat" slot comes out identical in both, because its mask row is closed on everything after it. Right, the real 7 × 7 mask for "a cat and a dog", grey where a token may not read.

**The idea.**

$$M_{ab} = \begin{cases}0 & b\le a\\ -\infty & b > a\end{cases}\qquad\mathrm{Attn}(Q,K,V) = \mathrm{softmax}\!\Big(\frac{QK^{T}}{\sqrt d} + M\Big)V$$

Row a of the score table belongs to position a and column b to the position it reads. Adding −∞ to a score makes its exponential exactly 0, so a blocked position gets exactly 0 weight and the open ones share the whole weight among themselves *(cited: [the CLIP rebuild, rung 7](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/rebuild-clip-from-fundamentals.md#rung-7-adding--before-the-softmax-makes-a-weight-exactly-0))*. In CLIP only the text tower has the mask; every image patch reads every other patch. The paper kept it so the text encoder could be started from a pre-trained language model *(cited: CLIP paper page 5)*.

**Words the name uses.** *Causal*: a cause comes before its effect, so position k may be shaped only by positions 0 to k. *Attention*: the mask works inside attention, on the table of query-key scores. *Mask*: a cover laid over that table; 0 leaves a cell open and −∞ hides it.

**One number from the real model.** CLIP's 77 × 77 mask holds 2926 entries of −∞ *(computed: the code walk's [rig.json](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/code-walk/what-each-line-of-clip-computes/pictures/rig.json), entry `mask_neg_inf_count`)*. Run "a cat" and "a cat and a dog" through the text transformer: the "cat" slot's 512 numbers differ by at most 0.0 between the two captions, while the end-of-text slot, which now sits after "dog", differs by up to 2.1823 *(computed: journey 02's [CLIP numbers](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/clip_numbers.json), entry `causal_mask`)*.

## Where to learn this

**Causal Attention Mask**, 0 on the scores a position may read and −∞ on every later one, added before the softmax. Also: causal mask, causal masking, masked self-attention, causal self-attention.

**Textbooks**

- Understanding deep learning, section 12.7.2: [pages 237 to 238](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=237). Masked self-attention sets the dot products with later positions to negative infinity before the softmax, so a decoder that predicts every next token at once cannot cheat by looking at the tokens it has to predict.

**Videos**

- CS231n lecture 8, 53:53 to 55:24: [watch](https://www.youtube.com/watch?v=RQowiOF_FvQ&t=3233s). Masked self-attention on "attention is very good": the blocked scores set to minus infinity before the softmax so each word sees only earlier words. Caption-read.
- CS224N 2023 lecture 8, 33:02 to 34:58: [watch](https://www.youtube.com/watch?v=LWMzyfvuehA&t=1982s). The full n by n score matrix computed, every score where j is after i set to minus infinity, and the softmax turning those into weight 0, drawn as a grid of greyed-out cells. From the video lessons index.
- CS229 lecture 14, 57:44 to 1:05:26: [watch](https://www.youtube.com/watch?v=pwQ0l4hFCVI&t=3464s). Attention in matrix form, softmax(QKᵀ/c)V, then the causal mask, −∞ on the upper triangle so position t never sees later tokens. Caption-read.
- 3Blue1Brown, Deep Learning chapter 6, 11:05 to 12:42: [watch](https://www.youtube.com/watch?v=eMlx5fFNoYc&t=665s). Why the mask exists (training predicts every next word at once) and why blocked scores become minus infinity before the softmax and not 0 after it. From the video lessons index.

**Papers**

- [CLIP paper, page 5](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/learning-transferable-visual-models-from-natural-language-supervision.pdf#page=5): "Masked self-attention was used in the text encoder" to keep the option of starting it from a pre-trained language model.

**Our plans and chapters**

- [Mask the future and add position](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/42-mask-the-future-and-add-position.md#work-the-masked-rows), deep-learning/transformers, chapter 42. The masked rows of a toy sentence worked by hand, then checked in code.
- [CLIP on one small network, 1.1: the caption tower, one masked head](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/textbook/01-clip-on-one-small-network.md#11-the-caption-tower-one-masked-head), deep-learning/generative-models/02-stable-diffusion-and-clip, chapter 1. A 4-slot caption through one head under the mask, each row's weights split evenly over the positions it may read.
- [The CLIP rebuild, rung 7: adding −∞ before the softmax makes a weight exactly 0](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/rebuild-clip-from-fundamentals.md#rung-7-adding--before-the-softmax-makes-a-weight-exactly-0), papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers, beside the CLIP paper. The end-of-text row puts 0.0 weight on all 70 padding positions after it.
- [The CLIP rebuild, section 13: build_attention_mask](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/rebuild-clip-from-fundamentals.md#13-masked-build_attention_mask), the same file. `model.py` lines 328 to 334 fill the 77 × 77 table, and "a cat" against "a cat and a dog" shows what the mask buys.
- [Under a causal mask position 0 depends only on position 0](/home/molef/goal-setting/learning/deep-learning/diffusion-models/text-embedding-arithmetic-in-sdxl/plans/02-position-zero-depends-on-itself.md), deep-learning/diffusion-models/text-embedding-arithmetic-in-sdxl, plan 02. Why the first position of a causal text encoder cannot depend on the prompt at all, derived on three small cards.
- [CLIP, read through a small network, section 1: a caption becomes a vector, each word reading only backward](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/clip-read-through-a-small-network.md#1-a-caption-becomes-a-vector-each-word-reading-only-backward), papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers, beside the CLIP paper. Each word's vector takes a mean of itself and the words before it, never the words after.

**Scenes**

- [CLIP module tree, Text encoder](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#text-encoder). Twelve pre-norm transformer blocks under the causal mask, 8 heads × 64 = 512.
- [CLIP code walk, Masked: build_attention_mask](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#mask). Build_attention_mask filling the upper triangle with minus infinity so no word reads ahead.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv4-the-cat-vector-cannot-see-dog.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv4-the-cat-vector-cannot-see-dog.png" width="200" alt="The tokens of a cat above and a cat and a dog below; the cat outputs match exactly and the end outputs differ"></a> Journey 02's network view, "The cat vector cannot see dog": [what it shows](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/README.md). The "cat" slot identical in both captions (largest difference 0.0 over 512 values), the end token's differing by up to 2.1823, and the cat's mask row showing why.
- <a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv3-inside-one-text-block.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv3-inside-one-text-block.png" width="200" alt="Layer norm, attention, add, layer norm, MLP, add; below, the 7 by 7 causal mask"></a> Journey 02's network view, "Inside one text block": [what it shows](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/README.md). The real 7 × 7 causal mask, grey where a token may not read, with the end token's block-12 weights in the bottom row.
- <a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv3b-one-query-asks-the-keys.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv3b-one-query-asks-the-keys.png" width="200" alt="Seven tokens each projected to a query, key and value; the end token's query scores every key, divided by 8, plus a zero mask, softmaxed into weights"></a> Journey 02's network view, "One query asks the keys": [what it shows](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/README.md). The end token's row, where the mask adds 0 everywhere because the end comes after every word, before the softmax gives 0.385 to "dog".

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-17. The textbook pages were read in the PDF with pdftotext, found through the back-of-book tables in `~/.claude/cache/book-indexes/` ("masked self-attention"). The CS231n and CS229 rows were read in the caption-read lecture maps under `~/.claude/cache/captions/`; the CS224N and 3Blue1Brown rows are copied from the video lessons index, `Mathematics/references/videos/Video Lessons.md`, section "Masking the future in self-attention". CME295 lecture 1 at 1:13:43 names masked self-attention in the decoder and was left out to keep four videos. The CLIP paper sentence was read on page 5. Each plan and chapter was read at its heading and opening lines, and the worked numbers were read from `rig.json` and `clip_numbers.json`. "attention mask" is not an alias: in the tokenizer output the learning tree quotes, `attention_mask` marks padding, a different mask. A script then opened every link.
