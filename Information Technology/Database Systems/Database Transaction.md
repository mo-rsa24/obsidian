---
aliases: [database transaction, transaction, ACID, ACID transaction, ACID transactions, commit and rollback, BEGIN and COMMIT, atomicity]
link-only-in: [system-design, projects/attica]
standard: vault-note v2
---

# Database Transaction

Up: [[Database Systems]]

Information Technology, Database Systems. [[Isolation Level]] says what one transaction may see of another that runs beside it, and [[Database Locking]] is how a database keeps two of them off the same row.

**A database transaction groups several reads and writes into one unit that either commits as a whole or rolls back as if it never ran, and ACID names the four promises it keeps: atomicity, consistency, isolation and durability.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches transactions writes the rest around it.

## Where to learn this

**Database transaction**, writes that commit together or not at all. Also: ACID, ACID transaction, commit and rollback, BEGIN and COMMIT, atomicity.

**Textbooks**

- Grokking the system design interview, section 11.3, Concurrency: [page 13](../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=13). Works a ticket booking as one SQL transaction: `BEGIN TRANSACTION`, check that seats 54, 55 and 56 of show 99 are still free, update the seat and booking rows, then `COMMIT`, so no two users can book the same seat.
- Grokking the system design interview, section 16, SQL and NoSQL: [pages 20 to 21](../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=20). ACID spelled out as atomicity, consistency, isolation and durability, and ACID compliance as the reason to pick a relational database for e-commerce and financial work.
- System design interview, chapter 15, Design Google Drive: [page 256](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=256). A design that chooses a relational database for its file metadata because ACID comes built in, where a NoSQL store would need it written into the sync logic.
- System design big archive, How SQL Query Executes In A Database?: [pages 202 to 203](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=202). Where transactions live inside a database: the storage engine's transaction manager, lock manager and recovery manager, which handles rollback.

**Videos**

- Hussein Nasser, Relational Database ACID Transactions (Explained by Example), What is a Transaction?, 2:00 to 4:30: [watch](https://www.youtube.com/watch?v=pomxJOFVcQs&t=120s). The opening definition of a long walk through each ACID letter with examples. Chapter-timed.
- Hussein Nasser, What is a Database transaction?, 0:00 to 2:52: [watch](https://www.youtube.com/watch?v=P80Js_qClUE&t=0s). The idea in under three minutes. Whole video.
- ByteByteGo, ACID Properties in Databases With Examples, Atomicity explained, 0:19 to 1:00: [watch](https://www.youtube.com/watch?v=GAe5oB742dw&t=19s). Atomicity, the all-or-nothing property, as the first of the four letters. Chapter-timed.
- Hayk Simonyan, SQL Transactions and ACID Properties, SQL Transactions and ACID Properties, 0:25 to 2:50: [watch](https://www.youtube.com/watch?v=LoxO-P7hhUQ&t=25s). Transactions in SQL and the four ACID properties, before the video turns to isolation. Chapter-timed.

**Our plans and chapters**

- [What a transaction is: atomicity, commit, rollback](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/04-transactions.md), projects/attica/architecture-decisions, plan 04. Works it on Attica: two writes wrapped in `transaction.atomic()`, a rollback forced, then the same two writes without it to compare what survives.
- [The booking-request transaction](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/14-booking-request-transaction.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 14. One click writes four rows (booking request, audit log, outbox event, notification) in a single transaction.
- [The outbox, the queue and the worker](/home/molef/goal-setting/learning/system-design/foundations/plans/19-outbox-queue-and-worker.md), system-design/foundations, plan 19. The order and its "order placed" event written in one transaction, then published to RabbitMQ by a relay.
- [Server-side SQL: net revenue defined once, amount kept honest by a trigger, a refund recorded atomically](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/08-functions-triggers-and-a-procedure.md), ai-engineering/one-business-end-to-end, plan 08. A stored procedure that records a refund and its effects atomically.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "transaction", "ACID" and "rollback" across the system design books. Systems analysis and design was searched too: its "transaction" entries are transaction files and transaction processing systems, a different idea, so it has no line. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description; the compiled chapter for foundations plan 19 has headings and no text yet, so the plan is cited. Left out: Hussein Nasser's two-phase commit videos, which belong to distributed transactions. Bare "transaction" was sampled in the learning tree (784 uses; 25 sampled, about 15 meaning a database transaction and 10 a bank or till transaction, the vehicle of the data-engineering, data-agents and Genie journeys), so `link-only-in` limits it, and "atomicity", to the system design and Attica journeys, where it means this idea.
