---
aliases: [TLS, HTTPS, SSL, SSL/TLS, TLS handshake, TLS certificate, SSL certificate, transport layer security, certificate authority, certification authority, root CA, local CA, mkcert]
standard: vault-note v2
---

# TLS

Up: [[Networking]]

Information Technology, Networking. TLS starts after the [[TCP]] handshake and turns [[HTTP]] into HTTPS; a [[Reverse Proxy]] often ends it in front of the servers.

**TLS is the protocol that encrypts a connection: in its handshake the server proves who it is with a certificate signed by a trusted authority, the two sides agree on a session key, and everything after is encrypted with that key.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches TLS writes the rest around it.

## Where to learn this

**TLS**, transport layer security, the S in HTTPS. Also: HTTPS, SSL, TLS handshake, TLS certificate, certificate authority, mkcert.

**Textbooks**

- Computer networking: a top-down approach, section 8.6, Securing TCP connections: SSL: [pages 661 to 667](../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=661). Builds the protocol in two passes: an almost-SSL first (the TCP connection, a hello, the server's certificate, a master secret encrypted under the server's public key, keys derived from it, and records carrying a MAC and a sequence number), then the real handshake's steps with the cipher list and the two nonces, and how a connection is closed.
- Computer networking: a top-down approach, section 8.3.3, Public key certification: [pages 647 to 650](../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=647). Why a public key needs a certificate, told as a pizza prank in which Trudy orders as Bob, then the certification authority that verifies an identity and signs the binding of a name to its public key with the authority's own private key.
- System design big archive, How does HTTPS work?: [pages 176 to 177](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=176). Walks one connection in four steps: the TCP connection, client hello and server hello with the cipher suites and TLS version, the certificate checked and a session key sent under the server's public key, then symmetric encryption, with the two reasons for switching to it.
- System design big archive, HTTP vs. HTTPS: [pages 395 to 396](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=395). Plain HTTP's readable traffic set against HTTPS's TCP handshake, certificate check, key exchange and encrypted data, with what the browser verifies in the certificate.
- Systems analysis and design, chapter 8, Architecture design, encryption and authentication requirements: [pages 324 to 325](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=324). The ideas a TLS certificate rests on: symmetric against public key encryption, digital signatures, and the public key infrastructure where a certificate authority signs a requester's public key.
- System design big archive, Which Protocols Run on TCP and UDP: [pages 371 to 372](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=371). HTTPS as TLS over TCP, the TCP connection first and the TLS handshake after, and QUIC carrying TLS 1.3 inside HTTP/3.

**Videos**

- Hussein Nasser, The TLS Handshake Explained with Example (the Math), 0:00 to 5:39: [watch](https://www.youtube.com/watch?v=64geP_LAZ5U&t=0s). The handshake worked through as an example with its maths, in under six minutes. Whole video.
- Hussein Nasser, Transport Layer Security, TLS 1.2 and 1.3 (Explained by Example), TLS 1.2, 8:35 to 14:30: [watch](https://www.youtube.com/watch?v=AlE5X1NlHgg&t=515s). The TLS 1.2 handshake worked by example, after chapters on plain HTTP and HTTPS and before Diffie-Hellman and TLS 1.3. Chapter-timed.
- ByteByteGo, SSL, TLS, HTTPS Explained, TLS, 1:06 to 5:54: [watch](https://www.youtube.com/watch?v=j9QmMEWmcfo&t=66s). TLS, after a short chapter on HTTPS. Chapter-timed.
- Hussein Nasser, What are SSL/TLS Certificates? Why do we Need them? and How do they Work?, How do they work, 8:41 to 14:35: [watch](https://www.youtube.com/watch?v=r1nJT63BFQ0&t=521s). How a certificate works, after a long chapter on why certificates are needed. Chapter-timed.
- Hussein Nasser, Certificates and Certificate Authority Explained, Certificate Authority, 6:30 to 8:30: [watch](https://www.youtube.com/watch?v=x_I6Qc35PuQ&t=390s). The authority that signs a server's certificate, after a chapter on how a client verifies a server and before one on checking the certificate itself. Chapter-timed.

**Our plans and chapters**

- [HTTPS, and three round trips](/home/molef/goal-setting/learning/system-design/foundations/plans/09-https-and-three-round-trips.md), system-design/foundations, plan 09. Puts the front nginx container on 443 with a certificate from the laptop's own mkcert authority, then times the TLS handshake with `curl -w` as the third round trip before the first byte.
- [Preflight: the tools answering](/home/molef/goal-setting/learning/system-design/foundations/textbook/00-preflight-docker-mkcert-dig-dbeaver.md), system-design/foundations, chapter 00, section 0.2. mkcert makes a private certificate authority and signs a certificate for `shop.test`, and where the authority is trusted (WSL or Windows) decides which browser shows a padlock.
- [System Design: Security and Auth](/home/molef/goal-setting/learning/system-design/security-and-auth/MASTER_PLAN.md), system-design/security-and-auth. Encryption in transit with TLS, and what it protects against, as the data protection objective; it holds goals and no plans yet.
- [Payment, notification, and a timeout](/home/molef/goal-setting/learning/system-design/foundations/plans/14-payment-notification-and-a-timeout.md), system-design/foundations, plan 14, instruction 3.3. Postman answers `unable to verify the first certificate` until mkcert's `rootCA.pem` is added under its CA certificates, which is what trusting a local certificate authority means for a second client.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-08-tls-ssl-and-vpn.jpg"><img src="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-08-tls-ssl-and-vpn.jpg" width="140" alt="Day 08 card: TLS handshake, certificate chain, and a site-to-site VPN tunnel"></a> Tech Fusionist on X, "Day 8: TLS/SSL & VPN", from the 12-day networking playbook: [the post](https://x.com/techyoutbe/status/2074125684222685404), [what it shows](/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/README.md#the-twelve-day-cards). Sections A and B draw the handshake in five steps (ClientHello, ServerHello with the certificate, key exchange, Finished, the encrypted session) and a certificate chain from the root CA through an intermediate to the example.com leaf, with the sticky note "TLS = encryption + identity". The handshake is the TLS 1.2 shape with no version label, while TLS 1.3 takes one round trip; the client's signature check at each link of the chain against its own trust store is missing; and in ordinary TLS only the server proves its identity ([the reading](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/08-tls-ssl-and-vpn.md#what-it-flattens)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the chapter tables in `Textbooks.md`, a page-text search for "TLS", "SSL" and "HTTPS" across the four system design books, and the Systems analysis and design back-of-book index ("Encryption", "PKI"). Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title, description and the section named. Left out: the TLS 1.3 chapter of Hussein Nasser's TLS video (17:55 to 24:20), to keep the list short; the big archive's How HTTPS Works? (pages 256 to 257), a second telling of pages 176 to 177 that adds only the change cipher spec message; System design interview's mention of SSL termination at an API gateway (page 54). The Computer networking: a top-down approach lines were read with pdftotext on 2026-10-24, found through the book's back-of-book index and its outline in `Textbooks.md`.
