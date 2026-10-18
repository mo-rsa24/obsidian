# Abstention In Agreement Scores: illustrated map

The drawn picture for the vault note [[Abstention In Agreement Scores]]: the three scoring rules on one table, with the bound on full-set accuracy. `1 prompts · 1 rendered · 0 stuck · 0 rendering · 0 waiting`

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Glyph vocabulary](#glyph-vocabulary)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane](#subject-lane)
- [Prompt 1 (Subject): One table of 105 decisions, scored three ways](#prompt-1-subject-one-table-of-105-decisions-scored-three-ways)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[Chance-Corrected Agreement]]: the folder's map.
2. [[Abstention In Agreement Scores]]: one concept picture. A vault note has no scope above it.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: no subject here needs a repeatable named look across the set. Zoom depth: one level, a concept picture per gap. The style paragraph is embedded verbatim at the head of every prompt.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. Nothing in these pictures is a real-world object or a real product.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Green: a verdict the reviewer would also give. Red: a wrong pass, where the judge passes and the reviewer would stop the product. Amber: a wrong fail, or a row sent to review. Blue and grey are structural only (axes, groups, which rows are good or bad pages) and never carry a verdict. Nothing else is coloured with these three.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A table cell is a count of rows, coloured by the verdict outcome (primary tier). A wide bar on a number line is a bound, and a mark on it is one score.

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Left to right: the counts, the rule applied, the score it gives. Top to bottom: the three rules in the note's order. The number line at the bottom runs from low to high accuracy.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Three thin arrows from the source table. No step badges or containers.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): One table of 105 decisions, scored three ways](#prompt-1-subject-one-table-of-105-decisions-scored-three-ways) ➡️

Concept pictures for sections the note's existing pictures do not cover, one per gap. Every judge outcome, confidence and count drawn is invented, and each picture says so on its face.

### Prompt 1 (Subject): One table of 105 decisions, scored three ways

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[planned] 🖼️ rendered 2026-10-18, script-drawn by `sandbox/make_pictures.py`
Save as: `../Mathematics/Statistics/Chance-Corrected Agreement/assets/one-table-three-scores.webp`

Visual thesis: The same 105 decisions score 0.963, 0.962 or 0.733 depending on what a review verdict counts as, and the accuracy over all rows is only known to lie in [0.733, 0.971].

```
Style: no named house style is imposed, but the result is a clean, welcoming UI-grade picture
and never a wireframe. Every component gets an icon, an emoji or a small illustration of what it
actually is; a real product carries its official logo only where the component is that product;
a physical thing (a RAM stick, a building, a server rack, a phone) is drawn as the real object,
not a labelled box. Cards and panels are rounded, with a thin coloured border, a soft drop shadow
and a lightly tinted background that tells groups apart; grey is kept for secondary text,
dividers and things that are off or inactive. Light background, generous spacing, a clear type
hierarchy. Any colour the prompt names a meaning for keeps that meaning alone. Beyond that, let
the composition and visual treatment that best communicate this subject emerge from the context
below, rather than from an imposed convention.

Production: Use a deterministic figure script for every square, bar, axis and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: Top left, a counts table with row headers "reviewer: good" (total 8) and "reviewer: bad" (total 97) and column headers "judge passes" (total 10), "judge fails" (total 70), "judge sends to review" (total 25), grand total 105. Cells: good and passes 7 (green), good and fails 0 (amber, pale), good and review 1 (amber), bad and passes 3 (red), bad and fails 70 (green), bad and review 24 (amber).
Right of it, three smaller copies of the same table stacked, each headed by a rule, with the same six counts, recoloured and with the score beside it:
Rule 1 "Drop the review rows": the review column greyed out and crossed; beside it "80 rows, accuracy 0.963, kappa 0.803".
Rule 2 "Count review as fail": the 24 bad and review cell turns green, the 1 good and review cell stays amber; beside it "105 rows, accuracy 0.962, kappa 0.757".
Rule 3 "Keep review as its own label": both review cells amber; beside it "105 rows, accuracy 0.733, kappa 0.292".
Along the bottom a horizontal number line from 0.70 to 1.00. A wide bar spans 0.733 to 0.971, labelled "Accuracy over all 105 rows lies in [0.733, 0.971]". Three marks on the line: 0.733 labelled "0.733 keep review", 0.962 labelled "0.962 count as fail", 0.963 labelled "0.963 drop". A footer chip: "All judge verdicts invented".

Cast: one source table, three recoloured tables with score labels, one number line with one bar and three marks, one footer chip.

Flows: three thin neutral arrows from the source table, one to each rule's table.

Text in the image, spelled exactly: "reviewer: good", "reviewer: bad", "judge passes", "judge fails", "judge sends to review", "7", "0", "1", "3", "70", "24", "8", "97", "10", "25", "105", "Drop the review rows", "Count review as fail", "Keep review as its own label", "80 rows, accuracy 0.963, kappa 0.803", "105 rows, accuracy 0.962, kappa 0.757", "105 rows, accuracy 0.733, kappa 0.292", "Accuracy over all 105 rows lies in [0.733, 0.971]", "0.733 keep review", "0.962 count as fail", "0.963 drop", "0.70", "1.00", "All judge verdicts invented"

Exclusions: no fourth rule, no pie charts, no confidence-interval wording, no error bars, no curves. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Counts are the note's table, counted from assets/abstention-output.txt: good (7 passed, 0 failed, 1 review), bad (3 passed, 70 failed, 24 review), totals 8, 97, 10, 70, 25, 105. Scores from the same file: exclusion 80 rows, accuracy 0.963, kappa 0.803; recoding 105 rows, 0.962, 0.757; three-class 105 rows, 0.733, 0.292. The bar runs from 0.733 to 0.971 (equation 10, coverage 0.762) and is drawn as a bound, never as a confidence interval. Under rule 2 the 24 bad and review cell is green and the 1 good and review cell amber; under rule 3 both are amber. Every label in the image, exactly: the 29 strings in the Text list above.

## Process lane

Navigation: ⬅️ [Prompt 1 (Subject): One table of 105 decisions, scored three ways](#prompt-1-subject-one-table-of-105-decisions-scored-three-ways) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
