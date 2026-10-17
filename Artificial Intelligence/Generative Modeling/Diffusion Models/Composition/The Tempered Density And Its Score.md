---
aliases: [tempering, tempered density, powered density, p(x)^beta, temperature score, tempered score, score of a tempered density, score of a powered density, pi_beta, Z_beta, beta = 0, beta zero endpoint, geometric path, geometric annealing path, base^(1 - beta) p^beta, log of the tempered density, log pi_beta]
sources:
  - "Neal, Annealed Importance Sampling, Statistics and Computing 11, 125 to 139, 2001: https://arxiv.org/abs/physics/9803008"
  - "Wikipedia, Gaussian integral: https://en.wikipedia.org/wiki/Gaussian_integral, read 2026-10-17, CC BY-SA 4.0"
---

# The Tempered Density And Its Score

Up: [[Composition]] · ⬅️ [[Three Things Called Annealing]] · [[Why The Normaliser Has No Slope In X]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models, Composition. Needs: [[Three Things Called Annealing]] and [[The Log Of A Power And Of A Quotient]].

> [!question] Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. This note's sections are not in it yet.

> [!warning] Unfinished
> - Prompt 27, the concept picture, is stuck after three revisions and waits for a word from the learner (panel 3 bells off-centre), in the vault's `.prompts/Diffusion Models.md`.
> - This note has not been run: this machine (the cluster) has no prepared environment `~/.vault-sandbox/bin/python`. Make it with `uv venv ~/.vault-sandbox` then `uv pip install --python ~/.vault-sandbox/bin/python pandas numpy scipy matplotlib statsmodels openpyxl`, run `tempered.py`, and file its real output in place of the hand-worked lines.

**Raising a density to a power $\beta$ and dividing by the new area gives the tempered density $\pi_\beta(x) = p(x)^\beta / Z_\beta$, and its score is $\beta$ times the score of $p$, so a sampler that follows scores never needs $Z_\beta$.** The normaliser $Z_\beta = \int p(x)^\beta\,dx$ is the area under the powered heights. $\beta$ is the inverse temperature, $T = 1/\beta$: a large $\beta$ is a cold, sharp target and a small one a hot, flat target. *Derived* below.

**The log turns the power into a multiplier.** By the [log rules](../../../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=110), $\log(a^b) = b \log a$ and $\log(a / b) = \log a - \log b$, so

$$
\begin{aligned}
\log \pi_\beta(x) &= \log \frac{p(x)^\beta}{Z_\beta} \\
&= \log p(x)^\beta - \log Z_\beta \\
&= \beta \log p(x) - \log Z_\beta
\end{aligned}
$$

The first term is the old log density scaled by $\beta$. The second is one number, the same at every $x$. *Derived.* [[The Log Of A Power And Of A Quotient]] says why both rules hold and checks them on numbers.

**The score drops the normaliser.** The [score](../../../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=114) is the slope of the log density in $x$. $Z_\beta$ is an integral over $x$, so $x$ has been integrated out of it and its slope in $x$ is 0. This is the same reason [a model's score ignores its partition function](../../../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=179).

$$
\begin{aligned}
\nabla_x \log \pi_\beta(x) &= \beta\, \nabla_x \log p(x) - \nabla_x \log Z_\beta \\
&= \beta\, \nabla_x \log p(x) - 0 \\
&= \beta\, \mathrm{score}(x)
\end{aligned}
$$

A sampler can walk a temperature schedule by multiplying the score it already has, without computing an area at any step. *Derived.*

**Worked on $\mathcal{N}(3, 4)$.** Its log density is $-(x - 3)^2 / 8$ plus a constant, so its score is $-(x - 3) / 4$:

$$
\begin{aligned}
\mathrm{score}(5) &= -(5 - 3) / 4 = -0.5 \\
\beta = 2: \quad \beta\, \mathrm{score}(5) &= 2 \times (-0.5) = -1.0
\end{aligned}
$$

*Derived.*

**A powered Gaussian is a Gaussian with the same mean and variance $\sigma^2 / \beta$**, which [[Powers Of Gaussians]] derives. That gives a second route to the same score. $\mathcal{N}(3, 4)$ at $\beta = 2$ is $\mathcal{N}(3, 2)$, whose own score at 5 is $-(5 - 3) / 2 = -1.0$, the number the scaled score gave. Expert a, $\mathcal{N}(-1, 0.5)$, at $\beta = 0.25$ is $\mathcal{N}(-1, 2)$:

$$
\begin{aligned}
\beta\, \mathrm{score}_a(0) &= 0.25 \times \left(-\frac{0 + 1}{0.5}\right) = 0.25 \times (-2) = -0.5 \\
\text{score of } \mathcal{N}(-1, 2) \text{ at } 0 &= -\frac{0 + 1}{2} = -0.5
\end{aligned}
$$

*Derived.*

**At $\beta = 0$ there is no density to normalise.** Take the standard normal's heights $e^{-x^2/2}$. Their powered area is a stretched [[Gaussian Integral#The area under the bell|Gaussian integral]], $\int e^{-a x^2}\,dx = \sqrt{\pi / a}$ (*cited:* Wikipedia, Gaussian integral, "The integral of a Gaussian function"), with $a = \beta / 2$:

$$
\begin{aligned}
Z_\beta &= \int_{-\infty}^{\infty} e^{-\beta x^2 / 2}\,dx = \sqrt{2\pi / \beta} \\
\beta = 1: &\quad \sqrt{2\pi} = 2.506628 \\
\beta = 0.01: &\quad \sqrt{200\pi} = 25.066283 \\
\beta \to 0: &\quad Z_\beta \to \infty
\end{aligned}
$$

At $\beta = 0$ every height is $p(x)^0 = 1$: a flat line of height 1 over the whole real line. From $-L$ to $L$ its area is $2L$, which grows without limit, so no $Z_0$ exists. The variance $1/\beta$ says the same thing: 100 at $\beta = 0.01$, and no value at 0. *Derived.*

**So a temperature schedule starts at a positive $\beta$, or bends from a proper base density.** The bent form is

$$
\pi_\beta(x) \propto \mathrm{base}(x)^{1 - \beta}\, p(x)^\beta
$$

At $\beta = 0$ it is the base, which has area 1, and at $\beta = 1$ it is $p$. By the same log rule its score is $(1 - \beta)\,\mathrm{score}_{\text{base}}(x) + \beta\,\mathrm{score}(x)$. With base $\mathcal{N}(0, 1)$ and $p = \mathcal{N}(3, 4)$, the precision rule in [[Powers Of Gaussians]] gives, at $\beta = 0.5$:

$$
\begin{aligned}
P &= \frac{0.5}{1} + \frac{0.5}{4} = 0.625 \\
\text{variance} &= 1 / 0.625 = 1.6 \\
\text{mean} &= \frac{0.5 \times 3 / 4}{0.625} = 0.6
\end{aligned}
$$

*Derived.* Annealed importance sampling moves "from a tractable distribution to a distribution of interest via a sequence of intermediate distributions" (*cited:* Neal, Annealed Importance Sampling, abstract). That its intermediate distributions take this bent form is *stated*, not checked against the paper's body here.

*🖼️ Diagram wanted: the concept, $\mathcal{N}(3, 4)$ and $\mathcal{N}(3, 2)$ on one axis with their score arrows at $x = 5$, the bells of $e^{-\beta x^2/2}$ flattening toward the flat line at $\beta = 0$, and the bent path from the base to $p$. Prompt 27 in the same file.*

> [!note]- How this was checked
> This note was added on 2026-10-17 on the cluster, from piece 2 of the same walk. Nothing in it was run, for the same reason, so `tempered.py` and its expected output are worked by hand; the next machine with the prepared environment runs it and replaces the expected lines. Every printed number, including both rectangle sums, was computed by the writer with `awk` running the same loops in double precision, and each matched the walk's numbers to the digits shown. The base-and-$p$ example at $\beta = 0.5$ is new to this note. The standard normal at $\beta = 0.5$ and $\beta = 2$ is left out on purpose: the walk holds those answers back for the learner's own check. The textbook links are the shelf index's rows for log rules (algebra handbook page 110), the score with its Gaussian example (the little book of generative AI foundations, page 114) and why the score ignores the partition function (the same book, page 179); the cluster has no PDF reader, so none was reopened. The Gaussian integral formula $\int e^{-a(x+b)^2}\,dx = \sqrt{\pi / a}$ was read on Wikipedia's Gaussian integral page, section "The integral of a Gaussian function", on 2026-10-17. Neal's paper was fetched from arXiv, but without a PDF reader only its first page could be read, so the quotation is from the abstract and the bent form's attribution stays stated.
