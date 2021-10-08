---
title: Fairmot
date: 2021-10-08
tags: ['paper', 'mot']
draft: false
summary: 
---
# Vital info


![/static/images/ai/fairmot.png](/static/images/ai/fairmot.png)


- Backbone : 
	- Deep Layer Aggregation (DLA-34)
	- Input ( 1088 x 604 ) ---> Backbone --->  ( H/4 , W/4 ) 

- Detection Branch :
	- Detection branch is built on top of CenterNet 
		- 3 Parallel heads on top of DLA 
			- Heatmap Head : Detect center of the object ( Loss ->L_heat  )
			- Box Offset : Detect offset size of box ( Loss --> L_box )
			- Center Offset 

- Re-ID Branch :
	- The re-ID feature of the object centered at (x,y) is extracted from the reID feature map.
	- reID features are learned through classification task. All object instances of same object are treated as same class. (Loss --> L_identity )

- Total train loss :
	- L_detection = L_heat + L_box
	- $$ L_{total} =  1 / 2 ( 1/e^{w1} * L_{detection} + 1/e^{w2} * L_{identity} + w1 + w2),$$
	- w1 and w2 are learnable parameters.
	
- Given an image with a few objects and their corresponding IDs, we generate ground-truth heatmaps, box offset and size maps as well as one-hot class representation of the objects. These are compared to the estimated measures to obtain losses to train the whole network.

- **Online object association **
	- Initialize number of tracklets based on estimated objects in the first frame. 
	- Then in subsequent frames link the detected objects to existing tracklets based on below :
		- Cosine distance computed on ReID features. 
		- Box overlap - Bipatriate matching. 
		- Also use Kalman filter to predict location of tracklets in current frame --> If too far from the linked detection --> then set corresponding cost to infinity --> which effectively avoid linking detections with large motions.
		- Update the appearance features of the trackers in each time step to handle appearance variations.


# Related Work

- ## Non - Deep learning 

	- ### Online methods  
		- Use current and previous frames from MOT
		- Ex : SORT, IOU-Tracker 

		- #### SORT ( Simple online and real time tracking ) algorithm
			- Uses Kalman filter to predict future object locations, compute their overlaps with with the detected objects in the future frames. 
			- Finally adopts Hungarian algorithm for tracking. 
			- One of the early solutions 
			- **Cons**
				- Does not have reID features.
				- Fail in crowded scenes or fast camera motion 

		- #### IOU-Tracker 
			- directly associates detections in neighboring frames by their spatial overlap without using Kalman filter and achieves 100K fps inference speed
			- **Cons**
				- Same as SORT 

	- ### Batch methods :
		- Use whole sequence for MOT
		- Achieved better results than the online ones due to its effective global optimization in the whole sequence


- ## Deep learning 

	- ### Treats MOT as 2 tasks 
		- Localize object of interest in input image, Using object detection models ( YOLO or FRCNN  )
		- Extract objects from image and feed to identity embedding network to extract ReID features.
		- ReID features are used to link boxes over time. 
		- Linking cost is based on below values : 
			- ReID features 
			- IOU of bbox
		- Once cost is calculated, Use Kalman filter and Hungarian algorithm to accomplish linking task. 
		- **Cons :**
			- 2 tasks are done separately without sharing parameters.
			- Not suitable for real time applications.  

	- ### One Shot ( 1 task ) 
		- Goal : Accomplish object detection and identity embedding ( reID features ) in  a single network to reduce inference times. 
		- Ex : Tack-RCNN, JDE 
		- **Cons** :
			- Fast but reduction in accuracy is significant 
			- Especially loss in re-ID tracking accuracy and mismatches happen.  

	- ### Fair MOT
		- Goal : Provide real time MOT using one shot without loss of tracking accuracy like previous one shot methods. 
		- Solution : 
			- Treat object detection and re-ID fairly 
			- Avoid anchor based object detection. 


# Metric Evaluation 

- In order to measure the accuracies of bounding boxes and identity matches at the same time, we use multiple metrics in MOT.  
	- MOTA ( Multi object tracking accuracy  )
	- FAF ( False alarm per frame )
	- MT ( Number of mostly tracked targets )
	- ML (Number of mostly lost targets )
	- IDF1  ( Identification F1 score )
	- IDS ( Identity Switches )
	- FPS ( Frames per second )

-  [Paper in which metrics are defined for Multi Camera Multi Object Tracking system](https://arxiv.org/pdf/1609.01775v2.pdf)


# New terms

### Hungarian Algorithm

- The Hungarian Algorithm is used to find the minimum cost in assignment problems that involve example --> assigning people to activities
-  [[AI/Papers/detection-transformer-detr#New terms or questions]]


### Kalman Filter 

- Kalman filtering is **an algorithm that provides estimates of some unknown variables given the measurements observed over time**


### Kanade Lucas Tomashi

- [[AI/Knowledge/Optical Flow#Sparse optical flow]]
- [Kanade–Lucas–Tomasi feature tracker](https://en.wikipedia.org/wiki/Kanade%E2%80%93Lucas%E2%80%93Tomasi_feature_tracker)


---
Status: #done

Tags: 
#paper
#mot

References: 
- [Medium blog nice overview on MOT](https://blog.netcetera.com/object-detection-and-tracking-in-2020-f10fb6ff9af3)
- [Openvino Muti camera multi object tracking ](https://github.com/openvinotoolkit/open_model_zoo/tree/master/demos/multi_camera_multi_target_tracking_demo/python)
- [Torchreid: Deep learning person re-identification in PyTorch.](https://github.com/KaiyangZhou/deep-person-reid)
- [ Simple model to Track and Re-identify individuals in different cameras/videos.(Yolov3 & Yolov4) ](https://github.com/samihormi/Multi-Camera-Person-Tracking-and-Re-Identification)
- One Short trackers 
	- [Towards Real-Time Multi-Object Tracking](https://arxiv.org/pdf/1909.12605.pdf)

