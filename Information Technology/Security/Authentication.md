---
aliases: [authentication, authn, session authentication, login flow]
standard: vault-note v2
---

# Authentication

Up: [[Security]]

Information Technology, Security. [[Authorization]] is the check that comes after it, and a [[JSON Web Token]] is one way to carry its result from request to request.

**Authentication is the check that a caller is who it claims to be, by a password, a session cookie, a signed token or a key, before the system decides what that caller may do.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches authentication writes the rest around it.

## Where to learn this

**Authentication**, proving who the caller is. Also: authn, session authentication, login flow.

**Textbooks**

- System design interview, chapter 1, Stateless web tier: [pages 20 to 21](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=20). Works a concrete case: user A's session data lives on server 1, so a request routed to server 2 fails authentication, and moving the session into a shared store lets any server check it.
- System design big archive, 5 REST API Authentication Methods: [pages 403 to 404](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=403). Basic authentication, session cookies, signed tokens, OAuth access tokens and API keys side by side, each with where it is used.
- System design big archive, Session, Cookie, JWT, Token, SSO, and OAuth 2.0 Explained in One Diagram: [pages 36 to 37](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=36). How a login is remembered: a server-side session with a cookie, a token the browser sends back, a signed JWT, single sign-on and a QR-code login.
- System design big archive, How Does SSO Work?: [pages 268 to 269](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=268). One login at an identity provider walked through 15 steps, with Gmail and then Slack accepting the token it issues.
- System design big archive, How Two-factor Authentication (2FA) Works?: [pages 104 to 105](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=104). A password as the first factor, then an OTP, an authenticator app or a biometric as the second, in seven steps.

**Videos**

- Hussein Nasser, Five Password Authentications From Least to Most Secure, Auth Method 1: Authentication password plain text, 4:00 to 8:00: [watch](https://www.youtube.com/watch?v=_t8EPImx9LI&t=240s). The first of five password checks built in NodeJS against Postgres, before the chapters that add a hash, a salt, bcrypt and encryption. Chapter-timed.
- ByteByteGo, Session Vs JWT: The Differences You May Not Know!, Session authentication, 0:18 to 1:23: [watch](https://www.youtube.com/watch?v=fyTxwIa-1U0&t=18s). Session authentication, before the chapter on the JSON Web Token flow. Chapter-timed.
- Hayk Simonyan, Authentication Explained: When to Use Basic, Bearer, OAuth2, JWT & SSO, What is Authentication?, 0:28 to 1:10: [watch](https://www.youtube.com/watch?v=9JPnN1Z_iSY&t=28s). What authentication is, before chapters on basic authentication, bearer tokens, OAuth2 and JWT, refresh tokens and SSO. Chapter-timed.
- freeCodeCamp, System Design Course: APIs, Databases, Caching, CDNs, Load Balancing and Production Infra, Authentication, 1:24:52 to 1:45:51: [watch](https://www.youtube.com/watch?v=C842vFY5kRo&t=5092s). The course's authentication chapter, a 21-minute pass placed after its API chapters. Chapter-timed.

**Our plans and chapters**

- [Django, refreshed](/home/molef/goal-setting/learning/system-design/foundations/textbook/06-django-refresher.md), system-design/foundations, chapter 06. Section 6.2 logs in to the Django admin with curl, carrying the session cookie and the `csrftoken` from the login page, and reads the redirect that proves the login worked.
- [Login and Draft Creation](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/01-tour-the-real-flow/plans/02-login-and-draft-creation.md), projects/attica/event-creation/plans/01-tour-the-real-flow, plan 02. Attica's real login toured in DevTools and the debugger, including the one request that skips the Vite proxy.
- [Auth & Authorization for Mobile Clients](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/00-requirements-and-foundations/plans/04-auth-authz-mobile-clients.md), projects/tms-mobility/system-design/plans/00-requirements-and-foundations, plan 04. Token-based authentication in Django REST Framework for two React Native apps.
- [System Design: Security and Auth](/home/molef/goal-setting/learning/system-design/security-and-auth/MASTER_PLAN.md), system-design/security-and-auth. Goals 1 and 2: password hashing and salting from scratch, then session and JWT authentication built for the same login flow; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext; the big archive pages were found through its chapter table in Textbooks.md, and the System design interview page through a pdftotext search of every page for "authenticat". Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title and description. Left out: Systems analysis and design, pages 324 to 325, whose authentication is digital signatures and certificates and sits on [[Encryption]]; the big archive's Cookies Vs Sessions Vs JWT Vs PASETO (pages 26 to 27), which sits on [[JSON Web Token]]; [the OIDC federation plan](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/16-no-stored-keys-oidc.md), where a pipeline logs in to Azure with no stored key, a machine login rather than a user's. The bare word "authentication" was sampled in the learning tree's prose: 139 uses, and 25 random lines all mean checking an identity (a Databricks profile, Postgres peer authentication, a 401 for missing credentials). Bare "login" was left out: of 147 prose uses most name one tool's sign-in step (`databricks auth login`, the import-time login) rather than the idea, so only "login flow" links.
