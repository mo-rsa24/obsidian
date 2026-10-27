---
aliases: [service discovery, service registry]
standard: vault-note v2
---

# Service Discovery

Up: [[System Design]]

Information Technology, System Design. It is how [[Microservices]] find each other, [[DNS]] is its simplest form, and an [[API Gateway]] or a [[Load Balancer]] can read the registry to route.

**Service discovery is how a service finds the current address of another one by name: each running copy registers itself in a service registry (or is found through DNS), callers or a gateway ask the registry, and copies that stop sending heartbeats are dropped from it.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches service discovery writes the rest around it.
> - The placement is unsure: here beside [[Microservices]], or inside a Microservices folder once that note grows parts.

## Where to learn this

**Service discovery**, finding a service's current address by name. Also: service registry.

**Textbooks**

- System design interview, chapter 12, Design a chat system, Service discovery: [page 190](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=190). Works the login flow in four steps: the load balancer sends the login to the API servers, Apache Zookeeper, which registers every chat server, picks the best one by location and capacity and returns it, and the client opens a WebSocket to that server.
- System design interview, chapter 12, the adjusted high-level design: [page 185](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=185). Service discovery as the one service the chapter builds itself, whose job is to give the client a list of chat server host names and keep any one server from overloading.

**Videos**

- Hello Interview, Networking Essentials for System Design Interviews w/ Ex Meta Senior Manager, Client-Side Load Balancing, 40:00 to 43:00: [watch](https://www.youtube.com/watch?v=SHkbPm1Wrno&t=2400s). Clients query a registry for the servers that exist and pick one themselves, with DNS as the case that tolerates slow updates and gRPC's built-in support for internal services. Caption-read.
- Gaurav Sen, Service discovery and heartbeats in micro-services, 0:00 to 6:44: [watch](https://www.youtube.com/watch?v=lWE_UIbm8NA&t=0s). Service discovery taken together with the heartbeats between microservices, in one short talk. Whole video.

**Our plans and chapters**

- [System Design: Microservices](/home/molef/goal-setting/learning/system-design/microservices/MASTER_PLAN.md#goals), system-design/microservices. Goal 3: a simple service registry so services locate each other by name, not by a hard-coded address; it holds goals and no plans yet.
- [System Design: API Gateways](/home/molef/goal-setting/learning/system-design/api-gateways/MASTER_PLAN.md#goals), system-design/api-gateways. Goal 1: a gateway routing to at least three services whose locations come from a simple service registry; it holds goals and no plans yet.
- [Docker and Compose on the corner shop](/home/molef/goal-setting/learning/system-design/foundations/plans/07-docker-and-compose-on-the-corner-shop.md), system-design/foundations, plan 07. Every service in the corner shop's Compose file reaches the others by service name on one network, which is Docker's own DNS doing the discovery; a name that does not resolve is the failure later plans meet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page was read with pdftotext after a page-text search of the five system design books for "service discovery" and "service registry"; no back-of-book table has either. The Hello Interview chapter was read in its captions (yt-dlp) and its chapter list; Gaurav Sen's video has no chapters and is cited whole, described from its title. Each plan was read at its title and the lines that name discovery or reaching a service by name. Left out: the big archive's Top 20 System Design Concepts (pages 134 to 135), a one-line definition; System design interview page 198, a closing line on Zookeeper handing a client a new server when one goes offline; Computer networking's DNS section, which teaches name lookup in general rather than finding services; ByteByteGo's What Are Microservices Really All About? and KodeKloud's What is a Istio Service Mesh?, whose chapters do not name discovery and whose captions were not read (YouTube refused further caption downloads with HTTP 429). The textbook chapter 07 section 7.2 ("A second service that reaches it by name") is not linked because it is not written yet.
