# 56: The keys, found by counting overlaps

Counts over the three whole files, saved privately as `data/derived/key-counts.json` in the work repo. No identifiers here. **Status:** the predictions are mine; the counts and their write-up are Claude's draft, for me to revise.

## What a barcode and an article are

**Barcode (GTIN).** Assigned by the manufacturer to a kind of item: one brand, product and size. Every box of that item carries the same barcode; a different size or flavour has a different one.

**Article (SKU).** Dis-Chem's own number for a product it stocks. It means nothing outside Dis-Chem.

## How each key is made comparable, and what is counted

| Key | Normalisation | Counting unit |
|---|---|---|
| Article | leading zeros removed from SAP `ARTICLE` and Amplience `Sku` | one image row; also one distinct SKU |
| Barcode | every run of 8 to 14 digits padded with leading zeros to 14 | one image row, or one Silo product |
| SAP side | only the 371,839 rows with a barcode | one row per article (no article repeats) |

## My predictions, and what the counts showed

| Question | My prediction | Counted |
|---|---|---|
| Which route reaches more of the 60,929 images? | article | **article: 60,882 (99.9%)**; filename barcode: 59,534 (97.7%) |
| How many of Silo's 10,557 products find a SAP row? | about 200 | **10,484 (99.3%)** |

**The first held.** 1,351 images reach SAP only by article, 3 only by barcode, and 44 by neither.

**The second missed by a factor of fifty.** I expected a match to be a coincidence of timing. The three files are exports of one catalogue, so nearly every Silo product is in SAP. The 200 I had in mind is the size of the prototype set the later plans freeze, not the size of the overlap.

## The counts

**Silo to SAP, by barcode**

| Rule | Products matched | Share of 10,557 |
|---|---|---|
| the whole `GTIN` cell must be one barcode | 9,882 | 93.6% |
| any barcode inside the cell | 10,484 | 99.3% |

605 Silo cells hold two or more barcodes. Reading the whole cell as one value loses 602 products that a split recovers. 73 products find no SAP row either way.

**Amplience to SAP**

| Route | Images | Share of 60,929 |
|---|---|---|
| by article | 60,882 | 99.9% |
| by filename barcode | 59,534 | 97.7% |
| by both | 59,531 | |
| by neither | 44 | |

36,642 of Amplience's 36,658 distinct SKUs are in SAP.

**Do the two routes agree?** Of the 59,531 images that reach SAP both ways, 59,466 carry a filename barcode that belongs to the same article (99.9%). The other 65 are filed under a barcode SAP gives to a different article. Those are candidates for §11's hard block, an image that does not match the barcode or product.

**All three together.** 9,948 Silo products have a SAP row and at least one image (94.2% of 10,557).

**Repeats.** No SAP article appears on more than one barcode row. 517 barcodes are shared by more than one article, which is what makes a barcode join return two rows for one product.

## The keys to use

- Silo to SAP: the barcode, padded to 14 digits, trying every code in the cell.
- Amplience to SAP: the article number with zeros stripped. The filename barcode is the cross-check, and the fallback for the 3 images the article misses.

## What these counts do not say

They count matches, not correct matches. A barcode that pads to the same 14 digits as another product's would count as found. The 65 disagreeing images and the 517 shared barcodes are where to look by eye.
