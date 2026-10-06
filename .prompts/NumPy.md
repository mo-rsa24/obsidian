# NumPy: illustrated map

The drawn pictures for the vault note [[NumPy]], sections [[NumPy#Arrays versus Python lists]], [[NumPy#Broadcasting]] and [[NumPy#Random numbers from a seeded generator]]. `9 prompts · 9 rendered · 0 waiting`

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
Save as: `../Software/Python/assets/numpy-arrays-the-form.webp`

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
Save as: `../Software/Python/assets/numpy-arrays-the-mechanism.webp`

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
Save as: `../Software/Python/assets/numpy-arrays-deep-dive-sheet.webp`

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

The form, the mechanism and the deep-dive sheet for [[NumPy#Broadcasting]].

### Prompt 4 (Subject): Broadcasting, the form

Navigation: ⬅️ [Subject lane: Broadcasting](#subject-lane-broadcasting) | 📋 [TOC](#table-of-contents) | [Prompt 5 (Subject): Broadcasting, the mechanism](#prompt-5-subject-broadcasting-the-mechanism) ➡️

[planned] 🖼️ rendered 2026-10-04 broadcasting-the-form.webp
Save as: `../Software/Python/assets/broadcasting-the-form.webp`

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

[planned] 🖼️ rendered 2026-10-04 broadcasting-the-mechanism.webp
Save as: `../Software/Python/assets/broadcasting-the-mechanism.webp`

Visual thesis: A (2,) row is reused for every row of a (5, 2) matrix, a (3, 1, 1) column is applied to the whole matrix once per level, and a (3,) against a (100000, 2) fails because 3 meets 2.

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

Scene: Three panels. Panel 1, titled (2,) across (5, 2): a one-row strip holding -2 and 0, and five faint copies of it stacked downward beside a 5 by 2 grid, with a plus between them and a 5 by 2 result grid. Panel 2, titled (3, 1, 1) across (5, 2): three level tiles 1.0, 0.5 and 0.0058 stacked as a column; each tile multiplies a full copy of the 5 by 2 grid; the three results stack into a small 3-deep block labelled (3, 5, 2). Panel 3, titled (3,) against (100000, 2): the two shapes lined up from the right, with the 3 above the 2 circled in red and the label 3 meets 2: ValueError.

Cast: the row strip and its faint copies, the 5 by 2 grids, the level tiles, the stacked result block, the red error circle.

Flows: short arrows from each input to its result inside each panel; nothing crosses panels.

Text in the image, spelled exactly: "(2,) across (5, 2)", "-2", "0", "(3, 1, 1) across (5, 2)", "1.0", "0.5", "0.0058", "(3, 5, 2)", "(3,) against (100000, 2)", "3 meets 2: ValueError".

Exclusions: no list-versus-array imagery, no shapes other than those listed, no loops drawn as code. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Panel 1 shows exactly five copies; panel 2 shows exactly three levels with the listed values and a 3-deep result; panel 3 circles the 3 aligned over the 2 in red. Every label in the image, exactly: "(2,) across (5, 2)", "-2", "0", "(3, 1, 1) across (5, 2)", "1.0", "0.5", "0.0058", "(3, 5, 2)", "(3,) against (100000, 2)", "3 meets 2: ValueError".

### Prompt 6 (Subject capstone): Broadcasting, the deep-dive sheet

Navigation: ⬅️ [Prompt 5 (Subject): Broadcasting, the mechanism](#prompt-5-subject-broadcasting-the-mechanism) | 📋 [TOC](#table-of-contents) | [Subject lane: Random numbers from a seeded generator](#subject-lane-random-numbers-from-a-seeded-generator) ➡️

[planned] 🖼️ rendered 2026-10-04 broadcasting-deep-dive-sheet.webp
Save as: `../Software/Python/assets/broadcasting-deep-dive-sheet.webp`

Visual thesis: Shapes lined up from the right decide every result shape, and the run prints each one.

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

Production: Use a deterministic figure script. A tall sheet of exactly four panes stacked vertically, each the full width, designed for reading at 800 px wide; add height rather than shrinking text, with output and field text at least 20 px at that width. The first two panes are compact reminders of the form and the mechanism, not full copies. The run pane is the focal pane. Field cards run 1 to N in one column in the same order as the markers, each starting with its red number, and are matched to the output by number alone: no leader lines between panes.

Scene: Pane 1, The form: a compact reminder of prompt 4, the two aligned rows ending in (n, 2) and (3, n, 2). Pane 2, The mechanism: a compact reminder of prompt 5, the copied row, the three levels and the red 3 meets 2. Pane 3, The run: four lines of monospace output, exactly: $ ~/.vault-sandbox/bin/python shapes.py | mu (2,) eps (5, 2) x (5, 2) | row 0: eps [ 0.126 -0.132] -> x [-1.874 -0.264] | abar (3,) a (3, 1, 1) a * x (3, 5, 2) (the | marks a new line and is not printed). Red markers: 1 over x (5, 2), 2 over [-1.874 -0.264], 3 over a (3, 1, 1), 4 over (3, 5, 2). Pane 4, Reading it: four cards in order.

Cast: the reminder shape tables and grids, the output block, four numbered field cards.

Flows: none between panes.

Text in the image, spelled exactly: "The form", "The mechanism", "The run", "Reading it", "$ ~/.vault-sandbox/bin/python shapes.py", "mu (2,) eps (5, 2) x (5, 2)", "row 0: eps [ 0.126 -0.132] -> x [-1.874 -0.264]", "abar (3,) a (3, 1, 1) a * x (3, 5, 2)", "1 the (2,) row reached all five rows", "2 -2 + 1 x 0.126 and 0 + 2 x (-0.132)", "3 two length-1 axes added after the 3", "4 one (5, 2) cloud per level".

Exclusions: no fifth pane, no leader lines between panes, no altered output text. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The output lines match the note's captured run character for character; markers 1 to 4 sit over the same fields as the note's rendered output picture; four panes only. Every label in the image, exactly: "The form", "The mechanism", "The run", "Reading it", "$ ~/.vault-sandbox/bin/python shapes.py", "mu (2,) eps (5, 2) x (5, 2)", "row 0: eps [ 0.126 -0.132] -> x [-1.874 -0.264]", "abar (3,) a (3, 1, 1) a * x (3, 5, 2)", "1 the (2,) row reached all five rows", "2 -2 + 1 x 0.126 and 0 + 2 x (-0.132)", "3 two length-1 axes added after the 3", "4 one (5, 2) cloud per level".

## Subject lane: Random numbers from a seeded generator
<!-- student-read: 2026-10-05 job 20261005-001726-42e135 -->

Navigation: ⬅️ [Prompt 6 (Subject capstone): Broadcasting, the deep-dive sheet](#prompt-6-subject-capstone-broadcasting-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents) | [Prompt 7 (Subject): Seeding, the form](#prompt-7-subject-seeding-the-form) ➡️

The form, the mechanism and the deep-dive sheet for [[NumPy#Random numbers from a seeded generator]].

### Prompt 7 (Subject): Seeding, the form

Navigation: ⬅️ [Subject lane: Random numbers from a seeded generator](#subject-lane-random-numbers-from-a-seeded-generator) | 📋 [TOC](#table-of-contents) | [Prompt 8 (Subject): Seeding, the mechanism](#prompt-8-subject-seeding-the-mechanism) ➡️

[planned] 🖼️ rendered 2026-10-04 seeding-the-form.webp
Save as: `../Software/Python/assets/seeding-the-form.webp`

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

[planned] 🖼️ rendered 2026-10-04 seeding-the-mechanism.webp
Save as: `../Software/Python/assets/seeding-the-mechanism.webp`

Visual thesis: A seed sets a generator's starting state; each draw reads the next numbers and moves the state on; a second generator with the same seed replays the stream from the start.

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

Scene: A horizontal tape of numbers read left to right, the stream of seed 0: 0.1257, -0.1321, 0.6404, 0.1049, -0.5357, 0.3616, then an ellipsis cell. Above the tape, a teal reading head labelled rng; a bracket over the first three cells labelled first draw and over the next three labelled second draw. Below the tape, a second, identical tape with its own head at the very start, labelled fresh rng, and a bracket over its first three cells labelled same three numbers. At the far left of both tapes, a small seed tag reading seed 0, and the label PCG64 on the first tape.

Cast: two number tapes, two reading heads, three brackets, the seed tags.

Flows: one short arrow showing the first head moving from the first bracket to the second.

Text in the image, spelled exactly: "seed 0", "PCG64", "rng", "first draw", "second draw", "fresh rng", "same three numbers", "0.1257", "-0.1321", "0.6404", "0.1049", "-0.5357", "0.3616".

Exclusions: no global generator, no other numbers, no randomness imagery such as dice or coins. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The six numbers appear in the listed order on the first tape; the second tape's first three cells repeat 0.1257, -0.1321, 0.6404. Every label in the image, exactly: "seed 0", "PCG64", "rng", "first draw", "second draw", "fresh rng", "same three numbers", "0.1257", "-0.1321", "0.6404", "0.1049", "-0.5357", "0.3616".

### Prompt 9 (Subject capstone): Seeding, the deep-dive sheet

Navigation: ⬅️ [Prompt 8 (Subject): Seeding, the mechanism](#prompt-8-subject-seeding-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[planned] 🖼️ rendered 2026-10-04 seeding-deep-dive-sheet.webp
Save as: `../Software/Python/assets/seeding-deep-dive-sheet.webp`

Visual thesis: A seeded generator's stream continues across draws and restarts for a fresh generator with the same seed, as the run prints.

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

Production: Use a deterministic figure script. A tall sheet of exactly four panes stacked vertically, each the full width, designed for reading at 800 px wide; add height rather than shrinking text, with output and field text at least 20 px at that width. The first two panes are compact reminders of the form and the mechanism, not full copies. The run pane is the focal pane. Field cards run 1 to N in one column in the same order as the markers, each starting with its red number, and are matched to the output by number alone: no leader lines between panes.

Scene: Pane 1, The form: a compact reminder of prompt 7, the seeded generator with its two calls beside the hidden global generator. Pane 2, The mechanism: a compact reminder of prompt 8, the tape with first draw and second draw, and the fresh tape. Pane 3, The run: five lines of monospace output, exactly: $ ~/.vault-sandbox/bin/python stream.py | PCG64 | first draw:  [ 0.1257 -0.1321  0.6404] | second draw: [ 0.1049 -0.5357  0.3616] | fresh rng:   [ 0.1257 -0.1321  0.6404] (the | marks a new line and is not printed; keep the spaces). Red markers: 1 over PCG64, 2 over the first draw's array, 3 over the second draw's array, 4 over the fresh rng's array. Pane 4, Reading it: four cards in order.

Cast: the reminders, the output block, four numbered field cards.

Flows: none between panes.

Text in the image, spelled exactly: "The form", "The mechanism", "The run", "Reading it", "$ ~/.vault-sandbox/bin/python stream.py", "PCG64", "first draw:  [ 0.1257 -0.1321  0.6404]", "second draw: [ 0.1049 -0.5357  0.3616]", "fresh rng:   [ 0.1257 -0.1321  0.6404]", "1 the algorithm behind the stream", "2 the first three numbers of seed 0", "3 the next three: the generator moved on", "4 a new generator with seed 0 starts again: equals field 2".

Exclusions: no fifth pane, no leader lines between panes, no altered output text. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The output lines match the note's captured run character for character; markers 1 to 4 sit over the same fields as the note's rendered output picture; four panes only. Every label in the image, exactly: "The form", "The mechanism", "The run", "Reading it", "$ ~/.vault-sandbox/bin/python stream.py", "PCG64", "first draw:  [ 0.1257 -0.1321  0.6404]", "second draw: [ 0.1049 -0.5357  0.3616]", "fresh rng:   [ 0.1257 -0.1321  0.6404]", "1 the algorithm behind the stream", "2 the first three numbers of seed 0", "3 the next three: the generator moved on", "4 a new generator with seed 0 starts again: equals field 2".

## Process lane

Navigation: ⬅️ [Prompt 9 (Subject capstone): Seeding, the deep-dive sheet](#prompt-9-subject-capstone-seeding-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
