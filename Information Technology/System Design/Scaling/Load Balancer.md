---
aliases: [load balancer, load balancing, round robin]
link-skip: [load-balancing loss, load balancing loss]
standard: vault-note v2
---

# Load Balancer

Up: [[Scaling]]

Information Technology, System Design. A load balancer is the box that makes [[Scalability]] by adding servers work, and it is usually run as a [[Reverse Proxy]].

**A load balancer receives every incoming request and passes each one to one of several identical servers, so the traffic is shared and a failed server is routed around.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches load balancing writes the rest around it.

## Where to learn this

**Load balancer**, one entry point spreading requests over many servers. Also: load balancing, round robin, least connections, health check.

**Textbooks**

- System design interview, chapter 1, Load balancer: [pages 10 to 11](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=10). Works the two-server case: users reach the balancer's public IP, the servers sit on private IPs, and when server 1 goes offline all traffic moves to server 2 while new servers join the pool.
- Grokking the system design interview, section 12, Load balancing: [pages 14 to 15](../../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=14). Health checks that drop a failed server from the pool, then six algorithms: least connections, least response time, least bandwidth, round robin, weighted round robin and IP hash.
- System design big archive, Load balancers vs API gateways vs reverse proxy: [pages 312 to 313](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=312). One request passing through all three: an edge balancer in front of the gateway, the gateway's checks, then a second balancer spreading the request over a service's instances.

**Videos**

- Hussein Nasser, Spin up an Nginx Docker Container as a Load Balancer, nginx.conf, 2:44 to 4:44: [watch](https://www.youtube.com/watch?v=BRPvjNQsqis&t=164s). Writes the nginx configuration that balances requests over Node.js containers, a working balancer on one laptop. Chapter-timed.
- ByteByteGo, What is a LOAD BALANCER really about?, Introduction to load balancers, 0:00 to 1:23: [watch](https://www.youtube.com/watch?v=LQuuoHTyYz8&t=0s). What a load balancer is for, before the video's chapters on layer 4 against layer 7 and the balancing algorithms. Chapter-timed.
- Hayk Simonyan, Load Balancers Explained in 7 Minutes, Round Robin, 0:22 to 1:08: [watch](https://www.youtube.com/watch?v=sXUh9vuOTXk&t=22s). Round robin, the first of the seven algorithms the video walks. Chapter-timed.
- Gaurav Sen, What is LOAD BALANCING?, Hashing Requests, 3:58 to 6:37: [watch](https://www.youtube.com/watch?v=K0Ta65OqQkY&t=238s). Choosing a server by hashing the request, worked on a whiteboard as the step towards consistent hashing. Chapter-timed.

**Our plans and chapters**

- [The balancer over two gateway copies](/home/molef/goal-setting/learning/system-design/foundations/plans/11-the-balancer-over-two-gateways.md), system-design/foundations, plan 11. An nginx balancer over two Traefik gateway copies; one copy is stopped and 20 requests in a row still return 2xx.
- [nginx in front of two Daphnes](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/25-nginx-load-balancer.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 25. Two daphne containers behind nginx, one killed mid-traffic and the rerouting watched, then what websockets demand.
- [Load Balancing Algorithms](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/02-api-and-traffic-control/plans/04-load-balancing.md), projects/tms-mobility/system-design/plans/02-api-and-traffic-control, plan 04. Round robin, weighted, least connections and least response time, and choosing one for TMS's hosting path.
- [System Design: Load Balancing](/home/molef/goal-setting/learning/system-design/load-balancing/MASTER_PLAN.md), system-design/load-balancing. The journey that rebuilds what a balancer decides on every request, layer 4 against layer 7, and health checks; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "load balanc" and "round robin" across the system design books; neither language model book covers this load balancer (their "load balancing" is the mixture-of-experts loss, which the `link-skip` phrases leave alone). Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description; the compiled chapter for foundations plan 11 has headings and no text yet. Left out: ByteByteGo's Top 6 Load Balancing Algorithms and Hayk Simonyan's How to Scale Like a Senior Engineer chapter "Load Balancing Algorithms", which repeat the algorithms above; freeCodeCamp's System Design Course chapter "Load Balancing" (16:22 to 25:08, at `C842vFY5kRo`), a longer walk of the same ground.
