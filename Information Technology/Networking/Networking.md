# Networking

Up: [[Information Technology]]

Information Technology, Networking. The API styles built on top of HTTP are under [[APIs]], in System Design.

**Networking is how one machine's request reaches another and the answer comes back. These notes follow a request down from the browser: the domain name looked up, the TCP or UDP connection, TLS encryption, the HTTP messages with their cookies and cross-origin rules, and the WebSocket that keeps a connection open.**

- [[DNS]]: DNS is the internet's directory: a resolver turns a name such as shop.test into an IP address by asking the root, top-level-domain and authoritative name servers in turn, caching each answer for its time to live.
- [[TCP]]: TCP is the transport protocol that opens a connection with a three-way handshake and then delivers a stream of bytes reliably and in order, resending whatever is lost.
- [[UDP]]: UDP is the connectionless transport protocol: it sends each datagram on its own, with no handshake and no promise of delivery or order, which keeps it fast and light.
- [[TLS]]: TLS is the protocol that encrypts a connection: in its handshake the server proves who it is with a certificate signed by a trusted authority, the two sides agree on a session key, and everything after is encrypted with that key.
- [[HTTP]]: HTTP is the request and response protocol of the web: a client sends a method, a path and headers, and the server answers with a status code, headers and a body.
- [[HTTP Cookie]]: A cookie is a small named value a server sets with a `Set-Cookie` header; the browser stores it and sends it back on every later request to that site, which is how a site remembers a session.
- [[CORS]]: CORS is how a server tells a browser which other origins may read its responses: the browser's same-origin policy blocks a page from reading another origin's reply unless the server answers with an `Access-Control-Allow-Origin` header, and for some requests the browser first asks permission with an OPTIONS preflight request.
- [[WebSocket]]: A WebSocket is a persistent, two-way connection between a browser and a server: it starts as an HTTP request that is upgraded (status 101), and from then on either side can send a message at any time without a new request.
