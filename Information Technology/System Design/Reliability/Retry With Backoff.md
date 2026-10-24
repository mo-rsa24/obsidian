---
aliases: [retry with backoff, exponential backoff, backoff, retry, retry policy, rate-limit backoff]
link-only-in: [system-design, projects, data-engineering]
standard: vault-note v2
---

# Retry With Backoff

Up: [[Reliability]]

Information Technology, System Design. A retry usually follows a [[Timeout]], and it is safe only when the operation has [[Idempotency]]; a [[Message Queue]] is a common place to park a failed job until its retry.

**Retry with backoff sends a failed request again after a pause that grows with each attempt (1 second, then 2, then 4), up to a limit, often with a little random jitter so many clients do not retry at the same instant.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches retries writes the rest around it.

## Where to learn this

**Retry with backoff**, try again after a pause that grows each time. Also: retry, exponential backoff, backoff, jitter, retry policy.

**Textbooks**

- Hands-on large language models, chapter 4, Text classification with generative models, a tip on rate limit errors: [page 189](../../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=189). Exponential backoff for an API that refuses calls made too often: sleep after each rate limit error, retry, and lengthen the sleep until the call succeeds or the retry limit is reached.
- System design interview, chapter 10, Design a notification system, Retry mechanism: [page 161](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=161). A notification that a third-party service failed to send goes back on the message queue to be retried, and an alert goes to the developers if it keeps failing.
- AI engineering, chapter 10, Step 2, Put in guardrails, output guardrails: [page 860](../../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=860). Retrying an empty or malformed model response, what each retry adds in latency and cost, and sending the same query twice at once instead of waiting for the first to fail.

**Videos**

- Hello Interview, Networking Essentials for System Design Interviews, Timeouts, Backoff, and Retries, 55:49 to 1:00:15: [watch](https://www.youtube.com/watch?v=SHkbPm1Wrno&t=3349s). Timeouts, backoff and retries taken together, before cascading failures and circuit breakers, from a former Meta senior manager. Chapter-timed.
- Arpit Bhayani, Thundering Herd Problem and How not to do API retries, 0:00 to 10:43: [watch](https://www.youtube.com/watch?v=8sTuCPh3s0s&t=0s). Why many clients retrying together can overwhelm a recovering server, and how not to write retries. Whole video.
- Arpit Bhayani, How to safely and gracefully handle timeouts in a microservices, Retry only if needed, 16:35 to 20:05: [watch](https://www.youtube.com/watch?v=Hxja4crycBg&t=995s). When a call that timed out should be retried and when it should not. Chapter-timed.
- Arpit Bhayani, Designing Idempotent API Endpoints for Payments at Stripe, Retry, 2:34 to 4:46: [watch](https://www.youtube.com/watch?v=J2IcD9FZvZU&t=154s). The client retry that a payment endpoint must survive. Chapter-timed.

**Our plans and chapters**

- [The providers, the webhook, and one key](/home/molef/goal-setting/learning/system-design/foundations/plans/20-providers-webhook-and-one-key.md), system-design/foundations, plan 20. The order service retries a charge whose reply was lost, and the idempotency key keeps the retry from charging twice.
- [The agent's first real score on the shop](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/45-the-first-real-score.md), ai-engineering/one-business-end-to-end, plan 45. Forty model calls in a loop hit the provider's rate limit on the first run, so a one-second pause and a retry with backoff go in.
- [The outbox worker and Celery](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/22-outbox-worker-celery.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 22. Its breadth video names retry with backoff as the one feature the hand-built worker lacks.
- [The retry that only catches crashes](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/30-the-retry-that-only-catches-crashes.md), ai-engineering/one-business-end-to-end, plan 30. A retry around an agent's SQL call, measured: a statement that crashes is repaired, and one that runs and returns the wrong number is never retried.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The Hands-on large language models page was found through its back-of-book index ("exponential backoff"), the AI engineering page through a page-text search for "retry", and the System design interview page through a page-text search across the system design books, each then read with pdftotext. Left out: Natural language processing with Python's "backoff" entries (pages 222 to 230), which are backoff tagging, another idea; System design interview page 69, which gives backoff one bullet. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; no ByteByteGo, Hayk Simonyan or Gaurav Sen video on retries was found in their cached upload lists. Each plan was read at its title and description. Bare "retry" is scoped with `link-only-in`: of 25 sampled learning-tree lines, about 18 mean re-asking a language model after a bad answer in the ai-engineering journeys, so the single word links only under system-design, projects and data-engineering, where it means re-sending a failed call; "retry with backoff" and "exponential backoff" link everywhere. "backoff" (6 lines) means this idea in all of them. Bare "jitter" is not an alias: 4 of its 7 lines are Gaussian jitter in the diffusion journeys.
