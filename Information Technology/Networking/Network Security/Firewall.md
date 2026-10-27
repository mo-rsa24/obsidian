---
aliases: [security group, network ACL, NACL, packet filter, stateful firewall, web application firewall, WAF]
link-skip: [injection and the firewall, "IBM Technology, the firewall"]
standard: vault-note v2
---

# Firewall

Up: [[Network Security]] · [[VPN]] ➡️

Information Technology, Networking, Network Security. Its rules are written in [[Subnet]] ranges and ports, and a [[Virtual Private Cloud]] carries two kinds of it: a network ACL on each subnet and a security group on each server.

**A firewall sits at a network's edge or on a host and lets each packet through or drops it by rules on its addresses, ports and protocol, and a stateful one also remembers which connections are already open so their replies pass.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches firewalls writes the rest around it.

## Where to learn this

**Firewall**, the checkpoint at a network's edge. Also: security group, network ACL, packet filter, stateful firewall, web application firewall.

**Textbooks**

- Computer networking: a top-down approach, section 8.9.1, Firewalls, traditional packet filters: [pages 681 to 684](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=681). A firewall's three goals, then filtering worked on one organisation's network 130.207/16: each policy beside its rule (drop every incoming TCP SYN except to the web server 130.207.244.203 on port 80, drop incoming UDP except DNS), and the access control list a router reads top to bottom.
- Computer networking: a top-down approach, section 8.9.1, Firewalls, stateful packet filters and application gateways: [pages 684 to 688](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=684). A stateful filter's connection table, which lets a reply through only when it belongs to a connection already open, and the application gateway that filters by user and application. A cloud network ACL is the stateless kind and a security group the stateful kind.
- System design big archive, What is a Firewall?: [pages 407 to 408](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=407). The network firewall at the edge, filtering at layers 3 and 4 by address, protocol and port, set against the host-based firewall on each laptop or server, filtering at layers 3 to 7.

**Videos**

- KodeKloud, Firewall & Port Basics EVERY DevOps Engineer Must Know, Types of Firewalls, 0:53 to 2:33: [watch](https://www.youtube.com/watch?v=w7p7pK0Kcxs&t=53s). The kinds of firewall, after a short chapter on what a firewall is and before chapters on ports and opening them. Chapter-timed.
- KodeKloud, NGINX Firewall Setup Explained, UFW Firewall Tutorial, Enabling UFW & Opening Ports, 2:25 to 4:23: [watch](https://www.youtube.com/watch?v=SwT6LTDuEzI&t=145s). UFW switched on in front of nginx and its ports opened one rule at a time, followed by a chapter on keeping SSH's port 22 open. Chapter-timed.
- Hussein Nasser, How a Machine Becomes a Router, Acting Like a Firewall, 11:30 to 12:55: [watch](https://www.youtube.com/watch?v=hVyI4ppUZRs&t=690s). The same Linux machine that forwards packets choosing to drop some, after the chapter on acting like a router. Chapter-timed.

**Our plans and chapters**

- [Day 7: Firewalls, security groups and network ACLs](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/07-firewalls-sg-and-nacls.md), system-design/networking, staged playbook, day 7. A packet's path through the subnet's network ACL and then the instance's security group, the two compared in five rows (stateful or stateless, the scope, allow and deny rules, return traffic, evaluation order), and a security group written as two rules.
- [Day 12: Troubleshooting and the capstone](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/12-troubleshoot-and-capstone.md), system-design/networking, staged playbook, day 12. The firewall as the fifth rung of the bottom-up debugging ladder, after the link, the address, the route and DNS.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-07-firewalls-sg-and-nacls.jpg"><img src="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-07-firewalls-sg-and-nacls.jpg" width="140" alt="Day 07 card: firewalls, security groups and network ACLs, compared across five properties"></a> Tech Fusionist on X, "Day 7: Firewalls, SG & NACLs", from the 12-day networking playbook: [the post](https://x.com/techyoutbe/status/2074125684222685404), [what it shows](/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/README.md#the-twelve-day-cards). Section A puts two checkpoints in series on a packet's way in, the subnet's network ACL and then the instance's security group, and section B compares them on five rows: the security group is stateful, instance-level and allow-only, and the network ACL is stateless, subnet-level, takes deny rules and is evaluated in rule-number order. The packet path is drawn inbound only, so the security group's default allow-all egress never appears, and the rule numbering that makes network ACL deny rules take effect is named and never explained ([the reading](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/07-firewalls-sg-and-nacls.md#what-it-flattens)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each Kurose page range was read with pdftotext after the book's back-of-book index ("firewalls", PDF page 681; "traditional packet filters", 682; "stateful filters", 682 and 684; "access control lists", 684 and 686; "application gateways", 686 and 689). The big archive pages came from a page-text search for "firewall" across the four system design books; the other books only name firewalls in passing. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; Hello Interview and ByteByteGo have no firewall video. Each staged topic file was read whole. The skip phrases keep a prompt-injection "firewall" (an IBM Technology video cited in a retrieval-augmented generation plan) unlinked.
