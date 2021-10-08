---
title: Deep floor plan recognition
date: 2021-10-08
tags: ['paper', 'deep_floor_plan']
draft: false
summary: 
---
# Deep Floor Plan Recognition
- Design a deep multi-task neural network to learn the spatial relations between floor plan elements to maximize network learning. 
- Introduced a spatial contextual module with the room-boundary-guided attention mechanism to learn the spatial semantic information, and formulate the cross-and within-task weighted loss to balance the losses for our tasks

- Pros 
	- Semantic information of floor plan elements is learned 
	- Detect floor plan elements --> walls of uniform & non uniform thickness + windows + doors etc 
	- Detect rectangular + non rectangular rooms eg: dinning room, bathroom, bedroom etc  
	

![/static/images/ai/dfp_arch_2.png](/static/images/ai/dfp_arch_2.png)



# Vital info


![/static/images/ai/dfp_arch_1.png](/static/images/ai/dfp_arch_1.png)


- **VGG Encoder** : A single encoder is used to extract the features. 
- **2 Decoders** : The extracted features are shared among the 2 decoders, each decoder has its own task. 

	- **Room boundary prediction decoder : **
		- Tries to learn floor plan elements like walls, doors, windows 
	
	- **Room type prediction decoder :**
		- Tries to learn pixels corresponding to room types like restroom, bedroom, hall etc 
		

![/static/images/ai/dfp_context_attention_module.png](/static/images/ai/dfp_context_attention_module.png)


- **Spatial Contextual Module : **
	- To maximize the performance of the room type predictions a module is designed to pass the room boundary features from top decoder to bottom decoder. 
	- This room boundary spatial context features bound and guide the discovery of room regions and room type. 


# Loss 

- We have 2 tasks and each task has multiple labels. 
	- Task pixel imbalance
		- Room prediction task has much more pixels than floor plan elements prediction task. 
	- Label pixel imbalance 
		-  With in task Floor plan elements --> Wall pixels are much more than window pixels 
		-  With in room type task --> Hall pixels are more than bathroom. 
	-  To handle such imbalances during training, we use "Cross-and-within-task weighted loss"

- **Cross-and-within-task weighted loss**
	- Within task weighted loss :
	
		EQ --> 1 $$ L_{task} = w_{i} * \sum_{i=1}^{C} -y_{i} * log(p_{i}) $$ 

		$$ w_{i} = ( \hat{N} - \hat{N_i} ) \div \sum_{j=1}^{C} (\hat{N} - \hat{N_j}) $$

		$$ \hat{N} = \sum_{i=1}^{C} \hat{N_i}  $$

		- $y_{i}$ : label of i th floor plan element
		- $p_{i}$ : prediction label of pixels of i th floor plan element 
		- C : number of floor plan elements 
		- $\hat{N_i}$ : Total number of ground truth pixels for ith floor plan element. 
		- $\hat{N}$ : Total ground truth pixels for all floor plan elements. 
	
	- Cross + With in task weighted : 
		- $L_{rb}$ :  within task wt loss for room boundary  ( get from EQ 1)
		- $L_{rt}$ :  within task wt loss for room type  ( get from EQ 1) 

		- Overall cross and within task weighted loss -->
		
			 $$ L = w_{rb}*L_{rb} + w_{rt}*L_{rt} $$
			 $$ w_{rb} = N_{rt} / (N_{rt} + N_{rb}) $$
			 $$ w_{rt} = N_{rb} / (N_{rt} + N_{rb}) $$


# Metrics 

- Overall accuracy :  $\sum_{i}^{} N_i / \sum_{i}^{} \hat{N_i}$
- Average accuracy :  $N_i / \hat{N_i}$

- $\hat{N_i}$ : Total ground truth pixels for i th floor plan element 
- $N_i$ : Total correctly predicted pixel for i th floor plan element


![/static/images/ai/dfp_stats.png](/static/images/ai/dfp_stats.png)


# Post Processing 

- Due to the per-pixel prediction, the output may contain certain noise.
-  Create boundary segment --> Combine wall + door + window pixels --> Fill line breaks by Morph and create boundary regions 
- Create room segment --> Using boundary segment and fill the gaps in rooms using  erosion.
- Count the number of pixels of each predicted room type in each bounded region, and set the overall predicted type as the type of the largest frequency 


# Related Work

- Raster-to-Vector: Revisiting floorplan transformation : 
	- CNN
	- Recognize junction points in floor plan and connect junctions to locate walls 
	- Cons :
		- Can only locate walls of uniform thickness and rectangular rooms 
	
- Apartment structure estimation using FCNN 
	- Uses a segmentation network to recognize different pixels of different classes.
	- Cons :
		- Ignores the spatial relations between floor plan elements and room boundary 


# Datasets used in paper 

- R2V - 815 images from Raster-to- Revisiting floor plan transformation
- R3D - 214 images from Rent3D: Floor-plan priors for monocular layout estimation


# Other Paper Datasets  

- [Wall segmentation + Object Detection + OCR --> Uses CVC-FP dataset , Real estate floor plan dataset (R-FP)](http://bjornstenger.github.io/papers/dodge_mva2017.pdf)  or [Blog](https://rit.rakuten.co.jp/news/article/projects/2017/1220_01/)
- [Improvements over Raster to Vector Implementation : CubiCasa5k](https://github.com/CubiCasa/CubiCasa5k)
	- [Download Dataset - 5000 Images ](https://zenodo.org/record/2613548)
- [All datasets paths](https://iapr-tc10.univ-lr.fr/?page_id=71)


---
Status: #done

Tags: 
#paper
#deep_floor_plan

Related: 
- [ 2021 - FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting](https://arxiv.org/pdf/2105.07147v1.pdf)
- [[2016 - 1612.02103] Richer Convolutional Features for Edge Detection (arxiv.org)](https://arxiv.org/abs/1612.02103)
- Paper --> Raster-to-Vector: Revisiting floor plan transformation
- Paper --> Apartment structure estimation using FCNN + GNN 
- Paper --> Framework for Indoor Elements Classification via Inductive Learning on Floor Plan Graphs
- [MapSegNet](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9488192)

