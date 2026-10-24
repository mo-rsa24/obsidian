---
aliases: [isolation level, transaction isolation, transaction isolation level, read committed, read uncommitted, repeatable read, serializable isolation, snapshot isolation]
standard: vault-note v2
---

# Isolation Level

Up: [[Database Systems]]

Information Technology, Database Systems. Isolation is the I in a [[Database Transaction]]'s ACID; [[Database Locking]] is one way a database enforces the stricter levels.

**An isolation level says how much one running transaction may see of another's uncommitted or newly committed work: read uncommitted, read committed, repeatable read and serializable each forbid one more anomaly (dirty reads, non-repeatable reads, phantom reads) than the level before.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches isolation levels writes the rest around it.

## Where to learn this

**Isolation level**, how much concurrent transactions see of each other. Also: transaction isolation, read committed, repeatable read, serializable isolation, snapshot isolation.

**Textbooks**

- Grokking the system design interview, section 11.3, Concurrency: [page 13](../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=13). Works a seat booking under `SET TRANSACTION ISOLATION LEVEL SERIALIZABLE`: serializable is the highest level and rules out dirty, non-repeatable and phantom reads, and rows read inside the transaction take a write lock so nobody else can update them.

**Videos**

- Hussein Nasser, Serializable vs Repeatable Read Isolation Level, Demo in Postgres, 3:00 to 8:18: [watch](https://www.youtube.com/watch?v=KoULlXKK1H8&t=180s). The two strictest levels compared, then shown in a running Postgres. Chapter-timed.
- Hussein Nasser, Relational Database ACID Transactions (Explained by Example), Isolation Levels vs Read phenomena Table, 25:00 to 27:45: [watch](https://www.youtube.com/watch?v=pomxJOFVcQs&t=1500s). The table of which read phenomenon each level allows, after chapters on dirty, non-repeatable and phantom reads and on each level in turn. Chapter-timed.
- ByteByteGo, ACID Properties in Databases With Examples, Phantom reads and levels, 3:24 to 4:00: [watch](https://www.youtube.com/watch?v=GAe5oB742dw&t=204s). Phantom reads and the isolation levels, after dirty and non-repeatable reads. Chapter-timed.
- Arpit Bhayani, Everything you need to know about Read Uncommitted Isolation Level, Read Uncommitted Isolation Level, 1:24 to 2:37: [watch](https://www.youtube.com/watch?v=AiPGbVjl3JY&t=84s). The weakest level on its own, before chapters on the reads it lets through and when anyone would choose it. Chapter-timed.

**Our plans and chapters**

- [Isolation levels and what each permits](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/06-isolation-levels.md), projects/attica/architecture-decisions, plan 06. The four standard levels listed on paper with the one anomaly each permits, then the level your own database actually runs at, predicted first and checked.
- [Attica Architecture Decisions: the bid-accept mechanism](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/MASTER_PLAN.md), projects/attica/architecture-decisions. The journey whose locking arguments all rest on which anomalies the running level permits, attached to the one row two concurrent accepts fight over.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The textbook page was read with pdftotext after a page-text search for "isolation", "read committed", "repeatable read", "serializ" and "phantom" across the system design books and AI engineering; Grokking's page 13 is the only shelf page that teaches the levels (the big archive names isolation levels once, in a learning map, with no teaching). Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; Hayk Simonyan's SQL Transactions and ACID Properties (chapter "Isolation Layers", 2:50 to 4:48) also covers the levels and was left out to keep the list short. Each plan was read at its title and description. Bare "serializable" is never an alias: the learning tree uses it 4 times in prose lines, twice for a serializable transaction and twice in a "not JSON serializable" error.
