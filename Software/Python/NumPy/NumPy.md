---
aliases: [numpy, np]
sources:
  - "NumPy reference, numpy.array: https://numpy.org/doc/stable/reference/generated/numpy.array.html, read 2026-10-04"
  - "NumPy user guide, the absolute basics: https://numpy.org/doc/stable/user/absolute_beginners.html, read 2026-10-04"
  - "NumPy user guide, broadcasting: https://numpy.org/doc/stable/user/basics.broadcasting.html, read 2026-10-04"
  - "NumPy reference, Random Generator: https://numpy.org/doc/stable/reference/random/generator.html, read 2026-10-04"
  - "NumPy reference, Legacy random generation: https://numpy.org/doc/stable/reference/random/legacy.html, read 2026-10-04"
  - "NumPy reference, Generator.standard_normal: https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html, read 2026-10-04"
---

# NumPy

Up: [[Python]]

Software, Python. Needs: [[Modules And Imports]] for how a second file gets at the arrays you define.

> [!question] Test yourself
> [The NumPy quiz](https://claude.ai/artifact/Lh1wvXBiirkRyDvn76yZKR) covers [[Arrays Versus Python Lists]], [[Broadcasting]] and [[Random Numbers From A Seeded Generator]] in 19 questions. Your attempts are saved on the page.

> [!warning] Unfinished
> - No project has applied NumPy yet. Every run in these notes is a sandbox run.
>
> Each note below lists its own missing pictures and runs at its top.

**NumPy gives Python an array: a block of numbers of one type that arithmetic acts on number by number.** This note shows why a plain Python list cannot do that job, then does the same arithmetic with arrays on three small Gaussians. The sandbox is one empty folder.

## Where you work

- Any terminal with Python 3 and `uv`. On the PC, that is Ubuntu under WSL.
- A new empty folder. Nothing here touches a real project.

**Prepare the sandbox.** Make the folder and check NumPy loads.

```bash
mkdir -p ~/playground/sandbox/numpy-arrays && cd ~/playground/sandbox/numpy-arrays
uv run --no-project --with numpy python -c "import numpy; print(numpy.__version__)"
```

You should see a version number. This run printed `2.4.6`. Any NumPy 1.x or 2.x behaves the same here.

If `uv` is missing, install it from [the uv installation page](https://docs.astral.sh/uv/getting-started/installation/), or use a virtual environment with `pip install numpy` and drop the `uv run --no-project --with numpy` prefix from every command below.

## Notes in this folder

Read them in this order.

- [[Arrays Versus Python Lists]]: why a Python list cannot do number-by-number arithmetic, and the same arithmetic with arrays on three small Gaussians.
- [[Broadcasting]]: how arrays of different shapes line up from the right, and the error when they cannot.
- [[Random Numbers From A Seeded Generator]]: a seeded generator that repeats its stream, and why the global generator ignores your seed.

> [!note]- How this was checked
> The list-based `toy.py` is the learner's own file, copied byte for byte from the walk, and its output matched the learner's run exactly. The array values match the walk's answer key, `checks/toy.py` in the paper's folder under the journey's `sources/mechanisms-of-projective-composition/`.
>
> `unseeded.py` reproduces the walk's step 2 slip in the learner's own `samples.py`, which made `rng` and drew from `np.random.standard_normal`; the learner's file is quoted in its sampler line and import, with the print reduced to one cloud.
>
> The six output pictures were rendered from the captured text by a script in DejaVu Sans Mono, never drawn.
>
> References, each link checked on 2026-10-04 and answering 200: [numpy.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html), [the absolute basics](https://numpy.org/doc/stable/user/absolute_beginners.html), [broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html), [Random Generator](https://numpy.org/doc/stable/reference/random/generator.html), [Legacy random generation](https://numpy.org/doc/stable/reference/random/legacy.html), [Generator.standard_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html). NumPy's documentation is under the BSD 3-Clause licence. No tldr-pages entry exists for NumPy.
