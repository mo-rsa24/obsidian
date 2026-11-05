---
aliases: [for each task, for-each task, For each task, for_each_task, For each loop task]
link-only-in: [ai-engineering/databricks-production-deployment]
link-scope-words: [for_each_task, for-each task, For each task]
standard: vault-note v2
---

# For Each Task

Up: [[Databricks]]

Software, Databricks. Needs: [[Declarative Automation Bundle]], [[Entry Point]]. It is how the product validation backfill job runs `pv-validate` over many batches without one job per batch, and why each batch needs its own copy of the agent rather than a shared [[Agent Server]].

**A For each task is a Databricks Jobs task type, written `for_each_task` in a job's YAML, that runs one nested task once per value in an input list, with `concurrency` setting how many of those runs go at the same time.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that builds the backfill job writes the rest around it.

## Where to learn this

**For each task**, a job task that loops one nested task over a list of inputs. Also: `for_each_task`, for-each task.

**The form.** Three keys sit under `for_each_task`. `inputs` is required and holds the list, as a JSON array or a reference to an upstream task's value. `task` is required and holds the nested task, with its own `task_key`. `concurrency` is optional, the most iterations that run at once, and defaults to 1. Inside the nested task, `{{input}}` is the current element, and `{{input.<key>}}` reads one field when each element is an object.

**How the backfill job uses it.** Annemarie Bester's design page, "Mapping Product Data Validation functionality to a DAB", sections 5 and 6, gives the backfill job a step `split_into_batches` (entry point `pv-plan-batches`) that writes `backfill_batches`. The next step, `validate_all_batches`, is a For each task that runs `validate_one_batch` (entry point `pv-validate`) once per batch, over batches 0 to 13, two at a time. Its results go to `publish_results`, which writes [[review_queue]] and [[run_metrics]].

**Official docs**

- [Use a For each task to run another task in a loop](https://docs.databricks.com/aws/en/jobs/for-each), Databricks documentation. The Inputs field takes a JSON array, each element passed to one iteration; `{{input}}` sets a nested task's value to the current element and `{{input.table}}` reads a field of an object element; Concurrency defaults to 1. Limits: the Inputs box holds 5,000 characters, a nested task cannot itself be a For each task, and downstream tasks cannot depend on the nested task directly.
- [Add tasks to jobs in Declarative Automation Bundles, For each task](https://docs.databricks.com/aws/en/dev-tools/bundles/job-task-types), Databricks documentation. The bundle YAML: `for_each_task` with `inputs` (required, the loop's input data), `task` (required, the nested task to run per input) and `concurrency` (optional, the most iterations running at once), in an example whose inputs come from an upstream task's value `{{tasks.generate_countries_list.values.countries}}`.

**Our plans and chapters**

- [The validate step and the agent server, why a job never starts the agent server](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07b-the-validate-step-and-the-agent-server.md#why-a-job-never-starts-the-agent-server), ai-engineering/databricks-production-deployment, starter pack page 07b. Its fourth reason is that each parallel backfill batch would start its own agent server, which is the For each task's iterations running two at a time.

> [!note]- How this was checked
> Both docs pages were opened on 2026-11-03 and answered. The first is the For each task page under Jobs; it shows the UI fields and the `{{input}}` references but no YAML. The second is the bundle task-types page, whose For each task section holds the YAML keys and their required or optional status; its example does not use `{{input}}`. The backfill job's steps, batch range and concurrency come from the design page, sections 5 and 6, and are not yet in the repo's `resources/` on the branch `feature/v4_prototype`.
