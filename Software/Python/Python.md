# Python

Software, Python. The language itself, and the Python libraries the walks use, one note each.

- [[Modules And Imports]]: how a `.py` file becomes a module another file imports, why names under `if __name__ == "__main__":` cannot be imported, and why code left above that line runs on every import.
- [[NumPy]]: arrays whose arithmetic acts on every number at once, in a folder: arrays against Python lists, broadcasting, and random numbers from a seeded generator.
- [[Structural Typing]]: Structural typing decides whether a class fits a type by the methods it has, so in Python any class with the right methods satisfies a `typing.Protocol` without naming it; nominal typing, as with an abstract base class, fits only a class that declares the parent by inheriting from it.
- [[Pydantic]]: Pydantic is a Python library whose models check and convert data as it is built, so a request body, a settings file or an API response with a wrong or missing field is refused with a message naming the field instead of travelling on into the program.
- [[Dataclass]]: A dataclass is a Python class whose `__init__`, `__repr__` and equality are written for you from its typed fields by the standard library's `@dataclass` decorator; with `frozen=True` its fields cannot change after it is built.
- [[import-linter]]: import-linter is a Python tool that reads contracts from a config file (layers that may import only downward, modules that must never import each other) and makes its command, `lint-imports`, fail with the offending import line when the code breaks one.
- [[ASGI]]: the Python standard between a web server and an application for asynchronous traffic, which carries WebSockets where WSGI cannot; Daphne and Uvicorn are ASGI servers.
