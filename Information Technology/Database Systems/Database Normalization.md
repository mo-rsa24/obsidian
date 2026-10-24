---
aliases: [database normalization, database normalisation, normal form, first normal form, second normal form, third normal form, 1NF, 2NF, 3NF, BCNF, Boyce-Codd normal form, denormalization, denormalisation, denormalize, denormalise, denormalized, denormalised]
standard: vault-note v2
---

# Database Normalization

Up: [[Database Systems]]

Information Technology, Database Systems. Normalization splits a wide table into tables tied by a [[Foreign Key]], and the result is the [[Database Schema]]; denormalization puts some of it back for faster reads.

**Database normalization splits a table so each fact is stored once: first normal form removes repeating groups, second removes columns that depend on only part of the key, third removes columns that depend on another non-key column, and each step removes an update, insert or delete anomaly.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches normalization writes the rest around it.

## Where to learn this

**Database normalization**, storing each fact once by splitting tables. Also: normal form, first normal form, third normal form, 3NF, BCNF, denormalization.

**Textbooks**

- Systems analysis and design, appendix 6A, Normalizing the data model: [pages 276 to 280](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=276). Works a real CD purchase file from zero normal form to third: the repeating CD lines pulled out for 1NF, partial dependencies on the purchase key removed for 2NF, then transitive dependencies for 3NF, with the entity diagram redrawn at each step.
- Systems analysis and design, chapter 6, Validating an entity relationship diagram: [page 272](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=272). The three normal forms in one paragraph each: no repeating attributes, no partial dependency, no transitive dependency.
- System design big archive, 5 Database Normal Forms Every Developer Should Know: [pages 214 to 215](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=214). 1NF, 2NF and 3NF, then Boyce-Codd and fourth normal form, one line each.
- Systems analysis and design, chapter 11, Optimizing access speed: [pages 453 to 455](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=453). Denormalization: the customer's name added back into the order table because order queries always need it, and the four cases where duplicating data to skip a join pays off.

**Videos**

- Decomplexify, Learn Database Normalization - 1NF, 2NF, 3NF, 4NF, 5NF, What is database normalization?, 0:00 to 3:55: [watch](https://www.youtube.com/watch?v=GFQaEYEc8_8&t=0s). The opening of a walk through each normal form in turn. Chapter-timed.
- Decomplexify, the same video, Third Normal Form (3NF), 16:08 to 20:29: [watch](https://www.youtube.com/watch?v=GFQaEYEc8_8&t=968s). Third normal form, after the chapters on first and second. Chapter-timed.
- Hello Interview, Data Modeling in System Design Interviews, Normalization, 21:31 to 23:33: [watch](https://www.youtube.com/watch?v=TUcPS6dsWx4&t=1291s). Normalization as one step of data modelling, after entities, keys and relationships. Chapter-timed.
- ByteByteGo, 7 Must-know Strategies to Scale Your Database, Database denormalization, 3:02 to 3:47: [watch](https://www.youtube.com/watch?v=_1IKwnbscQU&t=182s). Denormalization as a way to scale reads. Chapter-timed.

**Our plans and chapters**

- [Normalisation to third normal form, each anomaly shown live on the shop's sheet](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/03-third-normal-form-with-the-anomalies.md), ai-engineering/one-business-end-to-end, plan 03. Works it on the shop's own rows: the functional dependencies of the wide sheet, the three anomalies each shown, and the decomposition that recovers ten tables.
- [Third normal form, and the three anomalies](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/textbook/01-the-design-region.md#13-third-normal-form-and-the-three-anomalies), the same journey, chapter 1, section 1.3. The written argument: which columns depend on which, the key `(sale, product)`, and what second and third normal form each remove.
- [Third normal form, as functional dependencies](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/03-a3-3nf-math.md), data-engineering/many-sources-one-lakehouse, plan 03. Normal forms written as arrows between attributes, worked on paper against the wide table built in plan 02.
- [Each normalization anomaly, demonstrated live on your rows](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/04-a3-3nf-mech.md), the same journey, plan 04. The three anomalies caused on purpose in a throwaway database holding one wide table.
- [Third normal form, with each anomaly produced live](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/plans/07-third-normal-form.md), ai-engineering/product-data-validation-end-to-end, plan 07. The same move on your own 26 product rows.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the back-of-book index of Systems analysis and design ("Normalization, rules of", "First normal form", "Denormalization") and a page-text search for "normal form" and "denormaliz" across the system design books. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; the Decomplexify video is the one our plans already link. Each plan and chapter was read at its title and description, and the chapter section at its first lines. Bare "normalization" is never an alias: in the learning tree it also means layer, batch and data normalization in machine learning. "Normal form" (84 uses) was sampled and means a database normal form in every sampled line.
