# Affine Map: illustrated map

The drawn pictures for the vault note [[Affine Map]], sections [[Affine Map#What an affine map is]] and [[Affine Map#Affine combination]]. `3 prompts · 0 rendered · 3 waiting`

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

1. [[Affine Map]]: subject "Affine combination", one sheet. A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: no subject here needs a repeatable named look across the set. Zoom depth: one level, the section's form and mechanism, composed by the deep-dive sheet. The style paragraph is embedded verbatim at the head of every prompt. Lines, points and arrows sit at exact coordinates, so every one is drawn by a deterministic figure script.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

Pass the note's code-drawn figure `affine-map-sum-one-and-sum-zero.svg` and its output picture `affine-map-which-combinations-it-keeps.png` as references. Nothing here is a real-world object.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Blue: the linear part L and what it outputs. Orange: the offset c and anything that carries it. Green: the weights and the combination they make. Red: the gap equal to the offset, and the numbered output markers.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

An arrow from the origin is a vector. A thick orange arrow is the offset. A green number beside an arrow is its weight. A red double-headed bracket is a gap. All primary tier.

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

On a plane, x runs right and y runs up, origin marked. Panels read left to right: weights adding to 1, then weights adding to 0.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Numbered markers only on the deep-dive sheet's output pane, matching the numbered fields in the note's rendered output picture. No step badges or phase containers.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The form](#prompt-1-subject-the-form) ➡️

The form, the mechanism, then the deep-dive sheet that composes them with the run's output, per the vault-note exception in the illustration style guide.

### Prompt 1 (Subject): The form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism) ➡️

[planned] ⏳ not rendered
Save as: `../Mathematics/Linear Algebra/assets/affine-map-the-form.webp`

Visual thesis: An affine map is the linear part followed by one fixed orange shift, so 0 lands on c.

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

Production: deterministic figure script, one row read at 800 px wide, labels at least 18 px.

Scene: Left: the input x = 1 on a number line. Middle: a blue box "L(x) = 3x" turning 1 into 3. Right: an orange arrow of length 2 labelled "+ c, c = 2" moving 3 up to 5. Below the row, the same path for x = 0: L gives 0, and the orange arrow moves it to 2, labelled "f(0) = c = 2".

Cast: two number lines, the blue box, two orange arrows, the points 1, 3, 5, 0, 2.

Flows: left to right only.

Text in the image, spelled exactly: "x = 1", "L(x) = 3x", "3", "+ c, c = 2", "f(1) = 5", "x = 0", "0", "f(0) = c = 2", "f(x) = L(x) + c".

Exclusions: no second offset, no matrix, no paragraphs of text, no legend, no decorative icons, no watermark, no crossing arrows, no arrow terminating in whitespace.
```

Faithfulness note: The orange shift has length 2 in both rows; L sends 1 to 3 and 0 to 0; f(1) = 5 and f(0) = 2. Every label in the image, exactly: "x = 1", "L(x) = 3x", "3", "+ c, c = 2", "f(1) = 5", "x = 0", "0", "f(0) = c = 2", "f(x) = L(x) + c".

### Prompt 2 (Subject): The mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The form](#prompt-1-subject-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject capstone): The deep-dive sheet](#prompt-3-subject-capstone-the-deep-dive-sheet) ➡️

[planned] ⏳ not rendered
Save as: `../Mathematics/Linear Algebra/assets/affine-map-the-mechanism.webp`

Visual thesis: Weights adding to 1 carry the offset once and pass through; weights adding to 0 carry it zero times and lose it.

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

Production: deterministic figure script, two panels side by side, read at 800 px wide, labels at least 18 px.

Scene: Left panel, titled "weights add to 1": the four made-up vectors (4, 1), (1, 2), (2, 0) and (0, 1) with green weights 1, -1, -1 and 2 combine into (1, 1); its image F(1, 1) = (4, 0) and the combination of the four images, also (4, 0), coincide, with a small orange tag "offset counted 1 time". Right panel, titled "weights add to 0": the same four vectors with weights 1, -1, -1 and 1 combine into (1, 0); F(1, 0) = (3, -1) and the combination of images (2, 0) are drawn apart, joined by a red bracket labelled "gap = c = (1, -1)", with an orange tag "offset counted 0 times".

Cast: four input arrows per panel, the combination, the two results, the bracket and the two tags.

Flows: none beyond the arrows.

Text in the image, spelled exactly: "weights add to 1", "weights add to 0", "1", "-1", "2", "(1, 1)", "(4, 0)", "(1, 0)", "(3, -1)", "(2, 0)", "offset counted 1 time", "offset counted 0 times", "gap = c = (1, -1)".

Exclusions: no third panel, no start-token panel, no paragraphs of text, no legend, no decorative icons, no watermark, no crossing arrows, no arrow terminating in whitespace.
```

Faithfulness note: Left panel: one point (4, 0) for both results; right panel: (3, -1) and (2, 0) one offset (1, -1) apart; the weights are 1, -1, -1, 2 on the left and 1, -1, -1, 1 on the right. Every label in the image, exactly: "weights add to 1", "weights add to 0", "1", "-1", "2", "(1, 1)", "(4, 0)", "(1, 0)", "(3, -1)", "(2, 0)", "offset counted 1 time", "offset counted 0 times", "gap = c = (1, -1)".

### Prompt 3 (Subject capstone): The deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[planned] ⏳ not rendered
Save as: `../Mathematics/Linear Algebra/assets/affine-map-deep-dive-sheet.webp`

Visual thesis: The form and the mechanism above the numbered run of affine.py, each output line tied to its reading.

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

Production: deterministic figure script, four full-width panes stacked, read at 800 px wide, output text at least 20 px, no wrapped output lines, narrow monospace face sized so the longest line fits.

Scene: Pane 1, The form: compact copy of prompt 1. Pane 2, The mechanism: compact copy of prompt 2. Pane 3, The run: print the note's captured run of affine.py verbatim, seven lines beginning "$ python3 affine.py", with red markers 1 to 6 before the six output lines as in affine-map-which-combinations-it-keeps.png. Pane 4, Reading it: six cards: "1 f sends 0 to its offset", "2 weights add to 1: both ways 8.0", "3 weights add to 0: the offset is lost", "4 the plane: gap (1, -1) is the offset", "5 weights add to 1: both ways (4, 0)", "6 a shared vector: cancelled, then kept once".

Cast: two compact reminder drawings, the output block, six cards.

Flows: none between panes.

Text in the image, spelled exactly: "The form", "The mechanism", "The run", "Reading it", the seven run lines as captured, and the six cards above.

Exclusions: no fifth pane, no altered output text or spacing, no paragraphs of text, no legend, no decorative icons, no watermark, no crossing arrows, no arrow terminating in whitespace.
```

Faithfulness note: The run lines match the note's captured run of affine.py character for character, double spaces included; markers 1 to 6 match affine-map-which-combinations-it-keeps.png. Every label in the image, exactly: "The form", "The mechanism", "The run", "Reading it", "$ python3 affine.py", the six output lines as captured, "1 f sends 0 to its offset", "2 weights add to 1: both ways 8.0", "3 weights add to 0: the offset is lost", "4 the plane: gap (1, -1) is the offset", "5 weights add to 1: both ways (4, 0)", "6 a shared vector: cancelled, then kept once".

## Process lane

Navigation: ⬅️ [Prompt 3 (Subject capstone): The deep-dive sheet](#prompt-3-subject-capstone-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
