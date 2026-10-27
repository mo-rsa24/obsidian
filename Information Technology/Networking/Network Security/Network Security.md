# Network Security

Up: [[Networking]]

Information Technology, Networking. Chapter 8 of [[computer-networking-a-top-down-approach.pdf#page=623|Computer networking: a top-down approach]] teaches these, beside [[TLS]], which secures one connection and sits with the other protocols under Networking.

**Network security decides which packets may cross a network's edge and keeps the ones that cross a public network private. A firewall filters traffic at the boundary by address, port and connection state, and a VPN carries a private network's traffic across the internet inside an encrypted tunnel.**

- [[Firewall]]: A firewall sits at a network's edge or on a host and lets each packet through or drops it by rules on its addresses, ports and protocol, and a stateful one also remembers which connections are already open so their replies pass.
- [[VPN]]: A VPN joins two private networks, or one remote machine to a private network, across the public internet, by wrapping each packet whole inside an encrypted one sent between the two ends of a tunnel.
