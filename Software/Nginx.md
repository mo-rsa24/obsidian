---
aliases: [Nginx, NGINX, nginx]
standard: vault-note v2
---

# Nginx

Up: [[Software]]

Software. Nginx is the [[Reverse Proxy]], [[Load Balancer]] and [[Cache]] that most of our system design plans run in front of their services.

**Nginx is a web server that is mostly used in front of other servers, as a reverse proxy, load balancer, cache and TLS terminator, handling many connections at once with a few event-driven worker processes.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches Nginx writes the rest around it.

## Where to learn this

**Nginx**, the web server and reverse proxy. Also: NGINX, nginx.conf, proxy_pass.

**Textbooks**

- System design big archive, Why is Nginx so popular?: [pages 431 to 432](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=431). Why Nginx overtook Apache, and its four roles: high-performance web server, reverse proxy and load balancer, caching layer, and TLS termination.

**Videos**

- Hussein Nasser, NginX Crash Course, Nginx as a Web Server (webserver.conf), 15:00 to 20:00: [watch](https://www.youtube.com/watch?v=hcw-NjOh8r0&t=900s). The first configuration file of a two-hour course that goes on to proxy_pass, layer 4 and layer 7 proxying, load balancing and HTTPS. Chapter-timed.
- Hussein Nasser, What is NginX and What are its use cases?, What is NginX?, 0:00 to 2:30: [watch](https://www.youtube.com/watch?v=WHv_t_yK-QM&t=0s). What Nginx is, before the chapters on the problems it solves. Chapter-timed.
- KodeKloud, What is NGINX? | Basic Concepts Explained for Beginners, Event-Driven Architecture, 3:33 to 5:28: [watch](https://www.youtube.com/watch?v=rNF3QJPlagg&t=213s). The event-driven design behind Nginx's speed, in a beginner's tour that ends on load balancing, proxying and caching. Chapter-timed.
- Hussein Nasser, NGINX Internal Architecture - Workers, Worker Processes, 1:15 to 3:22: [watch](https://www.youtube.com/watch?v=vVYM2QBk-iQ&t=75s). The worker processes inside Nginx, before how they handle requests. Chapter-timed.

**Our plans and chapters**

- [Dev under Compose, with Nginx in front](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/13-dev-under-compose-with-nginx.md), system-design/devops-and-deployment, plan 13. Nginx in one Compose file with the app and PostgreSQL, serving `/static/` itself and forwarding `/api/` to the app.
- [The nginx cache: MISS, then HIT](/home/molef/goal-setting/learning/system-design/foundations/plans/10-the-nginx-cache.md), system-design/foundations, plan 10. Nginx as the cache in front of the corner shop, answering the catalogue page itself on the second request.
- [The balancer over two gateway copies](/home/molef/goal-setting/learning/system-design/foundations/plans/11-the-balancer-over-two-gateways.md), the same journey, plan 11. Nginx as the balancer over two Traefik gateway copies, one of them stopped mid-loop.
- [nginx in front of two Daphnes](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/25-nginx-load-balancer.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 25. An upstream block over two daphne containers, `proxy_pass` and the websocket upgrade headers, each line explained.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The textbook pages were read with pdftotext after a page-text search for "nginx" across the shelf; the other pages that name Nginx (System design big archive pages 31, 34, 98 and 109) mention it in one line each, so the card has one textbook line. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; ByteByteGo has no Nginx upload, so Hussein Nasser, routed first for proxies, leads, and Hussein Nasser's NginX as a Layer 7 Proxy is members-only and was skipped. Each plan was read at its title and description.
