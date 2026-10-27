# System Design

Up: [[Information Technology]]

Information Technology, System Design. The database parts of a design are under [[Database Systems]], the wire under [[Networking]], and the installable building blocks ([[Redis]], [[Nginx]], [[Apache Kafka]]) under Software.

**System design is choosing the parts of a service and how they talk so it stays fast and correct as users grow. These notes group the building blocks by the job they do: caching, scaling, APIs, messaging and reliability, with a few that stand alone.**

- [[Caching]]: Caching keeps copies of data close to where it is used, so a repeated request is answered fast without going back to the source.
- [[Scaling]]: Scaling is how a system takes on more load: a bigger machine, or more machines with traffic spread across them.
- [[APIs]]: An API is the contract a service offers other programs.
- [[Messaging]]: Messaging lets one part of a system hand work or news to another without waiting for it.
- [[Reliability]]: Reliability is a system doing the right thing when its parts are slow or fail.
- [[Microservices]]: Microservices is an architecture that splits one application into small services, each owning one business capability and its own data, deployed on its own and reached over the network, where a monolith keeps everything in one deployable unit.
- [[Object Storage]]: Object storage keeps whole files (images, videos, PDFs) as objects in flat buckets, each reached by a key over HTTP, and copies every object across machines so it survives disk and server failures; Amazon S3 is the standard example, and MinIO and Azure Blob Storage speak the same idea.
- [[Full-Text Search]]: Full-text search finds documents by the words they contain: an inverted index maps each term to the documents holding it, and a scorer such as BM25 ranks the matches by how often the query's rarer terms appear.
- [[Service Discovery]]: Service discovery is how a service finds the current address of another one by name: each running copy registers itself in a service registry (or is found through DNS), callers or a gateway ask the registry, and copies that stop sending heartbeats are dropped from it.
- [[Saga Pattern]]: A saga carries out one business operation across several services as a sequence of local transactions, each committed on its own; when a later step fails, the saga runs a compensating transaction for every step already done, so the system ends consistent without one transaction spanning every database.
- [[Eventual Consistency]]: Eventual consistency is the guarantee that once writes stop, every replica converges to the same value, while a read made before then may return an older value from a replica that has not caught up.
- [[Software Architecture]]: Software architecture here is how the code inside one service is arranged so the business rules do not depend on the database, the web framework or any other detail. These notes follow the clean architecture and its hexagonal twin, in the order a learner builds them.
