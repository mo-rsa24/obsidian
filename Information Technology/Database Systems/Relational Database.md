---
aliases: [relational database, relational database management system, RDBMS, SQL database]
standard: vault-note v2
---

# Relational Database

Up: [[Database Systems]]

Information Technology, Database Systems. Tables in a relational database are tied by [[Foreign Key]] columns and shaped by a [[Database Schema]]; [[Database Transaction]], [[Database Index]] and [[Database Replication]] each describe one part of how it runs.

**A relational database stores data as tables of rows and columns, each table with a primary key, links tables by repeating one table's key in another, and answers SQL queries that join those tables; PostgreSQL, MySQL and Oracle are the common ones.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches relational databases writes the rest around it.

## Where to learn this

**Relational database**, tables of rows joined by keys and queried with SQL. Also: RDBMS, SQL database, relational database management system.

**Textbooks**

- Database systems textbook, section 3-1, A logical view of data: [pages 99 to 101](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=99). The relational model's three parts (relations, integrity rules, operations), then Table 3.1's characteristics of a relational table and Figure 3.1's STUDENT table.
- Systems analysis and design, chapter 11, Relational databases: [pages 437 to 439](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=437). Works it on a Customer table and an Order table with real rows: each table has a primary key, Cust ID repeated in Order links the two, SQL operates on whole tables at once, and tables are joined on their key columns before a query reads them.
- System design interview, chapter 1, Which databases to use?: [page 8](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=8). Relational against non-relational: tables, rows and joins on one side, four NoSQL families without joins on the other, and the cases where a non-relational store is the better choice.
- Grokking the system design interview, section 16, SQL and NoSQL: [pages 19 to 21](../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=19). The differences point by point (storage, schema, querying, scalability, ACID) and when to choose each.
- System design big archive, PostgreSQL 101: The Everything Database: [pages 63 to 64](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=63). One relational database from the inside: PostgreSQL's multiprocess design, with a server process per client connection and ACID guarantees.

**Videos**

- ByteByteGo, How To Choose The Right Database?, Key Points To Consider, 0:22 to 1:12: [watch](https://www.youtube.com/watch?v=kkeFE6iRfMM&t=22s). What to weigh before picking a database. Chapter-timed.
- Hayk Simonyan, 7 Database Types Every Software Engineer Should Know, Relational databases, 0:38 to 7:45: [watch](https://www.youtube.com/watch?v=5coDJ2b4Xuo&t=38s). Relational databases as the first of seven types, before key-value, document, wide-column, graph, search and vector stores. Chapter-timed.
- Hello Interview, Data Modeling in System Design Interviews, Database Options, 3:30 to 14:39: [watch](https://www.youtube.com/watch?v=TUcPS6dsWx4&t=210s). The database choices a design starts from, before modelling the data. Chapter-timed.
- Hussein Nasser, PostgreSQL Internal Architecture Explained, Overview, 1:30 to 3:30: [watch](https://www.youtube.com/watch?v=Q56kljmIN14&t=90s). The overview of a long walk through PostgreSQL's processes, shared buffers and write-ahead log. Chapter-timed.

**Our plans and chapters**

- [Postgres in psql and in DBeaver](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/plans/16-postgres-two-ways.md), ai-engineering/product-data-validation-end-to-end, plan 16. Works it with counts: one database read in the terminal and in a GUI, both giving the same six table counts and four seeded verdict counts.
- [One service: Postgres in Compose, seeded](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/11-b2-one-service.md), data-engineering/many-sources-one-lakehouse, plan 11. The smallest running stack: one Postgres service with a named volume, a published port and an init script.
- [Three services: MySQL and MongoDB beside it](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/12-b3-three-services.md), the same journey, plan 12. Two relational databases and a document store side by side, each with its own client.
- [System Design: Database Design](/home/molef/goal-setting/learning/system-design/database-design/MASTER_PLAN.md), system-design/database-design. The journey that sets SQL against NoSQL as a real trade-off of consistency, schema flexibility and query patterns; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the back-of-book index of Systems analysis and design ("Relational databases", "RDBMSs") and a page-text search for "relational database" and "RDBMS" across the system design books. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. "PostgreSQL" and "Postgres" are not aliases although no note owns them: they appear 1,247 times in the learning tree, a database you install with a version belongs under `Software/` by the vault's tree test, and every one of those mentions would otherwise link to this general card. The Database systems textbook lines were opened on 2026-10-25: each page was read with pdftotext after the book's back-of-book index ("relational model") and its chapter table.
