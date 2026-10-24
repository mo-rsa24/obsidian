---
aliases: [rate limiter, rate limiting, rate limit, token bucket, leaky bucket, leaking bucket, throttling]
standard: vault-note v2
---

# Rate Limiter

Up: [[APIs]]

Information Technology, System Design. A rate limiter usually runs inside an API gateway or a [[Reverse Proxy]], and keeps its counters in a fast shared store such as [[Redis]].

**A rate limiter caps how many requests a client may make in a stretch of time and rejects the rest, usually with HTTP 429, to protect a service from overload and abuse.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches rate limiting writes the rest around it.

## Where to learn this

**Rate limiter**, a cap on requests per client per window. Also: rate limiting, rate limit, token bucket, leaky bucket, throttling.

**Textbooks**

- System design interview, chapter 4, Design a rate limiter, the algorithms: [pages 55 to 62](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=55). Works five algorithms with numbers: a token bucket of capacity 4 refilled 2 tokens a second, the leaking bucket, a fixed window of 3 requests a second, the sliding window log, and a sliding window counter that estimates 3 + 5 × 70% = 6.5 requests against a limit of 7 a minute.
- System design interview, chapter 4, Design a rate limiter, the design: [pages 63 to 68](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=63). Counters kept in Redis, rules and the 429 response with its headers, then the distributed case: two requests reading a counter of 3 at once and both writing 4, and keeping several limiters in sync.
- Grokking the system design interview, section 7, API rate limiter: [page 7](../../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=7). Why a service limits rates: denial-of-service and brute-force attacks, misbehaving clients, cost and spam.
- Hands-on large language models, chapter 4, Text classification with generative models: [page 189](../../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=189). The client's side of a rate limit: an API returns rate-limit errors, and the caller retries with exponential backoff.

**Videos**

- ByteByteGo, Rate Limiter System Design: Token Bucket, Leaky Bucket, Scaling, Token bucket algorithm, 3:08 to 4:33: [watch](https://www.youtube.com/watch?v=YXkOdWBwqaA&t=188s). The token bucket, reached after the fixed window algorithm and its flaws. Chapter-timed.
- Hayk Simonyan, API Security Explained: Rate Limiting, CORS, SQL Injection, CSRF, XSS & More, Rate Limiting, 0:18 to 2:39: [watch](https://www.youtube.com/watch?v=FsB_nRGdeLs&t=18s). Rate limiting as the first defence of a public API. Chapter-timed.
- Hello Interview, Design a Distributed Rate Limiter, High Level Design, 14:31 to 38:50: [watch](https://www.youtube.com/watch?v=MIJFyUPG4Z4&t=871s). A distributed rate limiter designed end to end as an interview problem, after its requirements and interface. Chapter-timed.
- Arpit Bhayani, Inside Stripe's Rate Limiter Architecture, Request Rate Limiter, 5:15 to 9:20: [watch](https://www.youtube.com/watch?v=Oxy-6MAiYPw&t=315s). The request rate limiter a real payments company runs, before its load shedders. Chapter-timed.

**Our plans and chapters**

- [Rate Limiting](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/02-api-and-traffic-control/plans/03-rate-limiting.md), projects/tms-mobility/system-design/plans/02-api-and-traffic-control, plan 03. Token-bucket rate limiting keyed by user, for coupon abuse and the panic button's fail-open or fail-closed choice.
- [System Design: API Gateways](/home/molef/goal-setting/learning/system-design/api-gateways/MASTER_PLAN.md), system-design/api-gateways. Rate limiting added at the gateway and shown rejecting a request; it holds goals and no plans yet.
- [System Design: API Design and Contracts](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/MASTER_PLAN.md), system-design/api-design-and-contracts. A rate limiter among the API pieces the journey rebuilds.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each System design interview and Grokking page range was read with pdftotext after the chapter tables in `Textbooks.md`; the Hands-on large language models page came from its back-of-book index ("rate limit errors"). Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: AI engineering's note that providers throttle too many concurrent requests (page 788), one sentence; Arpit Bhayani's How to Protect Your Systems with Throttling & Rate Limiting, behind the four above. "Throttling" is in the learning tree twice, both meaning this idea.
