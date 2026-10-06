# 49: The questions that settle the design

Beside the harm table in `48-who-gets-hurt.md`. **Status:** Claude's draft, for me to revise.

## 2.1 My questions, before the chapter's list

Each question says what its answer changes.

1. **What decision does the tool's output support: blocking a product from publishing, or feeding a clean-up queue?** This changes whether §11's hard blocks are enforced by the tool or only reported.
2. **Who acts on each kind of exception (images, names, attributes, regulated information), and how many flags can they review in a day?** This changes how precise each check must be before it is worth running.
3. **Which mistake costs more for one product: passing a wrong page, or flagging a correct one? Is the answer different for regulated products?** This changes the confidence threshold §12 leaves open.
4. **Does the Medicines Act placeholder count toward §5.2's minimum of 2 images?** This changes whether the image-count rule must read the drug schedule first (Flomist).
5. **§5.1 asks for sentence case, but every storefront title is in Title Case. Does the rule cover new names only, or the whole catalogue?** This changes whether a case check is built at all (178 of 178 titles, run r2).
6. **When a title and its image disagree, which one is the record of truth, and who owns the fix?** This changes where the exception report routes the row (the snack).
7. **When Silo and SAP disagree on a name or brand, which source wins, and which field feeds the storefront's brand line?** This changes the join's precedence and the brand check (the snack's brand line, Silo's `Brand` and `Sub-Brand`).
8. **Are images judged on the parent product or on each shade and variant?** This changes the variant logic in §3.2 (the lipstick).
9. **Which systems does the first release read: the three extracts only, or Commerce Cloud and Sales Layer too?** This changes whether schedule-aware rules can be built, since the storefront shows a drug schedule and NAPPI code; SAP's plain `SCHEDULE` is 2.7% filled and Silo has no schedule column, but SAP's `SCHEDULE_ZA` and `NAPPI_CODE_ZA` matched the site for one traced product, so the schedule-aware rules can read SAP: 9,879 barcode rows carry a schedule from 1 to 6 (see `54-a-file-too-big.md`).
10. **Batch or real time, and how many changed products arrive per day?** This changes the architecture and the cost of each model call.
11. **What counts as done for the prototype: which §9 outputs, on what sample, against what bar?** This changes what the demo must show.
12. **Where may product data and images be processed: the Databricks workspace, external model endpoints, both?** This changes where the model runs; today only a small sample may be uploaded.

## 2.2 An escape and a false alarm, on my own cases

**Escape (a wrong page passes).** The snack: the tool accepts a pack reading "SWEET AND SMOKEY BBQ FLAVOUR" under the title "Sweet Chilli". A customer buys the flavour they did not choose.

**False alarm (a correct page is flagged).** Flomist: the tool flags the Medicines Act placeholder as a missing image. The page follows policy, and a reviewer spends time confirming it. Across every scheduled medicine, that repeats for each one.

**Which costs more (my judgement, not evidence).** For a single product the escape costs more, because it reaches the customer and §11 lists an image that does not match the product as a hard block. At catalogue scale a false alarm that fires on a whole category costs more reviewer time and teaches reviewers to ignore the flag. So the answer depends on how often each happens, which is question 3.

## 2.3 §12 against the rest of the BRS

| §12 open question | Where the BRS already speaks | What stays open |
|---|---|---|
| Which source systems in the first release | §6.1 names ERP, Sales Layer PIM, Commerce Cloud and Magento; §6.2 names Azure blob storage for images | Which of these the first release reads (question 9) |
| Real time, scheduled batches or both | §10 step 1 says data is ingested from approved systems or uploaded files | Cadence and daily volume (question 10) |
| Where exceptions are surfaced | §7 requires exception management grouped by severity; §9's exception report names owner team, due date and resolution status | The channel: dashboard, queue, email or Teams |
| What confidence triggers pass, review or reject | §8 routes low-confidence image matches to manual review; §8 classifies issues as critical, major, minor or informational | The number itself (question 3) |
| Export format for outputs | §9 lists the five outputs and their required fields | The file format and where it lands |

## 2.4 Each question, by the route to its answer

