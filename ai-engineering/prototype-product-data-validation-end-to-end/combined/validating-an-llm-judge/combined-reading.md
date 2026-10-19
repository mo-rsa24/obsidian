# Combined reading: validating an LLM judge against human labels

A combined reading of one idea across four sources, read on 2026-10-16 to 2026-10-19 for route r1
of the v3 product-content judge (Dis-Chem product data repo). It chose how that judge is
validated against people with 8 approved gold pages plus 97 planted defects. The method chosen is
[[Selective Evaluation]] (Jung, Brahman and Choi 2407.18370), reported with chance-corrected
agreement and bootstrap ranges per Rao and Callison-Burch 2606.00093.

The plain readings and comparisons are the reading's own interpretation of the quoted text.
Every number from the checks comes from invented judge outcomes.

## Sources

PDF page numbers, not the printed page numbers.

| Source | Pages | What the pages do | Kept |
|---|---|---|---|
| Thakur et al., Judging the Judges (2406.12624), `sources/judging-the-judges/paper/` | p4 §3 Alignment; p5 §4.1; p7 §5.4; p14 App F | defines percent agreement and Scott's π; experiment comparing them; leniency experiment; metric formulas | kept (reader: keep all) |
| Rao and Callison-Burch, Agreement Metrics (2606.00093), `sources/agreement-metrics-for-llm-judges/paper/` | p2 to 3 §3; p5 to 6 §4.2 to 4.3; p7 to 9 §5 | the 2×2 table as the object; κ against φ and the marginals; sampling variance; abstention and coverage bounds | kept (reader: keep all) |
| Jung, Brahman and Choi, Trust or Escalate (2407.18370), `sources/trust-or-escalate/paper/` | p2 to 3 §2 and 2.1; p7 §3.3; p14 App A | selective evaluation and the agreement guarantee; what gets abstained on; the proof | kept (reader: keep all) |
| Your textbook, chapter 10.3, Two labellers and how far they agree (`textbook/10-measurement.md`), with plan 45 | §10.3 | observed agreement, expected agreement, Cohen's κ, the bands | home source, always shown last |

## Idea spine

| # | Idea | In which sources | State |
|---|---|---|---|
| 1 | raw agreement against chance-corrected agreement | Thakur p5 · Rao p6 · Jung p3 · textbook §10.3 | tested (test Jung, 2026-10-18: holds with a condition, see Differences row 2) |
| 2 | which corrected number, and the pass rates beside it | Thakur p14 · Rao p5 to 6 · textbook §10.3 | tested (test 2) |
| 3 | which way the judge errs: the full 2×2 and leniency | Thakur p7 · Rao p3 · textbook §10.3 | tested (test 3, `checks/test-3-and-gold-design.py`) |
| 4 | review as abstention: what a number covers when the judge will not call | Rao p7 to 8 · Jung p2 to 3 | tested (test 4, `checks/test-4-review-as-abstention.py`) |
| 5 | choosing the threshold so that passes agree with people | Jung p3 · Rao p8 to 9 | tested (test 5, `checks/test-5-threshold-walk.py`) |
| 6 | how sure a number is from few labels | Rao p7 · Jung p3 · Thakur p18 | compared |

## Idea 6: how sure a number is from few labels

**Rao and Callison-Burch, p7**
> "Rank judges only with an uncertainty estimate attached; at N = 300 binary decisions the
> delta-method standard error of κ̂ falls between 0.04 and 0.06 for most tables, so gaps of a few
> points are within sampling noise. Resample whole items rather than individual verdicts, and
> avoid variance formulas built for continuous values."

In plain words: a kappa from a sample would come out different on another sample, so report how
far it could move, by redrawing whole products with replacement.

**Jung, Brahman and Choi, p3**
> "Since the empirical risk is a binomial random variable with n(λ) trials, we can compute the
> exact (1 − δ) upper confidence bound of the risk as: R̂⁺(λ) = sup{ R : P(Bin(n(λ), R) ≤
> ⌈n(λ) R̂(λ)⌉) ≥ δ }."

In plain words: on the items the judge answered, the bound is the highest disagreement rate that
could still plausibly produce as few disagreements as were seen. It is one-sided because only the
worst case matters.

**Thakur et al., p18**
> "we further take 5 samples of 300 randomly selected questions from the evaluation set and
> calculate the mean and standard deviation of Scott's Pi … Standard deviation of all the judge
> models from the mean Scott's π is also minimal, barring EM lexical match."

In plain words: five 300-question subsets of the same 400 questions barely moved Scott's π.

