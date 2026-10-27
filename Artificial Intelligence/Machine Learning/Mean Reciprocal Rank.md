---
aliases: [mean reciprocal rank, MRR, MRR@3, MRR@5, MRR@k, reciprocal rank]
link-skip: [reciprocal rank fusion, Reciprocal rank fusion, Reciprocal Rank Fusion, RRF]
standard: vault-note v2
---

# Mean Reciprocal Rank

Up: [[Machine Learning]]

Artificial Intelligence, Machine Learning. Its sibling recall@k sits on [[Precision And Recall]]; both score the retrieval step of [[Retrieval-Augmented Generation]].

**Mean reciprocal rank scores a ranked list by where the first relevant item lands: each query scores 1 divided by that rank (1 for first place, 1/2 for second, 1/3 for third), and MRR is the mean over queries; MRR@k scores 0 when the item is outside the top k.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches mean reciprocal rank writes the rest around it.

## Where to learn this

**Mean reciprocal rank (MRR)**, the average over queries of 1 / (rank of the first relevant item). Also: reciprocal rank, MRR@k.

**Textbooks**

- Hands-on large language models, chapter 8, Scoring a single query with average precision: [pages 345 to 347](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=345). Teaches the idea under another name: with one relevant document, a system that ranks it first scores 1 and one that ranks it third scores 0.3, which is 1/3, so average precision on a one-answer query is the reciprocal rank and mean average precision is MRR.
- AI engineering, chapter 6, Retrieval algorithms: [page 514](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=514). Names MRR beside NDCG and mean average precision as the metrics to use when the order of the retrieved documents matters; it works no example.

No shelf book defines MRR and works it; the back-of-book indexes do not list it.

**Videos**

- CME295 lecture 7, 47:31 to 57:44: [watch](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2851s). Defines the retrieval metrics: NDCG, MRR from the rank of the first relevant chunk, recall@k and precision@k, then the MTEB benchmark. Caption-read.

**Our plans and chapters**

- [3.3 MRR](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/textbook/03-scoring-retrieval.md#33-mrr), ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions, chapter 03. Works MRR@3 on three questions: vector search alone gives (1 + 0 + 0.333) / 3 = 0.444, the permission filter gives 0.667, and dropping the cut-off would give 0.5 on the same ranks.
- [recall@3 and MRR by hand](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/plans/08-recall-and-mrr-by-hand.md), ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions, plan 08. The plan for that section, computing both metrics on paper before the build prints them.
- [The permission filter](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/textbook/07-the-permission-filter.md), ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions, chapter 07. Checks that the filtered build prints MRR@3 0.667 against 0.444 unfiltered, with no leaks.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27. Each textbook page was read in the PDF with pdftotext. The gather script found MRR only on AI engineering page 514, which names it; mean average precision came from Hands-on large language models' back-of-book index ("MAP (mean average precision)"), and its one-relevant-document case is the reciprocal rank. AI engineering page 519 teaches reciprocal rank fusion, a way to merge rankings that is a different idea, so it has no line and "reciprocal rank fusion" is a skip phrase; plan 18 of the same journey works fusion and is left off for the same reason. The CME295 row was read in its caption-read lecture map. No figure was found. This is a card of its own rather than a "Ranking metrics" card because recall@k already sits on [[Precision And Recall]], where it reads as precision and recall cut at k, and an alias names one note only. A script then opened every link and confirmed the file exists, the page is inside the PDF, and the video start matches a lecture-map row.
