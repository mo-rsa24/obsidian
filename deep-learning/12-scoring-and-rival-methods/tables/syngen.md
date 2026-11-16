# SynGen on the seed 9 to 12 toy (Stable Diffusion 1.5)

Prompt "a black cat and a white dog", seeds 9, 10, 11, 12, Stable Diffusion 1.5 in half precision, 50 steps, guidance 7.5, 512 pixels.
SynGen settings: repository defaults (step size 20, attention resolution 16 by 16, 25 intervention steps). Renders: `out/plain_seedNN.png` and `out/syngen_seedNN.png`. Scores are copied from `scratch_score.log` (produced by `score_all.sh`).


## CLIP cosine

| Seed | plain | SynGen |
|---|---|---|
| 9 | 0.3036 | 0.3433 |
| 10 | 0.3333 | 0.3358 |
| 11 | 0.2970 | 0.3220 |
| 12 | 0.3006 | 0.3048 |
| mean | 0.3086 | 0.3265 |

## ImageReward

| Seed | plain | SynGen |
|---|---|---|
| 9 | -0.6026 | 1.4295 |
| 10 | 1.2264 | 1.3673 |
| 11 | 0.1487 | 1.2306 |
| 12 | 0.5504 | 0.2610 |
| mean | 0.3307 | 1.0721 |

## BLIP-VQA "a black cat?"

| Seed | plain | SynGen |
|---|---|---|
| 9 | 0.9695 | 0.9864 |
| 10 | 0.9880 | 0.9933 |
| 11 | 0.9742 | 0.9896 |
| 12 | 0.9881 | 0.9406 |
| mean | 0.9799 | 0.9775 |

## BLIP-VQA "a white dog?"

| Seed | plain | SynGen |
|---|---|---|
| 9 | 0.0240 | 0.9891 |
| 10 | 0.9915 | 0.9590 |
| 11 | 0.0219 | 0.6822 |
| 12 | 0.0194 | 0.0754 |
| mean | 0.2642 | 0.6764 |

## BLIP-VQA product

| Seed | plain | SynGen |
|---|---|---|
| 9 | 0.0233 | 0.9756 |
| 10 | 0.9796 | 0.9526 |
| 11 | 0.0213 | 0.6751 |
| 12 | 0.0192 | 0.0709 |
| mean | 0.2608 | 0.6686 |

## GenEval (one black cat and one white dog)

| Seed | plain | SynGen |
|---|---|---|
| 9 | fail: 'expected dog>=1, found 0' (found {'cat': [0.948, 0.853, 0.804]}) | pass (found {'cat': [0.965], 'dog': [0.972, 0.969], 'potted plant': [0.35]}) |
| 10 | pass (found {'cat': [0.972], 'dog': [0.979]}) | fail: 'expected white dog>=1, found 0 white; and 1 pink' (found {'cat': [0.969], 'dog': [0.96], 'couch': [0.859], 'bed': [0.686]}) |
| 11 | fail: 'expected black cat>=1, found 0 black; and 1 white; expected dog>=1, found 0' (found {'cat': [0.977, 0.97], 'dining table': [0.512]}) | pass (found {'cat': [0.981, 0.967], 'dog': [0.969], 'couch': [0.724, 0.31], 'potted plant': [0.392]}) |
| 12 | fail: 'expected dog>=1, found 0' (found {'cat': [0.978, 0.977]}) | fail: 'expected dog>=1, found 0' (found {'cat': [0.974, 0.97]}) |
| passes | 1 of 4 | 2 of 4 |

## Engagement checks (plan 09)

1. Code: passed. SynGen ran in `.venv/` on the toy by a background worker; the numbers above are the scorers' printed output.
2. Visualize: passed. The chart `artifacts/figures/batch-methods/syngen-seeds.svg` puts the plain and SynGen renders side by side on four seeds, with BLIP and GenEval verdicts and the means.
3. Compare: passed. Learner, looking at the SynGen render on seed 10: "seed 10 dog is white with pink paws, GenEval is wrong." GenEval's colour fail on that render is therefore a wrong fail: the dog is white and the detector's colour check read its pink paws.
   Two sentences: SynGen is a rival method, so it fills the SynGen row of the results table's Stable Diffusion 1.5 column, one cell per scorer, with the four scorers' numbers above. It brings a white dog back on seeds 9 and 11 (BLIP white dog 0.024 to 0.989 and 0.022 to 0.682), but seed 12 still has no dog, a third animal appears on two seeds, GenEval's colour check fails a correct white dog because of its paws, it needs a spaCy parse and was run with a three-line precision cast in its loss code, it runs only on Stable Diffusion 1.x, and four seeds show nothing about how often it works.

## Step 1.3: the edited prompt

Prompt "a white cat and a black dog", seed 9, SynGen on. Parse for both prompts: [[6, 7], [2, 3]], identical. Render `out/syngen_swapped_seed09.png`: a white cat and a black dog. Not scored. Learner: "the parse is the same pairs for both and the render has a white cat and a black dog".
Not yet read: the SynGen paper body on its limits. The sentences above make no claim about it.
