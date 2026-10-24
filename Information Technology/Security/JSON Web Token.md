---
aliases: [JWT, JSON Web Token, bearer token]
standard: vault-note v2
---

# JSON Web Token

Up: [[Security]]

Information Technology, Security. It is one way to carry the result of [[Authentication]] between requests, and its claims are what [[Authorization]] reads.

**A JSON Web Token is a header, a payload of claims and a signature, three base64url pieces joined by dots, which a server can trust without a session lookup because only the holder of the signing key could have produced the signature.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches JWTs writes the rest around it.

## Where to learn this

**JSON Web Token (JWT)**, a signed token that carries its own claims. Also: JWT, bearer token.

**Textbooks**

- System design big archive, Tokens vs API Keys: [pages 236 to 237](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=236). Works the token flow in eight steps: a login, an identity service issuing the JWT, the frontend sending it in the Authorization header, and the gateway checking its signature, expiry and claims before forwarding.
- System design big archive, JWT 101: Key to Stateless Authentication: [pages 51 to 52](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=51). The header, payload and signature, then signing with one shared secret against signing with a private key and verifying with a public one.
- System design big archive, Cookies Vs Sessions Vs JWT Vs PASETO: [pages 26 to 27](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=26). Where the JWT sits among the ways to stay logged in: stateless and scalable, at the cost of token theft and expiry to manage.
- System design big archive, JWT vs PASETO: The Two Players of Token-Based Authentication: [pages 282 to 283](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=282). PASETO as the alternative that fixes the algorithm choice JWT leaves open, with signed and encrypted variants.

**Videos**

- Hussein Nasser, JWT: JSON Web Token Crash Course (NodeJS & Postgres), Example coding, 28:16 to 42:00: [watch](https://www.youtube.com/watch?v=T0k-3Ze4NLo&t=1696s). JWT authentication coded in NodeJS against Postgres, after the chapters on session-based auth, JWT-based auth, refresh tokens and asymmetric JWTs. Chapter-timed.
- ByteByteGo, Why is JWT popular?, Token structure and claims, 1:08 to 2:10: [watch](https://www.youtube.com/watch?v=P2CPd9ynFLg&t=68s). The token's parts and its claims, before the chapters on signing and on JWT's vulnerabilities. Chapter-timed.
- ByteByteGo, Session Vs JWT: The Differences You May Not Know!, JSON Web Tokens flow, 1:23 to 2:40: [watch](https://www.youtube.com/watch?v=fyTxwIa-1U0&t=83s). The JWT request flow, set against the session authentication chapter before it. Chapter-timed.

**Our plans and chapters**

- [Read a token by hand](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/plans/09-a-token-decoded-by-hand.md), ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions, plan 09. A staff member's JWT decoded on paper four characters at a time until the `role` claim reads `staff`, then what the signature proves.
- [Validate a token, and watch a forged one fail](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/plans/10-a-token-validated-in-code.md), the same journey, plan 10. A token signed with a local key and checked with PyJWT, then a forged role run through a validating and a non-validating reader.
- [Tokens and claims](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/textbook/04-tokens-and-claims.md), the same journey, chapter 04. The compiled chapter for both plans: a real token read by hand, validated, and forged.
- [Read the role from a validated token](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/plans/34-the-role-from-a-validated-token.md), the same journey, plan 34. An MCP server validating the bearer token on every call and reading the role from its claims.
- [What "How JWT Works" assumes, and where each piece is taught](/home/molef/goal-setting/learning/system-design/security-and-auth/sources/jwt/how-jwt-works-prerequisites.md), system-design/security-and-auth. Every idea a seven-step JWT infographic assumes (base64url, signing, cookie storage, CSRF), with where each is taught and a learning goal for each.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after finding it in the big archive's chapter table in Textbooks.md; no other shelf book names JWT. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title and description. Left out: the big archive's Explaining JSON Web Token (JWT) with simple terms (pages 156 to 157), the same three parts told as a sealed box, and JWT Simply Explained (pages 166 to 167), a repeat of JWT 101. The phrase "bearer token" was sampled in the learning tree's prose: 19 uses, most of them the validated JWT the permissions chatbot reads its role from, with the rest naming Postman's Bearer Token setting for the same header. "Access token" was left out: of 27 prose uses about half are Databricks personal access tokens, a stored key with no claims.
