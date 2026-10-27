---
aliases: [composition root]
standard: vault-note v2
---

# Composition Root

Up: [[Software Architecture]]

Information Technology, System Design, Software Architecture. It is where each port in [[Ports And Adapters]] gets its adapter and each [[Use Case]] gets built, and tests build the same application with a [[Test Double]] in place of each adapter.

**A composition root is the one module that loads the settings, builds every adapter, passes them into the use cases and hands the wired application to whatever runs it, so no other module constructs its own dependencies.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the composition root writes the rest around it.

## Where to learn this

**Composition root**, the one place where the application's objects are built and wired together.

**Videos**

- ArjanCodes, Dependency Injection Makes Code Easier to Change and Test, After, 3:47 to 6:42: [watch](https://www.youtube.com/watch?v=DpMGEhwuuyA&t=227s). The same code after dependency injection, where objects are built outside and passed in, which is the move a composition root gathers into one module. Chapter-timed.
- ArjanCodes, Dependency INVERSION vs Dependency INJECTION in Python, Applying dependency injection, 6:37 to 8:35: [watch](https://www.youtube.com/watch?v=2ejbLVkCndI&t=397s). Dependency injection applied to a worked example before its unit tests. Chapter-timed.

**Our plans and chapters**

- [The composition root](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/18-the-composition-root.md), system-design/clean-architecture-in-python, plan 18. One `app.py` doing all the wiring with no module-level singletons, and the test wiring building the same application with fakes without running that file.
- [The composition root: XBL_ settings that fail loudly](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/plans/archived/17-xbl-configuration.md), ai-engineering/prototype-product-data-validation-end-to-end, plan 17. Every setting read once, from `XBL_` variables, before the providers are assembled.
- [Settings read once, and refused when unknown](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/03-the-project-and-the-hexagon.md#34-settings-read-once-and-refused-when-unknown), ai-engineering/prototype-product-data-validation-end-to-end, chapter 3.4. A mistyped `XBL_MAX_FILE_SIZE_KBB=200` silently keeps the 2000 KB limit when each module reads its own variable, and stops startup with exit 2 when the composition root loads settings once.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No book on the shelf names the composition root (a page-text search of the five software and system design books found it nowhere), so the card has no textbook line. No video found names it either: ByteByteGo, Hello Interview and KodeKloud have nothing on it, and the open search returned dependency injection videos, two of which are listed because injection is the move the composition root collects in one place. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title, description and its lines on the composition root. "Composition root" is a two-word name, so it links everywhere; its 22 files in the learning tree all mean this module.
