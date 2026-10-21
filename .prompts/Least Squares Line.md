# Least Squares Line: illustrated map

The drawn pictures for the vault note [[Least Squares Line]], section [[Least Squares Line#How the line is found]]: its form, its mechanism (the two normal equations as two balances), and the deep-dive sheet that composes them with the run of `least_squares_line.py`. `3 prompts · 0 rendered · 3 waiting`

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

1. [[Least Squares Line]]: subject "How the line is found", one sheet. A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: no subject here needs a repeatable named look across the set. Zoom depth: one level, the section's form and mechanism, composed by the deep-dive sheet. The style paragraph is embedded verbatim at the head of every prompt. The four points, the two lines and every residual are exact numbers, so every point, line and square is placed by a deterministic figure script. The note already carries a rendered two-panel plot of the same points (`least-squares-four-points-two-lines.png`); these drawings explain it and must agree with it.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

`../Mathematics/Statistics/assets/least-squares-four-points-two-lines.png`, for the positions of the four points, the two lines and the residual values. Nothing in these pictures is a real-world object or a real product.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Blue: the least-squares line with its intercept, y = 1.5 + x, and its residuals and squares. Orange: the line forced through (0, 0), y = 1.6429 x, and its residuals and squares. Near-black: the four data points. Red: numbered output markers only.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A filled dot is one data point. A straight line across the plot is a fitted line. A dashed vertical segment from a point to a line is that point's residual. A square standing on a residual, with the residual as its side, is that residual squared. A beam balanced on a pivot is a sum that comes out to zero. All primary tier.

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

x runs left to right from 0 to 3; y runs up from 0 to 5, one unit the same length on both axes so a residual's square is drawn as a true square. Panels read left to right: the line with its intercept, then the line forced through (0, 0).

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Numbered markers only on the deep-dive sheet's run pane, matching the numbered fields in the note's rendered output picture `least-squares-four-points-output.png`. No step badges or phase containers.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The form](#prompt-1-subject-the-form) ➡️

The form, the mechanism, then the deep-dive sheet that composes them with the run's output, per the vault-note exception in the illustration style guide.

### Prompt 1 (Subject): The form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism) ➡️

[planned] ⏳ not rendered
Save as: `../Mathematics/Statistics/assets/least-squares-line-the-form.webp`

Visual thesis: Each piece of the residual sum of squares names one part of the picture: a point, the line's height under it, the vertical miss between them, and that miss's square; the four squares together have area 1.0.

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

Production: Use a deterministic figure script for the points, the line and the squares. Landscape, 16:9, designed for reading at 800 px wide, with every label at least 18 px at that width. Equal scale on both axes.

Scene: Top: the quantity to make small written large in one line, RSS = Σ (y_i − a − b x_i)², each of its pieces in its own soft rounded chip: "Σ", "y_i", "a + b x_i", "y_i − a − b x_i", "( )²". Below: axes with x from 0 to 3 and y from 0 to 5, ticks at every whole number. Four near-black dots at (0, 1), (1, 3), (2, 4), (3, 4). The blue line y = 1.5 + x from x = −0.2 to x = 3.2, passing through (0, 1.5), (1, 2.5), (2, 3.5), (3, 4.5). From each dot a dashed blue vertical segment to the line, labelled with its residual: −0.5 at x = 0, +0.5 at x = 1, +0.5 at x = 2, −0.5 at x = 3. On each segment a light-blue square with that segment as one side, side 0.5, area 0.25, printed inside "0.25". The dot at x = 2 is the worked one: its chip "y_i" points to the dot's height 4, its chip "a + b x_i" points to the line's height 3.5 under it, its chip "y_i − a − b x_i" points to the dashed segment of length 0.5, its chip "( )²" points to the square of area 0.25. The chip "Σ" points to a small tally at the right edge: "0.25 + 0.25 + 0.25 + 0.25 = 1.0".

Cast: the five chips, the axes, four dots, the blue line, four dashed residuals, four light-blue squares, the tally.

Flows: five leader lines, one from each chip, none crossing.

Text in the image, spelled exactly: "RSS = Σ (y_i − a − b x_i)²", "Σ", "y_i", "a + b x_i", "y_i − a − b x_i", "( )²", "y = 1.5 + x", "−0.5", "+0.5", "0.25", "0.25 + 0.25 + 0.25 + 0.25 = 1.0", "x", "y", "0", "1", "2", "3", "4", "5".

Exclusions: no second line, no line through (0, 0), no horizontal residuals, no perpendicular residuals, no numbers other than those listed, no matrix notation. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Exactly four dots, at (0, 1), (1, 3), (2, 4), (3, 4); the blue line passes through (0, 1.5) and (3, 4.5) with slope 1; every residual is vertical and has length 0.5; the residuals at x = 0 and x = 3 run down from the line to the dot (the dot is below), and those at x = 1 and x = 2 run up (the dot is above); the four squares are true squares of side 0.5, each labelled 0.25; the tally adds to 1.0. Every label in the image, exactly: "RSS = Σ (y_i − a − b x_i)²", "Σ", "y_i", "a + b x_i", "y_i − a − b x_i", "( )²", "y = 1.5 + x", "−0.5", "+0.5", "0.25", "0.25 + 0.25 + 0.25 + 0.25 = 1.0", "x", "y", "0", "1", "2", "3", "4", "5".

### Prompt 2 (Subject): The mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The form](#prompt-1-subject-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject capstone): The deep-dive sheet](#prompt-3-subject-capstone-the-deep-dive-sheet) ➡️

[planned] ⏳ not rendered
Save as: `../Mathematics/Statistics/assets/least-squares-line-the-mechanism.webp`

Visual thesis: The two normal equations are two balances: the residuals add to 0, and the residuals weighted by x add to 0; the line forced through (0, 0) keeps the second balance, loses the first (its residuals add to 2.1429), and its squares grow from 1.0 to 4.2143.

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

Production: Use a deterministic figure script. Two panels side by side on one shared y axis from −0.5 to 5.5, landscape 16:9, designed for reading at 800 px wide; add height rather than shrinking text, with labels at least 18 px at that width. Under each panel, two balance beams stacked.

Scene: Left panel, titled "with the intercept: y = 1.5 + x": the four near-black dots at (0, 1), (1, 3), (2, 4), (3, 4), the blue line, and dashed blue residuals −0.5, +0.5, +0.5, −0.5 at x = 0, 1, 2, 3. Under it, beam 1, titled "residuals add to 0": four blue weights hanging at equal spacing, two pulling up labelled +0.5 and two pulling down labelled −0.5, the beam level, with "−0.5 + 0.5 + 0.5 − 0.5 = 0" beneath. Beam 2, titled "x times residual adds to 0": the same four weights hung at distances 0, 1, 2, 3 from the pivot's left end, labelled 0 × (−0.5), 1 × 0.5, 2 × 0.5, 3 × (−0.5), the beam level, with "0 + 0.5 + 1 − 1.5 = 0" beneath. A blue chip: "RSS 1.0". Right panel, titled "forced through (0, 0): y = 1.6429 x": the same four dots, the orange line through (0, 0) and (3, 4.9286), dashed orange residuals +1, +1.3571, +0.7143, −0.9286 at x = 0, 1, 2, 3. Under it, beam 1 tipped clearly, titled "residuals add to 2.1429", with "1 + 1.3571 + 0.7143 − 0.9286 = 2.1429" beneath. Beam 2 level, titled "x times residual adds to 0", with "0 + 1.3571 + 1.4286 − 2.7857 = 0" beneath. An orange chip: "RSS 4.2143".

Cast: two panels, eight dots, the blue and orange lines, eight dashed residuals, four beams, two RSS chips.

Flows: none.

Text in the image, spelled exactly: "with the intercept: y = 1.5 + x", "forced through (0, 0): y = 1.6429 x", "residuals add to 0", "residuals add to 2.1429", "x times residual adds to 0", "−0.5", "+0.5", "+1", "+1.3571", "+0.7143", "−0.9286", "−0.5 + 0.5 + 0.5 − 0.5 = 0", "0 + 0.5 + 1 − 1.5 = 0", "1 + 1.3571 + 0.7143 − 0.9286 = 2.1429", "0 + 1.3571 + 1.4286 − 2.7857 = 0", "RSS 1.0", "RSS 4.2143", "x", "0", "1", "2", "3".

Exclusions: no third panel, no squares in this picture, no slope or intercept formulas, no matrix notation, no tipped beam on the left side, no tipped second beam on the right side. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: On the left, the residuals −0.5, +0.5, +0.5, −0.5 add to 0 and the x-weighted ones 0, 0.5, 1, −1.5 add to 0, so both left beams are level; on the right, the residuals 1, 1.3571, 0.7143, −0.9286 add to 2.1429, so beam 1 is tipped, while the x-weighted ones 0, 1.3571, 1.4286, −2.7857 add to 0, so beam 2 is level; the orange line passes through (0, 0); the blue line through (0, 1.5) with slope 1; the dots are identical in both panels; RSS 1.0 is blue and RSS 4.2143 is orange. Every label in the image, exactly: "with the intercept: y = 1.5 + x", "forced through (0, 0): y = 1.6429 x", "residuals add to 0", "residuals add to 2.1429", "x times residual adds to 0", "−0.5", "+0.5", "+1", "+1.3571", "+0.7143", "−0.9286", "−0.5 + 0.5 + 0.5 − 0.5 = 0", "0 + 0.5 + 1 − 1.5 = 0", "1 + 1.3571 + 0.7143 − 0.9286 = 2.1429", "0 + 1.3571 + 1.4286 − 2.7857 = 0", "RSS 1.0", "RSS 4.2143", "x", "0", "1", "2", "3".

### Prompt 3 (Subject capstone): The deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[planned] ⏳ not rendered
Save as: `../Mathematics/Statistics/assets/least-squares-line-deep-dive-sheet.webp`

Visual thesis: Read the run one field at a time: the four sums 6, 12, 14 and 23 give S_xx = S_xy = 5, so b = 1 and a = 1.5; the residuals balance with RSS 1; dropping the intercept gives RSS 4.2143; lstsq returns the same line.

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

Production: Use a deterministic figure script. A tall sheet of exactly four panes stacked vertically, each the full width, designed for reading at 800 px wide; add height rather than shrinking text, with output and field text at least 20 px at that width. The first two panes are compact reminders of the form and the mechanism, not full copies. The run pane is the focal pane. Field cards run 1 to 6 in one column in the same order as the markers, each starting with its red number, and are matched to the output by number alone: no leader lines between panes.

Scene: Pane 1, The form: a compact reminder of prompt 1, the four dots, the blue line y = 1.5 + x and the four squares of area 0.25, with "RSS = Σ (y_i − a − b x_i)²" above. Pane 2, The mechanism: a compact reminder of prompt 2, the two level beams under the blue line and the tipped beam under the orange line, with "RSS 1.0" and "RSS 4.2143". Pane 3, The run: six lines of monospace output, exactly: $ python least_squares_line.py | n 4, sum x 6, sum y 12, sum x^2 14, sum xy 23 | xbar 1.5, ybar 3, S_xx 5, S_xy 5, slope b 1, intercept a 1.5 | residuals [-0.5, 0.5, 0.5, -0.5] RSS 1 sum r 0 sum x*r 0 | no intercept: slope 1.6429, residuals [1.0, 1.3571, 0.7143, -0.9286] RSS 4.2143, sum r 2.1429 | lstsq [a, b]: [1.5 1. ]  M^T M: [[4.0, 6.0], [6.0, 14.0]]  M^T y: [12.0, 23.0] (the | marks a new line and is not printed; keep the two spaces before "M^T M:" and before "M^T y:", and the space inside "[1.5 1. ]"). Red markers: 1 after 23 on the sums line, 2 after S_xy 5, 3 after intercept a 1.5, 4 after sum x*r 0, 5 after sum r 2.1429, 6 after [12.0, 23.0]. Pane 4, Reading it: six cards in order.

Cast: the reminder plot, the reminder beams, the output block, six numbered field cards.

Flows: none between panes.

Text in the image, spelled exactly: "The form", "The mechanism", "The run", "Reading it", "RSS = Σ (y_i − a − b x_i)²", "RSS 1.0", "RSS 4.2143", "$ python least_squares_line.py", "1 the four sums the line needs", "2 centred sums: S_xx = 5, S_xy = 5", "3 b = 5 / 5 = 1, a = 3 − 1 × 1.5 = 1.5", "4 residuals add to 0, RSS 1", "5 no intercept: RSS 4.2143, residuals add to 2.1429", "6 lstsq gives the same a and b".

Exclusions: no fifth pane, no leader lines between panes, no altered output text, no wrapped output line that loses its spacing, no legend panel or colour key, no matrix inverse anywhere. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The five output lines match the note's captured run of `least_squares_line.py` character for character, runs of spaces included; markers 1 to 6 sit after the same fields as the note's rendered output picture `least-squares-four-points-output.png`, where markers 2 and 3 share the second output line; four panes only; no legend anywhere. Every label in the image, exactly: "The form", "The mechanism", "The run", "Reading it", "RSS = Σ (y_i − a − b x_i)²", "RSS 1.0", "RSS 4.2143", "$ python least_squares_line.py", "1 the four sums the line needs", "2 centred sums: S_xx = 5, S_xy = 5", "3 b = 5 / 5 = 1, a = 3 − 1 × 1.5 = 1.5", "4 residuals add to 0, RSS 1", "5 no intercept: RSS 4.2143, residuals add to 2.1429", "6 lstsq gives the same a and b".

## Process lane

Navigation: ⬅️ [Prompt 3 (Subject capstone): The deep-dive sheet](#prompt-3-subject-capstone-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
