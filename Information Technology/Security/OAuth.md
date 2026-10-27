---
aliases: [OAuth, OAuth 2.0, OAuth2, OAuth 2.1]
standard: vault-note v2
---

# OAuth

Up: [[Security]]

Information Technology, Security. It is delegated [[Authorization]], [[OpenID Connect]] adds [[Authentication]] on top of it, and the access token it issues is often a [[JSON Web Token]].

**OAuth 2.0 lets one application act on your data at another service without ever seeing your password: you log in at that service's authorization server and approve, the application receives a short-lived access token, and it calls the service's API with that token. OpenID Connect adds an ID token to the same flow so the application also learns who you are, which is what "Sign in with Google" runs on.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches OAuth writes the rest around it.

## Where to learn this

**OAuth 2.0**, delegated access without sharing a password. Also: OAuth, OAuth2, OAuth 2.1.

**Textbooks**

- System design big archive, 5 REST API Authentication Methods: [pages 403 to 404](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=403). OAuth-based authentication: the client gets an access token through an authorization grant from the provider and calls resource servers with it on the user's behalf, for third-party integrations, set beside basic, session, token and API key authentication.
- System design big archive, Session, Cookie, JWT, Token, SSO, and OAuth 2.0 Explained in One Diagram: [pages 36 to 37](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=36). OAuth2 in one line among the ways to stay logged in: limited access to your data on one site by another, without giving away passwords.

**Videos**

- Gaurav Sen, Authorization across Distributed Systems: The OAuth Protocol, OAuth Flow, 1:25 to 4:22: [watch](https://www.youtube.com/watch?v=65-6asTjuB8&t=85s). The flow, after the chapter on what is wrong with handing an application your password, and before a war story where OAuth doubled sign-ups. Chapter-timed.
- ByteByteGo, OAuth 2 Explained In Simple Terms, 0:00 to 4:32: [watch](https://www.youtube.com/watch?v=ZV5yTm4pT8g&t=0s). OAuth 2 in one short explainer, where one site gets limited access to your data on another. Whole video.
- ByteByteGo, Top 12 Tips For API Security, Implementing OAuth 2.0, 0:53 to 2:22: [watch](https://www.youtube.com/watch?v=6WZ6S-qmtqY&t=53s). OAuth 2.0 as the second of twelve tips for securing an API, after HTTPS. Chapter-timed.
- Hayk Simonyan, 7 Authentication Concepts Every Developer Should Know, OAuth2, 14:38 to 16:14: [watch](https://www.youtube.com/watch?v=iX8g4LqF8p8&t=878s). OAuth2 after the chapters on bearer tokens and on access and refresh tokens. Chapter-timed.
- Hayk Simonyan, 7 Authentication Concepts Every Developer Should Know, OpenID Connect, 16:14 to 17:41: [watch](https://www.youtube.com/watch?v=iX8g4LqF8p8&t=974s). OpenID Connect as the identity layer that follows OAuth2, before single sign-on. Chapter-timed.
- Hayk Simonyan, Authorization Explained: When to Use RBAC, ABAC, ACL & More, Delegated Authorization with OAuth2, 7:26 to 9:12: [watch](https://www.youtube.com/watch?v=DT6Zy1X3ytM&t=446s). OAuth2 placed among the authorization models as the delegated one. Chapter-timed.

**Our plans and chapters**

- [System Design: Security and Auth](/home/molef/goal-setting/learning/system-design/security-and-auth/MASTER_PLAN.md#goals), system-design/security-and-auth. Goal 3: an OAuth login flow implemented against a real provider, with every redirect and token exchange traced; it holds goals and no plans yet.
- [Read the role from a validated token](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/plans/34-the-role-from-a-validated-token.md), ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions, plan 34. An MCP server validating the bearer token on every call, unblocked by a segment of a tutorial on OAuth 2.1 for remote MCP servers that shows the well-known endpoint and the token-validating middleware.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The existing [[Authentication]], [[Authorization]] and [[JSON Web Token]] notes were read first: Authorization's card carries two OAuth videos as examples of delegated access, but none of the three takes OAuth as an alias or explains the flow, so OAuth has its own note. Each textbook page range was read with pdftotext after a page-text search of the five system design books for "oauth" and "openid"; no back-of-book table has either. Each video's chapter list was read with `cache-video-chapters.py` (ByteByteGo's OAuth video has none and is cited whole), and each line is described from its chapter title and the video title only. Each plan was read at its title and the lines that name OAuth. Left out: the big archive's Top 12 Tips for API Security (pages 65 to 66) and Network Services That Power Modern Connectivity (page 379), which each name OAuth in one line; the document-qa chapter 14, which names the MCP specification's OAuth requirement in one sentence; Hello Interview and KodeKloud, which have no OAuth segment (Hello Interview's API design video was read in its captions and never says OAuth; KodeKloud's Building an Authentication System has no captions or chapters to read). "OIDC" was not added as an alias: all 33 of its uses in the tree are the devops-and-deployment journey's keyless pipeline login to Azure, a machine login the card does not teach, and "OpenID Connect" spelled out appears nowhere in the tree. All of the tree's other uses of "OAuth" mean the protocol (Databricks OAuth profiles, the MCP authorization spec), so it links unscoped.
