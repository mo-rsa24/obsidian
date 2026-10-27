---
aliases: [password hashing, password hash, hashed password, salted hash, salt, salting, rainbow table, bcrypt, slow hash]
link-only-in: [system-design]
standard: vault-note v2
---

# Password Hashing

Up: [[Security]]

Information Technology, Security. It is how a password login's [[Authentication]] keeps the password it checks, and unlike [[Encryption]] a hash cannot be turned back into the password.

**Password hashing stores a password as the output of a deliberately slow one-way hash (bcrypt, scrypt, Argon2) computed over the password plus a random salt kept beside it, so a stolen table reveals no passwords, two users with the same password store different hashes, and a precomputed rainbow table of common passwords is useless.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches password hashing writes the rest around it.

## Where to learn this

**Password hashing**, storing a password as a salted, slow, one-way hash. Also: password hash, hashed password, salted hash, salt, salting, rainbow table, bcrypt, slow hash.

**Textbooks**

- Computer networking, chapter 8, 8.3.1 Cryptographic Hash Functions: [pages 641 to 643](../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=641). The one-way, collision-resistant property a password hash rests on, worked with an IOU message whose simple checksum a forger can match, then MD5 and SHA-1; it hashes messages, not passwords.

**Videos**

- Hussein Nasser, Five Password Authentications From Least to Most Secure (Explained with NodeJS & Postgres), Auth Method 2 - Authentication with Password hash, 8:00 to 11:30: [watch](https://www.youtube.com/watch?v=_t8EPImx9LI&t=480s). The second of five logins coded in NodeJS against Postgres: the password stored as a plain hash, after the plain-text version. Chapter-timed.
- Hussein Nasser, Five Password Authentications From Least to Most Secure (Explained with NodeJS & Postgres), Auth Method 3 - Authentication with Password hash and Salt, 11:30 to 16:30: [watch](https://www.youtube.com/watch?v=_t8EPImx9LI&t=690s). The same login with a salt added to the hash. Chapter-timed.
- Hussein Nasser, Five Password Authentications From Least to Most Secure (Explained with NodeJS & Postgres), Auth Method 4 - Authentication with bcrypt hash with inline salt, 16:30 to 20:30: [watch](https://www.youtube.com/watch?v=_t8EPImx9LI&t=990s). bcrypt, which keeps its salt inside the stored hash. Chapter-timed.
- ByteByteGo, System Design: How to store passwords in the database?, Modern hashing algorithm, 0:54 to 1:19: [watch](https://www.youtube.com/watch?v=zt8Cocdy15c&t=54s). The modern slow hashing algorithms, before the legacy ones to avoid. Chapter-timed.
- ByteByteGo, System Design: How to store passwords in the database?, Salt, 1:37 to 2:30: [watch](https://www.youtube.com/watch?v=zt8Cocdy15c&t=97s). The salt added to each password before hashing. Chapter-timed.
- BugBytes, Django ORM Deep Dive - Models, Migrations and Admin UI Integration, Django Password Hashing, 34:07 to 35:38: [watch](https://www.youtube.com/watch?v=t7diJPGxCGo&t=2047s). How Django stores a user's password as a hash, the framework the foundations journey builds the user service in. Chapter-timed.

**Our plans and chapters**

- [What "How JWT Works" assumes, and where each piece is taught](/home/molef/goal-setting/learning/system-design/security-and-auth/sources/jwt/how-jwt-works-prerequisites.md#the-learning-goal-for-each-concept), system-design/security-and-auth. The password hashing goal: SHA-256 of a salt followed by `password` worked by hand, then bcrypt timed at cost factors 10, 12 and 14, each step landing on one field (salt, cost, hash) of a stored-row diagram.
- [System Design: Security and Auth](/home/molef/goal-setting/learning/system-design/security-and-auth/MASTER_PLAN.md#goals), system-design/security-and-auth. Goal 1: hashing and salting implemented from scratch, with a rainbow table shown breaking the unsalted column; it holds goals and no plans yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The Computer networking pages were found through its back-of-book index ("cryptographic hash functions", book pages 639 to 641, PDF pages 641 to 643) and read with pdftotext. No shelf book teaches storing a password as a hash: a pdftotext search of every page of the five system design books for "password hash", "salt", "bcrypt" and "rainbow table" found nothing. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; BugBytes is outside the creator list and comes from the chapter cache, where an earlier sweep left it. Each plan was read at its title and the lines that name hashing. Left out: Computer networking's 8.4.3 and 8.4.4 (pages 653 to 654), which send a password over the network and replay it rather than store it; Hussein Nasser's No, You Don't have to Encrypt Passwords before sending POST requests, about the wire rather than storage. KodeKloud's Building an Authentication System was not read: it has no chapters and YouTube returned no captions. The bare word "salt" is used 4 times in the learning tree's prose and "salting" 5 times, every one meaning a password salt, all in system-design; `link-only-in: [system-design]` keeps those single words from linking elsewhere, where "salt" is food or chemistry, while the multi-word aliases link everywhere.
