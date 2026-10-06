# 60: One clean record per product

Which source owns each field, what happens when two disagree, and what the rules give on the real data. The owner table is `assets/field-owners.xlsx`. The code is in the work repo: `eda/helpers/owners.py`, `tools/reconcile/reconcile_products.py` and notebook 13. Counts only. **Status:** Claude's draft, for me to revise; every owner is a prototype decision for the client to confirm.

## What one record is

**One SAP article that at least one online product reaches.** The article number, with its leading zeros removed, is the identity.

**A Silo cell holding several barcodes** is split, each barcode is padded to 14 digits, and the first one SAP knows links the product. Several barcodes do not make several records.

**A barcode sitting on more than one SAP article** is never resolved automatically. The products on it are set aside.

## Who owns each field

| Field | Owner | Fallback when the owner is blank | A disagreement is |
|---|---|---|---|
| Online name | Silo | SAP's name, flagged | the two names share under 20% of their words |
| Barcode | SAP | none | none of Silo's barcodes equals SAP's |
| Brand | Silo | none | not equal once case, spaces and punctuation are ignored |
| Category, status, variants, drug schedule, NAPPI code | SAP | none; a blank is reported | no second source |
| Descriptions, ingredients, usage, storage, warnings, features, nutrition, claims, attributes | Silo | none; a blank is reported | no second source |
| Size | Silo | none (SAP's size columns are empty) | none |
| Weight and dimensions | Silo, read as grams and millimetres | SAP's gross weight, in grams | both present and more than 1.5 times apart |
| Images and their size rules | Amplience | none | none |
| Specifications, shoe size, age range, foundation type | none | unresolved | none |

**Why Silo owns the name.** Over the 10,484 online products found in SAP, Silo's name passes the measurable BRS naming rules on 98 to 99 in every 100, depending on how "names a size" is read, and SAP's on 0.7 in every 100.

**An owner is a working choice.** Both values are kept side by side with a flag. Choosing one does not show the other was wrong.

**Against the plan's starting examples** (SAP for status and BMC, Silo for online text, Amplience for images): the same on all three. The additions are the name, the brand and the weight, where two sources both have data.

## What the rules give

| | Online products |
|---|---|
| reconciled, one record each | 10,463 |
| set aside: no SAP row | 73 |
| set aside: barcode shared by several SAP articles | 11 |
| set aside: several online products claiming one article | 10 (5 articles) |
| total | 10,557 |

**Disagreements, over the 10,463 reconciled records**

| Field | Records |
|---|---|
| brand | 2,031 |
| weight | 1,570 (of the 7,526 where both sources have a weight) |
| name | 1,222 |
| barcode | 0 (the join reaches SAP through the barcode, so it cannot disagree) |

4,021 records have at least one.

**Fallbacks.** Weight came from SAP on 2,600 records, and 272 have no weight in either source.

**Family context.** 1,275 base articles are kept beside the set for 4,051 variants. They are context and are not counted as products.

## What zero means, column by column

| Column | A zero is |
|---|---|
| net and gross weight | a blank (written `0.000`) |
| drug schedule | a value: Schedule 0 |
| NAPPI code | a blank (8,755 records carry 0) |

## The order of the sources does not change the result

A made-up conflict was run through the rules twice, with the two sources listed in opposite orders. The same owner was chosen and the same conflict was flagged both times.

## For a person to decide

- Every owner row, with the client.
- **Brand.** 2,031 disagreements may mean Silo's brand is the wrong owner, or that SAP's brand column holds something at a different level, such as a manufacturer where Silo has a product line.
- **Twenty-five records** whose Silo cell holds barcodes of two different SAP articles. They are reconciled to the first barcode SAP knows. They could be set aside instead.
- Which online product wins on the 5 doubly claimed articles.
- Whether grams and millimetres are right for Silo's measurements. Over the 7,526 records where both sources have a weight, the larger of the two is typically 1.07 times the smaller, which supports grams. On 1,570 of them, about one in five, it is more than 1.5 times the smaller.
