---
aliases: [value object, entity, entities, domain entity]
link-skip: [Unprocessable Entity]
link-only-in: [system-design/clean-architecture-in-python]
standard: vault-note v2
---

# Entity And Value Object

Up: [[Software Architecture]]

Information Technology, System Design, Software Architecture. Both live in the innermost layer of [[Clean Architecture]], and the [[Dependency Rule]] keeps them free of any database or framework import.

**An entity is a domain object with an identity that outlives a request (two customers with the same name are still two customers), and a value object has no identity and is equal to any other with the same values (two amounts of R100 are the same amount).**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches entities and value objects writes the rest around it.

## Where to learn this

**Entity and value object**, the two kinds of domain object, told apart by whether identity matters. Also: value object, entity, domain entity.

**Textbooks**

- System design big archive, Key Terms in Domain-Driven Design: [pages 272 to 273](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=272). Evans's definitions: an entity has an ID and a life cycle, a value object has no ID and describes a property of an entity, then aggregates, repositories and factories, ending on how equality differs between the two.
- System design big archive, How Clean Architecture Works?: [page 264](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=264). The clean architecture's own use of "entities": the innermost layer of core business rules, independent of any framework.

**Videos**

- Amichai Mantinband, Aggregates, Entities & Value Objects, Example, 0:36 to 4:41: [watch](https://www.youtube.com/watch?v=UEtmOW8uZZY&t=36s). One domain modelled into entities, value objects and aggregates. Chapter-timed.
- Amichai Mantinband, Aggregates, Entities & Value Objects, Modeling Steps, 6:29 to 7:51: [watch](https://www.youtube.com/watch?v=UEtmOW8uZZY&t=389s). The steps for deciding which noun becomes which. Chapter-timed.

**Our plans and chapters**

- [The fact list: entities and value objects](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/02-the-fact-list.md), system-design/clean-architecture-in-python, plan 2. Every noun the behaviour touches given a one-word verdict, entity or value, with a reason that would survive being argued.
- [Draw the three layers by hand](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/03-draw-the-three-layers.md), system-design/clean-architecture-in-python, plan 3. The entities and value objects from the fact list placed in the domain layer of the first drawing.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The textbook pages were read with pdftotext after a page-text search for "value object" across the five software and system design books. Systems analysis and design indexes "Entity (ERDs)" on pages 252 to 272; those pages teach the database table sense and were left out. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. ByteByteGo, Hello Interview and KodeKloud have no video on the domain sense; Hello Interview's data modelling video covers database entities. Each plan was read at its title, description and purpose. Bare "entity" and "entities" mean a database or ERD entity across most of the learning tree (197 and 324 files, including Attica's architecture-decisions plans), so those words link only inside clean-architecture-in-python, where plan 12's "422 Unprocessable Entity" is listed under `link-skip`.
