# Thesis Topic: Risk Classification Using Object Interactions in Images

## Introduction
The goal of my research is to perform **risk classification of scenarios** within images, based on the interactions of objects identified in each image. For each classification, the system will provide an **NLP-based justification** that explains why that particular classification was made, grounded in the interactions and relationships between objects. This research focuses on applying **vision-language models (VLMs)** and **distance-based rules** to quantify and justify risks, making the system more explainable.

The motivation behind this work is to create a **robust and informative architecture** that can provide actionable insights, especially for industries like agriculture or environmental management, where understanding the spatial and interaction dynamics of objects (e.g., plants, cattle tracks) can help inform risk-based decisions.

## Pipeline Structure
For my pipeline, I need a structure to **evaluate the performance of the risk classifications** and their corresponding **descriptions**. The core architecture will be a combination of **object detection, distance computation, and vision-language modeling** to generate both the classification and the justification.

### Key Components:
1. **Object Detection (YOLOv11)**: Used to extract the positions of various objects in an image, such as plants, water bodies, and cattle tracks.
2. **Distance-Based Ruleset**: A ruleset based on object distances will determine the level of risk.
3. **Vision-Language Models (VLMs)**: Encode the image into vector space and generate the descriptions.
4. **RAG (Retrieval-Augmented Generation)**: Although retrieval may not be necessary due to a small document set, it is worth exploring for potential improvements in description quality.

---

## Current Architecture Plans
![diagram](https://github.com/user-attachments/assets/d0c9e460-166b-4e6b-bca2-bc8be5c138b4)


## Ruleset for Risk Classification
The following rules will guide the classification process based on the proximity of objects within the image:

1. **Proximity to Water** → Risk of Propogation (grow faster, propogate more)
2. **Proximity to Other Plants** → Risk of competition (take resources from other species causes their death)
3. **Proximity to Cattle Tracks** → Risk of Dispersal (picked up by cattle and not dispersed to anywhere to cattle go)


### Risk Categories:
- **Low Risk**: Mean distance > 10m
- **Medium Risk**: 5m < Mean distance < 10m
- **High Risk**: 0m < Mean distance < 5m
- **Critical Risk**: Direct contact between objects

This ruleset provides a simple yet effective way to **annotate images** and guide the model's classification decisions. Additionally, since we know the **pixel-to-meter ratio**, we can accurately calculate distances within the images.  Even without the pixel to metre ratio we can still use the labelled images in order to provide
enough training data such that the damage can be mitigated. 

### Risk Categories Extended
#### New Ideas
After talking to Peter he seemed to think that the parkinsonia spread as far as they are tall.  Using a provieded research paper he outlined a relationship between the parkinsonias dry weight, its height and its diameter and if I rearrange these equations I may be able to get an equation that can tell me its height given its diameter.  

Then using this in combination with the systems current capabilities we can use this calculated height and calculate the maximum spreading distance for each of the parkinsonia within the image. 

This means we could do a system where we get the low, med, high, critical based on the percentage distance of the planets height.  For example no risk is distances greater than 100% of its height, low within 100% to 75%, medium within 75% to 50%, high within 50% to 25% and critical from 25% to 0%. Furthermore, another idea is to models the risk as a 3D normal distribution for the chance of spreading.  

#### Calculating the diameter to height ratio
Using the provided formulas of
W = 0.091D^3.04 
W = 0.025H^4.47

We can get that H = ((0.091D)^3.04/0.025)^(1/4.47) allowing us to calculate the height of the parkinsonia given its diameter. 

The only Issue is that this is the canopy diameter but I think is this case it will be fine to do it this way.  We will make it such that the maximum risk radius from a 5 * the height of the tree.  This will be easy to quantify using the known drone pixel to metre ratio or getting info about the drone image metadata in order to calculate these distances using projections. 

This will then need to be used in order to make an accurately labelled dataset for the vlm model finetuning like for lava as well as finetuning the openai vlm models in order to see how each of these compare in there results for risk identification in images.  

---

## Model Architecture
### Vision-Language Modeling & Object Detection
The architecture I plan to use combines several techniques to provide robust and informative descriptions of object interactions in images.

1. **YOLOv11**: This model will detect the various objects within the image, such as weeds, plants, water bodies, or cattle tracks, and calculate the distance between them.
2. **Vision-Language Encoding**: A VLM will encode the image into vector space, allowing the model to understand spatial and contextual relationships between the objects.

The combination of these approaches should produce more accurate and **explainable results** compared to traditional methods. This architecture also ensures flexibility in scaling up for larger datasets or more complex environments.

---

## Preliminary Testing
### Initial Focus:
The first set of experiments will focus on measuring the system's ability to classify risks between **Parkinsonia weed** and other plants within the images. The model will compute distances between Parkinsonia and other objects to assess risk levels based on the defined ruleset. 

### Possible Approaches:
- **LLaVA Fine-Tuning**: Fine-tuning the LLaVA model on this task.
- **Voltron Architecture**: Exploring the effectiveness of this alternative architecture.
- **Combined LLaVA (Voltron + LLaVA Architecture)**: A hybrid approach that may offer performance improvements by leveraging the strengths of both models.

The goal is to determine which approach yields the best results for **scenario and risk classification**.

---

## Defining the Research Goal
I need to clearly define what my project aims to achieve. The current focus is an **exploratory study** on the ability of machine learning models to perform **scenario and risk classification** based on **object interactions** within images. The risk classifications will be based on the **ruleset** mentioned earlier, and the system will provide justifications for each decision.

### Key Questions to Explore:
1. **How accurately can the system identify risks based on object interactions?**
2. **Can the model generate meaningful NLP justifications for each classification?**
3. **How do different architectures (LLaVA, Voltron, etc.) perform in this task?**

---

## Additional Considerations
### Sentiment Analysis:
An interesting addition to the evaluation process could be to apply **sentiment analysis** on the generated descriptions. This would allow us to verify whether the **correct risk** was identified based on the sentiment expressed in the descriptions. For example, a high-risk scenario should generate a description with more cautionary or negative sentiment.

### Long-Term Impact:
Incorporating **more advanced NLP techniques** into the system can help improve the quality of justifications and make the model more transparent and trustworthy for real-world applications. Additionally, by refining the ruleset, the project could expand to other domains where **scenario risk assessments** are needed, such as **construction**, **wildlife monitoring**, or **disaster management**.

---

## Evaluation Metrics:
### Classification:
We need to first check whether the models provided the correct risk scenario classification based off of what is happening in the image, we can do this with a basic categorical cross entropy loss.  

### Justifications:
We also need to evaluate the natural lanaguage jsutification the model provides for its answer, in this we are not explicitely always looking for a exact word match but more semantic similarity between the provided answer and the gold label ground truth 

### Evaluation Methodology


---

## Conclusion
This project aims to push the boundaries of **scenario and risk classification** using object interactions in images. By combining **state-of-the-art object detection** with **vision-language models** and **distance-based rules**, the goal is to create a system that not only classifies risks accurately but also provides insightful, NLP-driven explanations.

Ultimately, this research will help me build a portfolio showcasing my ability to design and implement complex machine learning architectures, making it a valuable asset for future opportunities in **AI research**, **machine learning engineering**, or **computer vision** roles.

### Next Steps:
- Define a clear evaluation metric for risk classifications and justifications.
- Compare the performance of different model architectures.
- Explore sentiment analysis as part of the justification validation.
- **Proposal for the system process One Weed - All Weeds - Extending to creating tables etc**
- **Risk defined based on std deviations from mean of normal distrbution**
- **Final challenge apply to whole orthomosiac - there would be an amazing paper to write here**

---
