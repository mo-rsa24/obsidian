---
aliases: [foreign key, primary key, foreign key constraint, composite primary key, referential integrity]
standard: vault-note v2
---

# Foreign Key

Up: [[Database Systems]]

Information Technology, Database Systems. Keys are what tie the tables of a [[Relational Database]] together, [[Database Normalization]] decides which table each column belongs in, and a [[Database Index]] on a foreign key keeps joins fast.

**A primary key is the column, or set of columns, whose value is different in every row of a table; a foreign key is that primary key copied into another table, so each row there points at exactly one row of the first, and the database refuses a pointer to a row that does not exist.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches keys writes the rest around it.

## Where to learn this

**Foreign key**, a column pointing at another table's primary key. Also: primary key, foreign key constraint, composite primary key, referential integrity.

**Textbooks**

- Database systems textbook, section 3-2b, Types of keys: [pages 105 to 106](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=105). Defines the foreign key on Figure 3.2's rows: VEND_CODE, the primary key of VENDOR, placed in PRODUCT, then referential integrity as every foreign key entry being null or a valid primary key value, and Table 3.3 setting the foreign key beside superkey, candidate, primary and secondary keys.
- Database systems textbook, section 3-3, Integrity rules: [pages 106 to 107](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=106). Table 3.4's entity and referential integrity rules, worked on the CUSTOMER and AGENT tables of Figure 3.3, where customer 10013 has a null AGENT_CODE because no agent is assigned yet.
- Database systems textbook, section 7-2, Data definition commands: [pages 283 to 288](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=283). The foreign key in SQL: `FOREIGN KEY (V_CODE) REFERENCES VENDOR ON UPDATE CASCADE` on PRODUCT, then the LINE table's composite primary key `(INV_NUMBER, LINE_NUMBER)` with `ON DELETE CASCADE` back to INVOICE, so deleting an invoice deletes its lines.
- Database systems textbook, section 3-2b, Types of keys: [pages 103 to 104](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=103). Composite key, superkey and candidate key worked on the STUDENT table, ending with the primary key as the candidate key chosen and entity integrity's two requirements.
- Systems analysis and design, chapter 11, Relational databases: [pages 437 to 438](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=437). Works it on real rows: Cust ID is the primary key of a Customer table and a foreign key in an Order table (order 234 belongs to customer 4254), Payment Type is a foreign key into a lookup table, and referential integrity means every Cust ID in Order must first exist in Customer.
- Systems analysis and design, chapter 11, Moving from logical to physical data models: [pages 445 to 447](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=445). Adding primary keys (unique per row, a system-generated `cust_id` where nothing natural fits) and then foreign keys, copied from the table on the "one" end of a relationship to the table on the "many" end.
- System design interview, chapter 12, Data models: [pages 187 to 188](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=187). A chat system's message tables: `message_id` as the primary key for one-to-one chat, and the composite primary key `(channel_id, message_id)` for group chat.

**Videos**

- Hussein Nasser, Primary Key vs Secondary Key - What you probably didn't know, Primary keys and clustering, 2:39 to 8:01: [watch](https://www.youtube.com/watch?v=PQcIfqE85Co&t=159s). What a primary key does to how rows are stored, after a chapter on the heap. Chapter-timed.
- CockroachDB, What is a Foreign Key Constraint? Understanding Primary & Foreign Keys, What is a foreign key?, 1:19 to 2:02: [watch](https://www.youtube.com/watch?v=5kiMg7GXAsY&t=79s). The foreign key defined, after a chapter on the primary key and before one on what foreign keys do. Chapter-timed.

**Our plans and chapters**

- [The entity diagram from sentence tests, the foreign key on the many side, the optional relationship drawn](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/04-the-entity-diagram.md), ai-engineering/one-business-end-to-end, plan 04. Works it on the shop's ten tables: each relationship tested as a sentence both ways ("a sale has many lines") and the foreign key placed on the many side.
- [Superkeys and candidate keys: could two rows share this?](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/05-candidate-keys.md), the same journey, plan 05. For every table, which columns no two rows could ever share, the primary key chosen from them, and the one place the obvious natural key fails.
- [The ERD, and why the foreign key sits on the many side](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/06-a5-erd.md), data-engineering/many-sources-one-lakehouse, plan 06. The design drawn by hand with crow's feet and the foreign key column on the side that holds many rows.
- [Database constraints: UNIQUE, CHECK, NOT NULL, foreign keys](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/03-constraints.md), projects/attica/architecture-decisions, plan 03. A constraint violation forced in a shell to watch what the database raises.
- [The foreign keys that stop being enforced](/home/molef/goal-setting/learning/ai-engineering/genie-on-databricks/plans/08-b4-unenforced-keys.md), ai-engineering/genie-on-databricks, plan 08. Postgres enforced the foreign keys; Unity Catalog lets you declare them and enforces nothing, and the plan names what that stops protecting.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the back-of-book index of Systems analysis and design ("Foreign keys", "Primary keys") and a page-text search for "foreign key" and "primary key" across the system design books. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; the CockroachDB video is the one our plans already link. Each plan was read at its title and description. The Database systems textbook lines were opened on 2026-10-25: each page was read with pdftotext after the book's back-of-book index ("foreign key", "primary keys", "referential integrity", "composite key") and its chapter table.
