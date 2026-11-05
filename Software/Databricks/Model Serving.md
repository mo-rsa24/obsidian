---
aliases: [Databricks Model Serving, Model Serving endpoint, Model Serving endpoints, model serving endpoint, model serving endpoints, serving endpoint, serving endpoints]
link-skip-in: [ai-engineering/foundations]
link-scope-words: [Model Serving]
standard: vault-note v2
---

# Model Serving

Up: [[Databricks]]

Software, Databricks. Needs: [[Unity Catalog]]. It is what the product validation agent calls through [[XBL_MODEL_ENDPOINT]], and where a registered model version picked by its [[Model Alias]] is put behind a REST address.

**Databricks Model Serving deploys a model as a serving endpoint: one stable name with a REST `invocations` address, behind which sit one or more served entities (registered model versions, each with its own scaling), with a traffic percentage per entity.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that stands up an endpoint writes the rest around it.

## Where to learn this

**Model Serving**, Databricks' serverless way to put a model behind a REST endpoint. Also: Databricks Model Serving, serving endpoint, model serving endpoint.

**Textbooks**

- The big book of MLOps, chapter 5, Model deployment and Model Serving: [pages 47 to 48](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=47). Works the deploy step through: find the "Champion" model version, update the existing endpoint to serve it with a zero-downtime update or create one if none exists, and split one endpoint's traffic between two models for a Champion against Challenger comparison.
- The big book of MLOps, chapter 4, Model Serving: [pages 27 to 30](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=27). What a real-time deployment adds: readiness checks and load tests (median and 95th or 99th percentile latency, queries per second), then A/B testing, gradual rollout and shadow deployment, implemented by splitting one endpoint's traffic between two model versions.
- The big book of MLOps, chapter 3, Model Serving: [pages 13 to 14](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=13). Model Serving builds a container from a logged MLflow model and deploys it as a REST endpoint, logs requests and responses to inference tables in Unity Catalog, quotes p50 overhead latency under 10 ms and over 25,000 queries per second, and scales down to zero.
- The big book of MLOps, chapter 5, Integration tests: [page 41](../../Mathematics/references/textbooks/ai-engineering/big-book-of-mlops.pdf#page=41). Creates a temporary endpoint in staging, loads a test model and tests it before the code reaches production.

**Videos**

- Marvelous MLOps, Lecture 6, Deploying a model serving endpoint, Deploying a serving endpoint, 5:07 to 12:53: [watch](https://www.youtube.com/watch?v=Rt8qtjskuSs&t=307s). Deploys a model to a serving endpoint, after a chapter on concepts and limitations. Chapter-timed.
- Marvelous MLOps, the same lecture, AB testing implementation, 12:53 to 21:47: [watch](https://www.youtube.com/watch?v=Rt8qtjskuSs&t=773s). An A/B test between two models on one endpoint, the traffic split chapter 4 of the book describes. Chapter-timed.
- Praveen Reddy Learnings, Explained Model Serving, Creating an endpoint via UI, 1:34 to 4:46: [watch](https://www.youtube.com/watch?v=N1t9Hq-2AZU&t=94s). Creates an endpoint for a custom model from the Serving page; later chapters query it and open its inference table. Chapter-timed.

**Official docs**

- [Deploy models using Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/), Databricks documentation. Model Serving as one interface to deploy, govern and query models for real-time and batch inference, with each served model available as a REST API.
- [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints), Databricks documentation. The `POST /api/2.0/serving-endpoints` body: `served_entities` with `entity_name` (`catalog.schema.model`), `entity_version` and `scale_to_zero_enabled`, and `traffic_config.routes` with a `traffic_percentage` per served entity, plus the warning that scale to zero is not recommended in production.

**Our plans and chapters**

- [Model Serving, at the reading level](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/05-mlflow-and-model-serving.md#model-serving-at-the-reading-level), ai-engineering/databricks-production-deployment, starter pack page 05. Picture 05 taken apart: the endpoint `product-validator`, two served entities v2 and v3 under a 90/10 traffic split, and `scale_to_zero_enabled: true`.
- [See the model endpoints yourself, in the free workspace](/home/molef/goal-setting/learning/ai-engineering/databricks-production-deployment/sources/starter-pack/05-mlflow-and-model-serving.md#see-the-model-endpoints-yourself-in-the-free-workspace), the same page. The Serving page's table of 12 Ready endpoints, `databricks serving-endpoints list` and `get`, and which endpoints read an image.
- [The endpoint called with curl](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/06-the-model-and-the-agent.md#61-the-endpoint-called-with-curl), ai-engineering/prototype-product-data-validation-end-to-end, chapter 6.1. One POST to `/serving-endpoints/databricks-llama-4-maverick/invocations` with a bearer token, expecting status 200 and `OK` at `choices[0].message.content`, and the 401 when the header is left out.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-11-03. No note in the vault covered Model Serving; [[XBL_MODEL_ENDPOINT]] is an environment variable note that only cites the Model Serving docs. The big book of MLOps has no back-of-book index, so its pages come from the chapter table in `Textbooks.md`, and pages 13 to 14, 27 to 30, 41 and 46 to 48 were read in full with pdftotext. No other shelf book names Model Serving. No lecture map, video lessons row, paper or worked example teaches it. `find-figures.py` returned one figure, the AI engineering roadmap in ai-engineering/foundations, which names model serving in general as a branch, so it is left out, and `link-skip-in` keeps "Model Serving" plain in that journey. No creator in `VIDEO_CREATORS.md` covers Databricks, so the three videos fill a topic no listed creator covers; each time is a chapter start and end read with `cache-video-chapters.py`, and the content is judged from the chapter titles, since captions were refused with HTTP 429. Both docs pages answered and were read at the passages their lines describe. Bare "serving" is left out as an alias because it has other senses.
