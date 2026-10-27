# Gaussian Integral: illustrated map

The drawn pictures for the vault note [[Gaussian Integral]], section [[Gaussian Integral#The area under the bell]]. `3 prompts · 3 rendered · 0 waiting`

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

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[Gaussian Integral]]: subject "The area under the bell", one sheet. A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: no subject here needs a repeatable named look across the set. Zoom depth: one level, the section's form and mechanism, composed by the deep-dive sheet. The style paragraph is embedded verbatim at the head of every prompt. The bell's heights are exact numbers, so every curve and bar is drawn by a deterministic figure script.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. Nothing in these pictures is a real-world object or a real product.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Blue: the bell $e^{-x^2}$ and the area under it. Orange: the rectangles that measure that area. Green: expert a's bell, the same bell slid left by 1. Red: numbered output markers only.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A smooth curve over a horizontal number line is a bell. A shaded region under it is an area. A thin upright bar standing on the line is one rectangle of a sum. All primary tier.

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

x runs left to right along the number line; height runs up. Panels read left to right: the bell measured, then the bell slid.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Numbered markers only on the deep-dive sheet's output pane, matching the numbered fields in the note's rendered output picture `the-area-under-the-bell-rectangles.png`. No step badges or phase containers.

## Subject lane
<!-- student-read: 2026-10-16 job 20261016-150718-b86c22 -->

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The form](#prompt-1-subject-the-form) ➡️

The form, the mechanism, then the deep-dive sheet that composes them with the run's output, per the vault-note exception in the illustration style guide.

### Prompt 1 (Subject): The form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism) ➡️

[planned] ⏳ not rendered
Save as: `../Mathematics/Calculus/Integration/assets/the-area-under-the-bell-the-form.webp`
The file at this path exists from an earlier render but is unchecked against this prompt, which job 20261016-150718-b86c22 rewrote after a student read.

Visual thesis: Follow each integral chip to one visible target: the shaded area, the extent of the number line, the strip's height, or the strip's width.

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

Production: Use a deterministic figure script for every curve, strip and connector. Design for reading at 800 px wide, with every label at least 18 px at that width. The mathematical marks themselves illustrate the components; add no decorative icons. Use direct labels instead of a legend.

Scene: Place the integral in one readable row above the plot, with four soft chips for I, the integral with its limits, e^(-x²), and dx. Put their meanings directly underneath: area, the whole line, height at x, thin width. Keep the chips subordinate to the shaded bell and its single orange strip.

Below, draw the computed blue bell over a horizontal number line, with whole-number ticks from -3 through 3 and outward arrows showing continuation. Shade the entire visible region beneath the curve light blue. Keep the bell symmetric, peak 1 over 0, height 0.3679 at both -1 and 1, and positive tails near the baseline. Print 1 at the peak and 0.3679 beside the point at -1.

Outline exactly one thin orange rectangle near x = 1. Its top touches the curve at its centre. Align an orange vertical height bracket immediately beside the rectangle, from the baseline to its top. Put e^(-x²) next to this bracket. Put the orange width bracket directly above the rectangle, with its two ends aligned with the rectangle's sides; place dx beside it. Leave enough room that the height label, width label and curve do not overlap.

Draw a shallow neutral extent bracket below the number line, spanning the visible plot and ending beneath its two outward arrows. This is the target for the whole-line chip. It must read as an annotation of the axis, never as a frame around the figure.

Cast: four formula chips, the blue bell and shaded area, the number line, one outlined orange strip, its height and width brackets, and the axis-extent bracket.

Flows: Exactly four leaders, one from each chip. The I leader ends inside the shaded area, away from the strip. The limits leader routes through the outside margin and terminates on the axis-extent bracket. The height leader terminates on the vertical height bracket. The width leader terminates on the horizontal width bracket itself. Keep all four leaders separate and uncrossed. No endpoint floats above or beside its target. Do not route a connector across the top and both sides of the figure.

Text in the image, spelled exactly: "I = ∫ e^(-x²) dx, from -∞ to ∞", "the whole line", "height at x", "thin width", "area", "dx", "e^(-x²)", "1", "0.3679", "x", "-3", "-2", "-1", "0", "1", "2", "3". Typeset the integral conventionally, with its limits attached to the integral sign.

Exclusions: No rectangles other than the one strip, no second curve, no additional numbers, no normal-distribution formula, no 1/sqrt(2 pi) factor, no legend, no decorative icons, no enclosing connector frame, no floating leader endpoints, no crossing leaders, no paragraphs, no watermark.
```

Faithfulness note: The bell peaks at height 1 over x = 0 and is symmetric; at x = ±1 its height is 0.3679; it is close to 0 at x = ±3 but never drawn below the line; the whole area under it is shaded, not a slice; exactly one strip is outlined; each of the four chips has exactly one leader line to the part it names. Every label in the image, exactly: "I = ∫ e^(-x²) dx, from -∞ to ∞", "the whole line", "height at x", "thin width", "area", "dx", "e^(-x²)", "1", "0.3679", "x", "-3", "-2", "-1", "0", "1", "2", "3".

### Prompt 2 (Subject): The mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The form](#prompt-1-subject-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject capstone): The deep-dive sheet](#prompt-3-subject-capstone-the-deep-dive-sheet) ➡️

[planned] 🖼️ rendered 2026-10-16 the-area-under-the-bell-the-mechanism.webp
Save as: `../Mathematics/Calculus/Integration/assets/the-area-under-the-bell-the-mechanism.webp`

Visual thesis: Thirteen rectangles of width 0.5 measure the area as 1.7724, and sliding the bell left by 1 moves the area without changing it.

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

Production: Use a deterministic figure script. Two panels side by side on one shared height axis from 0 to 1, designed for reading at 800 px wide; add height rather than shrinking text, with labels at least 18 px at that width.

Scene: Left panel, titled "rectangles": the blue bell y = e^(-x^2) over x from -3.5 to 3.5. Under it, 13 orange rectangles of width 0.5, each centred on one of x = -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, each as tall as the bell at its centre: 1, then 0.7788, 0.3679, 0.1054, 0.0183, 0.0019, 0.0001 going outward on each side, the same on both sides. Print each height above its bar for x = 0, 0.5, 1 and 1.5 only. Under the panel, one line: "0.5 × 3.5449 = 1.7724". Right panel, titled "slid left by 1": the green bell y = e^(-(x+1)^2), peak 1 at x = -1, its area shaded light green, with the blue bell's outline faint behind it at x = 0 and a short arrow from the blue peak to the green peak labelled "slide by 1". Under the panel, one line: "same area: 1.772454".

Cast: the blue bell, 13 orange rectangles, the green slid bell, the faint blue outline, the slide arrow.

Flows: one arrow, from the blue peak at x = 0 to the green peak at x = -1.

Text in the image, spelled exactly: "rectangles", "slid left by 1", "e^(-x²)", "e^(-(x+1)²)", "1", "0.7788", "0.3679", "0.1054", "width 0.5", "0.5 × 3.5449 = 1.7724", "slide by 1", "same area: 1.772454", "x", "-1", "0".

Exclusions: no third panel, no stretched bell, no rectangles in the right panel, no heights printed on the small outer bars, no formula sqrt(pi). no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Exactly 13 orange bars of width 0.5, centred at -3 to 3 in steps of 0.5, each top touching the bell at its centre; heights 1, 0.7788, 0.3679, 0.1054 printed over x = 0, 0.5, 1, 1.5; the bars are symmetric about 0; the green bell has the same shape and peak height 1 as the blue one, centred at -1. Every label in the image, exactly: "rectangles", "slid left by 1", "e^(-x²)", "e^(-(x+1)²)", "1", "0.7788", "0.3679", "0.1054", "width 0.5", "0.5 × 3.5449 = 1.7724", "slide by 1", "same area: 1.772454", "x", "-1", "0".

### Prompt 3 (Subject capstone): The deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[planned] ⏳ not rendered
Save as: `../Mathematics/Calculus/Integration/assets/the-area-under-the-bell-deep-dive-sheet.webp`
The file at this path exists from an earlier render but is unchecked against this prompt, which job 20261016-150718-b86c22 rewrote after a student read.

Visual thesis: The numbered run connects sampled heights to their sum and the rectangle area; the final line gives the finer numerical estimate.

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

Production: Use a deterministic figure script. Exactly four full-width panes stacked vertically, designed for reading at 800 px wide. Output and explanation text must remain at least 20 px at that displayed width. Measure the longest output line together with its marker before laying out the run pane. Use a legible narrow monospace face and modest horizontal padding so the line fits without wrapping, clipping, changing spaces or shrinking below the minimum size. Add vertical space wherever explanations wrap. Use mathematical marks as the illustrations, with no decorative icons or legend.

Hierarchy: Make The run the focal pane through its stronger border and heading. Keep The form and The mechanism as shallow reminder bands, together occupying no more than about a fifth of the sheet. Their compact plots sit beside their equations, rather than beneath them. Keep Reading it immediately below the run, with restrained card borders and no large empty gaps.

Scene: Pane 1, The form: a small computed blue bell with its area shaded, beside the integral "I = ∫ e^(-x²) dx, from -∞ to ∞", conventionally typeset with limits. Pane 2, The mechanism: a compact computed blue bell over exactly 13 orange rectangles of width 0.5, centred from -3 to 3 in steps of 0.5. Place "0.5 × 3.5449 = 1.7724" beside the plot. Keep the equations readable while reducing the plots' empty margins.

Pane 3, The run: print the following thirteen lines verbatim. The | separators below mark line breaks and are not printed. Preserve the two leading spaces on indented lines and the three spaces between each x value and e^(-x^2).

$ ~/.vault-sandbox/bin/python area.py | heights at x = 0, 0.5, ..., 3: |   x = 0.0   e^(-x^2) = 1.0000 |   x = 0.5   e^(-x^2) = 0.7788 |   x = 1.0   e^(-x^2) = 0.3679 |   x = 1.5   e^(-x^2) = 0.1054 |   x = 2.0   e^(-x^2) = 0.0183 |   x = 2.5   e^(-x^2) = 0.0019 |   x = 3.0   e^(-x^2) = 0.0001 | rectangles, width 0.5, x = -3..3: 13 of them |   sum of heights: 3.5449 |   area: 1.7724 | rectangles, width 0.001, x = -6..6: 1.772454

Place red markers immediately after the same fields as before: 1 after 1.0000, 2 after 0.3679, 3 after 0.0001, 4 after 13 of them, 5 after 3.5449, 6 after 1.7724, 7 after 1.772454. Markers are separate drawn objects, not inserted characters. Leave a consistent small gap before each marker and clear space after marker 7. Keep command and output text dark neutral; green is reserved for the shifted bell elsewhere in the set.

Pane 4, Reading it: seven compact cards in one column, in marker order. Each starts with the matching red numbered marker. Use these exact explanations, subject to approval of the two corrections identified in the review:
1 the peak: e^0 = 1
2 one step out: e^(-1), about a third of the peak
3 at x = 3: e^(-9), the tail is nearly zero
4 one rectangle at each of -3, -2.5, ..., 3
5 the peak plus each side's six heights
6 width 0.5 times the sum of heights
7 width 0.001: the area to six decimals

Cast: two compact reminder plots, the captured output block, and seven numbered explanations.

Flows: None between panes. Match output fields to explanations by number alone.

Text in the image, spelled exactly: "The form", "The mechanism", "The run", "Reading it", "I = ∫ e^(-x²) dx, from -∞ to ∞", "0.5 × 3.5449 = 1.7724", the thirteen verbatim run lines above, and the seven numbered explanations above. Typeset mathematical expressions in the explanations; retain literal code notation in the output.

Exclusions: No fifth pane, no leader lines between panes, no altered output text or spacing, no wrapped output lines, no legend or colour key, no sqrt(pi), no added claims that the tail reaches zero, no decorative icons, no watermark.
```

Faithfulness note: The thirteen output lines match the note's captured run of `area.py` character for character, runs of spaces included; markers 1 to 7 sit after the same fields as the note's rendered output picture `the-area-under-the-bell-rectangles.png`; four panes only; no legend anywhere; the bars in pane 2 are 13, of width 0.5. Every label in the image, exactly: "The form", "The mechanism", "The run", "Reading it", "I = ∫ e^(-x²) dx, from -∞ to ∞", "0.5 × 3.5449 = 1.7724", "$ ~/.vault-sandbox/bin/python area.py", "1 the peak: e^0 = 1", "2 one step out: e^(-1), about a third of the peak", "3 at x = 3: e^(-9), the tail is nearly zero", "4 one rectangle at each of -3, -2.5, ..., 3", "5 the peak plus each side's six heights", "6 width 0.5 times the sum of heights", "7 width 0.001: the area to six decimals".

## Process lane

Navigation: ⬅️ [Prompt 3 (Subject capstone): The deep-dive sheet](#prompt-3-subject-capstone-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
