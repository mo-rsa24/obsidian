---
aliases: [tokenization, tokenisation, tokenizer, tokeniser, tokenize, tokenise, byte-pair encoding, byte pair encoding, BPE, subword tokenization]
standard: vault-note v2
---

# Tokenization

Up: [[Large Language Models]]

Artificial Intelligence, Large Language Models. The token IDs it produces are what a [[Transformer]] reads.

**Tokenization splits text into tokens from a fixed vocabulary and gives each an integer ID, and byte-pair encoding builds that vocabulary by repeatedly merging the most frequent adjacent pair of symbols.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches tokenization writes the rest around it.

## Where to learn this

**Tokenization**, splitting text into vocabulary tokens and their IDs. Also: tokenizer, byte-pair encoding, BPE, subword tokenization.

**Textbooks**

- Understanding deep learning, section 12.5.1: [pages 231 to 232](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=231). Works byte-pair encoding on a nursery rhyme with the counts shown: the first merge joins s and e, the second e and the space, and after 22 merges the tokens are a mix of letters, fragments and common words (Figure 12.8).
- Hands-on large language models, chapter 2, LLM tokenization: [pages 68 to 94](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=68). Runs a tokenizer in code (token 3323 is "Sub" and 622 is "ject"), compares word, subword, character and byte tokens, then splits one test text with a row of real trained tokenizers.
- AI engineering, chapter 1: [page 36](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=36). Defines tokenization and the vocabulary (32,000 tokens for Mixtral 8x7B, 100,256 for GPT-4), and gives three reasons models use tokens instead of words or characters.
- Natural language processing with Python, section 3.7: [pages 131 to 134](../../Mathematics/references/textbooks/natural-language-processing/natural-language-processing-with-python.pdf#page=131). Classic word tokenization with regular expressions and NLTK's tokenizer, worked on a passage of Alice's Adventures in Wonderland.

**Videos**

- CME295 lecture 1, 22:52 to 30:04: [watch](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1372s). Splits "a cute teddy bear is reading" with word, subword and character tokenizers and weighs what each costs: subwords share roots like bear and bears, characters survive typos but make sequences much longer. Caption-read.
- Stanford CS336 lecture 1, Tokenization deep dive, 1:05:06 to 1:19:22: [watch](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=3906s). The lecture's deep dive on tokenization, in a course that builds a language model from scratch. Chapter-timed.
- Vizuara, Lecture 8: The GPT Tokenizer: Byte Pair Encoding, Implementing BPE in Python, 40:51 to 47:47: [watch](https://www.youtube.com/watch?v=fKd8s29e-l4&t=2451s). Byte-pair encoding written in Python, after the lecture's algorithm and practical demonstration. Chapter-timed.
- Under The Hood, LLM Training Starts Here: Dataset Preparation & Tokenization Explained!, Byte Pair Encoding (BPE) Tokenization, 4:54 to 7:06: [watch](https://www.youtube.com/watch?v=bNjVxUDZQfM&t=294s). A short visual pass over byte-pair encoding. Chapter-timed.

**Scenes**

- [SDXL cross-attention, PoE and LoRA notebook, Tokenizing the prompt](https://claude.ai/artifact/RP59hpFThMPmbftvvWPpbi#nb-sec4). "a cat and a dog" turned into 77 token ids, 7 words and 70 padding.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/natural-language-processing/artifacts/figures/llm-concepts-cheatsheet/jaydeepkarale-ai-llm-concepts-part1.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/natural-language-processing/artifacts/figures/llm-concepts-cheatsheet/jaydeepkarale-ai-llm-concepts-part1.jpg" width="140" alt="A ten-panel cheat sheet whose panel 1 splits I love AI! into four tokens with ids 101, 732, 4287 and 0"></a> Jaydeep Karale on X, "AI / LLM Concepts Cheat Sheet (Part 1)": [the post](https://x.com/_jaydeepkarale/status/2095815664187609355), [what it shows](/home/molef/goal-setting/learning/deep-learning/natural-language-processing/artifacts/figures/llm-concepts-cheatsheet/README.md#jaydeepkarale-ai-llm-concepts-part1jpg). Panel 1 splits "I love AI!" into "I", "love", "AI" and "!" with ids 101, 732, 4287 and 0, and says a token can be a word, a subword or a character and that the split is model-specific (BPE, SentencePiece, tiktoken).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after the books' back-of-book indexes pointed to them ("tokenization" and "byte pair encoding" in Understanding deep learning, "tokens and tokenizers" in Hands-on large language models, "tokenization, defined" in AI engineering, "tokenization, regular expressions for" in Natural language processing with Python). Probabilistic machine learning: an introduction mentions byte-pair encoding in one sentence on PDF page 53 and has no line. The CME295 row was read in its caption-read lecture map under `~/.claude/cache/captions/`, and paraphrases the map. The CS336, Vizuara and Under The Hood lines come from chapter lists read with cache-video-chapters.py and are described from the chapter titles only. CS229 lecture 14 at 1:36 to 10:38 (caption-read) also explains BPE and was left out to keep four videos. No plan or compiled chapter in the learning tree teaches tokenization, so there is no plans group; `ai-engineering/agent-architecture/artifacts/results/how-two-tokenizers-split-the-same-phrases/` holds a real export of two tokenizers splitting five phrases, and is a results folder, not a plan.
