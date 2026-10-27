---
aliases: [virtual private network, IPsec, site-to-site VPN, VPN tunnel]
standard: vault-note v2
---

# VPN

Up: [[Network Security]] · ⬅️ [[Firewall]]

Information Technology, Networking, Network Security. It joins two private address ranges such as a [[Virtual Private Cloud]] and an office network, and it encrypts at the network layer where [[TLS]] encrypts one connection.

**A VPN joins two private networks, or one remote machine to a private network, across the public internet, by wrapping each packet whole inside an encrypted one sent between the two ends of a tunnel.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches VPNs writes the rest around it.

## Where to learn this

**VPN**, a virtual private network. Also: IPsec, site-to-site VPN, VPN tunnel.

**Textbooks**

- Computer networking: a top-down approach, section 8.7.1, IPsec and virtual private networks (VPNs): [pages 668 to 669](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=668). A private network is costly to build from its own routers and links, so a VPN sends the institution's traffic over the public internet instead: a headquarters, a branch office and a salesperson in a hotel, plain IPv4 inside each site and IPsec datagrams between them.
- Computer networking: a top-down approach, sections 8.7.3 and 8.7.4, Security associations and the IPsec datagram: [pages 671 to 673](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=671). The tunnel worked between router R1 at headquarters (172.16.1/24) and R2 at the branch (172.16.2/24): the original datagram encrypted whole and carried behind a new IP header, which every router in between forwards as an ordinary datagram.

**Videos**

- KodeKloud, AWS Networking Basics, AWS VPC & Subnets for Beginners, Connecting Securely: VPN and Direct Connect, 15:07 to 15:55: [watch](https://www.youtube.com/watch?v=QM63dyA_4Pc&t=907s). A VPN as one of the two ways to join an AWS VPC to an office, after the chapter on the virtual private gateway. Chapter-timed.
- Hussein Nasser, VPN vs Proxy Explained Pros and Cons, What is a VPN, 1:10 to 9:56: [watch](https://www.youtube.com/watch?v=npnqyRT77Zc&t=70s). What a VPN does to a packet, before chapters on its pros and cons and on proxies. Chapter-timed.
- PowerCert Animated Videos, VPN (Virtual Private Network) Explained, VPNs for remote work, 4:18 to 5:27: [watch](https://www.youtube.com/watch?v=R-JUOpCgTZc&t=258s). The remote worker reaching the office network, after chapters on hiding an address and encrypting the traffic. Chapter-timed.

**Our plans and chapters**

- [Day 8: TLS/SSL and VPN](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/08-tls-ssl-and-vpn.md), system-design/networking, staged playbook, day 8. Site A (10.1.0.0/16) and site B (10.2.0.0/16) joined by an IPsec tunnel, with a separate client VPN path for a remote user, and WireGuard and OpenVPN named as tools.
- [Day 10: Cloud networking (VPC)](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/10-cloud-networking-vpc.md), system-design/networking, staged playbook, day 10. A VPN listed beside peering, transit gateway, PrivateLink and Direct Connect as a way to connect a VPC.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-08-tls-ssl-and-vpn.jpg"><img src="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-08-tls-ssl-and-vpn.jpg" width="140" alt="Day 08 card: TLS handshake, certificate chain, and a site-to-site VPN tunnel"></a> Tech Fusionist on X, "Day 8: TLS/SSL & VPN", from the 12-day networking playbook: [the post](https://x.com/techyoutbe/status/2074125684222685404), [what it shows](/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/README.md#the-twelve-day-cards). Section C joins Site A (10.1.0.0/16) and Site B (10.2.0.0/16) through an encrypted IPsec tunnel across the public internet, with a remote user's client VPN reaching the same tunnel.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each Kurose page range was read with pdftotext after the book's back-of-book index ("virtual private networks (VPNs)", PDF pages 667 and 668). The system design books name VPNs only in lists (System design big archive pages 377, 378 and 438), so no line comes from them. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; Hello Interview and ByteByteGo have no VPN video. Each staged topic file was read whole. Left out: Hussein Nasser's 54-minute "VPN is just NAT", which has no chapters; the data engineering plans that name a VPN as one of the network paths a Databricks ingestion gateway needs, since they use the idea without teaching it.
