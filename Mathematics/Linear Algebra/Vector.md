---
aliases: [vector, column vector, row vector]
link-skip: [vector search, vector database, vector store, vector-only, vector index, keyword and vector, keyword-plus-vector, hybrid search, pgvector, vector diagram]
standard: vault-note v2
---

# Vector

Up: [[Linear Algebra]]

Mathematics, Linear Algebra.

**A vector is an ordered list of numbers, read as an arrow from the origin, that can be added to another vector and scaled by a number.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches vectors writes the rest around it.

## Where to learn this

**Vector**, an ordered list of numbers that adds and scales. Also: column vector, row vector.

**Textbooks**

- Linear algebra textbook, section 3.1: [pages 145 to 155](../references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=145). Vectors drawn as arrows in 2-space and 3-space, then written as ordered n-tuples in Rⁿ (Definition 1, page 150).
- Mathematics for machine learning, chapter 2 opening: [pages 23 to 24](../references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=23). What counts as a vector: anything that adds and scales, with geometric arrows and polynomials as the first examples.
- Deep learning textbook, section 2.1: [pages 47 to 49](../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=47). Scalars, vectors, matrices and tensors in the notation the rest of deep learning uses.
- Understanding deep learning, appendix B.3: [page 456](../references/textbooks/machine-learning/understanding-deep-learning.pdf#page=456). A vector as a column of D numbers, beside matrices and tensors as PyTorch and TensorFlow store them.

**Videos**

- Stanford CME296, lecture 1, 28:04 to 28:52: [watch](https://www.youtube.com/watch?v=tr-CUpw--ck&t=1684s). An image as one vector whose length is the number of pixels times 3, which is what x_0 and x_t are in diffusion. Caption-read, from the video lessons index.
- 3Blue1Brown, Vectors (Essence of linear algebra, chapter 1), Three perspectives on vectors, 0:00 to 2:52: [watch](https://www.youtube.com/watch?v=fNk_zzaMoSs&t=0s). The physics arrow, the computer-science list of numbers and the mathematician's view, set side by side. Chapter-timed.
- 3Blue1Brown, Vectors (Essence of linear algebra, chapter 1), Coordinates and space, 2:52 to 4:45: [watch](https://www.youtube.com/watch?v=fNk_zzaMoSs&t=172s). Reading a vector's coordinates as instructions for walking from the origin. Chapter-timed.
- Professor Leonard, Calculus 3 lecture 11.1, An Introduction to Vectors, 0:00 to 2:37:47: [watch](https://www.youtube.com/watch?v=tGVnBAHLApA&t=0s). A full lecture introducing vectors, worked on the board. Whole video.

**Our plans and chapters**

- [Compute vectors, the dot product, length and the angle between them](/home/molef/goal-setting/learning/ai-engineering/string-similarity-measures/foundations/plans/06-vectors-dot-product-and-length.md), ai-engineering/string-similarity-measures/foundations, plan 06. A text turned into a vector of word counts over a shared vocabulary.
- [Find a length, a unit vector and an angle from two lengths and a dot product](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/02-find-a-length-a-unit-vector.md), deep-learning/transformers, chapter 02. The arrow to [3, 4], its length 5 and its unit vector [0.6, 0.8], worked by hand.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after finding it through the back-of-book tables in `~/.claude/cache/book-indexes/` and the chapter tables in `Textbooks.md`. The CME296 line is copied from the video lessons index, section "An image as a vector". The 3Blue1Brown and Leonard chapter lists were read with cache-video-chapters.py; Leonard's 11.1 has no chapter list, so it is cited whole. Each plan and chapter was read at its title and description. The word "vector" alone was sampled in the learning tree (25 lines, 14 meaning this idea and 11 meaning vector search or vector databases), so it is an alias and the retrieval phrases are in `link-skip`. gather-concept-sources.py was started but stopped at its time limit under machine load, so the same sources it reads were searched by hand. A script then opened every link.
