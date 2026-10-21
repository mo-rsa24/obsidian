# Variance: illustrated map

The drawn pictures for the vault note [[The Scaling Rule For Variance]], section [[The Scaling Rule For Variance#Scaling a draw scales its variance by the square]]: its form, its mechanism, and the deep-dive sheet that composes them with step 6's run. `3 prompts · 1 rendered · 2 replaced by code-drawn SVGs · 0 stuck · 0 rendering · 0 waiting`

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Glyph vocabulary](#glyph-vocabulary)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane](#subject-lane)
- [Prompt 1 (Subject): The scaling rule, the form](#prompt-1-subject-the-scaling-rule-the-form)
- [Prompt 2 (Subject): The scaling rule, the mechanism](#prompt-2-subject-the-scaling-rule-the-mechanism)
- [Prompt 3 (Subject capstone): The scaling rule, the deep-dive sheet](#prompt-3-subject-capstone-the-scaling-rule-the-deep-dive-sheet)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[The Scaling Rule For Variance]]: the scaling rule's form, mechanism and deep-dive sheet. A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: nothing here needs a repeatable named look. Zoom depth: one level, the three pictures a vault section gets. The style paragraph is embedded verbatim at the head of every prompt.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. Nothing in these pictures is a real-world object or a real product. The run pane of prompt 3 copies the text of `assets/variance-a-scaled-standard-normal-draw.png`, the rendered output of step 6, which may be attached for its layout.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Blue: the draw before scaling, $X$ or $\varepsilon$, with variance 1. Orange: the same draw after it is multiplied by $c$. Grey is structural only (axes, brackets, dividers). No other colour carries a meaning.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A bell curve is a distribution (primary tier). A dot on a number line is one face of the coin (primary tier). A square drawn on a miss is that miss squared, its side the miss and its area the squared miss (secondary tier). An operation card holds the one line that does the scaling (artifact tier).

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Left to right: before scaling, the scaling, after scaling. In prompt 2, top row before, bottom row after.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Numbered markers in prompt 3's run pane, matching the note's field table. Measurement brackets. No step badges or phase containers.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The scaling rule, the form](#prompt-1-subject-the-scaling-rule-the-form) ➡️

The three pictures for the scaling rule. Every number drawn comes from the note's own derivation or its step 6 output.

### Prompt 1 (Subject): The scaling rule, the form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The scaling rule, the mechanism](#prompt-2-subject-the-scaling-rule-the-mechanism) ➡️

[built] 🔁 replaced 2026-10-21 by the code-drawn `../Mathematics/Statistics/assets/scaling-rule-the-unit-bell-stretched-by-c.svg`, because this faithfulness note needs exact widths and bracket ends (per VAULT_NOTE_FORMAT.md, Pictures); the drain had stopped at: pixel check after 3 revisions, orange bell 0.801 of the blue bell's half-height width (needs 0.7223), blue sd bracket ends at 1.16 and orange at 0.62 (need 1 and 0.7223); last attempt ~/.cache/codex-drop/obsidian/variance-the-form.png
Save as: `../Mathematics/Statistics/assets/variance-the-form.webp`

Visual thesis: Multiplying a draw by c multiplies its standard deviation by |c| and its variance by c squared, so a wanted variance v needs c = sqrt(v).

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

Production: Use a deterministic figure script for both bell curves, the axes and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "Scaling a draw by c". Three panels left to right. Panel 1: a blue bell curve, the standard normal N(0, 1), on a horizontal axis from -3 to 3 with ticks at -3, -2, -1, 0, 1, 2, 3, its peak over 0. Above it the label "eps ~ N(0, 1)". A grey horizontal bracket from 0 to 1 at about 60 percent of the bell's height, labelled "sd 1", and under the bell the chip "variance 1". Panel 2: an operation card holding the line "Y = c * eps" in monospace, with a chip under it "c = 0.7223". Panel 3: an orange bell curve on the same axis and the same horizontal scale as panel 1, its peak over 0, exactly 0.7223 times as wide as the blue bell and 1 / 0.7223 = 1.384 times as tall, so its area stays the same. Above it the label "Y ~ N(0, 0.5217)". A grey bracket from 0 to 0.7223 at the same relative height, labelled "sd 0.7223", and under the bell the chip "variance 0.5217". Beneath all three panels, one strip of two rule cards side by side: "sd x |c|" and "variance x c squared". Under the strip, one line: "want variance v? use c = sqrt(v)".

Cast: two bell curves (blue, orange), one operation card, one c chip, two brackets, two variance chips, two rule cards, one footer line.

Flows: one short arrow from panel 1 into the operation card, one short arrow from the operation card into panel 3. No other connectors.

Text in the image, spelled exactly: "Scaling a draw by c", "eps ~ N(0, 1)", "sd 1", "variance 1", "Y = c * eps", "c = 0.7223", "Y ~ N(0, 0.5217)", "sd 0.7223", "variance 0.5217", "sd x |c|", "variance x c squared", "want variance v? use c = sqrt(v)", "-3", "-2", "-1", "0", "1", "2", "3"

Exclusions: no bracket labelled with a variance, no orange bell wider than the blue one, no third bell, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The orange bell's width at half its height is 0.7223 times the blue bell's (blue about 2.355 axis units, orange about 1.701), and its peak is 1.384 times as tall; both peak over 0 on one shared axis from -3 to 3. The blue bracket spans 0 to 1 and the orange bracket 0 to 0.7223 on that axis; brackets are labelled standard deviations, never variances. Blue is the draw before scaling, orange after. Numbers checked against the note: $0.7223^2 = 0.5217$ ([[The Scaling Rule For Variance#How the scaling rule works]]). Every label in the image, exactly: the 19 strings in the Text list above.

### Prompt 2 (Subject): The scaling rule, the mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The scaling rule, the form](#prompt-1-subject-the-scaling-rule-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject capstone): The scaling rule, the deep-dive sheet](#prompt-3-subject-capstone-the-scaling-rule-the-deep-dive-sheet) ➡️

[built] 🖼️ rendered 2026-10-20: `variance-the-mechanism.webp`
Save as: `../Mathematics/Statistics/assets/variance-the-mechanism.webp`

Visual thesis: Each miss from the mean is multiplied by c, so the square drawn on it has its area multiplied by c squared, and the average of those areas is the variance.

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

Production: Use a deterministic figure script for both number lines, every dot and square, and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel. Both rows share one horizontal scale, so equal numbers have equal lengths.

Scene: A title across the top: "Scaling a miss scales its square". Two rows, one above the other, each a horizontal number line from -1.5 to 1.5 with a grey tick and the label "mean 0" at 0.
Top row, titled "the coin": two blue dots at -1 and +1, each with a small coin icon above it and the labels "-1" and "+1". From 0 to each dot, a blue bar labelled "miss 1". Standing on each bar, a light blue square with side exactly 1 axis unit, labelled inside "1". At the right end of the row a card: "average: variance 1".
Bottom row, titled "the coin times c": two orange dots at -0.7223 and +0.7223 with the labels "-0.7223" and "+0.7223". From 0 to each dot, an orange bar labelled "miss 0.7223". Standing on each bar, a light orange square with side exactly 0.7223 axis units, labelled inside "0.5217". At the right end of the row a card: "average: variance 0.5217".
Between the rows, on the left, a grey down-arrow chip "x c = 0.7223" pointing from the top bars to the bottom bars, and on the right a grey down-arrow chip "x c squared = 0.5217" pointing from the top squares to the bottom squares.

Cast: two number lines, four dots (two blue, two orange), four miss bars, four squares, two variance cards, two scaling chips.

Flows: the two grey down-arrow chips only.

Text in the image, spelled exactly: "Scaling a miss scales its square", "the coin", "the coin times c", "mean 0", "-1", "+1", "-0.7223", "+0.7223", "miss 1", "miss 0.7223", "1", "0.5217", "average: variance 1", "average: variance 0.5217", "x c = 0.7223", "x c squared = 0.5217"

Exclusions: no square whose side differs from its miss bar, no bell curves, no third row, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Both rows share one scale. Top squares have side 1 axis unit, bottom squares side 0.7223, so each bottom square's area is 0.5217 of a top square's, measurable in pixels. Dots sit at -1, +1 (top) and -0.7223, +0.7223 (bottom). "1" labels the top squares' area and "0.5217" the bottom squares'; the bars are labelled as misses, never as variances. Numbers counted from the note's step 4 output (`squared misses [1.0, 1.0] variance 1.0` and `squared misses [0.5217, 0.5217] variance 0.5217`). Every label in the image, exactly: the 16 strings in the Text list above.

### Prompt 3 (Subject capstone): The scaling rule, the deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The scaling rule, the mechanism](#prompt-2-subject-the-scaling-rule-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[built] 🔁 replaced 2026-10-21 by the code-drawn `../Mathematics/Statistics/assets/scaling-rule-the-unit-bell-stretched-by-c.svg` (pane 1), `scaling-rule-one-miss-scaled-by-c.svg` (pane 2) and `scaling-rule-200000-scaled-draws.svg` beside the rendered `variance-a-scaled-standard-normal-draw.png` (panes 3 and 4), because this faithfulness note needs exact ratios (orange bell 0.7223 of the blue, square side 0.7223); pane 5's formula is in the note's text. The drain had stopped at: pane 1 pixel check after 3 revisions, both sd brackets end near 0.9 on the shared axis (need 1 and 0.7223) and the bells' half-height widths miss 2.355 and 1.701; panes 2 to 5 pass; last attempt ~/.cache/codex-drop/obsidian/variance-deep-dive-sheet.png
Save as: `../Mathematics/Statistics/assets/variance-deep-dive-sheet.webp`

Visual thesis: One sheet holds the rule's form, why it works on one miss, the run that confirms it on 200,000 draws, and where the forward process uses it.

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

Production: Use a deterministic figure script for every curve, square, terminal line and all typography. Compose as a portrait sheet for reading at 1000 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A sheet title across the top: "Var(cX) = c squared Var(X)". Five rounded panes.
Pane 1, top left, titled "The form": the blue bell "eps ~ N(0, 1)" with bracket "sd 1" and the orange bell "Y = c * eps" with bracket "sd 0.7223", on one shared axis, the orange bell 0.7223 times as wide; chips "variance 1" and "variance 0.5217".
Pane 2, top right, titled "Why: one miss": one blue bar "miss 1" with its square "1", an arrow chip "x c", one orange bar "miss 0.7223" with its square "0.5217", and the line "each square grows by c squared".
Pane 3, middle, full width, titled "The run: 200,000 draws": a light terminal card in monospace showing exactly these five lines:
"$ python3 scaled_normal.py"
"eps itself:    mean +0.0033  variance 0.997925"
"c = +0.72230: mean +0.0024  variance 0.520635  ratio 0.521717  c squared 0.521717  sd 0.72155  |c| 0.72230"
"c = -0.72230: mean -0.0024  variance 0.520635  ratio 0.521717  c squared 0.521717  sd 0.72155  |c| 0.72230"
"c = +0.02512: mean +0.0001  variance 0.000630  ratio 0.000631  c squared 0.000631  sd 0.02509  |c| 0.02512"
with seven small numbered orange markers placed just above: 1 over "variance 0.997925", 2 over the first "variance 0.520635", 3 over the first "ratio 0.521717", 4 over the first "c squared 0.521717", 5 over the first "sd 0.72155", 6 over "c = -0.72230", 7 over "ratio 0.000631".
Pane 4, below the run, titled "Reading the run": seven small cards in a grid, numbered 1 to 7 to match the markers, each with exactly this text:
1 "eps variance near 1: 0.66 standard errors low"
2 "scaled variance: c squared times eps's"
3 "ratio: exactly c squared, draw by draw"
4 "c squared matches the ratio"
5 "sd shrinks by |c|, not c squared"
6 "negative c: same variance, sign erased"
7 "0.000631 is beta_0, the noise at t = 0"
Pane 5, bottom, full width, titled "Where it is used": the formula "x_t = sqrt(abar_t) x_0 + sqrt(1 - abar_t) eps" with an orange chip under its second term: "sqrt(1 - 0.4783) = 0.7223, variance 0.5217".

Cast: two bells, two brackets, two miss bars with squares, one terminal card with seven markers, seven reading cards, one formula with one chip.

Flows: the single "x c" arrow chip in pane 2 only.

Text in the image, spelled exactly: "Var(cX) = c squared Var(X)", "The form", "eps ~ N(0, 1)", "sd 1", "Y = c * eps", "sd 0.7223", "variance 1", "variance 0.5217", "Why: one miss", "miss 1", "1", "x c", "miss 0.7223", "0.5217", "each square grows by c squared", "The run: 200,000 draws", the five terminal lines above, the markers "1" to "7", "Reading the run", the seven card texts above, "Where it is used", "x_t = sqrt(abar_t) x_0 + sqrt(1 - abar_t) eps", "sqrt(1 - 0.4783) = 0.7223, variance 0.5217"

Exclusions: no terminal line other than the five given, no marker over the wrong field, no card longer than its given text, no sixth pane, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Five panes, the deep-dive exception's maximum. The terminal lines are copied character for character from the note's step 6 output and its rendered picture `assets/variance-a-scaled-standard-normal-draw.png`; the seven markers sit over the same fields as that picture's markers 1 to 7. Pane 1's orange bell is 0.7223 times the blue bell's width; pane 2's orange square has side 0.7223 of the blue square's. The seven cards each stay under 20 words and match the note's step 6 field table: 0.66 standard errors, ratio equal to $c^2$, sd times $|c|$, sign erased, $\beta_0 = 0.000631$. Pane 5's numbers: $\bar\alpha_{50} = 0.4783$, $\sqrt{0.5217} = 0.7223$. Every label in the image, exactly: the strings in the Text list above, with the five terminal lines and seven card texts written out in the Scene.

## Process lane

Navigation: ⬅️ [Prompt 3 (Subject capstone): The scaling rule, the deep-dive sheet](#prompt-3-subject-capstone-the-scaling-rule-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
