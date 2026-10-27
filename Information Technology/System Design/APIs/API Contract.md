---
aliases: [API contract, contract-first]
standard: vault-note v2
---

# API Contract

Up: [[APIs]]

Information Technology, System Design. A [[REST API]] is the style it most often describes, [[OpenAPI]] is one way to write it in a file tools can read, and [[API Versioning]] and [[Idempotency]] keep it usable as it changes.

**An API contract is the agreement between a client and a service about every request and reply: each route's method and path, the JSON it takes and returns, and every status code it can answer with, written down before either side is built so both can be checked against it.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches API contracts writes the rest around it.

## Where to learn this

**API contract**, the agreed shape of every request and reply. Also: contract-first.

**Textbooks**

- System design big archive, A Cheatsheet on REST API Design Best Practices: [pages 143 to 144](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=143). The rules a contract writes down: resource paths with the right HTTP verbs, a versioning scheme, standard error codes, idempotency keys on POST, pagination and authentication.
- System design big archive, The 5 Pillars of API Design: [pages 168 to 169](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=168). API design as defining the inputs and outputs first, then the style, the relationships between entities shown in the endpoints, versioning and rate limits.
- System design big archive, How to Design Good APIs: [pages 380 to 381](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=380). Which HTTP methods must be idempotent, an idempotency key kept in Redis or a database so a retry gets the original reply, noun-based resource names, and limit and offset parameters.

**Videos**

- Hello Interview, API Design in System Design Interviews w/ Meta Staff Engineer, REST, 3:59 to 12:44: [watch](https://www.youtube.com/watch?v=DQ57zYedMdQ&t=239s). Resources as plural nouns in the path, the HTTP methods and which are safe to repeat, path and query parameters against the body, then a reply as a status code plus a body. Caption-read.
- Nerdi Coda, Use contract-first approach and generate code with OpenAPI, Contract-first methodology, 0:29 to 1:25: [watch](https://www.youtube.com/watch?v=1LpItQ3vPeQ&t=29s). Writing the contract before the code, so documentation, server stubs and clients can all come from it. Chapter-timed.
- freeCodeCamp, System Design Course: APIs, Databases, Caching, CDNs, Load Balancing and Production Infra, API Design, 31:01 to 47:17: [watch](https://www.youtube.com/watch?v=C842vFY5kRo&t=1861s). The course's API design chapter, a 16-minute pass. Chapter-timed.

**Our plans and chapters**

- [The API contract on paper](/home/molef/goal-setting/learning/system-design/foundations/textbook/02-the-api-contract-on-paper.md), system-design/foundations, chapter 02. Works the corner shop's four routes with their request and response JSON, every status code each route can return and the hop that returns it, and the Idempotency-Key header on `POST /payments`.
- [The API contract on paper](/home/molef/goal-setting/learning/system-design/foundations/plans/02-the-api-contract-on-paper.md), system-design/foundations, plan 02. The same contract written from memory and checked against chapter 2, then built as a Postman collection of saved examples and exported beside the design.
- [The API contract on paper](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/08-api-contract-on-paper.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 08. The event-creation flow's endpoints designed blind (method, path, payload, success and failure statuses), then compared with Attica's real contract in at least four decision records.
- [The API contract on paper](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/04-the-api-contract-on-paper.md), system-design/clean-architecture-in-python, plan 04. One endpoint's method, path, request body and response body settled on paper before FastAPI decides any of it.
- [System Design: API Design and Contracts](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/MASTER_PLAN.md#goals), system-design/api-design-and-contracts. Objective 2 is the contract itself (schema definition, request and response shape, status and error conventions), and its goals keep a contract usable through versions, pagination and idempotency keys; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No shelf book uses the phrase "API contract": a pdftotext search of every page of the five system design books found it nowhere, and no back-of-book table has it. The three big archive pages were found through its chapter table in Textbooks.md and read with pdftotext; each lists what a contract has to settle without calling it a contract. The Hello Interview chapter was read from its captions (yt-dlp) and its chapter list; the other two videos from their chapter lists with `cache-video-chapters.py`, described from the chapter and video titles only. Each plan and chapter was read at its title, description and the lines that name the contract. This is its own note, apart from [[OpenAPI]]: the learning tree's 86 uses of "API contract" are almost all the hand-written contract of the three "API contract on paper" plans, in no particular notation, and OpenAPI is one notation such a contract can later be written in. Bare "contract" is not an alias, since most of its uses on the shelf and in the tree are sales and vendor contracts.
