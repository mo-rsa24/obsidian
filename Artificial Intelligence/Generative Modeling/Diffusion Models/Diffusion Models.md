---
aliases: [diffusion model, diffusion models, DDPM, denoising diffusion, denoising diffusion probabilistic model]
sources:
  - "Ho, Jain, Abbeel, Denoising Diffusion Probabilistic Models, NeurIPS 2020: https://arxiv.org/abs/2006.11239"
  - "Bradley, Nakkiran, Berthelot, Thornton, Susskind, Mechanisms of Projective Composition of Diffusion Models, ICML 2025: https://arxiv.org/abs/2502.04549"
  - "Du, Durkan, Strudel, Tenenbaum, Dieleman, Fergus, Sohl-Dickstein, Doucet, Grathwohl, Reduce, Reuse, Recycle: Compositional Generation with Energy-Based Diffusion Models and MCMC, ICML 2023: https://arxiv.org/abs/2302.11552"
  - "Wikipedia, Product of experts: https://en.wikipedia.org/wiki/Product_of_experts, read 2026-10-04, CC BY-SA 4.0"
  - "Hinton, Training Products of Experts by Minimizing Contrastive Divergence, Neural Computation 14(8), 1771 to 1800, 2002: https://doi.org/10.1162/089976602760128018"
  - "Liu, Li, Du, Torralba, Tenenbaum, Compositional Visual Generation with Composable Diffusion Models, ECCV 2022: https://arxiv.org/abs/2206.01714"
  - "Chefer, Alaluf, Vinker, Wolf, Cohen-Or, Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models, SIGGRAPH 2023: https://arxiv.org/abs/2301.13826"
  - "Bar-Tal, Yariv, Lipman, Dekel, MultiDiffusion: Fusing Diffusion Paths for Controlled Image Generation, ICML 2023: https://arxiv.org/abs/2302.08113"
  - "Geirhos, Jacobsen, Michaelis, Zemel, Brendel, Bethge, Wichmann, Shortcut Learning in Deep Neural Networks, Nature Machine Intelligence 2020: https://arxiv.org/abs/2004.07780"
---

# Diffusion Models

Up: [[Generative Modeling]]

Artificial Intelligence, Generative Modeling. Needs: [[Sampling A Diagonal Gaussian]] for drawing a cloud, [[Products And Quotients Of Diagonal Gaussians]] for the arithmetic of composing, and [[Broadcasting]] for noising many levels in one line.

> [!question] Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers [[The Forward Process]], [[Composing Models With A Background]] with the paper's figures, [[Kinds Of Composition]] with its parts world, [[What An Expert Learns From Its Training Set]] and [[When Neither Training Set Holds A And B]] with its four-quadrant answer key, and [[Three Things Called Annealing]] apart from [[The Tempered Density And Its Score]], in 91 questions. Your attempts are saved on the page.

Each note below lists its own missing pictures and runs at its top.

**A diffusion model learns to undo a fixed noising process, and two trained models can be combined by multiplying what each believes and dividing out what they share.** The notes here start with the noising, written as one jump from a clean point to any noise level, and then take composition apart: the rule for combining two models, the samplers that reach their product, what each model learns from its training set, and the three numbers this literature calls annealed: the temperature, the noise level and the guidance scale. All of it is worked on small Gaussian clouds and a 16-pixel cat-dog toy, and every number can be checked by hand.

