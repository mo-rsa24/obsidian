# Networking

Up: [[Information Technology]]

Information Technology, Networking. The API styles built on top of HTTP are under [[APIs]], in System Design. The textbook for the whole subject is Kurose and Ross, [[computer-networking-a-top-down-approach.pdf#page=31|Computer networking: a top-down approach]], which follows a request down the same layers.

**Networking is how one machine's request reaches another and the answer comes back. These notes follow a request down from the browser: the domain name looked up, the TCP or UDP connection, TLS encryption, the HTTP messages with their cookies and cross-origin rules, and the WebSocket that keeps a connection open. Under them sit the addresses and routes that carry every packet, and the private networks and firewalls a deployed service lives behind.**

## A request, top to bottom

- [[DNS]]: DNS is the internet's directory: a resolver turns a name such as shop.test into an IP address by asking the root, top-level-domain and authoritative name servers in turn, caching each answer for its time to live.
- [[TCP]]: TCP is the transport protocol that opens a connection with a three-way handshake and then delivers a stream of bytes reliably and in order, resending whatever is lost.
- [[UDP]]: UDP is the connectionless transport protocol: it sends each datagram on its own, with no handshake and no promise of delivery or order, which keeps it fast and light.
- [[TLS]]: TLS is the protocol that encrypts a connection: in its handshake the server proves who it is with a certificate signed by a trusted authority, the two sides agree on a session key, and everything after is encrypted with that key.
- [[Round Trip]]: A round trip is one message going from client to server and the reply coming back, and its duration, the round-trip time (RTT), is paid again for every exchange a request needs before its first byte arrives.
- [[HTTP]]: HTTP is the request and response protocol of the web: a client sends a method, a path and headers, and the server answers with a status code, headers and a body.
- [[HTTP Cookie]]: A cookie is a small named value a server sets with a `Set-Cookie` header; the browser stores it and sends it back on every later request to that site, which is how a site remembers a session.
- [[CORS]]: CORS is how a server tells a browser which other origins may read its responses: the browser's same-origin policy blocks a page from reading another origin's reply unless the server answers with an `Access-Control-Allow-Origin` header, and for some requests the browser first asks permission with an OPTIONS preflight request.
- [[WebSocket]]: A WebSocket is a persistent, two-way connection between a browser and a server: it starts as an HTTP request that is upgraded (status 101), and from then on either side can send a message at any time without a new request.

## Addresses, routes and private networks

- [[Network Layer]]: The network layer moves a packet across many networks: subnets, routing tables, DHCP and network address translation.
- [[Network Security]]: Network security decides which packets may cross a network's edge and keeps traffic private across the internet: firewalls and VPNs.
- [[Virtual Private Cloud]]: A virtual private cloud is a private network carved out of a cloud provider's data centre: you choose its address range and split it into subnets, and its route tables, gateways and security groups decide what can reach what.
