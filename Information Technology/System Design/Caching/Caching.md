# Caching

Up: [[System Design]]

Information Technology, System Design, Caching. The [[KV Cache]] of a language model is its own note under Artificial Intelligence, and [[Redis]] is under Software.

**Caching keeps copies of data close to where it is used, so a repeated request is answered fast without going back to the source. The hard part is deciding how long a copy may be served before it is stale.**

- [[Cache]]: A cache is a small, fast store that keeps copies of data read often, so a repeated request is answered without going back to the slower place the data lives.
- [[Time To Live]]: A time to live (TTL) is the number of seconds a stored copy may be served before it counts as expired and must be fetched again from its source.
- [[Content Delivery Network]]: A content delivery network (CDN) is a set of servers spread across many locations that keep copies of static files, so each user is served from the server nearest them instead of from the origin.
