# APIs

Up: [[System Design]]

Information Technology, System Design, APIs. The protocol underneath is [[HTTP]], under Networking.

**An API is the contract a service offers other programs. These notes cover the three common styles, the gateway in front of a set of services, and the rules that keep an API usable as it grows: versions, pages, limits and the middleware every request passes through.**

- [[REST API]]: A REST API exposes resources at URLs and lets clients act on them with the standard HTTP methods (GET, POST, PUT, DELETE), each request carrying everything the server needs, so the server keeps no session state between calls.
- [[GraphQL]]: GraphQL is an API style with a single endpoint and a typed schema, where the client writes a query naming exactly the fields it wants, nested as deep as it needs, and gets back only those fields.
- [[gRPC]]: gRPC is a remote procedure call framework: a service and its messages are defined in a protocol buffers file, code is generated from it, and a client calls a method on another machine as if it were local, with the call sent as compact binary over HTTP/2.
- [[API Gateway]]: An API gateway is the single entry point in front of a set of backend services: it checks each request (authentication, rate limits, validation) and routes it by path to the service that owns it.
- [[Middleware]]: Middleware is code that sits in a request's path before the handler: each piece sees the request, can check or change it (a token check, a rate limit, a log line) and either passes it on or answers it itself.
- [[Rate Limiter]]: A rate limiter caps how many requests a client may make in a stretch of time and rejects the rest, usually with HTTP 429, to protect a service from overload and abuse.
- [[Pagination]]: Pagination returns a long list in pages: offset pagination asks for "skip 20, take 10", which slows down and skips or repeats rows when rows are inserted mid-scroll, while cursor (keyset) pagination asks for "the 10 after this last key", which stays fast and stable.
- [[API Versioning]]: API versioning lets an API change without breaking the clients already calling it: a breaking change goes out under a new version (in the URL, such as `/v2/orders`, or in a header) while the old version keeps answering until its clients have moved.
