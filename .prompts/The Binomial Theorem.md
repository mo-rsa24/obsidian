# The Binomial Theorem: illustrated map

The drawn pictures for the vault note [[The Binomial Theorem]]: the form of $(a + b)^n$ as picks sorted into piles, its mechanism as the 2 by 2 box and Pascal's triangle, and the deep-dive sheet that composes them with the sandbox run, the slip and the checks. `3 prompts · 0 rendered · 0 stuck · 0 rendering · 3 waiting`

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Glyph vocabulary](#glyph-vocabulary)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane](#subject-lane)
- [Prompt 1 (Subject): The binomial theorem, the form](#prompt-1-subject-the-binomial-theorem-the-form)
- [Prompt 2 (Subject): The binomial theorem, the mechanism](#prompt-2-subject-the-binomial-theorem-the-mechanism)
- [Prompt 3 (Subject capstone): The binomial theorem, the deep-dive sheet](#prompt-3-subject-capstone-the-binomial-theorem-the-deep-dive-sheet)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[The Binomial Theorem]]: the form, the mechanism and the deep-dive sheet. A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: nothing here needs a repeatable named look. Zoom depth: one level, the three pictures a vault section gets. The style paragraph is embedded verbatim at the head of every prompt.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. There is no real-world object. The run pane of prompt 3 copies the text of `assets/binomial-theorem-worked-and-checked.png`, the rendered output of the sandbox, which may be attached for its layout.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Blue: a pick of the first number, $a = 2$. Orange: a pick of the second number, $b = 3$. Red: a number produced by a slip, never a true value. Grey is structural only (brackets, dividers, the lines joining a Pascal entry to its parents). No other colour carries a meaning.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A small rounded tile is one bracket's pick, blue "2" or orange "3" (primary tier). A strip of four tiles is one full pick across four brackets (primary tier). A pile is a group of strips with the same number of orange tiles, with a label card under it (secondary tier). A box cell holds one product of the 2 by 2 multiplication (secondary tier). A red-bordered card is a slip and its wrong number (artifact tier).

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Left to right: the number of orange tiles in a pick grows from 0 to 4. In prompt 2, Pascal's triangle reads top to bottom, row 0 to row 5.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Pile label cards, parent lines in the triangle, measurement chips. No numbered markers, step badges or phase containers.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The binomial theorem, the form](#prompt-1-subject-the-binomial-theorem-the-form) ➡️

The three pictures for $(a + b)^n$ on $(2 + 3)^4$. Every number drawn comes from the note's hand table, its derivation or its sandbox output.

### Prompt 1 (Subject): The binomial theorem, the form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The binomial theorem, the mechanism](#prompt-2-subject-the-binomial-theorem-the-mechanism) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Algebra/assets/binomial-theorem-the-form.webp`

Visual thesis: Multiplying out (2 + 3)^4 makes 16 picks, and sorting them by how many 3s they took gives piles of 1, 4, 6, 4 and 1, the binomial coefficients.

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

Production: Use a deterministic figure script for every tile, strip, pile and all typography. Compose for reading at 1000 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "(2 + 3)^4: 16 picks, sorted by how many 3s". Under it, a row of four grey bracket cards, each holding "(2 + 3)", labelled "bracket 1" to "bracket 4".
Below, five piles side by side, left to right, each a vertical stack of strips; a strip is four small rounded tiles in a row, one per bracket, blue tiles reading "2" and orange tiles reading "3".
Pile 1: one strip, 2 2 2 2.
Pile 2: four strips, 3 2 2 2 / 2 3 2 2 / 2 2 3 2 / 2 2 2 3.
Pile 3: six strips, 3 3 2 2 / 3 2 3 2 / 3 2 2 3 / 2 3 3 2 / 2 3 2 3 / 2 2 3 3.
Pile 4: four strips, 3 3 3 2 / 3 3 2 3 / 3 2 3 3 / 2 3 3 3.
Pile 5: one strip, 3 3 3 3.
Under each pile a label card with two lines: "0 threes: C(4, 0) = 1" and "1 x 2^4 = 16"; "1 three: C(4, 1) = 4" and "4 x 2^3 x 3 = 96"; "2 threes: C(4, 2) = 6" and "6 x 2^2 x 3^2 = 216"; "3 threes: C(4, 3) = 4" and "4 x 2 x 3^3 = 216"; "4 threes: C(4, 4) = 1" and "1 x 3^4 = 81".
Across the bottom, one wide card: "16 + 96 + 216 + 216 + 81 = 625 = 5^4".

Cast: four bracket cards, sixteen strips of four tiles (64 tiles), five pile label cards, one sum card.

Flows: none.

Text in the image, spelled exactly: "(2 + 3)^4: 16 picks, sorted by how many 3s", "(2 + 3)", "bracket 1", "bracket 2", "bracket 3", "bracket 4", "2", "3", "0 threes: C(4, 0) = 1", "1 x 2^4 = 16", "1 three: C(4, 1) = 4", "4 x 2^3 x 3 = 96", "2 threes: C(4, 2) = 6", "6 x 2^2 x 3^2 = 216", "3 threes: C(4, 3) = 4", "4 x 2 x 3^3 = 216", "4 threes: C(4, 4) = 1", "1 x 3^4 = 81", "16 + 96 + 216 + 216 + 81 = 625 = 5^4"

Exclusions: no strip repeated, no strip with a tile count other than four, no pile holding a strip with the wrong number of orange tiles, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Exactly 16 strips, all different, each of four tiles, so 64 tiles: 32 blue and 32 orange in all (pile by pile, orange tiles 0, 4, 12, 12, 4). Pile sizes 1, 4, 6, 4, 1 match $\binom{4}{k}$ and add to $16 = 2^4$. The pile products match the note's hand table in [[The Binomial Theorem#How the binomial theorem works]]: 16, 96, 216, 216, 81, adding to 625. Every label in the image, exactly: the 19 strings in the Text list above.

### Prompt 2 (Subject): The binomial theorem, the mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The binomial theorem, the form](#prompt-1-subject-the-binomial-theorem-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject capstone): The binomial theorem, the deep-dive sheet](#prompt-3-subject-capstone-the-binomial-theorem-the-deep-dive-sheet) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Algebra/assets/binomial-theorem-the-mechanism.webp`

Visual thesis: The coefficient counts the mixed picks, which the 2 by 2 box shows for a square, and Pascal's triangle builds every count by adding the two counts above it.

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

Production: Use a deterministic figure script for the box, the triangle, every line and all typography. Compose for reading at 1000 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "Counting picks: the box and the triangle". Two panels side by side.
Left panel, titled "(2 + 3)^2 as a box": a 2 by 2 grid. Along the top edge, a blue header "2" over the left column and an orange header "3" over the right column; along the left edge, a blue header "2" beside the top row and an orange header "3" beside the bottom row. Cells: top left "4" (blue tint), top right "6" (orange-and-blue split tint), bottom left "6" (orange-and-blue split tint), bottom right "9" (orange tint). Under the grid a neutral card "4 + 6 + 6 + 9 = 25", a chip pointing at the two split cells "mixed picks: 6 + 6 = 12 = 2ab", and a red-bordered card "slip: 4 + 9 = 13".
Right panel, titled "Pascal's triangle": six centred rows, labelled at the left "row 0" to "row 5": "1"; "1 1"; "1 2 1"; "1 3 3 1"; "1 4 6 4 1"; "1 5 10 10 5 1". Every entry below row 0 that is not at a row's end has two thin grey lines up to the two entries above it. Row 4's middle entry "6" and its two parents "3" and "3" are ringed, with a chip "3 + 3 = 6". Row 5 is on a light tinted band with a chip at its right "(x + 1)^5 = x^5 + 5x^4 + 10x^3 + 10x^2 + 5x + 1". At the right of each row a small grey chip with the row's total: "1", "2", "4", "8", "16", "32".

Cast: one 2 by 2 box with four headers, one sum card, one mixed-picks chip, one slip card, one six-row triangle with its parent lines, one ringed trio with its chip, one row-5 band with its expansion chip, six row-total chips.

Flows: the parent lines in the triangle only.

Text in the image, spelled exactly: "Counting picks: the box and the triangle", "(2 + 3)^2 as a box", "2", "3", "4", "6", "9", "4 + 6 + 6 + 9 = 25", "mixed picks: 6 + 6 = 12 = 2ab", "slip: 4 + 9 = 13", "Pascal's triangle", "row 0", "row 1", "row 2", "row 3", "row 4", "row 5", "1", "5", "10", "3 + 3 = 6", "(x + 1)^5 = x^5 + 5x^4 + 10x^3 + 10x^2 + 5x + 1", "8", "16", "32"

Exclusions: no third row in the box, no triangle row beyond row 5, no parent line to an entry that is not directly above-left or above-right, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The box cells are the products of their headers: $2 \times 2 = 4$, $2 \times 3 = 6$, $3 \times 2 = 6$, $3 \times 3 = 9$, adding to $25 = 5^2$; the diagonal alone is 13 (the note's "Where it goes wrong"). Every triangle entry equals the sum of its two parents, and row 5 is $1, 5, 10, 10, 5, 1$, the sandbox's output line 11. The row totals are $2^r$: 1, 2, 4, 8, 16, 32. Every label in the image, exactly: the strings in the Text list above, each digit string used wherever the Scene places it.

### Prompt 3 (Subject capstone): The binomial theorem, the deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The binomial theorem, the mechanism](#prompt-2-subject-the-binomial-theorem-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Algebra/assets/binomial-theorem-deep-dive-sheet.webp`

Visual thesis: One sheet holds the theorem's form, why each coefficient counts picks, the run that adds the terms of (2 + 3)^4 to 625, the slips with their wrong numbers, and the probability check that adds to 1.

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

Production: Use a deterministic figure script for every tile, terminal line and all typography. Compose as a portrait sheet for reading at 1000 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A sheet title across the top: "(a + b)^n = sum of C(n, k) a^(n - k) b^k". Five rounded panes.
Pane 1, top left, titled "The form": the line "C(n, k) * a^(n - k) * b^k" in monospace, with three chips under its three parts: "how many picks", "a's power counts down", "b's power counts up".
Pane 2, top right, titled "Why: count the picks": five small piles of four-tile strips (blue "2", orange "3") with 1, 4, 6, 4 and 1 strips, under them "1 + 4 + 6 + 4 + 1 = 16 = 2^4".
Pane 3, middle, full width, titled "The run": a light terminal card in monospace showing exactly these seven lines:
"$ python3 binomial.py"
"k = 0: C(4, 0) = 1, 2^4 = 16, 3^0 = 1, term 16"
"k = 1: C(4, 1) = 4, 2^3 = 8, 3^1 = 3, term 96"
"k = 2: C(4, 2) = 6, 2^2 = 4, 3^2 = 9, term 216"
"k = 3: C(4, 3) = 4, 2^1 = 2, 3^3 = 27, term 216"
"k = 4: C(4, 4) = 1, 2^0 = 1, 3^4 = 81, term 81"
"the terms add to 625; (2 + 3)^4 = 5^4 = 625"
Pane 4, below the run, titled "Three slips": three red-bordered cards side by side, each with exactly this text:
"no coefficients: 2^2 + 3^2 = 13, truth 25"
"a^n + b^n: 2^4 + 3^4 = 97, truth 625"
"144 printed for 216: x = 1 gives -71, truth 1"
Pane 5, bottom, full width, titled "The check: chances add to 1": four chips in a row, "k = 0: 0.421875", "k = 1: 0.421875", "k = 2: 0.140625", "k = 3: 0.015625", and at the right a card "sum = 1 = (0.25 + 0.75)^3".

Cast: one formula with three chips, five piles of strips with a sum line, one terminal card, three red-bordered slip cards, four probability chips with one sum card.

Flows: none.

Text in the image, spelled exactly: "(a + b)^n = sum of C(n, k) a^(n - k) b^k", "The form", "C(n, k) * a^(n - k) * b^k", "how many picks", "a's power counts down", "b's power counts up", "Why: count the picks", "2", "3", "1 + 4 + 6 + 4 + 1 = 16 = 2^4", "The run", the seven terminal lines above, "Three slips", the three slip card texts above, "The check: chances add to 1", "k = 0: 0.421875", "k = 1: 0.421875", "k = 2: 0.140625", "k = 3: 0.015625", "sum = 1 = (0.25 + 0.75)^3"

Exclusions: no terminal line other than the seven given, no numbered markers, no card longer than its given text, no sixth pane, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Five panes, the deep-dive exception's maximum. The seven terminal lines are the command and output lines 1 to 6 of the note's sandbox, copied character for character from `assets/binomial-theorem-worked-and-checked.png`. Pane 2's piles hold 1, 4, 6, 4, 1 strips. Red marks only the slip numbers 13, 97 and -71. Pane 5's four numbers are output line 18 and add to 1. Every label in the image, exactly: the strings in the Text list above, with the seven terminal lines and three slip card texts written out in the Scene.

## Process lane

Navigation: ⬅️ [Prompt 3 (Subject capstone): The binomial theorem, the deep-dive sheet](#prompt-3-subject-capstone-the-binomial-theorem-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
