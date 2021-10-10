---
title: Metrics
date: 2021-10-10
tags: ['metrics', 'precision', 'recall', 'map', 'average_precision']
draft: false
summary: 
---
## Object Detection 

Measuring the performance of object detectors involves determining if a detection is valid or not. 

- **True Positive** : A valid detection 
- **False Positive** : An Invalid Detection 
- **False Negative**: Ground truth missed by the model 
- **True Negative** : This metric is ignored in object detectors as there are way too many instances of true negatives. 

For determining the validity of a detection we use Intersection Over Union (IOU) also called as **Jaccard Index**

- **IOU**  
	- IOU evaluates the overlap of ground truth (gt) and predicted mask (pd). It is the area of intersection between gt and pd divided by area of union. 

	- 
![/static/images/ai/Metric_iou.png](/static/images/ai/Metric_iou.png)

	
	- IOU ranges from 0 to 1, 1 being perfect overlap between gt and pd and 0 being no overlap at all. 	
	- We define a threshold for IOU called **$\alpha$ ** that is used to identify if a detection is valid or not. 
		- IOU >= $\alpha$ --> True Positive 	
		- IOU < $\alpha$   --> False Positive 
		- IOU = 0                 --> False Negative (gt missed by model)
		
		- 
![/static/images/ai/Metric_iou_thresolding.png](/static/images/ai/Metric_iou_thresolding.png)
		
		- Observe the figure above when $\alpha$ = 0.5 
	
	
- **Precision**
	- Precision means ability to identify most of the relevant objects only.
	- Total positive detection's made by model : TP + FP
	- Precision --> $\dfrac{TP}{TP+FP}$ 
	
	
- **Sensitivity / True Positive Rate / Recall**
	- Ability to identify most ground truth objects.
	- Total ground truths available : TP + FN 
	- Recall --> $\dfrac{TP}{TP+FN}$ 


- **False Negative Rate**
	- FNR tells us what proportion of positive labels got mis-classified as Negative. 
	- FNR --> $\dfrac{FN}{TP+FN}$
	- A higher TPR and a lower FNR is desirable since we want to correctly classify the positive class.


- **Specificity / True Negative Rate**
	- Specificity tells us what proportion of Negatives are detected correctly. 
	- Specificity --> $\dfrac{TN}{TN+FP}$


- **False Positive Rate**
	- Tells us what proportion of negative classes got mis-classified as positives. 
	- FPR = 1 - Specificity = $\dfrac{FP}{FP+TN}$
	- A higher TNR and a lower FPR is desirable since we want to correctly classify the negative class.


- **Precision Recall Curve (PR Curve)**
	- The PR curve is a plot of Precision & Recall functions for varying confidence values of model prediction. 
	- If FP is low then we have high precision but the model may missing many instances, Increasing FN thereby increasing Recall.
	- Conversely if we lower the threshold, then the recall increase as most of detection are flagged as positives but this could also increase FP thereby lowering Precision. 
	- **For a good model the Precision and Recall should remain high even if the confidence threshold varies **


- **Average Precision @ $\alpha$**
	- AP@α is ideally the area under the PR curve (AUC-PR)
	> AP@α = $\int_{0}^{1} P(r) dr$ 
	-  AP@α  means Average Precision at IOU threshold α. 
	-  Normally PR is a zigzag curve, we remove this behavior and convert the curve to monotonically decreasing using the Interpolation methods.   
	-  
![/static/images/ai/Metric_all_point_interpolation.png](/static/images/ai/Metric_all_point_interpolation.png)


	- In the above figure you can observe the real AUC is orange curve which is in zigzap pattern, this is converted to monotonically decreasing curve using all point interpolation method. Where precision value at a recall is replaced by max precision after that recall point. 	
	
	> $$AP = \sum( r_{n+1} - r_n ) * P_interp( r_{n+1} )$$
	> $$P_{interp}( r_{n+1} ) = max_{r>= r_{n+1}} p(r)$$

- The above equation is simply a sum of rectangle at certain recall intervals. 
	
	
- **MAP**
	- AP is calculated at an IOU threshold for each class. 
	- Average of AP over all classes gives us Mean AP.
	
	 >  $$MAP@\alpha$$ = $$\dfrac{1}{n} * \sum_{i=1}^{n} AP_i$$
	 >  for n classes 
	 
	 
- **MAP [0.5 : 0.5 : 0.95]**
	-  This can defined as calculation of AP of a given category at 10 different IOU's ranging from 0.5 to 0.95 at a step size of 0.5 


-  **AUC-ROC Curve**:
	-  The **Receiver Operator Characteristic (ROC)** curve is an evaluation metric for binary classification problems. 
	-  It is a probability curve that plots the **TPR** against **FPR** at various threshold values 
	-  The **Area Under the Curve (AUC)** is the measure of the ability of a classifier to distinguish between classes and is used as a summary of the ROC curve
	-  Full Read : https://www.analyticsvidhya.com/blog/2020/06/auc-roc-curve-machine-learning/
	
	
-  **Notes**
	-   Multiple detection's of same object in an image are considered as False Positives 
	-   Some detectors can output multiple detection's for a ground truth that are above IOU threshold level, in such situation we pick detection with highest confidence as the TP and others as FP. 


# To Read 

- Negative Predictive Value (NPV)
- Receiver Operating Characteristics (ROC)


# Implementations :

- [Faster RCNN Training along with metrics calculation code (Precision, Recall, F1, MAP@Threshold)](https://colab.research.google.com/drive/1-2-Qm7idYsZnhPVZOa97vVQsljtL3auK?usp=sharing)


---
Tags: 
#metrics
#precision
#recall
#map 
#average_precision

References: 

- [Precision, Recall, AUC-PR]( https://towardsdatascience.com/on-object-detection-metrics-with-worked-example-216f173ed31e)
- [Precision, Recall, F1]( https://towardsdatascience.com/the-5-classification-evaluation-metrics-you-must-know-aa97784ff226)
- [Good read on ROC & Implementation](https://www.analyticsvidhya.com/blog/2020/06/auc-roc-curve-machine-learning/)

