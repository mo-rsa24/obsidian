---
aliases: [end-of-text pooling, end-of-text token, end-of-text position, end-of-text row, end token, EOS token, EOT token, pooled vector, pooled embedding]
standard: vault-note v2
---

# End-of-Text Pooling

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. It works because of the [[Causal Attention Mask]], and the picked vector then goes through [[Layer Normalization]] and the [[Linear Projection]] into the space [[Contrastive Image-Text Training]] compares in.

**End-of-text pooling turns a caption's many position vectors into one by keeping only the vector at the end-of-text token, which under the causal mask is the first position to have read every word.**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the CLIP chapters need. The explanation beyond them is not written yet.

## What the chapters need

**The picture.**

<a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv5-the-end-token-becomes-the-captions-point.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv5-the-end-token-becomes-the-captions-point.png" width="200" alt="The end token's attention bars over the seven tokens, then layer norm, projection, divide by length, the unit vector u"></a> <a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv5b-four-ways-to-pool.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv5b-four-ways-to-pool.png" width="200" alt="The end token found by argmax, the summary token in front, the mean over tokens with its 4 by 4 scores, a learned query, and SDXL's pooled vector joining the time vector"></a>

Left, the end token's attention row over the seven tokens of "a cat and a dog", then its vector through layer norm, the projection and division by length. Right, four ways to pool: the end token CLIP's text half uses, the summary token in front that its image half uses, the mean over tokens, and a learned query.

