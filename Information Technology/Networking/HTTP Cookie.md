---
aliases: [cookie, session cookie, HttpOnly, Set-Cookie, SameSite, HTTP cookie]
link-skip: [cookies and cream, cookies & cream, chocolate chip cookies, Biscuits]
standard: vault-note v2
---

# HTTP Cookie

Up: [[Networking]]

Information Technology, Networking. A cookie travels in [[HTTP]] headers, is kept from script and from other sites by its HttpOnly, Secure and SameSite attributes, and is what lets a [[CORS]] request carry a login.

**A cookie is a small named value a server sets with a `Set-Cookie` header; the browser stores it and sends it back on every later request to that site, which is how a site remembers a session.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches cookies writes the rest around it.

## Where to learn this

**HTTP cookie**, a value the server sets and the browser sends back. Also: cookie, session cookie, HttpOnly, SameSite.

**Textbooks**

- System design big archive, Cookies vs Sessions: [pages 322 to 323](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=322). Data kept in the cookie itself and sent on every request, against a session where the cookie holds only a session ID that the server looks up in its store.
- System design big archive, Session, Cookie, JWT, Token, SSO, and OAuth 2.0 Explained in One Diagram: [pages 36 to 37](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=36). The session ID cookie beside the other ways a site keeps a login: tokens, JWTs, single sign-on, OAuth 2.0 and QR code login.
- System design big archive, Cookies Vs Sessions Vs JWT Vs PASETO: [pages 26 to 27](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=26). Cookies and sessions as one authentication mechanism, with session data on the server referenced by a client-side cookie, and the scaling cost that pushes some systems to JWTs.

**Videos**

- Hussein Nasser, HTTP Cookies Crash Course, Section 1: Creating Cookies, 4:15 to 14:38: [watch](https://www.youtube.com/watch?v=sovAIX4doOE&t=255s). Creating cookies, the first section of a course that goes on to their properties, types and security. Chapter-timed.
- Hussein Nasser, SameSite Cookie Attribute Explained by Example (Strict, Lax, None & No SameSite), SameSite=Strict, 1:10 to 6:00: [watch](https://www.youtube.com/watch?v=aUF2QCEudPo&t=70s). The strictest SameSite value shown by example, before the Lax, None and missing-attribute chapters. Chapter-timed.
- Hussein Nasser, HTTP Cookies Crash Course, Section 2: Cookie Properties, 14:38 to 44:00: [watch](https://www.youtube.com/watch?v=sovAIX4doOE&t=878s). The attributes a cookie can carry. Chapter-timed.
- ByteByteGo, Session Vs JWT: The Differences You May Not Know!, Session authentication, 0:18 to 1:23: [watch](https://www.youtube.com/watch?v=fyTxwIa-1U0&t=18s). Session authentication, before the chapters on the JWT flow. Chapter-timed.

**Our plans and chapters**

- [Django, refreshed](/home/molef/goal-setting/learning/system-design/foundations/textbook/06-django-refresher.md), system-design/foundations, chapter 06, section 6.2. Follows the admin login with `curl -c` and `-b` and a cookie jar file, where the POST needs the `csrftoken` cookie sent back as a form field or Django answers 403.
- [System Design: Security and Auth](/home/molef/goal-setting/learning/system-design/security-and-auth/MASTER_PLAN.md), system-design/security-and-auth. Session auth beside JWT auth for one login, and a source that recommends an HttpOnly cookie while the next reads the token in JavaScript; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the chapter tables in `Textbooks.md` and a page-text search for "cookie" across the four system design books; System design interview mentions cookies once, as a CDN cache key. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each chapter and plan was read at its title and the section named. Left out: the big archive's 5 REST API Authentication Methods (page 403), one line on session authentication issuing a cookie. The bare word "cookie" is used 46 times on 35 lines of the learning tree. 29 lines mean the HTTP cookie (HttpOnly, `Set-Cookie`, SameSite, a cookie jar for `curl`, CSRF); the other 6 are the food in product-data-validation's test products ("cookies and cream", "Chocolate Chip Cookies", a pack reading "Cookies" against a title reading "Biscuits"), and the `link-skip` phrases catch all 6.
