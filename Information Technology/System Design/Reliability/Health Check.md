---
aliases: [health check, healthcheck, liveness probe, readiness probe, health endpoint]
standard: vault-note v2
---

# Health Check

Up: [[Reliability]]

Information Technology, System Design. A [[Load Balancer]] runs health checks to drop a failed server from its pool, and each check is a request with a [[Timeout]]; the answer it gives is only as deep as what the check tests.

**A health check is a small request a load balancer, orchestrator or monitor sends to a service on a schedule, often to an endpoint such as `/healthz`, to decide whether the service is alive and ready for traffic; a service that fails it is taken out of rotation or restarted.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches health checks writes the rest around it.

## Where to learn this

**Health check**, a scheduled request that decides whether a service gets traffic. Also: healthcheck, liveness probe, readiness probe, health endpoint.

**Textbooks**

- Grokking the system design interview, section 12.2, Load balancing algorithms: [page 14](../../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=14). Health checks that regularly try to connect to each backend, remove a server that fails from the pool, and send it traffic again only once it passes.
- System design interview, chapter 6, Design a key-value store, failure detection: [pages 100 to 101](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=100). The push form of a health check: each node increments a heartbeat counter and gossips it to random peers, and node s0 marks node s2 offline when s2's counter stops rising.

**Videos**

- freeCodeCamp, System Design Course: APIs, Databases, Caching, CDNs, Load Balancing and Production Infra, Health Checks, 25:08 to 28:00: [watch](https://www.youtube.com/watch?v=C842vFY5kRo&t=1508s). Health checks as the chapter after load balancing, before single points of failure. Chapter-timed.
- KodeKloud, Kubernetes Liveness vs Readiness Probes, Done Right!, 0:00 to 2:47: [watch](https://www.youtube.com/watch?v=oM5-knpFPw4&t=0s). The two health checks Kubernetes runs on a container: is it running, and can it serve traffic yet. Whole video.

**Our plans and chapters**

- [Health check and alert: /healthz polled every 60 s, downtime manufactured, one alert seen](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/74-health-check-and-alert.md), ai-engineering/one-business-end-to-end, plan 74. Works one end to end: a `/healthz` endpoint that checks the database, polled every 60 seconds, the container stopped on purpose, and one alert saying when it went down and came back.
- [Chapter 10: Deploy](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/textbook/10-deploy.md#103-compose-and-the-health-check-dependency), the same journey, chapter 10, section 10.3. A Compose `healthcheck` that runs `pg_isready` every 5 seconds, and the web service that waits for the database to pass it.
- [Zones, and a copy under load](/home/molef/goal-setting/learning/system-design/foundations/plans/25-zones-and-a-copy-under-load.md), system-design/foundations, plan 25. A whole zone of gateway copies stopped while orders still go through, with a few 502s in the first seconds until the balancer's health check drops the stopped copy.
- [System Design: High Availability and Fault Tolerance](/home/molef/goal-setting/learning/system-design/high-availability-and-fault-tolerance/MASTER_PLAN.md), system-design/high-availability-and-fault-tolerance. A shallow check that reports healthy while a deep check sees a dependency down, on the same service; it holds goals and no plans yet.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/docker-8-day-playbook/day-5-docker-compose.jpg"><img src="/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/docker-8-day-playbook/day-5-docker-compose.jpg" width="200" alt="Day 5 card: three tangled docker run lines against one compose file, an annotated docker-compose.yml, depends_on with a healthcheck, and a command table"></a> Tech Fusionist on X, "Docker & Containers for Cloud & DevOps, Day 5: Docker Compose": [the post](https://x.com/techyoutbe/status/2086017393999090067), [what it shows](/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/docker-8-day-playbook/README.md#day-5-docker-composejpg). Panel C draws `depends_on` from web to db with a healthcheck loop on db, the case where a service should start only once its dependency answers. The panel's prose says Compose waits for db to report healthy, but plain `depends_on: [db]` waits only for the container to start; waiting for health needs `condition: service_healthy`, as the card's own sticky note warns ([the reading](/home/molef/goal-setting/learning/system-design/devops-and-deployment/sources/docker-8-day-playbook/SOURCES.md#three-places-the-source-is-wrong-or-incomplete)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "health check" and "heartbeat" across the system design books; System design interview's other heartbeats (online presence on page 195, load balancers watching each other on page 260) were left out. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; the KodeKloud line also leans on the video's own description. No ByteByteGo, Hayk Simonyan or Gaurav Sen video on health checks was found in their cached upload lists. Each plan and the chapter section were read at their titles and opening lines. "heartbeat" is not an alias: its 9 learning-tree lines are a chat app's presence ping, a figure's icon and a figure of speech about CI, none of them a service health check.
