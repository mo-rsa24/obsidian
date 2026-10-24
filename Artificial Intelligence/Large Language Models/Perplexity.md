---
aliases: [perplexity, PPL]
standard: vault-note v2
---

# Perplexity

Up: [[Large Language Models]]

Artificial Intelligence, Large Language Models. It is the exponential of [[Cross-Entropy]].

**Perplexity is a language model's cross-entropy on a text turned back into a count, 2 to the power H in bits, so it reads as the number of equally likely next tokens the model is choosing between.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches perplexity writes the rest around it.
> - The placement is unsure. The two best places are `Artificial Intelligence/Large Language Models/` and `Mathematics/Statistics/`, beside [[Cross-Entropy]].

## Where to learn this

**Perplexity**, the exponential of cross-entropy used to score a language model. Also: PPL.

**Textbooks**

- AI engineering, chapter 3, Perplexity: [pages 246 to 251](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=246). Works it with numbers: a model whose cross-entropy over 4 position tokens is 2 bits has perplexity 2² = 4, then nats against bits, why longer context and more structured data lower it, and why post-training raises it.
- Probabilistic machine learning: an introduction, section 6.1.5: [pages 241 to 242](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=241). Defines perplexity as 2^H(p), shows a uniform distribution over K states has perplexity K, and reads a language model's perplexity as its weighted average branching factor.

**Videos**

- CME295 lecture 1, 10:32 to 22:52: [watch](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=632s). Sorts NLP tasks by kind and gives each its metric, with perplexity as the measure for text generation beside BLEU and ROUGE. Caption-read.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after the books' back-of-book indexes pointed to them ("perplexity" in both). Three other index hits were opened and have no line: Hands-on large language models PDF page 349 (the RAG section) and Probabilistic machine learning: advanced topics PDF page 268 (continuous entropy) are not about perplexity, and the same book's PDF page 808 defines it as 2^H in one sentence while evaluating generative models. The CME295 row was read in its caption-read lecture map under `~/.claude/cache/captions/`, and is the only row in the four lecture maps that names perplexity. Stanford CS336 lecture 12 (Evaluation) has no chapter list, and CS224N lecture 5's chapter titles do not name perplexity, so neither could be cited to a moment. No plan or compiled chapter in the learning tree teaches perplexity, so there is no plans group.
