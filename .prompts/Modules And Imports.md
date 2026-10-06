# Modules And Imports: illustrated map

The drawn pictures for the vault note [[Modules And Imports]], section [[Modules And Imports#Names defined under __main__]]. `3 prompts · 3 rendered · 0 waiting`

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
- [Process lane](#process-lane)

## Abstraction chain

Navigation: ⬅️ [Table of contents](#table-of-contents) | 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [[Modules And Imports]]: subject "Names under __main__, one sheet". A vault note has no scope above it, so the chain is one link.

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

Empty, the default: no subject here needs a repeatable named look across the set. Zoom depth: one level, the section's form and mechanism, composed by the deep-dive sheet. The style paragraph is embedded verbatim at the head of every prompt.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

None. Nothing in these pictures is a real-world object or a real product.

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Glyph vocabulary](#glyph-vocabulary) ➡️

Teal: code at module level, seen by every importer. Amber: code under the main guard, run only directly. Green check and red cross: the guard passing or failing. Red: an error, and numbered output markers.

## Glyph vocabulary

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

A rounded file card is a .py file. A horizontal divider is the if __name__ line. A terminal icon is a direct run. A red badge is an error. All primary tier.

## Reading axes

Navigation: ⬅️ [Glyph vocabulary](#glyph-vocabulary) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Left to right: who runs the file, then what of it runs. Top to bottom inside a file: the order Python executes it.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Numbered markers only on the deep-dive sheet's output pane, matching the numbered fields in the note's output picture. No step badges or phase containers.

## Subject lane
<!-- student-read: 2026-10-04 job 20261004-193336-cc4c90 -->

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Prompt 1 (Subject): The form](#prompt-1-subject-the-form) ➡️

The form, the mechanism, then the deep-dive sheet that composes them with the run's output, per the vault-note exception in the illustration style guide.

### Prompt 1 (Subject): The form

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism) ➡️

[planned] 🖼️ rendered 2026-10-04 modules-the-form.webp
Save as: `../Software/Python/assets/modules-the-form.webp`

Visual thesis: The if __name__ == "__main__" line splits a file into what every importer sees and what only a direct run sees.

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

Scene: One tall rounded card drawn as a Python file named toy.py. A horizontal divider across it at the line if __name__ == "__main__":. Above the divider, a teal band holding three short lines of assignments. Below it, an amber band holding two print lines. On the left, an icon of a terminal with the command python toy.py, with arrows reaching both bands. On the right, a second small file card use.py with from toy import shared, with an arrow reaching only the teal band.

Cast: the toy.py card, the divider, the teal band (module level), the amber band (run-only), the terminal, the use.py card.

Flows: from the terminal, two solid arrows into both bands; from use.py, one solid arrow into the teal band and a short arrow stopping with a small barrier at the divider.

Text in the image, spelled exactly: "toy.py", "use.py", "python toy.py", "from toy import shared", "if __name__ == \"__main__\":", "every importer sees", "direct run only".

Exclusions: no Python logo, no third file. no duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: The importer's arrow reaches only the band above the divider; the terminal's arrows reach both; teal means module level, amber means run-only; labels exactly as listed.

### Prompt 2 (Subject): The mechanism

Navigation: ⬅️ [Prompt 1 (Subject): The form](#prompt-1-subject-the-form) | 📋 [TOC](#table-of-contents) | [Subject capstone: The deep-dive sheet](#subject-capstone-the-deep-dive-sheet) ➡️

[planned] 🖼️ rendered 2026-10-04 modules-the-mechanism.webp
Save as: `../Software/Python/assets/modules-the-mechanism.webp`

Visual thesis: In this version, shared is assigned only inside the main guard. Importing skips that assignment, so the subsequent request for shared fails.

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

Scene: Two aligned columns showing the same file run two ways. Across the top, one prominent sentence: "Here, shared is assigned only inside the guard." Beneath it, a smaller bridge from the opening picture: "The opening picture puts shared above the guard. This version puts it inside."

Left column title: "run directly", with a small terminal icon and "python toy.py". Right column title: "imported", with a small file icon and "from toy import shared". Neither column title carries a success or failure symbol.

Each column contains a toy.py file card. First show its name tag: __name__ = "__main__" on the left and __name__ = "toy" on the right. Beneath each tag show the identical line if __name__ == "__main__":. Put the green check only beside the left guard and the red cross only beside the right guard. Label these "True" and "False" so the symbols clearly describe the condition.

Under each guard, show the same indented code: shared = [(mu_b, var_b), (mu_1, var_1), (mu_2, var_2)] followed by print(f"shared: {shared}"). Break the assignment across lines inside its brackets if needed for legibility, without changing its contents. Add one small shared note above the file cards: "The mu and var names are already defined above."

The left block is amber and labelled "block runs". The right block has a grey fill, retains a thin amber border identifying it as guarded code, and is labelled "block skipped". Keep the skipped code dark enough to read. Give the word shared in both assignments the strongest typographic emphasis within the code.

End the left file card with "shared is created". End the right file card with "shared is not created". Outside and below the right file card, show a short labelled arrow, "importer requests shared", leading to a red error badge containing ImportError and cannot import name 'shared'. This separates successful loading of the module from the failed request for its missing name.

Flows: downward through the name tag and guard in each file. On the left, continue through the assignment to "shared is created". On the right, route around the skipped block to "shared is not created", then continue outside the file to the importer's request and error. Do not draw an arrow from the false condition straight to the error.

Text in the image: use exactly the commands, code, labels and explanatory sentences specified above. Preserve every underscore and quote in the code. Do not add numerical output, which is not needed to explain the missing assignment.

Hierarchy and size: compose for reading at 800 px wide. The assignment to shared and the contrasting created/not-created outcomes are the focal points. Keep file icons small. Use neutral column backgrounds so red means the failed condition or error, rather than the act of importing. Use a compact semantic legend only: amber "guarded code", grey "skipped", green check "True", red cross "False". Do not add legend entries for ordinary text or background colours.

Exclusions: no Python logo, no other modules, no large red cross beside the imported title, no unexplained numerical output, no decorative output panel, no numbered step badges, no orphan arrows, no crossing arrows, no illegible code, no watermark.
```

Faithfulness note: The left column runs the guarded block and the right skips it; the right column's error names shared, matching the note's run; green check left, red cross right; amber is the guarded block, grey means skipped. Every label in the image: "Here, shared is assigned only inside the guard.", "The opening picture puts shared above the guard. This version puts it inside.", "run directly", "python toy.py", "imported", "from toy import shared", "The mu and var names are already defined above.", "True", "False", "block runs", "block skipped", "shared is created", "shared is not created", "importer requests shared", "ImportError", "cannot import name 'shared'", "guarded code", "skipped".

### Subject capstone: The deep-dive sheet

Navigation: ⬅️ [Prompt 2 (Subject): The mechanism](#prompt-2-subject-the-mechanism) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[planned] 🖼️ rendered 2026-10-04 modules-deep-dive-sheet.webp
Save as: `../Software/Python/assets/modules-deep-dive-sheet.webp`

Visual thesis: The error names the requested binding and the module searched. Here, shared is missing because its only assignment is inside the skipped guard; putting that assignment at module level makes it available to an importer.

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

Scene: Exactly four panes in a tall sheet, each using the full width. Preserve the titles and their order: "The form", "The mechanism", "The run", "Reading it". Compose for reading at 800 px wide; use additional height instead of shrinking text. The run and its field explanations are the main visual focus. The first two panes are compact reminders, not miniature reproductions of entire posters.

Pane 1, "The form": preserve prompt 1's toy.py card, teal module-level band, amber guarded block, and guard divider. Keep the assignments shared = "Hello", count = 2, ready = True above the guard, and print(shared), print(count) inside it. Retain the terminal command python toy.py and the use.py command from toy import shared. The terminal's arrows reach both bands; the importer's arrow reaches only the teal band. Keep the labels "every importer sees" and "direct run only". Add one short caption: "Here, shared is above the guard and can be imported." Use small labelled file and terminal icons rather than large surrounding cards.

Pane 2, "The mechanism": preserve the revised prompt 2's two aligned execution paths and its contrasting name tags, __name__ = "__main__" and __name__ = "toy". Introduce them with "In the failing version, shared is assigned only inside the guard." Both paths show the identical guard and guarded assignment from prompt 2. Keep its note that the mu and var names are already defined above. Use a green check labelled "True" beside the left guard and a red cross labelled "False" beside the right guard. Show "block runs" and "shared is created" on the left; show "block skipped" and "shared is not created" on the right. Amber identifies the guarded block; grey means skipped. The missing-name outcome leads to the importer's request, not directly from the false condition. Do not repeat the full error here; pane 3 supplies it.

Pane 3, "The run": give this pane ample vertical space and readable monospace type. Reproduce these two logical lines character for character:
$ uv run --no-project --with numpy python -c "from toy import shared, split"
ImportError: cannot import name 'shared' from 'toy' (/home/molef/playground/sandbox/numpy-arrays/toy.py)

Wrap the display at natural spaces as needed, with hanging indentation, while preserving all characters and their order. Do not insert continuation symbols, abbreviate the path, or reduce the type to force either logical line onto one visual line. Keep command and error visibly separated. Put red numbered markers directly above these fields: 1 over ImportError, 2 over 'shared', 3 over 'toy'. Lightly outline only those fields. The path remains readable secondary text.

Pane 4, "Reading it": stack three explanation rows in numerical order, 1 then 2 then 3. Repeat the corresponding field verbatim at the start of each row so each explanation can be matched without a long leader line:
"1 ImportError: module loaded, name missing"
"2 'shared': first missing name"
"3 'toy': the module searched"
Below the rows, add: "This error reports shared. It does not tell you whether split is available."
Close the same pane with: "To make shared available on import, move its assignment above the guard. Keep direct-run printing inside."

Flows: retain only the execution arrows needed inside panes 1 and 2. Match output fields to explanations through their repeated numbers and names. Do not route leaders around pane boundaries.

Legend: one small strip inside the fourth pane, not a fifth pane: teal "module level", amber "run-only", grey "skipped", red "error". Green checks and red crosses are labelled True and False beside their guards.

Text in the image: use only the pane titles, code, commands, output, labels and captions specified above or explicitly retained from the revised prompts. The captured output is exact; the explanations are separate text and must not look like terminal output.

Exclusions: no fifth pane, no reversed marker order, no looping connector lines, no miniature legends inside the first two panes, no large decorative icons, no unexplained numerical output, no tiny monospace text, no ellipses replacing the captured path, no watermark.
```

Faithfulness note: Output lines match the note's captured run character for character; three markers over ImportError, 'shared' and 'toy' as in the rendered output picture; panes 1 and 2 match prompts 1 and 2; four panes only. Pane 4's rows read exactly "1 ImportError: module loaded, name missing", "2 'shared': first missing name", "3 'toy': the module searched", then "This error reports shared. It does not tell you whether split is available." and "To make shared available on import, move its assignment above the guard. Keep direct-run printing inside."

## Process lane

Navigation: ⬅️ [Subject capstone: The deep-dive sheet](#subject-capstone-the-deep-dive-sheet) | 📋 [TOC](#table-of-contents)

None. A vault note's section has no plan tree to draw over it.
