---
aliases: [ORM, object-relational mapping, object relational mapping, object-relational mapper, object relational mapper]
standard: vault-note v2
---

# Object-Relational Mapping

Up: [[Database Systems]]

Information Technology, Database Systems. An ORM maps classes onto the tables of a [[Relational Database]] and writes the [[Database Schema]] migrations when a class changes.

**An object-relational mapping (ORM) lets code work with database rows as objects: each class is a table and each attribute a column, and the ORM writes the SQL for every query and save, so the programmer has to read that SQL to know what actually runs.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the ORM writes the rest around it.

## Where to learn this

**Object-relational mapping**, classes mapped onto tables so code queries objects. Also: ORM, object-relational mapper.

**Videos**

- Patrick God, Object-Relational Mapping Explained for EVERYONE (with Code Examples), Add the Object-Relational Mapper/ORM Entity Framework 7, 1:36 to 2:35: [watch](https://www.youtube.com/watch?v=c2K5QRYjmeA&t=96s). Adding an ORM to a small web API, before chapters on code-first migrations and the table it maps to in SQL Server. Chapter-timed.
- BugBytes, Django ORM Deep Dive - Models, Migrations and Admin UI Integration, Building Django models, 2:55 to 6:19: [watch](https://www.youtube.com/watch?v=t7diJPGxCGo&t=175s). Django's ORM models built as Python classes, the video our Django plans already link. Chapter-timed.

**Our plans and chapters**

- [Read the SQL the ORM emits](/home/molef/goal-setting/learning/projects/attica/architecture-decisions/plans/01-read-sql.md), projects/attica/architecture-decisions, plan 01. Works it on Attica: the SQL Django emits for the accept-path queryset printed, read line by line, and written again as raw SQL to confirm the columns match.
- [ORM aggregates: revenue by branch, and the discount fan-out reproduced in the ORM](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/16-orm-aggregates-and-the-discount-fan-out.md), ai-engineering/one-business-end-to-end, plan 16. Revenue by branch predicted, produced with `values` and `annotate`, and a discount summed once per line instead of once per sale reproduced in the ORM.
- [The ORM aggregate, and the discount fan-out reproduced live](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/textbook/02-the-django-app.md#26-the-orm-aggregate-and-the-discount-fan-out-reproduced-live), the same journey, chapter 2, section 2.6. The same aggregate written out against the shop's own figures.
- [The ORM calling net_revenue() against computing the same figure in Python](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/17-the-orm-calling-net-revenue.md), the same journey, plan 17. A database function called from Django two ways and matched to the cent against the same figure computed in Python.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No textbook on the shelf teaches object-relational mapping: a page-text search for "ORM", "object-relational" and "SQLAlchemy" found only Systems analysis and design's object databases, a different idea, so the card has no Textbooks group. No creator in the topic routing has an ORM video in the cached upload lists; the BugBytes video is the one our plans link, and the Patrick God video was found by a YouTube search. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title and description, and the chapter section at its first lines. "SQLAlchemy ORM" is not an alias: the learning tree uses "SQLAlchemy" only for a package the ADK database extra installs.
