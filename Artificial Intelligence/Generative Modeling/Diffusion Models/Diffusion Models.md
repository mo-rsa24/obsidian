---
aliases: [diffusion model, diffusion models, DDPM, denoising diffusion]
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

Artificial Intelligence, Generative Modeling. Needs: [[Multivariate Normal Distribution#Sampling a diagonal Gaussian]] for drawing a cloud, [[Multivariate Normal Distribution#Products and quotients of diagonal Gaussians]] for the arithmetic of composing, and [[NumPy#Broadcasting]] for noising many levels in one line.

> [!question] Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers [[The Forward Process]], [[Composing Models With A Background]] with the paper's figures, [[Kinds Of Composition]], [[What An Expert Learns From Its Training Set]] and [[When Neither Training Set Holds A And B]], in 41 questions. Your attempts are saved on the page.

Each note below lists its own missing pictures and runs at its top.

**A diffusion model learns to undo a fixed noising process, and two trained models can be combined by multiplying what each believes and dividing out what they share.** The notes here start with the noising, written as one jump from a clean point to any noise level, and then take composition apart: the rule for combining two models, the samplers that reach their product, and what each model learns from its training set. All of it is worked on small Gaussian clouds, and every number can be checked by hand.

## Where you work


- Any terminal with Python 3, NumPy and Matplotlib. On the PC, that is Ubuntu under WSL, with the prepared environment `~/.vault-sandbox/bin/python`.
- A new empty folder. Nothing here touches a real project.

**Prepare the sandbox**

```bash
mkdir -p ~/playground/sandbox/gaussian-clouds && cd ~/playground/sandbox/gaussian-clouds
~/.vault-sandbox/bin/python -c "import numpy; print(numpy.__version__)"
```

You should see a version number. This run printed `2.4.6`. If the environment is missing, [[Multivariate Normal Distribution#Try sampling yourself]] steps 1 and 2 say how to make it, or how to use `uv run` instead.

Both sections use the learner's `toy.py` and `samples.py`. Save them from [[Multivariate Normal Distribution#Try sampling yourself]], steps 3 and 5, into this folder.

## Notes in this folder

Read them in this order.

- [[The Forward Process]]: noising a clean point to any noise level in one step, and why that matches fifty small steps.
- [[Composition]]: combining trained models by multiplying what each believes, in eight notes from the rule to what each expert learns.

The samplers composition borrows are taught under Mathematics, in [[Markov Chain Monte Carlo]].

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
