---
aliases: [race condition, data race, lost update, double booking, double-booking, check-then-act, read-modify-write]
standard: vault-note v2
---

# Race Condition

Up: [[Concurrency]]

Information Technology, Concurrency. A race condition is the failure [[Concurrency]] makes possible; a [[Database Transaction]] at a strict enough [[Isolation Level]], a lock or a unique constraint is how a design closes it, and [[Idempotency]] closes the related case of one request arriving twice.

**A race condition is a bug whose result depends on the timing of two operations running at once: both read the same value, both act on it, and one write silently overwrites the other, as when two requests book the same date.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches race conditions writes the rest around it.

## Where to learn this

**Race condition**, two operations interleave and one silently undoes the other. Also: data race, lost update, double booking, check-then-act, read-modify-write.

**Textbooks**

- System design interview, chapter 4, Design a rate limiter, Race condition: [page 66](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=66). Works it with numbers: the counter in Redis is 3, two requests both read 3 before either writes, both write 4, and the right answer was 5; locks fix it but slow the system, so a Lua script or a sorted set is used instead.
- Grokking the system design interview, section 11.3, Concurrency: [page 13](../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=13). Keeps two users from booking the same seat with a serializable transaction that reads the seats and locks them before updating them, with the SQL written out.

**Videos**

- Hello Interview, Concurrency in Low-level Design Interviews, Motivating Example, 1:11 to 3:23: [watch](https://www.youtube.com/watch?v=d8rmosXttTE&t=71s). The concrete case the rest of the video fixes, from a staff engineer. Chapter-timed.
- Hello Interview, Concurrency in Low-level Design Interviews, Correctness: Check-Then-Act & Read-Modify-Write, 3:23 to 9:52: [watch](https://www.youtube.com/watch?v=d8rmosXttTE&t=203s). The two shapes most race conditions take, named in the chapter title. Chapter-timed.
- Hello Interview, Why Shopify Moved Inventory Reservations from Redis to MySQL, Making it atomic with a Lua script, 4:14 to 5:44: [watch](https://www.youtube.com/watch?v=CheTuMvFXwc&t=254s). A real reservation system closing its race with a Lua script in Redis, the same fix System design interview names for the rate limiter, before the move to MySQL and row contention. Chapter-timed.
- Hussein Nasser, Concurrent Requests and Unique Keys on Web Applications, Spice things up, 3:33 to 8:29: [watch](https://www.youtube.com/watch?v=w6GzQa9R7-4&t=213s). The last part of a hands-on demonstration of concurrent requests against a table with a unique key, after creating the table, inserting a row and starting a transaction. Chapter-timed.

**Our plans and chapters**

- [Trace a two-actor race by hand](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/08-trace-the-race.md), projects/attica/architecture-decisions, plan 08. Two accept requests drawn on paper as interleaved steps against one free date, ending in the state where both wrongly succeed.
- [Reproduce the race against Attica](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/09-reproduce-the-race.md), the same journey, plan 09. Two concurrent accepts fired at the same provider and date against a running Attica, the prediction written down first; the script is the test every later fix is judged by.
- [Pessimistic locking: SELECT FOR UPDATE](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/10-pessimistic-lock.md), the same journey, plan 10. `select_for_update()` on the availability read, and the second transaction blocks instead of failing.
- [Optimistic locking: version column](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/11-optimistic-lock.md), the same journey, plan 11. A version column rejects an update whose version has moved, and the losing user must retry.
- [The constraint as the enforcer](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/12-constraint-as-enforcer.md), the same journey, plan 12. Two concurrent transactions insert the same provider and date, and the unique constraint rejects the loser at commit time, the fix already in Attica's code.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page was read with pdftotext after a page-text search for "race condition", "lost update", "double book" and "concurren" across the system design, AI engineering and language model books; only these two pages work the problem. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: Hussein Nasser's How to Avoid Double Booking and Race Conditions in Online Web Applications, which is members-only and whose chapter list could not be read; Hello Interview's Design Ticketmaster, whose deep dives (35:18 to 58:10) are not titled by topic. "double booking" was sampled in the learning tree: all 13 lines name this failure in the Attica booking flow.
