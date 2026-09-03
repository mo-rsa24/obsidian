**Paper:** @mengNovelUnifiedConditional2022
# Relation 

## Papers By Category
### Brain
- [[Score-based Diffusion Models for Accelerated MRI]]
- [[Robust Compressed Sensing MRI with Deep Generative Prior]]
- [[Conversion Between CT and MRI Images Using Diffusion and Score-Matching Models]]

## Textbook

## Tags 

#MRI, #CT


# 📄 **Aim:**
## Abstract 
This paper introduces the Unified Multi-Modal Conditional Score-based Generative Model (UMM-CSGM) to address the challenge of missing modalities in multi-modal medical imaging. By leveraging Score-based Generative Models (SGMs), UMM-CSGM models and samples from target probability distributions, enabling cross-modal conditional synthesis for various missing-modality configurations within a unified framework

## Research Statement / Question 
Can a unified conditional score-based generative framework effectively handle multiple missing-modality configurations in medical imaging by accurately modeling cross-modal relationships and inherent uncertainties?

## Contributions of the Paper
- Proposes UMM-CSGM, extending SGMs to cross-modal conditional synthesis for diverse missing-modality scenarios.
- Introduces a novel multi-in multi-out Conditional Score Network (mm-CSN) to learn comprehensive cross-modal conditional distributions via conditional diffusion and reverse generation in the complete modality space.
- Demonstrates the model's effectiveness in synthesizing missing modalities with higher similarity to ground truth compared to existing state-of-the-art methods.

# 📚 **Background:**

## **Background of the Paper:**  
Multi-modal medical imaging provides complementary information crucial for accurate diagnosis and treatment planning. However, acquiring all modalities for every patient is often impractical due to time, cost, or patient-related constraints, leading to missing modality issues. Addressing this challenge through reliable image synthesis is essential for enhancing diagnostic tasks.
## **Background of the Method:**  
Score-based Generative Models (SGMs) have shown success in image generation by capturing and effectively sampling target distributions through stochastic diffusion (transition to noise distribution) and reverse generation (denoising). Their probabilistic nature allows for modeling inherent uncertainties in data distributions.
## **Limitations of Previous Work:**  
Existing synthesis methods often rely on deterministic mappings from available modalities, neglecting the uncertainties in cross-modal relationships. Additionally, many approaches are tailored to specific missing-modality configurations, lacking the flexibility to handle various scenarios within a single framework.
## **Related Work:**  

- Recent studies have applied SGMs to medical imaging tasks, demonstrating their potential in modeling complex data distributions. However, extending SGMs to unified cross-modal conditional image completion, capable of addressing multiple missing-modality configurations, remains an underexplored area.
# 🔧 **Method:**

## **Contribution:**  
UMM-CSGM employs a multi-in multi-out Conditional Score Network (mm-CSN) to learn a comprehensive set of cross-modal conditional distributions via conditional diffusion and reverse generation in the complete modality space. This design enables the generation process to be accurately conditioned by all available information, accommodating all possible configurations of missing modalities within a single network.
## **Insights:**
- Modeling cross-modal relationships probabilistically captures inherent uncertainties, leading to more reliable synthesis of missing modalities.
- A unified framework capable of handling various missing-modality configurations enhances flexibility and applicability in clinical settings.
## **Novelty:**  
This work is among the first to generalize SGMs for unified cross-modal conditional image completion, introducing a framework that accommodates any missing-modality configuration within a single model.
## **Limitations:**  
- The study focuses on the BraTS19 dataset; further validation on diverse datasets and imaging modalities is necessary to assess generalizability. Additionally, the computational complexity associated with training and inference in SGMs may pose challenges for real-time clinical applications.
## **Results:**

Experiments on the BraTS19 dataset demonstrate that UMM-CSGM can more reliably synthesize heterogeneous enhancement and irregular areas in tumor-induced lesions for any missing modalities, outperforming existing state-of-the-art generative methods.
# 🧪 **Experimental Evaluation:**

## Dataset
The BraTS19 dataset, comprising multi-modal MRI scans of brain tumors, was utilized to evaluate the model's performance in synthesizing missing modalities.
## Experiments
- UMM-CSGM was tested across various missing-modality configurations to assess its flexibility and robustness.
- Comparative analyses with existing state-of-the-art generative methods were conducted to evaluate synthesis quality, focusing on similarity to ground truth images.
# 📊Conclusion
- UMM-CSGM presents a significant advancement in multi-modal medical image completion by introducing a unified framework capable of handling various missing-modality configurations.
- By leveraging the probabilistic nature of SGMs, the model effectively captures inherent uncertainties in cross-modal relationships, leading to more reliable and accurate synthesis of missing modalities.
- Future work should focus on validating the framework across diverse datasets and imaging modalities, as well as optimizing computational efficiency for potential clinical integration.