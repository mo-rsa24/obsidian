---
aliases: [paired difference, paired comparison, paired differences, difference per prompt and seed, ours minus PoE]
standard: vault-note v2
---

# Paired Difference

Up: [[Statistics]]

Mathematics, Statistics. Needs: [[Bootstrap]] for the interval and [[Confidence Interval]] for how to read it. Used by [[Comparing Methods Fairly]].

**A paired difference is the gap between two measurements taken on the same item, found by subtracting item by item and then averaging the gaps.**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the journey's chapters need. The Textbooks and Videos groups of the card are not built; waiting: `/concept-link build a card for Paired Difference`.
> - No claim is marked stated.

## What the chapters need

**The calculation.** The two methods are scored on the same prompt and seed with the starting noise shared, so each item gives two numbers. Subtract ours minus plain PoE per prompt and seed, average over seeds for each prompt, then over prompts for the set, and put a 95% interval on it by resampling prompts and then seeds, 10,000 times *(cited: journey chapter 5)*.

**Toy.** On the animals set the two means are 0.5031 for ours and 0.2251 for plain PoE on BLIP-VQA, and 0.5031 minus 0.2251 is 0.2780, which is the file's paired mean *(cited: chapter 5, the review session's result as it stood on 2026-11-12, which may change)*.

**Why pair.** Each gap is taken on one prompt and seed, so what varies inside a gap is the method. A verdict is a paired difference with an interval, written to its own file, and it supports the claim when the interval sits above zero in all three sets; that rule was fixed before any evaluation score.

**What is unknown here.** Why the pairing makes the interval narrower than unpaired is not shown in the files read.

## Where to learn this

**Paired Difference**, the gap between two measurements on the same items. Also: paired comparison, paired differences, difference per prompt and seed, ours minus PoE.

**Our plans and chapters**

- [Journey chapter 5, from a score to a table cell](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/05-the-four-side-by-side.md#from-a-score-to-a-table-cell): the cell, the verdict and the hand check.
- [Journey textbook index, Words this uses](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/00-INDEX.md#words-this-uses): the verdict as a paired difference.
