---
aliases: [structural typing, nominal typing, typing.Protocol, Protocol, protocol class, structural subtyping, static duck typing]
link-only-in: [system-design/clean-architecture-in-python]
standard: vault-note v2
---

# Structural Typing

Up: [[Python]]

Software, Python. A `Protocol` is how a port in [[Ports And Adapters]] is written in Python, and a [[Test Double]] satisfies it the same way the real adapter does.

**Structural typing decides whether a class fits a type by the methods it has, so in Python any class with the right methods satisfies a `typing.Protocol` without naming it; nominal typing, as with an abstract base class, fits only a class that declares the parent by inheriting from it.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches structural typing writes the rest around it.

## Where to learn this

**Structural typing**, a class fits a type by having its methods, with no inheritance. Also: nominal typing, `typing.Protocol`, Protocol, protocol class, structural subtyping, static duck typing.

**Videos**

- ArjanCodes, Protocols vs ABCs in Python, 5:39 to 9:21: [watch](https://www.youtube.com/watch?v=dryNwWvSd4M&t=339s). A Protocol worked in code: any class with the right methods fits, with no inheritance. Chapter-timed.
- ArjanCodes, Protocols vs ABCs in Python, 1:53 to 5:39: [watch](https://www.youtube.com/watch?v=dryNwWvSd4M&t=113s). The nominal side first: an abstract base class, where the subclass must name its parent. Chapter-timed.
- ArjanCodes, Protocols vs ABCs in Python, 9:21 to 12:45: [watch](https://www.youtube.com/watch?v=dryNwWvSd4M&t=561s). `runtime_checkable` and the other ways a Protocol is made stricter. Chapter-timed.

**Our plans and chapters**

- [Writing a Protocol](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/10-writing-a-protocol.md), system-design/clean-architecture-in-python, plan 10. A first port as a Protocol with an async method, a class that satisfies it without inheriting, and mypy catching a mismatch introduced on purpose.
- [Structural versus nominal typing](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/09-structural-vs-nominal-typing.md), system-design/clean-architecture-in-python, plan 9. Why a class can satisfy an interface it has never heard of, and why the XBL standard bans adapters inheriting from their Protocol.
- [Three layers and ports as Protocols](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/03-the-project-and-the-hexagon.md#33-three-layers-and-ports-as-protocols), ai-engineering/prototype-product-data-validation-end-to-end, chapter 3.3. Four collaborators each given a `Protocol` class, filled by real adapters and by fakes alike.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No book on the shelf teaches Python's typing (a page-text search of the five software and system design books found no "structural typing", "duck typing" or Protocol class), so the card has no textbook line. The three video rows are the video lessons index's section "Protocols against abstract base classes", placed by the journey's video pulse of 2026-10-24; ByteByteGo, Hello Interview, KodeKloud and freeCodeCamp have no video on it. Each plan and chapter was read at its title and description. Bare "protocol" means a network or HTTP protocol across most of the learning tree (230 files), so the single word links only inside clean-architecture-in-python, where all 52 lines using it mean the Protocol class.
