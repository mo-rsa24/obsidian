# Scenes

The shelf of interactive pages built across the learning journeys and projects: scenes, notebook walks and system drawings. Each section says what one page is for and which places in it show an idea, so a word that has a concept card can open the exact place a scene shows it. `scene-cards.py` copies every row onto the cards it names, under **Scenes**, and `link-concepts.py --refresh-marks` then puts a ◈ mark after the word wherever it is linked.

## How a scene is kept here

**One section per page.** The heading is the page's name. The comment under it holds the page's link, then a paragraph says what the page is for and what it is built from.

**One row per place.** "Where" links the place in the page (a level's anchor), "What it shows" says it in the words a reader would look for, and "Cards" links the concept cards whose idea that place shows. A row with no card is still kept: it names an idea worth a card.

**Written when the page is.** The session or agent that publishes a scene writes or updates its section in the same act, then runs `python3 -I ~/.claude/skills/concept-link/scripts/scene-cards.py --apply`.

## Kinds of composition notebook
<!-- scene: https://claude.ai/artifact/DBmJtn6xy75sPtQwPEvQZU -->

The worked-examples notebook for claims 1 and 7 of the overlap-dial idea map (`/home/molef/PhD/poe_repair_min-dog-and-rain/artifacts/ideas/poe-overlap-dial/what-an-expert-learns-and-kinds-of-composition.ipynb`), drawn section by section from its own headings. Each section opens into its cells and functions, every line can be walked with its maths in steps, each cell shows the figure it drew, and the words in its markdown link to where they are taught. No network is trained: every expert is the ideal one, the training points smoothed by a Gaussian.

| Where | What it shows | Cards |
|---|---|---|
| [Setup: the ideal expert](https://claude.ai/artifact/DBmJtn6xy75sPtQwPEvQZU#nb-sec1) | the ideal expert's log-density on a grid, in four steps from the 2D Gaussian to its logsumexp form, then normalised so it integrates to 1 | [Probability Density Function](../../Statistics/Distributions/Probability%20Density%20Function.md), [Multivariate Normal Distribution](../../Statistics/Distributions/Multivariate%20Normal%20Distribution/Multivariate%20Normal%20Distribution.md), [Log-Sum-Exp](../../Algebra/Logarithms/Log-Sum-Exp.md), [Diffusion Models](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Diffusion%20Models.md) |
| [Same points, two labellings](https://claude.ai/artifact/DBmJtn6xy75sPtQwPEvQZU#nb-sec2) | the denoising loss and one gradient step, showing the gradient is identical under two labellings because no label enters the loss | [Loss Function](../../../Artificial%20Intelligence/Machine%20Learning/Loss%20Function.md), [Gradient](../../Calculus/Gradient.md), [Backpropagation](../../../Artificial%20Intelligence/Deep%20Learning/Backpropagation.md) |
| [A classifier learns "not B"](https://claude.ai/artifact/DBmJtn6xy75sPtQwPEvQZU#nb-sec4) | a classifier trained on the labels the data carries learns the hidden-B points as "not B" | [Classifier](../../../Artificial%20Intelligence/Machine%20Learning/Classifier.md) |
| [Four kinds of composition](https://claude.ai/artifact/DBmJtn6xy75sPtQwPEvQZU#nb-sec5) | co-occurrence, contention and interaction computed as products of two experts' densities on one grid | [Product Of Experts](../../../Artificial%20Intelligence/Generative%20Modeling/Product%20Of%20Experts.md) |

## The SDXL notebook in ten parts
<!-- scene: https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW -->

The teaching notebook `/home/molef/PhD/SDXL/notebooks/sdxl_crossattn_poe_lora.ipynb`, drawn as ten parts in the order one denoising step runs, each opening into its cells and the functions they define. Every numeric line can be walked with its maths in steps. Everything runs on toy tensors with SDXL's shapes: the latent, the two text encoders, the cross-attention, the product-of-experts composition that fails on "a cat and a dog", and the LoRA that repairs it. The notebook stores no figures, because its last run used a non-interactive plotting backend.

| Where | What it shows | Cards |
|---|---|---|
| [Forward diffusion](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-latent) | the clean latent and noise mixed into the noisy latent at t = 50, 500 and 950 under the cosine schedule, with alpha-bar worked to 0.992, 0.494 and 0.006 | [Diffusion Models](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Diffusion%20Models.md), [The Forward Process](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/The%20Forward%20Process.md), [The Cosine Noise Schedule](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/The%20Cosine%20Noise%20Schedule.md) |
| [Tokenizing the prompt](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-text) | "a cat and a dog" turned into 77 token ids, 7 words and 70 padding | [Tokenization](../../../Artificial%20Intelligence/Large%20Language%20Models/Tokenization.md) |
| [Two text encoders](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-text) | SDXL's two text encoders, 768 and 1280 wide, joined per token into 2048 | no card yet |
| [The UNet's shapes](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-image) | the latent's shape through a toy UNet, down to 16 by 16 and back to 128 by 128 | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [Feature maps into image tokens](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-image) | a 64 by 64 feature map flattened into 4096 image tokens, with every query, key and value shape traced | no card yet |
| [Self-attention](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-attn) | self-attention among image tokens, a 4096 by 4096 map at full size | [Attention](../../../Artificial%20Intelligence/Deep%20Learning/Attention.md), [Softmax](../../../Artificial%20Intelligence/Deep%20Learning/Softmax.md) |
| [Cross-attention](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-attn) | cross-attention from 4096 image tokens to 77 text tokens, softmax over each row, scaled by one over root d | [Cross-Attention](../../../Artificial%20Intelligence/Deep%20Learning/Cross-Attention.md), [Softmax](../../../Artificial%20Intelligence/Deep%20Learning/Softmax.md) |
| [PoE fails on cat and dog](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-poe) | adding a cat expert's score to a dog expert's lands at the origin, distance 2 from both modes, while the two-mode mixture's score keeps both | [Product Of Experts](../../../Artificial%20Intelligence/Generative%20Modeling/Product%20Of%20Experts.md), [Score Function](../../../Artificial%20Intelligence/Generative%20Modeling/Score%20Function.md) |
| [Guidance inside each PoE branch](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-poe) | classifier-free guidance applied to each prompt's branch before the PoE sum | [Classifier-Free Guidance](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Classifier-Free%20Guidance.md), [Product Of Experts](../../../Artificial%20Intelligence/Generative%20Modeling/Product%20Of%20Experts.md) |
| [LoRA on cross-attention](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-lora) | a frozen projection plus a low-rank update that starts at zero, on the query, key and value projections | [LoRA](../../../Artificial%20Intelligence/Large%20Language%20Models/LoRA.md) |
| [Training LoRA against the Mono teacher](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-lora) | the student's guided PoE on prompts A and B trained toward a frozen teacher on the joint prompt, with gradients reaching only A and B | [LoRA](../../../Artificial%20Intelligence/Large%20Language%20Models/LoRA.md), [Classifier-Free Guidance](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Classifier-Free%20Guidance.md) |
| [Residual injection](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-infer) | the frozen and adapted noise predictions blended by lambda, shown equal to linear interpolation | [LoRA](../../../Artificial%20Intelligence/Large%20Language%20Models/LoRA.md) |
| [The DDIM step](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-infer) | the clean latent predicted from the noise, then re-noised to the earlier step | [DDIM](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/DDIM.md) |
| [Attention shifted by training](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-see) | a dog-snout query whose attention on 'dog' rises from 0.239 by real gradient steps on a LoRA | [Cross-Attention](../../../Artificial%20Intelligence/Deep%20Learning/Cross-Attention.md), [LoRA](../../../Artificial%20Intelligence/Large%20Language%20Models/LoRA.md) |

## SDXL as a latent diffusion model
<!-- scene: https://claude.ai/artifact/KPpMEVBfkJnq3mwgGSbyPs -->
<!-- kind: map -->
<!-- home: PhD poe_repair_min, artifacts/results/how-sdxl-turns-a-prompt-into-an-image -->
<!-- source: /home/molef/PhD/poe_repair_min/artifacts/results/how-sdxl-turns-a-prompt-into-an-image/sdxl-ldm-high-level-design-explainer.json -->

The whole SDXL sampling pipeline as a system map: seventeen running parts in four lanes, every box
opening onto the lines of pipeline code that run it. Built from a forward-hook trace of one 50-step
generation, so every shape on it is a shape that was actually passed. Its unit is a running part, not
a layer, which is why the VAE appears here as two boxes and has its own page below.

**Also useful in**: a plan or note that needs where a piece of SDXL sits before going into it;
the conditioning lane is the only place the size, crop and aspect-ratio vector is drawn.

**Caveat**: the trace is one generation of one prompt; counts of steps and shapes are that run's.

| Where | What it shows | Cards |
|---|---|---|
| [The pixel space lane](https://claude.ai/artifact/KPpMEVBfkJnq3mwgGSbyPs#pixel-space) | where images become latents and back, as methods of AutoencoderKL, with the 48-fold size drop | [Diffusion Models](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Diffusion%20Models.md) |
| [The latent space lane](https://claude.ai/artifact/KPpMEVBfkJnq3mwgGSbyPs#latent-space) | the sampling loop built once and called fifty times: expand, scale, call the UNet, guide, step | [Diffusion Models](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Diffusion%20Models.md), [Classifier-Free Guidance](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Classifier-Free%20Guidance.md) |
| [The timestep embedding lane](https://claude.ai/artifact/KPpMEVBfkJnq3mwgGSbyPs#timestep) | the pooled text and the size, crop and aspect-ratio numbers turned into Fourier features, concatenated to 2816 and projected to 1280, then added to the timestep embedding | no card yet |
| [The cross-attention lane](https://claude.ai/artifact/KPpMEVBfkJnq3mwgGSbyPs#cross-attention) | two text encoders concatenated per token into 77 by 2048, entering the UNet at every resolution | [Cross-Attention](../../../Artificial%20Intelligence/Deep%20Learning/Cross-Attention.md), [Tokenization](../../../Artificial%20Intelligence/Large%20Language%20Models/Tokenization.md), [Attention](../../../Artificial%20Intelligence/Deep%20Learning/Attention.md) |
| [The UNet box](https://claude.ai/artifact/KPpMEVBfkJnq3mwgGSbyPs#unet) | one denoising call: the noisy latent, the step, and what the prompt said, in and a noise prediction out | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |

## Inside the SDXL VAE
<!-- scene: https://claude.ai/artifact/PWPgjgzaRtjZnBMnVXx3BU -->
<!-- kind: scene -->
<!-- home: PhD poe_repair_min, artifacts/results/how-the-sdxl-vae-is-built -->
<!-- source: /home/molef/PhD/poe_repair_min/artifacts/results/how-the-sdxl-vae-is-built/build_page.py -->

The SDXL autoencoder as a hierarchy, sixteen stages across encoder and decoder, each opening into its
own modules and then into the lines of diffusers source that run them. All 242 traced modules are
reachable, the convolution arithmetic is worked against the traced shapes rather than asserted, and
the residual chain can be walked line by line with its equations rendered beside the code.

**Also useful in**: anything that needs what an encoder-decoder actually contains at full depth, or
the reparameterisation as real code rather than as an equation.

**Caveat**: shapes and parameter counts are from one forward hook at batch 1 on a 1024 by 1024 image.

| Where | What it shows | Cards |
|---|---|---|
| [The latent z stage](https://claude.ai/artifact/PWPgjgzaRtjZnBMnVXx3BU#x-latent) | the encoder's eight channels split into a four-channel mean and a four-channel log-variance, and the latent drawn as mean plus sigma times epsilon | [KL Divergence](../../Statistics/Information%20Theory/KL%20Divergence.md) |
| [down 0](https://claude.ai/artifact/PWPgjgzaRtjZnBMnVXx3BU#encoder-down_blocks-0) | one encoder stage walked line by line: group norm, the activation, the 3 by 3 convolution, the second pair, then the skip | no card yet |
| [The encoder mid block](https://claude.ai/artifact/PWPgjgzaRtjZnBMnVXx3BU#encoder-mid_block) | the narrowest point, where a self-attention block lets every position see every other before the code is formed | [Attention](../../../Artificial%20Intelligence/Deep%20Learning/Attention.md) |
| [conv_in](https://claude.ai/artifact/PWPgjgzaRtjZnBMnVXx3BU#encoder-conv_in) | the first convolution, with the output-size arithmetic worked against the shape the hook saw | no card yet |
| [The decoder stages](https://claude.ai/artifact/PWPgjgzaRtjZnBMnVXx3BU#decoder-mid_block) | the half that runs at sampling time, three resnets per block against the encoder's two, forced to fp32 | no card yet |

## Why the latent is scaled
<!-- scene: https://claude.ai/artifact/7yTQUKjEawymqWRnk9gvjn -->
<!-- kind: walk -->
<!-- home: PhD poe_repair_min, artifacts/results/why-the-latent-is-scaled -->
<!-- source: /home/molef/PhD/poe_repair_min/artifacts/results/why-the-latent-is-scaled/build_page.py -->

Eleven frames on why SDXL multiplies its latent by 0.13025: what the pipeline costs in pixels, what
the autoencoder is for, what the diffusion schedule assumes about the size of its data, and what
happens when the factor is removed. The schedule, the signal-to-noise ratio and every curve are
recomputed in the browser from SDXL's own scaled-linear betas, and the forward process is run on a
real SDXL sample so the break is watchable: at the same step the calibrated square is noise and the
uncalibrated one still holds the picture.

**Also useful in**: any plan or note that meets the noise schedule, signal-to-noise over a diffusion
run, or why a latent space needs a fixed scale; the prediction question before the reveal is a
ready-made check.

**Caveat**: the squares show a real SDXL sample standing in for the latent, which is a 4 by 128 by
128 code and not a picture; the raw spread 7.68 is inferred from 1/0.13025, not measured.

| Where | What it shows | Cards |
|---|---|---|
| [A prompt in, a megapixel out](https://claude.ai/artifact/7yTQUKjEawymqWRnk9gvjn#p1) | the pixel grid and the latent grid drawn to scale by number count, 3,145,728 against 65,536, and what fifty passes over each would cost | [Diffusion Models](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Diffusion%20Models.md) |
| [The autoencoder is a learned codec](https://claude.ai/artifact/7yTQUKjEawymqWRnk9gvjn#p2) | encode and decode around a latent drawn to scale and deliberately blank, because the latent is not a picture | no card yet |
| [The shape of the squeeze](https://claude.ai/artifact/7yTQUKjEawymqWRnk9gvjn#p3) | the encoder narrowing and the decoder widening, with width as the spatial size and height as the channel count | no card yet |
| [Why it is variational](https://claude.ai/artifact/7yTQUKjEawymqWRnk9gvjn#p4) | draws of the code around the encoder's centre at its predicted spread, and why nearby codes have to decode to similar images | [KL Divergence](../../Statistics/Information%20Theory/KL%20Divergence.md) |
| [What runs 50 times](https://claude.ai/artifact/7yTQUKjEawymqWRnk9gvjn#p5) | the two routes the prompt takes into the UNet: cross-attention at every resolution, and one vector added to the timestep embedding | [Cross-Attention](../../../Artificial%20Intelligence/Deep%20Learning/Cross-Attention.md), [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [The schedule mixes in a fixed ratio](https://claude.ai/artifact/7yTQUKjEawymqWRnk9gvjn#p6) | the signal and noise weights at each of the 1000 steps, to scale, with a real sample shown at that step | [The Forward Process](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/The%20Forward%20Process.md), [The Cosine Noise Schedule](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/The%20Cosine%20Noise%20Schedule.md) |
| [The autoencoder hands over something larger](https://claude.ai/artifact/7yTQUKjEawymqWRnk9gvjn#p7) | the latent's value distribution against the unit normal the schedule assumes, at the shipped factor and at 1 | no card yet |
| [Move the factor and watch it go wrong](https://claude.ai/artifact/7yTQUKjEawymqWRnk9gvjn#p9) | signal-to-noise over the whole schedule as the factor moves, against the unit-scale curve it is meant to sit on, with eight steps shown as pictures | [The Forward Process](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/The%20Forward%20Process.md) |
| [Take it out entirely](https://claude.ai/artifact/7yTQUKjEawymqWRnk9gvjn#p10) | the same step and the same noise draw at two factors, where one square is noise and the other still holds the picture | [The Forward Process](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/The%20Forward%20Process.md) |

## HR policy assistant on local Postgres
<!-- scene: https://claude.ai/artifact/Gsj44q2Vehu8RNjgJyWwpb -->
<!-- kind: map -->
<!-- home: xbigly internal-policies-rag, artifacts/results/how-the-hr-policy-assistant-works -->
<!-- source: /Users/molefemolefe/xbigly/internal-policies-rag/artifacts/results/how-the-hr-policy-assistant-works/hr-policy-assistant-local-pg-high-level-design-explainer.json -->

The running parts of an HR policy question-answering assistant (branch dev_local_pg) as one system map: twelve boxes, from the browser through a Gradio chat page, a Google ADK agent, a semantic answer cache and an MCP search tool, to two Postgres databases with pgvector and two Databricks serving endpoints. Every box opens a panel saying what the part is, whether it has been run, and the commands that check it. It is drawn from the code at commit 91b719a; the database, the loader, the embedding endpoint and the PDFs were run and checked on 2026-11-08.

**Also useful in**: a plan or note that needs a small, real retrieval-augmented generation system to point at, with the retrieval and the answer cache as separate parts that both call the same embedding endpoint.

**Caveat**: the search tool, the agent, the cache and the chat endpoint are drawn from the code and not yet run; the 0.70 cache threshold is the code's default, not measured behaviour.

| Where | What it shows | Cards |
|---|---|---|
| [The MCP tool server](https://claude.ai/artifact/Gsj44q2Vehu8RNjgJyWwpb#mcp) | the search tool that embeds the question and returns the three closest policy chunks by cosine distance | [Retrieval-Augmented Generation](../../../Artificial%20Intelligence/Large%20Language%20Models/Retrieval-Augmented%20Generation.md), [Cosine Similarity](../../Linear%20Algebra/Cosine%20Similarity.md) |
| [The semantic cache](https://claude.ai/artifact/Gsj44q2Vehu8RNjgJyWwpb#cache) | a past answer reused when a new question's embedding scores at least 0.70 against a stored one, which skips the agent run | [Cosine Similarity](../../Linear%20Algebra/Cosine%20Similarity.md), [Embedding](../../../Artificial%20Intelligence/Deep%20Learning/Embedding.md) |
| [The embedding endpoint](https://claude.ai/artifact/Gsj44q2Vehu8RNjgJyWwpb#embed) | one endpoint turning chunks and questions into 1024 numbers each, called by the loader, the search tool and the cache | [Embedding](../../../Artificial%20Intelligence/Deep%20Learning/Embedding.md) |
| [The hr_policies database](https://claude.ai/artifact/Gsj44q2Vehu8RNjgJyWwpb#hrpol) | policy chunks stored with their vectors and an HNSW cosine index in Postgres with pgvector | no card yet |
