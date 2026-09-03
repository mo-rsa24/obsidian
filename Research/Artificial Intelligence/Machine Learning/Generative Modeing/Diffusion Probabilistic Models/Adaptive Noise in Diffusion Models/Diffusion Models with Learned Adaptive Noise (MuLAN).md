**Paper:** @sahooDiffusionModelsLearned2024
# Relation 

## **Papers By Category**

## **Textbook**

## **Tags** 

#tag1, #tag2


# 📄 **Aim:**
## **Abstract** 
MuLAN (Multivariate Learned Adaptive Noise) challenges the conventional assumption that **ELBO (Evidence Lower Bound) is invariant to noise schedules** in diffusion models. By introducing a **learnable, adaptive noise process**, MuLAN improves **log-likelihood estimation, sample efficiency, and training speed**. Unlike traditional diffusion models that rely on **fixed Gaussian noise schedules**, MuLAN learns to **inject noise dynamically at different rates across different pixels** based on their structural importance. This approach leads to **better density estimation and generative modeling performance**

## **Research Statement / Question** 
- **Can diffusion models benefit from learning an adaptive noise process rather than using a fixed Gaussian schedule?**
- **Does learning a per-pixel multivariate noise schedule improve sample likelihood and efficiency?**

## **Contributions of the Paper**
✅ **Introduces MuLAN, a diffusion model with learned multivariate noise schedules** instead of fixed Gaussian noise.  
✅ **Shows that ELBO is not invariant to noise schedules**, contrary to prior assumptions.  
✅ **Proposes auxiliary latent variables** to improve density estimation and generative quality.  
✅ **Achieves state-of-the-art log-likelihood estimation** while reducing training time by **50%** on CIFAR-10 and ImageNet.
# 📚 **Background:**

## **Background of the Paper:**  
- Diffusion models use **progressive noise addition and denoising** to generate high-quality samples.
- Existing models **assume a fixed Gaussian forward process**, meaning **all pixels degrade at the same rate**.
- However, this approach **ignores structural variations** in images, potentially limiting generative performance.

## **Background of the Method:**  
- **Multivariate adaptive noise schedules** allow pixels to degrade **at different rates**, enabling **context-aware diffusion**.
- Instead of applying **global noise**, MuLAN **learns a noise function per pixel**.
- Uses **auxiliary latent variables** to improve the learned noise estimation.
## **Limitations of Previous Work:**  
❌ **Fixed noise schedules do not adapt to image content**, potentially leading to inefficient sampling.  
❌ **ELBO was previously assumed to be noise-invariant**, limiting improvements in likelihood estimation.  
❌ **Existing diffusion models require extensive training time** due to inefficient noise injection

## **Related Work:**  

📄 **Variational Diffusion Models (VDM)** – Prior work focused on **variational inference for diffusion**, but assumed **fixed schedules**.  
📄 **Blurring Diffusion Models** – Explored structured noise, but did not learn **per-pixel schedules**.  
📄 **DiffEnc (Variational Diffusion with Learned Encoder)** – Introduced auxiliary latent variables, but without multivariate noise adaptation.
# 🔧 **Method:**
## **Architecture Breakdown**

1️⃣ **Multivariate Adaptive Noise Scheduler:**

- Unlike DDPMs, which use **fixed Gaussian noise**, MuLAN learns **σt\sigma_tσt​** per pixel.
- Modeled as: $$q(xt∣x0)=N(xt;αtx0,diag(σt2))q(x_t | x_0) = \mathcal{N} (x_t; \alpha_t x_0, diag(\sigma^2_t))q(xt​∣x0​)=N(xt​;αt​x0​,diag(σt2​))$$
- This ensures that **edges, textures, and homogeneous regions degrade differently**.

2️⃣ **Auxiliary Latent Variables:**

- Introduces **latent embeddings $z$ that help reconstruct missing information**.
- This improves **sample diversity and likelihood estimation**.

3️⃣ **Context-Adaptive Noise Process:**

- The noise schedule is **conditioned on a context variable ccc**, such as:
    - Class labels.
    - Structural embeddings of the image.
    - Learned latent representations.
