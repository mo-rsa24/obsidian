---
aliases: [use case, use case interactor, interactor]
link-skip: [use cases, "example, use case", "intuition, use case", "use case, user needs", questions from the use case, questions in the use case, suppliers in the use case, derived from the use case, section from the use case, the use case's, shop's use case, use case has a second, use case words, use case names, use case leaves, open the use case, from a use case, start at the use case, written as a use case, use case scenario, use case explains, per the use case, failures and the use case, failures and use case, email use case, Redis use case, real use case, third use case, our use case, dispatch use case, use case. Every number, as the use case, each a use case, Managed by | Use case, use-case list, use-case icons, its use-case, a named use case, production use case, For this use case, applied use case, The use case demands]
standard: vault-note v2
---

# Use Case

Up: [[Software Architecture]]

Information Technology, System Design, Software Architecture. It sits in the application layer of [[Clean Architecture]], reaches the outside only through the ports of [[Ports And Adapters]], and is built by the [[Composition Root]].

**A use case is one class in the application layer that carries out one thing the application does: it takes its ports in its constructor, holds the business rule, and returns a plain result, so it can be built and tested with no database and no network.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the use case writes the rest around it.

## Where to learn this

**Use case**, the application-layer class that performs one operation through ports. Also: use case interactor, interactor.

**Textbooks**

- System design big archive, How Clean Architecture Works?: [page 264](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=264). Use cases as the second layer: the specific operations the application performs, moving data between entities and the outside without caring how it is shown or stored.
- Systems analysis and design, chapter 4, Use case analysis: [page 175](../../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=175). The older requirements sense the clean architecture's word grew from: a use case as the activities a system performs when an outside user triggers an event, such as renting a DVD.

**Videos**

- ArjanCodes, Stop Mixing FastAPI with Business Logic: Fix It with Ports & Adapters, Step 4: Write the Use Case as Pure Logic, 14:39 to 19:25: [watch](https://www.youtube.com/watch?v=FXwBWS4qDAA&t=879s). The use case written in Python as logic that calls only its port. Chapter-timed.
- Amichai Mantinband, Understand Clean Architecture in 7 Minutes, Layer breakdown, 5:32 to 6:52: [watch](https://www.youtube.com/watch?v=1OLSE6tX71Y&t=332s). Where the application layer and its use cases sit among the other layers. Chapter-timed.

**Our plans and chapters**

- [The use case](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/15-the-use-case.md), system-design/clean-architecture-in-python, plan 15. The business rule lifted out of the route handler into `CategoriseTransaction`, which takes ports in its constructor and builds with both ports set to `None`.
- [Application tests with no database](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/17-application-tests-with-no-database.md), system-design/clean-architecture-in-python, plan 17. The use case tested against fakes only, match and no-match paths green in under five seconds with Postgres stopped.
- [Three layers and ports as Protocols](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/03-the-project-and-the-hexagon.md#33-three-layers-and-ports-as-protocols), ai-engineering/prototype-product-data-validation-end-to-end, chapter 3.3. A use case returning one result per catalogue row, S01, S02 and S09, through four ports.
- [The three layers](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/textbook/06-the-rules-engine.md#61-the-three-layers), ai-engineering/product-data-validation-end-to-end, chapter 6.1. The use case and its ports placed in `application/`, between a domain that imports nothing and infrastructure that touches the world.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The big archive page came from a page-text search for "use case"; the Systems analysis and design page came from its back-of-book index ("Use cases, defined", pages 174 and 537) and was read with pdftotext. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. ByteByteGo, Hello Interview and KodeKloud have no video on the application-layer use case. Each plan and chapter was read at its title, description and its lines on the use case. "Use case" is two words, so `link-only-in` cannot scope it and it links everywhere. Across the learning tree it also means a requirements scenario (the one-business and data-agents journeys, about 30 lines), a row label in the maths video tables ("Worked example, use case"), and a plain "what it is used for" (Redis use cases); the plural is always the ordinary sense. Those lines carry the phrases under `link-skip`.
