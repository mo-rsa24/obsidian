---
aliases: [run_metrics, run_metrics.csv, run metrics table]
link-only-in: [ai-engineering/databricks-production-deployment]
link-scope-words: [run_metrics, run_metrics.csv]
standard: vault-note v2
---

# run_metrics

Up: [[Databricks]] · ⬅️ [[review_queue]]

Software, Databricks. Needs: [[Entry Point]]. The product validation [[Declarative Automation Bundle]] writes it in the same step as [[review_queue]], and the quality check job writes it too.

**`run_metrics` is the product validation Delta table with one row per run, keyed by `run_id`, that records the run's decision counts, runtime, model calls, tokens and cost.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that runs `pv-publish` writes the rest around it.

## Where to learn this

**run_metrics**, one row per run with its counts and costs. Also: `run_metrics.csv`.

**Who writes it.** Annemarie Bester's design page, "Mapping Product Data Validation functionality to a DAB", sections 5 and 6: the `publish_results` task (entry point `pv-publish`) of the daily and backfill jobs, and the quality check job's `check_against_limits` task (entry point `pv-benchmark-gate`).

**What it holds now.** Until the Delta tables of ticket MR-12, `pv-publish` writes it as `run_metrics.csv`, one row with the columns `run_id, run_type, products, pass, warning, review, fail`: the number of products and how many got each decision. Runtime, tokens and cost are not recorded until the agent runs in the job's own process, the [[In-Process Agent]] of ticket MR-05, and the step prints that.

**Our plans and chapters**

- [The validate step and the agent server, where each step runs](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07b-the-validate-step-and-the-agent-server.md#where-each-step-runs), ai-engineering/databricks-production-deployment, starter pack page 07b. The publish row: `pv-publish` runs on the laptop with `uv run`, because it needs the `agent` extra.
- [The same page, what MR-05 changes](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07b-the-validate-step-and-the-agent-server.md#what-mr-05-changes): the agent loaded into the job's own process, which is the change `run_metrics` waits on for runtime, tokens and cost.

> [!note]- How this was checked
> The table's key, writers and full column list come from the design page, sections 5 and 6, read on 2026-11-03. The CSV's columns were read in the product validation repo on the branch `feature/v4_prototype`: `METRIC_COLUMNS` and `run_metrics` in `src/product_validation/publish.py`, and the MR-05 line printed by `publish` in `src/product_validation/jobs.py`, uncommitted that day. No official docs page is cited because the table is this project's own.
