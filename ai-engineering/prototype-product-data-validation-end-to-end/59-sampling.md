# 59: Three ways to sample, compared

What each way of drawing 5,000 of Silo's 10,557 online products keeps and breaks. The comparison is notebook 11 in the work repo (`eda/notebooks/11_sampling_compared.py`), and its table is saved privately as `data/derived/sampling_comparison.csv`. Counts only. **Status:** the Excel observation is mine; the comparison and its write-up are Claude's draft.

## What I saw in Excel

I filtered the working subset to one family by `sap.GENERIC_ARTICLE`. It showed three rows. Each article was the family number with three more digits on the end, so all three were variants, and no row was the base product. Selecting a variant did not bring its parent along.

**A variant's article is its family's number plus a three-digit suffix.** The base product's article equals the family number.

## The comparison

Same seed (0) for all three. One unit is one Silo product.

| | Catalogue | Plain random | By group (the working subset) | Whole families |
|---|---|---|---|---|
| products drawn | 10,557 | 5,000 | 5,000 | 5,001 |
| division mix: share of the sample in the wrong division | 0 | 0.8 points | 4.2 points | 1.7 points |
| products with an image failure | 76.9% | 76.6% | 74.3% | 76.5% |
| families of two or more touched | 992 | 823 | 838 | 483 |
| of those, arriving complete | all | 122 (14.8%) | 215 (25.7%) | 483 (100%) |
| variants whose base product is in the sample | | 0 of 1,906 | 0 of 2,169 | 0 of 1,930 |

**No method keeps all three.** Plain random keeps the division mix and the failure share and breaks six families in seven. The working subset drifts most on divisions and understates image failures by 2.5 points, because it adds 600 clean passes on purpose. Whole families keeps every family and stays close on the other two.

**My predictions:** none made. I asked for the comparison to be run without them.

## The finding that matters more than the method

**No sample can bring a variant's parent along, because the parents are not online products.** Silo's 4,062 variants point at 1,279 base articles, and none of those 1,279 is among Silo's products.

**The parents are in SAP, among the rows the filter drops.** All 1,279 base articles have a SAP row, 1,275 with a name, and only 6 with a barcode. One family and its base are shown in notebook 06, section 13. A base article is a record with no barcode of its own, which is exactly the kind of row "keep rows with a barcode" removes. So the variant checks in BRS §3.2 and §11 (a variant mapped to its base, a base discontinued while a variant is active) need the base rows fetched from SAP by article number, as context, alongside the products being validated.

**Their status is mostly blank.** Across the base articles' rows, status is blank on nearly all, `D` on 10 and `S` on 7. Whichever code means "discontinued", there is little there to check.

## What was chosen

| | |
|---|---|
| Method | by group for the working subset (all rare cases, a fixed number per larger group, then a random slice) |
| Seed | 0 |
| Selection unit | one Silo product |
| Actual size | 5,000 |
| Family policy | families are not kept whole; each variant's base article is fetched from SAP as a context row and is not counted among the products |
| Known limits | understates the image-failure share by 2.5 points and drifts 4.2 points on division mix, so no percentage about the catalogue is read off the whole subset |

## Which numbers come from where

- **A share of the catalogue** ("76.9% of online products have an image failure"): from all 10,557 products, or from the subset's random slice with its weights.
- **What a problem looks like, with enough cases to build a check:** from the working subset.
- **Anything about a family:** from the variant's row plus its base article's SAP row.

## Does the design support the claims?

It supports building and testing each check, and showing examples of each case. It does not support a catalogue percentage, which is why those are computed on the full set. It does not support a check against the base product, and neither does any other design, since the parents are outside Silo.
