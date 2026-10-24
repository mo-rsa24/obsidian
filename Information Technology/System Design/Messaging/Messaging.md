# Messaging

Up: [[System Design]]

Information Technology, System Design, Messaging. [[Apache Kafka]] is under Software, and the [[WebSocket]] connection is under Networking.

**Messaging lets one part of a system hand work or news to another without waiting for it. These notes cover queues and publish-subscribe, fanning one event out to many readers, the outbox that makes sending reliable, and the two ways an outside party hears about a change: being called back or asking again.**

- [[Message Queue]]: A message queue is a buffer between services: a producer writes a message and moves on, and a worker takes it off the queue and does the work later, so neither side waits for the other.
- [[Publish-Subscribe]]: Publish-subscribe is a messaging pattern where a publisher sends a message to a named topic or channel and every service subscribed to it receives its own copy, without the publisher knowing who they are.
- [[Fan-Out]]: Fan-out is delivering one event to many recipients, as when one post is copied into the feed of every follower; a design chooses to do that work when the post is written or when each feed is read.
- [[Outbox Pattern]]: The outbox pattern writes a service's data change and the event announcing it into the same database transaction, the event as a row in an outbox table, so a separate relay can publish it to the broker afterwards and the two can never disagree.
- [[Webhook]]: A webhook is an HTTP request that another system sends to a URL you registered with it, the moment something happens on its side, such as a payment provider confirming a charge.
- [[Polling]]: Polling is a client asking a server again and again whether anything has changed; long polling keeps each request open until there is news or a timeout, so the answer arrives sooner and fewer requests come back empty.
