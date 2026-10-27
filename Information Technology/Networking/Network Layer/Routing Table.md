---
aliases: [route table, forwarding table, longest prefix match, longest prefix matching]
link-skip: [one column of prices]
standard: vault-note v2
---

# Routing Table

Up: [[Network Layer]] · ⬅️ [[Subnet]] · [[DHCP]] ➡️

Information Technology, Networking, Network Layer. Its rows are written as [[Subnet]] prefixes. An [[API Gateway]] keeps a table of its own one layer up, keyed by URL path, which is [[Gateway Routing]].

**A routing table maps a destination prefix to where traffic goes next, and the longest matching prefix wins, in a router choosing the outgoing link for each packet.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches routing tables writes the rest around it.

## Where to learn this

**Routing table**, destination prefix to next hop. Also: route table, forwarding table, longest prefix match.

**Textbooks**

- Computer networking: a top-down approach, section 4.2.1, Input port processing and destination-based forwarding: [pages 346 to 347](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=346). Works a router with four links: three address ranges collapse into a four-row prefix table, one destination address is matched against it, and the longest prefix matching rule settles an address that matches two rows.
- Computer networking: a top-down approach, section 4.1.1, Forwarding and routing: the data and control planes: [pages 338 to 339](../../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=338). The forwarding table every router holds, a header value of 0110 indexed to interface 2, then forwarding (one router, nanoseconds) set against routing (the whole network, seconds), the step that fills the tables.
- System design big archive, Network debugging commands every engineer should know: [pages 433 to 434](../../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=433). `ip route` printing the machine's own routing table, to confirm which gateway and next hop a packet will take.

**Videos**

- Hussein Nasser, How a Machine Becomes a Router, Acting Like a Router, 9:00 to 11:30: [watch](https://www.youtube.com/watch?v=hVyI4ppUZRs&t=540s). A Linux machine forwarding packets that are not addressed to it, after chapters on matching layer 2 and layer 3 addresses, and before one on acting as a firewall. Chapter-timed.

**Our plans and chapters**

- [Day 6: Routing and switching](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/06-routing-and-switching.md), system-design/networking, staged playbook, day 6. A router's table ending in a default route 0.0.0.0/0, and the longest prefix match worked for 10.0.0.55 against a /24, a /16 and the default, then `ip route` and `traceroute` as practice.
- [Day 10: Cloud networking (VPC)](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/10-cloud-networking-vpc.md), system-design/networking, staged playbook, day 10. A VPC's public and private route tables printed side by side, differing only in where 0.0.0.0/0 goes: an internet gateway or a NAT gateway.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-06-routing-and-switching.jpg"><img src="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-06-routing-and-switching.jpg" width="140" alt="Day 06 card: routing tables with metrics, longest-prefix match, and switching"></a> Tech Fusionist on X, "Day 6: Routing & Switching", from the 12-day networking playbook: [the post](https://x.com/techyoutbe/status/2074125684222685404), [what it shows](/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/README.md#the-twelve-day-cards). Section B gives one router's table with destination, prefix, next hop, interface and metric, ending in the default route 0.0.0.0/0, then matches destination 10.0.0.55 against 10.0.0.0/24, 10.0.0.0/16 and 0.0.0.0/0, where the /24 wins as the longest prefix. The 10.0.0.0/16 candidate does not match the router's own interfaces (G0/1 is 172.16.0.1/16), so the two halves of section B cannot be reconciled, and BGP is named beside OSPF with no word that BGP runs between autonomous systems ([the reading](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/06-routing-and-switching.md#what-it-flattens)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each Kurose page range was read with pdftotext after the book's back-of-book index ("forwarding tables", PDF pages 338 and 339; "longest prefix matching rule", 347). Kurose keeps "routing table" for a routing algorithm's own state (pages 416 and 431) and calls the router's lookup table the forwarding table, which is what the tree's "routing table" means, so the card follows the forwarding pages. The big archive pages came from a page-text search for "routing table" and from the API Gateway card's own source. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only; Hussein Nasser's Network Routing Crash Course is members-only and was left out. Each plan, chapter and staged topic file was read at its title, description and the section named. The skip phrase keeps the one-business journey's model routing table, which picks an LLM provider by price, plain.
