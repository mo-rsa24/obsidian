# 57: The questions, before the charts

Each question the BRS raises about the data, with what is counted, what it is a share of, the answer, where the chart is, and what the chart leaves out. Counts only. **Status:** Claude's draft. The questions were written after the measurements existed, so the "if the answer is bad" line records the consequence, not a prediction made beforehand.

**The five populations, kept apart**

| Name | What one unit is | How many |
|---|---|---|
| SAP rows | one article | 569,033 |
| SAP rows with a barcode | one product record | 371,839 |
| Silo products | one online product | 10,557 |
| barcode tokens | one barcode read out of a Silo `GTIN` cell | more than Silo products: 605 cells hold two or more |
| image rows | one image | 60,929, across 36,658 SKUs |

A percentage over one of these is never set beside a percentage over another.

## 1. Are the mandatory fields filled? (BRS §5.1, §5.2)

**Counting unit and denominator.** One Silo product, of 10,557, for the three text fields. One SAP row with a barcode, of 371,839, for the barcode and SAP's name.

**If the answer is bad:** a mandatory field that is mostly empty cannot be validated, only reported as missing.

**Answer.** Product name 100% in both sources. Short description 23.6% (2,489 products). Long description, read as `Ecommerce Marketing Description`, 96.7%.

**Shown in:** notebook 07, the mandatory fill chart; findings page 03.

**What the chart leaves out.** Filled is not correct. A filled name can still be the wrong name, and 100% says nothing about that. Whether `Ecommerce Marketing Description` is the long description at all is still a question for the client.

## 2. How far does each source reach? (BRS §6)

**Counting unit and denominator.** One Silo product, of 10,557, for reach into SAP and Amplience. One SAP row with a barcode, and one Amplience SKU, for how much of each Silo covers.

**If the answer is bad:** products that reach only one source can have only that source's rules checked.

**Answer.** 10,484 Silo products are in SAP (99.3%). 9,941 are in SAP and have an image (94.2%). In the other direction Silo covers 2.8% of SAP's barcode rows and 27.1% of Amplience's SKUs.

**Shown in:** notebook 06, the funnel and the coverage chart; findings pages 01 and 02.

**What the chart leaves out.** A match is not a correct match: 517 SAP barcodes are shared by more than one article. The funnel also says nothing about the 361,360 SAP products with no Silo record, which the prototype never sees.

## 3. How big are the variant families? (BRS §3.2)

**Counting unit and denominator.** One Silo product found in SAP, of 10,484, for whether it is a variant. One base article for the size of its family.

**If the answer is bad:** the §11 blocks on variants (a missing relationship, a discontinued base with an active variant) need the base product, and most bases may be outside the data.

**Answer.** 4,062 Silo products are variants of another article, across 1,279 base products, a little over three variants per family on average. 6,422 are singles and 73 have no SAP row. Only 36 variants have a base article that has an image.

**Shown in:** notebook 06, the variant kinds chart; findings page 05.

**What the chart leaves out.** The spread of family sizes: an average of three hides whether a few families are very large. That chart does not exist yet. The status codes (D, X, S, N) are unexplained, so "discontinued" cannot be read at all.

## 4. How many images does a product have? (BRS §4.1, §5.2)

**Counting unit and denominator.** One Amplience SKU, of 36,658, for the image library as a whole. One Silo product, of 10,557, for what is online. One image, of 60,929, for the size rules.

**If the answer is bad:** the rule of two to four images fails most products, and the flag stops being useful.

**Answer.** Per SKU: 22,937 have one image (62.6%), 12,894 have two to four (35.2%), 827 have more. Per image: 88.4% are at least 1200 px on each side, 83.0% are 200 KB or less, and 71.6% pass both. Per Silo product: 2,804 are in SAP with two to four usable images (26.6%).

**Shown in:** notebook 04 and notebook 06's funnel; findings page 02.

**What the chart leaves out.** The three shares above are over three different populations, which is why they do not agree. Listed pixel sizes are Amplience's own figures and were checked against the downloaded image for a handful only. Whether the picture shows the right product, or a white background, cannot be counted from these columns.

## 5. Do the texts fit the BRS length bands? (BRS §5.2)

**Counting unit and denominator.** One Silo product that has the text, so the denominator changes per field: 10,557 names, 2,489 short descriptions, 10,207 long descriptions.

**If the answer is bad:** a length check would flag a large share of what little text exists.

**Answer.** Names outside 20 to 100 characters: 54. Short descriptions under the 100-character minimum: 776 of 2,489. Long descriptions under the 200-character minimum: 4,099 of 10,207.

**Shown in:** notebook 03, the two length histograms; findings page 03.

**What the chart leaves out.** A text of the right length can still say nothing about the product. Length is the cheapest check and the weakest. The 4,099 "short" long descriptions may mean the column is really the short description.

## 6. Do the keys hold? (BRS §3.3, §5.2 Barcode)

**Counting unit and denominator.** One image, of 60,929, for the image routes. One barcode token for check digits.

**If the answer is bad:** every count above rests on the join, so a weak key makes all of them soft.

**Answer.** By article 60,882 images reach SAP, by filename barcode 59,534. Of the 59,531 that reach it both ways, 65 carry a barcode that belongs to another article, 43 of them a sibling variant. 96.8% of SAP's barcodes pass the check digit.

**Shown in:** notebook 05; findings page 02.

**What the chart leaves out.** A barcode that passes its check digit can still be the wrong product's.

## Where the plan's five required questions are

Mandatory-field fill per source: question 1. Source reach: question 2. Variant-family sizes: question 3. Images per SKU: question 4. Text lengths against the BRS bands: question 5.

## Still open

- The spread of variant family sizes, as a chart.
- Fill of each text field within the SAP department it applies to, instead of across all products.
- My own predictions: none were written before the answers.