<!-- video-table: forward-process rev=1 -->
Stanford CS236, then Vizuara, on the forward process, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | The noising process that turns data into noise | Intuition | [Stanford CS236, lecture 16, 12:22 to 16:23](https://www.youtube.com/watch?v=VsllsC2JMGY&t=742s) |
| 2 | Many small noising steps combined into one transition to any noise level | Proof | [Stanford CS236, lecture 16, 16:23 to 19:05](https://www.youtube.com/watch?v=VsllsC2JMGY&t=983s) |
| 3 | Why each step scales the mean down as well as adding noise | Intuition | [Vizuara, Principles of Diffusion Models, lecture 3, 33:51 to 42:46](https://www.youtube.com/watch?v=Dx-1agEjlJs&t=2031s) |

Vizuara is added for row 3, which no CS236 chapter covers; neither noises a two-dimensional Gaussian cloud and checks the closed form. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

## Where you work


- Any terminal with Python 3, NumPy and Matplotlib. On the PC, that is Ubuntu under WSL, with the prepared environment `~/.vault-sandbox/bin/python`.
- A new empty folder. Nothing here touches a real project.

**Prepare the sandbox**

```bash
mkdir -p ~/playground/sandbox/gaussian-clouds && cd ~/playground/sandbox/gaussian-clouds
~/.vault-sandbox/bin/python -c "import numpy; print(numpy.__version__)"
```

You should see a version number. This run printed `2.4.6`. If the environment is missing, [[Sampling A Diagonal Gaussian#Try sampling yourself]] steps 1 and 2 say how to make it, or how to use `uv run` instead.

Both sections use the learner's `toy.py` and `samples.py`. Save them from [[Sampling A Diagonal Gaussian#Try sampling yourself]], steps 3 and 5, into this folder.

## Notes in this folder

Read them in this order.

- [[The Forward Process]]: noising a clean point to any noise level in one step, and why that matches fifty small steps.
- [[From Many Steps To One Jump]]: why the small steps collapse into the one jump, two steps by hand and then induction, with $\bar\alpha_t$ as the product of the $1 - \beta$ factors.
- [[Running From Many Steps To One Jump]]: the two steps and the induction run in an empty folder, from the cosine schedule and the forgotten shrink to 200,000 drawn chains, each output read field by field.
- [[The Density Of The One Jump]]: the noise as one draw, the density $q(x_t \mid x_0)$ of the noised point for a fixed clean point, and why its exponent at the drawn point is $-|\varepsilon|^2/2$ at every step.
- [[How The Density Follows From The Draw]]: the derivation of that density from the one-shot draw, the noise as one draw, its centre, spread and shape, the 2D Gaussian written out, then the exponent worked on the toy with the centre's square root dropped.
- [[Running The Density Of The One Jump]]: the density run in an empty folder, from the centre without its square root and the density at two steps to SciPy's check and the same draw at five steps, each output read field by field.
- [[The Cosine Noise Schedule]]: where every $\bar\alpha_t$ comes from, the 101 boundary values $C_k$ of a 100-step timetable, each the squared cosine of an angle on a quarter turn, computed by hand.
- [[How Each Piece Of The Cosine Schedule Works]]: the formula for $C_k$ run one move per line and drawn at post 51, then the angles of posts 0, 1, 51 and 100 on the unit circle, with the runs without the offset and without the denominator beside them.
- [[Running The Cosine Noise Schedule]]: the boundary values run in an empty folder, from the formula as three functions to four posts by hand, the code's form beside $\bar\alpha$ and three more posts, each output read field by field.
- [[The Quarter Circle Under The Cosine Schedule]]: the geometry under $C_k$ on a Cartesian plane, drawn by the Python that computes it: the name taken apart word by word, then the 101 posts on the quarter arc as a ruler, with the offset and the division by $1 + \delta$ each removed beside them.
- [[How The Quarter Circle Gives The Multipliers]]: the point at post 51 as step 50's signal and noise multipliers, why the multipliers lie exactly on the circle and 0.0001 off the drawn point, and the quarter turn, the point and the fraction in one mechanism figure.
- [[Running The Quarter Circle Under The Cosine Schedule]]: the quarter circle's figure scripts run in an empty folder, from the plane and `cosine.py` to the six moves at post 51 in one run, each output read field by field.
- [[The Quarter Turn And The Fraction]]: the squared cosine walked across all 101 posts, flat at both ends, and the fraction $\cos^2\theta_k / \cos^2\theta_0$, each name taken apart word by word; then each piece removed in turn, with what it changes.
- [[Which Pieces Of C_k Change The Noise]]: why the denominator cancels out of every $\beta_t$, worked at steps 0, 50 and 98, and the square and the division by $1 + \delta$ each removed and drawn, with what they do to $\beta_{50}$ and $\beta_{99}$.
- [[Running The Quarter Turn And The Fraction]]: the fraction's scripts run in the quarter circle's folder, from the curve's first step to β with and without each piece, each output read field by field.
- [[Composition]]: combining trained models by multiplying what each believes, in notes from the rule to what each expert learns and what annealing moves.
- [[DDIM]]: DDIM samples a trained diffusion model through a family of non-Markovian reverse steps that keep DDPM's marginals, and with its noise set to zero the sampler is deterministic and can skip most of the steps.
- [[Classifier-Free Guidance]]: Classifier-free guidance steers a diffusion model toward a condition by taking its unconditional prediction and adding ω times the difference between the conditional and unconditional predictions, both made by one network trained with the condition sometimes dropped.

The samplers composition borrows are taught under Mathematics, in [[Markov Chain Monte Carlo]].

## Where to learn this

**Diffusion model**, the denoising diffusion probabilistic model. Also: DDPM, denoising diffusion, diffusion models.

**Textbooks**

- Understanding deep learning, sections 18.1 to 18.6: [pages 362 to 379](../../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=362). Works the forward process on one-dimensional data with numbers (T = 100 steps at β = 0.03, and the diffusion kernel from x = 2.0 drawn at t = 20, 40 and 80), then the decoder, the loss, its reparameterisation as noise prediction, and the training and sampling algorithms on page 377.
- Probabilistic machine learning: advanced topics, section 25.2: [pages 890 to 896](../../../Mathematics/references/textbooks/machine-learning/probabilistic-machine-learning-advanced-topics.pdf#page=890). The DDPM as a VAE whose encoder is a fixed noising chain, illustrated on 1d data in Figure 25.2, through the training objective and a learned noise schedule.
- The little book of generative AI foundations, chapter 4: [pages 68 to 88](../../../Mathematics/references/textbooks/machine-learning/the-little-book-of-generative-ai-foundations.pdf#page=68). The discrete-time DDPM derived in full: the forward chain and its closed form, the reverse process, the ELBO, the exact reverse posterior, and the noise-prediction objective with its training and sampling loop.

**Videos**

- CME296 lecture 1, 23:31 to 26:35: [watch](https://www.youtube.com/watch?v=tr-CUpw--ck&t=1411s). Introduces DDPM's forward process q, which corrupts a training image with noise step by step, and the learned reverse process p_θ, which removes it. Caption-read.
- CME296 lecture 1, 38:51 to 46:03: [watch](https://www.youtube.com/watch?v=tr-CUpw--ck&t=2331s). Derives on the board the closed form x_t = √ᾱ_t x_0 + √(1 − ᾱ_t) ε by merging independent Gaussian noise terms. Caption-read.
- CME296 lecture 1, 1:26:55 to 1:29:34: [watch](https://www.youtube.com/watch?v=tr-CUpw--ck&t=5215s). The DDPM training loop (sample x_0, ε and t, regress the noise) and the sampling loop from x_T to x_0 with fresh noise at each step. Caption-read.
- CS231n lecture 14, 30:50 to 35:55: [watch](https://www.youtube.com/watch?v=Edr4uZFh4EE&t=1850s). The intuition: noise of the data's shape mixed in by a level t from 0 (clean) to 1 (pure noise), a network that removes a little at a time, and sampling from pure noise. Caption-read.

**Papers**

- Chan 2024, Tutorial on diffusion models for imaging and vision, sections 2.1 to 2.5: [pages 18 to 39](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/tutorial-on-diffusion-models-for-imaging-and-vision.pdf#page=18). DDPM built as an extension of the VAE: building blocks, the ELBO, the reverse-process distribution, training and inference, and predicting the noise.

**Our plans and chapters**

- [Write DDPM's forward and reverse steps again](/home/molef/goal-setting/learning/deep-learning/generative-models/03-sampling-from-a-graph/plans/30-ddpm-step-refresher.md), deep-learning/generative-models/03-sampling-from-a-graph, plan 30. Both steps worked on a single pixel x₀ = 1 with β_t = 0.02 for 50 steps.
- [DDPM end to end on two moons](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/plans/01-ddpm-end-to-end-on-two-moons.md), deep-learning/diffusion-models/00-from-scratch-to-sdxl, plan 01. A whole DDPM trained and sampled on the two-moons toy, then the same code with 10 steps in place of 1000.
- [The schedule and one reverse step](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/10-schedule-and-reverse-step.md), deep-learning/diffusion-models/01-poe-derivation-foundations, plan 10. The noise schedule plotted from your own configuration, and one reverse step written out with every term named.

**Scenes**

- [Kinds of composition notebook, Setup: the ideal expert](https://claude.ai/artifact/DBmJtn6xy75sPtQwPEvQZU#nb-sec1). The ideal expert's log-density on a grid, in four steps from the 2D Gaussian to its logsumexp form, then normalised so it integrates to 1.
- [The SDXL notebook in ten parts, Forward diffusion](https://claude.ai/artifact/1GayZthQkRL4FmukdCV9WW#nb-latent). The clean latent and noise mixed into the noisy latent at t = 50, 500 and 950 under the cosine schedule, with alpha-bar worked to 0.992, 0.494 and 0.006.

**Figures**

- <a href="/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/hero-diffusion-against-bridge.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/hero-diffusion-against-bridge.jpg" width="200" alt="Top row a cat fading to noise under a diffusion model, bottom row a cat morphing into a dog under a Schrodinger bridge"></a> Sophia Tang, "Foundations of Schrödinger Bridges for Generative Modeling", cover figure: [the paper](https://arxiv.org/abs/2603.18992), [what it shows](/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/README.md#hero-diffusion-against-bridgejpg). The top row is a diffusion model, a cat fading to a concentric Gaussian and run back with the score, and the bottom row is a Schrödinger bridge carrying the cat to a dog, so a diffusion model is the bridge whose far end is fixed to noise.
- <a href="/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/ch6-score-based-models.jpg"><img src="/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/ch6-score-based-models.jpg" width="200" alt="A cat fading to noise, the reverse SDE with its score term highlighted, a parameterised score box, and the score matching loss"></a> Sophia Tang, "Foundations of Schrödinger Bridges for Generative Modeling", chapter 6 figure: [the paper](https://arxiv.org/abs/2603.18992), [what it shows](/home/molef/goal-setting/learning/deep-learning/diffusion-models/04-schrodinger-bridges/artifacts/figures/foundations-of-schrodinger-bridges/README.md#ch6-score-based-modelsjpg). The same diffusion row with its one learned part boxed: the network s_θ(x, s) replaces the score in the reverse SDE and is trained by the score-matching loss on every noise level.

> [!note]- How this was checked
> Every output above was run by the writer in an empty folder, `~/playground/sandbox/gaussian-clouds`, on the PC: Ubuntu under WSL2, through the prepared environment `~/.vault-sandbox/bin/python` (Python 3.11.13, NumPy 2.4.6, Matplotlib 3.11.2), on 2026-10-04. The folder was removed afterwards and the clean-up check returned 2.
>
> `toy.py` is the learner's own file from the walk's playground. `noised.py` is the learner's file with its print line rewritten to show the closed form beside each level, which the walk asked for. Its measured values matched the walk's answer key, `checks/noised.out`, to the digits shown. The four $\alpha$ values and $\bar\alpha = 0.4788$ in step 5 are plan 09's, line 143.
>
> The terminal picture was rendered from the captured text by a script in DejaVu Sans Mono, never drawn. The composition picture is `picture.py`'s own saved figure, checked by eye: the green dots sit at $(-2, 2)$ and $(-1.5, 0)$ and the purple crosses at $(-1.6, 1.6)$ and $(-1.2, 0)$.
>
> The paper's Figures 1, 2, 3, 4, 5, 7, 8 and 12 are the authors' own image files, copied byte for byte from the arXiv source package (`paper/source/figures/` in the journey's staged sources) into `references/`, and each was opened before filing. Each caption is the LaTeX caption from `src/intro.tex` (Figures 1, 2, 3), `src/projective_comp.tex` (4, 5), `src/practical.tex` (7, 8) and `src/appendix_notes.tex` (12), with LaTeX markup removed and every cross-reference written as the PDF prints it. The figure numbers are the ones printed in `2502.04549.pdf`, version 3. The paper is under arXiv's non-exclusive distribution licence, which does not grant a reuse licence; the copies are here for study, with citation on every embed. The lines under each caption tying a figure to the toy are the writer's, and each is marked shown, derived or cited.
>
> The five output pictures were rendered from the captured text by a script in DejaVu Sans Mono, never drawn, and each was opened before filing. The paper's Figure 2 is the authors' `fig/comp_fig4.pdf` from the arXiv source package, converted to PNG at 150 dpi with `pdftoppm` and opened before filing; its caption is the LaTeX caption from `text/method.tex` lines 36 to 43 with markup removed. Quotations from the paper are from its source: `text/abstract.tex` line 2, `text/method.tex` lines 31 to 131, `text/appendix.tex` line 232. The figure numbers and equation numbers 11 and 12 are as the journey's read-ahead reads them from `2302.11552.pdf`.
>
> The re-teach in the walk described expert 2 in shared as an object in the left half only. It also narrows the right half, from variance 4 to 1, and the table and derivation here carry that.
>
> References, each answering 200 on 2026-10-04: [Ho et al. on arXiv](https://arxiv.org/abs/2006.11239), [Bradley et al. on arXiv](https://arxiv.org/abs/2502.04549), [Du et al. on arXiv](https://arxiv.org/abs/2302.11552) (checked 2026-10-09), [Product of experts](https://en.wikipedia.org/wiki/Product_of_experts) on Wikipedia, CC BY-SA 4.0. Definition 5.1 and Definition 5.2 were read in the walk's read-ahead, `read-ahead/05-simple-construction.md`, which quotes the paper's source `src/composition.tex` lines 33 to 46. The sketchpad link is the learner's own private artifact and was not fetched. No tldr-pages entry covers this.
>
> The Where to learn this card was checked on 2026-10-24: every textbook and paper page range was read in the PDF with pdftotext (Understanding deep learning and Probabilistic machine learning: advanced topics found through their back-of-book indexes), each video row was read in the caption-read CME296 and CS231n lecture maps under `~/.claude/cache/captions/`, each plan was read at its title and description, and check-cards.py opened every link.
