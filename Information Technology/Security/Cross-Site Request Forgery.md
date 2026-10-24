---
aliases: [CSRF, cross-site request forgery, CSRF token]
standard: vault-note v2
---

# Cross-Site Request Forgery

Up: [[Security]]

Information Technology, Security. It attacks a site that keeps [[Authentication]] in a cookie, and a [[JSON Web Token]] stored in a cookie reopens it.

**Cross-site request forgery is an attack in which another site makes your browser send a request to a site you are logged in to, and the browser attaches your cookie, so the request runs as you.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches CSRF writes the rest around it.

## Where to learn this

**Cross-site request forgery (CSRF)**, a forged request that rides on your cookie. Also: CSRF, CSRF token.

**Videos**

- Hussein Nasser, Cross Site Request Forgery vs Server Side Request Forgery Explained, CSRF, 0:20 to 4:19: [watch](https://www.youtube.com/watch?v=a7OMdTuYaGc&t=20s). CSRF on its own, before the chapter on server-side request forgery it is often confused with. Chapter-timed.
- Hussein Nasser, 1 Hour of Popular Web Attacks (XSS, CSRF, SSRF, SQL Injection, MIME Sniffing, Smuggling and more!), CSRF, 19:47 to 24:10: [watch](https://www.youtube.com/watch?v=pdC3H8SX-F4&t=1187s). CSRF as one of eight web attacks, straight after the XSS chapter. Chapter-timed.
- Hussein Nasser, SameSite Cookie Attribute Explained by Example (Strict, Lax, None & No SameSite), SameSite=Lax, 6:00 to 8:00: [watch](https://www.youtube.com/watch?v=aUF2QCEudPo&t=360s). The Lax setting of the cookie attribute that decides whether a cookie goes with a cross-site request, after the Strict chapter. Chapter-timed.
- Hayk Simonyan, API Security Explained: Rate Limiting, CORS, SQL Injection, CSRF, XSS & More, CSRF, 6:24 to 7:17: [watch](https://www.youtube.com/watch?v=FsB_nRGdeLs&t=384s). A short CSRF chapter in a list of API defences, before XSS. Chapter-timed.

**Our plans and chapters**

- [Django, refreshed](/home/molef/goal-setting/learning/system-design/foundations/textbook/06-django-refresher.md), system-design/foundations, chapter 06. Section 6.2 logs in to the Django admin with curl and has to send the `csrftoken` cookie back as a form field; a POST without it gets a 403, Django refusing a form that did not come from its own page.
- [What "How JWT Works" assumes, and where each piece is taught](/home/molef/goal-setting/learning/system-design/security-and-auth/sources/jwt/how-jwt-works-prerequisites.md), system-design/security-and-auth. The CSRF learning goal: another site making your browser send a request with your cookie, defended with `SameSite=Lax` and separately with a CSRF token, and why an HttpOnly JWT cookie reopens it.
- [System Design: Security and Auth](/home/molef/goal-setting/learning/system-design/security-and-auth/MASTER_PLAN.md), system-design/security-and-auth. Goal 5: a CSRF hole introduced on a toy app, exploited, fixed and shown failing after the fix; it holds goals and no plans yet.
- [User and order in Django](/home/molef/goal-setting/learning/system-design/foundations/plans/13-user-and-order-in-django.md), system-design/foundations, plan 13. Lists "CSRF verification failed" among its failures, meaning the site was reached on an address missing from `CSRF_TRUSTED_ORIGINS`.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. No shelf book teaches CSRF: a pdftotext search of every page of the four system design books for "csrf" and "cross-site request" found nothing, and no back-of-book table has the term, so the card has no Textbooks group. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title and the lines that name CSRF. Left out: Hussein Nasser's Will the New Chrome version 80 finally end Cross-Site Request forgery? (`ULKEr8Bdjlc`), whose chapter list was not read.
