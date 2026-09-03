**Paper:** @chungScorebasedDiffusionModels2022
# Relation 

## Papers By Category

### Brain
- [[Robust Compressed Sensing MRI with Deep Generative Prior]]
- [[Conversion Between CT and MRI Images Using Diffusion and Score-Matching Models]]
### Pathology
[[A Morphology Focused Diffusion Probabilistic Model for Synthesis of Histopathology Image]]

## Textbook

## Tags 

#MRI, #score-based, 

# Paper Title
## 📄 **Aim:**
### Abstract 
This paper introduces a method for reconstructing c**omplex-valued MRI data** from **undersampled measurements** using score-based diffusion models. 

The approach involves training a **continuous time-dependent score function** with denoising score matching and iteratively applying a **numerical SDE solver** alongside a data consistency projection during inference

### Research Statement / Question 
Can score-based diffusion models effectively reconstruct high-quality MRI images from undersampled data, outperforming traditional supervised learning methods?

### Contributions of the Paper

Developed a framework that utilizes score-based diffusion models for MRI reconstruction, **requiring only magnitude images** for training yet capable of reconstructing complex-valued data.

Demonstrated the **method's agnosticism to subsampling patterns**, allowing flexibility with various sampling schemes.

Showcased the model's ability to quantify uncertainty in reconstructions, a feature not typically available in standard regression approaches.

## 📚 **Background:**

### **Background of the Paper:**  
Accelerated MRI aims to **reduce scan times by acquiring undersampled data**, necessitating robust reconstruction methods to recover high-fidelity images from incomplete measurements. 


Traditional methods often rely on hand-crafted priors or supervised learning, which may lack generalization across different sampling patterns and anatomies.

### **Background of the Method:**  
Score-based diffusion models perturb data distributions through forward SDEs by adding Gaussian noise, leading to a tractable distribution. 

Sampling from the data distribution is achieved by training a neural network to estimate the gradient of the log data distribution (score function) and solving the reverse SDE numerically.

### **Limitations of Previous Work:**  

Supervised learning methods for MRI reconstruction typically require **retraining for each new sampling scheme** and may not generalize well to different anatomies or contrasts.

Additionally, they often lack mechanisms for uncertainty quantification in reconstructions.

### **Related Work:**  
Recent advancements in generative models, particularly score-based diffusion models, have shown promise in various imaging tasks, including image generation and inverse problems

However, their application to MRI reconstruction, especially in a manner agnostic to sampling patterns and capable of handling complex-valued data, remains underexplored.
## 🔧 **Method:**

### **Contribution:**  
The authors propose a method that trains a continuous time-dependent score function using denoising score matching on **magnitude images.** 

During inference, the method alternates between a **numerical SDE solver** and a **data consistency projection** step to reconstruct complex-valued MRI data from undersampled measurements.
    
### **Insights:**

Training solely on magnitude images suffices to reconstruct complex-valued data, simplifying the training data requirements.

The model's generative nature allows for **uncertainty quantification in reconstructions**, providing confidence estimates alongside images.

### **Novelty:**  

This approach is the first to apply score-based diffusion models to MRI reconstruction in a manner that is agnostic to subsampling patterns and capable of handling complex-valued data without requiring fully sampled training data.

### **Limitations:**  
The method's performance in extremely high undersampling scenarios or with highly noisy data requires further investigation. 

Additionally, the computational complexity associated with iterative SDE solving may pose challenges for real-time applications.

### **Results:**


> [!NOTE] Analysis Of Results
> - The proposed method outperforms supervised learning models trained specifically for MRI reconstruction tasks, achieving higher quality reconstructions.
> - It generalizes well across different sampling schemes and anatomies, demonstrating robustness and flexibility.
> - The model provides uncertainty quantification, offering valuable insights into the reliability of reconstructions.

## 🧪 **Experimental Evaluation:**

### Dataset

Experiments were conducted using various MRI datasets, focusing on different anatomies and sampling patterns to assess the model's generalization capabilities.

### Experiment 1
The proposed method was compared against supervised learning models trained for specific sampling schemes, evaluating reconstruction quality and generalization to unseen sampling patterns.

The ability to reconstruct complex-valued data from magnitude-only training was assessed, highlighting the model's versatility.

Uncertainty quantification was demonstrated by generating multiple reconstructions from the same measurement vector, showcasing the model's stochastic nature.

## 📊Conclusion

The study presents a novel application of **score-based diffusion models** for **MRI reconstruction,** achieving state-of-the-art performance while being agnostic to subsampling patterns and capable of handling complex-valued data.

The method's generative nature enables uncertainty quantification, providing additional insights beyond standard reconstruction techniques.

Future work may explore optimizing the computational aspects of the method for real-time applications and extending the approach to other imaging modalities