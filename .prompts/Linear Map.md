# Linear Map: illustrated map

The drawn pictures for the vault note [[Linear Map]], section [[Linear Map#What a linear map is]]. `3 prompts · 0 rendered · 3 waiting`

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
- [Prompt 3 (Subject capstone): The deep-dive sheet](#prompt-3-subject-capstone-the-deep-dive-sheet)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[Linear Map]]: subject "What a linear map is", one sheet. A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: no subject here needs a repeatable named look across the set. Zoom depth: one level, the section's form and mechanism, composed by the deep-dive sheet. The style paragraph is embedded verbatim at the head of every prompt. Lines, points and arrows sit at exact coordinates, so every one is drawn by a deterministic figure script.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

Pass the note's code-drawn figure `linear-map-through-the-origin.svg` and its output picture `linear-map-the-rule-checked.png` as references. Nothing here is a real-world object.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Blue: the map and what it outputs. Green: the weights 2 and 3. Orange: a fixed number added after the map, shown only on the rule that is not linear. Red: numbered output markers only.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

An arrow from the origin is a vector. A thick rounded box with an arrow in and an arrow out is the map. A small green number beside an arrow is its weight. All primary tier.

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Inputs on the left, the map in the middle, outputs on the right. On a plane, x runs right and y runs up, origin marked.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Numbered markers only on the deep-dive sheet's output pane, matching the numbered fields in the note's rendered output picture. No step badges or phase containers.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The form](#prompt-1-subject-the-form) ➡️

The form, the mechanism, then the deep-dive sheet that composes them with the run's output, per the vault-note exception in the illustration style guide.

### Prompt 1 (Subject): The form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism) ➡️

[planned] ⏳ not rendered
Save as: `../Mathematics/Linear Algebra/assets/linear-map-the-form.webp`

Visual thesis: Mixing two arrows and then mapping lands on the same arrow as mapping each and then mixing.

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

Production: deterministic figure script, two rows read at 800 px wide, labels at least 18 px.

Scene: Top row: two blue input arrows u = (3, 1) and v = (1, 2) on a small grid, combined into 2u + 3v = (9, 8), which goes into a box labelled "M" and comes out as (26, 8). Bottom row: u and v go into the same box "M" separately, come out as M(u) = (7, 1) and M(v) = (4, 2), and are then combined with weights 2 and 3 into (26, 8). A green equals sign joins the two results at the right edge.

Cast: the grid, the arrows u, v, 2u + 3v, M(u), M(v), (26, 8) twice, two boxes labelled M, the weights 2 and 3.

Flows: one arrow into and one out of each box.

Text in the image, spelled exactly: "u = (3, 1)", "v = (1, 2)", "2u + 3v = (9, 8)", "M", "M(u) = (7, 1)", "M(v) = (4, 2)", "(26, 8)", "mix, then map", "map, then mix", "2", "3".

Exclusions: no third row, no offset, no curved arrows, no paragraphs of text, no legend, no decorative icons, no watermark, no crossing arrows, no arrow terminating in whitespace.
```

Faithfulness note: Both rows end on the same vector (26, 8); the top row mixes before the box and the bottom row after; the weights are 2 on u and 3 on v in both rows. Every label in the image, exactly: "u = (3, 1)", "v = (1, 2)", "2u + 3v = (9, 8)", "M", "M(u) = (7, 1)", "M(v) = (4, 2)", "(26, 8)", "mix, then map", "map, then mix", "2", "3".

### Prompt 2 (Subject): The mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The form](#prompt-1-subject-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject capstone): The deep-dive sheet](#prompt-3-subject-capstone-the-deep-dive-sheet) ➡️

[planned] ⏳ not rendered
Save as: `../Mathematics/Linear Algebra/assets/linear-map-the-mechanism.webp`

Visual thesis: A matrix is where the two basis arrows land, and any input is rebuilt from them.

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

Production: deterministic figure script, two panels side by side on a shared grid from -1 to 10 in x and -1 to 9 in y, read at 800 px wide, labels at least 18 px.

Scene: Left panel, titled "before": the basis arrows (1, 0) and (0, 1) from the origin, and the input (9, 8) drawn as 9 steps along (1, 0) then 8 steps along (0, 1). Right panel, titled "after M": (1, 0) has become the column (2, 0) and (0, 1) the column (1, 1); the output (26, 8) is drawn as 9 copies of (2, 0) then 8 copies of (1, 1), with the x axis extended to 27. The origin is marked "0 stays at 0" in both panels.

Cast: two basis arrows per panel, the step chains, the input and output points.

Flows: one faint arrow from the left panel to the right panel labelled "M".

Text in the image, spelled exactly: "before", "after M", "(1, 0)", "(0, 1)", "(2, 0)", "(1, 1)", "(9, 8)", "(26, 8)", "9 ×", "8 ×", "0 stays at 0", "M".

Exclusions: no third panel, no offset vector, no curved grid, no paragraphs of text, no legend, no decorative icons, no watermark, no crossing arrows, no arrow terminating in whitespace.
```

Faithfulness note: (1, 0) goes to (2, 0) and (0, 1) to (1, 1); 9 × (2, 0) + 8 × (1, 1) = (26, 8); the origin does not move. Every label in the image, exactly: "before", "after M", "(1, 0)", "(0, 1)", "(2, 0)", "(1, 1)", "(9, 8)", "(26, 8)", "9 ×", "8 ×", "0 stays at 0", "M".

### Prompt 3 (Subject capstone): The deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[planned] ⏳ not rendered
Save as: `../Mathematics/Linear Algebra/assets/linear-map-deep-dive-sheet.webp`

Visual thesis: The form and the mechanism above the numbered run of linear.py, each output line tied to its reading.

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

Production: deterministic figure script, four full-width panes stacked, read at 800 px wide, output text at least 20 px, no wrapped output lines.

Scene: Pane 1, The form: a compact copy of prompt 1's two rows. Pane 2, The mechanism: a compact copy of prompt 2's two panels. Pane 3, The run: print these five lines verbatim (| marks a line break and is not printed):

$ python3 linear.py | L(0) = 0, M((0, 0)) = (0, 0) | L(2*1 + 3*3) = L(11) = 33; 2*L(1) + 3*L(3) = 33 | M(2u + 3v) = (26, 8); 2*M(u) + 3*M(v) = (26, 8) | g(0) = 2; g(2*1 + 3*3) = 35; 2*g(1) + 3*g(3) = 43

Red markers 1 to 4 before the four output lines, as in the note's linear-map-the-rule-checked.png. Pane 4, Reading it: four cards: "1 zero goes to zero", "2 mix then map equals map then mix", "3 the same with a matrix", "4 adding 2 breaks it: 35 against 43".

Cast: two compact reminder drawings, the output block, four cards.

Flows: none between panes.

Text in the image, spelled exactly: "The form", "The mechanism", "The run", "Reading it", the five run lines above, and the four cards above.

Exclusions: no fifth pane, no altered output text, no paragraphs of text, no legend, no decorative icons, no watermark, no crossing arrows, no arrow terminating in whitespace.
```

Faithfulness note: The five run lines match the note's captured run of linear.py character for character; markers 1 to 4 match linear-map-the-rule-checked.png. Every label in the image, exactly: "The form", "The mechanism", "The run", "Reading it", "$ python3 linear.py", the four output lines as captured, "1 zero goes to zero", "2 mix then map equals map then mix", "3 the same with a matrix", "4 adding 2 breaks it: 35 against 43".

## Process lane

Navigation: ⬅️ [Prompt 3 (Subject capstone): The deep-dive sheet](#prompt-3-subject-capstone-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
