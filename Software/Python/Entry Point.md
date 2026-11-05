---
aliases: [entry point, entry points, console script, console scripts, console_scripts, project.scripts, python_wheel_task entry point]
link-only-in: [ai-engineering/databricks-production-deployment]
link-scope-words: [entry point, entry points]
standard: vault-note v2
---

# Entry Point

Up: [[Python]]

Software, Python. A [[Python Wheel]] stores its entry points in `entry_points.txt`, and a Databricks `python_wheel_task` runs one by name.

**An entry point is a name a Python package declares, under `[project.scripts]` in `pyproject.toml`, that points at one function in the package; installing the package makes the name a command, and `pv-preflight = "product_validation.jobs:preflight"` runs the function `preflight` in `product_validation/jobs.py`.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches entry points writes the rest around it.

## Where to learn this

**Entry point**, a name in `[project.scripts]` that points at one function and becomes a command. Also: console script, `console_scripts`, `[project.scripts]`, the `entry_point` of a `python_wheel_task`.

**Official docs**

- [Entry points specification](https://packaging.python.org/en/latest/specifications/entry-points/), Python Packaging User Guide. How `console_scripts` entry points each name a function, how an installer turns them into commands, and the `entry_points.txt` file that stores them.
- [Writing your pyproject.toml, creating executable scripts](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/), Python Packaging User Guide. A `[project.scripts]` table with one line, and the command it gives after install.
- [The pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/), Python Packaging User Guide. The `[project.scripts]`, `[project.gui-scripts]` and `[project.entry-points]` tables and what each one means.
- [Python wheel task for jobs](https://docs.databricks.com/aws/en/jobs/tasks/python-wheel), Databricks documentation. The Package name and Entry Point fields of a wheel task, which the job YAML writes as `package_name` and `entry_point`.

**Our plans and chapters**

- [From the Python file to the job YAML, the wiring](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/02b-from-the-python-file-to-the-job-yaml.md#the-wiring-which-name-in-which-file-must-equal-which), ai-engineering/databricks-production-deployment, starter pack page 02b. The left side of `pv-preflight = "pv_try.jobs:preflight"` must equal the YAML's `entry_point`, and the right side must equal the folder, file and function, with what breaks when either differs.
- [The real entry point from the repo, step 1](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/07-the-real-entry-point-from-the-repo.md#step-1-run-the-entry-point-on-the-laptop-first), the same journey, page 07. The product validation repo's `pv-preflight` runs on the laptop with `uv run pv-preflight` and prints 24 products, before the daily job runs the same entry point on serverless.
- [The Python file to the job YAML, step 4](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/02b-from-the-python-file-to-the-job-yaml.md#step-4-the-same-job-built-by-hand-in-the-ui), page 02b. The same job built in the workspace UI, where the Entry Point form field becomes the YAML's `entry_point`.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-03. No shelf book, lecture map, paper or staged figure teaches Python entry points: `gather-concept-sources.py` returned page-text hits in other senses, and `find-examples.py` and `find-figures.py` returned none. Each docs page answered 200 and was read at the passage its line describes. Pages 02b and 07 were read in full. Bare "entry point" was sampled across the learning tree (85 lines): outside this journey it often means something else (a LaTeX `main.tex`, the start of a reading, a gateway in front of services), so the phrase links only inside the databricks-production-deployment journey and the longer aliases link everywhere.
