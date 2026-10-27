---
aliases: [WebSocket, websocket, WebSocket handshake, WebSocket connection]
standard: vault-note v2
---

# WebSocket

Up: [[Networking]]

Information Technology, Networking. A WebSocket replaces [[Polling]] when the server must push the moment something happens; a [[Load Balancer]] in front of WebSocket servers has to keep each long-lived connection on one server, and [[Publish-Subscribe]] is how several servers share one message between their connected clients.

**A WebSocket is a persistent, two-way connection between a browser and a server: it starts as an HTTP request that is upgraded (status 101), and from then on either side can send a message at any time without a new request.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches WebSockets writes the rest around it.

## Where to learn this

**WebSocket**, one upgraded HTTP connection kept open for two-way messages. Also: WebSockets, WebSocket handshake, WebSocket connection.

**Textbooks**

- System design interview, chapter 12, Design a chat system, WebSocket: [pages 182 to 184](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=182). The connection the client opens as HTTP and upgrades through a handshake, bi-directional and persistent, working through firewalls on ports 80 and 443, then used for both sending and receiving in the chat design.
- System design interview, chapter 12, Design a chat system, Service discovery and 1 on 1 chat flow: [pages 190 to 191](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=190). Works one message end to end: user A connects to chat server 2 over WebSocket, sends a message, and the server holding user B's persistent connection forwards it.
- System design big archive, Can a web server provide real-time updates?: [pages 425 to 426](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=425). WebSocket against server-sent events: both let the server send the latest data once connected, but only WebSocket is full-duplex.

**Videos**

- Hussein Nasser, WebSockets Crash Course, WebSockets Example Code, 14:30 to 36:40: [watch](https://www.youtube.com/watch?v=2Nt-ZrNP22A&t=870s). A WebSocket server and client written on screen. Chapter-timed.
- Hussein Nasser, WebSockets Crash Course, WebSockets Handshake, 8:00 to 11:20: [watch](https://www.youtube.com/watch?v=2Nt-ZrNP22A&t=480s). The upgrade handshake that turns an HTTP request into a WebSocket. Chapter-timed.
- ByteByteGo, FAANG System Design Interview: Design A Chat System, Communication protocols, 0:39 to 2:04: [watch](https://www.youtube.com/watch?v=okrR1KXNLtA&t=39s). The protocol choice at the start of a chat design. Chapter-timed.
- Hello Interview, Networking Essentials for System Design Interviews, WebSockets (WS), 30:34 to 34:18: [watch](https://www.youtube.com/watch?v=SHkbPm1Wrno&t=1834s). WebSockets after server-sent events and before WebRTC, in a networking primer for system design interviews. Chapter-timed.

**Our plans and chapters**

- [Channels websocket push](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/23-channels-websocket-push.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 23. A Channels consumer over the Redis channel layer, the `/ws` proxy rule fixed, the 101 handshake watched in DevTools and two tabs updating live.
- [HTTP/WebSocket Handshake](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/01-distributed-systems-primitives/plans/01-http-websocket-handshake.md), projects/tms-mobility/system-design/plans/01-distributed-systems-primitives, plan 01. The HTTP request-response cycle and the WebSocket upgrade handshake, the prerequisite for real-time dispatch.
- [nginx in front of two Daphnes](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/25-nginx-load-balancer.md), projects/attica/event-creation/plans/02-rebuild-from-scratch, plan 25. Two daphne containers behind nginx, one killed mid-traffic, then what WebSockets demand of the balancer.
- [System Design: Notification Systems](/home/molef/goal-setting/learning/system-design/notification-systems/MASTER_PLAN.md), system-design/notification-systems. Its second goal delivers a notification over WebSocket to a connected client in under a second; it holds goals and no plans yet.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/api-design-and-contracts/artifacts/figures/api-styles/six-api-styles.jpg"><img src="/home/molef/goal-setting/learning/system-design/api-design-and-contracts/artifacts/figures/api-styles/six-api-styles.jpg" width="200" alt="Six small panels: Soap, WebSocket, Rest, WebHook, GraphQL and gRPC, each drawn as boxes and arrows between machines"></a> Fernando on X, "APIs Architectural Styles": [the post](https://x.com/Franc0Fernand0/status/2096870374524793160), [what it shows](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/artifacts/figures/api-styles/README.md#six-api-stylesjpg). The WebSocket panel puts a red "Push" box between a desktop client and a server with arrows leaving it in both directions, so the server can send without being asked. It sits in the same row as REST and GraphQL, though a WebSocket is a connection that stays open and does not shape a single request ([the reading](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/sources/api-styles/SOURCES.md#three-kinds-of-thing-drawn-as-one-list)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "websocket" across the system design books. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; ByteByteGo has no dedicated WebSocket video in its cached upload list beyond a 52-second short. Each plan was read at its title and description. Left out: Hayk Simonyan's API Protocols Explained chapter "Websockets" (4:09 to 6:48), a shorter pass over the same ground; TMS plan 03 under operations-and-delivery (Async Django) and plan 03 under dispatch-integration-and-architecture (real-time dispatch delivery), which build on the handshake plan above; Hussein Nasser's 5-hour The Complete Guide to WebSockets.
