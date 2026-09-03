**Paper:** @miaoTrainingDiffusionModels2024
# Relation 

## Papers By Category

## Textbook

## Tags 

#tag1, #tag2


# 📄 **Aim:**
## Abstract 
Diffusion models have achieved **state-of-the-art performance** in **image generation**, but they **amplify biases present in training data**, leading to **limited diversity** in generated images. This paper proposes a **reinforcement learning (RL)-based fine-tuning framework** to improve **image diversity** by using a novel **Diversity Reward** function. This reward function measures the discrepancy between the **generated image distribution** and a **reference distribution** of diverse images.

## Research Statement / Question 
Can **reinforcement learning** be used to fine-tune diffusion models to **generate more diverse images** while maintaining visual quality?

## Contributions of the Paper4
Demonstrates the effectiveness of the approach **on multiple datasets**, including **ImageNet, CIFAR-10, CIFAR-100, and StableDiffusion text-to-image models**.

# 📚 **Background:**

## **Background of the Paper:**  
- Diffusion models (e.g., **StableDiffusion, Imagen**) have revolutionized generative modeling but often **exhibit biases**—such as **overrepresenting certain demographics** in text-to-image tasks.
- **Class-conditional models** suffer from **mode collapse**, generating **highly uniform images** when conditioned on certain labels.
- Existing methods to mitigate bias include **re-weighted loss functions** and **classifier-based guidance**, but these approaches often lack generalizability

## **Background of the Method:**  
- **Diffusion Models (DDPMs):** Gradually add noise to an image and learn to reverse this process to reconstruct images.
- **Reinforcement Learning (RL):** A decision-making framework where a model **learns by receiving rewards** for desirable outcomes.
## **Limitations of Previous Work:**  
- Prior techniques **only modify training data or use hand-crafted loss functions**.
- Previous methods **cannot generalize across different diffusion models**
## **Related Work:**  
- **Debiasing in GANs:** Prior methods applied **loss re-weighting** to generative adversarial networks (GANs).
- **Reinforcement Learning for Generative Models:** RL has been applied to **text-to-image alignment** but not for **diversity improvement** in diffusion models.


# 🔧 **Method:**

## **Contribution:**  

## **Architecture Breakdown**
### Diversity Reward Function
- Measures the **distribution gap** between generated and reference images using **Maximum Mean Discrepancy (MMD)**.
- Uses **mutual information** to capture **feature space similarities** between generated and reference images.
- Assigns an **individual reward per image** based on its contribution to diversity.
### RL Fine-Tuning Process
- Reformulates **image generation as a Markov Decision Process (MDP)**.
- Trains the diffusion model to **maximize Diversity Reward** using **policy gradient methods**.
## **How To Train The Architecture**
- **Pre-train a diffusion model** on a **large dataset**.
- **Select a diverse reference dataset** for the fine-tuning process.
- **Use RL fine-tuning**:
    - Generate **multiple image samples**.
    - Compute **Diversity Reward** based on similarity to **reference distribution**.
    - **Adjust model parameters** to maximize diversity while preserving visual quality.
## **Insights:**

## **Novelty:**  

## **Limitations:**  

## **Results:**


# 🧪 **Experimental Evaluation:**

## Dataset

## Experiments
- **Post-Sampling Selection Task:**
    - Selects the **most diverse subset of generated images** based on **Diversity Reward**.
- **Class-Conditional Image Generation:**
    - Evaluates **whether RL fine-tuning improves diversity**.
- **Text-Conditional Image Generation:**
    - Tests improvements in **StableDiffusion** on **face generation tasks**.
## Results
- **RL Fine-tuning improved recall (diversity) while preserving FID (image quality).**
- **StableDiffusion fine-tuned with RL generated more balanced gender distributions.**

# 🔄Comparison to Predecessors
|**Method**|**Diversity Reward?**|**FID (↓)**|**Recall (↑)**|**KL Divergence (↓)**|
|---|---|---|---|---|
|**Baseline (No RL)**|❌ No|**24.49**|**36.15**|**0.578**|
|**Re-weighted Loss**|❌ No|**23.00**|**40.35**|**0.423**|
|**Classifier-Based Guidance**|❌ No|**22.31**|**46.31**|**0.371**|
|**Our RL Fine-Tuning**|✅ Yes|**20.48**|**49.30**|**0.272**|

- RL fine-tuning **outperforms all baselines** in diversity and quality.

# 📝 **Problem and Value Proposition:**

## Problem 
- **Diffusion models inherit biases** from their training data, leading to **non-diverse image outputs**.
- Current methods **lack generalizability** across different diffusion models.

## Value Proposition
- **RL-based fine-tuning improves diversity** without sacrificing image quality.
- **Works on both class-conditional & text-to-image models**.
- **Generalizable to future generative AI models**.

# 🔍 **Related Impactful Problems**
- **Bias Mitigation in AI:**
    - Improves fairness in **AI-generated content** (e.g., **job applicant avatars**).
- **Medical Imaging:**
    - Can enhance **diversity in synthetic medical datasets**, reducing dataset biases.
- **Multimodal AI:**
    - Applies to **speech-to-image and video generation models**.

# 📊Conclusion
- **This paper introduces the first RL-based fine-tuning framework for diffusion models**, improving their **diversity while preserving image quality**.
- The **Diversity Reward function effectively guides the model** toward unbiased generation.
- **Experiments confirm that RL fine-tuning consistently improves diversity across datasets.**
- **Future Work:** Applying this approach to **video and multimodal diffusion models**.