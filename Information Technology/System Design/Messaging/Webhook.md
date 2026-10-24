---
aliases: [webhook, callback URL]
standard: vault-note v2
---

# Webhook

Up: [[Messaging]]

Information Technology, System Design. A webhook is the alternative to [[Polling]]: the other system calls you instead of you asking it again and again, and a retried webhook is safe only when its handler has [[Idempotency]].

**A webhook is an HTTP request that another system sends to a URL you registered with it, the moment something happens on its side, such as a payment provider confirming a charge.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches webhooks writes the rest around it.

## Where to learn this

**Webhook**, the other system calls your URL when something happens. Also: callback URL.

**Videos**

- Hussein Nasser, Webhooks Tutorial with Discord and Vanilla Javascript (fetch api), Example, 5:20 to 15:06: [watch](https://www.youtube.com/watch?v=-4Lid7tBr6Y&t=320s). Sends messages to a Discord channel through its webhook URL with plain `fetch`, a working webhook built on screen. Chapter-timed.
- ByteByteGo, Top 3 Things You Should Know About Webhooks!, How webhooks work, 1:30 to 2:00: [watch](https://www.youtube.com/watch?v=x_jjhcDrISk&t=90s). The mechanism, straight after the chapter on polling and long polling that it replaces. Chapter-timed.
- ByteByteGo, Top 3 Things You Should Know About Webhooks!, Webhook best practices, 2:00 to 3:11: [watch](https://www.youtube.com/watch?v=x_jjhcDrISk&t=120s). The video's best practices for webhooks, before its chapter on alternative technologies. Chapter-timed.
- Hussein Nasser, Webhooks Tutorial with Discord and Vanilla Javascript (fetch api), Webhooks Explained, 1:10 to 5:20: [watch](https://www.youtube.com/watch?v=-4Lid7tBr6Y&t=70s). What a webhook is before the example. Chapter-timed.

**Our plans and chapters**

- [The providers, the webhook, and one key](/home/molef/goal-setting/learning/system-design/foundations/plans/20-providers-webhook-and-one-key.md), system-design/foundations, plan 20. The fake payment provider calls back to the corner shop's payment service by webhook, and a retried charge lands once even when the reply to the first attempt is lost.
- [Requirements, gates and environments on paper](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/01-requirements-gates-and-environments.md), system-design/devops-and-deployment, plan 01. A second service, `payments-webhook`, which a card processor calls to confirm payment, added to the requirements table and the environment matrix.
- [System Design: API Design and Contracts](/home/molef/goal-setting/learning/system-design/api-design-and-contracts/MASTER_PLAN.md), system-design/api-design-and-contracts. Places webhooks among the API styles, the one used for event callbacks; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No shelf book teaches webhooks: a page-text search of the system design, AI engineering and language model books found the word once, in the big archive's API learning roadmap (page 31), as a name in a list, so the card has no Textbooks group. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: the compiled chapter for foundations plan 20, whose sections are headings with no text yet.
