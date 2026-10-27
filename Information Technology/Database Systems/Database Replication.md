---
aliases: [database replication, replication, replica, read replica, primary-replica, leader-follower, primary and replica, leader and replica, stale read, replication lag]
link-skip: [useful replication, seed replication, isolates replication, GVAE replication, replication of the TC, manages replicas, manual replicas, replicas and autoscaling, rolling updates, three replicas, independent replicas, Walk deployment, smallest replica, cache-aside, crashed mid-write, stale-read bug, stale-read gap, stale read happens, mark the stale read, stale read accepts]
standard: vault-note v2
---

# Database Replication

Up: [[Database Systems]]

Information Technology, Database Systems. [[Sharding]] splits rows across servers, while replication copies the same rows to more of them; a [[Cache]] is a second copy that can fall behind in the same way a replica does.

**Database replication keeps copies of one database on several servers: a primary takes the writes and streams them to replicas that serve reads and can take over if the primary fails.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches replication writes the rest around it.
> - The placement is unsure. The two best places are `Information Technology/Database Systems/` and `Information Technology/System Design/Scaling/`, beside [[Scalability]].

## Where to learn this

**Database replication**, copies of one database on several servers. Also: replication, replica, read replica, primary-replica, leader-follower, replication lag, stale read.

**Textbooks**

- System design interview, chapter 1, Database replication: [pages 11 to 13](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=11). Works the master and slave case: writes go to the master, reads to the more numerous slaves, and what happens when a slave goes offline (reads move) or the master does (a slave is promoted).
- System design interview, chapter 6, Data replication and Consistency: [pages 94 to 96](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=94). Each key copied to N servers along the hash ring, then quorum consensus with numbers: with N = 3, a write needs W acknowledgements and a read R answers, and W + R > N keeps reads current.
- System design interview, chapter 6, CAP theorem: [pages 91 to 92](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=91). Works the stale read on three replicas n1, n2 and n3: a write reaches n3 but not the other two, so they hold stale data, and the system either blocks writes (consistency) or keeps answering reads that may be stale (availability).
- System design big archive, How MongoDB works?: [pages 220 to 221](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=220). A real replica set: one primary for writes, secondaries for reads and availability, and a secondary elected when the primary fails.

**Videos**

- Hayk Simonyan, Database Replication & Sharding Explained, Leader-Follower Replication, 1:02 to 1:28: [watch](https://www.youtube.com/watch?v=jLEp1XI_L6Q&t=62s). One leader taking writes and followers copying it, before leader-leader replication. Chapter-timed.
- ByteByteGo, 7 Must-know Strategies to Scale Your Database, Database replication, 6:00 to 6:57: [watch](https://www.youtube.com/watch?v=_1IKwnbscQU&t=360s). Replication as one of seven ways to scale a database, just before sharding. Chapter-timed.
- Gaurav Sen, Distributed Consensus and Data Replication strategies on the server, Synchronous replication vs. Asynchronous replication, 1:24 to 3:36: [watch](https://www.youtube.com/watch?v=GeGxgmPTe4c&t=84s). Whether a write waits for its copies, drawn on a whiteboard. Chapter-timed.
- Hussein Nasser, All Types of Database Replication Discussed, Streaming replication, 8:21 to 11:39: [watch](https://www.youtube.com/watch?v=aE2UPg3Ckck&t=501s). Streaming replication among the kinds a database offers, from statement-based to synchronous. Chapter-timed.
- KodeKloud, System Design for Beginners (2026), 1:13:01 to 1:19:34: [watch](https://www.youtube.com/watch?v=SE2KF-vxvS0&t=4381s). A primary copying to its replicas, and which reads and writes each one serves. Chapter-timed.
- Hello Interview, CAP Theorem in System Design Interviews, 2:18 to 4:00: [watch](https://www.youtube.com/watch?v=VdrEq0cODu4&t=138s). Choosing between a fresh answer and any answer when a copy has fallen behind, which is the stale read's trade-off. Chapter-timed.

**Our plans and chapters**

- [Primary, replica, and the stale read](/home/molef/goal-setting/learning/system-design/foundations/plans/16-primary-replica-and-the-stale-read.md), system-design/foundations, plan 16. A second PostgreSQL server streams a copy of the first and takes the reads, then is caught answering "my orders" before a new order has reached it.
- [Postgres logical replication and the write-ahead log](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/20-c3-wal.md), data-engineering/many-sources-one-lakehouse, plan 20. The write-ahead log every change goes through first, and logical replication reading it.
- [Replication slots, and the one nobody dropped](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/21-c4-slots.md), the same journey, plan 21. A replication slot keeps every log segment its consumer has not read, and fills the disk when the consumer goes away.
- [System Design: Consistency and Distributed Systems](/home/molef/goal-setting/learning/system-design/consistency-and-distributed-systems/MASTER_PLAN.md), system-design/consistency-and-distributed-systems. Its second mission writes to one replica, reads from another before replication completes to show the stale read, then shows it resolve after the replication delay; it holds goals and no plans yet.
- [System Design: High Availability and Fault Tolerance](/home/molef/goal-setting/learning/system-design/high-availability-and-fault-tolerance/MASTER_PLAN.md), system-design/high-availability-and-fault-tolerance. How replication serves both read scaling and failover; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "replicat" and "replica" across the system design books; neither language model book covers database replication (AI engineering's "replica parallelism" copies a model, and sits on [[Scalability]]). Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; Hussein Nasser's Database Replication Crash Course is members-only and was skipped. Each plan was read at its title and description; the compiled chapter for foundations plan 16 has headings and no text yet. "Replication" (121 uses) and "replica" (248 uses) were sampled in the learning tree: most lines are database replication (logical replication, replication slots, the primary and its replica, replication lag); the `link-skip` phrases cover the research sense in two diffusion journeys ("a useful replication of the TC hypothesis", "seed replication") and Kubernetes pod replicas. "stale read" (36 prose lines in 18 files) and "replication lag" (5 lines) were added on 2026-10-24. "Replication lag" always means a replica behind its primary. "Stale read" means that in system-design/foundations plan 16, consistency-and-distributed-systems and database-design, and something else in two places: a cache serving an outdated value (foundations plan 17 and its diagram prompts, all carrying "cache-aside", and three lines of the caching master plan) and Attica's check-then-act race between two writers (architecture-decisions plan 08, its scaffold and sources). The new `link-skip` phrases cover both. The textbook pages came from a pdftotext search of the system design books for "stale"; the big archive's eventual-consistency entries (pages 135, 249 and 361) are one-line list items and were left out. The KodeKloud and Hello Interview lines come from rows of the video lessons index read by the foundations video pulse the same day.
