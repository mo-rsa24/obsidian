---
aliases: [full-text search, full text search, inverted index, keyword search, keyword index, lexical search, term-based retrieval, Elasticsearch, BM25]
standard: vault-note v2
---

# Full-Text Search

Up: [[System Design]]

Information Technology, System Design. The inverted index is one kind of [[Database Index]], built for words instead of column values; keyword search is the older half of the hybrid retrieval in [[Retrieval-Augmented Generation]].

**Full-text search finds documents by the words they contain: an inverted index maps each term to the documents holding it, and a scorer such as BM25 ranks the matches by how often the query's rarer terms appear.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches full-text search writes the rest around it.

## Where to learn this

**Full-text search**, finding documents by their words through an inverted index. Also: inverted index, keyword search, lexical search, term-based retrieval, Elasticsearch, BM25.

**Textbooks**

- AI engineering, chapter 6, Term-based retrieval: [pages 503 to 506](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=503). Works it with numbers: term frequency, then inverse document frequency (a term in 5 of 10 documents has IDF 10 / 5 = 2), TF-IDF, an inverted index drawn as a table ("banana" in 2 documents, at (10, 3) and (5, 2)), Elasticsearch on Lucene, and BM25 normalising term frequency by document length.
- Hands-on large language models, chapter 8, Dense retrieval: [pages 326 to 328](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=326). BM25 keyword search written in Python with `rank_bm25`, then run on the same question as dense retrieval to show the passage it misses because the words differ.
- System design big archive, 5 Data Structures That Make DB Queries Super Fast: [page 241](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=241). The inverted index in two sentences, beside the hash and bitmap indexes.
- System design big archive, 10 Essential Components of a Production Web Application: [pages 34 to 35](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=34). Where full-text search sits in a real system: a separate search service, built on Elasticsearch or Apache Solr.

**Videos**

- Arpit Bhayani, Inverted Index - The Data Structure Behind Search Engines, Building an inverted index, 3:33 to 6:23: [watch](https://www.youtube.com/watch?v=iHHqnyThrqE&t=213s). Building the index, after chapters on why naive search is slow and what the index looks like. Chapter-timed.
- Hello Interview, Elasticsearch Deep Dive, Inverted Indexes, 32:24 to 35:09: [watch](https://www.youtube.com/watch?v=PuZvF2EyfBM&t=1944s). The inverted index inside Elasticsearch's Lucene segments, in a long walk through ingesting, filtering, sorting and the cluster. Chapter-timed.
- Hello Interview, DB Indexing in System Design Interviews, Inverted index, 10:53 to 12:43: [watch](https://www.youtube.com/watch?v=BHCSL_ZifI0&t=653s). The inverted index as one index type beside the B-tree, hash and geospatial ones. Chapter-timed.
- ByteByteGo, How Search Really Works, The indexing process, 2:33 to 3:37: [watch](https://www.youtube.com/watch?v=TByRaraQqW4&t=153s). How a web search engine indexes the pages it crawled. Chapter-timed.

**Our plans and chapters**

- [Keyword search against vector search: BM25 beside embeddings on the same documents and twenty questions](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/52-keyword-search-against-vector-search.md), ai-engineering/one-business-end-to-end, plan 52. Works it on the shop's passages: a BM25 index over the same chunks as the embeddings, twenty questions asked of both, and a count of where the top three differ and which was right.
- [TF-IDF over the four documents, and BM25 beside it](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/textbook/06-retrieval.md#63-tf-idf-over-the-four-documents-and-bm25-beside-it), the same journey, chapter 6, section 6.3. TF-IDF built in code over four documents, with BM25 run beside it.
- [Hybrid keyword and vector search](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/plans/19-hybrid-search.md), ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions, plan 19. BM25 keyword search built beside an existing vector search and the two rankings fused in code.
- [System Design: Search and Indexing](/home/molef/goal-setting/learning/system-design/search-and-indexing/MASTER_PLAN.md), system-design/search-and-indexing. The journey that implements an inverted index from scratch and then Elasticsearch's analyzers and mappings; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the back-of-book index of Hands-on large language models ("BM25 algorithm", "keyword search") and a page-text search for "inverted index", "BM25", "Elasticsearch" and "full-text" across the shelf. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title and description, and the chapter section at its first lines. BM25 and Elasticsearch had no card of their own, so they are aliases here.
