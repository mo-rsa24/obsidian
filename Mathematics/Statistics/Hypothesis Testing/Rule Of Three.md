---
aliases: [rule of three, rule-of-three, 3/n rule, zero events and the rule of three, zero-event bound]
standard: vault-note v2
---

# Rule Of Three

Up: [[Hypothesis Testing]]

Mathematics, Statistics, Hypothesis Testing. It approximates the one-sided [[Confidence Interval]] bound that [[Selective Evaluation]] computes exactly in "The exact binomial upper bound".

**After zero events in n independent trials, the rule of three says the true event rate is below about 3/n with 95% confidence; it approximates the exact bound 1 − 0.05^(1/n), because ln(0.05) ≈ −3, and it overstates the bound a little when n is small (0.375 against 0.312 at n = 8).**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the rule of three writes the rest around it.

## Where to learn this

**Rule of three**, the 95% upper bound 3/n on a rate after zero events in n trials. Also: 3/n rule, zero-event bound.

**Textbooks**

- Pattern classification (Duda, Hart and Stork), section 9.6.2, Binomial confidence interval for a test error rate: [pages 562 to 563](../../references/textbooks/machine-learning/pattern-classification.pdf#page=562). Models k errors in n test samples as binomial and reads a 95% band off Figure 9.10: no errors on 50 samples still allows a true error rate up to 8%, and more than 250 error-free samples are needed to be sure it is below 2%. Its band is two-sided and read off a chart, so it sits above the one-sided 3/50 = 6%.

No other shelf book names the rule of three or works a zero-event bound; `find-examples.py` found only the Duda page.

**Videos**

- Natal Sphere, What is the rule of three in clinical trials?, 0:00 to 0:39: [watch](https://www.youtube.com/watch?v=juPW2dri3P4&t=0s). Zero adverse events in 100 patients bounds the risk below 3%, and in 1,000 below 0.3%; the exact 95% values are 0.0295 and 0.0030. It states the rule without deriving the 3. Whole video, caption-read by the sampling journey's pass.

**Our plans and chapters**

- [Zero events and the rule of three](/home/molef/goal-setting/learning/mathematics/statistics/sampling/textbook/03-zero-events-and-the-rule-of-three.md), mathematics/statistics/sampling, chapter 3. Starts from 0 false fails in 8 read as 0%, solves (1 − u)ⁿ = δ for the exact bound 0.312, takes logs to get 3/n = 0.375, then shows the gap shrinking below 0.003 by 45 checks and the rule failing when kept at 90%.
- [Bound a rate after zero events, and check it with 3/n](/home/molef/goal-setting/learning/mathematics/statistics/sampling/plans/04-zero-events-and-the-rule-of-three.md), mathematics/statistics/sampling, plan 4. The plan for that chapter, opening on the clinical-trial clip and deriving where its 3 comes from.
- [4.3 Escapes against false alarms](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/textbook/04-images-and-barcodes.md#43-escapes-against-false-alarms), ai-engineering/product-data-validation-end-to-end, chapter 04. Applies the rule to a photo checker with zero escapes, and prints 3/n beside 1 − 0.05^(1/n) for n = 15 (20.0% against 18.1%) and n = 45 (6.7% against 6.4%).
- [The exact one-sided upper bound](/home/molef/goal-setting/learning/ai-engineering/agent-evaluation/validating-an-llm-judge/plans/15-the-exact-one-sided-bound.md), ai-engineering/agent-evaluation/validating-an-llm-judge, plan 15. Derives 1 − δ^(1/n) for zero judge errors at n = 8, 20, 50 and 100, with the Duda page above as its textbook worked example.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27. The Duda pages were read in the PDF with pdftotext; the gather script's back-of-book search found no shelf entry for "rule of three", and its page-text hits were Cramer's rule and glossary rules, none about the idea. `find-examples.py --concept "zero errors"` and `--shape binomial-tail-probability` returned the Duda page as the only zero-event bound on the shelf. No lecture map or listed creator in `VIDEO_CREATORS.md` covers it; the one video is the clip the sampling journey already caption-read (it cites 0:04 to 0:29), cited here at its cached whole-video chapter. `find-figures.py` found no saved figure. Each plan and chapter was read at its heading and worked numbers. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a cached chapter.
