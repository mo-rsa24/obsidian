# Central Limit Theorem: illustrated map

The drawn pictures for the vault note [[Central Limit Theorem]]: its form, its mechanism, and the deep-dive sheet that composes them with the `clt.py` run and the fourth moment of a sum. `3 prompts · 0 rendered · 3 waiting`

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Glyph vocabulary](#glyph-vocabulary)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane](#subject-lane)
- [Prompt 1 (Subject): The central limit theorem, the form](#prompt-1-subject-the-central-limit-theorem-the-form)
- [Prompt 2 (Subject): The central limit theorem, the mechanism](#prompt-2-subject-the-central-limit-theorem-the-mechanism)
- [Prompt 3 (Subject capstone): The central limit theorem, the deep-dive sheet](#prompt-3-subject-capstone-the-central-limit-theorem-the-deep-dive-sheet)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[Central Limit Theorem]]: the theorem's form, mechanism and deep-dive sheet. A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: nothing here needs a repeatable named look. Zoom depth: one level, the three pictures a vault note gets. The style paragraph is embedded verbatim at the head of every prompt.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. Nothing in these pictures is a real-world object or a real product. The run pane of prompt 3 copies five lines of `../Mathematics/Statistics/assets/clt-fingerprints-close-in-on-the-bell.png`, which may be attached for its layout.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Amber: the lopsided variable $X$ (its two bars and its moments). Blue: the scaled sum $Y_n$ with $\frac{1}{\sqrt n}$ and its fingerprint values. Grey-blue dashed: the bell's target $e^{1/2}$. Red: the plain sum with no scaling. Green: the average, scaled by $\frac1n$. Purple: the fourth moment of a sum. Grey is structural only (axes, leader lines, dividers). No other colour carries a meaning.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A bar on a number line is one value of $X$ with its probability as height (primary tier). A dot over $n$ is one fingerprint value at $\lambda = 1$ (primary tier). An operation card holds one line of algebra (artifact tier).

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Left to right: one draw, then the scaled sum of many, then the fingerprint as $n$ grows on a scale where 1, 4, 16, 100 and 10000 are evenly spaced. A plot over a value is a distribution; a plot over $n$ is a fingerprint at $\lambda = 1$, and the two are never drawn on one axis.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Numbered markers in prompt 3's run pane, matching the note's field table. Dashed target lines. No step badges or phase containers.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The central limit theorem, the form](#prompt-1-subject-the-central-limit-theorem-the-form) ➡️

The three pictures for the theorem. Every number drawn comes from the note's worked examples or its `clt.py` and `fourth.py` outputs.

### Prompt 1 (Subject): The central limit theorem, the form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The central limit theorem, the mechanism](#prompt-2-subject-the-central-limit-theorem-the-mechanism) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Statistics/assets/clt-the-form.webp`

Visual thesis: A lopsided variable with mean 0 and variance 1, summed n times and scaled by one over root n, has a fingerprint at lambda = 1 that climbs from 1.346044 to within 0.250% of the bell's 1.648721.

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

Production: Use a deterministic figure script for the bars, the dots, the dashed line, the axes and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "Many lopsided draws, one bell". Three panels left to right.
Panel 1, titled "One draw": a number line from -2.5 to 1 (ticks -2, -1, 0, 0.5) with two amber bars, at -2 of height 0.2 labelled "0.2" and at 0.5 of height 0.8 labelled "0.8". Under it three amber chips: "mean 0", "variance 1", "E[X^3] = -1.5".
Panel 2, titled "Scale the sum": one blue operation card "Y_n = (X_1 + ... + X_n) / sqrt n" with two chips under it: "mean 0, variance 1 at every n" and "fingerprint M_X(lambda / sqrt n)^n".
Panel 3, titled "Fingerprint at lambda = 1": a plot with horizontal axis "n" with five evenly spaced ticks "1", "4", "16", "100", "10000", and vertical axis from 1.3 to 1.7 (ticks 1.3, 1.4, 1.5, 1.6, 1.7). Five blue dots at heights 1.346044, 1.468344, 1.551337, 1.608291, 1.644606, the first labelled "1.346044" and the last "1.644606". A grey-blue dashed line at 1.648721 labelled "bell: e^(1/2) = 1.648721". Small grey shortfall labels beside the dots: "18.358%", "10.940%", "5.907%", "2.452%", "0.250%".
A grey arrow from panel 1 to panel 2 and from panel 2 to panel 3.

Cast: one number line with two bars and three chips, one operation card with two chips, one plot with five dots, one dashed line and five shortfall labels, two arrows.

Flows: two grey arrows left to right.

Text in the image, spelled exactly: "Many lopsided draws, one bell", "One draw", "-2", "-1", "0", "0.5", "0.2", "0.8", "mean 0", "variance 1", "E[X^3] = -1.5", "Scale the sum", "Y_n = (X_1 + ... + X_n) / sqrt n", "mean 0, variance 1 at every n", "fingerprint M_X(lambda / sqrt n)^n", "Fingerprint at lambda = 1", "n", "1", "4", "16", "100", "10000", "1.3", "1.4", "1.5", "1.6", "1.7", "1.346044", "1.644606", "bell: e^(1/2) = 1.648721", "18.358%", "10.940%", "5.907%", "2.452%", "0.250%"

Exclusions: no bell curve drawn over the bars, no dot above the dashed line, no connecting curve, no coin, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The amber bars stand at -2 (height 0.2) and 0.5 (height 0.8), four to one in height. The five blue dots sit at 1.346044, 1.468344, 1.551337, 1.608291, 1.644606, all below the dashed 1.648721, measurable on the 1.3 to 1.7 axis, and rising with n. Numbers from the note's [[Central Limit Theorem#Worked on a lopsided variable]] table and markers 1 to 7 of the `clt.py` run. Every label in the image, exactly: the 35 strings in the Text list above.

### Prompt 2 (Subject): The central limit theorem, the mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The central limit theorem, the form](#prompt-1-subject-the-central-limit-theorem-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject capstone): The central limit theorem, the deep-dive sheet](#prompt-3-subject-capstone-the-central-limit-theorem-the-deep-dive-sheet) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Statistics/assets/clt-the-mechanism.webp`

Visual thesis: The log of the fingerprint is t squared over 2 plus a t cubed term, and putting t = lambda over root n and multiplying by n keeps lambda squared over 2 while the cubed term shrinks like one over root n; scaling by nothing or by one over n sends the fingerprint to infinity or to 1 instead.

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

Production: Use a deterministic figure script for the cards, the three lanes and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "Why only lambda^2/2 survives". Two bands.
Band 1: four blue operation cards left to right joined by grey arrows with short grey labels. Card 1: "M_X(t) = 1 + t^2/2 + E[X^3] t^3/6 + ...". Arrow label "take the log". Card 2: "log M_X(t) = t^2/2 + E[X^3] t^3/6 + ...". Arrow label "t = lambda/sqrt n, times n". Card 3: "lambda^2/2 + E[X^3] lambda^3/(6 sqrt n) + ...". Arrow label "n grows". Card 4 (bold border): "-> lambda^2/2, so M -> e^(lambda^2/2)". Under card 3 a small grey note: "lopsided X, lambda = 1: 0.5 - 0.25/sqrt n".
Band 2, titled "Three scalings, at lambda = 1": three horizontal lanes, each a row of value chips ending in an arrow to a result chip.
Red lane labelled "no scaling: M_X(1)^n": chips "n = 4: 3.282745", "n = 16: 116.131085", result chip "grows without end".
Blue lane labelled "1/sqrt n: M_X(1/sqrt n)^n": chips "n = 16: 1.551337", "n = 10000: 1.644606", result chip "-> e^(1/2) = 1.648721".
Green lane labelled "1/n: M_X(1/n)^n": chips "n = 16: 1.030740", "n = 10000: 1.000050", result chip "-> 1, the mean".

Cast: four operation cards, three labelled arrows and one note in band 1; three lanes with six value chips, three arrows and three result chips in band 2.

Flows: three grey arrows in band 1; one arrow per lane in band 2.

Text in the image, spelled exactly: "Why only lambda^2/2 survives", "M_X(t) = 1 + t^2/2 + E[X^3] t^3/6 + ...", "take the log", "log M_X(t) = t^2/2 + E[X^3] t^3/6 + ...", "t = lambda/sqrt n, times n", "lambda^2/2 + E[X^3] lambda^3/(6 sqrt n) + ...", "n grows", "-> lambda^2/2, so M -> e^(lambda^2/2)", "lopsided X, lambda = 1: 0.5 - 0.25/sqrt n", "Three scalings, at lambda = 1", "no scaling: M_X(1)^n", "n = 4: 3.282745", "n = 16: 116.131085", "grows without end", "1/sqrt n: M_X(1/sqrt n)^n", "n = 16: 1.551337", "n = 10000: 1.644606", "-> e^(1/2) = 1.648721", "1/n: M_X(1/n)^n", "n = 16: 1.030740", "n = 10000: 1.000050", "-> 1, the mean"

Exclusions: no plot, no coin, no fourth lane, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Band 1 is steps 3 to 7 of [[Central Limit Theorem#The method, step by step]]; the note's "0.25/sqrt n" is $\frac{-1.5}{6\sqrt n}$ with its sign carried as the minus. Band 2's chips are markers 9 and 10 of the `clt.py` run and its table, from [[Central Limit Theorem#Where it goes wrong: the wrong scaling]]. Every label in the image, exactly: the 22 strings in the Text list above.

### Prompt 3 (Subject capstone): The central limit theorem, the deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The central limit theorem, the mechanism](#prompt-2-subject-the-central-limit-theorem-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Statistics/assets/clt-deep-dive-sheet.webp`

Visual thesis: One sheet holds the lopsided variable, the log route to lambda squared over 2, the run that shows the fingerprints closing in, what the fingerprints do not prove, and the fourth moment of a sum heading to the bell's 3.

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

Production: Use a deterministic figure script for every bar, terminal line and all typography. Compose as a portrait sheet for reading at 1000 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A sheet title across the top: "Y_n = (X_1 + ... + X_n) / sqrt n -> the bell". Five rounded panes.
Pane 1, top left, titled "One lopsided draw": two amber bars at -2 (height 0.2) and 0.5 (height 0.8), with the chips "mean 0, variance 1" and "E[X^3] = -1.5, E[X^4] = 3.25".
Pane 2, top right, titled "Through the log": the blue line "n log M_X(lambda/sqrt n) = lambda^2/2 + E[X^3] lambda^3/(6 sqrt n) + ..." with the chip "-> lambda^2/2" and a small grey chip "proves the fingerprints converge; the CDF needs Berry-Esseen".
Pane 3, middle, full width, titled "The run": a light terminal card in monospace showing exactly these six lines:
"$ python3 clt.py"
"the bell's fingerprint at lambda = 1: e^(1/2) = 1.648721"
"n =     1: M_X(1/sqrt n)^n = 1.346044  short by 18.358%  e^(1/2 + E[X^3]/(6 sqrt n)) = 1.284025"
"n =   100: M_X(1/sqrt n)^n = 1.608291  short by  2.452%  e^(1/2 + E[X^3]/(6 sqrt n)) = 1.608014"
"n = 10000: M_X(1/sqrt n)^n = 1.644606  short by  0.250%  e^(1/2 + E[X^3]/(6 sqrt n)) = 1.644605"
"slip, no scaling: M_X(1)^4 = 3.282745  M_X(1)^16 = 116.131085"
with five small numbered orange markers placed just above: 1 over "1.648721", 2 over "1.346044", 3 over the first "1.644606", 4 over "1.644605", 5 over "116.131085".
Pane 4, below the run, titled "Reading the run": five small cards in a grid, numbered 1 to 5 to match the markers, each with exactly this text:
1 "the bell's fingerprint, the target"
2 "one draw: 18.358% short"
3 "ten thousand draws: 0.250% short"
4 "the lambda^3 term predicts it"
5 "no scaling: no limit"
Pane 5, bottom, full width, titled "The fourth moment of a sum": the purple line "E[S^4] = n E[X^4] + 3n(n - 1) E[X^2]^2", then three chips: "three coins: 3 + 18 = 21 = (81 + 3 + 3 + 81)/8", "lopsided, scaled: 3 + 0.25/n -> 3", and a red chip "pair term dropped: 0.333333, under 1".

Cast: two bars with two chips, one formula line with two chips, one terminal card with five markers, five reading cards, one formula line with three chips.

Flows: none; markers and cards are matched by number.

Text in the image, spelled exactly: "Y_n = (X_1 + ... + X_n) / sqrt n -> the bell", "One lopsided draw", "mean 0, variance 1", "E[X^3] = -1.5, E[X^4] = 3.25", "Through the log", "n log M_X(lambda/sqrt n) = lambda^2/2 + E[X^3] lambda^3/(6 sqrt n) + ...", "-> lambda^2/2", "proves the fingerprints converge; the CDF needs Berry-Esseen", "The run", the six terminal lines above, the markers "1" to "5", "Reading the run", the five card texts above, "The fourth moment of a sum", "E[S^4] = n E[X^4] + 3n(n - 1) E[X^2]^2", "three coins: 3 + 18 = 21 = (81 + 3 + 3 + 81)/8", "lopsided, scaled: 3 + 0.25/n -> 3", "pair term dropped: 0.333333, under 1"

Exclusions: no terminal line other than the six given, no marker over the wrong field, no card longer than its given text, no sixth pane, no coin fingerprint, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Five panes, the deep-dive exception's maximum. The five output lines are copied character for character from the `clt.py` run (`assets/clt-fingerprints-close-in-on-the-bell.png`), including the padded spaces after "n =" and "short by"; the sheet's markers 1 to 5 sit over the fields the note's markers 4, 5, 7, 8 and 9 mark. Pane 2's grey chip states what [[Central Limit Theorem#What the fingerprints prove, and what they do not]] says, citing Chan pp. 390 to 391. Pane 5's numbers are the note's [[Central Limit Theorem#Worked on three fair coins]] and the `fourth.py` run's markers 1, 2 and 4. Every label in the image, exactly: the strings in the Text list above, with the six terminal lines and five card texts written out in the Scene.

## Process lane

Navigation: ⬅️ [Prompt 3 (Subject capstone): The central limit theorem, the deep-dive sheet](#prompt-3-subject-capstone-the-central-limit-theorem-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note has no plan tree to draw over it.
