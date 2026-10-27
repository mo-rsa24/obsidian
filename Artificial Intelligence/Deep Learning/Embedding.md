---
aliases: [embedding, embedding vector, word embedding, token embedding, embedding model, embedding layer, embedding matrix, text embedding, sentence embedding, embedding space]
link-skip: [embedding that section, rather than embedding them]
standard: vault-note v2
---

# Embedding

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. Embeddings are what [[Attention]] mixes and what [[Retrieval-Augmented Generation]] searches over.

**An embedding is a learned vector of numbers that stands for a token, a word, a sentence, an image or any other item, placed so that items with similar meaning sit close together.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches embeddings writes the rest around it.

## Where to learn this

**Embedding**, a learned vector for an item. Also: embedding vector, word embedding, token embedding, embedding model.

**Textbooks**

- Hands-on large language models, chapter 2: [pages 100 to 108](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=100). Works it in code: "Best movie ever!" becomes one vector of 768 numbers, and in 50-dimensional GloVe word embeddings the nearest words to "king" are "prince" at 0.82 and "queen" at 0.78, before word2vec's contrastive training.
- Understanding deep learning, section 12.5.2: [page 232](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=232). Each token in the vocabulary gets a learned column of an embedding matrix, applied as the matrix times a one-hot vector, with a typical size D = 1024 for a vocabulary of 30,000.
- Hands-on large language models, chapter 2: [pages 94 to 96](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=94). A language model holds one embedding vector per token of its tokenizer's vocabulary, randomly initialised and set by training, which ties the model to its tokenizer.
- AI engineering, chapter 3, Introduction to Embedding: [pages 267 to 268](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=267). "The cat sits on a mat" as a toy vector [0.11, 0.02, 0.54], real sizes from 100 to 10,000, and a table of embedding sizes for BERT, CLIP, OpenAI's and Cohere's embedding models.

**Videos**

- CME295 lecture 1, 40:48 to 45:57: [watch](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2448s). Trains a toy next-word network with a vocabulary of 6 and hidden size 2, then reads the learned hidden weights off as the embedding. Caption-read.
- CS229 lecture 13, 0:06 to 3:07: [watch](https://www.youtube.com/watch?v=lNTajqxxOn4&t=6s). Defines an embedding φ_θ(x) for images, text or audio: similar inputs map close, different inputs far, with similarity search as the main use. Caption-read.
- StatQuest, Word Embedding and Word2Vec, Building a Neural Network to do Word Embedding, 4:25 to 8:18: [watch](https://www.youtube.com/watch?v=viZrOnJclY0&t=265s). Builds the small neural network whose weights become the word embeddings. Chapter-timed.
- Under The Hood, What Are Word Embeddings?, Embedding Layer in Transformer Architecture, 14:46 to 17:16: [watch](https://www.youtube.com/watch?v=hVM8qGRTaOA&t=886s). Where the embedding layer sits in a transformer, after one-hot encoding and word2vec earlier in the video. Chapter-timed.

**Our plans and chapters**

- [Show an embedding table is a one-hot vector times a matrix](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/33-show-an-embedding-table-is-a-one.md), deep-learning/transformers, chapter 33. A lookup in an embedding table shown to be a one-hot vector times a matrix, worked by hand.
- [Watch two word vectors move together in one hand-run update](/home/molef/goal-setting/learning/deep-learning/transformers/plans/37-watch-two-word-vectors-move-together.md), the same journey, plan 37. One training update run by hand that pulls two co-occurring words' vectors closer.
- [Chunking and embeddings: the shop's documents chunked, embedded, and ranked against a question](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/51-chunking-and-embeddings.md), ai-engineering/one-business-end-to-end, plan 51. Real documents chunked, embedded with an embedding model and ranked against a question.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/natural-language-processing/artifacts/figures/llm-concepts-cheatsheet/jaydeepkarale-ai-llm-concepts-part1.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/natural-language-processing/artifacts/figures/llm-concepts-cheatsheet/jaydeepkarale-ai-llm-concepts-part1.jpg" width="140" alt="A ten-panel cheat sheet whose panel 2 maps king, queen, man and woman to small coloured vectors with similar meaning drawn as similar vectors"></a> Jaydeep Karale on X, "AI / LLM Concepts Cheat Sheet (Part 1)": [the post](https://x.com/_jaydeepkarale/status/2095815664187609355), [what it shows](/home/molef/goal-setting/learning/deep-learning/natural-language-processing/artifacts/figures/llm-concepts-cheatsheet/README.md#jaydeepkarale-ai-llm-concepts-part1jpg). Panel 2 maps "king", "queen", "man" and "woman" to four-cell coloured vectors and draws similar meaning as similar vectors, naming 768 and 1536 as typical widths.
- <a href="/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/clip-by-hand-thumbnail.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/clip-by-hand-thumbnail.jpg" width="200" alt="A hand-worked sheet: three text-image pairs encoded on two sides, projected into a yellow shared embedding space, then softmax similarity matrices and cross-entropy gradients against identity targets"></a> Prof. Tom Yeh on X, "CLIP by hand": [the post](https://x.com/ProfTomYeh/status/2094791189371261274), [what it shows](/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/README.md#clip-by-hand-thumbnailjpg). Three text-image pairs (big table, mini chair, top hat) are encoded on two sides and mean-pooled, then a projection maps the 3-number text vectors and the 4-number image vectors into one shared 2-number embedding space, highlighted in yellow, where a dot product can score every pair.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, first found through the books' back-of-book indexes ("token embeddings", "word embeddings", "embedding", "embedding models"). The Deep learning textbook's word embeddings (PDF page 480) have no line, to keep four. The two lecture rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`. The StatQuest and Under The Hood chapter lists were read with `cache-video-chapters.py` and their lines are described from chapter and video titles only. Each plan and chapter was read at its title and opening lines. Bare "embedding" is an alias because 24 of 25 sampled uses in the learning tree mean the vector; the link-skip phrases cover embedding a section or a frame into a page. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map or a cached chapter list.
