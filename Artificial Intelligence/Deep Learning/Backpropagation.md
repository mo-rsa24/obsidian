---
aliases: [backpropagation, backprop, back-propagation, backward pass, error backpropagation, reverse-mode differentiation, reverse-mode automatic differentiation]
standard: vault-note v2
---

# Backpropagation

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning.

**Backpropagation computes the gradient of a network's loss with respect to every weight by applying the chain rule backward from the loss, one layer at a time.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches backpropagation writes the rest around it.

## Where to learn this

**Backpropagation**, the backward pass. Also: backprop, error backpropagation, reverse-mode differentiation.

**Textbooks**

- Understanding deep learning, sections 7.2 to 7.4: [pages 113 to 120](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=113). A toy network worked through its forward pass and two backward passes, then the algorithm for a deep ReLU network and its summary on page 120.
- Deep learning textbook, section 6.5: [pages 220 to 229](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=220). The chain rule over a computational graph, then the algorithm (Algorithm 6.2 on page 226) and its forward and backward passes for a fully-connected network.
- Mathematics for machine learning, section 5.6: [pages 165 to 169](../../Mathematics/references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=165). Gradients in a deep network by the chain rule, then automatic differentiation with a worked example (Example 5.14).
- Probabilistic machine learning: an introduction, section 13.3: [pages 479 to 488](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=479). Forward against reverse mode, vector-Jacobian products for common layers, and computation graphs.
- AI engineering, chapter 7, Backpropagation and Trainable Parameters: [pages 620 to 622](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=620). The backward pass in three plain steps and why it sets the memory a finetuning run needs.

**Videos**

- CS231n lecture 4, 43:34 to 50:29: [watch](https://www.youtube.com/watch?v=25zD5qJHYsk&t=2614s). Backprops f = (x + y)z with x = −2, y = 5, z = −4 node by node, naming upstream and local gradients. Caption-read.
- CS231n lecture 4, 50:29 to 54:08: [watch](https://www.youtube.com/watch?v=25zD5qJHYsk&t=3029s). One node's rule: downstream gradient equals upstream gradient times local gradient, so nobody writes the whole network's derivative. Caption-read.
- CS229 lecture 8, 23:08 to 26:53: [watch](https://www.youtube.com/watch?v=ne2ngVAoMG8&t=1388s). Writes the chain rule as ∂J/∂z = (Jacobian of g)ᵀ ∂J/∂u and names it a module's backward function, as in PyTorch. Caption-read.
- CS229 lecture 8, 6:47 to 10:19: [watch](https://www.youtube.com/watch?v=ne2ngVAoMG8&t=407s). The theorem that a circuit of size N has its gradient computable in O(N) time, so the backward pass costs about as much as the forward one. Caption-read.

**Our plans and chapters**

- [Backpropagate through one small network by hand](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/11-backpropagate-through-one-small-network-by-hand.md), deep-learning/transformers, chapter 11. A 2-input, 2-hidden, 1-output network carried backward by hand, keeping track of the hidden unit that switches off.
- [Check a hand backprop against a numeric gradient in code](/home/molef/goal-setting/learning/deep-learning/transformers/plans/12-check-a-hand-backprop-against-a-numeric.md), deep-learning/transformers, plan 12. Rebuilds that network's forward and backward passes and perturbs each weight to check every slope.
- [Apply the chain rule through two and three steps by hand](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/09-apply-the-chain-rule-through-two.md), deep-learning/transformers, chapter 9. The chain rule that backpropagation repeats, on two and three nested functions.

**Scenes**

- [Kinds of composition notebook, Same points, two labellings](https://claude.ai/artifact/DBmJtn6xy75sPtQwPEvQZU#nb-sec2). The denoising loss and one gradient step, showing the gradient is identical under two labellings because no label enters the loss.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-22. Each textbook page range was read in the PDF with pdftotext; the AI engineering pages were first found through the links in its back-of-book index (PDF pages 932 to 988). Pattern recognition and machine learning also derives backpropagation, in section 5.3 from PDF page 260, and has no line here only to keep the list short. Each video row was read in its course's caption-read lecture map under `~/.claude/cache/captions/`, and its description paraphrases the map, never the machine-translated captions. Each plan and chapter was read at its title and description. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start.
