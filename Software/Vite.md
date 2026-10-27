---
aliases: [Vite, Vite dev server, Vite proxy]
standard: vault-note v2
---

# Vite

Up: [[Software]]

Software, front-end tooling. Vite serves Attica's [[React]] app while it is developed and forwards its API and WebSocket calls to Django, a small [[Reverse Proxy]] for one developer.

**Vite is a JavaScript build tool and development server: while you develop it serves your source files straight to the browser as native modules and updates the page on every save, it can proxy chosen paths to a backend, and it bundles the app for production.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches Vite writes the rest around it.

## Where to learn this

**Vite**, the JavaScript build tool and development server. Also: Vite dev server, Vite proxy.

**Videos**

- Fireship, Vite in 100 Seconds, How Vite works, 0:37 to 1:01: [watch](https://www.youtube.com/watch?v=KCrXgy8qtjM&t=37s). Native ES modules served unbundled while developing, against the bundlers before it. Chapter-timed.
- Fireship, the same video, Local development, 1:31 to 1:55: [watch](https://www.youtube.com/watch?v=KCrXgy8qtjM&t=91s). The dev server and its hot reload. Chapter-timed.

**Our plans and chapters**

- [The Vite proxy and CORS](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/13-vite-proxy-and-cors.md), projects/attica/event-creation, rebuild plan 13. The wizard wired to the backend three ways: broken cross-origin, fixed with CORS, made moot with Vite's proxy, and the dead /ws lane shown.
- [Connect frontend to backend, Postman first](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/03-connect-and-postman.md), projects/attica/event-creation, rebuild plan 03. The React app on Vite reaching the Django API.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27. No shelf book teaches Vite, so the card has no Textbooks group. The video's chapter list was read with cache-video-chapters.py; each plan's goal paragraph was read.
