---
aliases: [model aliases, registered model alias, registered model aliases, MLflow model alias, MLflow model aliases, champion alias, challenger alias, Champion and Challenger aliases]
standard: vault-note v2
---

# Model Alias

Up: [[Databricks]]

Software, Databricks. Needs: [[Unity Catalog]]. It is how a job or a [[Model Serving]] endpoint asks for "the production version" of a registered model by name, as the product validation model's `@prod` alias does, so promoting a new version needs no change to the caller.

**A model alias is a mutable, named reference to one version of an MLflow registered model in Unity Catalog, such as `Champion` on version 1 of `prod.ml_team.iris_model`; a caller loads `models:/<catalog>.<schema>.<model>@Champion`, and moving the alias to another version changes what every caller gets. Aliases replace the stages of the older Workspace Model Registry, which Unity Catalog models do not support.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that registers a model writes the rest around it.

## Where to learn this

**Model alias**, a movable name on one version of a registered model, such as Champion or Challenger. Also: registered model alias, champion alias, challenger alias, MLflow model alias.

**Textbooks**

- The big book of MLOps, chapter 5, Model validation and Model deployment: [pages 45 to 47](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=45). Works the whole promotion through: a version that passes validation gets the "Challenger" alias, it is compared offline or online with the "Champion", and either it takes the "Champion" alias or the old one keeps it; the first deployment, with no Champion yet, compares against a business baseline.
- The big book of MLOps, chapter 4, Concepts: [page 20](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=20). Defines registered model, model version and model alias side by side, with the load URIs `models:/<catalog>.<schema>.<model>/<model_version>` and `models:/<catalog>.<schema>.<model>@Champion`.
- The big book of MLOps, chapter 5, Model validation and deployment development: [pages 37 to 38](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=37). The validation task attaches "Challenger" after its checks pass, and the deployment task promotes Challenger to Champion with an alias update.
- The big book of MLOps, chapter 5, Inference: batch or streaming: [page 48](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=48). The inference pipeline loads the model by its "Champion" alias, so it picks up a newly promoted version on its next run, which decouples deployment from inference.
- The big book of MLOps, chapter 3, Models in Unity Catalog: [page 12](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=12). The alias as a mutable, named reference that marks a version for deployment, with inference targeting "Champion" on `fraud_clf`.
- The big book of MLOps, chapter 5, Reference architecture: [page 31](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=31). A side note that Champion and Challenger are a naming convention, and a team may name its aliases to fit its own terms.

**Official docs**

- [Manage model lifecycle in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/), Databricks documentation, the section "Use model aliases". Sets an alias with `client.set_registered_model_alias("prod.ml_team.iris_model", "Champion", 1)` or **Add alias** in the UI, loads `models:/prod.ml_team.iris_model@Champion`, and states that stages are not supported for models in Unity Catalog.

**Our plans and chapters**

- [Tracking and the Registry, in this tool's own terms](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/05-mlflow-and-model-serving.md#tracking-and-the-registry-in-this-tools-own-terms), ai-engineering/databricks-production-deployment, starter pack page 05. The product validation logic wrapped as one pyfunc model, registered under a name in Unity Catalog, with an `@prod` alias so a caller asks for the production version by name instead of by run id.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-03. No note in the vault covered model aliases. The big book of MLOps has no back-of-book index, so its pages come from the chapter table in `Textbooks.md` and a page-text search for "alias", and pages 12, 20, 31, 33, 37 to 38 and 45 to 48 were read in full with pdftotext. The book never names stages; it says Models in Unity Catalog replace the classic Workspace Model Registry (page 11), and the stages statement comes from the docs page. No other shelf book, lecture map, video lessons row, paper, worked example or staged figure teaches aliases. No creator in `VIDEO_CREATORS.md` covers Databricks, and no video found by an open search has a chapter whose title names aliases: Marvelous MLOps lecture 4's chapter "Registering models", 15:43 to 17:17, may set one, but its captions were refused with HTTP 429, so there is no video line. The docs page answered and was read at its alias sections. The one plan in the learning tree that teaches an alias is starter pack page 05. "Registered model" and "model registry in Unity Catalog" are left out as aliases because each names a different object: the book's page 20 defines the registered model, its versions and the alias as three things, and the registry is the store that holds all of them.
