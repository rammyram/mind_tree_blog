---
title: Data Samplers And Optimizers
date: 2021-10-10
tags: ['optimizers', 'adam', 'rmsprop', 'adagrad', 'adadelta']
draft: false
summary: 
---
# Stochastic Gradient Descent

- SGD uses single sample of data per iteration.
- Advantages 
	- Avoids getting stuck in local minima.
	- Provides immediate feedback.

- Disadvantages 
	- Computationally intensive. 
	- May not settle in global minima. 
	- Very noisy performance.
	
	
# Batch Gradient Descent

- BGD uses the entire dataset samples per iteration.
- Advantages
	- Computationally efficient.
	- Stable performance ( less noise ).
	
- Disadvantages
	- Requires lot of memory.
	- Slow learning process.
	- May get stuck in local minima.


# Mini Batch Gradient Descent

- Uses a small batch of the dataset per iteration. In this way, it reduces the variance when the parameters are updated, and which in turn makes convergence more stable. It can make full use of the matrix operations which are highly optimized in the deep learning library for more efficient gradient calculations.
- Advantages
	- Avoids getting stuck in local minima. 
	- More computationally efficient than SGD.
	- More memory efficient than BGD.
	
- Disadvantages
	-   New hyperparameter batch size, which is one of the most influential parameters in the outcome of a neural network, to worry about.


# Momentum 

[[AI/Basics/optimizers-case-study#Momentum]]


# Adagrad

- Adagrad is an algorithm that provides adoptive learning rate for parameters. 
- The same learning rate for all parameters may not be effective, so adaptive learning rate per parameter is introduced. 
- It is most suited for sparse data, i.e. where most of the data has a number of features not used very frequently. So these features require different learning rate. 

- Advantages
	- Eliminates manually tuning the learning rate.
- Disadvantages	
	- The learning rate keeps decreasing.
	- The learning rate of the late training period is very small.
	- It requires a lot of manually setting a global initial learning rate.


![/static/images/ai/Optimier_adaGrad.png](/static/images/ai/Optimier_adaGrad.png)



# Adadelta

- Adadelta is an extension of Adagrad and it tries to fix Adagrad’s aggressively reducing the learning rate.
- It is done by restricting the past accumulated gradient to some fixed size of w . Running average at time t will depend on the previous average and the current gradient.


# RMSProp

- RMSProp tries to resolve Adagrad’s radically diminishing learning rate problem by using a moving average of the squared gradient. It utilizes the magnitude of the recent gradient descents to normalize the gradient.
- [[AI/Basics/optimizers-case-study#RMSProp]]
-[[AI/Basics/optimizers-case-study]]


# Adam

-  Adaptive Moment Estimation (Adam)  computes adaptive learning rates for each parameter. It remembers and stores an exponentially decaying average of past squared gradients like Adadelta and RMSprop.
- Adam also keeps an exponentially decaying average of past gradients, similar to momentum.
- Adam is a combination of both Momentum and RMSprop, Momentum brings in smothering effect and reduces noise while RMSProp brings in Learning rate update in a proper way which is free from disadvantages of Adagrad.
- [[AI/Basics/optimizers-case-study#Adam]]


---
Tags: 
#optimizers 
#adam 
#rmsprop
#adagrad
#adadelta

References: 
 - [intro-to-optimization-momentum-rmsprop-adam](https://blog.paperspace.com/intro-to-optimization-momentum-rmsprop-adam/)

Sources: 

