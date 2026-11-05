---
aliases: [XBL_MODEL_ENDPOINT variable, DATABRICKS_MODEL, DATABRICKS_MODEL variable]
standard: vault-note v2
---

# XBL_MODEL_ENDPOINT

Up: [[Google ADK]] · ⬅️ [[Agent Server]] · [[In-Process Agent]] ➡️

Software, Google ADK. Needs: [[Agent Server]].

**`XBL_MODEL_ENDPOINT` is the environment variable that overrides the Databricks serving endpoint the product validation agent calls; the repo's `config.py` reads it once, when the module is imported inside the agent server, and unset it leaves the value in `local.toml`, `databricks-gpt-5-6-luna`.**

> [!warning]- Unfinished
> - No sandbox yet: a run with the variable set and one without, compared in the server's log, is not built from an empty folder.

## What it is

**Where the value comes from.** `src/product_validation/config.py` is the only module in the repo that reads environment variables. It loads `local.toml` beside it and lets an `XBL_` variable override each setting:

```python
def value(name):
    """One setting: `XBL_<NAME>` when it is set, else the local run's value."""
    return os.environ.get(f"XBL_{name.upper()}") or LOCAL[name]


AGENT_URL = value("agent_url")
MODEL_ENDPOINT = value("model_endpoint")
DATA_ROOT = Path(value("data_root") or Path(__file__).parent / "data")
```

The local value sits in `src/product_validation/local.toml`:

```toml
model_endpoint = "databricks-gpt-5-6-luna"  # the Databricks serving endpoint the agent calls
```

The same file holds `agent_url` (`http://127.0.0.1:8000`, overridden by `XBL_AGENT_URL`) and `data_root` (empty, meaning the package's own `data/` folder, overridden by `XBL_DATA_ROOT`).

**Where the agent takes it.** Line 9 of `src/agents/product_validation_agent/agent.py`, after `from product_validation import config` on line 6:

```python
MODEL_ENDPOINT = config.MODEL_ENDPOINT
```

Line 15 builds the model as `LiteLlm(model=f"databricks/{MODEL_ENDPOINT}")`, so the endpoint name becomes LiteLLM's model name with the `databricks/` provider in front.

**How it is set.** On the command that starts the server, beside the login profile:

```bash
DATABRICKS_CONFIG_PROFILE=PLAYGROUND XBL_MODEL_ENDPOINT=databricks-llama-4-maverick uv run adk api_server src/agents
```

**How to see it took.** Every product's block in the server's log prints `LiteLLM completion() model= databricks-llama-4-maverick; provider = databricks`. A different model name in that line means the server was started with a different value, or none.

## Why a job parameter cannot change it

**It is read once.** `config.py` reads the variable when the module is imported, and the [[Agent Server]] imports it when it loads the agent on its first session. After that the value is fixed for every product the server judges, until the server restarts.

**The job step talks to a server that already loaded it.** `pv-validate` takes `--model_endpoint`, but by the time it runs, the server has already read its own environment. So the step only prints `validate: the agent server must be started with XBL_MODEL_ENDPOINT=<endpoint>` and cannot pass the value on.

**What changes this.** The [[In-Process Agent]] (ticket MR-05) builds the agent inside the step's own process, so the step can hand it `--model_endpoint` before the first call. Until then the server's start command is the only place the model is chosen.

## Why this matters

The value in `local.toml`, `databricks-gpt-5-6-luna`, is a different model from the one the bundle's `model_endpoint` variable names (`databricks-llama-4-maverick`). Starting the server without the variable gives a run that completes and reports decisions from a model the job never asked for.

The variable is part of ticket MR-02, which keeps every value that differs between environments out of the code: the local run's values live in `local.toml`, each overridden by its `XBL_` variable, and `config.py` is the one place they are read.

## Where to learn this

**XBL_MODEL_ENDPOINT**, the environment variable that picks the product validation agent's serving endpoint at server start. Also: `DATABRICKS_MODEL`.

**Official docs**

- [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/), Databricks documentation. What a serving endpoint is: a model run for live requests or batches behind a REST API, which is what the variable names.

**Our plans and chapters**

- [The validate step and the agent server, step 2](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07b-the-validate-step-and-the-agent-server.md#step-2-start-the-agent-server-in-terminal-1), ai-engineering/databricks-production-deployment, starter pack page 07b. Why both variables go on the server's command, and the lines of `config.py` and `agent.py` that read the endpoint.
- [The same page, what MR-05 changes](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07b-the-validate-step-and-the-agent-server.md#what-mr-05-changes), why `--model_endpoint` does not steer the model until the agent runs in-process.

> [!note]- How this was checked
> `config.py`, `local.toml`, `agent.py` lines 6, 9 and 15 and the `pv-validate` print line in `jobs.py` were read in the product validation repo on the branch `feature/v4_prototype` on 2026-11-03. A local check that day with `XBL_MODEL_ENDPOINT=databricks-llama-4-maverick` on the server's command showed `model= databricks-llama-4-maverick` in the server log for both calls. The Model Serving page was opened the same day.
