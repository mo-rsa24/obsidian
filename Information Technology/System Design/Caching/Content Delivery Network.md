---
aliases: [content delivery network, CDN, edge cache]
standard: vault-note v2
---

# Content Delivery Network

Up: [[Caching]]

Information Technology, System Design. A CDN is a [[Cache]] spread across many cities, and its copies expire by [[Time To Live]].

**A content delivery network (CDN) is a set of servers spread across many locations that keep copies of static files, so each user is served from the server nearest them instead of from the origin.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches CDNs writes the rest around it.

## Where to learn this

**Content delivery network (CDN)**, copies of files at the edge, near users. Also: CDN, edge cache, edge server.

**Textbooks**

- Computer networking: a top-down approach, section 2.6.3, Content distribution networks: [pages 179 to 183](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=179). The two placements, enter deep and bring home, then one request worked through a CDN: a NetCinema link carries a video.netcinema.com name whose DNS lookup is handed to KingCDN's authoritative server, which answers with a nearby cluster, followed by how a cluster is chosen.
- Computer networking: a top-down approach, section 2.6.4, Case studies: Netflix, YouTube, and Kankan: [pages 183 to 186](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=183). How Netflix pushes videos to its own servers inside ISPs and YouTube pulls them into Google's clusters on a miss.
- System design interview, chapter 1, Content delivery network (CDN): [pages 17 to 18](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=17). Works one image request step by step (miss at the CDN, fetch from the origin, cache with a TTL, serve the next user from cache), then cost, expiry, falling back when the CDN is down, and invalidating files by API or by a version in the URL.
- System design big archive, Where do we cache data?: [page 302](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=302). The CDN as the second caching layer after the browser, serving static resources from a nearby node.
- System design big archive, 8 system design concepts explained in 1 diagram: [pages 248 to 249](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=248). A CDN named as the way to cut latency, the delay a user feels, by serving from servers closer to them.

**Videos**

- ByteByteGo, What Is A CDN? How Does It Work?, 0:00 to 4:23: [watch](https://www.youtube.com/watch?v=RI9np1LWzqw&t=0s). A short animated explainer of what a CDN is and how a request reaches the edge. Whole video.
- Hayk Simonyan, The Ultimate Guide to Caching and CDNs, Pull-based and Push-based CDNs, 5:06 to 5:51: [watch](https://www.youtube.com/watch?v=RCdAGvtTYI0&t=306s). The two ways files reach the edge: fetched on the first miss, or uploaded ahead of time. Chapter-timed.
- Gaurav Sen, What is a CDN (Content Delivery Network)?, Content Delivery Networks, 4:01 to 4:56: [watch](https://www.youtube.com/watch?v=b4_6thkYZXs&t=241s). The CDN reached after the problem with one central cache and the idea of caches placed by geography. Chapter-timed.
- Arpit Bhayani, How Giphy uses CDN to serve 10 billion GIFs every day, Giphy CDN architecture, 2:33 to 5:40: [watch](https://www.youtube.com/watch?v=-bo7oVejgRM&t=153s). How a real company puts a CDN in front of its GIFs. Chapter-timed.

**Our plans and chapters**

- [The nginx cache: MISS, then HIT](/home/molef/goal-setting/learning/system-design/foundations/plans/10-the-nginx-cache.md), system-design/foundations, plan 10. An nginx cache standing in for the CDN answers the catalogue page itself on the second request, so it never reaches the balancer.
- [System Design: CDN and Content Delivery](/home/molef/goal-setting/learning/system-design/cdn-and-content-delivery/MASTER_PLAN.md), system-design/cdn-and-content-delivery. The journey that rebuilds edge caching, what the edge has cached, and a miss against a hit; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "CDN" and "content delivery" across the system design books; neither language model book covers CDNs. Each video's chapter list was read with `cache-video-chapters.py` (the ByteByteGo explainer has none and is cited whole), and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: System design interview's CDN pages in chapter 14 (Design YouTube, pages 222 to 228), which apply the idea to video; freeCodeCamp's System Design for Beginners chapter "Content Delivery Networks" (0:32 long) and System Design Concepts Course chapter "Caching and CDNs", covered by the four videos above. The Computer networking: a top-down approach lines were read with pdftotext on 2026-10-24, found through the book's back-of-book index and its outline in `Textbooks.md`.
