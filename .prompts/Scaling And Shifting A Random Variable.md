# Scaling And Shifting A Random Variable: illustrated map

The drawn pictures for the vault note [[Scaling And Shifting A Random Variable]]: the form of $Y = aX + b$, its mechanism on a fair die, and the deep-dive sheet that composes them with the sandbox run and the slips. `3 prompts · 0 rendered · 0 stuck · 0 rendering · 3 waiting`

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Glyph vocabulary](#glyph-vocabulary)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane](#subject-lane)
- [Prompt 1 (Subject): Scaling and shifting, the form](#prompt-1-subject-scaling-and-shifting-the-form)
- [Prompt 2 (Subject): Scaling and shifting, the mechanism](#prompt-2-subject-scaling-and-shifting-the-mechanism)
- [Prompt 3 (Subject capstone): Scaling and shifting, the deep-dive sheet](#prompt-3-subject-capstone-scaling-and-shifting-the-deep-dive-sheet)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[Scaling And Shifting A Random Variable]]: the form, the mechanism and the deep-dive sheet. A vault note has no scope above it, so the chain is one link. The scale half alone has its own three pictures in the vault's `.prompts/Variance.md`.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: nothing here needs a repeatable named look. Zoom depth: one level, the three pictures a vault section gets. The style paragraph is embedded verbatim at the head of every prompt.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. A die face icon is the only real-world object, and any plain six-sided die drawing serves. The run pane of prompt 3 copies the text of `assets/scale-and-shift-a-fair-die.png`, the rendered output of the sandbox, which may be attached for its layout.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Blue: the die before the change, $X$. Orange: the same die after it, $Y = 2X + 1$. Red: a number produced by a slip, never a true value. Grey is structural only (axes, ticks, brackets, dividers, the mean markers' outlines). No other colour carries a meaning.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A vertical stem on a number line is one face with its probability, all six stems the same height (primary tier). A small grey triangle under the axis is the mean, the balance point (primary tier). A horizontal bar from the mean to a face is that face's miss (secondary tier). An operation card holds the one line that does the change (artifact tier). A red-bordered card is a slip and its wrong number (artifact tier).

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Left to right: before the change, the change, after the change. In prompt 2, top row before, bottom row after, on one shared axis.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Mean markers, miss bars and their labels. Measurement chips. No numbered markers, step badges or phase containers.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): Scaling and shifting, the form](#prompt-1-subject-scaling-and-shifting-the-form) ➡️

The three pictures for $Y = aX + b$ on a fair die. Every number drawn comes from the note's hand table, its derivation or its sandbox output.

### Prompt 1 (Subject): Scaling and shifting, the form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): Scaling and shifting, the mechanism](#prompt-2-subject-scaling-and-shifting-the-mechanism) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Statistics/assets/scale-and-shift-the-form.webp`

Visual thesis: The mean of 2X + 1 goes through both the times 2 and the plus 1, while the spread goes through only the times 2.

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

Production: Use a deterministic figure script for both number lines, every stem and marker, and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "Y = aX + b: scale, then shift". Two number lines stacked, each running from 0 to 14 with grey ticks and labels at 0, 2, 4, 6, 8, 10, 12, 14, sharing one horizontal scale.
Top line, labelled at its left "X, a fair die" with a small die icon: six blue stems of equal height at 1, 2, 3, 4, 5, 6, the first one labelled "1/6" at its top. A grey triangle under the axis at 3.5 labelled "mean 3.5". To the right of the stems, two blue chips: "variance 35/12 = 2.9167" and "sd 1.7078".
Between the lines, centred, an operation card holding "Y = 2X + 1" in monospace, with two chips beside it: "x 2 stretches" and "+ 1 slides".
Bottom line, labelled at its left "Y = 2X + 1": six orange stems of the same height at 3, 5, 7, 9, 11, 13. A grey triangle under the axis at 8 labelled "mean 8". To the right of the stems, two orange chips: "variance 35/3 = 11.6667" and "sd 3.4157".
Beneath both lines, one strip of three rule cards side by side: "mean: 2 x 3.5 + 1 = 8", "variance: 2 squared x 35/12; the + 1 drops out", "sd: |2| x 1.7078 = 3.4157".

Cast: two number lines, twelve stems (six blue, six orange), two mean triangles, one die icon, one operation card, two operation chips, four measurement chips, three rule cards.

Flows: one short grey arrow from the top line's mean triangle down through the operation card to the bottom line's mean triangle. No other connectors.

Text in the image, spelled exactly: "Y = aX + b: scale, then shift", "X, a fair die", "1/6", "mean 3.5", "variance 35/12 = 2.9167", "sd 1.7078", "Y = 2X + 1", "x 2 stretches", "+ 1 slides", "mean 8", "variance 35/3 = 11.6667", "sd 3.4157", "mean: 2 x 3.5 + 1 = 8", "variance: 2 squared x 35/12; the + 1 drops out", "sd: |2| x 1.7078 = 3.4157", "0", "2", "4", "6", "8", "10", "12", "14"

Exclusions: no stem at a value other than those listed, no stems of different heights, no bell curves, no third number line, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Both number lines share one scale from 0 to 14. Blue stems at 1 to 6, one unit apart, spanning 5 units; orange stems at 3, 5, 7, 9, 11, 13, two units apart, spanning 10 units, exactly twice the blue span, measurable in pixels. All twelve stems are the same height. The mean triangles sit at 3.5 and 8. Numbers checked against the note's hand table and sandbox output: $2 \times 3.5 + 1 = 8$, $4 \times 35/12 = 35/3 = 11.6667$, $\sqrt{35/12} = 1.7078$, $2 \times 1.7078 = 3.4157$ ([[Scaling And Shifting A Random Variable#How scaling and shifting work]]). Every label in the image, exactly: the 23 strings in the Text list above.

### Prompt 2 (Subject): Scaling and shifting, the mechanism

Navigation: ⬅️ [Prompt 1 (Subject): Scaling and shifting, the form](#prompt-1-subject-scaling-and-shifting-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject capstone): Scaling and shifting, the deep-dive sheet](#prompt-3-subject-capstone-scaling-and-shifting-the-deep-dive-sheet) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Statistics/assets/scale-and-shift-the-mechanism.webp`

Visual thesis: Every miss from the mean doubles, so every squared miss grows by 4, and the plus 1 moves the faces and the mean together so no miss changes.

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

Production: Use a deterministic figure script for both number lines, every dot and bar, and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel. Both rows share one horizontal scale from 0 to 14, so equal numbers have equal lengths.

Scene: A title across the top: "The misses double; the shift cancels". Two rows, one above the other, each a horizontal number line from 0 to 14.
Top row, titled "X, the die": six blue dots at 1, 2, 3, 4, 5, 6 and a grey tick labelled "mean 3.5" at 3.5. From the tick to each dot, a blue bar, stacked at slightly different heights so none overlaps, labelled "-2.5", "-1.5", "-0.5", "+0.5", "+1.5", "+2.5" from left to right. At the right end of the row a card: "squared misses add to 17.5; / 6 = 2.9167".
Bottom row, titled "Y = 2X + 1": six orange dots at 3, 5, 7, 9, 11, 13 and a grey tick labelled "mean 8" at 8. From the tick to each dot, an orange bar, stacked the same way, labelled "-5", "-3", "-1", "+1", "+3", "+5" from left to right. At the right end of the row a card: "squared misses add to 70; / 6 = 11.6667".
Between the rows, on the left, a grey down-arrow chip "x 2: every miss doubles"; on the right, a grey down-arrow chip "x 4: every squared miss". Under the bottom row, one grey line: "+ 1 moves every face and the mean together, so it cancels from every miss".

Cast: two number lines, twelve dots (six blue, six orange), two mean ticks, twelve miss bars, two sum cards, two scaling chips, one footer line.

Flows: the two grey down-arrow chips only.

Text in the image, spelled exactly: "The misses double; the shift cancels", "X, the die", "Y = 2X + 1", "mean 3.5", "mean 8", "-2.5", "-1.5", "-0.5", "+0.5", "+1.5", "+2.5", "-5", "-3", "-1", "+1", "+3", "+5", "squared misses add to 17.5; / 6 = 2.9167", "squared misses add to 70; / 6 = 11.6667", "x 2: every miss doubles", "x 4: every squared miss", "+ 1 moves every face and the mean together, so it cancels from every miss"

Exclusions: no bar whose length differs from its label, no squares drawn on the bars, no bell curves, no third row, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Both rows share one scale. Each orange bar is exactly twice the length of the blue bar in the same position (5 against 2.5, 3 against 1.5, 1 against 0.5), measurable in pixels, and each bar starts at its row's mean tick (3.5 top, 8 bottom). The sums are the note's hand table: $6.25 + 2.25 + 0.25 + 0.25 + 2.25 + 6.25 = 17.5$ and $25 + 9 + 1 + 1 + 9 + 25 = 70$ ([[Scaling And Shifting A Random Variable#How scaling and shifting work]]). Every label in the image, exactly: the 22 strings in the Text list above.

### Prompt 3 (Subject capstone): Scaling and shifting, the deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): Scaling and shifting, the mechanism](#prompt-2-subject-scaling-and-shifting-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Statistics/assets/scale-and-shift-deep-dive-sheet.webp`

Visual thesis: One sheet holds the rule's form, why the shift cancels and the scale squares, the run that confirms it face by face, the three slips with their wrong numbers, and where the forward process uses it.

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

Production: Use a deterministic figure script for every stem, bar, terminal line and all typography. Compose as a portrait sheet for reading at 1000 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A sheet title across the top: "E[aX + b] = a E[X] + b, Var(aX + b) = a squared Var(X)". Five rounded panes.
Pane 1, top left, titled "The form": six blue stems at 1 to 6 with a grey mean triangle "mean 3.5", an operation card "Y = 2X + 1", and six orange stems at 3, 5, 7, 9, 11, 13 with a grey mean triangle "mean 8", on one shared axis from 0 to 14.
Pane 2, top right, titled "Why: the misses": one blue bar "-2.5" from 3.5 to 1, an arrow chip "x 2", one orange bar "-5" from 8 to 3, and the two lines "every squared miss grows by 4" and "the + 1 cancels from every miss".
Pane 3, middle, full width, titled "The run": a light terminal card in monospace showing exactly these six lines:
"$ python3 scale_shift.py"
"X: mean 3.5, variance 35/12 = 2.9167"
"Y = 2X + 1 face by face: values [3, 5, 7, 9, 11, 13], mean 8.0, variance 35/3 = 11.6667, sd 3.4157"
"by the rules: mean a*3.5 + b = 8.0, variance a^2 * 35/12 = 11.6667, sd |a| * sqrt(35/12) = 3.4157"
"slip, a in place of a^2: 5.8333; slip, b added to the variance: 12.6667"
"Z = -2X + 1: mean -6.0, variance 11.6667, sd 3.4157 (|a| = 2, not -2)"
Pane 4, below the run, titled "Three slips": three red-bordered cards side by side, each with exactly this text:
"a in place of a squared: 5.8333, truth 11.6667"
"b added to the variance: 12.6667, truth 11.6667"
"sign kept: sd -3.4157 cannot exist, truth 3.4157"
Pane 5, bottom, full width, titled "Where it is used": the formula "x_t = sqrt(abar_t) x_0 + sqrt(1 - abar_t) eps" with an orange chip under its second term, "a = sqrt(1 - 0.4783) = 0.7223, variance 0.5217", a grey chip under its first term, "b = sqrt(0.4783) x_0, no variance", and one red-bordered card at the right, "a = 0.5217 by mistake: variance 0.2722".

Cast: twelve stems with two mean triangles and one operation card, two miss bars with one arrow chip, one terminal card, four red-bordered slip cards, one formula with two chips.

Flows: the single "x 2" arrow chip in pane 2 only.

Text in the image, spelled exactly: "E[aX + b] = a E[X] + b, Var(aX + b) = a squared Var(X)", "The form", "mean 3.5", "Y = 2X + 1", "mean 8", "Why: the misses", "-2.5", "x 2", "-5", "every squared miss grows by 4", "the + 1 cancels from every miss", "The run", the six terminal lines above, "Three slips", the three slip card texts above, "Where it is used", "x_t = sqrt(abar_t) x_0 + sqrt(1 - abar_t) eps", "a = sqrt(1 - 0.4783) = 0.7223, variance 0.5217", "b = sqrt(0.4783) x_0, no variance", "a = 0.5217 by mistake: variance 0.2722"

Exclusions: no terminal line other than the six given, no numbered markers, no card longer than its given text, no sixth pane, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Five panes, the deep-dive exception's maximum. The six terminal lines are the command and the first five output lines of the note's sandbox, copied character for character from `assets/scale-and-shift-a-fair-die.png`; the sixth output line (the ladder) is too long for the card and its three numbers appear in pane 5 instead. Pane 1's orange stems span twice the blue span on one shared axis; pane 2's orange bar is twice the blue bar's length. Red marks only the four slip numbers 5.8333, 12.6667, -3.4157 and 0.2722. Pane 5's numbers: $\bar\alpha_{50} = 0.4783$, $\sqrt{0.5217} = 0.7223$, $0.5217^2 = 0.2722$. Every label in the image, exactly: the strings in the Text list above, with the six terminal lines and three slip card texts written out in the Scene.

## Process lane

Navigation: ⬅️ [Prompt 3 (Subject capstone): Scaling and shifting, the deep-dive sheet](#prompt-3-subject-capstone-scaling-and-shifting-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
