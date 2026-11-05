---
aliases: [Python wheel, Python wheels, wheel, wheels, wheel file, wheel files, whl file]
link-skip: [mouse wheel, reinvent the wheel, steering wheel, colour wheel, color wheel]
standard: vault-note v2
---

# Python Wheel

Up: [[Python]]

Software, Python. A wheel carries its [[Entry Point]] names and its dependencies, including any [[Optional Dependencies]], and a [[Declarative Automation Bundle]] builds one with `uv build` before it deploys the job that installs it.

**A Python wheel is a built package in one `.whl` file, a zip archive with a fixed file name, that an installer such as pip or uv unpacks straight into an environment without running a build step.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches wheels writes the rest around it.

## Where to learn this

**Python wheel**, a built package in one `.whl` file, installed without a build. Also: wheel, wheel file, whl file.

**Official docs**

- [Wheel distribution format](https://packaging.python.org/en/latest/specifications/binary-distribution-format/), Python Packaging User Guide. The specification: a zip archive with a fixed file name and the `.whl` extension, holding one distribution nearly as it would be installed.
- [Building distributions](https://docs.astral.sh/uv/concepts/projects/build/), uv documentation. What `uv build` makes, a source distribution and a wheel, and that uv calls the project's build backend to do it.
- [Python wheel task for jobs](https://docs.databricks.com/aws/en/jobs/tasks/python-wheel), Databricks documentation. How a Databricks job runs a wheel, by its package name and an entry point.

**Our plans and chapters**

- [From the Python file to the job YAML, step 1](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/02b-from-the-python-file-to-the-job-yaml.md#step-1-the-package-and-its-entry-point), ai-engineering/databricks-production-deployment, starter pack page 02b. `uv build` makes `dist/pv_try-0.1.0-py3-none-any.whl` for the `preflight` job and `unzip -p` reads the entry point back out of it.
- [The real entry point from the repo, errors met](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07-the-real-entry-point-from-the-repo.md#errors-met-in-this-job), the same journey, page 07. The product validation wheel installed on serverless three times on 3 Nov 2026: Python too old in run 1, ten dependencies too many in run 2, and `databricks-sdk` alone passing in run 3.
- [The wiring over the code](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/artifacts/figures/playground-bundle/wiring/the-wiring-over-the-code.png), the same journey, the picture its links table pairs with wheel words. The real lines of `pyproject.toml`, `jobs.py`, the job YAML and `databricks.yml`, with each shared name in one colour.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-03. No shelf book, lecture map, paper or staged figure teaches wheels: `gather-concept-sources.py` returned page-text hits in other senses (a carnival wheel, "reinvent the wheel"), `find-examples.py` returned a game-theory wheel, and `find-figures.py` returned none. Each docs page answered 200; the Databricks wheel task address redirects from `/jobs/python-wheel` to `/jobs/tasks/python-wheel`, which is cited. Pages 02b and 07 were read in full and the picture opened. Bare "wheel" was read on every line outside this journey that uses it: all but two mean a Python wheel, and those two are a mouse wheel, so the card keeps "wheel" with skip phrases for the other senses.
