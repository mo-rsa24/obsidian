---
aliases: [scalability, horizontal scaling, vertical scaling, scale horizontally, scale vertically]
standard: vault-note v2
---

# Scalability

Up: [[Scaling]]

Information Technology, System Design. Horizontal scaling needs a [[Load Balancer]] in front and a [[Stateless Service]] behind it; [[Sharding]] scales the database the same way.

**Scalability is a system's ability to take on more load by adding resources, either a bigger machine (vertical scaling) or more machines (horizontal scaling), without its performance falling away.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches scalability writes the rest around it.

## Where to learn this

**Scalability**, growing a system by adding resources. Also: horizontal scaling (scale out), vertical scaling (scale up).

**Textbooks**

- System design interview, chapter 1, Database scaling: [page 28](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=28). Works vertical scaling with real figures (a 24 TB RAM server on Amazon RDS, Stack Overflow serving 10 million monthly visitors from one master database in 2013) and its limits, then turns to horizontal scaling.
- System design interview, chapter 1, Vertical scaling vs horizontal scaling: [page 9](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=9). Scale up against scale out, and why the hard ceiling and missing failover of one big server make large applications scale out.
- System design big archive, A crash course on architectural scalability: [pages 22 to 23](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=22). Scalability as a cost-effective strategy applied again and again, its three bottlenecks, and four techniques: load balancing, caching, event-driven processing and sharding.
- AI engineering, chapter 9, Parallelism: [page 841](../../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=841). Replica parallelism, scaling a model service out by running more copies, with the bin-packing of 8B to 70B models onto 24 to 80 GB GPUs.
- Systems analysis and design, chapter 8, Architecture design: [pages 310 to 311](../../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=310). Client-server and n-tiered architectures called scalable because an overloaded server can be joined by another.

**Videos**

- ByteByteGo, Scalability Simply Explained in 10 Minutes, Scalability strategies, 4:08 to 9:20: [watch](https://www.youtube.com/watch?v=EWS_CIxttVw&t=248s). The strategies that follow the video's chapters on what scalability is and where it bottlenecks. Chapter-timed.
- ByteByteGo, Vertical Vs Horizontal Scaling: Key Differences You Should Know, 0:00 to 4:34: [watch](https://www.youtube.com/watch?v=dvRFHG2-uYs&t=0s). The two ways to scale compared in one short explainer. Whole video.
- Gaurav Sen, System Design BASICS: Horizontal vs. Vertical Scaling, Horizontal vs. Vertical Scaling, 4:10 to 6:25: [watch](https://www.youtube.com/watch?v=xpDnVSmNFX0&t=250s). The two compared on a whiteboard, after a business outgrows one computer. Chapter-timed.
- freeCodeCamp, System Design Course: APIs, Databases, Caching, CDNs, Load Balancing and Production Infra, Vertical vs Horizontal Scaling, 13:32 to 16:22: [watch](https://www.youtube.com/watch?v=C842vFY5kRo&t=812s). The same choice inside a long course that grows a single server into a production system. Chapter-timed.

**Our plans and chapters**

- [Zones, and a copy under load](/home/molef/goal-setting/learning/system-design/foundations/plans/25-zones-and-a-copy-under-load.md), system-design/foundations, plan 25. A third gateway copy added when p95 latency crosses a threshold, with p95 recorded under the same load before and after.
- [System Design: Scalability](/home/molef/goal-setting/learning/system-design/scalability/MASTER_PLAN.md), system-design/scalability. The journey that rebuilds horizontal against vertical scaling and makes a stateful toy service stateless to scale it out; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext; the Systems analysis and design pages came from its back-of-book index ("Scalable architectures"), the AI engineering page from its index ("replica parallelism"), and the rest from page-text searches across the system design books. Each video's chapter list was read with `cache-video-chapters.py` (the ByteByteGo comparison has none and is cited whole), and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: Hayk Simonyan's Vertical vs Horizontal Scaling in System Design (3:37) and How to Scale Like a Senior Engineer, which repeat the comparison. "Scale up" and "scale out" were left off the aliases: the learning tree uses them 4 times, none in this sense ("scale up using an LLM arbitrator", "the input scale out of both files"). Bare "scaling" is never an alias because the statistics notes use it for the scaling rule for variance.
