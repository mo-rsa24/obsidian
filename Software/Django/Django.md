---
aliases: [Django, Django framework, MVT, model-view-template, model view template, Django REST framework, DRF, Django template, Django templates, URL conf, URLconf, ROOT_URLCONF]
standard: vault-note v2
---

# Django

Up: [[Software]]

Software, Python web frameworks. Django is what Attica's backend is built on: its parts here are [[Channels Consumer]], [[Channel Layer]] and [[DRF Serializer]].

**Django is a Python web framework that answers each request by matching its URL to a view, which reads and writes models (one class per database table, through its ORM) and returns what a template or a serializer builds: the model-view-template pattern.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches Django writes the rest around it.

## Where to learn this

**Django**, the Python web framework of models, views and templates. Also: MVT, model-view-template, Django REST framework, DRF.

**Videos**

- Telusko, #9 Django tutorials, Model View Template in Django, Model View Template, 2:33 to 3:10: [watch](https://www.youtube.com/watch?v=GGkFg52Ot5o&t=153s). The three parts named and placed, after a chapter on separation of concerns. Chapter-timed.
- Telusko, the same video, MVT vs MVC, 5:03 to 5:54: [watch](https://www.youtube.com/watch?v=GGkFg52Ot5o&t=303s). Where Django's template stands in for MVC's view and its view for MVC's controller. Chapter-timed.
- Code Stack, How Django Works (MVT Pattern), 0:00 to 1:28: [watch](https://www.youtube.com/watch?v=cyP4Uw2b2XM&t=0s). One request drawn from URL to view to model and template in under a minute and a half. Whole video.

**Our plans and chapters**

- [Django basics, fit for purpose](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/02-django-basics.md), projects/attica/event-creation, rebuild plan 02. Project against app, the urls-to-views-to-settings path, and runserver against daphne, for Attica's own backend.
- [Django, refreshed](/home/molef/goal-setting/learning/system-design/foundations/plans/06-django-refresher.md), system-design/foundations, plan 06. One model written and migrated into the corner shop's orders schema, with the Django admin as the diagram's admin client.
- [User and order in Django](/home/molef/goal-setting/learning/system-design/foundations/plans/13-user-and-order-in-django.md), system-design/foundations, plan 13. Two Django services each reading only its own schema of the shop's PostgreSQL.
- [Chapter 2: The Django app](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/textbook/02-the-django-app.md), ai-engineering/one-business-end-to-end, chapter 2. The shop's Django app built from a template, with models derived from the live schema by inspectdb.
- [Async Django (ASGI/Channels)](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/03-operations-and-delivery/plans/03-async-django-channels.md), projects/tms-mobility. Django under ASGI with Channels, for a persistent WebSocket connection.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27. No shelf book teaches Django: a page-text search found it only as a name in lists (the big archive's API terminology, page 31, and its Instagram design, page 89), so the card has no Textbooks group. No listed creator covers Django, so the videos come from an open search, each chapter list read with cache-video-chapters.py. Each plan's goal paragraph was read.
