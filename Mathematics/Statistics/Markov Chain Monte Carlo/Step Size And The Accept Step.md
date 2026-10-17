---
aliases: [step size and the accept step, accept step, accept-reject step, acceptance rate, acceptance rate as a dial, share accepted, stability limit, 2 / P, Langevin step-size bias, unadjusted Langevin, transient chain, lighter-than-Gaussian tails]
---

# Step Size And The Accept Step

Up: [[Markov Chain Monte Carlo]] · ⬅️ [[Annealed MCMC]]

Mathematics, Statistics, Markov Chain Monte Carlo. Needs: [[Multivariate Normal Distribution]] for a Gaussian's precision.

> [!warning] Unfinished
> - One concept picture is waiting to be drawn: prompt 18 in the vault's `.prompts/Diffusion Models.md`.
>
> Stated, not checked: 1 claim, marked where it sits.

Textbook: [Volume L3, section 12, the Metropolis corrector by hand, p. 97](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/l3-stochastic-processes.pdf#page=97)

**An unadjusted Langevin chain<sub>[1](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/l3-stochastic-processes.pdf#page=99 "volume L3, stochastic processes, p. 99"), [2](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/l3-stochastic-processes.pdf#page=63 "volume L3, stochastic processes, p. 63")</sub> on a Gaussian of [precision](../../references/textbooks/machine-learning/pattern-recognition-and-machine-learning.pdf#page=43) $P$ settles at variance $1 / (P(1 - \eta P/2))$ and runs away once its step $\eta$ passes $2/P$. A Metropolis accept step<sub>[1](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/l3-stochastic-processes.pdf#page=98 "volume L3, stochastic processes, p. 98"), [2](/home/molef/goal-setting/learning/deep-learning/diffusion-models/00-from-scratch-to-sdxl/textbook/l3-stochastic-processes/l3-stochastic-processes.pdf#page=21 "volume L3, stochastic processes, p. 21")</sub> holds the target's width at any step, and turns the share of proposals accepted into the dial for choosing the step.** The settled variance is derived in [[The Energy Parameterisation#How the energy works]].

<!-- video-table: metropolis-hastings rev=1 -->
ritvikmath, then Stanford CS236, on the Metropolis-Hastings accept step, in the order to watch:

| Order | What it covers | Kind | Watch |
|---|---|---|---|
| 1 | Working out the acceptance probability for a candidate | Proof | [ritvikmath, Metropolis-Hastings, 7:50 to 12:04](https://www.youtube.com/watch?v=yCv2N7wGDCw&t=470s) |
| 2 | Accepting or rejecting the candidate with that probability | Intuition | [ritvikmath, Metropolis-Hastings, 12:04 to 13:31](https://www.youtube.com/watch?v=yCv2N7wGDCw&t=724s) |
| 3 | The Metropolis algorithm, the special case with a symmetric proposal | Intuition | [ritvikmath, Metropolis-Hastings, 13:31 to 18:15](https://www.youtube.com/watch?v=yCv2N7wGDCw&t=811s) |
| 4 | Sampling an energy-based model with MCMC, accepting or rejecting each move | Intuition | [Stanford CS236, lecture 12, 8:35 to 16:25](https://www.youtube.com/watch?v=Nci1Bepcy0g&t=515s) |

None of these uses a Langevin step as the proposal (MALA) or reads the share of proposals accepted. Times are chapter boundaries read from each video's chapter list, not from captions, so each is good to the chapter and the sentence inside it is not checked.
<!-- /video-table -->

![Settled variance against step size with and without the accept step, and the share accepted above|800](assets/step-size-and-the-accept-step-the-concept.webp)

*The concept, settled variance against step size with and without the accept step, and the share accepted above.*

**The stability limit.** One unadjusted step multiplies an offset from the centre by $1 - \eta P$. The offset shrinks only while that factor is between $-1$ and $1$:

$$
\begin{aligned}
|1 - \eta P| < 1 \quad &\Longleftrightarrow \quad 0 < \eta < \frac{2}{P} \\
\frac{2}{P} = \frac{2}{3.25} &= 0.615385 \\
\eta = 0.6: \quad \frac{1}{3.25\,(1 - 0.6 \times 3.25 / 2)} &= \frac{1}{3.25 \times 0.025} = 12.3077
\end{aligned}
$$

*Derived.* Step 8's `step_sizes.py` printed 12.4 at 0.6 and $5.2 \times 10^{42}$ at 0.7. With the accept step the variance stayed between 0.3055 and 0.3084 from step 0.01 to 0.8. *Shown.*

**Light tails break unadjusted Langevin at every step size.** On $q \propto e^{-x^4/4}$ one step without noise is $x \mapsto x - \eta x^3 = x(1 - \eta x^2)$. It overshoots further each time once $|1 - \eta x^2| > 1$, that is once $|x| > \sqrt{2/\eta}$, which is $\sqrt{20} = 4.4721$ at step 0.1. From 5: $5 - 0.1 \times 125 = -7.5$, then 34.69, then $-4139$. *Derived*, with the sequence from `checks/ula_light_tails.out`. A Gaussian's pull grows like $x$, so one small step is safe everywhere; this pull grows like $x^3$, so every step size has a distance past which chains are lost, and the noise eventually carries some chain there: 1 in 100,000 at step 0.1. *Shown*, step 8. The paper names this case: "targets with lighter-than-Gaussian tails where the ULA chain is transient". *Cited:* `text/method.tex` line 142. The accept step rejects a proposal that lands where the target's height is tiny, so no chain leaves; the cost is chains that start far out and stay stuck, 1,317 of 100,000 at step 0.5.

**The share accepted is a dial.** On the clean product:

| Step size | Share accepted | Variance with the accept step |
|---|---|---|
| 0.01 | 99.9% | 0.3055 |
| 0.3 | 79% | 0.3081 |
| 0.5 | 60% | 0.3084 |
| 0.8 | 38% | 0.3082 |

The width is right on every row; only the share changes, and it falls as the step grows. A sampler can therefore raise its step until the share reaches a target. The paper does this, choosing the multiplier of $\beta_t$ in each level's step "so that the average acceptance rate of MALA and HMC samplers across timesteps is approximately 60% and 70% respectively". *Cited:* `text/appendix.tex` line 154. An unadjusted sampler has no such reading, because it accepts every proposal.

**Table 1 on the pair, and where its LL column misleads.** The paper's Table 1 scores samplers on its 2D toys by LL, the "log-likelihood of generated samples under composed distribution", and Var, a difference of variances. For the energy model's product it gives Var 0.064 for reverse diffusion, 0.027 for ULA, 0.022 for U-HMC, 0.013 for MALA and 0.009 for HMC, and LL $-6.03$ for reverse diffusion against 2.73 for MALA. *Cited:* `table/toy2d.tex` and `text/results.tex` line 17. The ladder in step 8 agrees on Var: reverse diffusion worst, the unadjusted samplers next, the two adjusted ones best, with MALA and HMC in the opposite order. On LL it disagrees: reverse diffusion scores highest. The mean log height under the product of samples with mean $m$ and variance $v$ is

$$
\begin{aligned}
\text{LL} &= -\tfrac12 \log(2\pi V_P) - \frac{v + (m - M_P)^2}{2 V_P} \\
\text{reverse, } m = -0.1567,\ v = 0.2102: \quad \text{LL} &= -0.329611 - \frac{0.2102 + 0.005486}{0.615385} = -0.329611 - 0.350490 = -0.680101 \\
\text{the product itself, } v = V_P,\ m = M_P: \quad \text{LL} &= -0.329611 - \tfrac12 = -0.829611
\end{aligned}
$$

with $M_P = -0.230769$ and $V_P = 0.307692$. *Derived*, using [the log](../../references/textbooks/algebra/algebra-handbook.pdf#page=110) of the Gaussian density; the printed $-0.6802$ differs in the last place because $m$ and $v$ are rounded here. LL rises as $v$ falls, so a cloud squeezed onto the product's peak beats samples of the product itself. On the paper's toys reverse diffusion leaves samples where the product has almost no height, as on the ring in Figure 2, and LL punishes that; on the pair its error is a squeeze, and LL rewards it. *Stated*: the paper does not say why its reverse row scores low. LL ranks samplers only beside a measure of width, as Table 1 sets it beside Var.

**The paper's step-size claim does not hold on the pair.** Appendix B.3 says that for the unadjusted variants "we set step sizes to be the same as adjusted samplers, and found limited gains when step sizes were specifically tuned towards the un-adjusted samplers". *Cited:* `text/appendix.tex` line 154. On the pair, at the adjusted samplers' steps, ULA ends at variance 12.1 and U-HMC at 2.96; ULA at its own step of 0.01 ends within 0.0047. Retuning is the whole difference here. *Shown*, step 8, `ladder.py`. Whether the paper's image models behave like the pair is not tested here.

> [!note]- How this was checked
> The shared setup and sources are in the box at the end of [[Diffusion Models]].
