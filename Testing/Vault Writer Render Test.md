# Vault Writer Render Test

A throwaway note. It holds each piece of markup once, so you can see by eye which ones Obsidian renders. Open it in reading view, tick what works, and tell the walk which numbers failed. Delete it afterwards, together with `assets/lsof-output.png`.

## Contents

- [[#1 Callouts]]
- [[#2 Pictures]]
- [[#3 Links to a section]]
- [[#4 Links to one line]]
- [[#5 Display maths]]
- [[#6 A closed box]]
- [[#7 A section shown inside another]]
- [[#The target section]]

## 1 Callouts

↑ [[#Contents]]

You should see three coloured boxes, each with an icon and a title.

> [!TIP]
> **1a.** A tip, written the way the textbooks write it.

> [!CAUTION]
> **1b.** A caution. Expect the warning colour, orange.

> [!question] Test yourself: the quiz link goes here
> **1c.** The line planned for the top of every reference note.

- [ ] 1a renders as a box
- [ ] 1b renders as a box
- [ ] 1c renders as a box, with the custom title

## 2 Pictures

↑ [[#Contents]]

The same picture four ways. Each should show a small terminal picture about 300 pixels wide.

**2a. Markdown form, with a width**

![lsof output with nine numbered markers|300](assets/lsof-output.png)

**2b. Obsidian embed form, with a width**

![[lsof-output.png|300]]

**2c. HTML image tag, the way the textbooks write it**

<img src="assets/lsof-output.png" width="300" alt="lsof output with nine numbered markers">

**2d. HTML image tag wrapped in a link to itself**

<a href="assets/lsof-output.png"><img src="assets/lsof-output.png" width="300" alt="lsof output with nine numbered markers"></a>

- [ ] 2a shows the picture
- [ ] 2b shows the picture
- [ ] 2c shows the picture
- [ ] 2d shows the picture, and clicking it opens it full size

## 3 Links to a section

↑ [[#Contents]]

Each link should jump to the heading "The target section" at the bottom.

- **3a.** Obsidian form: [[#The target section]]
- **3b.** Obsidian form with its own text: [[#The target section|jump to the target]]
- **3c.** Markdown form with spaces encoded: [jump to the target](#The%20target%20section)
- **3d.** Markdown form with a kebab-case slug, the way the journeys write it: [jump to the target](#the-target-section)

- [ ] 3a jumps
- [ ] 3b jumps
- [ ] 3c jumps
- [ ] 3d jumps

## 4 Links to one line

↑ [[#Contents]]

The map line links down to the definition, and the colon in the definition links back up to the map line. The ids are made from the term's own words.

- [[#^def-stream|Stream]] ^nav-stream
- [[#^def-batch|Batch]] ^nav-batch

**Stream[[#^nav-stream|:]]** read a file one row at a time, never holding the whole of it. ^def-stream

**Batch[[#^nav-batch|:]]** a fixed number of rows held in memory together, then written out. ^def-batch

- [ ] 4a clicking "Stream" in the map lands on its definition
- [ ] 4b clicking the colon after "Stream" lands back on the map line
- [ ] 4c the ids `^def-stream` and `^nav-stream` do not show in reading view

## 5 Display maths

↑ [[#Contents]]

You should see two typeset lines, the second aligned under the first.

$$
\begin{aligned}
M_{\mathrm{stream}} &= O(S + bw) \\
&= O(S + 1000w)
\end{aligned}
$$

- [ ] 5 renders as typeset maths

## 6 A closed box

↑ [[#Contents]]

You should see one line you can click to open. Inside it, the word "bold" should be bold and the command should be in code face.

<details>
<summary>6a. How this was checked</summary>

Ran on the PC. The word **bold** is bold, and `lsof -i :8000` is code.

</details>

> [!note]- 6b. How this was checked, as a folded callout
> Ran on the PC. The word **bold** is bold, and `lsof -i :8000` is code.

- [ ] 6a opens and closes
- [ ] 6a shows bold and code face inside
- [ ] 6b opens and closes, with bold and code face inside

## 7 A section shown inside another

↑ [[#Contents]]

The box below should show the whole of "The target section", pulled in from the bottom of this note. This is how a reference note would show a worked example that is written once, in the lesson.

![[Vault Writer Render Test#The target section]]

- [ ] 7 shows the target section's text inside a box

## The target section

↑ [[#Contents]]

You arrived. This paragraph is the text that section 7 pulls in.
