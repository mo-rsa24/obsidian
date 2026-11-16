# CLIP score on the seed 9 toy

CLIP ViT-B/32 cosine between each render and the prompt. All three renders are cat and dog, held-out seed 9.
Command: `python run_clip.py "a cat and a dog"` (transformers 4.57.6, CPU).

| Render | File | Prompt | Cosine |
|---|---|---|---|
| fused (plain product) | renders/fused_poe_seed09.png | a cat and a dog | 0.2482 |
| clear (adapter) | renders/clear_adapter_seed09.png | a cat and a dog | 0.3025 |
| clear (joint prompt) | renders/joint_prompt_seed09.png | a cat and a dog | 0.3021 |

## Broken run: single-animal prompts (task 1.3)

| Render | "a cat and a dog" | "a cat" | "a dog" |
|---|---|---|---|
| fused (plain product) | 0.2482 | 0.2538 | 0.2720 |
| clear (adapter) | 0.3025 | 0.2304 | 0.2294 |
| clear (joint prompt) | 0.3021 | 0.2344 | 0.2304 |

## What moved between the joint prompt and the single-animal prompts (instruction 2.1)

Read off the chart by Claude at the learner's request ("you tell me"). Going from "a cat and a dog" to "a cat" or "a dog",
both clear renders fell by about 0.07 (adapter 0.3025 to 0.2304 and 0.2294; joint prompt 0.3021 to 0.2344 and 0.2304), while the
fused render rose (0.2482 to 0.2538 on "a cat" and to 0.2720 on "a dog"), so the order flipped and the printed scores did not
stay the same.

## Engagement checks (plan 01)

1. Code: passed. CLIP score ran in this folder on the three seed 9 renders; the nine numbers above are its printed output.
2. Visualize: passed on Claude's reading at the learner's request. The chart `artifacts/figures/clip-seed9/clip-seed9-three-renders.svg` puts the three renders beside their cosines. Read against the toy page: the two clear renders behave like the toy's "both" arrow (highest on the joint prompt), the fused render like the arrow turned away from the prompt (lower on the joint prompt, relatively higher on one animal).
3. Compare: passed. Learner saw, in a split view of the two clear renders: "Adapter has some strange details", namely a bowl of kibble at the bottom and a small gnarled creature figure at the right, both absent from the joint-prompt render.
   Two sentences: CLIP score fills one scorer column of the results table, with one cell per method row; these seed 9 renders are SDXL, so they fill the plain PoE and our adapter rows. On this seed it tells the fused render (0.2482) from the two clear renders (0.3025 and 0.3021) under the joint prompt, but it cannot tell the two clear renders apart although the adapter render carries a bowl of kibble and a gnarled creature the joint-prompt render lacks, and on a single-animal prompt it ranks the fused render above the clear ones.

Not yet read: the CLIP paper body on whole-image matching. The sentences above make no claim about it.

## Cross-references

- The sitting that measured these numbers: [the plan "run CLIP score and say what it cannot tell apart"](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/plans/01-clip-score-and-what-it-cannot-tell-apart.md).
- The chapter that teaches the scorer: [the textbook chapter](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/01-clip-score.md).
- The reusable note: [[CLIP Score]].
