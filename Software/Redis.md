---
aliases: [Redis]
standard: vault-note v2
---

# Redis

Up: [[Software]]

Software. Redis is the store most of our plans use as a [[Cache]], and it holds the counters behind a [[Rate Limiter]].

**Redis is an in-memory key-value data store, used as a cache, a counter store, a message broker and sometimes a database, fast because its data lives in RAM.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches Redis writes the rest around it.

## Where to learn this

**Redis**, an in-memory key-value store. Also: Redis cache, redis-cli.

**Textbooks**

- System design interview, chapter 4, Design a rate limiter, High-level architecture: [pages 62 to 63](../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=62). Works Redis as the counter store with its two commands: INCR adds one to a client's counter and EXPIRE sets a timeout that resets it, checked on every request.
- System design big archive, The life of a Redis query: [pages 318 to 319](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=318). Why an in-memory store can lose data on a restart, and Redis's two ways to persist it: the append-only file of every command and periodic RDB snapshots.
- System design big archive, Redis vs Memcached: [page 97](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=97). What Redis's data structures are good for: a hash to count clicks, a sorted set to rank and dedupe users, a bitmap for yes-or-no facts about millions of users.

**Videos**

- Hussein Nasser, Spin up Redis on Docker and learn basic commands, 0:00 to 9:47: [watch](https://www.youtube.com/watch?v=ZkwKyUZWkp4&t=0s). Redis started in a Docker container and driven with its basic commands. Whole video.
- ByteByteGo, What Is Redis Really About? Why Is It So Popular?, Introduction to Redis, 0:00 to 2:36: [watch](https://www.youtube.com/watch?v=z_NbVtbgBJw&t=0s). What Redis is, before the chapters on persistence, scaling it and its common uses. Chapter-timed.
- ByteByteGo, System Design: Why is single-threaded Redis so fast?, Single-threaded architecture, 1:05 to 2:47: [watch](https://www.youtube.com/watch?v=5TRFpFBccQM&t=65s). How one thread serves many clients, after the in-memory design. Chapter-timed.
- Hello Interview, Redis Deep Dive w/ a Ex-Meta Senior Manager, Redis as a User, 1:51 to 5:36: [watch](https://www.youtube.com/watch?v=fmT5nlEkl3U&t=111s). Redis from the caller's side, before its uses as a cache, a rate limiter, a job queue, a leaderboard and pub/sub. Chapter-timed.

**Our plans and chapters**

- [Redis cache-aside, and the stale price](/home/molef/goal-setting/learning/system-design/foundations/plans/17-redis-cache-aside-and-the-stale-price.md), system-design/foundations, plan 17. Redis in Docker Compose holding a product price for 60 seconds, read with `redis-cli TTL`, and the stale price it serves.
- [Redis as a cache](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/21-redis-cache.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 21. Cache-aside on an availability search, with `redis-cli MONITOR` showing every command.
- [Key-Value Store for Live Operator/Rider Location](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/03-operations-and-delivery/plans/04-kv-store-live-location.md), projects/tms-mobility/system-design/plans/03-operations-and-delivery, plan 04. A Redis-backed location store that resolves conflicting concurrent writes, and why Redis suits it.
- [System Design: Caching](/home/molef/goal-setting/learning/system-design/caching/MASTER_PLAN.md), system-design/caching. Opens with an infographic of ten Redis use cases among its sources; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "Redis" across the system design books; neither language model book does more than name Redis. Each video's chapter list was read with `cache-video-chapters.py` (Hussein Nasser's Docker video has none and is cited whole), and each line is described from its chapter title and the video title only. Each plan was read at its title and the lines that name Redis. Left out: Arpit Bhayani's Redis Internals series (building Redis commands from scratch), which sits on [[Time To Live]] for the TTL command; Hussein Nasser's 50-minute Redis In-Memory Database Crash Course, which has two chapters only.
