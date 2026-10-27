---
aliases: [dynamic host configuration protocol, DHCP lease, DHCP server]
standard: vault-note v2
---

# DHCP

Up: [[Network Layer]] · ⬅️ [[Routing Table]] · [[Network Address Translation]] ➡️

Information Technology, Networking, Network Layer. It hands out addresses from a [[Subnet]], its messages travel over [[UDP]], and the default gateway and [[DNS]] server it names are the first places a new machine sends traffic.

**DHCP is how a machine joining a network gets its IP address, subnet mask, default gateway and DNS server automatically, in four messages: discover, offer, request and acknowledge.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches DHCP writes the rest around it.

## Where to learn this

**DHCP**, the dynamic host configuration protocol. Also: DHCP lease, DHCP server.

**Textbooks**

- Computer networking: a top-down approach, section 4.3.3, Obtaining a host address: the Dynamic Host Configuration Protocol: [pages 372 to 375](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=372). What DHCP hands over (an address, the subnet mask, the default gateway and the local DNS server), then the four messages between an arriving client and the server at 223.1.2.5 with a 3,600-second lease, the lease renewal, and why moving between subnets breaks an open TCP connection.
- Computer networking: a top-down approach, section 6.7.1, Getting started: DHCP, UDP, IP, and Ethernet: [pages 530 to 532](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=530). A laptop plugged into a school network asks for its address before anything else: the DHCP request inside a UDP segment from port 68 to port 67, broadcast over Ethernet, and the ACK that returns its address, gateway and DNS server.
- System design big archive, Modem vs. Router: [pages 409 to 410](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=409). The home router giving a phone a private address such as 192.168.1.x the moment it joins the WiFi.

**Videos**

- Hussein Nasser, How DNS and DHCP Servers Communicate (With wireshark), DHCP Discover, 6:30 to 14:40: [watch](https://www.youtube.com/watch?v=FYcO4ZshG8Q&t=390s). The discover message read in a Wireshark capture, followed by one chapter each on the offer, the request and the ACK. Chapter-timed.
- Hussein Nasser, How DNS and DHCP Servers Communicate (With wireshark), How DHCP Updates DNS, 22:00 to 26:15: [watch](https://www.youtube.com/watch?v=FYcO4ZshG8Q&t=1320s). How the DHCP server tells DNS the name of the machine it just gave an address to. Chapter-timed.
- PowerCert Animated Videos, DHCP Explained - Dynamic Host Configuration Protocol, DHCP Lease, 4:35 to 5:11: [watch](https://www.youtube.com/watch?v=e6-TaH5bkjo&t=275s). The lease, after the chapters on static against dynamic addresses and the server's scope. Chapter-timed.

**Our plans and chapters**

- [Day 5: DHCP, NAT and gateways](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/05-dhcp-nat-and-gateways.md), system-design/networking, staged playbook, day 5. The four DORA messages and what DHCP hands over, address, mask, gateway and DNS, with the note that the card leaves out the lease time.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-05-dhcp-nat-and-gateways.jpg"><img src="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-05-dhcp-nat-and-gateways.jpg" width="140" alt="Day 05 card: DHCP leases, NAT translation with ports, and the default gateway"></a> Tech Fusionist on X, "Day 5: DHCP, NAT & Gateways", from the 12-day networking playbook: [the post](https://x.com/techyoutbe/status/2074125684222685404), [what it shows](/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/README.md#the-twelve-day-cards). Section A draws DORA, the four messages Discover, Offer, Request and Acknowledge between a client and a DHCP server, and a sticky note lists what the server hands out: an IP, a mask, a gateway and DNS. Discover and Request are broadcasts, which the card says in text and draws as point-to-point arrows, and the lease time, the DHCP setting that causes operational trouble, is absent ([the reading](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/05-dhcp-nat-and-gateways.md#what-it-flattens)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each Kurose page range was read with pdftotext after the book's back-of-book index ("Dynamic Host Configuration Protocol", PDF page 372; "DHCP request message", 374 and 531). The big archive page came from a page-text search for "DHCP" across the four system design books; its other mentions (pages 49, 118, 377, 378 and 438) only name DHCP in a list of ports or protocols. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; Hello Interview, ByteByteGo and KodeKloud have no video on DHCP. The staged topic file was read whole. "DORA" is not an alias, because the CI/CD source in system-design/devops-and-deployment uses it for the DORA delivery metrics.
