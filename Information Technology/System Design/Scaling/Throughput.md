---
aliases: [throughput, requests per second, queries per second, QPS, RPS]
standard: vault-note v2
---

# Throughput

Up: [[Scaling]]

Information Technology, System Design. [[Latency]] is the other half of performance, how long one request waits; [[Scalability]] is how a system raises its throughput.

**Throughput is how much work a system completes per unit of time, usually counted as requests or queries per second (RPS or QPS), or tokens per second for a model.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches throughput writes the rest around it.

## Where to learn this

**Throughput**, work completed per second. Also: requests per second (RPS), queries per second (QPS), tokens per second.

**Textbooks**

- System design interview, chapter 2, Example: Estimate Twitter QPS and storage requirements: [page 39](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=39). Works QPS with numbers: 300 million monthly users, half of them daily, 2 tweets each, gives 150 million × 2 / 86,400 s, about 3,500 tweets per second, and a peak of about 7,000.
- System design big archive, System performance metrics every engineer should know: [pages 429 to 430](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=429). QPS, transactions per second, concurrency and response time tied by QPS = concurrency ÷ average response time, with 100 requests per second at 5 seconds each meaning 500 requests in flight.
- AI engineering, chapter 9, Throughput and goodput: [pages 788 to 790](../../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=788). A model service's throughput in tokens and requests per second, priced with numbers ($2 an hour at 100 tokens per second is about $5.56 per million output tokens), then the trade against latency and goodput, the requests per second that meet the latency targets.
- System design big archive, Latency vs. throughput: [pages 358 to 359](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=358). Throughput as the volume delivered per second, the capacity of the pipe, set against latency as the delay each packet feels.

**Videos**

- ByteByteGo, Back-Of-The-Envelope Estimation / Capacity Planning, Twitter traffic example, 2:44 to 3:56: [watch](https://www.youtube.com/watch?v=UC5xf8FbdJc&t=164s). A traffic estimate for Twitter worked as an example, after the chapter on calculating capacity. Chapter-timed.
- freeCodeCamp, System Design Concepts Course and Interview Prep, Design Requirements (CAP Theorem, Throughput, Latency, SLOs and SLAs), 7:12 to 14:40: [watch](https://www.youtube.com/watch?v=F2FmTdLtb_4&t=432s). Throughput named among the requirements a design is held to, beside latency and service-level targets. Chapter-timed.
- Hussein Nasser, How HAProxy forwards 2 Million Requests Per Second?, Latency and Throughput in HAProxy 2.3 vs 2.4, 11:55 to 21:00: [watch](https://www.youtube.com/watch?v=JZ-ivZrsHEc&t=715s). The throughput and latency of two versions of a real proxy read from a published benchmark. Chapter-timed.

**Our plans and chapters**

- [The envelope, and the context drawing](/home/molef/goal-setting/learning/system-design/foundations/textbook/03-envelope-and-context-drawing.md#31-orders-per-second-at-corner-shop-scale), system-design/foundations, chapter 03, section 3.1. The corner shop's real order history turned into orders per second, because capacity is always quoted per second.
- [Capacity estimates at Attica's scale](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/18-capacity-estimates.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 18. Users, events, requests per second and storage for the real system, feeding every later design decision.
- [Capacity Estimation](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/00-requirements-and-foundations/plans/03-capacity-estimation.md), projects/tms-mobility/system-design/plans/00-requirements-and-foundations, plan 03. Year 1 and Year 3 operator and rider targets converted by hand into QPS and storage.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The AI engineering pages were found through its back-of-book index ("throughput/goodput") and the other pages through page-text searches for "throughput", "QPS" and "requests per second" across the system design books; each range was read with pdftotext. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and the chapter section were read at their titles and first lines. Left out: Systems analysis and design's case of transaction throughput (page 320), a one-paragraph box; Gaurav Sen's capacity-planning video, which estimates storage rather than request rates. "Throughput" was sampled in the learning tree: 13 lines of 58 uses, all meaning work per unit of time (requests, training steps, reviews).
