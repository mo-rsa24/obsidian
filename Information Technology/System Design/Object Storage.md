---
aliases: [object storage, object store, blob storage, blob store, S3, Amazon S3, S3 bucket]
link-skip: [Waits on F5, "S3, C8", sitting (S3), S3 in the quiz, taxable-income-assembly]
standard: vault-note v2
---

# Object Storage

Up: [[System Design]]

Information Technology, System Design. A [[Content Delivery Network]] usually serves the files an object store holds, while the files' metadata lives in a [[Relational Database]].

**Object storage keeps whole files (images, videos, PDFs) as objects in flat buckets, each reached by a key over HTTP, and copies every object across machines so it survives disk and server failures; Amazon S3 is the standard example, and MinIO and Azure Blob Storage speak the same idea.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches object storage writes the rest around it.

## Where to learn this

**Object storage**, files kept as objects in buckets behind an HTTP API. Also: blob storage, object store, S3, Amazon S3.

**Textbooks**

- System design interview, chapter 15, Design Google Drive: [pages 250 to 251](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=250). Works the move from one server's disk to Amazon S3: files stored in S3, replicated within a region and across regions so a lost region loses nothing, and a bucket described as a folder.
- System design big archive, How Amazon S3 Works?: [pages 106 to 107](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=106). Inside S3: over 350 trillion objects at eleven nines of durability, each object given a unique identifier and metadata, front-end, indexing, placement and durability services, and erasure coding with replication across availability zones.
- System design interview, chapter 14, Design YouTube: [pages 223 to 224](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=223). Blob storage holding the original uploaded videos, a cloud service the design uses instead of building, with the definition of a binary large object.
- System design big archive, How to Design a System like Instagram: [pages 89 to 90](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=89). Images and videos go to object storage while their metadata goes to the database.

**Videos**

- Hello Interview, Object Storage in System Design Interviews, Why Object Storage, 0:00 to 3:29: [watch](https://www.youtube.com/watch?v=RvaMHMxHjp4&t=0s). Why a design reaches for object storage, before chapters on how it works and what to know for an interview. Chapter-timed.
- Hello Interview, Object Storage in System Design Interviews, How it works, 3:29 to 7:00: [watch](https://www.youtube.com/watch?v=RvaMHMxHjp4&t=209s). How an object store works underneath. Chapter-timed.
- Hayk Simonyan, Object Storage (BLOBs) Explained for System Design, 0:00 to 3:55: [watch](https://www.youtube.com/watch?v=dEcQK4-pqiw&t=0s). Object storage for binary large objects in under four minutes. Whole video.

**Our plans and chapters**

- [MinIO holds the receipt](/home/molef/goal-setting/learning/system-design/foundations/plans/18-minio-holds-the-receipt.md), system-design/foundations, plan 18. Works it on the corner shop: a paid order's receipt PDF written by the notification service into a `receipts` bucket in MinIO, standing in for S3.
- [The blob trigger and a local Azure Function](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/plans/30-blob-trigger-and-function.md), ai-engineering/product-data-validation-end-to-end, plan 30. An Azure Function on your own machine triggered by a blob arriving in the `product-images` container.
- [How AWS S3 Works: staged, pre-journey](/home/molef/goal-setting/learning/system-design/applications/how-aws-s3-works/README.md), system-design/applications/how-aws-s3-works. A nine-panel S3 infographic read panel by panel, staged before it becomes a journey.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the chapter tables in `Textbooks.md` and a page-text search for "object storage", "blob storage" and "S3" across the system design books. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. ByteByteGo's 10+ Key Memory & Storage Systems covers RAM, disks and portable storage, not object storage, so it has no line. Each plan was read at its title and description; the compiled chapter for foundations plan 18 has headings and no text yet. "S3" (111 uses in the learning tree) means Amazon S3 in most lines; the `link-skip` phrases cover the few where S3 labels a step or a quiz question in the diffusion, transformer and statistics journeys. Bare "bucket" (202 uses) is never an alias: it also means a rate limiter's token bucket and the buckets of a merge.
