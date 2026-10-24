---
aliases: [LoRA, low-rank adaptation, low rank adaptation, LoRA adapter, QLoRA]
standard: vault-note v2
---

# LoRA

Up: [[Large Language Models]]

Artificial Intelligence, Large Language Models. It is one way of doing [[Fine-Tuning]].

**LoRA fine-tunes a large model by freezing each chosen weight matrix W and training only a low-rank update BA beside it, so W + BA keeps W's shape while the trainable parameters fall from d² to 2dr.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches LoRA writes the rest around it.
> - The placement is unsure. The two best places are `Artificial Intelligence/Large Language Models/` and `Artificial Intelligence/Deep Learning/`, since the same update adapts diffusion UNets.

## Where to learn this

**LoRA**, low-rank adaptation. Also: low-rank adaptation, LoRA adapter, QLoRA.

**Textbooks**

- AI engineering, chapter 7, LoRA: [pages 649 to 663](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=649). Works the parameter saving with numbers (a 9 × 9 matrix of 81 parameters against a 9 × 1 and a 1 × 9 factor of 18), gives the merged weight W′ = W + (α/r)W_AB, then configurations, serving many adapters, and QLoRA.
- Hands-on large language models, chapter 12, LoRA: [pages 497 to 499](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=497). Rebuilds a 10 × 10 matrix from two smaller ones, 20 weights in place of 100, and why language models' low intrinsic dimension lets a small rank work.
- Hands-on large language models, chapter 12, Instruction tuning with QLoRA: [pages 503 to 511](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=503). Fine-tunes TinyLlama in code with a 4-bit base and LoRA adapters, explains the rank r, lora_alpha and target_modules settings on page 507, and merges the adapter back on page 511.

**Videos**

- CS229 lecture 12, 1:02:18 to 1:08:24: [watch](https://www.youtube.com/watch?v=_kREM2UAiJ8&t=3738s). Works the count with numbers: W₀ + AB with inner rank r cuts the free parameters from d² to 2dr, at d = 1000 and r = 10, with A started at zero so training begins at W₀. Caption-read.
- CME295 lecture 4, 1:37:48 to 1:44:56: [watch](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5868s). Freeze W₀ and learn BA with rank about 4 to 10, one pair per task; it helps most in the feed-forward layers, wants about a 10 times higher learning rate, and does worse with large batches. Caption-read.
- Luis Serrano, Low Rank Adaptation (LoRA), Small-scale example, 4:04 to 7:54: [watch](https://www.youtube.com/watch?v=Gy9jrVQTY4Q&t=244s). LoRA on a small example, before the video turns to parameter reduction and matrix rank. Chapter-timed.
- CME296 lecture 6, 1:10:05 to 1:16:14: [watch](https://www.youtube.com/watch?v=IvXTl3yj-4Y&t=4205s). LoRA in an image model: DreamBooth personalisation with a rare token, then training only a low-rank update AB to the weights. Caption-read.

**Our plans and chapters**

- [The low-rank update, B times A](/home/molef/goal-setting/learning/deep-learning/diffusion-models/latent-diffusion-architecture-rebuilt/plans/08-lora-update.md), deep-learning/diffusion-models/latent-diffusion-architecture-rebuilt, plan 08. Derives the parameter count r · (in + out) for (W + BA)x and computes it for the toy at rank 2 and the real model at rank 8.
- [Attaching the LoRA to attn2 only](/home/molef/goal-setting/learning/deep-learning/diffusion-models/latent-diffusion-architecture-rebuilt/plans/09-lora-attn2-only.md), the same journey, plan 09. The real model attaches its adapter to the cross-attention projections `attn2.to_q`, `to_k` and `to_v` and never to `attn1`, and this plan states the cost and the reason on paper.
- [Training the toy LoRA on single concepts, testing on the joint](/home/molef/goal-setting/learning/deep-learning/diffusion-models/latent-diffusion-architecture-rebuilt/plans/12-train-toy-lora.md), the same journey, plan 12. Trains the injected adapter on two concepts alone and runs it on their combination.
- [Four adapter settings, two prompts, and the number that matters](/home/molef/goal-setting/learning/deep-learning/diffusion-models/where-the-lora-touches-the-unet-corridor/plans/02-four-adapters-two-prompts.md), deep-learning/diffusion-models/where-the-lora-touches-the-unet-corridor, plan 02. The toy rendered with no LoRA, `attn2` only, `attn1` only and both, on two prompts, then one number for how much the `attn1`-only correction moves when the prompt changes.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after the books' back-of-book indexes pointed to them ("LoRA (low-rank adaptation)" and "QLoRA" in both books). The CS229, CME295 and CME296 rows were read in the caption-read lecture maps under `~/.claude/cache/captions/` and paraphrase the map, never the machine-translated captions. The Serrano line comes from the video's chapter list, read with cache-video-chapters.py, and is described from the chapter title only. CS229 lecture 12 at 1:08:24 to 1:15:36 weighs LoRA's costs and was left out to keep four videos. Each plan was read at its title and description. The paper Test-time compositional generalization via concept discovery uses LoRA as a baseline without teaching it and has no line.
