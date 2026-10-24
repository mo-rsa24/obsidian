---
aliases: [latency, tail latency, percentile latency, p95, p99]
standard: vault-note v2
---

# Latency

Up: [[Scaling]]

Information Technology, System Design. [[Throughput]] is the other half of performance, how much work is done per second; a [[Cache]] and a [[Content Delivery Network]] exist mostly to cut latency.

**Latency is the time one request takes from being sent to its answer arriving, and because it varies from request to request it is read as percentiles: p95 is the time 95% of requests beat.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches latency writes the rest around it.

## Where to learn this

**Latency**, how long one request waits for its answer. Also: tail latency, percentile latency, p50, p95, p99.

**Textbooks**

- AI engineering, chapter 9, Inference performance metrics: [pages 784 to 787](../../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=784). Works latency as a distribution with numbers: ten time-to-first-token values whose mean of 390 ms is dragged up by one 3,000 ms request, so p50, p90, p95 and p99 are read instead; before that, a response's latency split into time to first token and time per output token.
- System design interview, chapter 2, Latency numbers every programmer should know: [pages 36 to 37](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=36). Jeff Dean's 2010 table of how long typical computer operations take, with its units from nanoseconds to milliseconds, and the conclusions drawn from it: memory is fast, disk is slow, avoid disk seeks, compress before sending, and data centres are far apart.
- System design big archive, Latency vs. throughput: [pages 358 to 359](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=358). Latency as the delay per packet, what a user feels after clicking a button, set against throughput as the volume delivered per second.

**Videos**

- Hussein Nasser, Percentile Tail Latency Explained (95%, 99%), Calculating Percentile, 2:09 to 5:20: [watch](https://www.youtube.com/watch?v=3JdQOExKtUY&t=129s). How a p95 or p99 is calculated from a set of request times, after why an average is not enough. Chapter-timed.
- ByteByteGo, Latency Numbers Programmer Should Know: Crash Course System Design #1, Time Units, 1:03 to 2:50: [watch](https://www.youtube.com/watch?v=FqR5vESuKe0&t=63s). The units the latency numbers are written in, before the operations that take microseconds. Chapter-timed.
- Gaurav Sen, How 100 milliseconds cost Amazon 3 BILLION DOLLARS, The Impact of Reduced Latency, 0:50 to 1:54: [watch](https://www.youtube.com/watch?v=I8FeITQvLAk&t=50s). Why a small cut in latency is worth money to a business. Chapter-timed.
- freeCodeCamp, System Design Concepts Course and Interview Prep, Design Requirements (CAP Theorem, Throughput, Latency, SLOs and SLAs), 7:12 to 14:40: [watch](https://www.youtube.com/watch?v=F2FmTdLtb_4&t=432s). Latency beside throughput and the service-level targets written on both. Chapter-timed.

**Our plans and chapters**

- [Prometheus, Grafana, and the alert](/home/molef/goal-setting/learning/system-design/foundations/plans/22-prometheus-grafana-and-the-alert.md), system-design/foundations, plan 22. Every service gets a metrics endpoint and Grafana draws request rate, errors and p95 latency.
- [HTTPS, and three round trips](/home/molef/goal-setting/learning/system-design/foundations/plans/09-https-and-three-round-trips.md), the same journey, plan 09. `curl -w` times the three round trips every new connection pays before the first byte: the DNS lookup, the TCP connection and the TLS handshake.
- [Trace one question, and time and price it](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/plans/30-traces-latency-and-cost.md), ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions, plan 30. One question through a RAG build, timed and priced stage by stage.
- [Load & Performance Testing](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/03-operations-and-delivery/plans/06-load-performance-testing.md), projects/tms-mobility/system-design/plans/03-operations-and-delivery, plan 06. Load, stress, spike and soak tests on a dispatch endpoint, summarised as p95 latency and error rate.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The AI engineering pages were found through its back-of-book index ("inference performance metrics, latency, TTFT, and TPOT") and the other pages through page-text searches across the system design books; each range was read with pdftotext. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description; the compiled chapter for foundations plan 22 has headings and no text yet. Left out: the CME295 lecture-map rows that mention latency only in passing (the cost of best-of-N in preference tuning). "Latency" was sampled in the learning tree: 25 random lines of 276 uses, all meaning a request's waiting time, in web services and in model calls alike.
