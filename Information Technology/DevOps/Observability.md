---
aliases: [observability, monitoring, telemetry, OpenTelemetry, distributed tracing]
link-skip: [Lakehouse Monitoring]
standard: vault-note v2
---

# Observability

Up: [[DevOps]]

Information Technology, DevOps. [[Latency]] percentiles are among the metrics it watches, and a [[Continuous Integration And Delivery]] pipeline uses its alerts to stop a bad release.

**Observability is collecting enough metrics, logs and traces from a running system to work out what went wrong inside it from the outside, while monitoring is the act of tracking those signals and alerting on them.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches observability writes the rest around it.

## Where to learn this

**Observability**, metrics, logs and traces that explain a running system. Also: monitoring, telemetry, OpenTelemetry, distributed tracing.

**Textbooks**

- AI engineering, chapter 10, Logs and traces: [pages 885 to 887](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=885). Works a debugging session: metrics say something broke five minutes ago, the logs from that moment say what happened, and a trace links one request's steps, with the time and cost of each.
- AI engineering, chapter 10, Monitoring and Observability: [pages 877 to 880](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=877). What monitoring is for, the three numbers that grade it (mean time to detection, mean time to response, change failure rate), and monitoring set against observability.
- System design interview, chapter 1, Logging, metrics, automation: [page 26](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=26). Error logs aggregated in one place, and host, tier-level and business metrics, as the tools a site needs once it grows.

**Videos**

- KodeKloud, How Prometheus Monitoring Works: Explaining Prometheus Architecture, Prometheus Architecture, 4:44 to 10:50: [watch](https://www.youtube.com/watch?v=f4W_eEJC-20&t=284s). Prometheus's parts, before the chapters on its pull model against a push model. Chapter-timed.
- Gaurav Sen, Google Dapper, a Large-Scale Distributed Systems Tracing Infrastructure, Request Tracing Requirements, 0:53 to 3:59: [watch](https://www.youtube.com/watch?v=AZhIjNHzURQ&t=53s). What tracing one request across services has to do, before Dapper's data schema, design and sampling. Chapter-timed.
- Arpit Bhayani, Stripe's Smarter Approach to Structured Logging: Canonical Log Lines, Structured logging, 1:08 to 2:40: [watch](https://www.youtube.com/watch?v=9XJtEzmzG3g&t=68s). Structured logging, after the problem with ordinary logs and before Stripe's one canonical line per request. Chapter-timed.

**Our plans and chapters**

- [One order, one trace](/home/molef/goal-setting/learning/system-design/foundations/plans/23-one-order-one-trace.md), system-design/foundations, plan 23. Every service instrumented with OpenTelemetry and one order's trace opened in Jaeger as a waterfall, one bar per hop across at least four services.
- [Prometheus, Grafana, and the alert](/home/molef/goal-setting/learning/system-design/foundations/plans/22-prometheus-grafana-and-the-alert.md), the same journey, plan 22. A `/metrics` endpoint on every service, scraped by Prometheus, with request rate, errors and p95 latency drawn in Grafana and an alert on them.
- [Watch and feed back: a 5xx alert becomes a card](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/22-watch-and-feed-back.md), system-design/devops-and-deployment, plan 22. Application Insights on production and an alert that counts only 5xx responses, fires under a bad release and opens a card on both boards.
- [OpenTelemetry through that port](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/plans/57-opentelemetry-through-it.md), ai-engineering/product-data-validation-end-to-end, plan 57. A tracer producing one span per run and one per check, with the article number and rule id as attributes, exported over OTLP to Jaeger.
- [System Design: Observability and Monitoring](/home/molef/goal-setting/learning/system-design/observability-and-monitoring/MASTER_PLAN.md), system-design/observability-and-monitoring. Metrics, structured logs with a correlation ID, a distributed trace and an alert rule, each on a toy multi-service system; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext; the AI engineering pages came from its back-of-book index ("monitoring and observability", 877 to 890, with "logs and traces" at 885 to 887), and the System design interview page from a pdftotext search of every page for "monitor" and "logging". The big archive has no post on observability and only lists monitoring tools in passing. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: AI engineering's metrics pages (881 to 885), the middle of the same section; [What a trace, a span and an attribute are](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/40-f1-trace-span.md) in many-sources-one-lakehouse, which teaches the same three words on MLflow traces. The bare words were sampled in the learning tree's prose: "monitoring" has 123 uses, mostly production monitoring, and the `link-skip` phrase covers Databricks' product Lakehouse Monitoring; "observability" has 87 and "telemetry" 11, all meaning this idea, including observability of LLM calls through MLflow traces.
