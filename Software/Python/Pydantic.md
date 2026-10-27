---
aliases: [pydantic, Pydantic v2, pydantic model, BaseModel, response model, request model]
link-skip: [actual response model, "endpoint, response model"]
standard: vault-note v2
---

# Pydantic

Up: [[Python]]

Software, Python. Where a [[Dataclass]] holds trusted values inside the application, a pydantic model checks untrusted ones at its edge.

**Pydantic is a Python library whose models check and convert data as it is built, so a request body, a settings file or an API response with a wrong or missing field is refused with a message naming the field instead of travelling on into the program.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches pydantic writes the rest around it.

## Where to learn this

**Pydantic**, models that validate data at the edge of a program. Also: Pydantic v2, pydantic model, `BaseModel`, request model, response model.

**Videos**

- ArjanCodes, Why Python Needs Pydantic for Real Applications, Using Pydantic for Data Validation, 2:29 to 5:39: [watch](https://www.youtube.com/watch?v=502XOB0u8OY&t=149s). A model built and fed bad data in code, in the updated Pydantic v2 tutorial. Chapter-timed.
- ArjanCodes, Why Python Needs Pydantic for Real Applications, Field validation, 5:39 to 7:45: [watch](https://www.youtube.com/watch?v=502XOB0u8OY&t=339s). Validators on single fields. Chapter-timed.
- ArjanCodes, Why Python Needs Pydantic for Real Applications, FastAPI Integration, 11:28 to 13:21: [watch](https://www.youtube.com/watch?v=502XOB0u8OY&t=688s). Pydantic models as a FastAPI endpoint's request and response. Chapter-timed.
- ArjanCodes, Attrs, Pydantic, or Python Data Classes?, 14:14 to 15:58: [watch](https://www.youtube.com/watch?v=zN4VCb0LbQI&t=854s). What pydantic adds over a dataclass and what it costs. Chapter-timed.

**Our plans and chapters**

- [pydantic v2 on a boundary](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/12-pydantic-on-a-boundary.md), system-design/clean-architecture-in-python, plan 12. Request and response models on one endpoint, a discriminated union covering the match and no-match shapes, and a 422 caused on purpose with a bad body.
- [Frozen dataclass versus pydantic model](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/11-dataclass-vs-pydantic.md), system-design/clean-architecture-in-python, plan 11. Each type sorted by whether it crosses a trust boundary, which decides pydantic model or frozen dataclass.
- [One async route with a Pydantic body](/home/molef/goal-setting/learning/system-design/foundations/textbook/05-fastapi-refresher.md#51-one-async-route-with-a-pydantic-body), system-design/foundations, chapter 5.1. FastAPI validates a Pydantic body before the function runs, and a bad body gets a 422 with the reason.
- [Settings read once, and refused when unknown](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/03-the-project-and-the-hexagon.md#34-settings-read-once-and-refused-when-unknown), ai-engineering/prototype-product-data-validation-end-to-end, chapter 3.4. Pydantic `BaseSettings` with `extra="forbid"`, tested on whether a mistyped `XBL_` variable is really refused.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No book on the shelf covers pydantic (a page-text search of the five software and system design books found it nowhere), so the card has no textbook line. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; the last row is the video lessons index's section "A dataclass or a pydantic model". ByteByteGo, Hello Interview and KodeKloud have no video on it. Each plan and chapter was read at its title and description. "Pydantic" is not an ordinary English word, so it links everywhere. "Response model" also names an embedding endpoint's model in two prototype-pdv lines (the encoder manifest), which are listed under `link-skip`.