- Modeled as: $$q(xt∣x0,c)=N(xt;αt(c)x0,σt2(c))q(x_t | x_0, c) = \mathcal{N} (x_t; \alpha_t(c) x_0, \sigma^2_t(c))q(xt​∣x0​,c)=N(xt​;αt​(c)x0​,σt2​(c))$$

## **How To Train The Architecture**
1️⃣ **Train a standard diffusion model** but replace the **fixed noise schedule with a learnable multivariate schedule**.  
2️⃣ **Optimize ELBO** while updating the learned noise function.  
3️⃣ **Introduce auxiliary latent variables zzz** that **improve density estimation**.  
4️⃣ **Train on CIFAR-10 and ImageNet-32/64** using a combination of:

- **Reconstruction loss** for denoising.
- **Diffusion loss** to learn the optimal noise schedule.
- **Latent loss** to ensure stable encoding.
## **How Inference Works**
1️⃣ **Sample noise from the learned multivariate distribution** instead of a global Gaussian.  
2️⃣ **Use the learned adaptive noise schedule** to guide denoising.  
3️⃣ **Utilize auxiliary latent variables** to reconstruct fine details.  
4️⃣ **Generate images with better likelihood and lower computational cost.**

## **Insights:**
✅ **Learning the noise process improves ELBO and sample efficiency.**  
✅ **Multivariate noise schedules allow structure-aware denoising.**  
✅ **Auxiliary variables improve sample diversity without extra computation.**

## **Limitations:**  
❌ **Adding latent variables increases complexity**, requiring additional memory.  
❌ **The learned noise process must be tuned per dataset**, which may not generalize perfectly.


# 🧪 **Experimental Evaluation:**

## **Dataset**
✅ **CIFAR-10 (32x32)**  
✅ **ImageNet-32, ImageNet-64**
## **Experiments**
****

## **Metrics**
📊 **Bits per Dimension (BPD) – Lower is better**  
📊 **Fréchet Inception Distance (FID) – Lower is better**  
📊 **Number of Function Evaluations (NFE) – Measures efficiency**

## **Results**

|**Model**|**CIFAR-10 (BPD ↓)**|**ImageNet (BPD ↓)**|**Training Steps**|**FID ↓**|
|---|---|---|---|---|
|**VDM**|**2.65**|**3.72**|**10M**|23.91|
|**MuLAN (Ours)**|**2.55**|**3.67**|**2M**|**18.54**|
|**MuLAN (10M steps)**|**2.60**|**3.71**|**10M**|**17.62**|

✅ **New SOTA in likelihood estimation (lower BPD).**  
✅ **Reduces training time by 50% while improving density estimation.**

## **Results**


# 🔄Comparison to Predecessors
|**Model**|**Type**|**Learned Noise?**|**Multivariate Noise?**|**Context Adaptive?**|**Auxiliary Latents?**|
|---|---|---|---|---|---|
|**VDM**|Diffusion|✅ Yes|❌ No|❌ No|❌ No|
|**Blurring Diffusion**|Diffusion|❌ No|✅ Yes|❌ No|❌ No|
|**DiffEnc**|Diffusion|✅ Yes|❌ No|❌ No|✅ Yes|
|**MuLAN (Ours)**|Diffusion|✅ Yes|✅ Yes|✅ Yes|✅ Yes|

✅ **MuLAN is the first method to integrate learned noise schedules, per-pixel adaptive noise, and latent variables.**

# 📝 **Problem and Value Proposition:**
### **Problem**
- Diffusion models assume **fixed Gaussian noise schedules**, limiting generative efficiency.
- ELBO was previously **assumed to be noise-invariant**, which this work disproves.

### **Value Proposition**
✅ **Learns optimal noise schedules for improved likelihood estimation.**  
✅ **Reduces training time while increasing sample diversity.**  
✅ **Provides a theoretical foundation for optimizing diffusion processes.**

# 🔍 **Related Impactful Problems**
- Can this method **generalize to text-to-image diffusion models?**
- How does adaptive noise **affect video diffusion models?**
- Can MuLAN **replace score-based denoising?**

# 📊Conclusion
✅ **MuLAN introduces a paradigm shift by proving ELBO is noise-dependent.**  
✅ **Learning an adaptive noise schedule improves generative quality & efficiency.**  
✅ **Sets new SOTA in likelihood estimation while reducing training costs.**
