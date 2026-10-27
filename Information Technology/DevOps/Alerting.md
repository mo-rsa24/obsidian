---
aliases: [alerting, alert, alert rule, alerting rule, Alertmanager, alert fatigue]
link-skip: [GitHub alert]
standard: vault-note v2
---

# Alerting

Up: [[DevOps]]

Information Technology, DevOps. Alerts fire on the metrics that [[Observability]] collects, and a [[Health Check]] is often the signal behind one.

**Alerting is a rule that watches a metric and notifies a person or opens a ticket when the value crosses a threshold for long enough, so a failure is noticed by the team before a user reports it.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches alerting writes the rest around it.

## Where to learn this

**Alerting**, a rule on a metric that tells someone when it crosses a threshold. Also: alert, alert rule, alerting rule, Alertmanager, alert fatigue.

**Textbooks**

- System design interview, chapter 10, Design a notification system, retry mechanism and monitoring: [page 161](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=161). Works one case: a failed send goes back on the queue for a retry, and an alert goes to developers if the failure persists; the number to watch is the count of queued notifications, which says when more workers are needed.
- AI engineering, chapter 10, Monitoring and Observability: [page 878](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=878). The three numbers that grade how well failures are caught: mean time to detection, mean time to response and change failure rate.
- System design big archive, 10 Essential Components of a Production Web Application: [pages 34 to 35](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=34). Monitoring tools (Sentry, Grafana, Prometheus) as one component and alerting services that notify developers through Slack as the last one.

**Videos**

- KodeKloud, Kubernetes Monitoring Made Easy with Prometheus, Alert manager Rules, 59:41 to 1:07:29: [watch](https://www.youtube.com/watch?v=6xmWr7p5TE0&t=3581s). Alertmanager rules written against a running Prometheus, right after the chapter that adds Prometheus rules. Chapter-timed.
- KodeKloud, Kubernetes Monitoring Made Easy with Prometheus, Adding Rules, 56:44 to 59:41: [watch](https://www.youtube.com/watch?v=6xmWr7p5TE0&t=3404s). The rules an alert is built on, added to the Prometheus install from the earlier chapters. Chapter-timed.
- ByteByteGo, 8 Most Important Tips for Designing Fault-Tolerant System, Monitoring and alerting, 3:37 to 4:03: [watch](https://www.youtube.com/watch?v=3Lis4w4_bBc&t=217s). Monitoring and alerting as one of the fault-tolerance habits, in a short chapter. Chapter-timed.
- Hello Interview, Senior System Design Mock Interview: Design an e-commerce platform, Checkout and observability, 43:40 to 51:14: [watch](https://www.youtube.com/watch?v=RuGY_1pap74&t=2620s). Checkout through a payment provider, then what to watch on the running shop, with queue size as the number to watch. Chapter-timed.
- KodeKloud, System Design: Metric Collection Pipeline for Microservices, 0:00 to 2:25: [watch](https://www.youtube.com/watch?v=QMPCogrLTeA&t=0s). The pipeline that collects every service's metrics, which the alert rules then read. Whole video.

**Our plans and chapters**

- [Prometheus, Grafana, and the alert](/home/molef/goal-setting/learning/system-design/foundations/plans/22-prometheus-grafana-and-the-alert.md), system-design/foundations, plan 22. An error-rate rule (over 5% for 1 minute) driven by declined cards, watched turning Pending, then Firing, then clearing at `localhost:9090/alerts`.
- [Watch and feed back: a 5xx alert becomes a card](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/22-watch-and-feed-back.md), system-design/devops-and-deployment, plan 22. An Application Insights alert that counts only 5xx responses, fires under a bad release and opens a card on both boards.
- [Health check and alert](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/74-health-check-and-alert.md), ai-engineering/one-business-end-to-end, plan 74. `/healthz` polled every 60 seconds, the container stopped on purpose, and one alert card saying when the shop went down and when it came back.
- [System Design: Observability and Monitoring](/home/molef/goal-setting/learning/system-design/observability-and-monitoring/MASTER_PLAN.md), system-design/observability-and-monitoring. Objective 4 turns a metric threshold into an actionable alert and tunes it against a demonstrated case of alert fatigue; it holds goals and no plans yet.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/observability-and-monitoring/artifacts/figures/logs-metrics-traces/levelupcoding-logs-vs-metrics-vs-traces.jpg"><img src="/home/molef/goal-setting/learning/system-design/observability-and-monitoring/artifacts/figures/logs-metrics-traces/levelupcoding-logs-vs-metrics-vs-traces.jpg" width="200" alt="Three stacked bands for logs, metrics and traces, each flowing from a source through a named tool to an incident"></a> Nikki Siapno (Level Up Coding) on X, "Logs vs Metrics vs Traces": [the post](https://x.com/NikkiSiapno/status/2098034092164219230), [what it shows](/home/molef/goal-setting/learning/system-design/observability-and-monitoring/artifacts/figures/logs-metrics-traces/README.md#levelupcoding-logs-vs-metrics-vs-tracesjpg). The metrics band runs from a time-series database into New Relic or Datadog, which "detect conditions & fire alerts" at an incident. It gives no alert threshold and says nothing about alert fatigue ([the reading](/home/molef/goal-setting/learning/system-design/observability-and-monitoring/sources/logs-metrics-traces/SOURCES.md#logs-vs-metrics-vs-traces-by-nikki-siapno)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page was read with pdftotext after a page-text search for "alert" across the system design books, AI engineering and Code simplicity; no shelf book has "alerting" in its back-of-book index. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title, the video title and, for the ByteByteGo and Hello Interview lines, the segment notes in `system-design/foundations/video-scout/pulse-2026-10-24.md`. Each plan was read at its title, description and goal. Left out: the networking book's intrusion detection alerts (pages 625 and 691), a security sense; the big archive's pages 146, 185, 189 and 351, which name alerts in passing; KodeKloud's Prometheus install tutorial, which sets Prometheus up under systemd and has no alert chapter; the compiled chapters for both plans 22, whose sections are headings with no text yet. The bare word was sampled across the learning tree: "alert" is a monitoring alert in every prose use outside one idea file, where "GitHub alerts" means the callout boxes, covered by the `link-skip` phrase.
