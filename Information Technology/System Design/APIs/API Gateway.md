---
aliases: [API gateway, gateway]
link-skip: [payment gateway, NAT gateway, default gateway, internet gateway, transit gateway, Bad Gateway, tool gateway, model gateway, AI gateway, test gateways]
link-only-in: [system-design]
standard: vault-note v2
---

# API Gateway

Up: [[APIs]]

Information Technology, System Design. A gateway often runs the [[Rate Limiter]] and request [[Middleware]], sits behind a [[Load Balancer]], and is itself a kind of [[Reverse Proxy]].

**An API gateway is the single entry point in front of a set of backend services: it checks each request (authentication, rate limits, validation) and routes it by path to the service that owns it.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches API gateways writes the rest around it.

## Where to learn this

**API gateway**, the one door in front of many services. Also: gateway.

**Textbooks**

- System design big archive, What does API gateway do?: [pages 10 to 11](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=10). Walks one HTTP request through the gateway: parsing and validation, allow and deny lists, authentication with an identity provider, rate limiting, routing by path, protocol translation to the backend, then error handling, circuit breaking, logging and caching.
- System design interview, chapter 4, Design a rate limiter: [page 54](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=54). The API gateway as a managed service that does rate limiting, SSL termination, authentication and IP whitelisting, and when to put a rate limiter there rather than in your own servers.
- System design big archive, Load Balancers vs API Gateways vs Reverse Proxy! And how can they Work Together?: [pages 312 to 313](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=312). Where the gateway sits between an edge load balancer and the service-level load balancers, and the checks it runs in order before its reverse proxy forwards the request.
- System design big archive, Tokens vs API Keys: [pages 236 to 237](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=236). The gateway as the place a JWT is validated for end users and an API key for third-party developers, before the request reaches a service.
- AI engineering, chapter 10, Gateway: [pages 866 to 870](../../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=866). The same idea in front of model APIs: a model gateway as one interface to several providers, sketched as a small Flask route, then access control, cost limits and fallbacks.

**Videos**

- ByteByteGo, What is API Gateway?, API Gateway Flow, 0:50 to 1:15: [watch](https://www.youtube.com/watch?v=6ULyxuHKxg8&t=50s). One request's path through the gateway, before the chapters on its rate limit check and its authentication. Chapter-timed.
- Gaurav Sen, What is an API Gateway?, What is an API Gateway?, 0:00 to 1:02: [watch](https://www.youtube.com/watch?v=RbMxB_Cyx6A&t=0s). The definition, opening a video whose next chapters take authentication, transformation, validation, rate limiting and routing one at a time. Chapter-timed.
- Hello Interview, API Gateways in System Design Interviews w/ Ex-Meta Staff Engineer, What an API Gateway does, 2:52 to 5:10: [watch](https://www.youtube.com/watch?v=7-6F3b14baA&t=172s). What a gateway does, after a chapter on how gateways came about. Chapter-timed.
- ByteByteGo, Reverse Proxy vs API Gateway vs Load Balancer, API Gateway, 0:48 to 1:42: [watch](https://www.youtube.com/watch?v=RqfaTIWc3LQ&t=48s). The gateway set between the reverse proxy and the load balancer. Chapter-timed.

**Our plans and chapters**

- [Traefik: routes and tokens](/home/molef/goal-setting/learning/system-design/foundations/plans/12-traefik-routes-and-tokens.md), system-design/foundations, plan 12. Gives the corner shop's Traefik gateway a routing table written as Compose labels for four paths, and a ForwardAuth token check that refuses a request with no token with a 401.
- [The balancer over two gateway copies](/home/molef/goal-setting/learning/system-design/foundations/plans/11-the-balancer-over-two-gateways.md), system-design/foundations, plan 11. An nginx balancer in front of two Traefik gateway copies, one stopped, and 20 requests in a row still answered 2xx.
- [System Design: API Gateways](/home/molef/goal-setting/learning/system-design/api-gateways/MASTER_PLAN.md), system-design/api-gateways. A gateway built to route by path to at least three services through a service registry, then given JWT validation, rate limiting, one aggregation endpoint and a circuit breaker; it holds goals and no plans yet.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/api-gateways/artifacts/figures/how-an-api-gateway-works/techyoutbe-how-an-api-gateway-works.png"><img src="/home/molef/goal-setting/learning/system-design/api-gateways/artifacts/figures/how-an-api-gateway-works/techyoutbe-how-an-api-gateway-works.png" width="200" alt="Two panels: a client reaching three services through one API gateway, and the same client wired straight to each service"></a> Tech Fusionist on X, "How does an API Gateway Work?": [the post](https://x.com/techyoutbe/status/2096342443474260210), [what it shows](/home/molef/goal-setting/learning/system-design/api-gateways/artifacts/figures/how-an-api-gateway-works/README.md#techyoutbe-how-an-api-gateway-workspng). The top panel sends one arrow from the client through the gateway, the bottom panel draws three arrows straight to the services, and a strip of six cards names the request path from authentication to the aggregated response. It labels the gateway hop "Encrypted", which overclaims: TLS does the encrypting, and what a gateway centralises is where the certificate lives and where the connection ends ([the reading](/home/molef/goal-setting/learning/system-design/api-gateways/sources/how-an-api-gateway-works/SOURCES.md#one-infographic-two-halves)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the chapter tables in `Textbooks.md` and a page-text search for "API gateway" across the four system design books; the AI engineering pages came from its back-of-book index ("gateways"). Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: the agent harness journey's tool gateway (`ai-engineering/agent-harness`), a gateway in front of an agent's tools rather than in front of services. The bare word "gateway" is used 650 times in the learning tree: 436 in system-design, almost all meaning the corner shop's Traefik API gateway (29 of 30 random lines), and 155 in ai-engineering, mostly the tool gateway and the model gateway. So `link-only-in: [system-design]` keeps bare "gateway" linking only there, and the `link-skip` phrases leave the payment, NAT, default, internet and transit gateways and the 502 Bad Gateway status plain.
