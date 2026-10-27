---
aliases: [SQL Join, SQL join, SQL joins, inner join, inner joins, INNER JOIN, left join, left joins, LEFT JOIN, left outer join, outer join, outer joins, natural join, join statement, join statements, join condition]
standard: vault-note v2
---

# SQL Join

Up: [[Database Systems]]

Information Technology, Database Systems. A join follows a [[Foreign Key]] from one table to the table it points at; an [[Object-Relational Mapping]] writes one whenever it pulls a related row in, as Django's `select_related` does.

**A SQL join combines rows of two tables by a condition on their columns, usually a foreign key equal to the other table's key: an inner join keeps only rows that match on both sides, and a left (outer) join keeps every row of the left table, with nulls where the right has no match.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches joins writes the rest around it.

## Where to learn this

**SQL join**, rows of two tables combined by a condition on their columns. Also: inner join, left join, outer join, natural join.

**Textbooks**

- Database systems textbook, section 8-1, SQL Join Operators: [page 367](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=367). Joins PRODUCT to VENDOR through their common V_CODE, the old-style WHERE join, before the operators that replace it.
- Database systems textbook, section 8-1e, Outer Joins: [page 373](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=373). The left and right outer joins that keep unmatched rows, which is what a nullable foreign key needs.
- Database systems textbook, section 8-1b, Natural Join: [page 369](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=369). Joining on the columns two tables share by name, with duplicate columns dropped.
- Database systems textbook, section 8-1d, JOIN ON Clause: [page 371](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=371). Joining on an explicit condition, the form Django's select_related writes.
- System design big archive, The 4 Types of SQL Joins: [page 151](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=151). Inner, left, right and full joins side by side in one page.

**Videos**

- Anton Putra, 6 SQL Joins you MUST know! (Animated + Practice), Inner Join, 2:39 to 5:00: [watch](https://www.youtube.com/watch?v=Yh4CrPHVBdE&t=159s). Two tables joined on a foreign key, animated row by row, after a chapter on primary and foreign keys. Chapter-timed.
- Anton Putra, the same video, Left Join, 5:00 to 5:47: [watch](https://www.youtube.com/watch?v=Yh4CrPHVBdE&t=300s). The unmatched left rows kept with nulls. Chapter-timed.
- Maven Analytics, SQL JOINs, INNER vs LEFT vs RIGHT vs FULL OUTER, Demo, 4:35 to 8:52: [watch](https://www.youtube.com/watch?v=K9Y8P3X45kE&t=275s). The four join types run on real tables after the diagrams. Chapter-timed.

- Caleb Curry, SQLite Introduction, Creating a Join, 18:32 to 21:49: [watch](https://www.youtube.com/watch?v=8Xyn8R9eKB8&t=1112s). A join written in the sqlite3 shell across two tables linked by a foreign key, the chapter after foreign keys. Chapter-timed.

**Our plans and chapters**

- [A join is a filter](/home/molef/goal-setting/learning/ai-engineering/data-agents/plans/13-a-join-is-a-filter.md), ai-engineering/data-agents, plan 13. Predict how many rows survive an inner join from the null count, run it, then run the left join and predict that count too.
- [The null drop: predict it, reproduce it, name it](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/38-the-null-drop.md), ai-engineering/one-business-end-to-end, plan 38. An inner join to `category` silently drops the 509 sale lines of the 4 products with no category, and a left join keeps them.
- [ORM aggregates: revenue by branch, and the discount fan-out](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/16-orm-aggregates-and-the-discount-fan-out.md), ai-engineering/one-business-end-to-end, plan 16. A join written by the ORM repeats a sale's discount once per line, the fan-out reproduced and printed as SQL.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27: each textbook page's text was read with pdftotext, each video's chapter list with cache-video-chapters.py, and each plan's goal paragraph. Bare "join" is not an alias, because the learning tree uses it far more for Python's str.join.
