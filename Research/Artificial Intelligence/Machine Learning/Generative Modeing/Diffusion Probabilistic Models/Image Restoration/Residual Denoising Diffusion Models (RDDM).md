**Paper:** @liuResidualDenoisingDiffusion2024
# Relation 

## **Papers By Category**

## **Textbook**

## **Tags** 

#tag1, #tag2


# 📄 **Aim:**
## **Abstract** 

This paper introduces **Residual Denoising Diffusion Models (RDDM)**, a **dual diffusion framework** that decouples **residual diffusion** from **noise diffusion** to enhance **image generation and restoration**. Unlike conventional **denoising diffusion probabilistic models (DDPMs)**, which rely on a single diffusion process, RDDM explicitly separates the **certainty-driven residual component** (which models the transformation from the target image to the degraded input) from **random perturbations** (which capture diversity). This enables **more interpretable, efficient, and versatile diffusion models** for **both image restoration and synthesis tasks**.

## **Research Statement / Question** 

Can **decoupling residual and noise diffusion** improve the interpretability and effectiveness of **image restoration and generation** compared to standard denoising diffusion models?

## **Contributions of the Paper**

- Proposes **RDDM**, a novel dual diffusion framework that explicitly models **residual transformation** (certainty) and **noise perturbation** (diversity).
- Provides **a mathematically grounded formulation** that unifies DDPM and DDIM through **coefficient transformation**.
- Introduces **a partially path-independent generation process**, improving the interpretability and control of image diffusion.
- Achieves **state-of-the-art (SOTA) performance in image restoration tasks** (e.g., **shadow removal, low-light enhancement, deraining**) while maintaining competitive performance in **image generation**.

# 📚 **Background:**

## **Background of the Paper:**  

- Standard **diffusion models** (e.g., DDPMs) focus solely on **denoising**, treating image degradation and noise as a **single process**.
- Existing **image restoration methods** use diffusion models **without modifying the original forward process**, making the restoration process **less interpretable**.
- RDDM introduces **a dual diffusion process** where the **residual component** explicitly encodes **deterministic degradation**, while **noise diffusion** accounts for randomness.

## **Background of the Method:**  
## **Limitations of Previous Work:**  

- **Standard diffusion models** treat image generation and restoration as the same process, despite their distinct needs.
- **Existing restoration diffusion models** implicitly condition on degraded images **without defining explicit transformation directions**.
- **DDPM and DDIM require large batch sizes and long sampling steps** to achieve high-quality restoration.

## **Related Work:**  
- **Score-Based Diffusion Models (SGMs):** Used for **image denoising** but lack explicit decomposition into **residual and noise**.
- **Cold Diffusion & InDI:** Attempted **non-stochastic diffusion models**, but lacked a structured **residual-based forward process**.
- **Denoising-Based Super-Resolution (SR3, DvSR):** Extended diffusion to **image restoration** but still relied on **one single diffusion process**.


# 🔧 **Method:**

#### **Input / Output**

- **Input:**
    - **Degraded image (e.g., noisy, shadowed, low-light, or blurred image)**
    - **Noise perturbation (random component)**
- **Output:**
    - **Restored image (for restoration tasks)**
    - **Generated image (for synthesis tasks)**
## **Architecture Breakdown**

- **Dual Diffusion Process:**
    - **Residual Diffusion:** Models **directional degradation** from the **target image to the input image**, encoding known transformations.
    - **Noise Diffusion:** Captures **random perturbations** that exist in the diffusion process, enhancing diversity.

- **Key Innovations:**    
    - **Decoupled Diffusion Scheduling:** Two independent schedules control **residual diffusion speed** and **noise diffusion intensity**.
    - **Partially Path-Independent Sampling:**
        - Enables **flexible modification of diffusion speed** without affecting sample quality.
        - Allows for **removing residuals before noise** or vice versa, affecting certainty and diversity trade-offs.

## **How To Train The Architecture**

- **Forward Process:**
    - Applies **simultaneous residual and noise diffusion**, progressively converting the target image into either **pure noise (for generation)** or a **degraded input image with noise (for restoration)**.
- **Reverse Process:**
    - Uses a **learned network** to predict both **residual and noise components**, guiding the reconstruction process.
- **Training Loss:**
    - **L1 Loss on residual estimation** (certainty).
    - **L2 Loss on noise estimation** (diversity).
- **Adaptive Objective Selection:**
    - Dynamically selects whether to predict **residuals, noise, or both** depending on the task.

## **How Inference Works**

- **For Image Generation:**
    - Sample noise and progressively **denoise it** while adding residuals, generating high-quality samples.
- **For Image Restoration:**
    - Remove **residual distortions first**, then **denoise the remaining artifacts**.
- **For Image Inpainting & Translation:**
    - Fill missing regions **by first predicting residuals, then refining details using noise removal**.

## **Insights:**

## **Limitations:**  


# 🧪 **Experimental Evaluation:**

## **Dataset**

## **Experiments**
- - **Compared RDDM against standard diffusion-based restoration and generation models**.
****

## **Metrics**

- **Fréchet Inception Distance (FID):** Measures image generation quality.
- **Peak Signal-to-Noise Ratio (PSNR) & Structural Similarity Index (SSIM):** Evaluate image restoration accuracy.

## **Results**

- **RDDM achieves competitive FID scores for image generation**.
- **Outperforms existing restoration diffusion models** on low-light, deraining, and shadow removal tasks.
- **Generalizes across various restoration and synthesis tasks with a single architecture.**

# 🔄Comparison to Predecessors

|**Method**|**Dual Diffusion Process?**|**Image Restoration?**|**Image Generation?**|**FID (↓)**|**PSNR (↑)**|
|---|---|---|---|---|---|
|**DDPM**|❌ No|✅ Yes|✅ Yes|**23.66**|**30.28**|
|**DDIM**|❌ No|✅ Yes|✅ Yes|**24.92**|**30.42**|
|**RDDM (Ours)**|✅ Yes|✅ Yes|✅ Yes|**22.05**|**32.51**|

- **RDDM surpasses DDPM/DDIM in restoration quality while maintaining competitive generative capabilities.**

# 📝 **Problem and Value Proposition:**
### **Problem**
- Existing diffusion models **fail to separate deterministic degradation from random noise**, making restoration **less interpretable**.
- **Current approaches require large batch sizes** and **long sampling steps**, making real-time applications impractical.

### **Value Proposition**

- **RDDM introduces an interpretable, efficient dual diffusion framework**.
- **Outperforms SOTA in image restoration tasks** while maintaining **strong generative capabilities**.

# 🔍 **Related Impactful Problems**

- **Medical Image Enhancement** (MRI noise reduction, X-ray enhancement).
- **Self-Supervised Image Restoration** (Learning from unpaired real-world degraded images).
- **AI-Assisted Image Editing** (Smart shadow removal, detail enhancement, photo restoration).
- **Physics-Based Image Simulation** (Weather-based image transformations)

# 📊Conclusion

- **RDDM redefines diffusion models** with a **dual diffusion approach**, improving interpretability and efficiency.
- **Achieves SOTA results in restoration tasks** while maintaining generative power.
- **Future Work:** Extending RDDM to **video restoration, medical imaging, and multimodal generation.**