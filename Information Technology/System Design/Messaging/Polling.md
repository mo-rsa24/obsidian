---
aliases: [polling, long polling, short polling, long poll, poller]
link-skip: [yes/no polling]
standard: vault-note v2
---

# Polling

Up: [[Messaging]]

Information Technology, System Design. A [[Webhook]] and a [[WebSocket]] are the two ways to stop polling: the first has the other side call you, the second keeps one connection open for the server to push on.

**Polling is a client asking a server again and again whether anything has changed; long polling keeps each request open until there is news or a timeout, so the answer arrives sooner and fewer requests come back empty.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches polling writes the rest around it.

## Where to learn this

**Polling**, asking again and again instead of being told. Also: long polling, short polling, poller.

**Textbooks**

- System design interview, chapter 12, Design a chat system, Polling and Long polling: [pages 180 to 182](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=180). Polling and then long polling as two ways to fake a server-initiated message, with long polling's three drawbacks: the sender may reach a different server, the server cannot tell a client has gone, and quiet users still reconnect after every timeout.
- System design big archive, Can a web server provide real-time updates?: [pages 425 to 426](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=425). Short polling, where the browser keeps asking, against long polling, where the server holds the answer until new data arrives, beside WebSocket and server-sent events.
- System design interview, chapter 15, Design Google Drive, Notification service: [pages 259 to 260](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=259). Chooses long polling over WebSocket for file-change notifications because they are rare and one-way, and walks a client reopening its long poll after each change or timeout.

**Videos**

- ByteByteGo, Top 3 Things You Should Know About Webhooks!, Polling vs long polling, 0:42 to 1:30: [watch](https://www.youtube.com/watch?v=x_jjhcDrISk&t=42s). The two kinds of polling a webhook is set against. Chapter-timed.
- Hussein Nasser, The genius of long polling, Long Polling, 3:50 to 8:18: [watch](https://www.youtube.com/watch?v=5aRamFLgtis&t=230s). Long polling explained right after the chapters on plain polling and its problem, followed by its timeouts. Chapter-timed.
- Hussein Nasser, Long Polling and how it differs from Push, Poll and SSE, Polling, 2:45 to 6:30: [watch](https://www.youtube.com/watch?v=J0okraIFPJ0&t=165s). Plain polling as the first of four ways a backend delivers news, before push, long polling and SSE. Chapter-timed.

**Our plans and chapters**

- [Chapter 1: The design](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/textbook/01-the-design.md#15-polling-against-being-told), ai-engineering/product-data-validation-end-to-end, chapter 1, section 1.5. Works polling on numbers: pulling the whole SAP table returns 26 rows every time, and a watermark query returns only the 5 that changed since the last pull.
- [Being told against asking repeatedly](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/plans/04-polling-against-event.md), the same journey, plan 04. Queries `sap.article` on a timer, then watches a folder for new files, each in about forty lines of Python, and measures what each costs.
- [Four that poll and one that pushes](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/plans/23-poll-against-push.md), the same journey, plan 23. A poll loop against the SAP mock with a change made while it runs, timed, beside the one source that pushes.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "polling" across the system design books; Grokking's Ticketmaster section names long polling in one sentence and was left out. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and the chapter section were read at their titles and opening lines. Left out: Hussein Nasser's Difference between Client Polling vs Server Push in Notifications, which covers the same ground. The bare word "polling" was sampled in the learning tree: 25 of 29 lines, and all but one, mean this idea; the exception is a hallucination benchmark's "yes/no polling", which the `link-skip` phrase covers.
