# Maclaurin Series: illustrated map

The drawn pictures for the vault note [[Maclaurin Series]]: its form, its mechanism, and the deep-dive sheet that composes them with the `series.py` run. `3 prompts · 0 rendered · 3 waiting`

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Glyph vocabulary](#glyph-vocabulary)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane](#subject-lane)
- [Prompt 1 (Subject): Maclaurin series, the form](#prompt-1-subject-maclaurin-series-the-form)
- [Prompt 2 (Subject): Maclaurin series, the mechanism](#prompt-2-subject-maclaurin-series-the-mechanism)
- [Prompt 3 (Subject capstone): Maclaurin series, the deep-dive sheet](#prompt-3-subject-capstone-maclaurin-series-the-deep-dive-sheet)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[Maclaurin Series]]: the series' form, mechanism and deep-dive sheet. A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: nothing here needs a repeatable named look. Zoom depth: one level, the three pictures a vault note gets. The style paragraph is embedded verbatim at the head of every prompt.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. Nothing in these pictures is a real-world object or a real product. The run pane of prompt 3 copies seven lines of `../Mathematics/Calculus/Sequences And Series/assets/maclaurin-series-the-four-series-run.png`, which may be attached for its layout.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Blue: the series for $e^x$ and its partial sums. Teal: $e^{-x}$'s terms. Green: the cosh series, the average of blue and teal. Purple: $\log(1 + y)$ and the composed $\log\cosh$ series. Red: a slip (no factorial, the cosine's signs, the dropped square term). Grey is structural only (axes, leader lines, dividers). No other colour carries a meaning.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A term card holds one term of a series with its value (primary tier). A step over $k$ is one partial sum (primary tier). An operation card holds one line of algebra (artifact tier). A dashed horizontal line is a true value a series is aiming at.

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Left to right: the term index $k$ grows, and each added term moves the sum closer to the true value. Top to bottom in the mechanism: one series feeds the next.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Numbered markers in prompt 3's run pane, matching the note's field table. Dashed target lines. No step badges or phase containers.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): Maclaurin series, the form](#prompt-1-subject-maclaurin-series-the-form) ➡️

The three pictures for the series. Every number drawn comes from the note's worked examples or its `series.py` and `checks.py` outputs.

### Prompt 1 (Subject): Maclaurin series, the form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): Maclaurin series, the mechanism](#prompt-2-subject-maclaurin-series-the-mechanism) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Calculus/Sequences And Series/assets/maclaurin-series-the-form.webp`

Visual thesis: A Maclaurin series is a row of terms, each the k-th rate of change at 0 over k factorial times x to the k, and for e to the 0.5 the partial sums climb to 1.648721 while the slip without factorials overshoots.

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

Production: Use a deterministic figure script for both step plots, the axes and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "A function as an endless sum". Two panels left to right.
Panel 1, titled "The form": one operation card holding the line "f(x) = f(0) + f'(0) x + f''(0)/2! x^2 + ... + f^(k)(0)/k! x^k + ..." in monospace. Three short grey leader labels point at parts of its last term: at "f^(k)(0)" the label "k-th rate of change at 0", at "k!" the label "divide by k factorial", at "x^k" the label "the k-th power". Under the card one chip: "stop after x^n: the partial sum". Under the chip a second blue card: "e^x = 1 + x + x^2/2! + x^3/3! + ...".
Panel 2, titled "e^0.5, term by term": a plot with horizontal axis "k" (ticks 0, 1, 2, 3, 4, 5) and vertical axis from 0.9 to 1.75 (ticks 1.0, 1.2, 1.4, 1.6). A blue staircase of partial sums at k = 0 to 5 with heights 1.000000, 1.500000, 1.625000, 1.645833, 1.648438, 1.648698; the last step labelled "1.648698". A grey dashed horizontal line at 1.648721 labelled "e^0.5 = 1.648721". A red staircase for the slip at heights 1.000000, 1.500000, 1.625000, 1.666667, 1.682292, 1.688542, matching blue for k = 0 to 2 and rising above the dashed line from k = 3; its last step labelled "x^k / k, no factorial: 1.688542".

Cast: two operation cards with three leader labels and one chip, one plot with two staircases, one dashed target line.

Flows: none; leader lines only.

Text in the image, spelled exactly: "A function as an endless sum", "The form", "f(x) = f(0) + f'(0) x + f''(0)/2! x^2 + ... + f^(k)(0)/k! x^k + ...", "k-th rate of change at 0", "divide by k factorial", "the k-th power", "stop after x^n: the partial sum", "e^x = 1 + x + x^2/2! + x^3/3! + ...", "e^0.5, term by term", "k", "0", "1", "2", "3", "4", "5", "1.0", "1.2", "1.4", "1.6", "1.648698", "e^0.5 = 1.648721", "x^k / k, no factorial: 1.688542"

Exclusions: no smooth curve in place of the staircases, no third staircase, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The blue steps sit at 1.000000, 1.500000, 1.625000, 1.645833, 1.648438, 1.648698, all below the dashed line at 1.648721, the last one visibly touching it at this scale; the red steps match blue for k = 0, 1, 2 (1, 1.5, 1.625) and then sit above the dashed line at 1.666667, 1.682292, 1.688542. Numbers from the note's [[Maclaurin Series#e^x worked at x = 0.5]] table and markers 1 to 3 of the `series.py` run; the red heights recomputed with Python as $1 + \sum_{k=1}^{K} 0.5^k/k$. Every label in the image, exactly: the 23 strings in the Text list above.

### Prompt 2 (Subject): Maclaurin series, the mechanism

Navigation: ⬅️ [Prompt 1 (Subject): Maclaurin series, the form](#prompt-1-subject-maclaurin-series-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject capstone): Maclaurin series, the deep-dive sheet](#prompt-3-subject-capstone-maclaurin-series-the-deep-dive-sheet) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Calculus/Sequences And Series/assets/maclaurin-series-the-mechanism.webp`

Visual thesis: Averaging the e to the x and e to the minus x term rows cancels every odd term and leaves the cosh series, and putting cosh minus 1 into log of 1 plus y turns the plus x to the fourth over 24 into minus x to the fourth over 12 through the minus y squared over 2 term.

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

Production: Use a deterministic figure script for the term rows, cards and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "Cancel, then compose". Two stacked bands.
Band 1, titled "cosh: the odd terms cancel": three rows of five small term cards, columns headed "k = 0" to "k = 4". Blue row labelled "e^0.5": "+1", "+0.5", "+0.125", "+0.020833", "+0.002604". Teal row labelled "e^-0.5": "+1", "-0.5", "+0.125", "-0.020833", "+0.002604". Green row labelled "average": "1", "0", "0.125", "0", "0.002604", with the two "0" cards drawn pale grey and struck through. At the right end of the green row a green chip: "cosh 0.5 = 1.12762587 through x^6".
Band 2, titled "log cosh: put y into log(1 + y)": four operation cards left to right joined by grey arrows. Card 1 (green): "y = x^2/2 + x^4/24 + ...". Card 2 (purple): "log(1 + y) = y - y^2/2 + ...". Card 3 (purple): "y^2/2 = x^4/8 + ...". Card 4 (purple, bold border): "x^2/2 + x^4/24 - x^4/8 = x^2/2 - x^4/12". Under card 4 a purple chip "at x = 0.3: 0.04432500, true 0.04434077" and beside it a red chip "drop -y^2/2: 0.04533750".

Cast: fifteen term cards in three rows, one green chip, four operation cards, three arrows, one purple chip, one red chip.

Flows: three grey arrows from card 1 to card 2 to card 3 to card 4.

Text in the image, spelled exactly: "Cancel, then compose", "cosh: the odd terms cancel", "k = 0", "k = 1", "k = 2", "k = 3", "k = 4", "e^0.5", "e^-0.5", "average", "+1", "+0.5", "+0.125", "+0.020833", "+0.002604", "-0.5", "-0.020833", "1", "0", "0.125", "0.002604", "cosh 0.5 = 1.12762587 through x^6", "log cosh: put y into log(1 + y)", "y = x^2/2 + x^4/24 + ...", "log(1 + y) = y - y^2/2 + ...", "y^2/2 = x^4/8 + ...", "x^2/2 + x^4/24 - x^4/8 = x^2/2 - x^4/12", "at x = 0.3: 0.04432500, true 0.04434077", "drop -y^2/2: 0.04533750"

Exclusions: no odd-power card in the green row with a value other than 0, no sixth column, no plot, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The three rows are the `checks.py` table at k = 0 to 4 (the note's [[Maclaurin Series#cosh worked at x = 0.5]]); the green row's odd entries are 0 and its even entries equal the blue ones. Band 2's algebra is the four-line composition in [[Maclaurin Series#log(1 + y) worked at y = 0.2, and log cosh at x = 0.3]], and the chips are markers 9 to 11 of the `series.py` run. Every label in the image, exactly: the 29 strings in the Text list above.

### Prompt 3 (Subject capstone): Maclaurin series, the deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): Maclaurin series, the mechanism](#prompt-2-subject-maclaurin-series-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Calculus/Sequences And Series/assets/maclaurin-series-deep-dive-sheet.webp`

Visual thesis: One sheet holds the series' form, the cancel-then-compose mechanism, the run that checks e to the 0.5, cosh 0.5 and log cosh 0.3, and the two slips beside their true values.

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

Production: Use a deterministic figure script for every staircase, terminal line and all typography. Compose as a portrait sheet for reading at 1000 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A sheet title across the top: "f(x) = sum of f^(k)(0)/k! x^k". Five rounded panes.
Pane 1, top left, titled "The form": the card "f(x) = f(0) + f'(0) x + f''(0)/2! x^2 + ..." and a small blue staircase over "k" from 0 to 5 climbing to "1.648698" under a dashed line "e^0.5 = 1.648721".
Pane 2, top right, titled "Cancel, then compose": three short term rows "e^0.5: +1 +0.5 +0.125", "e^-0.5: +1 -0.5 +0.125", "average: 1 0 0.125" in blue, teal and green, and under them the purple line "x^2/2 + x^4/24 - x^4/8 = x^2/2 - x^4/12".
Pane 3, middle, full width, titled "The run": a light terminal card in monospace showing exactly these eight lines:
"$ python3 series.py"
"  k = 5: term 0.000260  sum 1.648698"
"  math.exp(0.5) = 1.648721"
"  slip, x^k / k with no factorial: 1.688542"
"  through x^6: 1.12762587"
"  math.cosh(0.5) = 1.12762597"
"  x^2/2 - x^4/12           = 0.04432500"
"  math.log(math.cosh(0.3)) = 0.04434077"
with six small numbered orange markers placed just above: 1 over "sum 1.648698", 2 over "1.648721", 3 over "1.688542", 4 over "1.12762587", 5 over "1.12762597", 6 over "0.04432500".
Pane 4, below the run, titled "Reading the run": six small cards in a grid, numbered 1 to 6 to match the markers, each with exactly this text:
1 "six terms of e^x at 0.5"
2 "the true value: 0.000023 above"
3 "no factorial: too high"
4 "four even terms of cosh"
5 "true cosh: 0.0000001 above"
6 "x^2/2 - x^4/12 at 0.3"
Pane 5, bottom, full width, titled "Two slips": a red card "cos signs: 1 - x^2/2 + x^4/24 = 0.87760417" with the chip "below 1: cosh never is", and a red card "drop -y^2/2: 0.04533750" with the chip "63 times the right answer's miss".

Cast: one card and one small staircase, three term rows and one composed line, one terminal card with six markers, six reading cards, two red slip cards with two chips.

Flows: none; markers and cards are matched by number.

Text in the image, spelled exactly: "f(x) = sum of f^(k)(0)/k! x^k", "The form", "f(x) = f(0) + f'(0) x + f''(0)/2! x^2 + ...", "k", "1.648698", "e^0.5 = 1.648721", "Cancel, then compose", "e^0.5: +1 +0.5 +0.125", "e^-0.5: +1 -0.5 +0.125", "average: 1 0 0.125", "x^2/2 + x^4/24 - x^4/8 = x^2/2 - x^4/12", "The run", the eight terminal lines above, the markers "1" to "6", "Reading the run", the six card texts above, "Two slips", "cos signs: 1 - x^2/2 + x^4/24 = 0.87760417", "below 1: cosh never is", "drop -y^2/2: 0.04533750", "63 times the right answer's miss"

Exclusions: no terminal line other than the eight given, no marker over the wrong field, no card longer than its given text, no sixth pane, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Five panes, the deep-dive exception's maximum. The seven output lines are copied character for character from the `series.py` run (`assets/maclaurin-series-the-four-series-run.png`), with their leading spaces; the sheet's markers 1 to 6 sit over the fields the note's markers 1, 2, 3, 4, 5 and 9 mark. The cards match the note's reading table rows run 1 to 5 and run 9; "0.000023" is $1.648721 - 1.648698$ and "0.0000001" is $1.12762597 - 1.12762587$ rounded; "63 times" is $0.000997 / 0.0000158$. Every label in the image, exactly: the strings in the Text list above, with the eight terminal lines and six card texts written out in the Scene.

## Process lane

Navigation: ⬅️ [Prompt 3 (Subject capstone): Maclaurin series, the deep-dive sheet](#prompt-3-subject-capstone-maclaurin-series-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note has no plan tree to draw over it.
