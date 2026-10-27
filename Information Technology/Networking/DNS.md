---
aliases: [DNS, domain name system, DNS lookup, DNS record, DNS resolver, DNS query]
standard: vault-note v2
---

# DNS

Up: [[Networking]]

Information Technology, Networking. A DNS answer is cached for its [[Time To Live]], its queries usually travel over [[UDP]], and the address it returns is where the [[HTTP]] request goes next.

**DNS is the internet's directory: a resolver turns a name such as shop.test into an IP address by asking the root, top-level-domain and authoritative name servers in turn, caching each answer for its time to live.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches DNS writes the rest around it.

## Where to learn this

**DNS**, the domain name system. Also: DNS lookup, DNS record, DNS resolver, domain name system.

**Textbooks**

- Computer networking: a top-down approach, section 2.4.2, Overview of how DNS works: [pages 159 to 164](../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=159). The root, top-level-domain and authoritative servers and the local DNS server, then one lookup worked end to end: cse.nyu.edu asks its local server dns.nyu.edu for gaia.cs.umass.edu, which asks a root server, the edu server and dns.umass.edu in turn, 10 DNS messages in all with both recursive and iterative queries, and the caching that lets most lookups skip the root.
- Computer networking: a top-down approach, section 2.4.3, DNS records and messages: [pages 165 to 168](../../Mathematics/references/textbooks/system-design/computer-networking-a-top-down-approach.pdf#page=165). The resource record as (Name, Value, Type, TTL), the A, NS, CNAME and MX types each with an example, the query and reply message format, and how a new domain's records are inserted.
- System design big archive, How DNS Works: [pages 423 to 424](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=423). Works one lookup step by step: the browser and OS caches miss, the resolver asks a root server, then the .com TLD server, then the authoritative server, whose A record answers 172.67.21.11 for bytebytego.com, cached on the way back.
- System design big archive, What happens when you type a URL into a browser?: [pages 254 to 255](../../Mathematics/references/textbooks/system-design/system-design-big-archive.pdf#page=254). DNS as the first step of loading a page: the cache layers checked in order, the recursive lookup, then the TCP connection and HTTPS request that use the address.
- System design interview, chapter 1, Scale from zero to millions of users: [page 7](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=7). DNS in the simplest design: usually a paid third-party service, returning 15.125.23.214 for api.mysite.com before any HTTP request is sent.
- System design interview, chapter 9, Design a web crawler: [page 146](../../Mathematics/references/textbooks/system-design/system-design-interview.pdf#page=146). The DNS resolver as a bottleneck, at 10 ms to 200 ms a lookup with threads blocked behind it, and a local DNS cache refreshed by cron jobs as the fix.

**Videos**

- ByteByteGo, Everything You Need to Know About DNS: Crash Course System Design #4, The DNS query process, 2:47 to 4:04: [watch](https://www.youtube.com/watch?v=27r4Bzuj5NQ&t=167s). One query through the resolver and the name servers, after the chapters on DNS's components and hierarchy. Chapter-timed.
- ByteByteGo, Everything You Need to Know About DNS: Crash Course System Design #4, Managing DNS records, 4:04 to 5:08: [watch](https://www.youtube.com/watch?v=27r4Bzuj5NQ&t=244s). The records a domain owner manages. Chapter-timed.
- Hussein Nasser, DNS is beautiful, How DNS works (Details), 7:40 to 15:44: [watch](https://www.youtube.com/watch?v=tgWx81_NGcg&t=460s). The detailed resolution, followed by a chapter on why DNS uses UDP and others on poisoning and abuse. Chapter-timed.
- Arpit Bhayani, How DNS really works and how it scales infinitely?, Resolution process, 8:02 to 16:35: [watch](https://www.youtube.com/watch?v=g_gKI2HCElk&t=482s). The resolution process, after chapters on zones, authoritative name servers and the resolver. Chapter-timed.

**Our plans and chapters**

- [dnsmasq answers shop.test](/home/molef/goal-setting/learning/system-design/foundations/plans/08-dnsmasq-answers-shop-test.md), system-design/foundations, plan 08. A dnsmasq container answers `shop.test` with the balancer's address, read with `dig @localhost shop.test` down to the answer's TTL.
- [Preflight: the tools answering](/home/molef/goal-setting/learning/system-design/foundations/textbook/00-preflight-docker-mkcert-dig-dbeaver.md), system-design/foundations, chapter 00, section 0.3. Installs dig, the DNS question-asker, and adds the Windows hosts-file line Chrome needs, since dnsmasq answers WSL only.
- [HTTPS, and three round trips](/home/molef/goal-setting/learning/system-design/foundations/plans/09-https-and-three-round-trips.md), system-design/foundations, plan 09. Times the DNS lookup with `curl -w` as the first of the three round trips a new connection pays.

**Figures**

- <a href="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-04-dns.jpg"><img src="/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/day-04-dns.jpg" width="140" alt="Day 04 card: DNS resolution, record types, and where a lookup is cached"></a> Tech Fusionist on X, "Day 4: DNS Deep Dive", from the 12-day networking playbook: [the post](https://x.com/techyoutbe/status/2074125684222685404), [what it shows](/home/molef/goal-setting/learning/system-design/networking/artifacts/figures/twelve-day-playbook/README.md#the-twelve-day-cards). Section A walks one lookup in five steps from the browser's stub resolver through the recursive resolver, the root, the .com TLD server and the authoritative server to 93.184.216.34, section B tabulates eight record types from A to PTR, and section C caches the answer for its TTL. It draws one cache at the resolver, while the browser, the operating system and each step of the chain also cache, which is why a TTL change does not take effect everywhere at once; negative caching is absent ([the reading](/home/molef/goal-setting/learning/system-design/networking/sources/twelve-day-playbook/topics/04-dns.md#what-it-flattens)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read with pdftotext after the chapter tables in `Textbooks.md` and a page-text search for "DNS" across the four system design books. Each video's chapter list was read with `cache-video-chapters.py`, and each line is described from its chapter title and the video title only. Each plan and chapter was read at its title, description and the section named. Left out: Grokking the system design interview's web crawler (page 9), which makes the same point as System design interview's page 146 in two sentences; the big archive's "What happens when you type google.com" (pages 18 to 19), a shorter version of pages 254 to 255. The Computer networking: a top-down approach lines were read with pdftotext on 2026-10-24, found through the book's back-of-book index and its outline in `Textbooks.md`.
