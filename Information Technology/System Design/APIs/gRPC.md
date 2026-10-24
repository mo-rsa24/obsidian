---
aliases: [protocol buffers, protobuf]
standard: vault-note v2
---

# gRPC

Up: [[APIs]]

Information Technology, System Design. A [[REST API]] and [[GraphQL]] are the styles it is weighed against, and it runs over HTTP/2 (see [[HTTP]]).

**gRPC is a remote procedure call framework: a service and its messages are defined in a protocol buffers file, code is generated from it, and a client calls a method on another machine as if it were local, with the call sent as compact binary over HTTP/2.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches gRPC writes the rest around it.

## Where to learn this

**gRPC**, remote calls defined in protocol buffers and sent over HTTP/2. Also: protocol buffers, protobuf.

**Textbooks**

- System design big archive, How does gRPC work?: [pages 12 to 13](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=12). Walks one call in 14 steps: a REST call reaches an order service, which as gRPC client encodes a call to the payment service into binary, sends it over HTTP/2, and decodes the reply on the way back, with gRPC put at 5 times faster than JSON.

**Videos**

- Hussein Nasser, gRPC Crash Course: Modes, Examples, Pros & Cons and more, gRPC Coding Example!, 19:49 to 57:00: [watch](https://www.youtube.com/watch?v=Yw4rkaTc0f8&t=1189s). A gRPC service coded on screen, after the motivation and the four call modes (unary, server streaming, client streaming, bidirectional). Chapter-timed.
- ByteByteGo, What is RPC? gRPC Introduction., Protocol buffers explained, 0:56 to 1:42: [watch](https://www.youtube.com/watch?v=gnchfOojMk4&t=56s). Protocol buffers, after a chapter on what a remote procedure call is and before the chapters on HTTP/2 and the request flow. Chapter-timed.
- ByteByteGo, What is RPC? gRPC Introduction., The gRPC request flow, 3:32 to 4:41: [watch](https://www.youtube.com/watch?v=gnchfOojMk4&t=212s). One request through gRPC. Chapter-timed.
- Hussein Nasser, Protocol Buffers Crash Course, Writing .proto file, 8:20 to 14:00: [watch](https://www.youtube.com/watch?v=46O73On0gyI&t=500s). An app first written with JSON and then rewritten with protocol buffers, starting from its `.proto` file and going on to `protoc`. Chapter-timed.

**Our plans and chapters**

- [System Design: API Design and Contracts](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/MASTER_PLAN.md), system-design/api-design-and-contracts. One resource built as a REST API, a gRPC service and a GraphQL schema; its sources show a `.proto` service and a client call. It holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The textbook page range was read with pdftotext after the chapter tables in `Textbooks.md` and a page-text search for "gRPC" and "protocol buffers" across the four system design books; every other page names gRPC in a list of API styles. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. The master plan was read at its objectives, goals and its REST, GraphQL and gRPC source entry. Left out: Arpit Bhayani's account of Jira moving from JSON to Protobuf (`roNgG4QVjTU`) and Hussein Nasser's This is why gRPC was invented (`u4LWEXDP7_M`), neither read at its chapters. The name gRPC matches in any case and names nothing else.
