---
aliases: [serverless environment version, serverless environment versions, environment version, environment versions, environment_version, serverless environment]
standard: vault-note v2
---

# Serverless Environment Version

Up: [[Databricks]]

Software, Databricks. Its preinstalled packages are the [[Serverless Core Package]] list a job's dependencies may not replace, and its Python version must satisfy the `requires-python` of the [[Python Wheel]] the job installs.

**A serverless environment version is the numbered base image a Databricks serverless job or notebook runs on, which fixes the Python version and a list of preinstalled packages; a job sets it as `environment_version` in its environment's `spec`, and version 2 runs Python 3.11.10 while version 3 runs Python 3.12.3.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches environment versions writes the rest around it.

## Where to learn this

**Serverless environment version**, the numbered base image that fixes a serverless job's Python and preinstalled packages. Also: environment version, environment_version, serverless environment.

**Official docs**

- [Environment version 3](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/three), Databricks release notes. Python 3.12.3 and the installed library list, with pyarrow 15.0.2, requests 2.32.2 and google-auth 2.38.0.
- [Environment version 2](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/two), Databricks release notes. Python 3.11.10 and its installed library list, with pyarrow 14.0.1.
- [Serverless environment versions](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/), Databricks release notes. What an environment version is for and the Python version of each one.
- [Configure the serverless environment](https://docs.databricks.com/aws/en/compute/serverless/dependencies), Databricks documentation. How a job task picks its environment version and adds dependencies on top of the preinstalled libraries.

**Our plans and chapters**

- [The real entry point from the repo, errors met](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07-the-real-entry-point-from-the-repo.md#errors-met-in-this-job), ai-engineering/databricks-production-deployment, starter pack page 07. Run 1 on 3 Nov 2026 fails with `ERROR_UNSUPPORTED_PYTHON_VERSION` on version 2, because the wheel needs Python 3.12 or newer, and `environment_version: "3"` fixes it.
- [Her design line beside ours](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07-the-real-entry-point-from-the-repo.md#her-design-line-beside-ours), the same page. Why the design page's `client: "2"` became `environment_version: "3"` in the product validation job.
- [Write a bundle from intent, three surprises](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/06-write-a-bundle-from-intent.md#three-surprises-one-per-mistake-the-ladder-hides), the same journey, page 06. The deprecated `client: "1"` passes validate and deploy and fails only at run time, and `environment_version: "2"` runs in 22 seconds.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-03. No shelf book, lecture map, video lessons row, paper or staged figure teaches environment versions: `gather-concept-sources.py` returned only three scattered page-text hits, and `find-examples.py` and `find-figures.py` returned none. Each docs page answered 200. The Python versions and the pyarrow, requests and google-auth versions were read from the release notes' own text that day. Pages 07 and 06 were read in full. The phrases were sampled across the learning tree (9 uses of "environment version", 8 of "serverless environment"), and every use means this idea, so the card needs no skip phrase.
