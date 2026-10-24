# Security

Up: [[Information Technology]]

Information Technology, Security. [[TLS]], which encrypts traffic on the wire, and [[CORS]] are under Networking.

**Security is how a system knows who is calling, decides what they may do, and keeps data unreadable to anyone else. These notes cover proving identity, granting access, the signed tokens that carry both, one attack on browser sessions, and encryption itself.**

- [[Authentication]]: Authentication is the check that a caller is who it claims to be, by a password, a session cookie, a signed token or a key, before the system decides what that caller may do.
- [[Authorization]]: Authorization decides what an already identified caller may do, by its role, its attributes or an explicit list of permissions, so a request can be correctly authenticated and still be refused.
- [[JSON Web Token]]: A JSON Web Token is a header, a payload of claims and a signature, three base64url pieces joined by dots, which a server can trust without a session lookup because only the holder of the signing key could have produced the signature.
- [[Cross-Site Request Forgery]]: Cross-site request forgery is an attack in which another site makes your browser send a request to a site you are logged in to, and the browser attaches your cookie, so the request runs as you.
- [[Encryption]]: Encryption turns readable data into ciphertext that only the holder of the right key can turn back, with one shared key in symmetric encryption and a public and private key pair in asymmetric encryption.
