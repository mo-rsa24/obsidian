---
aliases: [canary, canary release, canary deployment, canary deploy, traffic split, traffic splitting]
link-only-in: [system-design/]
standard: vault-note v2
---

# Canary Release

Up: [[DevOps]]

Information Technology, DevOps. A failed canary ends in a [[Rollback]], usually watched through [[Observability]]; a [[Feature Flag]] can limit a new feature to the canary's users.

**A canary release runs the new version beside the old one and sends it a small share of real traffic, watches a measured signal such as its server-error rate against a stop line written beforehand, and only then moves the rest of the traffic across or rolls back.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches canary releases writes the rest around it.

## Where to learn this

**Canary release**, a small share of traffic on the new version first. Also: canary, canary deployment, traffic split.

**Textbooks**

- System design big archive, How to Deploy Services: [pages 160 to 161](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=160). Services upgraded for a growing subset of users, cheaper than blue-green and easy to roll back, at the price of testing in production and watching the canary throughout.
- Systems analysis and design, chapter 13, Selecting the Conversion Strategy: [pages 501 to 503](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=501). Pilot conversion, the older organisational form: one location converted first as a test, the rest only if it succeeds, rated lower risk because a bug stays in the pilot.

**Videos**

- Hussein Nasser, Canary Deployment (Explained by Example), 0:00 to 7:08: [watch](https://www.youtube.com/watch?v=3IJ5ko8jSIA&t=0s). A worked example from 2:12 to 4:32: YouTube's reverse proxy sends 3% of requests to one server running a thumbnail experiment and the other 97% to the rest. Whole video, caption-read.
- ByteByteGo, Top 5 Most-Used Deployment Strategies, 5:38 to 7:49: [watch](https://www.youtube.com/watch?v=AWVTKBUnoIg&t=338s). A small share of traffic on the new version first. Chapter-timed.
- KodeKloud, Canary Deployment in Kubernetes Explained, 0:00 to 2:55: [watch](https://www.youtube.com/watch?v=HTe2_uIWSuY&t=0s). A canary on Kubernetes. Whole video, described from its title.
- Arpit Bhayani, An in-depth introduction to Canary Deployments, Implementation of Canary Deployment, 8:04 to 16:20: [watch](https://www.youtube.com/watch?v=nnseeKxovaM&t=484s). Building a canary, after a chapter on what it is and before chapters on its uses, its costs and monitoring both versions in parallel. Chapter-timed.

**Our plans and chapters**

- [The failure table](/home/molef/goal-setting/learning/system-design/devops-and-deployment/textbook/03-failure-table-budget-and-branching.md#31-the-failure-table), system-design/devops-and-deployment, chapter 3, section 3.1. The canary's stop condition catches v2's bug at 244 of 1,000 orders, 24.4% against 5%, and misses a rename that breaks the old revision, because a canary only watches the new one.
- [Canary on Container Apps: v2 caught at 24.4%](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/21-canary-on-container-apps.md), the same journey, plan 21. v2 released as a second revision beside v1 on Azure Container Apps, the order mix replayed, the server-error rate read against the 5% stop line, and the weights set back to 100/0.
- [Checking the design against the sources](/home/molef/goal-setting/learning/system-design/devops-and-deployment/textbook/04-draw-and-check-the-design.md#42-checking-the-design-against-the-sources), the same journey, chapter 4, section 4.2. One canary step instead of the source's 20, 50 and 100% ramp, because the bug trips at the first step, and the source's 5%-for-5-minutes trigger adopted.
- [The rename that breaks a canary, and the two-step migration](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/23-the-rename-that-breaks-a-canary.md), the same journey, plan 23. A column rename that breaks whichever version does not match the schema, shipped instead as expand then contract so both versions serve throughout.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/deployment-patterns/aiguides-deployment-patterns.jpg"><img src="/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/deployment-patterns/aiguides-deployment-patterns.jpg" width="200" alt="Five boxed panels: blue-green deployments, canary releases, feature toggles, dark launches and A/B testing, each drawn around a load balancer or a code icon"></a> AI Guides on X, "What are Deployment Patterns?": [the post](https://x.com/free_ai_guides/status/2096614413432410357), [what it shows](/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/deployment-patterns/README.md#aiguides-deployment-patternsjpg). The canary panel fans a load balancer out to two v1 boxes and one "v2 – Canary" box, so only the requests routed to v2 meet a fault in it. The panel gives no traffic share, and the post says only "a small slice" ([the reading](/home/molef/goal-setting/learning/system-design/devops-and-deployment/sources/deployment-patterns/SOURCES.md#what-are-deployment-patterns)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The big archive pages were found by a page-text search for "canary" across the system design, software engineering and AI engineering books, and the Systems analysis and design pages through its back-of-book index ("Pilot conversion", 501, 503 and 504); each was read with pdftotext. Each video's chapter list was read with `cache-video-chapters.py`; the Hussein Nasser line was checked against its automatic captions, and the others are described from their chapter titles and the video titles. Chapters 3 and 4 were read at the sections cited; each plan was read at its title and description. The chapters for plans 21 and 23 hold headings only. Left out: KodeKloud's blue-green video, whose 80/20 shift sits on [[Blue-Green Deployment]]; the tms-mobility strategy plan, also on that card. Bare "canary" was sampled across the learning tree's prose: 289 lines, and 30 random lines in the system design journeys all mean this release style; the only other use is the diffusion journey's `--check-canary` sanity check, so `link-only-in` keeps the single word to paths under system-design. "Traffic split" was sampled too (about 50 lines): every use is weights between two versions, including Databricks serving two model versions 90/10, so it links everywhere.
