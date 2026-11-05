---
aliases: [review_queue, review_queue.csv, review queue table]
link-only-in: [ai-engineering/databricks-production-deployment]
link-scope-words: [review_queue, review_queue.csv]
standard: vault-note v2
---

# review_queue

Up: [[Databricks]] · [[run_metrics]] ➡️

Software, Databricks. Needs: [[Entry Point]]. The product validation [[Declarative Automation Bundle]] writes it in the same step as [[run_metrics]].

**`review_queue` is the product validation Delta table that holds only the products a reviewer must look at, the fail and review decisions of each run, keyed by `sku` and `run_id`, and read by reviewers in the review app.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that runs `pv-publish` writes the rest around it.

## Where to learn this

**review_queue**, the table of products sent to reviewers. Also: `review_queue.csv`.

**Who writes it.** Annemarie Bester's design page, "Mapping Product Data Validation functionality to a DAB", sections 5 and 6: the `publish_results` task, entry point `pv-publish`, in both the daily job and the backfill job. In the backfill job it runs after the [[For Each Task]] that validates every batch.

**What it holds now.** Until the Delta tables of ticket MR-12, `pv-publish` writes it as `review_queue.csv` in its output folder, one row per product whose decision is review or fail, with the columns `run_id, sku, decision, decision_reason, decision_action`. Pass and warning products never reach it. It prints `publish: <n> of <total> products to <path>/review_queue.csv`.

**Our plans and chapters**

- [The validate step and the agent server, where each step runs](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07b-the-validate-step-and-the-agent-server.md#where-each-step-runs), ai-engineering/databricks-production-deployment, starter pack page 07b. The publish row: `pv-publish` runs on the laptop with `uv run`, because it needs the `agent` extra.

> [!note]- How this was checked
> The table's key, writer and readers come from the design page, sections 5 and 6, read on 2026-11-03. The CSV's columns and the review-or-fail filter were read in the product validation repo on the branch `feature/v4_prototype`: `REVIEW_COLUMNS` and `review_rows` in `src/product_validation/publish.py`, and `publish` in `src/product_validation/jobs.py`, uncommitted that day. No official docs page is cited because the table is this project's own.
