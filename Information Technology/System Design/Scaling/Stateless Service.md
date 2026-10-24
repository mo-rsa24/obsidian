---
aliases: [stateless service, stateless, stateful, stateful service, statelessness]
link-skip: [security group, NACL, stateful tracking, stateless evaluation, stateful versus stateless is]
standard: vault-note v2
---

# Stateless Service

Up: [[Scaling]]

Information Technology, System Design. A stateless service is what lets a [[Load Balancer]] send any request to any copy, which is how [[Scalability]] by adding servers works.

**A stateless service keeps nothing about a client between requests, so every request carries or fetches what it needs and any copy of the service can answer it; a stateful service remembers the client and must keep seeing the same client.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches statelessness writes the rest around it.

## Where to learn this

**Stateless service**, a service that remembers nothing between requests. Also: stateless, stateful, statelessness.

**Textbooks**

- System design interview, chapter 1, Stateless web tier: [pages 20 to 22](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=20). Works user A's case: on a stateful server A's session lives on server 1, so a request routed to server 2 fails to authenticate; moving sessions to a shared store lets any server answer and the web tier autoscale.
- System design interview, chapter 12, Design a chat system, High-level design: [pages 184 to 185](../../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=184). One system split into stateless request and response services behind a load balancer and one stateful chat service whose clients hold a persistent connection to a single server.
- System design big archive, JWT 101: Key to stateless authentication: [page 51](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=51). A token that carries its own claims, so the server checks a signature instead of looking up a session.

**Videos**

- Hayk Simonyan, Stateful vs Stateless Architectures Explained, Online shopping example, 1:41 to 2:35: [watch](https://www.youtube.com/watch?v=20tpk8A_xa0&t=101s). The two architectures applied to one shopping cart, followed by why the stateless one scales better. Chapter-timed.
- Hussein Nasser, Stateful vs Stateless Applications (Explained by Example), Stateless Application, 8:40 to 14:44: [watch](https://www.youtube.com/watch?v=nFPzI_Qg3FU&t=520s). The stateless version of the application the video first builds stateful, explained by example. Chapter-timed.
- Hussein Nasser, Stateful vs Stateless Applications (Explained by Example), Stateful Application, 1:14 to 8:40: [watch](https://www.youtube.com/watch?v=nFPzI_Qg3FU&t=74s). The stateful version first, so the contrast is seen on one example. Chapter-timed.

**Our plans and chapters**

- [System Design: Scalability](/home/molef/goal-setting/learning/system-design/scalability/MASTER_PLAN.md), system-design/scalability. Its second objective takes a toy service holding sessions in memory, makes it stateless, and runs it behind several instances and a load balancer where the stateful version broke; it holds goals and no plans yet.
- [System Design: Security and Auth](/home/molef/goal-setting/learning/system-design/security-and-auth/MASTER_PLAN.md), system-design/security-and-auth. What a stateless token costs: it cannot be revoked before it expires.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "stateless" and "stateful" across the system design books. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; ByteByteGo and Gaurav Sen have no upload on this, so the routing's next creators were used. Each plan was read at its title and the lines that name statelessness. "Stateless" and "stateful" were sampled in the learning tree (21 and 17 uses, 38 lines read): most mean this idea, applied to services, tokens, REST and retries, and about five are the firewall sense (a security group tracks connections, a network ACL does not), which the `link-skip` phrases leave alone.
