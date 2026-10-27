---
aliases: [Kubernetes, k8s, pod]
link-only-in: [system-design, ai-engineering/agent-architecture, ai-engineering/tooling-deployment-route]
standard: vault-note v2
---

# Kubernetes

Up: [[Software]]

Software. It schedules containers built with [[Docker]] across a cluster of machines.

**Kubernetes runs containers across a cluster of machines and keeps the cluster at the state its manifests declare: a control plane schedules pods, the smallest unit of one or more containers, onto worker nodes and replaces them when they fail.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches Kubernetes writes the rest around it.

## Where to learn this

**Kubernetes (k8s)**, a cluster that keeps containers running as declared. Also: k8s, pod.

**Textbooks**

- System design big archive, The Lifecycle of a Kubernetes Pod: [pages 288 to 289](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=288). Works one pod from start to finish: the manifest stored in etcd, the scheduler binding it to a node, the kubelet pulling images and probing health, the phases from Pending to Succeeded, then SIGTERM and cleanup.
- System design big archive, How Kubernetes Works?: [pages 61 to 62](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=61). Manifest files in, then the control plane (API server, scheduler, controller manager, etcd) and the worker nodes (kubelet, kube-proxy, container runtime).
- System design big archive, Kubernetes Explained: [pages 297 to 298](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=297). The same parts with the pod named as the smallest deployable unit and the container runtime that runs it.
- System design big archive, Docker vs. Kubernetes. Which one should we use?: [pages 14 to 15](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=14). Docker runs containers on one host; Kubernetes manages them across a cluster, with load balancing, scaling and desired state.
- System design big archive, Top Kubernetes Scaling Strategies You Must Know: [pages 172 to 173](../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=172). Horizontal and vertical pod autoscaling, cluster autoscaling and predictive autoscaling.

**Videos**

- KodeKloud, Kubernetes Crash Course: Learn the Basics and Build a Microservice Application, Demo: Pods, 28:40 to 35:00: [watch](https://www.youtube.com/watch?v=XuSQU5Grv1g&t=1720s). Pods created and inspected live, after the chapter explaining them and before ReplicaSets, deployments and services. Chapter-timed.
- KodeKloud, Kubernetes Architecture Simplified: K8s Explained in 10 Minutes, Kubernetes Architecture, 1:07 to 4:54: [watch](https://www.youtube.com/watch?v=8C_SCDbUJTg&t=67s). The cluster's parts, before the chapter on the API server. Chapter-timed.
- ByteByteGo, Kubernetes Explained in 6 Minutes: k8s Architecture, Kubernetes Architecture, 1:01 to 6:28: [watch](https://www.youtube.com/watch?v=TlHvYWVUZyc&t=61s). The control plane and the worker nodes, after a short "what is Kubernetes". Chapter-timed.

**Our plans and chapters**

- [Kubernetes from zero: pod, deployment, service](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/18-kubernetes-from-zero.md), system-design/devops-and-deployment, plan 18. A pod, a deployment that keeps three of them and a service in front, each made with `kubectl` on a kind cluster and read back.
- [Kubernetes from zero: pod, deployment, service](/home/molef/goal-setting/learning/system-design/devops-and-deployment/textbook/18-kubernetes-from-zero.md), the same journey, chapter 18. The compiled chapter: a cluster on the laptop, pod and deployment, then the service.
- [Staging on kind: a rolling update watched pod by pod](/home/molef/goal-setting/learning/system-design/devops-and-deployment/plans/19-staging-on-kind-rolling-update.md), the same journey, plan 19. v1 then v2 deployed from the pipeline, with the rolling update replacing pods one at a time while the service keeps answering.
- [Tooling and Deployment](/home/molef/goal-setting/learning/ai-engineering/tooling-deployment-route/MASTER_PLAN.md), ai-engineering/tooling-deployment-route. Goal 4 puts a model behind a multi-replica Kubernetes service with a rolling update; it holds goals and no plans yet.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-11-kubernetes-networking.jpg"><img src="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-11-kubernetes-networking.jpg" width="140" alt="Day 11 card: Kubernetes networking, with a cluster map carrying real pod and service IPs"></a> Tech Fusionist on X, "Day 11: Kubernetes Networking", from the 12-day networking playbook: [the post](https://x.com/techyoutbe/status/2074125684222685404), [what it shows](/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/README.md#the-twelve-day-cards). Section A maps a user through an Ingress to a ClusterIP service at 10.96.0.10 and on to four pods with flat IPs, 10.244.1.2 and 10.244.1.3 on worker node 1 and 10.244.2.2 and 10.244.2.3 on node 2, section B lists ClusterIP, NodePort, LoadBalancer and Ingress, and section C names the CNI plugins and service meshes. The four are drawn as peers when they nest (NodePort builds on ClusterIP, LoadBalancer on NodePort) and Ingress is a separate object that routes to services, as the card's own map shows; kube-proxy, which carries the routing arrows, is never named ([the reading](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/11-kubernetes-networking.md#what-it-flattens)).
- <a href="/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/docker-8-day-playbook/day-8-kubernetes-and-capstone.jpg"><img src="/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/docker-8-day-playbook/day-8-kubernetes-and-capstone.jpg" width="200" alt="Day 8 card: why orchestration, a Docker-to-Kubernetes concept table, a troubleshooting ladder and a capstone diagram from Dockerfile to Ingress"></a> Tech Fusionist on X, "Docker & Containers for Cloud & DevOps, Day 8: From Docker to Kubernetes & Capstone": [the post](https://x.com/techyoutbe/status/2086017393999090067), [what it shows](/home/molef/goal-setting/learning/system-design/devops-and-deployment/artifacts/figures/docker-8-day-playbook/README.md#day-8-kubernetes-and-capstonejpg). Panel B maps five Docker ideas onto Kubernetes (container to Pod, `docker run` to Deployment, the Compose file to manifests, a Docker network to a Service plus CNI, a volume to a PersistentVolume and its claim), and panel D draws Dockerfile, CI, registry, a multi-pod Deployment, Service and Ingress in one line to users. Kubernetes is mapped here and never taught: no manifest, and only two `kubectl` commands ([the reading](/home/molef/goal-setting/learning/system-design/devops-and-deployment/sources/docker-8-day-playbook/SOURCES.md#where-it-fits-and-what-it-does-not-give)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after finding it in the big archive's chapter table in Textbooks.md; no other shelf book covers Kubernetes. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title and description. Left out: the big archive's A Cheatsheet on Kubernetes (page 210) and How to Learn Kubernetes? (page 178), which repeat the architecture or list resources. The bare word "pod" was sampled in the learning tree's prose: 72 uses, 49 of them the Kubernetes pod in system-design journeys and 19 a customer connection's monthly consumption in mathematics/statistics, so `link-only-in` keeps "pod" linking only in system-design and the two ai-engineering journeys that use it for Kubernetes; "Kubernetes" and "k8s" link everywhere.
