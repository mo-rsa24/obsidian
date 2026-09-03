**Paper:** @moghadamMorphologyFocusedDiffusion2022

#Pathology, #Diffusion

## Relation:
### Brain 
- Robust Compressed Sensing MRI with Deep Generative Prior
## 📄 **Aim:**
#### Abstract 
- This paper investigates the use of diffusion probabilistic models for generating synthetic histopathology images. 
- The focus is on brain cancer images, aiming to improve image quality through prioritized morphology and color normalization.
#### Research Statement / Question 
- Can diffusion probabilistic models outperform GANs in synthesizing high-quality histopathology images for educational, privacy, and data augmentation applications?

#### Contributions of the Paper
- Introduces the use of diffusion probabilistic models to generate synthetic histopathology images.
- Incorporates color normalization and perception-prioritized weighting to enhance the quality of generated images.
- Compares the proposed method with GAN-based approaches using various quality metrics.

## 📚 **Background:**

### **Background of the Paper:**  
- Histopathology, the microscopic study of diseased tissue, is critical for cancer diagnosis.
- Generating synthetic images is useful for training, testing, and preserving patient privacy.

### **Background of the Method:**  
- Generative models like GANs have been used for image synthesis but have limitations, including mode collapse and instability. 
- Diffusion models offer a stable alternative by generating images through iterative denoising.
### **Limitations of Previous Work:**  
- GAN-based methods struggle with rare subtypes and overfitting. They are also difficult to train and may produce artifacts in images.

### **Related Work:**  
- Diffusion models have been used for other tasks (e.g., image segmentation, text-to-speech) but have not been applied to histopathology image generation.

## 🔧 **Method:**

### **Contribution:**  
- The authors propose a diffusion probabilistic model with a Unet-based backbone to synthesize histopathology images with color normalization and morphology prioritization.
    
### **Insights:**
- Color normalization addresses inconsistencies in tissue staining, improving model performance.
- Perception-prioritized weighting enhances focus on key morphological details during diffusion steps.
### **Novelty:**  
- The first application of diffusion probabilistic models to histopathology image synthesis.

### **Limitations:**  
- Longer sampling time compared to GANs due to multiple diffusion steps.

### **Results:**
- Outperforms ProGAN across multiple metrics, including Inception Score, FID, and sFID.
- Produces images that pathologists found indistinguishable from real ones in a survey.

## 🧪 **Experimental Evaluation:**

### Data
- Used a dataset of 344 whole slide images (WSIs) of low-grade gliomas from the Cancer Genome Atlas.

### Experiment 1
- Compared the diffusion model with ProGAN using metrics like IS, FID, and sFID. The diffusion model scored significantly better

### Experiment 2 
- Conducted a survey with pathologists to assess the realism of synthetic images. 
- The diffusion model's images were often mistaken for real.

## 📊Conclusion
- The proposed diffusion probabilistic model generates high-quality histopathology images that are indistinguishable from real images in most cases.
- It addresses the limitations of GANs, such as mode collapse and instability.
- The method can be used for educational purposes, proficiency testing, and privacy-preserving data sharing.
- Future work could focus on optimizing the model to reduce sampling time.