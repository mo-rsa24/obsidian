# 52: The BRS as a field checklist

The workbook is `assets/brs-fields.xlsx`: a `fields` sheet (one row per field) and a `hard-blocks` sheet (one row per §11 bullet). **Status:** Claude's draft, for me to revise.

## 1.1 One field first: Online Name

**Rule.** Mandatory. At most 100 characters (§5.1), at least 20 (§5.2). No truncation, no abbreviations. Sentence case with lower-case units; acronyms upper case; brand names keep their own format. Order: brand, product name, then variant, size, weight or quantity. UK English.

**Section.** §5.1 and §5.2, with §11's "missing mandatory online name" as its hard block.

**Why each rule belongs to this field.** Length, case, units and order are all properties of the name's text, so a check can read them off the one field. The hard block is narrower than the rules: §11 blocks a *missing* name, not a badly formed one. "Tferg Whey Protein 420g Choc" breaks the abbreviation rule and the brand-format rule, but is not a hard block.

## 1.4 The counts, and what each one counts

**41 field rows.** One per named field or relationship in §§3.1 to 3.3, §4.1, §5.1, §5.1.1 and §5.2, with the §5.1 and §5.2 entries for the same field merged into one row.

**4 rows labelled mandatory.** Online Name, Short Description, Long Description and Barcode: the rows where the BRS uses the word "Mandatory". Product Images is labelled "required by count" (minimum 2) because the BRS never calls it mandatory. Ten rows say "where applicable". Twelve are left blank because the document does not say.

**11 field rows marked yes for a hard block.** Four of them are conditional: Ingredients, Usage Instructions and Warnings (only where regulated information applies), and BMC (only where the wrong category affects compliance or discoverability). This is a count of field rows, not of blocks: one block (image does not match the product) touches three rows, and one (missing mandatory ERP attributes) links to no row yet.

**11 §11 bullets, 10 hard blocks.** The eleventh, that business users understand each failure and its fix, is a requirement on every block, so it is recorded with `no` in the hard-block column and `yes` for explanation required.

**Check against the plan.** §5.1 has 6 online attributes and §5.1.1 has 4 optional ones; both match.

## Questions the document leaves open

- **Which ERP attributes are "mandatory … needed for product display or filtering" (§11)?** §5.2 uses "Mandatory" only for Barcode, so the eighth hard block names no settled field. Client question.
- **Ingredients: sentence case (§5.1) or title case (§5.2)?** The two sections disagree. Client question.
- **Optional fields that can block.** Warnings and Usage Instructions are optional in §5.1.1, but §11 blocks missing regulated information "where applicable". Who decides where it applies? Client question, and plan 49's question 4 is related.
- **Online Name length: max 100 (§5.1) or 20 to 100 (§5.2)?** Read together as 20 to 100; the workbook keeps both.
- **§4.1 calls "≤ 200kb" a "Minimum File Size".** The value is a maximum. Read as 200 KB or less.
- **Aspect ratio and resolution (§3.3) have no values.** No check can be built until they do. Client question.
- **§3.3 and §3.4 are the same list twice.** Treated as one workstream; worth a line to the client in case §3.4 was meant to say something else.

## Which extract could evidence each rule

The join walkthrough's Part 7 crosswalk answers this row by row, and plan 55 builds it properly. Two rows are already placed: Drug Schedule is in SAP's `SCHEDULE_ZA` (9,879 barcode rows carry a schedule from 1 to 6, about 2.7%, which is the share of scheduled medicines and not an empty column), and Image background has no extract behind it because it needs the pixels.
