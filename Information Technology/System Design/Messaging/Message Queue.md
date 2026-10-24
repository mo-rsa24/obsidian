---
aliases: [message queue, job queue, task queue, message broker, RabbitMQ, SQS]
standard: vault-note v2
---

# Message Queue

Up: [[Messaging]]

Information Technology, System Design. [[Publish-Subscribe]] is the one-to-many form of the same idea, [[Apache Kafka]] is a log that is often used as one, and the [[Outbox Pattern]] is how a service puts a message on the queue without losing it; [[Redis]] can also serve as the broker.

**A message queue is a buffer between services: a producer writes a message and moves on, and a worker takes it off the queue and does the work later, so neither side waits for the other.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches message queues writes the rest around it.

## Where to learn this

**Message queue**, a buffer that lets a producer hand work to a worker without waiting. Also: job queue, task queue, message broker, RabbitMQ, SQS.

**Textbooks**

- System design interview, chapter 1, Message queue: [page 25](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=25). Works one case: web servers publish photo-processing jobs to a queue, workers pick them up, and the worker count grows when the queue gets long and shrinks when it is empty.
- System design interview, chapter 10, Design a notification system, high-level design and reliability: [pages 159 to 161](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=159). One queue per notification type so an outage at one provider stops only its own queue, workers that pull from each queue, and a failed send put back on the queue for a retry.
- System design big archive, How RabbitMQ Works?: [pages 206 to 207](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=206). A broker from the inside: producer, exchange, bindings, the direct, topic and fanout exchange types, and the consumer pulling from its queue.
- System design big archive, SQS vs SNS vs EventBridge vs Kinesis: [pages 69 to 70](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=69). Four AWS messaging services side by side, with SQS chosen when one consumer should process each job, such as an image-processing job.

**Videos**

- Gaurav Sen, What is a MESSAGE QUEUE and Where is it used?, Pizza Shop Example, 0:00 to 1:40: [watch](https://www.youtube.com/watch?v=oUJbuFMyBDk&t=0s). A pizza shop that takes orders faster than it bakes them, the worked case the rest of the video turns into a queue. Chapter-timed.
- Hayk Simonyan, Message Queues in System Design, 0:00 to 4:30: [watch](https://www.youtube.com/watch?v=DYFocSiPOl8&t=0s). A short explainer of what a message queue is and where a design uses one. Whole video.
- Hello Interview, Message Queues in System Design Interviews, What is a message queue?, 4:17 to 12:47: [watch](https://www.youtube.com/watch?v=1ISRd0bS714&t=257s). A former Meta staff engineer defines the queue after a motivating example, before the chapters on when to use one and Kafka, SQS and RabbitMQ. Chapter-timed.
- ByteByteGo, Kafka vs. RabbitMQ vs. Messaging Middleware vs. Pulsar, Scalability and decoupling, 0:24 to 0:57: [watch](https://www.youtube.com/watch?v=x4k1XEjNzYQ&t=24s). The opening chapter of a short history of message brokers, from IBM MQ through RabbitMQ and Kafka to Pulsar. Chapter-timed.

**Our plans and chapters**

- [The outbox, the queue and the worker](/home/molef/goal-setting/learning/system-design/foundations/plans/19-outbox-queue-and-worker.md), system-design/foundations, plan 19. A relay publishes the corner shop's "order placed" event to RabbitMQ and one worker sends the email and acknowledges it, safely even when it dies halfway.
- [The outbox worker and Celery](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/22-outbox-worker-celery.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 22. Celery over Redis drains the outbox rows Attica parks, the worker Attica never runs.
- [Message Queue / Pub-Sub / Event-Driven Semantics](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/01-distributed-systems-primitives/plans/06-message-queue-pubsub-event-driven.md), projects/tms-mobility/system-design/plans/01-distributed-systems-primitives, plan 06. Queue mechanics and the publisher-subscriber model, for the job dispatch queue the TMS proposal named.
- [System Design: Message Queues and Streaming](/home/molef/goal-setting/learning/system-design/message-queues-and-streaming/MASTER_PLAN.md), system-design/message-queues-and-streaming. The journey that rebuilds a point-to-point queue, at-least-once delivery and backpressure; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "message queue", "message broker", "RabbitMQ" and "SQS" across the system design books; the chapter tables in `Textbooks.md` gave the big archive's sections. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: Hussein Nasser's What is a Message Queue and When should you use Messaging Queue Systems Like RabbitMQ and Kafka, whose "Implementing message queues" chapter (7:13 to 9:16) covers the same ground and whose queue against pub-sub chapter sits on [[Publish-Subscribe]]; the big archive's Apache Kafka vs. RabbitMQ (pages 419 to 420), which sits on [[Apache Kafka]]; Hayk Simonyan's How Message Queues Handle Traffic Spikes, which covers the same ground as his explainer above; the compiled chapter for foundations plan 19, whose sections are headings with no text yet; the notification-systems master plan, which [[Publish-Subscribe]] and [[WebSocket]] carry. Bare "queue" is not an alias: in the learning tree it also means the cadence queue, the Codex queue and review queues, so only the multi-word names link.
