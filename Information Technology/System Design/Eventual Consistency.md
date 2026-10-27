---
aliases: [eventual consistency, eventually consistent, eventual consistency model]
standard: vault-note v2
---

# Eventual Consistency

Up: [[System Design]]

Information Technology, System Design. Stale reads under eventual consistency come from [[Database Replication]] lag, and a [[Cache]] is eventually consistent with the database behind it. The placement is unsure: this note may move into a consistency folder beside the [[Saga Pattern]], or into Database Systems.

**Eventual consistency is the guarantee that once writes stop, every replica converges to the same value, while a read made before then may return an older value from a replica that has not caught up.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches eventual consistency writes the rest around it.

## Where to learn this

**Eventual consistency**, replicas that agree only after the updates have spread, so a read can be stale for a while. Also: eventually consistent, eventual consistency model.

**Textbooks**

- System design interview, chapter 6, Design a key-value store, Consistency models: [pages 95 to 96](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=95). Works the numbers first (with N = 3 replicas, W + R > N guarantees strong consistency, such as W = R = 2), then sets strong, weak and eventual consistency side by side and recommends eventual, as Dynamo and Cassandra use.
- System design interview, chapter 6, CAP theorem: [pages 90 to 91](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=90). Three replicas n1, n2 and n3 with n3 cut off by a partition, and the choice it forces between refusing writes and serving stale data.
- System design interview, chapter 6, Inconsistency resolution: versioning: [page 97](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=97). Two servers change the same name at once on two replicas, the conflict eventual consistency lets in, and vector clocks to detect it.
- System design big archive, How CQRS Works?: [pages 218 to 219](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=218). A read database kept eventually consistent with the write database through events applied asynchronously.
- System design interview, chapter 15, Design Google Drive, High consistency requirement: [page 256](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=256). Memory caches are eventually consistent by default, and what the design does to get strong consistency for file metadata instead.

**Videos**

- ByteByteGo, CAP Theorem Simplified, Social Media Example, 2:47 to 3:25: [watch](https://www.youtube.com/watch?v=BHqjEjzAicA&t=167s). A social media feed as the case where a stale read is acceptable, after the ATM case where it is not. Chapter-timed.
- ByteByteGo, CAP Theorem Simplified, ATM System Example, 1:22 to 2:47: [watch](https://www.youtube.com/watch?v=BHqjEjzAicA&t=82s). An ATM as the case that needs consistency over availability. Chapter-timed.
- Hello Interview, CAP Theorem in System Design Interviews, Choosing availability, 5:36 to 7:11: [watch](https://www.youtube.com/watch?v=VdrEq0cODu4&t=336s). Designing for availability over consistency. Chapter-timed.
- Hello Interview, CAP Theorem in System Design Interviews, Consistency vs availability, 2:18 to 4:00: [watch](https://www.youtube.com/watch?v=VdrEq0cODu4&t=138s). Choosing between a fresh answer and any answer. Chapter-timed.
- Gaurav Sen, Data Consistency and Tradeoffs in Distributed Systems, Data Copies, 7:10 to 12:01: [watch](https://www.youtube.com/watch?v=m4q7VkgDWrM&t=430s). Copies of the data on several nodes and the disagreements they bring, before two-phase commit. Chapter-timed.
- Gaurav Sen, Data Consistency and Tradeoffs in Distributed Systems, Eventual Consistency, 25:00 to 25:42: [watch](https://www.youtube.com/watch?v=m4q7VkgDWrM&t=1500s). Eventual consistency as the closing alternative to two-phase commit. Chapter-timed.

**Our plans and chapters**

- [System Design: Consistency and Distributed Systems](/home/molef/goal-setting/learning/system-design/consistency-and-distributed-systems/MASTER_PLAN.md), system-design/consistency-and-distributed-systems. Goal 2: write to one replica, read from another before replication completes, show the stale read, then show it resolve; it holds goals and no plans yet.
- [Distributed Systems Basics](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/01-distributed-systems-primitives/plans/02-distributed-systems-basics.md), projects/tms-mobility/system-design/plans/01-distributed-systems-primitives, plan 02. Gaurav Sen's consistency video watched, then the strong or eventual choice made for TMS booking state against live location, each with a failure scenario.
- [Panel 5: Consistency Model](/home/molef/goal-setting/learning/system-design/applications/how-aws-s3-works/sources/how-aws-s3-works/topics/05-consistency-model.md), system-design/applications/how-aws-s3-works, source topic 05. S3's read-after-write strong consistency, and the eventual consistency for overwrites and deletes it had until December 2020.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "eventual consistency", "eventually consistent", "consistency model" and "strong consistency" across the system design books. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title, the video title and, for the Hello Interview lines, the segment notes in `system-design/foundations/video-scout/pulse-2026-10-24.md`. Each plan was read at its title and goals, and the source topic in full. Left out: the big archive's pages 90, 114 to 115, 135, 190 to 191, 249 and 361, which name eventual consistency in passing; Hussein Nasser's Can you get Eventual Consistency in Relational Databases?, members-only; the lecture-map row on consistency models in CME296, a generative-models idea with the same name. "Consistency model" is not an alias for that reason. The aliases are multi-word, so no ordinary-word sampling was needed.
