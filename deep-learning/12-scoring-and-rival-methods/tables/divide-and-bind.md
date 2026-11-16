# Divide-and-Bind on the toy (Stable Diffusion 1.5)

Prompt "a cat and a dog", seeds 9 to 12, Stable Diffusion 1.5 in half precision, 50 steps, guidance 7.5, 512 pixels. Subject tokens [2, 5] ("cat", "dog"), no attribute tokens.
Divide-and-Bind settings from the repository's notebook: loss mode `tv_bind` (total-variation attendance loss plus binding loss; with no attribute tokens the binding part has nothing to bind), thresholds {0: 0.05, 10: 0.2, 20: 0.3}, 50 refinement steps at the first iteration, optimisation up to iteration 25, scale factor 20, attention resolution 16 by 16.
Renders: `out/plain_seedNN.png` (the pipeline's own standard mode, `run_standard_sd=True`) and `out/dnb_seedNN.png`.

| CLIP cosine | seed 9 | seed 10 | seed 11 | seed 12 | mean |
|---|---|---|---|---|---|
| plain | 0.2356 | 0.2537 | 0.2880 | 0.2527 | 0.2575 |
| Divide-and-Bind | 0.2788 | 0.2923 | 0.2527 | 0.2332 | 0.2642 |

| ImageReward | seed 9 | seed 10 | seed 11 | seed 12 | mean |
|---|---|---|---|---|---|
| plain | -0.2802 | -1.0836 | 1.1235 | -0.2386 | -0.1197 |
| Divide-and-Bind | 0.5514 | 0.9509 | 0.7706 | -0.8091 | 0.3659 |

| BLIP-VQA "a cat?" | seed 9 | seed 10 | seed 11 | seed 12 | mean |
|---|---|---|---|---|---|
| plain | 0.9827 | 0.9915 | 0.9494 | 0.9870 | 0.9777 |
| Divide-and-Bind | 0.9371 | 0.9856 | 0.9865 | 0.9751 | 0.9711 |

| BLIP-VQA "a dog?" | seed 9 | seed 10 | seed 11 | seed 12 | mean |
|---|---|---|---|---|---|
| plain | 0.0812 | 0.0125 | 0.9244 | 0.0062 | 0.2561 |
| Divide-and-Bind | 0.8294 | 0.7815 | 0.9513 | 0.0186 | 0.6452 |

| BLIP-VQA product | seed 9 | seed 10 | seed 11 | seed 12 | mean |
|---|---|---|---|---|---|
| plain | 0.0798 | 0.0124 | 0.8776 | 0.0061 | 0.2440 |
| Divide-and-Bind | 0.7772 | 0.7702 | 0.9385 | 0.0181 | 0.6260 |

| GenEval, one cat and one dog | seed 9 | seed 10 | seed 11 | seed 12 | passes |
|---|---|---|---|---|---|
| plain | fail: expected dog>=1, found 0 (two cat boxes 0.981, 0.979) | fail: expected dog>=1, found 0 (two cat boxes 0.975, 0.967) | pass: cat 0.983, dog 0.982 | fail: expected dog>=1, found 0 (cat boxes 0.977, 0.959, 0.386) | 1 of 4 |
| Divide-and-Bind | pass: cat 0.968, dog 0.974 | pass: cat 0.963, dog 0.977 | pass: cat 0.980, dog 0.972 and 0.960 | pass: cat 0.968, 0.959, 0.718, 0.662, dog 0.644 | 4 of 4 |

GenEval used the metadata line "a photo of a cat and a dog" (cat 1, dog 1) as given, with one folder per render. BLIP-VQA product is the product of the two yes probabilities.
Scorer noise from the CONFORM table applies here: differences under about 0.001 on CLIP and 0.08 on ImageReward between two renders are not evidence. Four seeds show nothing about how often either model works.
Divide-and-Bind seed 12 passes GenEval but looks like three cats with a small dark animal at the bottom edge (dog box 0.644, BLIP dog 0.0186); read the render before counting that pass.

## Engagement checks (plan 10)

1. Code: passed. Divide and Bind ran in `.venv/` on the toy (loss mode `tv_bind`, subject tokens 2 and 5, seeds 9 to 12) by a background worker; the numbers above are the scorers' printed output.
2. Visualize: passed. The chart `artifacts/figures/batch-methods/divide-and-bind-seeds.svg` puts the plain and Divide and Bind renders side by side on four seeds, with BLIP and GenEval verdicts and the means.
3. Compare: passed. Learner, looking at the Divide and Bind render on seed 12: "seed 12 has no dog, the small animal is a cat." GenEval's pass on that render is therefore a false pass.
   Two sentences: Divide and Bind is a rival method, so it fills the Divide and Bind row of the results table's Stable Diffusion 1.5 column, one cell per scorer, with the four scorers' numbers above. It replaces two cats with a cat and a dog on seeds 9 and 10 (BLIP dog 0.08 to 0.83 and 0.01 to 0.78) and keeps seed 11's dog, but seed 12 still has no dog while GenEval passes it, the prompt had no attribute for its binding loss to bind so only the attendance loss acted, it needs the subject tokens given by hand, it runs only on Stable Diffusion 1.x, and four seeds show nothing about how often it works.

Open in plan 10: step 1.3, the attendance-only and binding-only runs, which have not been made.
Not yet read: the Divide and Bind paper body on its limits. The sentences above make no claim about it.

## Step 1.3: the repository's other loss modes (same toy, method on only, seeds 9 to 12)

Scored by `rescore/rescore.py` (results in `rescore/results.json`). `tv` is the attendance loss alone; binding has no mode of its own in this repository, and this prompt has no attribute tokens, so `tv` is expected to match `tv_bind`.

| Mode | CLIP mean | ImageReward mean | BLIP "a dog?" mean | GenEval passes |
|---|---|---|---|---|
| `tv_bind` (both losses, the worker's run) | 0.2642 | 0.3659 | 0.6452 | 4 of 4 |
| `tv` (attendance only) | 0.2636 | 0.3686 | 0.6443 | 4 of 4 |
| `max` (max-attention loss) | 0.2696 | 0.4175 | 0.5498 | 4 of 4 |
| plain | 0.2575 | -0.1197 | 0.2561 | 1 of 4 |

`tv` against `tv_bind`, mean absolute pixel difference per seed: 0.30, 0.62, 0.50 and 3.28 (of 255). The pictures are the same to the eye, so the binding loss changed nothing on this prompt and only the attendance loss acted. `max` against `tv_bind` differs by 35 to 59, a different picture on every seed.
Seed 12 under `tv` and `max`: BLIP dog 0.0126 and 0.0631, yet GenEval passes both, the same doubtful pass as the both-losses render.
