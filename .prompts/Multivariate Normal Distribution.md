# Multivariate Normal Distribution: illustrated map

The drawn pictures for the vault note [[Multivariate Normal Distribution]], sections [[Multivariate Normal Distribution#Diagonal covariance]], [[Multivariate Normal Distribution#Sampling a diagonal Gaussian]] and [[Multivariate Normal Distribution#Products and quotients of diagonal Gaussians]]. `9 prompts · 7 rendered · 2 stuck · 0 waiting`

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
- [Subject lane: Sampling a diagonal Gaussian](#subject-lane-sampling-a-diagonal-gaussian)
- [Prompt 3 (Subject): Sampling, the form](#prompt-3-subject-sampling-the-form)
- [Prompt 4 (Subject): Sampling, the mechanism](#prompt-4-subject-sampling-the-mechanism)
- [Prompt 5 (Subject capstone): Sampling, the deep-dive sheet](#prompt-5-subject-capstone-sampling-the-deep-dive-sheet)
- [Subject lane: Products and quotients of diagonal Gaussians](#subject-lane-products-and-quotients-of-diagonal-gaussians)
- [Prompt 6 (Subject): Precisions, the form](#prompt-6-subject-precisions-the-form)
- [Prompt 7 (Subject): Precisions, the mechanism](#prompt-7-subject-precisions-the-mechanism)
- [Prompt 8 (Subject capstone): Precisions, the deep-dive sheet](#prompt-8-subject-capstone-precisions-the-deep-dive-sheet)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[Multivariate Normal Distribution]]: subjects "Diagonal covariance", "Sampling a diagonal Gaussian" and "Products and quotients of diagonal Gaussians", one sheet each. A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: no subject here needs a repeatable named look across the set. Zoom depth: one level, the section's form and mechanism, composed by the deep-dive sheet. The style paragraph is embedded verbatim at the head of every prompt.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. Nothing in these pictures is a real-world object or a real product.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Blue: the mean and the 2D surface's shape. Orange: a variance, or a one-dimensional bell's height. Purple: the 2D surface's height at a point. Red: numbered output markers only. In the sampling lane, grey is the standard-normal draws and orange the standard deviation. In the precisions lane, blue is expert 1, orange expert 2, grey the background and green the composition.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A dot is a mean. An oval outline is a contour of the density. A double arrow across the oval is a spread along one axis. A rounded card with slots is a NumPy array. All primary tier. A neutral grey bracket is a measured length, labelled as a standard deviation and never as a variance. A vertical bar is a precision; a bar below the baseline is a subtracted one.

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Left to right: what is stored, then what it draws, then what it computes. Vertical position carries density height in the mechanism picture.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Numbered markers only on the deep-dive sheet's output pane, matching the numbered fields in the note's output picture. No step badges or phase containers.

## Subject lane
<!-- student-read: 2026-10-04 job 20261004-193336-6e3d5a -->

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The form](#prompt-1-subject-the-form) ➡️

The form, the mechanism, then the deep-dive sheet that composes them with the run's output, per the vault-note exception in the illustration style guide.

### Prompt 1 (Subject): The form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism) ➡️

[planned] 🖼️ rendered 2026-10-04 diagonal-gaussian-the-form.webp
Save as: `../Mathematics/Statistics/Distributions/assets/diagonal-gaussian-the-form.webp`

Visual thesis: The mean array places the centre; the variance array determines the squared spreads along the two coordinate axes.

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

Production: Use a deterministic figure script for the plot, geometry and typography. Compose at 800 px reading width; every teaching label must remain legible at that width.

Scene: Read left to right, from two compact array cards to one large coordinate plot. The mean card contains two populated slots, -2 and 0. The variance card contains two populated slots, 1 and 4. Label the columns x1 and x2 once, above the cards. Each card shows shape (2,). Place mu = (-2, 0) and var = (1, 4) as the respective card headings. Put Sigma = diag(1, 4) immediately below the variance card.

The plot is the focal element. Use equal physical scale on both axes. Draw the blue mean dot at (-2, 0), with an axis-aligned blue contour extending one unit horizontally and two units vertically from its centre. Use a faint grid and only useful coordinate ticks. Identify the outline as a density contour.

Teach the spread without labelling a length as a variance. Keep variance 1 and variance 4 beside the corresponding variance-array entries. On the plot, mark centre-to-contour distances with neutral measurement brackets, labelled standard deviation 1 and standard deviation 2. Add the short caption: Contour semiaxes show standard deviations, the square roots of the variances.

Flows: One short blue connector from the mean card to the centre dot. Use coordinate labels to pair the variance entries with their axes; do not route orange connectors around the page. Orange highlights variance entries only. Blue identifies the mean and contour. Neutral grey brackets are geometric measurements, not another data series.

Required original labels: mu = (-2, 0); var = (1, 4); x1; x2; variance 1; variance 4; shape (2,); Sigma = diag(1, 4).

Additional teaching labels: Mean; Variance; density contour; standard deviation 1; standard deviation 2; Contour semiaxes show standard deviations, the square roots of the variances.

Exclusions: no empty array slots, no full-diameter arrow labelled variance, no tilted ellipse, no 3D surface, no second Gaussian, no oversized legend strip, no repeated decorative icons, no connectors around the perimeter, no orphan arrows, no tiny labels, no watermark.
```

Faithfulness note: The oval must be taller than wide by a factor of two (standard deviations 1 and 2) and aligned with the axes; the mean dot sits at x1 = -2 on the x1 axis; the eight original labels are exactly mu = (-2, 0), var = (1, 4), x1, x2, variance 1, variance 4, shape (2,), Sigma = diag(1, 4); blue means the mean, orange means a variance. It also carries the teaching labels Mean, Variance, density contour, standard deviation 1, standard deviation 2, and the caption "Contour semiaxes show standard deviations, the square roots of the variances."; the variance labels sit beside the stored entries, never on a drawn length.

### Prompt 2 (Subject): The mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The form](#prompt-1-subject-the-form) | 📋 [TOC](#table-of-contents) | [Subject capstone: The deep-dive sheet](#subject-capstone-the-deep-dive-sheet) ➡️

[planned] 🖼️ rendered 2026-10-04 diagonal-gaussian-the-mechanism.webp
Save as: `../Mathematics/Statistics/Distributions/assets/diagonal-gaussian-the-mechanism.webp`

Visual thesis: For a diagonal Gaussian, the coordinates are independent, so multiplying their marginal density heights gives the joint density height.

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

Production: Use a deterministic figure script for the density curves, surface, coordinates and typography. Design for reading at 800 px wide.

Scene: Begin with a small, explicit example label: This calculation uses mu = (0, 0), with var = (1, 4). Under it write: Diagonal covariance makes the Gaussian coordinates independent.

Across the upper row, place the two marginal plots side by side. Give them the same horizontal coordinate scale and the same density-height scale so the second bell visibly spreads wider and peaks lower. Titles: Marginal density of x1 and Marginal density of x2. Label each horizontal axis, show the mean at 0, and label the evaluated coordinate at the foot of its dashed vertical guide: 1 for x1 and 2 for x2. Use blue curves and orange evaluation dots. Put N(1; 0, 1) = 0.2420 and N(2; 0, 4) = 0.1210 beside their respective marks. A small key says: N(value; mean, variance).

Immediately below, give the product the strongest typographic emphasis: 0.2420 x 0.1210 = 0.0293. Colour the factors orange and the result purple. Two short downward arrows connect the marginal marks to their factors.

Below the product, place the joint surface N(0, diag(1, 4)), wider along x2. Label the floor axes x1 and x2. Show the floor point x = (1, 2) with short coordinate guides, and erect a purple vertical stick from it to the surface. Label the top directly: Joint density height 0.0293. One short purple connector carries the product result to this label. Keep the surface translucent enough to see the stick.

End with the caption: Multiply the two marginal heights to get the joint height at the chosen point.

Colour meanings: blue curves and surface shape; orange marginal density heights; purple joint density height. Direct labels replace a separate legend panel.

Exclusions: no unexplained change of mean, no unlabelled evaluation coordinates, no correlation or tilted principal axes, no long looping arrows, no oversized legend, no probability label for a density height, no extra numerical example, no watermark.
```

Faithfulness note: The heights are exactly 0.2420 and 0.1210 and their product 0.0293, matching the note's run (0.241971, 0.120985, 0.029275); the surface is wider along x2 than x1; the stick stands at (1, 2); orange means a single-coordinate bell's height, purple the 2D surface's height. It also carries "This calculation uses mu = (0, 0), with var = (1, 4).", "Diagonal covariance makes the Gaussian coordinates independent.", "Marginal density of x1", "Marginal density of x2", "N(value; mean, variance)", "Joint density height 0.0293" and the caption "Multiply the two marginal heights to get the joint height at the chosen point."

### Subject capstone: The deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism) | 📋 [TOC](#table-of-contents) | [Subject lane: Sampling a diagonal Gaussian](#subject-lane-sampling-a-diagonal-gaussian) ➡️

[planned] 🖼️ rendered 2026-10-04 diagonal-gaussian-deep-dive-sheet.webp
Save as: `../Mathematics/Statistics/Distributions/assets/diagonal-gaussian-deep-dive-sheet.webp`

Visual thesis: Read the output field by field: the matrix and per-coordinate calculations give the same squared distance and the same joint density.

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

Production: Compose with a deterministic figure script. Use a tall sheet designed for display at 800 px wide, increasing its height until every label and output line is legible. Keep exactly four panes, stacked vertically. Do not shrink a landscape dashboard to fit. Use at least 20 px text at the intended display width for output and field explanations.

Pane 1, The form: A compact recap of the corrected form picture. Put the mean and variance entries inside their array slots, beside the axis-aligned ellipse centred at (-2, 0). Preserve mu = (-2, 0), var = (1, 4), x1, x2, variance 1, variance 4, shape (2,), and Sigma = diag(1, 4). Variance labels belong to the stored entries. Label the centre-to-contour lengths standard deviation 1 and standard deviation 2. Keep the two-to-one contour aspect ratio with equal axis scaling.

Pane 2, The mechanism: Begin with This calculation uses mu = (0, 0), with var = (1, 4). Use two adjacent marginal bells, their directly labelled orange heights and the product underneath. Preserve N(1; 0, 1) = 0.2420, N(2; 0, 4) = 0.1210, 0.2420 x 0.1210, = 0.0293, x1, x2 and x = (1, 2). Include a compact joint surface with a purple stick at (1, 2), wider along x2. Keep connectors short. State: Independent coordinates: multiply the marginal heights.

Pane 3, The run: This is the sheet's focal pane. Print all seven output lines in large, crisp monospace text, preserving every character below. Use generous line spacing. Place red markers 1 to 7 immediately above their corresponding result fields, without covering any character. The result fields are, in order: the covariance array; the first 2.0; the second 2.0; the first 0.029275; the array of marginal heights; the second 0.029275; 0.1995. Use subtle neutral emphasis to pair the two quadratic results and to pair the two density results.

Sigma: [[1.0, 0.0], [0.0, 4.0]]
quad, full matrix: 2.0
quad, per coordinate: 2.0
density, full matrix: 0.029275
1D bells: [0.241971 0.120985]
density, product of bells: 0.029275
bell height at c2 = 0, var 4: 0.1995

Pane 4, Reading it: Seven full-width cards in the same order as the output. Red numbers identify the matching fields. No leader lines between panes are needed. Use these proposed card labels:
1 Sigma: variances on the diagonal
2 quad: sum of squared standardized offsets
3 same sum, no matrix
4 surface height at (1, 2)
5 one bell per coordinate
6 bells multiplied: equals field 4
7 slice scale factor: fixing x2 at 0 multiplies the x1 bell by 0.1995

Colour meanings stay consistent: blue mean and density shape; orange variance entries or marginal heights; purple joint density height; red numbered output markers only. Keep any colour key to a single compact line within a pane, not a fifth container.

Exclusions: no fifth pane, no tiny nested dashboard, no empty slots, no length labelled as a variance, no unexplained change of mean, no quadratic form labelled as unsquared distance, no leader lines crossing between panes, no red numerical emphasis apart from markers, no altered output text, no watermark.
```

Faithfulness note: Every output line matches the note's captured run character for character; markers 1 to 7 sit over the same fields as the rendered output picture; the field cards say exactly the listed text; panes 1 and 2 carry the same labels and values as prompts 1 and 2; four panes only. The field cards now read exactly: "1 Sigma: variances on the diagonal", "2 quad: sum of squared standardized offsets", "3 same sum, no matrix", "4 surface height at (1, 2)", "5 one bell per coordinate", "6 bells multiplied: equals field 4", "7 slice scale factor: fixing x2 at 0 multiplies the x1 bell by 0.1995"; pane 2 opens with "This calculation uses mu = (0, 0), with var = (1, 4)." and states "Independent coordinates: multiply the marginal heights."

## Subject lane: Sampling a diagonal Gaussian

Navigation: ⬅️ [Subject capstone: The deep-dive sheet](#subject-capstone-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject): Sampling, the form](#prompt-3-subject-sampling-the-form) ➡️

The form, the mechanism and the deep-dive sheet for [[Multivariate Normal Distribution#Sampling a diagonal Gaussian]].

### Prompt 3 (Subject): Sampling, the form

Navigation: ⬅️ [Subject lane: Sampling a diagonal Gaussian](#subject-lane-sampling-a-diagonal-gaussian) | 📋 [TOC](#table-of-contents) | [Prompt 4 (Subject): Sampling, the mechanism](#prompt-4-subject-sampling-the-mechanism) ➡️

[planned] ⚠️ stuck: pixel check, panel 3 cloud is 2.6 times taller than wide (note says 2) and centred near x1 = -2.7, after 3 revisions; last attempt ~/.cache/codex-drop/obsidian/mvn-samp-form.png
Save as: `../Mathematics/Statistics/Distributions/assets/sampling-the-form.webp`

Visual thesis: A sample from a diagonal Gaussian is a standard-normal point, moved by the mean and stretched along each axis by the standard deviation, the square root of that axis's variance.

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

Scene: Three panels left to right on one shared, equal-scale grid from -6 to 6 on both axes. Panel 1: a round cloud of about 300 grey dots centred at the origin, titled with the label eps ~ N(0, I) and the tag shape (n, 2). Panel 2: an operation card holding the line x = mu + np.sqrt(var) * eps, and under it two array cards with their entries inside the slots: mu = (-2, 0) in blue, and np.sqrt(var) = (1, 2) in orange, with var = (1, 4) written small beside the orange card. Panel 3: the same dots moved to a cloud centred at (-2, 0), as wide as panel 1's along x1 and twice as tall along x2, with a blue dot at its centre. In panel 3 draw two neutral grey measurement brackets from the centre: horizontal, labelled standard deviation 1; vertical, labelled standard deviation 2. Axis labels x1 and x2 on panels 1 and 3.

Cast: the standard-normal cloud (grey dots), the operation card, the mean array card (blue), the standard-deviation array card (orange), the moved cloud (blue dots) with its centre dot, two grey brackets.

Flows: one short arrow from panel 1 into the operation card, and one short arrow from the operation card to panel 3. No other connectors.

Text in the image, spelled exactly: "eps ~ N(0, I)", "shape (n, 2)", "x = mu + np.sqrt(var) * eps", "mu = (-2, 0)", "np.sqrt(var) = (1, 2)", "var = (1, 4)", "standard deviation 1", "standard deviation 2", "x1", "x2".

Exclusions: no length labelled as a variance, no tilted cloud, no second Gaussian, no empty array slots, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Panel 3's cloud is centred at (-2, 0) and twice as tall along x2 as it is wide along x1, aligned with the axes; panel 1's cloud is round at the origin; the brackets are labelled standard deviations 1 and 2, never variances; blue means the mean, orange the standard deviation, grey the standard-normal draws. Every label in the image, exactly: "eps ~ N(0, I)", "shape (n, 2)", "x = mu + np.sqrt(var) * eps", "mu = (-2, 0)", "np.sqrt(var) = (1, 2)", "var = (1, 4)", "standard deviation 1", "standard deviation 2", "x1", "x2".

### Prompt 4 (Subject): Sampling, the mechanism

Navigation: ⬅️ [Prompt 3 (Subject): Sampling, the form](#prompt-3-subject-sampling-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 5 (Subject capstone): Sampling, the deep-dive sheet](#prompt-5-subject-capstone-sampling-the-deep-dive-sheet) ➡️

[planned] 🖼️ rendered 2026-10-04 sampling-the-mechanism.webp
Save as: `../Mathematics/Statistics/Distributions/assets/sampling-the-mechanism.webp`

Visual thesis: Shifting a standard-normal variable by m moves its bell without changing its width, and multiplying it by s widens the bell so its variance becomes s squared; one coordinate at a time, that turns N(0, 1) into N(m, sigma^2).

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

Scene: Two rows, one per coordinate, each read left to right on a shared horizontal scale from -6 to 6. Row 1, titled coordinate x1: a standard bell centred at 0, an arrow labelled + (-2), then the same-width bell centred at -2, labelled N(-2, 1). Row 2, titled coordinate x2: a standard bell centred at 0, an arrow labelled x 2, then a bell centred at 0 that is twice as wide and half as tall, labelled N(0, 4). Each standard bell is labelled N(0, 1). Under both rows, a compact check strip: stored var (1, 4) beside measured var [1.0, 4.02], with the caption: the measured variance matches the stored one within sampling error.

Cast: four bells (grey for the standard bells, blue for the results), two operation arrows, the check strip.

Flows: within each row, one arrow from the standard bell to the result bell, carrying its operation label. Nothing crosses between rows.

Text in the image, spelled exactly: "coordinate x1", "coordinate x2", "N(0, 1)", "+ (-2)", "N(-2, 1)", "x 2", "N(0, 4)", "stored var (1, 4)", "measured var [1.0, 4.02]", "the measured variance matches the stored one within sampling error".

Exclusions: no third coordinate, no 2D surface, no change of mean in row 2, no change of width in row 1. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Row 1's result bell has the same width and height as its standard bell and sits at -2; row 2's result bell sits at 0 and is twice as wide and half as tall; the check strip's numbers are the note's run, 4.02 for the second coordinate. Every label in the image, exactly: "coordinate x1", "coordinate x2", "N(0, 1)", "+ (-2)", "N(-2, 1)", "x 2", "N(0, 4)", "stored var (1, 4)", "measured var [1.0, 4.02]", "the measured variance matches the stored one within sampling error".

### Prompt 5 (Subject capstone): Sampling, the deep-dive sheet

Navigation: ⬅️ [Prompt 4 (Subject): Sampling, the mechanism](#prompt-4-subject-sampling-the-mechanism) | 📋 [TOC](#table-of-contents) | [Subject lane: Products and quotients of diagonal Gaussians](#subject-lane-products-and-quotients-of-diagonal-gaussians) ➡️

[planned] ⚠️ stuck: pixel check, pane 1 moved cloud is 1.7x the grey cloud's width and 1.74x taller than wide (should match width, 2x tall); labels N(0,1), N(-2,1), N(0,4) lack the spaces; run pane and cards correct; last attempt ~/.cache/codex-drop/obsidian/mvn-samp-sheet.png
Save as: `../Mathematics/Statistics/Distributions/assets/sampling-deep-dive-sheet.webp`

Visual thesis: Sampling is a shift and a stretch, and the run's measured mean and variance confirm the stored arrays field by field.

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

Scene: Pane 1, The form: a compact reminder of prompt 3, the round cloud, the line x = mu + np.sqrt(var) * eps, and the moved cloud centred at (-2, 0) with brackets standard deviation 1 and standard deviation 2. Pane 2, The mechanism: a compact reminder of prompt 4, the two rows N(0, 1) to N(-2, 1) by + (-2), and N(0, 1) to N(0, 4) by x 2. Pane 3, The run: four lines of monospace output, exactly: $ ~/.vault-sandbox/bin/python samples.py | p_b (100000, 2) mean [0.0, -0.0] var [4.02, 4.0] | p_1 (100000, 2) mean [-2.0, -0.0] var [1.0, 4.02] | p_2 (100000, 2) mean [2.01, 0.0] var [4.01, 1.0] (the | marks a new line and is not printed). Red markers 1, 2, 3 sit just above (100000, 2), [-2.0, -0.0] and [1.0, 4.02] on the p_1 line, lightly underlined. Pane 4, Reading it: three cards in order.

Cast: the reminder clouds and bells, the output block, three numbered field cards.

Flows: short arrows inside panes 1 and 2 only.

Text in the image, spelled exactly: "The form", "The mechanism", "The run", "Reading it", "x = mu + np.sqrt(var) * eps", "standard deviation 1", "standard deviation 2", "N(0, 1)", "+ (-2)", "N(-2, 1)", "x 2", "N(0, 4)", "$ ~/.vault-sandbox/bin/python samples.py", "p_b (100000, 2) mean [0.0, -0.0] var [4.02, 4.0]", "p_1 (100000, 2) mean [-2.0, -0.0] var [1.0, 4.02]", "p_2 (100000, 2) mean [2.01, 0.0] var [4.01, 1.0]", "1 shape: one row per point, one column per coordinate", "2 mean: measured, against the stored (-2, 0)", "3 var: measured, about one standard error above 4".

Exclusions: no fifth pane, no leader lines between panes, no altered output text, no reversed marker order. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The output lines match the note's captured run character for character; markers 1 to 3 sit over the same fields as the note's rendered output picture; panes 1 and 2 carry prompts 3 and 4's values; four panes only. Every label in the image, exactly: "The form", "The mechanism", "The run", "Reading it", "x = mu + np.sqrt(var) * eps", "standard deviation 1", "standard deviation 2", "N(0, 1)", "+ (-2)", "N(-2, 1)", "x 2", "N(0, 4)", "$ ~/.vault-sandbox/bin/python samples.py", "p_b (100000, 2) mean [0.0, -0.0] var [4.02, 4.0]", "p_1 (100000, 2) mean [-2.0, -0.0] var [1.0, 4.02]", "p_2 (100000, 2) mean [2.01, 0.0] var [4.01, 1.0]", "1 shape: one row per point, one column per coordinate", "2 mean: measured, against the stored (-2, 0)", "3 var: measured, about one standard error above 4".

## Subject lane: Products and quotients of diagonal Gaussians
<!-- student-read: 2026-10-05 job 20261005-001727-b845ec -->

Navigation: ⬅️ [Prompt 5 (Subject capstone): Sampling, the deep-dive sheet](#prompt-5-subject-capstone-sampling-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents) | [Prompt 6 (Subject): Precisions, the form](#prompt-6-subject-precisions-the-form) ➡️

The form, the mechanism and the deep-dive sheet for [[Multivariate Normal Distribution#Products and quotients of diagonal Gaussians]].

### Prompt 6 (Subject): Precisions, the form

Navigation: ⬅️ [Subject lane: Products and quotients of diagonal Gaussians](#subject-lane-products-and-quotients-of-diagonal-gaussians) | 📋 [TOC](#table-of-contents) | [Prompt 7 (Subject): Precisions, the mechanism](#prompt-7-subject-precisions-the-mechanism) ➡️

[planned] 🖼️ rendered 2026-10-04 products-the-form.webp
Save as: `../Mathematics/Statistics/Distributions/assets/products-the-form.webp`

Visual thesis: Composing Gaussians adds the experts' precisions and subtracts the background's, and the composed mean is each mean weighted by its precision, summed the same way, over the composed precision.

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

Scene: One coordinate, the shared left half, worked as a picture. Top: three precision bars on one baseline, then an equals sign and a result bar. Expert 1's bar is blue, height 1, labelled 1/1 = 1. Expert 2's bar is orange, height one quarter of that, labelled 1/4 = 0.25. The background's bar is grey and hangs below the baseline, depth one quarter, labelled - 1/4 = -0.25. The result bar is green, height 1, labelled P = 1. Middle: one line of arithmetic, B = -2 x 1 + 2 x 0.25 - 0 x 0.25 = -1.5. Bottom: a number line from -3 to 3 with a blue dot at -2 labelled expert 1, an orange dot at +2 labelled expert 2, a grey dot at 0 labelled background, and a larger green dot at -1.5 labelled mean = B / P = -1.5. Beside the green dot, var = 1 / P = 1.

Cast: four precision bars, the arithmetic line, the number line with four dots.

Flows: none beyond the equals sign between the bars and the result bar.

Text in the image, spelled exactly: "1/1 = 1", "1/4 = 0.25", "- 1/4 = -0.25", "P = 1", "B = -2 x 1 + 2 x 0.25 - 0 x 0.25 = -1.5", "expert 1", "expert 2", "background", "mean = B / P = -1.5", "var = 1 / P = 1".

Exclusions: no second coordinate, no 2D plot, no bell curves, no bar heights other than 1, 0.25 and -0.25 in the proportions stated. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Expert 1's bar is four times expert 2's; the background bar hangs below the baseline with expert 2's size; the result bar equals expert 1's; the green dot sits at -1.5, three quarters of the way from 0 to -2; blue is expert 1, orange expert 2, grey the background, green the composition. Every label in the image, exactly: "1/1 = 1", "1/4 = 0.25", "- 1/4 = -0.25", "P = 1", "B = -2 x 1 + 2 x 0.25 - 0 x 0.25 = -1.5", "expert 1", "expert 2", "background", "mean = B / P = -1.5", "var = 1 / P = 1".

### Prompt 7 (Subject): Precisions, the mechanism

Navigation: ⬅️ [Prompt 6 (Subject): Precisions, the form](#prompt-6-subject-precisions-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 8 (Subject capstone): Precisions, the deep-dive sheet](#prompt-8-subject-capstone-precisions-the-deep-dive-sheet) ➡️

[planned] 🖼️ rendered 2026-10-04 products-the-mechanism.webp
Save as: `../Mathematics/Statistics/Distributions/assets/products-the-mechanism.webp`

Visual thesis: In log space, multiplying and dividing densities adds and subtracts parabolas, and the composed parabola's vertex is the composed mean while its curvature is the composed precision.

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

Scene: Main panel: a horizontal axis x from -5 to 5 and a vertical axis log density. Three parabolas: blue, opening downward, vertex at -2, curvature 1, labelled log p1, curvature 1; orange, opening downward, vertex at +2, flatter, labelled log p2, curvature 0.25; grey, opening upward, vertex at 0, as flat as the orange one, labelled - log p_b, curvature -0.25. Their sum, a thicker green parabola opening downward with its vertex at -1.5, labelled sum: curvature 1, vertex at -1.5. A thin vertical guide drops from the green vertex to the axis at -1.5. Small inset panel at the lower right, titled narrow background: the same three, with the grey parabola much steeper, and the green sum opening upward, labelled P = -0.75: not a density.

Cast: three component parabolas, the green sum, the vertex guide, the inset.

Flows: none; the parabolas share one axis.

Text in the image, spelled exactly: "x", "log density", "log p1, curvature 1", "log p2, curvature 0.25", "- log p_b, curvature -0.25", "sum: curvature 1, vertex at -1.5", "narrow background", "P = -0.75: not a density".

Exclusions: no density curves, no second coordinate, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The green parabola's vertex is at -1.5 and its curvature equals the blue one's; the grey parabola opens upward; in the inset the sum opens upward; colours match prompt 6. Every label in the image, exactly: "x", "log density", "log p1, curvature 1", "log p2, curvature 0.25", "- log p_b, curvature -0.25", "sum: curvature 1, vertex at -1.5", "narrow background", "P = -0.75: not a density".

### Prompt 8 (Subject capstone): Precisions, the deep-dive sheet

Navigation: ⬅️ [Prompt 7 (Subject): Precisions, the mechanism](#prompt-7-subject-precisions-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[planned] 🖼️ rendered 2026-10-04 products-deep-dive-sheet.webp
Save as: `../Mathematics/Statistics/Distributions/assets/products-deep-dive-sheet.webp`

Visual thesis: The composed precision, the weighted sum, the mean and the variance come from adding and subtracting, and the run shows the background moving split to (-2, 2) and shared to (-1.5, 0).

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

Scene: Pane 1, The form: a compact reminder of prompt 6, the four precision bars and the green dot at -1.5. Pane 2, The mechanism: a compact reminder of prompt 7, the three parabolas and the green sum with its vertex at -1.5. Pane 3, The run: five lines of monospace output, exactly: $ ~/.vault-sandbox/bin/python compose.py | split  p1 p2 / p_b  P [1.0, 1.0]  B [-2.0, 2.0]  mean [-2.0, 2.0]  var [1.0, 1.0] | split  p1 p2        P [1.25, 1.25]  B [-2.0, 2.0]  mean [-1.6, 1.6]  var [0.8, 0.8] | shared p1 p2 / p_b  P [1.0, 1.0]  B [-1.5, 0.0]  mean [-1.5, 0.0]  var [1.0, 1.0] | shared p1 p2        P [1.25, 1.25]  B [-1.5, 0.0]  mean [-1.2, 0.0]  var [0.8, 0.8] (the | marks a new line and is not printed; keep the runs of spaces). Red markers: 1 over P [1.0, 1.0], 2 over B [-2.0, 2.0], 3 over mean [-2.0, 2.0], 4 over var [1.0, 1.0], all on the first output line; 5 over mean [-1.6, 1.6] on the second; 6 over mean [-1.5, 0.0] on the third. Pane 4, Reading it: six cards in order.

Cast: the reminder bars and parabolas, the output block, six numbered field cards.

Flows: none between panes.

Text in the image, spelled exactly: "The form", "The mechanism", "The run", "Reading it", "P = 1", "mean = B / P = -1.5", "sum: curvature 1, vertex at -1.5", "$ ~/.vault-sandbox/bin/python compose.py", "1 P: the composed precision of each coordinate", "2 B: each mean times its precision, background taken away", "3 mean = B / P: each half takes its own expert's value", "4 var = 1 / P: as narrow as the narrow expert", "5 no background: the same B over P = 1.25, pulled toward 0", "6 shared: -1.5, a value neither expert put there".

Exclusions: no fifth pane, no leader lines between panes, no altered output text, no wrapped output line that loses its spacing. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The four output lines match the note's captured run character for character, runs of spaces included; markers 1 to 6 sit over the same fields as the note's rendered output picture; four panes only. Every label in the image, exactly: "The form", "The mechanism", "The run", "Reading it", "P = 1", "mean = B / P = -1.5", "sum: curvature 1, vertex at -1.5", "$ ~/.vault-sandbox/bin/python compose.py", "1 P: the composed precision of each coordinate", "2 B: each mean times its precision, background taken away", "3 mean = B / P: each half takes its own expert's value", "4 var = 1 / P: as narrow as the narrow expert", "5 no background: the same B over P = 1.25, pulled toward 0", "6 shared: -1.5, a value neither expert put there".

## Process lane

Navigation: ⬅️ [Prompt 8 (Subject capstone): Precisions, the deep-dive sheet](#prompt-8-subject-capstone-precisions-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
