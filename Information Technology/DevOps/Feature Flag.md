---
aliases: [feature flag, feature toggle]
standard: vault-note v2
---

# Feature Flag

Up: [[DevOps]]

Information Technology, DevOps. It works inside one deployed version, where a [[Canary Release]] or a [[Blue-Green Deployment]] chooses between two versions.

**A feature flag is a switch read at runtime that turns a piece of already deployed code on or off, for everyone or for chosen users, so shipping the code and releasing the feature become two separate steps.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches feature flags writes the rest around it.

## Where to learn this

**Feature flag**, a runtime switch that separates deploying code from releasing it. Also: feature toggle.

**Videos**

- IBM Technology, What are Feature Flags?, Feature Flag Code, 2:27 to 6:40: [watch](https://www.youtube.com/watch?v=AJa2B-twtG4&t=147s). A feature flag as it appears in code, after the chapter on what flags are for. Chapter-timed.
- ByteByteGo, Top 5 Most-Used Deployment Strategies, Feature toggles and conclusion, 7:49 to 10:00: [watch](https://www.youtube.com/watch?v=AWVTKBUnoIg&t=469s). A switch in the code that turns a feature on for some users, used with any release style (on for the canary's users only), and the toggle debt left by flags nobody removes. Caption-read.
- IBM Technology, What are Feature Flags?, Feature Flags, 0:20 to 2:27: [watch](https://www.youtube.com/watch?v=AJa2B-twtG4&t=20s). What a feature flag is and why teams use one. Chapter-timed.
- ByteByteGo, CI/CD In 5 Minutes | Is It Worth The Hassle: Crash Course System Design #2, Feature Flags, 3:30 to 4:15: [watch](https://www.youtube.com/watch?v=42UP1fxi2SY&t=210s). Feature flags as the step after continuous deployment. Chapter-timed.

**Our plans and chapters**

- [Learning goals for what the tree does not teach](/home/molef/goal-setting/learning/system-design/caching/sources/redis-use-cases/redis-use-cases-prerequisites.md#learning-goals-for-what-the-tree-does-not-teach), system-design/caching, the Redis use cases source. A goal, not yet a plan: a percentage rollout that hashes each user into a bucket from 0 to 99, so at 10% about 1,000 of 10,000 users see the feature and raising it to 25% keeps those 1,000 and adds about 1,500, with the flag read from Redis by a FastAPI endpoint.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/deployment-patterns/aiguides-deployment-patterns.jpg"><img src="/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/deployment-patterns/aiguides-deployment-patterns.jpg" width="200" alt="Five boxed panels: blue-green deployments, canary releases, feature toggles, dark launches and A/B testing, each drawn around a load balancer or a code icon"></a> AI Guides on X, "What are Deployment Patterns?": [the post](https://x.com/free_ai_guides/status/2096614413432410357), [what it shows](/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/deployment-patterns/README.md#aiguides-deployment-patternsjpg). The feature-toggles panel splits one piece of code through a red switch and a blue switch to two user groups, which separates deploying code from turning it on. It never says where a toggle lives (a config file, a database flag, a vendor service such as LaunchDarkly) or how a per-user decision is made ([the reading](/home/molef/goal-setting/learning/system-design/devops-and-deployment/sources/deployment-patterns/SOURCES.md#what-are-deployment-patterns)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No shelf book teaches feature flags: a pdftotext search of every page of the system design, software engineering and AI engineering books for "feature flag", "feature toggle" and "feature switch" found none. Each video's chapter list was read with `cache-video-chapters.py`; the ByteByteGo deployment strategies line was checked against its automatic captions, and the others are described from their chapter titles and the video titles. ByteByteGo, Hello Interview and KodeKloud were searched first; IBM Technology comes from the open search. No plan teaches feature flags: the devops journey's video sweep left ByteByteGo's toggle chapter unplaced for that reason, and the Redis source's prerequisite map proposes a devops plan for them that is still waiting for a yes. The phrases were sampled across the learning tree's prose (27 lines): all mean this idea.
