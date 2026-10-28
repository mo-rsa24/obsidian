---
aliases: [U-Net, UNet, U-shaped network, hourglass network]
standard: vault-note v2
---

# U-Net

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. It is an [[Encoder-Decoder]] for images, and the denoiser inside most image diffusion models; a condition reaches it through [[Attention]].

**A U-Net is a convolutional network that downsamples an image through an encoder, upsamples it back through a decoder to the input's size, and copies each encoder level's feature maps across to the matching decoder level, so the output keeps fine spatial detail.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the U-Net writes the rest around it.

## Where to learn this

**U-Net**, the encoder-decoder with skip connections. Also: UNet, hourglass network.

**Textbooks**

- Understanding deep learning, section 11.5.3: [pages 211 to 213](../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=211). The U-Net as an encoder-decoder whose earlier representations are concatenated to the later ones, the original's cropping of "valid" convolutions, and its segmentation of HeLa cells (figure 11.10).
- Probabilistic machine learning: an introduction, section 14.5.4: [page 534](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=534). Semantic segmentation with an encoder that convolves down to a small bottleneck, a decoder that upsamples with transposed convolution, and skip connections that give the U shape.
- Probabilistic machine learning: advanced topics, section 25.2.5: [page 896](../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=896). The U-Net as the usual denoiser of an image diffusion model, with the time step encoded as a vector and fed into its residual blocks.

**Videos**

- TileStats, U-Net clearly explained, How U-Net works, with a simple example, 2:22 to 11:58: [watch](https://www.youtube.com/watch?v=oxcgx75k6yU&t=142s). Walks the U-Net on a simple example before the original architecture. Chapter-timed.
- CS231n lecture 9, 28:28 to 32:47: [watch](https://www.youtube.com/watch?v=PTypu6GqEd4&t=1708s). The U-shaped downsampling and upsampling path with encoder feature maps copied to the decoder to keep spatial detail, still state of the art in medical segmentation. Caption-read.
- CME296 lecture 5, 19:06 to 22:11: [watch](https://www.youtube.com/watch?v=HpFdSlMeXzQ&t=1146s). Builds the U-Net for diffusion: a downsampling path that widens the receptive field to the bottleneck and an upsampling path back to the input size. Caption-read.
- CME296 lecture 5, 22:11 to 27:19: [watch](https://www.youtube.com/watch?v=HpFdSlMeXzQ&t=1331s). The crop-and-copy skip connections that concatenate encoder feature maps into the decoder, and why the output must match the input's shape. Caption-read.

**Our plans and chapters**

- [A UNet reproduces one 8×8 image](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/plans/02-a-unet-reproduces-one-image.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, plan 02. A first UNet trained until it reproduces a single 8 by 8 image.
- [Time embedding: one UNet denoises MNIST at every noise level](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/plans/03-time-embedding-one-unet-every-noise-level.md), the same journey, plan 03. One UNet told the noise level through a time embedding, so it denoises MNIST at every level.
- [Wiring VAE, UNet and cross-attention into one forward pass](/home/molef/goal-setting/learning/deep-learning/diffusion-models/latent-diffusion-architecture-rebuilt/plans/10-wire-forward-pass.md), deep-learning/diffusion-models/latent-diffusion-architecture-rebuilt, plan 10. The UNet joined to a VAE and cross-attention in one latent diffusion forward pass.
- [Where the LoRA touches the UNet, and what each place can change](/home/molef/goal-setting/learning/deep-learning/diffusion-models/where-the-lora-touches-the-unet-corridor/MASTER_PLAN.md), deep-learning/diffusion-models/where-the-lora-touches-the-unet-corridor. A corridor across two journeys about which UNet layers a LoRA adapts and what each can change.

**Scenes**

- [SDXL cross-attention, PoE and LoRA notebook, The UNet's shapes](https://claude.ai/artifact/RP59hpFThMPmbftvvWPpbi#nb-sec6). The latent's shape through a toy UNet, down to 16 by 16 and back to 128 by 128.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page was read in the PDF with pdftotext, first found through the books' back-of-book indexes ("U-Net", "U-net"). The three lecture rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`. The TileStats chapter list was read with `cache-video-chapters.py` and its line is described from chapter and video titles only. The video lessons index section "How a condition reaches a UNet through attention" covers cross-attention into a UNet rather than the UNet itself and has no line. Each plan was read at its title and position line. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map or a cached chapter list.
