# T2I-CompBench++ attribute-binding scorer (BLIP-VQA) on the shipped examples and on our seed 9 pair

Same scorer and venv as the BLIP-VQA table, in `../blip-vqa/` (run folders `run1` for our renders and `run2` for the shipped examples).
Each prompt is split into noun phrases and BLIP is asked one yes-or-no question per phrase; the metric's number is the product of the yes probabilities.

## Working run: the four example renders the repository ships (attribute-binding style prompts)

| Prompt | Question 1 | Question 2 | Product |
|---|---|---|---|
| a green bench and a blue bowl | a green bench? 0.7147 | a blue bowl? 0.9948 | 0.7110 |
| a brown horse and a blue vase | a brown horse? 0.9800 | a blue vase? 0.9405 | 0.9217 |
| a blue bench and a green cake | a blue bench? 0.9579 | a green cake? 0.8930 | 0.8554 |
| a horse on the right of a car | a horse? 0.9894 | a car? 0.9175 | 0.9078 |

Mean of the four products: 0.8490.

## Broken run: our prompt, outside the categories (presence of both animals only)

Seed 9 renders of "a cat and a dog", questions "a cat?" and "a dog?" with no color in either.

| Render | a cat? | a dog? | Product |
|---|---|---|---|
| fused (plain product) | 0.0332 | 0.4207 | 0.0140 |
| clear (adapter) | 0.9566 | 0.6428 | 0.6149 |
| clear (joint prompt) | 0.9768 | 0.6485 | 0.6335 |

## Engagement checks (plan 04)

1. Code: passed. The attribute-binding scorer ran in `../blip-vqa/` on the four shipped example renders and on the three seed 9 renders; the numbers above are its output files.
2. Visualize: passed. The chart `artifacts/figures/t2i-compbench-seed9/t2i-compbench-seed9.svg` puts the renders beside the per-question yes probabilities, on the benchmark's own prompts and on ours.
3. Compare: passed. Learner, looking at the "a blue bench and a green cake" render: "not green, it is pale mint." The scorer gave "a green cake?" 0.8930, so it is more generous with a pale colour than the learner.
   Two sentences: The T2I-CompBench++ attribute-binding scorer fills the fourth scorer column of the results table, and these seed 9 renders are SDXL, so the cat and dog prompt is an extra labelled outside the categories on the plain PoE and our adapter rows. It fixes the prompts every method is scored on, which a single hand-picked prompt cannot, but it checks only that each named object is present with its colour, so it accepts a pale mint cake as green (0.893) and never asks whether the horse is on the right of the car.

Not yet read: the T2I-CompBench++ paper body on its metrics and limits. The sentences above make no claim about it.

## Cross-references

- The sitting that measured these numbers: [the plan "run one T2I-CompBench++ category and place our pairs"](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/plans/04-t2i-compbench-a-fixed-prompt-set-per-category.md).
- The chapter that teaches the scorer: [the textbook chapter](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/03-blip-vqa.md#t2i-compbench-colour-and-shape).
- The reusable note: [[T2I-CompBench]].
