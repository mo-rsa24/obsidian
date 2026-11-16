# ImageReward on the seed 9 toy

ImageReward-v1.0 reward for each render and prompt. The same three renders as the CLIP table, held-out seed 9, cat and dog.
Command: `python run_ir.py "a cat and a dog" "a horse and a cow"` (transformers 4.45.2, CPU).

| Render | File | "a cat and a dog" | "a horse and a cow" |
|---|---|---|---|
| fused (plain product) | renders/fused_poe_seed09.png | -1.0717 | -2.2738 |
| clear (adapter) | renders/clear_adapter_seed09.png | 1.0691 | -2.1843 |
| clear (joint prompt) | renders/joint_prompt_seed09.png | 0.8993 | -2.2661 |

Drop from the right prompt to the wrong one: adapter 3.2534, joint prompt 3.1654, fused 1.2021.
Gap between the best clear render and the fused render on the right prompt: 2.1408 (adapter) and 1.9710 (joint prompt).

## Engagement checks (plan 02)

1. Code: passed. ImageReward ran in this folder on the three seed 9 renders; the six rewards above are its printed output.
2. Visualize: passed. The chart `artifacts/figures/imagereward-seed9/imagereward-seed9-three-renders.svg` puts the three renders beside their rewards and sets ImageReward beside CLIP on the right prompt.
3. Compare: passed. Learner's pick between the two clear renders: the joint-prompt render ("done joint"), because the adapter render has "some strange details" (a bowl of kibble and a small gnarled creature). ImageReward picks the other one, by 0.17.
   Two sentences: ImageReward fills the second scorer column of the results table, with one cell per method row; these seed 9 renders are SDXL, so they fill the plain PoE and our adapter rows. It separates the fused render from the clear ones by about 2 reward units, far more than CLIP's 0.054, but between the two clear renders it prefers the adapter render where the learner prefers the joint-prompt one, and under a wrong prompt all three renders fall within 0.09 of each other.

Not yet read: the ImageReward paper body on its limits. The sentences above make no claim about it.

## Cross-references

- The sitting that measured these numbers: [the plan "run ImageReward and say what its number prefers"](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/plans/02-imagereward-the-preference-number.md).
- The chapter that teaches the scorer: [the textbook chapter](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/02-imagereward.md).
- The reusable note: [[ImageReward]].
