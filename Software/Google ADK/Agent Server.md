---
aliases: [agent server, agent servers, ADK server, adk api_server, api_server, ADK API server]
link-only-in: [ai-engineering/databricks-production-deployment]
link-scope-words: [agent server]
standard: vault-note v2
---

# Agent Server

Up: [[Google ADK]] · [[XBL_MODEL_ENDPOINT]] ➡️

Software, Google ADK. Needs: [[Entry Point]]. The agent's packages come from the `agent` extra ([[Optional Dependencies]]), which cannot install on serverless ([[Serverless Core Package]]), so the server runs on the laptop.

**The agent server is the ADK program `adk api_server`: it loads every agent in a folder and answers HTTP on `http://127.0.0.1:8000`, with `GET /list-apps`, a session per conversation, and `POST /run` for one turn.**

> [!warning]- Unfinished
> - No sandbox yet: the nine parts of "Try it yourself" are not built from an empty folder.
> - No drawn pictures for the form or the mechanism.

## What it is

**The program.** `uv run adk api_server src/agents`, run from the product validation repo's root, loads `src/agents/product_validation_agent` and prints `Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)`. It keeps running until Ctrl+C.

**What it answers.** `GET /list-apps` returns the agents it found. `POST /apps/<app>/users/<user>/sessions/<id>` opens a session. `POST /run` sends one message into that session and returns the agent's events. The repo's client opens a fresh session per product, so one product's answer never reaches the next.

**When it loads the agent.** On the first session, the log prints `Found root_agent in product_validation_agent.agent`. That is when the agent module runs, and when its `config.py` reads [[XBL_MODEL_ENDPOINT]].

## How the repo starts it and checks it

**The check: `server_is_up`.** In `src/product_validation/__main__.py`, it sends `GET /list-apps` to `ADK_BASE_URL` (`http://127.0.0.1:8000`, in `agent_client.py`) with a two-second timeout and returns whether the answer is OK. In the server's log the check shows as `GET /list-apps 200 OK`.

**The start: `start_server`.** The local one-command run, `python -m product_validation`, launches `adk api_server src/agents` as a child process, writes its output to a log file, polls `server_is_up` until it is true, and stops the process at the end. When the server does not come up in time, it prints the last 15 lines of that log.

**The job steps only check.** `pv-validate` calls `server_is_up` and, when nothing answers, prints `validate: no agent server is answering; start one with ...` and exits 1. It never calls `start_server`.

## Why a job does not start one

Annemarie Bester's design page, section 4, "Why the local agent server doesn't suit a Databricks job", gives four reasons.

**Fragile.** A second program and a port stay open for hours.

**Wasted runtime.** Waiting for start-up counts against the job's time limit.

**Hidden errors.** The agent's errors go to the server's log and not to the job's output.

**It multiplies.** Each parallel backfill batch would start its own server.

Her fix is the [[In-Process Agent]], ticket MR-05.

## Why this matters

The server is a second program the validation depends on, and it decides the model for every product it judges. A run that sends products to a server started with the wrong environment gets answers from the wrong model, with nothing in `pv-validate`'s output to show it except the line naming which model the server must have.

## Where to learn this

**Agent server**, the ADK program `adk api_server` that serves agents over HTTP. Also: ADK server, ADK API server, `api_server`.

**Official docs**

- [Use the API server](https://adk.dev/runtime/api-server/), ADK documentation. Starting `adk api_server`, its default address `http://localhost:8000`, and the endpoints `GET /list-apps`, the session routes under `/apps/{app_name}/users/{user_id}/sessions/{session_id}`, `POST /run` and `POST /run_sse`.

**Our plans and chapters**

- [The validate step and the agent server, step 2](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07b-the-validate-step-and-the-agent-server.md#step-2-start-the-agent-server-in-terminal-1), ai-engineering/databricks-production-deployment, starter pack page 07b. Starts the server with the PLAYGROUND profile and `XBL_MODEL_ENDPOINT=databricks-llama-4-maverick`.
- [The same page, step 4](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07b-the-validate-step-and-the-agent-server.md#step-4-read-the-servers-log-in-terminal-1), the server's log read block by block for 3 products, 13:32:13 to 13:32:42: session, LiteLLM call, profile, `POST /run 200 OK`.
- [The same page, why a job never starts the agent server](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07b-the-validate-step-and-the-agent-server.md#why-a-job-never-starts-the-agent-server), the four reasons from the design page.

> [!note]- How this was checked
> The ADK docs page was opened on 2026-11-03 (the old `google.github.io/adk-docs` address redirects to `adk.dev`). `server_is_up`, `start_server` and `ADK_BASE_URL` were read in the product validation repo on the branch `feature/v4_prototype`. The log lines come from the user's screenshot of the `local-4` run on 3 Nov 2026.
