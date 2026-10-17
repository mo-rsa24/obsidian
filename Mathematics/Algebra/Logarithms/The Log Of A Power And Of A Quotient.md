---
aliases: [log of a power, log of a quotient, log rules, logarithm rules, laws of logarithms, power rule for logs, quotient rule for logs, log(a^b) = b log a, log(a / b) = log a - log b]
sources:
  - "Algebra Handbook, version 3.5, October 2022, chapter 15, page 110, the properties of logarithms: the vault's shelf copy, Mathematics/references/textbooks/algebra/algebra-handbook.pdf"
---

# The Log Of A Power And Of A Quotient

Up: [[Logarithms]]

Mathematics, Algebra, Logarithms. Needs: nothing beyond the log of a product.

> [!warning] Unfinished
> - Prompt 28, the concept picture, is stuck after three revisions and waits for a word from the learner (tangent segments at x = 5 not parallel), in the vault's `.prompts/Diffusion Models.md`.
> - `logs.py` has not been run through the prepared environment: this machine (the cluster) has no prepared environment `~/.vault-sandbox/bin/python`. Make it with `uv venv ~/.vault-sandbox` then `uv pip install --python ~/.vault-sandbox/bin/python pandas numpy scipy matplotlib statsmodels openpyxl`, and run it.

