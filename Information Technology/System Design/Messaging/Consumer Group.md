---
aliases: [consumer group, Kafka consumer group]
standard: vault-note v2
---

# Consumer Group

Up: [[Messaging]]

Information Technology, System Design. Consumer groups are how [[Apache Kafka]] gives each message to one worker within a group and to every group, which makes one topic both a [[Message Queue]] and [[Publish-Subscribe]].

**A consumer group is a set of consumers that share one subscription: each partition of a topic is read by exactly one member of the group, so the members split the work, while a second group reads the same messages again from its own offsets.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches consumer groups writes the rest around it.

## Where to learn this

**Consumer group**, consumers that split a topic's partitions between them, each group keeping its own place. Also: Kafka consumer group.

**Textbooks**

- System design big archive, How Apache Kafka Works?: [pages 310 to 311](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=310). Follows one message through nine steps, ending with a consumer group that subscribes to the topic and whose members each read different partitions to balance the work.
- System design big archive, Apache Kafka Explained (At the high level): [pages 330 to 331](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=330). Consumer groups named beside producers, topics and partitions, the broker cluster and the controller quorum.

**Videos**

- KodeKloud, 6 Kafka Interview Questions You Must Know (With Answers), Q4: How do consumers split work without overlap?, 3:30 to 5:02: [watch](https://www.youtube.com/watch?v=jOpC3bhWxXU&t=210s). How the consumers in one group divide a topic's partitions so no message is handled twice. Chapter-timed.
- ByteByteGo, Apache Kafka Fundamentals You Should Know, Consumer groups and rebalancing, 2:55 to 3:33: [watch](https://www.youtube.com/watch?v=-RDyEFvnTXI&t=175s). Consumer groups, and the rebalance when a member joins or leaves. Chapter-timed.
- Hussein Nasser, Kafka Consumer Group is a Brilliant Design Choice and We should Discuss it, Consumer Group, 6:55 to 10:00: [watch](https://www.youtube.com/watch?v=e5uAhoT1hhU&t=415s). The consumer group itself, after the chapters on partitioning and on pub/sub against a queue. Chapter-timed.
- Hussein Nasser, Kafka Consumer Group is a Brilliant Design Choice and We should Discuss it, Achieving Pub/Sub with Consumer Group, 11:30 to 14:00: [watch](https://www.youtube.com/watch?v=e5uAhoT1hhU&t=690s). How separate groups turn the same topic into publish-subscribe. Chapter-timed.

**Our plans and chapters**

- [Topic, partition, offset, consumer group](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/16-c1-topics.md), data-engineering/many-sources-one-lakehouse, plan 16. The log drawn as an append-only numbered list with two consumer groups on it at different offsets.
- [Running Kafka: produce and consume by hand](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/18-c2-kafka-by-hand.md), the same journey, plan 18. A keyed producer and a grouped consumer written by hand for 834 transaction rows, with the uneven split across two partitions read off the consumer group.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "consumer group" across the shelf; the big archive holds the only two hits. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: Hello Interview's Kafka System Design Deep Dive, whose 10-minute Overview chapter (8:09 to 18:41) could not be confirmed to cover consumer groups from its chapter list; the Redis use-cases prerequisites in the caching journey, a source reading that mentions Redis Streams consumer groups. The alias is two words, so no ordinary-word sampling was needed.
