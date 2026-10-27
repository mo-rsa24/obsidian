---
aliases: [UDP, user datagram protocol]
standard: vault-note v2
---

# UDP

Up: [[Networking]]

Information Technology, Networking. [[TCP]] is the reliable transport beside it; [[DNS]] queries and HTTP/3 (through QUIC) run on it.

**UDP is the connectionless transport protocol: it sends each datagram on its own, with no handshake and no promise of delivery or order, which keeps it fast and light.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches UDP writes the rest around it.

## Where to learn this

**UDP**, the connectionless transport. Also: user datagram protocol.

**Textbooks**

- Computer networking: a top-down approach, section 3.3, Connectionless transport: UDP: [pages 230 to 235](../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=230). Why an application picks UDP (no connection setup, no connection state, an 8-byte header, sending exactly when it wants), DNS as the example, then the segment's four header fields and the checksum worked on three 16-bit words.
- System design big archive, 18 Common Ports Worth Knowing: [pages 48 to 49](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=48). Names the services that use UDP and their ports: DNS on 53 (UDP or TCP), DHCP on 67 and 68, NTP on 123.
- System design big archive, TCP vs UDP: [page 334](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=334). UDP as connectionless and lightweight, with no guarantee of delivery or order, suited to gaming, streaming and real-time calls.
- System design big archive, Which Protocols Run on TCP and UDP: [pages 371 to 372](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=371). No handshake and no ordering, then HTTP/3 over QUIC, which rebuilds TCP's reliability inside UDP with several streams on one connection.
- System design big archive, Must-Know Network Protocol Dependencies: [pages 118 to 119](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=118). The protocols that sit on UDP (DNS, DHCP, SIP, RTP, NTP), and QUIC as a UDP-based replacement for TCP plus TLS.

**Videos**

- Hussein Nasser, TCP vs UDP Crash Course, UDP demo (code), 31:25 to 35:40: [watch](https://www.youtube.com/watch?v=qqRYkcta6IE&t=1885s). A UDP server written and run on screen, after the chapter on UDP's pros and cons. Chapter-timed.
- Hussein Nasser, When to use UDP vs TCP in Building a Backend Application?, UDP vs TCP for Building a Multiplayer game, 9:20 to 15:30: [watch](https://www.youtube.com/watch?v=G86axGfnWag&t=560s). The choice made for one concrete system, between the chapters on a chat system and a browser with its web server. Chapter-timed.
- Hussein Nasser, TCP vs UDP Crash Course, UDP pros cons, 24:25 to 31:25: [watch](https://www.youtube.com/watch?v=qqRYkcta6IE&t=1465s). What UDP gains and gives up. Chapter-timed.
- Hayk Simonyan, Transport Layer Explained: TCP vs UDP, 0:00 to 5:08: [watch](https://www.youtube.com/watch?v=QyrHol2Ylfo&t=0s). A short explainer of the transport layer and its two protocols. Whole video.

**Our plans and chapters**

- [dnsmasq answers shop.test](/home/molef/goal-setting/learning/system-design/foundations/plans/08-dnsmasq-answers-shop-test.md), system-design/foundations, plan 08. Publishes UDP port 53 for a dnsmasq container, and checks that the question goes over UDP, one packet out and one back.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-03-transport-and-app-protocols.jpg"><img src="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-03-transport-and-app-protocols.jpg" width="140" alt="Day 03 card: TCP against UDP, and the application protocols above them"></a> Tech Fusionist on X, "Day 3: Transport & App Protocols", from the 12-day networking playbook: [the post](https://x.com/techyoutbe/status/2074125684222685404), [what it shows](/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/README.md#the-twelve-day-cards). Section A draws UDP as a postcard (fast, connectionless, no delivery guarantees) with packets arriving 1, 3, 2, 4 beside TCP's 1, 2, 3, 4 in order, and section D puts HTTP/3 on QUIC over UDP. The card never says when UDP is chosen on purpose, so the postcard reads as a defect when it is a design choice ([the reading](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/03-transport-and-app-protocols.md#what-it-flattens)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the chapter tables in `Textbooks.md` and a page-text search for "UDP" across the four system design books; only the big archive mentions UDP. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. The plan was read at its title, description and the lines on UDP port 53. Left out: freeCodeCamp's Transport Layer chapter (at `C842vFY5kRo`, 59:10 to 1:04:22), which is on the [[TCP]] card and covers the same ground. The Computer networking: a top-down approach lines were read with pdftotext on 2026-10-24, found through the book's back-of-book index and its outline in `Textbooks.md`.