Textbook: [Algebra handbook, ch. 15, p. 110](../../references/textbooks/algebra/algebra-handbook.pdf#page=110)

**The log of a power is the power times the log, $\log(a^b) = b \log a$, and the log of a quotient is the difference of the logs, $\log(a / b) = \log a - \log b$, so $\log \pi_\beta(x) = \log\big(p(x)^\beta / Z_\beta\big)$ becomes $\beta \log p(x) - \log Z_\beta$: the old log density scaled by $\beta$, minus one constant.** *Cited* for both rules: algebra handbook, page 110, "The log of something to a power is the power times the log" and "The log of a quotient is the difference of the logs". [[The Tempered Density And Its Score]] uses them in one line; this subsection says why they hold and checks them on numbers.

**Why the power rule holds.** A whole-number power multiplies $a$ by itself, and a log turns multiplying into adding, $\log(uv) = \log u + \log v$ (the same page: "The log of a product is the sum of the logs"):

$$
\begin{aligned}
\log(a^2) &= \log(a \cdot a) = \log a + \log a = 2 \log a \\
\log(a^3) &= \log(a \cdot a \cdot a) = \log a + \log a + \log a = 3 \log a
\end{aligned}
$$

*Derived* for whole-number powers. The handbook lists the rule for any power, which is how it reaches $\beta = 0.5$ (*cited*); the first row of the table below checks that power on numbers.

**Why the quotient rule holds.** Dividing by $b$ is multiplying by $1/b$, and $\log(1/b) = -\log b$, because the two add to $\log(b \cdot 1/b) = \log 1 = 0$ (the same page: the log of 1 is zero):

$$
\log \frac{a}{b} = \log\left(a \cdot \frac{1}{b}\right) = \log a + \log \frac{1}{b} = \log a - \log b
$$

*Derived* from the product rule.

**Worked on the height of $\mathcal{N}(3, 4)$ at $x = 7$.** The unnormalised height is $h(x) = e^{-(x - 3)^2 / 8}$. The plan behind this walk writes the state as $y$; this note writes $x$.

$$
\begin{aligned}
h(7) &= e^{-(7 - 3)^2 / 8} = e^{-2} = 0.135335, \qquad \log h(7) = -2 \\
\beta = 2: \quad h(7)^2 &= 0.135335^2 = 0.018316 \\
\log h(7)^2 &= \log 0.018316 = -4 = 2 \times (-2)
\end{aligned}
$$

Squaring the height doubles its log. *Derived.*

**With the normaliser.** By the [exponent rules](../../references/textbooks/algebra/algebra-handbook.pdf#page=109), $h(x)^\beta = e^{-\beta (x - 3)^2 / 8}$, a slid and stretched bell. The [[Gaussian Integral#The area under the bell|Gaussian integral]] $\int e^{-a(x + b)^2}\,dx = \sqrt{\pi / a}$, with $a = \beta / 8$, gives its area:

$$
\begin{aligned}
Z_\beta &= \int_{-\infty}^{\infty} e^{-\beta (x - 3)^2 / 8}\,dx = \sqrt{8\pi / \beta} \\
Z_2 &= \sqrt{4\pi} = 3.544908, \qquad \log Z_2 = 1.265512 \\
\pi_2(7) &= 0.018316 / 3.544908 = 0.005167 \\
\log \pi_2(7) &= 2 \log h(7) - \log Z_2 = -4 - 1.265512 = -5.265512
\end{aligned}
$$

The log of 0.005167 taken directly is the same $-5.265512$, to six decimals from the unrounded quotient. Using $h$ in place of $p$ changes nothing: $p = h / Z_1$, so $p^\beta / \int p^\beta\,dx = h^\beta / \int h^\beta\,dx$, because the constant $Z_1^{-\beta}$ sits on the top and inside the area and cancels. *Derived.*

**Four more on the same rules.** Each row works the log by the rules and then directly, and the two agree.

| # | Setting | By the rules | Directly |
|---|---|---|---|
| 1 | $\beta = 0.5$ at $x = 7$ | $\log h(7)^{0.5} = 0.5 \times (-2) = -1$ | $h(7)^{0.5} = 0.367879 = e^{-1}$ |
| 2 | the same, with $Z_{0.5} = \sqrt{16\pi} = 7.089815$, $\log Z_{0.5} = 1.958659$ | $\log \pi_{0.5}(7) = -1 - 1.958659 = -2.958659$ | $0.367879 / 7.089815 = 0.051888$, whose log is $-2.958659$ |
| 3 | the guidance heights of [[Three Things Called Annealing#How the three knobs work]], $p(x \mid c) = 0.4$, $p(x) = 0.1$, scale 2 | $\log(0.4^2 / 0.1) = 2 \log 0.4 - \log 0.1 = 2(-0.916291) + 2.302585 = 0.470004$ | $\log 1.6 = 0.470004$ |
| 4 | the two-dimensional height $h(x_1, x_2) = e^{-(x_1^2 + x_2^2)/2}$ at $(1, 2)$, $\beta = 2$ | the exponent is $-2.5$, so $\log h^2 = 2 \times (-2.5) = -5$ | $h = 0.082085$, $h^2 = 0.006738 = e^{-5}$ |

*Derived*, every row.

**The two-dimensional score.** The [score](../../references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=114) of $\pi_\beta$ is the slope of $\beta \log h - \log Z_\beta$ in each coordinate. With $\log h = -(x_1^2 + x_2^2)/2$:

$$
\begin{aligned}
\nabla_x \big(\beta \log h(x)\big) &= \beta\,(-x_1,\ -x_2) \\
\beta = 2,\ (1, 2): &\quad 2 \times (-1,\ -2) = (-2,\ -4)
\end{aligned}
$$

$\log Z_\beta$ adds the same number at every point, so its slope is 0 in both coordinates and the score is $(-2, -4)$. *Derived.*

**What each number does to the logs.** Changing $\beta$ multiplies every log height by the same factor: the log curve stretches vertically and its slope at every point is multiplied by $\beta$. Changing $Z$ subtracts one number from every log height: the log curve slides down and every slope stays as it was. That is why the score in [[The Tempered Density And Its Score]] keeps $\beta$ and loses $Z_\beta$. *Derived* above.

**Why it matters.** Every sampler in this note works on log densities and their slopes, and every tempered, guided or composed density arrives as a power over an area. These two rules are what turn that into a scaled log minus a constant, and the constant is what a score-only sampler is allowed to ignore.

*🖼️ Diagram wanted: the concept, the log heights of $\mathcal{N}(3, 4)$ at $\beta = 1$ and $\beta = 2$, and then minus $\log Z_2$, on one axis, with the value at $x = 7$ going $-2 \to -4 \to -5.265512$ and a slope that the shift leaves unchanged. Prompt 28 in the same file.*

> [!note]- How this was checked
> This note was added on 2026-10-17 on the cluster, from piece 2.1 of the same walk, "the log of a power and of a quotient", and its example. The cluster still has no `~/.vault-sandbox`, so `logs.py` is filed as not run through the prepared environment. Its expected output is the output of the same lines run by the writer with the system `python3` (standard library only) in an empty scratch folder that was removed afterwards, the clean-up check returning 2; every number matched the walk's to the digits shown. The two areas were also checked with a rectangle sum of 120,001 rectangles of width 0.001 from $x = -60$ to $60$: 3.544908 at $\beta = 2$ and 7.089815 at $\beta = 0.5$, matching $\sqrt{8\pi/\beta}$, and the two-dimensional score $(-2, -4)$ with a central difference. The algebra handbook's page 110 was opened by decompressing its text stream with Python's standard library, since the cluster has no PDF reader: it prints "Page 110 of 187" and lists the log of a product, of a quotient and of a power, and the log of 1, in the words quoted. The exponent-rules link reuses page 109, which this note already links. The standard normal at $\beta = 0.5$ and $\beta = 2$ and the product's powered variances are left out on purpose: the walk holds those answers back for the learner's own check.
