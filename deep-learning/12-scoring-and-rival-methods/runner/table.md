# Results table: one prompt, one seed, scorers as columns

Every row carries the settings it ran under. A row whose prompt differs from its table's is flagged. Unmeasured cells say so.

## SDXL table (model SDXL, prompt "a cat and a dog", seed 9, resolution 1024)

| Method | CLIP cosine | ImageReward | BLIP dog yes | GenEval | Settings | Source |
|---|---|---|---|---|---|---|
| plain PoE (fused) | 0.2482 | -1.0717 | 0.0140 | pass (false: one animal boxed as cat and dog) | same | clip-score/table.md, imagereward/table.md, blip-vqa/table.md, geneval/table.md |
| our adapter (clear) | 0.3025 | +1.0691 | 0.6149 | pass | same | same four table files |
| joint prompt (reference) | 0.3021 | +0.8993 | 0.6335 | pass | same | same four table files |
| CO3 | to be measured | to be measured | to be measured | to be measured | same | not rendered yet: route step 8 |
| ToMe | to be measured | to be measured | to be measured | to be measured | same | not run: laptop too slow |

## SD 1.5 table (model SD 1.5, prompt "a cat and a dog", seed 9, resolution 512)

| Method | CLIP cosine | ImageReward | BLIP dog yes | GenEval | Settings | Source |
|---|---|---|---|---|---|---|
| plain SD 1.5 | 0.2380 | -0.2715 | 0.0568 | fail | same | attend-and-excite/table.md |
| Attend-and-Excite | 0.2884 | +0.8530 | 0.4243 | pass | same | attend-and-excite/table.md |
| CONFORM | 0.2844 | +0.9187 | 0.6589 | pass | same | conform/table.md |
| Divide and Bind | 0.2788 | +0.5514 | 0.8294 | pass | same | divide-and-bind/table.md |
| InitNO | 0.2666 | +0.3624 | 0.7595 | pass | same | initno/table.md |
| SynGen | 0.3433 | +1.4295 | 0.9891 | pass | DIFFERENT: prompt a black cat and a white dog | syngen/table.md (BLIP asks about a white dog) |
