---
aliases: [serverless core package, serverless core packages, core package, core packages, ERROR_CORE_PACKAGE_VERSION_CHANGE]
link-only-in: [ai-engineering/databricks-production-deployment]
link-scope-words: [core package, core packages]
standard: vault-note v2
---

# Serverless Core Package

Up: [[Databricks]]

Software, Databricks. The list comes from the [[Serverless Environment Version]] the job runs on, and moving the packages that would replace one into [[Optional Dependencies]] is how the product validation wheel got past it.

**A core package on Databricks serverless is a package the environment version ships preinstalled and a job may not replace, such as pyarrow, requests or google-auth; a job whose dependencies ask for a different version of one fails its install with `ERROR_CORE_PACKAGE_VERSION_CHANGE`.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that meets the error writes the rest around it.

## Where to learn this

**Serverless core package**, a preinstalled package a serverless job may not replace. Also: core package, `ERROR_CORE_PACKAGE_VERSION_CHANGE`.

**Official docs**

- [Environment version 3](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/three), Databricks release notes. The installed library list, holding the three versions run 2 tried to replace: pyarrow 15.0.2, requests 2.32.2 and google-auth 2.38.0.
- [Configure the serverless environment](https://docs.databricks.com/aws/en/compute/serverless/dependencies), Databricks documentation. Says the base environment sets the preinstalled libraries a task inherits, and that packages which break or change the core environment must be removed and the environment reset.

**Our plans and chapters**

- [The real entry point from the repo, errors met](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07-the-real-entry-point-from-the-repo.md#errors-met-in-this-job), ai-engineering/databricks-production-deployment, starter pack page 07. Run 2 on 3 Nov 2026 installs for about 7 minutes and fails because the wheel's ten dependencies ask for pyarrow 26.0.0, requests 2.34.2 and google-auth 2.62.1, and cutting the base install to `databricks-sdk` lets run 3 pass; it also shows why no environment version from 3 to 6 fixes it.
- [Read a failed run without the web page](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07-the-real-entry-point-from-the-repo.md#step-4-read-a-failed-run-without-the-web-page), the same page, step 4. Where the error code appears: `databricks jobs get-run` prints each task's `state.state_message`, which holds it.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-03. No official Databricks page found that day names `ERROR_CORE_PACKAGE_VERSION_CHANGE`: a web search for the code returned community threads only, so the error and what triggers it are cited from run 2 on page 07, and the docs lines cite the library list and the dependencies page. No shelf book, lecture map, paper or staged figure teaches the idea: `gather-concept-sources.py` returned scattered page-text hits in other senses (a diffusion paper, the NLTK book's contrib package). "Core packages" in the prototype journey's runbook means that project's own base dependencies, so the bare phrase links only inside the databricks-production-deployment journey.
