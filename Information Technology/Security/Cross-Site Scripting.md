---
aliases: [XSS, cross-site scripting, stored XSS, reflected XSS, DOM-based XSS]
standard: vault-note v2
---

# Cross-Site Scripting

Up: [[Security]]

Information Technology, Security. Its sibling attack is [[Cross-Site Request Forgery]]; an `HttpOnly` [[HTTP Cookie]] keeps a session out of its reach, while a [[JSON Web Token]] kept in localStorage is exposed to it.

**Cross-site scripting is an attack in which a site sends an attacker's script to your browser as part of its own page, because it echoed someone's input without escaping it, so the script runs with that page's rights and can read its tokens and act as you.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches XSS writes the rest around it.

## Where to learn this

**Cross-site scripting (XSS)**, an attacker's script running inside your page. Also: XSS, stored XSS, reflected XSS, DOM-based XSS.

**Textbooks**

- System design big archive, Cross-Site Scripting (XSS) Attacks: [pages 347 to 348](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=347). The three kinds: reflected (the payload in a link's URL, echoed back in the response), stored (saved in a comment or profile and run for every visitor) and DOM-based (never reaching the server, so server-side validation misses it).

**Videos**

- Hussein Nasser, Cross-Site Scripting Explained with Examples and How to Prevent XSS with Content Security Policy, XSS Stored Attacks, 2:40 to 4:50: [watch](https://www.youtube.com/watch?v=pD6C1-zSxIM&t=160s). A stored attack shown by example, before the reflected one and the source code behind both. Chapter-timed.
- Hussein Nasser, Cross-Site Scripting Explained with Examples and How to Prevent XSS with Content Security Policy, Reflected XSS Attacks, 4:50 to 8:00: [watch](https://www.youtube.com/watch?v=pD6C1-zSxIM&t=290s). A reflected attack, where the script arrives in the request and comes back in the page. Chapter-timed.
- Hussein Nasser, Cross-Site Scripting Explained with Examples and How to Prevent XSS with Content Security Policy, Prevent XSS Attacks with CSP, 9:50 to 16:00: [watch](https://www.youtube.com/watch?v=pD6C1-zSxIM&t=590s). A Content Security Policy header stopping the injected script, then a policy that blocks every inline script. Chapter-timed.
- Hussein Nasser, 1 Hour of Popular Web Attacks (XSS, CSRF, SSRF, SQL Injection, MIME Sniffing, Smuggling and more!), XSS, 1:16 to 19:47: [watch](https://www.youtube.com/watch?v=pdC3H8SX-F4&t=76s). XSS at length as the first of eight web attacks, before CSRF. Chapter-timed.
- Hayk Simonyan, API Security Explained: Rate Limiting, CORS, SQL Injection, CSRF, XSS & More, XSS, 7:17 to 8:41: [watch](https://www.youtube.com/watch?v=FsB_nRGdeLs&t=437s). A short XSS chapter closing a list of API defences, after CSRF. Chapter-timed.

**Our plans and chapters**

- [What "How JWT Works" assumes, and where each piece is taught](/home/molef/goal-setting/learning/system-design/security-and-auth/sources/jwt/how-jwt-works-prerequisites.md#the-learning-goal-for-each-concept), system-design/security-and-auth. The XSS goal: a toy page echoing a comment unescaped, the injected script reading a token from localStorage the way Attica stores it under `tokens`, then the fix by escaping the output, with the token showing up in the attacker's request log as the visible failure.
- [Sources: JWT](/home/molef/goal-setting/learning/system-design/security-and-auth/sources/jwt/SOURCES.md#where-the-picture-contradicts-itself), system-design/security-and-auth. A token in local or session storage can be read and stolen through any XSS bug, an HttpOnly cookie cannot but reopens CSRF, and that choice between two failure modes is set aside for its own worked example.
- [System Design: Security and Auth](/home/molef/goal-setting/learning/system-design/security-and-auth/MASTER_PLAN.md#goals), system-design/security-and-auth. Goal 5: an XSS hole introduced on a toy app, exploited and fixed, beside SQL injection and CSRF; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The big archive pages were found through its chapter table in Textbooks.md and read with pdftotext; a page-text search of the five system design books for "xss" and "cross-site scripting" found no other page, and no back-of-book table has the term. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. ByteByteGo, Hello Interview and KodeKloud have no XSS segment that a channel search found. Each plan and source file was read at its title and the lines that name XSS. Left out: Hussein Nasser's Microsoft Awards them $20k for finding one of a kind XSS bug in Edge (`yBevYAQBXfY`), a news story about one bug, whose chapters were not read. "XSS" matches in capitals only, and all of its uses in the learning tree mean the attack.
