---
aliases: [integral, definite integral, indefinite integral, antiderivative, anti-derivative, Riemann sum, fundamental theorem of calculus, numerical integration]
link-skip: [integration picture, WSL integration, one integration, integration capstone, vertical integration, continuous integration, existing integration, integration test, integration regression, approved integration, integration dealmaking, integral part, integral to]
link-not: [Integration]
---

# Integration

Mathematics, Calculus, Integration. One note per integral or technique that earns its own explanation.

- [[Gaussian Integral]]: the area under the bell $e^{-x^2}$ over the whole line, $\sqrt{\pi} = 1.772454$; why no antiderivative gives it, the rectangle sums that find it, and the normalisers $Z_a$ and $Z_b$ it sets for a slid or stretched bell.
- [[The Front Factor Of A Gaussian Density]]: why a density's area is 1, and how the substitution $u = (x - \mu)/\sigma$ turns the bell's area into $\sigma\sqrt{2\pi}$, so the front factor is $1/(\sigma\sqrt{2\pi})$; worked at $\sigma = 0.5$ and $\sigma = 2$, in two dimensions as $1/(2\pi\sigma^2)$, and the slip of writing $\sigma^2$ for $\sigma$.

## Where to learn this

**Integral**, the area under a curve, found by adding thin rectangles or by an antiderivative. Also: definite integral, antiderivative, Riemann sum.

**Textbooks**

- Calculus textbook, section 5.5: [pages 377 to 385](../../references/textbooks/calculus/calculus-textbook.pdf#page=377). Defines the definite integral as a limit of Riemann sums (Definition 5.5.1) and when a function is integrable.
- Calculus textbook, section 5.2: [pages 346 to 355](../../references/textbooks/calculus/calculus-textbook.pdf#page=346). Antiderivatives (Definition 5.2.1), the indefinite integral, its notation and the constant of integration.
- Calculus textbook, section 5.6: [pages 386 to 399](../../references/textbooks/calculus/calculus-textbook.pdf#page=386). The fundamental theorem of calculus, which evaluates a definite integral with an antiderivative and makes integration undo differentiation.
- Calculus handbook, chapter 7: [pages 87 to 94](../../references/textbooks/calculus/calculus-handbook.pdf#page=87). Definite integrals as Riemann sums drawn on an interval, the rules of definite integration, both fundamental theorems (page 92) and the properties of definite integrals.
- Calculus handbook, chapter 4: [page 56](../../references/textbooks/calculus/calculus-handbook.pdf#page=56). The rules of indefinite integration, power rule first, on one page.

**Videos**

- Leonard, Calculus 1, 4.3, 1:05:50 to 1:22:30: [watch](https://www.youtube.com/watch?v=F0uuW-I6icY&t=3950s). Works the area under x² on [0, 1] as a limit of rectangle sums, which comes to 1/3. Caption-read, from the video lessons index.
- Leonard, Calculus 1, 4.3, 22:51 to 53:00: [watch](https://www.youtube.com/watch?v=F0uuW-I6icY&t=1371s). Area under a curve as a limit of rectangles, and why the sum becomes an integral. Caption-read, from the video lessons index.
- Leonard, Calculus 1, 4.5, 0:01 to 8:00: [watch](https://www.youtube.com/watch?v=xjtEfS0vY2o&t=1s). Plugging the bounds into the antiderivative, with no +C. Caption-read, from the video lessons index.
- 3Blue1Brown, Integration and the fundamental theorem of calculus (Essence of calculus, chapter 8), Fundamental theorem of calculus, 11:18 to 16:20: [watch](https://www.youtube.com/watch?v=rfG8ce4nNh0&t=678s). Why the area under a graph is found from an antiderivative. Chapter-timed.

**Our plans and chapters**

- [2. Joint and marginal: summing out and integrating out](/home/molef/goal-setting/learning/mathematics/statistics/conditional-expectation/textbook/02-joint-and-marginal-summing-out.md), mathematics/statistics/conditional-expectation, section 2. An integral that removes a variable from a joint density, the way every noised density in diffusion is built.
- [Mathematics: Calculus](/home/molef/goal-setting/learning/mathematics/calculus/MASTER_PLAN.md), mathematics/calculus. Its second objective is integration by substitution, by parts, by partial fractions and improper integrals, each checked against numerical quadrature; no plan files exist under it yet.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after finding it through the chapter tables in `Textbooks.md` and the back-of-book tables in `~/.claude/cache/book-indexes/`. The three Leonard lines are copied from the video lessons index, section "Area under a curve, and the integral over the whole line", whose times come from his auto-generated captions. The 3Blue1Brown chapter list was read with cache-video-chapters.py, and that line describes only the chapter and video titles. Each plan and chapter was read at its title and description. The Gaussian integral has its own note, [[Gaussian Integral]], and keeps its name. "integration" alone was sampled in the learning tree (25 lines, about 3 meaning this idea; the rest were WSL integration, integration pictures and continuous integration), so it is not an alias; the note's own name still links, so the common other phrases are in `link-skip`. gather-concept-sources.py stopped at its time limit, so its sources were searched by hand. A script then opened every link.
