# Databricks

Up: [[Software]]

Software, Databricks. The Databricks platform, its CLI and its serverless compute, one note per idea the walks use.

- [[Declarative Automation Bundle]]: a project's Databricks jobs written as YAML beside its code, which `databricks bundle deploy` builds, uploads and creates in a workspace; formerly called a Databricks Asset Bundle.
- [[Serverless Environment Version]]: the numbered base image a serverless job runs on, which fixes the Python version and the preinstalled packages, set as `environment_version` in the job's environment spec.
- [[Serverless Core Package]]: a package the environment version ships and a job may not replace, such as pyarrow, requests or google-auth; asking for another version of one fails the install with `ERROR_CORE_PACKAGE_VERSION_CHANGE`.
- [[For Each Task]]: a job task, `for_each_task` in YAML, that runs one nested task once per input value with a `concurrency` limit, as the backfill job runs `pv-validate` over its batches.
- [[review_queue]]: the product validation table of fail and review decisions, keyed by `sku` and `run_id`, that `pv-publish` writes for reviewers.
- [[run_metrics]]: the product validation table with one row per run, keyed by `run_id`, holding decision counts and, once the agent runs in-process, runtime, model calls, tokens and cost.
