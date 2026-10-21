# The Exponent Rules: illustrated map

The drawn pictures for the vault note [[The Exponent Rules]]: the five rules' form, their mechanism, and the deep-dive sheet that composes them with the `exponents.py` run. `3 prompts · 0 rendered · 0 stuck · 0 rendering · 3 waiting`

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Glyph vocabulary](#glyph-vocabulary)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane](#subject-lane)
- [Prompt 1 (Subject): The five rules, the form](#prompt-1-subject-the-five-rules-the-form)
- [Prompt 2 (Subject): The five rules, the mechanism](#prompt-2-subject-the-five-rules-the-mechanism)
- [Prompt 3 (Subject capstone): The five rules, the deep-dive sheet](#prompt-3-subject-capstone-the-five-rules-the-deep-dive-sheet)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[The Exponent Rules]]: the five rules' form, mechanism and deep-dive sheet. A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: nothing here needs a repeatable named look. Zoom depth: one level, the three pictures a vault section gets. The style paragraph is embedded verbatim at the head of every prompt.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. Nothing in these pictures is a real-world object or a real product. The run pane of prompt 3 copies the text of `Mathematics/Algebra/assets/exponent-rules-checked-on-the-toy-gaussian.png`, the rendered output of the note's check, which may be attached for its layout.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Teal: a factor of e, drawn as a bead. Orange: a slip, a wrong answer from a misapplied rule. Grey is structural only (strings, fraction bars, dividers). No other colour carries a meaning.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A teal bead marked "e" is one factor of e (primary tier). A grey string holding beads is one power of e, its bead count the exponent (primary tier). A grey fraction bar with beads under it is a negative exponent (secondary tier). A rule card holds one rule's plain-words line, its symbol form and its toy number (artifact tier).

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Left to right: what goes in, the rule, what comes out. Rules are stacked top to bottom in the note's order: product of powers, power of a power, power of a product, zero exponent, negative exponent.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Numbered markers in prompt 3's run pane, matching the note's field table. No step badges or phase containers.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The five rules, the form](#prompt-1-subject-the-five-rules-the-form) ➡️

The three pictures for the five rules. Every number drawn comes from the note's own derivations or its `exponents.py` output.

### Prompt 1 (Subject): The five rules, the form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The five rules, the mechanism](#prompt-2-subject-the-five-rules-the-mechanism) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Algebra/assets/the-exponent-rules-the-form.webp`

Visual thesis: Five rules, each one line of plain words, one symbol form and one number from the toy Gaussian N(0, 0.25), so a reader can find the rule a line of maths used by its shape.

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

Production: Use a deterministic figure script for every card, bead and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A title across the top: "The exponent rules". Five rounded rule cards in one column, top to bottom, each split into three cells left to right: plain words, symbol form, toy number. A small row of teal beads marked "e" sits at the left edge of each card as its icon.
Card 1: "multiplying adds the counts" | "e^a e^b = e^(a+b)" | "e^-0.5 x e^-0.5 = 0.367879 = e^-1".
Card 2: "a power on a power multiplies them" | "(e^a)^b = e^(ab)" | "(e^-0.5)^2 = 0.367879 = e^-1".
Card 3: "a power on a product goes on every factor" | "(uv)^p = u^p v^p" | "(0.5 sqrt(2 pi))^2 = 0.25 x 2 pi = 1.570796".
Card 4: "a count of zero leaves 1" | "e^0 = 1" | "peak of N(0, 0.25) = 0.7979 x 1".
Card 5: "a negative count divides" | "e^-a = 1 / e^a" | "e^-0.5 = 1 / 1.648721 = 0.606531".
Under the column, one footer line: "height at x = 0.5: 0.7979 x e^-0.5 = 0.4839".

Cast: five rule cards, five small bead icons, one title, one footer line.

Flows: none.

Text in the image, spelled exactly: "The exponent rules", "multiplying adds the counts", "e^a e^b = e^(a+b)", "e^-0.5 x e^-0.5 = 0.367879 = e^-1", "a power on a power multiplies them", "(e^a)^b = e^(ab)", "(e^-0.5)^2 = 0.367879 = e^-1", "a power on a product goes on every factor", "(uv)^p = u^p v^p", "(0.5 sqrt(2 pi))^2 = 0.25 x 2 pi = 1.570796", "a count of zero leaves 1", "e^0 = 1", "peak of N(0, 0.25) = 0.7979 x 1", "a negative count divides", "e^-a = 1 / e^a", "e^-0.5 = 1 / 1.648721 = 0.606531", "height at x = 0.5: 0.7979 x e^-0.5 = 0.4839", "e"

Exclusions: no sixth card, no orange anywhere (no slip is shown in this picture), no bell curve, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Five cards in the note's order (product of powers, power of a power, power of a product, zero exponent, negative exponent), each with its plain-words cell, symbol cell and number cell exactly as listed; every number copied from the note's [[The Exponent Rules#The five rules and why each holds]] and lines 1 to 6 of the `exponents.py` run (0.367879, 0.6366 from 1/1.570796, 1.0, 0.606531, 0.7979, 0.4839). No orange. Every label in the image, exactly: the 18 strings in the Text list above.

### Prompt 2 (Subject): The five rules, the mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The five rules, the form](#prompt-1-subject-the-five-rules-the-form) | 📋 [TOC](#table-of-contents) | [Prompt 3 (Subject capstone): The five rules, the deep-dive sheet](#prompt-3-subject-capstone-the-five-rules-the-deep-dive-sheet) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Algebra/assets/the-exponent-rules-the-mechanism.webp`

Visual thesis: An exponent is a count of e beads on a string, so joining strings adds counts, copying a string multiplies them, an empty string is 1, and beads under a fraction bar are a negative count.

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

Production: Use a deterministic figure script for every bead, string, fraction bar and all typography. Compose for reading at 800 px wide, 3:2 landscape; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel. Every bead is the same size, so counts can be checked by eye.

Scene: A title across the top: "An exponent counts factors of e". Five rows, each read left to right as input, a short grey arrow, output.
Row 1, titled "product of powers": a string of 2 teal beads labelled "e^2" and a string of 3 teal beads labelled "e^3", a grey arrow, one string of exactly 5 beads labelled "e^5 = e^(2+3)".
Row 2, titled "power of a power": the 2-bead string "e^2" drawn 3 times side by side under the bracket "copied 3 times", a grey arrow, one string of exactly 6 beads labelled "e^6 = e^(2 x 3)".
Row 3, titled "power of a product": the pair "u v" drawn twice, "(uv)(uv)", a grey arrow, the regrouped "u u v v" labelled "u^2 v^2".
Row 4, titled "zero exponent": an empty grey string with no beads labelled "e^0", a grey arrow, the number "1" with the note "multiplying by it changes nothing".
Row 5, titled "negative exponent": a grey fraction bar with "1" above it and a string of 2 teal beads under it, labelled "e^-2 = 1 / (e x e)".

Cast: five rows of bead strings, four grey arrows, one fraction bar, one bracket.

Flows: the four grey arrows in rows 1 to 4 only.

Text in the image, spelled exactly: "An exponent counts factors of e", "product of powers", "e^2", "e^3", "e^5 = e^(2+3)", "power of a power", "copied 3 times", "e^6 = e^(2 x 3)", "power of a product", "(uv)(uv)", "u v", "u u v v", "u^2 v^2", "zero exponent", "e^0", "1", "multiplying by it changes nothing", "negative exponent", "e^-2 = 1 / (e x e)", "e"

Exclusions: no bead count other than the ones given (2 and 3 in, 5 out; 2 three times, 6 out; 0; 2 under the bar), no orange, no decimals, no bell curve. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Bead counts are checkable by eye and must be exact: row 1 has 2 and 3 beads in and 5 out; row 2 has three strings of 2 in and 6 out; row 4's string is empty; row 5 has 2 beads under the bar. These are the whole-number derivations in [[The Exponent Rules#The five rules and why each holds]] ($e^2 e^3 = e^5$, $(e^2)^3 = e^6$, $(uv)^2 = u^2 v^2$, $e^0 = 1$, $e^{-a} = 1/e^a$). No orange. Every label in the image, exactly: the 20 strings in the Text list above.

### Prompt 3 (Subject capstone): The five rules, the deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The five rules, the mechanism](#prompt-2-subject-the-five-rules-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[built] ⏳ not rendered
Save as: `../Mathematics/Algebra/assets/the-exponent-rules-deep-dive-sheet.webp`

Visual thesis: One sheet holds the five rules, why they hold as bead counts, the run that checks them on the toy Gaussian, and the two slips that land above 1.

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

Production: Use a deterministic figure script for every bead, card, terminal line and all typography. Compose as a portrait sheet for reading at 1000 px wide; every label must stay legible at that width, so add height rather than shrinking text. Label each thing directly on or beside it; no separate legend panel.

Scene: A sheet title across the top: "The exponent rules on N(0, 0.25)". Five rounded panes.
Pane 1, top left, titled "The rules": five short rule chips stacked: "e^a e^b = e^(a+b)", "(e^a)^b = e^(ab)", "(uv)^p = u^p v^p", "e^0 = 1", "e^-a = 1 / e^a".
Pane 2, top right, titled "Why: count the beads": two rows only. Row 1: a 2-bead teal string and a 3-bead teal string, a grey arrow, a 5-bead string "e^5". Row 2: an empty string "e^0" equal to "1".
Pane 3, middle, full width, titled "The run": a light terminal card in monospace showing exactly these ten lines:
"$ python3 exponents.py"
"product of powers: e^a * e^b = 0.367879, e^(a+b) = 0.367879"
"power of a power: (e^-0.5)^2 = 0.367879, e^(-0.5*2) = 0.367879"
"power of a product: (1/(0.5*sqrt(2pi)))^2 = 0.6366, 1/(2*pi*0.25) = 0.6366"
"negative power: e^-0.5 = 0.606531, 1/e^0.5 = 0.606531"
"zero power: e^0 = 1.0, so the peak of N(0, 0.25) is the front factor 0.7979"
"the toy: 0.7979 * e^-0.5 = 0.4839"
"repeated multiplication: 0.999^692.8 = 0.5000"
"slip, sum taken as a product: e^a + e^b = 1.213061, not e^(a+b) = 0.367879"
"slip, power of a power added: e^(-0.5+2) = 4.481689, not (e^-0.5)^2 = 0.367879"
with nine small numbered teal markers 1 to 7 and orange markers 8 and 9, each placed just above: 1 over "e^(a+b) = 0.367879", 2 over "e^(-0.5*2) = 0.367879", 3 over "1/(2*pi*0.25) = 0.6366", 4 over "1/e^0.5 = 0.606531", 5 over "e^0 = 1.0", 6 over "0.4839", 7 over "0.5000", 8 over "1.213061", 9 over "4.481689".
Pane 4, below the run, titled "Reading the run": nine small cards in a grid, numbered 1 to 9 to match the markers, each with exactly this text:
1 "adding exponents gives the product"
2 "multiplying exponents gives the square"
3 "2D front factor 1 / (2 pi sigma^2)"
4 "negative means one over"
5 "peak = front factor"
6 "height one sd out"
7 "half-life: 692.8 steps"
8 "sum slip: 3.30 times too big"
9 "power slip: above 1"
Pane 5, bottom, full width, titled "The slips land above 1": a horizontal number line from 0 to 5 with a grey tick at 1 labelled "1". A teal dot at 0.367879 labelled "right: 0.367879". An orange dot at 1.213061 labelled "sum slip: 1.213061". An orange dot at 4.481689 labelled "power slip: 4.481689".

Cast: five rule chips, two bead rows, one terminal card with nine markers, nine reading cards, one number line with three dots.

Flows: the single grey arrow in pane 2's first row only.

Text in the image, spelled exactly: "The exponent rules on N(0, 0.25)", "The rules", the five rule chips above, "Why: count the beads", "e^5", "e^0", "1", "e", "The run", the ten terminal lines above, the markers "1" to "9", "Reading the run", the nine card texts above, "The slips land above 1", "0", "5", "right: 0.367879", "sum slip: 1.213061", "power slip: 4.481689"

Exclusions: no terminal line other than the ten given, no marker over the wrong field, no card longer than its given text, no sixth pane, no orange on anything but markers 8 and 9 and the two slip dots, no numbers other than those listed. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: Five panes, the deep-dive exception's maximum. The ten terminal lines are copied character for character from the note's check (step 6) and its rendered picture `assets/exponent-rules-checked-on-the-toy-gaussian.png`; markers 1 to 9 sit over the same fields as that picture's markers and match the note's "Reading the output" table rows 1 to 9. Pane 2's bead counts are exact: 2 and 3 in, 5 out; the zero string is empty. Pane 5's dots sit at 0.367879, 1.213061 and 4.481689 on a 0 to 5 scale, the two orange ones right of the tick at 1. The ratio 3.30 is $1.213061 / 0.367879$. Every label in the image, exactly: the strings in the Text list above, with the five chips, ten terminal lines and nine card texts written out in the Scene.

## Process lane

Navigation: ⬅️ [Prompt 3 (Subject capstone): The five rules, the deep-dive sheet](#prompt-3-subject-capstone-the-five-rules-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
