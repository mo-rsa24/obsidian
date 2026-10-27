---
aliases: [subnetting, subnet mask, CIDR, CIDR block, CIDR notation, public subnet, private subnet]
standard: vault-note v2
---

# Subnet

Up: [[Network Layer]] · [[Routing Table]] ➡️

Information Technology, Networking, Network Layer. A [[Routing Table]] is written in subnets, [[DHCP]] hands out addresses from one, and a [[Virtual Private Cloud]] is split into public and private ones.

**A subnet is a block of IP addresses sharing one prefix, written in CIDR form such as 10.0.1.0/24, whose machines reach each other directly without a router between them.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches subnets writes the rest around it.

## Where to learn this

**Subnet**, a block of addresses with one prefix. Also: subnetting, subnet mask, CIDR, public subnet, private subnet.

**Textbooks**

- Computer networking: a top-down approach, section 4.3.3, IPv4 addressing: [pages 365 to 368](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=365). Works one router joining three subnets: 223.1.1.0/24 holds three hosts and the router's interface 223.1.1.4, the /24 subnet mask says the leftmost 24 bits name the subnet, and detaching every interface into islands finds six subnets among three routers.
- Computer networking: a top-down approach, section 4.3.3, IPv4 addressing, CIDR and obtaining a block of addresses: [pages 367 to 371](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=367). CIDR's a.b.c.d/x form and its prefix, why the old class A, B and C networks of exactly 8, 16 or 24 bits wasted addresses, and an ISP's 200.23.16.0/20 split into eight /23 blocks for eight organisations.

**Videos**

- KodeKloud, AWS Networking Basics, AWS VPC & Subnets for Beginners, Understanding Subnets: Public vs Private, 5:47 to 11:51: [watch](https://www.youtube.com/watch?v=QM63dyA_4Pc&t=347s). Subnets inside an AWS VPC, and what makes one public and another private, after the chapter on the VPC itself. Chapter-timed.
- Practical Networking, How to solve ANY Subnetting Problems in 60 seconds or less, Example 1 - 10.1.1.55 /28, 0:44 to 3:21: [watch](https://www.youtube.com/watch?v=5-wlfAdcmFQ&t=44s). One address and prefix worked out to its subnet by hand, followed by a second example on 10.1.1.27 /29. Chapter-timed.
- Practical Networking, What is Subnetting? - Subnetting Mastery - Part 1 of 7, What are CIDR notations and Subnet Masks?, 2:31 to 3:15: [watch](https://www.youtube.com/watch?v=BWZ-MHIhqjM&t=151s). The two ways of writing a subnet's size, between chapters on how many addresses a subnet holds and what its network ID is. Chapter-timed.

**Our plans and chapters**

- [Day 2: IP addressing and subnetting](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/02-ip-addressing-and-subnetting.md), system-design/networking, staged playbook, day 2. Splits 192.168.1.0/24 into four /26s with every host range and broadcast address, prints the CIDR table from /24 to /28, and sets 10.0.0.0/16 into four /18s as practice.
- [Day 10: Cloud networking (VPC)](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/10-cloud-networking-vpc.md), system-design/networking, staged playbook, day 10. Four /24 subnets inside a 10.0.0.0/16 VPC, where a subnet is public only because its route table sends 0.0.0.0/0 to an internet gateway.
- [Days 3 and 4: Networking and storage](/home/molef/goal-setting/learning/system-design/devops-and-deployment/sources/docker-8-day-playbook/topics/day-3-4-networking-and-storage.md), system-design/devops-and-deployment, staged Docker playbook, days 3 and 4. The default bridge's 172.17.0.0/16 set against a user-defined network, which gets a subnet of its own.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-02-ip-addressing-and-subnetting.jpg"><img src="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-02-ip-addressing-and-subnetting.jpg" width="140" alt="Day 02 card: IP addressing and subnetting, worked as a /24 split into four /26s"></a> Tech Fusionist on X, "Day 2: IP Addressing & Subnetting", from the 12-day networking playbook: [the post](https://x.com/techyoutbe/status/2074125684222685404), [what it shows](/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/README.md#the-twelve-day-cards). Section C writes 192.168.1.0/24 as 24 network bits and 8 host bits and splits it into four /26s, each with its host range and broadcast address (192.168.1.0/26 holds hosts .1 to .62 and broadcasts on .63), and section D tabulates /24 to /28 with usable hosts falling from 254 to 14. The usable-hosts rule 2^(host bits) minus 2 stops holding at /31 and /32, which the table leaves out, and IPv6, which opens the card, has no broadcast address at all ([the reading](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/02-ip-addressing-and-subnetting.md#what-it-flattens)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each Kurose page range was read with pdftotext after the book's back-of-book index ("subnets", PDF page 365; "subnet mask", 366; "Classless Interdomain Routing (CIDR)", 367). A page-text search for "subnet" and "CIDR" across the four system design books found only a storage subnetwork in Systems analysis and design, so no line comes from them. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; Hello Interview and ByteByteGo have no video on subnets. Each staged topic file was read whole.
