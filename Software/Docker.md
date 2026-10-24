---
aliases: [Docker, Docker image, Dockerfile, Docker container, Docker Compose, containerization]
standard: vault-note v2
---

# Docker

Up: [[Software]]

Software. [[Kubernetes]] runs Docker-built images across a cluster, and [[Nginx]] and [[Redis]] are the images our plans most often start beside an app.

**Docker packages an application and its dependencies into an image, built from a Dockerfile, and runs that image as a container: an isolated process sharing the host's kernel, with Docker Compose starting several of them together.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches Docker writes the rest around it.

## Where to learn this

**Docker**, images and the containers that run them. Also: Dockerfile, Docker image, Docker container, Docker Compose, containerization.

**Textbooks**

- System design big archive, Docker vs Kubernetes: [page 349](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=349). Works the path one app takes: code and dependencies written into a Dockerfile, built into a portable image, run by a container runtime on the host, and networked to other services.
- System design big archive, How does Docker Work?: [page 265](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=265). The three parts: the client you type into, the host whose daemon manages images, containers, networks and volumes, and the registry that stores images.
- System design big archive, Virtualization vs. Containerization: [pages 401 to 402](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=401). Why a container starts in milliseconds and a VM in minutes: containers share the host kernel and are isolated processes, while each VM boots its own operating system.
- System design big archive, 9 Docker Best Practices You Should Know: [pages 295 to 296](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=295). Pinned image versions, multi-stage builds, `.dockerignore`, a non-root user, step order for the layer cache, and image scanning.

**Videos**

- KodeKloud, Learn Docker in 2 Hours: A Full Tutorial (2025), An introduction to Docker Commands, 20:00 to 42:06: [watch](https://www.youtube.com/watch?v=zJ6WbK9zFpI&t=1200s). The everyday Docker commands, after the overview and the install, before chapters on images, networking, storage and Compose. Chapter-timed.
- KodeKloud, What are Containers? Containerization Explained, Containers vs Virtual Machines, 7:45 to 9:34: [watch](https://www.youtube.com/watch?v=ZWReEReO2xE&t=465s). Containers set against virtual machines, after the chapter on containers sharing the host kernel. Chapter-timed.
- KodeKloud, Docker Compose Tutorial, Building a Docker Compose File: Services and Images, 8:49 to 10:13: [watch](https://www.youtube.com/watch?v=iOGEBj7Ozak&t=529s). A sample voting app's `docker run` commands turned into a Compose file of services and images. Chapter-timed.
- ByteByteGo, System Design: Why Is Docker Important?, Building Docker images, 0:36 to 1:21: [watch](https://www.youtube.com/watch?v=QEzbZKtLi-g&t=36s). Building an image from a Dockerfile, before the chapters on containers, registries, volumes and Compose. Chapter-timed.

**Our plans and chapters**

- [Docker from zero: a container is a process](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/10-docker-from-zero.md), system-design/devops-and-deployment, plan 10. Pull and run an image, publish a port, read its logs, then find the same container from the host as an ordinary process.
- [The Dockerfile: layers, cache, multi-stage](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/11-the-dockerfile-layers-cache-multi-stage.md), the same journey, plan 11. The bookshop's own Dockerfile, timed on a cache hit against a miss, and the size a multi-stage build saves.
- [What an image, a container, a volume and a network are](/home/molef/goal-setting/learning/data-engineering/many-sources-one-lakehouse/plans/10-b1-containers.md), data-engineering/many-sources-one-lakehouse, plan 10. The four words each run and watched, including a container deleted with data in it.
- [Docker and Compose on the corner shop](/home/molef/goal-setting/learning/system-design/foundations/plans/07-docker-and-compose-on-the-corner-shop.md), system-design/foundations, plan 07. PostgreSQL started from an image with the shop's schema and seed, then the shop's services found by name under Compose.
- [Compose: app, Postgres and the seed up from an empty folder with one command](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/71-compose-from-an-empty-folder.md), ai-engineering/one-business-end-to-end, plan 71. The Django app and its database brought up together by one `docker compose` command.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after finding it in the big archive's chapter table in Textbooks.md; System design interview names Docker once in its closing reading list and no other shelf book covers it. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan was read at its title and description. Left out: the big archive's Docker vs. Kubernetes. Which one should we use? (pages 14 to 15) and Virtualization vs Containerization (pages 112 to 113), shorter passes over the same ground; [Docker basics](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/19-docker-basics.md) in the Attica rebuild and [the Dockerfile](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/70-the-dockerfile.md) in one-business-end-to-end, which cover what the listed plans already do. The bare word "container" is not an alias because it also names CSS and Python containers; "containerization" has 5 prose uses in the learning tree, all meaning packaging an app with Docker.
