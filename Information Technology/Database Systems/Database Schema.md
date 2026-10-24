---
aliases: [database schema, table schema, schema design, schema migration, database migration, schema, migration, DDL]
link-only-in: [system-design, projects/attica, projects/tms-mobility, data-engineering, ai-engineering/one-business-end-to-end, ai-engineering/data-agents, ai-engineering/product-data-validation-end-to-end]
link-skip: ["catalog, schema, table", three-level name, JSON schema, tool schema, Pydantic schema, result schema, label schema, label-schema]
link-skip-in: [system-design/api-design-and-contracts/]
standard: vault-note v2
---

# Database Schema

Up: [[Database Systems]]

Information Technology, Database Systems. [[Database Normalization]] decides which tables a schema has, [[Foreign Key]] constraints tie them together, and an [[Object-Relational Mapping]] writes the schema's migrations from model classes.

**A database schema is the declared shape of a database: its tables, each column's name and type, the keys and the constraints, written as DDL (`CREATE TABLE`); a schema migration is a versioned script that changes that shape, such as adding a column, without losing the rows already stored.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches schemas writes the rest around it.

## Where to learn this

**Database schema**, the tables, columns, types and constraints a database declares. Also: table schema, schema design, schema migration, DDL.

**Textbooks**

- Database systems textbook, section 7-2, Data definition commands: [pages 277 to 282](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=277). A schema as a logical group of tables and indexes created with `CREATE SCHEMA AUTHORIZATION JONES`, then the data types and the `CREATE TABLE` statements for VENDOR and PRODUCT with their primary and foreign keys.
- Database systems textbook, section 7-5, Additional data definition commands: [pages 309 to 316](../../Mathematics/references/textbooks/database-systems/database-systems-textbook.pdf#page=309). Changing a schema after it exists: `ALTER TABLE` with ADD, MODIFY and DROP for columns and constraints, adding primary and foreign key designations, and `DROP TABLE`.
- System design interview, chapter 15, Metadata database: [pages 256 to 257](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=256). Works a real schema: Google Drive's metadata tables (user, device, namespace, file, file version and block), what each holds, and why file version rows are read-only.
- Systems analysis and design, chapter 11, Moving from logical to physical data models: [pages 445 to 447](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=445). The steps that turn a diagram into a schema: entities to tables, attributes to typed fields (`CHAR(10)` with a default and a validation rule), then primary keys and foreign keys.
- Grokking the system design interview, section 16.3, Differences: SQL vs. NoSQL: [page 20](../../Mathematics/references/textbooks/system-design/grokking-the-system-design-interview.pdf#page=20). A relational schema is fixed before data goes in and costly to change, against the dynamic schema of a NoSQL store.
- System design interview, chapter 3, A framework for system design interviews: [page 44](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=44). When a design interview should go down to the database schema and when that is too low a level.

**Videos**

- Hello Interview, Data Modeling in System Design Interviews, Entities, Keys, & Relationships, 17:14 to 21:31: [watch](https://www.youtube.com/watch?v=TUcPS6dsWx4&t=1034s). Laying out the entities, their keys and the relationships between them, after a guided practice problem. Chapter-timed.
- BugBytes, Django ORM Deep Dive - Models, Migrations and Admin UI Integration, Migrations in Django to apply database changes, 11:11 to 15:31: [watch](https://www.youtube.com/watch?v=t7diJPGxCGo&t=671s). Django migrations applying model changes to the database schema. Chapter-timed.
- Arpit Bhayani, How Stripe Migrates Millions of Records and Schema with Zero Downtime and No Data Inconsistency, Online data migration, 0:00 to 2:40: [watch](https://www.youtube.com/watch?v=FtJPvgMsn-Q&t=0s). Changing a schema under live traffic, before the Stripe case study and its backfill, read-path and write-path steps. Chapter-timed.

**Our plans and chapters**

- [The DDL written and run, with CHECK constraints encoding the three kinds of till row](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/06-the-ddl-written-and-run.md), ai-engineering/one-business-end-to-end, plan 06. Works it on the shop: `CREATE TABLE` for ten tables from your own diagram, run into an empty database, and two `CHECK` constraints made to fail on purpose.
- [A model and a migration against PostgreSQL](/home/molef/goal-setting/learning/system-design/foundations/textbook/06-django-refresher.md#61-a-model-and-a-migration-against-postgresql), system-design/foundations, chapter 6, section 6.1. A Django model as a table described in Python, `makemigrations` writing the change down and `migrate` applying it.
- [Migrations: makemigrations, migrate, the file read, one change round-tripped](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/14-migrations.md), ai-engineering/one-business-end-to-end, plan 14. The first migration read operation by operation against your DDL, then one column added, migrated, removed and migrated back.
- [The rename that breaks a canary, and the two-step migration](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/23-the-rename-that-breaks-a-canary.md), system-design/devops-and-deployment, plan 23. A column rename that breaks whichever app version does not match the schema, and the expand-then-contract migration that avoids it.
- [Database Schema Design](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/00-requirements-and-foundations/plans/05-database-schema-design.md), projects/tms-mobility/system-design/plans/00-requirements-and-foundations, plan 05. Entities, keys, relationships and normalization for TMS's operator, booking and coupon data.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "schema" and "database schema" across the system design books; Systems analysis and design's "migration plan" index entries are about moving people to a new system, a different idea, and have no line. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title and description, and the chapter section at its first lines; the chapter for devops-and-deployment plan 23 has headings and no text yet. Bare "schema" was sampled in the learning tree (639 lines read by keyword: about 450 a database schema, about 80 a tool, JSON or result schema in the agent journeys and 38 Unity Catalog's `catalog.schema.table` namespace), so `link-only-in` limits "schema" and "migration" (131 uses, every sampled line a schema migration) to the journeys that build databases, and `link-skip` covers the Unity Catalog and tool-schema lines inside them. "DDL" (200 uses) always means the schema's SQL. The Database systems textbook lines were opened on 2026-10-25: each page was read with pdftotext after the book's back-of-book index ("schema", "CREATE SCHEMA command") and its chapter table.
