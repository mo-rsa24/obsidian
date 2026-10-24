---
aliases: [database index, database indexing, B-tree index, composite index, secondary index, covering index, clustered index]
standard: vault-note v2
---

# Database Index

Up: [[Database Systems]]

Information Technology, Database Systems. An inverted index is the kind built for words in text, under [[Full-Text Search]]; [[Foreign Key]] columns are among the first a table indexes, so joins stay fast.

**A database index is a separate, sorted structure that maps a column's values to the rows holding them, so a query can jump to matching rows instead of scanning the whole table, at the cost of extra space and slower writes.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches indexing writes the rest around it.

## Where to learn this

**Database index**, a sorted lookup from column values to rows. Also: database indexing, B-tree index, secondary index, clustered index, composite index, covering index.

**Textbooks**

- Systems analysis and design, chapter 11, Indexing: [pages 457 to 458](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=457). Works it on an order table: a payment-type index lets a query for every American Express order find those rows without scanning the table, then the cost (space, and slower inserts and updates) and guidelines such as indexing every primary key and foreign key.
- System design big archive, Database Index Types Every Developer Should Know: [pages 226 to 227](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=226). Three kinds: the primary index made with a primary key (dense or sparse), the clustered index that fixes the rows' physical order, and the secondary index that points back at rows.
- System design big archive, 5 Data Structures That Make DB Queries Super Fast: [pages 240 to 241](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=240). The structures underneath: B-tree and B+ tree for range and point queries, hash for equality only, bitmap for low-cardinality columns, inverted for full-text search.

**Videos**

- Hussein Nasser, what is a database index?, Heap vs index lookup, 2:50 to 4:44: [watch](https://www.youtube.com/watch?v=Jemuod4wKWo&t=170s). Reading rows from the table's heap against finding them through an index, after the chapters on slow searches and what an index is for. Chapter-timed.
- Hello Interview, DB Indexing in System Design Interviews, B-tree index, 2:18 to 4:01: [watch](https://www.youtube.com/watch?v=BHCSL_ZifI0&t=138s). The B-tree index, right after the chapter on the problem with full scans. Chapter-timed.
- ByteByteGo, 7 Must-know Strategies to Scale Your Database, Database indexing, 0:50 to 2:06: [watch](https://www.youtube.com/watch?v=_1IKwnbscQU&t=50s). Indexing as the first way to scale a database. Chapter-timed.

**Our plans and chapters**

- [An index at scale](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/20-index-at-scale.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 20. Works it with numbers: a million-row table queried with and without an index, the milliseconds written down and `EXPLAIN QUERY PLAN` read line by line.
- [Reading a query plan: what the database actually did](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/25-d1-query-plan.md), data-engineering/many-sources-one-lakehouse, plan 25. A sequential scan, an index scan and a join read in DBeaver on a real 834-row table.
- [System Design: Database Design](/home/molef/goal-setting/learning/system-design/database-design/MASTER_PLAN.md), system-design/database-design. Its indexing goal adds an index to a slow query and measures both the faster read and the slower write; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the chapter tables in `Textbooks.md` and a page-text search for "index", "B-tree" and "clustered index" across the system design books. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Hussein Nasser's Database Indexing Explained and B-Tree vs B+Tree in Production Database Systems are members-only and were skipped. Each plan was read at its title and description. Bare "index" is never an alias: in the learning tree it mostly names an index file, a plan index or a back-of-book index.
