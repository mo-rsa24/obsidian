---
aliases: [fine-tuning, fine-tune, finetuning, finetune, supervised fine-tuning, supervised finetuning, SFT, instruction tuning, full fine-tuning]
standard: vault-note v2
---

# Fine-Tuning

Up: [[Large Language Models]]

Artificial Intelligence, Large Language Models. A cheap way to do it, training only a small update, has its own note: [[LoRA]].

**Fine-tuning continues training a pretrained model on a smaller task-specific dataset, and supervised fine-tuning does it on prompt and response pairs so a base model that only continues text learns to follow instructions.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches fine-tuning writes the rest around it.
> - The placement is unsure. The two best places are `Artificial Intelligence/Large Language Models/` and `Artificial Intelligence/Deep Learning/`, since any pretrained network is fine-tuned the same way.

## Where to learn this

**Fine-tuning**, further training of a pretrained model on task data. Also: fine-tune, finetuning, supervised fine-tuning, SFT, instruction tuning.

**Textbooks**

- Hands-on large language models, chapter 12, Instruction tuning with QLoRA: [pages 503 to 511](../../Mathematics/references/textbooks/natural-language-processing/hands-on-large-language-models.pdf#page=503). Works supervised fine-tuning end to end in code: TinyLlama, a base model that cannot follow instructions, is given chat-templated instruction data, trained with SFTTrainer and then prompted.
- AI engineering, chapter 2, Supervised finetuning: [pages 173 to 179](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=173). Why a pre-trained model completes "How to make pizza" instead of answering it, and the demonstration data (InstructGPT's task mix) that SFT trains on.
- AI engineering, chapter 7, Finetuning overview: [pages 596 to 601](../../Mathematics/references/textbooks/ai-engineering/ai-engineering.pdf#page=596). Fine-tuning as transfer learning, why it needs a few hundred examples where training from scratch needs millions, and who fine-tunes what (the Code Llama variants in Figure 7-1).
- Understanding deep learning, section 9.3.6: [pages 165 to 166](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=165). Transfer learning in general: replace the last layer, then train only the new layers or fine-tune the entire model.

**Videos**

- CME295 lecture 4, 1:02:19 to 1:08:32: [watch](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3739s). Starts from "can I wash my teddy bear in the washing machine?", which a pretrained model only continues, and defines SFT: train on prompt and response pairs with the loss on the response tokens only. Caption-read.
- CS229 lecture 16, 1:04:17 to 1:08:20: [watch](https://www.youtube.com/watch?v=hHC-SF3utxg&t=3857s). Instruction tuning as supervised fine-tuning: minimise −Σₜ log p_θ(y_t ∣ x, y_<t) over instruction and response pairs, starting from the pretrained checkpoint. Caption-read.
- Stanford CS224N 2023 lecture 9, 29:58 to 35:53: [watch](https://www.youtube.com/watch?v=DGfCRXuNA2w&t=1798s). Pretraining followed by fine-tuning on a task's own data. Chapter-timed, from the video lessons index.
- CS231n lecture 6, 58:00 to 1:07:03: [watch](https://www.youtube.com/watch?v=aVJy4O5TOk8&t=3480s). Fine-tuning outside language models: freeze an ImageNet network and train a new last layer on small data, or fine-tune everything with more data. Caption-read.

**Our plans and chapters**

- [OPT as the baseline: a 2022 base model on structured output, and why it fails](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/open-models/plans/03-opt-as-the-baseline.md), ai-engineering/one-business-end-to-end/open-models, plan 03. Runs a base model with no instruction tuning on the coffee shop's SQL-only prompt ten times and counts the failures, so instruction tuning becomes something you can point at.
- [Prune a trained layer by weight size, and find where it breaks](/home/molef/goal-setting/learning/deep-learning/model-compression/plans/02-magnitude-pruning.md#4--fine-tune-past-the-knee), deep-learning/model-compression, plan 02. A 300-step fine-tune with the pruning mask held wins back the accuracy a one-shot prune lost.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, after the books' back-of-book indexes pointed to them ("SFT (supervised fine-tuning)" and "fine-tuning generative models" in Hands-on large language models, "supervised finetuning (SFT)" and "finetuning, overview" in AI engineering, "fine-tuning" in Understanding deep learning). The CME295, CS229 and CS231n rows were read in the caption-read lecture maps under `~/.claude/cache/captions/` and paraphrase the map, never the machine-translated captions. The CS224N row is copied from the video lessons index, `Mathematics/references/videos/Video Lessons.md`, section "Fine-tuning a pretrained model", whose times are chapter boundaries. Each plan was read at its title and description. The model-adaptation scope in `ai-engineering/llm-applications/` is about fine-tuning but holds no plans yet, so it has no line.
