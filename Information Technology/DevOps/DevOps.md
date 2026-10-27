# DevOps

Up: [[Information Technology]]

Information Technology, DevOps. The tools themselves, [[Docker]] and [[Kubernetes]], are under Software.

**DevOps is the practice of building, shipping and running software as one loop. These notes cover the pipeline that tests and deploys every change, infrastructure written as code, and watching the running system.**

- [[Continuous Integration And Delivery]]: Continuous integration runs automated builds and tests on every change pushed to a shared repository, and continuous delivery carries each passing build toward production, with continuous deployment releasing it there without a human step.
- [[Infrastructure As Code]]: Infrastructure as code declares servers, databases and networks in versioned files that a tool such as Terraform or Bicep compares with what exists and then creates, changes or destroys to match.
- [[Observability]]: Observability is collecting enough metrics, logs and traces from a running system to work out what went wrong inside it from the outside, while monitoring is the act of tracking those signals and alerting on them.
- [[Alerting]]: Alerting is a rule that watches a metric and notifies a person or opens a ticket when the value crosses a threshold for long enough, so a failure is noticed by the team before a user reports it.
- [[Distributed Tracing]]: Distributed tracing follows one request across every service it touches: an ID minted at the edge travels with the request, each service records a timed span under it, and the spans join into one trace drawn as a waterfall.
- [[Canary Release]]: A canary release runs the new version beside the old one and sends it a small share of real traffic, watches a measured signal such as its server-error rate against a stop line written beforehand, and only then moves the rest of the traffic across or rolls back.
- [[Rollback]]: A rollback puts the last version that worked back in front of users, by redeploying its image or moving traffic back to it, when a release fails its checks.
- [[Smoke Test]]: A smoke test is a handful of quick calls that check a freshly built or deployed system starts and answers its most important request, run before slower tests or right after a release.
- [[Rolling Update]]: A rolling update replaces the copies of a running service with the new version a few at a time, taking each out of the load balancer before it is upgraded, so the service keeps answering while old and new versions serve side by side.
- [[Blue-Green Deployment]]: A blue-green deployment keeps two identical production environments, releases the new version to the idle one, tests it there, then switches the load balancer so all traffic moves at once, leaving the old environment ready to switch back to.
- [[Service Level Objective]]: A service level objective is a target for a measured signal of a service, such as 99.9% availability over a year, and the room left below the target is the error budget that decides whether releases can keep going out.
- [[Feature Flag]]: A feature flag is a switch read at runtime that turns a piece of already deployed code on or off, for everyone or for chosen users, so shipping the code and releasing the feature become two separate steps.
