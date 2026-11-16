# Plan 12 notes (instruction 2.1)

Working run: CONFORM with Attend-and-Excite printed OK (both SD 1.5, 512, seed 9, "a cat and a dog").
Broken run: our adapter with CONFORM printed REFUSED (model SDXL vs SD 1.5; resolution 1024 vs 512), although both rows hold numbers (CLIP 0.3025 and 0.2844).
Learner's reading: "the runner refuses the adapter vs CONFORM pair".

# Engagement check 2 (visualize)
Picture: artifacts/figures/runner-and-table/runner-and-table.svg in the journey folder.
Learner's reading: "plain SDXL is the fused animal and GenEval passes it wrongly".

# Engagement checks (plan 12)
1. Code: passed. runner.py wrote table.md from records.json; 14 numbers matched their source table files.
2. Visualize: passed on the learner's reading ("plain SDXL is the fused animal and GenEval passes it wrongly").
3. Compare: passed, the learner accepted the draft ("done"): the runner fills no single cell, it makes every cell comparable by attaching model, prompt, seed and resolution to each row and refusing rows that differ; it cannot see whether a scorer's number is right (GenEval's false pass on the fused animal went into the table) or what a gap means, since each row is one prompt and one seed.
