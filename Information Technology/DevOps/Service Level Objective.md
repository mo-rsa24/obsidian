---
aliases: [SLO, SLI, service level objective, service level indicator, error budget]
standard: vault-note v2
---

# Service Level Objective

Up: [[DevOps]]

Information Technology, DevOps. Its indicator is a signal from [[Observability]], and the same kind of threshold decides a [[Canary Release]]'s stop line.

**A service level objective is a target for a measured signal of a service, such as 99.9% availability over a year, and the room left below the target is the error budget that decides whether releases can keep going out.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches service level objectives writes the rest around it.

## Where to learn this

**Service level objective (SLO)**, a target for a measured signal, with an error budget below it. Also: SLO, SLI, service level indicator, error budget.

**Textbooks**

- AI engineering, chapter 9, Inference Optimization: [pages 790 to 791](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=790). Goodput, the requests per minute that meet the SLO, worked with a time to first token of at most 200 ms and a time per output token of at most 100 ms: 30 of 100 requests meet it, so goodput is 30 requests per minute.
- System design interview, chapter 2, Availability numbers: [page 38](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=38). Availability as a percentage counted in nines, and the service level agreement through which a provider such as Amazon, Google or Microsoft promises 99.9% or more.

**Videos**

- Google Cloud Tech, SLIs, SLOs, SLAs, oh my! (class SRE implements DevOps), Service Level Indicator, 3:25 to 4:25: [watch](https://www.youtube.com/watch?v=tEylFyxbDLE&t=205s). Two worked indicators: is the 99th-percentile latency over the last five minutes under 300 ms, and is the ratio of errors to requests under 1%. Caption-read.
- Google Cloud Tech, SLIs, SLOs, SLAs, oh my! (class SRE implements DevOps), Service Level Objectives, 4:25 to 5:37: [watch](https://www.youtube.com/watch?v=tEylFyxbDLE&t=265s). The indicator added up over a year against a 99.9% target, about nine hours of downtime, and why an SLO is a lower and an upper bound. Caption-read.
- LeadDev, Improving Reliability w/ Error Budgets & SRE - Liz Fong-Jones | #LeadDevNewYork, What is DevOps, 3:00 to 13:45: [watch](https://www.youtube.com/watch?v=9kphSZi69tg&t=180s). The error budget from about 6:36: 100% is the wrong target, users decide what level they notice, and budget left over pays for experiments and faster releases. Caption-read.
- Better Stack, SLAs, SLOs, and SLIs EXPLAINED in 7 Minutes (2025), What Is an SLO? (Service Level Objective), 3:17 to 4:52: [watch](https://www.youtube.com/watch?v=pouVbehfnqQ&t=197s). The objective, between chapters on the agreement and the indicator. Chapter-timed.

**Our plans and chapters**

- [Release requirements](/home/molef/goal-setting/learning/system-design/devops-and-deployment/textbook/01-requirements-gates-and-environments.md#11-release-requirements), system-design/devops-and-deployment, chapter 1, section 1.1. Requirement R7 has an objective's shape without the name: an indicator (the server-error rate) held under 5% over 5 minutes, enforced by the smoke test and the canary's stop condition.
- [Day 17: Monitoring & Failure Handling](/home/molef/goal-setting/learning/system-design/devops-and-deployment/sources/cicd-18-day-plan/topics/module-6-production-readiness.md#day-17-monitoring--failure-handling), the same journey, a staged source topic, not a plan. The 18-day plan's one panel on SLI, SLO and error budget (99.9% uptime, the 0.1% allowed to fail), read as the only idea in that plan that says when to stop shipping.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The textbook pages were found by a case-sensitive pdftotext search of every page of the system design, software engineering and AI engineering books for SLO, SLI, SLA, "error budget" and "service level"; the AI engineering page expands SLO as "software-level objective", and the System design interview page teaches the agreement and the nines rather than the objective itself. Each video's chapter list was read with `cache-video-chapters.py`; the Google Cloud Tech and LeadDev lines were checked against their captions, and the Better Stack line is described from its chapter title. None of ByteByteGo, Hello Interview or KodeKloud has a video on SLOs, so all four come from the open search. No plan in the learning tree teaches SLOs or error budgets: the devops journey's video sweep lists them as uncovered, and the chapter 1 line is the nearest. "SLA" is not an alias, because the agreement is a separate idea with consequences attached; it appears with SLOs in the tms-mobility and tooling-deployment-route files. The acronyms match in capitals only.
