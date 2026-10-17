---
aliases: [annealed MCMC, annealed MCMC sampling, annealed Langevin, Reduce Reuse Recycle Algorithm 1, Algorithm 1, ULA, unadjusted Langevin algorithm, U-HMC, unadjusted HMC]
---

# Annealed MCMC

Up: [[Markov Chain Monte Carlo]] · [[Step Size And The Accept Step]] ➡️

Mathematics, Statistics, Markov Chain Monte Carlo. Needs: [[The Order Of Multiplying And Noising]], whose route B this sampler follows.

> [!warning] Unfinished
> - One concept picture is waiting to be drawn: prompt 17 in the vault's `.prompts/Diffusion Models.md`.

**Annealed MCMC, the paper's Algorithm 1, takes a few MCMC steps at every noise level from the noisiest to the clean one, each aimed at that level's composed curve, and carries the cloud down to the next level unchanged.** With summed scores the curve at each level is route B, and route B ends at the product, so the cloud ends there too. *Cited:* section 4.1, Algorithm 1, `text/method.tex` lines 99 and 107 to 121 of the paper's source.

```text
x ~ p_T                                   start from pure noise
for t = T, T-1, ..., 0:                   every level, noisiest first
    repeat N times:  x ~ k_t( . | x)      an MCMC kernel aimed at level t's composed curve
    carry x to level t - 1 unchanged
return x
unadjusted Langevin kernel:  k_t: x + eta * s(x, t) + sqrt(2 eta) z,  s = the summed score
cost: N x (T + 1) score evaluations per sample; 10 x 101 = 1,010 against the reverse process's 100
```

*🖼️ Diagram wanted: the concept, route A and route B bells at five levels with the chain settling on route B at each. Prompt 17 in the vault's `.prompts/Diffusion Models.md`.*

**What each setting controls.** The number of steps per level sets how close the mean gets: $-0.148$ with one step of 0.01 per level, $-0.2286$ with 10, $-0.2305$ with 30, against the product's $-0.2308$. The step size sets the final width: 0.3128 at step 0.01, 0.3235 at 0.03, 0.3674 at 0.1, each the width an unadjusted chain at that step keeps on the clean product, derived in [[The Energy Parameterisation#How the energy works]]. More steps per level do not shrink it. A step too small for the steps given, 0.001 with 10 per level, never travels and ends at mean $-0.147$. *Shown*, step 8, `steps_per_level.py`.

**Score models allow only unadjusted kernels.** With the standard noise-predicting network there is no energy, so no Metropolis correction: the paper uses ULA, unadjusted Langevin, and U-HMC, unadjusted Hamiltonian Monte Carlo. ULA at one level is the reverse step "repeatedly running the diffusion reverse process at the same noise level with composed score functions". *Cited:* `text/method.tex` line 127. An accept step removes the width error at any step size; see [[Step Size And The Accept Step]].

> [!note]- How this was checked
> The shared setup and sources are in the box at the end of [[Diffusion Models]].
