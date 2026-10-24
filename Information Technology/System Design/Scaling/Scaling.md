# Scaling

Up: [[System Design]]

Information Technology, System Design, Scaling. Splitting the data itself is in [[Sharding]] and [[Database Replication]], under Database Systems.

**Scaling is how a system takes on more load: a bigger machine, or more machines with traffic spread across them. Latency and throughput are the two numbers that say whether it worked.**

- [[Scalability]]: Scalability is a system's ability to take on more load by adding resources, either a bigger machine (vertical scaling) or more machines (horizontal scaling), without its performance falling away.
- [[Load Balancer]]: A load balancer receives every incoming request and passes each one to one of several identical servers, so the traffic is shared and a failed server is routed around.
- [[Reverse Proxy]]: A reverse proxy is a server that stands in front of backend servers and takes every client request on their behalf, while a forward proxy stands in front of clients and makes their requests on theirs.
- [[Stateless Service]]: A stateless service keeps nothing about a client between requests, so every request carries or fetches what it needs and any copy of the service can answer it; a stateful service remembers the client and must keep seeing the same client.
- [[Consistent Hashing]]: Consistent hashing places servers and keys on the same ring of hash values and stores each key on the first server clockwise from it, so adding or removing a server moves only about k/n of the k keys instead of nearly all of them.
- [[Latency]]: Latency is the time one request takes from being sent to its answer arriving, and because it varies from request to request it is read as percentiles: p95 is the time 95% of requests beat.
- [[Throughput]]: Throughput is how much work a system completes per unit of time, usually counted as requests or queries per second (RPS or QPS), or tokens per second for a model.
