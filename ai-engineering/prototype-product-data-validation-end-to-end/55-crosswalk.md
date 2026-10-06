# 55: The crosswalk, BRS fields to extract columns

The table is the `crosswalk` sheet of `assets/brs-fields.xlsx`: one row per checklist field, with its SAP, Silo and Amplience column, how the mapping was checked, and what is still open. **Status:** Claude's draft, for me to revise. Column names and counts only.

## 1.1 One field first: Brand

| BRS field | Silo | SAP | Amplience | On the storefront |
|---|---|---|---|---|
| Brand (§3.1, §5.1 naming) | `Brand`; `Sub-Brand` | `BRAND` (a code) and `T_BRAND` (its name); `T_VENDOR` is the supplier, not the brand | none | the line above the title |

**Evidence.** For the traced spray, Silo's `Brand`, SAP's `T_BRAND` and the storefront's brand line all held the same name.

**What would disprove it.** Silo brand names that do not appear in SAP's `T_BRAND`. Counted over both files: 817 of 1,117 distinct Silo `Brand` values appear in SAP's `T_BRAND` ignoring case, 73.1% (Wilson 95% interval 70.5% to 75.7%, as a description of these values, not an estimate for another catalogue). The other 300 are spelt differently or missing in SAP.

**How sure.** The columns mean the same thing. The values agree for about three in four brands, so a brand check needs a spelling list, which is what the BRS asks for when it says brand names keep their own format.

**Sub-Brand does not explain the snack.** `Sub-Brand` is 47.5% filled, and only 146 of its 1,229 distinct values appear in SAP's `T_BRAND`. Whether the storefront's brand line reads `Brand`, `Sub-Brand` or SAP is still open.

## 1.5 Coverage, counted

Of the 41 checklist fields:

| Served by | Fields | Which |
|---|---|---|
| one source | 28 | most online content (Silo), most ERP attributes (SAP), most image rules (Amplience) |
| several sources | 8 | Online Name, Barcode, Colour Description, Size, Dimensions / Weight, Brand, Image matches the product, Image name against barcode |
| none | 5 | Specifications, Shoe Size, Age From, Age To, Foundation Type |

**How each mapping was checked.** 15 by comparing values on the traced product, the rest by column name and a fill count, and 4 are marked tentative (Long Description, Fulfilment Attribute, Skin Concern, Image type).

**Apparent coverage against real fill.** 36 of 41 fields have a column. Far fewer have data:

| Field | Column | Filled |
|---|---|---|
| Online Name | SAP `T_ARTICLE`, Silo `Product Name` | 100% each |
| Short Description (mandatory) | Silo `Short Description` | 23.6% |
| Long Description (mandatory) | Silo `Ecommerce Marketing Description`, tentative | 96.7% |
| Ingredients | Silo `Ingredients` | 70.6% |
| Warnings | Silo `General Warnings` | 60.3% |
| Usage Instructions | Silo `Usage Instructions` | 62.5% |
| Colour, Size | SAP `COLOUR`, `SIZE`, `SIZE_2`, `PACK_SIZE` | 0.0% each |
| Colour | Silo `Colour` | 12.3% |
| Weight | SAP `GROSS_WEIGHT` 51.9%, Silo `Weight` 72.6% | |
| Status | SAP `NATIONAL_ARTICLE_STATUS` | 76.8% |
| Drug Schedule | SAP `SCHEDULE_ZA` | 9,879 rows with 1 to 6 |

Silo percentages are over its 10,557 products; SAP percentages are over its 371,839 rows with a barcode. They are different populations and are not compared with each other.

**"Several" is where the conflicts are.** For colour and size, SAP's columns exist and are empty, so in practice Silo is the only source. For name, weight and brand, both sources have data and they disagree for at least the traced product. Which source wins is plan 49's question 7.

## Open questions

- Is `Ecommerce Marketing Description` the long description, the short one, or neither?
- What do the four status codes (D, X, S, N) mean, and which is "discontinued"? The §11 block on a discontinued base with an active variant cannot be built until this is known.
- Do SAP's `ARTICLES_LISTED_FOR_…` flags describe fulfilment (click and collect, delivery) or only where a product is listed? `Y` appears on 1,092 rows.
- Does gallery position 1 in an Amplience filename always mean the base image?
- Is Silo's `Skin Condition` the BRS's "Skin Concern"?
