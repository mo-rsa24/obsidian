---
aliases: [saga, saga pattern, compensating transaction, compensating action]
standard: vault-note v2
---

# Saga Pattern

Up: [[System Design]]

Information Technology, System Design. Each step of a saga is one local [[Database Transaction]] in one of the [[Microservices]], and its events often leave through the [[Outbox Pattern]]. The placement is unsure: this note may move into a consistency folder beside [[Eventual Consistency]].

**A saga carries out one business operation across several services as a sequence of local transactions, each committed on its own; when a later step fails, the saga runs a compensating transaction for every step already done, so the system ends consistent without one transaction spanning every database.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches sagas writes the rest around it.

## Where to learn this

**Saga pattern**, a chain of local transactions undone step by step by compensating transactions when one fails. Also: saga, compensating transaction, compensating action.

**Videos**

- Hello Interview, Distributed Transactions Explained: 2 Phase Commit vs Saga Pattern, The saga pattern, 5:52 to 7:23: [watch](https://www.youtube.com/watch?v=DOFflggE_0Q&t=352s). A saga of local transactions with compensations. Chapter-timed.
- Hello Interview, Distributed Transactions Explained: 2 Phase Commit vs Saga Pattern, Implementing compensation, 9:40 to 11:06: [watch](https://www.youtube.com/watch?v=DOFflggE_0Q&t=580s). Writing the compensating step that undoes a committed one. Chapter-timed.
- Hello Interview, Distributed Transactions Explained: 2 Phase Commit vs Saga Pattern, Choreography vs orchestration, 7:23 to 8:31: [watch](https://www.youtube.com/watch?v=DOFflggE_0Q&t=443s). The two ways to drive a saga: services reacting to each other's events, or one orchestrator calling each in turn. Chapter-timed.
- Hello Interview, Distributed Transactions Explained: 2 Phase Commit vs Saga Pattern, The two-phase commit flaw, 2:33 to 5:52: [watch](https://www.youtube.com/watch?v=DOFflggE_0Q&t=153s). Why two-phase commit, which holds every participant until all agree, is the problem a saga avoids. Chapter-timed.
- Hello Interview, Distributed Transactions Explained: 2 Phase Commit vs Saga Pattern, Choosing the right strategy, 12:23 to 14:46: [watch](https://www.youtube.com/watch?v=DOFflggE_0Q&t=743s). When to pick a saga, two-phase commit, or neither. Chapter-timed.

**Our plans and chapters**

- [System Design: Consistency and Distributed Systems](/home/molef/goal-setting/learning/system-design/consistency-and-distributed-systems/MASTER_PLAN.md), system-design/consistency-and-distributed-systems. Goal 4: the same multi-service operation built as a two-phase commit and as a saga with compensating actions, compared when one participant fails mid-operation; it holds goals and no plans yet.
- [System Design: Microservices](/home/molef/goal-setting/learning/system-design/microservices/MASTER_PLAN.md), system-design/microservices. Goal 4: one local transaction rebuilt across two services, with the partial failure handled by a saga or compensating action; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No shelf book teaches sagas: a page-text search for "saga", "compensating transaction", "distributed transaction", "two-phase commit" and "choreography" across every system design and software engineering book found only a "family saga" analogy in the networking book (page 220) and unrelated uses of "two-phase", and no back-of-book index lists the word. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title, the video title and, for the first line, the segment note in `system-design/foundations/video-scout/pulse-2026-10-24.md`. Each master plan was read at its objectives and goals. Left out: Hussein Nasser's What is a Distributed Transaction in Microservices?, members-only; ByteByteGo's Top 7 Most-Used Distributed System Patterns, whose chapter list names no saga; the Attica architecture-decisions scope, whose master plan lists three saga sources as not matched to any objective; foundations plan 19, which names the saga video only for its outbox chapter. The bare word "saga" was sampled across the learning tree: all 16 prose uses mean this pattern, so it links everywhere.
