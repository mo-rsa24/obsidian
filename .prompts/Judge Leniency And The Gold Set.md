# Judge Leniency And The Gold Set: illustrated map

The drawn pictures for the vault note [[Judge Leniency And The Gold Set]]: the plane that places judges by leniency. The pictures for the 105-row design are in the prompts file of [[The 105-Row Gold Set]]. `1 prompts · 1 rendered · 0 stuck · 0 rendering · 0 waiting`

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Glyph vocabulary](#glyph-vocabulary)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane](#subject-lane)
- [Prompt 1 (Subject): Judges placed on the P_c and P+ plane](#prompt-1-subject-judges-placed-on-the-pc-and-p-plane)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[Chance-Corrected Agreement]]: the folder's map.
2. [[Judge Leniency And The Gold Set]]: one concept picture. A vault note has no scope above it.

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

A dark-blue dot with a letter is one judge. A thin vertical line through a dot is the 90% range from resampling.

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

On the plane, right means more verdicts judged by the rubric and up means the guesses lean to pass. 

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

A whisker and tinted bands on the plane. No step badges or containers.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): Judges placed on the P_c and P+ plane](#prompt-1-subject-judges-placed-on-the-pc-and-p-plane) ➡️

Concept pictures for sections the note's existing pictures do not cover, one per gap. Every judge outcome, confidence and count drawn is invented, and each picture says so on its face.

### Prompt 1 (Subject): Judges placed on the P_c and P+ plane

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[planned] 🖼️ rendered 2026-10-18, script-drawn by `sandbox/make_pictures.py`
Save as: `../Mathematics/Statistics/Chance-Corrected Agreement/assets/judges-on-the-pc-and-pplus-plane.webp`

Visual thesis: Two numbers place a judge: how often it uses the rubric (P_c) and which way it guesses the rest (P+). Rubber stamp C and strict judge D sit in opposite corners, and judge A, from 20 products, could be anywhere on its vertical line.

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

Scene: One square plot fills most of the frame. Horizontal axis: "P_c: share of verdicts judged by the rubric", ticks 0, 0.5, 1. Vertical axis: "P+: share of the other verdicts that pass", ticks 0, 0.5, 1. Equal physical scale on both axes. The band above P+ 0.5 is tinted pale red with the small label "guesses lean to pass"; the band below is tinted pale amber with the label "guesses lean to fail". Plot four large dark-blue dots, each with its letter inside and a label beside it:
A at P_c 0.275, P+ 0.919, label "A  P_c 0.275, P+ 0.919".
B at P_c 0.333, P+ 1.000, label "B  P_c 0.333, P+ 1.000".
C at P_c 0.000, P+ 1.000, on the left edge at the top, label "C rubber stamp  P_c 0.000, P+ 1.000".
D at P_c 0.824, P+ 0.000, on the bottom edge, label "D strict  P_c 0.824, P+ 0.000".
Through dot A draw a thin vertical whisker from P+ 0 up to P+ 1 with the label "90% range from resampling the 20 products: 0 to 1". A footer chip: "All judge verdicts invented".

Cast: one square plot with two tinted bands, four dots, one whisker, one footer chip.

Flows: none.

Text in the image, spelled exactly: "P_c: share of verdicts judged by the rubric", "P+: share of the other verdicts that pass", "guesses lean to pass", "guesses lean to fail", "A  P_c 0.275, P+ 0.919", "B  P_c 0.333, P+ 1.000", "C rubber stamp  P_c 0.000, P+ 1.000", "D strict  P_c 0.824, P+ 0.000", "90% range from resampling the 20 products: 0 to 1", "All judge verdicts invented", "0", "0.5", "1"

Exclusions: no fifth dot, no curves, no diagonal lines, no 3D, no extra judges from the 105-row set, no green. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Dot positions are counted from the note's leniency table and its saved output (assets/leniency-output.txt): A (0.275, 0.919), B (0.333, 1.000), C (0.000, 1.000), D (0.824, 0.000), as (P_c, P+). C is on the left edge at the top and D on the bottom edge. The whisker through A runs from 0 to 1 because the bootstrap line reads 5%=0.00, 95%=1.00 (9,489 usable of 10,000). The pale red band means guesses that pass and the pale amber band guesses that fail; they are background tints, not verdicts. Every label in the image, exactly: the 13 strings in the Text list above.

## Process lane

Navigation: ⬅️ [Prompt 1 (Subject): Judges placed on the P_c and P+ plane](#prompt-1-subject-judges-placed-on-the-pc-and-p-plane) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
