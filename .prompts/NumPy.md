# NumPy: illustrated map

The drawn pictures for the notes in the vault's [[NumPy]] folder, sections [[Arrays Versus Python Lists]], [[Broadcasting]] and [[Random Numbers From A Seeded Generator]]. `9 prompts · 9 rendered · 0 waiting`

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Glyph vocabulary](#glyph-vocabulary)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane](#subject-lane)
- [Prompt 1 (Subject): The form](#prompt-1-subject-the-form)
- [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism)
- [Subject capstone: The deep-dive sheet](#subject-capstone-the-deep-dive-sheet)
- [Subject lane: Broadcasting](#subject-lane-broadcasting)
- [Prompt 4 (Subject): Broadcasting, the form](#prompt-4-subject-broadcasting-the-form)
- [Prompt 5 (Subject): Broadcasting, the mechanism](#prompt-5-subject-broadcasting-the-mechanism)
- [Prompt 6 (Subject capstone): Broadcasting, the deep-dive sheet](#prompt-6-subject-capstone-broadcasting-the-deep-dive-sheet)
- [Subject lane: Random numbers from a seeded generator](#subject-lane-random-numbers-from-a-seeded-generator)
- [Prompt 7 (Subject): Seeding, the form](#prompt-7-subject-seeding-the-form)
- [Prompt 8 (Subject): Seeding, the mechanism](#prompt-8-subject-seeding-the-mechanism)
- [Prompt 9 (Subject capstone): Seeding, the deep-dive sheet](#prompt-9-subject-capstone-seeding-the-deep-dive-sheet)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[NumPy]]: subjects "Arrays versus lists", "Broadcasting" and "Random numbers from a seeded generator", one sheet each. A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: no subject here needs a repeatable named look across the set. Zoom depth: one level, the section's form and mechanism, composed by the deep-dive sheet. The style paragraph is embedded verbatim at the head of every prompt.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. Nothing in these pictures is a real-world object or a real product.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Grey: a plain Python list. Green: a NumPy array. Red: an error, and numbered output markers. In the broadcasting lane, green marks a result shape and red the one column that fails. In the seeding lane, teal is the seeded generator and grey the hidden global generator.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A paper strip in square brackets is a Python list. A snug block of cells is a NumPy array. A red badge is an error. All primary tier. A shape box holds one axis length; a dashed box is an implied length of 1. A tape of number cells is a generator's stream, read by a head.

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Left to right: input, operation, result. Rows compare the list behaviour (top) with the array behaviour (bottom).

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Numbered markers only on the deep-dive sheet's output pane, matching the numbered fields in the note's output picture. No step badges or phase containers.

## Subject lane
<!-- student-read: 2026-10-04 job 20261004-193336-542c8e -->

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The form](#prompt-1-subject-the-form) ➡️

The form, the mechanism, then the deep-dive sheet that composes them with the run's output, per the vault-note exception in the illustration style guide.

### Prompt 1 (Subject): The form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism) ➡️

[planned] 🖼️ rendered 2026-10-04 numpy-arrays-the-form.webp
Save as: `../Software/Python/NumPy/assets/numpy-arrays-the-form.webp`

Visual thesis: np.array turns a list of numbers into an array of shape (2,) whose arithmetic acts on each entry.

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

Scene: Left: a plain Python list drawn as two numbers inside square brackets on a grey paper strip. Middle: a funnel-like step labelled with the call np.array. Right: a NumPy array drawn as two snug numbered cells in one block, with its shape tag. Below the array: one example operation, 1 / array, producing a second two-cell array. Reading direction: left to right, then down.

Cast: the list strip (grey), the np.array step (green), the array block (green border), the shape tag, the result array.

Flows: a green arrow from the list through np.array to the array; a green arrow from the array down to the result, with one thin line per cell showing each cell divided on its own.

Text in the image, spelled exactly: "[1.0, 4.0]", "Python list", "np.array(...)", "NumPy array", "shape (2,)", "1 / var", "[1.0, 0.25]".

Exclusions: no NumPy logo, no matrix, no third cell. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The array has exactly two cells holding 1.0 and 4.0; the result cells hold 1.0 and 0.25; each result cell connects only to the cell above it; green means an array, grey means a plain list.

### Prompt 2 (Subject): The mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The form](#prompt-1-subject-the-form) | 📋 [TOC](#table-of-contents) | [Subject capstone: The deep-dive sheet](#subject-capstone-the-deep-dive-sheet) ➡️

[planned] 🖼️ rendered 2026-10-04 numpy-arrays-the-mechanism.webp
Save as: `../Software/Python/NumPy/assets/numpy-arrays-the-mechanism.webp`

Visual thesis: The same + sign joins two lists end to end but adds corresponding entries of two arrays.

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

Scene: Two comparison rows and a shallow error footer. Make the corresponding-entry paths in the green array row the visual focus. All labels must remain readable when the whole picture is displayed at 800 px wide.

Top row, titled list + list: show [1, 4] and [4, 1] as continuous grey paper strips with square brackets and commas, separated by a plus sign. A short arrow labelled joins leads to one longer paper strip containing [1, 4, 4, 1]. Do not draw lists as individual cell tiles. Preserve a little extra space between the two original pairs in the result so the reader can see where the second list was appended, without changing the printed sequence.

Bottom row, titled array + array: show the two arrays as green two-cell blocks stacked vertically, [1, 4] above [4, 1]. Keep corresponding cells in the same vertical columns. Below them, put one small plus node in each column and a two-cell result block containing 5 and 5. Each plus node receives exactly two paths: one from the individual cell in the upper array and one from the corresponding individual cell in the lower array. Route the upper cell's path around the outside edge of its own column and the lower cell's path straight down. Keep paths separated and uncrossed. Each plus node sends one short arrow to its own result cell. Label the operation adds matching entries. Print [5 5] once beneath the result block.

Footer: show 1 / [1, 4] on a grey paper strip, followed by a short arrow ending at a red TypeError badge. Keep this smaller than the addition comparison but legible.

Cast: grey paper strips for lists, green cell blocks for arrays, small labelled addition nodes, a red error badge. Use these teaching objects as the component illustrations; avoid redundant header icons.

Flows: the list arrow carries the whole strip to the joined result. The array row has four separate input paths and two separate output paths. Every array input path begins at a specific cell, never at an enclosing array border.

Text in the image, spelled exactly: "list + list", "[1, 4]", "[4, 1]", "[1, 4, 4, 1]", "array + array", "[5 5]", "1 / [1, 4]", "TypeError", "joins", "adds matching entries". Cell values: upper array 1, 4; lower array 4, 1; result 5, 5. Compact legend: "list", "array", "error".

Exclusions: no NumPy logo, no other operators, no shared input bus, no paths starting from an entire array block, no list drawn as array cells, no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The list result has four entries in the order 1, 4, 4, 1; the array result has two entries, 5 and 5; the error row shows TypeError; grey means a list, green an array, red an error; values match the note's runs. Every label in the image: "list + list", "[1, 4]", "[4, 1]", "[1, 4, 4, 1]", "array + array", "[5 5]", "1 / [1, 4]", "TypeError", "joins", "adds matching entries", "list", "array", "error"; each array cell has its own path into its own plus node, and lists are paper strips, never cell tiles.

### Subject capstone: The deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism) | 📋 [TOC](#table-of-contents) | [Subject lane: Broadcasting](#subject-lane-broadcasting) ➡️

[planned] 🖼️ rendered 2026-10-04 numpy-arrays-deep-dive-sheet.webp
Save as: `../Software/Python/NumPy/assets/numpy-arrays-deep-dive-sheet.webp`

Visual thesis: Read the composed output one field at a time: shape, reciprocal variances, then the mean and variance before and after background removal.

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

Scene: Exactly four panes in a landscape sheet with enough height for readable output and six explanations. Use two compact reminder panes across the top and two larger panes below. The top reminders occupy about one third of the height. Give the lower run pane about three fifths of the width and the reading pane the remaining width. The output is the first place the eye lands. Test all text at a displayed width of 800 px; increase the sheet's height instead of shrinking the output type.

Pane 1, The form: a compact reminder of prompt 1. A grey paper strip [1.0, 4.0] passes through np.array(...) to a green two-cell array holding 1.0 and 4.0, tagged shape (2,). Below it, 1 / var leads to the green result cells 1.0 and 0.25. Keep one separate path from each input cell to its corresponding result cell. Place the label var beside the input array so the operation's name has a visible referent. Do not repeat the large funnel, legend card or decorative header icons.

Pane 2, The mechanism: a compact reminder of prompt 2. The grey list row shows [1, 4] + [4, 1] leading to [1, 4, 4, 1], labelled joins. The green array row shows the same two inputs leading to [5 5], labelled adds matching entries. Keep the arrays as snug cell blocks and the lists as continuous paper strips. A small footer shows 1 / [1, 4] leading to TypeError. Do not repeat the full connector diagram from the previous picture.

Pane 3, The run: make this the largest and most prominent pane. Typeset the four supplied output lines in clear monospace, exactly as provided, without wrapping, re-spacing or adding a fifth line. Add generous vertical space between lines. Put small red numbered markers immediately above their fields without obscuring characters: 1 above the first (2,), 2 above [1.   0.25], 3 above [-1.2  0. ], 4 above [0.8 0.8], 5 above [-1.5  0. ], and 6 above [1. 1.]. Use subtle underlines to identify field spans instead of heavy red rectangles.

Pane 4, Reading it: six compact field cards in a single vertical column, ordered 1 through 6. Each card begins with the matching red numbered marker. The repeated numbers supply the connection to the output; omit the long leader lines. Keep card text left aligned and at least as legible as the output. Cards 3 and 4 interpret the two-expert line; cards 5 and 6 interpret the with-p_b line. Use spacing to make those pairs apparent, without adding containers or panes.

Cast: grey list strips, green array cells, the output block, six numbered field cards, a red error badge. The teaching objects themselves supply the component illustrations. Keep shadows and title icons quiet so the run dominates.

Flows: short local arrows only inside the two reminder panes. Match output fields to explanations by repeated marker numbers; no leaders between panes.

Text in the image, spelled exactly:
Pane titles: "The form", "The mechanism", "The run", "Reading it".
Form labels: "[1.0, 4.0]", "np.array(...)", "var", "shape (2,)", "1 / var". Form array cells: 1.0, 4.0; result cells: 1.0, 0.25.
Mechanism labels: "list + list", "[1, 4]", "[4, 1]", "[1, 4, 4, 1]", "array + array", "[5 5]", "joins", "adds matching entries", "1 / [1, 4]", "TypeError".
Output lines exactly:
shape: (2,) (2,)
1/var_1: [1.   0.25]
two experts:  mean [-1.2  0. ]  var [0.8 0.8]
with p_b:     mean [-1.5  0. ]  var [1. 1.]
Field cards:
"1 Each array has one axis with two entries: one number per coordinate."
"2 Take one over each variance, entry by entry."
"3 The composed mean has one entry per coordinate. See plan 13."
"4 Each coordinate's variance: 1/(1 + 1/4) = 0.8"
"5 The mean with background removed has one entry per coordinate."
"6 Each coordinate's variance with background removed: 1/(1.25 - 0.25) = 1"
Compact legend: "list", "array", "error / field marker".

Exclusions: no fifth pane, no text beyond what is listed, no wrapped output lines, no connecting lines between output and cards, no repeated large legends, no decorative field-card icons, no duplicated components beyond the required reminders, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Output lines match the note's captured run character for character; six markers over the same fields as the rendered output picture; panes 1 and 2 carry the same values as prompts 1 and 2; four panes only. The six field cards read exactly as listed in the prompt, in order 1 to 6 in one column, matched by number with no leader lines; pane 1 carries "var" beside the input array.

## Subject lane: Broadcasting
<!-- student-read: 2026-10-05 job 20261005-001726-d15258 -->

Navigation: ⬅️ [Subject capstone: The deep-dive sheet](#subject-capstone-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents) | [Prompt 4 (Subject): Broadcasting, the form](#prompt-4-subject-broadcasting-the-form) ➡️

The form, the mechanism and the deep-dive sheet for [[Broadcasting]].

### Prompt 4 (Subject): Broadcasting, the form

Navigation: ⬅️ [Subject lane: Broadcasting](#subject-lane-broadcasting) | 📋 [TOC](#table-of-contents) | [Prompt 5 (Subject): Broadcasting, the mechanism](#prompt-5-subject-broadcasting-the-mechanism) ➡️

[planned] 🖼️ rendered 2026-10-04 broadcasting-the-form.webp
Save as: `../Software/Python/NumPy/assets/broadcasting-the-form.webp`

Visual thesis: Two shapes are written one above the other and lined up from the right; each column must hold equal lengths or a 1, and a missing place counts as 1.

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

Production: Use a deterministic figure script for any plot, curve, cloud or grid, and for all typography. Compose for reading at 800 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: Two worked rows, each a small table of shape boxes with three columns aligned on the right. Row 1: top line (n, 2) as two boxes n and 2 with an empty dashed box on its left; second line (2,) as one box 2 under the 2, with dashed boxes reading 1 in the empty places; result line (n, 2) in green. Row 2: top line (3, 1, 1) as boxes 3, 1, 1; second line (n, 2) as boxes n and 2 under the right two, a dashed 1 on its left; result line (3, n, 2) in green. Beside each 1 that is stretched, a short outward double arrow labelled stretched. A footer line in monospace: arr[:, None, None] turns (3,) into (3, 1, 1).

Cast: shape boxes (green for the result, neutral for the inputs, dashed for an implied 1), stretch arrows, the footer.

Flows: none; the columns line the shapes up.

Text in the image, spelled exactly: "(n, 2)", "(2,)", "(3, 1, 1)", "(3, n, 2)", "n", "2", "3", "1", "stretched", "lined up from the right", "arr[:, None, None] turns (3,) into (3, 1, 1)".

Exclusions: no arrays of numbers, no third row, no error case. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Columns are aligned on the right in both rows; every dashed box reads 1; the results are (n, 2) and (3, n, 2); green marks a result shape. Every label in the image, exactly: "(n, 2)", "(2,)", "(3, 1, 1)", "(3, n, 2)", "n", "2", "3", "1", "stretched", "lined up from the right", "arr[:, None, None] turns (3,) into (3, 1, 1)".

### Prompt 5 (Subject): Broadcasting, the mechanism

Navigation: ⬅️ [Prompt 4 (Subject): Broadcasting, the form](#prompt-4-subject-broadcasting-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 6 (Subject capstone): Broadcasting, the deep-dive sheet](#prompt-6-subject-capstone-broadcasting-the-deep-dive-sheet) ➡️

[planned] ⏳ not rendered
Save as: `../Software/Python/NumPy/assets/broadcasting-the-mechanism.webp`
The file at this path exists from an earlier render but is unchecked against this prompt, which job 20261005-001726-d15258 rewrote after a student read.

Visual thesis: The same two entries act on every matrix row; each level's scalar acts on every matrix cell; an unequal trailing pair with neither length equal to 1 stops broadcasting.

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

Production: Use a deterministic figure script for every grid, connector and label. Compose for reading at 800 px wide. Add height instead of shrinking labels. Use direct labels rather than a separate legend panel. Input grids have neutral outlines; result grids have green outlines; red identifies only the failing axis pair. The arrays and shape boxes themselves supply the component illustrations.

Scene: Three full-width panels in reading order. Give the working examples most of the space. Keep the error panel shallow, with a quiet background so its red annotation does not overpower the reuse demonstration.

Panel 1, titled (2,) across (5, 2): show a separate, solid two-cell source holding -2 and 0 above a five-row, two-column broadcast footprint. The footprint contains exactly five faint pairs of -2 and 0. Thin dashed paths from each source cell lead only to its corresponding column in the footprint. The source is outside the footprint, so it cannot be mistaken for a sixth matrix row. Dashed paths and faint entries depict reuse, not a memory-allocation sequence.

Beside the footprint, show a plus sign, a neutral five-by-two input grid, a short right arrow and a green five-by-two result grid. Align all three grids row for row. Outline the first left cell in each grid more strongly, and connect these corresponding cells with a quiet local guide through the operation. This draws attention to one matching position without adding numerical input or output values. All remaining rows remain visible and evenly spaced. Do not use an empty result grid as the only explanation of the operation: the source-to-footprint paths and corresponding-cell guide must be plainly visible.

Panel 2, titled (3, 1, 1) across (5, 2): use three aligned horizontal rows. Each row contains one scalar tile, a multiplication sign, a complete neutral five-by-two input grid, a short arrow and a complete green five-by-two result grid. The scalar tiles read 1.0, 0.5 and 0.0058 from top to bottom. Draw the same small corner notch and the same emphasized first left cell in every input grid to establish that the same matrix is reused at all three levels. The emphasis continues to the corresponding result cell. Keep all ten cells visible in every grid.

Group the three result grids with one bracket labelled (3, 5, 2). These are the three planes of one result, shown separately so none is hidden. Keep each scalar, its operation and its result on the same horizontal line. Do not fill the result planes with the scalar value: each plane contains the matrix after multiplication by that scalar.

Panel 3, titled (3,) against (100000, 2): typeset the two shapes one above the other, aligned from the right. Preserve the comma in the one-axis tuple (3,). Circle only the trailing 3 and 2 together in red. A short arrow from that circle ends at 3 meets 2: ValueError. Keep 100000 outside the circle.

Cast: one source pair, five faint reused pairs, neutral input grids, three scalar tiles, green result grids, one grouping bracket and the red mismatch annotation.

Flows: source cells connect to their own broadcast columns; each operation leads to its own result. No connectors cross panels. No extra step badges.

Text in the image, spelled exactly: "(2,) across (5, 2)", "-2", "0", "(3, 1, 1) across (5, 2)", "1.0", "0.5", "0.0058", "(3, 5, 2)", "(3,) against (100000, 2)", "3 meets 2: ValueError". The mismatch drawing repeats the shapes named in its heading. Use plus and multiplication signs as operation glyphs.

Exclusions: no invented matrix values, no scalar-filled result planes, no obscured grid cells, no perspective distortion, no list-versus-array imagery, no shapes other than those listed, no code loops, no extra copies beyond those required to demonstrate reuse, no decorative header icons, no standalone legend, no orphan arrows, no arrows ending in whitespace, no crossing paths, no watermark.
```

Faithfulness note: Panel 1 shows exactly five copies; panel 2 shows exactly three levels with the listed values and a 3-deep result; panel 3 circles the 3 aligned over the 2 in red. Every label in the image, exactly: "(2,) across (5, 2)", "-2", "0", "(3, 1, 1) across (5, 2)", "1.0", "0.5", "0.0058", "(3, 5, 2)", "(3,) against (100000, 2)", "3 meets 2: ValueError".

### Prompt 6 (Subject capstone): Broadcasting, the deep-dive sheet

Navigation: ⬅️ [Prompt 5 (Subject): Broadcasting, the mechanism](#prompt-5-subject-broadcasting-the-mechanism) | 📋 [TOC](#table-of-contents) | [Subject lane: Random numbers from a seeded generator](#subject-lane-random-numbers-from-a-seeded-generator) ➡️

[planned] ⏳ not rendered
Save as: `../Software/Python/NumPy/assets/broadcasting-deep-dive-sheet.webp`
The file at this path exists from an earlier render but is unchecked against this prompt, which job 20261005-001726-d15258 rewrote after a student read.

Visual thesis: Read the four marked fields as the broadcast result, one computed row, two added axes and three matrix-shaped levels.

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

Production: Use a deterministic figure script for all typography and diagrams. Exactly four full-width panes stacked vertically, designed for reading at 800 px wide. Output and field-card text must be at least 20 px at that displayed width. Keep the output lines unwrapped. Add height instead of reducing text size. Give the first two panes together no more than one third of the sheet's height. The run is the focal pane, with the strongest title and clearest contrast. Use neutral input outlines, green result outlines and red only for the mismatch and numbered field markers. Label objects directly; no separate legend.

Pane 1, The form: show two compact shape tables beside one another. The first has exactly two axis columns: (n, 2) above (2,), with a dashed implied 1 before the second shape's 2; its green result is (n, 2). The second has exactly three axis columns: (3, 1, 1) above (n, 2), with a dashed implied 1 before n; its green result is (3, n, 2). Keep all axis lengths vertically aligned. Use the tables themselves as illustrations, with no decorative header icon or repeated Right-aligned shapes headings.

Pane 2, The mechanism: a compact reminder with three small motifs in a single row. First, a two-cell source holding -2 and 0 above five faint reused pairs, with dashed paths into the corresponding columns. Second, three scalar tiles 1.0, 0.5 and 0.0058, each beside a multiplication sign and the same neutral five-by-two grid; short arrows lead to three green five-by-two result planes grouped under (3, 5, 2). Leave result values unspecified. Do not fill result grids with the scalar values. Third, align (3,) above (100000, 2) and mark only the trailing 3 and 2 in red, with 3 meets 2: ValueError beneath. Keep this reminder visually quieter than the run. Do not add explanatory paragraphs, a colour legend or a full repetition of the previous figure.

Pane 3, The run: use the full width for the four exact monospace lines below. Preserve every space and punctuation mark. Provide generous space above each output line for the small red field markers. Place marker 1 over x (5, 2), marker 2 over [-1.874 -0.264], marker 3 over a (3, 1, 1), and marker 4 over the final (3, 5, 2). Add a thin underline beneath each marked field so its extent is clear. Markers must not obscure characters. Do not add an output caption or a sentence about the captured run.

Pane 4, Reading it: four full-width cards in one vertical column, ordered 1 through 4. Each begins with its matching red number and the exact field text below. Match cards to output by number alone, with no leader lines between panes. Text is the main content; omit redundant right-hand explanations.

Card 1: beside the text, show a small two-cell source feeding five faint pairs. Keep it compact.
Card 2: give the supplied arithmetic text the full card width. It may break at the word and onto a second line, without changing any characters. Add no second arithmetic transcription or duplicate result box.
Card 3: beside the text, show three adjacent shape boxes containing 3, 1, 1. Use solid borders because these axes are present in a. Put a small brace beneath only the two trailing 1 boxes. Do not illustrate this field with a single scalar tile.
Card 4: beside the text, show exactly three small five-by-two result planes, separated enough that every row and column remains countable. Use green outlines and a grouping bracket. Do not add constant values to the planes.

Cast: two shape tables, compact reuse and multiplication reminders, a mismatch pair, the output block and four numbered field cards. The teaching objects supply the illustrations. Keep shadows and panel borders quiet.

Flows: local arrows only within the reminder motifs and card 1. No connectors between panes or between output and cards.

Text in the image, spelled exactly:
Pane titles: "The form", "The mechanism", "The run", "Reading it".
Output lines exactly:
$ ~/.vault-sandbox/bin/python shapes.py
mu (2,) eps (5, 2) x (5, 2)
row 0: eps [ 0.126 -0.132] -> x [-1.874 -0.264]
abar (3,) a (3, 1, 1) a * x (3, 5, 2)
Field cards:
"1 the (2,) row reached all five rows"
"2 -2 + 1 x 0.126 and 0 + 2 x (-0.132)"
"3 two length-1 axes added after the 3"
"4 one (5, 2) cloud per level"
Reminder labels and cell contents: "(n, 2)", "(2,)", "(3, 1, 1)", "(3, n, 2)", "n", "2", "3", "1", "-2", "0", "1.0", "0.5", "0.0058", "(3, 5, 2)", "(3,)", "(100000, 2)", "3 meets 2: ValueError". Use multiplication signs as operation glyphs in the mechanism reminder.

Exclusions: no fifth pane, no extra prose, no legend panel, no decorative header icons, no altered or wrapped output lines, no leader lines between panes, no constant-filled result grids, no single-value tile beside card 3, no obscured grid cells, no invented input values, no orphan arrows, no crossing paths, no watermark.
```

Faithfulness note: The output lines match the note's captured run character for character; markers 1 to 4 sit over the same fields as the note's rendered output picture; four panes only. Every label in the image, exactly: "The form", "The mechanism", "The run", "Reading it", "$ ~/.vault-sandbox/bin/python shapes.py", "mu (2,) eps (5, 2) x (5, 2)", "row 0: eps [ 0.126 -0.132] -> x [-1.874 -0.264]", "abar (3,) a (3, 1, 1) a * x (3, 5, 2)", "1 the (2,) row reached all five rows", "2 -2 + 1 x 0.126 and 0 + 2 x (-0.132)", "3 two length-1 axes added after the 3", "4 one (5, 2) cloud per level".

## Subject lane: Random numbers from a seeded generator
<!-- student-read: 2026-10-05 job 20261005-001726-42e135 -->

Navigation: ⬅️ [Prompt 6 (Subject capstone): Broadcasting, the deep-dive sheet](#prompt-6-subject-capstone-broadcasting-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents) | [Prompt 7 (Subject): Seeding, the form](#prompt-7-subject-seeding-the-form) ➡️

The form, the mechanism and the deep-dive sheet for [[Random Numbers From A Seeded Generator]].

### Prompt 7 (Subject): Seeding, the form

Navigation: ⬅️ [Subject lane: Random numbers from a seeded generator](#subject-lane-random-numbers-from-a-seeded-generator) | 📋 [TOC](#table-of-contents) | [Prompt 8 (Subject): Seeding, the mechanism](#prompt-8-subject-seeding-the-mechanism) ➡️

[planned] 🖼️ rendered 2026-10-04 seeding-the-form.webp
Save as: `../Software/Python/NumPy/assets/seeding-the-form.webp`

Visual thesis: One seeded generator feeds every draw in a file; a bare np.random call draws from a separate hidden global generator that the seed never reaches.

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

Production: Use a deterministic figure script for any plot, curve, cloud or grid, and for all typography. Compose for reading at 800 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: Left, a teal generator card: a small dial icon with the seed 0 on it, titled rng = np.random.default_rng(0). Two short teal arrows lead from it to two call cards: rng.standard_normal(shape) and rng.normal(mean, std, shape), each tagged repeats every run. Right, separated by a thin divider, a grey card titled hidden global generator, with no seed on its dial, and one grey arrow to a call card np.random.standard_normal(shape), tagged changes every run. Under the right side, the label rng is not used.

Cast: the seeded generator (teal), the global generator (grey), three call cards.

Flows: teal arrows only from the seeded generator to its two calls; one grey arrow from the global generator to its call; no arrow between the two sides.

Text in the image, spelled exactly: "rng = np.random.default_rng(0)", "rng.standard_normal(shape)", "rng.normal(mean, std, shape)", "repeats every run", "hidden global generator", "np.random.standard_normal(shape)", "changes every run", "rng is not used".

Exclusions: no dice, no code beyond the listed calls, no arrow from the seeded generator to the bare np.random call. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The seeded generator connects to exactly two calls and never to np.random.standard_normal; teal means seeded, grey means the global generator. Every label in the image, exactly: "rng = np.random.default_rng(0)", "rng.standard_normal(shape)", "rng.normal(mean, std, shape)", "repeats every run", "hidden global generator", "np.random.standard_normal(shape)", "changes every run", "rng is not used".

### Prompt 8 (Subject): Seeding, the mechanism

Navigation: ⬅️ [Prompt 7 (Subject): Seeding, the form](#prompt-7-subject-seeding-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 9 (Subject capstone): Seeding, the deep-dive sheet](#prompt-9-subject-capstone-seeding-the-deep-dive-sheet) ➡️

[planned] ⏳ not rendered
Save as: `../Software/Python/NumPy/assets/seeding-the-mechanism.webp`
The file at this path exists from an earlier render but is unchecked against this prompt, which job 20261005-001726-42e135 rewrote after a student read.

Visual thesis: The same generator advances to the next group of numbers; a fresh generator with the same seed starts at the first group again.

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

Production: Use a deterministic figure script for the complete diagram and all typography. Design for display at 800 px wide, with labels and cell values at least 20 px at that width. Add height rather than shrinking text. Use directly labelled teaching objects instead of a separate legend.

Scene: Two horizontal number tapes with identical cell widths and vertically aligned cell boundaries. Each tape contains 0.1257, -0.1321, 0.6404, 0.1049, -0.5357, 0.3616, then an ellipsis cell. Place a small seed tag reading seed 0 to the left of each tape. Keep any seed illustration small and secondary.

Upper tape: Make the movement of the rng reading head the focal element. Draw an outlined teal head pointing to the centre of the first cell and a solid teal head pointing to the centre of the fourth cell. These are two positions of the same head, not two generators. Connect the outlined position to the solid position with one horizontal teal arrow that ends on the solid head. Label this connected head-and-arrow assembly rng once, with PCG64 directly beneath the label in smaller type. Leave enough vertical separation between this movement and the grouping brackets to avoid overlaps.

Place a bracket labelled first draw over exactly the first three cells: its left endpoint aligns with the tape's left boundary and its right endpoint with the boundary after 0.6404. Place a bracket labelled second draw over exactly the next three cells: its endpoints align with the boundaries before 0.1049 and after 0.3616. Give the first group a very light teal fill and the second group a slightly stronger teal fill, keeping both fully legible. The arrow's destination points to 0.1049, where the second draw starts.

Lower tape: Draw one solid teal head labelled fresh rng pointing to the centre of the first cell. A bracket labelled same three numbers spans exactly the first three cells, with endpoints aligned to the same boundaries as first draw above. Emphasise those three cells with a light teal fill; keep the remaining cells unfilled but readable. Do not draw a movement arrow on this tape.

Cast: two number tapes, an outlined and solid position of the upper reading head, one fresh reading head, three precisely aligned brackets, two small seed tags. The tapes and heads are the component illustrations.

Flows: one arrow from the upper head's initial position to its position at the fourth cell. No connector between the two generators.

Text in the image, spelled exactly: "seed 0", "PCG64", "rng", "first draw", "second draw", "fresh rng", "same three numbers", "0.1257", "-0.1321", "0.6404", "0.1049", "-0.5357", "0.3616". An ellipsis ends each tape.

Exclusions: no global generator, no other numbers, no dice or coins, no extra explanatory labels, no bracket beginning inside a cell, no arrow ending in whitespace, no third tape, no decorative header icons, no crossing connectors, no paragraphs, no watermark. Do not depict the upper head's two positions as independent generators.
```

Faithfulness note: The six numbers appear in the listed order on the first tape; the second tape's first three cells repeat 0.1257, -0.1321, 0.6404. Every label in the image, exactly: "seed 0", "PCG64", "rng", "first draw", "second draw", "fresh rng", "same three numbers", "0.1257", "-0.1321", "0.6404", "0.1049", "-0.5357", "0.3616".

### Prompt 9 (Subject capstone): Seeding, the deep-dive sheet

Navigation: ⬅️ [Prompt 8 (Subject): Seeding, the mechanism](#prompt-8-subject-seeding-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[planned] ⏳ not rendered
Save as: `../Software/Python/NumPy/assets/seeding-deep-dive-sheet.webp`
The file at this path exists from an earlier render but is unchecked against this prompt, which job 20261005-001726-42e135 rewrote after a student read.

Visual thesis: Read the output to see the same generator continue, then a fresh generator repeat the first draw.

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

Production: Use a deterministic figure script for the complete sheet, including diagrams, output and typography. Exactly four full-width panes stacked vertically, designed for display at 800 px wide. Keep all teaching text at least 20 px at that width. Add height rather than shrinking text. The run is the visual focus through its dark background and clear monospace text. Use modest pane headings of equal size. The reminder panes should occupy about one third of the total height, with the remaining space devoted to the run and its explanations. Omit the palette legend and decorative terminal chrome.

Pane 1, The form: A compact reminder of the two separate generator paths. Use two full-width rows rather than narrow side-by-side panels. In the first row, a small teal generator dial accompanies rng = np.random.default_rng(0). Two short teal branches end at rng.standard_normal(shape) and rng.normal(mean, std, shape), stacked beneath it. Place repeats every run once beside the pair. In the second row, a small grey generator dial accompanies hidden global generator and connects only to np.random.standard_normal(shape). Place changes every run and rng is not used beneath that call. Preserve separation between the two paths. All call labels use the same readable type size. The grey path remains clearly visible: it is a separate generator that is used by its own call.

Pane 2, The mechanism: A compact reminder of continuation and restart. Draw one six-cell tape containing 0.1257, -0.1321, 0.6404, 0.1049, -0.5357, 0.3616, followed by an ellipsis. Label its seed tag seed 0 and its reading head rng. Brackets labelled first draw and second draw span exactly three whole cells each. Show the upper head's outlined position at the first cell connected by one short arrow to its solid position at the fourth cell. Below, draw a short tape with the first three values and an ellipsis, with its own seed 0 tag and fresh rng head at the first cell. Label its three-cell bracket same three numbers. Align the three repeated values vertically with the upper tape. Do not repeat large seed illustrations.

Pane 3, The run: Make this the strongest pane on the sheet. Typeset the five supplied lines exactly in monospace, without wrapping or changing spaces. Separate lines vertically enough to fit markers above their fields. Put red marker 1 immediately above PCG64; marker 2 above the first draw's array; marker 3 above the second draw's array; marker 4 above the fresh rng's array. Keep every character unobscured. Use a subtle underline beneath each array to show the field span. No icons inside the output and no additional terminal labels.

Pane 4, Reading it: Four compact cards in one vertical column, ordered 1 through 4. Each card begins at the same left edge with its red numbered marker, followed immediately by its explanation. The number and sentence form the card's focal element; omit the large gear, number tiles, arrow and seed illustrations from the existing sheet. The diagrams in the reminder panes already supply those visual connections. Match cards to output by number alone, without leader lines. Allow the fourth explanation to wrap naturally.

Cast: small generator dials, three call labels connected to their own generators, number tapes and reading heads, one output block, four numbered explanation cards. Use the teaching objects as the component illustrations.

Flows: short local connectors inside the reminder panes only. No connector between the seeded and global generators. No connectors between panes.

Text in the image, spelled exactly:
Pane titles: "The form", "The mechanism", "The run", "Reading it".
Form reminder: "rng = np.random.default_rng(0)", "rng.standard_normal(shape)", "rng.normal(mean, std, shape)", "repeats every run", "hidden global generator", "np.random.standard_normal(shape)", "changes every run", "rng is not used".
Mechanism reminder: "seed 0", "rng", "first draw", "second draw", "fresh rng", "same three numbers". Upper tape values: 0.1257, -0.1321, 0.6404, 0.1049, -0.5357, 0.3616. Lower tape values: 0.1257, -0.1321, 0.6404. Each tape ends with an ellipsis.
Output lines exactly:
$ ~/.vault-sandbox/bin/python stream.py
PCG64
first draw:  [ 0.1257 -0.1321  0.6404]
second draw: [ 0.1049 -0.5357  0.3616]
fresh rng:   [ 0.1257 -0.1321  0.6404]
Field cards, with the initial number rendered as the red marker:
"1 the algorithm behind the stream"
"2 the first three numbers of seed 0"
"3 the next three: the generator moved on"
"4 a new generator with seed 0 starts again: equals field 2"

Exclusions: no fifth pane, no legend panel, no added recommendation heading, no decorative field-card icons, no terminal window buttons, no leader lines between panes, no altered or wrapped output text, no extra labels, no orphan arrows, no arrow ending in whitespace, no crossing connectors, no watermark. Teal identifies the seeded generator; grey identifies the separate hidden global generator; red identifies output markers.
```

Faithfulness note: The output lines match the note's captured run character for character; markers 1 to 4 sit over the same fields as the note's rendered output picture; four panes only. Every label in the image, exactly: "The form", "The mechanism", "The run", "Reading it", "$ ~/.vault-sandbox/bin/python stream.py", "PCG64", "first draw:  [ 0.1257 -0.1321  0.6404]", "second draw: [ 0.1049 -0.5357  0.3616]", "fresh rng:   [ 0.1257 -0.1321  0.6404]", "1 the algorithm behind the stream", "2 the first three numbers of seed 0", "3 the next three: the generator moved on", "4 a new generator with seed 0 starts again: equals field 2".

## Process lane

Navigation: ⬅️ [Prompt 9 (Subject capstone): Seeding, the deep-dive sheet](#prompt-9-subject-capstone-seeding-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
