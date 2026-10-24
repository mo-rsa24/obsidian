---
aliases: [encoder-decoder, encoder, decoder, encoder-decoder architecture, encoder-decoder model, sequence-to-sequence, seq2seq, encoder-only, decoder-only]
link-skip: [cross-encoder, bi-encoder, GPT-2 encoder, tiktoken]
standard: vault-note v2
---

# Encoder-Decoder

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. The [[U-Net]] is an encoder-decoder for images, a transformer's decoder reads its encoder through [[Cross-Attention]], and [[Variational Autoencoders]] train an encoder and decoder together through the [[Evidence Lower Bound]].

**An encoder maps an input to an internal representation (a code, a latent or a sequence of vectors) and a decoder maps that representation to the output, so an encoder-decoder network can turn one kind of thing into another, such as an English sentence into French or a noisy latent back into an image.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches encoders and decoders writes the rest around it.

## Where to learn this

**Encoder and decoder**, the two halves of an encoder-decoder network. Also: encoder, decoder, sequence-to-sequence, seq2seq, encoder-only, decoder-only.

**Textbooks**

- Understanding deep learning, sections 12.6 to 12.8: [pages 233 to 241](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=233). The three transformer layouts: an encoder model (BERT), a decoder model (GPT3), and an encoder-decoder for English-to-French translation whose decoder layers also attend to the encoder's output.
- Deep learning textbook, section 10.4: [pages 412 to 414](../../Mathematics/references/textbooks/machine-learning/deep-learning-textbook.pdf#page=412). The recurrent sequence-to-sequence architecture: an encoder reads the input sequence into a context C, and a decoder generates an output sequence of a different length from it (figure 10.12).
- Understanding deep learning, section 10.5.3: [page 193](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=193). A segmentation network whose downsampling side is called the encoder and upsampling side the decoder, an hourglass shape that leads to the U-Net.
- Mathematics for machine learning, section 10.8: [page 349](../../Mathematics/references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=349). PCA read as a linear auto-encoder: the encoder maps the data to a code z and the decoder maps it back to an approximation of the data.

**Videos**

- StatQuest, Sequence-to-Sequence (seq2seq) Encoder-Decoder Neural Networks, Building the Encoder, 3:43 to 8:27: [watch](https://www.youtube.com/watch?v=L8HKweZIOmg&t=223s). Builds the encoder half of a small seq2seq network, before the decoder chapter that follows (8:27 to 12:58). Chapter-timed.
- CS231n lecture 8, 2:37 to 9:11: [watch](https://www.youtube.com/watch?v=RQowiOF_FvQ&t=157s). A recurrent network translating "we see the sky" to Italian: the encoder squeezes the input into one context vector and the decoder generates words, and that fixed-size vector is a bottleneck for long inputs. Caption-read.
- CME295 lecture 3, 1:03 to 7:19: [watch](https://www.youtube.com/watch?v=Q5baLehv5So&t=63s). The three transformer families, encoder-decoder T5, encoder-only BERT and decoder-only GPT without cross-attention, then an LLM defined as a decoder-only language model of at least a billion parameters. Caption-read.
- CME296 lecture 4, 1:00:16 to 1:05:58: [watch](https://www.youtube.com/watch?v=WUUq6TVAu8U&t=3616s). The trade-off inside a latent diffusion autoencoder: the encoder keeps semantics so the latent space is easy to learn, and a larger decoder restores perceptual detail. Caption-read.

**Our plans and chapters**

- [Run cross-attention with a 2-word decoder reading a 3-word encoder](/home/molef/goal-setting/learning/deep-learning/transformers/plans/46-run-cross-attention-with-a-2-word.md), deep-learning/transformers, plan 46. Works the numbers: decoder words D = [[0.9, 0.1], [0.1, 0.9]] ask, encoder words E = [[1, 0], [0.8, 0.6], [0, 1]] supply keys and values, and the weights and outputs are printed in code.
- [Say how cross-attention differs from self-attention](/home/molef/goal-setting/learning/deep-learning/transformers/textbook/45-say-how-cross-attention-differs-from-self.md), the same journey, chapter 45. Queries from the decoder, keys and values from the encoder, traced row by row on a toy with identity projections.
- [The VAE encoder, decoder, and the latent](/home/molef/goal-setting/learning/deep-learning/diffusion-models/latent-diffusion-architecture-rebuilt/plans/03-vae-latent.md), deep-learning/diffusion-models/latent-diffusion-architecture-rebuilt, plan 03. The image encoder and decoder of a latent diffusion model, and the latent between them.
- [A VAE on MNIST, from the ELBO](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/plans/05-a-vae-on-mnist-from-the-elbo.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, plan 05. An encoder and decoder trained together on MNIST from the ELBO.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page range was read in the PDF with pdftotext, first found through the books' back-of-book indexes ("encoder-decoder network", "encoder, transformer", "decoder") and the shelf index's chapter tables. The four lecture rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`. The StatQuest chapter list was read with `cache-video-chapters.py` and its line is described from chapter and video titles only. Each plan and chapter was read at its title and the lines naming its toy. Bare "decoder" is an alias because all 25 sampled uses in the learning tree mean a network's decoder; bare "encoder" is one because about 15 of 25 do, and the link-skip phrases cover the rest: cross-encoder and bi-encoder rerankers, and tiktoken's GPT-2 encoder that turns text into token ids. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map or a cached chapter list.
