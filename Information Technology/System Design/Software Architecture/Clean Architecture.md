---
aliases: [clean architecture, the three layers, controller and presenter, controller, presenter, interface adapters]
link-skip: [the three layers (schema, through the three layer]
link-only-in: [system-design/clean-architecture-in-python]
standard: vault-note v2
---

# Clean Architecture

Up: [[Software Architecture]]

Information Technology, System Design, Software Architecture. Its layers hold [[Entity And Value Object]] types and [[Use Case]] classes, the [[Dependency Rule]] says which way they may import, and [[Ports And Adapters]] is the same idea drawn as a hexagon.

**Clean architecture arranges an application in rings, with the business rules at the centre and the web, the database and other frameworks outside, so that every source dependency points inward and the rules can be built and tested without the outside.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches clean architecture writes the rest around it.

## Where to learn this

**Clean architecture**, business rules at the centre and frameworks outside, with dependencies pointing inward. Also: the three layers (domain, application, infrastructure), controller, presenter, interface adapters.

**Textbooks**

- System design big archive, How Clean Architecture Works?: [page 264](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=264). The four layers (entities, use cases, interface adapters with their controllers and presenters, frameworks and drivers) and the rule that dependencies always point inward.
- Systems analysis and design, chapter 8, Architecture design, elements of an architecture design: [page 309](../../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=309). The older split every system is cut into: data storage, data access logic, application logic and presentation logic, which the clean architecture's layers rearrange around the application logic.

**Videos**

- Amichai Mantinband, Understand Clean Architecture in 7 Minutes, Clean architecture principles, 3:15 to 5:03: [watch](https://www.youtube.com/watch?v=1OLSE6tX71Y&t=195s). The principles, after a three-tier version of the same example. Chapter-timed.
- Amichai Mantinband, Understand Clean Architecture in 7 Minutes, Layer breakdown, 5:32 to 6:52: [watch](https://www.youtube.com/watch?v=1OLSE6tX71Y&t=332s). What each layer holds. Chapter-timed.
- ByteByteGo, Top 5 Most Used Architecture Patterns, 0:34 to 1:25: [watch](https://www.youtube.com/watch?v=f6zXyq4VPP8&t=34s). Plain layered architecture, presentation, business and data each calling only the one below, which is the arrangement clean architecture inverts. Chapter-timed.
- ArjanCodes, Stop Mixing FastAPI with Business Logic: Fix It with Ports & Adapters, Step 6: FastAPI Adapter Becomes Translation-Only, 24:36 to 24:48: [watch](https://www.youtube.com/watch?v=FXwBWS4qDAA&t=1476s). The route handler reduced to translation, which is the controller's whole job. Chapter-timed.

**Our plans and chapters**

- [Draw the three layers by hand](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/03-draw-the-three-layers.md), system-design/clean-architecture-in-python, plan 3. Each piece of the service placed in domain, application or infrastructure on paper before any code exists.
- [Controller and presenter](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/19-controller-and-presenter.md), system-design/clean-architecture-in-python, plan 19. The route handler cut down to parsing, validation, one use case call and translating the result, with the no-match case mapped to its status code there.
- [The three layers](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/textbook/06-the-rules-engine.md#61-the-three-layers), ai-engineering/product-data-validation-end-to-end, chapter 6.1. Three packages and one import rule: `domain/` imports only the standard library, `application/` holds the use case and its ports, `infrastructure/` touches the world.
- [Three layers and ports as Protocols](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/plans/archived/16-layers-and-ports.md), ai-engineering/prototype-product-data-validation-end-to-end, plan 16. An empty package given its three layers and the four ports named on paper.
- [Draw it again](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/23-draw-it-again.md), system-design/clean-architecture-in-python, plan 23. The three layers redrawn from the finished service and set beside the first drawing to find every difference.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The textbook pages were read with pdftotext: the big archive's page 264 came from a page-text search for "clean architecture" (its other hits, pages 67, 162, 224 and 345, only name the book in reading lists), and the Systems analysis and design page from a search for "data access logic". Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. ByteByteGo's layered architecture row is the one the journey's video pulse of 2026-10-24 placed; Hello Interview and KodeKloud have no video on the idea. Each plan and chapter was read at its title and description. "Controller" and "presenter" mean an SDN controller, a game controller or a person presenting elsewhere in the learning tree (65 and 26 files), so those single words link only inside clean-architecture-in-python. "The three layers" is kept with its article because bare "three layers" also counts neural network layers in the transformers journey; the two remaining lines where it means something else (a RAG chapter's schema, signature and role, and a deep-learning plan's network layers) are listed under `link-skip`.
