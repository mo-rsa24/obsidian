---
aliases: [REST, REST API, RESTful, RESTful API]
standard: vault-note v2
---

# REST API

Up: [[APIs]]

Information Technology, System Design. [[GraphQL]] and [[gRPC]] are the two styles it is most often weighed against, and every REST call is an [[HTTP]] request.

**A REST API exposes resources at URLs and lets clients act on them with the standard HTTP methods (GET, POST, PUT, DELETE), each request carrying everything the server needs, so the server keeps no session state between calls.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches REST writes the rest around it.

## Where to learn this

**REST API**, resources at URLs acted on with HTTP methods. Also: REST, RESTful API.

**Textbooks**

- System design interview, chapter 8, Design a URL shortener: [pages 121 to 122](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=121). Works two REST-style endpoints for one service, `POST api/v1/data/shorten` taking the long URL and `GET api/v1/shortUrl` answering with a redirect, then weighs a 301 against a 302 response.
- System design big archive, What is a REST API?: [pages 411 to 412](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=411). The six constraints an API must follow to be RESTful: client-server, stateless, uniform interface, cacheable, layered system and the optional code on demand.
- System design big archive, REST API Vs. GraphQL: [pages 234 to 235](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=234). REST's HTTP methods for CRUD and its easy caching, against the several round trips it may need to assemble related data.
- System design big archive, A Cheatsheet on REST API Design Best Practices: [pages 143 to 144](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=143). Resource-oriented paths, versioning, standard error codes, idempotency keys, pagination and security, as a checklist.

**Videos**

- Hussein Nasser, REST API Pros and Cons (Explained by Example), REST API github api, 18:18 to 25:45: [watch](https://www.youtube.com/watch?v=M3XQ6yEC51Q&t=1098s). A real REST API worked through, after the chapters on representations and state transfer and on REST's constraints. Chapter-timed.
- ByteByteGo, What Is REST API? Examples And How To Use It: Crash Course System Design #3, REST API Basics, 0:47 to 2:05: [watch](https://www.youtube.com/watch?v=-mN3VyJuCjM&t=47s). The basics, followed by a chapter on CRUD. Chapter-timed.
- Hayk Simonyan, REST API Basics & Best Practices Explained, Resource Modeling, 0:46 to 2:33: [watch](https://www.youtube.com/watch?v=DkSeXHS0kAQ&t=46s). Modelling resources, before chapters on filtering and pagination, HTTP methods and status codes. Chapter-timed.
- freeCodeCamp, System Design Course: APIs, Databases, Caching, CDNs, Load Balancing and Production Infra, RESTful APIs, 1:04:22 to 1:19:04: [watch](https://www.youtube.com/watch?v=C842vFY5kRo&t=3862s). RESTful APIs inside a full system design course, followed by its GraphQL chapter. Chapter-timed.

**Our plans and chapters**

- [curl against a REST mock](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/plans/19-curl-against-rest-mock.md), ai-engineering/product-data-validation-end-to-end, plan 19. `curl` against two running mocks, reading the status line, headers and body, and telling an empty list from a 404 and a 500.
- [The API contract on paper](/home/molef/goal-setting/learning/system-design/foundations/textbook/02-the-api-contract-on-paper.md), system-design/foundations, chapter 02. Four routes with their request and response JSON, every status code each returns, and an `Idempotency-Key` header.
- [The DRF draft endpoint](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/11-drf-draft-endpoint.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 11. One endpoint built twice in Django REST framework, as a function view and then as a ViewSet.
- [API Design Conventions](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/02-api-and-traffic-control/plans/01-api-design-conventions.md), projects/tms-mobility/system-design/plans/02-api-and-traffic-control, plan 01. Naming, versioning, pagination and query-string conventions for the backend two mobile apps call.
- [System Design: API Design and Contracts](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/MASTER_PLAN.md), system-design/api-design-and-contracts. One resource built as a REST API, a gRPC service and a GraphQL schema, with an OpenAPI spec for the REST one; it holds goals and no plans yet.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/api-design-and-contracts/artifacts/figures/api-styles/six-api-styles.jpg"><img src="/home/molef/goal-setting/learning/system-design/api-design-and-contracts/artifacts/figures/api-styles/six-api-styles.jpg" width="200" alt="Six small panels: Soap, WebSocket, Rest, WebHook, GraphQL and gRPC, each drawn as boxes and arrows between machines"></a> Fernando on X, "APIs Architectural Styles": [the post](https://x.com/Franc0Fernand0/status/2096870374524793160), [what it shows](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/artifacts/figures/api-styles/README.md#six-api-stylesjpg). The Rest panel draws a desktop client sending a request through a blue "Resource" box to a server, one of six panels beside Soap, WebSocket, WebHook, GraphQL and gRPC. The six are drawn as equal choices, but only SOAP, REST, GraphQL and gRPC answer the same question (how one request and its response are shaped); WebSocket is a connection that stays open, and a webhook is usually a plain REST-style `POST` ([the reading](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/sources/api-styles/SOURCES.md#three-kinds-of-thing-drawn-as-one-list)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the chapter tables in `Textbooks.md` and a page-text search for "REST" across the four system design books. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title and description. Left out: Arpit Bhayani's Everything you need to know about REST (chapter "REST and HTTP Synergy", 4:42 to 11:48, at `uFGJVQvR59A`), behind the four above; the big archive's 5 REST API Authentication Methods (pages 403 to 404), which is about authentication. The aliases match "REST" in capitals only, and "RESTful" appears three times in the learning tree, each meaning this idea.
