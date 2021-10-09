---
title: Unsupervised student teacher anomaly
date: 2021-10-09
tags: ['paper', 'student_teacher', 'anomaly_detection']
draft: false
summary: 
---
# Main Idea 

- The idea is that ensemble of students are trained on anomaly free images and teacher is a model trained on huge datasets like ImageNet. During inference when anomaly images are fed to students. The output of students is compared to teacher to get anomaly scores per pixel. 
- Firstly, use of discriminative feature extraction ability of models, that are  pre-trained on humongous data for anomaly detection.
- Secondly, semantic anomaly detection requires huge labeling effort. This paper proposes unsupervised  student teacher framework for anomaly detection. 

# Related Work

- Most of the research in anomaly detection went into GAN and VAE. These models detect anomalies using per pixel reconstruction error. So due to inaccurate reconstructions of GAN, the results could be inaccurate when we are dealing with tiny (millimetre) level anomalies. 
- Progress is also made in using supervised computer vision algorithms. The problem with such methods is 
	- Data labeling 
	- These models take images of reduced dimensions leading to diminished results. Where as in anomaly detection usually the images are of high resolution.  

# Teacher 


![/static/images/ai/unsupervised-student-teacher-anomaly-teacher.png](/static/images/ai/unsupervised-student-teacher-anomaly-teacher.png)


- GOAL : Provide feature descriptors for every possible square of length p with in input image i 
- Using convolution & max pooling,  each image  patch of size $R^{PxPxC}$  is embed to dimension d $R^{PxPxD}$
- Now to make these feature descriptors stronger, we use 3 losses. 

### Knowledge distillation Loss 

- Here we distill the knowledge of powerful pre-trained model to make our teacher learn how to extract local feature descriptors. 
- Instead of directly using these pre-trained models, we are distilling because these pre-trained models are too deep and complex to extract local patch descriptors. 
- Loss $L_K$ : minimize the distance between feature vectors of teacher and pre trained model. 

### Metric Learning ( Triplet Loss )

- Self supervised loss to improve teachers patch feature descriptor. 
- Loss $L_M$: 
	- Push $P$ and $P^+$ closer 
	- Push $P$ and $P^-$ far 

###  Descriptor Compactness Loss 

- The input patch images of size P has overlaps with adjacent patches. So the patch descriptors may hold redundant data. 
- To make descriptors more compact and focused on patch central pixels this loss is introduced. 
- Loss $L_C$ : The correlation matrix between all descriptors in the current mini batch. 

# Ensemble of Students 
- Ensemble of student networks $S_i$ is trained to predict the teacher's output on anomaly free data. 
- We then use students predictive uncertainty and regression error during inference to detect anomalies.


![/static/images/ai/unsupervised-student-teacher-anomaly-student.png](/static/images/ai/unsupervised-student-teacher-anomaly-student.png)


# Multi-Scale Anomaly Segmentation

- Consider our anomaly size is too small then a select patch of size P has more anomaly free region than anomaly pixels. 
- Therefore the students can produce good descriptors matching the teacher which leads to failure in detecting small anomalies. 
- SOLUTION : 
	- Control over the size of Student Teacher receptive field P. 
	- Train an ensemble of L Student teacher ensemble pairs at various scales of receptive field by changing P. 
	- Finally we can average the scores of multiple scales to get final anomaly score per pixel. 


![/static/images/ai/unsupervised-student-teacher-anomaly-loss.png](/static/images/ai/unsupervised-student-teacher-anomaly-loss.png)


![/static/images/ai/unsupervised-student-teacher-anomaly-ex.png](/static/images/ai/unsupervised-student-teacher-anomaly-ex.png)


![/static/images/ai/unsupervised-student-teacher-anomaly-ex-2.png](/static/images/ai/unsupervised-student-teacher-anomaly-ex-2.png)


# Hyper Parameters 

| Name                       | Value                                           |
| -------------------------- | ----------------------------------------------- |
| w,h                        | 256 X 256                                       |
| Anomaly free images Epochs | 100                                             |
| Batch size                 | 1                                               |
| LR                         | 10-4                                            |
| Weight Decay               | 10-5                                            |
| $\lambda_k$                | 1                                               |
| $\lambda_c$                | 1                                               |
| $\lambda_m$                 | 0                                               |
| Students (M)               | 3                                               |
| Dataset                    | MVTech (5000 HD images, 10 objects, 5 textures) |


![](/static/images/ai/unsupervised-student-teacher-anomaly-mvtech-dataset.png))


---
# Meta
Status: #done

Tags: 
#paper #student_teacher
#anomaly_detection 

References: 
- Paper : [1911.02357.pdf (arxiv.org)](https://arxiv.org/pdf/1911.02357.pdf)

