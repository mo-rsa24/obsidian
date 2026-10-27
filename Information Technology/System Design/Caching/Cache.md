---
aliases: [cache, caching, cache hit, cache miss, cache-aside, cache invalidation, write-through cache]
link-skip: [from the earlier cache, captions cache, video cache, term index cache, claude/cache]
standard: vault-note v2
---

# Cache

Up: [[Caching]]

Information Technology, System Design. [[KV Cache]] is the cache a language model keeps of its own attention keys and values; [[Time To Live]] and [[Content Delivery Network]] sit beside this note.

**A cache is a small, fast store that keeps copies of data read often, so a repeated request is answered without going back to the slower place the data lives.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches caching writes the rest around it.

## Where to learn this

**Cache**, a fast copy in front of a slow store. Also: caching, cache hit, cache miss, cache-aside, cache invalidation, write-through cache.

**Textbooks**

- Computer networking: a top-down approach, section 2.2.5, Web caching: [pages 140 to 145](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=140). A web cache, or proxy server, in front of an institution's 15 Mbps access link worked with numbers: 15 requests a second for 1 Mbit objects load the link to traffic intensity 1, and a cache with a hit rate of 0.4 brings it down to 0.6 without buying a faster link, then the conditional GET that keeps cached copies fresh.
- System design interview, chapter 1, Cache: [pages 15 to 16](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=15). Walks one web request through a cache tier (check the cache, on a miss query the database and store the answer), then the expiration policy, keeping cache and database consistent, the cache as a single point of failure, and LRU eviction.
- Grokking the system design interview, section 13, Caching: [pages 15 to 16](../../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=15). The three invalidation schemes (write-through, write-around and write-back), each with what it costs on a write or a later miss, then six eviction policies.
- AI engineering, chapter 10, Step 4, Reduce latency with caches: [pages 871 to 874](../../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=871). Exact caching and semantic caching of model answers, how long to keep a query, and how a cached answer can leak one user's data to another.
- System design big archive, Where do we cache data?: [pages 301 to 302](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=301). The eight places a typical architecture caches, from the browser and the CDN through Redis to the database's buffer pool.
- System design big archive, How can cache systems go wrong?: [pages 246 to 247](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=246). The thundering herd, cache penetration, cache breakdown and a crashed cache, each with its fix.

**Videos**

- ByteByteGo, Cache Systems Every Developer Should Know, Distributed and backend cache, 3:59 to 4:42: [watch](https://www.youtube.com/watch?v=dGAgxozNWFE&t=239s). The shared cache that sits between services and the database, after the hardware, operating system and CDN layers. Chapter-timed.
- Hayk Simonyan, The Ultimate Guide to Caching and CDNs, Cache HIT, MISS, and Ratio, 1:37 to 2:09: [watch](https://www.youtube.com/watch?v=RCdAGvtTYI0&t=97s). Names a hit, a miss and the hit ratio that measures a cache. Chapter-timed.
- Gaurav Sen, Caching in distributed systems: A friendly introduction, Caching use cases, 0:20 to 3:42: [watch](https://www.youtube.com/watch?v=zw7VwIlkPPc&t=20s). Why a system caches at all, drawn on a whiteboard. Chapter-timed.
- Hello Interview, Caching in System Design Interviews, Cache architectures, 9:59 to 14:58: [watch](https://www.youtube.com/watch?v=1NngTUYPdpI&t=599s). The read and write patterns a design chooses between, from a former Meta staff engineer. Chapter-timed.

**Our plans and chapters**

- [The nginx cache: MISS, then HIT](/home/molef/goal-setting/learning/system-design/foundations/plans/10-the-nginx-cache.md), system-design/foundations, plan 10. An nginx cache answers the corner shop's catalogue page by itself on the second request, timed against the first.
- [Redis cache-aside, and the stale price](/home/molef/goal-setting/learning/system-design/foundations/plans/17-redis-cache-aside-and-the-stale-price.md), the same journey, plan 17. Redis holds a price for 60 seconds and keeps serving R69.99 after the admin changes it to R74.99.
- [Redis as a cache](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/21-redis-cache.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 21. Cache-aside on an availability search, with `redis-cli MONITOR` open so every hit and miss is watched.
- [In-Memory Key-Value Stores & Caching Patterns](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/01-distributed-systems-primitives/plans/04-kv-store-caching-patterns.md), projects/tms-mobility/system-design/plans/01-distributed-systems-primitives, plan 04. Cache-aside, expiry and eviction, and why short-lived data suits an in-memory store.
- [System Design: Caching](/home/molef/goal-setting/learning/system-design/caching/MASTER_PLAN.md), system-design/caching. The journey that rebuilds the write patterns, invalidation and stampedes; it holds sources and goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext; the AI engineering pages were found through its back-of-book index ("engineering architecture, step 4: reducing latency with caches") and the others through the chapter tables in `Textbooks.md`. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: AI engineering's prompt caching (pages 838 to 840), which reuses a model's processed prompt and sits closer to [[KV Cache]]; the KV cache pages in both language model books; Hussein Nasser's Basic Caching Techniques and freeCodeCamp's System Design Concepts Course chapter "Caching and CDNs", which repeat what the four videos cover; the compiled chapters for foundations plans 10 and 17 and devops-and-deployment plan 11, whose sections are not written yet. The bare word "cache" was sampled in the learning tree: 40 lines that are not the KV cache, and all but two (a code path and a Hugging Face folder) mean this idea, including Docker's and uv's build caches; the `link-skip` phrases cover the "Caption-read from the earlier cache" lines (19) and the cache folders under `~/.claude/`. The Computer networking: a top-down approach lines were read with pdftotext on 2026-10-24, found through the book's back-of-book index and its outline in `Textbooks.md`.
