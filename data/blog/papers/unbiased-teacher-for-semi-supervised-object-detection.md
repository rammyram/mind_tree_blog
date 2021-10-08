---
title: Unbiased teacher for semi supervised object detection
date: 2021-10-08
tags: ['paper', 'focal_loss', 'EMA', 'student_teacher']
draft: false
summary: 
---
# Main Idea 

- The heart of this paper is coming up with a new learning framework called **Unbiased Teacher**, which can avoid the class imbalance problem when pseudo labeling is used in SSL. 
- **Unbiased Teacher consists of 2 stages** 
	- **1. Burn In Stage :**
		- In this stage the object detector is simply trained using the available supervised data. 
		
	- **2. 	TEACHER-STUDENT MUTUAL LEARNING : **
		- At the beginning of this stage we duplicate the trained detector from burn in stage into 2 models, Teacher and Student model. 
		
		- This teacher student stage aims at evolving both models by mutual learning mechanism.

		- The Teacher generates Pseudo labels to train the student and the student updates the knowledge it learned back to the teacher gradually.

		- The class imbalance problem which is elevated due to use of pseudo labels in training is handled by EMA (Exponential Moving Average) & Focal Loss 


![/static/images/ai/unbiased_teacher_ssl_architecture.png](/static/images/ai/unbiased_teacher_ssl_architecture.png)


- **Burn In Stage :**
	- Lets consider the model in this stage be model ($\theta$) i.e with $\theta$ weights. 
	- The model is trained to optimize $\theta$ with supervised loss $L_{sup}$ . 
	>**Supervised Loss**
	>  $L_{sup}$  = RPN Classification Loss + RPN Regression Loss + ROI Classification Loss + ROI Regression Loss. 
	- After model convergence, we copy the weights $\theta$ to teacher and student models. 
	 > ( $\theta_t$ ← $\theta$ , $\theta_s$ ← $\theta$ )

