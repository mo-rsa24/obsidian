---
aliases: [rollback, roll back, rolled back, rolling back, automatic rollback]
link-only-in: [system-design/, projects/xbiglylabs/, ai-engineering/tooling-deployment-route/, ai-engineering/prototype-product-data-validation-end-to-end/]
link-skip: [transaction, "rollback;", refund, worktree, recorded commit, re-run, "Availability, rollback", rolled back or undone, rolled-back experiments, same verdict]
standard: vault-note v2
---

# Rollback

Up: [[DevOps]]

Information Technology, DevOps. A [[Smoke Test]] or a [[Canary Release]] decides when to roll back, and a [[Blue-Green Deployment]] makes it one switch. Undoing uncommitted writes inside a database is a [[Database Transaction]] rollback, a different idea.

**A rollback puts the last version that worked back in front of users, by redeploying its image or moving traffic back to it, when a release fails its checks.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches rollback writes the rest around it.

## Where to learn this

**Rollback**, the previous version put back when a release fails. Also: roll back, rolled back, rolling back, automatic rollback.

**Textbooks**

- System design big archive, How to Deploy Services: [pages 160 to 161](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=160). Four release styles judged partly by how hard each is to roll back: hard when every service upgrades at once, simple with blue-green and canary.
- AI engineering, chapter 10, Monitoring and Observability: [page 878](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=878). Change failure rate, the share of deployments that end in a fix or a rollback, as one of three numbers that say how observable a system is.
- Systems analysis and design, chapter 13, Selecting the Conversion Strategy: [page 503](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=503). Parallel conversion rated low risk because the old system keeps running, so a new one with bugs can be shut down while the old one carries the work.

**Videos**

- Arpit Bhayani, An in-depth introduction to Blue Green Deployments, Implementation, 9:12 to 15:04: [watch](https://www.youtube.com/watch?v=W6HANd8c9t4&t=552s). Rollback as flipping traffic back to the blue setup, one configuration change that takes effect at once, from about 12:41. Caption-read.
- ByteByteGo, Top 5 Most-Used Deployment Strategies, Blue-green deployment, 3:17 to 5:38: [watch](https://www.youtube.com/watch?v=AWVTKBUnoIg&t=197s). The idle blue environment kept as a safety net, so switching the load balancer back to it is the rollback. Caption-read.
- Arpit Bhayani, An in-depth introduction to Rolling Deployments, Pros of Rolling Deployment, 15:59 to 18:37: [watch](https://www.youtube.com/watch?v=9kjUG_yvVqM&t=959s). Watching the error rate while a few servers at a time take the new version, so a bad release is rolled back before it reaches the rest. Caption-read.

**Our plans and chapters**

- [Release requirements](/home/molef/goal-setting/learning/system-design/devops-and-deployment/textbook/01-requirements-gates-and-environments.md#11-release-requirements), system-design/devops-and-deployment, chapter 1, section 1.1. Requirement R7 states the rollback rule as a number: a release whose server-error rate passes 5% for 5 minutes is withdrawn without waiting for a person.
- [Smoke test and automatic rollback](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/20-smoke-test-and-automatic-rollback.md), the same journey, plan 20. After each deploy a job calls `/health` and `/version` and places one real order, and rolls the release back on its own when any of them fails.
- [Canary on Container Apps: v2 caught at 24.4%](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/21-canary-on-container-apps.md), the same journey, plan 21. Rolling back by weight: the traffic split set back to 100/0 once the new revision's server-error rate reaches 24.4% against the 5% stop line.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/deployment-patterns/aiguides-deployment-patterns.jpg"><img src="/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/deployment-patterns/aiguides-deployment-patterns.jpg" width="200" alt="Five boxed panels: blue-green deployments, canary releases, feature toggles, dark launches and A/B testing, each drawn around a load balancer or a code icon"></a> AI Guides on X, "What are Deployment Patterns?": [the post](https://x.com/free_ai_guides/status/2096614413432410357), [what it shows](/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/deployment-patterns/README.md#aiguides-deployment-patternsjpg). The blue-green panel's two swapping arrows are the rollback: the load balancer points production back at the old box with no redeploy. The other four panels give no rollback story, and turning a toggle off is implied without being said ([the reading](/home/molef/goal-setting/learning/system-design/devops-and-deployment/sources/deployment-patterns/SOURCES.md#what-are-deployment-patterns)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page was read with pdftotext after a page-text search of the system design, software engineering and AI engineering books for "rollback", "roll back" and "rolling back"; the Systems analysis and design page came from its back-of-book index ("Risk(s), with conversion to new system", 503). Each video's chapter list was read with `cache-video-chapters.py`, and the three lines were checked against the videos' automatic captions. Each plan was read at its title and description; chapter 1 section 1.1 was read in full. The chapters for plans 20 and 21 hold headings only, so the plans are cited. Left out: the big archive's How SQL Query Executes (page 203), whose recovery manager rolls back a transaction; [Git rollback as recovery](/home/molef/goal-setting/learning/ai-engineering/agent-harness/plans/10-git-rollback-as-recovery.md) in agent-harness, which resets a worktree to a commit rather than putting back a deployed release. The word was sampled across the learning tree's prose (about 400 lines in 100 files): in the system design journeys, xbiglylabs, the tooling-deployment route and the Uber Eats talk summaries it means a release put back; in Attica, product-data-validation, one-business-end-to-end and data-engineering it is a database transaction or an optimistic update undone, and in agent-harness a git reset. So `link-only-in` keeps bare "rollback" to the first group, and the `link-skip` phrases keep the two-word forms plain on transaction, git and refund lines.
