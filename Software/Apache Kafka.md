---
aliases: [Apache Kafka, Kafka]
standard: vault-note v2
---

# Apache Kafka

Up: [[Software]]

Software. Kafka is often used as a [[Message Queue]] and for [[Publish-Subscribe]], though it keeps every message in a log instead of deleting it once read; [[Redis]] is the other store our plans use for messaging.

**Apache Kafka is a distributed event streaming platform: producers append messages to ordered, partitioned topic logs kept on a cluster of brokers, and consumer groups read them at their own pace by offset, able to replay from any point.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches Kafka writes the rest around it.

## Where to learn this

**Apache Kafka**, an append-only, partitioned event log read by offset. Also: Kafka.

**Textbooks**

- System design big archive, How Apache Kafka Works?: [pages 310 to 311](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=310). Follows one message through nine steps, from a producer's click or payment event through the serializer, the partitioner and the replicated brokers to a consumer group whose members each read different partitions.
- System design big archive, Apache Kafka vs. RabbitMQ: [pages 419 to 420](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=419). Kafka as a distributed log whose messages stay until the retention policy removes them, set against RabbitMQ, a broker that deletes a message once it is acknowledged.
- System design big archive, Apache Kafka Explained (At the high level): [pages 330 to 331](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=330). The parts named once each: producers, topics and partitions, the broker cluster, the KRaft controller quorum and consumer groups.

**Videos**

- Hello Interview, Kafka System Design Deep Dive, Motivating Example, 1:53 to 8:09: [watch](https://www.youtube.com/watch?v=DU8o-OTeoCc&t=113s). A concrete case that needs Kafka, worked before the overview, by a former Meta staff engineer. Chapter-timed.
- ByteByteGo, System Design: Apache Kafka In 3 Minutes, Kafka core architecture, 0:32 to 1:01: [watch](https://www.youtube.com/watch?v=HZklgPkboro&t=32s). The architecture in half a minute, followed by use cases and limitations. Chapter-timed.
- ByteByteGo, Apache Kafka Fundamentals You Should Know, Topics and partitions, 1:05 to 1:35: [watch](https://www.youtube.com/watch?v=-RDyEFvnTXI&t=65s). How a topic is split into partitions, before producers, consumer groups and brokers. Chapter-timed.
- Gaurav Sen, Apache Kafka: a Distributed Messaging System for Log Processing, High-Level Design, 1:47 to 4:36: [watch](https://www.youtube.com/watch?v=hNDjd9I_VGA&t=107s). Kafka's design drawn from the original paper, before scaling and the three delivery guarantees. Chapter-timed.

**Our plans and chapters**

- [Running Kafka: produce and consume by hand](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/18-c2-kafka-by-hand.md), data-engineering/many-sources-one-lakehouse, plan 18. A broker in Docker, a topic you create, and a producer and a consumer you write, carrying rows of the seeded transaction data.
- [Topic, partition, offset, consumer group](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/16-c1-topics.md), the same journey, plan 16. The four words every later Debezium message rests on, fixed by drawing the log as an append-only numbered list with a reader's position on it.
- [Debezium: the connector, configured](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/22-c5-connector.md), the same journey, plan 22. Kafka Connect with one connector registered by POSTing its JSON configuration, and the topics it creates by itself.
- [System Design: Message Queues and Streaming](/home/molef/goal-setting/learning/system-design/message-queues-and-streaming/MASTER_PLAN.md), system-design/message-queues-and-streaming. Sets point-to-point queues against a Kafka-style event log and builds a windowed stream job; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext; the chapter tables in `Textbooks.md` gave the three big archive sections. System design interview names Kafka only in a reference list (pages 218 to 219). Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: Hussein Nasser's What is Kafka and How does it work? and Apache Kafka Crash Course, and KodeKloud's Kafka videos, which cover the same parts at greater length; the compiled chapter section 19.4 in system-design/foundations ("What Kafka would do differently"), which is a heading with no text yet. "Kafka" is an ordinary dictionary word (the novelist), and the learning tree uses it only for this software.
