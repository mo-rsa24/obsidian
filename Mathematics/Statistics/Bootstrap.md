---
aliases: [bootstrap, bootstrapping, resampling, resample, bootstrap resampling, bootstrap standard error, bootstrapped variance, standard error, percentile interval, bootstrap confidence interval, confidence interval from percentiles, standard error of the mean, non-parametric bootstrap, parametric bootstrap]
sources:
  - Introduction to Probability for Data Science (Chan), section 9.2 Bootstrapping, PDF pages 575 to 582, and section 9.1 for the standard error of a mean, PDF page 568
  - Rao and Callison-Burch, agreement metrics for LLM judges, section 4.3, https://arxiv.org/abs/2606.00093
---

# Bootstrap

Up: [[Statistics]]

Mathematics, Statistics. Needs: the mean of a list of numbers, and the idea of a standard deviation. The kappa examples use [[Chance-Corrected Agreement]].

> [!warning] Unfinished
> - The three drawn pictures (form, mechanism, deep-dive sheet) are not drawn, and no output picture is rendered: `~/.vault-sandbox` is missing on this machine, so there was no plotting library. To make it: `uv venv ~/.vault-sandbox` then `uv pip install --python ~/.vault-sandbox/bin/python pandas numpy scipy matplotlib statsmodels openpyxl`.
> - No quiz page covers this note yet. The [Judge Agreement Quiz](https://claude.ai/artifact/RthoGPnogcnYFtTDMgPvqM) has seven questions that lean on it (E5, G4, I1, I2, I3, I4, X2).
> - 2 claims are marked stated and keep nothing unfinished.

**The bootstrap measures how much a number computed from your data would move if you had collected a different sample of the same size.** You have one sample. You draw many new samples from it, each the same size, recompute the number on each, and look at how much the results differ. The size of that difference is the noise in your number.

**Where you work.** Any folder with Python 3.10 or later. Nothing is installed: the scripts use the standard library and run with `python3 -I`. Every value and every judge outcome in this note is invented.

## Table of contents

- [What the bootstrap is and why it is here](#what-the-bootstrap-is-and-why-it-is-here)
- [Worked example one: the mean of six values](#worked-example-one-the-mean-of-six-values)
- [Worked example two: kappa on 20 products](#worked-example-two-kappa-on-20-products)
- [The method in numbered steps](#the-method-in-numbered-steps)
- [Where it goes wrong](#where-it-goes-wrong)
- [Check it by script](#check-it-by-script)
- [Other ways](#other-ways)
- [Taught in, applied in](#taught-in-applied-in)
- [How this was checked](#how-this-was-checked)
- [Videos](#videos)

## What the bootstrap is and why it is here

Navigation: 📋 [[#Table of contents]] | [[#Worked example one: the mean of six values]] ➡️

Textbook: [Introduction to probability for data science, 9.2 bootstrapping, pp. 575 to 582](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=575). The standard error of a mean is on [p. 568](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=568).

In plain words: you measured something once, say how long six reviews took, and you computed one number from it, the average. A second set of six reviews would give a different average. How different? You cannot go and collect the second set. The bootstrap pretends the six values you have are the whole supply, draws a new set of six from them, and computes the average again. It does that many times. The averages it gets scatter around, and the width of the scatter says how far a fresh sample's average would plausibly sit from yours.

**Why it is here.** For an average there is a formula for that scatter (below). For a median, a ratio, or Cohen's kappa there is no short formula, and the bootstrap gives the scatter anyway, by recomputing. It does not improve your number. It only says how far to trust it (the textbook, p. 576).

### Standard error

**Standard error** is the spread of a statistic across repeated samples: draw many samples of the same size, compute the statistic on each, and the standard deviation of those values is the standard error. A statistic is any number computed from a sample (a mean, a median, kappa). The textbook defines it for a mean as $\sqrt{\mathrm{Var}[\hat\Theta]} = \sigma/\sqrt{N}$ (equation 9.7, p. 568). The bootstrap standard error is the same quantity, found by resampling the one sample you have in place of collecting new ones (equation 9.22, p. 582).

### Percentile interval

**A confidence interval from percentiles**, also the percentile interval, is the middle 90% of the resampled values. Sort the resampled values from smallest to largest, drop the lowest 5% and the highest 5%, and the smallest and largest values left are the two ends. The textbook builds its interval a different way, as the estimate plus or minus a Gaussian multiplier times the bootstrap standard error (equation 9.23, p. 582). The percentile version needs no Gaussian assumption and is the one used in this vault's kappa notes, following Rao and Callison-Burch (section 4.3, PDF page 7). Backing: cited (both).

**Why this matters.** A number without its spread cannot be compared with another number. The judge-agreement notes lean on this in seven quiz questions, from "why resample whole products" to "whether kappa 0.41 against 0.34 shows a win". Backing: cited (Chan, section 9.2).

## Worked example one: the mean of six values

Navigation: ⬅️ [[#What the bootstrap is and why it is here]] | 📋 [[#Table of contents]] | [[#Worked example two: kappa on 20 products]] ➡️

**Six invented values** (minutes to review six products): 4, 6, 7, 9, 12, 14. Number the positions 1 to 6.

**The number and its formula spread.**

$$
\bar x = \frac{4+6+7+9+12+14}{6} = \frac{52}{6} = 8.6667
$$

Distance of each value from 8.6667, squared: $21.7778,\ 7.1111,\ 2.7778,\ 0.1111,\ 11.1111,\ 28.4444$. Their sum is $71.3333$.

The textbook standard error divides the sum by $n-1 = 5$ to get the sample variance, takes the square root, and divides by $\sqrt{n}$:

$$
s = \sqrt{71.3333/5} = \sqrt{14.2667} = 3.7771, \qquad \frac{s}{\sqrt{6}} = \frac{3.7771}{2.4495} = 1.5420
$$

**Six resamples, written in full.** Each resample draws a position from 1 to 6, writes down its value, puts it back, and does that six times. The positions come from a seeded generator.

| Resample | Positions drawn | Values drawn | Sum | Mean |
|---|---|---|---|---|
| 1 | 4, 2, 6, 5, 3, 2 | 9, 6, 14, 12, 7, 6 | 54 | 9.0000 |
| 2 | 6, 4, 6, 3, 5, 2 | 14, 9, 14, 7, 12, 6 | 62 | 10.3333 |
| 3 | 6, 6, 4, 3, 4, 5 | 14, 14, 9, 7, 9, 12 | 65 | 10.8333 |
| 4 | 6, 5, 2, 3, 5, 6 | 14, 12, 6, 7, 12, 14 | 65 | 10.8333 |
| 5 | 3, 5, 1, 6, 2, 6 | 7, 12, 4, 14, 6, 14 | 57 | 9.5000 |
| 6 | 6, 4, 6, 6, 2, 5 | 14, 9, 14, 14, 6, 12 | 69 | 11.5000 |

**The spread of the six means.** Their average is $62.0/6 = 10.3333$. Distance of each mean from it, squared: $1.7778,\ 0.0,\ 0.25,\ 0.25,\ 0.6944,\ 1.3611$, sum $4.3333$. Divide by the number of resamples $K = 6$ (equation 9.21 divides by $K$):

$$
V_{\text{boot}} = 4.3333/6 = 0.7222, \qquad \mathrm{se}_{\text{boot}} = \sqrt{0.7222} = 0.8498
$$

**Six resamples are too few.** 0.8498 is far from the formula's 1.5420, and the average of the six means (10.33) sits well above the original mean (8.67) by chance. The same seeded generator with more resamples:

```text
K =   100 resamples: mean of means 8.8450, bootstrap standard error 1.3732
K = 10000 resamples: mean of means 8.6503, bootstrap standard error 1.4024
90% range of the K = 10000 resampled means: 6.333 to 11.000
```

**They agree.** The bootstrap treats the six values as the whole supply, and the spread of a whole supply divides the squared distances by $n = 6$, not $n-1 = 5$. With that divisor the formula gives $\sqrt{71.3333/6}/\sqrt{6} = 3.4480/2.4495 = 1.4077$. The 10,000-resample figure 1.4024 is within 0.005 of it. The textbook's 1.5420 is larger by the factor $\sqrt{6/5} = 1.0954$, the usual correction for estimating the spread from a sample. Backing: shown (the run), derived (the divisor).

## Worked example two: kappa on 20 products

Navigation: ⬅️ [[#Worked example one: the mean of six values]] | 📋 [[#Table of contents]] | [[#The method in numbered steps]] ➡️

**The table.** Judge A on 20 products, invented: both pass 16 (TP), reviewer passes and the judge fails 1 (FN), judge passes and the reviewer fails 2 (FP), both fail 1 (TN). The table is built in [[Chance-Corrected Agreement#Expected agreement]].

**Kappa by hand.** Observed agreement $p_o = (16+1)/20 = 0.85$. Reviewer pass rate $17/20 = 0.85$, judge pass rate $18/20 = 0.90$. Agreement expected by luck $p_e = 0.85 \cdot 0.90 + 0.15 \cdot 0.10 = 0.765 + 0.015 = 0.78$.

$$
\kappa = \frac{p_o - p_e}{1 - p_e} = \frac{0.85 - 0.78}{1 - 0.78} = \frac{0.07}{0.22} = 0.3182
$$

**Resample the 20 products.** Each resample draws 20 products with replacement, keeping a product's reviewer and judge verdicts together. Number the products 1 to 16 (TP), 17 (FN), 18 and 19 (FP), 20 (TN). The first three resamples, seed 11:

| Resample | Table (TP, FN, FP, TN) | $p_o$ | Pass rates (reviewer, judge) | $p_e$ | $\kappa$ |
|---|---|---|---|---|---|
| 1: products 2, 3, 4, 5, 6, 6, 7, 10, 15, 15, 15, 15, 16, 17, 17, 18, 18, 19, 20, 20 | 13, 2, 3, 2 | 0.75 | 0.75, 0.80 | 0.65 | 0.2857 |
| 2: products 1, 1, 2, 2, 3, 6, 7, 7, 8, 11, 13, 15, 15, 15, 17, 17, 19, 20, 20, 20 | 14, 2, 1, 3 | 0.85 | 0.80, 0.75 | 0.65 | 0.5714 |
| 3: products 1, 1, 3, 3, 3, 4, 8, 8, 9, 9, 10, 10, 11, 13, 14, 15, 16, 17, 18, 19 | 17, 1, 2, 0 | 0.85 | 0.90, 0.95 | 0.86 | −0.0714 |

Resample 3 as a check: $p_e = 0.90 \cdot 0.95 + 0.10 \cdot 0.05 = 0.855 + 0.005 = 0.86$, and $\kappa = (0.85-0.86)/(1-0.86) = -0.0714$. A resample with no product 20 has no pair of failures, so the same 0.85 agreement now scores below luck.

**Ten thousand resamples.**

```text
10000 resamples: 8534 usable, 1466 undefined (dropped)
mean of resampled kappas 0.314, standard deviation (bootstrap standard error) 0.302
5th percentile -0.111, median 0.318, 95th percentile 0.773
share of usable resamples at or below 0: 0.254
```

**Reading it.** 1,466 resamples (14.7%) drew either no product the reviewer failed or a judge column that never changes, so kappa has a zero denominator. They are dropped, which is a choice that slightly favours the resamples that kept a bad product. The other 8,534 are sorted, the lowest 5% and highest 5% cut, and the ends read: **the 90% range of kappa is −0.11 to 0.77**, with bootstrap standard error 0.302. A kappa of 0.318 from 20 products, only 3 of them bad, is compatible with agreement no better than luck, and 25.4% of the resamples land at or below zero. Rao and Callison-Burch put the standard error at 0.04 to 0.06 for 300 decisions; this one is five to seven times that, and a share of the gap is likely the three bad products (inferred, stated). Backing: shown (the run), cited (Rao and Callison-Burch, page 7).

## The method in numbered steps

Navigation: ⬅️ [[#Worked example two: kappa on 20 products]] | 📋 [[#Table of contents]] | [[#Where it goes wrong]] ➡️

1. **Decide the unit that is independent.** One product, one respondent, one family of copies. Number the units $1$ to $n$. The sample is these $n$ units.
2. **Write the statistic as a function of a list of units.** The mean of the values, kappa of the table the units make. Compute it on the original list. That is your point value.
3. **Draw one resample.** Pick a unit number from 1 to $n$ at random, write down that unit, put it back, and repeat until you have $n$ units. A unit can appear twice or not at all.
4. **Compute the statistic on the resample** and write it down. If it is undefined (a zero denominator), count it and leave it out.
5. **Repeat steps 3 and 4** $K$ times. Use at least 2,000 for an interval; the 6 in the first example is only for reading.
6. **Standard error.** Average the $K$ values, take each value's distance from that average, square, add, divide by $K$, take the square root.
7. **Percentile interval.** Sort the $K$ values. For a 90% range read the value at position $0.05K$ and the value at position $0.95K$.
8. **Say what you left out.** Report $K$, how many resamples were undefined, and the unit you resampled.

Run the loop from step 3 to step 5 on new numbers by changing `x` and the statistic in `sandbox/bootstrap_mean.py`.

## Where it goes wrong

Navigation: ⬅️ [[#The method in numbered steps]] | 📋 [[#Table of contents]] | [[#Check it by script]] ➡️

**Resampling single rows when rows come in groups.** The judge-agreement set has 105 rows that are 8 products: each a good page plus its planted copies (3 products with 14 copies, 5 with 11, so $3 \cdot 14 + 5 \cdot 11 = 97$ copies). Resampling rows treats the 105 rows as 105 independent units. They are 8. If a judge's verdict on one copy predicts its verdict on the other copies of that product, the row version reports less noise than there is.

The existing run in [[How Sure Kappa Is#Rows against whole products]] has judge verdicts drawn independently per row, and there rows gave the wider range: 0.14 to 0.53 (sd 0.119) against 0.20 to 0.51 (sd 0.094) for whole products. Independence per row means copies did not move together, so rows did not understate anything. That run does not show the failure. To show it, `sandbox/bootstrap_groups.py` makes the copies of a product share one fate (right together or wrong together, probability 0.85) and compares the two resamplings over 30 different seeded data sets:

```text
independent: mean sd rows 0.109, mean sd products 0.087, rows gave the smaller sd in 2 of 30 data sets
shared     : mean sd rows 0.090, mean sd products 0.203, rows gave the smaller sd in 23 of 30 data sets
```

**The number that shows it.** When copies share their fate, resampling rows reports a standard deviation of 0.090 and resampling whole products reports 0.203. The row version claims 44% of the noise ($0.090/0.203$). A single data set can mislead either way: seed 3 gave rows 0.78 to 1.00 (sd 0.083) against products 0.75 to 1.00 (sd 0.075), because kappa 0.928 sits against its ceiling of 1. The 30-seed average is the figure to quote. Resampling whole products rests on 8 units, so its own range is wide and uncertain (stated). Backing: shown (the run), cited (Rao and Callison-Burch advise resampling whole items).

**Two smaller ways it goes wrong.** Too few resamples (the 0.8498 in example one). Dropping undefined resamples without saying so (the 1,466 in example two).

## Check it by script

Navigation: ⬅️ [[#Where it goes wrong]] | 📋 [[#Table of contents]] | [[#Other ways]] ➡️

**What you need:** Python 3.10 or later (`python3 --version`). If it is missing, install it from python.org; nothing else is needed. The scripts are in `sandbox/` beside this note: [bootstrap_mean.py](sandbox/bootstrap_mean.py), [bootstrap_kappa.py](sandbox/bootstrap_kappa.py), [bootstrap_groups.py](sandbox/bootstrap_groups.py). Copy them into an empty folder and run each from there.

```bash
python3 -I bootstrap_mean.py
python3 -I bootstrap_kappa.py
python3 -I bootstrap_groups.py
```

You should see the full outputs saved beside this note: [bootstrap_mean-output.txt](assets/bootstrap_mean-output.txt), [bootstrap_kappa-output.txt](assets/bootstrap_kappa-output.txt), [bootstrap_groups-output.txt](assets/bootstrap_groups-output.txt). The key lines are the ones quoted in the examples above.

**A second route for the mean.** The script prints the formula route (`s/sqrt(n)` with divisor $n-1$ is 1.5420, with divisor $n$ is 1.4077) beside the 10,000-resample figure 1.4024. **A hand count for kappa.** The first line of `bootstrap_kappa.py`'s output, `po=0.8500 a=0.8500 b=0.9000 pe=0.7800 kappa=0.3182`, matches the hand steps in example two. **Clean-up.** Delete the empty folder; `ls` on the parent shows nothing of it. The scripts write nothing.

## Problems to practise on

<!-- worked-examples-table: resampling-the-bootstrap rev=2 -->
Problems on resampling one small data set with replacement to get a standard error or an interval for a statistic, from the easiest to the hardest. They are meant to serve the Judge Agreement Quiz questions that need resampling: I1, I2, I3, I4, E5, G4 and X2.

| Order | What it asks | Kind | Where | Difficulty | Full-steps solution | Quiz question |
|---|---|---|---|---|---|---|
| 1 | Resample ten exam scores (72, 69, 75, 58, 67, 70, 60, 71, 59, 65) with replacement 1,000 times, take the median of each resample, and read off the bootstrapped variance, standard error and interval. Also: why sampling with replacement and not a shuffle | Worked example, with Python code: `bootstrap_se(x, stat, K)` | [[introduction-to-probability-for-data-science.pdf#page=578\|Chan 9.2, the method, PDF pp. 578 to 580]] and [[introduction-to-probability-for-data-science.pdf#page=581\|the code, PDF pp. 581 to 582]] | Easy | Partial. The book gives the algorithm, the code and the formulas (9.20 to 9.23) and prints no resulting number for these scores: none: to be written for the numbers | I1, I2 |
| 2 | Five invented record decisions, three right and two wrong: draw five cards with replacement by hand, then list all 3,125 resamples in code and read the 95% percentile interval, which comes out 0.2 to 1.0 | Tutorial, Python: `bootstrap_toy.py`, with `empirical_quantile(values, q)` | [the measurement chapter, section 10.4, "Rehearse bootstrap sampling"](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/10-measurement.md#104-the-prototypes-baseline-scored-with-mlflow) | Easy | In the chapter: the formula (10.16), the script and its expected output (accuracy 0.6000, interval 0.2000 to 1.0000) | I1, G4, I2 |
| 3 | A lognormal sample of 100 values: bootstrap a 95% interval for its skewness, with resample sizes 30, 70 and 10, and plot the histograms. A statistic that is not a mean, so no formula gives its spread | Programming exercise, Python or MATLAB: `bootstrap_ci_skewness(y, K, B)` | [[introduction-to-probability-for-data-science.pdf#page=624\|Chan, Exercise 4, PDF p. 624]] | Medium | none: to be written | X2 (practice only: its solution is still to be written) |
| 4 | Resample the 20 products behind one judge's agreement table (16 both pass, 1 reviewer-only pass, 2 judge-only passes, 1 both fail) 10,000 times and report the 5th, 50th and 95th percentiles of the agreement score P+, dropping resamples where it is undefined | Tutorial, Python (standard library): `bootstrap_pplus(items, n_resamples)` | [the check script, last line of test 3](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/drips/combine-validating-an-llm-judge/checks/test-3-and-gold-design.py) | Medium | Partial. Running the script prints 9,489 usable of 10,000, 5th percentile 0.00, median 0.92, 95th percentile 1.00; the script has no written steps: none: to be written for the steps | E5, X2 |
| 5 | Compare two systems scored on the same products: resample the products once per replicate, score both systems on that one resample, and take the interval of the difference. Then the exact paired test on the 15-case table | Tutorial | [the measurement chapter, section 10.4, "Bootstrap a paired change"](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/10-measurement.md#104-the-prototypes-baseline-scored-with-mlflow) | Medium | Partial. The chapter gives the formulas and the paired table; it works the exact test and not a bootstrap run: none: to be written for the bootstrap numbers | I3, I4 |
| 6 | The largest of 50 uniform draws on (0, θ) with θ = 1 estimates θ: find its distribution, show it equals θ with probability zero, and bootstrap its histogram to see where resampling fails | Programming exercise, Python or MATLAB: `bootstrap_max_hist(x, K)` | [[introduction-to-probability-for-data-science.pdf#page=624\|Chan, Exercise 5, PDF p. 624]] | Hard | none: to be written | G4 (practice only: its solution is still to be written) |

No row resamples a correlation coefficient: the nearest statistics are a median, a skewness and the agreement score P+, and the correlation case still has to be written. The kappa case is worked in the note this block sits in. The Rao and Callison-Burch interval for kappa 0.402 (page 7 of the paper) is a reported result with no steps, so it is not a row. Row 3 asks for subsamples of size B inside 100 values, which is a variant of the full-size resampling that row 1 describes.
Read in full: Chan PDF pp. 575 to 582 and 621 to 625, the measurement chapter's section 10.4 from "Rehearse bootstrap sampling" to the paired table, and the check script, which was also run. Only found: the bootstrap mentions in Bishop (PDF pp. 42, 661 and 671, which are bagging and error bars in a paragraph), the Goodfellow deep learning book (PDF p. 272) and Understanding Deep Learning (PDF p. 160), none of which works an example. No solutions exist on the shelf for Chan's exercises 4 and 5.
<!-- /worked-examples-table -->

## Other ways

Navigation: ⬅️ [[#Check it by script]] | 📋 [[#Table of contents]] | [[#Taught in, applied in]] ➡️

**A formula when one exists.** For a mean, $s/\sqrt{n}$ needs no resampling and is the first thing to use. For kappa, Rao and Callison-Burch use a delta-method formula ([[How Sure Kappa Is#Other ways]]).

**Comparing two statistics.** Resample the units once and score both on the same resample: [[How Sure Kappa Is#When two kappa values are inside each other's noise]].

**Picking a unit number at random** is the discrete case of inverse transform sampling with every probability $1/n$: [[Inverse Transform Sampling#Other ways]].

**Resampling a correlation.** Phi is a correlation coefficient for two yes-or-no columns ([[Correlation Coefficient]], [[Phi And Q]]), and the same loop gives its spread. No worked case is written for it here.

**A bound instead of an interval for skipped rows**: [[Selective Evaluation]] gives a guaranteed bound on disagreement from a calibration set, which resampling does not.

## Taught in, applied in

Navigation: ⬅️ [[#Other ways]] | 📋 [[#Table of contents]] | [[#How this was checked]] ➡️

**Taught in.**

- [The combined reading of validating an LLM judge](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/drips/combine-validating-an-llm-judge/COMBINE_MAP.md), idea 6, how sure a number is from few labels.
- [The measurement chapter, section 10.4](/Users/molefemolefe/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/10-measurement.md#104-the-prototypes-baseline-scored-with-mlflow), "Rehearse bootstrap sampling": five invented outcomes resampled by hand and all 3,125 resamples listed in code.

**Applied in.**

- The v3 product-content judge in the Dis-Chem product data repo: kappa on 8 gold pages with 97 planted copies; the question was how wide kappa's range is when almost every row is a copy. Outcomes here are invented.

## How this was checked

Navigation: ⬅️ [[#Taught in, applied in]] | 📋 [[#Table of contents]] | [[#Videos]] ➡️

> [!note]- How this was checked
> The three scripts were run on 2026-10-18 on a Mac with Python 3.12 (standard library only) using `python3 -I`, each from an empty folder that was removed afterwards. The seeds are 2024 (example one), 11 (example two) and 1, 3 and 7 (the group runs). The textbook pages were read with PyMuPDF: PDF pages 575 to 582 teach the bootstrap and page 568 the standard error of a mean; page 583 starts hypothesis testing and does not teach it, so it is not cited. The book prints no result for its ten-score example, so no number here is checked against the book; the formulas (9.7, 9.21, 9.22, 9.23) are. `~/.vault-sandbox` does not exist on this machine. The note has not been rendered in Obsidian. The Where to learn this card at the end of the note was checked on 2026-10-24: each textbook range was read with pdftotext after finding it through the books' back-of-book indexes, the StatQuest bootstrapping row was copied from the video lessons index, the TileStats and StatQuest standard-error chapter lists were read with cache-video-chapters.py and described from their chapter titles only, and each plan and chapter was read at its title and description.
>
> Claims marked stated, 2: that the larger error in example two is partly from the three bad products; that resampling whole products is itself uncertain on 8 units.

## Videos

<!-- video-table: bootstrap-resampling rev=1 -->
StatQuest, then Joshua French from the open web, on the bootstrap (resampling a data set with replacement to get a standard error or an interval), in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Eight patients with a mean response of 0.5, and why repeating the whole experiment to see how far that mean moves is too costly | Intuition | [StatQuest, Bootstrapping Main Ideas, 0:17 to 2:18](https://www.youtube.com/watch?v=Xz0x-8-cgaQ&t=17s) |
| 2 | Draw from the eight values eight times with replacement, take the mean, repeat thousands of times; the four steps and the name for sampling with replacement | Worked example | [StatQuest, Bootstrapping Main Ideas, 2:18 to 5:22](https://www.youtube.com/watch?v=Xz0x-8-cgaQ&t=138s) |
| 3 | The standard error is the standard deviation of the bootstrap means; a 95 percent interval is the stretch that covers 95 percent of them | Definition | [StatQuest, Bootstrapping Main Ideas, 6:30 to 7:02](https://www.youtube.com/watch?v=Xz0x-8-cgaQ&t=390s) |
| 4 | A sample of numbers, 1000 resamples in R, the 2.5 and 97.5 percent quantiles of the resample means, and the interval 2.44 to 4.98 for a true mean of 3 | Worked example, code walk, open web | [Joshua French, Bootstrap confidence interval example, 2:12 to 6:12](https://www.youtube.com/watch?v=IBuJSRu9Quw&t=132s) |

StatQuest shows the eight values on screen without reading them out and gives no number for the standard error. French reaches an interval, not a standard error, and uses the percentile interval only. Neither covers when the bootstrap fails. Mahesh Huddar's channel has no video on it. Times are read from automatic captions and good to about 30 seconds.
<!-- /video-table -->

## Where to learn this

**Bootstrap**, resampling one data set with replacement to see how far a statistic would move on another sample, and the standard error that spread gives. Also: bootstrapping, resampling, standard error, standard error of the mean, bootstrap confidence interval.

**Textbooks**

- Introduction to probability for data science, section 9.2: [pages 575 to 582](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=575). Why bootstrapping is needed, a brute-force approach first, the procedure and the bootstrapped distribution, its interpretation, then the bootstrap standard error in MATLAB and Python on page 581.
- Introduction to probability for data science, section 9.1.4: [pages 567 to 568](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=567). The standard error of the sample mean and how it sets a confidence interval's width (Example 9.4).
- Probabilistic machine learning: an introduction, section 4.7.3: [pages 176 to 177](../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=176). The parametric and non-parametric bootstrap as an approximation to an estimator's sampling distribution, drawn for a Bernoulli MLE with 10,000 resamples and set beside the Bayesian posterior.
- Probabilistic machine learning: advanced topics, section 3.3.2: [page 106](../references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=106). The same two bootstraps more briefly, with why a resample holds only about 0.632 N distinct points.
- Deep learning textbook, section 5.4.3: [page 144](../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=144). The standard error of the mean, σ/√m, and its use for confidence intervals when comparing models.

**Videos**

- TileStats, Bootstrap confidence intervals: explained, How to calculate a 95% bootstrap confidence interval, 1:40 to 5:00: [watch](https://www.youtube.com/watch?v=AA7Jtuu9TaE&t=100s). Builds a 95 percent bootstrap interval from resamples of one sample. Chapter-timed.
- TileStats, Bootstrap confidence intervals: explained, Do bootstrap confidence intervals work?, 5:00 to 10:36: [watch](https://www.youtube.com/watch?v=AA7Jtuu9TaE&t=300s). Checks whether the bootstrap interval covers the true value as often as it claims. Chapter-timed.
- StatQuest, Bootstrapping Main Ideas, 2:18 to 5:22: [watch](https://www.youtube.com/watch?v=Xz0x-8-cgaQ&t=138s). Draws from eight values eight times with replacement, takes the mean, and repeats thousands of times. Caption-read, from the video lessons index.
- StatQuest, The standard error, Clearly Explained, Example, 2:43 to 5:59: [watch](https://www.youtube.com/watch?v=XNgt7F6FqDU&t=163s). The standard error of a mean shown on repeated samples. Chapter-timed.
- StatQuest, The standard error, Clearly Explained, Bootstrapping, 8:45 to 11:12: [watch](https://www.youtube.com/watch?v=XNgt7F6FqDU&t=525s). Getting the standard error by bootstrapping when only one sample exists. Chapter-timed.

**Our plans and chapters**

- [The percentile bootstrap over whole products](/home/molef/goal-setting/learning/mathematics/statistics/sampling/textbook/08-the-percentile-bootstrap.md#84-why-with-replacement-and-the-bootstrap-standard-error), mathematics/statistics/sampling, chapter 08, section 8.4. Why resampling is done with replacement, and the bootstrap standard error.
- [Resample the 105 rows by whole product, and see where the bootstrap stops](/home/molef/goal-setting/learning/mathematics/statistics/sampling/plans/14-the-product-level-bootstrap-built.md), mathematics/statistics/sampling, plan 14. Builds a 10,000-resample bootstrap over whole products, reproduces a published κ interval, and runs it to where it fails.
- [The normal interval from a standard error](/home/molef/goal-setting/learning/mathematics/statistics/sampling/textbook/06-the-normal-interval.md#62-the-standard-error), mathematics/statistics/sampling, chapter 06, section 6.2. The standard error itself, before any interval is built from it.
- [Say how the standard error shrinks as the draws grow](/home/molef/goal-setting/learning/mathematics/statistics/sampling/plans/21-how-the-standard-error-shrinks-with-n.md), mathematics/statistics/sampling, plan 21. Moves a standard error from one sample size to another with c/√n.
