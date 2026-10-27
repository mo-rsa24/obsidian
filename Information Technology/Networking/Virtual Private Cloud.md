---
aliases: [VPC, VNet, VPC peering]
standard: vault-note v2
---

# Virtual Private Cloud

Up: [[Networking]]

Information Technology, Networking. A VPC is assembled from parts with notes of their own: its address range is split into each [[Subnet]], a [[Routing Table]] per subnet decides where traffic leaves, [[Network Address Translation]] lets private servers reach out, a [[Firewall]] in the form of security groups and network ACLs filters what comes in, and a [[VPN]] joins it to an office.

**A virtual private cloud is a private network carved out of a cloud provider's data centre: you choose its address range and split it into subnets, and its route tables, gateways and security groups decide what can reach what.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches VPCs writes the rest around it.

## Where to learn this

**Virtual private cloud (VPC)**, your own network inside a cloud provider. Also: VPC, VNet (Azure's name for it), VPC peering.

**Textbooks**

- Computer networking: a top-down approach, section 8.7.1, IPsec and virtual private networks (VPNs): [pages 668 to 669](../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=668). The book predates the cloud VPC and teaches the idea under it: an institution's private network, costly to build as separate routers and links, provided instead over shared infrastructure with its traffic kept apart.
- Computer networking: a top-down approach, section 4.3.3, IPv4 addressing: [pages 365 to 368](../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=365). The subnets a VPC is cut into, worked as 223.1.1.0/24, 223.1.2.0/24 and 223.1.3.0/24 behind one router.
- Computer networking: a top-down approach, section 4.3.4, Network address translation (NAT): [pages 375 to 377](../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=375). The private address ranges reserved for networks like a VPC, 10.0.0.0/8 among them, and the translation a NAT gateway does for a private subnet.

**Videos**

- KodeKloud, AWS Networking Basics, AWS VPC & Subnets for Beginners, What is a Virtual Private Cloud (VPC)?, 0:54 to 5:47: [watch](https://www.youtube.com/watch?v=QM63dyA_4Pc&t=54s). What an AWS VPC is, before chapters on public and private subnets, the internet and NAT gateways, the virtual private gateway, and VPN and Direct Connect. Chapter-timed.
- KodeKloud, AWS Networking Basics, AWS VPC & Subnets for Beginners, AWS Networking - Summary, 15:55 to 17:47: [watch](https://www.youtube.com/watch?v=QM63dyA_4Pc&t=955s). The whole VPC put back together after its parts. Chapter-timed.

**Our plans and chapters**

- [Day 10: Cloud networking (VPC)](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/10-cloud-networking-vpc.md), system-design/networking, staged playbook, day 10. A 10.0.0.0/16 VPC across two availability zones with a public and a private /24 in each, their two route tables printed in full, the ways to connect a VPC to others, and the AWS, Azure and Google names for it.
- [Day 11: Kubernetes networking](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/11-kubernetes-networking.md), system-design/networking, staged playbook, day 11. The cluster of the capstone running in the private subnets of day 10's VPC.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-10-cloud-networking-vpc.jpg"><img src="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-10-cloud-networking-vpc.jpg" width="140" alt="Day 10 card: a two-zone VPC with public and private subnets, route tables and gateways"></a> Tech Fusionist on X, "Day 10: Cloud Networking (VPC)", from the 12-day networking playbook: [the post](https://x.com/techyoutbe/status/2074125684222685404), [what it shows](/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/README.md#the-twelve-day-cards). Section A draws a 10.0.0.0/16 VPC across two availability zones with public subnets 10.0.1.0/24 and 10.0.2.0/24 and private subnets 10.0.3.0/24 and 10.0.4.0/24, and two route tables make the difference: the public one sends 0.0.0.0/0 to the internet gateway and the private one sends it to a NAT gateway. It draws an internet gateway in each zone, while AWS has one per VPC (the NAT gateway really is per zone), and its practice of one NAT gateway for two zones gives up the high availability its own sticky note promises ([the reading](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/10-cloud-networking-vpc.md#what-it-flattens)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Kurose names no cloud VPC: a search of the whole book for "VPC" and "virtual private cloud" found nothing, so its lines point at the private network, subnet and NAT pages a VPC is built from, read with pdftotext after the back-of-book index ("virtual private networks (VPNs)", PDF page 668; "subnets", 365; "network address translation (NAT)", 375). The system design books name VPCs only in lists of AWS services (System design big archive pages 146, 154, 239, 384 and 385), so no line comes from them. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; Hello Interview and ByteByteGo have no VPC video. Each staged topic file was read whole.
