---
aliases: [smoke test, smoke testing]
standard: vault-note v2
---

# Smoke Test

Up: [[DevOps]]

Information Technology, DevOps. A [[Continuous Integration And Delivery]] pipeline runs it right after a deploy, and a failed one triggers a [[Rollback]].

**A smoke test is a handful of quick calls that check a freshly built or deployed system starts and answers its most important request, run before slower tests or right after a release.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches smoke tests writes the rest around it.

## Where to learn this

**Smoke test**, the quick check that a new release starts and answers. Also: smoke testing.

**Videos**

- Google Cloud Tech, What are smoke tests? | Serverless Reliability, Verifying returned data with smoke tests, 5:24 to 6:24: [watch](https://www.youtube.com/watch?v=_u03uI-zCCk&t=324s). A smoke test that checks the data a call returns as well as its status. Chapter-timed.
- Google Cloud Tech, What are smoke tests? | Serverless Reliability, What are smoke tests?, 1:46 to 2:37: [watch](https://www.youtube.com/watch?v=_u03uI-zCCk&t=106s). What a smoke test is, before chapters on monitoring, a deep health check and where each kind of smoke test goes. Chapter-timed.
- ByteByteGo, Top 9 Most Popular Types of API Testing, 0:28 to 1:12: [watch](https://www.youtube.com/watch?v=qquIJ1Ivusg&t=28s). Smoke testing as the first and cheapest kind of API test, then functional testing. Chapter-timed.
- KodeKloud, Install Kubernetes from Scratch [20] - End to End Tests: Run Smoke Test, 0:00 to 3:02: [watch](https://www.youtube.com/watch?v=eJQ-Yla85rM&t=0s). A smoke test run against a freshly installed Kubernetes cluster. Whole video, described from its title.

**Our plans and chapters**

- [The failure table](/home/molef/goal-setting/learning/system-design/devops-and-deployment/textbook/03-failure-table-budget-and-branching.md#31-the-failure-table), system-design/devops-and-deployment, chapter 3, section 3.1. Works out what the smoke test must call: `/health` catches a wrong `DATABASE_URL` because it queries the database, and passes a renamed column that fails 100 of 100 orders, so the smoke test places one real order too.
- [Smoke test and automatic rollback](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/20-smoke-test-and-automatic-rollback.md), the same journey, plan 20. After each production deploy a job calls `/health` and `/version` and places one real order, and rolls back on its own when any of them fails.
- [GitHub Actions: the smoke test](/home/molef/goal-setting/learning/system-design/foundations/plans/24-github-actions-smoke-test.md), system-design/foundations, plan 24. A workflow brings the whole stack up with `docker compose`, waits on the healthchecks and posts one order, run green once and red once on purpose.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No shelf book teaches smoke tests: a pdftotext search of every page of the system design, software engineering and AI engineering books for "smoke test" found none, and the two machine learning pages the search tool returned use "smoke" in another sense. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. ByteByteGo, Hello Interview and KodeKloud were searched first; Google Cloud Tech comes from the open search. Chapter 3 section 3.1 was read in full; each plan was read at its title and description. The chapters for devops plan 20 and foundations plan 24 hold headings only, so the plans are cited. The phrase was sampled across the learning tree's prose (about 140 lines): every use means a quick check that something starts and answers, from a post-deploy job to a first check on a SQL file, so it needs no skip phrase.
