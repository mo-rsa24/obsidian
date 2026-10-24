---
aliases: [database locking, database lock, optimistic locking, optimistic lock, pessimistic locking, pessimistic lock, row lock, row-level lock, SELECT FOR UPDATE, optimistic concurrency control]
standard: vault-note v2
---

# Database Locking

Up: [[Database Systems]]

Information Technology, Database Systems. Locks are taken inside a [[Database Transaction]], and how strict they must be depends on the [[Isolation Level]] the database runs at.

**Database locking keeps two transactions from changing the same row at once: pessimistic locking takes the lock before reading (`SELECT ... FOR UPDATE`) so the second writer waits, while optimistic locking takes none and instead rejects a write whose row changed since it was read, usually by checking a version column.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches locking writes the rest around it.

## Where to learn this

**Database locking**, keeping concurrent writers off the same row. Also: optimistic locking, pessimistic locking, row lock, row-level lock, SELECT FOR UPDATE, optimistic concurrency control.

**Textbooks**

- Database systems textbook, section 10-3b, Lock types: [pages 525 to 526](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=525). Table 10.12 traces two transactions updating PROD_QOH under a binary lock, so the second cannot read until the first has written, then shared and exclusive locks and the deadlocks locking can cause.
- Database systems textbook, section 10-3a, Lock granularity: [pages 522 to 524](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=522). Locks at the database, table, page, row and field level, each drawn as a time sequence of two transactions, with the overhead row-level locking costs.
- Database systems textbook, section 10-5, Concurrency control with optimistic methods: [pages 529 to 530](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=529). Optimistic concurrency control's read, validation and write phases: updates go to a private copy and are discarded if validation fails.
- Grokking the system design interview, section 11.3, Concurrency: [page 13](../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=13). Works a seat booking where the transaction reads seats 54, 55 and 56 of show 99 and takes a write lock on those rows, so no one else can update them before it commits.
- System design big archive, A Cheatsheet on Database Performance: [pages 46 to 47](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=46). Pessimistic and optimistic locking named as the way to manage concurrency and contention, beside indexing, sharding, denormalisation and replication.
- System design big archive, How SQL Query Executes In A Database?: [pages 202 to 203](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=202). The lock manager inside the storage engine, which acquires the locks a query's plan needs.

**Videos**

- Hussein Nasser, Row-Level Database Locks Explained - (Read vs Exclusive), 0:00 to 8:20: [watch](https://www.youtube.com/watch?v=nuBi2XbHH18&t=0s). Row-level locks and the difference between a read lock and an exclusive one. Whole video.
- Hussein Nasser, All Postgres Locks Explained | A Deep Dive, FOR UPDATE, 30:00 to 33:00: [watch](https://www.youtube.com/watch?v=URwmzTeuHdk&t=1800s). The `FOR UPDATE` row lock in Postgres, the first of four row-lock modes after the table-level locks. Chapter-timed.
- Arpit Bhayani, Optimistic Locking - What, When, Why, and How?, Optimistic locking concept, 3:00 to 4:41: [watch](https://www.youtube.com/watch?v=eMotoFvgdUo&t=180s). Optimistic locking as an idea, after a chapter on the drawbacks of pessimistic locking and before compare-and-swap. Chapter-timed.

**Our plans and chapters**

- [Pessimistic locking: SELECT FOR UPDATE](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/10-pessimistic-lock.md), projects/attica/architecture-decisions, plan 10. Works it on Attica: `select_for_update()` on the availability read, the two-actor test rerun, and the second transaction seen to block instead of fail.
- [Optimistic locking: version column](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/11-optimistic-lock.md), the same journey, plan 11. A version column on the contended row and an update rejected when the version has moved, which moves the failure onto the user, who must retry.
- [Reproduce the race against Attica](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/09-reproduce-the-race.md), the same journey, plan 09. Two concurrent accepts fired at the same provider and date, the rerunnable test every locking mechanism in the journey is checked against.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "optimistic", "pessimistic", "lock" and "for update" across the system design books. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Hussein Nasser's Database Exclusive lock vs Shared Lock is members-only and was skipped. Each plan was read at its title and description. Bare "lock" is never an alias: in the learning tree it also names lock files such as `uv.lock`. The Database systems textbook lines were opened on 2026-10-25: each page was read with pdftotext after the book's back-of-book index ("lock(s)", "pessimistic locking", "row-level lock") and its chapter table.
