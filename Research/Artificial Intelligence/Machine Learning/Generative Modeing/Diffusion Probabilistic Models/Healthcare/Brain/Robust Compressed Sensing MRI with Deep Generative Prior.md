**Paper:** @jalalRobustCompressedSensing2021
# Relation 

## Papers By Category

### Brain
- [[Score-based Diffusion Models for Accelerated MRI]]
- [[Conversion Between CT and MRI Images Using Diffusion and Score-Matching Models]]
### Pathology
 - [[A Morphology Focused Diffusion Probabilistic Model for Synthesis of Histopathology Image]]

## Textbook

## Tags 

#tag1, #tag2

# Robust Compressed Sensing MRI with Deep Generative Prior
## 📄 **Aim:**
### Abstract 
- This paper explores the application of deep generative priors within the **Compressed Sensing Generative Model (CSGM) framework** to enhance MRI reconstruction. 
- The authors train a **generative prior** on brain scans from the fastMRI dataset and utilize posterior sampling via **Langevin dynamics** to achieve high-quality reconstructions

### Research Statement / Question 
- Can deep generative priors improve the robustness and quality of compressed sensing MRI reconstructions, especially when dealing with out-of-distribution samples?

### Contributions of the Paper
- First successful application of the **CSGM framework** on clinical MRI data.
- Demonstrated that posterior sampling via Langevin dynamics achieves high-quality reconstructions.
- Provided theoretical and empirical evidence of robustness to changes in ground-truth distribution and measurement processes.

## 📚 **Background:**

### **Background of the Paper:**  

**Context:** Compressed sensing has enabled reductions in the number of measurements needed for successful reconstruction in imaging inverse problems, notably shortening scan times for MRI. Traditional sparsity-based methods are limited by achievable acceleration rates due to hand-crafted assumptions.

### **Background of the Method:**  
The CSGM framework utilizes deep generative models as priors for **solving inverse problems**, generalizing the theoretical framework of compressed sensing for signals lying on the range of a deep generative model.

### **Limitations of Previous Work:**  
Prior applications of the CSGM framework were empirically successful only on certain datasets (e.g., human faces, MNIST digits) and performed poorly on out-of-distribution samples

### **Related Work:**  
Generative priors have been applied to various inverse problems, including non-linear phase retrieval and improved compressed sensing, demonstrating the utility of deep generative models in enhancing reconstruction quality

## 🔧 **Method:**

### **Contribution:**  
The authors trained a **score-based deep generative model** for complex-valued, T2-weighted brain MR images without assumptions on the measurement scheme. They applied posterior sampling via Langevin dynamics for MRI reconstruction under the CSGM framewor
    
### **Insights:**
- Posterior sampling with the correct prior is within **constant factors of the optimal recovery** method for any measurements, including Fourier measurements in MRI.
- Even with an incorrect prior that assigns some probability mass to the true distribution, posterior sampling for Gaussian measurements remains nearly optimal with minimal loss.
### **Novelty:**  
This work represents the first successful application of the CSGM framework on clinical MRI data, demonstrating robustness to changes in ground-truth distribution and measurement processes

### **Limitations:**  
The study primarily focuses on T2-weighted brain MR images; further research is needed to generalize the approach to other imaging modalities and anatomies

### **Results:**

- Achieved competitive performance compared to end-to-end deep learning methods when test-time data were sampled within distribution.
- Demonstrated robustness to various out-of-distribution shifts, with end-to-end methods showing significant degradation in some cases.


## 🧪 **Experimental Evaluation:**

### Dataset
Utilized brain scans from the fastMRI dataset for training and evaluation.

### Experiments

- Compared reconstruction quality using the proposed method against end-to-end deep learning approaches under various sampling patterns and anatomical shifts.
- Assessed robustness to out-of-distribution samples, including different sampling patterns and imaging anatomies


## 📊Conclusion
- The study successfully applied deep generative priors within the CSGM framework to clinical MRI data, achieving high-quality reconstructions.
- The proposed method demonstrated robustness to changes in ground-truth distribution and measurement processes, outperforming end-to-end deep learning methods in out-of-distribution scenarios.
- Future work could explore extending this approach to other imaging modalities and further improving robustness and generalization capabilities.