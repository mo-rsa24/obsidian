# Selective Evaluation: illustrated map

The drawn pictures for the vault note [[Selective Evaluation]]: the cut-off as a gate on one calibration set, and the fixed-sequence walk that picks it. `2 prompts · 2 rendered · 0 stuck · 0 rendering · 0 waiting`

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Glyph vocabulary](#glyph-vocabulary)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane](#subject-lane)
- [Prompt 1 (Subject): The gate on one calibration set](#prompt-1-subject-the-gate-on-one-calibration-set)
- [Prompt 2 (Subject): The fixed-sequence walk stops at 0.86](#prompt-2-subject-the-fixed-sequence-walk-stops-at-086)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[Chance-Corrected Agreement]]: the folder's map, which points to this note.
2. [[Selective Evaluation]]: two concept pictures. A vault note has no scope above it.

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

A thin cell is one calibration row sorted by confidence (primary tier). A vertical line across the strip is the cut-off. A step card is one cut-off tried, with its answered count, disagreements and bound.

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

On the strip, left to right is confidence falling from 1.0 to 0.5. On the walk, left to right is the cut-off falling and time passing.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Thin arrows between step cards in the walk picture, a dashed line for the tolerated rate, and a stop sign on the failing step. No step badges beyond the word "chosen".

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The gate on one calibration set](#prompt-1-subject-the-gate-on-one-calibration-set) ➡️

Concept pictures for sections the note's existing pictures do not cover, one per gap. Every judge outcome, confidence and count drawn is invented, and each picture says so on its face.

### Prompt 1 (Subject): The gate on one calibration set

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The fixed-sequence walk stops at 0.86](#prompt-2-subject-the-fixed-sequence-walk-stops-at-086) ➡️

[planned] 🖼️ rendered 2026-10-18, script-drawn by `sandbox/make_pictures.py`
Save as: `../Mathematics/Statistics/assets/selective-evaluation-the-gate-on-one-calibration-set.webp`

Visual thesis: One cut-off on confidence splits the calibration set: rows above it are answered by the judge and rows below it go to a person, and the cut-off is chosen so the answered rows keep a stated disagreement rate.

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

Scene: A banner: "Choosing the cut-off on one labelled calibration set". Under it the rule in a rounded card: "answer if confidence c is at least the cut-off, otherwise send to review".
The main element is one long horizontal strip of 105 cells sorted by confidence, highest on the left, lowest on the right, with the axis label "confidence c, from 1.0 down to 0.5" below it. A vertical gate line crosses the strip at the cut-off, labelled "cut-off 0.86". The 45 cells left of the gate are green, the 60 cells right of it are amber. Brackets above: over the green part "answered by the judge: 45 of 105, 0 disagree", over the amber part "sent to review: 60 of 105". A small caption under the strip: "coverage 0.429".
Under the strip a rounded card: "Promise: answered rows disagree with people at most 7% of the time, with a 10% chance of the promise being wrong. Bound on the answered rows: 0.050." A caption: "The strip is the 105-row set: 8 approved pages plus 97 planted copies." Footer chip: "Confidences and verdicts invented".

Cast: one banner, one rule card, one strip of 105 cells with one gate line and two brackets, one promise card, captions, one footer chip.

Flows: none.

Text in the image, spelled exactly: "Choosing the cut-off on one labelled calibration set", "answer if confidence c is at least the cut-off, otherwise send to review", "confidence c, from 1.0 down to 0.5", "cut-off 0.86", "answered by the judge: 45 of 105, 0 disagree", "sent to review: 60 of 105", "coverage 0.429", "Promise: answered rows disagree with people at most 7% of the time, with a 10% chance of the promise being wrong. Bound on the answered rows: 0.050.", "The strip is the 105-row set: 8 approved pages plus 97 planted copies.", "Confidences and verdicts invented"

Exclusions: no red, no cells other than 105, no curve, no ROC plot, no second gate line, no per-cell numbers. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The strip has 105 cells, 45 green and 60 amber, drawn in that proportion with the gate between them. Counted from the note's walk for the underconfident judge at the tolerated rate 0.07: last passing cut-off 0.86, answers 45 of 105 (coverage 0.429), 0 disagree, bound 0.050; 105 - 45 = 60 sent to review. The 7% is the tolerated rate alpha = 0.07 and the 10% is delta = 0.10, fixed in the script. Which of the 60 review rows would have disagreed is not in the note, so no cell in the amber part is marked as a disagreement. Every label in the image, exactly: the 10 strings in the Text list above.

### Prompt 2 (Subject): The fixed-sequence walk stops at 0.86

Navigation: ⬅️ [Prompt 1 (Subject): The gate on one calibration set](#prompt-1-subject-the-gate-on-one-calibration-set) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[planned] 🖼️ rendered 2026-10-18, script-drawn by `sandbox/make_pictures.py`
Save as: `../Mathematics/Statistics/assets/selective-evaluation-the-walk-stops-at-0-86.webp`

Visual thesis: The walk tries cut-offs from high to low, keeps going while the bound stays under 0.07, and stops at the first step that fails: 0.86 passes with a bound of 0.050 and 0.85 fails with 0.073.

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

Scene: A banner: "Walking the cut-off down until the bound passes 0.07". Four step cards in a row, left to right as the cut-off falls: "cut-off 0.90", "cut-off 0.89 to 0.87", "cut-off 0.86", "cut-off 0.85". Each card shows what the run gives:
Card 0.90: "37 answered, 0 disagree, bound 0.060", a green tick.
Card 0.89 to 0.87: three short lines, "38 answered, 0 disagree, bound 0.059", "40 answered, 0 disagree, bound 0.056", "43 answered, 0 disagree, bound 0.052", and a green tick.
Card 0.86: "45 answered, 0 disagree, bound 0.050", a green tick and the badge "chosen", and an amber chip "60 rows to review".
Card 0.85: "52 answered, 1 disagree, bound 0.073", a dark grey stop sign and the words "bound above 0.07: stop".
Below the cards, a bar chart aligned to the cards, one bar per step tried (six bars): vertical axis "bound on the disagreement rate" from 0 to 0.10, bars at 0.060, 0.059, 0.056, 0.052, 0.050 and 0.073 in that left-to-right order, with the middle three bars standing under the middle card, and a horizontal dashed line across the chart at 0.07 labelled "tolerated rate 0.07". The first five bars are green and sit under the line; the 0.073 bar is dark grey and crosses the line. A dashed outline to the right of card 0.85 reads "lower cut-offs are never tried". Footer chip: "Confidences and verdicts invented".

Cast: one banner, four step cards, six bars, one dashed line, one dashed outline, one footer chip.

Flows: thin neutral arrows from each card to the next, left to right, ending at the stop sign.

Text in the image, spelled exactly: "Walking the cut-off down until the bound passes 0.07", "cut-off 0.90", "cut-off 0.89 to 0.87", "cut-off 0.86", "cut-off 0.85", "37 answered, 0 disagree, bound 0.060", "38 answered, 0 disagree, bound 0.059", "40 answered, 0 disagree, bound 0.056", "43 answered, 0 disagree, bound 0.052", "45 answered, 0 disagree, bound 0.050", "chosen", "60 rows to review", "52 answered, 1 disagree, bound 0.073", "bound above 0.07: stop", "bound on the disagreement rate", "tolerated rate 0.07", "lower cut-offs are never tried", "0.060", "0.059", "0.056", "0.052", "0.050", "0.073", "Confidences and verdicts invented"

Exclusions: no red, no numbers other than those spelled in the text list, no curves, no more than four cards, no more than six bars. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Numbers are the note's alpha 0.07 run for the underconfident judge, from the saved walk output: first step at 0.90 answers 37 rows with 0 disagree and bound 0.060; last passing cut-off 0.86 answers 45 of 105 with 0 disagree and bound 0.050; the next step 0.85 answers 52 rows with 1 disagree and bound 0.073, above 0.07, so the walk stops. Cut-offs 0.89, 0.88 and 0.87 are the run's own steps: 38 answered with bound 0.059, 40 answered with bound 0.056, and 43 answered with bound 0.052, all with 0 disagree (`test-5-threshold-walk.out`, alpha 0.07 run, underconfident judge). The bar chart therefore has six bars, five green and one dark grey. 105 - 45 = 60 rows to review at 0.86. The single disagreement at 0.85 carries no verdict colour. Every label in the image, exactly: the 24 strings in the Text list above.

## Process lane

Navigation: ⬅️ [Prompt 2 (Subject): The fixed-sequence walk stops at 0.86](#prompt-2-subject-the-fixed-sequence-walk-stops-at-086) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
