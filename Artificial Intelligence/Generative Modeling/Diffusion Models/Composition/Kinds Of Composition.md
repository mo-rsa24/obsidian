---
aliases: [kinds of composition, types of composition, composition taxonomy, intersection composition, interaction composition, interaction term, co-occurrence intersection interaction, contention, chimera, concept bleeding, attribute leakage, catastrophic neglect, attribute binding, product over the same variables, region-restricted product, product over a partition, wet dog]
sources:
  - "Bradley, Nakkiran, Berthelot, Thornton, Susskind, Mechanisms of Projective Composition of Diffusion Models, ICML 2025: https://arxiv.org/abs/2502.04549"
  - "Du, Durkan, Strudel, Tenenbaum, Dieleman, Fergus, Sohl-Dickstein, Doucet, Grathwohl, Reduce, Reuse, Recycle: Compositional Generation with Energy-Based Diffusion Models and MCMC, ICML 2023: https://arxiv.org/abs/2302.11552"
  - "Hinton, Training Products of Experts by Minimizing Contrastive Divergence, Neural Computation 14(8), 1771 to 1800, 2002: https://doi.org/10.1162/089976602760128018"
  - "Liu, Li, Du, Torralba, Tenenbaum, Compositional Visual Generation with Composable Diffusion Models, ECCV 2022: https://arxiv.org/abs/2206.01714"
  - "Chefer, Alaluf, Vinker, Wolf, Cohen-Or, Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models, SIGGRAPH 2023: https://arxiv.org/abs/2301.13826"
  - "Bar-Tal, Yariv, Lipman, Dekel, MultiDiffusion: Fusing Diffusion Paths for Controlled Image Generation, ICML 2023: https://arxiv.org/abs/2302.08113"
---

# Kinds Of Composition

