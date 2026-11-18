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
- Principles and practice of deep representation learning, section 8.6.4, Realizing denoising with a U-Net: [pages 383 to 386](../../Mathematics/references/textbooks/machine-learning/deep-representation-learning.pdf#page=383). Traces the denoising U-Net from DDPM through the ADM ablations to the latent diffusion U-Net with cross-attention: encoder stages, a bottleneck with self-attention, a mirrored decoder joined by skip connections, a sinusoidal timestep embedding, and why it scales worse than a transformer.

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

- [The SDXL notebook in ten parts, The UNet's shapes](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-image). The latent's shape through a toy UNet, down to 16 by 16 and back to 128 by 128.
- [SDXL as a latent diffusion model, The UNet box](https://claude.ai/artifact/KPpMEVBfkJnq3mwgGSbyPs#unet). One denoising call: the noisy latent, the step, and what the prompt said, in and a noise prediction out.
- [Why the latent is scaled, What runs 50 times](https://claude.ai/artifact/7yTQUKjEawymqWRnk9gvjn#p5). The two routes the prompt takes into the UNet: cross-attention at every resolution, and one vector added to the timestep embedding.
- [SDXL pipeline map, conv_in](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#conv-in). A 3 × 3 convolution lifting 4 channels to 320.
- [SDXL pipeline map, Down block 0](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#down-0). ResBlocks only: group norm, convolution, the time vector added, the skip.
- [SDXL pipeline map, Down block 2](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#down-2). The same pairing at 32 × 32, ten transformer blocks deep.
- [SDXL pipeline map, Middle block](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#mid). ResBlock, a ten-deep attention stack, ResBlock, at 32 × 32 with 1280 channels.
- [SDXL pipeline map, Up block 0](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#up-0). Each ResBlock joining a saved skip; one patch's self-attention against its cross-attention.
- [SDXL pipeline map, Up block 2](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#up-2). The last up block's ResBlocks, back at 128 × 128.
- [SDXL pipeline map, conv_out](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#conv-out). Group norm, SiLU and conv_out to the noise prediction ε_θ, 4 × 128 × 128.
- [SDXL code walk, Hidden: one U-Net call gives both predictions](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#unet_call). X_t twice, t, C and the conditioning in; noise_pred (2, 4, 128, 128) out.
- [SDXL code walk, Hidden: conv_in lifts 4 channels to 320](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#conv_in). A 3 × 3 convolution, (2, 320, 128, 128) out.
- [SDXL code walk, Hidden: three down blocks, each output saved for a skip](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#down). Down 0 ResBlocks only, down 1 and 2 with attention stacks reading C, every output kept for the up path.
- [SDXL code walk, Hidden: the middle block](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#mid). ResBlock, a ten-deep attention stack, ResBlock, at 32 × 32 with 1280 channels.
- [SDXL code walk, Hidden: three up blocks, each joining the saved skips](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#up). Each up block joining a saved output to each ResBlock's input along the channels.
- [SDXL code walk, Output: group norm, SiLU, conv_out to 4 channels](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#conv_out). The prediction in the latent's own shape, ε_uncond and ε_c of lengths 246.02 and 246.15.
- [SDXL code walk, Hidden: one ResBlock, group norm, conv, + e_t, group norm, conv, skip](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#resblock). One ResBlock at 64 × 64, 320 channels in and 640 out, group norm over 32 groups of 10 channels.
- [SDXL code walk, Hidden: a down block pairs each ResBlock with an attention stack](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#crossattn_down). A ResBlock then a transformer stack reading C, twice, then a stride-2 convolution.
- [SDXL code walk, Hidden: an up block joins a skip before every ResBlock](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#crossattn_up). The saved feature map joined along the channels, 2560 channels into up block 0's first ResBlock.
- [Readout Guidance loop walk, The head: each decoder resnet keeps its hidden state](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#rn_hidden). Each tapped resnet keeps hidden_states after conv2 and before the skip is added back.
- [Readout Guidance loop walk, The head: which layers are tapped, the up-block resnets only](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#rn_collect). The nine up-block resnets of SDXL, 1280, 640 and 320 channels; the mid and down blocks never read.
- [Readout Guidance loop walk, Frozen model: the U-Net run for exactly one step](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#df_steps). The frozen U-Net run for one step on the empty prompt to give the features.
- [Count head walk, Ours: three whole blocks read through forward hooks](https://claude.ai/artifact/2VgqMaBHqrXNoHdTWjxro1#c_readout). Hooks on the mid block and up blocks 0 and 1 keeping each block's output.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-24. Each textbook page was read in the PDF with pdftotext, first found through the books' back-of-book indexes ("U-Net", "U-net"). The three lecture rows were read in their caption-read lecture maps under `~/.claude/cache/captions/`. The TileStats chapter list was read with `cache-video-chapters.py` and its line is described from chapter and video titles only. The video lessons index section "How a condition reaches a UNet through attention" covers cross-attention into a UNet rather than the UNet itself and has no line. Each plan was read at its title and position line. A script then opened every link and confirmed the file exists, the page is inside the PDF, and each video start matches a row's start in a lecture map or a cached chapter list.
