---
aliases: [Declarative Automation Bundles, Databricks Asset Bundle, Databricks Asset Bundles, Databricks bundle, Databricks bundles, DAB, DABs, asset bundle, asset bundles]
standard: vault-note v2
---

# Declarative Automation Bundle

Up: [[Databricks]]

Software, Databricks. It is how a [[Python Wheel]] and the job that runs it reach a workspace: `databricks bundle deploy` builds the wheel and creates the job its YAML describes.

**A Declarative Automation Bundle, formerly called a Databricks Asset Bundle, is a folder whose `databricks.yml` and resource YAML files describe Databricks jobs and other resources as code, which the Databricks CLI validates, deploys to a named target workspace and runs.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches bundles writes the rest around it.

## Where to learn this

**Declarative Automation Bundle**, a project's Databricks jobs written as YAML beside its code and deployed by the CLI. Also: Databricks Asset Bundle, DAB, DABs, Databricks bundle, asset bundle.

**Textbooks**

- The big book of MLOps, chapter 5, Implementing MLOps on Databricks: [page 50](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=50). One paragraph, from October 2023 under the old name: the MLOps Stacks template deploys its CI/CD and ML pipelines as jobs through the CLI with asset bundles, which validate, deploy and run jobs and pipelines and manage MLflow experiments and models.

**Official docs**

- [What are Declarative Automation Bundles?](https://docs.databricks.com/aws/en/dev-tools/bundles/), Databricks documentation. What a bundle is, under its current name and its former one, and when a project should use one.
- [Bundle configuration](https://docs.databricks.com/aws/en/dev-tools/bundles/settings), Databricks documentation. Every top-level key of `databricks.yml`, including the `artifacts` block that builds a wheel before deploy.
- [Build a Python wheel file using bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/python-wheel), Databricks documentation. The official walk from a Python package to a bundle that builds it as a wheel and runs it as a job.
- [The bundle command group](https://docs.databricks.com/aws/en/dev-tools/cli/bundle-commands), Databricks documentation. What `bundle validate`, `deploy`, `run` and `destroy` each do, with every option.

**Our plans and chapters**

- [The real entry point from the repo, step 3](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07-the-real-entry-point-from-the-repo.md#step-3-validate-deploy-and-run), ai-engineering/databricks-production-deployment, starter pack page 07. Validates, deploys and runs the product validation bundle's daily job in the playground, and the third run on 3 Nov 2026 ends `TERMINATED SUCCESS` in 34 seconds with 24 products counted.
- [Write a bundle from intent](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/06-write-a-bundle-from-intent.md#the-five-questions), the same journey, page 06. Five questions that place every key of a bundle, then the command ladder saying what each command changes and how to undo it.
- [From the Python file to the job YAML](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/02b-from-the-python-file-to-the-job-yaml.md#the-order-to-write-it-in), the same journey, page 02b. Builds the `preflight` wheel job in the playground bundle in five steps, from the Python function to `bundle run preflight`.
- [DABs and the smallest bundle](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/02-dabs-and-templates.md#the-smallest-bundle-write-it-and-validate-it), the same journey, page 02. Writes and validates the smallest bundle, the page the journey's links table sends bundle words to.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-03. The one shelf book that names bundles, the big book of MLOps, gives them a single paragraph on page 50, read in full. No lecture map, video lessons row, paper or staged figure teaches bundles: `gather-concept-sources.py` with every alias returned only scattered page-text hits for "DAB" (readability, AdaBoost), `find-examples.py` returned none, and `find-figures.py` returned none. Each docs page answered 200 and was read at the passage its line describes. Pages 07, 06 and 02b were read in full and page 02 at its headings. The journey's links table (`LINKS.md`) routes "Databricks Asset Bundles, DAB, DABs, Declarative Automation Bundles" to page 02 and the bundles docs. Bare "bundle" is left out as an alias because walks use it in other senses.
