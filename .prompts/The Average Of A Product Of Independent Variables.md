# The Average Of A Product Of Independent Variables: illustrated map

The drawn pictures for the vault note [[The Average Of A Product Of Independent Variables]]: the form, $\mathbb{E}[XY] = \mathbb{E}[X]\,\mathbb{E}[Y]$ as the two-dice table whose rows each total $x \times 21$, its mechanism as the joint table split into two single tables beside the same-die table that cannot split, and the deep-dive sheet that composes them with the die-and-coin example, the slip and the check. `3 prompts · 0 rendered · 0 stuck · 0 rendering · 3 waiting`

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Glyph vocabulary](#glyph-vocabulary)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane](#subject-lane)
- [Prompt 1 (Subject): The average of a product, the form](#prompt-1-subject-the-average-of-a-product-the-form)
- [Prompt 2 (Subject): The average of a product, the mechanism](#prompt-2-subject-the-average-of-a-product-the-mechanism)
- [Prompt 3 (Subject capstone): The average of a product, the deep-dive sheet](#prompt-3-subject-capstone-the-average-of-a-product-the-deep-dive-sheet)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[The Average Of A Product Of Independent Variables]]: the form, the mechanism and the deep-dive sheet. A vault note has no scope above it, so the chain is one link. The cross term this rule removes has its own pictures in the vault's `.prompts/Multivariate Normal Distribution.md`, prompts 13 and 14.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: nothing here needs a repeatable named look. Zoom depth: one level, the three pictures a vault section gets. The style paragraph is embedded verbatim at the head of every prompt.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. A die and a coin are the only real-world objects, and any plain six-sided die and plain coin drawing serves. The run pane of prompt 3 copies the text of `assets/average-of-a-product-dice-and-coin.png`, the rendered output of the sandbox, which may be attached for its layout.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Blue: the first quantity, $X$, its faces and its chances. Orange: the second quantity, $Y$, its faces and its chances. Red: a number produced by a slip, never a true value. Grey is structural only (grid lines, dividers, unlit cells of the same-die table). No other colour carries a meaning.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A square table cell holds one pair's product or chance (primary tier). A blue header is a face of $X$, an orange header a face of $Y$ (primary tier). A total chip at a row's right edge holds that row's sum (secondary tier). A red-bordered card is a slip and its wrong number (artifact tier).

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Down the side: the first die's face, 1 at the top to 6 at the bottom. Across the top: the second die's face, 1 at the left to 6 at the right. In prompt 2, left panel independent, right panel the same die twice.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Row-total chips, measurement chips, one multiply sign between the two single tables. No numbered markers, step badges or phase containers.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The average of a product, the form](#prompt-1-subject-the-average-of-a-product-the-form) ➡️

The three pictures for $\mathbb{E}[g(X)\,h(Y)] = \mathbb{E}[g(X)]\,\mathbb{E}[h(Y)]$ on two fair dice and a die with a coin. Every number drawn comes from the note's hand tables, its derivation or its sandbox output.

### Prompt 1 (Subject): The average of a product, the form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The average of a product, the mechanism](#prompt-2-subject-the-average-of-a-product-the-mechanism) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Statistics/assets/average-of-a-product-the-form.webp`

Visual thesis: In the table of two independent dice, every row is its face times the same row of 1 to 6, so the table's total is 21 times 21 and its average is 3.5 times 3.5.

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

Production: Use a deterministic figure script for the grid, every number and all typography. Compose for reading at 1000 px wide, 4:3 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "Two independent dice: E[XY] = E[X] E[Y]". At the top left corner of a 6 by 6 grid, a small blue die icon labelled "X" pointing down the side and a small orange die icon labelled "Y" pointing across the top. Orange headers across the top: "1", "2", "3", "4", "5", "6". Blue headers down the side: "1", "2", "3", "4", "5", "6". Each cell holds the product of its row header and column header:
row 1: 1, 2, 3, 4, 5, 6
row 2: 2, 4, 6, 8, 10, 12
row 3: 3, 6, 9, 12, 15, 18
row 4: 4, 8, 12, 16, 20, 24
row 5: 5, 10, 15, 20, 25, 30
row 6: 6, 12, 18, 24, 30, 36
A small grey caption above the grid: "each cell has chance 1/36". At the right edge of each row a total chip: "21 = 1 x 21", "42 = 2 x 21", "63 = 3 x 21", "84 = 4 x 21", "105 = 5 x 21", "126 = 6 x 21".
Under the grid, two cards side by side: "all 36 cells add to 441 = 21 x 21" and "E[XY] = 441/36 = 12.25 = 3.5 x 3.5".

Cast: two die icons, twelve headers (six blue, six orange), 36 cells, six row-total chips, one caption, two result cards.

Flows: none.

Text in the image, spelled exactly: "Two independent dice: E[XY] = E[X] E[Y]", "X", "Y", "each cell has chance 1/36", the 36 cell values and 12 header digits in the Scene, "21 = 1 x 21", "42 = 2 x 21", "63 = 3 x 21", "84 = 4 x 21", "105 = 5 x 21", "126 = 6 x 21", "all 36 cells add to 441 = 21 x 21", "E[XY] = 441/36 = 12.25 = 3.5 x 3.5"

Exclusions: no cell value other than its row header times its column header, no seventh row or column, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Every cell is its row header times its column header, and each row total is the row's face times 21; the six totals add to 441. These are the note's hand table and the sandbox's output lines 2 to 8 in [[The Average Of A Product Of Independent Variables#How the average of a product factors]]. Every label in the image, exactly: the strings in the Text list above, with the 36 cells and 12 headers written out in the Scene.

### Prompt 2 (Subject): The average of a product, the mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The average of a product, the form](#prompt-1-subject-the-average-of-a-product-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject capstone): The average of a product, the deep-dive sheet](#prompt-3-subject-capstone-the-average-of-a-product-the-deep-dive-sheet) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Statistics/assets/average-of-a-product-the-mechanism.webp`

Visual thesis: Independence makes every cell's chance a product of two single chances, so the joint table splits into two single tables; the same die read twice puts all its chance on the diagonal and cannot split.

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

Production: Use a deterministic figure script for both grids, every number and all typography. Compose for reading at 1000 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "Why the average splits, and when it cannot". Two panels side by side.
Left panel, titled "Independent: every chance is a product". A blue column of six cells, each "1/6", beside the blue faces "1" to "6", labelled "X alone"; a multiply sign "x"; an orange row of six cells, each "1/6", above the orange faces "1" to "6", labelled "Y alone"; an equals sign; a 6 by 6 grid, every cell "1/36", labelled "joint chances". Under the panel one line: "sum of x y (1/6)(1/6) = (sum of x / 6)(sum of y / 6) = 3.5 x 3.5 = 12.25".
Right panel, titled "Same die twice: Y = X". A 6 by 6 grid with blue headers "1" to "6" down the side and the same blue headers across the top. Only the six diagonal cells are lit, each "1/6"; the other 30 cells are grey and read "0". A chip pointing at the top-left diagonal cell: "1/6, not 1/36". Under the grid a red-bordered card: "E[X X] = 91/6 = 15.166667, not 12.25", and a grey line under it: "gap 35/12 = Var(X)".

Cast: one six-cell blue column, one six-cell orange row, one 36-cell joint grid, one 36-cell same-die grid with six lit cells, one chip, one red-bordered card, two footer lines.

Flows: none; the multiply and equals signs are plain glyphs.

Text in the image, spelled exactly: "Why the average splits, and when it cannot", "Independent: every chance is a product", "X alone", "Y alone", "joint chances", "1/6", "1/36", "x", "=", "1", "2", "3", "4", "5", "6", "sum of x y (1/6)(1/6) = (sum of x / 6)(sum of y / 6) = 3.5 x 3.5 = 12.25", "Same die twice: Y = X", "0", "1/6, not 1/36", "E[X X] = 91/6 = 15.166667, not 12.25", "gap 35/12 = Var(X)"

Exclusions: no lit cell off the diagonal in the right grid, no cell in the left grid other than "1/36", no orange in the right panel, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Left grid: 36 cells of $1/36 = (1/6)(1/6)$, which is independence (Chan, Definition 5.4). Right grid: six lit cells of $1/6$, which still add to 1, and 30 cells of 0; the right panel uses blue only, because $Y$ is the same quantity as $X$. Numbers from the note's "Where it goes wrong": $91/6 = 15.166667$, $3.5^2 = 12.25$, gap $35/12$. Every label in the image, exactly: the strings in the Text list above.

### Prompt 3 (Subject capstone): The average of a product, the deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The average of a product, the mechanism](#prompt-2-subject-the-average-of-a-product-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Statistics/assets/average-of-a-product-deep-dive-sheet.webp`

Visual thesis: One sheet holds the rule's form, the split of the double sum, the die-and-coin example with functions, the same-die slip and the run that checks every number by listing outcomes.

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

Production: Use a deterministic figure script for every row of values, terminal line and all typography. Compose as a portrait sheet for reading at 1000 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A sheet title across the top: "Independent X and Y: E[g(X) h(Y)] = E[g(X)] E[h(Y)]". Five rounded panes.
Pane 1, top left, titled "The form": a blue die icon "X", an orange die icon "Y", and the line "E[XY] = 3.5 x 3.5 = 12.25".
Pane 2, top right, titled "Why it splits": three short lines in monospace, "sum over x, y of g(x) h(y) pX(x) pY(y)", "= sum over x of g(x) pX(x) x E[h(Y)]", "= E[g(X)] E[h(Y)]".
Pane 3, middle, full width, titled "A die and a coin": a blue die icon "X" and an orange coin icon "Y = -1 or +1"; two rows of six values, the first labelled "y = -1: x^2 x 0.5" with "0.5, 2, 4.5, 8, 12.5, 18" and a chip "45.5", the second labelled "y = +1: x^2 x 2" with "2, 8, 18, 32, 50, 72" and a chip "182"; under them "227.5 / 12 = 18.958333 = 15.166667 x 1.25".
Pane 4, below, titled "The slip": one red-bordered card "Y = X: E[X X] = 15.166667, not 12.25" and a grey line "gap 35/12 = Var(X)".
Pane 5, bottom, full width, titled "The run": a light terminal card in monospace showing exactly these four lines:
"$ python3 product_of_averages.py"
"factored: E[X] = E[Y] = 7/2 = 3.5, E[X] E[Y] = 49/4 = 12.25"
"listed: 36 cells, each 1/36, products add to 441 = 21 x 21, E[XY] = 441/36 = 49/4 = 12.250000"
"listed: 12 outcomes, each 1/12, E[X^2 2^Y] = 227.5/12 = 455/24 = 18.958333"

Cast: two die icons and one coin icon, three derivation lines, two rows of six values with two chips and one result line, one red-bordered card with one grey line, one terminal card.

Flows: none.

Text in the image, spelled exactly: "Independent X and Y: E[g(X) h(Y)] = E[g(X)] E[h(Y)]", "The form", "X", "Y", "E[XY] = 3.5 x 3.5 = 12.25", "Why it splits", "sum over x, y of g(x) h(y) pX(x) pY(y)", "= sum over x of g(x) pX(x) x E[h(Y)]", "= E[g(X)] E[h(Y)]", "A die and a coin", "Y = -1 or +1", "y = -1: x^2 x 0.5", "0.5, 2, 4.5, 8, 12.5, 18", "45.5", "y = +1: x^2 x 2", "2, 8, 18, 32, 50, 72", "182", "227.5 / 12 = 18.958333 = 15.166667 x 1.25", "The slip", "Y = X: E[X X] = 15.166667, not 12.25", "gap 35/12 = Var(X)", "The run", the four terminal lines above

Exclusions: no terminal line other than the four given, no numbered markers, no card longer than its given text, no sixth pane, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Five panes, the deep-dive exception's maximum. The four terminal lines are the command and output lines 1, 8 and 12 of the note's sandbox, copied character for character from `assets/average-of-a-product-dice-and-coin.png`. Pane 3's rows add to 45.5 and 182, and $227.5/12 = 18.958333 = (91/6)(5/4)$. Red marks only the slip number 15.166667. Every label in the image, exactly: the strings in the Text list above, with the four terminal lines written out in the Scene.

## Process lane

Navigation: ⬅️ [Prompt 3 (Subject capstone): The average of a product, the deep-dive sheet](#prompt-3-subject-capstone-the-average-of-a-product-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
