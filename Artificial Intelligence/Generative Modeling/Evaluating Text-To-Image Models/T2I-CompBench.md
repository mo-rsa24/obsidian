---
aliases: [T2I-CompBench, T2I-CompBench++, T2I-CompBench sub-categories, T2I-CompBench colour, T2I-CompBench shape, compositional text-to-image benchmark]
sources:
  - "The T2I-CompBench++ paper, pages 3, 4, 6, 7 and 12: /home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/benchmarks/t2i-compbench-benchmark-for-compositional-text-to-image-generation.pdf"
  - "The journey's figure of the eight sub-categories, drawn from the paper: /home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/artifacts/figures/metric-sheets/blip-vqa/t2i-compbench-categories.svg"
standard: vault-note v2
---

# T2I-CompBench

Up: [[Evaluating Text-To-Image Models]] · ⬅️ [[GenEval]] · [[Comparing Methods Fairly]] ➡️

Artificial Intelligence, Generative Modeling. Needs: [[Benchmark]] for what a prompt set is, [[BLIP-VQA]] for the scorer behind colour, shape and texture.

**T2I-CompBench++ is a prompt set of eight sub-categories of 1,000 prompts each, and each sub-category is scored by one fixed scorer, so the name of a column tells you which scorer produced it.**

> [!question]- Test yourself
> No quiz page covers this folder yet. It is waiting to be built.

> [!warning]- Unfinished
> - The three drawn pictures (form, mechanism, deep-dive sheet) are not drawn; the one code-drawn SVG of the table below is filed.
> - No sandbox was built: nothing here is a command, and the scorers other than BLIP-VQA were not read from code.
> - UniDet is named in the journey's files but not explained in them, so what it is stays unknown here.
> - No quiz page yet.
> - No claim is marked stated.

## Table of contents

- [What T2I-CompBench is](#what-t2i-compbench-is)
- [Which scorer measures each sub-category](#which-scorer-measures-each-sub-category)
- [The colour and shape prompt sets](#the-colour-and-shape-prompt-sets)

## What T2I-CompBench is

Navigation: 📋 [TOC](#table-of-contents)

**T2I-CompBench++** is a [[Benchmark]] with eight sub-categories of 1,000 prompts each, 700 for training and 300 for testing, 8,000 prompts in all *(cited: paper page 3)*. A "T2I-CompBench colour" cell is the scorer of the colour sub-category run on the colour prompt set.

### Words the name uses

**T2I.** Text to image, the task the prompts are for. **Comp.** Compositional: prompts that name several things, their colours, shapes or positions. **Bench.** A [[Benchmark]], a fixed set of prompts and scorers. The `++` is the paper's extended version. *(cited: the paper's title, "benchmark for compositional text-to-image generation")*

**All the words together.** A fixed prompt set for compositional text-to-image generation, with a scorer chosen per kind of prompt.

**The consequence.** To know what a number means, find its sub-category in the table below, then read the scorer's note.

## Which scorer measures each sub-category

![T2I-CompBench++ has eight sub-categories of 1,000 prompts each and the scorer for each: colour, shape and texture use BLIP-VQA, 2D spatial and numeracy use UniDet, 3D spatial uses UniDet plus depth, non-spatial uses CLIPScore, complex uses a 3-in-1 metric|800](assets/t2i-compbench-eight-sub-categories-and-their-scorers.svg)

| Group | Sub-category | Scorer | Where the paper says it |
|---|---|---|---|
| attribute binding | colour | [[BLIP-VQA]] | page 6 |
| attribute binding | shape | [[BLIP-VQA]] | page 6 |
| attribute binding | texture | [[BLIP-VQA]] | page 6 |
| object relationships | 2D spatial | UniDet, a detector | page 6 |
| object relationships | 3D spatial | UniDet plus depth | pages 6 and 7 |
| object relationships | non-spatial | [[CLIP Score]] (CLIPScore) | page 7 |
| numeracy | numeracy | UniDet | page 6 |
| complex compositions | complex | a 3-in-1 metric | page 7 |

**How to read this table.** Each row is one sub-category with 1,000 prompts. The scorer is the model that turns one render of one of its prompts into a number. *(cited: the journey's figure, from the paper's pages 6 and 7)*

**What to look for.** Only three rows use the scorer that carries the project's verdict. The paper states that BLIP-VQA is applied to colour, shape and texture, and that CLIPScore works best for non-spatial relationships, with the 3-in-1 metric designed for complex ones *(cited: pages 6 and 7)*. UniDet is listed as a detector in the figure; what UniDet itself is, is unknown here. The detector in [[GenEval]] is a different one.

**A caution about the project's tables.** In the layout sheet's table R14 as filed, the T2I-CompBench columns are spatial and complex, which are not BLIP-VQA. Colour and shape in the main table use BLIP-VQA. *(cited: the journey's chapter 3)*

## The colour and shape prompt sets

Colour and shape each have 1,000 prompts: 800 follow the template "a {adj} {noun} and a {adj} {noun}", such as "a red flower and a yellow vase", and 200 are natural sentences such as "a room with blue curtains and a yellow chair" *(cited: page 4)*. For the paper's models, the colour score runs from 0.38 (Stable Diffusion v1.4) to 0.81 (Stable Diffusion 3) and the shape score from 0.36 to 0.62 *(cited: Table XIII, page 12)*.

**Other ways.** [[GenEval]] is a different prompt set with its own detector rules.

**Why this matters.** The same word, "T2I-CompBench", sits over columns made by three kinds of scorer. Quoting a score without its sub-category leaves the reader unable to say what it measured.

**Taught in.**

- [Journey chapter 3, the T2I-CompBench section](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/03-blip-vqa.md#t2i-compbench-colour-and-shape), deep-learning/diffusion-models, plan folder 12: the eight sub-categories and which use BLIP-VQA.
- [Journey plan 4, run one T2I-CompBench++ category and place our pairs](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/plans/04-t2i-compbench-a-fixed-prompt-set-per-category.md): the sitting that runs it.
- The T2I-CompBench++ paper, [page 3](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/benchmarks/t2i-compbench-benchmark-for-compositional-text-to-image-generation.pdf#page=3) for the prompt counts and [page 6](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/benchmarks/t2i-compbench-benchmark-for-compositional-text-to-image-generation.pdf#page=6) for the scorers.

**Applied in.** The research project's colour and shape columns in its main tables use BLIP-VQA, and its table R14 names two T2I-CompBench columns (spatial and complex) that use other scorers. In words only.

> [!note]- How this was checked
> The table was copied from the journey's `t2i-compbench-categories.svg` and chapter 3 on 2026-11-12, and nothing was run. The 3D spatial row and its "UniDet plus depth" scorer are in the figure only, not in the chapter's prose. The figure is a copy of the journey's own.
