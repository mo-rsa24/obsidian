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

## SDXL pipeline map
<!-- scene: https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf -->
<!-- kind: map -->
<!-- home: learning tree, deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/scenes/sdxl-pipeline -->
<!-- source: /home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/scenes/sdxl-pipeline/build_page.py -->

SDXL's text-to-image loop as one system, rung 0 of journey 02's Stable Diffusion ladder, with the U-Net opened into its down, middle and up blocks. The caption is read once by two text encoders and joined into the word vectors C; the step number and six size numbers become the time vector; the U-Net runs twice each step (empty caption, then caption), guidance combines the two predictions, an Euler step moves the latent, and after 50 steps the VAE decoder makes the picture. Each of the 21 boxes opens onto its network-view figure, its traced shapes and its real lines of diffusers v0.43.0. Every shape comes from one CPU trace of the pipeline's own `__call__` on "a cat and a dog", one step from t = 481 to 461.

**Also useful in**: journey 00's plans 10, 11 and 14, which draw the same pipeline left to right, its size numbers and its capstone; journey 13's network view, whose figures several boxes open; the Stable Diffusion rebuild and closing page on the paper shelf.

**Caveat**: one step of one caption on one starting latent, on CPU; the inside of a ResBlock, a transformer block and the decoder are left to the network view, the code walk and Inside the SDXL VAE.

