---
aliases: [consistent hashing, hash ring]
standard: vault-note v2
---

# Consistent Hashing

Up: [[Scaling]]

Information Technology, System Design. Consistent hashing is how [[Sharding]] and a distributed [[Cache]] pick a server for each key, so a [[Load Balancer]] or a client can add servers without moving most keys.

**Consistent hashing places servers and keys on the same ring of hash values and stores each key on the first server clockwise from it, so adding or removing a server moves only about k/n of the k keys instead of nearly all of them.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches consistent hashing writes the rest around it.

## Where to learn this

**Consistent hashing**, a hash ring that moves few keys when servers change. Also: hash ring, virtual nodes.

**Textbooks**

- System design interview, chapter 5, Design consistent hashing: [pages 71 to 85](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=71). Works the rehashing problem with numbers (8 keys on 4 servers by `hash(key) % 4`, then most keys moving when one server goes offline), then the hash ring, adding and removing a server, and virtual nodes that even out the load.
- Grokking the system design interview, section 18, Consistent hashing: [pages 22 to 24](../../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=22). Why `key % n` breaks a distributed cache when a host is added, then the ring algorithm where only k/n keys are remapped.
- System design interview, chapter 6, Data partition: [pages 93 to 94](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=93). Consistent hashing reused to partition a key-value store across eight servers, with virtual nodes sized to each server's capacity.

**Videos**

- ByteByteGo, Consistent Hashing | Algorithms You Should Know #1, Insight of Consistent Hashing, 2:43 to 4:50: [watch](https://www.youtube.com/watch?v=UF9Iqmg94tk&t=163s). The ring idea, after the chapters on what consistent hashing is and what it aims for. Chapter-timed.
- Hello Interview, Consistent Hashing: Easy Explanation for System Design Interviews, How consistent hashing works, 3:01 to 5:10: [watch](https://www.youtube.com/watch?v=vccwdhfqIrI&t=181s). The ring, right after a chapter on what goes wrong with modulo hashing. Chapter-timed.
- Gaurav Sen, What is CONSISTENT HASHING and Where is it used?, Virtual Servers, 7:01 to 9:40: [watch](https://www.youtube.com/watch?v=zaRkONvyGr8&t=421s). Virtual servers on the whiteboard, the fix for an uneven ring. Chapter-timed.
- Arpit Bhayani, Consistent Hashing and Its Implementation From the First Principles, 0:00 to 13:55: [watch](https://www.youtube.com/watch?v=Jvimt56KPnk&t=0s). The ring derived and then implemented from scratch. Whole video.

**Our plans and chapters**

- [Consistent Hashing: Math](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/04-dispatch-integration-and-architecture/plans/01-consistent-hashing-math.md), projects/tms-mobility/system-design/plans/04-dispatch-integration-and-architecture, plan 01. Hash-ring placement derived by hand before any code.
- [Consistent Hashing: Mechanism](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/04-dispatch-integration-and-architecture/plans/02-consistent-hashing-mechanism.md), the same journey, plan 02. Consistent hashing implemented with virtual nodes, showing how few keys move when a server is added or removed.
- [Hash Tables & the Modulo-Sharding Resize Problem](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/01-distributed-systems-primitives/plans/03-hash-tables-resize-problem.md), projects/tms-mobility/system-design/plans/01-distributed-systems-primitives, plan 03. Why naive modulo sharding breaks when the server count changes, the problem consistent hashing solves.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext, found through the chapter tables in `Textbooks.md` and a page-text search for "consistent hash" and "hash ring" across the system design books. Each video's chapter list was read with `cache-video-chapters.py` (Arpit Bhayani's video has none and is cited whole), and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: the System design big archive's "12 algorithms for system design interviews" (page 59), which names consistent hashing in one line; Hayk Simonyan's Load Balancers Explained chapter "Consistent Hashing", a one-minute mention at the end of a load-balancing video.
