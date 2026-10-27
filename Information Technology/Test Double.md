---
aliases: [test double, fake, in-memory fake, hand-built fake, fake adapter]
link-only-in: [system-design/clean-architecture-in-python, product-data-validation-end-to-end, ai-engineering/agent-architecture, system-design/foundations]
standard: vault-note v2
---

# Test Double

Up: [[Information Technology]]

Information Technology. In this vault it is met as the fake that stands in for an adapter in [[Ports And Adapters]], so a [[Use Case]] can be tested with no database. The placement is unsure: it belongs either in a software testing family under Information Technology, which does not exist yet, or beside [[Ports And Adapters]] in Software Architecture.

**A test double is any object that stands in for a real dependency during a test: a fake really works but holds its data in memory, a stub returns fixed answers, and a mock records how it was called so the test can check the calls.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches test doubles writes the rest around it.

## Where to learn this

**Test double**, a stand-in for a real dependency in a test: a fake, a stub or a mock. Also: fake, in-memory fake, hand-built fake, fake adapter.

**Textbooks**

- Systems analysis and design, chapter 12, Testing, test planning: [page 477](../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=477). Stubs as placeholders for unfinished modules that return a hardcoded value or show a message, so the modules around them can be tested, worked on a main menu whose five functions are each stubbed.

**Videos**

- The Theory Of Code, Unit Tests and Test Doubles like Mocks, Stubs & Fakes, Test Doubles, 8:30 to 10:49: [watch](https://www.youtube.com/watch?v=NPp2pvhGbkM&t=510s). What a test double is, before the chapters on each kind. Chapter-timed.
- The Theory Of Code, Unit Tests and Test Doubles like Mocks, Stubs & Fakes, Mocks: Mocks replaces external interface, 10:49 to 13:37: [watch](https://www.youtube.com/watch?v=NPp2pvhGbkM&t=649s). Mocks replacing an external interface. Chapter-timed.
- The Theory Of Code, Unit Tests and Test Doubles like Mocks, Stubs & Fakes, STUBS: Generates Predefined Outputs, 13:37 to 17:19: [watch](https://www.youtube.com/watch?v=NPp2pvhGbkM&t=817s). Stubs returning predefined outputs. Chapter-timed.
- Keploy, Stubs vs Mocks vs Fake: In a nutshell, 0:00 to 3:08: [watch](https://www.youtube.com/watch?v=4AxXWjBSIdY&t=0s). The three kinds set side by side in three minutes. Whole video.
- Valentina (Cupać) Jemuović, Hexagonal Architecture, Episode 2: Ports & Adapters, 0:00 to 1:23:31: [watch](https://www.youtube.com/watch?v=bw7So5GMkyg&t=0s). Test doubles in a hexagonal application, with the argument for hand-built fakes over a mocking library from about 36:07. Whole video.

**Our plans and chapters**

- [A fake that satisfies a port](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/16-a-fake-that-satisfies-a-port.md), system-design/clean-architecture-in-python, plan 16. `InMemoryPayeeHistory` holding a dict, satisfying the port without inheriting from it, then the same test written again with `unittest.mock.AsyncMock` to compare.
- [The fake reader](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/textbook/06-the-rules-engine.md#62-the-fake-reader), ai-engineering/product-data-validation-end-to-end, chapter 6.2. A fake as a second real implementation of the same `Protocol`, set against a mock, which records calls and asserts about them.
- [Application tests with no database](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/17-application-tests-with-no-database.md), system-design/clean-architecture-in-python, plan 17. The use case tested against fakes only, green in under five seconds with Postgres stopped.
- [Three layers and ports as Protocols](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/03-the-project-and-the-hexagon.md#33-three-layers-and-ports-as-protocols), ai-engineering/prototype-product-data-validation-end-to-end, chapter 3.3. A fake fetch port reading image files from disk gives 3 of 3 results with no server started.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The textbook page came from Systems analysis and design's back-of-book index ("Stubs") and was read with pdftotext; no shelf book names test doubles, fakes or mocks. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title, the video title and, for Jemuović, the journey's transcript scoring in the agent-architecture video selection of 2026-09-07. ByteByteGo, Hello Interview and KodeKloud have no video on test doubles (one ByteByteGo chapter on writing testable code was read and judged too general by the journey's video pulse). The two other creators were found by one search of YouTube's listing. Each plan and chapter was read at its title, description and its lines on fakes. Bare "fake" appears on 353 lines outside this journey. In the two product-data-validation journeys, agent-architecture and foundations (about 300 lines) it means a stand-in implementation, a fake reader, a fake judge or a fake payment provider, so the word links in those folders and in clean-architecture-in-python. Elsewhere it means a fake quantizer (model-compression, 22 lines) or the verb ("fake a spend"), and stays plain. "Stub" was not added because it mostly means a gRPC client stub.
