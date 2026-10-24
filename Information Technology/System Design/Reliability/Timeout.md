---
aliases: [timeout, connection timeout, read timeout, request timeout]
standard: vault-note v2
---

# Timeout

Up: [[Reliability]]

Information Technology, System Design. What follows a timeout is usually [[Retry With Backoff]], which is safe only with [[Idempotency]]; a [[Health Check]] is itself a request with a timeout. [[Time To Live]] is a different clock: how long a cached copy stays valid.

**A timeout is the longest a caller will wait for a reply before giving up and treating the call as failed, so one slow or silent service cannot hold every caller behind it.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches timeouts writes the rest around it.

## Where to learn this

**Timeout**, the longest a caller waits before calling it a failure. Also: connection timeout, read timeout, request timeout.

**Textbooks**

- System design interview, chapter 9, Design a web crawler, Short timeout: [page 146](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=146). A crawler gives each web server a maximal wait time and, when a host does not answer within it, stops that job and crawls other pages.
- System design big archive, How to Debug a Slow API?: [pages 362 to 363](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=362). Set aggressive timeouts and retries on third-party calls such as Stripe or Google Maps, so one slow provider cannot slow the whole response.

**Videos**

- Hussein Nasser, Frontend and Backends Timeouts, Connection Timeout, 2:30 to 5:00: [watch](https://www.youtube.com/watch?v=2GAQVXGT_Zw&t=150s). The first of the timeouts a backend sets, before read, wait, usage and response timeouts. Chapter-timed.
- Hello Interview, Networking Essentials for System Design Interviews, Timeouts, Backoff, and Retries, 55:49 to 1:00:15: [watch](https://www.youtube.com/watch?v=SHkbPm1Wrno&t=3349s). Timeouts set on calls between services, paired with backoff and retries. Chapter-timed.
- Arpit Bhayani, How to safely and gracefully handle timeouts in a microservices, What is a timeout, 6:50 to 16:35: [watch](https://www.youtube.com/watch?v=Hxja4crycBg&t=410s). Timeouts between services, after a scenario and what can go wrong in it, and before when to retry. Chapter-timed.
- Hussein Nasser, How timeouts can make or break your Backend load balancers, Client/Load Balancer Timeouts, 2:00 to 11:30: [watch](https://www.youtube.com/watch?v=uNjACLXoH5A&t=120s). The timeouts between a client and a load balancer, then between the balancer and its backends. Chapter-timed.

**Our plans and chapters**

- [Payment, notification, and a timeout](/home/molef/goal-setting/learning/system-design/foundations/plans/14-payment-notification-and-a-timeout.md), system-design/foundations, plan 14. The order service calls payment with httpx and a 2-second timeout; a card ending 0003 takes 3 seconds, so the timeout fires, and the sitting ends on what the customer is told.
- [Call the model endpoint by hand](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/plans/04-call-the-endpoint-by-hand.md), ai-engineering/prototype-product-data-validation-end-to-end, plan 04. A broken run on purpose: a `requests` call with no timeout against a server that never answers, written up against the same call with `timeout=1`.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page was read with pdftotext after a page-text search for "timeout" across the system design and AI books; System design interview's other hits are Redis's EXPIRE (page 62, closer to [[Time To Live]]) and long polling's timeout (page 182, on [[Polling]]), and Grokking's is a seat reservation expiring. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; no ByteByteGo video on timeouts was found in its cached upload list. Each plan was read at its title and description; the compiled chapter for foundations plan 14 has headings and no text yet. Left out: Hussein Nasser's Request Read timeout chapter (5:00 to 10:00) and his two nginx timeout videos, which cover one proxy's settings. The bare word "timeout" (138 lines) was sampled in the learning tree: all 25 sampled lines mean a request's wait limit.
