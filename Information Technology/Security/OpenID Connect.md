---
aliases: [OIDC, OpenID Connect, OIDC federation, federated credential, workload identity federation, workload identity]
standard: vault-note v2
---

# OpenID Connect

Up: [[Security]]

Information Technology, Security. It is a form of [[Authentication]] built on OAuth 2.0, and its identity token is a [[JSON Web Token]]; a [[Continuous Integration And Delivery]] pipeline uses it to reach a cloud with no stored secret.

**OpenID Connect is a sign-in protocol on top of OAuth 2.0 in which a trusted issuer hands out a short-lived signed identity token, so a person ("Sign in with Google") or a pipeline (a GitHub Actions run) can prove who it is to another service without a password or a stored key.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches OpenID Connect writes the rest around it.

## Where to learn this

**OpenID Connect (OIDC)**, a short-lived signed identity token in place of a password or a stored key. Also: OIDC, OIDC federation, federated credential, workload identity federation.

**Textbooks**

- System design big archive, the network protocols overview: [page 379](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=379). One line placing OAuth 2.0 and OpenID Connect as the protocols behind "Sign in with Google", among the protocols a web application speaks.

**Videos**

- John Savill's Technical Training, GitHub Azure AD OIDC Authentication, 13:42 to 18:20: [watch](https://www.youtube.com/watch?v=XkhkkLBkAT4&t=822s). Works the setup: the `azure/login` step in a GitHub workflow, then the federated credential on the Azure app registration. Chapter-timed.
- John Savill's Technical Training, GitHub Azure AD OIDC Authentication, 0:47 to 5:21: [watch](https://www.youtube.com/watch?v=XkhkkLBkAT4&t=47s). The stored secret a pipeline used to hold, then what OIDC changes. Chapter-timed.
- John Savill's Technical Training, GitHub Azure AD OIDC Authentication, 5:21 to 8:08: [watch](https://www.youtube.com/watch?v=XkhkkLBkAT4&t=321s). GitHub's identity token exchanged for an Azure access token. Chapter-timed.
- ByteByteGo, What Is Single Sign-on (SSO)? How It Works, Comparing SAML and OpenID, 3:42 to 4:42: [watch](https://www.youtube.com/watch?v=O1cRJWYF-g4&t=222s). OpenID Connect set against SAML as the two protocols behind a person's single sign-on. Chapter-timed.

**Our plans and chapters**

- [No stored keys: OIDC federation](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/16-no-stored-keys-oidc.md), system-design/devops-and-deployment, plan 16. Federated credentials on GitHub and workload identity federation on Azure DevOps, so both pipelines log in to Azure with a short-lived token and no secret is stored anywhere.
- [The gate inventory](/home/molef/goal-setting/learning/system-design/devops-and-deployment/textbook/01-requirements-gates-and-environments.md#12-the-gate-inventory), the same journey, chapter 1, section 1.2. "No stored key" as a gate that costs nothing and runs at every cloud login, enforcing requirement R5 that neither pipeline holds a cloud password.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. A pdftotext search of every page of the system design, software engineering and AI engineering books for "OpenID", "OIDC", "federated credential" and "workload identity" found two pages, both in the big archive, and both only name it; page 379 says what it is for and is kept, page 438 ("OAuth and OpenID handle authorization and authentication") is left out. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. None of ByteByteGo, Hello Interview, KodeKloud or freeCodeCamp covers federation from a pipeline, so the John Savill rows come from the open search, as in the devops journey's video sweep. Chapter 1 section 1.2 was read in full; the plan was read at its title and description, and its chapter holds headings only. Left out: the big archive's Session, Cookie, JWT, Token, SSO, and OAuth 2.0 spread (pages 36 to 37), which never names OpenID Connect. The acronym matches in capitals only; "OpenID Connect" has no use in the learning tree's prose yet, and the other aliases are the Azure names for trusting an OIDC token from GitHub and from Azure DevOps.
