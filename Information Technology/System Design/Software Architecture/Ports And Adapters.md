---
aliases: [ports and adapters, port and adapter, hexagonal architecture, hexagonal, port, adapter, inbound adapter, outbound adapter, driving adapter, driven adapter]
link-skip: ["host, port", mapped port, port 8000, wrong port]
link-only-in: [system-design/clean-architecture-in-python]
standard: vault-note v2
---

# Ports And Adapters

Up: [[Software Architecture]]

Information Technology, System Design, Software Architecture. The rule that makes the shape hold is the [[Dependency Rule]], the code that calls the ports is a [[Use Case]], and the [[Composition Root]] decides which adapter fills each port.

**Ports and adapters splits an application from the outside world: the application names each thing it needs from outside as a port (an interface in its own words), and each technology that supplies it is an adapter written against that port.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches ports and adapters writes the rest around it.

## Where to learn this

**Ports and adapters**, an application that names its needs as ports and lets each technology plug in as an adapter. Also: hexagonal architecture, port, adapter, inbound adapter, outbound adapter, driving adapter, driven adapter.

**Textbooks**

- System design big archive, How Clean Architecture Works?: [page 264](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=264). The clean architecture's interface adapters layer (controllers, presenters and gateways) converting data between the web, the database and the use cases, which is the same seam in that book's vocabulary.

**Videos**

- ArjanCodes, Stop Mixing FastAPI with Business Logic: Fix It with Ports & Adapters, Step 3: Define the Port, 12:54 to 14:39: [watch](https://www.youtube.com/watch?v=FXwBWS4qDAA&t=774s). The port written as what the domain needs, in Python over FastAPI. Chapter-timed.
- ArjanCodes, Stop Mixing FastAPI with Business Logic: Fix It with Ports & Adapters, Step 5: Create SQLAlchemy Adapter Implementing the Port, 19:25 to 24:36: [watch](https://www.youtube.com/watch?v=FXwBWS4qDAA&t=1165s). The outbound adapter that satisfies that port with SQLAlchemy. Chapter-timed.
- ArjanCodes, Stop Mixing FastAPI with Business Logic: Fix It with Ports & Adapters, Ports & Adapters in One Minute, 3:11 to 4:25: [watch](https://www.youtube.com/watch?v=FXwBWS4qDAA&t=191s). The whole idea in one minute, before the build. Chapter-timed.
- Valentina (Cupać) Jemuović, Hexagonal Architecture, Episode 2: Ports & Adapters, 0:00 to 1:23:31: [watch](https://www.youtube.com/watch?v=bw7So5GMkyg&t=0s). The reasoning behind the shape, with the thesis that hexagonal architecture prescribes dependency inversion rather than layers. Whole video.

**Our plans and chapters**

- [Port and adapter](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/14-port-and-adapter.md), system-design/clean-architecture-in-python, plan 14. The database call pulled out of a tangled function into `ForReadingPayeeHistory` in the application layer and `PostgresPayeeHistory` in infrastructure, the adapter not inheriting from the port.
- [The ports on paper and the context diagram](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/02-design-before-code.md#23-the-ports-on-paper-and-the-context-diagram), ai-engineering/prototype-product-data-validation-end-to-end, chapter 2.3. Five outgoing arrows on a context diagram become four ports named with Cockburn's "For" convention, two input files sharing one port because they serve one need.
- [Three layers and ports as Protocols](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/03-the-project-and-the-hexagon.md#33-three-layers-and-ports-as-protocols), ai-engineering/prototype-product-data-validation-end-to-end, chapter 3.3. Four collaborators become `Protocol` ports; with the image server stopped, a fetch port and a fake still give 3 of 3 results where the direct `urllib` call gives 0.
- [The CLI as a driving adapter](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/03-the-project-and-the-hexagon.md#35-the-cli-as-a-driving-adapter), ai-engineering/prototype-product-data-validation-end-to-end, chapter 3.5. The inbound side: a command line that turns arguments into a call and results into output and an exit code.
- [Trace one request](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/22-trace-one-request.md), system-design/clean-architecture-in-python, plan 22. One request followed with the debugger from the route handler through the port into the adapter and back.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The textbook page was read with pdftotext after a page-text search of the five software and system design books for "hexagonal", "ports and adapters" and "adapter"; none has a back-of-book entry for the idea, and the big archive's only "hexagonal" (page 101) is a one-word mention in a list. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title, the video title and the journey's own transcript scoring in the agent-architecture video selection of 2026-09-07. The Jemuović video has no chapter list, so it is cited whole. ByteByteGo, Hello Interview and KodeKloud have no video on the idea (their upload lists, cached under `~/.claude/cache/video-chapters/_channels/`, were searched by title). Each plan and chapter was read at its title, description and its lines on ports. Bare "port" and "adapter" mean a network port or a LoRA adapter across most of the learning tree (377 and 133 files), so the single words link only inside clean-architecture-in-python; inside it, four lines in plans 05 and 06 use "port" for a network port and are listed under `link-skip`.
