# Network Layer

Up: [[Networking]]

Information Technology, Networking. Chapters 4 and 5 of [[computer-networking-a-top-down-approach.pdf#page=335|Computer networking: a top-down approach]] teach this layer, its data plane first and then the routing that fills its tables.

**The network layer moves a packet from one host to another across many networks. Every interface has an IP address inside a subnet, every router forwards a packet by looking its destination up in a table, DHCP hands a joining machine its address, and NAT lets a whole private network share one public address.**

- [[Subnet]]: A subnet is a block of IP addresses sharing one prefix, written in CIDR form such as 10.0.1.0/24, whose machines reach each other directly without a router between them.
- [[Routing Table]]: A routing table maps a destination prefix to where traffic goes next, and the longest matching prefix wins, in a router choosing the outgoing link for each packet.
- [[DHCP]]: DHCP is how a machine joining a network gets its IP address, subnet mask, default gateway and DNS server automatically, in four messages: discover, offer, request and acknowledge.
- [[Network Address Translation]]: Network address translation rewrites the private source address and port of outgoing packets to one public address and a fresh port, and keeps a table so each reply finds its way back to the machine that asked.
