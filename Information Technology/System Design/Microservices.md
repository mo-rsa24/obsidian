---
aliases: [microservice, microservice architecture, microservices architecture]
standard: vault-note v2
---

# Microservices

Up: [[System Design]]

Information Technology, System Design. Services talk to each other synchronously, where a [[Timeout]] and [[Retry With Backoff]] guard each call, or asynchronously through a [[Message Queue]]; the [[Outbox Pattern]] keeps a service's own data and the messages it sends in step.

**Microservices is an architecture that splits one application into small services, each owning one business capability and its own data, deployed on its own and reached over the network, where a monolith keeps everything in one deployable unit.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches microservices writes the rest around it.

## Where to learn this

**Microservices**, one application split into services that each own their data. Also: microservice, microservice architecture.

**Textbooks**

- System design big archive, The Evolution of Scaling at Netflix: [pages 258 to 259](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=258). Works one company's path: the monolithic NCCP application, its features extracted into microservices while the orchestration stayed behind, then a Zuul API gateway to cut the coupling between client and services.
- System design big archive, A picture is worth a thousand words: 9 best practices for developing microservices: [pages 441 to 442](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=441). Nine rules, from a separate data store and a separate build for each service through stateless services and domain-driven design to orchestration.
- System design big archive, What are Modular Monoliths?: [pages 353 to 354](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=353). The monolith as one deployment unit, microservices as many, and the modular monolith in between, with modules behind interfaces inside one unit.

**Videos**

- Hussein Nasser, Microservices Explained and their Pros & Cons, Microservices Example, 4:00 to 8:00: [watch](https://www.youtube.com/watch?v=T-m7ZFxeg1A&t=240s). A traditional service split into microservices on an example, before their pros and cons. Chapter-timed.
- ByteByteGo, What Are Microservices Really All About? (And When Not To Use It), How microservices work, 0:42 to 1:27: [watch](https://www.youtube.com/watch?v=lTAcCNbJ7KE&t=42s). The working parts, followed by independent deployment and information hiding. Chapter-timed.
- Gaurav Sen, What is a MICROSERVICE ARCHITECTURE and what are its advantages?, How do they differ?, 0:00 to 2:02: [watch](https://www.youtube.com/watch?v=qYhRvH9tJKw&t=0s). How a microservice architecture differs from a monolith, before each one's advantages and disadvantages. Chapter-timed.
- Arpit Bhayani, What are Microservices?, Monolith to Microservices, 16:19 to 18:33: [watch](https://www.youtube.com/watch?v=qoAox0FGzRQ&t=979s). The move from a monolith to microservices, after the monolith's disadvantages. Chapter-timed.

**Our plans and chapters**

- [Requirements, and who owns which table](/home/molef/goal-setting/learning/system-design/foundations/plans/01-requirements-and-table-ownership.md), system-design/foundations, plan 01. Decides which of the corner shop's four services owns each of the seven tables in `schema.sql`, before anything is built.
- [Payment, notification, and a timeout](/home/molef/goal-setting/learning/system-design/foundations/plans/14-payment-notification-and-a-timeout.md), the same journey, plan 14. Payment and notification services added in FastAPI beside the Django order service, and the one network call between them that the customer waits on.
- [Monolith vs Microservices: Round 1 Architecture Decision](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/04-dispatch-integration-and-architecture/plans/04-monolith-vs-microservices.md), projects/tms-mobility/system-design/plans/04-dispatch-integration-and-architecture, plan 04. Justifies or challenges a single-server design once the costs of scaling, fault tolerance and load testing are known.
- [System Design: Microservices](/home/molef/goal-setting/learning/system-design/microservices/MASTER_PLAN.md), system-design/microservices. Draws service boundaries by business capability, sync against async calls and service discovery, and what a monolith gives up when split; it holds goals and no plans yet.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/foundations/artifacts/figures/high-level-design/request-path-client-to-cloud.jpg"><img src="/home/molef/goal-setting/learning/system-design/foundations/artifacts/figures/high-level-design/request-path-client-to-cloud.jpg" width="200" alt="Hand-drawn high level design: clients, DNS, CDN, load balancer, API gateway, four microservices, data stores, external services, a message queue and an observability band"></a> AI Guides on X, "High Level Design": [the post](https://x.com/free_ai_guides/status/2094802575245922664), [what it shows](/home/molef/goal-setting/learning/system-design/foundations/artifacts/figures/high-level-design/README.md#request-path-client-to-cloudjpg). The application-layer box holds four services (user, order, payment, notification) behind one API gateway, each wired to its own store or outside service, and a dashed "Events / Async" arrow drops to a Kafka or RabbitMQ queue that feeds background workers. Solid arrows are synchronous calls and dashed ones asynchronous, per the drawing's own legend.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "microservice" across the system design books; the big archive's sections come from the chapter tables in `Textbooks.md`. System design interview names microservices only in passing (pages 54 and 185). Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: Gaurav Sen's Moving from MONOLITHS to MICROSERVICES, whose migration chapters repeat Arpit Bhayani's; Arpit Bhayani's dozen pattern videos (database per service, API composition, orchestration against choreography), which belong to narrower notes. "service mesh" is not an alias: no shelf book teaches it and no cached video beyond a Hussein Nasser proxy explainer covers it, so it waits for a note of its own. The bare word "microservice" (17 lines) means this idea in every sampled line.
