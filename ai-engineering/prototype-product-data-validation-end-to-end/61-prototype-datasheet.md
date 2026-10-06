# 61: Datasheet for the prototype set

**For the product data team lead.** This is a fixed set of 200 Dis-Chem online products that every measurement of the validation prototype is made on. It was drawn at random from the 10,463 online products that could be tied to exactly one SAP article, so a pass rate measured on it applies to those 10,463, give or take about 7 points in 100. It is a set of inputs. It carries no checked answers, so it can show how often the tool flags a product and cannot yet show how often the tool is right. Rare problems are thin in it: it holds no product family with two or more variants together and no image filed under another product's barcode, so family checks and that image check need their own examples.

**Status:** Claude's draft, for me to revise. Counts and fingerprints only; no product is named here.

## Where it is

All three files are in the work repo, in the git-ignored folder `prototype/product_validation/data/derived/prototype-set/`.

| File | What one row is | Rows | Columns | Key |
|---|---|---|---|---|
| `prototype-set.parquet` | one SAP article that exactly one online product reaches | 200 | 278 | `art_key` |
| `prototype-set-family-context.parquet` | the base article of a variant in the set | 74 | 8 | `base_key` |
| `prototype-set-manifest.json` | the record of what was frozen | | | |

**Fingerprints (SHA-256 of the file's bytes), frozen 2026-10-01**

```text
prototype-set.parquet                 368c3148c40a2673bbe4d5e178baad505d33c62ecadcbb91fe8d728a7e3439c8
prototype-set-family-context.parquet  74976a6b8d16b20965a7f9c117b0f50e75ea730a699e1db87a33071e25228423
```

**How to check a file is this one.** From `prototype/` in the work repo:

```bash
uv run --group eda python product_validation/tools/freeze/check_prototype_set.py
```

It exits 0 and ends `downstream work may use it`, or prints `STOP:` and exits 1.

## What it is for, and what it is not for

**Use it for** measuring how often each rule and each agent verdict fires, comparing two versions of the prototype on the same products, and the demonstration (12 products are marked for it, 2 for each of 6 cases).

**Do not use it for** accuracy claims, because no product has a checked answer. Do not use it for family checks, which need a parent and all its variants together. Do not read its counts as counts of the storefront: 94 online products were set aside before the draw and can never appear.

**Reference answers would be a separate collection.** Who labels, from which evidence, with what instructions and how disagreements are settled would each need writing down. None of that exists for these 200.

## Limits that affect a decision

- **Margin.** A rate measured on all 200 is good to about 7 points in 100 either way, 19 times in 20. On the 190 with an image, the same.
- **No family of two or more variants is whole.** 77 of the 200 are variants, from 74 different base articles. For 7 of them the variant in the set is the base's only online variant; for the other 67 bases, siblings exist online and are outside the set. No base article is itself online or has a barcode, and each sits in the context file.
- **Cases the draw did not reach.** No image filed under another product's barcode, and no product whose Silo barcode cell names two SAP articles.
- **Field owners are unconfirmed.** Silo owns the online name, brand, text and size; SAP owns the barcode, category, status, schedule and NAPPI code; Amplience owns images. The client has confirmed none of these.
- **73 of the 200 carry a disagreement between sources.** Both values are kept in the row with a flag. Nothing was resolved by choosing.

<details>
<summary>How the 200 were chosen, and the statistical detail</summary>

**The unit.** One SAP article, its number with leading zeros stripped, reached by exactly one Silo product through its barcode.

**What was lost before the draw**

| Step | Online products |
|---|---|
| Silo products | 10,557 |
| no SAP row | 73 set aside |
| barcode shared by several SAP articles | 11 set aside |
| several Silo products claiming one article | 10 set aside |
| reconciled, eligible for the draw | 10,463 |

**The draw.** The 10,463 were split by whether Amplience holds at least one image. Each group got a share of the 200 in proportion to its size, and inside a group every product had the same chance.

| Group | In the catalogue | Drawn | Chance of being drawn |
|---|---|---|---|
| with an image | 9,920 | 190 | 0.01915 |
| no image | 543 | 10 | 0.01842 |

The two chances differ by under 4%, so unweighted rates are a fair reading. The exact chance is in the column `set.inclusion_probability`.

**Seed.** 0, with pandas' `sample`. The same extracts and seed give the same 200 and the same fingerprints; this was run twice and matched.

**The 60 kept.** Sixty products with an image had already been drawn at random (seed 0, from the 9,941 products in SAP with an image) and run through the agent under both names and both question wordings. All 60 are reconciled records, so they are kept inside the 190 and marked in `set.kept_from_earlier_draw`. The other 130 were drawn at random from the rest of the group. An equal-chance draw followed by an equal-chance draw from the remainder is still an equal-chance draw of the group.

**Demonstration products.** 12 are marked in `set.demonstration_case`, 2 each for: passes every measurable rule, image rule failure, mandatory text missing, name in trouble, scheduled medicine, variant. They were picked by case inside the 200, so they illustrate and do not measure. Two of the 13 products hand-picked earlier happen to be in the set; the other 11 are outside it.

**How the set compares with the 10,463**

| | In the set (of 200) | In the catalogue (of 10,463) |
|---|---|---|
| brand disagreement | 33 (16.5%) | 2,031 (19.4%) |
| weight disagreement | 27 (13.5%) | 1,570 (15.0%) |
| name disagreement | 26 (13.0%) | 1,222 (11.7%) |
| at least one disagreement | 73 (36.5%) | 4,021 (38.4%) |

Division shares differ from the catalogue's by at most 3.8 points, over 8 divisions.

**Weight in the set.** From Silo on 137, from SAP's gross weight on 57, absent on 6.

**Drug schedule.** 29 of the 200 carry a schedule value, where 0 means Schedule 0, and 2 of those are Schedule 1 to 6. The other 171 are blank.

**Inputs, by fingerprint.** The manifest records the SHA-256 of the reconciled records file, the three extracts and the list of the 60, by file name.

**What each check answers**

| Question | What it catches | What it misses |
|---|---|---|
| row count | a lost or added product | a changed value, a swapped product |
| unique key | a product listed twice | everything else |
| columns and types | a dropped, renamed, retyped or added column | a changed value |
| fingerprint | any changed byte | it cannot say what changed |

Three changed copies were checked on 2026-10-01. One row removed was caught by the row count and the fingerprint. One column removed was caught by the columns and the fingerprint. One value changed was caught by the fingerprint alone. The untouched original passed again afterwards.

The expected rows, columns and fingerprint are read from the manifest written at the freeze. They are never recomputed from the file being checked, since a changed file would then describe itself and pass.

</details>

## Unknown

- What the four status codes in SAP mean, and so whether every one of the 200 is on sale.
- Whether the owners above match how Dis-Chem's teams work.
- Whether Silo's weights are all in grams. The two sources' weights are within 1.5 times of each other on about four in five products that have both.
- How the 200 compare with what the storefront shows. The storefront was not used as a source.
- Why brand disagrees on about one product in five. SAP's brand column may hold a different level, such as a manufacturer.

## Keeping it

**The frozen files are never overwritten.** The freeze tool refuses if the set is already there.

**A new extract means a new set.** Rerun the conversion, the reconciliation and the freeze into a new folder, and record the new fingerprints in a new datasheet. Results measured on this set stay tied to these fingerprints.

**Who refreshes it** is not decided.

## Handoff

The work that loads the set into Delta, and the work that rebuilds the join in the repo, read these three files. They carry forward the identity (`art_key`), the manifest and the two fingerprints above, and they run the check first. Nothing was uploaded.
