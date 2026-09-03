**Paper:** @AcceleratedMotionCorrection
# Relation 

## Papers By Category
- [[Score-based Diffusion Models for Accelerated MRI]]
- [[Robust Compressed Sensing MRI with Deep Generative Prior]]
- [[A Novel Unified Conditional Score-based Generative Framework for Multi-modal Medical Image Completion]]
- [[Conversion Between CT and MRI Images Using Diffusion and Score-Matching Models]]
## Textbook

## Tags 

#tag1, #tag2


# 📄 **Aim:**
## Abstract 
This paper introduces a framework that leverages score-based generative models to **jointly reconstruct highly undersampled MRI data while estimating patient motion**. The method does not rely on specific assumptions about sampling trajectories or motion patterns during training, allowing for flexible application to various measurement models and patient movements.

## Research Statement / Question 
Can score-based generative models be utilized to effectively perform simultaneous image reconstruction and motion correction in accelerated MRI without prior assumptions about sampling or motion patterns?
## Contributions of the Paper
- Developed a Bayesian framework using deep generative diffusion models for joint estimation of motion-free images and rigid motion parameters from undersampled, motion-corrupted k-space data.
- Demonstrated the method's flexibility in handling various sampling trajectories and motion patterns without specific training-time assumptions.
- Showcased the framework's effectiveness through experiments on retrospectively accelerated 2D brain MRI data corrupted by rigid motion.
# 📚 **Background:**

## **Background of the Paper:**  
Magnetic Resonance Imaging (MRI) is a crucial medical imaging modality but is hindered by long scan times, leading to increased costs and susceptibility to patient motion artifacts. Motion during acquisition causes inconsistencies in measured data, resulting in blurring and ghosting artifacts if not addressed during image reconstruction.

## **Background of the Method:**  
Score-based generative models, particularly diffusion models, have shown promise in modeling complex data distributions by estimating the gradient of the data distribution (score) and generating samples through iterative refinement. These models can be adapted for inverse problems like MRI reconstruction by incorporating measurement processes into the generative framework.
## **Limitations of Previous Work:**  
Traditional deep learning-based reconstruction techniques often require specific assumptions about sampling patterns and motion during training, limiting their adaptability to different scenarios. End-to-end motion correction methods may also be vulnerable to distribution shifts at test time, affecting their robustness.
## **Related Work:**  
Recent advancements have applied deep generative models to MRI reconstruction, demonstrating improved performance in handling undersampled data. However, integrating motion correction into these frameworks without relying on specific training assumptions remains an area requiring further exploration.

# 🔧 **Method:**

## **Contribution:**  
The proposed framework employs a Bayesian approach using deep generative diffusion models to jointly estimate motion-free images and rigid motion parameters from undersampled, motion-corrupted k-space data. This is achieved without making specific assumptions about sampling trajectories or motion patterns during training, enhancing the method's flexibility and applicability
## **Insights:**
- By modeling the joint distribution of images and motion parameters, the framework can effectively **disentangle motion artifacts** from undersampled data, leading to improved image reconstruction quality.
- The use of score-based generative models allows for iterative refinement, progressively enhancing image quality while correcting for motion-induced inconsistencies.
## **Novelty:**  
- This work is among the first to integrate score-based generative models into a unified framework for simultaneous image reconstruction and motion correction in accelerated MRI, without relying on specific training-time assumptions about sampling or motion patterns.

## **Limitations:**  
The study focuses on 2D brain MRI data with simulated rigid motion; further research is needed to assess the framework's performance on real patient data, different anatomies, and more complex motion patterns. Additionally, the computational demands of diffusion models may pose challenges for real-time clinical applications.
## **Results:**
- Experiments on retrospectively accelerated 2D brain MRI data corrupted by rigid motion demonstrate that the proposed framework effectively reconstructs high-fidelity images while accurately estimating motion parameters.
- The method shows robustness across various sampling trajectories and motion patterns, highlighting its adaptability and potential for clinical use.


# 🧪 **Experimental Evaluation:**

## Dataset
The framework was evaluated on retrospectively accelerated 2D brain MRI data with simulated rigid motion to assess its performance in joint image reconstruction and motion correction.
## Experiments
- The method was tested across different sampling trajectories and motion patterns to evaluate its flexibility and robustness.
- Comparisons were made with traditional reconstruction techniques to demonstrate the advantages of the proposed framework in handling motion-corrupted, undersampled data.
# 📊Conclusion
- The proposed framework represents a significant advancement in accelerated MRI by integrating score-based generative models for simultaneous image reconstruction and motion correction.
- Its flexibility in handling various sampling trajectories and motion patterns without specific training-time assumptions makes it a promising candidate for clinical applications.
- Future work should focus on validating the framework with real patient data, extending it to 3D imaging and non-rigid motion scenarios, and optimizing computational efficiency for practical deployment.