---
aliases: [publish-subscribe, pub/sub, pub-sub, pubsub, publish/subscribe, publisher, subscriber]
link-skip: [Netflix subscriber, publisher Microsoft]
standard: vault-note v2
---

# Publish-Subscribe

Up: [[Messaging]]

Information Technology, System Design. A [[Message Queue]] hands each message to one worker, where publish-subscribe hands a copy to every subscriber; [[Fan-Out]] is the same copying seen from the sender, and [[Apache Kafka]] and [[Redis]] both offer it.

**Publish-subscribe is a messaging pattern where a publisher sends a message to a named topic or channel and every service subscribed to it receives its own copy, without the publisher knowing who they are.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches publish-subscribe writes the rest around it.

## Where to learn this

**Publish-subscribe**, one message copied to every subscriber of a topic. Also: pub/sub, pub-sub, publisher, subscriber.

**Textbooks**

- System design interview, chapter 12, Design a chat system, Online status fanout: [page 196](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=196). Works one case: user A's presence change is published to three channels, A-B, A-C and A-D, and friends B, C and D each receive it on the channel they subscribe to.
- System design big archive, SQS vs SNS vs EventBridge vs Kinesis: [pages 69 to 70](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=69). SNS as the managed publish/subscribe service that sends one message on a topic to many subscribers, set beside SQS's one-consumer queue.
- System design interview, chapter 15, Design Google Drive, Notification service: [page 253](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=253). The notification service as a publisher/subscriber system that tells every relevant client when a file is added, edited or removed elsewhere.

**Videos**

- Hussein Nasser, Publish-Subscribe Architecture (Explained by Example), Pub/sub pattern, 11:12 to 17:50: [watch](https://www.youtube.com/watch?v=O1PgqUqZKTA&t=672s). The pattern drawn on an example system, after the chapters on where request-response breaks. Chapter-timed.
- ByteByteGo, Top 7 Most-Used Distributed System Patterns, Pubsub, 3:35 to 4:18: [watch](https://www.youtube.com/watch?v=nH4qjmP2KEE&t=215s). Pub/sub as one of seven distributed system patterns, in under a minute. Chapter-timed.
- Gaurav Sen, What is the Publisher Subscriber Model?, Publisher Subscriber Model, 1:58 to 3:04: [watch](https://www.youtube.com/watch?v=FMhbR_kQeHw&t=118s). The model introduced as the answer to asynchronous events, before its advantages and drawbacks. Chapter-timed.
- Hussein Nasser, What is a Message Queue and When should you use Messaging Queue Systems Like RabbitMQ and Kafka, Queue vs pub-sub, 10:51 to 13:05: [watch](https://www.youtube.com/watch?v=W4_aGb_MOls&t=651s). Where a queue and a pub-sub topic part ways. Chapter-timed.

**Our plans and chapters**

- [Channels websocket push](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/23-channels-websocket-push.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 23. One `group_send` from the shell lands in two open tabs through the Redis channel layer, a group of subscribers fed by one publish.
- [Message Queue / Pub-Sub / Event-Driven Semantics](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/01-distributed-systems-primitives/plans/06-message-queue-pubsub-event-driven.md), projects/tms-mobility/system-design/plans/01-distributed-systems-primitives, plan 06. The publisher-subscriber model beside queue mechanics and event-driven design.
- [System Design: Message Queues and Streaming](/home/molef/goal-setting/learning/system-design/message-queues-and-streaming/MASTER_PLAN.md), system-design/message-queues-and-streaming. Its first goal builds a point-to-point queue and a pub/sub topic and shows the difference with several consumers.
- [System Design: Notification Systems](/home/molef/goal-setting/learning/system-design/notification-systems/MASTER_PLAN.md), system-design/notification-systems. An event published by an action becomes a notification that a push service consumes and delivers; it holds goals and no plans yet.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/message-queues-and-streaming/artifacts/figures/pub-sub-references/anurag-gharat-pubsub-fanout.jpg"><img src="/home/molef/goal-setting/learning/system-design/message-queues-and-streaming/artifacts/figures/pub-sub-references/anurag-gharat-pubsub-fanout.jpg" width="200" alt="Three publishers sending coloured messages into a broker holding three topics, which delivers them on to four consumers"></a> Anurag Gharat on X, "Pub-Sub": [the post](https://x.com/anurag_gharat/status/2095848853341864229), [what it shows](/home/molef/goal-setting/learning/system-design/message-queues-and-streaming/artifacts/figures/pub-sub-references/README.md#anurag-gharat-pubsub-fanoutjpg). Three publishers send coloured messages into one broker holding Topic 1, Topic 2 and Topic 3, and the broker delivers each topic to its consumers; Topic 3's blue message leaves twice, to consumers 3 and 4.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "pub/sub", "publish-subscribe" and "subscriber" across the system design books. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: Hussein Nasser's Publish-Subscribe Pattern vs Message Queues vs Request Response, whose pub/sub chapter (25:13 to 31:49) repeats his example video. Bare "topic" is not an alias: a sample of 25 learning-tree lines found it means a source topic file in almost all of them. "publisher" (5 lines) and "subscriber" (10 lines) mean this idea in 4 and 8 of them; the `link-skip` phrases cover the VS Code extension publisher and Netflix subscriber accounting.
