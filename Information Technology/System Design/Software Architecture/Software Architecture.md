# Software Architecture

Up: [[System Design]]

Information Technology, System Design. The Python pieces these notes lean on are under Software: [[Structural Typing]] for writing a port, [[Pydantic]] and [[Dataclass]] for the types that cross or stay inside a boundary, and [[import-linter]] for enforcing the import rule. Fakes are in [[Test Double]].

**Software architecture here is how the code inside one service is arranged so the business rules do not depend on the database, the web framework or any other detail. These notes follow the clean architecture and its hexagonal twin, in the order a learner builds them.**

- [[Entity And Value Object]]: the two kinds of domain object, told apart by whether identity matters.
- [[Clean Architecture]]: business rules at the centre, frameworks outside, in three or four rings.
- [[Dependency Rule]]: source imports point inward only, the one rule the rings exist to keep.
- [[Ports And Adapters]]: the application names what it needs as ports, and each technology plugs in as an adapter.
- [[Use Case]]: one application-layer class per operation, taking its ports in its constructor.
- [[Composition Root]]: the one module that builds the adapters and wires them into the use cases.
