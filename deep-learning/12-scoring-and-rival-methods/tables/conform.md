# CONFORM on the seed 9 toy (Stable Diffusion 1.5)

Prompt "a cat and a dog", seed 9, Stable Diffusion 1.5 in half precision, 50 steps, guidance 7.5. Subject token groups [[2], [5]] ("cat", "dog").
CONFORM settings from the repository's notebook: temperature 0.5, NT-Xent loss, 20 refinement steps at iterations 0, 10 and 20, scale factor 20, attention resolution 16 by 16.
Renders: `out/plain.png` (plain model), `out/conform_off.png` (scale factor 0, the contrastive weight zero; pixel-identical to the plain render) and `out/conform_on.png`.

| Scorer, on "a cat and a dog" | plain / weight zero (two cats) | CONFORM on |
|---|---|---|
| CLIP cosine | 0.2374 | 0.2844 |
| ImageReward | -0.1914 | 0.9187 |
| BLIP-VQA "a cat?" | 0.9836 | 0.9905 |
| BLIP-VQA "a dog?" | 0.0613 | 0.6589 |
| BLIP-VQA product | 0.0603 | 0.6526 |
| GenEval, one cat and one dog | fail: expected dog>=1, found 0 (two cat boxes, 0.982 and 0.978) | pass: cat 0.974, dog 0.979 |

Attention maps (16 by 16, cat token 2 and dog token 5, steps 0, 10, 20, 30, 49): `out/maps_conform_on.png` and `out/maps_conform_off.png`.
With the weight zero the dog token's attention scatters and peaks on the large cat at the upper left; with CONFORM on it gathers at the right edge from step 10.
These are the Stable Diffusion 1.5 column of the results table, kept apart from the SDXL rows. BLIP-VQA product is the product of the two yes probabilities.

## Engagement checks (plan 07)

1. Code: passed. CONFORM ran in `.venv/` on the toy with `run_conform.py`; the renders, maps and numbers above are its output.
2. Visualize: passed. The chart `artifacts/figures/conform-seed9/conform-seed9.svg` shows the toy and both SD 1.5 methods with GenEval boxes, four scorers across four renders, and the attention maps with the weight zero and on. Read against the toy: the weight-zero run is the broken run and is pixel-identical to the plain model (the dog's attention lands on the large cat); the CONFORM run gathers the dog's attention at the right edge and the dog appears there.
3. Compare: passed. Learner, looking at the CONFORM render: "the dog is back but only its head, cropped at the edge."
   Two sentences: CONFORM is a rival method, so it fills the CONFORM row of the results table's Stable Diffusion 1.5 column, one cell per scorer, with the CLIP, ImageReward, BLIP-VQA and GenEval numbers above. On seed 9 it brings the dog back (the dog question rises from 0.061 to 0.659 and GenEval stops finding two cats) by pushing the cat and dog attention maps apart, which the maps show directly, but only the dog's head is in frame, it needs the subject tokens given by hand, it runs only on Stable Diffusion 1.x, and one seed shows nothing about how often it works.

Scorer noise: the plain render made again in these libraries is the same picture to the eye (mean pixel difference about 1 of 255), and its scores differ from the toy's by 0.0006 on CLIP and 0.08 on ImageReward. Differences smaller than that between two renders are not evidence.

Not yet read: the CONFORM paper body on its limits. The sentences above make no claim about it.
