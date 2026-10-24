---
aliases: [RAG, retrieval augmented generation, retrieval-augmented generation, RAG pipeline, RAG system, retrieve-then-generate, grounded generation]
standard: vault-note v2
---

# Retrieval-Augmented Generation

Up: [[Artificial Intelligence]]

Artificial Intelligence.

**Retrieval-augmented generation looks up passages relevant to a question in an outside store and puts them in the model's prompt, so the answer can draw on them.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches retrieval-augmented generation writes the rest around it.
> - The placement is unsure. The two best places are this top level and a Large Language Models family under `Artificial Intelligence/`, which does not exist yet.

## Where to learn this

**Retrieval-augmented generation (RAG)**. Also: RAG, retrieval augmented generation, RAG pipeline, retrieve-then-generate, grounded generation.

**Textbooks**

- AI engineering, chapter 6, RAG: [pages 495 to 499](../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=495). Defines RAG as retrieving from external memory before generating, weighs it against long context, and splits a RAG system into a retriever and a generator.
- AI engineering, chapter 6, retrieval algorithms and retrieval optimisation: [pages 500 to 530](../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=500). Term-based against embedding-based retrieval, how to compare and combine retrievers (reciprocal rank fusion on page 520), then chunking, reranking and contextual retrieval.
- Hands-on large language models, chapter 8, Retrieval-Augmented Generation (RAG): [pages 349 to 358](../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=349). Turns a search pipeline into RAG in code, with grounded generation from an API model and a local model, then query rewriting, multi-hop and agentic RAG, and RAG evaluation.
- AI engineering, chapter 7, Finetuning and RAG: [pages 611 to 617](../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=611). Chooses between RAG and finetuning by whether the model fails for lack of information or because of its behaviour.

**Videos**

- CME295 lecture 7, 15:08 to 19:21: [watch](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=908s). Defines RAG as three steps on a local-election question: retrieve the relevant chunks, augment the prompt with them, generate the answer. Caption-read.
- CME295 lecture 7, 19:21 to 27:29: [watch](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1161s). Builds the knowledge base (chunks of about 500 tokens with overlap, then embeddings) and sets out two-stage retrieval: high-recall candidates, then a costlier ranking stage. Caption-read.
- CME295 lecture 7, 27:29 to 37:45: [watch](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1649s). Retrieves candidates by cosine similarity from a bi-encoder with approximate nearest neighbours, then adds BM25 keyword scoring and hybrid search. Caption-read.
- CS229 lecture 13 (contrastive learning and semantic search), 53:39 to 58:15: [watch](https://www.youtube.com/watch?v=lNTajqxxOn4&t=3219s). Retrieves about 5 to 10 private documents into the context and names modularity, access control and easy deletion as RAG's advantages over fine-tuning. Caption-read.

**Our plans and chapters**

- [Document question answering with permissions, the textbook](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/textbook/00-INDEX.md), ai-engineering/llm-applications/retrieval-augmented-generation. A permission-aware RAG chatbot over Kestrel Freight's documents, built across 17 chapters with every number from a reference build.
- [Hybrid search and the reranker](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/textbook/08-hybrid-and-rerank.md), chapter 8 of the same textbook. A keyword ranking beside the vector one, fused by rank, then reordered by a cross-encoder.
- [The retriever in the loop](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/53-the-retriever-in-the-loop.md), ai-engineering/one-business-end-to-end, plan 53. Three passages per question retrieved from pgvector into the prompt of the shop's agent.
- [Keyword search against vector search](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/52-keyword-search-against-vector-search.md), ai-engineering/one-business-end-to-end, plan 52. BM25 beside embeddings on the same documents and twenty questions.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-22. Each textbook page range was read in the PDF with pdftotext, and the AI engineering pages were first found through the links in its back-of-book index (PDF pages 932 to 988). Each video row was read in its course's caption-read lecture map under `~/.claude/cache/captions/`, and its description paraphrases the map, never the machine-translated captions. Each plan and chapter was read at its title and opening. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start.
