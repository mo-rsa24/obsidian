---
aliases: [import-linter, import linter, lint-imports, importlinter]
standard: vault-note v2
---

# import-linter

Up: [[Python]]

Software, Python. It is how the [[Dependency Rule]] of [[Clean Architecture]] becomes a check that fails a build instead of a convention.

**import-linter is a Python tool that reads contracts from a config file (layers that may import only downward, modules that must never import each other) and makes its command, `lint-imports`, fail with the offending import line when the code breaks one.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches import-linter writes the rest around it.

## Where to learn this

**import-linter**, contracts on which module may import which, checked by `lint-imports`. Also: import linter, lint-imports, importlinter.

**Our plans and chapters**

- [The import-linter layers contract](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/03-the-project-and-the-hexagon.md#36-the-import-linter-layers-contract), ai-engineering/prototype-product-data-validation-end-to-end, chapter 3.6. One wrong-way import added to `domain/records.py`: with no contract nothing complains, and with the layers contract `lint-imports` reports `Contracts: 0 kept, 1 broken.`, names the line and exits 1.
- [The five import-linter contracts](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/20-import-linter-contracts.md), system-design/clean-architecture-in-python, plan 20. A layered contract and four forbidden or independence contracts written from the standard's prose, with `lint-imports` passing on the tree.
- [Watch it refuse](/home/molef/goal-setting/learning/system-design/clean-architecture-in-python/plans/21-watch-it-refuse.md), system-design/clean-architecture-in-python, plan 21. A committed `import psycopg` in the application layer, the failing run, and its output read to name the broken contract.
- [The contracts](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/textbook/06-the-rules-engine.md#63-the-contracts), ai-engineering/product-data-validation-end-to-end, chapter 6.3. The fence from the layer picture turned into a contract file, and the test suite turning a broken contract into a red build.
- [The import-linter layers contract](/home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/plans/archived/19-import-linter-contract.md), ai-engineering/prototype-product-data-validation-end-to-end, plan 19. The sitting that writes chapter 3.6's contract after the import rule had nothing enforcing it.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No book on the shelf names import-linter. No video was found: the journey's scout of 2026-09-07 found nothing, ByteByteGo, Hello Interview and KodeKloud have nothing by title, and one open search on 2026-10-24 returned general linter talks and a PyCon talk on import order, none about import contracts. Each plan and chapter was read at its title, description and its lines on the contract. The name is the tool's own spelling, so the note keeps its lower case.
