---
aliases: [dependency rule, dependency inversion, dependency inversion principle]
standard: vault-note v2
---

# Dependency Rule

Up: [[Software Architecture]]

Information Technology, System Design, Software Architecture. It is the rule that holds [[Clean Architecture]] and [[Ports And Adapters]] together, and [[import-linter]] turns it into a check that fails a build.

**The dependency rule says source code may only import inward: the business rules never name the database, the web framework or any other outer detail, and the outer code depends on interfaces the inner code owns.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the dependency rule writes the rest around it.

## Where to learn this

**Dependency rule**, imports point inward only, so the core never names an outer detail. Also: dependency inversion, dependency inversion principle.

**Textbooks**

- System design big archive, How Clean Architecture Works?: [page 264](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=264). The rule as the clean architecture states it: the dependencies between the four layers always point inward.
- System design big archive, What is the SOLID Principle?: [pages 260 to 261](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=260). The dependency inversion principle, the D in SOLID: high-level modules do not depend on low-level ones, and both depend on abstractions.

**Videos**

- ArjanCodes, Dependency INVERSION vs Dependency INJECTION in Python, Applying dependency inversion, 11:20 to 12:51: [watch](https://www.youtube.com/watch?v=2ejbLVkCndI&t=680s). Dependency inversion applied to a worked Python example, after injection was applied to the same code. Chapter-timed.
- ArjanCodes, Dependency INVERSION vs Dependency INJECTION in Python, Dependency inversion, 1:36 to 2:03: [watch](https://www.youtube.com/watch?v=2ejbLVkCndI&t=96s). The definition, set against dependency injection a chapter earlier. Chapter-timed.
- ByteByteGo, KISS, SOLID, CAP, BASE: Important Terms You Might Not Know!, Solid design principles, 3:16 to 5:37: [watch](https://www.youtube.com/watch?v=cTyZ_hbmbDw&t=196s). The five SOLID principles, dependency inversion among them. Chapter-timed.
- Amichai Mantinband, Understand Clean Architecture in 7 Minutes, Dependency inversion, 5:03 to 5:32: [watch](https://www.youtube.com/watch?v=1OLSE6tX71Y&t=303s). Dependency inversion as the move that turns three tiers into clean architecture. Chapter-timed.
- Valentina (Cupać) Jemuović, Hexagonal Architecture, Episode 2: Ports & Adapters, 0:00 to 1:23:31: [watch](https://www.youtube.com/watch?v=bw7So5GMkyg&t=0s). The argument that hexagonal architecture prescribes dependency inversion rather than layers. Whole video.

**Our plans and chapters**

- [The dependency rule](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/13-the-dependency-rule.md), system-design/clean-architecture-in-python, plan 13. The rule in one sentence, two things it buys, one thing it costs, and a violation spotted by reading imports alone.
- [Watch it refuse](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/21-watch-it-refuse.md), system-design/clean-architecture-in-python, plan 21. A deliberate `import psycopg` in the application layer, refused by `lint-imports`, with the output read to name the contract it broke.
- [Three layers and ports as Protocols](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/03-the-project-and-the-hexagon.md#33-three-layers-and-ports-as-protocols), ai-engineering/prototype-product-data-validation-end-to-end, chapter 3.3. The rule applied to four collaborators, each reached through a port the application owns.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The textbook pages were read with pdftotext after a page-text search for "dependency rule" and "dependency inversion" across the five software and system design books; the Systems analysis and design hits for "dependency rule" (pages 272 and 276) are about data flow diagrams and were left out. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. ByteByteGo's SOLID chapter is the one video from the three named creators; Hello Interview and KodeKloud have none. Left out: ArjanCodes' one-minute dependency inversion tip (`8T9vJ3U1VEI`), which the longer video covers. Each plan was read at its title, description and goal. None of the card's words is a single ordinary English word, so they link everywhere; the 19 learning-tree files using "dependency rule" all mean this rule.
