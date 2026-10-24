---
aliases: [CORS, cross-origin resource sharing, preflight request, same-origin policy, cross-origin request]
standard: vault-note v2
---

# CORS

Up: [[Networking]]

Information Technology, Networking. CORS is read from [[HTTP]] headers, decides whether a cross-origin request may carry an [[HTTP Cookie]], and is often avoided by putting a [[Reverse Proxy]] or the dev server's proxy in front so the browser sees one origin.

**CORS is how a server tells a browser which other origins may read its responses: the browser's same-origin policy blocks a page from reading another origin's reply unless the server answers with an `Access-Control-Allow-Origin` header, and for some requests the browser first asks permission with an OPTIONS preflight request.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches CORS writes the rest around it.

## Where to learn this

**CORS**, cross-origin resource sharing. Also: same-origin policy, preflight request, cross-origin request.

**Videos**

- Hussein Nasser, Cross Origin Resource Sharing (Explained by Example), No 'Access-Control-Allow-Origin' header is present, 4:00 to 8:10: [watch](https://www.youtube.com/watch?v=Ka8vG5miErk&t=240s). The first CORS error produced and read, after a same-origin request that works, in a video built from one browser error message per chapter. Chapter-timed.
- Hussein Nasser, Cross Origin Resource Sharing (Explained by Example), OPTIONS 405 Method not Allowed (Preflight failed), 10:10 to 17:00: [watch](https://www.youtube.com/watch?v=Ka8vG5miErk&t=610s). A preflight request that fails, followed by a preflight answered without the allow header and a `Content-Type` header the server did not allow. Chapter-timed.
- Hayk Simonyan, API Security Explained: Rate Limiting, CORS, SQL Injection, CSRF, XSS & More, CORS, 2:39 to 4:05: [watch](https://www.youtube.com/watch?v=FsB_nRGdeLs&t=159s). CORS as one defence of a public API, between rate limiting and injection. Chapter-timed.
- Web Dev Simplified, Learn CORS In 6 Minutes, Preflight Methods, 3:30 to 5:19: [watch](https://www.youtube.com/watch?v=PNtFSVU-YTI&t=210s). The preflight, after a chapter on basic CORS and before one on sending credentials. Chapter-timed.

**Our plans and chapters**

- [The Vite proxy and CORS](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/13-vite-proxy-and-cors.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 13. The wizard wired to the backend three ways in turn: broken cross-origin, fixed with CORS, then made moot by the dev server's proxy, ending on the `/ws` route the proxy does not forward.
- [Connect frontend to backend, Postman first](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/03-connect-and-postman.md), the same journey, plan 03. The same GET from Postman and from the browser, where the CORS error is the point: Postman shows no CORS at all and the browser adds the origin and enforces it.
- [Debug Harness](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/01-tour-the-real-flow/plans/01-debug-harness.md), projects/attica/event-creation/plans/01-tour-the-real-flow, plan 01. Vite moved to port 5174 because 5173 is taken, and the allowed-origins setting the backend then needs.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No shelf book teaches CORS: a page-text search for "CORS", "same-origin" and "cross-origin" across the four system design books found nothing, so the card has no Textbooks group. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Web Dev Simplified is not on the creator list; it is here because no listed creator has a chapter on the preflight other than Hussein Nasser, and the Attica plan already sends the learner to this video. Each plan was read at its title, description and its lines on CORS. Left out: Sam Meech-Ward's React Proxy: Easiest Fix to CORS Errors (chapter "CORS", 2:56 to 3:38, at `N4yUiQiTvwU`), 42 seconds on CORS before a video about the proxy that avoids it.
