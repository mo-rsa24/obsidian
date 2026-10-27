---
aliases: [dataclass, frozen dataclass, dataclasses]
standard: vault-note v2
---

# Dataclass

Up: [[Python]]

Software, Python. Its counterpart for data arriving from outside is [[Pydantic]], which validates where a dataclass trusts.

**A dataclass is a Python class whose `__init__`, `__repr__` and equality are written for you from its typed fields by the standard library's `@dataclass` decorator; with `frozen=True` its fields cannot change after it is built.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the dataclass writes the rest around it.

## Where to learn this

**Dataclass**, a class built from typed fields by `@dataclass`, with no validation. Also: dataclasses, frozen dataclass.

**Videos**

- ArjanCodes, This Is Why Python Data Classes Are Awesome, Dataclasses basics, 4:00 to 5:45: [watch](https://www.youtube.com/watch?v=CvQ7e6yUtnw&t=240s). The decorator turning a class with typed fields into a dataclass. Chapter-timed.
- ArjanCodes, This Is Why Python Data Classes Are Awesome, Freezing a dataclass, 12:43 to 14:59: [watch](https://www.youtube.com/watch?v=CvQ7e6yUtnw&t=763s). `frozen=True`, the form the clean-architecture journey requires for internal types. Chapter-timed.
- ArjanCodes, Attrs, Pydantic, or Python Data Classes?, 11:26 to 13:00: [watch](https://www.youtube.com/watch?v=zN4VCb0LbQI&t=686s). What a dataclass is good for and where it stops, set against attrs and pydantic. Chapter-timed.
- ArjanCodes, This Is Why Python Data Classes Are Awesome, (new in Python 3.10) slots, 17:00 to 21:30: [watch](https://www.youtube.com/watch?v=CvQ7e6yUtnw&t=1020s). `slots=True` and what it changes. Chapter-timed.

**Our plans and chapters**

- [A str Enum and a result dataclass](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/01-the-python-pieces.md#11-a-str-enum-and-a-result-dataclass), ai-engineering/prototype-product-data-validation-end-to-end, chapter 1.1. A check's result written as a dataclass beside an `ImageType` enum, on three sample images known by their corners.
- [Frozen dataclass versus pydantic model](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/11-dataclass-vs-pydantic.md), system-design/clean-architecture-in-python, plan 11. Internal types written as frozen slotted dataclasses, and each type sorted by whether it crosses a trust boundary.
- [Dataclasses and a str Enum](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/plans/archived/01-enum-and-dataclass.md), ai-engineering/prototype-product-data-validation-end-to-end, plan 1. The sitting that writes chapter 1.1's enum and result dataclass by hand.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No book on the shelf covers Python's dataclasses (a page-text search of the five software and system design books found none), so the card has no textbook line. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; the Attrs row is the video lessons index's section "A dataclass or a pydantic model". ByteByteGo, Hello Interview and KodeKloud have no video on it. Each plan and chapter was read at its title and description. "Dataclass" is not an ordinary English word, so it links everywhere; its 28 files in the learning tree all mean Python's dataclass.