| # | Route | BRS section checked | What it already settles | Evidence still needed |
|---|---|---|---|---|
| 1 | Dis-Chem decision | §7 approval gating; §10 steps 4 to 6; §11 | Critical failures are blocked before publishing | Whether the prototype enforces or reports |
| 2 | split: Dis-Chem decision (owners); Dis-Chem decision (capacity) | §7; §9 exception report (owner team) | An owner team exists per exception | The named teams and their daily capacity |
| 3 | Dis-Chem decision | §8 exception classification; §12 | Critical and major issues need resolution or approval | The acceptable escape rate and review burden |
| 4 | split: data check (how many products carry a schedule); Dis-Chem decision (does a placeholder count) | §4.1; §5.2 Product Images and Drug Schedule | 2 to 4 images; a base pack shot | The client's rule for scheduled medicines |
| 5 | split: BRS answer (§5.1 says sentence case); data check (casing in the extracts, not only the storefront); Dis-Chem decision (scope) | §5.1 Online Name | Sentence case with lower-case units | Whether existing titles are in scope |
| 6 | Dis-Chem decision | §9 exception report; §11 | A mismatch between image and product is a hard block | Which field is the record of truth |
| 7 | split: data check (which field feeds the storefront brand line); Dis-Chem decision (precedence) | §3.1; §6.1 | Brands need a brand category | The source that wins on conflict |
| 8 | split: data check (variant counts from `GENERIC_ARTICLE`); Dis-Chem decision (parent or variant) | §3.2; §5.2 Variants | Variants map to their base product | Which record the image rules judge |
| 9 | split: data check (fill of SAP's `SCHEDULE_ZA` and `NAPPI_CODE_ZA`); Dis-Chem decision (first-release systems) | §6; §12 | The systems exist | Access to the system holding the schedule |
| 10 | split: data check (extract sizes); Dis-Chem decision (future volume) | §10; §12 | Ingestion from systems or uploads | Cadence and daily volume |
| 11 | Dis-Chem decision | §9 | The five outputs and their fields | The demo sample and acceptance bar |
| 12 | Dis-Chem decision | §6 | Where the data comes from | Where processing is allowed |

## 2.5 Handoff for the client (plan 39)

Only the Dis-Chem decisions, each with the decision it unlocks. Owners are unconfirmed throughout.

| Question | Why the answer changes the design | BRS section checked | Person to ask | Status |
|---|---|---|---|---|
| Does the prototype block publishing or report to a queue? | Decides whether §11 blocks are enforced | §7, §10, §11 | unconfirmed | open |
| Who owns each exception type, and how many flags a day can they review? | Sets the precision each check needs | §7, §9 | unconfirmed | open |
| What escape rate is acceptable, and what review load? | Sets the §12 confidence threshold | §8, §12 | unconfirmed | open |
| Does a Medicines Act placeholder count as a product image? | Decides the image rule for scheduled medicines | §4.1, §5.2 | unconfirmed | open |
| Does §5.1's sentence case apply to existing titles? | Decides whether a case check is built | §5.1 | unconfirmed | open |
| When title and image disagree, which is the record of truth? | Decides how mismatches are routed | §9, §11 | unconfirmed | open |
| When Silo and SAP disagree, which source wins? | Decides the join's precedence | §3.1, §6.1 | unconfirmed | open |
| Are image rules applied to the parent or to each variant? | Decides the variant logic | §3.2, §5.2 | unconfirmed | open |
| Which systems does the first release read, and can we reach the one holding the drug schedule? | Decides whether schedule-aware rules are possible | §6, §12 | unconfirmed | open |
| What daily volume and cadence should the tool expect? | Decides batch against real time | §10, §12 | unconfirmed | open |
| What does the demo show, on what sample, against what bar? | Decides acceptance | §9 | unconfirmed | open |
| Where may data and images be processed? | Decides where the model runs | §6 | unconfirmed | open |

## Task 1: checks on this register

**Citations.** Every section cited above was read against the BRS V2: §3.1, §3.2, §4.1, §5.1, §5.2, §6, §7, §8, §9, §10, §11 and §12 say what the tables attribute to them.

**Questions that mix routes, split above.** Questions 2, 4, 5, 7, 8, 9 and 10 each combine a data check with a client decision, and the route column shows each part separately. No answer is supplied for either part.

**Data checks, for the T2 plans.** How many products carry a drug schedule (question 4); the casing of names in Silo and SAP (question 5); which field the storefront brand line reads (question 7); variant counts from `GENERIC_ARTICLE` (question 8); extract sizes (question 10).

## The problem statement these questions serve

`ai-engineering/prototype-product-data-validation-end-to-end/51-the-problem-statement.md` in this vault. Its unresolved decisions are questions 1, 3, 5, 8 and 9 above, carried in the 2.5 handoff for plan 39.
