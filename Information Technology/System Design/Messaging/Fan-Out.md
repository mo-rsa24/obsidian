---
aliases: [fan-out on write, fan-out on read, fanout on write, fanout on read, fan-out on load, fanout-on-write, fanout-on-load, fanout service, fan-out service, write-time fan-out, read-time fan-out, fan-out to followers, fan-out behavior, fan-out design decision, fan-out choice, fan-out diagram]
link-not: [Fan-Out]
standard: vault-note v2
---

# Fan-Out

Up: [[Messaging]]

Information Technology, System Design. [[Publish-Subscribe]] is the messaging pattern that does the copying, usually through a [[Message Queue]] that fanout workers drain, and a [[Cache]] holds the feeds it writes.

**Fan-out is delivering one event to many recipients, as when one post is copied into the feed of every follower; a design chooses to do that work when the post is written or when each feed is read.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches fan-out writes the rest around it.

## Where to learn this

**Fan-out**, one event delivered to many recipients, on write or on read. Also: fanout, fan-out on write, fan-out on read, fanout service, write-time fan-out, read-time fan-out.

**Textbooks**

- System design interview, chapter 11, Design a news feed system, Fanout service: [pages 172 to 173](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=172). Works the news feed both ways: fanout on write pre-computes every friend's feed and suffers the hotkey problem, fanout on read pulls on demand, and the hybrid pushes for most users and lets a celebrity's followers pull; then the five steps of the fanout service through a message queue into the feed cache.
- Grokking the system design interview, section 9.2, Feed publishing: [page 10](../../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=10). The pull model (fan-out-on-load) and the push model (fan-out-on-write), what each costs, and the hybrid that stops pushing for users with millions of followers.
- System design big archive, How RabbitMQ Works?: [page 207](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=207). The broker's fanout exchange, which copies every message to all bound queues regardless of routing key.

**Videos**

- Gaurav Sen, Designing INSTAGRAM: System Design of News Feed, Celebrity post fanout, 21:32 to 24:29: [watch](https://www.youtube.com/watch?v=QmX2NPkJTKg&t=1292s). The celebrity case that breaks fanout on write, at the end of a news feed design worked on a whiteboard. Chapter-timed.
- Hello Interview, System Design Interview Walkthrough: Design Twitter, Building the timeline, 14:07 to 16:48: [watch](https://www.youtube.com/watch?v=Nfa-uUHuFHg&t=847s). The timeline step of a full Twitter design worked end to end. Chapter-timed.
- ByteByteGo, FAANG System Design Interview: Design A Chat System, Group chat fan-out, 5:33 to 6:02: [watch](https://www.youtube.com/watch?v=okrR1KXNLtA&t=333s). Fan-out inside a chat design: one group message delivered to every member. Chapter-timed.

**Our plans and chapters**

- [Channels websocket push](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/23-channels-websocket-push.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 23. Two browser tabs manufacture the fan-out: one `group_send` reaches both through the Redis channel layer.
- [System Design Applications: How Twitter Works](/home/molef/goal-setting/learning/system-design/applications/how-twitter-works/MASTER_PLAN.md), system-design/applications/how-twitter-works. The tweet-publish flow fans each tweet out to followers' timelines, the toy system has to justify its write-time or read-time choice, and a follow updates the fan-out service; it holds goals and no plans yet.
- [System Design: Consistency and Distributed Systems](/home/molef/goal-setting/learning/system-design/consistency-and-distributed-systems/MASTER_PLAN.md), system-design/consistency-and-distributed-systems. Treats write-time against read-time fan-out as a consistency decision in disguise; it holds goals and no plans yet.
- [System Design: Message Queues and Streaming](/home/molef/goal-setting/learning/system-design/message-queues-and-streaming/MASTER_PLAN.md), system-design/message-queues-and-streaming. Its first goal shows the different fan-out of a queue and a pub/sub topic to several consumers.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "fan-out" and "fanout" across the system design books. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: the "Fan-out" entries in Systems analysis and design's index (pages 414 and 416, the number of modules one program module calls) and in both Probabilistic machine learning books (a network layer's inputs), which are other ideas; Hayk Simonyan's Design Twitter (X), whose chapters do not name fan-out; Hello Interview's Design FB News Feed, whose deep dives (16:17 to 25:48) are not titled by topic; one-business-end-to-end plan 16, whose "discount fan-out" is a join duplicating rows. The bare word is dropped with `link-not`: a sample of 25 learning-tree lines found "fan-out" means that join duplication in about 17 of them (the one-business-end-to-end journey), so only the multi-word names link. On 2026-10-24 the bare word was read in all 72 prose lines of the learning tree: outside system-design it is mostly that join duplication (one-business-end-to-end, dimensional-modelling, data-agents), and inside system-design 14 of 24 lines mean this card's idea while the rest are an API gateway splitting one request across services, a query sent to every shard, or a load balancer spreading clients. `link-only-in` cannot scope a hyphenated word, so the card instead gained the multi-word phrases the system-design journeys use for its idea (fan-out service, write-time and read-time fan-out, fan-out to followers, fan-out behavior, the fan-out design decision or choice, a fan-out diagram), each checked to mean one event copied to many recipients in every use. The how-twitter-works master plan was read at its mission and objectives; the shelf's news feed chapters (System design interview pages 166 to 173, Grokking section 9) hold nothing beyond the pages already listed.
