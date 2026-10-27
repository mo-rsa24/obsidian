---
aliases: [temperature, sampling temperature, softmax temperature, temperature scaling, temperature parameter]
standard: vault-note v2
---

# Temperature

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. Needs: [[Softmax]]. How the composition notes anneal a temperature is in [[Three Things Called Annealing]] and [[The Tempered Density And Its Score]].

**Temperature is the number T that divides the logits before the softmax, so a T below 1 sharpens the distribution toward its largest logit and a T above 1 flattens it toward uniform.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches temperature writes the rest around it.

## Where to learn this

**Temperature**, the T in softmax(z/T), and its reciprocal β in a tempered density p(x)^β. Also: sampling temperature, softmax temperature, temperature scaling, temperature parameter.

**Textbooks**

- AI engineering, chapter 2, Sampling strategies, Temperature: [pages 192 to 194](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=192). Divides the logits [1, 2] by T and works the change by hand: [0.27, 0.73] at T = 1 becomes [0.12, 0.88] at T = 0.5, then says why temperature 0 means picking the largest logit.
- Probabilistic machine learning: an introduction, section 2.5.2, The softmax function: [page 79](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=79). Writes S(a/T) and shows it goes to the argmax as T → 0 ("winner takes all") and spreads the mass uniformly as T grows.
- Hands-on large language models, chapter 6, Temperature: [pages 240 to 241](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=240). Sets `temperature` with `do_sample=True` in a transformers pipeline and compares 0.2 against 0.8.
- Deep learning, section 17.5.1, Tempering to mix between modes: [page 619](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=619). Writes an energy-based model at inverse temperature β, p_β(x) ∝ exp(−βE(x)), and samples at β < 1 (tempered transitions, parallel tempering) so a Markov chain crosses between modes.
- Probabilistic machine learning: advanced topics, section 14.2.2.5, Temperature scaling: [page 607](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=607). Calibrates a trained classifier with one learned T, q = softmax(z/T), which changes its confidence and never its predicted class.

**Videos**

- CS229 lecture 14, 29:06 to 36:12: [watch](https://www.youtube.com/watch?v=pwQ0l4hFCVI&t=1746s). Works temperature: dividing the logits (2, 1, −1) by a tiny τ gives (200, 100, −100) and a near one-hot softmax, a low τ approaches greedy decoding and a τ above 1 flattens it. Caption-read.
- CME295 lecture 3, 50:44 to 1:00:15: [watch](https://www.youtube.com/watch?v=Q5baLehv5So&t=3044s). Writes p_i = exp(x_i/T) / Σ_j exp(x_j/T) and factors out the largest logit to prove the distribution goes one-hot as T → 0 and uniform as T → ∞. Caption-read.
- CME295 lecture 3, 1:00:15 to 1:06:58: [watch](https://www.youtube.com/watch?v=Q5baLehv5So&t=3615s). High temperature for creative text and low for deterministic text, and why T = 0 can still vary when GPU reductions run in different orders. Caption-read.
- Vizuara, Top-k sampling in Large Language Models, 0:00 to 5:39: [watch](https://www.youtube.com/watch?v=EhU32O7DkA4&t=0s). Temperature scaling of the scores before the softmax, recapped. Chapter-timed, from the video lessons index.

**Our plans and chapters**

- [2.3 Temperature and repeatability](/home/molef/goal-setting/learning/ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions/textbook/02-the-model.md#23-temperature-and-repeatability), ai-engineering/llm-applications/retrieval-augmented-generation/document-qa-with-permissions, chapter 02. Sends one welcome request 20 times at each setting: 1 distinct answer at temperature 0 and 17 at 0.8.
- [The same prompt, five different answers](/home/molef/goal-setting/learning/ai-engineering/data-agents/plans/10-the-same-prompt-five-different-answers.md), ai-engineering/data-agents, plan 10. Asks one question repeatedly and watches the answer change while the price per call holds.
- [Distil a small student from a teacher's softened outputs](/home/molef/goal-setting/learning/deep-learning/model-compression/plans/03-distillation-with-soft-targets.md), deep-learning/model-compression, plan 03. Softens a teacher's outputs with a temperature, computes them by hand at T = 1 and T = 4, and writes the distillation loss with its T² factor.
- [The Metropolis corrector by hand: step size, temperature and method](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/12-the-metropolis-corrector-by-hand.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, chapter 12. Runs a tempered chain aimed at p^β, where β < 1 makes the valleys shallower so the chain crosses them more often.

**Figures**

- <a href="/home/molef/goal-setting/learning/ai-engineering/agent-architecture/artifacts/figures/agentic-engineering-course/05-temperature.png"><img src="/home/molef/goal-setting/learning/ai-engineering/agent-architecture/artifacts/figures/agentic-engineering-course/05-temperature.png" width="200" alt="A temperature gauge from 0.0 to 1.5+ with the needle at 0.8, a red box reading low temp is not no hallucination, and LLM proposes, backend validates, API executes"></a> Rahul on X, "Become AI Agentic Engineer in 6 Weeks", week 1, redrawn from the article: [the post](https://x.com/sairahul1/status/2093989227696623658), [what it shows](/home/molef/goal-setting/learning/ai-engineering/agent-architecture/artifacts/figures/agentic-engineering-course/README.md#05-temperaturepng). The gauge runs from cold at 0.0 (predictable, repetitive, still hallucinates) through warm at 0.8 (a good default) to hot at 1.5 and above, and a red box says a wrong answer the model rates at 99% is picked every time at low temperature, so safety comes from a backend that validates what the model proposes. The 0.8 default and the 1.5 boundary are conventions drawn for teaching, with no model or measurement behind them ([the reading](/home/molef/goal-setting/learning/ai-engineering/agent-architecture/sources/agentic-engineering-course/topics/05-temperature.md#what-it-does-not-carry)).
- <a href="/home/molef/goal-setting/learning/ai-engineering/llm-inference/artifacts/figures/llm-concepts-cheatsheet/jaydeepkarale-ai-llm-concepts-part1.jpg"><img src="/home/molef/goal-setting/learning/ai-engineering/llm-inference/artifacts/figures/llm-concepts-cheatsheet/jaydeepkarale-ai-llm-concepts-part1.jpg" width="140" alt="A ten-panel cheat sheet whose panel 8 answers the capital of France at temperature 0.2, 0.7 and 1.2"></a> Jaydeep Karale on X, "AI / LLM Concepts Cheat Sheet (Part 1)": [the post](https://x.com/_jaydeepkarale/status/2095815664187609355), [what it shows](/home/molef/goal-setting/learning/ai-engineering/llm-inference/artifacts/figures/llm-concepts-cheatsheet/README.md#jaydeepkarale-ai-llm-concepts-part1jpg). Panel 8 answers the same prompt at 0.2 ("The capital of France is Paris."), 0.7 and 1.2, the answer growing more elaborate as the setting rises, over a stated range of 0.0 to 2.0 with 0.7 as a common default. It never shows the mechanism, the logits divided by the temperature before the softmax ([the reading](/home/molef/goal-setting/learning/ai-engineering/llm-inference/sources/llm-concepts-cheatsheet/SOURCES.md#ai--llm-concepts-cheat-sheet-part-1-context-window-inference-temperature-hallucination)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page was read in the PDF with pdftotext, after finding it through the book's back-of-book index or a page search. Each video row was read in its course's caption-read lecture map under `~/.claude/cache/captions/` or in the video lessons index, and its description paraphrases that row. Each plan and chapter was read at its title and opening. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start.
