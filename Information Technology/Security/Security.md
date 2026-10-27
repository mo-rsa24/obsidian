# Security

Up: [[Information Technology]]

Information Technology, Security. [[TLS]], which encrypts traffic on the wire, and [[CORS]] are under Networking.

**Security is how a system knows who is calling, decides what they may do, and keeps data unreadable to anyone else. These notes cover proving identity, granting access, the signed tokens that carry both, one attack on browser sessions, and encryption itself.**

- [[Authentication]]: Authentication is the check that a caller is who it claims to be, by a password, a session cookie, a signed token or a key, before the system decides what that caller may do.
- [[Authorization]]: Authorization decides what an already identified caller may do, by its role, its attributes or an explicit list of permissions, so a request can be correctly authenticated and still be refused.
- [[JSON Web Token]]: A JSON Web Token is a header, a payload of claims and a signature, three base64url pieces joined by dots, which a server can trust without a session lookup because only the holder of the signing key could have produced the signature.
- [[Cross-Site Request Forgery]]: Cross-site request forgery is an attack in which another site makes your browser send a request to a site you are logged in to, and the browser attaches your cookie, so the request runs as you.
- [[Encryption]]: Encryption turns readable data into ciphertext that only the holder of the right key can turn back, with one shared key in symmetric encryption and a public and private key pair in asymmetric encryption.
- [[Cross-Site Scripting]]: Cross-site scripting is an attack in which a site sends an attacker's script to your browser as part of its own page, because it echoed someone's input without escaping it, so the script runs with that page's rights and can read its tokens and act as you.
- [[OAuth]]: OAuth 2.0 lets one application act on your data at another service without ever seeing your password: you log in at that service's authorization server and approve, the application receives a short-lived access token, and it calls the service's API with that token. OpenID Connect adds an ID token to the same flow so the application also learns who you are, which is what "Sign in with Google" runs on.
- [[OpenID Connect]]: OpenID Connect is a sign-in protocol on top of OAuth 2.0 in which a trusted issuer hands out a short-lived signed identity token, so a person ("Sign in with Google") or a pipeline (a GitHub Actions run) can prove who it is to another service without a password or a stored key.
- [[Password Hashing]]: Password hashing stores a password as the output of a deliberately slow one-way hash (bcrypt, scrypt, Argon2) computed over the password plus a random salt kept beside it, so a stolen table reveals no passwords, two users with the same password store different hashes, and a precomputed rainbow table of common passwords is useless.
