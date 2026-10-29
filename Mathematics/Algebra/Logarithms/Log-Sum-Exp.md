---
aliases: [log-sum-exp, logsumexp, log sum exp, log-sum-exp trick, LSE, lse]
standard: vault-note v2
---

# Log-Sum-Exp

Up: [[Logarithms]]

Mathematics, Algebra, Logarithms. It is the log of the normaliser inside [[Softmax]], and its gradient is the softmax.

**Log-sum-exp is $\log \sum_i e^{x_i}$, a smooth stand-in for $\max_i x_i$ that lands just above the largest input; it is computed as $m + \log \sum_i e^{x_i - m}$ with $m = \max_i x_i$, so the largest term exponentiated is $e^0 = 1$ and the sum can neither overflow to infinity nor underflow to zero.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches log-sum-exp writes the rest around it.
> - The note is not yet listed in the [[Logarithms]] map note.

## Where to learn this

**Log-sum-exp**, log Σᵢ exp(xᵢ) = m + log Σᵢ exp(xᵢ − m) with m = maxᵢ xᵢ. Also: logsumexp, log-sum-exp trick, LSE.

**Textbooks**

- Probabilistic machine learning: an introduction, section 2.5.4, Log-sum-exp trick: [pages 80 to 81](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=80). Works it with numbers: logits (0, 1, 0) give a normaliser of 4.71, logits (1000, 1001, 1000) overflow to infinity and (−1000, −999, −1000) underflow to 0, and subtracting m = max a fixes both (equation 2.99); then the binary cross-entropy is written with lse so it never forms a probability.
- Algebra handbook, chapter 15, Exponent formulas: [page 109](../../references/textbooks/algebra/algebra-handbook.pdf#page=109). The product of powers, aᵖ · a^q = a^(p+q), is the step that splits each e^(xᵢ) into e^m · e^(xᵢ − m) so e^m factors out of the sum.
- Algebra handbook, chapter 15, Logarithm formulas: [page 110](../../references/textbooks/algebra/algebra-handbook.pdf#page=110). The log of a product is the sum of the logs, and ln eˣ = x, which together turn log(e^m · Σ e^(xᵢ − m)) into m + log Σ e^(xᵢ − m).
- Deep learning textbook, section 4.1, Overflow and underflow: [pages 96 to 97](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=96). Why exp of a large input overflows and of a very negative one underflows, the fix z = x − maxᵢ xᵢ, and why log softmax needs its own stable function.
- Deep learning textbook, section 6.2.2.3: [pages 200 to 202](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=200). Writes log softmax(z)ᵢ = zᵢ − log Σⱼ exp(zⱼ) and reads the log-sum-exp term as roughly maxⱼ zⱼ, so the loss punishes the most confident wrong class.
- Probabilistic machine learning: advanced topics, section 28.2.5.3, Numerical issues: [pages 961 to 962](../../references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=961). A Gaussian mixture's log-likelihood log Σₖ αₖ N(x | μₖ, Σₖ) written as a logsumexp of βₖ = log αₖ + log N(·) with M = maxₖ βₖ taken out, so no component's tiny density underflows.
- Pattern recognition and machine learning, section 13.2.4, Scaling factors: [pages 642 to 643](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=642). The same calculation in another subject: a hidden Markov model's forward messages are sums of products of small probabilities that underflow after about 100 steps, and rescaling each step by its normaliser keeps them near 1, the job subtracting the max does for log-sum-exp.

**Videos**

- Bert Huang, Avoid Numerical Explosions with the Log Sum Exp Trick, 17:21 to 20:34: [watch](https://www.youtube.com/watch?v=pZbkVup7fYE&t=1041s). The trick worked on numbers, in the chapter "Numerical example". Chapter-timed.
- Bert Huang, the same video, 6:55 to 9:16: [watch](https://www.youtube.com/watch?v=pZbkVup7fYE&t=415s). What goes wrong when very large or very negative numbers are exponentiated, in the chapter "Numerical stability issues". Chapter-timed.
- Bert Huang, the same video, 9:16 to 12:06: [watch](https://www.youtube.com/watch?v=pZbkVup7fYE&t=556s). The trick itself, factoring out the largest term, in the chapter "The log-sum-exp trick". Chapter-timed.

**Our plans and chapters**

- [Log-sum-exp and the softmax gradient](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l0-simple-maths/01-log-sum-exp-and-the-softmax-gradient.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L0, section 1. Defines LSE, its shift invariance and the stable form (1.1), proves its gradient is the softmax, and bounds it between max and max + T log n.
- [Log-sum-exp and the softmax gradient](/home/molef/goal-setting/learning/deep-learning/diffusion-models/06-diffusion-speciation-dynamics/plans/00-foundation/plans/01-logsumexp-softmax-gradient.md), deep-learning/diffusion-models/06-diffusion-speciation-dynamics, foundation plan 01. Differentiates log Σ exp(aᵢ) to the softmax weights by hand, then sweeps the scale until the weights harden into an argmax.
- [From log-sum-exp to the log-cosh term](/home/molef/goal-setting/learning/deep-learning/diffusion-models/05-poe-composition-diffusion/plans/26-log-sum-exp-to-log-cosh.md), deep-learning/diffusion-models/05-poe-composition-diffusion, plan 26. Writes a symmetric two-Gaussian mixture's log-density as a log-sum-exp of two terms and simplifies it to a log cosh, whose derivative is tanh.
- [The exact score of a Gaussian mixture](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l4-continuous-time/09-the-exact-score-of-a-gaussian-mixture.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L4, section 9. Writes log p(x) as a logsumexp over weighted components (9.1) and differentiates it into a softmax-weighted sum of directions to each mean.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-28. Each textbook page range was read in the PDF with pdftotext, found through the two Probabilistic machine learning back-of-book index entries for "log-sum-exp trick" and the shelf's worked-examples catalogue (`find-examples.py`, which also gave the hidden Markov model scaling as a same-shape example). The algebra handbook pages are the ones the [[Softmax]] card already cites for subtracting the largest input and undoing the exp. The three video rows match the video lessons index section "Underflow and the log-sum-exp trick", and the chapter list was read with `cache-video-chapters.py`, so each line describes only its chapter's title and span. No lecture map in `~/.claude/cache/captions/` has a log-sum-exp segment, the paper shelf has no paper on it, and `find-figures.py` found no staged figure, so the card has no Papers or Figures group. Each plan and chapter was read at its title and opening lines. A script then opened every link with `check-cards.py`.
