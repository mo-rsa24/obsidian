# 50: What others learned, with the limits kept

Beside `48-who-gets-hurt.md` and `49-the-senior-questions.md`. **Status:** Claude's draft, for me to revise. Every source was read on 2026-09-30.

## 2.1 What I expect each source to help decide

- **Instacart PARSE:** when a model's answer is uncertain enough to send to a person. For me, this is question 3 in plan 49 (the threshold).
- **Shopify classification:** whether to find the category first and check only that category's attributes. For me, this is which §5.1 and §5.2 rules apply to which product.
- **Attributes-first listing generation:** whether writing descriptions from extracted facts reduces made-up content. For me, this is BRS §3.5 and §8's description improvement.
- **Rules against LLMs:** which checks need a model and which a rule does as well. For me, this is the brand-spelling and naming checks from plan 48.

## 2.2 and 2.3 The four readings

### Instacart PARSE

**Source:** [Scaling Catalog Attribute Extraction with Multi-modal LLMs](https://company.instacart.com/how-its-made/scaling-catalog-attribute-extraction-with-multi-modal-llms)

**Question I brought:** how does an extraction become uncertain enough to need a person?

**What they automated:** attribute extraction end to end, from product data to catalogue ingestion, configured through an interface without custom code.

**Where a person remains:** low-confidence values are treated as possibly wrong and are reviewed and corrected by human auditors.

**Reported metric:** images raised recall by 10% over text-only models on one attribute, sheet count (a value printed on packs). Simple attributes such as "organic" reached 95% accuracy in a day; cheaper models lost 60% accuracy on difficult attributes. No cost figures.

**Principle in my own words:** ask the model a second time whether its own answer is right, and send the answers it doubts to a person.

**Committed tool and its job:** a LiteLLM call to `databricks-llama-4-maverick` for the self-check, with an ADK step routing low-confidence results to review.

**What we still need locally:** whether the Databricks endpoint returns the token probabilities this needs; how well that score separates right from wrong on our own labelled images. PARSE's numbers are about extracting attributes, not about deciding whether an image belongs to a product.

### Shopify classification

**Source:** [Evolution of Product Classification at Shopify](https://shopify.engineering/evolution-product-classification)

**Question I brought:** why predict the category before asking for attributes?

**What they automated:** category classification, attribute extraction and simplified descriptions, with vision-language models and their product taxonomy.

**Where a person remains:** in building the training data. People review complex edge cases and novel product types, and an arbitration system settles conflicting annotations. The article does not describe a person reviewing each live prediction.

**Reported metric:** over 30 million predictions a day; 85% of predicted categories accepted by merchants; hierarchical precision and recall doubled against their earlier neural network. Acceptance is what merchants kept, not a measured accuracy.

**Principle in my own words:** the category decides which attributes matter, so settle the category first.

**Committed tool and its job:** an ADK step that fixes the product's category first, then Python selecting the BRS rules for that category from category data in Delta.

**What we still need locally:** how often SAP's category levels are wrong, and how a wrong category changes the checks that follow.

### Attributes-first listing generation

**Source:** [A Multimodal, Multitask System for Generating E-Commerce Text Listings from Images](https://arxiv.org/abs/2510.21835)

**Question I brought:** what changes when text is written from extracted attributes?

**What they automated:** a product name and description written from a single image, with price and attributes predicted alongside.

**Where a person remains:** the abstract does not describe one.

**Reported metric:** feeding the model's own predicted attributes into the text step cut the factual hallucination rate from 12.7% to 7.1% (a 44.5% relative reduction) against the same system without that step. The abstract names no evaluation set; the attributes it gives as examples are clothing ones (colour, hemline, neck style).

**Principle in my own words:** extract and check the facts first, then write the description only from those facts.

**Committed tool and its job:** an ADK sequential workflow that extracts pack facts, validates them, then drafts §3.5 descriptions from the validated fields.

**What we still need locally:** how many unsupported facts our drafts contain when checked against the pack, reviewed by a person. Every generated description still needs approval under §8.

### Rules against LLMs

**Source:** [When Do LLMs Actually Help? Evaluating LLMs as Data Quality Annotators](https://arxiv.org/abs/2608.18158)

**Question I brought:** on which task does the model earn its place over rules?

**What they automated:** two data-quality checks, entity matching and brand mislabelling, done once by rules and once by an LLM.

**Where a person remains:** the abstract does not describe one.

**Reported metric:** entity matching on the Abt-Buy benchmark: rules F1 0.950, zero-shot LLM 0.948, few-shot LLM 0.914. Brand mislabelling: LLM F1 0.833, rules 0.721. Their conclusion: LLMs add little where strong lexical signals exist, and help where the task needs background knowledge.

**Principle in my own words:** pick the technique per check; a rule is enough when the words themselves carry the answer.

**Committed tool and its job:** Python rules for the deterministic checks (name length, units, image size); the model only where knowledge is needed (does "Tferg" mean Tony Ferguson); MLflow comparing both on the same labelled cases.

**What we still need locally:** both approaches' errors on our own cases. Plan 48 gives candidates: "Tferg", "Bionike", "Ant-dark".

## 2.4 Where people enter the two flows

**Instacart, from memory:** extract attributes → the model checks its own answer → low-confidence values → a human auditor corrects them. A person sits in the live flow, on the doubtful values only.

**Shopify, from memory:** predict the category → predict that category's attributes. People review edge cases and novel types when the training data is built, not on each live prediction. The chapter's diagram draws that review as part of the live flow, which is more than the article says.

**Why neither defines the BRS approval gate.** Both routes decide which cases a person looks at, to save review effort. The BRS asks for something else: §7 requires critical failures to stop until corrected or formally overridden, and §8 requires every AI-generated description and recommended attribute to be accepted, edited or rejected by an authorised person before it is written back. A high confidence score can decide where a flag goes in the queue. It cannot grant permission to change product data.

## 2.5 Wrong-image detection is new ground

**Source:** [Towards Cross-Modal Error Detection with Tables and Images](https://arxiv.org/abs/2510.12383)

It benchmarks five baseline methods on four datasets for errors where a table row and its image disagree. Cleanlab and DataScope did best when paired with an AutoML framework, and the authors say current methods remain limited on heavy-tailed real-world data.

**The open question for this prototype:** how often does a Dis-Chem image show a different product or flavour from its record, and can the model find those cases at a false-alarm rate reviewers will accept? Plan 48 found one real case in the snack. Nothing published answers this for our catalogue, so it needs a labelled local sample (region M) before any number is trusted.

**Labels stay independent.** When building that sample, reviewers label without seeing the model's suggestion, which is a different job from approving a suggestion under §8.

## Task 1: checks on this note

**Attributions.** Each metric above is quoted from its own source and tied to that source's task and comparison. No other catalogue's number is presented as this prototype's result.

**Acceptance and accuracy kept apart.** Shopify's 85% is recorded as merchant acceptance.

**Human approval kept.** §§7 and 8 approval stays in force in 2.4 and in every mapping; confidence only routes.

**Local evidence named.** Confidence measurement (PARSE) and wrong-image detection (2.5) are both marked as needing our own labelled evidence.
