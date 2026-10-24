---
aliases: [reverse proxy, forward proxy, proxy server, proxy]
link-skip: [proxy for, sufficient proxy, proxy label, proxy measure, proxy metric, proxy variable]
standard: vault-note v2
---

# Reverse Proxy

Up: [[Scaling]]

Information Technology, System Design. A [[Load Balancer]] is a reverse proxy with a choice of server to make, and [[Nginx]] is the reverse proxy most of our plans run.

**A reverse proxy is a server that stands in front of backend servers and takes every client request on their behalf, while a forward proxy stands in front of clients and makes their requests on theirs.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches proxies writes the rest around it.

## Where to learn this

**Reverse proxy**, the server in front of the servers. Also: forward proxy, proxy server, proxy.

**Textbooks**

- System design big archive, Forward proxy versus reverse proxy: [pages 397 to 398](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=397). The two side by side: a forward proxy acts for users (protecting them, blocking sites, caching pages), a reverse proxy acts for servers (spreading traffic, handling TLS, shielding the backend from DDoS attacks).
- Grokking the system design interview, section 15, Proxy server: [pages 18 to 19](../../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=18). Open, anonymous and transparent proxies, then the reverse proxy that fetches from servers and answers as if it were the origin.
- System design big archive, Load balancers vs API gateways vs reverse proxy: [pages 312 to 313](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=312). How a reverse proxy overlaps with a load balancer and an API gateway, and how the three can work together.
- System design big archive, Why is Nginx so popular?: [pages 431 to 432](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=431). Nginx as the common reverse proxy, with load balancing, caching and TLS termination listed among its roles.

**Videos**

- Hussein Nasser, The Anatomy of a Proxy Server, Connection Establishment with an HTTP Proxy, 5:00 to 15:22: [watch](https://www.youtube.com/watch?v=B2G49HZxnRE&t=300s). Traces one connection through an HTTP proxy, after the same connection without one. Chapter-timed.
- ByteByteGo, Proxy vs Reverse Proxy (Real-world Examples), Reverse Proxy, 2:12 to 4:15: [watch](https://www.youtube.com/watch?v=4NB0NDtOwIQ&t=132s). The reverse proxy after the forward and transparent proxy chapters. Chapter-timed.
- Hayk Simonyan, Proxy Servers: How Proxies Work, Forward Proxies, 2:00 to 4:07: [watch](https://www.youtube.com/watch?v=sYhKiPzGPYc&t=120s). The forward proxy, before the reverse proxy chapter that follows it. Chapter-timed.
- Arpit Bhayani, Understanding Proxy, Forward Proxy, and Reverse Proxy, Understanding reverse proxy, 4:16 to 7:29: [watch](https://www.youtube.com/watch?v=HrG0MHkSsCA&t=256s). The reverse proxy, followed by proxies placed in front of databases. Chapter-timed.

**Our plans and chapters**

- [Dev under Compose, with Nginx in front](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/13-dev-under-compose-with-nginx.md), system-design/devops-and-deployment, plan 13. Nginx serves `/static/` itself and forwards `/api/` to the app container by its Compose service name.
- [The Vite proxy and CORS](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/13-vite-proxy-and-cors.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 13. A cross-origin call broken, fixed with CORS, then made moot by the dev server's proxy, ending on the `/ws` route the proxy does not forward.
- [nginx in front of two Daphnes](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/25-nginx-load-balancer.md), the same journey, plan 25. `proxy_pass` and the websocket upgrade headers, each line explained, then one deleted to watch it fail.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "proxy" across the system design books; System design interview never names a proxy, and neither language model book covers one. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: ByteByteGo's Reverse Proxy vs API Gateway vs Load Balancer, whose reverse proxy chapter is 30 seconds; freeCodeCamp's System Design Concepts Course chapter "Proxy Servers (Forward/Reverse Proxies)" (36:33 to 42:36, at `F2FmTdLtb_4`), a longer pass over the same ground. The bare word "proxy" was sampled in the learning tree: 30 random lines and a count of 198 uses, most of them the network proxy (Vite's proxy, Nginx as a reverse proxy, a 502 at whichever proxy got no answer); about a dozen use "a proxy for" in the sense of a stand-in measure, and the `link-skip` phrases leave those lines alone.
