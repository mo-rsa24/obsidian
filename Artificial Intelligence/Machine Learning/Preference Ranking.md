---
aliases: [preference ranking, ranked pairs, ranked-pairs loss, human preference ranking, ranking of images by people]
standard: vault-note v2
---

# Preference Ranking

Up: [[Machine Learning]]

Artificial Intelligence, Machine Learning. Needs: [[Loss Function]] and [[Probability]]. Used by [[ImageReward]].

**Preference ranking teaches a model from people putting several outputs in order, so the model learns to give the better one a higher number.**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the journey's chapters need. The Textbooks and Videos groups of the card are not built; waiting: `/concept-link build a card for Preference Ranking`.
> - No claim is marked stated.

## What the chapters need

**The data.** People ranked several images made for the same prompt. The paper collected 136,892 compared pairs over 8,878 prompts, and the annotators rated how well the picture matches the prompt, how well made it looks and whether it is harmful, then ranked *(cited: ImageReward paper page 3)*.

### The ranked-pairs loss

$$
\underbrace{\mathrm{loss}(\theta)}_{\text{what training lowers}}=-\underbrace{E}_{\text{average over ranked pairs}}\ \log\ \underbrace{\sigma}_{\text{logistic}}\Big(\underbrace{f(T,{\color{#2f855a}x_i})-f(T,{\color{#c53030}x_j})}_{\text{preferred above the other}}\Big)
$$

**What the equation says.** f(T, x) is the number the model gives image x for prompt T; x_i is the image people ranked better, x_j the one ranked worse. The loss is small when the preferred image's number sits well above the other's. *(cited: ImageReward paper page 4)*

**Why the subtraction is there.** It is the gap between the two numbers, so only the order of a pair is rewarded. **Why the sigma is there.** It turns the gap into a value between 0 and 1. **Why the minus and the log are there.** The loss is small when sigma is near 1.

**At scoring time none of this runs.** The number is just f(T, x).

**What it misses.** The number blends alignment, fidelity and harm, so a change in it cannot be assigned to one of them.

## Where to learn this

**Preference Ranking**, training from people's orderings. Also: ranked pairs, ranked-pairs loss, human preference ranking, ranking of images by people.

**Papers**

- [ImageReward paper, page 3](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/imagereward-human-preferences-for-text-to-image-generation.pdf#page=3): the annotation and the pair counts.
- [ImageReward paper, page 4](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/scorers/imagereward-human-preferences-for-text-to-image-generation.pdf#page=4): the training loss and Table 1.

**Our plans and chapters**

- [Journey chapter 2, how it was taught](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/02-imagereward.md#how-it-was-taught): the loss taken apart.
