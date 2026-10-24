---
aliases: [sharding, shard, database sharding, horizontal partitioning, partitioning, partition key, shard key, sharding key]
standard: vault-note v2
---

# Sharding

Up: [[Database Systems]]

Information Technology, Database Systems. [[Database Replication]] copies the same rows to more servers, while sharding splits different rows across them; [[Consistent Hashing]] is the usual way to choose each row's shard.

**Sharding splits one large database into smaller databases called shards, each with the same schema but its own rows, and a partition key decides which shard holds each row.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches sharding writes the rest around it.
> - The placement is unsure. The two best places are `Information Technology/Database Systems/` and `Information Technology/System Design/Scaling/`, beside [[Scalability]].

## Where to learn this

**Sharding**, splitting one database's rows across many servers. Also: shard, horizontal partitioning, partitioning, partition key, shard key.

**Textbooks**

- System design interview, chapter 1, Database scaling: [pages 28 to 30](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=28). Works sharding on a user table with `user_id % 4` choosing one of four shards, then the sharding key, and the problems sharding brings: resharding when a shard fills, a celebrity's hot shard, and joins across shards.
- Grokking the system design interview, section 14, Data partitioning: [pages 16 to 18](../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=16). Four partitioning schemes (hash, list, round robin and composite), then joins, referential integrity and rebalancing on a partitioned database.
- System design interview, chapter 6, Data partition: [pages 93 to 94](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=93). A key-value store partitioned across eight servers with consistent hashing, so data spreads evenly and little moves when a server joins.
- System design big archive, How MongoDB works?: [pages 220 to 221](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=220). A real sharded database: a query router sends each query to the shard its shard key names, config servers hold the routing metadata, and each shard is itself a replica set.

**Videos**

- Hello Interview, Sharding in System Design Interviews, Example, 0:34 to 3:35: [watch](https://www.youtube.com/watch?v=L521gizea4s&t=34s). The worked example that opens a long walk through how to shard and what it costs. Chapter-timed.
- ByteByteGo, 7 Must-know Strategies to Scale Your Database, Database sharding, 6:57 to 8:27: [watch](https://www.youtube.com/watch?v=_1IKwnbscQU&t=417s). Sharding as the last of seven strategies, after indexing, views, denormalisation, vertical scaling, caching and replication. Chapter-timed.
- Gaurav Sen, What is DATABASE SHARDING?, Horizontal Partitioning, 1:59 to 3:20: [watch](https://www.youtube.com/watch?v=5faMjKuB9bc&t=119s). Horizontal partitioning on a whiteboard, the idea sharding is built on. Chapter-timed.
- Hayk Simonyan, Database Replication & Sharding Explained, Shard Keys, 4:55 to 5:45: [watch](https://www.youtube.com/watch?v=jLEp1XI_L6Q&t=295s). Choosing the key that decides each row's shard. Chapter-timed.

**Our plans and chapters**

- [Hash Tables & the Modulo-Sharding Resize Problem](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/01-distributed-systems-primitives/plans/03-hash-tables-resize-problem.md), projects/tms-mobility/system-design/plans/01-distributed-systems-primitives, plan 03. Why sharding by modulo breaks when the server count changes.
- [System Design: Database Design](/home/molef/goal-setting/learning/system-design/database-design/MASTER_PLAN.md), system-design/database-design. The journey that ends on how sharding and replication take a database past one machine; it holds goals and no plans yet.
- [System Design: Scalability](/home/molef/goal-setting/learning/system-design/scalability/MASTER_PLAN.md), system-design/scalability. Sharding as one of the moves that removes a bottleneck as load grows; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the chapter tables in `Textbooks.md` and a page-text search for "shard" and "partition" across the system design books; neither language model book covers sharding. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: Hussein Nasser's Horizontal vs Vertical Database Partitioning and Arpit Bhayani's How GitHub sharded their databases, behind the four above; the Kafka topic partition in data-engineering/many-sources-one-lakehouse plan 16, a different kind of partition. "Partitioning" is in the learning tree 3 times (horizontal partitioning, and an Iceberg table's partitioning by a column, both this idea); bare "partition" (218 uses, most of them the partition function in statistics) is never an alias.
