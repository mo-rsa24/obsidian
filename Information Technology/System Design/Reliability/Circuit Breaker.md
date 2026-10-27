---
aliases: [circuit breaker, circuit breaking]
standard: vault-note v2
---

# Circuit Breaker

Up: [[Reliability]]

Information Technology, System Design. It stops the calls a [[Timeout]] would otherwise wait on and a [[Retry With Backoff]] would repeat, and an [[API Gateway]] is a common place to run one.

**A circuit breaker sits in front of calls to another service and counts failures; past a threshold it trips open and fails every call at once without sending it, then after a pause lets a trial call through and closes again if that call succeeds, so one failing service cannot drag its callers down with it.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches circuit breakers writes the rest around it.

## Where to learn this

**Circuit breaker**, failing fast instead of waiting on a service that is down. Also: circuit breaking.

**Textbooks**

- System design big archive, How can Cache Systems go wrong?: [pages 246 to 247](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=246). Case 4, a cache crash: a circuit breaker stops the application services reaching the cache or the database while the cache is down, set against running the cache as a cluster.
- System design big archive, What does API gateway do?: [pages 10 to 11](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=10). Steps 9 to 12 of one request through a gateway, where faults that take longer to recover are handled by circuit breaking, beside logging and caching.

**Videos**

- Hello Interview, Networking Essentials for System Design Interviews w/ Ex Meta Senior Manager, Cascading Failures and Circuit Breakers, 1:00:15 to 1:04:35: [watch](https://www.youtube.com/watch?v=SHkbPm1Wrno&t=3615s). One slow server dragging its callers down, then the breaker explained through the one in a house: it trips past a failure level, fails fast, and resets once the server answers in time again, with an alarm on every trip. Caption-read.
- ByteByteGo, Top 7 Most-Used Distributed System Patterns, Circuit Breaker, 0:58 to 1:38: [watch](https://www.youtube.com/watch?v=nH4qjmP2KEE&t=58s). The pattern as the first of seven, before CQRS and event sourcing. Chapter-timed.

**Our plans and chapters**

- [System Design: API Gateways](/home/molef/goal-setting/learning/system-design/api-gateways/MASTER_PLAN.md#goals), system-design/api-gateways. Goal 4: a circuit breaker at the gateway, shown tripping when a backend service fails and recovering after; it holds goals and no plans yet.
- [Fault Tolerance & Redundancy](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/03-operations-and-delivery/plans/05-fault-tolerance-redundancy.md), projects/tms-mobility/system-design/plans/03-operations-and-delivery, plan 05. A breaker that opens after N consecutive failures and half-opens after a cooldown, checked failing fast while open, with its state transitions plotted.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search of the five system design books for "circuit break", which found only these two pages; no back-of-book table has the term. The Hello Interview chapter was read in its captions (yt-dlp) and its chapter list; the ByteByteGo chapter from its chapter list with `cache-video-chapters.py`, described from the chapter and video titles only. Each plan was read at its title and the lines that name the breaker. Left out: Gaurav Sen's How to avoid cascading failures in a distributed system (`xrizarXJgC8`), whose Cascading Failure chapter does not name a breaker and whose captions were not read; foundations plan 14, which lists the Hello Interview chapter in its video table but teaches the timeout, not the breaker; and the agent-architecture reference diagram's Layer 7, which names a circuit breaker among five mechanisms without teaching it.
