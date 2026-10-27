---
aliases: [round trips, one round trip, each round trip, per round trip, round-trip time, RTT]
link-not: [Round Trip]
link-skip: [round-trip note, one round trip out and back, every stage of one round trip]
standard: vault-note v2
---

# Round Trip

Up: [[Networking]]

Information Technology, Networking. A [[TCP]] handshake costs one round trip and a [[TLS]] handshake at least one more, which is why [[Latency]] has a floor that no faster server removes.

**A round trip is one message going from client to server and the reply coming back, and its duration, the round-trip time (RTT), is paid again for every exchange a request needs before its first byte arrives.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches round trips writes the rest around it.

## Where to learn this

**Round trip**, one crossing out and back. Also: round trips, round-trip time, RTT.

**Textbooks**

- Computer networking: a top-down approach, section 2.2.2, Non-persistent and persistent connections: [pages 132 to 133](../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=132). Defines the RTT as a small packet's time from client to server and back, with propagation, queuing and processing delays inside it, then works one page fetch as two RTTs plus the file's transmission time: one RTT for the first two parts of the TCP handshake, one for the request and its response, and persistent connections saving the first one on every later object.
- Computer networking: a top-down approach, section 1.4.3, End-to-end delay: [page 72](../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=72). Traceroute measures the round-trip delay to every router between gaia.cs.umass.edu and cis.poly.edu, three probes each, and the real output climbs from about 1 ms at the first hop to about 13 ms in New York.
- Computer networking: a top-down approach, section 3.5.3, Round-trip time estimation and timeout: [pages 271 to 274](../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=271). How TCP measures a SampleRTT per segment, smooths it into EstimatedRTT = 0.875 · EstimatedRTT + 0.125 · SampleRTT, plots the two against each other, and sets its retransmission timeout from the estimate and its deviation.
- System design big archive, Network debugging commands every engineer should know: [pages 433 to 434](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=433). `ping` reporting the round-trip time, then `traceroute` and `mtr` showing where on the path the delay and loss build up.
- System design big archive, REST API vs. GraphQL: [pages 234 to 235](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=234). REST may need several round trips to assemble related data from separate endpoints, where GraphQL asks one endpoint for exactly the fields it needs.

**Videos**

- Hello Interview, Networking Essentials for System Design Interviews, TCP/UDP, 7:38 to 12:37: [watch](https://www.youtube.com/watch?v=SHkbPm1Wrno&t=458s). TCP's handshake and what it guarantees, set against UDP, which sends with no handshake. Chapter-timed.
- ByteByteGo, HTTP 1 Vs HTTP 2 Vs HTTP 3!, HTTP III, 5:43 to 7:21: [watch](https://www.youtube.com/watch?v=UMwQjFzTQXw&t=343s). HTTP/3, after the chapters on HTTP/1.1 and HTTP/2's single connection. Chapter-timed.
- Practical Networking, TLS 1.3 Handshake: many changes from prior versions, TLS 1.3 One Round Trip Handshake (1RTT) simply explained, 2:46 to 5:48: [watch](https://www.youtube.com/watch?v=JA0vaIb4158&t=166s). TLS 1.3 finishing its handshake in one round trip where TLS 1.2 took two, followed by a chapter on the zero round trip resumption. Chapter-timed.
- Hussein Nasser, What is the TCP 3-Way Handshake and Why Backend Engineers should understand it, Impact of Handshake on Performance, 8:50 to 11:37: [watch](https://www.youtube.com/watch?v=bW_BILl7n0Y&t=530s). What the handshake's round trip costs a backend, after the chapter that walks the handshake itself. Chapter-timed.

**Our plans and chapters**

- [HTTPS, and three round trips](/home/molef/goal-setting/learning/system-design/foundations/plans/09-https-and-three-round-trips.md), system-design/foundations, plan 09. Saves one request's `time_namelookup`, `time_connect`, `time_appconnect` and `time_starttransfer` from `curl -w` and places them on three bands, the DNS lookup, the TCP connection and the TLS handshake, as the round trips paid before the first byte.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each Kurose page range was read with pdftotext after the book's back-of-book index ("round-trip time (RTT)", PDF page 132; "RTT estimation", 271); the big archive pages came from a page-text search for "round trip" across the four system design books, which System design interview, Grokking and Systems analysis and design never use. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; Hello Interview's captions were unavailable. The plan was read at its description, goal and video table. Left out: Kurose's congestion control pages, where the RTT sets how fast the window grows, since the card points at the round trip itself; the big archive's "full round trip" in its transactions-per-second definition (page 430), which means one request's whole path. Bare "round trip" is left out of the card's words with `link-not`, because across the learning tree it mostly names something else: a journey's capstone run end to end, a VAE's encode and decode, a speech-to-text-to-speech pipeline, a base64 or migration round trip. The plural and the counted forms ("three round trips", "one round trip", "each round trip") link, and the skip phrases keep the three counted uses that mean a capstone or a migration plain.
