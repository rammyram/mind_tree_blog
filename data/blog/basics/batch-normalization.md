---
title: Batch Normalization
date: 2021-10-10
tags: ['batch_normalization']
draft: false
summary: 
---
# What is Batch normalization 
- Batch normalization is the process of normalizing the activated output of hidden layers. 


# Why 
- Usually input data to a model is normalized to scale all the features to the same range. This helps to avoid certain features dominating the network, this also helps to avoid gradient descent and regularization to some extent. 
- Also the weight initialization in the model is done such that the weights are normalized. 
- When back propagation happens and weights are updated, the hidden layer inputs and their weights aren't normalized anymore. 
- There's a good chance certain feature could be dominating in the hidden layers and delays the training speed or cause vanishing gradient.
- This is why we batch normalize the hidden layers activated outputs. 


# How
- Batch normalization could have learnable parameters. 
	
	
![/static/images/ai/batch_normalization.png](/static/images/ai/batch_normalization.png)


- As you can see above, output of a hidden layer is normalized but then again it scaled by factor $g$ and added by $b$. So the input can have any mean and STD. Then whats the point of scaling if we are gonna undo the normalization by scaling and adding. 
- Normalizing a hidden unit can reduce the expressing power of the unit, to maintain the expressive power instead of feeding normalized Z, we scale and add. 
- So why even normalized in the first place ?
	- The mean of $x$ is determined by complex interaction of previous layers. However In the new input $(z*g)+b$ the mean is solely determined by b, this is much easier for gradient descent to learn.  

---
Status: #done

Tags: 
#batch_normalization

References: 
- [Deep lizard batch normalization explained](https://deeplizard.com/learn/video/dXB-KQYkzNU)


Related:

