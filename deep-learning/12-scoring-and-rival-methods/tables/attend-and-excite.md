# Attend-and-Excite on the seed 9 toy (Stable Diffusion 1.5)

Prompt "a cat and a dog", seed 9, Stable Diffusion 1.5 in half precision, 50 steps, guidance 7.5. Subject tokens 2 ("cat") and 5 ("dog").
Renders: `scored/plain_sd15_seed09.png` (method off, two cats) and `scored/ae_on_seed09.png` (method on). The method-off render from the method's own code is pixel-identical to the toy.

| Scorer, on "a cat and a dog" | method off (two cats) | method on |
|---|---|---|
| CLIP cosine | 0.2380 | 0.2884 |
| ImageReward | -0.2715 | 0.8530 |
| BLIP-VQA "a cat?" | 0.9832 | 0.9860 |
| BLIP-VQA "a dog?" | 0.0568 | 0.4243 |
| BLIP-VQA product | 0.0558 | 0.4184 |
| GenEval, one cat and one dog | fail: expected dog>=1, found 0 (two cat boxes, 0.981 and 0.978) | pass: cat 0.965, dog 0.970 |

BLIP-VQA product is computed as the product of the two yes probabilities. These are the SD 1.5 column of the results table, kept apart from the SDXL rows.

## Engagement checks (plan 06)

1. Code: passed. Attend-and-Excite ran in `ae-venv/` on the toy (prompt "a cat and a dog", seed 9, tokens 2 and 5); the renders are in `ae_out/` and the numbers above are the scorers' printed output.
2. Visualize: passed. The chart `artifacts/figures/attend-and-excite-seed9/ae-seed9.svg` puts the toy and the method render side by side with GenEval's boxes and four scorers. Read against the toy, the plain render is the broken run (the dog is dropped, two cats) and the method render is the working run (a dog is present); the measured numbers agree in direction: the dog question rises from 0.0568 to 0.4243.
3. Compare: passed. Learner, looking at the method render: "the dog is back but cropped at the edge."
   Two sentences: Attend-and-Excite is a rival method, so it fills the Attend-and-Excite row of the results table's Stable Diffusion 1.5 column, one cell per scorer, with the CLIP, ImageReward, BLIP-VQA and GenEval numbers above. On seed 9 it brings the dog back, so the dog question rises from 0.057 to 0.424 and GenEval stops finding two cats, but it needs the subject token positions given by hand, it changes the picture (a larger cat and a dog cropped at the frame edge, so BLIP's dog yes stays below the 0.64 it gave a clear dog), it runs only on Stable Diffusion 1.x, and one seed shows nothing about how often it works.

Not yet read: the Attend-and-Excite paper body on its limits. The sentences above make no claim about it.
