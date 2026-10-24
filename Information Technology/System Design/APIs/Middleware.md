---
aliases: [middleware, request middleware]
standard: vault-note v2
---

# Middleware

Up: [[APIs]]

Information Technology, System Design. A [[Rate Limiter]] and a token check are the usual middleware, and an [[API Gateway]] runs them for every service behind it.

**Middleware is code that sits in a request's path before the handler: each piece sees the request, can check or change it (a token check, a rate limit, a log line) and either passes it on or answers it itself.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches middleware writes the rest around it.

## Where to learn this

**Middleware**, the checks a request passes before its handler. Also: request middleware.

**Textbooks**

- System design interview, chapter 4, Design a rate limiter: [pages 53 to 54](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=53). Works a rate limiter middleware with numbers: an API allows 2 requests a second, a client sends 3, the first two reach the API servers and the middleware answers the third with HTTP 429, then the API gateway is named as a middleware of this kind.
- Systems analysis and design, chapter 8, Architecture design, client-server architectures: [page 310](../../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=310). The older, wider sense of the word: system software installed on both client and server that translates between different vendors' software.

**Videos**

- Web Dev Simplified, Learn Express Middleware In 14 Minutes, Authentication middleware, 7:50 to 14:48: [watch](https://www.youtube.com/watch?v=lY6icfhap2o&t=470s). An authentication middleware written in Express, after a logging middleware and one attached to a single route. Chapter-timed.
- Web Dev Simplified, Learn Express Middleware In 14 Minutes, What is middleware, 2:10 to 3:20: [watch](https://www.youtube.com/watch?v=lY6icfhap2o&t=130s). What middleware is, before the examples. Chapter-timed.
- IBM Technology, What is Middleware?, 0:00 to 10:11: [watch](https://www.youtube.com/watch?v=1oWPUpMheGk&t=0s). Middleware in the wider sense, as software between applications and the systems they use. Whole video.

**Our plans and chapters**

- [Traefik: routes and tokens](/home/molef/goal-setting/learning/system-design/foundations/plans/12-traefik-routes-and-tokens.md), system-design/foundations, plan 12. A ForwardAuth middleware attached to the gateway's four routers hands each request's headers to a token checker and refuses a request with no token with a 401 before any service sees it.
- [Validate a token, and watch a forged one fail](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/plans/10-a-token-validated-in-code.md), ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions, plan 10. The token validated in middleware before any tool code runs, with one claim pulled out as the user id.
- [Rate Limiting](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/02-api-and-traffic-control/plans/03-rate-limiting.md), projects/tms-mobility/system-design/plans/02-api-and-traffic-control, plan 03. Token-bucket rate limiting written as DRF middleware keyed by user.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "middleware" across the four system design books; the Systems analysis and design page came from its back-of-book index ("Middleware"). Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. No listed creator has a video or chapter on request middleware (ByteByteGo's "Messaging Middleware" is the message-broker sense), so the two creators here are outside the list and were found by one search of YouTube's listing. Each plan was read at its title, description and its lines on middleware. Left out: Christian Lempa's Traefik tutorial, cited in plan 12, whose middleware segment sits inside a chapter on Docker labels with no chapter of its own. "Middleware" is not an ordinary dictionary word; of its 38 uses in the learning tree, the 12 lines sampled all mean request middleware (Traefik's ForwardAuth, a token check, a rate-limiting middleware, Django's middleware setting, CORS middleware).
