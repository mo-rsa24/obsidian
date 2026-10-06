# 58: The filter, designed from what the delivery needs

Which rows and columns the prototype works on, from each source, with a reason for every exclusion. The counting unit throughout is **one Silo product**, of 10,557. **Status:** Claude's draft from the code in the work repo, with one decision of mine recorded below.

## The decision I made

**The set includes products with no SAP row and products with no image.** That is 616 products. The plan's reference target keeps only products that reach SAP and have at least one image (9,941). I keep the rest because the tool must report them, and a set without them cannot show that it does.

## Rows, source by source

| Source | Rows kept | How many | Why |
|---|---|---|---|
| Silo | every product, after dropping the repeated header rows | 10,557 | Silo is what is online, so it defines the set |
| SAP | the row each Silo product reaches by barcode | 10,479 articles for 10,484 products | the product record behind each online product |
| Amplience | every image of a product in the set | 17,971 images | no image is dropped for failing a rule, since those failures are what the tool reports |
| SAP, as context | the base article of each variant, fetched by article number | 1,279 base articles | a variant check needs its base, and the base has no barcode so the barcode filter drops it; these rows are context and are not counted as products |
| Storefront | none in bulk; a search link per product, and a hand-checked sample | by hand | it is not an extract; see below |

## Rows left out, and why

| Left out | How many | Reason |
|---|---|---|
| SAP rows with no barcode | 197,194 of 569,033 SAP rows | a product record needs a barcode to be joined; 162,273 of these have no name, brand or category at all. The exception is the 1,279 base articles of variants, kept as context |
| SAP rows with a barcode and no Silo product | 361,360 of 371,839 | not online, so no online content to validate |
| Amplience images of products with no Silo record | 42,958 of 60,929 images | the same reason; counted in the coverage report |
| Silo's repeated header rows | 2 | not products |

**How a skeleton row is recognised.** No barcode. Every one of the 162,273 rows with no name, brand or category also has no barcode, so the barcode test alone removes them.

**How a missing barcode is recognised.** In SAP, a blank or `0` in `BARCODE`. In Silo, a `GTIN` cell holding no run of 8 to 14 digits (none of the 10,557 products).

**Nothing is left out for failing a rule.** A product with a short name, a missing description, one image, or a small image stays in. So does a scheduled medicine and a variant.

## The keys

- Silo to SAP: the barcode, padded to 14 digits, trying every barcode in the cell.
- Images to a product: the **article number** first. The barcode in the image's filename is used only where the article finds nothing (76 products).

## Columns

**SAP, 22 of 221.** `ARTICLE`, `BARCODE` (the keys); `T_ARTICLE` (name); `BRAND`, `T_BRAND`, `T_VENDOR`; `T_DIVISION`, `T_GROUP`, `T_DEPARTMENT`, `T_CATEGORY`, `BMC`, `T_BMC` (category); `GENERIC_ARTICLE` (variants); `NATIONAL_ARTICLE_STATUS`; `GROSS_WEIGHT`, `NET_WEIGHT_OF_ITEM`, `WEIGHT_UNIT`, `VOLUME`, `VOLUME_UNIT`; `SCHEDULE_ZA`, `NAPPI_CODE_ZA`; `ARTICLES_LISTED_FOR_ONLINE_SITES`.

**SAP columns considered and dropped.** `COLOUR`, `SIZE`, `SIZE_2`, `PACK_SIZE`: 0.0% filled, so nothing to check. Plain `SCHEDULE` and `NAPPI_CODE`: the country columns carry the data. The logistics, stock and ordering columns: no BRS field reads them.

**Silo, all 133.** The text, attribute and nutrition columns are the BRS §5.1 fields themselves, and a column that is empty for one kind of product is the evidence for another.

**Amplience, all 6**, plus the four parts read out of the filename (SKU, barcode, position, extension).

**What removing a column would make impossible.** Without `GENERIC_ARTICLE`, no variant check (§3.2). Without `SCHEDULE_ZA`, the image rule cannot excuse medicines. Without `T_BRAND`, the brand in the name cannot be compared (§5.1). Without Amplience's `width`, `height` and `file_size_kb`, none of §4.1.

## The storefront

**The storefront is what the BRS sets out to fix, so it is not a source of truth.** SAP, Silo and Amplience together are the reference. The storefront is used for a few linked examples: to see how the data flows onto a page, and to let stakeholders see how the three systems map to what a customer looks at. It was read by eye for a handful of products and matched SAP's article, barcode, category code, schedule and NAPPI code on the one traced in full.

**It is not read in bulk.** The BRS has the tool ingest from approved source systems or uploaded files (§10). A question for the client: can the storefront's own data be exported?

## Checked: every exclusion has a reason, and the counting unit does not change

Four exclusions, four reasons, above. Each "how many" names its own population (SAP rows, SAP rows with a barcode, images), and the set itself is counted in Silo products everywhere.

## Still open

- What the status codes mean. The base articles' status is blank on nearly all their rows.
- Whether the client will supply a storefront export.