| Where | What it shows | Cards |
|---|---|---|
| [The whole system](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#overview) | the pipeline in five lanes: text, time, U-Net, the step, pixels | [Diffusion Models](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Diffusion%20Models.md) |
| [Caption to ids](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#caption-to-ids) | "a cat and a dog" cut into 77 token ids by each tokenizer | [Tokenization](../../../Artificial%20Intelligence/Large%20Language%20Models/Tokenization.md) |
| [Text encoder 1](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#text-encoder-1) | CLIP ViT-L's text tower, its second-to-last layer kept | [Transformer](../../../Artificial%20Intelligence/Deep%20Learning/Transformer.md), [Contrastive Image-Text Training](../../../Artificial%20Intelligence/Deep%20Learning/Contrastive%20Image-Text%20Training.md) |
| [Text encoder 2](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#text-encoder-2) | OpenCLIP bigG's text tower, its second-to-last layer kept and its end-token vector projected into the pooled vector p | [Transformer](../../../Artificial%20Intelligence/Deep%20Learning/Transformer.md), [End-of-Text Pooling](../../../Artificial%20Intelligence/Deep%20Learning/End-of-Text%20Pooling.md) |
| [Word vectors](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#word-vectors) | the two encoders' rows joined end to end, C = 77 × 2048 | [Embedding](../../../Artificial%20Intelligence/Deep%20Learning/Embedding.md) |
| [Size numbers](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#size-ids) | the six size and crop numbers, 1280 + 6 × 256 = 2816 | no card yet |
| [Add embedding](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#add-embedding) | p and the size numbers' waves mapped to 1280 and added to the time vector | [Multilayer Perceptron](../../../Artificial%20Intelligence/Deep%20Learning/Multilayer%20Perceptron.md) |
| [Time embedding](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#time-embedding) | the step number as cosine and sine waves, then two linear layers with SiLU to the 1280 time vector | [Multilayer Perceptron](../../../Artificial%20Intelligence/Deep%20Learning/Multilayer%20Perceptron.md) |
| [Latent](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#latent) | the U-Net's input x_t, and the Euler sampler's scaled latent x̃_t = √(σ² + 1) x_t | [The Forward Process](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/The%20Forward%20Process.md) |
| [conv_in](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#conv-in) | a 3 × 3 convolution lifting 4 channels to 320 | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [Down block 0](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#down-0) | ResBlocks only: group norm, convolution, the time vector added, the skip | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [Down block 1](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#down-1) | ResBlocks paired with transformer blocks whose cross-attention reads C, softmax(QKᵀ/√64)V, at 64 × 64 | [Cross-Attention](../../../Artificial%20Intelligence/Deep%20Learning/Cross-Attention.md), [Attention](../../../Artificial%20Intelligence/Deep%20Learning/Attention.md), [Softmax](../../../Artificial%20Intelligence/Deep%20Learning/Softmax.md) |
| [Down block 2](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#down-2) | the same pairing at 32 × 32, ten transformer blocks deep | [Cross-Attention](../../../Artificial%20Intelligence/Deep%20Learning/Cross-Attention.md), [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [Middle block](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#mid) | ResBlock, a ten-deep attention stack, ResBlock, at 32 × 32 with 1280 channels | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md), [Cross-Attention](../../../Artificial%20Intelligence/Deep%20Learning/Cross-Attention.md) |
| [Up block 0](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#up-0) | each ResBlock joining a saved skip; one patch's self-attention against its cross-attention | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md), [Cross-Attention](../../../Artificial%20Intelligence/Deep%20Learning/Cross-Attention.md) |
| [Up block 1](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#up-1) | where "cat" and "dog" land in the cross-attention maps | [Cross-Attention](../../../Artificial%20Intelligence/Deep%20Learning/Cross-Attention.md) |
| [Up block 2](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#up-2) | the last up block's ResBlocks, back at 128 × 128 | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [conv_out](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#conv-out) | group norm, SiLU and conv_out to the noise prediction ε_θ, 4 × 128 × 128 | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [Guidance](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#guidance) | ε̂ = ε_uncond + γ(ε_c − ε_uncond), the two runs combined | [Classifier-Free Guidance](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Classifier-Free%20Guidance.md) |
| [Scheduler](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#scheduler) | the clean guess x̂₀ = x̃ − σε̂, then one Euler step toward it | [DDIM](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/DDIM.md), [Ordinary Differential Equation](../../Calculus/Differential%20Equations/Ordinary%20Differential%20Equation.md) |
| [VAE decoder](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#vae-decoder) | the clean guess divided by 0.13025 and decoded to the picture | [Variational Autoencoders](../../../Artificial%20Intelligence/Generative%20Modeling/Variational%20Autoencoders/Variational%20Autoencoders.md) |
| [Training](https://claude.ai/artifact/96WQEXeRKy357BEFe8iYEf#training) | x_t = √ᾱ x₀ + √(1 − ᾱ) ε and the loss ‖ε − ε_θ‖² | [The Forward Process](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/The%20Forward%20Process.md), [Mean Squared Error](../../../Artificial%20Intelligence/Machine%20Learning/Mean%20Squared%20Error.md), [Loss Function](../../../Artificial%20Intelligence/Machine%20Learning/Loss%20Function.md) |

## SDXL code walk
<!-- scene: https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i -->
<!-- kind: walk -->
<!-- home: learning tree, deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/code-walk/what-each-line-of-sdxl-computes -->
<!-- source: /home/molef/goal-setting/learning/deep-learning/generative-models/02-stable-diffusion-and-clip/artifacts/code-walk/what-each-line-of-sdxl-computes/gen_codewalk.py -->

SDXL base 1.0's text-to-image loop walked line by line through diffusers v0.43.0 for one denoising step, rung 3 of journey 02's Stable Diffusion ladder: the pipeline's `__call__`, `UNet2DConditionModel.forward`, one `ResnetBlock2D`, one `BasicTransformerBlock` with its attention, and `EulerDiscreteScheduler.step`, in 32 sections over nine files. Each section gives its role, the breakpoint and the shapes to read, the equation with its paper and page, every symbol named, and for 8 of them a figure computed from the rig's own tensors. `rig.py` runs the pipeline from the clone on CPU on "a cat and a dog" at t = 481 and agrees with the network view's numbers on 47 of 47 checks.

**Also useful in**: journey 00's plans 03, 10 and 11 (the time features, one generation in the debugger, the size numbers); the Stable Diffusion rebuild beside the paper shelf, which takes each equation the walk uses down to the fundamentals; journey 13's sampler, whose DDIM step lands on the same latent as SDXL's Euler step.

**Caveat**: every number is one step (t = 481) of one caption on one starting latent, on CPU with float16 weights lifted to float32; only 8 of the 32 sections carry a term figure, and training was not run. Each row below opens the walk at its own section.

| Where | What it shows | Cards |
|---|---|---|
| [Input: two tokenizers cut the caption into 77 ids each](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#tokenize) | both tokenizers cut "a cat and a dog" into the same 7 pieces and pad to 77, the second with "!" | [Tokenization](../../../Artificial%20Intelligence/Large%20Language%20Models/Tokenization.md) |
| [Hidden: each encoder's second-to-last layer, and the second's pooled vector](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#encoders) | hidden_states[-2] kept from each encoder, and the second encoder's projected end-token vector as p | [Transformer](../../../Artificial%20Intelligence/Deep%20Learning/Transformer.md), [End-of-Text Pooling](../../../Artificial%20Intelligence/Deep%20Learning/End-of-Text%20Pooling.md) |
| [The caption acts: the empty caption is all zeros](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#zeros) | force_zeros_for_empty_prompt: the empty run reads zeros for C and p, not the encoded empty string | [Classifier-Free Guidance](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Classifier-Free%20Guidance.md) |
| [Input: x_t scaled up for the Euler sampler](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#latents) | x_t multiplied by init_noise_sigma, √(σ² + 1) = 1.8188, into Euler's state x̃ | no card yet |
| [Input: the six size numbers](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#add_time_ids) | original size, crop corner and target size, (1024, 1024, 0, 0, 1024, 1024) | no card yet |
| [The caption acts: the empty run and the captioned run stacked as a batch of two](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#batch_of_two) | one U-Net call computes both predictions, empty caption first | [Classifier-Free Guidance](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Classifier-Free%20Guidance.md) |
| [Sampler: the loop doubles x̃ and scales it back to x_t](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#loop_in) | the latent stacked once per caption row and divided by √(σ² + 1), so the U-Net reads x_t | no card yet |
| [Hidden: one U-Net call gives both predictions](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#unet_call) | x_t twice, t, C and the conditioning in; noise_pred (2, 4, 128, 128) out | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [Guidance: the two predictions combined, the caption's difference times γ](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#guidance) | the two runs 0.89 degrees apart, their difference 3.83 multiplied by γ = 5 | [Classifier-Free Guidance](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Classifier-Free%20Guidance.md) |
| [Output: unscale the latent and decode it](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#decode_call) | the latent divided by the scaling factor 0.13025, then the VAE once | [Variational Autoencoders](../../../Artificial%20Intelligence/Generative%20Modeling/Variational%20Autoencoders/Variational%20Autoencoders.md) |
| [Hidden: t made a tensor, spread over the batch, turned into waves](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#get_time_embed) | t = 481 expanded to the batch and turned into 320 wave features | no card yet |
| [The caption acts: p and the size numbers become a second time vector](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#aug_embed) | six size numbers as 256 waves each, joined to p into 2816 and mapped to 1280 | [Multilayer Perceptron](../../../Artificial%20Intelligence/Deep%20Learning/Multilayer%20Perceptron.md) |
| [Hidden: the time vector e_t is the two added](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#emb_sum) | the 320 waves mapped to 1280 plus the caption-and-size vector, read by all 17 ResBlocks | [Multilayer Perceptron](../../../Artificial%20Intelligence/Deep%20Learning/Multilayer%20Perceptron.md) |
| [Hidden: conv_in lifts 4 channels to 320](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#conv_in) | a 3 × 3 convolution, (2, 320, 128, 128) out | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [Hidden: three down blocks, each output saved for a skip](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#down) | down 0 ResBlocks only, down 1 and 2 with attention stacks reading C, every output kept for the up path | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [Hidden: the middle block](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#mid) | ResBlock, a ten-deep attention stack, ResBlock, at 32 × 32 with 1280 channels | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md), [Cross-Attention](../../../Artificial%20Intelligence/Deep%20Learning/Cross-Attention.md) |
| [Hidden: three up blocks, each joining the saved skips](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#up) | each up block joining a saved output to each ResBlock's input along the channels | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [Output: group norm, SiLU, conv_out to 4 channels](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#conv_out) | the prediction in the latent's own shape, ε_uncond and ε_c of lengths 246.02 and 246.15 | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [Hidden: the step number as 160 cosines and 160 sines](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#sines) | cos(t ω_k) then sin(t ω_k) with ω_k = 10000^(−k/160), frequencies over 160, not 159 | no card yet |
| [Hidden: two linear layers with SiLU between](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#timestep_mlp) | the one TimestepEmbedding class used for time_embedding (320 → 1280) and add_embedding (2816 → 1280) | [Multilayer Perceptron](../../../Artificial%20Intelligence/Deep%20Learning/Multilayer%20Perceptron.md) |
| [Hidden: one ResBlock, group norm, conv, + e_t, group norm, conv, skip](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#resblock) | one ResBlock at 64 × 64, 320 channels in and 640 out, group norm over 32 groups of 10 channels | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [Hidden: a down block pairs each ResBlock with an attention stack](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#crossattn_down) | a ResBlock then a transformer stack reading C, twice, then a stride-2 convolution | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md), [Cross-Attention](../../../Artificial%20Intelligence/Deep%20Learning/Cross-Attention.md) |
| [Hidden: an up block joins a skip before every ResBlock](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#crossattn_up) | the saved feature map joined along the channels, 2560 channels into up block 0's first ResBlock | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [Hidden: one transformer block, self-attention, cross-attention, feed-forward](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#transformer_block) | 4096 positions of 640, each part reading a layer-normed copy and adding its answer back | [Transformer](../../../Artificial%20Intelligence/Deep%20Learning/Transformer.md), [Attention](../../../Artificial%20Intelligence/Deep%20Learning/Attention.md), [Cross-Attention](../../../Artificial%20Intelligence/Deep%20Learning/Cross-Attention.md), [Layer Normalization](../../../Artificial%20Intelligence/Deep%20Learning/Layer%20Normalization.md) |
| [The caption acts: one patch's weights over the 77 words](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#scores) | Q times Kᵀ times 1/√64, softmax per row; at the cat's head "cat" 0.1614 and "dog" 0.1586 | [Attention](../../../Artificial%20Intelligence/Deep%20Learning/Attention.md), [Softmax](../../../Artificial%20Intelligence/Deep%20Learning/Softmax.md) |
| [The caption acts: queries from the picture, keys and values from the words](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#attn_processor) | keys and values with 77 rows from C in cross-attention, 20 heads of 64 | [Cross-Attention](../../../Artificial%20Intelligence/Deep%20Learning/Cross-Attention.md), [Attention](../../../Artificial%20Intelligence/Deep%20Learning/Attention.md) |
| [Sampler: init_noise_sigma, how big Euler's starting latent is](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#init_sigma) | √(σ_max² + 1): 13.1585 for the full 50 steps | no card yet |
| [Sampler: scale_model_input divides back to x_t](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#scale_input) | Euler's x̃ divided by √(σ² + 1) before every U-Net call | no card yet |
| [Sampler: 50 timesteps, leading spacing, and a noise level for each](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#set_timesteps) | 981 … 1 in steps of 20, each with σ = √((1 − ᾱ)/ᾱ) | no card yet |
| [Sampler: the clean guess, then one Euler step along the line to it](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#euler_step) | no noise added, the clean guess, the slope of the line to it and the step σ′ − σ = −0.0971 | [DDIM](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/DDIM.md), [Ordinary Differential Equation](../../Calculus/Differential%20Equations/Ordinary%20Differential%20Equation.md) |
| [Output: post_quant_conv, then the decoder](https://claude.ai/artifact/HAq4Qwm2HwHcF3E8Ad325i#vae_decode) | a 1 × 1 convolution, then three doublings of the side, 128 → 1024 | [Variational Autoencoders](../../../Artificial%20Intelligence/Generative%20Modeling/Variational%20Autoencoders/Variational%20Autoencoders.md) |

## Readout Guidance loop walk
<!-- scene: https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H -->
<!-- kind: walk -->
<!-- home: PhD concept-composition, 2-classifier-guidance/artifacts/results/what-each-line-of-readout-guidance-computes -->
<!-- source: /home/molef/PhD/concept-composition/2-classifier-guidance/artifacts/results/what-each-line-of-readout-guidance-computes/gen_codewalk.py -->

The code Luo et al. released with Readout Guidance (google-research/readout_guidance at `a8a699c`) walked line by line, level 3 of journey 13's Readout Guidance ladder. The top row trains the SDXL pose head: a picture noised forward to one random step, one frozen U-Net step on the empty prompt, nine decoder resnets caught and resized to 128 px, nine bottlenecks with the time vector added, mixed by learnt shares, a 3-channel readout, and the sparse MSE against an OpenPose label. The bottom row is one guided step: the U-Net on the CFG batch of four, the same taps and head, the distance to the pose, one fresh AdamW step on the latent, then the ordinary DDIM step. `rg_rig.py` runs the authors' functions unchanged on CPU with the released SDXL pose head at the pose config's first guided step (seed 100, t = 991), and the term figures come from its tensors.

**Also useful in**: journey 13's chapter 6 and plan 11, which work the same head and push by hand; the Readout Guidance rebuild and closing page beside the shelved PDF; journey 14, whose noise-aware classifier also takes the step as an input.

**Caveat**: the backward pass through SDXL does not fit on the laptop, so the real push gradient's size is not shown, and the training code is read, not run. Each row below opens the walk at its own section.

| Where | What it shows | Cards |
|---|---|---|
| [The head: each decoder resnet keeps its hidden state](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#rn_hidden) | each tapped resnet keeps hidden_states after conv2 and before the skip is added back | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [The head: which layers are tapped, the up-block resnets only](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#rn_collect) | the nine up-block resnets of SDXL, 1280, 640 and 320 channels; the mid and down blocks never read | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [The head: resizing one layer to the latent's 128 × 128](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#h_resize) | one layer resized by bilinear interpolation to the latent's grid, channels last | no card yet |
| [The head: all nine layers resized and stacked into one tensor](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#h_collect) | the stack [4, 128, 128, 6720], 1680 MB in float32 | no card yet |
| [Ordinary sampler: the DDIM step, stochastic at η = 1](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#h_ddim) | the clean guess, then the step to the next timestep with fresh noise at η = 1 | [DDIM](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/DDIM.md) |
| [The head's time input: the U-Net's own time vector](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#h_time) | the U-Net's sinusoid and two-layer embedding giving the head a 1280-number time vector, from different step numbers in training and at guidance | [Multilayer Perceptron](../../../Artificial%20Intelligence/Deep%20Learning/Multilayer%20Perceptron.md) |
| [The head: one bottleneck's layers, with its time projection](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#a_block_init) | 1 × 1 down to 96 channels, 3 × 3, 1 × 1 up to 384, and a linear map from the time vector to the 96 inner channels | [Linear Projection](../../../Artificial%20Intelligence/Deep%20Learning/Linear%20Projection.md) |
| [The head: one bottleneck run, the time vector added in the middle](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#a_block_fwd) | the projected time vector added to every pixel between the bottleneck's convolutions | no card yet |
| [The head: split the stack, run each bottleneck, mix, read out](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#a_forward) | nine learnt weights turned into shares summing to 1, each layer's bottleneck output scaled and summed, read out inside ±1 | [Softmax](../../../Artificial%20Intelligence/Deep%20Learning/Softmax.md) |
| [Training the head: a clean picture noised forward to one random step](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#de_forward) | one generation step drawn uniformly and the latent noised forward to it, the same step for the whole batch | [The Forward Process](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/The%20Forward%20Process.md) |
| [Frozen model: the U-Net run for exactly one step](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#df_steps) | the frozen U-Net run for one step on the empty prompt to give the features | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [Training the head: pose and edges switch the sparse loss on](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#ds_sparse) | black background mapped to −0.5: 82.9% of the pose sample's elements | no card yet |
| [Training the head: MSE with null and drawn pixels weighted equally](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#ts_loss) | squared errors averaged separately over background and drawn pixels, then the two averages averaged | [Mean Squared Error](../../../Artificial%20Intelligence/Machine%20Learning/Mean%20Squared%20Error.md), [Loss Function](../../../Artificial%20Intelligence/Machine%20Learning/Loss%20Function.md) |
| [Training the head: 8-bit AdamW on the mixing weights, bottlenecks and output head](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#th_opt) | three parameter groups at learning rate 1e-3, weight decay 0 | [Gradient Descent](../../../Artificial%20Intelligence/Machine%20Learning/Gradient%20Descent.md), [Learning Rate](../../../Artificial%20Intelligence/Machine%20Learning/Learning%20Rate.md) |
| [Training the head: features read with no gradient, the head run with one](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#th_hyper) | the U-Net under inference mode, so the gradient reaches the head only | [Backpropagation](../../../Artificial%20Intelligence/Deep%20Learning/Backpropagation.md) |
| [The push: loss_rescale, the paper's rg weight 0.5](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#o_rescale) | the loss times 0.5, which a fresh AdamW step mostly divides away | no card yet |
| [The push: the distance between the readout and the pose](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#o_spatial) | readout and pose mapped into the latent's own range and compared by plain per-element MSE | [Mean Squared Error](../../../Artificial%20Intelligence/Machine%20Learning/Mean%20Squared%20Error.md) |
| [The push: the loss on one half of the batch](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#o_guidance) | 0.3551 on the unconditional half and 0.3830 on the conditional half; the gradient reaches rows 1 and 3 only | [Loss Function](../../../Artificial%20Intelligence/Machine%20Learning/Loss%20Function.md), [Gradient](../../Calculus/Gradient.md) |
| [Ordinary sampler: one U-Net call on the CFG batch, and the features](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#p_unet) | the batch doubled to four, classifier-free guidance at γ = 7.5, the taps read | [Classifier-Free Guidance](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Classifier-Free%20Guidance.md) |
| [The method: one fresh AdamW step on the latent itself](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#p_push) | a new optimizer on every guided step with learning rate 0.02, one step moving the latent | [Gradient Descent](../../../Artificial%20Intelligence/Machine%20Learning/Gradient%20Descent.md), [Learning Rate](../../../Artificial%20Intelligence/Machine%20Learning/Learning%20Rate.md), [Gradient](../../Calculus/Gradient.md) |
| [Ordinary sampler: the normal step after the push](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#p_step) | the U-Net run again on the moved latent and the DDIM step taken, two forwards and one backward per guided step | [DDIM](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/DDIM.md) |
| [The push: which steps it runs on](https://claude.ai/artifact/SHnMMo46yDvhj2GaXuEs7H#p_window) | rg_ratio [0.0, 0.5] of 100 steps: pushed on t = 991 to 501 and none after | no card yet |

## Count head walk
<!-- scene: https://claude.ai/artifact/2VgqMaBHqrXNoHdTWjxro1 -->
<!-- kind: walk -->
<!-- home: PhD concept-composition, 2-classifier-guidance/artifacts/results/what-each-line-of-readout-guidance-computes -->
<!-- source: /home/molef/PhD/concept-composition/2-classifier-guidance/artifacts/results/what-each-line-of-readout-guidance-computes/gen_codewalk.py -->

The concept-composition count head script, `scripts/rung2/train_count_head.py` at `c5e61cec`, walked line by line in 11 sections beside the Readout Guidance loop walk: the three hooks, pooling to 32 px, the density head, the blob target, the training batch from plan 23's states, the loss, and the held-out check with its bar. Every place it departs from the released code is named by the read map's caveats R1 to R10. The rig compiles lines 1 to 91 of the committed file and runs its readout and head on SDXL's real features.

**Also useful in**: journey 13's chapter 6 and plan 11, whose miniature is a count head on two decoder layers; the Readout Guidance rebuild's sections 11 and 12 on the count head; the classifier-guided PoE route, which this head serves.

**Caveat**: there is no push in the script, and the page says nothing about the head's trained behaviour: no training run or `check.json` existed when it was built. Each row below opens the walk at its own section.

| Where | What it shows | Cards |
|---|---|---|
| [Ours: three whole blocks read through forward hooks](https://claude.ai/artifact/2VgqMaBHqrXNoHdTWjxro1#c_readout) | hooks on the mid block and up blocks 0 and 1 keeping each block's output | [U-Net](../../../Artificial%20Intelligence/Deep%20Learning/U-Net.md) |
| [Ours: pool each block to 32 × 32, project, sum, and read out a density](https://claude.ai/artifact/2VgqMaBHqrXNoHdTWjxro1#c_head) | each block pooled to 32 × 32 and projected to 128 channels, the three summed, one positive channel out | [Linear Projection](../../../Artificial%20Intelligence/Deep%20Learning/Linear%20Projection.md) |
| [Ours: one Gaussian blob per detector box, each summing to 1](https://claude.ai/artifact/2VgqMaBHqrXNoHdTWjxro1#c_target) | one blob per box, each divided by its own total, so the map sums to the number of boxes | [Multivariate Normal Distribution](../../Statistics/Distributions/Multivariate%20Normal%20Distribution/Multivariate%20Normal%20Distribution.md) |
| [Ours: noise each tile forward, read its count, score balanced accuracy](https://claude.ai/artifact/2VgqMaBHqrXNoHdTWjxro1#c_check) | each held-out tile noised forward four times, its counts averaged, plural at 1.5 or more | [The Forward Process](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/The%20Forward%20Process.md), [Accuracy](../../../Artificial%20Intelligence/Machine%20Learning/Accuracy.md) |
| [Ours: a training batch from the product's own trajectory](https://claude.ai/artifact/2VgqMaBHqrXNoHdTWjxro1#c_batch) | eight drawings, one saved state of each paired with its finished drawing's target | no card yet |
| [Ours: the loss, the map term and the count term](https://claude.ai/artifact/2VgqMaBHqrXNoHdTWjxro1#c_loss) | the map's MSE times 1000 plus 0.1 times the squared error of the total, one AdamW step | [Mean Squared Error](../../../Artificial%20Intelligence/Machine%20Learning/Mean%20Squared%20Error.md), [Loss Function](../../../Artificial%20Intelligence/Machine%20Learning/Loss%20Function.md) |

## CO3 Corrector Round
<!-- scene: https://claude.ai/artifact/9hHS8hf9vtTWHikPVcm52x -->
<!-- kind: walk -->
<!-- home: PhD concept-composition, artifacts/scenes/how-co3-corrects-a-step -->
<!-- source: /home/molef/PhD/concept-composition/artifacts/scenes/how-co3-corrects-a-step/index.html -->

One round of the CO3 corrector on SDXL, taken apart one symbol per press on an invented two-entry latent. The reader follows four noise predictions into three Tweedie estimates, sets the concept weights from each concept's distance to the joint prediction, and sees the weighted sum land at the concept centre mirrored through the joint estimate. The page then marks where the released code at commit 35ea972 departs from Algorithm 3. Every number comes from the released `co3_corrector`, run on CPU with a stub U-Net.

**Also useful in**: the `sampler-correctors-for-composition` journey, and the CO3 reproduction under `artifacts/notes/progress/reproductions/CO3/` in concept-composition.

**Caveat**: the vectors are invented and no SDXL model ran, so the gap between the two rescales here says nothing about its size on a real latent. The page takes no side on the guidance setting, which is the owner's open board question 16.

| Where | What it shows | Cards |
|---|---|---|
| [Three estimates](https://claude.ai/artifact/9hHS8hf9vtTWHikPVcm52x#estimates) | guidance moving each noise prediction along a line, and the Tweedie estimate as √ᾱ times the clean-latent guess | [Classifier-Free Guidance](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Classifier-Free%20Guidance.md), [DDIM](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/DDIM.md) |
| [Weights](https://claude.ai/artifact/9hHS8hf9vtTWHikPVcm52x#weights) | distance to the joint prediction turned into negative concept weights through exp(−β d), with β as a slider | none yet: exponential-kernel weights |
| [The sum](https://claude.ai/artifact/9hHS8hf9vtTWHikPVcm52x#sum) | a weighted sum with weights adding to 1, drawn as the concept centre mirrored through the joint estimate | none yet: Tweedie's formula, affine combination |
| [Back to noise](https://claude.ai/artifact/9hHS8hf9vtTWHikPVcm52x#rescale) | rescaling by a ratio of L2 norms against a ratio of largest entries, then matching the length of x on a circle | [Norm](../../Linear%20Algebra/Norm.md) |
| [Paper and script](https://claude.ai/artifact/9hHS8hf9vtTWHikPVcm52x#disagree) | guidance 5.0 in section 4.1, 0.8 and 0.9 in appendix A.8, and CFG++ at 0.8 in the released script | [Classifier-Free Guidance](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Classifier-Free%20Guidance.md) |

## The Line Toy
<!-- scene: https://claude.ai/artifact/MsbtS4cNQaMSSyEQs3X7mv -->
<!-- kind: scene -->
<!-- home: learning journey deep-learning/diffusion-models/13-classifier-guidance-by-hand, textbook/scenes/line-toy -->
<!-- source: /home/molef/goal-setting/learning/deep-learning/diffusion-models/13-classifier-guidance-by-hand/textbook/scenes/line-toy/index.html -->

Plays the noising of a one-dimensional cat and dog toy, then applies classifier guidance to its noise prediction at three strengths. It is built from the journey's toy answer key, and its curves are recomputed in the browser.

**Also useful in**: plans 00, 01 and 02 of the classifier guidance journey.

**Caveat**: it shows one noise level and does not simulate the reverse sampler.

| Where | What it shows | Cards |
|---|---|---|
| [Noise the line toy](https://claude.ai/artifact/MsbtS4cNQaMSSyEQs3X7mv#noising) | the centres move inward, the signal narrows, and independent noise restores variance 1 | [Score Function](../../../Artificial%20Intelligence/Generative%20Modeling/Score%20Function.md) |
| [Change guidance](https://claude.ai/artifact/MsbtS4cNQaMSSyEQs3X7mv#guidance) | the guided noise prediction at strengths 0, 1 and 3 on the unconditional base, against the cat-only line | [Score Function](../../../Artificial%20Intelligence/Generative%20Modeling/Score%20Function.md), [Classifier](../../../Artificial%20Intelligence/Machine%20Learning/Classifier.md) |
| [Leave out the noise level](https://claude.ai/artifact/MsbtS4cNQaMSSyEQs3X7mv#no-sigma) | the correction keeps its direction but is too long when the noise-level factor is missing | [Score Function](../../../Artificial%20Intelligence/Generative%20Modeling/Score%20Function.md) |

## Learned Log-Odds Line
<!-- scene: https://claude.ai/artifact/TBhyvLikicJutLVhURJxZH -->
<!-- kind: scene -->
<!-- home: learning journey deep-learning/diffusion-models/13-classifier-guidance-by-hand, textbook/scenes/discriminator-training -->
<!-- source: /home/molef/goal-setting/learning/deep-learning/diffusion-models/13-classifier-guidance-by-hand/textbook/scenes/discriminator-training/index.html -->

Steps through recorded checkpoints of a logistic discriminator as its log-odds line approaches the exact target of slope 1.6. It is built from the recorded trajectory in the journey's toy answer key.

**Also useful in**: plan 06 and chapter 3 of the classifier guidance journey.

**Caveat**: it shows stored checkpoints only, with no samples or individual gradient calculations.

| Where | What it shows | Cards |
|---|---|---|
| [Training checkpoints](https://claude.ai/artifact/TBhyvLikicJutLVhURJxZH) | the learned slope rising from 0 toward the exact target as training proceeds | [Logit](../../../Artificial%20Intelligence/Deep%20Learning/Logit.md), [Classifier](../../../Artificial%20Intelligence/Machine%20Learning/Classifier.md) |

## The Dropped Term
<!-- scene: https://claude.ai/artifact/QHSBgCTcrRVxhWa42j4ywq -->
<!-- kind: scene -->
<!-- home: learning journey deep-learning/diffusion-models/13-classifier-guidance-by-hand, textbook/scenes/dropped-term -->
<!-- source: /home/molef/goal-setting/learning/deep-learning/diffusion-models/13-classifier-guidance-by-hand/textbook/scenes/dropped-term/index.html -->

Changes one choice at a time on a four-picture toy to show what a discriminator push repairs on a product of two classifiers. Shares are recomputed in the browser from hand-set probabilities.

**Also useful in**: plans 04 and 08 and chapter 4 of the classifier guidance journey.

**Caveat**: it uses hand-set probabilities and shows no diffusion trajectory or measured image scores.

| Where | What it shows | Cards |
|---|---|---|
| [How much push?](https://claude.ai/artifact/QHSBgCTcrRVxhWa42j4ywq#weight) | the four picture shares against the joint-caption target as the discriminator weight changes | [Product Of Experts](../../../Artificial%20Intelligence/Generative%20Modeling/Product%20Of%20Experts.md), [Classifier](../../../Artificial%20Intelligence/Machine%20Learning/Classifier.md) |
| [Which negatives?](https://claude.ai/artifact/QHSBgCTcrRVxhWa42j4ywq#negatives) | raw-prior negatives leave an extra product preference, while product negatives recover the target | [Classifier](../../../Artificial%20Intelligence/Machine%20Learning/Classifier.md) |
| [What was dropped?](https://claude.ai/artifact/QHSBgCTcrRVxhWa42j4ywq#dropped) | the dropped log term on the fused animal, and how it vanishes when the scores agree | [Product Of Experts](../../../Artificial%20Intelligence/Generative%20Modeling/Product%20Of%20Experts.md) |

## Four-Picture Product
<!-- scene: https://claude.ai/artifact/P91CWE6nz9F9RTp3MnWY3P -->
<!-- kind: scene -->
<!-- home: learning journey deep-learning/diffusion-models/13-classifier-guidance-by-hand, textbook/scenes/product-as-two-classifiers -->
<!-- source: /home/molef/goal-setting/learning/deep-learning/diffusion-models/13-classifier-guidance-by-hand/textbook/scenes/product-as-two-classifiers/index.html -->

Shows how a product of two classifiers shares weight across four pictures, and why a stronger push cannot put the pair first. Shares are recomputed in the browser from the chapter's hand-set toy.

**Also useful in**: chapter 2 of the classifier guidance journey.

**Caveat**: these are toy numbers, with no trained classifier or measured images.

| Where | What it shows | Cards |
|---|---|---|
| [Push harder](https://claude.ai/artifact/P91CWE6nz9F9RTp3MnWY3P#strength) | the fused animal stays first at every strength on the product base | [Product Of Experts](../../../Artificial%20Intelligence/Generative%20Modeling/Product%20Of%20Experts.md), [Classifier](../../../Artificial%20Intelligence/Machine%20Learning/Classifier.md) |
| [Raise the pair's scores](https://claude.ai/artifact/P91CWE6nz9F9RTp3MnWY3P#scores) | the pair and the fused animal tie once their classifier scores match | [Product Of Experts](../../../Artificial%20Intelligence/Generative%20Modeling/Product%20Of%20Experts.md) |

## The Commitment Time
<!-- scene: https://claude.ai/artifact/KMf73EpZmTtaFBp268sbMh -->
<!-- kind: walk -->
<!-- home: learning deep-learning/diffusion-models/05-poe-composition-diffusion, plans 46 and 47 -->
<!-- source: /home/molef/PhD/concept-composition/artifacts/scenes/the-commitment-time/index.html -->

The formula T_s = ½ ln λ_max taken apart one piece per press on a 2D toy: two equal Gaussian classes at +m and −m with variance 1 and |m|² = 19, so λ_max = 20 and T_s ≈ 1.498. The reader turns a line to find the widest spread, watches the forward process shrink it, solves the crossing one algebra move at a time, and copies a backward trajectory at different times as Biroli's cloning test does. The agreement curve is simulated from 40,000 cloned pairs per time and drawn beside Biroli's Equation 6.

**Also useful in**: the `06-diffusion-speciation-dynamics` journey, whose speciation plan 07 derives the same closed form.

**Caveat**: the 2D toy shows the mechanism and its agreement curve is gradual (76.7% at T_s). The sharp transition needs high dimension. The same-mean frame states only Achilli's ¼ log N scaling and gives no verdict on which data the formula covers.

| Where | What it shows | Cards |
|---|---|---|
| [Spread](https://claude.ai/artifact/KMf73EpZmTtaFBp268sbMh#spread) | the largest eigenvalue of a covariance as the variance along the widest line through a 2D cloud, 1 + 19 = 20 | [Eigenvalue](../../Linear%20Algebra/Eigenvalue.md), [Covariance](../../Statistics/Covariance.md) |
| [Shrink](https://claude.ai/artifact/KMf73EpZmTtaFBp268sbMh#shrink) | the forward process multiplying coordinates by e^(−t) and variance by e^(−2t), with a square whose side and area show the square | [The Forward Process](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/The%20Forward%20Process.md) |
| [Crossing](https://claude.ai/artifact/KMf73EpZmTtaFBp268sbMh#crossing) | signal variance λ_max e^(−2t) falling to the noise variance's limit of 1 at t ≈ 1.498 | [The Forward Process](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/The%20Forward%20Process.md) |
| [Solve](https://claude.ai/artifact/KMf73EpZmTtaFBp268sbMh#solve) | solving λ_max e^(−2t) = 1 for t, one log move per press, on a line that starts at ln 20 and falls at speed 2 | none yet: speciation time |
| [Clones](https://claude.ai/artifact/KMf73EpZmTtaFBp268sbMh#clones) | copying a backward trajectory early and late, and the chance two copies end in the same class | none yet: cloning test, speciation time |
| [Slider](https://claude.ai/artifact/KMf73EpZmTtaFBp268sbMh#slider) | the commitment time growing with the log of the spread, each doubling adding 0.347 | none yet: speciation time |
| [Stops](https://claude.ai/artifact/KMf73EpZmTtaFBp268sbMh#stops) | two classes with one mean and different variances, and Achilli's ¼ log N beside ½ log N | none yet: speciation time |
| [Letters](https://claude.ai/artifact/KMf73EpZmTtaFBp268sbMh#letters) | T_s and λ_max rewritten as Biroli's t_S and Λ in Equation 4 | none yet: speciation time |

## Sampler or Score
<!-- scene: https://claude.ai/artifact/GRMF1EVkXeB82XNP5CFK8Q -->
<!-- kind: walk -->
<!-- home: PhD concept-composition, artifacts/scenes/sampler-or-score -->
<!-- source: /home/molef/PhD/concept-composition/artifacts/scenes/sampler-or-score/index.html -->

Five frames that separate the two ways a composition of two Gaussian experts can miss its target, for reading 6. Switches turn the sampler error, the score error and a 16-particle Feynman-Kac corrector on and off across 8 runs, measured by the sliced Wasserstein-2 distance to fresh target samples. The experts come from Catastrophic Compositional Generation, and the last frame shows the object counts from Bradley's Local Mechanisms paper.

**Also useful in**: plan 23 of the `01-poe-derivation-foundations` journey, on what r_t costs the samples, and plan 26 of `02-sampler-correctors-for-composition`, on Feynman-Kac correctors.

**Caveat**: the base variance of 1.25, the trained networks and every distance are this page's illustrative toy, and none reproduces a number in the paper. A second trained network moves the same way with different sizes, so read the trained-score distances as directions.

| Where | What it shows | Cards |
|---|---|---|
| [The target reaches past the data](https://claude.ai/artifact/GRMF1EVkXeB82XNP5CFK8Q#f1) | two stretched Gaussian experts composed into a wide target, with 16.9% of its samples outside every training cloud's 99% region | [Product Of Experts](../../../Artificial%20Intelligence/Generative%20Modeling/Product%20Of%20Experts.md), [Multivariate Normal Distribution](../../Statistics/Distributions/Multivariate%20Normal%20Distribution/Multivariate%20Normal%20Distribution.md) |
| [Error one: the sampler](https://claude.ai/artifact/GRMF1EVkXeB82XNP5CFK8Q#f2) | exact scores on a base of variance 1.25 still finishing at variance 7.04 against a target of 3.33 | [Product Of Experts](../../../Artificial%20Intelligence/Generative%20Modeling/Product%20Of%20Experts.md); none yet: inference-time approximation error |
| [Error two: the score](https://claude.ai/artifact/GRMF1EVkXeB82XNP5CFK8Q#f3) | a heat map of the trained composed score's error, 2.8 times larger outside the data than inside at noise 0.1 | [Score Function](../../../Artificial%20Intelligence/Generative%20Modeling/Score%20Function.md); none yet: score estimation error |
| [What the corrector can repair](https://claude.ai/artifact/GRMF1EVkXeB82XNP5CFK8Q#f4) | a 16-particle corrector that cuts the distance to the target when only the sampler is wrong and raises it when only the score is wrong, on this toy | none yet: Feynman-Kac corrector |
| [The local model reaches furthest](https://claude.ai/artifact/GRMF1EVkXeB82XNP5CFK8Q#f5) | which pixels and labels one pixel's score reads, beside the most objects reached by three models trained on 1 to 3 objects | [Score Function](../../../Artificial%20Intelligence/Generative%20Modeling/Score%20Function.md); none yet: conditional locality |

## Composing by Regions
<!-- scene: https://claude.ai/artifact/6qY8W3eiRtmoL48yNxUVpx -->
<!-- kind: walk -->
<!-- home: PhD concept-composition, artifacts/scenes/composing-by-regions -->
<!-- source: /home/molef/PhD/concept-composition/artifacts/scenes/composing-by-regions/index.html -->

Six frames on how region-based methods reconcile overlapping windows, for reading 7. Two windows denoise overlapping parts of an invented canvas of 8 positions, MultiDiffusion's step keeps their weighted average at every noise level, and Domain Expansion adds a trained network before that average. The last frame compares what each base model saw with Paper 1's setting.

**Also useful in**: none found. A search of the learning tree finds MultiDiffusion only on the paper shelf and in the words-to-learn list, and no journey plan teaches composing by regions.

**Caveat**: every position and value is invented, and no model ran, so the toy's falling gap says nothing about a real model. The page trains no coordinator and gives no verdict on it against Domain Expansion's Table 2 baselines.

| Where | What it shows | Cards |
|---|---|---|
| [Each window denoises its own part](https://claude.ai/artifact/6qY8W3eiRtmoL48yNxUVpx#f1) | one noisy canvas going into two overlapping windows, each pulled toward its own target | none yet: MultiDiffusion |
| [Where they overlap, they disagree](https://claude.ai/artifact/6qY8W3eiRtmoL48yNxUVpx#f2) | two proposed values at each shared position, 2.4 brightness units apart on this toy | none yet: MultiDiffusion |
| [Reconcile: the value closest to both](https://claude.ai/artifact/6qY8W3eiRtmoL48yNxUVpx#f3) | a weighted squared miss solved at zero slope into a weighted average, with Equations 4 and 5 compared at unequal weights | [Loss Function](../../../Artificial%20Intelligence/Machine%20Learning/Loss%20Function.md), [Derivative](../../Calculus/Derivative.md); none yet: weighted least squares |
| [Repeat at every noise level](https://claude.ai/artifact/6qY8W3eiRtmoL48yNxUVpx#f4) | the toy's gap at position 3 falling from 2.40 to 0.09 with reconciling on and growing to 3.68 with it off | none yet: MultiDiffusion |
| [A trained step before the average](https://claude.ai/artifact/6qY8W3eiRtmoL48yNxUVpx#f5) | Domain Expansion's trained network between the window outputs and the overlap average | none yet: Domain Expansion coordinator |
| [What each base model saw](https://claude.ai/artifact/6qY8W3eiRtmoL48yNxUVpx#f6) | what the pages state about MultiDiffusion's and Domain Expansion's data, beside Paper 1's exclusion of real joint images | none yet: CLEVR |

## Outside Planners and Critics
<!-- scene: https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME -->
<!-- kind: walk -->
<!-- home: PhD concept-composition, artifacts/scenes/outside-planners-and-critics -->
<!-- source: /home/molef/PhD/concept-composition/artifacts/scenes/outside-planners-and-critics/index.html -->

Fourteen presses on what an outside model adds to text-to-image, for reading 10. RPG's language model rewrites the prompt and plans regions, CountLoop's vision models plan, critique and repair an image in a loop, and Revisiting CFG tests guidance rules under one fixed protocol. Prompts, ratios, weights and table values come from the papers, with page numbers in the page's sources panel.

**Also useful in**: plan 12 of the `12-scoring-and-rival-methods` journey, which builds one runner and fills the results table.

**Caveat**: the scene drawings, graph, layout and colour tiles are illustrative and are not model outputs. The papers print no calls, time or money per image, and the page gives no verdict on whether the second CountLoop row of Table 1 is scored by its own critic.

| Where | What it shows | Cards |
|---|---|---|
| [A language model rewrites the prompt](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p2) | RPG pulling key phrases from a prompt and expanding each into a subprompt | none yet: recaptioning |
| [The plan splits the canvas](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p3) | a split ratio read as rows and columns of image regions | none yet: region planning |
| [Each region gets its own subprompt](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p4) | each region denoised with its own subprompt, then resized and concatenated into one latent | none yet: regional diffusion |
| [The whole prompt blends back in](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p5) | the whole-prompt latent mixed with the regional latent at weights 0.2 and 0.8 | none yet: regional diffusion |
| [A vision model plans the layout](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p6) | CountLoop's design model turning a prompt into a planning graph and a layout | none yet: vision-language model |
| [A second vision model critiques it](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p8) | a critic checking count with GroundingDINO and appearance with Q-Align | [Object Detector](../../../Artificial%20Intelligence/Deep%20Learning/Object%20Detector.md); none yet: vision-language model |
| [The critique repairs the plan](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p9) | the critic's feedback updating the plan until the objectives are met | none yet: critic loop |
| [Which critic parts cut the error](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p10) | counting error of 29.59 with the vision model alone and 7.59 with the detector and scorer together | [Mean Absolute Error](../../../Artificial%20Intelligence/Machine%20Learning/Mean%20Absolute%20Error.md) |
| [RPG's cost: one outside model](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p11) | the language-model dependency RPG adds before sampling | none yet: outside language model |
| [CountLoop's cost: four outside parts](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p12) | the planner, critic, detector and scorer CountLoop needs, with the critic run again every repair round | [Object Detector](../../../Artificial%20Intelligence/Deep%20Learning/Object%20Detector.md) |
| [Fix everything except the guidance rule](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p13) | holding the rest constant within each model so only the guidance rule and its settings change | [Classifier-Free Guidance](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Classifier-Free%20Guidance.md), [Benchmark](../../../Artificial%20Intelligence/Machine%20Learning/Benchmark.md) |
| [A gain can vanish on another model](https://claude.ai/artifact/HJYL5qt4kpdn4D4g4dVZME#p14) | SAG's GenEval gain over CFG on SD3.5 and its result on FLUX.2, each against a printed 95% margin | [Classifier-Free Guidance](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Classifier-Free%20Guidance.md), [Confidence Interval](../../Statistics/Hypothesis%20Testing/Confidence%20Interval.md) |

## Join and Batch
<!-- scene: https://claude.ai/artifact/FCNt5NPT8UrQE8ND8YFLec -->
<!-- kind: scene -->
<!-- home: learning journey ai-engineering/prototype-product-data-validation-end-to-end, textbook/scenes/05-the-join-and-the-batch -->
<!-- source: /home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/scenes/05-the-join-and-the-batch/index.html -->

This page follows a made-up CSV catalogue to show which rows survive an outer join on SKU, which become errors, and what one results-table row represents. It is built from the chapter's supplied outcomes for its 15-SKU sample.

**Also useful in**: ai-engineering/prototype-product-data-validation-end-to-end.

**Caveat**: All judge verdicts are fake, and the page fetches no images and runs no model. It uses the chapter's SKU-layout sample, so its 16 joined rows differ from the 17 in the separate GTIN-layout exercise.

| Where | What it shows | Cards |
|---|---|---|
| [Join](https://claude.ai/artifact/FCNt5NPT8UrQE8ND8YFLec) | outer merge on SKU with a duplicate-record fault: deduplicating removes the blank S10 copy and keeps both S13 image rows |  |
| [Batch errors](https://claude.ai/artifact/FCNt5NPT8UrQE8ND8YFLec) | silent skips against reported errors: S09, S11 and S12 vanish or appear as 3 errors among 16 results |  |
| [S08's image type](https://claude.ai/artifact/FCNt5NPT8UrQE8ND8YFLec) | how the A+ image type and the 2000 KB or 200 KB file-size limit change the Section 4 pass count out of 14 rows |  |
| [Table grain](https://claude.ai/artifact/FCNt5NPT8UrQE8ND8YFLec) | one row per result against one row per SKU, with S13's two URLs and all three errors kept |  |

## Model and Agent
<!-- scene: https://claude.ai/artifact/BiM9CqGRjXx2i1KGm7hErG -->
<!-- kind: scene -->
<!-- home: learning journey ai-engineering/prototype-product-data-validation-end-to-end, textbook/scenes/06-the-model-and-the-agent -->
<!-- source: /home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/scenes/06-the-model-and-the-agent/index.html -->

This page lets you change one part of a crafted product check and follow what reaches the next boundary, from the model request to the final verdict. It is built from the chapter's made-up SUNVITA fixtures and expected behavior, and it makes no network calls.

**Also useful in**: ai-engineering/prototype-product-data-validation-end-to-end.

**Caveat**: HTTP replies and server states are expected behavior from a local teaching model, so record what your own workspace returns. The severity rule is a prototype decision policy and says nothing about calibrated model accuracy.

| Where | What it shows | Cards |
|---|---|---|
| [Request](https://claude.ai/artifact/BiM9CqGRjXx2i1KGm7hErG#request) | How a missing bearer header gives HTTP 401 and the older prompt body gives HTTP 400 on the chat endpoint |  |
| [Event filter](https://claude.ai/artifact/BiM9CqGRjXx2i1KGm7hErG#events) | Why keeping every event's text breaks the JSON parser and keeping only the model's event parses |  |
| [Missing level](https://claude.ai/artifact/BiM9CqGRjXx2i1KGm7hErG#levels) | How Python's all() skips a missing level, so an incomplete reply still comes out as a pass |  |
| [Severity](https://claude.ai/artifact/BiM9CqGRjXx2i1KGm7hErG#severity) | The all() rule beside a severity rule that sends minor failures and missing levels to review |  |

## Round Trip Review
<!-- scene: https://claude.ai/artifact/T8nraQzWaSaPfHR3ZJft3f -->
<!-- kind: scene -->
<!-- home: learning journey ai-engineering/prototype-product-data-validation-end-to-end, textbook/scenes/08-the-round-trip-and-the-review -->
<!-- source: /home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/scenes/08-the-round-trip-and-the-review/index.html -->

This page holds three exercises: following the calls behind one results CSV, checking a file-size decision against its evidence, and placing 22 design-review records by build stage. It is built from the made-up sample catalogue and supplied example counts.

**Also useful in**: ai-engineering/prototype-product-data-validation-end-to-end.

**Caveat**: No server is contacted and no model verdict is measured, so model values stay prediction slots until an endpoint run. The suggested record grouping is a teaching arrangement and not a finding about the repository.

| Where | What it shows | Cards |
|---|---|---|
| [Follow the calls](https://claude.ai/artifact/T8nraQzWaSaPfHR3ZJft3f) | step through image GETs, ADK sessions, POST /run calls and events for S14 or the full batch, against what the CSV alone reveals |  |
| [Inspect the evidence](https://claude.ai/artifact/T8nraQzWaSaPfHR3ZJft3f) | decision record DR-01: S04 at 383.8 KB against the 200 KB and 2000 KB limits, with 8 or 9 of 14 images passing all four rules |  |
| [Check review coverage](https://claude.ai/artifact/T8nraQzWaSaPfHR3ZJft3f) | recall the 12 differences and 10 overlaps, then drag each record card onto build bands L1 to L10 |  |

## Python Pieces
<!-- scene: https://claude.ai/artifact/GSwF6su3rUhc9S2LEW9ggZ -->
<!-- kind: scene -->
<!-- home: learning journey ai-engineering/prototype-product-data-validation-end-to-end, textbook/scenes/python-pieces -->
<!-- source: /home/molef/goal-setting/learning/ai-engineering/prototype-product-data-validation-end-to-end/textbook/scenes/python-pieces/index.html -->

Change one Python decision at a time and follow the failure it causes or prevents. The page is built from the chapter's made-up catalogue and recorded outputs.

**Also useful in**: the prototype product data validation journey.

**Caveat**: the page runs no Python, fetches no images and contacts no agent, so its results are recorded or modelled.

| Where | What it shows | Cards |
|---|---|---|
| [Enum](https://claude.ai/artifact/GSwF6su3rUhc9S2LEW9ggZ) | where a misspelled image type stops once the value is validated at the boundary |  |
| [JPEG budget](https://claude.ai/artifact/GSwF6su3rUhc9S2LEW9ggZ) | three measured JPEG qualities against a fixed 200 KB limit |  |
| [Join](https://claude.ai/artifact/GSwF6su3rUhc9S2LEW9ggZ) | which rows survive when multi-barcode cells, duplicates and merge type change |  |
| [Timeout](https://claude.ai/artifact/GSwF6su3rUhc9S2LEW9ggZ) | a silent server, with and without a one-second request timeout |  |
