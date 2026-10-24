---
aliases: [pagination, paginate, paginated, cursor pagination, cursor-based pagination, offset pagination, offset-based pagination, keyset pagination, keyset-based pagination]
standard: vault-note v2
---

# Pagination

Up: [[APIs]]

Information Technology, System Design. [[Rate Limiter]] is the other guard an API puts on a large list endpoint; cursor pagination reads in the order of a [[Database Index]], which is what makes it fast.

**Pagination returns a long list in pages: offset pagination asks for "skip 20, take 10", which slows down and skips or repeats rows when rows are inserted mid-scroll, while cursor (keyset) pagination asks for "the 10 after this last key", which stays fast and stable.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches pagination writes the rest around it.

## Where to learn this

**Pagination**, returning a long list one page at a time. Also: cursor pagination, offset pagination, keyset pagination, paginated.

**Textbooks**

- System design big archive, How to Design Good APIs: [pages 380 to 381](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=380). Pagination with a concrete request, `?limit=10&offset=20`, among the habits of a well-designed API.
- System design big archive, A Cheatsheet on REST API Design Best Practices: [pages 143 to 144](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=143). Why APIs paginate (performance bottlenecks and payload bloat) and the three strategies: offset-based, cursor-based and keyset-based.
- System design big archive, Best Practices in API Design: [pages 270 to 271](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=270). Offset-based and cursor-based pagination beside sorting, filtering and versioning.

**Videos**

- PlanetScale, Pagination in MySQL - offset vs. cursor, Shifting records in offset pagination, 5:17 to 6:12: [watch](https://www.youtube.com/watch?v=zwDIN04lIpc&t=317s). The failure offset pagination has when rows move, shown on a `people` table after the chapter on limit and offset. Chapter-timed.
- ByteByteGo, API Pagination: Making Billions of Products Scrolling Possible, Cursor based pagination, 1:25 to 2:12: [watch](https://www.youtube.com/watch?v=14K_a2kKTxU&t=85s). Cursor pagination as the fix for the problems with offset, before keyset and time-based pagination. Chapter-timed.
- PlanetScale, Pagination in MySQL - offset vs. cursor, Cursor based pagination, 6:12 to 8:13: [watch](https://www.youtube.com/watch?v=zwDIN04lIpc&t=372s). Cursor pagination in SQL, followed by ordering by two columns and its drawbacks and advantages. Chapter-timed.
- Hello Interview, Elasticsearch Deep Dive, Cursors and Pagination, 16:45 to 20:36: [watch](https://www.youtube.com/watch?v=PuZvF2EyfBM&t=1005s). Paging through search results with cursors in Elasticsearch. Chapter-timed.

**Our plans and chapters**

- [System Design: API Design and Contracts](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/MASTER_PLAN.md), system-design/api-design-and-contracts. Its goal implements cursor and offset pagination on the same dataset and demonstrates the skipped and duplicated rows under concurrent writes that cursor pagination avoids; it holds goals and no plans yet.
- [API Design Conventions](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/02-api-and-traffic-control/plans/01-api-design-conventions.md), projects/tms-mobility/system-design/plans/02-api-and-traffic-control, plan 01. Pagination as one of the conventions for the backend both TMS mobile apps call, with a paginated list response.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after a page-text search for "paginat", "cursor-based" and "keyset" across the system design books. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; the PlanetScale and ByteByteGo videos are the ones the API design journey's sources already name. Hussein Nasser's dont use offset in your SQL is members-only and was skipped. Each plan was read at its title and description. Bare "offset" and "cursor" are never aliases: offset also means a Kafka offset in the learning tree, and cursor names an editor.
