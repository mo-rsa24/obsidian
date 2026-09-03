**Paper:** @moghadamMorphologyFocusedDiffusion2022
# Relation 

## Papers By Category

## Textbook

## Tags 

#tag1, #tag2


# 📄 **Aim:**
## Abstract 

This paper introduces SPIRiT-Diffusion, a novel diffusion model tailored for MRI reconstruction that integrates the **SPIRiT iterative reconstruction** algorithm. 

By characterizing the **prior distribution of coil-by-coil** images through score matching and leveraging **k-space redundancy** via self-consistency, the model achieves superior reconstruction results, particularly in vessel wall imaging

## Research Statement / Question 
Can integrating SPIRiT's self-consistency constraints with score-based generative models enhance MRI reconstruction quality, especially for vessel wall imaging?

## Contributions of the Paper
- Developed SPIRiT-Diffusion, combining score-based generative modeling with SPIRiT's k-space self-consistency constraints.
- Demonstrated improved reconstruction quality on the joint Intracranial and Carotid Vessel Wall imaging dataset.
- Highlighted the importance of incorporating multi-coil acquisition characteristics in diffusion models for MRI.

# 📚 **Background:**

## **Background of the Paper:**  
MRI is a pivotal imaging modality, but its prolonged acquisition times can impede clinical workflows. 

Accelerated imaging techniques, such as parallel imaging, aim to reduce scan times by acquiring undersampled data and reconstructing full images using prior information.

## **Background of the Method:**  
- **SPIRiT (Iterative Self-consistent Parallel Imaging Reconstruction):** A parallel imaging method that enforces self-consistency in k-space data across multiple coils, facilitating accurate image reconstruction from undersampled data.

- **Score-Based Generative Models:** These models perturb data by adding noise to transform the data distribution into a Gaussian distribution and then generate samples by reversing this process, effectively modeling complex data distributions.
## **Limitations of Previous Work:**  
Existing diffusion models applied to MRI reconstruction often overlook the multi-coil nature of MRI data, potentially limiting reconstruction quality. 

Additionally, inaccuracies in coil sensitivity maps can adversely affect image-domain methods.
## **Related Work:**  
Recent studies have applied diffusion models to MRI reconstruction, demonstrating promising results. 

However, the integration of k-space self-consistency constraints, as in SPIRiT, with score-based generative models remains underexplored

# 🔧 **Method:**

## **Contribution:**  
SPIRiT-Diffusion integrates score-based generative modeling with SPIRiT's k-space self-consistency constraints. 

It characterizes the **prior distribution of coil-by-coil images** through score matching and enforces k-space redundancy via self-consistency, effectively combining data-driven and physics-based priors
## **Insights:**

Incorporating k-space self-consistency constraints into diffusion models can enhance reconstruction quality, especially in scenarios with high acceleration factors.

## **Novelty:**  

## **Limitations:**  

## **Results:**


# 🧪 **Experimental Evaluation:**

## Dataset

## Experiments

# 📊Conclusion
