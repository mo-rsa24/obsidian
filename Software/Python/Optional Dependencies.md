---
aliases: [optional dependencies, optional dependency, project.optional-dependencies, optional-dependencies, package extras, package extra]
standard: vault-note v2
---

# Optional Dependencies

Up: [[Python]]

Software, Python. They let one [[Python Wheel]] install small for a Databricks serverless job and in full on a laptop, which is how the product validation wheel avoided replacing a [[Serverless Core Package]].

**Optional dependencies are packages a Python project lists under a name in `[project.optional-dependencies]`; a plain install of the package leaves them out, and naming the extra brings them in, as in `pip install "product-validation-prototype[agent]"`.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches extras writes the rest around it.

## Where to learn this

**Optional dependencies**, packages under a named extra that a plain install leaves out. Also: `[project.optional-dependencies]`, package extras.

**Official docs**

- [Managing dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/), uv documentation. `project.optional-dependencies` as published "extras", set beside `dependency-groups`, which stay local for development.
- [Writing your pyproject.toml, dependencies and optional dependencies](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/), Python Packaging User Guide. How to list base dependencies and named optional ones in `pyproject.toml`.
- [The pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/), Python Packaging User Guide. The `optional-dependencies` field and what each named list means.

**Our plans and chapters**

- [The real entry point from the repo, the files](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07-the-real-entry-point-from-the-repo.md#the-files-as-they-are), ai-engineering/databricks-production-deployment, starter pack page 07. The product validation `pyproject.toml` with `databricks-sdk` as its only base dependency, nine packages in the `agent` extra, and a `dev` group that installs the package with that extra.
- [The real entry point from the repo, errors met](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07-the-real-entry-point-from-the-repo.md#errors-met-in-this-job), the same page. Run 2 on 3 Nov 2026 fails with all ten dependencies in the base install, and moving nine into the `agent` extra lets run 3 pass in 34 seconds.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-03. No shelf book, lecture map, paper or staged figure teaches optional dependencies: `gather-concept-sources.py` returned page-text hits in other senses (dependency grammar in the NLTK book, a database textbook), and `find-examples.py` and `find-figures.py` returned none. Each docs page answered 200 and was read at the passage its line describes. Page 07 was read in full. Bare "extras" is left out as an alias: across the learning tree it mostly means extra objects or rows ("planted extras"), so the card keeps "package extras".
