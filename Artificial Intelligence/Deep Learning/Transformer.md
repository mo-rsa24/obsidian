---
aliases: [transformer, transformer architecture, transformer block, transformer layer, transformer model]
link-skip: [following the transformers]
standard: vault-note v2
---

# Transformer

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. Its central operation has its own note, [[Attention]], and so does the way a decoder reads an encoder, [[Cross-Attention]].

**A transformer is a stack of identical blocks, each one multi-head attention followed by a small feed-forward network applied to every token, with a residual connection and layer normalisation around both.**

<!-- video-table: multi-head-attention rev=2 -->
3Blue1Brown, then Stanford CS224N, on multi-head attention, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Orient, before you work two heads: different kinds of context change need different key, query and value maps, so many heads run in parallel (96 in GPT-3) and every head's proposed change is summed into the embedding. Watch for the output matrix, where papers staple the heads' value maps together | Intuition | [3Blue1Brown, Deep Learning chapter 6, 19:25 to 23:19](https://www.youtube.com/watch?v=eMlx5fFNoYc&t=1165s) |
| 2 | Confirm after the sitting: h heads, each with its own query, key and value matrices projecting to width d over h, a separate softmax per head, then the outputs concatenated and mixed by one final linear map. Watch for "look in different places for different reasons" | Proof | [CS224N 2023, lecture 8, 47:50 to 52:05](https://www.youtube.com/watch?v=LWMzyfvuehA&t=2870s) |

No toy with one-number heads; both use symbols and pictures. Times are caption-read from each video's captions, so each start and end is good to about 30 seconds.
<!-- /video-table -->

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the transformer writes the rest around it.

## Where to learn this

**Transformer**, the architecture built from stacked attention and feed-forward blocks. Also: transformer block, transformer layer, transformer architecture.

**Textbooks**

- Hands-on large language models, chapter 3, An overview of transformer models: [pages 117 to 143](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=117). Runs Phi-3 in code and prints its real layers (an embedding of 32,064 tokens by 3,072 numbers, then 32 decoder blocks, then the language-modelling head), then opens one block's attention.
- Understanding deep learning, sections 12.4 to 12.8: [pages 229 to 241](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=229). The transformer layer drawn as two residual blocks with LayerNorm (Figure 12.7 on page 230), then the encoder, decoder and encoder-decoder models built from it.
- Probabilistic machine learning: an introduction, section 15.5: [pages 574 to 578](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=574). Self-attention and multi-head attention, then the encoder block written as Z = LN(MHA(X, X, X) + X) and E = LN(FF(Z) + Z) on page 577, and the decoder block beside it.
- AI engineering, chapter 2, Transformer architecture: [pages 136 to 146](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=136). Why the transformer replaced seq2seq, what a transformer block holds, and how the model dimension, block count and vocabulary set the size of the Llama models in Table 2-4.

**Videos**

- CME295 lecture 1, 1:35:12 to 1:38:47: [watch](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5712s). Works one encoder layer of the lecture's example through to its output: the heads run in parallel, are concatenated and projected back with W_O, then pass the wider feed-forward layer, and N such layers feed every decoder layer. Caption-read.
- CME295 lecture 1, 1:13:43 to 1:22:46: [watch](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4423s). Walks the encoder (multi-head self-attention, then a feed-forward layer) and the decoder (masked self-attention, then cross-attention), and why positional encoding is needed. Caption-read.
- CS231n lecture 8, 1:02:27 to 1:04:29: [watch](https://www.youtube.com/watch?v=RQowiOF_FvQ&t=3747s). Builds the transformer block from self-attention with a residual and layer norm, then a per-token MLP with its own residual and layer norm, stacked 12 deep at about 200 million parameters in 2017. Caption-read.
- Under The Hood, Transformer Architecture Explained, Encoder: MHA, Add & Norm, FFNN, 10:05 to 13:20: [watch](https://www.youtube.com/watch?v=6vThlsJ_ASE&t=605s). A short visual pass over the parts of an encoder block after attention: multi-head attention, add and norm, and the feed-forward network. Chapter-timed.

**Our plans and chapters**

- [Work multi-head attention, position and the block on a toy](/home/molef/goal-setting/learning/deep-learning/transformers/plans/43-work-multi-head-attention-position.md), deep-learning/transformers, plan 43. Splits the toy into two one-number heads, adds a sinusoidal position, and says what a block is made of, by hand.
- [Build two heads and a sinusoidal position and see why order matters](/home/molef/goal-setting/learning/deep-learning/transformers/plans/44-build-two-heads-and-a-sinusoidal-position.md), deep-learning/transformers, plan 44. The same block built in code from an empty file and checked against the hand numbers.
- [Show why a residual connection keeps gradients alive](/home/molef/goal-setting/learning/deep-learning/transformers/plans/38-show-why-a-residual-connection-keeps-gradients.md), deep-learning/transformers, plan 38. The residual path every block wraps around attention and the feed-forward layer.
- [Normalise a vector by hand with layer norm](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/40-normalise-a-vector-by-hand-with-layer.md), deep-learning/transformers, chapter 40. Layer normalisation worked on [1, 2, 3, 4], the other wrapper inside each block.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/transformers/artifacts/figures/llm-concepts-cheatsheet/jaydeepkarale-ai-llm-concepts-part1.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/transformers/artifacts/figures/llm-concepts-cheatsheet/jaydeepkarale-ai-llm-concepts-part1.jpg" width="140" alt="A ten-panel cheat sheet whose middle row draws attention weights, a transformer block of self-attention, feed-forward and add and normalize repeated N times, and positional encoding added under six tokens"></a> Jaydeep Karale on X, "AI / LLM Concepts Cheat Sheet (Part 1)": [the post](https://x.com/_jaydeepkarale/status/2095815664187609355), [what it shows](/home/molef/goal-setting/learning/deep-learning/transformers/artifacts/figures/llm-concepts-cheatsheet/README.md#jaydeepkarale-ai-llm-concepts-part1jpg). Panel 5 feeds Token 1 to Token N into a block of self-attention, a feed-forward network and add-and-normalize repeated N times, and panel 6 adds a position row under each of six tokens, because without it "cat sat" and "sat cat" look the same to attention.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext; the AI engineering and Hands-on large language models pages were first found through their back-of-book indexes ("transformer architecture"), and the Understanding deep learning and Probabilistic machine learning pages through the chapter tables in the shelf index. The three Stanford rows were read in the caption-read lecture maps under `~/.claude/cache/captions/` and paraphrase the map, never the machine-translated captions. The Under The Hood line comes from its chapter list, read with cache-video-chapters.py, and is described from the chapter title only. CS224N 2023 lecture 8 has a chapter "Transformer architecture" at 35:11 to 41:15 and was left out to keep four videos. Each plan and chapter was read at its title and description. No paper on the shelf teaches the architecture itself, so there is no papers group.
