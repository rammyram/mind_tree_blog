---
title: Dimensionality reduction by learning an invariant mapping
date: 2021-10-08
tags: ['paper', 'siamese_architecture', 'contrastive_loss']
draft: false
summary: 
---
# Main Idea

The goal is to learn a function (G) parameterized by weights (W) that can map the high dimensional image data to low dimensional latent space, such that similar points ( consider image as a high dimensional vector point in space ) are mapped to near by points in the low dimensional latent space. 

Also the learned function G is invariant to transforms performed on the input data i.e an image of digit 4 even after transforms should be mapped to same location on the low dimensional space. 


## Goal 

Given a set input vectors x1,x2,x3....., find parametric function G(W) such that It has the following properties 

1. Simple distance measures in the output space (such as euclidean distance) should approximate the neighborhood relationships in the input space
2. The mapping should not be constrained to implementing simple distance measures in the input space and should be able to learn invariance's to complex transformations
3. It should be faithful even for samples whose neighborhood relationships are unknown.


## Contrastive Loss function 

A contrastive loss function is employed to learn the parameters W of a parameterized function G(W), in such a way that neighbors are pulled together and non-neighbors are pushed apart. Prior knowledge can be used to identify the neighbors for each training data point. 

We need to find weights (W) for function G such that the euclidean distance in the output latent space approximates the semantic similarity of the inputs in  the input space. 

> Let G(X1) be model output for image or point X1 and similarly G(X2) for input X2 
   Now the euclidean distance between the 2 images is given by 
> <center> DW( ~X1, ~X2) = ||GW( ~X1) −GW( ~X2)||2 </center>
> The above euclidean distance should be less for similar images and more for dissimilar images 

A meaningful mapping from high to low dimensional space maps similar input vectors to nearby points on the output manifold and dissimilar vectors to distant points. A new loss function whose minimization can produce such a function is now introduced. Unlike conventional learning systems where the loss function is a sum over samples, the loss function here runs over pairs of samples. Let ~X1, ~X2 ∈ I be a pair of input vectors shown to the system. 

Let Y be a binary label assigned to this pair. Y = 0 if ~X1 and X~2 are deemed similar, and Y = 1 if they are X~1, ~X2 deemed dissimilar. 


![/static/images/ai/dimensionality-reduction-by-learning-an-Invariant-mapping-contrastive-loss.png](/static/images/ai/dimensionality-reduction-by-learning-an-Invariant-mapping-contrastive-loss.png)



## Train Architecture 

The learning architecture is called a siamese architecture, it consists of two copies of the function GW which share the same set of parameters W, and a cost module. A loss module whose input is the output of this architecture is placed on top of it. 

The input to the entire system is a pair of images ( ~X1, ~X2) and a label Y. The images are passed through the functions, yielding two outputs G( ~X1) and G( ~X2). The cost module then generates the distance DW(GW( ~X1), GW( ~X2)). The loss function combines DW with label Y to produce the scalar loss (L), depending on the label Y. The parameter W is updated using stochastic gradient. The gradients can be computed by back-propagation through the loss, the cost, and the two instances of GW. The total gradient is the sum of the contributions from the two instances.

Now we know the input takes pairs of similar and dissimilar images, so we create pairs using our training data. Consider the below example case :

The training set is built from 3000 images of the handwritten digit 4 and 3000 images of the handwritten digit 9 chosen randomly from the MNIST dataset. Approximately 1000 images of each digit comprised the test set. These images were shuffled, paired, and labeled according to a simple euclidean distance measure: each sample X~i was paired with its 5 nearest neighbors, producing the set S(Xi). All other possible pairs were labeled dissimilar, producing 30,000 similar pairs and on the order of 18 million dissimilar pairs.


# Related Work

The problem of mapping a set of high dimensional points onto a low dimensional manifold has a long history. The two classical methods for the problem are Principal Component Analysis (PCA)  and Multi-Dimensional Scaling (MDS)

PCA involves the projection of inputs to a low dimensional subspace that maximizes the variance


# New terms

1. Energy based models :
		> def 
1. Siamese architecture is used in this paper : 
		>  A **Siamese** networks consists of two identical neural networks, each taking one of the two input images. The last layers of the two networks are then fed to a contrastive loss function , which calculates the similarity between the two images. ... Each image in the image pair is fed to one of these networks, (One shot learning uses siamese arch)
		

---
Tags:  
#paper 
#siamese_architecture 
#contrastive_loss 

Reference : 
	- **Good read for contrastive learning (SimCLR)** : https://amitness.com/2020/03/illustrated-simclr/
	- **Survey of self supervised learning** : https://amitness.com/2020/02/illustrated-self-supervised-learning/
	- Check Paper PDF

	



