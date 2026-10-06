# Diffusion Models: illustrated map

The drawn pictures for the vault note [[Diffusion Models]], sections [[Diffusion Models#The forward process in one jump]] and [[Diffusion Models#Composing models with a background]]. `6 prompts · 5 rendered · 1 stuck · 0 waiting`

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Glyph vocabulary](#glyph-vocabulary)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane: The forward process in one jump](#subject-lane-the-forward-process-in-one-jump)
- [Prompt 1 (Subject): The jump, the form](#prompt-1-subject-the-jump-the-form)
- [Prompt 2 (Subject): The jump, the mechanism](#prompt-2-subject-the-jump-the-mechanism)
- [Prompt 3 (Subject capstone): The jump, the deep-dive sheet](#prompt-3-subject-capstone-the-jump-the-deep-dive-sheet)
- [Subject lane: Composing models with a background](#subject-lane-composing-models-with-a-background)
- [Prompt 4 (Subject): Composition, the form](#prompt-4-subject-composition-the-form)
- [Prompt 5 (Subject): Composition, the mechanism](#prompt-5-subject-composition-the-mechanism)
- [Prompt 6 (Subject capstone): Composition, the deep-dive sheet](#prompt-6-subject-capstone-composition-the-deep-dive-sheet)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[Diffusion Models]]: subjects "The forward process in one jump" and "Composing models with a background", one sheet each. A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: no subject here needs a repeatable named look across the set. Zoom depth: one level, each section's form and mechanism, composed by its deep-dive sheet. The style paragraph is embedded verbatim at the head of every prompt.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. The wall, the ball and the cube in the composition form are generic objects, not real products.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

In the forward-process lane, blue is clean data, grey is noise and purple is the noised cloud. In the composition lane, blue is expert 1, orange is expert 2, grey is the background or wall, green is the composition with the background divided out, and purple is the plain product. Red: numbered output markers, and the one card that holds a hybrid.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A cloud of dots is a sample; an outline is a density contour; a dial is a weight. A wall split down the middle is a two-pixel scene, a ball or a cube on it is an object, and a blended ball-cube is a hybrid. A struck-through pair is a precision that cancels. All primary tier.

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Left to right: input, operation, result, and in the mechanism pictures, increasing noise. In the composition grid, rows are the two versions and columns the two halves.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane: The forward process in one jump](#subject-lane-the-forward-process-in-one-jump) ➡️

Numbered markers only on the deep-dive sheets' run panes, matching the numbered fields of the note's output picture or reading table. No step badges or phase containers.

## Subject lane: The forward process in one jump
<!-- student-read: 2026-10-05 job 20261005-001727-095bff -->

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The jump, the form](#prompt-1-subject-the-jump-the-form) ➡️

The form, the mechanism and the deep-dive sheet for [[Diffusion Models#The forward process in one jump]].

### Prompt 1 (Subject): The jump, the form

Navigation: ⬅️ [Subject lane: The forward process in one jump](#subject-lane-the-forward-process-in-one-jump) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The jump, the mechanism](#prompt-2-subject-the-jump-the-mechanism) ➡️

[planned] 🖼️ rendered 2026-10-04 forward-process-the-form.webp
Save as: `../Artificial Intelligence/Generative Modeling/assets/forward-process-the-form.webp`

Visual thesis: The noised cloud is the clean cloud scaled by the square root of abar plus fresh noise scaled by the square root of one minus abar.

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

Scene: Left to right on equal-scale axes from -5 to 5. A clean cloud of blue dots centred at (-2, 0), twice as tall as wide, labelled x0, expert 1. A plus sign. A round cloud of grey dots at the origin labelled eps ~ N(0, I). Above the blue cloud a dial reading sqrt(abar) = 0.707, above the grey cloud a dial reading sqrt(1 - abar) = 0.707, and between them the tag abar = 0.5. An equals sign, then the noised cloud of purple dots centred at (-1.41, 0), as wide as the clean one and less tall, labelled x_t. Under the whole row, one line: x_t = sqrt(abar) x0 + sqrt(1 - abar) eps.

Cast: the clean cloud (blue), the noise cloud (grey), the noised cloud (purple), two dials.

Flows: none beyond the plus and equals signs.

Text in the image, spelled exactly: "x0, expert 1", "eps ~ N(0, I)", "abar = 0.5", "sqrt(abar) = 0.707", "sqrt(1 - abar) = 0.707", "x_t", "x_t = sqrt(abar) x0 + sqrt(1 - abar) eps".

Exclusions: no other noise levels, no reverse process, no neural network. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The purple cloud is centred at (-1.41, 0), with variance 1 along x1 and 2.5 along x2, so it is as wide as the blue cloud and shorter; blue is clean data, grey is noise, purple is the noised result. Every label in the image, exactly: "x0, expert 1", "eps ~ N(0, I)", "abar = 0.5", "sqrt(abar) = 0.707", "sqrt(1 - abar) = 0.707", "x_t", "x_t = sqrt(abar) x0 + sqrt(1 - abar) eps".

### Prompt 2 (Subject): The jump, the mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The jump, the form](#prompt-1-subject-the-jump-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject capstone): The jump, the deep-dive sheet](#prompt-3-subject-capstone-the-jump-the-deep-dive-sheet) ➡️

[planned] 🖼️ rendered 2026-10-05 forward-process-the-mechanism.webp
Save as: `../Artificial Intelligence/Generative Modeling/assets/forward-process-the-mechanism.webp`

Visual thesis: As abar falls, the cloud's centre slides toward 0 by the square root of abar and each axis's variance heads toward 1.

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

Scene: Three panels left to right on identical axes from -5 to 5, one per level. Panel 1, abar = 1.0: the contour of expert 1 centred at (-2, 0), narrow along x1 and twice as tall along x2, labelled mean (-2, 0), var (1, 4). Panel 2, abar = 0.5: the contour centred at (-1.41, 0), labelled mean (-1.41, 0), var (1, 2.5). Panel 3, abar = 0.0058: an almost round contour of radius about 1 centred at (-0.15, 0), labelled mean (-0.15, 0), var (1.0, 1.02). In every panel a faint grey unit circle at the origin labelled pure noise, and a small dot at the contour's centre. Axis labels x1 and x2.

Cast: three contours (purple), three centre dots, three faint unit circles.

Flows: one thin arrow between panels labelled more noise.

Text in the image, spelled exactly: "abar = 1.0", "abar = 0.5", "abar = 0.0058", "mean (-2, 0), var (1, 4)", "mean (-1.41, 0), var (1, 2.5)", "mean (-0.15, 0), var (1.0, 1.02)", "pure noise", "more noise", "x1", "x2".

Exclusions: no point clouds of dots, no fourth level, no reverse arrows. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The contours' centres and variances match the listed values; the x1 width stays the same in all three panels while the x2 height shrinks; panel 3's contour nearly coincides with the unit circle. Every label in the image, exactly: "abar = 1.0", "abar = 0.5", "abar = 0.0058", "mean (-2, 0), var (1, 4)", "mean (-1.41, 0), var (1, 2.5)", "mean (-0.15, 0), var (1.0, 1.02)", "pure noise", "more noise", "x1", "x2".

### Prompt 3 (Subject capstone): The jump, the deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The jump, the mechanism](#prompt-2-subject-the-jump-the-mechanism) | 📋 [TOC](#table-of-contents) | [Subject lane: Composing models with a background](#subject-lane-composing-models-with-a-background) ➡️

[planned] 🖼️ rendered 2026-10-05 forward-process-deep-dive-sheet.webp
Save as: `../Artificial Intelligence/Generative Modeling/assets/forward-process-deep-dive-sheet.webp`

Visual thesis: The jump mixes clean data and noise by square-root weights, and the run's measured means and variances match the closed form at every level.

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

Scene: Pane 1, The form: a compact reminder of prompt 1, the two clouds, the two dials and the line x_t = sqrt(abar) x0 + sqrt(1 - abar) eps. Pane 2, The mechanism: a compact reminder of prompt 2, the three contours at abar = 1.0, 0.5 and 0.0058. Pane 3, The run: five lines of monospace output, exactly: $ ~/.vault-sandbox/bin/python noised.py | (3, 100000, 2) | level 1.0 measured [-2.0, -0.0] [1.0, 4.0] | closed form [-2.0, 0.0] [1.0, 4.0] | level 0.5 measured [-1.41, 0.0] [1.0, 2.5] | closed form [-1.41, 0.0] [1.0, 2.5] | level 0.0058 measured [-0.15, -0.0] [0.99, 1.02] | closed form [-0.15, 0.0] [1.0, 1.02] (here the | between lines marks a new line, while the | inside each level line is printed; the output has exactly four lines after the command). Red markers: 1 over (3, 100000, 2); 2 over the level 0.5 measured mean [-1.41, 0.0]; 3 over its measured variance [1.0, 2.5]; 4 over its closed form [-1.41, 0.0] [1.0, 2.5]; 5 over the level 0.0058 measured variance [0.99, 1.02]. Pane 4, Reading it: five cards in order.

Cast: the reminders, the output block, five numbered field cards.

Flows: none between panes.

Text in the image, spelled exactly: "The form", "The mechanism", "The run", "Reading it", "x_t = sqrt(abar) x0 + sqrt(1 - abar) eps", "$ ~/.vault-sandbox/bin/python noised.py", "(3, 100000, 2)", "level 1.0 measured [-2.0, -0.0] [1.0, 4.0] | closed form [-2.0, 0.0] [1.0, 4.0]", "level 0.5 measured [-1.41, 0.0] [1.0, 2.5] | closed form [-1.41, 0.0] [1.0, 2.5]", "level 0.0058 measured [-0.15, -0.0] [0.99, 1.02] | closed form [-0.15, 0.0] [1.0, 1.02]", "1 three levels, each a full cloud", "2 centre moved toward 0 by sqrt(0.5)", "3 narrow axis stays 1, wide axis shrinks", "4 the closed form: equals fields 2 and 3", "5 almost pure noise: both axes near 1".

Exclusions: no fifth pane, no leader lines between panes, no altered output text. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The output lines match the note's captured run character for character; markers 1 to 5 sit over the same fields as the note's rendered output picture; four panes only. Every label in the image, exactly: "The form", "The mechanism", "The run", "Reading it", "x_t = sqrt(abar) x0 + sqrt(1 - abar) eps", "$ ~/.vault-sandbox/bin/python noised.py", "(3, 100000, 2)", "level 1.0 measured [-2.0, -0.0] [1.0, 4.0] | closed form [-2.0, 0.0] [1.0, 4.0]", "level 0.5 measured [-1.41, 0.0] [1.0, 2.5] | closed form [-1.41, 0.0] [1.0, 2.5]", "level 0.0058 measured [-0.15, -0.0] [0.99, 1.02] | closed form [-0.15, 0.0] [1.0, 1.02]", "1 three levels, each a full cloud", "2 centre moved toward 0 by sqrt(0.5)", "3 narrow axis stays 1, wide axis shrinks", "4 the closed form: equals fields 2 and 3", "5 almost pure noise: both axes near 1".

## Subject lane: Composing models with a background

Navigation: ⬅️ [Prompt 3 (Subject capstone): The jump, the deep-dive sheet](#prompt-3-subject-capstone-the-jump-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents) | [Prompt 4 (Subject): Composition, the form](#prompt-4-subject-composition-the-form) ➡️

The form, the mechanism and the deep-dive sheet for [[Diffusion Models#Composing models with a background]].

### Prompt 4 (Subject): Composition, the form

Navigation: ⬅️ [Subject lane: Composing models with a background](#subject-lane-composing-models-with-a-background) | 📋 [TOC](#table-of-contents) | [Prompt 5 (Subject): Composition, the mechanism](#prompt-5-subject-composition-the-mechanism) ➡️

[planned] 🖼️ rendered 2026-10-05 composition-the-form.webp
Save as: `../Artificial Intelligence/Generative Modeling/assets/composition-the-form.webp`

Visual thesis: A two-pixel scene is a wall split into a left half and a right half; each expert puts an object in one half and repeats the wall elsewhere; the rule multiplies the experts and divides out the wall once.

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

Scene: Top: an empty grey wall drawn as a real plastered wall, split by a faint vertical line into two halves labelled x0, the left half and x1, the right half, captioned p_b, the empty wall. Below it, two rows. Row split: two small walls; the first with a blue ball in the left half, labelled p_1, object in the left half; the second with an orange cube in the right half, labelled p_2, object in the right half; then an arrow to a composed wall holding the blue ball on the left and the orange cube on the right, labelled co-occurrence. Row shared: the same p_1 wall; a wall with the orange cube in the left half, labelled p_2, another object in the left half; then an arrow to a composed wall holding a single object in the left half that is half ball, half cube, blue and orange blended, labelled hybrid. Along the bottom, the rule: C = p_b x (p_1 / p_b) x (p_2 / p_b).

Cast: the empty wall, the blue ball, the orange cube, the blended object, five small walls.

Flows: one arrow per row from the pair of experts to the composed wall.

Text in the image, spelled exactly: "x0, the left half", "x1, the right half", "p_b, the empty wall", "split", "shared", "p_1, object in the left half", "p_2, object in the right half", "p_2, another object in the left half", "co-occurrence", "hybrid", "C = p_b x (p_1 / p_b) x (p_2 / p_b)".

Exclusions: no Gaussian curves, no numbers, no real product or brand, no people or animals. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: In split the composed wall holds both objects, one per half; in shared it holds one blended object in the left half and nothing new in the right half; blue is expert 1, orange expert 2, grey the wall. Every label in the image, exactly: "x0, the left half", "x1, the right half", "p_b, the empty wall", "split", "shared", "p_1, object in the left half", "p_2, object in the right half", "p_2, another object in the left half", "co-occurrence", "hybrid", "C = p_b x (p_1 / p_b) x (p_2 / p_b)".

### Prompt 5 (Subject): Composition, the mechanism

Navigation: ⬅️ [Prompt 4 (Subject): Composition, the form](#prompt-4-subject-composition-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 6 (Subject capstone): Composition, the deep-dive sheet](#prompt-6-subject-capstone-composition-the-deep-dive-sheet) ➡️

[planned] 🖼️ rendered 2026-10-05 composition-the-mechanism.webp
Save as: `../Artificial Intelligence/Generative Modeling/assets/composition-the-mechanism.webp`

Visual thesis: In every half where an expert equals the wall, its precision cancels the wall's and the other expert decides alone; in shared's left half neither cancels, so the two pull against each other and land on -1.5.

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

Scene: A 2 by 2 grid of cards: rows split and shared, columns left half and right half. Each card shows its precision sum on one line, with the cancelling pair struck through in grey, then its result. Split, left half: P = 1/1 + 1/4 - 1/4 = 1, with + 1/4 - 1/4 struck, result mean -2, expert 1 decides. Split, right half: P = 1/4 + 1/1 - 1/4 = 1, with 1/4 ... - 1/4 struck, result mean 2, expert 2 decides. Shared, right half: P = 1/4 + 1/1 - 1/4 = 1, with the 1/4 pair struck, result mean 0, expert 2 narrows it. Shared, left half, highlighted with a red border: P = 1/1 + 1/4 - 1/4 = 1, nothing struck, B = -2 + 0.5 = -1.5, result mean -1.5, and a small number line from -2 to +2 with a blue dot at -2, an orange dot at +2 and a green dot at -1.5, labelled hybrid: neither -2 nor +2.

Cast: four precision cards, grey strike-throughs, one small number line.

Flows: none.

Text in the image, spelled exactly: "split", "shared", "left half", "right half", "P = 1/1 + 1/4 - 1/4 = 1", "P = 1/4 + 1/1 - 1/4 = 1", "mean -2, expert 1 decides", "mean 2, expert 2 decides", "mean 0, expert 2 narrows it", "B = -2 + 0.5 = -1.5", "mean -1.5", "hybrid: neither -2 nor +2".

Exclusions: no 2D plot, no third expert, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Exactly three cards show a struck cancelling pair; the shared left-half card has none and carries the red border; its number line places the green dot at -1.5. Every label in the image, exactly: "split", "shared", "left half", "right half", "P = 1/1 + 1/4 - 1/4 = 1", "P = 1/4 + 1/1 - 1/4 = 1", "mean -2, expert 1 decides", "mean 2, expert 2 decides", "mean 0, expert 2 narrows it", "B = -2 + 0.5 = -1.5", "mean -1.5", "hybrid: neither -2 nor +2".

### Prompt 6 (Subject capstone): Composition, the deep-dive sheet

Navigation: ⬅️ [Prompt 5 (Subject): Composition, the mechanism](#prompt-5-subject-composition-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[planned] ⚠️ stuck: pixel check, pane 3 marked points off the note's saved figure (split composition near (-2.65, 1.9) not (-2.0, 2.0); shared composition near -2.2 not -1.5; shared experts centred near -3 and +3 not -2 and +2), after 3 revisions; cards, markers and labels correct; last attempt ~/.cache/codex-drop/obsidian/dm-comp-sheet.png
Save as: `../Artificial Intelligence/Generative Modeling/assets/composition-deep-dive-sheet.webp`

Visual thesis: Dividing out the wall gives co-occurrence at (-2, 2) when each expert owns its half, and a hybrid at (-1.5, 0) when both want the same half.

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

Scene: Pane 1, The form: a compact reminder of prompt 4, the wall, the split row ending in co-occurrence and the shared row ending in hybrid. Pane 2, The mechanism: a compact reminder of prompt 5, the 2 by 2 grid with the shared left-half card highlighted. Pane 3, The picture: two square plots side by side, titled split: expert 2 owns the right half and shared: both experts want the left half, axes x0, the left half and x1, the right half from -7 to 7. Each shows the wall as a grey contour, expert 1 in blue, expert 2 in orange, a green filled round contour with a green dot at the composition, and a purple cross at the plain product. Split: green dot at (-2.0, 2.0), purple cross at (-1.6, 1.6). Shared: green dot at (-1.5, 0.0), purple cross at (-1.2, 0.0). Red markers: 1 on split's green dot, 2 on split's purple cross, 3 on shared's green dot, 4 on shared's purple cross, 5 on split's green filled contour. Pane 4, Reading it: five cards in order.

Cast: the reminders, the two plots, five numbered field cards.

Flows: none between panes.

Text in the image, spelled exactly: "The form", "The mechanism", "The picture", "Reading it", "split: expert 2 owns the right half", "shared: both experts want the left half", "x0, the left half", "x1, the right half", "1 split, p1 p2 / p_b at (-2.0, 2.0): co-occurrence", "2 split, p1 p2 at (-1.6, 1.6): the wall counted twice", "3 shared, p1 p2 / p_b at (-1.5, 0.0): a hybrid", "4 shared, p1 p2 at (-1.2, 0.0): pulled further toward 0", "5 the composed cloud: variance 1 on each axis".

Exclusions: no fifth pane, no leader lines between panes, no positions other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The four marked positions match the note's saved figure, composition-split-and-shared.png; markers 1 to 5 follow the note's reading table; four panes only. Every label in the image, exactly: "The form", "The mechanism", "The picture", "Reading it", "split: expert 2 owns the right half", "shared: both experts want the left half", "x0, the left half", "x1, the right half", "1 split, p1 p2 / p_b at (-2.0, 2.0): co-occurrence", "2 split, p1 p2 at (-1.6, 1.6): the wall counted twice", "3 shared, p1 p2 / p_b at (-1.5, 0.0): a hybrid", "4 shared, p1 p2 at (-1.2, 0.0): pulled further toward 0", "5 the composed cloud: variance 1 on each axis".

## Process lane

Navigation: ⬅️ [Prompt 6 (Subject capstone): Composition, the deep-dive sheet](#prompt-6-subject-capstone-composition-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