- **TEACHER-STUDENT MUTUAL LEARNING :**
	- As you can see in the above architecture, we feed strong augmentation for student, so that the student model could learn better. 
	- Where as very weak augmentation is fed for teacher model, so that the generated pseudo labels are reliable. 
	- To address the problem of noisy pseudo labels that leads to error accumulation over time, non-max suppression to filter duplicate predictions and after that confidence thresholding is applied to filter low confidence bboxes. 
	- Also student and teacher are detached i.e only learnable weights of student is updated during back propagation.
	
	> **Student Weight Update :**
	> $\theta_s$ =  $\theta_s$ + $\gamma * \frac{\partial (L_{sup} + \lambda * L_{unsup})} { \partial \theta_s}$ ) --> Eq 1
	> **Unsupervised Loss : **
	> $L_{unsup} = \sum(L^{rpn}_{cls} + L^{roi}_{cls} )$ --> Eq 2
	> -  $\gamma$ is the learning rate. 
	> - $\lambda$ is the unsupervised loss weight. 
	> - $L_{sup}$ : We get this loss when we feed labeled data to the student model, it's the sum of 4 losses --> roi classification + roi regression, rpn classification, rpn regression.
	> - $L_{Unsup}$ : We get this loss when we feed this Pseudo data to the model, it's the sum of 2 losses --> roi classification + rpn classification.
	> 
	> **Note :** we do not apply unsupervised losses for the bounding box regression since the naive confidence thresholding is not able to filter the pseudo-labels that are potentially incorrect for bounding box regression (because the confidence of predicted bounding boxes only indicate the confidence of predicted object categories instead of the quality of bounding box locations

- **Teacher Refinement via Exponential Moving Average :**
	- To get more stable pseudo labels, we apply EMA to gradually update the teacher model, the teacher model could be seen as ensemble of student model over different iterations. 
	- Teacher weights are updated periodically after certain number of iterations. 
	> ** Teacher weights update :**
	> $\theta_t$ = $\alpha * \theta_t + (1-\alpha) * \theta_s$ --> Eq 3
	> - Here $\alpha$ is the EMA coefficient	( Exponential Moving Average )
	- To be more specific, with the EMA mechanism, the new Teacher model is regularized by the previous Teacher model, and this prevents the decision boundary from drastically moving toward the minority classes. In detail, the weights of the Teacher model can be represented as follows
	
- **Multi Class Focal Loss :**
	- We know focal loss is designed to put more loss weight on samples with low confidence i.e hard examples instead of easy examples that are likely from dominant class. 
	- Although focal loss is not widely used in supervised learning and also said to degrade accuracy for supervised models. Here its very much necessary to handle biased Pseudo label problem. 
	- Multi class focal loss is applied to the **ROI head classifier. **

- **Hyper  Parameters :**
	-  EMA Rate ($\alpha$) : 0.99
	-  Pseudo Label Confidence Threshold ( $\sigma$ ) : 0.7 
	-  Unsupervised Loss Weight ($\lambda$) : 4 or 5 
	-  Focal Loss ($\gamma$) : 1.5 
	
	
![/static/images/ai/unbiased_teacher_hyper_parameters.png](/static/images/ai/unbiased_teacher_hyper_parameters.png)



# Vital info

- We highlight the contributions of this paper as follows: 	
	- By analyzing object detectors trained with limited-supervision, we identify that the nature of class-imbalance in object detection tasks impedes the effectiveness of pseudo-labeling method on SS-OD task. 

	-  We thus proposed a simple yet effective method, Unbiased Teacher, to address the pseudo labeling bias issue caused by class-imbalance existing in ground-truth labels and the over-fitting issue caused by the scarcity of labeled data. 
	
	-    Unbiased Teacher achieves state-of-the-art performance on SS-OD across COCO standard.


# Problems solved

- **Pseudo Labeling class imbalance problem :**
	- **Understand the problem : **
		- In object detection there's always background-foreground imbalance and foreground classes imbalance. These imbalances make the models trained in SSL settings prone to generate biased predictions. 
		- Model may be biased towards dominant classes as a result we will have biased pseudo labels. 
		- Now feeding this biased pseudo labels for training is gonna aggravate the class imbalance issue and cause sever over fitting. 
		- Observe heavy over-fitting in the below image for the background & foreground classifier in RPN and multi-class classification in ROI Head 
		
![/static/images/ai/unbiased_teacher_ssl_rpn_overfitting.png](/static/images/ai/unbiased_teacher_ssl_rpn_overfitting.png)

	-  **Solution :** 
		-  Unbiased Teacher Framework used in this paper
		-  Shifting from Cross entropy loss to Focal Loss.
		-  Use of EMA to update teacher. 	

-  **More Accurate Pseudo Labels are created :**
	-  Previous methods freeze the models trained on supervised data to generate Pseudo Labels .
	-  **Solution: ** But this method uses teacher student mutual learning framework to gradually improve the pseudo labels generated for SSL. 


# Related Work

![/static/images/ai/unbiased_teacher_ssl_comparisions.png](/static/images/ai/unbiased_teacher_ssl_comparisions.png)


- A Simple Semi-Supervised Learning Framework for Object Detection (STAC) ( [2005.04757.pdf (arxiv.org)](https://arxiv.org/pdf/2005.04757.pdf) )
	- This is created by adopting existing semi supervised classification solutions to object detection. 
	- This method does not address the pseudo label class imbalance issue. 
	- Github: https://github.com/google-research/ssl_detection
	
- Pseudo Labeling method is one of the most successful methods in SSL classification problems. 


# New terms

- pseudo-labeling : Using the high confidence predictions from test data as label data for training. 
- EMA (Exponential Moving Average) 


---
Status: #done

Tags: 
#paper 
#focal_loss
#EMA 

Source : 
- [paper](https://arxiv.org/abs/2102.09480)


