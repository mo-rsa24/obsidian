# Multivariate Normal Distribution: illustrated map

The drawn pictures for the notes in the vault's [[Multivariate Normal Distribution]] folder, sections [[Diagonal Covariance]], [[Sampling A Diagonal Gaussian]], [[Sums Of Independent Gaussians]] and [[Products And Quotients Of Diagonal Gaussians]]. `15 prompts · 8 rendered · 4 stuck · 0 rendering · 3 waiting`

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
- [Prompt 9 (Subject): The area a product loses](#prompt-9-subject-the-area-a-product-loses)
- [Prompt 10 (Subject): Powers of Gaussians](#prompt-10-subject-powers-of-gaussians)
- [Subject lane: Products of Gaussian mixtures](#subject-lane-products-of-gaussian-mixtures)
- [Prompt 11 (Subject): Products of Gaussian mixtures](#prompt-11-subject-products-of-gaussian-mixtures)
- [Subject lane: Sums of independent Gaussians](#subject-lane-sums-of-independent-gaussians)
- [Prompt 12 (Subject): Sums, the form](#prompt-12-subject-sums-the-form)
- [Prompt 13 (Subject): Sums, the mechanism](#prompt-13-subject-sums-the-mechanism)
- [Prompt 14 (Subject capstone): Sums, the deep-dive sheet](#prompt-14-subject-capstone-sums-the-deep-dive-sheet)
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
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/diagonal-gaussian-the-form.webp`

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
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/diagonal-gaussian-the-mechanism.webp`

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
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/diagonal-gaussian-deep-dive-sheet.webp`

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

The form, the mechanism and the deep-dive sheet for [[Sampling A Diagonal Gaussian]].

### Prompt 3 (Subject): Sampling, the form

Navigation: ⬅️ [Subject lane: Sampling a diagonal Gaussian](#subject-lane-sampling-a-diagonal-gaussian) | 📋 [TOC](#table-of-contents) | [Prompt 4 (Subject): Sampling, the mechanism](#prompt-4-subject-sampling-the-mechanism) ➡️

[planned] ⚠️ stuck: pixel check, panel 3 cloud is 2.6 times taller than wide (note says 2) and centred near x1 = -2.7, after 3 revisions; last attempt ~/.cache/codex-drop/obsidian/mvn-samp-form.png
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/sampling-the-form.webp`

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
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/sampling-the-mechanism.webp`

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
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/sampling-deep-dive-sheet.webp`

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

The form, the mechanism and the deep-dive sheet for [[Products And Quotients Of Diagonal Gaussians]].

### Prompt 6 (Subject): Precisions, the form

Navigation: ⬅️ [Subject lane: Products and quotients of diagonal Gaussians](#subject-lane-products-and-quotients-of-diagonal-gaussians) | 📋 [TOC](#table-of-contents) | [Prompt 7 (Subject): Precisions, the mechanism](#prompt-7-subject-precisions-the-mechanism) ➡️

[planned] 🖼️ rendered 2026-10-04 products-the-form.webp
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/products-the-form.webp`

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
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/products-the-mechanism.webp`

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

Navigation: ⬅️ [Prompt 7 (Subject): Precisions, the mechanism](#prompt-7-subject-precisions-the-mechanism) | 📋 [TOC](#table-of-contents) | [Prompt 9 (Subject): The area a product loses](#prompt-9-subject-the-area-a-product-loses) ➡️

[planned] 🖼️ rendered 2026-10-17 products-deep-dive-sheet.webp
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/products-deep-dive-sheet.webp`

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

Scene: Pane 1, The form: a compact reminder of prompt 6, the four precision bars and the green dot at -1.5. Pane 2, The mechanism: a compact reminder of prompt 7, the three parabolas and the green sum with its vertex at -1.5, each labelled directly on its curve with prompt 7's words: blue "log p1, curvature 1", orange "log p2, curvature 0.25", grey, opening upward, "- log p_b, curvature -0.25", green "sum: curvature 1, vertex at -1.5". The grey curve is minus the background's log, so its curvature is negative. No legend in this pane or anywhere on the sheet: every colour is named by the label on its own curve or bar, and the form pane's bars carry their values as labels, as in prompt 6. Pane 3, The run: five lines of monospace output, exactly: $ ~/.vault-sandbox/bin/python compose.py | split  p1 p2 / p_b  P [1.0, 1.0]  B [-2.0, 2.0]  mean [-2.0, 2.0]  var [1.0, 1.0] | split  p1 p2        P [1.25, 1.25]  B [-2.0, 2.0]  mean [-1.6, 1.6]  var [0.8, 0.8] | shared p1 p2 / p_b  P [1.0, 1.0]  B [-1.5, 0.0]  mean [-1.5, 0.0]  var [1.0, 1.0] | shared p1 p2        P [1.25, 1.25]  B [-1.5, 0.0]  mean [-1.2, 0.0]  var [0.8, 0.8] (the | marks a new line and is not printed; keep the runs of spaces). Red markers: 1 over P [1.0, 1.0], 2 over B [-2.0, 2.0], 3 over mean [-2.0, 2.0], 4 over var [1.0, 1.0], all on the first output line; 5 over mean [-1.6, 1.6] on the second; 6 over mean [-1.5, 0.0] on the third. Pane 4, Reading it: six cards in order.

Cast: the reminder bars and parabolas, the output block, six numbered field cards.

Flows: none between panes.

Text in the image, spelled exactly: "The form", "The mechanism", "The run", "Reading it", "P = 1", "mean = B / P = -1.5", "log p1, curvature 1", "log p2, curvature 0.25", "- log p_b, curvature -0.25", "sum: curvature 1, vertex at -1.5", "$ ~/.vault-sandbox/bin/python compose.py", "1 P: the composed precision of each coordinate", "2 B: each mean times its precision, background taken away", "3 mean = B / P: each half takes its own expert's value", "4 var = 1 / P: as narrow as the narrow expert", "5 no background: the same B over P = 1.25, pulled toward 0", "6 shared: -1.5, a value neither expert put there".

Exclusions: no fifth pane, no leader lines between panes, no altered output text, no wrapped output line that loses its spacing, no legend panel or colour key, no positive curvature written on the grey curve. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The four output lines match the note's captured run character for character, runs of spaces included; markers 1 to 6 sit over the same fields as the note's rendered output picture; four panes only; no legend anywhere; the grey curve in pane 2 opens upward and is labelled with curvature -0.25, minus sign included. Every label in the image, exactly: "The form", "The mechanism", "The run", "Reading it", "P = 1", "mean = B / P = -1.5", "log p1, curvature 1", "log p2, curvature 0.25", "- log p_b, curvature -0.25", "sum: curvature 1, vertex at -1.5", "$ ~/.vault-sandbox/bin/python compose.py", "1 P: the composed precision of each coordinate", "2 B: each mean times its precision, background taken away", "3 mean = B / P: each half takes its own expert's value", "4 var = 1 / P: as narrow as the narrow expert", "5 no background: the same B over P = 1.25, pulled toward 0", "6 shared: -1.5, a value neither expert put there".

### Prompt 9 (Subject): The area a product loses

Navigation: ⬅️ [Prompt 8 (Subject capstone): Precisions, the deep-dive sheet](#prompt-8-subject-capstone-precisions-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents) | [Prompt 10 (Subject): Powers of Gaussians](#prompt-10-subject-powers-of-gaussians) ➡️

[planned] ⚠️ stuck: pixel check after 3 revisions, the right panel's tangents sit at the parabolas' peak (x about -0.30 on the -3 to 3 axis) where the note puts them at x = 0, so a sloped tangent is drawn at a vertex, and the solid bump peaks at 0.066 on the dashed bell's scale where the note says near 0.054 (0.092 of the dashed bell's height, about one tenth); the constant gap (234 to 238 px at every x), expert b to expert a 0.778 against 0.791, the dashed bell 1.31 times expert a against 1.275, parallel tangents and every label correct; last attempt ~/.cache/codex-drop/obsidian/products-the-area-a-product-loses.png
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/products-the-area-a-product-loses.webp`

Visual thesis: Multiplying two densities point by point leaves a small bump whose area is 0.075126, and dividing by that area lifts its log by a constant, so the slope of the log, the score, stays the same.

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

Production: Use a deterministic figure script for every curve and all typography, from these exact densities: expert a is a Gaussian with mean -1 and variance 0.5, expert b a Gaussian with mean 1 and variance 0.8, the product is their heights multiplied point by point, and the normalised product is that divided by 0.075126 (a Gaussian with mean -0.230769 and variance 0.307692). Compose for reading at 800 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no legend.

Scene: Two panels side by side, the same x axis from -3 to 3. Left panel, titled "heights": a blue bell for expert a, peak 0.564 at x = -1, labelled "expert a, area 1"; an orange bell for expert b, peak 0.446 at x = 1, labelled "expert b, area 1"; a small solid green bump, their product, peak 0.054 at x = -0.23, filled with light green and labelled "a times b, area 0.075126"; a dashed green bell, the product divided by 0.075126, peak 0.719 at x = -0.23, labelled "divided by 0.075126: area 1". The vertical axis is labelled "height". Right panel, titled "log heights": the log of the solid green bump and the log of the dashed green bell, two downward parabolas of identical shape, one exactly 2.588582 above the other; a double-headed vertical arrow between them at x = 1.5 labelled "gap log Z = -2.588582, the same everywhere"; at x = 0 a short straight tangent line on each parabola, both with slope -0.75, labelled once "same slope at x = 0: -0.75". The vertical axis is labelled "log height".

Cast: the two experts, the product bump, the normalised product, the two log parabolas, the gap arrow, the two tangents.

Flows: none.

Text in the image, spelled exactly: "heights", "log heights", "height", "log height", "x", "expert a, area 1", "expert b, area 1", "a times b, area 0.075126", "divided by 0.075126: area 1", "gap log Z = -2.588582, the same everywhere", "same slope at x = 0: -0.75".

Exclusions: no legend panel, no third panel, no numbers other than those listed, no mixture curve. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The solid green bump peaks near 0.054 and is about one tenth the height of the dashed green bell, which peaks near 0.719, both at x = -0.23; the two right-panel parabolas have the same shape and differ by a constant vertical shift; both tangents at x = 0 are parallel. Every label in the image, exactly: "heights", "log heights", "height", "log height", "x", "expert a, area 1", "expert b, area 1", "a times b, area 0.075126", "divided by 0.075126: area 1", "gap log Z = -2.588582, the same everywhere", "same slope at x = 0: -0.75".

### Prompt 10 (Subject): Powers of Gaussians

Navigation: ⬅️ [Prompt 9 (Subject): The area a product loses](#prompt-9-subject-the-area-a-product-loses) | 📋 [TOC](#table-of-contents) | [Subject lane: Products of Gaussian mixtures](#subject-lane-products-of-gaussian-mixtures) ➡️

[planned] ⚠️ stuck: pixel check after 3 revisions, bars not to one scale (the blue 2-unit bar is 215, 215, 181 and 120 px in the four rows) and row 1's bells off their means on the -4 to 10 axis (expert a near -0.36 where it must be -1, the product near 0.57 where it must be -0.23, expert b near 1.95 where it must be 1); guidance near 0.27 and negation near -1.95, left of expert a, the row 4 curve opening upward with no peak, opacity and every label correct; two attempts came back semi-transparent (RGBA) and the last is opaque; last attempt ~/.cache/codex-drop/obsidian/products-powers-of-gaussians.png
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/products-powers-of-gaussians.webp`

Visual thesis: Raising each Gaussian to a power scales its precision bar by that power before the bars are added, and when a negative power takes the total below zero the result is no longer a bell.

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

Production: Use a deterministic figure script for every curve and all typography, from these exact densities: expert a is a Gaussian with mean -1 and variance 0.5, expert b a Gaussian with mean 1 and variance 0.8. Compose for reading at 800 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no legend.

Scene: Four rows, titled "product, w_b = 1", "guidance, w_b = 2", "negation, w_b = -0.5" and "not a density, w_a = -1". Each row has on the left two precision bars: a blue bar for expert a labelled "precision 2 times w_a" and an orange bar for expert b labelled "precision 1.25 times w_b", each bar's length scaled by its row's power (a negative power draws the bar pointing left of zero), joined into one total bar labelled with the row's precision: "precision 3.25", "precision 4.5", "precision 1.375", "precision -0.75". On the right of each row, the resulting curve on an x axis from -4 to 10: a green bell at mean -0.23 for the product, a green bell at 0.11 for guidance, a pink bell at -1.91 for negation, and for the last row a grey upward-opening curve that rises toward both edges with no peak. Thin "expert a" (blue, mean -1) and "expert b" (orange, mean 1) bells are drawn faintly in the first row only.

Cast: four rows, eight scaled precision bars, four total bars, four result curves.

Flows: none.

Text in the image, spelled exactly: "product, w_b = 1", "guidance, w_b = 2", "negation, w_b = -0.5", "not a density, w_a = -1", "expert a", "expert b", "precision 3.25", "precision 4.5", "precision 1.375", "precision -0.75", "precision 2 times w_a", "precision 1.25 times w_b".

Exclusions: no mixture, no noise levels, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Bar lengths are to scale: the blue bar is 2 units with power 1, the orange bar 1.25 units in row 1, 2.5 in row 2 and -0.625 pointing left in row 3; row 4's blue bar is -2 pointing left; the last row's curve opens upward and has no peak; the negation bell sits left of where expert a would be. Every label in the image, exactly: "product, w_b = 1", "guidance, w_b = 2", "negation, w_b = -0.5", "not a density, w_a = -1", "expert a", "expert b", "precision 3.25", "precision 4.5", "precision 1.375", "precision -0.75", "precision 2 times w_a", "precision 1.25 times w_b".

## Subject lane: Products of Gaussian mixtures

Navigation: ⬅️ [Prompt 10 (Subject): Powers of Gaussians](#prompt-10-subject-powers-of-gaussians) | 📋 [TOC](#table-of-contents) | [Prompt 11 (Subject): Products of Gaussian mixtures](#prompt-11-subject-products-of-gaussian-mixtures) ➡️

One picture for [[Products And Quotients Of Diagonal Gaussians#Products of Gaussian mixtures]], a subsection of the precisions section, whose form, mechanism and deep-dive sheet are prompts 6 to 8. Colours as in the precisions lane: blue expert 1 (the cat mixture), orange expert 2 (the dog mixture), grey for what is off or blended, green the kept composition. Every number is counted from the overlap-dial walk's `example-9-parts-world/numbers.json`, setting (c).

### Prompt 11 (Subject): Products of Gaussian mixtures

Navigation: ⬅️ [Subject lane: Products of Gaussian mixtures](#subject-lane-products-of-gaussian-mixtures) | 📋 [TOC](#table-of-contents) | [Subject lane: Sums of independent Gaussians](#subject-lane-sums-of-independent-gaussians) ➡️

[planned] 🖼️ rendered 2026-10-17 products-of-gaussian-mixtures.webp
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/products-of-gaussian-mixtures.webp`

Visual thesis: Multiplying two two-component mixtures gives one component per pair, four in all, and each pair's weight is how much its two components overlap, so the two pairs that agree keep all the weight and the two that clash keep none.

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

Production: Use a deterministic figure script for every 4 by 4 tile, the grid and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A banner across the top: "w_ij is proportional to pi_i rho_j N(mu_i; nu_j, S_i + L_j)". Below it a 2 by 2 grid of cells with row headers on the left and column headers on top. The row group is labelled "cat mixture" and its two headers are small 4 by 4 tiles: "cat left, 0.5" with the left two columns blue and the right two columns pale grey, and "cat right, 0.5" with the right two columns blue and the left two pale grey. The column group is labelled "dog mixture" and its two headers are tiles: "dog left, 0.5" with the left two columns orange and the right two pale grey, and "dog right, 0.5" with the right two columns orange and the left two pale grey. Each cell holds the product component's 4 by 4 tile and two lines of text. Cell cat left with dog left: a tile with every square mid-grey, "log w = -803.2" and "weight 0.00", the cell faded, grey border, with the caption "both in one half: they clash". Cell cat right with dog right: the same, faded, mid-grey tile, "log w = -803.2", "weight 0.00". Cell cat left with dog right: a tile with the left two columns blue and the right two orange, "log w = -24.1" and "weight 0.50", green border, with the caption "side by side: they agree". Cell cat right with dog left: a tile with the left two columns orange and the right two blue, "log w = -24.1" and "weight 0.50", green border.

Cast: one banner, four header tiles, four cells each with one tile.

Flows: none.

Text in the image, spelled exactly: "cat mixture", "dog mixture", "cat left, 0.5", "cat right, 0.5", "dog left, 0.5", "dog right, 0.5", "log w = -803.2", "log w = -24.1", "weight 0.00", "weight 0.50", "both in one half: they clash", "side by side: they agree", "w_ij is proportional to pi_i rho_j N(mu_i; nu_j, S_i + L_j)".

Exclusions: no bells or curves, no animals drawn, no fifth cell, no red. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The two diagonal cells pairing the same half (cat left with dog left, cat right with dog right) are faded with all-grey tiles at weight 0.00 and log w -803.2; the two off-diagonal cells are green-bordered with a blue half and an orange half, in opposite halves, at weight 0.50 and log w -24.1. Each header tile is coloured only on its own half. The numbers are setting (c)'s fields in `numbers.json`, rounded to one decimal. Every label in the image, exactly: "cat mixture", "dog mixture", "cat left, 0.5", "cat right, 0.5", "dog left, 0.5", "dog right, 0.5", "log w = -803.2", "log w = -24.1", "weight 0.00", "weight 0.50", "both in one half: they clash", "side by side: they agree", "w_ij is proportional to pi_i rho_j N(mu_i; nu_j, S_i + L_j)".

## Subject lane: Sums of independent Gaussians

Navigation: ⬅️ [Prompt 11 (Subject): Products of Gaussian mixtures](#prompt-11-subject-products-of-gaussian-mixtures) | 📋 [TOC](#table-of-contents) | [Prompt 12 (Subject): Sums, the form](#prompt-12-subject-sums-the-form) ➡️

The form, the mechanism and the deep-dive sheet for [[Sums Of Independent Gaussians]]. Colours in this lane: blue the first noise term $a\,e_1$, orange the second $b\,e_2$, green the one combined draw, purple a cross term that survives, grey the route that is wrong for fresh draws. Every number is the note's worked example: $\alpha_1 = 0.9$, $\alpha_2 = 0.8$, so $a = \sqrt{0.08} = 0.282843$ and $b = \sqrt{0.2} = 0.447214$. The sheet's third pane carries these derived numbers because the note's sandbox has not run yet; when it runs, the pane is improved to show the captured output.

### Prompt 12 (Subject): Sums, the form

Navigation: ⬅️ [Subject lane: Sums of independent Gaussians](#subject-lane-sums-of-independent-gaussians) | 📋 [TOC](#table-of-contents) | [Prompt 13 (Subject): Sums, the mechanism](#prompt-13-subject-sums-the-mechanism) ➡️

[planned] ⏳ not rendered
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/sums-the-form.webp`

Visual thesis: Two fresh noises combine by squaring each weight and adding, so weights 0.282843 and 0.447214 give one draw of variance 0.28 and standard deviation 0.529, while adding the weights first gives 0.730056, the spread only a reused draw has.

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

Production: Use a deterministic figure script for every bell and bar and all typography, from these exact numbers: the blue bell is a Gaussian with mean 0 and standard deviation 0.282843, the orange bell mean 0 and standard deviation 0.447214, the green bell mean 0 and standard deviation 0.529150; variance bars 0.08, 0.2 and 0.28 tall on one shared scale; the grey length 0.730056 on the same scale as the two weight lengths 0.282843 and 0.447214. Compose for reading at 800 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no legend.

Scene: On the left, two small bells one above the other: a blue bell labelled "a e_1, a = 0.282843" and a wider orange bell labelled "b e_2, b = 0.447214". From them two routes run to the right. The upper route, titled "fresh draws: variances add", squares each weight into a vertical bar: a blue bar labelled "a² = 0.08" and an orange bar labelled "b² = 0.2", stacked one on the other into a single bar labelled "a² + b² = 0.28", which ends in a green bell, wider than the orange one, labelled "one draw: √0.28 ε, std 0.529". The lower route, in grey, titled "same draw: standard deviations add", lays the two weights end to end as horizontal lengths, blue 0.282843 then orange 0.447214, into one grey length labelled "a + b = 0.730056", with the note "std only if e_2 = e_1".

Cast: two input bells, the upper route's three bars and its green bell, the lower route's two lengths and their grey total.

Flows: one arrow from the bells into each route, one arrow from the stacked bar to the green bell.

Text in the image, spelled exactly: "fresh draws: variances add", "same draw: standard deviations add", "a e_1, a = 0.282843", "b e_2, b = 0.447214", "a² = 0.08", "b² = 0.2", "a² + b² = 0.28", "one draw: √0.28 ε, std 0.529", "a + b = 0.730056", "std only if e_2 = e_1".

Exclusions: no third route, no numbers other than those listed, no x axis ticks. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The three variance bars are to one scale, 0.08 : 0.2 : 0.28, with the stacked bar exactly the two smaller ones on top of each other; the green bell is wider than the orange bell and narrower than the grey length; the grey length equals the blue and orange lengths laid end to end; the upper route is coloured, the lower route grey. Every label in the image, exactly: "fresh draws: variances add", "same draw: standard deviations add", "a e_1, a = 0.282843", "b e_2, b = 0.447214", "a² = 0.08", "b² = 0.2", "a² + b² = 0.28", "one draw: √0.28 ε, std 0.529", "a + b = 0.730056", "std only if e_2 = e_1".

### Prompt 13 (Subject): Sums, the mechanism

Navigation: ⬅️ [Prompt 12 (Subject): Sums, the form](#prompt-12-subject-sums-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 14 (Subject capstone): Sums, the deep-dive sheet](#prompt-14-subject-capstone-sums-the-deep-dive-sheet) ➡️

[planned] ⏳ not rendered
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/sums-the-mechanism.webp`

Visual thesis: Squaring the sum lays out four cells, and the two cross cells average to zero when the second noise is drawn fresh, leaving 0.08 + 0.2 = 0.28, but each stays at ab = 0.126491 when the draw is reused, giving 0.532982.

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

Production: Use a deterministic figure script for both grids and all typography. Compose for reading at 800 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no legend.

Scene: Two 2 by 2 grids side by side, the same size. Each grid has row headers "a e_1" and "b e_2" on its left and the same two as column headers on top. Left grid, titled "fresh e_2": the top-left cell blue, "a² E[e_1²] = 0.08"; the bottom-right cell orange, "b² E[e_2²] = 0.2"; the two off-diagonal cells faded light grey, each "ab E[e_1 e_2] = 0", with one caption across them, "cross cells average to zero". Under the grid, a green total: "sum of cells: 0.28". Right grid, titled "reused, e_2 = e_1": the same blue and orange diagonal cells with the same labels; the two off-diagonal cells purple, each "ab = 0.126491", with the caption "cross cells stay". Under it a grey total: "sum of cells: 0.532982".

Cast: two grids of four cells each, two totals.

Flows: none.

Text in the image, spelled exactly: "fresh e_2", "reused, e_2 = e_1", "a e_1", "b e_2", "a² E[e_1²] = 0.08", "b² E[e_2²] = 0.2", "ab E[e_1 e_2] = 0", "ab = 0.126491", "sum of cells: 0.28", "sum of cells: 0.532982", "cross cells average to zero", "cross cells stay".

Exclusions: no bells or curves, no numbers other than those listed, no third grid. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: In the left grid the two off-diagonal cells are faded grey and read 0; in the right grid they are purple and read 0.126491; the diagonal cells are identical in both grids; the left total is green and the right total grey. Every label in the image, exactly: "fresh e_2", "reused, e_2 = e_1", "a e_1", "b e_2", "a² E[e_1²] = 0.08", "b² E[e_2²] = 0.2", "ab E[e_1 e_2] = 0", "ab = 0.126491", "sum of cells: 0.28", "sum of cells: 0.532982", "cross cells average to zero", "cross cells stay".

### Prompt 14 (Subject capstone): Sums, the deep-dive sheet

Navigation: ⬅️ [Prompt 13 (Subject): Sums, the mechanism](#prompt-13-subject-sums-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[planned] ⏳ not rendered
Save as: `../Mathematics/Statistics/Distributions/Multivariate Normal Distribution/assets/sums-deep-dive-sheet.webp`

Visual thesis: One sheet carries the rule from its form to the two forward steps it licenses: square each weight and add, because independence zeroes the cross cells, and on the toy both routes give 0.28 while a reused draw gives 0.532982.

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

Production: Use a deterministic figure script for every bar, grid and all typography, with the numbers of prompts 12 and 13. Compose for reading at 1200 px wide, four panes in a 2 by 2 layout; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no legend.

Scene: Pane 1, titled "The form": the upper route of prompt 12 only, the bars "a² = 0.08" and "b² = 0.2" stacked into "a² + b² = 0.28" under the heading "fresh draws: variances add", with a small grey strip beside it reading "a + b = 0.730056". Pane 2, titled "The mechanism": the two grids of prompt 13 drawn small, titled "fresh e_2" and "reused, e_2 = e_1", with only their totals labelled, "sum of cells: 0.28" in green and "sum of cells: 0.532982" in grey. Pane 3, titled "The two-step toy": a rounded card of five lines in a monospaced font, "α_1 = 0.9, α_2 = 0.8", "a² = 0.8 × 0.1 = 0.08", "b² = 1 - 0.8 = 0.2", "long way: 0.08 + 0.2 = 0.28", "one jump: 1 - 0.72 = 0.28", and below it, in grey, "reused draw: 0.28 + 0.252982 = 0.532982". Pane 4, titled "Reading it": four small cards, one line each: "square each weight, then add", "independence zeroes the two cross cells", "both routes give 0.28 for any alphas", "a reused draw nearly doubles the variance".

Cast: four panes; pane 1 three bars and one strip, pane 2 two small grids, pane 3 one card, pane 4 four cards.

Flows: none.

Text in the image, spelled exactly: "The form", "The mechanism", "The two-step toy", "Reading it", "fresh draws: variances add", "a² = 0.08", "b² = 0.2", "a² + b² = 0.28", "a + b = 0.730056", "fresh e_2", "reused, e_2 = e_1", "sum of cells: 0.28", "sum of cells: 0.532982", "α_1 = 0.9, α_2 = 0.8", "a² = 0.8 × 0.1 = 0.08", "b² = 1 - 0.8 = 0.2", "long way: 0.08 + 0.2 = 0.28", "one jump: 1 - 0.72 = 0.28", "reused draw: 0.28 + 0.252982 = 0.532982", "square each weight, then add", "independence zeroes the two cross cells", "both routes give 0.28 for any alphas", "a reused draw nearly doubles the variance".

Exclusions: no fifth pane, no numbered markers, no terminal window, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Four panes only; pane 1's bars are to the scale 0.08 : 0.2 : 0.28; pane 2's left total is green and its right total grey; pane 3's lines are the note's worked numbers in order and are drawn as a card, not a terminal; no numbered markers, since the note has no captured output yet. Every label in the image, exactly: "The form", "The mechanism", "The two-step toy", "Reading it", "fresh draws: variances add", "a² = 0.08", "b² = 0.2", "a² + b² = 0.28", "a + b = 0.730056", "fresh e_2", "reused, e_2 = e_1", "sum of cells: 0.28", "sum of cells: 0.532982", "α_1 = 0.9, α_2 = 0.8", "a² = 0.8 × 0.1 = 0.08", "b² = 1 - 0.8 = 0.2", "long way: 0.08 + 0.2 = 0.28", "one jump: 1 - 0.72 = 0.28", "reused draw: 0.28 + 0.252982 = 0.532982", "square each weight, then add", "independence zeroes the two cross cells", "both routes give 0.28 for any alphas", "a reused draw nearly doubles the variance".

## Process lane

Navigation: ⬅️ [Prompt 14 (Subject capstone): Sums, the deep-dive sheet](#prompt-14-subject-capstone-sums-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