**The idea.** The text transformer returns 77 vectors, one per slot. Under the causal mask, slot k has read slots 0 to k and no more, so the end-of-text slot is the first to have read the whole caption. CLIP keeps that one vector and drops the rest. The code finds it by a trick: the end-of-text id, 49407, is the largest in the vocabulary and padding is 0, so `text.argmax(dim=-1)` lands on it *(cited: [the CLIP rebuild, rung 17](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/rebuild-clip-from-fundamentals.md#rung-17-under-the-mask-the-end-of-text-position-is-the-first-to-have-read-the-whole-caption))*. The paper says the same in words: the activations "at the [EOS] token are treated as the feature representation of the text" *(cited: CLIP paper page 5)*. SDXL's pooled vector is this read-out from OpenCLIP bigG's text encoder.

**Words the name uses.** *End-of-text*: the special token `<|endoftext|>`, id 49407, that the tokenizer puts after the last word of every caption. *Pooling*: gathering many vectors into one. A mean or a max pools by combining all of them; this pooling keeps a single row.

**One number by hand, then from the real model.** In the miniature, the ids of "cat dog" are (3, 1, 2, 4) with the end token's id 4 the largest, so argmax (3, 1, 2, 4) = 3 picks the end slot, the first row of the mask open on every word *(computed: the miniature's [answer key](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/substrate/clip_miniature_answer_key.json), entry `argmax`)*. In CLIP, "a cat and a dog" tokenizes to 7 real pieces with id 49407 at position 6, and the argmax lands there. Averaging the 10 real slots of "a photo of a cat and a dog" instead gives a vector at cosine 0.8612 to the end slot's, and that mean changes the winning caption for 2 of journey 13's 4 renders *(computed: journey 02's [CLIP numbers](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/clip_numbers.json), entries `tokens` and `pooling`)*.

## Where to learn this

**End-of-Text Pooling**, one sequence vector taken from the end-of-text position. Also: end-of-text token, end token, EOS token, EOT token, pooled vector, pooled embedding.

**Textbooks**

- Hands-on large language models, chapter 9: [page 372](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=372). Tokenizes "a puppy playing in the snow" for CLIP and prints ids 49406 to 49407 with the `<|startoftext|>` and `<|endoftext|>` pieces, then takes the 512-number text embedding.
- Understanding deep learning, section 12.6: [page 235](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=235). BERT's other choice: a `<cls>` token placed at the start of each string, whose vector alone is mapped to the class for text classification. CLIP's image tower pools the same way, from the token in front.

**Videos**

- CME296 lecture 4, 1:12:12 to 1:17:51: [watch](https://www.youtube.com/watch?v=WUUq6TVAu8U&t=4332s). The vision transformer's CLS token, whose output vector stands for the whole image, the image tower's version of reading one position out. Caption-read.
- CME295 lecture 2, 1:32:43 to 1:41:29: [watch](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5563s). BERT on "this teddy bear is so cute": CLS, SEP and padding added, the encoder run, and only the CLS output fed to a small network for sentiment. Caption-read.

**Papers**

- [CLIP paper, page 5](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/learning-transferable-visual-models-from-natural-language-supervision.pdf#page=5): the text is bracketed with [SOS] and [EOS], and the top layer's activations at the [EOS] token, layer normalized and linearly projected, are the text's feature.

**Our plans and chapters**

- [CLIP on one small network, 1.2: the end token is the caption's summary](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/textbook/01-clip-on-one-small-network.md#12-the-end-token-is-the-captions-summary), deep-learning/generative-models/02-stable-diffusion-and-clip, chapter 1. "cat" and "cat dog" through one block by hand: the cat slot stays (4.5, −1), the end slot moves from (1, 2) to (0, 2), argmax finds the end, and reading position 0 instead makes every caption the same vector.
- [The CLIP rebuild, rung 17: under the mask, the end-of-text position is the first to have read the whole caption](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/rebuild-clip-from-fundamentals.md#rung-17-under-the-mask-the-end-of-text-position-is-the-first-to-have-read-the-whole-caption), papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers, beside the CLIP paper. `model.py`'s `text.argmax(dim=-1)` lands at position 6 for "a cat and a dog", and the projected vector has length 10.1063.
- [CLIP, read through a small network, section 2: the end token is the caption's feature](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/clip-read-through-a-small-network.md#2-the-end-token-is-the-captions-feature), papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers, beside the CLIP paper. The last real token is the first to have read every word, so its vector is read out, found as the position of the largest id.
- [What pooling throws away](/home/molef/goal-setting/learning/deep-learning/diffusion-models/11-pixart-alphas-loop-by-hand/plans/02-what-pooling-throws-away.md), deep-learning/diffusion-models/11-pixart-alphas-loop-by-hand, plan 02. CLIP's one pooled vector against T5's every position and mask, and what a long prompt's later words lose.

**Scenes**

- [CLIP module tree, Text pool](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#text-pool). The end-of-text row picked as the caption's vector, token id 49407 at the picked row.
- [CLIP code walk, Output: the end-of-text position times W_t](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#text_head). The end-of-text position, found by text.argmax, after layer norm times W_t, the caption's vector.
- [SDXL pipeline map, Text encoder 2](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#text-encoder-2). OpenCLIP bigG's text tower, its second-to-last layer kept and its end-token vector projected into the pooled vector p.
- [SDXL code walk, Hidden: each encoder's second-to-last layer, and the second's pooled vector](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#encoders). Hidden_states[-2] kept from each encoder, and the second encoder's projected end-token vector as p.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv5-the-end-token-becomes-the-captions-point.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv5-the-end-token-becomes-the-captions-point.png" width="200" alt="The end token's attention bars over the seven tokens, then layer norm, projection, divide by length, the unit vector u"></a> Journey 02's network view, "The end token becomes the caption's point": [what it shows](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/README.md). The end token's real attention row (0.6781 on the start token), then its vector through layer norm, the 512 × 512 projection and division by its length, 10.1063.
- <a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv5b-four-ways-to-pool.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/cv5b-four-ways-to-pool.png" width="200" alt="The end token found by argmax, the summary token in front, the mean over tokens with its 4 by 4 scores, a learned query, and SDXL's pooled vector"></a> Journey 02's network view, "Four ways to pool": [what it shows](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/network-view/README.md). The end token by argmax, the summary token in front, the mean over tokens (cosine 0.8612 to the end token's vector, 2 of 4 winners changed), a learned query, and SDXL's pooled 1,280 vector joining the time vector.
- <a href="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/miniature/m2-the-cat-row-cannot-see-dog.png"><img src="/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/miniature/m2-the-cat-row-cannot-see-dog.png" width="200" alt="The same block on cat and on cat dog: the cat slot (4.5, -1) in both, the end slot (1, 2) against (0, 2), the mask's end row open on every word, argmax finding the end"></a> Journey 02's miniature, "The cat row cannot see dog": [what it shows](/home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/figures/clip/miniature/README.md). The miniature's two captions through one block, the mask's end row open on every word, and argmax on the ids finding the end.
- <a href="/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/clip-by-hand-thumbnail.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/clip-by-hand-thumbnail.jpg" width="200" alt="A hand-worked sheet: three text-image pairs encoded on two sides with mean pooling, projected into a yellow shared embedding space"></a> Prof. Tom Yeh on X, "CLIP by hand": [the post](https://x.com/ProfTomYeh/status/2094791189371261274), [what it shows](/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/README.md#clip-by-hand-thumbnailjpg). The sheet mean-pools each sentence's word columns into one vector before projecting. Real CLIP keeps the end-of-text row instead, and journey 02's "Four ways to pool" measures the mean landing at cosine 0.8612 to it and changing 2 of 4 winning captions ([the reading](/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/sources/clip-embeddings/SOURCES.md)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-17. The Hands-on large language models page was found through its back-of-book table ("CLIP", PDF pages 366 to 376) and read with pdftotext; the Understanding deep learning page through its table ("cls token"). The pooling pages in the deep learning textbook and Understanding deep learning's chapter 10 are max and average pooling over an image's grid, a different operation, and have no line. The two video rows were read in the caption-read lecture maps under `~/.claude/cache/captions/`; no lecture map row teaches reading a sequence out at its end token, so both teach the CLS form. The CLIP paper sentence was read on page 5. Each plan and chapter was read at its heading and opening lines, and the worked numbers were read from the miniature's answer key and `clip_numbers.json`. Bare "pooling" is not an alias, since its 47 uses in the learning tree also mean mean, average and attention pooling and database connection pooling; "pooled vector" and "pooled embedding" are, since the sampled uses mean CLIP's or SDXL's end-of-text read-out. A script then opened every link.
