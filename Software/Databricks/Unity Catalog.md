---
aliases: [Databricks Unity Catalog, UC, Unity Catalog metastore, metastore, metastores, three-level namespace, three-level name, catalog.schema.table]
link-skip: [Hive metastore, hive_metastore]
standard: vault-note v2
---

# Unity Catalog

Up: [[Databricks]]

Software, Databricks. It is where the product validation bundle's catalog, schema and Volume live, and where a registered model and its [[Model Alias]] are kept.

**Unity Catalog is Databricks' governance layer for data and AI: one metastore per region holds catalogs, each catalog holds schemas, and each schema holds tables, volumes, functions and models, so every asset has a three-level name `catalog.schema.object` that permissions are granted on.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the catalog and its grants writes the rest around it.

## Where to learn this

**Unity Catalog**, the metastore, catalog and schema levels that name and govern every table, volume and model. Also: UC, metastore, three-level namespace, three-level name, `catalog.schema.table`.

**Textbooks**

- The big book of MLOps, chapter 4, Recommended organization: [pages 23 to 26](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=23). Works one layout through: dev, staging and prod catalogs, each holding bronze, silver and gold schemas and a `fraud_detection` schema with its tables, volumes, the `fraud_clf` model and the `compute_distance` function, then says who may read and write each catalog.
- The big book of MLOps, chapter 4, Concepts: [pages 18 to 20](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=18). Defines catalog, schema, data table, volume, function, registered model, model version and model alias, each with its three-level name such as `<catalog>.<schema>.<table>`.
- The big book of MLOps, chapter 4, Considerations: [pages 21 to 22](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=21). How to choose what a schema stands for (a team, a medallion layer, a project) by team size, project complexity and access levels.
- The big book of MLOps, chapter 3, Unity Catalog: [pages 10 to 12](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=10). Why data and models sit under one governance layer: account-level sharing, read access to prod from dev, lineage from a model back to its training data, and Models in Unity Catalog in place of the Workspace Model Registry.
- The big book of MLOps, chapter 5, Reference architecture: [page 31](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=31). The one-to-one mapping of environments to catalogs, with read-only access to the prod catalog from development.

**Videos**

- Chris Gambill, End-to-End Unity Catalog Setup, Setting Up Medallion Architecture Catalogs, 2:39 to 5:57: [watch](https://www.youtube.com/watch?v=s_UkMM_4cLw&t=159s). Creates bronze, silver and gold catalogs in a Databricks Free Edition workspace and opens their default and information schemas. Chapter-timed.
- Marvelous MLOps, Lecture 8, CI/CD and deployment strategies, Catalog and workspace design, 0:39 to 2:08: [watch](https://www.youtube.com/watch?v=HwH8Q0DDDc4&t=39s). How catalogs are laid out against workspaces before the CI/CD flow is built. Chapter-timed.

**Official docs**

- [What is Unity Catalog?](https://docs.databricks.com/aws/en/data-governance/unity-catalog/), Databricks documentation. Unity Catalog as the layer that enforces access control, lineage and audit logging, and the `catalog.schema.object` namespace for tables, views, volumes, functions and models.
- [Create a Unity Catalog metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/create-metastore), Databricks documentation. The metastore as the top-level container, one per region, with every workspace attached to the metastore in its region.

**Our plans and chapters**

- [Make the three levels yourself, in a free workspace](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/03-unity-catalog-and-the-medallion.md#what-you-type-to-make-the-three-levels-yourself-in-a-free-workspace), ai-engineering/databricks-production-deployment, starter pack page 03. Creates `dev_qa_data_analytics_ai` in the UI, then the `product_validation` schema and the `landing` Volume from the CLI, with screenshots of each level.
- [The three-level name](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/03-unity-catalog-and-the-medallion.md#the-three-level-name), the same page. `catalog.schema.table` and the three `databricks ... list` commands, whose names are positional arguments.
- [Build the hierarchy](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/34-e2-unity-catalog.md#2--build-the-hierarchy), data-engineering/many-sources-one-lakehouse, plan 34. Creates the `bronze`, `silver` and `gold` catalogs, the schema `bronze.finances` and the Volume `landing`, then proves the names resolve from SQL.
- [The territory in ASCII](/home/molef/goal-setting/learning/data-engineering/unity-catalog-grants/diagram-gate.md#the-territory-in-ascii), data-engineering/unity-catalog-grants, diagram gate. The metastore, catalog, schema and Volume as three doors, each with the privilege that opens it and the error a shut door gives.
- [Create the catalog through the Catalog explorer](/home/molef/goal-setting/learning/ai-engineering/genie-on-databricks/plans/05-b1-three-level-name.md#3--create-the-catalog-through-the-catalog-explorer), ai-engineering/genie-on-databricks, plan 05. Creates `finances.main` and explains a permission error as missing CREATE CATALOG on the metastore.
- [Find each of the five in a real workspace](/home/molef/goal-setting/learning/ai-engineering/genie-on-databricks/plans/01-a1-vocabulary.md#3--find-each-of-the-five-in-a-real-workspace), the same journey, plan 01. Separates the metastore, which decides permissions, from the SQL warehouse, which runs queries.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-03. No note in the vault covered Unity Catalog by name, alias or first line. The big book of MLOps has no back-of-book index (`read-book-indexes.py --book big-book-of-mlops` reported "no index"), so its pages come from the chapter table in `Textbooks.md`, and pages 10 to 12, 17 to 26 and 31 were read in full with pdftotext. No other shelf book names Unity Catalog; the page-text hits for "UC" were inner-product and MapReduce pages. No lecture map, video lessons row, paper, worked example or staged figure teaches it. No creator in `VIDEO_CREATORS.md` covers Databricks, so the two videos fill a topic no listed creator covers; both times are chapter starts and ends read with `cache-video-chapters.py`. Gambill's chapter is judged from its title and from the caption reading in the many-sources journey's video selection, which notes that the captions say "catalog" and never "unity catalog". The Marvelous MLOps chapter is judged from its title only, since captions were refused with HTTP 429. Both docs pages answered and were read at the passages their lines describe. Bare "catalog" and "schema" are left out as aliases because the tree uses them in other senses, and "Hive metastore" is skipped because it names the legacy metastore Unity Catalog replaces.
