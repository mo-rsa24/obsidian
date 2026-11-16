---
aliases: [object detector, object detection, Mask2Former, MS-COCO, COCO classes]
standard: vault-note v2
---

# Object Detector

Up: [[Deep Learning]]

Artificial Intelligence, Deep Learning. Used by [[GenEval]]. Its colour step uses [[Contrastive Image-Text Training]].

**An object detector lists the objects it finds in an image, each with a class name, a box and a confidence.**

> [!warning]- Unfinished
> - The card is short on purpose: it holds what the journey's chapters need. The Textbooks and Videos groups of the card are not built; waiting: `/concept-link build a card for Object Detector`.
> - No claim is marked stated.

## What the chapters need

**What it returns.** For the two-object render of a mug and a wine glass the detector lists cup 0.94, wine glass 0.98 and wine glass 0.89. The mug carries two boxes at the same place, so one object can hold two labels *(shown: the journey's `probe_geneval.csv`)*.

### Mask2Former

**Mask2Former** is the detector GenEval uses, trained on MS-COCO and taken from the MMDetection toolbox. The repository keeps detections above 0.3 confidence and uses the Swin-S Mask2Former; the paper uses 0.9 for counting *(cited: GenEval paper page 5; code docstring)*. The paper names holes in an object getting included in its segmentation mask *(cited: page 7)*.

### MS-COCO classes

The detector only knows the classes of MS-COCO, a limited set at one level of detail, so a mug is named by the class cup and a concept with no class cannot be judged. The tool can count people and cannot count fingers *(cited: GenEval paper page 9)*.

**Other detectors in the journey.** T2I-CompBench++ scores spatial and numeracy sub-categories with a detector called UniDet. What UniDet is, is unknown here. See [[T2I-CompBench]].

**What it misses.** Overlapping objects of the same type give merged boxes and clip art is out of distribution *(cited: GenEval paper page 7)*.

## Where to learn this

**Object Detector**, a model that boxes and names the objects in a picture. Also: object detection, Mask2Former, MS-COCO, COCO classes.

**Papers**

- [GenEval paper, page 5](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/benchmarks/geneval-object-focused-framework-for-evaluating-text-to-image-alignment.pdf#page=5): the detector, its training set and the colour step.
- [GenEval paper, pages 7 and 9](/home/molef/goal-setting/learning/papers/deep-learning/diffusion-models/compositional-diffusion-models/benchmarks/geneval-object-focused-framework-for-evaluating-text-to-image-alignment.pdf#page=7): the failure modes and the stated limit.

**Our plans and chapters**

- [Journey chapter 4, how a pass is decided](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/textbook/04-geneval.md#how-a-pass-is-decided): the boxes and the rule.
- [Journey paper reading, GenEval](/home/molef/goal-setting/learning/deep-learning/diffusion-models/12-scoring-and-rival-methods/sources/paper-readings/geneval.md): the failure modes against our runs.
