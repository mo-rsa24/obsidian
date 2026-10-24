---
aliases: [infrastructure as code, IaC, Terraform, Bicep]
standard: vault-note v2
---

# Infrastructure As Code

Up: [[DevOps]]

Information Technology, DevOps. A [[Continuous Integration And Delivery]] pipeline often applies it, and [[Kubernetes]] manifests declare a cluster's workloads the same way.

**Infrastructure as code declares servers, databases and networks in versioned files that a tool such as Terraform or Bicep compares with what exists and then creates, changes or destroys to match.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches infrastructure as code writes the rest around it.

## Where to learn this

**Infrastructure as code (IaC)**, infrastructure declared in files and applied by a tool. Also: IaC, Terraform, Bicep.

**Textbooks**

- System design big archive, A Cheatsheet on Infrastructure as Code Landscape: [pages 20 to 21](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=20). Infrastructure defined in files that are versioned, tested and reused, with Terraform, CloudFormation and Ansible named, placed beside containers, orchestration and GitOps.

**Videos**

- KodeKloud, Terraform Tutorial for Beginners + Labs: Complete Step by Step Guide!, What is Infrastructure as Code?, 8:53 to 14:48: [watch](https://www.youtube.com/watch?v=YcJ9IeukJL8&t=533s). Infrastructure as code, after the chapter on traditional IT's problems and before the chapters on Terraform, HCL, state and lifecycle rules with labs. Chapter-timed.
- KodeKloud, What is Terraform? Introduction To Terraform Basics, How terraform functions, 7:48 to 9:29: [watch](https://www.youtube.com/watch?v=mzgfHmDRamk&t=468s). How Terraform works, before chapters on the resource lifecycle, providers and the CLI commands. Chapter-timed.
- KodeKloud, Infrastructure as Code (IaC) Explained: Types, Tools, and Best Practices, Infrastructure Provisioning Tools, 3:33 to 4:40: [watch](https://www.youtube.com/watch?v=IvY_o23y1zs&t=213s). Provisioning tools, Terraform's kind, after configuration management and server templating tools. Chapter-timed.

**Our plans and chapters**

- [Production by Terraform](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/17-production-by-terraform.md), system-design/devops-and-deployment, plan 17. Production declared in Terraform as an Azure Container App with its PostgreSQL, then planned, applied, destroyed and recreated with the recreate timed, and the state moved into Azure Storage.
- [Production by Terraform](/home/molef/goal-setting/learning/system-design/devops-and-deployment/textbook/17-production-by-terraform.md), the same journey, chapter 17. The compiled chapter: declaring the Container App, plan, apply and destroy, state and drift, remote state.
- [Chapter 16: Deploy, designed and not run](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/textbook/16-deploy.md), ai-engineering/product-data-validation-end-to-end, chapter 16. A Terraform template written, validated offline and never applied, beside the same box in Bicep for comparison, and what the compile proves and does not.
- [The Azure deploy, designed and not run](/home/molef/goal-setting/learning/ai-engineering/product-data-validation-end-to-end/plans/84-the-azure-design.md), the same journey, plan 84. The plan behind that chapter, running `terraform validate` with no `plan`, no `apply` and no `az login`.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. The textbook page range was read with pdftotext after finding it in the big archive's chapter table in Textbooks.md; a pdftotext search of every page of the four system design books for "terraform" and "infrastructure as code" found only roadmap lists besides it, and no back-of-book table has the term. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title, headings and the lines that name Terraform or Bicep. Left out: KodeKloud's HashiCorp Vault + Terraform and Pulumi tutorials, whose chapter lists were not read. "Bicep" was sampled in the learning tree's prose: 10 uses, all Azure's Bicep language in product-data-validation-end-to-end, so it is kept.
