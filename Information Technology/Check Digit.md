---
aliases: [check digit, check digits, check-digit, GS1 check digit, EAN-13 check digit, ISBN check digit, barcode check digit, check digit check]
standard: vault-note v2
---

# Check Digit

Up: [[Information Technology]]

Information Technology. Placement unsure: the two best places are a future error-detection note under [[Networking]], beside the checksum and CRC, or a modular-arithmetic note under [[Mathematics]]. The ISBN version is a [[Dot Product]] taken mod 11.

**A check digit is one extra digit computed from the others in an identifier, so that a mistyped or misread digit makes the computed and printed values disagree: GS1 barcodes weight the body digits 3 and 1 from the right and take what brings the sum up to a multiple of 10, and the old ten-digit ISBN weights its nine digits 1 to 9 and takes the remainder mod 11.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches check digits writes the rest around it.

## Where to learn this

**Check digit**, the last digit of a code computed from the others as a weighted sum mod 10 or mod 11. Also: GS1 check digit, EAN-13 check digit, ISBN check digit, check digit check.

**Textbooks**

- Linear algebra textbook, section 3.2, Application of dot products to ISBN numbers: [page 165](../Mathematics/references/textbooks/linear-algebra/linear-algebra-textbook.pdf#page=165). Works ISBN 0-471-15307-9: the dot product of (1, 2, …, 9) with the first nine digits is 152, and 152 mod 11 is 9, the check digit (a remainder of 10 is written X).
- Systems analysis and design, chapter 9, Input validation, Figure 9-15: [page 372](../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=372). Lists the check digit check as one of six validation checks: the system recomputes the digit from the others with a formula (a Social Security Number's ninth digit) and flags an error when it differs.
- Computer networking: a top-down approach, section 3.3.2, UDP checksum: [page 235](../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=235). Same shape: adds three 16-bit words with wraparound and flips the bits to get the checksum, and the receiver's sum of all four words must be all ones, as a scanner's recomputed check digit must match the printed one.
- Computer networking: a top-down approach, section 6.2.1, Parity checks: [pages 476 to 477](../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=476). Same shape at its smallest: one bit chosen so the count of 1s is even, which is a check digit taken mod 2, and why it misses an even number of flipped bits.
- Computer networking: a top-down approach, section 6.2.3, Cyclic redundancy check: [pages 479 to 480](../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=479). Same shape with polynomial division: D = 101110 and G = 1001 give the remainder R = 011, appended so the receiver's division leaves no remainder, as a check digit makes the weighted sum divisible by 10 or 11.
- GED handbook, Divisibility rules: [page 3](../Mathematics/references/textbooks/general/ged-handbook.pdf#page=3). The divisibility test for 11 is an alternating digit sum (9,482 gives 9 − 4 + 8 − 2 = 11), the same weighted-sum-mod-11 arithmetic the ISBN check uses with weights ±1.

**Videos**

- Dr. K Math, 12-Digit Barcode Check Digit Calculation Example and Explanation, 0:00 to 8:58: [watch](https://www.youtube.com/watch?v=iTovfYCooBI&t=0s). One worked 12-digit UPC barcode, the 3-and-1 weighted, mod-10 method GS1 uses; the video plan 31 asks the learner to watch before working its bad case. Whole video; captions not readable.
- Mr Bulmer's Learning Zone, Using check digits: modulo 11 and ISBN-13, Calculating ISBN 13, 0:41 to 2:15: [watch](https://www.youtube.com/watch?v=_fNpisi0eTA&t=41s). An ISBN-13 is an EAN-13 barcode, so this chapter computes the same 1-and-3 weighted, mod-10 digit as a GS1 code. Chapter-timed; captions not readable.
- Mr Bulmer's Learning Zone, Using check digits: modulo 11 and ISBN-13, Modulo 11 calculation, 3:17 to 5:23: [watch](https://www.youtube.com/watch?v=_fNpisi0eTA&t=197s). The mod-11 method the old ISBN-10 uses. Chapter-timed; captions not readable.

**Our plans and chapters**

- [4.8 The GS1 check digit](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/textbook/04-images-and-barcodes.md#48-the-gs1-check-digit), ai-engineering/product-data-validation-end-to-end, chapter 04. Works a tea packet's 4012346278001 by hand: twelve body digits weighted 3, 1 from the right sum to 69, the next multiple of ten is 70, so the check digit is 1; then the same in code.
- [The GS1 check digit, by hand then in code](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/plans/31-gs1-check-digit.md), ai-engineering/product-data-validation-end-to-end, plan 31. Starts from a bad file name, `6009876543210_1.jpg`, whose computed check digit is 9 but whose last digit is 0; the learner finds why on paper, writes four lines of code and runs them over all 26 articles.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27. Each textbook page was read in the PDF with pdftotext. The ISBN and check-digit pages came from the books' back-of-book indexes; the checksum, parity, CRC and divisibility pages came from `find-examples.py --like "check digit"`, which matched them by their shared weighted-sum-mod-n shape. No lecture map or listed creator in `VIDEO_CREATORS.md` covers check digits, so an open YouTube search found the Mr Bulmer chapters and plan 31 supplied the Dr. K Math video, both read with `cache-video-chapters.py`; neither video has captions the transcript tool could read, so their lines say only what the chapter titles state. `find-figures.py` found no saved figure. The word "checksum" is not an alias: a checksum is its own idea, taught on the networking pages above. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a cached chapter.
