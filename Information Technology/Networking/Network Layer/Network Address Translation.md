---
aliases: [NAT, NAT gateway, NAT table, NAT translation table, SNAT, DNAT]
standard: vault-note v2
---

# Network Address Translation

Up: [[Network Layer]] · ⬅️ [[DHCP]]

Information Technology, Networking, Network Layer. It sits at the edge of a private [[Subnet]], the router running it usually runs [[DHCP]] too, and a [[Virtual Private Cloud]]'s private subnets reach the internet through a NAT gateway.

**Network address translation rewrites the private source address and port of outgoing packets to one public address and a fresh port, and keeps a table so each reply finds its way back to the machine that asked.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches NAT writes the rest around it.

## Where to learn this

**Network address translation (NAT)**, many private addresses behind one public one. Also: NAT, NAT gateway, NAT translation table, SNAT, DNAT.

**Textbooks**

- Computer networking: a top-down approach, section 4.3.4, Network address translation (NAT): [pages 375 to 377](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=375). Works one request through a home router: host 10.0.0.1 at port 3345 asks web server 128.119.40.186 on port 80, the router rewrites the source to 138.76.29.7 at port 5001 and records the pair in its NAT translation table, and the reply is translated back, after the private 10.0.0.0/8 range and before the objections to NAT and NAT traversal.
- Computer networking: a top-down approach, section 6.6, Data center networking, load balancing: [pages 526 to 527](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=526). The same translation run in the other direction: a data centre's load balancer turns the public address a client used into the chosen host's internal address, and back again for the reply.
- System design big archive, Modem vs. Router: [pages 409 to 410](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=409). The home router sharing the modem's one public address across every device with NAT, each device on a private 192.168.1.x address, and the router tracking which device asked for what.

**Videos**

- KodeKloud, How Docker Networking Actually Works, Outbound Journey: Reaching the Internet with NAT, 4:11 to 6:00: [watch](https://www.youtube.com/watch?v=W7X6u2BGVRY&t=251s). A container's packet leaving through the host with its address translated, followed by a chapter on why the way in is closed. Chapter-timed.
- KodeKloud, AWS Networking Basics, AWS VPC & Subnets for Beginners, Internet Gateway vs NAT Gateway Explained, 11:51 to 14:00: [watch](https://www.youtube.com/watch?v=QM63dyA_4Pc&t=711s). The cloud's managed NAT gateway set against the internet gateway, after the chapter on public and private subnets. Chapter-timed.
- Hussein Nasser, Network Address Translation - NAT Explained, How NAT works, 7:43 to 17:26: [watch](https://www.youtube.com/watch?v=RG97rvw1eUo&t=463s). The translation itself, after a chapter on how machines inside one network talk, and before chapters on what NAT is used for. Chapter-timed.

**Our plans and chapters**

- [Day 5: DHCP, NAT and gateways](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/05-dhcp-nat-and-gateways.md), system-design/networking, staged playbook, day 5. Three devices' ports mapped onto 203.0.113.5 ports 62000 to 62002 in a printed translation table, then inbound port forwarding as the one-to-one case.
- [Day 10: Cloud networking (VPC)](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/10-cloud-networking-vpc.md), system-design/networking, staged playbook, day 10. A private subnet's default route pointing at a NAT gateway, so its servers can reach out and nothing outside can open a connection in.
- [Days 3 and 4: Networking and storage](/home/molef/goal-setting/learning/system-design/devops-and-deployment/sources/docker-8-day-playbook/topics/day-3-4-networking-and-storage.md), system-design/devops-and-deployment, staged Docker playbook, days 3 and 4. Docker's default bridge network, its containers translated out through the host.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-05-dhcp-nat-and-gateways.jpg"><img src="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-05-dhcp-nat-and-gateways.jpg" width="140" alt="Day 05 card: DHCP leases, NAT translation with ports, and the default gateway"></a> Tech Fusionist on X, "Day 5: DHCP, NAT & Gateways", from the 12-day networking playbook: [the post](https://x.com/techyoutbe/status/2074125684222685404), [what it shows](/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/README.md#the-twelve-day-cards). Section B's SNAT half maps three private sockets (192.168.1.10:51514, .11:51515 and .12:51516) onto the one public address 203.0.113.5 on ports 62000 to 62002 through a translation table, and its DNAT half forwards public port 80 to the web server at 192.168.1.20:80. The CGNAT sticky note leaves out its consequence: behind ISP-level NAT, the inbound port forward in the DNAT half does not work ([the reading](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/05-dhcp-nat-and-gateways.md#what-it-flattens)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each Kurose page range was read with pdftotext after the book's back-of-book index ("network address translation (NAT)", PDF page 375; "NAT translation table", 376; "load balancers", 526). The big archive page came from a page-text search for "NAT" across the four system design books; its one other mention (page 239) names NAT gateways in a list of AWS services. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each staged topic file was read whole. Every use of "NAT" in the learning tree was read before the alias went in: all of them mean address translation.
