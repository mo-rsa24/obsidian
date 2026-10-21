# The Limit That Defines E: illustrated map

The drawn pictures for the vault note [[The Limit That Defines E]]: its form, its mechanism, and the deep-dive sheet that composes them with the `limit.py` run. `3 prompts · 0 rendered · 3 waiting`

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Glyph vocabulary](#glyph-vocabulary)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane](#subject-lane)
- [Prompt 1 (Subject): The limit for e, the form](#prompt-1-subject-the-limit-for-e-the-form)
- [Prompt 2 (Subject): The limit for e, the mechanism](#prompt-2-subject-the-limit-for-e-the-mechanism)
- [Prompt 3 (Subject capstone): The limit for e, the deep-dive sheet](#prompt-3-subject-capstone-the-limit-for-e-the-deep-dive-sheet)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[The Limit That Defines E]]: the limit's form, mechanism and deep-dive sheet. A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: nothing here needs a repeatable named look. Zoom depth: one level, the three pictures a vault note gets. The style paragraph is embedded verbatim at the head of every prompt.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. Nothing in these pictures is a real-world object or a real product. The run pane of prompt 3 copies four lines of `../Mathematics/Calculus/Sequences And Series/assets/limit-for-e-the-run.png`, which may be attached for its layout.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Blue: $a = 1$ and its target e. Orange: $a = -0.3$ and its target $e^{-0.3}$. Purple: the log route ($n\log(1 + a/n)$ and its expansion). Red: the slip that says the power tends to 1. Grey is structural only (axes, leader lines, dividers). No other colour carries a meaning.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A dot over $n$ is one power $(1 + a/n)^n$ (primary tier). A dashed horizontal line is the target $e^a$. An operation card holds one line of algebra (artifact tier).

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Left to right: $n$ grows, on a scale where 1, 10, 100 and 1000 are evenly spaced. In the mechanism, left to right is one rewrite after another.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Numbered markers in prompt 3's run pane, matching the note's field table. Dashed target lines. No step badges or phase containers.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The limit for e, the form](#prompt-1-subject-the-limit-for-e-the-form) ➡️

The three pictures for the limit. Every number drawn comes from the note's tables or its `limit.py` output.

### Prompt 1 (Subject): The limit for e, the form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The limit for e, the mechanism](#prompt-2-subject-the-limit-for-e-the-mechanism) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Calculus/Sequences And Series/assets/limit-for-e-the-form.webp`

Visual thesis: In one plus a over n, raised to n, the power times the base's distance above 1 is always a, and the powers settle from below on e to the a, for a = 1 and for a = -0.3.

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

Production: Use a deterministic figure script for the dots, the dashed lines, the axes and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "One plus a little, many times". Two panels left to right.
Panel 1, titled "The form": one operation card holding "(1 + a/n)^n  ->  e^a" in monospace. Three grey leader labels point at its parts: at "1" the label "the start", at "a/n" the label "one share of the change a", at the exponent "n" the label "how many times". Under the card one chip: "power x (base - 1) = n x a/n = a".
Panel 2, titled "Settling on e^a": a plot with horizontal axis "n" with four evenly spaced ticks "1", "10", "100", "1000", and vertical axis from 0 to 3 (ticks 0, 1, 2, 3). Four blue dots at heights 2.000000, 2.593742, 2.704814, 2.716924, the last labelled "2.716924", under a blue dashed line at 2.718282 labelled "e = 2.718282". Four orange dots at heights 0.700000, 0.737424, 0.740484, 0.740785, under an orange dashed line at 0.740818 labelled "e^-0.3 = 0.740818". Small labels at the left of each row: "a = 1" in blue and "a = -0.3" in orange.

Cast: one operation card with three leader labels and one chip, one plot with eight dots and two dashed lines.

Flows: none; leader lines only.

Text in the image, spelled exactly: "One plus a little, many times", "The form", "(1 + a/n)^n  ->  e^a", "the start", "one share of the change a", "how many times", "power x (base - 1) = n x a/n = a", "Settling on e^a", "n", "1", "10", "100", "1000", "0", "2", "3", "2.716924", "e = 2.718282", "e^-0.3 = 0.740818", "a = 1", "a = -0.3"

Exclusions: no dot above its dashed line, no connecting curve through the dots, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Every dot sits below its dashed line: blue at 2.000000, 2.593742, 2.704814, 2.716924 under 2.718282, orange at 0.700000, 0.737424, 0.740484, 0.740785 under 0.740818, measurable on the 0 to 3 axis; the gap at n = 1000 is too small to see at this scale, which is the point. The n ticks are evenly spaced (a log scale). Numbers from the note's tables in [[The Limit That Defines E#The limit worked at a = 1 and a = -0.3]] and the `limit.py` run. Every label in the image, exactly: the 21 strings in the Text list above (the tick "1" serves both axes).

### Prompt 2 (Subject): The limit for e, the mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The limit for e, the form](#prompt-1-subject-the-limit-for-e-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject capstone): The limit for e, the deep-dive sheet](#prompt-3-subject-capstone-the-limit-for-e-the-deep-dive-sheet) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Calculus/Sequences And Series/assets/limit-for-e-the-mechanism.webp`

Visual thesis: Moving the power into an exponent and expanding the log leaves n times log of 1 plus a over n equal to a minus a squared over 2n, so the multiplication by n cancels one power of n from every term and only a survives; holding the base or the power wrong breaks this.

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

Production: Use a deterministic figure script for the cards, the table and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "Through the log, only a survives". Two bands.
Band 1: four purple operation cards left to right joined by grey arrows, each arrow carrying a short grey label. Card 1: "(1 + a/n)^n". Arrow label "power into the exponent". Card 2: "e^( n log(1 + a/n) )". Arrow label "expand the log". Card 3: "n ( a/n - a^2/(2n^2) + ... )". Arrow label "times n". Card 4 (bold border): "a - a^2/(2n) + ...  ->  a". Under card 4 a chip: "so the power -> e^a". Under card 3 a small grey note: "at a = 1, n = 1000: 0.999500".
Band 2, titled "The slip: the base tends to 1, so the power is 1": a small red-bordered table with columns "base", "power", "power x (base - 1)", "result" and three rows: "1.001", "1000", "1", "2.716924"; "1.001", "10000", "10", "21916.681339"; "1.0001", "1000", "0.1", "1.105165". Beside it a chip: "the product decides: e^1, e^10, e^0.1".

Cast: four operation cards, three labelled arrows, one chip and one note in band 1; one table with three rows and one chip in band 2.

Flows: three grey arrows from card 1 to card 4.

Text in the image, spelled exactly: "Through the log, only a survives", "(1 + a/n)^n", "power into the exponent", "e^( n log(1 + a/n) )", "expand the log", "n ( a/n - a^2/(2n^2) + ... )", "times n", "a - a^2/(2n) + ...  ->  a", "so the power -> e^a", "at a = 1, n = 1000: 0.999500", "The slip: the base tends to 1, so the power is 1", "base", "power", "power x (base - 1)", "result", "1.001", "1000", "1", "2.716924", "10000", "10", "21916.681339", "1.0001", "0.1", "1.105165", "the product decides: e^1, e^10, e^0.1"

Exclusions: no plot, no fourth table row, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Band 1 is steps 2 to 6 of [[The Limit That Defines E#The method through logs, step by step]]; "0.999500" is marker 2 of the `limit.py` run. Band 2 is the table in [[The Limit That Defines E#Where it goes wrong: the base tends to 1]], whose results are markers 4, 7 and 8 of the run. Every label in the image, exactly: the 26 strings in the Text list above ("1000" and "1.001" each appear twice in the table).

### Prompt 3 (Subject capstone): The limit for e, the deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The limit for e, the mechanism](#prompt-2-subject-the-limit-for-e-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Calculus/Sequences And Series/assets/limit-for-e-deep-dive-sheet.webp`

Visual thesis: One sheet holds the limit's form, the log route, the run that shows the log closing in on a and the power on e, the slip, and the place the central limit theorem uses the limit.

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

Production: Use a deterministic figure script for every dot, terminal line and all typography. Compose as a portrait sheet for reading at 1000 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A sheet title across the top: "(1 + a/n)^n -> e^a". Five rounded panes.
Pane 1, top left, titled "The form": the card "(1 + a/n)^n  ->  e^a" with the chip "power x (base - 1) = a", and a small plot over evenly spaced "1", "10", "100", "1000" with four blue dots under a dashed line "e = 2.718282".
Pane 2, top right, titled "Through the log": the purple line "n log(1 + a/n) = a - a^2/(2n) + ...  ->  a" with the chip "then e^(.) is continuous".
Pane 3, middle, full width, titled "The run": a light terminal card in monospace showing exactly these five lines:
"$ python3 limit.py"
"  n = 1000: base 1.001000  n log(base) 0.999500  a - a^2/(2n) 0.999500  power 2.716924"
"  1.001 ^ 10000 = 21916.681339"
"  1.0001 ^ 1000 = 1.105165"
"  n = 1000: n log(1 + 1/n + 3/n^2) = 1.002497"
with five small numbered orange markers placed just above: 1 over "n log(base) 0.999500", 2 over "a - a^2/(2n) 0.999500", 3 over "power 2.716924", 4 over "21916.681339", 5 over "1.002497".
Pane 4, below the run, titled "Reading the run": five small cards in a grid, numbered 1 to 5 to match the markers, each with exactly this text:
1 "the log of the power, near a = 1"
2 "the two-term prediction: equal"
3 "0.001358 short of e"
4 "base held fixed: no limit"
5 "extra 3/n^2: limit still 1"
Pane 5, bottom, full width, titled "Where it is used": the line "(1 + lambda^2/(2n) + smaller)^n -> e^(lambda^2/2)" with the chip "the last step of the central limit theorem".

Cast: one card, one chip and one small plot, one formula line with one chip, one terminal card with five markers, five reading cards, one formula line with one chip.

Flows: none; markers and cards are matched by number.

Text in the image, spelled exactly: "(1 + a/n)^n -> e^a", "The form", "(1 + a/n)^n  ->  e^a", "power x (base - 1) = a", "1", "10", "100", "1000", "e = 2.718282", "Through the log", "n log(1 + a/n) = a - a^2/(2n) + ...  ->  a", "then e^(.) is continuous", "The run", the five terminal lines above, the markers "1" to "5", "Reading the run", the five card texts above, "Where it is used", "(1 + lambda^2/(2n) + smaller)^n -> e^(lambda^2/2)", "the last step of the central limit theorem"

Exclusions: no terminal line other than the five given, no marker over the wrong field, no card longer than its given text, no sixth pane, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Five panes, the deep-dive exception's maximum. The four output lines are copied character for character from the `limit.py` run (`assets/limit-for-e-the-run.png`), with their leading spaces; the sheet's markers 1 to 5 sit over the fields the note's markers 2, 3, 4, 7 and 9 mark. Card 3's "0.001358" is $2.718282 - 2.716924$. Pane 5's bracket is Chan's step on PDF p. 390 with the smaller terms the note's step 7 allows. Every label in the image, exactly: the strings in the Text list above, with the five terminal lines and five card texts written out in the Scene.

## Process lane

Navigation: ⬅️ [Prompt 3 (Subject capstone): The limit for e, the deep-dive sheet](#prompt-3-subject-capstone-the-limit-for-e-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note has no plan tree to draw over it.
