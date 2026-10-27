# Reliability

Up: [[System Design]]

Information Technology, System Design, Reliability. Two requests changing the same thing at once is in [[Race Condition]], under Concurrency.

**Reliability is a system doing the right thing when its parts are slow or fail. These notes cover giving up on time, trying again safely, making a repeated request harmless, and checking that a service is alive.**

- [[Timeout]]: A timeout is the longest a caller will wait for a reply before giving up and treating the call as failed, so one slow or silent service cannot hold every caller behind it.
- [[Retry With Backoff]]: Retry with backoff sends a failed request again after a pause that grows with each attempt (1 second, then 2, then 4), up to a limit, often with a little random jitter so many clients do not retry at the same instant.
- [[Idempotency]]: An operation is idempotent when doing it twice has the same effect as doing it once; an idempotency key lets a server recognise a retried request and return the first result instead of charging or booking again.
- [[Health Check]]: A health check is a small request a load balancer, orchestrator or monitor sends to a service on a schedule, often to an endpoint such as `/healthz`, to decide whether the service is alive and ready for traffic; a service that fails it is taken out of rotation or restarted.
- [[Circuit Breaker]]: A circuit breaker sits in front of calls to another service and counts failures; past a threshold it trips open and fails every call at once without sending it, then after a pause lets a trial call through and closes again if that call succeeds, so one failing service cannot drag its callers down with it.