Up: [[Composition]] · ⬅️ [[The Product As An Intersection]] · [[The Order Of Multiplying And Noising]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models, Composition. Needs: [[Composing Models With A Background]].

> [!question] Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers this note, with the rest of the [[Diffusion Models]] folder. Your attempts are saved on the page.

> [!warning] Unfinished
> - One concept picture is waiting to be drawn: prompt 22 in the vault's `.prompts/Diffusion Models.md`.
> - The overlap-dial idea in the reduce-reuse-recycle repository applies this note in words only.

**"Composition" names at least three different operations, told apart by which variables each expert scores. Co-occurrence is a product over disjoint regions plus a layout. Intersection is a product over the same variables, which is what a product of experts computes. Interaction is the product plus a term that vanishes when the two labels are [conditionally independent](../../../../Mathematics/references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=201) given the image.** The operators are *derived* below. The three names are the walk's working names; the field's words for each are in the table.

**When to reach for it.** Before composing two concepts, ask which kind the pair is. A chest drain beside a pneumothorax edge is mostly different pixels, so it is co-occurrence. A shape that is both square-ish and circle-ish is one object scored by both experts, so it is intersection. A wet dog in the rain, or the lung pattern of tuberculosis with silicosis, is a change neither concept shows alone, so it is interaction. Each kind needs different training data and fails differently, and the plain product serves only intersection as written.

| Kind | What it is | The operator | What it needs from training data | How it fails | The field's words |
|---|---|---|---|---|---|
| co-occurrence | two concepts, each whole, each in its own region: a cat beside a dog | $p(\text{layout})\;p_A(x_S \mid \text{layout})\;p_B(x_{S'} \mid \text{layout})$, with $S$ and $S'$ disjoint sets of pixels | each concept alone, at many positions, over varied backgrounds; never the two together | **contention**: both experts score the same pixels, so the product lands on a chimera, the hybrid of the shared case above | Bradley et al.'s co-occurrence and projective composition (*cited*, above); catastrophic neglect when one subject vanishes and failed attribute binding (Chefer et al. 2023, *cited*); concept bleeding and attribute leakage (*stated*: common usage, no single source checked); region-restricted products in MultiDiffusion (Bar-Tal et al. 2023, *cited*) |
| intersection | one thing that satisfies both concepts on the same pixels | $p_A(x)\,p_B(x)$ | each expert must already give the overlap some density; a product intersects supports and creates none, as [[When Neither Training Set Holds A And B]] runs | **empty intersection**: the supports barely meet, so the product peaks in a gap neither expert believes in, the far pair of [[The Product As An Intersection]] | product of experts (Hinton 2002, *cited*); Du et al.'s "intersection" (*cited*, above); Composable Diffusion's AND (Liu et al. 2022, *cited*) |
| interaction | the concepts change each other: rain and a dog give a wet dog | the Bayes composition plus $\log \dfrac{p(A, B \mid x)}{p(A \mid x)\,p(B \mid x)}$ | joint samples showing the change, in whichever model carries it (see below) | **missing interaction**: a dry dog standing in rain | no single name found (*stated*) |

The split and shared toy above is co-occurrence done two ways: split gives each expert its own pixel, which is the operator in the first row, and shared makes both experts score $x_0$, which is contention. The ring-times-bar of Du et al.'s Figure 2, under [[Product, Mixture And Negation]], is an intersection toy: both experts score both coordinates.

**How the interaction term arises.** Write each conditional with [Bayes' rule](../../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=105), then divide:

$$
\begin{aligned}
p(x \mid A, B) &= \frac{p(A, B \mid x)\,p(x)}{p(A, B)} \\
\frac{p(x \mid A)\,p(x \mid B)}{p(x)} &= \frac{p(A \mid x)\,p(x)}{p(A)} \cdot \frac{p(B \mid x)\,p(x)}{p(B)} \cdot \frac{1}{p(x)} = \frac{p(A \mid x)\,p(B \mid x)\,p(x)}{p(A)\,p(B)} \\
\frac{p(x \mid A, B)}{p(x \mid A)\,p(x \mid B)/p(x)} &= \frac{p(A, B \mid x)}{p(A \mid x)\,p(B \mid x)} \cdot \frac{p(A)\,p(B)}{p(A, B)}
\end{aligned}
$$

Taking [logs](../../../../Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=110) turns the products into sums:

$$
\log p(x \mid A, B) = \log p(x \mid A) + \log p(x \mid B) - \log p(x) + \log \frac{p(A, B \mid x)}{p(A \mid x)\,p(B \mid x)} + \log \frac{p(A)\,p(B)}{p(A, B)}
$$

*Derived.* The last term holds no $x$, so its gradient is zero and the score form is exact without it: $\nabla \log p(x \mid A, B) = s(x \mid A) + s(x \mid B) - s(x) + \nabla \log \frac{p(A, B \mid x)}{p(A \mid x)\,p(B \mid x)}$. The interaction term is zero at every $x$ exactly when $p(A, B \mid x) = p(A \mid x)\,p(B \mid x)$ for every $x$, which is Definition 6.11 on the linked page. Composable Diffusion's AND is the first three terms. *Derived.*

<!-- video-table: bayes-theorem rev=1 -->
3Blue1Brown, then StatQuest, on Bayes' theorem, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | From a worked example to the general formula | Intuition | [3Blue1Brown, Bayes theorem, the geometry of changing beliefs, 4:09 to 10:13](https://www.youtube.com/watch?v=HZGCoVF3YvM&t=249s) |
| 2 | Bayes' theorem derived step by step | Proof | [StatQuest, Bayes' Theorem, Clearly Explained, 5:21 to 9:12](https://www.youtube.com/watch?v=9wCnvr7Xw4E&t=321s) |

Both work with events, not densities, so neither divides a conditional density by a prior the way the composition rule does. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

**Where a wet dog has to come from.** When each label is fixed by the image, so $p(A \mid x)$ and $p(B \mid x)$ are each 0 or 1, the joint label is fixed too, $p(A, B \mid x) = p(A \mid x)\,p(B \mid x)$, and the interaction term is zero everywhere. The Bayes composition is then exactly $p(x)$ restricted to images that are both A and B, so wet dogs appear only if $p(x)$, the unconditional model, saw wet dogs. A plain product $p_A\,p_B$ has no $p(x)$ in it, so it can produce a wet dog only if expert A's or expert B's own training images held some. *Derived* from the identity above.

![The kinds of composition as three cards, each showing which pixels each expert scores and its failure|800](assets/kinds-of-composition-the-concept.webp)

*The kinds of composition as three cards, each showing which pixels each expert scores and its failure.*

> [!note]- How this was checked
> Kinds Of Composition and [[What An Expert Learns From Its Training Set]] were written on 2026-10-14 on the cluster (mscluster, Linux), from one turn of the overlap-dial `drip-idea` walk. Nothing in them was run: the cluster has no `~/.vault-sandbox`, so `labels.py` and its expected output are worked by hand in [[What An Expert Learns From Its Training Set#How the expert's training set works]], and the section stays in the unfinished box until a machine with the environment runs it. The identity for the interaction term is derived in the note; the walk's own draft, `composition-terms.md` in the research repository, writes it without the constant $\log \frac{p(A)\,p(B)}{p(A, B)}$, which changes the density and not the score. The textbook pages were opened before linking: Bayes' theorem on page 105 of the probability book (Theorem 2.7), conditional independence on page 201 of Mathematics for Machine Learning (Definition 6.11), log rules on page 110 of the algebra handbook. The arXiv abstracts of Liu et al., Chefer et al., Bar-Tal et al. and Geirhos et al. were fetched on 2026-10-14, and the quoted phrases ("catastrophic neglect", attribute binding, the definition of shortcuts) are from them; Hinton 2002's DOI resolved to Neural Computation 14(8), pages 1771 to 1800. Ho et al.'s equation (14) and section 3.2 are cited from the paper as already listed, not re-read in this session. No old LibreOffice note was read: `/mnt/c/Users/molef/LibreOffice/Learning/` does not exist on the cluster.
