---
aliases: [encryption, encrypt, encryption at rest, encryption in transit]
link-skip: [Let's Encrypt]
standard: vault-note v2
---

# Encryption

Up: [[Security]]

Information Technology, Security. [[TLS]] is encryption in transit for web traffic, and a [[JSON Web Token]]'s payload is encoded and signed but not encrypted.

**Encryption turns readable data into ciphertext that only the holder of the right key can turn back, with one shared key in symmetric encryption and a public and private key pair in asymmetric encryption.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches encryption writes the rest around it.

## Where to learn this

**Encryption**, data only the key holder can read. Also: encrypt, encryption at rest, encryption in transit.

**Textbooks**

- System design big archive, How Digital Signatures Work?: [pages 55 to 56](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=55). Works one signed document from Alice to John in eight steps: Alice hashes it and encrypts the hash with her private key, and John decrypts it with her public key and compares hashes.
- Systems analysis and design, chapter 8, Encryption and authentication requirements: [pages 323 to 325](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=323). Symmetric algorithms (DES, AES) against public key encryption, digital signatures, and the certificate authorities of the public key infrastructure, ending on which data a system must encrypt.
- System design big archive, How does HTTPS work?: [pages 176 to 177](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=176). Encryption in transit: asymmetric encryption carries a session key to the server, then symmetric encryption carries the data, with the two reasons for switching.
- System design interview, chapter 15, Design Google Drive, Block servers: [page 255](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=255). Encryption at rest in a design: each block of a file is compressed and then encrypted before it is uploaded to cloud storage.

**Videos**

- Hussein Nasser, Symmetrical vs asymmetrical Encryption Pros and Cons by Example, Symmetric Encryption, 1:50 to 9:40: [watch](https://www.youtube.com/watch?v=Z3FwixsBE94&t=110s). Symmetric encryption by example, before the asymmetric chapter and the pros and cons of each. Chapter-timed.
- Hussein Nasser, How End-to-End encryption Works?, End to end encryption, 3:25 to 7:30: [watch](https://www.youtube.com/watch?v=hwQbPgvEQyw&t=205s). End-to-end encryption, after a classic encryption example and before the trust problem it leaves. Chapter-timed.
- Hussein Nasser, Five Password Authentications From Least to Most Secure, Auth Method 5: Encrypt everything, don't store password in the database, 20:30 to 25:10: [watch](https://www.youtube.com/watch?v=_t8EPImx9LI&t=1230s). The last of five password schemes built in NodeJS against Postgres, where encryption replaces the stored password. Chapter-timed.

**Our plans and chapters**

- [System Design: Security and Auth](/home/molef/goal-setting/learning/system-design/security-and-auth/MASTER_PLAN.md), system-design/security-and-auth. Objective 3, data protection: encryption in transit and at rest, and what each actually protects; it holds goals and no plans yet.
- [HTTPS, and three round trips](/home/molef/goal-setting/learning/system-design/foundations/plans/09-https-and-three-round-trips.md), system-design/foundations, plan 09. Points at where the encryption ends, at the nginx container holding the mkcert certificate, and times the round trip that agrees on encryption.
- [Tokens and claims](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/textbook/04-tokens-and-claims.md), ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions, chapter 04. Section 4.1 decodes a token's first two pieces with no key, because they are encoded and not encrypted.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext; the Systems analysis and design pages came from its back-of-book index ("Encryption", "Symmetric encryption algorithm", "Public key encryption"), and the big archive and System design interview pages from a pdftotext search of every page for "encrypt". Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title and the lines that name encryption. Left out: System design interview's YouTube chapter (page 239), which names AES encryption of videos in one bullet; ByteByteGo's SSL, TLS, HTTPS Explained, whose chapters are HTTPS and TLS and sit on [[TLS]]; Arpit Bhayani's End-to-end Message Encryption, whose chapter list was not read. The words TLS, HTTPS and SSL belong to the TLS card and are not aliases here. The bare word "encryption" was sampled in the learning tree's prose: 25 uses, all meaning encryption; "encrypt" has 4, one of them the certificate authority Let's Encrypt, which the `link-skip` phrase leaves alone.
