**Paper:** @lyuConversionCTMRI2022
# Relation 

## Papers By Category
### Brain
- [[Score-based Diffusion Models for Accelerated MRI]]
- [[Robust Compressed Sensing MRI with Deep Generative Prior]]
- [[A Novel Unified Conditional Score-based Generative Framework for Multi-modal Medical Image Completion]]
## Textbook

## Tags 

#CT, #MRI

# Conversion Between CT and MRI Images Using Diffusion and Score-Matching Models
## 📄 **Aim:**
### Abstract 
This paper explores the use of diffusion and score-matching models for converting images between CT and MRI modalities, with a focus on **generating synthetic CT images from MRI inputs.** 
The study adapts denoising diffusion probabilistic models (DDPM) and stochastic differential equation (SDE) approaches, employing four different sampling strategies, and compares their performance against convolutional neural networks (CNNs) and generative adversarial networks (GANs)

### Research Statement / Question 
Can diffusion and score-matching models provide superior image synthesis quality in CT to MRI conversions compared to traditional CNN and GAN models?

### Contributions of the Paper
- Introduced diffusion and score-matching models for CT to MRI image conversion.
- Implemented four distinct sampling strategies within these models.
- Conducted comparative analysis with CNN and GAN models.
- Investigated uncertainties in diffusion and score-matching networks using the Monte Carlo method.

## 📚 **Background:**

### **Background of the Paper:**  
MRI and CT are widely used medical imaging modalities, often requiring multi-modality images for diagnosis and treatment planning. However, acquiring both modalities can be costly and may introduce misalignment issues. Computational conversion between MRI and CT images offers a viable solution to these challenges

### **Background of the Method:**  
Diffusion models, including DDPM and SDE-based approaches, have emerged as powerful deep learning frameworks for image generation tasks, demonstrating advantages over traditional models like CNNs and GANs in terms of image quality and training stability.

### **Limitations of Previous Work:**  
CNNs and GANs, while effective in various image synthesis tasks, often face challenges such as training instability, mode collapse, and difficulty in capturing complex data distributions, which can limit their performance in medical image conversion tasks.

### **Related Work:**  
- Recent studies have applied diffusion models to medical imaging tasks, showing promising results in image synthesis and enhancement. However, their application in modality conversion, particularly between CT and MRI, remains underexplored.


## 🔧 **Method:**

### **Contribution:**  
The authors adapted DDPM and SDE-based diffusion models for the task of CT to MRI image conversion, implementing four different sampling strategies to assess their effectiveness. They compared the performance of these models against CNN and GAN architectures with consistent network configurations.
    
### **Insights:**

- Diffusion and score-matching models can generate higher quality synthetic CT images from MRI inputs compared to CNNs and GANs.
- Monte Carlo sampling can be used to quantify uncertainties in the generated images, and averaging multiple samples can improve the quality of the results.

### **Novelty:**  

This study is among the first to apply diffusion and score-matching models to the task of CT to MRI image conversion, demonstrating their potential advantages over traditional deep learning models.

### **Limitations:**  
The study primarily focuses on the conversion from MRI to CT images; further research is needed to assess the models' performance in the reverse direction and across diverse datasets.
### **Results:**

- Diffusion and score-matching models outperformed CNN and GAN models in generating synthetic CT images, as evidenced by superior performance metrics.
- Monte Carlo averaging of multiple outputs from the diffusion models led to improved image quality.

## 🧪 **Experimental Evaluation:**

### Dataset
- The study utilized paired MRI and CT images for training and evaluation, though specific dataset details are not provided in the summary.

### Experiments

- Implemented DDPM and SDE-based diffusion models with four sampling strategies.
- Trained and evaluated CNN and GAN models with consistent architectures for comparison.
- Assessed image quality using performance metrics and evaluated uncertainties using the Monte Carlo method.

## 📊Conclusion
- Diffusion and score-matching models are effective for CT to MRI image conversion, generating higher quality synthetic images compared to CNN and GAN models.
- These models offer analytical rigor, clear explainability, and competitive performance in image synthesis tasks.
- Incorporating Monte Carlo sampling allows for uncertainty quantification and improved image quality through averaging.
- Future work should explore the application of these models to other modality conversions and assess their performance across diverse datasets.