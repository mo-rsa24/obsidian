---
aliases: [two steps then induction, forward process by induction, chaining the forward steps, composing the forward steps, many steps to one jump, the one jump, shrink the old noise, why the forward steps collapse into one jump, "abar_t = prod (1 - beta_j)"]
sources:
  - "Ho, Jain, Abbeel, Denoising Diffusion Probabilistic Models, NeurIPS 2020, equations (2) and (4): https://arxiv.org/abs/2006.11239"
  - "Chan, Introduction to Probability for Data Science, PDF p. 25, the induction proof of the binomial theorem, and PDF p. 299, Theorem 5.12: ../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=25"
  - "Prince, Understanding Deep Learning, section 18.2.1, equations 18.4 to 18.7, PDF p. 366: ../../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=366"
  - "Deisenroth, Faisal, Ong, Mathematics for Machine Learning, section 6.5.3, equation 6.78, PDF p. 207: ../../../Mathematics/references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=207"
standard: vault-note v2
---

# From Many Steps To One Jump

Up: [[Diffusion Models]] · ⬅️ [[The Forward Process]] · [[Running From Many Steps To One Jump]] ➡️

Artificial Intelligence, Generative Modeling, Diffusion Models. Needs: [[The Forward Process]] for the one jump this note proves, [[The Scaling Rule For Variance#Scaling a draw scales its variance by the square|the scaling rule for variance]] for why the old noise shrinks, and [[Sums Of Independent Gaussians#Why independence kills the cross term|independent variances add]] for why the two noise pieces add.

**A hundred small forward steps collapse into one jump from the clean point.**

> [!question]- Test yourself
> [The diffusion models quiz](https://claude.ai/artifact/MyTdAaVfZW3wiqhbLKg4wu) covers the [[Diffusion Models]] folder. It has no questions on this note yet.

> [!warning]- Unfinished
> - The deep-dive sheet is waiting: prompt 36 in the vault's `.prompts/Diffusion Models.md`.
> - The diffusion models quiz has no questions on this note yet.

Stated claims: 0.

**What one step does.** Each small forward step shrinks everything already in the state by $\sqrt{1 - \beta_t}$, the old noise as well as the clean part. Then it adds fresh noise of variance $\beta_t$.

**What the steps add up to.** Two steps show the pattern, and induction carries it to every step. After steps $0$ to $t$ the state is $\sqrt{\bar\alpha_t}\,x_0$ plus noise of variance $1 - \bar\alpha_t$, with $\bar\alpha_t = \prod_{j=0}^{t}(1 - \beta_j)$. That is why a hundred small steps can be replaced by the one jump in [[The Forward Process]].

**Where it comes from.** The one step is *cited* from Ho et al., equation (2). The paper states the jump as equation (4) without the steps between, and they are *derived* below.

**How steps are counted.** Steps are counted as the rebuild's code counts them: step 0 is the first step, `betas[0]` is its noise, and `abar = np.cumprod(1 - betas)`. So $\bar\alpha_t$ multiplies the factors for steps 0 through $t$, and $\bar\alpha_0 = 1 - \beta_0 = 0.9994$ rather than 1.

**Counting from 1 instead.** Ho et al. and [[The Forward Process#One small step, fifty of them, and one jump]] count from 1. Their level 50 ($\bar\alpha = 0.4938$) is $\bar\alpha_{49}$ here, as [[Running From Many Steps To One Jump#Try the two steps yourself|step 4 of the sandbox]] prints.

**Colours in this note.** <span style="color:#00838f">**Teal is the state $s_t$**</span>, <span style="color:#1565c0">**blue is the clean point $x_0$**</span>, <span style="color:#6a1b9a">**purple is a standard normal draw $\varepsilon$**</span>, <span style="color:#2e7d32">**green is the kept signal share $\bar\alpha_t$**</span>, and <span style="color:#ef6c00">**orange is noise: its scale $\sqrt{1 - \bar\alpha_t}$ and its variance pieces**</span>. They mean the same as on the one-expert rebuild's step 4 page, where $s_t$ is the noisy point $x_t$, and as in [[The Scaling Rule For Variance]] and [[Sums Of Independent Gaussians]].

## Table of contents

- [[#Many steps collapse into one jump]]
- [[#One step, written as a recursion]]
- [[#Try the two steps yourself]]
- [[#How two steps become every step]]
- [[#Other ways to see it]]
- [[#Why the induction matters]]
- [[#The induction taught in, applied in]]

## Many steps collapse into one jump

Navigation: 📋 [[#Table of contents|TOC]] | [[#One step, written as a recursion]] ➡️

Textbook: [Understanding deep learning, section 18.2.1, the first two steps and the closed form, PDF p. 366](../../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=366)

**The one jump**, also many steps to one jump: the state after steps $0$ to $t$ is drawn straight from the clean point as $\sqrt{\bar\alpha_t}\,x_0$ plus one Gaussian noise of variance $1 - \bar\alpha_t$, with no step in between. *Derived* in [[#How two steps become every step]].

**The toy numbers.** Four steps of the 100-step cosine schedule, computed by `schedule.py` in [[Running From Many Steps To One Jump#Try the two steps yourself|the sandbox]]. Step 0 starts from the clean point, so it has no old noise to shrink.

<table>
<tr><th>step <i>t</i></th><th>β<sub><i>t</i></sub></th><th>1 − β<sub><i>t</i></sub></th><th style="color:#2e7d32">ᾱ<sub><i>t</i></sub></th><th style="color:#ef6c00">old noise, shrunk</th><th style="color:#ef6c00">fresh noise β<sub><i>t</i></sub></th><th style="color:#ef6c00">total noise 1 − ᾱ<sub><i>t</i></sub></th><th style="color:#2e7d32">signal multiplier √ᾱ<sub><i>t</i></sub></th></tr>
<tr><td>0</td><td>0.0006313</td><td>0.9993687</td><td>0.9993687</td><td>0</td><td>0.0006313</td><td>0.0006313</td><td>0.9996843</td></tr>
<tr><td>1</td><td>0.0011169</td><td>0.9988831</td><td style="border:2px solid #212121">0.9982525</td><td style="border:2px solid #212121">0.0006306</td><td>0.0011169</td><td style="border:2px solid #212121">0.0017475</td><td>0.9991</td></tr>
<tr><td>49</td><td>0.03059</td><td>0.96941</td><td style="border:2px solid #212121">0.4938</td><td>0.4756</td><td>0.0306</td><td style="border:2px solid #212121">0.5062</td><td>0.7027</td></tr>
<tr style="background:#fff8e1"><td><b>50</b></td><td>0.03155</td><td style="border:2px solid #212121"><b>0.96845</b></td><td><b>0.4783</b></td><td style="border:2px solid #212121"><b>0.4902</b></td><td style="border:2px solid #212121"><b>0.0315</b></td><td style="border:2px solid #212121"><b>0.5217</b></td><td style="border:2px solid #212121"><b>0.6916</b></td></tr>
</table>

**How to read this table.** Each row is one code step. The old noise column is the noise the state already held, times this step's 1 − β<sub>t</sub>; the fresh column is this step's own noise; the total is their sum. Green ᾱ<sub>t</sub> is the share of the clean point's variance still kept, and its square root is the multiplier on $x_0$.

**What to look for.** In every row the old and fresh noise add to exactly 1 − ᾱ<sub>t</sub>: $0.0006306 + 0.0011169 = 0.0017475$ at step 1, $0.4902 + 0.0315 = 0.5217$ at step 50. The highlighted row is the one worked by hand below, where the old noise 0.5062 of row 49 is shrunk by 0.96845.

### The base word: jump

**What the word means.** A jump goes from the clean point straight to the state after step $t$, without visiting the states between. The chain visits every one of them.

$$
\underbrace{\textcolor{#1565c0}{x_0} \to \textcolor{#00838f}{s_0} \to \textcolor{#00838f}{s_1} \to \dots \to \textcolor{#00838f}{s_t}}_{\text{the chain: } t + 1 \text{ steps}}
\qquad \text{against} \qquad
\underbrace{\textcolor{#1565c0}{x_0} \longrightarrow \textcolor{#00838f}{s_t}}_{\text{the jump}}
$$

**What it means.** At $t = 50$ the chain takes 51 steps, each with its own draw. [[Running From Many Steps To One Jump#Try the two steps yourself|Step 7 of the sandbox]] runs those 51 steps 200,000 times and lands on mean 0.6924 and variance 0.5207, beside the jump's 0.6916 and 0.5217.

### The qualifier: one

**What the word means.** One draw replaces every step's noise. The $t + 1$ fresh draws stack into noise of total variance $1 - \bar\alpha_t$, and [[Sums Of Independent Gaussians#How the rule works|a sum of independent Gaussians]] is one Gaussian of that variance.

$$
\underbrace{\text{the noise built from } \textcolor{#6a1b9a}{\varepsilon_0}, \dots, \textcolor{#6a1b9a}{\varepsilon_t}}_{t + 1 \text{ independent pieces}}
\;\;\overset{\text{same distribution}}{=}\;\;
\underbrace{\textcolor{#ef6c00}{\sqrt{1 - \bar\alpha_t}}\;\textcolor{#6a1b9a}{\varepsilon}}_{\text{one draw}}
$$

**What it means.** At $t = 50$ the 51 pieces have total variance 0.5217, so one draw times $\sqrt{0.5217} = 0.7223$ carries all of them. [[The Density Of The One Jump]] calls this the one-shot draw and writes its density.

### All the words together: the formula

$$
s_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon, \qquad \bar\alpha_t = \prod_{j=0}^{t} (1 - \beta_j)
$$

$$
\underbrace{\textcolor{#00838f}{s_t}}_{\text{after steps } 0 \text{ to } t}
=
\underbrace{\sqrt{\textcolor{#2e7d32}{\bar\alpha_t}}\,\textcolor{#1565c0}{x_0}}_{\text{kept clean signal}}
+
\underbrace{\textcolor{#ef6c00}{\sqrt{1 - \bar\alpha_t}}\,\textcolor{#6a1b9a}{\varepsilon}}_{\text{every step's noise as one draw}},
\qquad
\textcolor{#2e7d32}{\bar\alpha_t} = \underbrace{\prod_{j=0}^{t} (1 - \beta_j)}_{\text{every kept share, multiplied}}
$$

**What the equation says.** The state after steps $0$ to $t$ is the clean point scaled by $\sqrt{\bar\alpha_t}$ plus one noise draw scaled by $\sqrt{1 - \bar\alpha_t}$. At $t = 50$ that is $0.6916\,x_0 + 0.7223\,\varepsilon$.

### The consequence: training reaches any step in one line

$$
\underbrace{\frac{1}{100} \sum_{t=0}^{99} (t + 1)}_{\text{steps per training pair, as a chain}} = 50.5
\qquad \text{against} \qquad
\underbrace{1}_{\text{the jump}}
$$

**What it means.** The rebuild picks each training pair's step at random from 0 to 99 (`torch.randint(0, self.n_steps, ...)`, `rebuild/model.py` line 111), so a chain would cost 50.5 steps per pair on average. The jump makes the pair in one line, `xt = np.sqrt(abar[t]) * x0 + np.sqrt(1 - abar[t]) * eps` in step 4 of the rebuild walk (line 108 of `rebuild/model.py` in torch form).

## One step, written as a recursion

Navigation: ⬅️ [[#Many steps collapse into one jump]] | 📋 [[#Table of contents|TOC]] | [[#Try the two steps yourself]] ➡️

**One forward step**, also the recursion: write the state after step $t$ as $s_t$, with $s_t = \sqrt{1 - \beta_t}\,s_{t-1} + \sqrt{\beta_t}\,\varepsilon_t$ and $\varepsilon_t$ a fresh standard normal draw independent of everything before it. *Cited* from Ho et al., equation (2).

**Where it starts.** $x_0$ is the clean point and step 0 starts from it. Track the clean part and the noise variance separately, and each step updates them like this:

$$
\begin{aligned}
s_t &= \sqrt{1 - \beta_t}\,s_{t-1} + \sqrt{\beta_t}\,\varepsilon_t \\
\text{signal}_t &= \sqrt{1 - \beta_t}\;\text{signal}_{t-1} \\
\text{noise}_t &= (1 - \beta_t)\,\text{noise}_{t-1} + \beta_t \\
\text{result: } \text{signal}_t &= \sqrt{\bar\alpha_t}, \quad \text{noise}_t = 1 - \bar\alpha_t, \quad \bar\alpha_t = (1 - \beta_0)(1 - \beta_1) \cdots (1 - \beta_t)
\end{aligned}
$$

$$
\begin{aligned}
\underbrace{\textcolor{#00838f}{s_t}}_{\text{state after step } t}
&=
\underbrace{\sqrt{1 - \beta_t}}_{\text{shrink}}\;
\underbrace{\textcolor{#00838f}{s_{t-1}}}_{\text{everything already present}}
+
\underbrace{\sqrt{\beta_t}\,\textcolor{#6a1b9a}{\varepsilon_t}}_{\text{fresh noise, variance } \beta_t} \\
\underbrace{\text{signal}_t}_{\text{multiplier on } x_0}
&=
\underbrace{\sqrt{1 - \beta_t}}_{\text{shrunk once more}}\;\text{signal}_{t-1} \\
\underbrace{\textcolor{#ef6c00}{\text{noise}_t}}_{\text{noise variance}}
&=
\underbrace{(1 - \beta_t)\,\textcolor{#ef6c00}{\text{noise}_{t-1}}}_{\text{old noise, shrunk by the square}}
+
\underbrace{\beta_t}_{\text{fresh variance}}
\end{aligned}
$$

**What the equation says.** One step shrinks the whole old state, clean part and old noise alike, then adds a fresh independent draw. Tracked separately, the multiplier on $x_0$ shrinks by $\sqrt{1 - \beta_t}$ and the noise variance by $1 - \beta_t$, the square of that multiplier, by [[The Scaling Rule For Variance#Scaling a draw scales its variance by the square|the scaling rule]].

**Why the shrink on the old state is there.** It keeps signal plus noise at 1. At step 50 the old noise 0.5062 shrinks to 0.4902, and with the fresh 0.0315 the noise is 0.5217 beside the signal share 0.4783; without the shrink the noise is $0.5062 + 0.0315 = 0.5377$ and the total 1.0160.

**Why the square roots are there.** The coefficients multiply draws, so their squares set the variances. At step 50, $\sqrt{\beta_{50}} = 0.1776$ gives fresh variance 0.0315, while $\beta_{50}$ itself as the coefficient would give $0.03155^2 = 0.000995$, about 32 times too little. Likewise $1 - \beta_{50} = 0.96845$ as the shrink would scale the variance by $0.96845^2 = 0.9379$ and leave the total at 0.9694.

```python
import matplotlib.pyplot as plt

SIG, OLD, FRESH = "#2e7d32", "#ef6c00", "#ffcc80"
abar49, beta50 = 0.4938436, 0.0315463           # step 49's kept share, step 50's beta
keep = 1 - beta50                                # 0.96845, the shrink as a variance factor
bars = [("before: s_49", abar49, 1 - abar49, 0.0, "old noise"),
        ("both shrunk", keep * abar49, keep * (1 - abar49), 0.0, "old noise,\nshrunk"),
        ("after: s_50", keep * abar49, keep * (1 - abar49), beta50, "old noise,\nshrunk")]
fig, ax = plt.subplots(figsize=(10, 5.6))
for x, (name, sig, old, fresh, word) in enumerate(bars):
    ax.bar(x, sig, 0.5, color=SIG)
    ax.bar(x, old, 0.5, bottom=sig, color=OLD)
    ax.text(x, sig / 2, f"signal\n{sig:.4f}", ha="center", va="center", color="white", fontsize=12)
    ax.text(x, sig + old / 2, f"{word}\n{old:.4f}", ha="center", va="center", color="white", fontsize=12)
    if fresh:
        ax.bar(x, fresh, 0.5, bottom=sig + old, color=FRESH, ec=OLD)
        ax.text(x + 0.28, sig + old + fresh / 2, f"fresh noise\nβ₅₀ = {fresh:.4f}", va="center", fontsize=11)
ax.bar(1, beta50, 0.5, bottom=keep, fill=False, ls="--", ec="#757575")
ax.text(1.28, keep + beta50 / 2, f"gap {beta50:.4f}", va="center", color="#757575", fontsize=11)
ax.annotate("", (0.72, 0.62), (0.28, 0.62), arrowprops=dict(arrowstyle="->", lw=2))
ax.text(0.5, 0.66, f"× (1 − β₅₀)\n= {keep:.5f}", ha="center", fontsize=11)
ax.axhline(1, color="#424242", ls=":", lw=1)
ax.text(-0.45, 1.015, "total 1", fontsize=11)
ax.set_xticks(range(3), [b[0] for b in bars], fontsize=12)
ax.set_ylabel("share of the state's variance", fontsize=11)
ax.set_ylim(0, 1.12); ax.set_xlim(-0.5, 2.85)
ax.set_title("one step, t = 50: s_50 = √(1 − β₅₀) s_49 + √β₅₀ ε₅₀", fontsize=12)
fig.savefig("forward-induction-one-step-at-step-50.svg", format="svg", bbox_inches="tight")
```

![Three stacked bars for step 50: before, green signal 0.4938 under orange old noise 0.5062 reaching the dotted line at 1; both shrunk by 0.96845 to 0.4783 and 0.4902, leaving a dashed gap of 0.0315; after, the light orange fresh noise 0.0315 fills the gap back to 1|800](assets/forward-induction-one-step-at-step-50.svg)

**How to read this.** The y-axis is the share of the state's variance and each bar is one moment of step 50: green is the signal share, orange the old noise, light orange the fresh noise. Both lower segments shrink by the same 0.96845 between the first and second bars, which opens a gap of 0.0315 under the dotted line at 1. The fresh noise fills exactly that gap, so the third bar reaches 1 again.

## Try the two steps yourself

Navigation: ⬅️ [[#One step, written as a recursion]] | 📋 [[#Table of contents|TOC]] | [[#How two steps become every step]] ➡️

**In two lines.** Nine steps in an empty folder, from the cosine schedule to the forgotten shrink, two steps by hand, the recursion at all 100 steps and 200,000 drawn chains, each with its output read field by field, are in [[Running From Many Steps To One Jump#Try the two steps yourself]]. The steps this note cites by number (4, 5, 6 and 7) are the look at the schedule, the forgotten shrink, the two steps with the recursion, and the drawn chains there.

## How two steps become every step

Navigation: ⬅️ [[#Try the two steps yourself]] | 📋 [[#Table of contents|TOC]] | [[#Other ways to see it]] ➡️

Textbook: [Chan, Introduction to Probability for Data Science, an induction proof worked in full, PDF p. 25](../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=25) · [Understanding deep learning, the same two steps as equations 18.4 to 18.6, PDF p. 366](../../../Mathematics/references/textbooks/machine-learning/understanding-deep-learning.pdf#page=366)

**Two steps from any state $z$.** Put one step inside the next:

$$
\begin{aligned}
s_{j} &= \sqrt{1-\beta_j}\,z + \sqrt{\beta_j}\,\varepsilon_j \\
s_{j+1} &= \sqrt{1-\beta_{j+1}}\,\big[\sqrt{1-\beta_j}\,z + \sqrt{\beta_j}\,\varepsilon_j\big] + \sqrt{\beta_{j+1}}\,\varepsilon_{j+1} \\
&= \sqrt{(1-\beta_{j+1})(1-\beta_j)}\,z + \sqrt{(1-\beta_{j+1})\,\beta_j}\;\varepsilon_j + \sqrt{\beta_{j+1}}\;\varepsilon_{j+1}
\end{aligned}
$$

$$
\begin{aligned}
\textcolor{#00838f}{s_{j+1}}
&= \sqrt{1-\beta_{j+1}}\,\Big[\sqrt{1-\beta_j}\,z + \sqrt{\beta_j}\,\textcolor{#6a1b9a}{\varepsilon_j}\Big] + \sqrt{\beta_{j+1}}\,\textcolor{#6a1b9a}{\varepsilon_{j+1}}
&& \text{substitute step } j \\
&= \underbrace{\sqrt{(1-\beta_{j+1})(1-\beta_j)}}_{\text{signal multiplier: both kept shares}}\,z
 + \underbrace{\sqrt{(1-\beta_{j+1})\,\beta_j}\;\textcolor{#6a1b9a}{\varepsilon_j}}_{\text{old noise, shrunk}}
 + \underbrace{\sqrt{\beta_{j+1}}\;\textcolor{#6a1b9a}{\varepsilon_{j+1}}}_{\text{fresh noise}}
&& \text{multiply out}
\end{aligned}
$$

**What the equation says.** Two steps scale the starting state by both shrinks at once and leave two noise pieces. The first piece is step $j$'s noise, shrunk again by step $j + 1$; the second is step $j + 1$'s fresh draw.

**The noise variance.** The old noise piece has variance $(1-\beta_{j+1})\,\beta_j$ by [[The Scaling Rule For Variance#Scaling a draw scales its variance by the square|the scaling rule]], and the fresh piece has variance $\beta_{j+1}$. $\varepsilon_j$ and $\varepsilon_{j+1}$ are independent, so [[Sums Of Independent Gaussians#Why independence kills the cross term|the variances add]] and the sum is again Gaussian:

$$
\begin{aligned}
\textcolor{#ef6c00}{\text{noise variance}}
&= \underbrace{(1-\beta_{j+1})\,\beta_j}_{\text{old noise kept through step } j+1} + \underbrace{\beta_{j+1}}_{\text{fresh noise}} \\
&= \beta_j + \beta_{j+1} - \beta_j\,\beta_{j+1} && \text{multiply out} \\
&= \underbrace{1 - \textcolor{#2e7d32}{(1-\beta_j)(1-\beta_{j+1})}}_{\text{one minus the two-step signal share}} && \text{since } (1-\beta_j)(1-\beta_{j+1}) = 1 - \beta_j - \beta_{j+1} + \beta_j\beta_{j+1}
\end{aligned}
$$

**What the equation says.** Two steps are one step with keep-factor $(1-\beta_j)(1-\beta_{j+1})$: the signal multiplier is its square root and the noise variance is one minus it. On steps 0 and 1 the middle line reads $0.0017482 - 0.0000007 = 0.0017475$.

**Why the product is there.** The clean signal has to survive both steps, so the kept shares multiply. At step 50 this step keeps 0.96845 of what it receives, and the product over all 51 steps is $\bar\alpha_{50} = 0.4783$; keeping only this step's share would leave a signal share of 0.96845, as if steps 0 to 49 never ran.

**Why the sum is there.** Independent noise from different steps carries separate variance, and both pieces survive. At step 50, dropping the shrunk old noise 0.4902 leaves noise 0.0315 and a total of 0.5098; dropping the fresh 0.0315 leaves 0.4902 and a total of 0.9685.

**Why the complement is there.** The signal share and the noise variance must add to 1. With the complement the noise at step 50 is $1 - 0.4783 = 0.5217$; writing the product itself as the noise would give 0.4783 to both and a total of 0.9565.

**Two steps on the schedule: steps 0 and 1.**

$$
\begin{aligned}
\textcolor{#ef6c00}{\text{noise}}
&= \underbrace{0.9988831 \times 0.0006313}_{\text{step-0 noise, shrunk by step 1}} + \underbrace{0.0011169}_{\text{fresh}}
= 0.0006306 + 0.0011169 = 0.0017475 = 1 - \textcolor{#2e7d32}{\bar\alpha_1} \\
\textcolor{#2e7d32}{\bar\alpha_1} &= \underbrace{(1 - 0.0006313)(1 - 0.0011169)}_{\text{both kept shares}} = 0.9982525,
\qquad \text{signal: } \sqrt{0.9982525} = 0.9991
\end{aligned}
$$

**What the equation says.** After two steps the noise variance is 0.0017475, exactly one minus the kept share 0.9982525. The signal multiplier is $\sqrt{0.9982525} = 0.9991$, so the point is still almost clean.

**Two steps on the schedule: step 50.** Here $\bar\alpha_{49} = 0.4938$, so the old noise has variance 0.5062, and $\beta_{50} = 0.03155$:

$$
\begin{aligned}
\textcolor{#ef6c00}{\text{noise}}
&= \underbrace{0.96845 \times 0.5062}_{\text{old noise, shrunk}} + \underbrace{0.0315}_{\text{fresh}} = 0.4902 + 0.0315 = 0.5217 = 1 - \textcolor{#2e7d32}{\bar\alpha_{50}} \\
\text{signal} &= \underbrace{\sqrt{0.96845 \times \textcolor{#2e7d32}{0.4938}}}_{\text{signal multiplier}} = \sqrt{\textcolor{#2e7d32}{0.4783}} = 0.6916
\end{aligned}
$$

**What the equation says.** In the middle of the schedule the same two lines hold, with the whole earlier product 0.4938 in place of one kept share. The old noise shrinks from 0.5062 to 0.4902 and the fresh 0.0315 tops it up to 0.5217.

**The typical misses.** The standard deviations are $\sqrt{0.4902} = 0.7001$ for the old noise and $\sqrt{0.0315} = 0.1776$ for the fresh, and they combine to $\sqrt{0.5217} = 0.7223$; adding them would wrongly give 0.8777. [[Running From Many Steps To One Jump#Reading the two-step output]] reads them as field 7 and draws them as a right triangle.

**The broken run.** Leave the old noise unshrunk at step 50 and the noise is $0.5062 + 0.0315 = 0.5377$, so unit-variance data comes out with total variance $0.4783 + 0.5377 = 1.0160$. Make the same slip at every step and the noise becomes the plain sum of the $\beta$ values, which passes 1 and keeps climbing: $1.2085$ at $t = 50$ and $7.8789$ at $t = 99$, as [[Running From Many Steps To One Jump#Try the two steps yourself|step 5 of the sandbox]] printed.

**Every step, by induction.** The claim for step $t$:

$$
s_t = \sqrt{\bar\alpha_t}\,x_0 + n_t, \qquad n_t \text{ Gaussian with mean } 0 \text{ and variance } 1 - \bar\alpha_t, \qquad \bar\alpha_t = \prod_{j=0}^{t}(1 - \beta_j)
$$

$$
\underbrace{\textcolor{#00838f}{s_t}}_{\text{state after code step } t}
=
\underbrace{\sqrt{\textcolor{#2e7d32}{\bar\alpha_t}}\,\textcolor{#1565c0}{x_0}}_{\text{kept clean signal}}
+
\underbrace{\textcolor{#ef6c00}{n_t}}_{\text{built only from } \varepsilon_0, \dots, \varepsilon_t}
$$

**What the claim says.** The state is the clean point times one number, plus noise made only from the draws of steps 0 to $t$. The proof shows the first case, then shows that one more step keeps the claim true.

**First case, $t = 0$.** $s_0 = \sqrt{1-\beta_0}\,x_0 + \sqrt{\beta_0}\,\varepsilon_0$. Here $\bar\alpha_0 = 1 - \beta_0$, so the multiplier is $\sqrt{\bar\alpha_0}$ and the noise variance $\beta_0 = 1 - \bar\alpha_0$; on the schedule that is $\bar\alpha_0 = 1 - 0.000631 = 0.9994$ with noise variance 0.000631.

**From $t - 1$ to $t$.** Assume the claim at $t - 1$ and take one more step. $\varepsilon_t$ is fresh, so it is independent of $n_{t-1}$:

$$
\begin{aligned}
\textcolor{#00838f}{s_t} &= \sqrt{1-\beta_t}\,\big[\sqrt{\textcolor{#2e7d32}{\bar\alpha_{t-1}}}\,\textcolor{#1565c0}{x_0} + n_{t-1}\big] + \sqrt{\beta_t}\,\textcolor{#6a1b9a}{\varepsilon_t} \\
\text{signal: }&
\underbrace{\sqrt{1-\beta_t}}_{\text{this step's shrink}} \cdot \underbrace{\sqrt{\textcolor{#2e7d32}{\bar\alpha_{t-1}}}}_{\text{signal so far}}
= \sqrt{(1-\beta_t)\,\textcolor{#2e7d32}{\bar\alpha_{t-1}}}
= \sqrt{\textcolor{#2e7d32}{\bar\alpha_t}} \\
\text{noise: }&
\underbrace{(1-\beta_t)(1-\textcolor{#2e7d32}{\bar\alpha_{t-1}})}_{\text{old noise, shrunk}} + \underbrace{\beta_t}_{\text{fresh}}
= 1 - (1-\beta_t)\,\textcolor{#2e7d32}{\bar\alpha_{t-1}}
= 1 - \textcolor{#2e7d32}{\bar\alpha_t}
\end{aligned}
$$

**What the equation says.** One more step multiplies the signal by its shrink, and the product of kept shares gains one factor. The noise line is the two-step algebra again, with $\bar\alpha_{t-1}$ in place of $1 - \beta_j$, and the steps 0 and 1 numbers are this move at $t = 1$: $(1 - 0.0011169) \times 0.9993687 = 0.9982525$.

**The middle equality.** The same expansion as the two-step case gives it: $(1-\beta_t)(1-\bar\alpha_{t-1}) + \beta_t = 1 - \bar\alpha_{t-1} + \beta_t\,\bar\alpha_{t-1}$. The claim holds at $t$, so it holds at every step.

$$
\boxed{
\underbrace{\textcolor{#00838f}{s_t}}_{\text{after } t + 1 \text{ small steps}}
=
\sqrt{\textcolor{#2e7d32}{\bar\alpha_t}}\,\textcolor{#1565c0}{x_0}
+
\text{noise of variance } 1 - \textcolor{#2e7d32}{\bar\alpha_t}
}
$$

```python
import numpy as np
import matplotlib.pyplot as plt

SIG, NOISE, GHOST = "#2e7d32", "#ef6c00", "#757575"
def cosine_beta_schedule(timesteps, s=0.008):            # as in rebuild/model.py
    x = np.linspace(0, timesteps, timesteps + 1, dtype=np.float64)
    ac = np.cos(((x / timesteps) + s) / (1 + s) * np.pi * 0.5) ** 2
    ac = ac / ac[0]
    return np.clip(1 - ac[1:] / ac[:-1], 0, 0.999)
betas = cosine_beta_schedule(100)
abar = np.cumprod(1 - betas)
t = np.arange(100)
fig, (left, right) = plt.subplots(1, 2, figsize=(13, 5))
left.fill_between(t, 0, abar, color="#a5d6a7")
left.fill_between(t, abar, 1, color="#ffcc80")
left.plot(t, abar, color=SIG, lw=2)
for m, dx, ha in [(0, 3, "left"), (25, 3, "left"), (49, -3, "right"), (50, 3, "left"), (75, 3, "left"), (99, -3, "right")]:
    left.plot(m, abar[m], "o", color=SIG)
    left.text(m + dx, abar[m] + (0.04 if m == 99 else 0), f"t = {m}: {abar[m]:.4f}", ha=ha, va="center",
              fontsize=10, bbox=dict(fc="white", ec="none", pad=1))
left.text(5, 0.3, "signal share ᾱ_t", color=SIG, fontsize=12)
left.text(55, 0.8, "noise share 1 − ᾱ_t", color="#e65100", fontsize=12)
left.set_title("shrink kept: the two shares always fill 1", fontsize=12)
left.set_ylim(0, 1.05); left.set_ylabel("share of the variance", fontsize=11)
forgot = abar + np.cumsum(betas)                         # old noise never shrunk
right.plot(t, np.ones(100), color=NOISE, lw=2.5)
right.text(60, 0.45, "shrink kept: total 1", color=NOISE, fontsize=11)
right.plot(t, forgot, color=GHOST, lw=2.5, ls="--")
for m in (50, 99):
    right.plot(m, forgot[m], "o", color=GHOST)
    right.text(m - 2, forgot[m] + 0.25, f"t = {m}: total {forgot[m]:.4f}", ha="right", color=GHOST, fontsize=11)
right.text(5, 3.0, "shrink forgotten:\ntotal = ᾱ_t + β_0 + … + β_t", color=GHOST, fontsize=11)
right.set_title("shrink forgotten: the total climbs past 1", fontsize=12)
right.set_ylim(0, 8.6); right.set_ylabel("signal share + noise variance", fontsize=11)
for ax in (left, right):
    ax.set_xlabel("code step t of the 100-step cosine schedule", fontsize=11)
fig.savefig("forward-induction-shares-at-every-step.svg", format="svg", bbox_inches="tight")
```

![Left, the green signal share falling from 0.9994 to 0 under the orange noise share, the two always filling 1, marked at t = 0, 25, 49, 50, 75 and 99 with 0.9994, 0.8356, 0.4938, 0.4783, 0.1335 and 0.0000; right, the orange total held at 1 beside the grey dashed total with the shrink forgotten, 1.2085 at t = 50 and 7.8789 at t = 99|850](assets/forward-induction-shares-at-every-step.svg)

**How to read this.** Both x-axes are the code step $t$ of the 100-step cosine schedule. On the left the green area is the signal share $\bar\alpha_t$ and the orange area above it the noise share $1 - \bar\alpha_t$, so every vertical slice is exactly 1 tall; the dots are the six steps the table and the old drawn prompt used. On the right the y-axis is signal share plus noise variance: the orange line stays at 1 with the shrink, and the grey dashed line, with the old noise never shrunk, reaches 1.2085 at $t = 50$ and 7.8789 at $t = 99$.

**The stack is one draw.** The induction leaves the noise as a stack of independent pieces whose variance totals $1 - \bar\alpha_t$. [[Sums Of Independent Gaussians#How the rule works|A sum of independent Gaussians]] is itself a Gaussian ([Chan's Theorem 5.12, PDF p. 299](../../../Mathematics/references/textbooks/statistics/introduction-to-probability-for-data-science.pdf#page=299), and [Mathematics for machine learning, equation 6.78, PDF p. 207](../../../Mathematics/references/textbooks/machine-learning/mathematics-for-machine-learning.pdf#page=207)), so the scaling rule run backwards writes the stack as one standard normal draw times its standard deviation:

$$
\boxed{
\underbrace{\textcolor{#00838f}{x_t}}_{\text{the one jump}}
=
\underbrace{\sqrt{\textcolor{#2e7d32}{\bar\alpha_t}}\,\textcolor{#1565c0}{x_0}}_{\text{kept clean signal}}
+
\underbrace{\textcolor{#ef6c00}{\sqrt{1 - \bar\alpha_t}}\,\textcolor{#6a1b9a}{\varepsilon}}_{\text{the whole stack as one draw}}
}
$$

**What the equation says.** The state after $t + 1$ small steps has the same distribution as the clean point scaled once plus one scaled draw. [[The Density Of The One Jump#The one-shot draw and its density]] turns it into the density $q(x_t \mid x_0)$.

*🖼️ Diagram wanted: the deep-dive sheet composing the form, the mechanism and step 6's run. Prompt 36 in the vault's `.prompts/Diffusion Models.md`.*

## Other ways to see it

Navigation: ⬅️ [[#How two steps become every step]] | 📋 [[#Table of contents|TOC]] | [[#Why the induction matters]] ➡️

**Draw it.** [[Running From Many Steps To One Jump#Try the two steps yourself|Step 7 of the sandbox]] pushes 200,000 copies of the clean point through 51 steps, for when you want to see the distribution itself rather than its two numbers. It costs 200,000 × 51 draws and agrees only to sampling error.

**The fifty-step chain in NumPy.** [[The Forward Process#One small step, fifty of them, and one jump|The forward process note]] compares a whole cloud after 50 small steps against one jump, counted from 1.

**Telescoping the cosine schedule.** For [[The Cosine Noise Schedule#The boundary values C_k|the cosine schedule]] each $1 - \beta_j$ is a ratio $C_{j+1}/C_j$ of consecutive boundary values, so the product cancels to $\bar\alpha_t = C_{t+1}$ while no $\beta$ is clipped. That shortcut is specific to the cosine schedule; the induction holds for any schedule.

## Why the induction matters

Navigation: ⬅️ [[#Other ways to see it]] | 📋 [[#Table of contents|TOC]] | [[#The induction taught in, applied in]] ➡️

**One jump instead of a hundred steps.** The induction turns a hundred small steps into one jump with signal $\sqrt{\bar\alpha_t}$ and noise variance $1 - \bar\alpha_t$.

**What the next rung does with it.** [[The Density Of The One Jump#The one-shot draw and its density|The next rung]] writes that jump as one Gaussian draw and its density $q(x_t \mid x_0)$. That is how training makes a noised point at any step in one line instead of running every step before it.

## The induction taught in, applied in

Navigation: ⬅️ [[#Why the induction matters]] | 📋 [[#Table of contents|TOC]]

**Taught in:**

- the PoE derivation foundations journey's [plan 09](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/plans/09-the-forward-process.md), instruction 3 at lines 232 to 288 (substitute $x_1$ into $x_2$, check the noise variance is 0.28 both ways for $\alpha_1 = 0.9$ and $\alpha_2 = 0.8$, then continue to $x_4$ and name the pattern), and its [chapter 9.2 on the one-jump form](/home/molef/goal-setting/learning/deep-learning/diffusion-models/01-poe-derivation-foundations/textbook/09-the-forward-process-by-hand.md#92-reading-the-image-ladder-and-the-one-jump-form)
- the `drip --math` walk of the forward process and the score in the reduce-reuse-recycle research repository (`artifacts/drips/forward-process-and-the-score/`), piece 1, rung 3: two steps from a state $z$, then induction, worked at steps 0 and 1 and at step 50, with the unshrunk old noise as the broken run

**Applied in:** step 4 of the one-expert rebuild walk in the reduce-reuse-recycle research repository (`artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step-4-the-forward-process-and-the-cosine-schedule`), whose line `abar = np.cumprod(1 - betas)` is [the product this note proves](../../../../PhD/reduce-reuse-recycle/artifacts/drips/simple-distributions-rebuild/01-one-expert-from-scratch.md#step4-two-steps-then-every-step), so the training pairs for one diffusion expert can be made at any of the 100 steps in one line.

> [!note]- How this was checked
> Every number in the toy table, the derivation and the worked numbers matches the outputs of the scripts in [[Running From Many Steps To One Jump]], re-run byte for byte on 2026-10-21 on mscluster (Linux) with Python 3.12.10 in an empty `~/playground/sandbox/forward-induction`. The table's rows and the with-and-without moves (0.000995, 0.9379 and 0.9694, 0.5098, 0.9685, 0.9565, 50.5) were computed that day by a throwaway script on the same `schedule.py`.
>
> The three figure scripts were run on 2026-10-21 on mscluster with Python 3.12.10, matplotlib 3.10.8 and numpy 2.4.3 in that folder, by vault-writer, and each SVG was opened (rendered to PNG by PyMuPDF 1.27.2) before filing. The figures replace drawn prompts 34 (the form) and 35 (the mechanism) in `.prompts/Diffusion Models.md`, whose faithfulness notes asked for bar heights to scale. The prepared environment `~/.vault-sandbox` is missing on this machine; the system `python3` has matplotlib and numpy and drew the figures.
>
> The rebuild's training step choice and one-line draw are `rebuild/model.py` lines 111 and 108, and the NumPy line is step 4 of `01-one-expert-from-scratch.md` in the reduce-reuse-recycle repository, read on 2026-10-21.
>
> Ho et al.'s equations (2) and (4) were read from the arXiv PDF of 2006.11239, page 2, fetched on 2026-10-21. Chan's PDF pp. 25 and 299, Understanding deep learning's PDF p. 366 and Mathematics for machine learning's PDF p. 207 were opened in the vault's shelf copies and read as text on 2026-10-21: p. 25 proves the binomial theorem by induction with the base case, the assumption at $n$ and the case $n + 1$; p. 366 works $z_1$ and $z_2$ and states $z_t = \sqrt{\alpha_t}\,x + \sqrt{1 - \alpha_t}\,\epsilon$; p. 299 states Theorem 5.12; p. 207 states equation 6.78. No shelf book has a page teaching product notation $\prod$, so it carries no link.
