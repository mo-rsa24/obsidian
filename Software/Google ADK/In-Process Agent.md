---
aliases: [in-process agent, in process agent, agent in the job's process, MR-05]
link-only-in: [ai-engineering/databricks-production-deployment]
link-scope-words: [in-process agent]
standard: vault-note v2
---

# In-Process Agent

Up: [[Google ADK]] · ⬅️ [[XBL_MODEL_ENDPOINT]]

Software, Google ADK. Needs: [[Agent Server]], [[Entry Point]].

**An in-process agent is the agent loaded into the calling program's own Python process and called as a function, with no HTTP, no server and no port; for the product validation job it is ticket MR-05, and it is not built yet.**

> [!warning]- Unfinished
> - Not built: the repo still calls the agent through the [[Agent Server]].
> - No sandbox yet, and no worked run.

## What it is

**Today.** `pv-validate` sends each product over HTTP to `adk api_server` on `127.0.0.1:8000`, a second program started by hand in another terminal.

**With MR-05.** The job step imports the agent and runs it in its own process. The ADK's `Runner` is the piece that runs an agent this way, with `Runner.run_async` as its entry point (stated from the ADK docs' event loop page; MR-05's own design is on Annemarie Bester's page and may choose differently).

## What it fixes

Annemarie Bester's design page, section 4, names four problems with the [[Agent Server]] in a job, and running the agent in-process removes each.

**Fragile.** No second program and no port have to stay open for hours.

**Wasted runtime.** No start-up wait counts against the job's time limit.

**Hidden errors.** The agent's errors land in the job's own output, not in a server's separate log.

**It multiplies.** Each parallel backfill batch runs its own copy without starting a server.

**It also lets the job choose the model.** The step builds the agent itself, so it can hand it `--model_endpoint` before the first call, where today the server's [[XBL_MODEL_ENDPOINT]] decides.

## Why this matters

It is also why the agent's packages must install on the job's compute: an in-process agent needs the `agent` extra ([[Optional Dependencies]]) in the job's own environment, and on serverless that extra fails with `ERROR_CORE_PACKAGE_VERSION_CHANGE` ([[Serverless Core Package]]). MR-05 waits on the MLOps answer to that.

## Where to learn this

**In-process agent**, the agent called as a function inside the job's process. Also: MR-05.

**Official docs**

- [Runtime event loop](https://adk.dev/runtime/event-loop/), ADK documentation. The `Runner` as "the central coordinator for a single user invocation", with `Runner.run_async` as its primary entry point.

**Our plans and chapters**

- [The validate step and the agent server, what MR-05 changes](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07b-the-validate-step-and-the-agent-server.md#what-mr-05-changes), ai-engineering/databricks-production-deployment, starter pack page 07b. What the job gains, and why `--model_endpoint` starts to work.
- [The real entry point from the repo, why this matters for the tickets](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07-the-real-entry-point-from-the-repo.md#why-this-matters-for-the-tickets), page 07. MR-05 waits on how the agent's packages get onto the compute.

> [!note]- How this was checked
> The ADK event loop page was opened on 2026-11-03; it names `Runner.run_async` but does not say where the Runner runs, so "the Runner runs the agent in your own program" is stated, not checked. The four reasons and the ticket are from Annemarie Bester's design page as recorded on page 07b.
