---
aliases: [rolling update, rolling deployment, rolling upgrade]
standard: vault-note v2
---

# Rolling Update

Up: [[DevOps]]

Information Technology, DevOps. It is the default way a [[Kubernetes]] deployment replaces its pods; a [[Blue-Green Deployment]] and a [[Canary Release]] are the other common ways to release.

**A rolling update replaces the copies of a running service with the new version a few at a time, taking each out of the load balancer before it is upgraded, so the service keeps answering while old and new versions serve side by side.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches rolling updates writes the rest around it.

## Where to learn this

**Rolling update**, copies replaced with the new version a few at a time. Also: rolling deployment, rolling upgrade.

**Textbooks**

- Systems analysis and design, chapter 13, Selecting the Conversion Strategy: [pages 501 to 502](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=501). Phased conversion, the same idea at the scale of an organisation: one set of locations converted, then the next, sometimes with a pause between phases so problems show before too much is affected.

**Videos**

- Arpit Bhayani, An in-depth introduction to Rolling Deployments, How to implement Rolling Deployment, 5:42 to 11:32: [watch](https://www.youtube.com/watch?v=9kjUG_yvVqM&t=342s). Works the steps on eight servers: take one out of the load balancer, wait for its requests to finish, upgrade it, put it back, then the next. Caption-read.
- ByteByteGo, Top 5 Most-Used Deployment Strategies, 1:14 to 3:17: [watch](https://www.youtube.com/watch?v=AWVTKBUnoIg&t=74s). Ten servers upgraded one at a time, with no downtime, and why it cannot target particular users. Caption-read.
- Arpit Bhayani, An in-depth introduction to Rolling Deployments, What is Rolling Deployment, 2:36 to 5:42: [watch](https://www.youtube.com/watch?v=9kjUG_yvVqM&t=156s). Nine servers moving from version one to version two, and why both versions serving at once demands backward and forward compatibility. Caption-read.
- KodeKloud, Kubernetes Crash Course, 46:20 to 50:11: [watch](https://www.youtube.com/watch?v=XuSQU5Grv1g&t=2780s). A Kubernetes deployment owning ReplicaSets so it can roll out a new version. Chapter-timed.

**Our plans and chapters**

- [Staging on kind: a rolling update watched pod by pod](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/19-staging-on-kind-rolling-update.md), system-design/devops-and-deployment, plan 19. kind made the staging environment, v1 then v2 deployed from the pipeline, and the rolling update replacing pods one at a time while the service keeps answering.
- [Kubernetes from zero: pod, deployment, service](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/18-kubernetes-from-zero.md), the same journey, plan 18. The deployment and service objects a rolling update replaces and routes through, built first because plan 19 needs them.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The Systems analysis and design pages came from its back-of-book index ("Phased conversion", 501 to 502) and were read with pdftotext; a page-text search of the system design, software engineering and AI engineering books for "rolling update", "rolling deployment" and "rolling upgrade" found no other page (the big archive's How to Deploy Services, pages 160 to 161, covers blue-green and canary only). Each video's chapter list was read with `cache-video-chapters.py`; the ByteByteGo and Arpit Bhayani lines were checked against their automatic captions, and the KodeKloud line is described from its chapter title. Each plan was read at its title and description; the chapter for plan 19 holds headings only. Left out: the tooling-deployment route's master plan, whose goal 4 demonstrates a rolling update but holds no plans yet. "Rolling release" is not an alias, because it also names a Linux distribution's update model. The phrases were sampled across the learning tree's prose (about 60 lines): all mean this idea.
