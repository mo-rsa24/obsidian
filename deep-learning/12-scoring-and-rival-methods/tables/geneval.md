# GenEval on the seed 9 toy

GenEval's detector check (Mask2Former swin-s, threshold 0.3) on the three seed 9 renders, prompt "a photo of a cat and a dog",
requirement: at least one cat and at least one dog. CPU run, Python 3.9. Raw output: `results.jsonl` in this folder.

| Render | GenEval | cat box (score) | dog box (score) | overlap of the two boxes | also detected |
|---|---|---|---|---|---|
| fused (plain product) | pass | 0.808 | 0.965 | 0.996 | nothing |
| clear (adapter) | pass | 0.958 | 0.972 | 0.061 | bowl x2 (0.925, 0.922, one box listed twice), couch (0.776) |
| clear (joint prompt) | pass | 0.967 | 0.974 | 0.042 | nothing |

Overlap is intersection over union of the cat and dog boxes, computed from `details` in `results.jsonl`.
The picture with the boxes drawn on the renders: `/tmp` copy sent in the session; regenerate from `results.jsonl`.

## Engagement checks (plan 05)

1. Code: passed. GenEval's detector check ran in this folder on the three seed 9 renders; the table above is read from its `results.jsonl`.
2. Visualize: passed. The chart `artifacts/figures/geneval-seed9/geneval-seed9.svg` draws the detector's boxes on the renders, the overlap of the cat and dog boxes, and the four scorers side by side.
3. Compare: passed. Learner, counting the animals in the fused render: "one animal, it is a dog with cat ears." GenEval's pass for that render is therefore a false pass: one animal received both a cat box and a dog box.
   Two sentences: GenEval fills the fifth scorer column of the results table, and these seed 9 renders are SDXL, so they fill the plain PoE and our adapter rows. It counts objects by detector class, which the whole-picture scorers cannot, and it also reports clutter such as the bowl and couch in the adapter render, but it counts class names and not objects, so the fused render gets a cat box and a dog box on the same animal (overlap 0.996) and passes.

Not yet read: the GenEval paper body on its detector, thresholds and limits. The sentences above make no claim about it.

## Cross-references

- The sitting that measured these numbers: [the plan "run GenEval and read pass or fail per object"](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/plans/05-geneval-a-detector-checks-the-objects.md).
- The chapter that teaches the scorer: [the textbook chapter](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/04-geneval.md).
- The reusable note: [[GenEval]].
