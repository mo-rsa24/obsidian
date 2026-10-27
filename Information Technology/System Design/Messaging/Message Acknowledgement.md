---
aliases: [message acknowledgement, message acknowledgment, acknowledgement, acknowledgment, ack, manual ack, redelivery, redelivered]
link-skip-in: [deep-learning/, papers/, system-design/networking/]
link-skip: [SYN-ACK, SYN+ACK, write-acknowledgement, person's acknowledgement, an acknowledgement cannot, "discussion, acks"]
standard: vault-note v2
---

# Message Acknowledgement

Up: [[Messaging]]

Information Technology, System Design. A worker acknowledges each message it takes from a [[Message Queue]], and because an unacknowledged message comes back, the worker has to be safe to run twice, which is [[Idempotency]].

**A message acknowledgement is the consumer telling the broker it has finished with a message, so the broker can delete it; a message delivered and never acknowledged, because the worker died, is delivered again.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches acknowledgements writes the rest around it.

## Where to learn this

**Message acknowledgement**, the consumer's "done" that lets the broker drop a message, and the redelivery that follows when it never arrives. Also: ack, manual ack, acknowledgement, redelivery, redelivered.

**Textbooks**

- System design interview, chapter 10, Design a notification system, reliability: [page 160](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=160). Works the consequence of redelivery: a notification can arrive twice, so each event's ID is checked against those already seen and a repeat is discarded.
- System design big archive, Apache Kafka vs. RabbitMQ: [pages 419 to 420](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=419). RabbitMQ deletes a message once it is acknowledged, while Kafka keeps it until retention expires and each consumer tracks its own offset.

**Videos**

- Hello Interview, Message Queues in System Design Interviews, What is a message queue?, 4:17 to 12:47: [watch](https://www.youtube.com/watch?v=1ISRd0bS714&t=257s). Producers, consumers and acknowledgements, after a motivating example of a request doing too much work in line. Chapter-timed.
- Hello Interview, Message Queues in System Design Interviews, Common deep dives, 15:06 to 23:31: [watch](https://www.youtube.com/watch?v=1ISRd0bS714&t=906s). Retries, dead-letter queues and a message delivered twice. Chapter-timed.
- Hello Interview, Kafka vs RabbitMQ, Delivery and reliability, 6:46 to 8:11: [watch](https://www.youtube.com/watch?v=1HOVtQ-_fcE&t=406s). How the two brokers differ on delivery guarantees. Chapter-timed.

**Our plans and chapters**

- [The outbox, the queue and the worker](/home/molef/goal-setting/learning/system-design/foundations/plans/19-outbox-queue-and-worker.md), system-design/foundations, plan 19. A worker that acks by hand, killed after sending the email and before its ack, gets the message back marked redelivered and skips it through `orders.processed_events`, with Ready and Unacked read in the RabbitMQ console.
- [Message Queue / Pub-Sub / Event-Driven Semantics](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/01-distributed-systems-primitives/plans/06-message-queue-pubsub-event-driven.md), projects/tms-mobility/system-design/plans/01-distributed-systems-primitives, plan 06. At-least-once delivery shown by killing a worker mid-processing and confirming the ride-offer event is redelivered.
- [System Design: Message Queues and Streaming](/home/molef/goal-setting/learning/system-design/message-queues-and-streaming/MASTER_PLAN.md), system-design/message-queues-and-streaming. Goal 2: an at-least-once consumer, a redelivery triggered on purpose, and the consumer made idempotent against it; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "acknowledg", "redeliver", "ack", "dead letter", "at-least-once" and "exactly once" across the system design books and AI engineering. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title, the video title and, for the first two lines, the segment notes in `system-design/foundations/video-scout/pulse-2026-10-24.md`. Each plan was read at its title, description and goal. Left out: every TCP acknowledgement (the big archive's handshake posts on pages 19, 192 to 193, 395 and 440, and the networking book's reliable data transfer), a transport-layer sense; Hussein Nasser's RabbitMQ Crash Course, whose consumer chapter (20:30 to 33:50) could not be confirmed to cover acknowledgement from its chapter list; the compiled chapter for plan 19, whose section "The worker, the ack and the redelivery" is a heading with no text yet. The bare word "acknowledgement" was sampled across the learning tree: 17 of its 32 prose uses are a paper's Acknowledgements section under deep-learning/ and papers/, and others are TCP's in the networking journey, so those folders are under `link-skip-in`; the `link-skip` phrases cover TCP handshakes, an S3 write acknowledgement, and a person acknowledging an exception in the prototype product-data-validation plan 67.
