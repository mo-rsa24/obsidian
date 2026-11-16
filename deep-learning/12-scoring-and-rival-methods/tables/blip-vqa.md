# BLIP-VQA on the seed 9 toy

BLIP yes probability per noun-phrase question, from the T2I-CompBench++ BLIP-VQA metric. The same three renders as the CLIP and ImageReward tables, held-out seed 9.
Prompt "a cat and a dog" split by spaCy into the questions "a cat?" and "a dog?". Final number is the product of the two yes probabilities.
Command: `python BLIP_vqa.py --out_dir=<run1> --np_num 2` (transformers 4.45.2, CUDA torch on the laptop GPU). Mean of the three finals: 0.4208.

| Render | "a cat?" | "a dog?" | product (the metric's score) |
|---|---|---|---|
| fused (plain product) | 0.0332 | 0.4207 | 0.0140 |
| clear (adapter) | 0.9566 | 0.6428 | 0.6149 |
| clear (joint prompt) | 0.9768 | 0.6485 | 0.6335 |

Broken run, one question only: the cat question alone is column 2, the dog question alone is column 3.

## Engagement checks (plan 03)

1. Code: passed. The T2I-CompBench++ BLIP-VQA metric ran in this folder on the three seed 9 renders; the numbers above are its output files.
2. Visualize: passed. The chart `artifacts/figures/blip-vqa-seed9/blip-vqa-seed9-three-renders.svg` puts the three renders beside the yes probabilities and ranks CLIP, ImageReward and BLIP-VQA side by side.
3. Compare: passed. Learner, looking at the fused render and asked "is this a cat?": "its not a cat." BLIP's 0.0332 on "a cat?" agrees with the learner.
   Two sentences: BLIP-VQA fills the third scorer column of the results table, with one cell per method row; these seed 9 renders are SDXL, so they fill the plain PoE and our adapter rows. It names the phrase that failed, which CLIP and ImageReward could not: the fused render answers "a cat?" with 0.0332 against 0.9566 and 0.9768 for the clear renders. It still cannot see the clutter in the adapter render, since the dog question gives about 0.64 on both clear renders, and its yes numbers are the model's own estimates, not probabilities a person would give.

Not yet read: the T2I-CompBench++ paper body on BLIP-VQA's role and limits. The sentences above make no claim about it.

## Cross-references

- The sitting that measured these numbers: [the plan "run BLIP-VQA and read its yes score"](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/plans/03-blip-vqa-asking-a-question-per-phrase.md).
- The chapter that teaches the scorer: [the textbook chapter](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/03-blip-vqa.md).
- The reusable note: [[BLIP-VQA]].
