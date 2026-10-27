---
aliases: [gateway routing, path routing, path-based routing, route rule, route rules, routing rule, routing rules, routing table]
link-only-in: [system-design/foundations, system-design/api-gateways]
link-scope-words: [routing table]
standard: vault-note v2
---

# Gateway Routing

Up: [[APIs]]

Information Technology, System Design. The [[API Gateway]] does this for every request it receives. The network-layer table with the same name, which matches IP addresses rather than paths, is [[Routing Table]].

**Gateway routing matches each request's URL path (and sometimes its host or method) against a table of route rules and sends it to the one service that owns that path, so `/orders/*` reaches the order service and `/payments/*` the payment service.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches gateway routing writes the rest around it.

## Where to learn this

**Gateway routing**, URL path to the service that owns it. Also: path routing, path-based routing, route rules, the gateway's routing table.

**Textbooks**

- System design big archive, What does API gateway do?: [pages 10 to 11](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=10). The same idea at the application layer: in steps 6 and 7 the gateway matches the request's path to find the service to route it to.

**Videos**

- Hello Interview, API Gateways in System Design Interviews, What an API Gateway does, 2:52 to 5:10: [watch](https://www.youtube.com/watch?v=7-6F3b14baA&t=172s). Routing, authentication and rate limiting done in one place at the front, after a chapter on where gateways came from. Chapter-timed.

**Our plans and chapters**

- [Traefik routes and tokens](/home/molef/goal-setting/learning/system-design/foundations/plans/12-traefik-routes-and-tokens.md), system-design/foundations, plan 12. The gateway's routing table written as Compose labels, sending `/users`, `/orders`, `/payments` and `/notify` to four services, then read back in Traefik's dashboard.
- [The API contract on paper](/home/molef/goal-setting/learning/system-design/foundations/textbook/02-the-api-contract-on-paper.md), system-design/foundations, chapter 02, section 2.1. The four route prefixes written first, as the routing table's four rows on picture 1.

> [!note]- How this was checked
> These four lines were opened and confirmed on 2026-10-24 for the Routing Table card, and moved here on 2026-10-27 when that card was split by meaning: Routing Table keeps the IP sense (destination prefix to next hop) and this card takes the gateway sense (URL path to service).
