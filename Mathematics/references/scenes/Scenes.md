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
