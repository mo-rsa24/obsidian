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
| [Setup: the ideal expert](https://claude.ai/artifact/DBmJtn6xy75sPtQwPEvQZU#nb-sec1) | the ideal expert's log-density on a grid, in four steps from the 2D Gaussian to its logsumexp form, then normalised so it integrates to 1 | [Probability Density Function](../../Statistics/Distributions/Probability%20Density%20Function.md), [Diffusion Models](../../../Artificial%20Intelligence/Generative%20Modeling/Diffusion%20Models/Diffusion%20Models.md) |
| [Same points, two labellings](https://claude.ai/artifact/DBmJtn6xy75sPtQwPEvQZU#nb-sec2) | the denoising loss and one gradient step, showing the gradient is identical under two labellings because no label enters the loss | [Loss Function](../../../Artificial%20Intelligence/Machine%20Learning/Loss%20Function.md), [Gradient](../../Calculus/Gradient.md), [Backpropagation](../../../Artificial%20Intelligence/Deep%20Learning/Backpropagation.md) |
| [A classifier learns "not B"](https://claude.ai/artifact/DBmJtn6xy75sPtQwPEvQZU#nb-sec4) | a classifier trained on the labels the data carries learns the hidden-B points as "not B" | [Classifier](../../../Artificial%20Intelligence/Machine%20Learning/Classifier.md) |
| [Four kinds of composition](https://claude.ai/artifact/DBmJtn6xy75sPtQwPEvQZU#nb-sec5) | co-occurrence, contention and interaction computed as products of two experts' densities on one grid | [Product Of Experts](../../../Artificial%20Intelligence/Generative%20Modeling/Product%20Of%20Experts.md) |
