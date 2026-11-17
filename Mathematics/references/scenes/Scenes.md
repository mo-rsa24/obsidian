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
<!-- home: PhD concept-composition, artifacts/results/how-sdxl-turns-a-prompt-into-an-image -->
<!-- source: /home/molef/PhD/concept-composition/artifacts/results/how-sdxl-turns-a-prompt-into-an-image/sdxl-ldm-high-level-design-explainer.json -->

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
<!-- home: PhD concept-composition, artifacts/results/how-the-sdxl-vae-is-built -->
<!-- source: /home/molef/PhD/concept-composition/artifacts/results/how-the-sdxl-vae-is-built/build_page.py -->

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
<!-- home: PhD concept-composition, artifacts/results/why-the-latent-is-scaled -->
<!-- source: /home/molef/PhD/concept-composition/artifacts/results/why-the-latent-is-scaled/build_page.py -->

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

## Gaussian bowl sketchpad
<!-- scene: https://claude.ai/artifact/2TarMifiFoFyoB23eQFR64 -->

Seven frames that go from one bell in 1D to two cuts through a 2D density, with every number computed live from the formula beside it and the shaded numbers inside a formula draggable (`/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/artifacts/scenes/gaussian-bowl-sketchpad/`, drawn for chapter 2 of that journey's textbook).

| Where | What it shows | Cards |
|---|---|---|
| [One hump, three handles](https://claude.ai/artifact/2TarMifiFoFyoB23eQFR64#bell-1d) | the peak 1/√(2πσ²) with the same σ² under the root and inside the exponent, the root drawn in blue as the normaliser, so making σ² four times bigger halves the peak from 0.3989 to 0.1995 | [Normaliser](../../Statistics/Distributions/Normaliser.md) |
| [The 1D bowl you can widen](https://claude.ai/artifact/2TarMifiFoFyoB23eQFR64#bowl-1d) | the log of the bell split into a blue constant, which is the log of the normaliser, and an orange quadratic bowl; going from σ² = 1 to 4 drops the constant by 0.6931 while the bowl term shrinks from −2 to −0.5 | [Normaliser](../../Statistics/Distributions/Normaliser.md) |
| [The same density as rings](https://claude.ai/artifact/2TarMifiFoFyoB23eQFR64#rings-2d) | the 2D density seen from above as rings, one ring for each whole value of the cost uᵀΣ⁻¹u from 1 outwards, which tilt and stretch as Σ and ρ are dragged | [Contour](../../Calculus/Contour.md) |
| [A surface you can turn](https://claude.ai/artifact/2TarMifiFoFyoB23eQFR64#surface-2d) | the density as a surface with the normaliser included, the determinant of Σ and the normaliser printed live, the rings on the floor as level sets, and the height at the centre dropping by a factor of √2, from 0.0796 to 0.0563, when the determinant doubles | [Contour](../../Calculus/Contour.md), [Normaliser](../../Statistics/Distributions/Normaliser.md), [Determinant](../../Linear%20Algebra/Determinant.md) |

## The height-and-area walk
<!-- scene: https://claude.ai/code/artifact/72caec6e-b6a2-495e-86d3-b6e23c2d29c7 -->

Four frames on a density's height and area, with a predict-before-reveal slot, drawn for sitting 3 and chapter 2 of the diffusion-models foundations journey (`/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/artifacts/scenes/densities-and-the-gaussian/`).

| Where | What it shows | Cards |
|---|---|---|
| [Narrower means taller](https://claude.ai/code/artifact/72caec6e-b6a2-495e-86d3-b6e23c2d29c7) | frame 3: dragging σ in the formula while the peak 1/(σ√2π) passes 1 below σ = 0.3989 and the area stays 1 | [Normaliser](../../Statistics/Distributions/Normaliser.md) |
| [Covariance sets the shape](https://claude.ai/code/artifact/72caec6e-b6a2-495e-86d3-b6e23c2d29c7) | frame 4: contours at 0.6, 0.3 and 0.1 of the peak, ellipses that turn to Σ's eigenvectors and stretch by √(kλ) as the entries of Σ are dragged | [Contour](../../Calculus/Contour.md) |

## The wasted-bits walk
<!-- scene: https://claude.ai/code/artifact/7aff7fa0-ee51-411d-8d97-a7233baa8519 -->

Five frames on what KL divergence and mutual information measure, drawn for sitting 14 and chapter 11 of the diffusion-models foundations journey (`/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/artifacts/scenes/kl-and-mutual-information/`).

| Where | What it shows | Cards |
|---|---|---|
| [The wrong code costs extra](https://claude.ai/code/artifact/7aff7fa0-ee51-411d-8d97-a7233baa8519) | frame 1: the stacked bar H(p) plus the KL waste, with a switch from bits (1.5, 0.25 and 1.75) to nats (1.039721, 0.173287 and 1.213008) | [Nat](../../Statistics/Information%20Theory/Nat.md) |

## The two-bump gradient walk
<!-- scene: https://claude.ai/code/artifact/4bb4eef7-4d8f-4cca-b4ef-0b5259338648 -->

Six frames on the gradient of a two-bump function, with predictions locked before the arrows appear, drawn for sitting 6 of the diffusion-models foundations journey (`/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/artifacts/scenes/the-gradient-field-drawn/`).

| Where | What it shows | Cards |
|---|---|---|
| [Every arrow leaves its line square](https://claude.ai/code/artifact/4bb4eef7-4d8f-4cca-b4ef-0b5259338648) | frame 2: the contour through a draggable dot with its tangent and its gradient, showing the gradient meets the contour line at a right angle | [Contour](../../Calculus/Contour.md) |
| [A log turns slope into ratio](https://claude.ai/code/artifact/4bb4eef7-4d8f-4cca-b4ef-0b5259338648) | frame 5: the standard normal at (3, 4) with a constant multiplier c, which is what a missing normaliser is, dragged from 0.001 to 1e6 while the log-slope stays (−3, −4) | [Normaliser](../../Statistics/Distributions/Normaliser.md) |

## CLIP module tree
<!-- scene: https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ -->
<!-- kind: map -->
<!-- home: learning tree, deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/scenes/clip-module-tree -->
<!-- source: /home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/scenes/clip-module-tree/build_page.py -->

CLIP ViT-B/32 as one system, rung 0 of journey 02's CLIP ladder. The text tower runs along the top (77 tokens, 512 wide, causal mask), the image tower along the bottom (7 × 7 patches of 32 × 32 plus one summary token, 768 wide), and both meet in the 512-number shared space through their projections, the normalisation and logit_scale. Each of the 12 boxes opens onto its real code and its traced shapes. Every shape comes from a CPU forward-hook trace of all 306 modules on the caption "a cat and a dog" and journey 13's cat-and-dog-apart render at seed 42; the batch numbers (the 4 × 4 logits, the loss, the causal-mask comparison) come from the journey's `clip_numbers.json`.

**Also useful in**: journey 12's CLIP score chapter, journey 13's network view where SDXL's two CLIP text encoders appear, and the CLIP rebuild and closing page beside the CLIP paper on the shelf.

**Caveat**: one forward pass on one caption and one render; what happens inside each transformer block is left to the network view and the code walk.

| Where | What it shows | Cards |
|---|---|---|
| [Caption to ids](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#caption-to-ids) | the caption "a cat and a dog" as 7 real tokens and 70 padding, 77 ids | [Tokenization](../../../Artificial%20Intelligence/Large%20Language%20Models/Tokenization.md) |
| [Text embeddings](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#text-embeddings) | each id looked up as a row of the token table, 77 × 512 into the text encoder | [Embedding](../../../Artificial%20Intelligence/Deep%20Learning/Embedding.md) |
| [Text encoder](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#text-encoder) | twelve pre-norm transformer blocks under the causal mask, 8 heads × 64 = 512 | [Transformer](../../../Artificial%20Intelligence/Deep%20Learning/Transformer.md), [Attention](../../../Artificial%20Intelligence/Deep%20Learning/Attention.md), [Softmax](../../../Artificial%20Intelligence/Deep%20Learning/Softmax.md), [Causal Attention Mask](../../../Artificial%20Intelligence/Deep%20Learning/Causal%20Attention%20Mask.md) |
| [Text pool](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#text-pool) | the end-of-text row picked as the caption's vector, token id 49407 at the picked row | [End-of-Text Pooling](../../../Artificial%20Intelligence/Deep%20Learning/End-of-Text%20Pooling.md) |
| [Text projection](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#text-projection) | a linear layer, 512 in and 512 out, into the shared space | [Linear Projection](../../../Artificial%20Intelligence/Deep%20Learning/Linear%20Projection.md) |
| [Image patches](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#image-patches) | a stride-32 convolution cutting the 224-pixel picture into 7 × 7 patches, plus one class token, 50 tokens | [Vision Transformer](../../../Artificial%20Intelligence/Deep%20Learning/Vision%20Transformer.md) |
| [Image encoder](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#image-encoder) | twelve pre-norm transformer blocks with no mask, 12 heads × 64 = 768 | [Vision Transformer](../../../Artificial%20Intelligence/Deep%20Learning/Vision%20Transformer.md), [Transformer](../../../Artificial%20Intelligence/Deep%20Learning/Transformer.md), [Attention](../../../Artificial%20Intelligence/Deep%20Learning/Attention.md) |
| [Image pool](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#image-pool) | token 0 taken, then layer norm, 768 out | [Vision Transformer](../../../Artificial%20Intelligence/Deep%20Learning/Vision%20Transformer.md) |
| [Image projection](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#image-projection) | a linear layer, 768 in and 512 out, into the shared space | [Linear Projection](../../../Artificial%20Intelligence/Deep%20Learning/Linear%20Projection.md) |
| [Normalise](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#normalise) | each vector divided by its length, length 1.0 after for both | [Norm](../../Linear%20Algebra/Norm.md) |
| [Similarity](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#similarity) | the cosine times e to the logit_scale gives the logit | [Cosine Similarity](../../Linear%20Algebra/Cosine%20Similarity.md), [Temperature](../../../Artificial%20Intelligence/Deep%20Learning/Temperature.md), [Logit](../../../Artificial%20Intelligence/Deep%20Learning/Logit.md) |
| [Loss](https://claude.ai/artifact/4mePVaMV9NuxENRkJphieQ#loss) | the symmetric loss on the 4 × 4 batch: image-to-caption and caption-to-image averaged | [Contrastive Image-Text Training](../../../Artificial%20Intelligence/Deep%20Learning/Contrastive%20Image-Text%20Training.md), [Cross-Entropy](../../Statistics/Information%20Theory/Cross-Entropy.md) |

## CLIP code walk
<!-- scene: https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6 -->
<!-- kind: walk -->
<!-- home: learning tree, deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/code-walk/what-each-line-of-clip-computes -->
<!-- source: /home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/code-walk/what-each-line-of-clip-computes/gen_codewalk.py -->

openai/CLIP's `clip/model.py` walked line by line in 24 sections, with the loss the file leaves out taken from the paper's Figure 3 and open_clip's `ClipLoss`; rung 3 of journey 02's CLIP ladder. Each section gives its role, the breakpoint and the shapes to read, the equation with the paper's page, every symbol named, and for 14 of them a figure computed from the rig's own tensors. `rig.py` runs `model.py` unchanged on the original ViT-B/32 weights on journey 13's four renders and four captions, and matches the journey's `clip_numbers.json` at every stored digit.

**Also useful in**: the CLIP rebuild beside the CLIP paper, which follows the walk's 24 sections in order; journey 02's chapter 1 and its by-hand plan, whose instruction 7 finds the places in the real code; journey 12's CLIP score chapter.

**Caveat**: every number is one batch of four renders and four captions on CPU in float32, the loss's slope is with respect to the 16 similarities rather than the weights, and no training was run. Each row below opens the walk at its own section.

| Where | What it shows | Cards |
|---|---|---|
| [Hidden: LayerNorm](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#ln) | layer norm run in float32, before the attention and before the MLP in every block, after the text transformer, and before and after the vision transformer | [Layer Normalization](../../../Artificial%20Intelligence/Deep%20Learning/Layer%20Normalization.md) |
| [Hidden: QuickGELU](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#gelu) | x times sigmoid(1.702 x), the activation inside every block's MLP | [QuickGELU](../../../Artificial%20Intelligence/Deep%20Learning/QuickGELU.md) |
| [Hidden: one block, masked attention then an MLP](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#block) | one residual attention block: layer norm, attention with the mask added to the scores, add back, then the MLP | [Attention](../../../Artificial%20Intelligence/Deep%20Learning/Attention.md), [Softmax](../../../Artificial%20Intelligence/Deep%20Learning/Softmax.md), [Transformer](../../../Artificial%20Intelligence/Deep%20Learning/Transformer.md) |
| [Image path: conv1 cuts the picture into patches](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#patch) | conv1 cutting the picture into 49 patches of 32 × 32 | [Vision Transformer](../../../Artificial%20Intelligence/Deep%20Learning/Vision%20Transformer.md) |
| [Image path: a class row in front, a position row added](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#cls_pos) | the class row put in front of the patches and a position row added to each | [Vision Transformer](../../../Artificial%20Intelligence/Deep%20Learning/Vision%20Transformer.md), [Embedding](../../../Artificial%20Intelligence/Deep%20Learning/Embedding.md) |
| [Output: the class position times W_i](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#image_head) | the class position after layer norm times W_i, the picture's vector | [Linear Projection](../../../Artificial%20Intelligence/Deep%20Learning/Linear%20Projection.md), [Layer Normalization](../../../Artificial%20Intelligence/Deep%20Learning/Layer%20Normalization.md) |
| [Contrastive: the temperature, stored as its log](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#scale_init) | logit_scale stored as the log of 1/τ, e^t = 100 on the trained weights | [Temperature](../../../Artificial%20Intelligence/Deep%20Learning/Temperature.md) |
| [Masked: build_attention_mask](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#mask) | build_attention_mask filling the upper triangle with minus infinity so no word reads ahead | [Causal Attention Mask](../../../Artificial%20Intelligence/Deep%20Learning/Causal%20Attention%20Mask.md) |
| [Text path: each token id becomes its row, plus its position's row](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#embed) | token_embedding plus positional_embedding for each of the 77 slots | [Embedding](../../../Artificial%20Intelligence/Deep%20Learning/Embedding.md), [Tokenization](../../../Artificial%20Intelligence/Large%20Language%20Models/Tokenization.md) |
| [Output: the end-of-text position times W_t](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#text_head) | the end-of-text position, found by text.argmax, after layer norm times W_t, the caption's vector | [End-of-Text Pooling](../../../Artificial%20Intelligence/Deep%20Learning/End-of-Text%20Pooling.md), [Linear Projection](../../../Artificial%20Intelligence/Deep%20Learning/Linear%20Projection.md) |
| [Contrastive: divide each vector by its own length](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#normalise) | each picture and caption vector divided by its own length | [Norm](../../Linear%20Algebra/Norm.md) |
| [Contrastive: every picture against every caption, times e^t](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#logits) | every unit picture vector against every unit caption vector, times e^t = 100, the 4 × 4 logits | [Cosine Similarity](../../Linear%20Algebra/Cosine%20Similarity.md), [Dot Product](../../Linear%20Algebra/Dot%20Product.md), [Logit](../../../Artificial%20Intelligence/Deep%20Learning/Logit.md) |
| [Contrastive: the right answer for row i is column i](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#labels) | the labels 0 to N − 1, each picture's right caption on the diagonal | [Contrastive Image-Text Training](../../../Artificial%20Intelligence/Deep%20Learning/Contrastive%20Image-Text%20Training.md) |
| [Contrastive: the symmetric cross-entropy](https://claude.ai/artifact/4yYMLJMJZUdLM2vKzrjMn6#loss) | open_clip's ClipLoss: cross-entropy over captions and over pictures, averaged, 0.1698 on the rig | [Cross-Entropy](../../Statistics/Information%20Theory/Cross-Entropy.md), [Loss Function](../../../Artificial%20Intelligence/Machine%20Learning/Loss%20Function.md), [Contrastive Image-Text Training](../../../Artificial%20Intelligence/Deep%20Learning/Contrastive%20Image-Text%20Training.md) |
