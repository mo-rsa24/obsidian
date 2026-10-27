---
aliases: [distributed tracing, distributed trace, trace ID, span ID, span, request ID, correlation ID, X-Request-ID, Jaeger]
link-only-in: [system-design/foundations, system-design/observability-and-monitoring, ai-engineering/one-business-end-to-end, ai-engineering/product-data-validation-end-to-end, data-engineering/many-sources-one-lakehouse, ai-engineering/kestrel-judged-in-mlflow-corridor, ai-engineering/genie-on-databricks, ai-engineering/genie-improvement-loop-corridor, document-qa-with-permissions/plans]
link-skip: [hash the request id, hashing the request id, made-up request ids, request id into the draft, request id reaches the draft, that request ID, its request ID, three request IDs, request ID and session, session and request IDs, two systems no single, time span, a span of, date span]
link-skip-in: [many-sources-one-lakehouse/plans/17-h1-envelope-math]
standard: vault-note v2
---

# Distributed Tracing

Up: [[DevOps]]

Information Technology, DevOps. Traces are one of the three signals [[Observability]] collects, and a trace shows where a request's [[Latency]] went hop by hop.

**Distributed tracing follows one request across every service it touches: an ID minted at the edge travels with the request, each service records a timed span under it, and the spans join into one trace drawn as a waterfall.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches distributed tracing writes the rest around it.

## Where to learn this

**Distributed tracing**, one request followed across services as a tree of timed spans under one ID. Also: distributed trace, trace ID, span ID, span, request ID, correlation ID, X-Request-ID, Jaeger.

**Textbooks**

- AI engineering, chapter 10, Logs and traces: [page 887](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=887). A trace as related events linked into one timeline of a request's path through the system, with the time and cost of each step, shown as a LangSmith trace on the next page.

**Videos**

- KodeKloud, How Distributed Tracing Works Across Microservices in Kubernetes, 0:00 to 2:36: [watch](https://www.youtube.com/watch?v=nzg8KxL5ftI&t=0s). A trace ID carried across microservices and the spans joined into one trace. Whole video.
- Gaurav Sen, Google Dapper, a Large-Scale Distributed Systems Tracing Infrastructure, Data Schema, 3:59 to 6:15: [watch](https://www.youtube.com/watch?v=AZhIjNHzURQ&t=239s). How Dapper records a trace, after the chapter on what request tracing has to do. Chapter-timed.
- Gaurav Sen, Google Dapper, a Large-Scale Distributed Systems Tracing Infrastructure, Request Tracing Requirements, 0:53 to 3:59: [watch](https://www.youtube.com/watch?v=AZhIjNHzURQ&t=53s). What tracing one request across services has to do. Chapter-timed.

**Our plans and chapters**

- [One request ID on every line](/home/molef/goal-setting/learning/system-design/foundations/plans/21-one-request-id.md), system-design/foundations, plan 21. One `X-Request-ID` minted at the nginx balancer, passed through the gateway to every service an order touches, and that order's lines pulled out of `docker compose logs` with one `grep`.
- [One order, one trace](/home/molef/goal-setting/learning/system-design/foundations/plans/23-one-order-one-trace.md), the same journey, plan 23. Every service instrumented with OpenTelemetry, spans sent to Jaeger, and one order's trace opened as a waterfall with one bar per hop across at least four services.
- [What a trace, a span and an attribute are](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/40-f1-trace-span.md), data-engineering/many-sources-one-lakehouse, plan 40. The three words defined, then a three-span toy built in an empty folder and read in the MLflow interface.
- [A span tree drawn by hand for one agent request](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/63-a-span-tree-by-hand.md), ai-engineering/one-business-end-to-end, plan 63. One agent request drawn as nested timed bars, the children inside the parent and adding to less than it.
- [Spans emitted yourself](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/64-spans-emitted-yourself.md), the same journey, plan 64. The same tree emitted with the OpenTelemetry SDK and a console exporter, the model-call span carrying tokens and rand cost as attributes.
- [One run walked in Jaeger](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/plans/58-one-run-in-jaeger.md), ai-engineering/product-data-validation-end-to-end, plan 58. One pipeline run read top to bottom in Jaeger at `localhost:16686`, answering four questions off the trace.
- [System Design: Observability and Monitoring](/home/molef/goal-setting/learning/system-design/observability-and-monitoring/MASTER_PLAN.md), system-design/observability-and-monitoring. Goals 2 and 3: a correlation ID shared by every log line of one request, then a distributed trace of the same multi-service system; it holds goals and no plans yet.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/observability-and-monitoring/artifacts/figures/logs-metrics-traces/levelupcoding-logs-vs-metrics-vs-traces.jpg"><img src="/home/molef/goal-setting/learning/system-design/observability-and-monitoring/artifacts/figures/logs-metrics-traces/levelupcoding-logs-vs-metrics-vs-traces.jpg" width="200" alt="Three stacked bands for logs, metrics and traces, each flowing from a source through a named tool to an incident"></a> Nikki Siapno (Level Up Coding) on X, "Logs vs Metrics vs Traces": [the post](https://x.com/NikkiSiapno/status/2098034092164219230), [what it shows](/home/molef/goal-setting/learning/system-design/observability-and-monitoring/artifacts/figures/logs-metrics-traces/README.md#levelupcoding-logs-vs-metrics-vs-tracesjpg). The traces band draws one request crossing a mesh of services and databases, its operations correlated by trace and span IDs and read in Grafana or New Relic to find which service caused the latency or failure. It never shows a correlation ID shared between a log line and a trace ([the reading](/home/molef/goal-setting/learning/system-design/observability-and-monitoring/sources/logs-metrics-traces/SOURCES.md#logs-vs-metrics-vs-traces-by-nikki-siapno)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The textbook page was read with pdftotext after a page-text search for "distributed tracing", "trace ID", "span ID", "request ID", "correlation ID", "Jaeger", "Zipkin", "Dapper" and "OpenTelemetry" across the system design books and AI engineering; the only other hit is the big archive's list of AWS services naming X-Ray (page 146). Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title, the video title and, for the KodeKloud line, the segment note in `system-design/foundations/video-scout/pulse-2026-10-24.md`. Each plan was read at its title and description. Left out: [OpenTelemetry through that port](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/plans/57-opentelemetry-through-it.md), which [[Observability]] carries; the compiled chapters for plans 21 and 23, whose sections are headings with no text yet. Bare "trace" and "tracing" are not aliases: across the learning tree about 400 of their 1,577 prose uses are the verb (trace a route, trace the derivation), and others are a matrix trace, Langevin traces and stack traces. Bare "span" links only in the folders listed under `link-only-in`, where it means a tracing span; elsewhere it is the verb, a linear-algebra span or a text span. Inside those folders a dry run linked 214 uses of "span" and "spans", and those that meant something else ("no single transaction spans", a "time span", a "date span" and "a span of" two dates) are `link-skip` phrases; the lakehouse envelope-maths plan 17 uses "span" only for its date range, so it is under `link-skip-in`. The other `link-skip` phrases cover "request ID" as an A/B-test hashing key (hypothesis-testing plan 03, the Redis use-cases prerequisites), as Attica's booking request, and as an approval request in the prototype product-data-validation journey.
