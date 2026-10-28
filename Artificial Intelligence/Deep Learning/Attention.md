---
aliases: [attention, attention mechanism, self-attention, scaled dot-product attention, dot-product attention, dot-product self-attention, multi-head attention, softmax(QK^T/sqrt(d))V, query key value]
link-skip: [pay attention, needs attention, need attention, more attention, attention to detail, draw attention, your attention, centre of attention]
link-skip-in: [system-design/]
standard: vault-note v2
---

# Attention

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning.

**Attention scores a query against every key, turns the scores into softmax weights, and returns the weighted sum of the values.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches attention writes the rest around it.

## Where to learn this

**Attention**, the scaled dot-product attention of transformers. Also: attention mechanism, self-attention, dot-product self-attention, multi-head attention.

**Textbooks**

- Understanding deep learning, sections 12.2 and 12.3: [pages 222 to 229](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=222). Builds dot-product self-attention as routing: values, weights from query-key [dot products](../../Mathematics/references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=161) and a softmax, the matrix form, then positional encoding, scaling and multiple heads.
- Probabilistic machine learning: an introduction, section 15.4: [pages 566 to 574](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=566). Attention as a weighted average<sub>[1](../../Mathematics/references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=712 "linear algebra textbook p. 712"), [2](../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=165 "algebra handbook p. 165")</sub> of values with weights from comparing a query to keys, with several score functions and its use in sequence-to-sequence models.
- Hands-on large language models, chapter 3, the attention layer: [pages 137 to 142](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=137). Attention in two drawn steps, scoring each earlier token's relevance and combining the values, with heads in parallel and the query, key and value projections.
- AI engineering, chapter 2, Attention mechanism: [pages 139 to 143](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=139). Query, key and value vectors explained as looking up pages of a book, then multi-head attention inside the transformer block.

**Videos**

- CS231n lecture 8, 26:01 to 31:35: [watch](https://www.youtube.com/watch?v=RQowiOF_FvQ&t=1561s). Pulls attention out of the recurrent network as an operator: data vectors, a query, similarity scores, softmax weights and a weighted sum. Caption-read.
- CME295 lecture 1, 1:08:56 to 1:13:43: [watch](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4136s). Defines query, key and value: the query for "teddy bear" against every key, softmax weights, then the weighted sum of values from learned projections. Caption-read.
- CME295 lecture 1, 1:31:35 to 1:35:12: [watch](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5495s). Computes softmax(QKᵀ/√d_k)V [matrix by matrix](../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=91), Kᵀ being the [transpose](../../Mathematics/references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=49) of K, and shows why [dividing by √d_k](../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=86) stops dot products growing with dimension. Caption-read.
- CS229 lecture 14 (transformers and in-context learning), 57:44 to 1:05:26: [watch](https://www.youtube.com/watch?v=pwQ0l4hFCVI&t=3464s). Writes attention in matrix form and adds the causal mask, −∞ above the diagonal so position t never sees later tokens. Caption-read.

**Our plans and chapters**

- [Work self-attention as a 3 by 3 matrix](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/30-work-self-attention-as-a-3.md), deep-learning/transformers, chapter 30. The 3 by 3 weights and the three outputs for a 3-word sentence, by hand.
- [Build the self-attention weights and outputs from scratch](/home/molef/goal-setting/learning/deep-learning/transformers/plans/31-build-the-self-attention-weights-and-outputs.md), deep-learning/transformers, plan 31. The same weights built in code from an empty file and checked against the hand numbers.
- [Show why attention scores are divided by the square root of d](/home/molef/goal-setting/learning/deep-learning/transformers/plans/25-show-why-attention-scores-are-divided.md), deep-learning/transformers, plan 25. The [variance of a dot product](../../Mathematics/references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=199) of random vectors grows with their length d.
- [Say how cross-attention differs from self-attention](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/45-say-how-cross-attention-differs-from-self.md), deep-learning/transformers, chapter 45. A 2-word decoder reads a 3-word encoder, so the queries come from one sequence and the keys and values from the other.
- [Self-attention, attn1](/home/molef/goal-setting/learning/deep-learning/diffusion-models/latent-diffusion-architecture-rebuilt/plans/06-self-attention.md), deep-learning/diffusion-models/latent-diffusion-architecture-rebuilt, plan 06. Scaled dot-product attention derived by hand, then scoped to the UNet's image tokens.

**Scenes**

- [The SDXL notebook in ten parts, Self-attention](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-attn). Self-attention among image tokens, a 4096 by 4096 map at full size.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/transformers/artifacts/figures/llm-concepts-cheatsheet/jaydeepkarale-ai-llm-concepts-part1.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/transformers/artifacts/figures/llm-concepts-cheatsheet/jaydeepkarale-ai-llm-concepts-part1.jpg" width="140" alt="A ten-panel cheat sheet whose panel 4 draws weights 0.1, 0.4, 0.1, 0.1, 0.1 and 0.2 from The cat sat on the mat into cat"></a> Jaydeep Karale on X, "AI / LLM Concepts Cheat Sheet (Part 1)": [the post](https://x.com/_jaydeepkarale/status/2095815664187609355), [what it shows](/home/molef/goal-setting/learning/deep-learning/transformers/artifacts/figures/llm-concepts-cheatsheet/README.md#jaydeepkarale-ai-llm-concepts-part1jpg). Panel 4 draws one attention row over "The cat sat on the mat", weights 0.1, 0.4, 0.1, 0.1, 0.1 and 0.2 summing to 1 and converging on "cat". It never names queries, keys or values or the division by the square root of d, so it shows what attention outputs and nothing of how the weights are computed ([the reading](/home/molef/goal-setting/learning/deep-learning/transformers/sources/llm-concepts-cheatsheet/SOURCES.md#ai--llm-concepts-cheat-sheet-part-1-attention-transformer-positional-encoding)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-22. Each textbook page range was read in the PDF with pdftotext; the Hands-on large language models and AI engineering pages were first found through the links in their back-of-book indexes. Probabilistic machine learning: advanced topics also teaches attention, at PDF pages 661 to 663 (printed 628 to 630), as a soft dictionary lookup; the introduction's section 15.4 covers the same ground at greater length, so only that one has a line. Each video row was read in its course's caption-read lecture map under `~/.claude/cache/captions/`, and its description paraphrases the map, never the machine-translated captions. Each plan and chapter was read at its title and description. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start.
