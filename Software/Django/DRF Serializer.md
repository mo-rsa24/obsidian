---
aliases: [DRF Serializer, DRF serializer, DRF serializers, Django REST framework serializer, ModelSerializer, serializer, serializers]
link-skip-in: [data-engineering/]
standard: vault-note v2
---

# DRF Serializer

Up: [[Django]]

Software, Django. A serializer is the API's half of a Django view: what a [[REST API]] endpoint returns and accepts, the way a template is the HTML half.

**A Django REST framework serializer turns model instances into JSON-ready data for a response and turns incoming JSON back into validated data a view can save; a ModelSerializer builds its fields from the model.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches serializers writes the rest around it.

## Where to learn this

**DRF serializer**, what turns models into an API's JSON and validates what comes back. Also: ModelSerializer, Django REST framework serializer.

**Videos**

- BugBytes, Django REST Framework, Serializers & Response objects, Creating a ModelSerializer with REST Framework, 1:00 to 6:56: [watch](https://www.youtube.com/watch?v=BMym71Dwox0&t=60s). A ModelSerializer written for a model and run in the shell, its fields read from the model. Chapter-timed.
- BugBytes, the same video, Field level validation on serialisers, 6:56 to 9:42: [watch](https://www.youtube.com/watch?v=BMym71Dwox0&t=416s). The other direction: incoming data checked field by field before it is saved. Chapter-timed.
- Dennis Ivy, Django Rest Framework, Serializers & CRUD, Serializing data, 8:05 to 12:37: [watch](https://www.youtube.com/watch?v=TmsD8QExZ84&t=485s). A serializer feeding the list and detail views of a small API. Chapter-timed.

**Our plans and chapters**

- [The DRF draft endpoint](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/11-drf-draft-endpoint.md), projects/attica/event-creation, rebuild plan 11. Attica's draft serializer and endpoint built twice, as a function view and then as a ViewSet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27. No shelf book teaches Django REST framework, so the card has no Textbooks group. Each video's chapter list was read with cache-video-chapters.py; the plan's goal paragraph was read. The data-engineering journeys use "serializer" for Kafka's message serializers, so the card's single words stay plain there (link-skip-in).
