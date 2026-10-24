---
aliases: [idempotency, idempotent, idempotency key, Idempotency-Key, idempotent consumer]
link-skip: [is idempotent for the same reason, idempotent on its own image]
standard: vault-note v2
---

# Idempotency

Up: [[Reliability]]

Information Technology, System Design. Idempotency is what makes [[Retry With Backoff]] safe after a [[Timeout]], and a consumer of a [[Message Queue]] or the [[Outbox Pattern]] needs it because a message can arrive twice.

**An operation is idempotent when doing it twice has the same effect as doing it once; an idempotency key lets a server recognise a retried request and return the first result instead of charging or booking again.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches idempotency writes the rest around it.

## Where to learn this

**Idempotency**, the same request twice, the effect once. Also: idempotent, idempotency key, Idempotency-Key header, idempotent consumer.

**Textbooks**

- System design interview, chapter 10, Design a notification system, Reliability: [page 160](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=160). Works the duplicate-notification case: delivery cannot be exactly once, so each arriving event's ID is checked and an event seen before is discarded.
- System design big archive, How to Design Good APIs: [pages 380 to 381](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=380). Which HTTP methods are idempotent (GET, HEAD, PUT, DELETE) and which are not (POST, PATCH), then idempotency keys kept in Redis or the database so a retry gets the original response.
- System design big archive, A Cheatsheet on REST API Design Best Practices: [page 143](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=143). Idempotent endpoints for safe retries, especially for POST, and idempotency keys to deduplicate operations with side effects.

**Videos**

- Arpit Bhayani, Build a robust Payments service using Idempotency Keys, Flow, 11:13 to 16:36: [watch](https://www.youtube.com/watch?v=m6DtqSb1BDM&t=673s). The flow of a payment request carrying an idempotency key, after the chapters on why a transaction repeats and two ways to implement it. Chapter-timed.
- Hussein Nasser, Why Idempotency is very critical in Backend Applications, What is Idempotency, 1:08 to 7:12: [watch](https://www.youtube.com/watch?v=4OuaONkZw1I&t=68s). What idempotency means for a backend request. Chapter-timed.
- Arpit Bhayani, Designing Idempotent API Endpoints for Payments at Stripe, Retry, 2:34 to 4:46: [watch](https://www.youtube.com/watch?v=J2IcD9FZvZU&t=154s). The retry that makes Stripe's payment endpoints need idempotency, before the unintended behaviour it causes. Chapter-timed.

**Our plans and chapters**

- [The API contract on paper](/home/molef/goal-setting/learning/system-design/foundations/textbook/02-the-api-contract-on-paper.md#23-the-idempotency-key-header), system-design/foundations, chapter 2, section 2.3. Works the three cases of `POST /payments` with an `Idempotency-Key`: a new key charges and returns 201, the same key and body returns the stored payment with 200, and the same key with a different body is refused with 409, held by a UNIQUE constraint.
- [Idempotency: making a retried accept safe](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/07-idempotency.md), projects/attica/architecture-decisions, plan 07. The same accept replayed twice with the same key lands one row, then whether Attica's `idempotency_key` protects `ProviderAvailability` or stops at the bid.
- [The providers, the webhook, and one key](/home/molef/goal-setting/learning/system-design/foundations/plans/20-providers-webhook-and-one-key.md), system-design/foundations, plan 20. A retried charge to the fake payment provider lands once even when the reply to the first attempt is lost.
- [Running the load twice: idempotent writes and a backfill](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/50-e9-idempotent-reruns.md), data-engineering/many-sources-one-lakehouse, plan 50. The same 834-row file loaded twice, once with a plain append and once with a keyed `MERGE`, and the row counts compared.
- [The outbox worker and Celery](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/22-outbox-worker-celery.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 22. An idempotent consumer proven by running the outbox worker twice over the same parked rows.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "idempoten" and "exactly once" across the system design books; the "Idempotency" and "Idempotent" index entries in the Linear algebra textbook and The Matrix Cookbook are the matrix property ($P^2 = P$), another idea. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and the chapter section were read at their titles and opening lines. The bare words were sampled in the learning tree: "idempotency" (88 lines) means this idea in all 20 sampled, and "idempotent" (23 lines) in 18 of 20; the other two are the matrix property in a diffusion textbook chapter and a model-collapse reading, which the `link-skip` phrases cover.
