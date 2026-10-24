---
aliases: [KV cache, key-value cache, KV caching, keys and values cache, kv cache, KV-cache]
standard: vault-note v2
---

# KV Cache

Up: [[Large Language Models]]

Artificial Intelligence, Large Language Models. Needs: [[Attention]] for what a key and a value are.

**The KV cache stores the attention keys and values of every token already processed, so each new decoding step computes them only for the newest token.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the KV cache writes the rest around it.

## Where to learn this

**KV cache**, the key-value cache. Also: key-value cache, KV caching, keys and values cache.

**Textbooks**

- AI engineering, chapter 9, Attention mechanism optimization: [pages 820 to 826](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=820). Defines the KV cache as reusing earlier tokens' key and value vectors, sizes it as 2 × B × S × L × H × M with Llama 2 13B (page 823), then shrinks it with multi-query and grouped-query attention, PagedAttention and cache quantization.
- Hands-on large language models, chapter 3, Speeding Up Generation by Caching Keys and Values: [pages 129 to 131](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=129). Shows why only the last token's stream needs computing once earlier results are cached, then times a 100-token generation with and without `use_cache`.

**Videos**

- CME295 lecture 3, 1:27:00 to 1:32:40: [watch](https://www.youtube.com/watch?v=Q5baLehv5So&t=5220s). Builds the KV cache: reuse the stored keys and values of earlier tokens and compute only the new token's, with why queries are not cached and why training with teacher forcing does not need it. Caption-read.
- CME295 lecture 3, 1:32:40 to 1:41:07: [watch](https://www.youtube.com/watch?v=Q5baLehv5So&t=5560s). Cuts KV-cache memory with PagedAttention's fixed blocks of 16 tokens and with DeepSeek's multi-head latent attention, which compresses keys and values into one low-rank vector per token. Caption-read.
- CME295 lecture 2, 55:58 to 1:02:43: [watch](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3358s). Shares key and value projections across heads (multi-query and grouped-query attention) to keep the cache small during decoding. Caption-read.
- CS229 lecture 16 (attention variants and mixture of experts), 4:41 to 7:44: [watch](https://www.youtube.com/watch?v=hHC-SF3utxg&t=281s). The cache keeps every past key and value, so memory grows linearly with the sequence length and limits the batch size. Caption-read.

**Our plans and chapters**

- [Prompt caching and the KV cache](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/25-prompt-caching-and-the-kv-cache.md), ai-engineering/one-business-end-to-end, plan 25. Sends the same schema-first prompt twice and reads from the response's usage how many input tokens came from the cache.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-22. Each textbook page range was read in the PDF with pdftotext, after finding it through the links in the book's back-of-book index (AI engineering PDF pages 932 to 988, Hands-on large language models PDF pages 537 to 595). Each video row was read in its course's caption-read lecture map under `~/.claude/cache/captions/`, and its description paraphrases the map, never the machine-translated captions. The plan was read at its title and description. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start.
