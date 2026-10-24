---
aliases: [LLM-as-a-judge, LLM as a judge, LLM judge, LLM judges, AI as a judge, AI judge, judge model, LLMs-as-judges, LLM-as-judge]
standard: vault-note v2
---

# LLM As A Judge

Up: [[Artificial Intelligence]]

Artificial Intelligence. The statistics of checking a judge against people are in [[Chance-Corrected Agreement]] and [[Selective Evaluation]].

**LLM-as-a-judge uses one language model to grade another model's answers against written criteria, in place of a human grader.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches LLM-as-a-judge writes the rest around it.
> - The placement is unsure. The two best places are this top level and an Evaluation family under `Artificial Intelligence/`, which does not exist yet.

## Where to learn this

**LLM-as-a-judge**, also AI as a judge. Also: LLM judge, AI judge, judge model, LLMs-as-judges.

**Textbooks**

- AI engineering, chapter 3, AI as a Judge: [pages 271 to 281](../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=271). Defines the AI judge, says why teams use one, and gives naive prompts for its three uses: score a response alone, against a reference, or against another response, with a judge being the model plus its prompt.
- AI engineering, chapter 3, limitations and biases of AI as a judge: [pages 281 to 295](../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=281). Inconsistency, ambiguous criteria, cost and latency, then self, position and verbosity bias (page 289), and which models can act as judges.

**Videos**

- CME295 lecture 8, 27:47 to 32:23: [watch](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1667s). Introduces the judge: it reads the prompt, the response and the criteria, and returns a rationale before a score. Caption-read.
- CME295 lecture 8, 38:35 to 42:17: [watch](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2315s). Position bias, fixed by asking A against B and B against A, and verbosity bias, fixed by instructions, examples or a length penalty. Caption-read.
- CME295 lecture 8, 47:03 to 52:37: [watch](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2823s). Best practices: crisp criteria, a binary pass or fail scale, rationale before score, calibration against human ratings, temperature around 0.1 to 0.2. Caption-read.
- CME296 lecture 7, 1:23:58 to 1:29:13: [watch](https://www.youtube.com/watch?v=iNaRBp4T57Q&t=5038s). A multimodal LLM as a judge of generated images, given the prompt, the image and a rubric, then aligned with people in three stages. Caption-read.

**Papers**

- Zheng and others 2023, Judging LLM-as-a-judge with MT-Bench and Chatbot Arena: [pages 4 to 6](/home/molef/goal-setting/learning/papers/llms/llm-as-a-judge/2306.05685.pdf#page=4). Names three judge setups (pairwise comparison, single-answer grading, reference-guided grading) and measures position, verbosity and self-enhancement bias.
- Gu and others, A survey on LLM-as-a-judge: [pages 6 to 7](/home/molef/goal-setting/learning/papers/llms/llm-as-a-judge/A%20Survey%20on%20LLM-as-a-Judge.pdf#page=6). Gives a formal definition, E ← P_LLM(x ⊕ C), with the input, the context and the evaluation each named.
- Thakur and others 2024, Judging the judges: [pages 1 to 5](/home/molef/goal-setting/learning/papers/llms/llm-as-a-judge/2406.12624.pdf#page=1). Measures how well judge models agree with human graders, shows that percent agreement hides differences Scott's π reveals, and finds a bias toward leniency.
- Shankar and others 2024, Who validates the validators: [pages 1 to 2](/home/molef/goal-setting/learning/papers/llms/llm-as-a-judge/Aligning%20LLM-Assisted%20Evaluation.pdf#page=1). Aligning a judge's criteria with people's grades, and criteria drift: grading outputs changes the criteria people meant to grade by.

**Our plans and chapters**

- [Validating an LLM judge](/home/molef/goal-setting/learning/ai-engineering/agent-evaluation/validating-an-llm-judge/MASTER_PLAN.md), ai-engineering/agent-evaluation. Who is graded, who grades, and how far the judge agrees with a person, computed from a 2 by 2 table for the v3 product-content judge.
- [The four roles](/home/molef/goal-setting/learning/ai-engineering/agent-evaluation/validating-an-llm-judge/plans/01-the-four-roles.md), plan 01 of the same journey. Names who is graded, who grades, what the judge reads and what it is scored against, first for Thakur and others' setup.
- [Selective evaluation for LLM judges](/home/molef/goal-setting/learning/ai-engineering/agent-evaluation/selective-evaluation/MASTER_PLAN.md), ai-engineering/agent-evaluation. Picks the confidence threshold above which a judge may publish, from a labelled calibration set.
- [Each answer as an MLflow trace, your row judge beside the built-in judge](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/plans/60-traces-and-two-judges.md), ai-engineering/one-business-end-to-end, plan 60. Logs forty answers as traces and runs a hand-written judge beside MLflow's built-in one.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-22. Each textbook page range was read in the PDF with pdftotext, after finding it through the links in the AI engineering book's back-of-book index (PDF pages 932 to 988). Hands-on large language models names LLM-as-a-judge only once, on PDF page 358, in a paragraph about the Ragas library, so it has no line. Each video row was read in its course's caption-read lecture map under `~/.claude/cache/captions/`, and its description paraphrases the map, never the machine-translated captions. Each paper was opened at the pages given; the four sit in `papers/llms/llm-as-a-judge/`, which `Papers.md` does not index yet. Each plan was read at its title and description. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start.
