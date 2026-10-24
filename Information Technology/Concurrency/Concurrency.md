---
aliases: [concurrency, concurrent requests, concurrent users, concurrent connections]
standard: vault-note v2
---

# Concurrency

Up: [[Information Technology]]

Information Technology, Concurrency. [[Race Condition]] is the bug concurrency makes possible; [[Throughput]] and [[Latency]] are the two numbers it ties together, and a [[WebSocket]] server is sized by how many connections it holds at once.

**Concurrency is a system making progress on many tasks or requests in overlapping time, switching between them while each waits, whether or not any two run at the same instant (running at the same instant on separate cores is parallelism).**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches concurrency writes the rest around it.
> - This note is also the map note of the Concurrency folder, and it does not list [[Race Condition]] as a child yet.

- [[Race Condition]]: A race condition is a bug whose result depends on the timing of two operations running at once: both read the same value, both act on it, and one write silently overwrites the other, as when two requests book the same date.

## Where to learn this

**Concurrency**, many tasks in progress at once, interleaved while each waits. Also: concurrent requests, concurrent users, concurrent connections.

**Textbooks**

- System design big archive, System Performance Metrics Every Engineer Should Know: [pages 429 to 430](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=429). Works concurrency as a number: 100 requests a second that each take 5 seconds means 500 requests in flight at once, tied together by QPS = concurrency ÷ average response time.
- System design interview, chapter 12, Design a chat system, Scalability: [page 185](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=185). Sizes concurrent connections: 1 million concurrent users at about 10 KB of server memory each is about 10 GB to hold every connection on one box.
- System design big archive, Concurrency is NOT Parallelism: [pages 280 to 281](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=280). Concurrency as tasks overlapping in time on one core through context switching, good for I/O waits, against parallelism as tasks running at once on several cores.
- System design big archive, Things Every Developer Should Know: Concurrency is NOT parallelism: [pages 399 to 400](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=399). Rob Pike's line that concurrency is dealing with many things at once and parallelism is doing many things at once, then where each pays off: I/O-bound against CPU-bound work.

**Videos**

- Gaurav Sen, How 100 milliseconds cost Amazon 3 BILLION DOLLARS: Latency, Concurrency and Parallelism, Concurrency Example, 1:54 to 2:28: [watch](https://www.youtube.com/watch?v=I8FeITQvLAk&t=114s). A worked example of concurrency, followed by one of parallelism and the two put together. Chapter-timed.
- ByteByteGo, Concurrency Vs Parallelism!, Concurrency, 0:13 to 1:03: [watch](https://www.youtube.com/watch?v=RlM9AfWf1WU&t=13s). Concurrency defined before parallelism and practical examples of both. Chapter-timed.
- Hello Interview, Concurrency in Low-level Design Interviews, Coordination: Blocking Queues & Backpressure, 9:52 to 15:59: [watch](https://www.youtube.com/watch?v=d8rmosXttTE&t=592s). Coordinating concurrent workers through a blocking queue, between the chapters on correctness and on semaphores and connection pools. Chapter-timed.

**Our plans and chapters**

- [Reproduce the race against Attica](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/09-reproduce-the-race.md), projects/attica/architecture-decisions, plan 09. Two concurrent accepts fired at the same provider and date against a running Attica, the prediction written down first.
- [Promises, Await, and the Event Loop](/home/molef/goal-setting/learning/frontend-foundations/plans/04-promises-await-and-the-event-loop.md), frontend-foundations, plan 04. Why a log line printed in the wrong order, traced through JavaScript's event loop, which runs concurrent work on one thread.
- [Async Django (ASGI/Channels)](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/03-operations-and-delivery/plans/03-async-django-channels.md), projects/tms-mobility/system-design/plans/03-operations-and-delivery, plan 03. Django Channels stood up so an async view can hold a persistent WebSocket connection.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "concurren" across the system design, AI engineering and language model books; the big archive's sections come from the chapter tables in `Textbooks.md`. AI engineering's "concurrent requests" (page 788) is a provider throttling metric and was left out. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. The bare word "concurrency" (21 lines) was sampled in the learning tree: about 17 of 20 mean this idea or its control in a database; the rest name a load-test setting, close enough to keep. "parallelism" is not an alias: it has 3 lines in the tree, one about recurrent networks, too few to show it means this idea.
