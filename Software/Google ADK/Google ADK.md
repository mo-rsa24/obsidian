---
aliases: [ADK, Agent Development Kit, Google Agent Development Kit, google-adk]
standard: vault-note v2
---

# Google ADK

Up: [[Software]]

Software, Google ADK. The product validation agent is built with it, and the Databricks job walk meets it where the agent has to run inside a job.

**The Agent Development Kit (ADK) is Google's Python library for building an LLM agent as a folder of code, and for running it through a development UI (`adk web`), the command line (`adk run`), an HTTP server (`adk api_server`), or a `Runner` inside your own program.**

Reading order:

- [[Agent Server]]: the program `adk api_server`, which loads an agents folder and answers sessions and `/run` over HTTP on `127.0.0.1:8000`; how the product validation repo starts and checks it, and why a Databricks job does not start one.
- [[XBL_MODEL_ENDPOINT]]: the environment variable the product validation agent's `config.py` reads once, when the server loads the agent, to pick the Databricks serving endpoint it calls.
- [[In-Process Agent]]: the agent loaded into the calling program and called as a function, with no server and no port; ticket MR-05, not built yet.
