---
aliases: [cross-attention, cross attention, encoder-decoder attention]
standard: vault-note v2
---

# Cross-Attention

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. The operation it varies is [[Attention]], and the block it sits in is the [[Transformer]].

**Cross-attention is attention whose queries come from one sequence and whose keys and values come from another, so a decoder can read its encoder or an image can read its text prompt.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches cross-attention writes the rest around it.
> - The placement is unsure. The two best places are `Artificial Intelligence/Deep Learning/` and the top of `Artificial Intelligence/`, beside [[Attention]].

## Where to learn this

**Cross-attention**, queries from one sequence reading keys and values from another. Also: cross attention, encoder-decoder attention.

**Textbooks**

- Understanding deep learning, section 12.8: [pages 240 to 241](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=240). The encoder-decoder translation model, where a new attention layer in each decoder block takes its queries from the decoder and its keys and values from the encoder (Figure 12.14).
- Probabilistic machine learning: an introduction, section 15.5.4: [pages 577 to 578](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=577). Writes the decoder block with the cross-attention step Z′ = LN(MHA(Z, E, E) + Z), where E is the encoder's output.

**Videos**

- CME295 lecture 1, 1:38:47 to 1:41:20: [watch](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5927s). Works the decoder of the lecture's example one token at a time from BOS: causal self-attention, then cross-attention on the encoder output, then the feed-forward layer and the softmax over the vocabulary. Caption-read.
- CS224N 2023 lecture 8, 1:10:02 to 1:12:39: [watch](https://www.youtube.com/watch?v=LWMzyfvuehA&t=4202s). The decoder's vectors supply the queries and the encoder's output supplies the keys and values, so two of the three arrows come from the encoder. Caption-read, from the video lessons index.
- CS231n lecture 8, 44:45 to 50:50: [watch](https://www.youtube.com/watch?v=RQowiOF_FvQ&t=2685s). Names cross-attention as queries and data from different sources, then defines self-attention against it and says when to use each. Caption-read.
- CME296 lecture 5, 1:13:04 to 1:20:43: [watch](https://www.youtube.com/watch?v=HpFdSlMeXzQ&t=4384s). Why a text-to-image model needs cross-attention: adaptive layer norm modulates every image token the same way, so "brown bear, white walls" fails, then cross-attention against joint attention. Caption-read.

**Papers**

- Dahary and others 2024, Be yourself: bounded attention for multi-subject text-to-image generation, sections 3 and 4.2: [pages 3 to 4](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/region-and-binding-failures/bounded-attention-for-multi-subject-text-to-image-generation.pdf#page=3). How Stable Diffusion's cross-attention layers inject the prompt into the latent, and how their queries leak meaning between two similar subjects (Figure 3).

**Our plans and chapters**

- [Say how cross-attention differs from self-attention](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/45-say-how-cross-attention-differs-from-self.md), deep-learning/transformers, chapter 45. Works a 2-word decoder reading a 3-word encoder by hand, down to its [2 by 3 weights matrix](../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=91).
- [Run cross-attention with a 2-word decoder reading a 3-word encoder](/home/molef/goal-setting/learning/deep-learning/transformers/plans/46-run-cross-attention-with-a-2-word.md), deep-learning/transformers, plan 46. The same calculation rebuilt in code, then rerun with the sources swapped to show what changes.
- [Cross-attention: asking for a 7](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/plans/04-cross-attention-asking-for-a-seven.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, plan 04. Derives cross-attention with image features as queries and the digit label as keys and values, then types it into a UNet.
- [Cross-attention, attn2, where text enters](/home/molef/goal-setting/learning/deep-learning/diffusion-models/latent-diffusion-architecture-rebuilt/plans/07-cross-attention.md), deep-learning/diffusion-models/latent-diffusion-architecture-rebuilt, plan 07. The `attn2` block of a toy latent-diffusion UNet: queries from image tokens, keys and values from the conditioning sequence.

**Scenes**

- [SDXL cross-attention, PoE and LoRA notebook, Cross-attention](https://claude.ai/artifact/RP59hpFThMPmbftvvWPpbi#nb-sec9). Cross-attention from 4096 image tokens to 77 text tokens, softmax over each row, scaled by one over root d.
- [SDXL cross-attention, PoE and LoRA notebook, Attention shifted by training](https://claude.ai/artifact/RP59hpFThMPmbftvvWPpbi#nb-sec20). A dog-snout query whose attention on 'dog' rises from 0.239 by real gradient steps on a LoRA.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook and paper page range was read in the PDF with pdftotext; the Understanding deep learning page was found through its back-of-book index ("cross-attention", PDF page 241). Hands-on large language models (PDF page 149) and AI engineering (PDF pages 830 and 848) only mention the word and have no line. The CME295, CS231n and CME296 rows were read in the caption-read lecture maps under `~/.claude/cache/captions/`; the CS224N row is copied from the video lessons index, `Mathematics/references/videos/Video Lessons.md`, section "Cross-attention in the encoder-decoder transformer". CME296 lecture 5 at 30:29 lists cross-attention as one of three ways to inject a condition and was left out to keep four videos. Each plan and chapter was read at its title and description.
