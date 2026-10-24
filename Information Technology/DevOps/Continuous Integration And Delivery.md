---
aliases: [CI/CD, CI, continuous integration, continuous delivery, continuous deployment, CI pipeline, CI/CD pipeline]
standard: vault-note v2
---

# Continuous Integration And Delivery

Up: [[DevOps]]

Information Technology, DevOps. A pipeline usually builds a [[Docker]] image, and [[Infrastructure As Code]] declares where it is deployed.

**Continuous integration runs automated builds and tests on every change pushed to a shared repository, and continuous delivery carries each passing build toward production, with continuous deployment releasing it there without a human step.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches CI/CD writes the rest around it.

## Where to learn this

**CI/CD**, every change built, tested and shipped by a pipeline. Also: CI, continuous integration, continuous delivery, continuous deployment, CI pipeline.

**Textbooks**

- System design big archive, How Do Companies Ship Code to Production?: [pages 184 to 185](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=184). Works one feature through 11 steps: a Jira story, a push to GitHub, Jenkins building and testing it, the build stored and deployed with Docker to dev, then QA, UAT and production, watched by the SRE team.
- System design big archive, CI/CD Simplified Visual Guide: [pages 308 to 309](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=308). Continuous integration as frequent merges with automatic checks, and continuous deployment as moving those changes to production automatically.
- System design big archive, CI/CD Pipeline Explained: [page 290](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=290). The pipeline as one workflow that builds, tests and deploys, with the tools used at each stage.
- System design interview, chapter 1, Logging, metrics, automation: [page 26](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=26). Continuous integration as the automation a growing site needs: each check-in verified automatically so problems surface early.
- System design big archive, How to Deploy Services: [pages 160 to 161](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=160). The release step's options: all services at once, blue-green, canary and A/B tests, each with its rollback cost.

**Videos**

- KodeKloud, CI/CD Explained: Enhance Your GitHub Workflow Today!, Workflow in Continuous Integration, 3:22 to 6:19: [watch](https://www.youtube.com/watch?v=IkglLTs5K6I&t=202s). The continuous integration workflow, before the continuous delivery workflow that follows it. Chapter-timed.
- KodeKloud, DevOps: CI/CD Introduction (Continuous Integration, Continuous Delivery, Continuous Deployment), CI: Continuous Integration, 0:42 to 2:12: [watch](https://www.youtube.com/watch?v=AlrImm1T8Wg&t=42s). Continuous integration, before one chapter on continuous delivery and deployment. Chapter-timed.
- ByteByteGo, CI/CD In 5 Minutes: Is It Worth The Hassle, CI, 0:51 to 1:39: [watch](https://www.youtube.com/watch?v=42UP1fxi2SY&t=51s). Continuous integration, before chapters on the tools, continuous deployment and feature flags. Chapter-timed.

**Our plans and chapters**

- [Pipeline as code on both platforms](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/08-pipeline-as-code-on-both-platforms.md), system-design/devops-and-deployment, plan 08. `.github/workflows/ci.yml` and `azure-pipelines.yml` written from a blank editor, run on every push, with each run timed.
- [Tests as the gate, cheapest checks first](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/09-tests-as-the-gate.md), the same journey, plan 09. Lint before tests, the pipeline made a required check, and a pull request with a failing test that cannot merge.
- [GitHub Actions: the smoke test](/home/molef/goal-setting/learning/system-design/foundations/plans/24-github-actions-smoke-test.md), system-design/foundations, plan 24. A workflow that brings the whole stack up with `docker compose`, waits on the healthchecks and posts one order, run green and then broken on purpose.
- [GitHub Actions on every push: test, build the image, push it, with the secrets kept out of the log](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/72-github-actions-on-every-push.md), ai-engineering/one-business-end-to-end, plan 72. Tests, an image build and a push tagged with the commit, on a machine you do not own.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext; the big archive pages came from its chapter table in Textbooks.md and the System design interview page from a pdftotext search of every page for "continuous integration". Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: [the registry by commit SHA](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/12-registry-by-commit-sha.md) and the canary and rollback plans that follow it in devops-and-deployment, which build on these pipelines; [CI/CD Pipelines for Django](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/03-operations-and-delivery/plans/02-cicd-pipelines.md) in tms-mobility, a scaffold leaf with no steps yet. The acronym "CI" was sampled in the learning tree's prose: 376 uses, and 25 random lines all mean continuous integration (a CI system, `ci.yml`, "CI runs a 30-product slice"); it matches in capitals only.
