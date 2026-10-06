# 53: One product, read across every column

The product is a paediatric nasal spray, a Schedule 1 medicine, traced through the storefront, Silo, Amplience and SAP. Column meanings and counts only; no values from the extracts. **Status:** Claude's draft from my terminal output, for me to revise.

## Silo: 12 of 133 columns filled

**The filled columns, and what each means**

| Column | What it holds | BRS field it serves |
|---|---|---|
| `GTIN` | the barcode; the key that joins Silo to SAP | §5.2 Barcode |
| `Brand` | the brand name | §5.1 naming, §3.1 brand category |
| `Unit of Size`, `Unit of Measure` | the amount of product in the pack and its unit | §5.1 name's size part; §5.2 Size |
| `Product Name` | Silo's own name for the product | §5.1 Online Name |
| `Weight`, `Height`, `Depth`, `Width` | the pack's weight and outer dimensions; no unit column, so the units are assumed (grams, millimetres) | §5.2 Dimensions / Weight |
| `Ingredients` | the active ingredient and strength, as a sentence | §5.1 Ingredients |
| `Usage Instructions` | who it is for and how often to use it; it also carries the age range | §5.1.1 Usage Instructions |
| `Ecommerce Marketing Description` | a short marketing paragraph | §5.1 Short or Long Description: which one is uncertain |

**The blanks that matter**

- `Short Description`: blank, on a field §5.1 calls mandatory.
- `General Warnings` and `Allergen Warnings`: blank, on a scheduled medicine. The age range sits in `Usage Instructions` instead.
- `Storage Instructions`, `Features and Benefits`, `Keywords`: blank (optional in §5.1.1).
- `Sub-Brand`, `Pack Size`, both country-of-origin columns: blank.

**The blanks that do not matter**

About 110 of the 121 blank columns cannot apply to a nasal spray: 45 nutrition columns (energy, fat, protein per 100g, per serving and as NRV), the cosmetics columns (coverage, finish, SPF, hair and skin type, fragrance notes), the appliance columns (voltage, wattage, batteries, cable length) and the kitchenware columns (oven, microwave, dishwasher safe). "12 of 133 filled" says almost nothing on its own; the useful number is how many of the columns that apply to a medicine are filled.

**Uncertain**

- Whether `Ecommerce Marketing Description` is the BRS's Short Description or its Long Description. Its length fits the short one's 100 to 400 range and falls under the long one's 200 minimum.
- The units of `Weight`, `Height`, `Depth` and `Width`.
- Why two columns exist for country of origin (one header is misspelt `Country oF Origin`), and whether `Input Voltager` is a typo for a column that matters.

## The three questions

**1. Do Silo's size and weight agree with SAP's?** The size roughly does: Silo's height × depth × width comes to about 15% more than SAP's volume, close enough for rounded box measurements, and the proportions match the tall narrow carton in the photo. The weight does not: Silo's is about 2.3 times SAP's gross weight, and SAP's net weight is zero, which is an unfilled field. One of the two weights is wrong, and the data cannot say which.

**2. What is in Silo but not on the storefront?** Three fields: the marketing description, the ingredients and the usage instructions (with the age range). The product page shows only a link to SAHPRA. So for this medicine the regulated information exists in the data and is not displayed.

**3. How many columns are filled?** 12 of 133.

## Amplience: 2 image rows

Six columns: `filename`, `file_size_kb`, `width`, `height`, `Sku`, `Url`. For this product there are 2 images, at gallery positions 1 and 2, both JPG, both exactly 1200 × 1200 pixels, and both under 200 KB. The barcode inside both filenames equals the Silo `GTIN` and the SAP `BARCODE`. `Sku` is written without leading zeros, while the filename carries the 18-digit padded form.

Against the BRS this product passes every measurable image rule: format, minimum size and file size (§4.1), and the 2 to 4 image count (§5.2). Background colour and whether the image shows the right product cannot be read from these columns.

## The same product in four places

| What | Storefront | SAP | Silo | Amplience |
|---|---|---|---|---|
| Name | SAP's name in softer case, one abbreviation spelt out | all capitals, one abbreviation | a short two-word name, under §5.2's 20-character minimum | none |
| Barcode | shown in More Info | `BARCODE` | `GTIN` | inside the filename |
| SKU | shown in More Info, 18 digits | `ARTICLE`, 18 digits | none | `Sku`, zeros stripped; padded in the filename |
| Category | BMC code | `BMC` code and `T_BMC` name | none | none |
| Schedule and NAPPI | shown in More Info | `SCHEDULE_ZA`, `NAPPI_CODE_ZA` | none | none |
| Description, ingredients, usage | not shown | none | filled | none |
| Images | 2 in the gallery | none | none | 2 rows |

## What one row cannot tell

- That Silo names are usually shorter than SAP's, or that the storefront always takes its title from SAP. One product showed it; plan 56 counts it.
- That medicines never show their description on the site. Three medicine pages showed only a SAHPRA link; that is three pages.
- How often `SCHEDULE_ZA` is filled. It was filled here.
- That Silo's weight is the wrong one.
