---
aliases: [authorization, authz, access control, role-based access control, RBAC]
link-skip: [Authorization tab, Authorization header, authorization against capture]
standard: vault-note v2
---

# Authorization

Up: [[Security]]

Information Technology, Security. It runs after [[Authentication]] has said who the caller is, and a [[JSON Web Token]] often carries the role it reads.

**Authorization decides what an already identified caller may do, by its role, its attributes or an explicit list of permissions, so a request can be correctly authenticated and still be refused.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches authorization writes the rest around it.

## Where to learn this

**Authorization**, what a known caller is allowed to do. Also: authz, access control, role-based access control, RBAC.

**Textbooks**

- Systems analysis and design, chapter 8, Access control requirements: [pages 322 to 323](../../Mathematics/references/textbooks/system-design/systems-analysis-and-design.pdf#page=322). Works example requirements: only department managers may change inventory in their own department, and customer service may read and create customer records but not change or delete them, each a choice of create, read, update and delete per role.
- System design big archive, Access Control Clearly Explained: [pages 324 to 325](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=324). Role-based access control, attribute-based access control and access control lists, with what each is good and bad at.
- System design big archive, Tokens vs API Keys: [pages 236 to 237](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=236). An API gateway checking a user's JWT claims, or a developer's API key against a key store, before it forwards the request.

**Videos**

- Hayk Simonyan, Authorization Explained: When to Use RBAC, ABAC, ACL & More, RBAC: Role-Based Access Control, 2:54 to 3:58: [watch](https://www.youtube.com/watch?v=DT6Zy1X3ytM&t=174s). Role-based access control, after the overview of authorization models and before ABAC, access control lists and OAuth2. Chapter-timed.
- ByteByteGo, OAuth 2 Explained In Simple Terms, 0:00 to 4:32: [watch](https://www.youtube.com/watch?v=ZV5yTm4pT8g&t=0s). OAuth 2, the delegated form, where one site gets limited access to your data on another without your password. Whole video.
- Gaurav Sen, Authorization across Distributed Systems: The OAuth Protocol, OAuth Flow, 1:25 to 4:22: [watch](https://www.youtube.com/watch?v=65-6asTjuB8&t=85s). The OAuth flow, after the chapter on what is wrong with handing over passwords. Chapter-timed.
- freeCodeCamp, System Design Course: APIs, Databases, Caching, CDNs, Load Balancing and Production Infra, Authorization, 1:45:51 to 1:57:02: [watch](https://www.youtube.com/watch?v=C842vFY5kRo&t=6351s). The course's authorization chapter, straight after its authentication chapter. Chapter-timed.

**Our plans and chapters**

- [Filter by role before ranking, and measure what it changed](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/plans/16-the-permission-filter.md), ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions, plan 16. A staff member's retrieval leaked salary bands on 4 of 5 questions; one line removing every record the asker may not read closes the leak, and the plan measures what else moved.
- [Role checks enforced in code](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/77-role-checks-enforced-in-code.md), ai-engineering/one-business-end-to-end, plan 77. A six-cell role table placed between an agent and the database, so the SQL the model writes is checked against what the logged-in role may touch.
- [Read the role from a validated token](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/plans/34-the-role-from-a-validated-token.md), the same journey, plan 34. A hard-coded role replaced by the role read from a validated bearer token, then a staff caller trying to claim `role='hr'`.
- [System Design: Security and Auth](/home/molef/goal-setting/learning/system-design/security-and-auth/MASTER_PLAN.md), system-design/security-and-auth. Goal 4: role-based access control on a toy API, showing a request that is authenticated and still refused; it holds goals and no plans yet.

**Figures**

- <a href="/home/molef/goal-setting/learning/ai-engineering/agent-harness/artifacts/figures/harness-engineering/autonomy-earned-by-evidence.png"><img src="/home/molef/goal-setting/learning/ai-engineering/agent-harness/artifacts/figures/harness-engineering/autonomy-earned-by-evidence.png" width="200" alt="A four-rung permission ladder: read automatic, write in workspace automatic plus checks, send merge or deploy needs evidence plus approval, delete pay or publish needs explicit human confirmation"></a> Ichigo on X, "Harness Engineering: Build a Reliable AI Agent in 6 Layers": [the post](https://x.com/iiiichigo_chan/status/2093765205276713218), [what it shows](/home/molef/goal-setting/learning/ai-engineering/agent-harness/artifacts/figures/harness-engineering/README.md#autonomy-is-earned-by-evidence). Authorization for an AI agent's actions, graded by consequence on four rungs: read or research is automatic, writing in a workspace is automatic plus checks, send, merge or deploy needs evidence plus approval, and delete, pay or publish needs explicit human confirmation.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext; the Systems analysis and design page came from its back-of-book index ("Access control requirements", 322 to 323) and the big archive pages from its chapter table in Textbooks.md. Each video's chapter list was read with `cache-video-chapters.py` (ByteByteGo's OAuth video has none and is cited whole), and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: the big archive's Top 12 Tips for API Security (pages 65 to 66), which only lists authorization among its tips; the CS229 lecture-map row naming access control as an advantage of retrieval over fine-tuning, which names the idea without teaching it. The bare word "authorization" was sampled in the learning tree's prose: 32 uses, about 25 meaning the idea; the rest are Postman's Authorization tab, the HTTP Authorization header and a card payment's authorization against capture, and the `link-skip` phrases leave those lines alone.
