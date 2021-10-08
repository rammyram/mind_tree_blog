---
title: Detection transformer detr
date: 2021-10-08
tags: ['paper', 'soft_nms', 'object_detectors', 'detection_transformer', 'transformer']
draft: false
summary: 
---
# Detection transformer (DETR)
- A simple end to end object detection strategy by using attention transformer combined with a feature extractor backbone like resnet.
- Unlike tradition object detector that has too many networks like classifier, regressor, RPN, FPN etc and post processing operations, this method is quite simple with a straight forward architecture.
- Could be easily extended to semantic segmentation's tasks.


# Problems solved
- #### Set Prediction ( Avoid post processing steps like NMS )
- Current object detector generate thousands of duplicate proposals and depends on post processing techniques like NMS to boost there accuracies.
- But set predictions are processing free, they handle duplicates by being able to develop relations among all predicted elements with the help of transformers attention nature.
- #### Parallel decoding
- One of the main advantages of attention-based models is their global computations and perfect memory, which makes them more suitable than RNN's on long sequences.
- All of the objects are detected at a time rather than in sequence.
- #### Reduce initialization dependencies
- Most modern object detectors predict boxes relative to initial guesses like initial proposals or prior anchors. The model performance very much depends on this initial anchor size and shapes.
- This paper removes this handcrafted initial guesses and directly predicts absolute bounding box w.r.t. input image itself.
- #### Reduced FLOPS / Computation
- Able to beat SATA models like FRCNN while having significantly less parameters.


# Limitations
- Requires more training time
- Detection of tiny / small object is not as good as FRCNN.


# Architecture

![/static/images/ai/detection_transformer_architecture_1.png](/static/images/ai/detection_transformer_architecture_1.png)



![/static/images/ai/detection_transformer_architecture_2.png](/static/images/ai/detection_transformer_architecture_2.png)



![/static/images/ai/detection_transformer_architecture_3.png](/static/images/ai/detection_transformer_architecture_3.png)


- #### Backbone
	- INPUT : Input image of shape 3 X $H_0$ X $W_0$
	- OUTPUT: Features extracted of shape C x H X W where C = 2048, H = $H_0/32$, W = $W_0/32$
	- Conventional CNN backbone to extract features from input image ex: Resnet
- #### Encoder
	- INPUT : ( C x H X W ) =>1x1 CONV => ( d X H X W ) => ( d X HW ) + Positional encoding => Fed to each attention layer in multi head attention in encoder.
	- OUTPUT : Outputs attention maps with contextual information ( d X HW )
	- To reduce the feature dimension, the output of backbone is passed through a 1x1 Conv that reduce channels from C to d.
	- Transformer accepts sequence of data so (d X H x W) is flattened to (d X HW). Remember that transformer architecture is permutation invariant so we supply it with position encoding.
- #### Decoder
	- INPUT : 1st input is N learned positional encoding's + Encoder output
	- OUTPUT : N output embedding's.
	- The decoder arch is same as vanilla transformer, only difference is all output predictions of decoder are made at a time.
	- How's value of N chosen -> This N is the final number of object predictions made by the model. So we need to make sure this value is more that the number of GT in the image.
- #### Feed Forward Network (FFN)
	- INPUT : N Output embedding's of the decoder.
	- OUTPUT : Normalized center co-ordinate's and height and width of box w.r.t the image.
	- All prediction FFN's share their weights


# Techniques
- Now let's wonder ourself with some questions !!!

- How does DETR deal with False positives problem majorly seen in traditional object detector that use NMS ?
	- Traditional detector employ the concept of generating thousands of prior anchors which create thousands of FP. But DETR strategy itself is different, it tries to directly predict N objects which is thousands of factors less than anchors proposed.

- What if model pays too much attention to one object that is very clear and make multiple detection's of the same object ?
	- Bipatriate matching helps to avoid this by making sure every prediction has a unique match in target.

- N predictions are matched with N targets ( ground truths + no objects ). How to make sure order of obj detection not effect the loss & matching is done properly ?
	- The loss function should be invariant by a permutation of the predictions. The usual solution is to design a loss based on the Hungarian algorithm, to find a bipartite matching between ground-truth and prediction. This enforces permutation-invariance, and guarantees that each target element has a unique match


# Losses

- Hungarian algorithm -> Find the best combination between N predictions and N GT's. The best combination is selected based on loss.
- Lets select a combination and calculate its loss.
- Hungarian matching loss for a combination = Bounding box loss + Class loss
- Bounding box loss =>
	- $\lambda_{iou} \; * L_{iou}(b_{pred}, b_{gt}) \;+\; \lambda_{L1} \;* L1(b_{pred}, b_{gt})$
	- The above bounding box is a combination of IOU loss that handles scale loss & L1 loss that handles position loss.
- Class loss =>
	- $-log( c_{pred} \;*\; c_{gt})$
	- This is simply a log loss
- So finally we need to pick the combination that gives minimum loss.

Note : For simplicity some details are omitted, for detailed info check the paper.


# Stats


![/static/images/ai/detection_transformer_stats.png](/static/images/ai/detection_transformer_stats.png)



# Training Hyper-parameters

- Backbone
	- Imagenet pretrained backbone --> ResNet-50
	- Backbone batch normalization weights and statistics are frozen during training.
	- Finetune backbone using LR --> $10^{-5}$
	- Having the backbone learning rate roughly an order of magnitude smaller than the rest of the network is important to stabilize training, especially in the first few epochs.
- Transformer
	- LR --> $10^{-4}$
	- Dropout --> 0.1 is applied after every multi head attention & FFN before layer normalization.
	- Weight initialization --> Xavier
	- Losses -->Linear combination of L1 and GIoU losses for bounding box regression with $λ_{L1}$ = 5 and $λ_{iou}$ = 2.
	- All models were trained with N = 100 decoder query slots.


# Terms / QA
- Bipatriate Matching
- Hungarian Algorithm
- Difference between NMS and Soft NMS, how does soft NMS improve small object detection ?
- Hungarian algorithm : Used in solving assignment problems and matching problems
- Set prediction : Predicting set of objects in an image is an example of set prediction. The main difficulty with set prediction comes from the ability to permute the elements in set freely, Which means there are n! equally good solutions for a set of size n. ( Which means we need a permutation-invariance loss function ex: Bipatriate matching )
- Auxiliary loss : 
	- In deep networks we often see vanishing gradient problem, to handle this problem loss from some early individual modules is included as a weighted loss  in the final loss, thereby encouraging there learning and gradient flow. 
	- [what-is-auxiliary-loss-as-mentioned-in-pspnet-paper](https://stats.stackexchange.com/questions/304699/what-is-auxiliary-loss-as-mentioned-in-pspnet-paper)


---
Status:
#done

Tags:
#paper
#soft_nms
#object_detectors
#detection_transformer
#transformer

References:
- [\[2005.12872\] End-to-End Object Detection with Transformers (arxiv.org)](https://arxiv.org/abs/2005.12872)
- [Comparison of Faster-RCNN and Detection Transformer (DETR) | by Subrata Goswami | Medium](https://whatdhack.medium.com/comparison-of-faster-rcnn-and-detection-transformer-detr-f67c2f5a2a04)
- [DETR: End-to-End Object Detection with Transformers (Paper Explained) - YouTube](https://www.youtube.com/watch?v=T35ba_VXkMY)

Related:
- [[AI/Knowledge/Transformer]]
- [[AI/Knowledge/Transformers Implementation]]






