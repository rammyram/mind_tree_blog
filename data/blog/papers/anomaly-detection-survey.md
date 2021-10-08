---
title: Anomaly detection survey
date: 2021-10-08
tags: ['paper', 'anomaly_detection']
draft: false
summary: 
---
## Deep Learning defect detection strategies 


![/static/images/ai/anomaly-detection-survey-solutions.png](/static/images/ai/anomaly-detection-survey-solutions.png)


- Siamese Network Classification 
	-  Unknown defect detection for printed circuit board based on multi-scale deep similarity measure method
		- Idea is to compare a PCB ground truth template with input PCB image to classify if a defect exists. 
		- The test was performed on the PCB data set with 6 types of defects including short circuit, open circuit, mouse bite, burr, leak, and copper, and the area under the ROC curve of all types was above 0.92.

		
![/static/images/ai/anomaly-detection-survey-siamese.png](/static/images/ai/anomaly-detection-survey-siamese.png)


		- [(PDF) Unknown defect detection for printed circuit board based on multi-scale deep similarity measure method (researchgate.net)](https://www.researchgate.net/publication/343257517_Unknown_defect_detection_for_printed_circuit_board_based_on_multi-scale_deep_similarity_measure_method)

	- A Siamese Network Utilizing Image Structural Differences for Cross-Category Defect Detection : Avoid retraining model when new product categories arrive. 


- Shuffle NET : Automatic Metallic Surface Defect Detection using ShuffleDefectNet


# Problems :
- Real time 

- Small sample : Usually we have small number of defect samples which could lead to over fitting. To avoid this we employ below methods
	- Augmentation
	- Unsupervised / Semi - Supervised 
	- Transfer learning 

- Small Target : When the absolute or relative size of target defect is quite small compared to entire input image. For this issue below solutions are employed. 
	- Feature fusion 
	- Augmentation
	- Multi-scale feature fusion 
	- Reduce network down sampling rate, thereby preserve small targets information
	- Using high resolution input 

- Unbalanced sample identification problem :  Defect type 1 , type 2, defect free images ...etc these categories are usually unbalanced with defect free images count dominating. This imbalance could lead to one class dominating over others and affect generalization.
	- Solutions : 
		- Data level solutions 
		
		 
![/static/images/ai/anomaly-detection-survey-problems.png](/static/images/ai/anomaly-detection-survey-problems.png)

		
		-  Model level solutions 
			-  Cost sensitive : 
				-  Reconstruct the training set: Without changing the existing algorithm, weights are assigned to each sample in the training set according to the different misclassification costs of the samples, and the original sample set is reconstructed according to the weight.

				- Introduce cost-sensitive factors: Assign higher costs to small-class samples and lower costs to large-class samples to balance the difference in the number of samples. Cost sensitive factor includes cost sensitive matrix.
	
			- Integrated learning: There are two main ways of using ensemble learning for defect detection, respectively: 
				- A: Integrated learning + data preprocessing: the typical algorithms include Smote bagging, Smote boost, Easy Ensemble and Balance cascade
				- B: Integrated learning + cost sensitive
			
			- Converted to anomaly detection problem: When the sample classes are extremely unbalanced, the defect detection problem can be regarded as an anomaly detection problem, and the anomaly detection algorithm (such as One-Class SVM, SVDD, etc.) can be used to establish a single classifier to detect the anomaly points 

# Datasets 
- Find the all available datasets for defect detection : [https://www.mdpi.com/2076-3417/11/16/7657/htm](https://www.mdpi.com/2076-3417/11/16/7657/htm)

# Solutions 
- Find list of solutions and their metrics on MVTec dataset :  [https://www.mdpi.com/2076-3417/11/16/7657/htm](https://www.mdpi.com/2076-3417/11/16/7657/htm)


---
Status: #done

Tags: #paper #anomaly_detection 

References: 
- [https://www.mdpi.com/2076-3417/11/16/7657/htm](https://www.mdpi.com/2076-3417/11/16/7657/htm)



