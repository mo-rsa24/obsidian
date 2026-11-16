# InitNO on "a cat and a dog", seeds 9 to 12 (Stable Diffusion 1.5)

Prompt "a cat and a dog", Stable Diffusion 1.5 in half precision, 50 steps, guidance 7.5, 512 pixels, seeds 9, 10, 11, 12. Subject tokens [2, 5] ("cat", "dog").
InitNO run with the repository default settings (`run_sd_initno.py` arguments: `max_iter_to_alter` 25, `run_sd=False`); plain model is plain diffusers `StableDiffusionPipeline` with the same seeds.
Renders: `out/plain_seedNN.png` and `out/initno_seedNN.png`. Each cell below is plain / InitNO.

## CLIP cosine

| Scorer | seed 9 | seed 10 | seed 11 | seed 12 | mean |
|---|---|---|---|---|---|
| CLIP cosine, "a cat and a dog" | 0.2385 / 0.2666 | 0.2541 / 0.2618 | 0.2879 / 0.2788 | 0.2526 / 0.2691 | 0.2583 / 0.2691 |

## ImageReward

| Scorer | seed 9 | seed 10 | seed 11 | seed 12 | mean |
|---|---|---|---|---|---|
| ImageReward | -0.2793 / 0.3624 | -1.1088 / 0.1371 | 1.1099 / 1.2291 | -0.3125 / 0.9300 | -0.1477 / 0.6646 |

## BLIP-VQA

| Scorer | seed 9 | seed 10 | seed 11 | seed 12 | mean |
|---|---|---|---|---|---|
| "a cat?" | 0.9837 / 0.9699 | 0.9917 / 0.9687 | 0.9495 / 0.9832 | 0.9868 / 0.9667 | 0.9779 / 0.9721 |
| "a dog?" | 0.0588 / 0.7595 | 0.0133 / 0.0024 | 0.9232 / 0.8416 | 0.0062 / 0.4449 | 0.2504 / 0.5121 |
| product | 0.0578 / 0.7366 | 0.0132 / 0.0023 | 0.8766 / 0.8275 | 0.0061 / 0.4301 | 0.2384 / 0.4991 |

BLIP-VQA product is the product of the two yes probabilities.

## GenEval, one cat and one dog (metadata: `geneval/runs/00000/metadata.jsonl`, prompt "a photo of a cat and a dog")

| Seed | plain | InitNO |
|---|---|---|
| 9 | fail: expected dog>=1, found 0 (found cat [0.982, 0.978]) | pass (found cat [0.984], dog [0.986]) |
| 10 | fail: expected dog>=1, found 0 (found cat [0.975, 0.967]) | fail: expected dog>=1, found 0 (found cat [0.96]) |
| 11 | pass (found cat [0.983], dog [0.982], suitcase [0.58]) | pass (found cat [0.975], dog [0.977]) |
| 12 | fail: expected dog>=1, found 0 (found cat [0.976, 0.959, 0.384]) | fail: expected dog>=1, found 0 (found cat [0.975]) |
| passes | 1 of 4 | 2 of 4 |

## How far the starting noise moved

L2 distance in the 4 by 64 by 64 latent between the seed's own noise and the noise InitNO handed to the denoising loop (before the 25 per-step latent updates that InitNO's pipeline still runs). Noise norm is about 128. Cosine of 1.0 means same direction.

| Seed | L2 distance | relative to noise norm | cosine | InitNO rounds (succeeded?) |
|---|---|---|---|---|
| 9 | 6.21 | 0.048 | 0.9988 | 1 (yes) |
| 10 | 7.52 | 0.059 | 0.9983 | 1 (yes) |
| 11 | 179.83 | 1.408 | 0.0074 | 2 (no, yes) |
| 12 | 181.44 | 1.421 | -0.0099 | 5 (no, no, no, no, yes) |

Seeds 11 and 12: the first rounds did not reach the thresholds, so the method drew a fresh random noise for the next round and kept the best-scoring round. The final noise is unrelated to the seed's own noise (cosine about 0), so for those seeds the render is a different starting point, not the seed's noise nudged.

## Engagement checks (plan 11)

1. Code: passed. InitNO ran in `.venv/` on the toy with the repository's defaults, by a background worker; the numbers above are the scorers' printed output and `out/noise_movement.json`.
2. Visualize: passed. The chart `artifacts/figures/batch-methods/initno-seeds.svg` puts the plain and InitNO renders side by side on four seeds, with BLIP and GenEval verdicts, the noise movement and the means.
3. Compare: passed. Learner, looking at the InitNO render on seed 12: "seed 12 has a cartoon dog, the style changed." GenEval's fail on that render is therefore a wrong fail: the dog is there and the detector misses it.
   Two sentences: InitNO is a rival method, so it fills the InitNO row of the results table's Stable Diffusion 1.5 column, one cell per scorer, with the four scorers' numbers above. On seed 9 it turns two cats into a cat and a puppy and on seed 11 it draws a clear cat and dog, but on seeds 11 and 12 it drew fresh random noise (cosine near 0 with the seed's own), so those are different pictures, not repairs; on seed 12 the dog is a flat cartoon that the detector misses; it also applies Attend-and-Excite's latent updates, so its gain is not the noise search alone; it needs the subject tokens given by hand, runs only on Stable Diffusion 1.x, and four seeds show nothing about how often it works.

Open in plan 11: step 1.3, the run with the optimisation steps set to zero, which has not been made.
Not yet read: the InitNO paper body on its limits. The sentences above make no claim about it.

## Step 1.3: InitNO with the noise optimisation switched off (same toy, seeds 9 to 12)

The pipeline hard-wires the noise search, so `fn_initno` was replaced by a function returning the seed's own noise unchanged (`run_noopt.py`); Attend-and-Excite's latent updates still run for 25 steps. Scored by `rescore/rescore.py`.

| Run | CLIP mean | ImageReward mean | BLIP "a dog?" mean | GenEval passes |
|---|---|---|---|---|
| plain | 0.2583 | -0.1477 | 0.2504 | 1 of 4 |
| noise search off (updates only) | 0.2695 | +0.0260 | 0.5415 | 3 of 4 |
| InitNO (search and updates) | 0.2691 | +0.6646 | 0.5121 | 2 of 4 |

Per seed, BLIP dog, updates only: 0.4243, 0.7693, 0.9197, 0.0527; GenEval fails seed 12 only.
Mean absolute pixel difference of the updates-only render from plain: 57.9, 38.6, 51.4 and 58.2 (of 255), so the latent updates alone change every picture. From full InitNO: 57.2, 45.6, 100.8 and 98.3, largest on seeds 11 and 12 where InitNO drew fresh noise.
Reading: on these four seeds the dog's presence comes with the latent updates, not the noise search (dog 0.54 with updates only against 0.51 with both); the noise search adds to ImageReward (+0.69) and changes the picture most where it discarded the seed's noise. One prompt and four seeds.