**The measurement textbook, chapter 10.4**
> "Consider a hypothetical audit with 0 errors in 45 independent representative known-truth
> auto-passes … gives the one-sided 95% Clopper–Pearson upper bound, about 6.4%"

In plain words: zero wrong passes seen bounds the risk below a ceiling that drops only as more
passes are checked.

**How they compare**
1. Same: all four say one agreement number from a sample needs a statement of how far it could move.
2. Differs (different method): Rao gives a two-sided interval on κ over all items; Jung and the
   textbook give a one-sided ceiling on the error rate among passes only.
3. Differs (different assumption): Thakur's subsets share at least 200 of 300 items, so the
   spread looks smaller than a fresh sample would give.
4. Adds: Jung's ceiling has the shape of v3's costly error, a wrong pass; the textbook works the
   zero-errors case.
5. Skips: none speaks to 8 gold pages; the smallest case in Rao and Thakur is 300.

## Symbols

| Object | Thakur | Rao | Jung | Textbook |
|---|---|---|---|---|
| how often the judge applies the rubric, and which way it guesses otherwise | P_c, P+ (leniency) | | | |
| matches as a share of all items | percent agreement | p_o, accuracy | P(f_LM(x) = y_human) | p_o, observed agreement |
| chance-corrected agreement | Scott's π | Cohen's κ | not used | Cohen's κ |
| agreement expected from the rates alone | (inside π) | p_e | not used | p_e |
| the rate at which each rater says yes | | π (human MET rate), π̂ (judge MET rate) | | a_j, b_j (marginal proportions) |

## Differences

| Idea | Kind | Source A says | Source B says | Resolved |
|---|---|---|---|---|
| 1 | different symbol | Thakur p5: corrects with Scott's π | Rao p6, textbook §10.3: correct with Cohen's κ | open (idea 2) |
| 1 | different scope | Jung p3: guarantees raw agreement on the items the judge does not abstain on, no chance correction | Thakur p5, Rao p6: raw agreement alone misleads | resolved by `test Jung` (`checks/test-jung.py`): not a conflict, they answer different questions. On 20 products κ 0.318 and Scott's π 0.314, while matching on passed items is 0.889; the 11.1% wrong-pass share is Jung's complement, and the judge still let 2 of 3 bad products through |
| 1 | different symbol | Rao: π is the human pass rate | Thakur: π is Scott's chance-corrected agreement | resolved by example: on the same 20 products Rao's π is 0.85 and Scott's π is 0.314 |

| 3 | different scope | Thakur p8: estimates a judge's lean P+ from its behaviour | Rao p3: κ, accuracy and φ cannot see the lean, since they are unchanged when false passes and false fails are exchanged | resolved by `test 3`: P_c and P+ separate judges A, C and D that the summary numbers could not, but 20 products are too few to trust P+ for A |
| 4 | different assumption | Rao p7: abstention is a case to handle when scoring (exclude, recode as not-met, or keep three classes) | Jung p2: abstention is the lever, and a threshold λ trades coverage for agreement | resolved by `test 4` (invented outcomes on the 105-row design): the same decisions give accuracy 0.963 (exclusion, coverage 0.762), 0.962 (recoding) and 0.733 (three-class), so the rule changes the number; full-set accuracy is only known to [0.733, 0.971] |

| 5 | different scope | Rao p8: reports the trade after the fact and bounds what is unknown | Jung p3: picks the threshold in advance so a promise holds | resolved by `test 5` (invented outcomes): a calibrated judge on 105 rows certifies no threshold at α 0.10; the observed-risk rule picks λ 0.76 whose bound is 0.158; an underconfident judge stops at λ 0.86 covering 45 of 105 at α 0.07 |
| 6 | different method | Rao p7: an interval from resampling whole items with replacement (percentile bootstrap, 10^4 replicates), or the delta-method standard error of κ | Jung p3: an exact binomial upper bound on the error rate among the items the judge passed, at level 1 − δ | open |
| 6 | different assumption | Thakur p18: 5 subsets of 300 drawn from the same 400 questions, std dev of Scott's π under 0.013 for every judge but EM | Rao p7: resample with replacement from the full set; subsets sharing most of their items understate the spread | open (inferred: Thakur's subsets share at least 200 of 300 items) |

## Where this went

- The route's return: `~/xbigly/trial/digital_product_data_enrichment_validation/artifacts/ideas/v3-prototype-prompt/routes/r1-return.md`
- Notes: [[Chance-Corrected Agreement]], [[How Sure Kappa Is]], [[Abstention In Agreement Scores]], [[Selective Evaluation]], [[Bootstrap]]
- The walk's map: `~/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/drips/combine-validating-an-llm-judge/COMBINE_MAP.md`
