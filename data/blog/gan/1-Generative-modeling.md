---
title: 1 Generative Modeling
date: 2021-10-09
tags: ['gan', 'generative_modeling', 'discriminative_modeling', 'representational_learning']
draft: false
summary: 
---
# What is Generative Modeling 

-  A generative model describes how a dataset is generated in terms of a probabilistic model. By sampling from this model, we are able to generate new data.

- Discriminative modeling attempts to estimate the probability that an observation x belongs to category y. Generative modeling doesn’t care about labeling observations. Instead, it attempts to estimate the probability of seeing the observation at all.

- The key point is that, even if we were able to build a perfect discriminative model to identify Van Gogh paintings, it would still have no idea how to create a painting that looks like a Van Gogh
	

# Generative modeling framework 

- We have a dataset of observations X. 
- We assume that the observations have been generated according to some unknown distribution (pdata).
- A generative model pmodel tries to mimic pdata. If we achieve this goal, we can sample from pmodel to generate observations that appear to have been drawn from pdata.
- We are impressed by pmodel if:
		Rule 1: It can generate examples that appear to have been drawn from pdata. 
		Rule 2: It can generate examples that are suitably different from the observations in X. In other words, the model shouldn’t simply reproduce things it has already seen.


# Representational Learning 

The core idea behind representation learning is that instead of trying to model the high-dimensional sample space directly, we should instead describe each observation in the training set using some low-dimensional latent space and then learn a mapping function that can take a point in the latent space and map it to a point in the original domain.

 
![/static/images/gan/gan_latent_space_of_biscuit_tins.png](/static/images/gan/gan_latent_space_of_biscuit_tins.png)


 
![/static/images/gan/gan_latent_space_1.png](/static/images/gan/gan_latent_space_1.png)


## Math 
check the math background before moving forward [[AI/Math/2_probability distribution]]

--- 
Tags: 
#gan
#generative_modeling 
#discriminative_modeling 
#representational_learning 

Reference : 

Source : 

