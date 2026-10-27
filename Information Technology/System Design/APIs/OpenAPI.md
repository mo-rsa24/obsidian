---
aliases: [OpenAPI, OpenAPI spec, OpenAPI specification, OpenAPI document, OpenAPI schema, Swagger, Swagger UI, Swagger Editor]
standard: vault-note v2
---

# OpenAPI

Up: [[APIs]]

Information Technology, System Design. It writes an [[API Contract]] down in a file tools can read, usually for a [[REST API]]; [[gRPC]] uses a protocol buffers file for the same job.

**OpenAPI is a standard format, in YAML or JSON, for describing a REST API: every path, its methods, parameters, request and response bodies and status codes, from which tools render interactive documentation (Swagger UI) and generate client and server code.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches OpenAPI writes the rest around it.

## Where to learn this

**OpenAPI specification**, a REST API's contract in a file tools can read. Also: OpenAPI spec, OpenAPI document, OpenAPI schema, Swagger, Swagger UI, Swagger Editor.

**Videos**

- Nerdi Coda, Use contract-first approach and generate code with OpenAPI, OpenAPI document structure, 3:31 to 5:35: [watch](https://www.youtube.com/watch?v=1LpItQ3vPeQ&t=211s). The parts of an OpenAPI document, before the chapters that fill in its info, servers and tags, its paths and its reusable components for a calculator API. Chapter-timed.
- Nerdi Coda, Use contract-first approach and generate code with OpenAPI, Defining API paths, 7:26 to 10:05: [watch](https://www.youtube.com/watch?v=1LpItQ3vPeQ&t=446s). The paths section of the document written out, operation by operation. Chapter-timed.
- Nerdi Coda, Use contract-first approach and generate code with OpenAPI, Automated code generation, 1:25 to 2:44: [watch](https://www.youtube.com/watch?v=1LpItQ3vPeQ&t=85s). Server stubs and client code generated from the document. Chapter-timed.
- TramoTech, Generate OpenAPI Spec & Client Code from Spring Boot REST API, Generating the YAML Spec, 1:36 to 2:35: [watch](https://www.youtube.com/watch?v=df7cBasFjww&t=96s). The other direction: the spec generated from a running Spring Boot REST API, before the chapter that generates a client from it. Chapter-timed.
- Gaurav Sen, Impeccable API Design: What you MUST CONSIDER before deploying APIs to production, OpenAPI Specs with Swagger, 5:28 to 5:54: [watch](https://www.youtube.com/watch?v=FqljO9B5grM&t=328s). A short chapter on publishing an API's OpenAPI spec through Swagger, after the chapter on HTTP error codes. Chapter-timed.

**Our plans and chapters**

- [FastAPI, refreshed](/home/molef/goal-setting/learning/system-design/foundations/textbook/05-fastapi-refresher.md#why-this-matters), system-design/foundations, chapter 05. FastAPI's Pydantic models are what write the OpenAPI schema served at `/docs`, so the chapter 2 contract can be checked against the running service.
- [FastAPI, refreshed](/home/molef/goal-setting/learning/system-design/foundations/plans/05-fastapi-refresher.md#3--serve-the-payment-route-and-call-it-three-ways), system-design/foundations, plan 05. Step 3.3 calls `POST /payments` from Chrome through Swagger UI at `/docs` (Try it out, Execute) and reads `Code 200` with the curl command Swagger UI sent.
- [Video index: system-design/api-design-and-contracts](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/sources/videos/SOURCES.md#leaf-b-schema), system-design/api-design-and-contracts, Leaf B. The Nerdi Coda and TramoTech videos above segmented by their captions: a document built in Swagger Editor with code generated from it, and a spec generated from a Spring Boot API with a client generated from the spec.
- [System Design: API Design and Contracts](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/MASTER_PLAN.md#goals), system-design/api-design-and-contracts. Goal 2: an OpenAPI spec written for the REST version of one resource and a client generated from it; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No shelf book teaches OpenAPI, so the card has no Textbooks group: a pdftotext search of every page of the five system design books found OpenAPI and Swagger only in two one-line lists of documentation tools (the big archive's The Ultimate API Learning Roadmap, page 31, and How to Learn API Development?, page 117), and no back-of-book table has either. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title, the video title and the journey's own caption segmentation where it has one. ByteByteGo, Hello Interview and KodeKloud have no OpenAPI segment: Hello Interview's API design video was read in its captions and never says OpenAPI or Swagger, and searches of the three channels found none. Each plan and chapter was read at its title and the lines that name OpenAPI or Swagger. "Swagger" is also an English word, but all 7 of its uses in the learning tree name the tool (Swagger UI, Swagger Editor, FastAPI with Swagger), so it links unscoped. "API contract" has its own note, [[API Contract]].
