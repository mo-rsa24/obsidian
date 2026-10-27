---
aliases: [sampling, sampling from a distribution, sample from a distribution, drawing samples, draw samples, drawing from a distribution, generating random numbers, random variate generation, sample, draw a sample, drawing a sample, random sample, sample of a population, sampling a population]
link-skip: [sample catalogue, sample image, sample artifacts, sample output, sample files, sample code, sample pipeline, sample workflow, sampling four words, sample inventory, sample rate, test samples]
standard: vault-note v2
---

# Sampling From A Distribution

Up: [[Statistics]]

Mathematics, Statistics. Two methods already have notes: [[Inverse Transform Sampling]] and [[Markov Chain Monte Carlo]].

**Sampling from a distribution means producing random values whose long-run frequencies follow it, usually by transforming uniform random numbers the computer already has.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches sampling writes the rest around it.

## Where to learn this

**Sampling**, drawing samples from a distribution. Also: drawing samples, sampling from a distribution, generating random numbers.

**Textbooks**

- Pattern recognition and machine learning, chapter 11: [pages 539 to 550](../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=539). Why expectations need samples, ancestral sampling of a directed graph (page 541), standard distributions from transformed uniforms (page 542), rejection sampling (page 544) and importance sampling (page 548).
- Introduction to probability for data science, section 4.8: [pages 245 to 251](../references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=245). Generates random numbers for any PDF by running a uniform through the inverse CDF, in Python, with Gaussian and exponential examples.
- Deep learning textbook, section 17.1: [pages 606 to 608](../references/textbooks/machine-learning/deep-learning-textbook.pdf#page=606). Why machine learning samples at all (Monte Carlo estimates of sums and integrals, and sampling as the goal of a generative model), then the basics of Monte Carlo sampling.
- Probabilistic machine learning: advanced topics, sections 11.3 to 11.5: [pages 513 to 521](../references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=513). Inverse-CDF sampling drawn for N(3, 1), then rejection and importance sampling.
- AI engineering, chapter 2, Sampling: [pages 188 to 199](../references/textbooks/ai-engineering/ai-engineering.pdf#page=188). How a language model picks its next token: logits, softmax, temperature, top-k, top-p and stopping conditions.
- Introduction to statistics (Wits lecture notes), section 1.3: [page 11](../references/textbooks/statistics/introduction-to-statistics.pdf#page=11). A sample of a population: the population is every item under study, the sample is the part picked to represent it, and sampling names the techniques that pick it.

**Videos**

- ritvikmath, Inverse Transform Sampling, 7:54 to 10:04: [watch](https://www.youtube.com/watch?v=9ixzzPQWuAY&t=474s). Inverts the exponential CDF and turns a uniform draw into an exponential one. Chapter-timed, from the video lessons index.
- ritvikmath, Accept-Reject Sampling, 3:52 to 7:45: [watch](https://www.youtube.com/watch?v=OXDqjdVVePY&t=232s). An easy proposal g scaled by M into an envelope above f, then each draw accepted with probability f/(M g). Caption-read, from the video lessons index.
- CME295 lecture 3, 46:35 to 50:44: [watch](https://www.youtube.com/watch?v=Q5baLehv5So&t=2795s). Samples the next token from the output distribution, restricted to the top K tokens or to the smallest set whose probabilities pass P. Caption-read.
- CME296 lecture 1, 17:26 to 23:31: [watch](https://www.youtube.com/watch?v=tr-CUpw--ck&t=1046s). Frames image generation as sampling from the data distribution and says why every method starts from Gaussian noise. Caption-read.
- Professor Leonard, Statistics lecture 1.5, Sampling Techniques, 6:17 to 12:40: [watch](https://www.youtube.com/watch?v=MfkJu7J1LE4&t=377s). What makes a sample of a population random, in the chapter "Definition of Random", before the lecture moves on to convenience, systematic and cluster samples. Chapter-timed.
- TileStats, Population vs Sample, 0:00 to 2:25: [watch](https://www.youtube.com/watch?v=YZGG5PpbJdc&t=0s). The difference between a population and a sample drawn from it, in the video's opening chapter. Chapter-timed.

**Papers**

- Chan 2024, Tutorial on diffusion models for imaging and vision, section 3.1: [pages 44 to 45](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=44). Why the inverse CDF works in one dimension and fails in many, and why sampling instead climbs toward high p(x).

**Our plans and chapters**

- [Drawing samples by hand: Monte Carlo, inverse transform and accept-reject](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/13-drawing-samples-by-hand.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, volume L3, section 13. Three ways to draw samples, each worked by hand.
- [Sampling from a graph](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/MASTER_PLAN.md), deep-learning/generative-models/03-sampling-from-a-graph. A generative model read as a directed graph and sampled one inverse-CDF draw per node.
- [Write the inverse-CDF draw as a function and check its histogram](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/06-inverse-cdf-in-code.md), the same journey, plan 06. The single draw in code, checked by its histogram.
- [Show that drawing parents first draws from the joint](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/11-ancestral-sampling-derived.md), the same journey, plan 11. Ancestral sampling derived.
- [Read DDPM's sampler as ancestral sampling on a chain](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/31-reverse-chain-as-a-factorisation.md), the same journey, plan 31. The diffusion sampler as the same parents-first draw.

**Figures**

- <a href="/home/molef/goal-setting/learning/ai-engineering/agent-architecture/artifacts/figures/agentic-engineering-course/02-the-generation-loop.png"><img src="/home/molef/goal-setting/learning/ai-engineering/agent-architecture/artifacts/figures/agentic-engineering-course/02-the-generation-loop.png" width="200" alt="Five boxes in a clockwise cycle: context comes in, calculate probabilities, sample one token, add token to context, repeat"></a> Rahul on X, "Become AI Agentic Engineer in 6 Weeks", week 1, redrawn from the article: [the post](https://x.com/sairahul1/status/2093989227696623658), [what it shows](/home/molef/goal-setting/learning/ai-engineering/agent-architecture/artifacts/figures/agentic-engineering-course/README.md#02-the-generation-looppng). A language model writes text by drawing from a distribution: the green box samples one token from the probabilities the yellow box computed, appends it, and repeats once per output token. The five equal boxes hide that computing the probabilities over the whole context costs far more than appending one token ([the reading](/home/molef/goal-setting/learning/ai-engineering/agent-architecture/sources/agentic-engineering-course/topics/02-the-generation-loop.md#what-it-does-not-carry)).

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-22. Each textbook and paper page range was read in the PDF with pdftotext; the AI engineering and Probabilistic machine learning: advanced topics pages were first found through their back-of-book indexes. Hands-on large language models covers token sampling more briefly, on PDF pages 125 to 126, and has no line. The two CME rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`, and their descriptions paraphrase the map, never the machine-translated captions. The two ritvikmath rows are copied from the video lessons index, `Mathematics/references/videos/Video Lessons.md`, sections "Inverse transform sampling" and "Accept-reject sampling". Each plan and chapter was read at its title and description. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map or the video lessons index.
>
> The lines on a sample of a population were checked on 2026-10-24: the Wits notes page was read with pdftotext, and the Professor Leonard and TileStats chapter lists were read with `cache-video-chapters.py`, so those two lines describe only each video's title and chapter titles. StatQuest's Population and Estimated Parameters (chapter "Estimated Parameters", 8:34 to 12:54) also covers estimating from a sample and has no line only to keep the list short.
