---
aliases: [cross-entropy, cross entropy, cross-entropy loss, H(p, q), log loss, softmax loss]
standard: vault-note v2
---

# Cross-Entropy

Up: [[Information Theory]]

Mathematics, Statistics, Information Theory.

**The cross-entropy H(p, q) = −Σ p(x) log q(x) is the average surprise of outcomes drawn from p when they are scored with the probabilities of q.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches cross-entropy writes the rest around it.

## Where to learn this

**Cross-entropy**, and the cross-entropy loss built on it. Also: cross entropy, H(p, q), log loss, softmax loss.

**Textbooks**

- Understanding deep learning, section 5.7, Cross-entropy loss: [pages 85 to 86](../../references/textbooks/machine-learning/understanding-deep-learning.pdf#page=85). Fits a model by minimising the KL divergence to the empirical distribution, which leaves the cross-entropy, and shows it equals the negative log-likelihood.
- Deep learning textbook, section 3.13: [page 91](../../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=91). Defines H(P, Q) = −E over P of log Q(x) (equation 3.51) and shows that minimising it in Q is minimising the KL divergence.
- Probabilistic machine learning: an introduction, section 6.1.2: [page 239](../../references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=239). Reads cross-entropy as the expected number of bits to code samples from p with a code built for q, least when q = p.
- AI engineering, chapter 3, Cross Entropy: [pages 244 to 245](../../references/textbooks/ai-engineering/ai-engineering.pdf#page=244). A language model's cross-entropy on its data as the data's entropy plus the model's KL divergence from it, and why it is not symmetric.

**Videos**

- CS231n lecture 2, 1:00:36 to 1:04:47: [watch](https://www.youtube.com/watch?v=pdqofxJeBN8&t=3636s). Derives the softmax loss as the negative log probability of the correct class and shows it equals the KL divergence and the cross-entropy against a one-hot target. Caption-read.
- CS229 lecture 4, 1:00:17 to 1:02:50: [watch](https://www.youtube.com/watch?v=8gVi4Rk21Eg&t=3617s). Trains softmax by maximising the log probability of the correct class, which with a one-hot label is the cross-entropy loss (`CrossEntropyLoss` in PyTorch). Caption-read.
- CS229 lecture 14 (transformers and in-context learning), 36:12 to 38:43: [watch](https://www.youtube.com/watch?v=pwQ0l4hFCVI&t=2172s). Writes the next-token loss as the negative log-likelihood −Σₜ log softmax(f_θ(x_{<t}))[xₜ]. Caption-read.
- CME295 lecture 1, 40:48 to 45:57: [watch](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2448s). Trains a toy next-word network with a vocabulary of 6 and hidden size 2, using softmax probabilities such as 0.2 and 0.4 and the cross-entropy loss. Caption-read.

**Our plans and chapters**

- [Cross-entropy is entropy plus KL](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/11-kl-cross-entropy-and-cmi.md#112-cross-entropy-is-entropy-plus-kl), deep-learning/diffusion-models/01-poe-derivation-foundations, section 11.2. The identity H(p, q) = H(p) + KL(p ‖ q), worked.
- [Find the gradient of the cross-entropy loss through a softmax](/home/molef/goal-setting/learning/deep-learning/transformers/plans/10-find-the-gradient-of-the-cross-entropy.md), deep-learning/transformers, plan 10. The gradient of softmax followed by cross-entropy, which comes out as the predicted probabilities minus the one-hot target.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/clip-by-hand-thumbnail.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/clip-by-hand-thumbnail.jpg" width="200" alt="A hand-worked sheet: three text-image pairs encoded on two sides, projected into a yellow shared embedding space, then softmax similarity matrices and cross-entropy gradients against identity targets"></a> Prof. Tom Yeh on X, "CLIP by hand": [the post](https://x.com/ProfTomYeh/status/2094791189371261274), [what it shows](/home/molef/goal-setting/learning/deep-learning/vision-language-modeling/artifacts/figures/clip-embeddings/README.md#clip-by-hand-thumbnailjpg). Step 13, the orange "Cross Entropy Loss Gradients" box, uses identity matrices as targets (each right pair should score 1, every other cell 0) and subtracts them from the two softmax matrices to get the gradients in both directions.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-22. Each textbook page range was read in the PDF with pdftotext; the AI engineering page was first found through the links in its back-of-book index (PDF pages 932 to 988). Probabilistic machine learning: advanced topics defines it too, as the average negative log-likelihood, at PDF page 262 (printed 229), and has no line only to keep the list short. Each video row was read in its course's caption-read lecture map under `~/.claude/cache/captions/`, and its description paraphrases the map, never the machine-translated captions. Each plan and chapter was read at its title and description. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start.
