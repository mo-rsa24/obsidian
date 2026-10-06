# 54: A file too big to use, made workable

Run on the Mac from `prototype/` with `uv run --group eda python`. Counts and times only. **Status:** Claude's record of my runs, for me to revise.

## My times, beside the reference

| Step | Mine | Reference |
|---|---|---|
| Excel opening the workbook | opens, slow and hard to navigate; not timed | give it two minutes |
| Unzipped size | 4,168,167,429 bytes in 19 files, about 8.9 times the 470 MB on disk | 4.1 GB of sheet XML |
| Stream the first 200 rows to CSV | 1.02 s | about 2 s |
| Convert all rows to Parquet | 133.10 s (2 min 13 s) | about 4 min |
| A count over the whole Parquet file | under 1 s | not given |

## What the conversion produced

`data/derived/sap.parquet`: 569,033 rows, 221 columns, every column stored as text, 56 MB on disk against the workbook's 470 MB.

**The head matches the reference.** Its 200 rows have 44 empty columns, the same as the reference count.

## What the whole file holds

| Count over 569,033 rows | Rows | What it means |
|---|---|---|
| `BARCODE` filled | 371,839 | the product records; the rest have no barcode |
| `T_ARTICLE` (name) filled | 406,558 | |
| No name, brand or category | 162,273 | the skeleton rows: an article number and logistics columns only. A population to explain, not corruption |
| `BMC` code filled | 406,741 | |
| `GENERIC_ARTICLE` filled | 405,815 | variant links |

## The drug schedule, measured

Among the 371,839 barcode rows, `SCHEDULE_ZA` holds:

| Value | Rows |
|---|---|
| blank | 346,676 |
| 0 | 15,283 |
| 1 | 560 |
| 2 | 1,140 |
| 3 | 2,355 |
| 4 | 4,474 |
| 5 | 1,129 |
| 6 | 221 |
| 9 | 1 |

**9,879 products carry a schedule from 1 to 6**, about 2.7% of barcode rows. That is the population the Medicines Act placeholder rule applies to.

**Here `0` is a value, not a blank.** Schedule 0 is a real category of medicine, so the 15,283 rows marked 0 are unscheduled medicines, and the 346,676 blanks are products that are not medicines. The rule "treat 0 as blank", which is right for a net weight, is wrong for this column.

**The plain `SCHEDULE` column is nearly the same** (10,070 filled against 9,895 for `SCHEDULE_ZA` over all rows). Its 2.7% fill is the true share of scheduled products, not a sign of an empty column.

**NAPPI codes live in `NAPPI_CODE_ZA`:** 23,026 rows filled, against 132 in plain `NAPPI_CODE`.

## Still open

- My own explanation of where the reader releases a finished row and where it writes a batch (plan 54, task 1.4).
- Why 162,273 rows have no name, brand or category.
- The single row with schedule 9.
