---
aliases: [time to live, time-to-live, TTL]
link-skip: [TTL drops, per hop, hop limit]
standard: vault-note v2
---

# Time To Live

Up: [[Caching]]

Information Technology, System Design. A TTL is how a [[Cache]] decides an entry is too old, and how a [[Content Delivery Network]] knows when to fetch a file again.

**A time to live (TTL) is the number of seconds a stored copy may be served before it counts as expired and must be fetched again from its source.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches TTLs writes the rest around it.

## Where to learn this

**Time to live (TTL)**, how long a cached copy stays valid. Also: TTL, time-to-live, expiry time.

**Textbooks**

- System design interview, chapter 1, Content delivery network: [pages 17 to 18](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=17). Works one image through a CDN step by step: the origin returns it with a TTL header, the CDN serves user B from cache until the TTL expires, and the expiry must be neither too long nor too short.
- System design interview, chapter 1, Cache: [page 15](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=15). The expiration policy for a cache tier: too short reloads the database too often, too long serves stale data.
- System design big archive, How can cache systems go wrong?: [pages 246 to 247](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=246). What goes wrong when many keys expire at the same moment or a hot key expires, and the fixes: a random offset on each expiry, and no expiry on hot keys.
- System design big archive, Where do we cache data?: [page 302](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=302). The browser keeps an HTTP response under the expiry policy in its header and tries its own cache first on the next request.

**Videos**

- ByteByteGo, Caching Pitfalls Every Developer Should Know, Understanding cache stampede, 0:42 to 2:52: [watch](https://www.youtube.com/watch?v=wh98s0XhMmQ&t=42s). The cache stampede, where a popular entry expires and every waiting request hits the database at once. Chapter-timed.
- Hussein Nasser, Browser Caching Best Practices, Pattern 1: Immutable content + long max-age, 2:00 to 5:40: [watch](https://www.youtube.com/watch?v=z4XdfFscxSk&t=120s). The browser's TTL, `max-age`, set long on content that never changes. Chapter-timed.
- Arpit Bhayani, Implementing GET, SET, and TTL Commands in Redis, Implementing the TTL command, 16:16 to 19:21: [watch](https://www.youtube.com/watch?v=1rnEpo56LFk&t=976s). Redis's TTL command built from scratch in a Redis clone. Chapter-timed.

**Our plans and chapters**

- [dnsmasq answers shop.test](/home/molef/goal-setting/learning/system-design/foundations/plans/08-dnsmasq-answers-shop-test.md), system-design/foundations, plan 08. A DNS answer read with `dig`, including its TTL: the seconds anyone who asked may keep the address.
- [Redis cache-aside, and the stale price](/home/molef/goal-setting/learning/system-design/foundations/plans/17-redis-cache-aside-and-the-stale-price.md), the same journey, plan 17. A 60-second TTL on a cached price, and the stale R69.99 it serves until the TTL runs out or the key is deleted.
- [In-Memory Key-Value Stores & Caching Patterns](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/01-distributed-systems-primitives/plans/04-kv-store-caching-patterns.md), projects/tms-mobility/system-design/plans/01-distributed-systems-primitives, plan 04. TTL beside cache-aside and eviction for short-lived data.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page was read with pdftotext after a page-text search for "TTL", "time to live" and "expir" across the system design books; neither language model book indexes the term. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description; the compiled chapter for foundations plan 08 has section 8.2 "dig at localhost, and the TTL" as a heading with no text yet, so the plan is linked instead. Left out: Arpit Bhayani's Implementing DEL, EXPIRE, and Cleanup in Redis, a second Redis-internals video on the same command family. "TTL" in the learning tree (105 uses) is almost always the cache sense; the `link-skip` phrases cover the networking sense, where an IP packet's TTL drops by one per hop.
