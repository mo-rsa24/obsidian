---
aliases: [GraphQL API, GraphQL schema]
standard: vault-note v2
---

# GraphQL

Up: [[APIs]]

Information Technology, System Design. It is most often weighed against a [[REST API]], and [[gRPC]] is the third style beside the two.

**GraphQL is an API style with a single endpoint and a typed schema, where the client writes a query naming exactly the fields it wants, nested as deep as it needs, and gets back only those fields.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches GraphQL writes the rest around it.

## Where to learn this

**GraphQL**, one endpoint where the client asks for exactly the fields it needs. Also: GraphQL API, GraphQL schema.

**Textbooks**

- System design big archive, REST API Vs. GraphQL: [pages 234 to 235](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=234). The single endpoint and nested field selection, mutations and subscriptions, then the costs: complexity moved to the client, abusive queries and harder caching, with when each style fits.

**Videos**

- Hussein Nasser, GraphQL Crash Course, GraphQL examples, 17:59 to 30:14: [watch](https://www.youtube.com/watch?v=fVmQCnQ_EPs&t=1079s). Queries worked as examples, after the chapters on core concepts and on schema and operations, and before REST and GraphQL compared in code. Chapter-timed.
- ByteByteGo, What Is GraphQL? REST vs. GraphQL, GraphQL vs REST, 0:52 to 2:27: [watch](https://www.youtube.com/watch?v=yWzKJPw_VzM&t=52s). GraphQL set against REST, before chapters on its benefits and its drawbacks. Chapter-timed.
- Hayk Simonyan, GraphQL API Basics & Best Practices (Explained Simply), GraphQL Schema Design, 1:53 to 3:22: [watch](https://www.youtube.com/watch?v=QHS1AUlBMzY&t=113s). Designing the schema, followed by queries and mutations. Chapter-timed.
- freeCodeCamp, System Design Course: APIs, Databases, Caching, CDNs, Load Balancing and Production Infra, GraphQL, 1:19:04 to 1:24:52: [watch](https://www.youtube.com/watch?v=C842vFY5kRo&t=4744s). GraphQL inside a full system design course, right after its RESTful APIs chapter. Chapter-timed.

**Our plans and chapters**

- [System Design: API Design and Contracts](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/MASTER_PLAN.md), system-design/api-design-and-contracts. One resource built as a REST API, a gRPC service and a GraphQL schema, with the trade-offs written down; its sources include a GraphQL query shown returning two response shapes. It holds goals and no plans yet.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/api-design-and-contracts/artifacts/figures/api-styles/six-api-styles.jpg"><img src="/home/molef/goal-setting/learning/system-design/api-design-and-contracts/artifacts/figures/api-styles/six-api-styles.jpg" width="200" alt="Six small panels: Soap, WebSocket, Rest, WebHook, GraphQL and gRPC, each drawn as boxes and arrows between machines"></a> Fernando on X, "APIs Architectural Styles": [the post](https://x.com/Franc0Fernand0/status/2096870374524793160), [what it shows](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/artifacts/figures/api-styles/README.md#six-api-stylesjpg). The GraphQL panel draws one client query passing through a GraphQL node to a server that fans out to two more servers, so one request gathers its fields from several places. The six are drawn as equal choices, but only SOAP, REST, GraphQL and gRPC answer the same question (how one request and its response are shaped); WebSocket is a connection that stays open, and a webhook is usually a plain REST-style `POST` ([the reading](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/sources/api-styles/SOURCES.md#three-kinds-of-thing-drawn-as-one-list)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The textbook page range was read with pdftotext after the chapter tables in `Textbooks.md` and a page-text search for "GraphQL" across the four system design books; every other big archive page that names GraphQL lists it among API styles in one line. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. The master plan was read at its objectives, goals and its REST, GraphQL and gRPC source entry. Left out: Hussein Nasser's When to use GraphQL over REST? (`J5NkUQ7XRYA`), behind his crash course. The name GraphQL matches in any case; it names nothing else.
