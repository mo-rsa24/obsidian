---
aliases: [TCP, TCP/IP, three-way handshake, 3-way handshake, TCP handshake, transmission control protocol]
standard: vault-note v2
---

# TCP

Up: [[Networking]]

Information Technology, Networking. [[UDP]] is the connectionless transport beside it, [[HTTP]] up to HTTP/2 runs on it, and [[TLS]] starts once its handshake is done.

**TCP is the transport protocol that opens a connection with a three-way handshake and then delivers a stream of bytes reliably and in order, resending whatever is lost.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches TCP writes the rest around it.

## Where to learn this

**TCP**, the reliable, connection-oriented transport. Also: three-way handshake, TCP/IP, transmission control protocol.

**Textbooks**

- Computer networking: a top-down approach, section 3.5.6, TCP connection management: [pages 285 to 290](../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=285). The three-way handshake segment by segment (a SYN carrying client_isn, a SYNACK carrying server_isn, then an ACK that may carry data), the four segments that close a connection, and the states each side passes through.
- Computer networking: a top-down approach, sections 3.5.1 and 3.5.2, The TCP connection and TCP segment structure: [pages 263 to 271](../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=263). TCP's byte-stream view, with a 500,000-byte file cut into 1,000-byte segments numbered by byte, then sequence and acknowledgment numbers worked on a Telnet session in which one typed letter crosses as three segments.
- System design big archive, How TCP Handshake Works?: [pages 192 to 193](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=192). Walks the three segments of one handshake: SYN carrying the client's initial sequence number, SYN-ACK acknowledging it by adding one, then the client's ACK.
- System design big archive, TCP vs UDP: [page 334](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=334). TCP as connection-oriented and reliable, with ordered, duplicate-free delivery and flow and congestion control, set against UDP.
- System design big archive, Which Protocols Run on TCP and UDP: [pages 371 to 372](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=371). TCP at the transport layer under HTTP, HTTPS (TLS after the TCP connection) and SMTP, then HTTP/3 leaving it for QUIC.
- System design big archive, 18 Common Ports Worth Knowing: [pages 48 to 49](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=48). The well-known ports that ride on TCP, among them SSH on 22, HTTP on 80, HTTPS on 443 and PostgreSQL on 5432.

**Videos**

- Hussein Nasser, TCP vs UDP Crash Course, Tcp demo (code), 19:00 to 24:25: [watch](https://www.youtube.com/watch?v=qqRYkcta6IE&t=1140s). A TCP server written and run on screen, after the chapter on TCP's pros and cons. Chapter-timed.
- Hussein Nasser, What is the TCP 3-Way Handshake and Why Backend Engineers should understand it, Handshake Explained, 4:40 to 8:50: [watch](https://www.youtube.com/watch?v=bW_BILl7n0Y&t=280s). The handshake itself, followed by a chapter on what it costs in performance. Chapter-timed.
- Hayk Simonyan, Transport Layer Explained: TCP vs UDP, 0:00 to 5:08: [watch](https://www.youtube.com/watch?v=QyrHol2Ylfo&t=0s). A short explainer of the transport layer and its two protocols. Whole video.
- freeCodeCamp, System Design Course: APIs, Databases, Caching, CDNs, Load Balancing and Production Infra, Transport Layer: TCP, UDP, 59:10 to 1:04:22: [watch](https://www.youtube.com/watch?v=C842vFY5kRo&t=3550s). TCP and UDP inside a full system design course, between its API protocols and RESTful APIs chapters. Chapter-timed.

**Our plans and chapters**

- [HTTPS, and three round trips](/home/molef/goal-setting/learning/system-design/foundations/plans/09-https-and-three-round-trips.md), system-design/foundations, plan 09. Times the TCP connection with `curl -w` as the second of the three round trips a new HTTPS connection pays before its first byte.
- [The shell, curl and status codes](/home/molef/goal-setting/learning/system-design/foundations/textbook/04-the-shell-curl-and-status-codes.md), system-design/foundations, chapter 04, section 4.2. `ss -ltnp` lists the listening TCP sockets, and a server bound to `0.0.0.0:8099` is read against PostgreSQL bound to `127.0.0.1:5432`.
- [Chapter 0: The environment](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/textbook/00-the-environment.md), ai-engineering/product-data-validation-end-to-end, chapter 00, section 0.4. DBeaver reaches PostgreSQL over TCP through WSL2's localhost forwarding, where psql used a Unix socket, and what a missing TCP listener looks like.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-03-transport-and-app-protocols.jpg"><img src="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-03-transport-and-app-protocols.jpg" width="140" alt="Day 03 card: TCP against UDP, and the application protocols above them"></a> Tech Fusionist on X, "Day 3: Transport & App Protocols", from the 12-day networking playbook: [the post](https://x.com/techyoutbe/status/2074125684222685404), [what it shows](/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/README.md#the-twelve-day-cards). Section A sets TCP (reliable, ordered, connection-oriented, "like a phone call") against UDP, and section B draws the three-way handshake as SYN, SYN-ACK and ACK between a client and a server. The card ticks "reliable" and "ordered" without naming the sequence numbers, acknowledgements and retransmission that produce them, and it opens a connection without ever closing one with FIN and TIME_WAIT ([the reading](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/03-transport-and-app-protocols.md#what-it-flattens)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the chapter tables in `Textbooks.md` and a page-text search for "TCP" across the four system design books; System design interview names TCP once (keep-alive saving handshakes, page 180) and the other two books not at all. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title and the section named. Left out: the big archive's "8 Popular Network Protocols" (page 440), which repeats the handshake in one line. The Computer networking: a top-down approach lines were read with pdftotext on 2026-10-24, found through the book's back-of-book index and its outline in `Textbooks.md`.
