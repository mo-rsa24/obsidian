---
aliases: [API versioning, versioned API, breaking change, URL versioning, header versioning]
standard: vault-note v2
---

# API Versioning

Up: [[APIs]]

Information Technology, System Design. A [[REST API]] usually carries its version in the URL path, and an [[API Gateway]] can route each version to its own backend.

**API versioning lets an API change without breaking the clients already calling it: a breaking change goes out under a new version (in the URL, such as `/v2/orders`, or in a header) while the old version keeps answering until its clients have moved.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches API versioning writes the rest around it.

## Where to learn this

**API versioning**, changing an API without breaking its callers. Also: versioned API, breaking change, URL versioning, header versioning.

**Textbooks**

- System design big archive, What do version numbers mean?: [pages 128 to 129](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=128). Works semantic versioning with numbers: MAJOR goes up for an incompatible API change, MINOR for a backward-compatible feature, PATCH for a fix, walked from 0.1.0 to 1.0.0, then 1.0.1, 1.1.0 and 2.0.0.
- System design big archive, Best Practices in API Design: [pages 270 to 271](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=270). Versioning among eight practices, as the way to change endpoints while keeping backward compatibility.
- System design big archive, The 5 Pillars of API Design: [pages 168 to 169](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=168). Versioning as one of five things to settle when designing an API, beside the interface, the paradigm, relationships and rate limiting.

**Videos**

- ByteByteGo, Good APIs Vs Bad APIs: 7 Tips for API Design, Add Versioning, 1:51 to 2:24: [watch](https://www.youtube.com/watch?v=_gQaygjm_hg&t=111s). Versioning as one tip for a good API, between reliability and pagination. Chapter-timed.
- Ambient Coder, Web API: Explicit Versioning, URI vs Headers vs Request Params, SemVer, Sunset Headers, URI Components, 2:12 to 3:22: [watch](https://www.youtube.com/watch?v=Yv_B0dniVhI&t=132s). The version carried in the URL, after a chapter on what explicit versioning is. Chapter-timed.
- Ambient Coder, Web API: Explicit Versioning, URI vs Headers vs Request Params, SemVer, Sunset Headers, HTTP Headers, 3:22 to 4:10: [watch](https://www.youtube.com/watch?v=Yv_B0dniVhI&t=202s). The version carried in a header, before request parameters, SemVer and sunset headers for deprecation. Chapter-timed.
- Neural Bytes, API Versioning in System Design: Complete Beginner to Advanced Guide, 0:00 to 31:56: [watch](https://www.youtube.com/watch?v=xRXXBgp3jRg&t=0s). A full guide to API versioning from first principles to the advanced cases. Whole video.

**Our plans and chapters**

- [System Design: API Design and Contracts](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/MASTER_PLAN.md), system-design/api-design-and-contracts. Versioning, backward compatibility and deprecation as one objective, with a goal to build URL versioning and header versioning for the same endpoint, each carrying a backward-compatible change; it holds goals and no plans yet.
- [API Design Conventions](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/02-api-and-traffic-control/plans/01-api-design-conventions.md), projects/tms-mobility/system-design/plans/02-api-and-traffic-control, plan 01. A versioned URL as one convention for the backend two mobile apps call, then an unversioned endpoint fixed into a versioned one.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the chapter tables in `Textbooks.md` and a page-text search for "versioning" and "breaking change" across the four system design books; System design interview's versioning pages (96 to 97) version data in a key-value store, a different idea. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Ambient Coder and Neural Bytes are not on the creator list: none of the listed creators has more than a short chapter on versioning, and the API design journey's own video index already chose these two. Each plan was read at its title, description and its lines on versioning. Left out: the big archive's What are some of the most popular versioning strategies? (page 293), on release numbering (SemVer and CalVer) with nothing on APIs. The bare word "versioning" is not an alias: of 25 random lines in the learning tree, about 10 mean API versioning and the rest mean data versioning with DVC, prompt and model versioning or release numbers. "Breaking change" is used 10 times, each for a change that breaks existing callers (5 in API versioning sources, 4 for a MAJOR release in SemVer, 1 for a library release), so it is an alias.
