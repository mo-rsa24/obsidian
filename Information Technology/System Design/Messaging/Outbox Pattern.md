---
aliases: [outbox, outbox pattern, transactional outbox, outbox table, outbox row, outbox relay]
standard: vault-note v2
---

# Outbox Pattern

Up: [[Messaging]]

Information Technology, System Design. The outbox feeds a [[Message Queue]] or [[Apache Kafka]], it rests on a [[Database Transaction]] holding two rows at once, and its consumers need [[Idempotency]] because a relay that crashes after publishing will publish the same event again.

**The outbox pattern writes a service's data change and the event announcing it into the same database transaction, the event as a row in an outbox table, so a separate relay can publish it to the broker afterwards and the two can never disagree.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the outbox pattern writes the rest around it.

## Where to learn this

**Outbox pattern**, the event saved in the same transaction as the change it announces. Also: outbox, transactional outbox, outbox table, outbox relay.

**Videos**

- Confluent, What is the Transactional Outbox Pattern? | Designing Event-Driven Microservices, What is the dual-write problem?, 0:23 to 0:51: [watch](https://www.youtube.com/watch?v=5YLpjPmsPCA&t=23s). The problem the pattern exists for: a service that writes to its database and to the broker separately can do one without the other. Chapter-timed.
- Confluent, What is the Transactional Outbox Pattern?, What is the transactional outbox pattern?, 0:51 to 1:33: [watch](https://www.youtube.com/watch?v=5YLpjPmsPCA&t=51s). The pattern itself, before how its events reach Kafka and which tools process an outbox. Chapter-timed.
- Confluent, What is the Transactional Outbox Pattern?, What delivery guarantees does the outbox pattern provide?, 2:49 to 3:34: [watch](https://www.youtube.com/watch?v=5YLpjPmsPCA&t=169s). The delivery guarantee an outbox gives, followed by the pattern's problems. Chapter-timed.

**Our plans and chapters**

- [The outbox, the queue and the worker](/home/molef/goal-setting/learning/system-design/foundations/plans/19-outbox-queue-and-worker.md), system-design/foundations, plan 19. The corner shop's order and an "order placed" event written in one transaction, a relay publishing the event to RabbitMQ, and a worker that sends the email and acknowledges it, safe when it dies halfway.
- [The booking-request transaction](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/14-booking-request-transaction.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 14. One click writes four rows atomically, the booking request, an audit log, an outbox event and a notification, and the outbox rows wait for a worker.
- [The outbox worker and Celery](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/22-outbox-worker-celery.md), the same journey, plan 22. The worker Attica never runs: Celery over Redis drains the parked outbox rows, publishing once and processing idempotently, proven by running it twice.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No shelf book teaches the outbox pattern: a page-text search of the system design, AI engineering and language model books for "outbox", "dual write", "change data capture" and "transactional messag" found nothing, so the card has no Textbooks group. None of the routed system design creators (ByteByteGo, Hayk Simonyan, Gaurav Sen, Arpit Bhayani, Hussein Nasser, Hello Interview) has an outbox video in their cached upload lists, so an open YouTube search chose Confluent's, the company founded by Kafka's creators; its chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description; the compiled chapter for foundations plan 19 has headings and no text yet. The bare word "outbox" (123 lines) was sampled in the learning tree: all 25 sampled lines mean this pattern.
