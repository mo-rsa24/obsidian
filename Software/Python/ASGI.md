---
aliases: [ASGI, ASGI server, ASGI servers, ASGI application, WSGI, Daphne, Asynchronous Server Gateway Interface]
standard: vault-note v2
---

# ASGI

Up: [[Python]]

Software, Python. ASGI is what lets [[Django]] hold a [[WebSocket]] open: Daphne, the server Attica runs, speaks ASGI and hands each connection to Django's router.

**ASGI (Asynchronous Server Gateway Interface) is the Python standard between a web server and an application for asynchronous traffic: unlike WSGI, which answers one request with one response, it carries long-lived connections such as WebSockets; Daphne and Uvicorn are ASGI servers.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches ASGI writes the rest around it.

## Where to learn this

**ASGI**, the Python server-to-application standard for asynchronous connections. Also: WSGI, ASGI server, Daphne.

**Videos**

- Jerin Jose, WSGI & ASGI Simplified, WSGI ASGI, 0:30 to 2:15: [watch](https://www.youtube.com/watch?v=LtpJup6vcS4&t=30s). The two interfaces side by side, the server on one side and the app on the other. Chapter-timed.
- Jerin Jose, the same video, ASGI Workers, 3:30 to 5:22: [watch](https://www.youtube.com/watch?v=LtpJup6vcS4&t=210s). How one ASGI worker serves many connections at once, after WSGI's one-request-per-worker. Chapter-timed.

**Our plans and chapters**

- [Daphne under systemd](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/24-daphne-under-systemd.md), projects/attica/event-creation, rebuild plan 24. Daphne made survivable: a unit file from zero, killed with -9 and watched coming back.
- [nginx in front of two Daphnes](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/25-nginx-load-balancer.md), projects/attica/event-creation, rebuild plan 25. Two Daphne containers behind nginx, one killed mid-traffic, and what WebSockets demand that plain HTTP does not.
- [Django basics, fit for purpose](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/02-django-basics.md), projects/attica/event-creation, rebuild plan 02. runserver against daphne, the WSGI and ASGI difference as Attica meets it.
- [Async Django (ASGI/Channels)](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/03-operations-and-delivery/plans/03-async-django-channels.md), projects/tms-mobility. Django under ASGI with Channels for a persistent connection.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27. No shelf book teaches ASGI (a page-text search found the letters only inside an unrelated word), so the card has no Textbooks group. The video's chapter list was read with cache-video-chapters.py; each plan's goal paragraph was read.
