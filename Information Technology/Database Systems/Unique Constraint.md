---
aliases: [UNIQUE constraint, unique constraint, unique index, uniqueness constraint, unique composite index, composite unique constraint, UniqueConstraint]
standard: vault-note v2
---

# Unique Constraint

Up: [[Database Systems]]

Information Technology, Database Systems. Declaring a primary key, under [[Foreign Key]], creates the same unique index; the database enforces the constraint through a [[Database Index]] whose keys may each point at one row only, which is how it can close a [[Race Condition]] that a check in application code leaves open.

**A unique constraint makes the database refuse a second row with the same value, or the same combination of values, in the columns it names; the database enforces it through a unique index, so the refusal holds even when two transactions insert at the same moment, and Attica uses one on `(provider, date)` as its guard against booking one provider twice on one day.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches constraints writes the rest around it.

## Where to learn this

**Unique constraint**, a refusal of a second row with the same values in the named columns. Also: UNIQUE constraint, unique index, unique composite index, composite unique constraint, uniqueness constraint, Django's `UniqueConstraint`.

**Textbooks**

- Database systems textbook, section 7-2f, SQL constraints: [page 288](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=288). Works it on the LINE table: the primary key is `(INV_NUMBER, LINE_NUMBER)`, and `CONSTRAINT LINE_UI1 UNIQUE(INV_NUMBER, P_CODE)` stops one product being ordered twice on one invoice, with the sentence that a UNIQUE constraint is enforced through a unique index.
- Database systems textbook, section 7-2g, SQL indexes: [pages 289 to 290](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=289). `CREATE UNIQUE INDEX P_CODEX ON PRODUCT(P_CODE)` and the "duplicate value in index" error it raises, then Table 7.5's duplicated test record, where employee 111's WEA test passes the primary key yet repeats, and the unique composite index on `(EMP_NUM, TEST_CODE, TEST_DATE)` that would have refused it.
- Database systems textbook, section 7-2f, SQL constraints: [pages 286 to 287](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=286). UNIQUE in the ANSI list beside NOT NULL, DEFAULT and CHECK, then `CONSTRAINT CUS_UI1 UNIQUE (CUS_LNAME, CUS_FNAME)` on CUSTOMER, which refuses two customers with the same first and last name, and the book's own warning that two John Smiths should be allowed.
- Database systems textbook, section 3-8, Indexes: [page 130](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=130). Defines a unique index as one whose key has only one pointer to a row, says declaring a primary key creates one automatically, and contrasts Figure 3.31's PAINTER_NUM index, where painter 123 points at three rows.

**Videos**

- Hussein Nasser, Concurrent Requests and Unique Keys on Web Applications, Duplicate a key, 1:54 to 2:15: [watch](https://www.youtube.com/watch?v=w6GzQa9R7-4&t=114s). A second insert of the same key refused on a live table, right after the table is created and its first row inserted. Chapter-timed.
- Hussein Nasser, Concurrent Requests and Unique Keys on Web Applications, Spice things up, 3:33 to 8:29: [watch](https://www.youtube.com/watch?v=w6GzQa9R7-4&t=213s). The same key inserted from concurrent transactions, which the video's description says the database still refuses to duplicate. Chapter-timed.
- Hello Interview, System Design Mock Interview: Design Yelp w/ Meta Staff Engineer, Deep dive: constraints, 29:29 to 32:52: [watch](https://www.youtube.com/watch?v=yz1jtze4qr8&t=1769s). One review per user per business held by a composite unique constraint at the database, the moment Attica's architecture-decisions sources place at 29:40 to 30:20. Chapter-timed.
- ritvikmath, SQL Constraints : Data Science Code, 0:00 to 6:30: [watch](https://www.youtube.com/watch?v=1LQd2VHicTU&t=0s). SQL constraints and how to use them to organise tables, described from the title and description only. Whole video.

**Our plans and chapters**

- [Database constraints: UNIQUE, CHECK, NOT NULL, foreign keys](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/03-constraints.md), projects/attica/architecture-decisions, plan 03. Reads `unique_provider_date` in Attica's models and forces a duplicate insert in a shell, predicting the `IntegrityError` before running it.
- [The constraint as the enforcer](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/12-constraint-as-enforcer.md), the same journey, plan 12. Two concurrent transactions insert the same provider and date, the constraint rejects the loser at commit time, and the plan asks what the API should return to it.
- [The Idempotency-Key header](/home/molef/goal-setting/learning/system-design/foundations/textbook/02-the-api-contract-on-paper.md#23-the-idempotency-key-header), system-design/foundations, chapter 2, section 2.3. `\d payments.payments` in psql shows `"payments_idempotency_key_key" UNIQUE CONSTRAINT, btree (idempotency_key)`, the rule that keeps a retried payment at one row.
- [CREATE TABLE with keys and types](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/plans/03-sql-ddl.md), ai-engineering/product-data-validation-end-to-end, plan 03. A repeated primary key is refused with `duplicate key value violates unique constraint`, the error that shows a primary key is held by a unique index.
- [The DDL, written and run](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/07-a6-ddl.md), data-engineering/many-sources-one-lakehouse, plan 07. Task 1.3 declares a unique constraint on the candidate key chosen in plan 05.
- [Attica's chat models](/home/molef/Work/attica/backend/main/chat/models.py), `ProviderAvailability`, lines 223 to 251. `UniqueConstraint(fields=['provider', 'date'], name='unique_provider_date')`, the guard against two bookings for one provider on one day.
- [Attica's scheduling models](/home/molef/Work/attica/backend/main/scheduling/models.py), `IdempotencyRecord`, lines 546 to 564. `UniqueConstraint(fields=["owner", "endpoint", "key"])`, so one user's retry of one endpoint with one idempotency key finds the stored response instead of writing a second row.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-25. Each textbook page was read with pdftotext after the book's back-of-book index ("unique index") and a page-text search for "UNIQUE constraint", "unique index" and "uniqueness constraint" across the shelf; the other books' hits on those words ("each company has its unique constraints", "a unique solution") use "unique" in its everyday sense and were left out. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title, the video title and its description only. Hussein Nasser's How to Avoid Double Booking and Race Conditions in Online Web Applications is members-only and was skipped. Each plan and chapter was read at its title and the lines that use the constraint, and Attica's two models were read in the working tree at commit `3b28ee3`. Bare "unique" is never an alias: in the learning tree it mostly means distinct, as in "unique SKUs" or "a unique solution".
