# Information Theory

Up: [[Statistics]]

Mathematics, Statistics, Information Theory.

**Information theory measures uncertainty and surprise in bits or nats. Entropy is the average surprise of one distribution, and the KL divergence is the extra surprise paid for using the wrong one.**

- [[Entropy]]: Entropy is the average surprise of a random variable, H = −Σ p(x) log p(x): zero when one outcome is certain, largest when every outcome is equally likely, and the fewest bits per draw any code can average.
- [[Cross-Entropy]]: The cross-entropy H(p, q) = −Σ p(x) log q(x) is the average surprise of outcomes drawn from p when they are scored with the probabilities of q.
- [[KL Divergence]]: The KL divergence KL(p‖q) = Σ p(x) log (p(x)/q(x)) is the average extra cost, in bits or nats, of coding draws from p with a code built for q: never negative, zero only when p = q, and not symmetric.
