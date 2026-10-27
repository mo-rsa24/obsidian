---
aliases: [blue-green, blue-green deployment, blue-green release, blue/green]
standard: vault-note v2
---

# Blue-Green Deployment

Up: [[DevOps]]

Information Technology, DevOps. It trades the cost of a second environment for a [[Rollback]] that is one switch, where a [[Rolling Update]] and a [[Canary Release]] move users across gradually.

**A blue-green deployment keeps two identical production environments, releases the new version to the idle one, tests it there, then switches the load balancer so all traffic moves at once, leaving the old environment ready to switch back to.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches blue-green deployment writes the rest around it.

## Where to learn this

**Blue-green deployment**, two identical environments and one switch between them. Also: blue-green, blue-green release, blue/green.

**Textbooks**

- System design big archive, How to Deploy Services: [pages 160 to 161](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=160). Blue as staging one version ahead of green as production, traffic switched once testing passes, with a simple rollback and the cost of two production-quality environments.
- Systems analysis and design, chapter 13, Selecting the Conversion Strategy: [pages 500 to 501](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=500). Parallel conversion, the older organisational form: old and new systems run side by side for a period with their outputs compared, the old one kept as the fallback.

**Videos**

- KodeKloud, Blue-Green Deployment on AWS with EC2 and a Load Balancer, 2:36 to 3:47: [watch](https://www.youtube.com/watch?v=X-NfwLUBco4&t=156s). Works the switch on AWS: the load balancer's weights moved 80/20 between the blue and green target groups, then all the way across. Chapter-timed.
- ByteByteGo, Top 5 Most-Used Deployment Strategies, 3:17 to 5:38: [watch](https://www.youtube.com/watch?v=AWVTKBUnoIg&t=197s). Two identical production systems, QA on the idle one, then the load balancer switched for every user at once, at double the infrastructure. Caption-read.
- Arpit Bhayani, An in-depth introduction to Blue Green Deployments, Blue Green Deployment, 3:12 to 9:12: [watch](https://www.youtube.com/watch?v=W6HANd8c9t4&t=192s). What blue-green is, before chapters on implementing it and on the idle setup as a disaster recovery plan. Chapter-timed.
- KodeKloud, 5 Proven CI/CD Strategies for Faster Deployments, Tip 4: Blue-Green Deployments (Octopus Deploy & Kubernetes), 3:26 to 4:08: [watch](https://www.youtube.com/watch?v=piZZ-8I7CCI&t=206s). Blue-green as a pipeline habit, with the tools named in the chapter title. Chapter-timed.

**Our plans and chapters**

- [Canary / Blue-Green / Rolling Deployment Strategies](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/03-operations-and-delivery/plans/07-canary-deployment-strategies.md), projects/tms-mobility, operations and delivery, plan 07. Choose a release strategy for a single-server setup and argue it against the other two; a goal with tasks and no worked steps yet.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/deployment-patterns/aiguides-deployment-patterns.jpg"><img src="/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/deployment-patterns/aiguides-deployment-patterns.jpg" width="200" alt="Five boxed panels: blue-green deployments, canary releases, feature toggles, dark launches and A/B testing, each drawn around a load balancer or a code icon"></a> AI Guides on X, "What are Deployment Patterns?": [the post](https://x.com/free_ai_guides/status/2096614413432410357), [what it shows](/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/deployment-patterns/README.md#aiguides-deployment-patternsjpg). The blue-green panel points a load balancer at a production box with a solid arrow and at a staging box with a dashed one, and a release swaps the two. The post frames rollback as the same swap run in reverse; the toggle, dark-launch and A/B panels carry no rollback at all ([the reading](/home/molef/goal-setting/learning/system-design/devops-and-deployment/sources/deployment-patterns/SOURCES.md#what-are-deployment-patterns)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The big archive pages were found by a page-text search for "blue-green" across the system design, software engineering and AI engineering books, and the Systems analysis and design pages through its back-of-book index ("Parallel conversion", 500 to 501); each was read with pdftotext. Each video's chapter list was read with `cache-video-chapters.py`; the ByteByteGo line was checked against its automatic captions, and the others are described from their chapter titles and the video titles. The plan was read in full. The system-design/devops-and-deployment journey uses blue-green only as a comparison beside its canary and rolling update, so no plan of its own is listed. The phrase was sampled across the learning tree's prose (34 lines): every use is the release style, never a colour.
