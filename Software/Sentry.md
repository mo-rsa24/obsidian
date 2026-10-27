---
aliases: [Sentry, Sentry SDK]
standard: vault-note v2
---

# Sentry

Up: [[Software]]

Software, monitoring. Sentry is one of the tools of [[Observability]]: Attica sends it errors only when SENTRY_DSN is set.

**Sentry is an error-tracking service: an SDK in the application catches each unhandled exception with its stack trace and request, sends it to Sentry, which groups repeats into one issue and alerts the team.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches Sentry writes the rest around it.

## Where to learn this

**Sentry**, the error-tracking service an application reports its exceptions to. Also: Sentry SDK.

**Textbooks**

- System design big archive, 10 Essential Components of a Production Web Application: [page 35](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=35). Monitoring tools such as Sentry, Grafana and Prometheus as one of the ten components, storing logs and helping analyse them.

**Videos**

- Very Academy, Sentry Django Integration, Error Reporting, Sentry, 5:07 to 14:00: [watch](https://www.youtube.com/watch?v=qGghfAmxaGU&t=307s). The SDK added to a Django project and an exception watched arriving as an issue. Chapter-timed.
- Sentry, Sentry 101: Error Monitoring For Backend Applications, Configure SDK, 5:08 to 5:52: [watch](https://www.youtube.com/watch?v=DzhVEK65eYg&t=308s). The SDK's setup from Sentry's own team, before data scrubbing, releases and alerting. Chapter-timed.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27: the textbook page's text, and each video's chapter list read with cache-video-chapters.py. No plan teaches Sentry; the plans that name it do so only in a hover title quoting the same textbook page.
