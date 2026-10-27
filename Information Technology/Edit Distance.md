---
aliases: [edit distance, Levenshtein distance, Levenshtein, Levenshtein edit distance, minimum edit distance, string edit distance, edit-distance table]
standard: vault-note v2
---

# Edit Distance

Up: [[Information Technology]]

Information Technology. Placement unsure: the two best places are a future Algorithms folder here, beside other dynamic programming, or a natural-language-processing family under [[Artificial Intelligence]].

**Edit distance (the Levenshtein distance) is the fewest one-character insertions, deletions and substitutions that turn one string into another, found by filling a table where D[i][j] = min(D[i−1][j] + 1, D[i][j−1] + 1, D[i−1][j−1] + [aᵢ ≠ bⱼ]) and reading the bottom-right corner.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches edit distance writes the rest around it.

## Where to learn this

**Edit distance**, the fewest insertions, deletions and substitutions between two strings. Also: Levenshtein distance, minimum edit distance, string edit distance.

**Textbooks**

- Pattern classification (Duda, Hart and Stork), section 8.5.2, Algorithm 3: [pages 486 to 487](../Mathematics/references/textbooks/machine-learning/pattern-classification.pdf#page=486). Fills the cost matrix column by column for "excused" to "exhausted" and reads C[7, 9] = 3 at the corner (substitute h for c, insert a, insert t), in O(mn) time (figure 8.9); then notes that unequal costs can break the triangle inequality.
- AI engineering, chapter 3, Lexical similarity: [pages 261 to 262](../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=261). Names the three edit operations on "brad", "bad", "bard" and "bed", and scores "bad" as one edit from "bard" and three from "cash", as a way to compare a model's answer with a reference.
- Pattern classification solutions, chapter 8, problems 23 to 26: [pages 286 to 289](../Mathematics/references/textbooks/machine-learning/pattern-classification-solutions.pdf#page=286). Classifies test strings such as "abacc" by the smallest edit distance to nine labelled strings, then repeats with substitutions costing double and shows a cost of 5 breaks the triangle inequality.
- Computer vision (Prince), section 11.2, MAP inference for chains: [page 251](../Mathematics/references/textbooks/computer-vision/computer-vision-textbook.pdf#page=251). Same shape: the Viterbi trellis fills each cell with the cheapest of its predecessors plus a cost, then traces back from the end, as the edit-distance table fills each cell from three neighbours and backtraces the alignment.
- Natural language processing with Python, chapter 4, exercise 25: [page 198](../Mathematics/references/textbooks/natural-language-processing/natural-language-processing-with-python.pdf#page=198). Asks the reader to try `nltk.edit_dist()` and say how it uses dynamic programming; it works no example.

**Videos**

- Stanford CS124, 2.2 Computing Minimum Edit Distance, 0:00 to 5:55: [watch](https://www.youtube.com/watch?v=NlGoRN1C13w&t=0s). The recurrence, the first row and column, and the "intention" against "execution" table filled to its corner. Whole video, caption-read by the string-similarity pass.
- Stanford CS124, 2.1 Defining Minimum Edit Distance, 0:00 to 7:05: [watch](https://www.youtube.com/watch?v=V14ikwzaLds&t=0s). Aligns "intention" with "execution" as 5 edits when every edit costs 1 and 8 when a substitution costs 2, then says why a table of prefix distances keeps only the cheapest path. Whole video, caption-read by the string-similarity pass.

**Our plans and chapters**

- [Edit distance: count the cheapest edits](/home/molef/goal-setting/learning/ai-engineering/string-similarity-measures/textbook/11-edit-distance.md), ai-engineering/string-similarity-measures, chapter 11. Starts from "powder" to "powders" at distance 1, then fills the table for product names: a different product needs 16 edits and the right Maybelline product 23, so the count measures text changes and says nothing about product identity.
- [Compute edit distance by hand](/home/molef/goal-setting/learning/ai-engineering/string-similarity-measures/plans/13-edit-distance-by-hand.md), ai-engineering/string-similarity-measures, plan 13. The plan for that chapter, with the CS124 segments placed before, during and after the table.
- [Normalised Levenshtein: divide by the longer length](/home/molef/goal-setting/learning/ai-engineering/string-similarity-measures/textbook/12-normalised-levenshtein.md), ai-engineering/string-similarity-measures, chapter 12. Divides the distance by the longer string's length: "grand-pa headache powders 12-pack" against "grand-pa headache powder 12 pack" is 2 edits.
- [Compute normalised Levenshtein by hand](/home/molef/goal-setting/learning/ai-engineering/string-similarity-measures/plans/15-normalised-levenshtein-by-hand.md), ai-engineering/string-similarity-measures, plan 15. The plan for chapter 12.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27. Each textbook page was read in the PDF with pdftotext, found through the books' back-of-book indexes ("edit distance") and `find-examples.py --concept` and `--like "edit distance"`; the Prince page shares the edit-distance table's shape. Probabilistic machine learning: advanced topics, section 29.3.3 (pages 1011 to 1013), uses edit distance inside spelling correction and has no line. The two CS124 videos have no chapter list, so they are cited whole; the string-similarity journey's video-scout pass caption-read them and placed narrower segments in plan 13. `find-figures.py` found no saved figure. Each plan and chapter was read at its heading and worked numbers. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a cached chapter.
