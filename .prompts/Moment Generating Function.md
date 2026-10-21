# Moment Generating Function: illustrated map

The drawn pictures for the vault note [[Moment Generating Function]]: its form, its mechanism, the deep-dive sheet that composes them with step 6's run, and the concept picture of a large dial reading the tails. `4 prompts · 1 rendered · 2 stuck · 0 rendering · 1 waiting`

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Glyph vocabulary](#glyph-vocabulary)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane](#subject-lane)
- [Prompt 1 (Subject): The fingerprint, the form](#prompt-1-subject-the-fingerprint-the-form)
- [Prompt 2 (Subject): The fingerprint, the mechanism](#prompt-2-subject-the-fingerprint-the-mechanism)
- [Prompt 3 (Subject capstone): The fingerprint, the deep-dive sheet](#prompt-3-subject-capstone-the-fingerprint-the-deep-dive-sheet)
- [Prompt 4 (Subject): The fingerprint, a large dial weighs the tails](#prompt-4-subject-the-fingerprint-a-large-dial-weighs-the-tails)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[Moment Generating Function]]: the fingerprint's form, mechanism and deep-dive sheet. A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: nothing here needs a repeatable named look. Zoom depth: one level, the three pictures a vault section gets. The style paragraph is embedded verbatim at the head of every prompt.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. Nothing in these pictures is a real-world object or a real product. The run pane of prompt 3 copies the text of `assets/mgf-the-fingerprints-tell-the-shapes-apart.png`, the rendered output of step 6, which may be attached for its layout.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Blue: the standard normal $\mathcal{N}(0, 1)$, its bell and its fingerprint $e^{\lambda^2/2}$. Orange: the weighted integrand $e^{\lambda u}\varphi(u)$, the bell after the weight is applied. Purple: $\mathcal{N}(0, 2)$ and its fingerprint $e^{\lambda^2}$. Green: the $\pm 1$ coins: the sum of two flips and its fingerprint $\cosh(\lambda)^2$, and in prompt 4 one flip and its two values. Grey is structural only (axes, brackets, dividers). No other colour carries a meaning.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A bell curve is a distribution over $u$ (primary tier). A rising curve over $\lambda$ is a fingerprint (primary tier). Three green bars on a number line are the coin sum's three values (primary tier). An operation card holds one line of algebra (artifact tier).

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Left to right: what goes in, the average, what comes out. A plot over $u$ is a distribution; a plot over $\lambda$ is a fingerprint, and the two are never drawn on one axis.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Numbered markers in prompt 3's run pane, matching the note's field table. Shaded areas under curves. No step badges or phase containers.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The fingerprint, the form](#prompt-1-subject-the-fingerprint-the-form) ➡️

The three pictures for the fingerprint. Every number drawn comes from the note's own derivation or its step 4 and step 6 outputs.

### Prompt 1 (Subject): The fingerprint, the form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The fingerprint, the mechanism](#prompt-2-subject-the-fingerprint-the-mechanism) ➡️

[built] ⚠️ stuck: pixel check after 3 revisions, purple leaves the top at lambda -1.517 and +1.482 (needs plus and minus 1.442) and reads 2.94 at lambda -1 (needs 2.7183), blue reads 3.22 and 3.43 at plus and minus 1.5 (needs 3.0802); axis spacing, the three heights at lambda +1, labels and card pass; last attempt ~/.cache/codex-drop/obsidian/mgf-the-form.png
Save as: `../Mathematics/Statistics/assets/mgf-the-form.webp`

Visual thesis: A fingerprint turns a distribution into one curve over the dial lambda, every curve starts at 1, and two distributions with the same variance can still have different curves.

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

Production: Use a deterministic figure script for all three curves, the axes and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "One curve per distribution". Two panels left to right.
Panel 1, titled "The form": one operation card holding the line "M_Z(lambda) = E[ e^(lambda Z) ]" in monospace. Four short grey leader labels point at its parts: at "Z" the label "the random variable", at "lambda" the label "a dial you choose", at "e^(lambda Z)" the label "the weight", at "E[ ]" the label "average over Z". Under the card one chip: "every M is 1 at lambda = 0".
Panel 2, titled "Three fingerprints": a plot with horizontal axis "lambda" from -2 to 2 (ticks -2, -1, 0, 1, 2) and vertical axis from 0 to 8 (ticks 0, 2, 4, 6, 8). Three curves, all symmetric about lambda = 0 and all passing through the point (0, 1), which carries a small grey dot labelled "1". Blue curve e^(lambda^2/2): 1.6487 at lambda = plus and minus 1, 7.3891 at plus and minus 2, staying inside the frame; labelled "N(0, 1): e^(lambda^2/2)". Purple curve e^(lambda^2): 2.7183 at plus and minus 1, leaving the top of the frame at lambda = plus and minus 1.442; labelled "N(0, 2): e^(lambda^2)". Green curve cosh(lambda)^2: 2.3811 at plus and minus 1, leaving the top of the frame at lambda = plus and minus 1.700, so it lies between blue and purple; labelled "two coin flips: cosh^2". At lambda = 1 a thin grey vertical guide with three small value chips in the curves' own colours: "1.6487", "2.3811", "2.7183". Under the plot one line: "green and purple: both variance 2".

Cast: one operation card with four leader labels and one chip, one plot with three curves, one shared dot, one guide with three value chips, one footer line.

Flows: none; leader lines only.

Text in the image, spelled exactly: "One curve per distribution", "The form", "M_Z(lambda) = E[ e^(lambda Z) ]", "the random variable", "a dial you choose", "the weight", "average over Z", "every M is 1 at lambda = 0", "Three fingerprints", "lambda", "-2", "-1", "0", "1", "2", "4", "6", "8", "N(0, 1): e^(lambda^2/2)", "N(0, 2): e^(lambda^2)", "two coin flips: cosh^2", "1.6487", "2.3811", "2.7183", "green and purple: both variance 2"

Exclusions: no curve that misses the point (0, 1), no bell curves in this picture, no fourth curve, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: All three curves pass through (0, 1) and are symmetric about lambda = 0. At lambda = 1 the heights are 1.6487 (blue), 2.3811 (green) and 2.7183 (purple), in that order from bottom to top, measurable in pixels on the 0 to 8 axis; blue reaches 7.3891 at lambda = 2 inside the frame, purple leaves the top at lambda = 1.442 and green at 1.700. Numbers from the note's step 6 output and [[Moment Generating Function#Where variance cannot tell two shapes apart]], recomputed with `math.exp` and `math.cosh`. The axis is lambda, never u. Every label in the image, exactly: the 25 strings in the Text list above.

### Prompt 2 (Subject): The fingerprint, the mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The fingerprint, the form](#prompt-1-subject-the-fingerprint-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject capstone): The fingerprint, the deep-dive sheet](#prompt-3-subject-capstone-the-fingerprint-the-deep-dive-sheet) ➡️

[built] 🖼️ rendered 2026-10-20: `mgf-the-mechanism.webp`
Save as: `../Mathematics/Statistics/assets/mgf-the-mechanism.webp`

Visual thesis: Weighting the standard normal bell by e to the lambda u slides it right by lambda and stretches it up by e to the lambda squared over 2, so its area, the fingerprint, is e to the lambda squared over 2.

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

Production: Use a deterministic figure script for both curves, the shading, the axes and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "The weight slides and stretches the bell". One plot with horizontal axis "u" from -3 to 4 (ticks -3, -2, -1, 0, 1, 2, 3, 4) and vertical axis from 0 to 0.7 (ticks 0, 0.2, 0.4, 0.6).
The blue curve is the standard normal density phi(u), peak 0.398942 at u = 0, its area shaded pale blue and labelled "phi(u), area 1".
The orange curve is e^(u) phi(u), which equals 1.648721 x phi(u - 1): the same bell shape with its peak moved to u = 1 and its height multiplied by 1.648721, peak 0.657745 at u = 1; it passes through 0.398942 at u = 0 and at u = 2, and 0.089016 at u = -1 and u = 3. Its area shaded pale orange and labelled "e^(u) phi(u), area 1.648721".
A grey horizontal arrow from the blue peak to directly under the orange peak, labelled "slide right by lambda = 1". A grey vertical arrow at u = 1 from height 0.398942 up to 0.657745, labelled "stretch by e^(1/2) = 1.648721".
Below the plot, one operation card in monospace: "lambda u - u^2/2 = -(u - lambda)^2/2 + lambda^2/2", with a chip under it: "so M(lambda) = e^(lambda^2/2)".

Cast: two bell curves (blue, orange) with shaded areas, two grey arrows, one operation card, one result chip.

Flows: the two grey arrows only.

Text in the image, spelled exactly: "The weight slides and stretches the bell", "u", "-3", "-2", "-1", "0", "1", "2", "3", "4", "0.2", "0.4", "0.6", "phi(u), area 1", "e^(u) phi(u), area 1.648721", "slide right by lambda = 1", "stretch by e^(1/2) = 1.648721", "lambda u - u^2/2 = -(u - lambda)^2/2 + lambda^2/2", "so M(lambda) = e^(lambda^2/2)"

Exclusions: no orange bell wider or narrower than the blue one, no third curve, no fingerprint curve over lambda, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The two bells have the same width at half their height (2.355 axis units each); the orange one peaks at u = 1 with height 0.657745 and the blue at u = 0 with height 0.398942, a ratio of 1.648721; the orange curve crosses 0.398942 at u = 0 and u = 2. Numbers copied from the note's step 4 output (`assets/mgf-the-integrand-is-a-shifted-bell.png`). The shaded areas are labelled 1 and 1.648721. Every label in the image, exactly: the 19 strings in the Text list above.

### Prompt 3 (Subject capstone): The fingerprint, the deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The fingerprint, the mechanism](#prompt-2-subject-the-fingerprint-the-mechanism) | 📋 [TOC](#table-of-contents) | [Prompt 4 (Subject): The fingerprint, a large dial weighs the tails](#prompt-4-subject-the-fingerprint-a-large-dial-weighs-the-tails) ➡️

[built] ⚠️ stuck: panes 1 and 2 pixel check after 3 revisions; pane 1's lambda ticks are uneven (gaps 91, 99.5, 103.5, 89.5 px) and purple reads 3.65 at lambda -1 and 3.06 at +1 (needs 2.7183); pane 2's blue bell crosses half height at u -1.04 and +0.93 (needs plus and minus 1.177) and the orange at -0.12 and 2.11 (needs -0.177 and 2.177), so the widths are 1.97 and 2.23 (need 2.355 each); title, terminal lines, six markers, six cards and pane 5 pass; last attempt ~/.cache/codex-drop/obsidian/mgf-deep-dive-sheet.png
Save as: `../Mathematics/Statistics/assets/mgf-deep-dive-sheet.webp`

Visual thesis: One sheet holds the fingerprint's form, why the bell's fingerprint is e to the lambda squared over 2, the run that tells a bell from a coin sum with the same variance, and where the forward process uses the product rule.

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

Production: Use a deterministic figure script for every curve, terminal line and all typography. Compose as a portrait sheet for reading at 1000 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A sheet title across the top: "M(lambda) = E[e^(lambda Z)]". Five rounded panes.
Pane 1, top left, titled "The form": the card "M_Z(lambda) = E[ e^(lambda Z) ]" with the chip "every M is 1 at lambda = 0", and a small plot over "lambda" from -2 to 2 with the blue curve "N(0, 1)", the green curve "two coin flips" and the purple curve "N(0, 2)", all through the point (0, 1), heights at lambda = 1 of 1.6487, 2.3811 and 2.7183 from bottom to top.
Pane 2, top right, titled "Why: complete the square": over an axis "u" from -3 to 4, the blue bell "phi(u)" peaking at u = 0 and the orange bell "e^(u) phi(u)" of the same width peaking at u = 1, 1.648721 times as tall; the line "area: e^(lambda^2/2)".
Pane 3, middle, full width, titled "The run": a light terminal card in monospace showing exactly these five lines:
"$ python3 fingerprint.py"
"N(0,1) lam 1.0: grid 1.648721  e^(lam^2/2) 1.648721"
"N(0,1) lam 2.0: grid 7.389056  e^(lam^2/2) 7.389056"
"coins  lam 1.0: two flips 2.381098  cosh(lam)^2 2.381098  N(0,2) e^(lam^2) 2.718282"
"coins  lam 2.0: two flips 14.154116  cosh(lam)^2 14.154116  N(0,2) e^(lam^2) 54.598150"
with six small numbered orange markers placed just above: 1 over the first "grid 1.648721", 2 over the first "e^(lam^2/2) 1.648721", 3 over "two flips 2.381098", 4 over "cosh(lam)^2 2.381098", 5 over "e^(lam^2) 2.718282", 6 over "54.598150".
Pane 4, below the run, titled "Reading the run": six small cards in a grid, numbered 1 to 6 to match the markers, each with exactly this text:
1 "the integral, added up on a grid"
2 "closed form agrees to six decimals"
3 "coin sum, from its four outcomes"
4 "product of two coin fingerprints"
5 "what N(0, 2) would give: different"
6 "the gap grows: bells have tails"
Pane 5, bottom, full width, titled "Where it is used": the line "e^(0.04 lambda^2) x e^(0.1 lambda^2) = e^(0.28 lambda^2 / 2)" with the chip "two noises, one N(0, 0.28) draw", and beside it in green the line "cosh(lambda)^2 is not e^(lambda^2)" with the chip "variance 2, not a bell".

Cast: one card, one small fingerprint plot with three curves, two bells, one terminal card with six markers, six reading cards, two formula lines with two chips.

Flows: none; markers and cards are matched by number.

Text in the image, spelled exactly: "M(lambda) = E[e^(lambda Z)]", "The form", "M_Z(lambda) = E[ e^(lambda Z) ]", "every M is 1 at lambda = 0", "lambda", "N(0, 1)", "two coin flips", "N(0, 2)", "Why: complete the square", "u", "phi(u)", "e^(u) phi(u)", "area: e^(lambda^2/2)", "The run", the five terminal lines above, the markers "1" to "6", "Reading the run", the six card texts above, "Where it is used", "e^(0.04 lambda^2) x e^(0.1 lambda^2) = e^(0.28 lambda^2 / 2)", "two noises, one N(0, 0.28) draw", "cosh(lambda)^2 is not e^(lambda^2)", "variance 2, not a bell"

Exclusions: no terminal line other than the five given, no marker over the wrong field, no card longer than its given text, no sixth pane, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Five panes, the deep-dive exception's maximum. The terminal lines are copied character for character from the note's step 6 output and its rendered picture `assets/mgf-the-fingerprints-tell-the-shapes-apart.png`; the six markers sit over the same fields as that picture's markers 1 to 6. Pane 1's curve heights at lambda = 1 are 1.6487, 2.3811 and 2.7183 in that order; pane 2's bells share one width and the orange peak is 1.648721 times the blue. The six cards each stay under 20 words and match the note's field table rows fingerprint 1 to 6. Pane 5's numbers: $0.04 + 0.1 = 0.14 = 0.28/2$ and $1.040811 \times 1.105171 = 1.150274$ from step 8. Every label in the image, exactly: the strings in the Text list above, with the five terminal lines and six card texts written out in the Scene.

### Prompt 4 (Subject): The fingerprint, a large dial weighs the tails

Navigation: ⬅️ [Prompt 3 (Subject capstone): The fingerprint, the deep-dive sheet](#prompt-3-subject-capstone-the-fingerprint-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Statistics/assets/mgf-a-large-dial-reads-the-tails.webp`

Visual thesis: A small dial reads the middle of the bell, where a coin and the bell agree, and a large dial reads the tail beyond 2, where the coin has nothing, so the coin's and the bell's fingerprints part as the dial grows.

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

Production: Use a deterministic figure script for both curves, the bars, the shading, the axes and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "A large dial reads the tails". Two rounded panes side by side, with the same axes: horizontal axis "u" from -3 to 5 (ticks -3, -2, -1, 0, 1, 2, 3, 4, 5) and vertical axis from 0 to 0.6 (ticks 0, 0.2, 0.4, 0.6).
Left pane titled "small dial, lambda = 0.5". The orange curve is the share of the fingerprint, phi(u - 0.5): a standard bell with peak 0.398942 at u = 0.5, labelled "where M(0.5) comes from". A grey dashed vertical line at u = 2 labelled "u = 2". The area under the orange curve to the right of u = 2 is shaded solid orange and labelled "0.0668 of M(0.5)". Two green bars at u = -1 and u = 1, each of height 0.5, labelled once between them "the coin: only -1 and 1". A chip at the bottom of the pane: "bell / coin = 1.0049".
Right pane titled "large dial, lambda = 2.5". The same orange curve slid to peak 0.398942 at u = 2.5, labelled "where M(2.5) comes from"; the same grey dashed line at u = 2 labelled "u = 2"; the area to the right of u = 2 shaded solid orange and labelled "0.6915 of M(2.5)"; the same two green bars at u = -1 and u = 1 with the label "the coin: only -1 and 1". A chip at the bottom of the pane: "bell / coin = 3.7115".

Cast: two orange bells with shaded tails, two grey dashed lines, four green bars, two chips.

Flows: none.

Text in the image, spelled exactly: "A large dial reads the tails", "small dial, lambda = 0.5", "large dial, lambda = 2.5", "u", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5", "0.2", "0.4", "0.6", "where M(0.5) comes from", "where M(2.5) comes from", "u = 2", "0.0668 of M(0.5)", "0.6915 of M(2.5)", "the coin: only -1 and 1", "bell / coin = 1.0049", "bell / coin = 3.7115"

Exclusions: no orange bell wider or narrower than a standard bell, no bell taller than 0.398942, no green bar anywhere but u = -1 and u = 1, no shading left of u = 2, no fingerprint curve over lambda, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The orange curve in each pane is $e^{\lambda u}\varphi(u)/e^{\lambda^2/2} = \varphi(u - \lambda)$, the share of the fingerprint carried at each $u$, derived in the note's section "A large dial weighs the tails"; both bells have the standard width, 2.355 axis units at half height. Left pane: peak 0.398942 at u = 0.5, height 0.129518 at u = 2, shaded area 0.0668. Right pane: peak 0.398942 at u = 2.5, height 0.352065 at u = 2, shaded area 0.6915. The shares and the ratios 1.0049 and 3.7115 are copied from the note's `tails.py` output (`assets/mgf-a-large-dial-weighs-the-tails.png`). The green bars are probabilities (1/2 each), drawn on the same axis as the densities only to show where the coin can land. Every label in the image, exactly: the 24 strings in the Text list above.

## Process lane

Navigation: ⬅️ [Prompt 4 (Subject): The fingerprint, a large dial weighs the tails](#prompt-4-subject-the-fingerprint-a-large-dial-weighs-the-tails) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
