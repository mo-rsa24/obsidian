---
aliases: [SQLite, sqlite3, SQLite3]
standard: vault-note v2
---

# SQLite

Up: [[Software]]

Software, databases. SQLite is a [[Relational Database]] with no server: Attica's whole database is one SQLite file, backend/main/db.sqlite3.

**SQLite is a relational database engine that runs inside the application as a library and keeps the whole database in one file, with no server process to start: the program reads and writes the file directly through SQL.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches SQLite writes the rest around it.

## Where to learn this

**SQLite**, the relational database in one file with no server. Also: sqlite3.

**Textbooks**

- System design big archive, Databases: [page 109](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=109). Places SQLite among the SQL databases beside Postgres and MySQL in the roadmap of database types.

**Videos**

- Database Dive, What is SQLite?, 0:00 to 0:52: [watch](https://www.youtube.com/watch?v=p2tOmltUh34&t=0s). What SQLite is, how it works with no server, and when to use it, in under a minute. Whole video.
- Caleb Curry, SQLite Introduction, What + why SQLite3, 0:53 to 2:01: [watch](https://www.youtube.com/watch?v=8Xyn8R9eKB8&t=53s). Why a file-backed database, then the sqlite3 shell, dot commands, DDL and DML in the chapters that follow. Chapter-timed.

**Our plans and chapters**

- [Keys and DDL](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/07-keys-and-ddl.md), projects/attica/event-creation, rebuild plan 07. Candidate keys found by hand, then the schema written as DDL and run in sqlite3.
- [State that survives a restart](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/plans/65-state-that-survives-a-restart.md), ai-engineering/prototype-product-data-validation-end-to-end, plan 65. An agent's state kept in a SQLite file so it survives a server restart.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27: the textbook page's text, each video's chapter list read with cache-video-chapters.py, and each plan's goal paragraph. The big archive's page names SQLite in a list and teaches no more than where it sits.
