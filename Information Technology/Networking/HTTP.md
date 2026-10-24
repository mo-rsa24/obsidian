---
aliases: [HTTP, HTTP/2, HTTP/3, HTTP request, HTTP response, status code, hypertext transfer protocol]
standard: vault-note v2
---

# HTTP

Up: [[Networking]]

Information Technology, Networking. HTTP rides on [[TCP]] (and HTTP/3 on [[UDP]]), finds its server through [[DNS]], and becomes HTTPS when [[TLS]] wraps it.

**HTTP is the request and response protocol of the web: a client sends a method, a path and headers, and the server answers with a status code, headers and a body.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches HTTP writes the rest around it.

## Where to learn this

**HTTP**, the request and response protocol of the web. Also: HTTP request, status code, HTTP/2, HTTP/3.

**Textbooks**

- System design interview, chapter 1, Scale from zero to millions of users: [page 7](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=7). Works one request with real values: DNS returns 15.125.23.214, then an HTTP request goes straight to the web server, which answers `GET /users/12` with a JSON user.
- System design big archive, Evolution of HTTP: [pages 427 to 428](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=427). Each version in one line: HTTP/0.9's single GET, HTTP/1.0's headers and status codes with a new connection per request, HTTP/1.1's persistent connections, HTTP/2's multiplexing and HTTP/3 moving to QUIC over UDP.
- System design big archive, HTTP/1 -> HTTP/2 -> HTTP/3: [pages 79 to 80](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=79). The dates (1996, 1997, 2015, 2019) and what each version added: pipelining and headers, then stream prioritization, server push and HPACK compression, then QUIC.
- System design big archive, Common HTTP Status Codes: [pages 262 to 263](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=262). The five classes of status code, each with an example: 100 Continue, 200 OK, 301 Moved Permanently, 404 Not Found and 500 Internal Server Error.
- System design interview, chapter 12, Design a chat system: [pages 180 to 183](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=180). Why HTTP being client-initiated makes server push hard: keep-alive for the sender, then polling, long polling and the WebSocket upgrade for the receiver.

**Videos**

- Hussein Nasser, Hyper Text Transfer Protocol Crash Course, Demo Request/Response, Build Web Server, 12:00 to 20:20: [watch](https://www.youtube.com/watch?v=0OrmKCB0UrQ&t=720s). A request and its response shown on a web server built in the video, after the chapters on the request and the response, in a crash course that ends on HTTP 1.0, 1.1, HTTP/2 and HTTP/3. Chapter-timed.
- Arpit Bhayani, What exactly is the HTTP protocol and how to write a new one from scratch?, Raw TCP HTTP request demo, 3:10 to 6:12: [watch](https://www.youtube.com/watch?v=SzwjnoPI--M&t=190s). An HTTP request typed by hand over a raw TCP connection. Chapter-timed.
- ByteByteGo, HTTP 1 Vs HTTP 2 Vs HTTP 3!, HTTP II, 3:32 to 5:43: [watch](https://www.youtube.com/watch?v=UMwQjFzTQXw&t=212s). HTTP/2, between the chapters on HTTP/1.1 and HTTP/3. Chapter-timed.
- ByteByteGo, HTTP Status Codes Explained In 5 Minutes, Troubleshooting 400s errors, 1:02 to 2:22: [watch](https://www.youtube.com/watch?v=qmpUfWN7hh4&t=62s). The 4xx client errors, after the 2xx chapter and before the 5xx and 3xx ones. Chapter-timed.

**Our plans and chapters**

- [The shell, curl and status codes](/home/molef/goal-setting/learning/system-design/foundations/textbook/04-the-shell-curl-and-status-codes.md), system-design/foundations, chapter 04. Reads one `curl -v` transcript line by line against a Python server, then gets 200, 404 and 000 from it and says which hop writes each code.
- [The app, HTTP, Azure and the boards](/home/molef/goal-setting/learning/system-design/devops-and-deployment/textbook/05-the-app-http-azure-and-the-boards.md), system-design/devops-and-deployment, chapter 05. Five status codes from one endpoint of the bookshop app, and which of them an alert counts.
- [The Python pieces](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/01-the-python-pieces.md), ai-engineering/prototype-product-data-validation-end-to-end, chapter 01, section 1.4. A GET with no time limit hanging on a silent server, then JSON sent to an echo server, from Python.
- [HTTP/WebSocket Handshake](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/01-distributed-systems-primitives/plans/01-http-websocket-handshake.md), projects/tms-mobility/system-design/plans/01-distributed-systems-primitives, plan 01. The HTTP request and response cycle, then the WebSocket upgrade handshake, for real-time dispatch.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the chapter tables in `Textbooks.md` and a page-text search for "HTTP" across the four system design books; Grokking the system design interview and Systems analysis and design only mention HTTP in passing. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title and the section named. Left out: the big archive's HTTP Mindmap (pages 421 to 422), a map of the field rather than a teaching page; the big archive's "What happens when you type a URL into a browser" (pages 254 to 255), which sits on the [[DNS]] card. The alias HTTP/1.1 is not listed, because a slash alias holding a dot is never matched in prose.
