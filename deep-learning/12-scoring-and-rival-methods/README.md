# Scoring and rival methods: measured tables

One file per tool in `tables/` holds the numbers each plan measured, its working run, its broken run and its engagement-check sentences, on the "a cat and a dog" toy (seed 9 for the scorers, seeds 9 to 12 for the rival methods). `runner/` holds the recorder and checker, `records.json` it reads, and the table it wrote.

Settings: SDXL rows are 1024 px, Stable Diffusion 1.5 rows are 512 px, kept in separate tables. SynGen ran on "a black cat and a white dog". ToMe was not run.

## Where the reusable notes are

What the journey's textbook teaches about the four scorers, the T2I-CompBench sub-categories and the fair-comparison rule is filed in [[Evaluating Text-To-Image Models]], with one note per scorer. The probe renders, the benchmark snapshot and the storyboard prompts stay in the journey's `artifacts/` and `sources/` folders, and the tables and runner here stay as they are.
